#!/usr/bin/env python3
"""Independent old-DESI simultaneous latent geometry probability audit.
No imports from forecast/producer. CSV likelihood, distance ODE, analytic A,
adaptive Omega integration. Frozen intervals alone are the audit targets.
"""
import json,csv,math,time,hashlib,itertools,sys
from pathlib import Path
from functools import lru_cache
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.optimize import brentq
from scipy.special import ndtr
from numpy.polynomial.chebyshev import chebfit,chebval,chebpts1
BASE=Path(__file__).resolve().parent.parent
OUT=Path(__file__).resolve().parent
frozen=json.load(open(BASE/'inputs/frozen_results.json'))
rr=list(csv.DictReader(open(BASE/'inputs/desi_dr2_table4.csv')))
zobs=np.array([float(r['z']) for r in rr])
zforecast=np.array(frozen['forecast_z_grid'])
zall=np.unique(np.r_[zobs,zforecast])
Y=[];C=np.zeros((13,13));p=0
for row in rr:
 if not row['DM']:
  Y.append(float(row['DV']));C[p,p]=float(row['DV_error'])**2;p+=1
 else:
  Y.extend([float(row['DM']),float(row['DH'])]);sm,sh,r=map(float,[row['DM_error'],row['DH_error'],row['rho_MH']])
  C[p:p+2,p:p+2]=[[sm*sm,r*sm*sh],[r*sm*sh,sh*sh]];p+=2
Y=np.array(Y);CI=np.linalg.inv(C)
io=np.searchsorted(zall,zobs);iz=np.searchsorted(zall,zforecast)
DEG=int(sys.argv[1]) if len(sys.argv)>1 else 80
# Independent ODE solution, interpolated spectrally only in Omega for speed.
# Refinement independently checks degree 80 versus 128 and ODE tolerances.
RTOL=2e-13 if DEG==80 else 5e-14
ATOL=2e-14 if DEG==80 else 5e-15
def ode(om):
 sol=solve_ivp(lambda z,y:np.array([1/math.sqrt(1+om*((1+z)**3-1))]),(0,float(max(zall))),[0.],method='DOP853',t_eval=zall,rtol=RTOL,atol=ATOL)
 assert sol.success
 return sol.y[0]
x=chebpts1(DEG+1);ox=.325+.275*x
cs=chebfit(x,np.array([ode(float(o)) for o in ox]),DEG)
validation_x=np.linspace(.05,.6,171)
err=max(float(np.max(np.abs(chebval((o-.325)/.275,cs)-ode(float(o))))) for o in validation_x)
assert err<2e-11,err
@lru_cache(maxsize=65536)
def geo(om):
 dm=chebval((om-.325)/.275,cs)
 dh=1/np.sqrt(1+om*((1+zall)**3-1))
 return dm,dh
@lru_cache(maxsize=65536)
def terms(om):
 dm,dh=geo(om);f=[]
 for i,row in enumerate(rr):
  j=io[i]
  f.extend([float((zobs[i]*dm[j]**2*dh[j])**(1/3))] if not row['DM'] else [dm[j],dh[j]])
 f=np.array(f);u=float(f@CI@f);mu=float(f@CI@Y/u);sig=1/math.sqrt(u)
 r=Y-mu*f;chisq=float(r@CI@r)
 return f,mu,sig,chisq

def cmass(a,b):
 if b<=a:return 0.
 return float(ndtr(-a)-ndtr(-b)) if a>0 else float(ndtr(b)-ndtr(a))

