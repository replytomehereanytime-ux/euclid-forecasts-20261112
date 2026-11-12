#!/usr/bin/env python3
"""Joint latent posterior coverage. No new data and no producer scientific imports."""
from pathlib import Path
from functools import lru_cache
import argparse,csv,datetime,hashlib,json,math,time,warnings
import numpy as np
from scipy.special import roots_legendre,log_ndtr
from scipy.linalg import solve_triangular
from scipy.integrate import quad,IntegrationWarning
from scipy.optimize import brentq,minimize_scalar

ROOT=Path(__file__).resolve().parent
SOURCE=json.loads((ROOT/'inputs/frozen_results.json').read_text())
PRIMARY=[.9,1.,1.2,1.5,1.8]

def save(path,obj):path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def logcdfmass(a,b):
    if not a<b:return -math.inf
    if a>0:lo,hi=float(log_ndtr(-b)),float(log_ndtr(-a))
    else:lo,hi=float(log_ndtr(a)),float(log_ndtr(b))
    return hi+math.log(-math.expm1(lo-hi))

def read_data():
    records=list(csv.DictReader((ROOT/'inputs/desi_dr2_table4.csv').open()))
    y=[];blocks=[]
    for r in records:
        if r['DM']:
            a,b,c=float(r['DM_error']),float(r['DH_error']),float(r['rho_MH'])
            blocks.append(np.array([[a*a,c*a*b],[c*a*b,b*b]]));y.extend([float(r['DM']),float(r['DH'])])
        else:blocks.append(np.array([[float(r['DV_error'])**2]]));y.append(float(r['DV']))
    cov=np.zeros((len(y),len(y)));o=0
    for b in blocks:cov[o:o+len(b),o:o+len(b)]=b;o+=len(b)
    assert np.array_equal(cov,np.array(SOURCE['stipulated_covariance']))
    assert np.array_equal(np.array(y),np.array(SOURCE['observations']))
    return records,np.array(y),cov