class Audit:
 def __init__(self,prior,model):
  self.prior=prior;self.model=model;self.config=frozen['priors'][prior];self.olo,self.ohi=self.config['om_bounds'];self.alo,self.ahi=self.config['A_bounds'];self.fixed=frozen['model_fixed_A'][model]
  self.shift=self.logdensity(.3)
  self.norm,self.normerr=quad(self.density,self.olo,self.ohi,epsabs=1e-12,epsrel=2e-12,limit=500,points=[.25,.3,.35])
 def logdensity(self,o):
  f,mu,sig,chi=terms(float(o))
  if self.fixed is None:
   val=-.5*chi+math.log(sig)+math.log(cmass((self.alo-mu)/sig,(self.ahi-mu)/sig))
  else:
   r=Y-self.fixed*f;val=-.5*float(r@CI@r)
  if self.config['om_density']=='scaled_beta22':
   t=(o-self.olo)/(self.ohi-self.olo)
   if t<=0 or t>=1:return -math.inf
   val+=math.log(t*(1-t))
  return val
 def density(self,o):return math.exp(self.logdensity(float(o))-self.shift)
 def shapes(self,o,inds):
  dm,dh=geo(float(o));return np.r_[dm[iz[inds]],dh[iz[inds]]]
 def ap(self,o,index):
  dm,dh=geo(float(o));i=iz[index];return float(dm[i]/dh[i])
 def root(self,fun,target,increasing=True):
  sign=1 if increasing else -1
  l,h=self.olo,self.ohi
  fl=sign*(fun(l)-target);fh=sign*(fun(h)-target)
  if fl>=0:return l
  if fh<=0:return h
  return float(brentq(lambda o:fun(o)-target,l,h,xtol=5e-15,rtol=1e-14))
 def coverage(self,k,inds,details=False):
  rows=frozen['results'][self.prior][self.model]['forecast']['rows']
  rr0=[rows[i] for i in np.r_[inds,11+inds,22+inds]]
  quant=np.array([r['quantiles'] for r in rr0]);med=quant[:,2]
  lower=med+k*(quant[:,0]-med);upper=med+k*(quant[:,4]-med)
  n=len(inds);ol,oh=self.olo,self.ohi
  for j,i in enumerate(inds):
   ol=max(ol,self.root(lambda o:self.ap(o,i),lower[2*n+j]))
   oh=min(oh,self.root(lambda o:self.ap(o,i),upper[2*n+j]))
  if self.fixed is not None:
   for j,i in enumerate(inds):
    for obs in [0,1]:
     fun=lambda o:float(self.fixed*geo(float(o))[obs][iz[i]])
     ol=max(ol,self.root(fun,upper[obs*n+j],False))
     oh=min(oh,self.root(fun,lower[obs*n+j],False))
   value,error=quad(self.density,ol,oh,epsabs=1e-12,epsrel=2e-12,limit=500)
   ans={'mass':value/self.norm,'omega_interval':[ol,oh],'quadrature_error':error/self.norm,'breakpoints':0}
   return ans if details else ans['mass']
  def bounds(o):
   s=self.shapes(o,inds)
   return np.r_[lower[:2*n]/s,self.alo],np.r_[upper[:2*n]/s,self.ahi]
  # Detect all pairwise boundary crossings, not merely the active envelope.
  grid=np.linspace(ol,oh,129 if DEG==80 else 257)
  bs=np.array([bounds(float(o)) for o in grid])
  bp=[ol,oh]
  for side in [0,1]:
   for i,j in itertools.combinations(range(2*n+1),2):
    ds=bs[:,side,i]-bs[:,side,j]
    for q in np.flatnonzero(ds[:-1]*ds[1:]<0):
     root=brentq(lambda o:bounds(float(o))[side][i]-bounds(float(o))[side][j],grid[q],grid[q+1],xtol=5e-15,rtol=1e-14)
     bp.append(root)
  def feasible(o):
   l,u=bounds(o);return float(min(u)-max(l))
  ds=np.min(bs[:,1,:],axis=1)-np.max(bs[:,0,:],axis=1)
  for q in np.flatnonzero(ds[:-1]*ds[1:]<0):bp.append(brentq(feasible,grid[q],grid[q+1],xtol=5e-15,rtol=1e-14))
  bp=np.unique(np.array(bp));bp=bp[np.r_[True,np.diff(bp)>1e-13]]
  def integrand(o):
   l,u=bounds(o);lo,hi=float(max(l)),float(min(u))
   if hi<=lo:return 0.
   _,mu,sig,_=terms(float(o))
   return self.density(o)*cmass((lo-mu)/sig,(hi-mu)/sig)/cmass((self.alo-mu)/sig,(self.ahi-mu)/sig)
  value=0.;error=0.
  for lo,hi in zip(bp[:-1],bp[1:]):
   v,e=quad(integrand,lo,hi,epsabs=1e-13,epsrel=2e-12,limit=200);value+=v;error+=e
  ans={'mass':value/self.norm,'omega_interval':[ol,oh],'quadrature_error':error/self.norm,'breakpoints':len(bp)-2}
  return ans if details else ans['mass']

def main():
 results=[];start=time.time()
 for prior in frozen['priors']:
  for model in frozen['model_fixed_A']:
   a=Audit(prior,model)
   for grid,inds in [('primary15',np.where(np.isin(zforecast,[.9,1.,1.2,1.5,1.8]))[0]),('all33',np.arange(11))]:
    mass=a.coverage(1.,inds,True)
    k=brentq(lambda k:a.coverage(k,inds)-.95,.99999,1.5,xtol=3e-12,rtol=1e-13)
    joint=a.coverage(k,inds,True)
    res={'prior':prior,'model':model,'grid':grid,'stored95_joint':mass,'common_factor_95':k,'expanded_joint':joint,'normalization_error_relative':a.normerr/a.norm}
    results.append(res);print(json.dumps(res),flush=True)
 payload={'method':'Independent CSV block likelihood; DOP853 distance ODE; Chebyshev interpolation only for speed, checked independently; analytic truncated-normal A mass; adaptive Omega quadrature split at boundary crossings; no producer imports','degree':DEG,'ode_rtol':RTOL,'ode_atol':ATOL,'distance_interpolation_validation_max_abs':err,'results':results,'elapsed_seconds':time.time()-start,'inputs':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (BASE/'inputs').iterdir() if p.is_file()}}
 output=OUT/f'audit_results_degree{DEG}.json'
 with output.open('x') as out:json.dump(payload,out,indent=2)
 print('SAVED',str(output),'ELAPSED',time.time()-start,flush=True)
if __name__=='__main__':main()