class Law:
    def __init__(self,model,prior,nint,tol,nscan):
        self.model,self.prior_name=model,prior
        self.fixed=SOURCE['model_fixed_A'][model]
        self.prior=SOURCE['priors'][prior]
        self.olo,self.ohi=self.prior['om_bounds'];self.alo,self.ahi=self.prior['A_bounds']
        self.tol,self.nscan=tol,nscan
        rr,y,cov=read_data();self.records=rr
        self.zdata=np.array([float(r['z']) for r in rr])
        self.zgrid=np.array(SOURCE['forecast_z_grid'])
        self.z=np.unique(np.concatenate([self.zdata,self.zgrid]))
        self.data_indices=[int(np.where(self.z==z)[0][0]) for z in self.zdata]
        self.grid_indices=[int(np.where(self.z==z)[0][0]) for z in self.zgrid]
        g,w=roots_legendre(nint)
        self.t=self.z[:,None]*(g+1)/2
        self.dw=self.z[:,None]*w/2
        self.gt=(1+self.t)**3-1;self.gz=(1+self.z)**3-1
        L=np.linalg.cholesky(cov);self.white=solve_triangular(L,np.eye(len(y)),lower=True)
        self.yw=self.white@y
        self.peak_om=float(minimize_scalar(lambda om:-self.logdensity(om),bounds=(self.olo+1e-10,self.ohi-1e-10),method='bounded',options={'xatol':1e-12}).x)
        self.peak=self.logdensity(self.peak_om)
        self.norm,self.norm_error=quad(self.scaled,self.olo,self.ohi,epsabs=1e-13,epsrel=min(1e-11,tol/20),points=[self.peak_om],limit=300)
        assert self.norm>0
    @lru_cache(maxsize=100000)
    def geometry(self,om):
        dh=1/np.sqrt(1+om*self.gz)
        dm=np.sum(self.dw/np.sqrt(1+om*self.gt),axis=1)
        shape=[]
        for r,i,z in zip(self.records,self.data_indices,self.zdata):
            shape.extend([dm[i],dh[i]] if r['DM'] else [np.cbrt(z*dm[i]*dm[i]*dh[i])])
        fw=self.white@np.array(shape)
        u=float(fw@fw);mu=float(fw@self.yw)/u;sig=1/math.sqrt(u)
        res=self.yw-(mu if self.fixed is None else self.fixed)*fw
        chisq=float(res@res)
        logtr=logcdfmass((self.alo-mu)/sig,(self.ahi-mu)/sig)
        ll=-chisq/2
        if self.fixed is None:ll+=math.log(math.sqrt(2*math.pi)*sig)+logtr-math.log(self.ahi-self.alo)
        ids=self.grid_indices
        return dm[ids],dh[ids],dm[ids]/dh[ids],mu,sig,logtr,ll
    def logdensity(self,om):
        if not self.olo<om<self.ohi:return -math.inf
        logprior=-math.log(self.ohi-self.olo)
        if self.prior['om_density']=='scaled_beta22':
            t=(om-self.olo)/(self.ohi-self.olo);logprior+=math.log(6*t*(1-t))
        return self.geometry(float(om))[-1]+logprior
    def scaled(self,om):return math.exp(self.logdensity(om)-self.peak)
    def integral(self,lo,hi,func=None,points=()):
        if lo>=hi:return 0.,0.
        pp=sorted({float(x) for x in points if lo<x<hi})
        v,e=quad(self.scaled if func is None else func,lo,hi,epsabs=self.tol*self.norm/8,epsrel=self.tol/8,points=pp,limit=500)
        return v/self.norm,e/self.norm
    def preimage(self,fun,lower,upper,increasing):
        lo,hi=self.olo,self.ohi
        a,b=fun(lo),fun(hi)
        if not increasing:
            lower,upper=-upper,-lower
            fun0=fun;fun=lambda om:-fun0(om);a,b=-a,-b
        assert a<b
        if upper<a or lower>b:return None
        l=lo if lower<=a else brentq(lambda om:fun(om)-lower,lo,hi,xtol=2e-14)
        h=hi if upper>=b else brentq(lambda om:fun(om)-upper,lo,hi,xtol=2e-14)
        return l,h
    def calculate(self,grid,t):
        selected=[i for i,z in enumerate(self.zgrid) if any(abs(z-q)<1e-12 for q in grid)]
        rows=SOURCE['results'][self.prior_name][self.model]['forecast']['rows']
        lower=[];upper=[]
        for obs in range(3):
            for j in selected:
                q=rows[obs*len(self.zgrid)+j]['quantiles'];m=q[2]
                lower.append(m+t*(q[0]-m));upper.append(m+t*(q[4]-m))
        lower=np.array(lower).reshape(3,-1);upper=np.array(upper).reshape(3,-1)
        ol,oh=self.olo,self.ohi
        for obs in range(3):
            if self.fixed is None and obs<2:continue
            for k,j in enumerate(selected):
                factor=1. if obs==2 else self.fixed
                interval=self.preimage(lambda om:self.geometry(float(om))[obs][j]*factor,lower[obs,k],upper[obs,k],obs==2)
                if interval is None:return {'probability':0.,'quad_error_estimate':0.,'Omega_interval':None,'switch_points':[]}
                ol=max(ol,interval[0]);oh=min(oh,interval[1])
        if ol>=oh:return {'probability':0.,'quad_error_estimate':0.,'Omega_interval':None,'switch_points':[]}
        if self.fixed is not None:
            mass,err=self.integral(ol,oh,points=[self.peak_om])
            return {'probability':mass,'quad_error_estimate':err,'Omega_interval':[ol,oh],'switch_points':[]}
        @lru_cache(maxsize=100000)
        def limits(om):
            dm,dh,*_=self.geometry(float(om));scales=np.concatenate([dm[selected],dh[selected]])
            lows=np.concatenate([[self.alo],lower[:2].ravel()/scales])
            highs=np.concatenate([[self.ahi],upper[:2].ravel()/scales])
            return lows,highs
        def feasible(om):
            lows,highs=limits(om);return float(highs.min()-lows.max())
        scan=np.linspace(ol,oh,self.nscan);pts=[]
        lim=[limits(float(x)) for x in scan]
        active=[(int(l.argmax()),int(h.argmin())) for l,h in lim]
        for i,(a,b) in enumerate(zip(scan[:-1],scan[1:])):
            for side in (0,1):
                u,v=active[i][side],active[i+1][side]
                if u!=v:
                    fn=lambda om:float(limits(float(om))[side][u]-limits(float(om))[side][v])
                    if fn(float(a))*fn(float(b))<=0:pts.append(brentq(fn,float(a),float(b),xtol=2e-14))
            fa,fb=feasible(float(a)),feasible(float(b))
            if fa*fb<0:pts.append(brentq(feasible,float(a),float(b),xtol=2e-14))
        def event(om):
            lows,highs=limits(float(om));lo,hi=float(lows.max()),float(highs.min())
            if hi<=lo:return 0.
            _,_,_,mu,sig,logtr,_=self.geometry(float(om))
            return self.scaled(om)*math.exp(logcdfmass((lo-mu)/sig,(hi-mu)/sig)-logtr)
        pts=sorted(set(pts))
        mass,err=self.integral(ol,oh,event,pts+[self.peak_om])
        return {'probability':mass,'quad_error_estimate':err,'Omega_interval':[ol,oh],'switch_points':pts}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--resolution',choices=['lower','higher'],required=True);args=ap.parse_args()
    res={'lower':(96,2e-8,129),'higher':(192,2e-10,257)}[args.resolution]
    out=ROOT/('RESULT_'+args.resolution+'.json')
    if out.exists():raise RuntimeError('Refuse to overwrite a result')
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();cases=[]
    for prior in SOURCE['priors']:
      for model in SOURCE['model_fixed_A']:
        law=Law(model,prior,*res)
        for name,grid in [('primary',PRIMARY),('all_frozen',SOURCE['forecast_z_grid'])]:
            pointwise=law.calculate(grid,1.)
            root=brentq(lambda t:law.calculate(grid,t)['probability']-.95,.01,4.,xtol=2e-11)
            expanded=law.calculate(grid,root)
            bands=[]
            for row in SOURCE['results'][prior][model]['forecast']['rows']:
                if any(abs(row['z']-z)<1e-12 for z in grid):
                    q=row['quantiles'];med=q[2]
                    bands.append({'observable':row['observable'],'z':row['z'],'median':med,'original_lower':q[0],'original_upper':q[4],'joint_lower':med+root*(q[0]-med),'joint_upper':med+root*(q[4]-med)})
            case={'prior':prior,'model':model,'grid':name,'coordinates':len(bands),'pointwise_band_joint_probability':pointwise,'simultaneous_multiplier':root,'expanded_band_joint_probability':expanded,'bands':bands}
            cases.append(case)
            print(prior,model,name,pointwise['probability'],root,expanded['probability'],flush=True)
    obj={'created_utc':started,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'resolution':args.resolution,'distance_order':res[0],'coverage_tolerance':res[1],'switch_scan_points':res[2],'cases':cases,'source_results_sha256':digest(ROOT/'inputs/frozen_results.json'),'source_csv_sha256':digest(ROOT/'inputs/desi_dr2_table4.csv'),'plan_sha256':digest(ROOT/'PLAN.json'),'code_sha256':digest(Path(__file__)),'scientific_scope':'Posterior mass of latent geometry bands under the unchanged compressed old-DESI model. Not measurement/frequentist/Euclid coverage.','status':'COMPUTED_AWAITING_COMPARISON'}
    save(out,obj)

if __name__=='__main__':
    warnings.simplefilter('error',IntegrationWarning)
    main()
