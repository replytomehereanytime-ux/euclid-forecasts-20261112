#!/usr/bin/env python3
"""Conditional latent geometry and retrospective posterior-predictive log scores.
No network; no model odds, significance, evidence output, or Euclid likelihood.
Analytic uniform-A integration + deterministic one-dimensional quadrature.
"""
from pathlib import Path
import argparse,csv,hashlib,json,math,platform,datetime,sys,time
from functools import lru_cache
import numpy as np
import scipy
from scipy.special import log_ndtr,logsumexp,ndtr
from scipy.optimize import brentq
from scipy.stats import truncnorm

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'inputs'
ZGRID=np.array([.295,.510,.706,.900,.934,1.,1.2,1.321,1.5,1.8,2.33])
MODELS={'free_A':None,'phi7_fixed_A':((1+math.sqrt(5))/2)**7,'29_fixed_A':29.,'843over29_fixed_A':843/29}
PRIORS={
 'primary':{'om_bounds':[.1,.5],'A_bounds':[20.,40.],'om_density':'uniform'},
 'broad_support':{'om_bounds':[.05,.6],'A_bounds':[15.,45.],'om_density':'uniform'},
 'beta22_shape':{'om_bounds':[.1,.5],'A_bounds':[20.,40.],'om_density':'scaled_beta22'}}
QLEVELS=[.025,.16,.5,.84,.975]

@lru_cache(maxsize=12)
def leggauss(n):return np.polynomial.legendre.leggauss(n)

def stamp():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def dump(path,obj):path.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
def hashf(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def read_inputs():
 with (SRC/'desi_dr2_table4.csv').open() as f: rr=list(csv.DictReader(f))
 rows=[];ys=[];cs=[];indices=[];labels=[];offset=0
 for rr0 in rr:
  r={k:(v if k=='tracer' else (float(v) if v else None)) for k,v in rr0.items()};rows.append(r)
  if r['DM'] is None:
   vals=[r['DV']];cov=np.array([[r['DV_error']**2]]);obs=['DV_over_rd']
  else:
   vals=[r['DM'],r['DH']];a,b,ro=r['DM_error'],r['DH_error'],r['rho_MH'];cov=np.array([[a*a,ro*a*b],[ro*a*b,b*b]]);obs=['DM_over_rd','DH_over_rd']
  ix=list(range(offset,offset+len(vals)));indices.append(ix);offset+=len(vals)
  ys.extend(vals);cs.append(cov);labels.extend([{'tracer':r['tracer'],'z':r['z'],'observable':o} for o in obs])
 C=np.zeros((offset,offset))
 for ix,cov in zip(indices,cs):C[np.ix_(ix,ix)]=cov
 y=np.array(ys)
 assert y.shape==(13,) and np.linalg.eigvalsh(C).min()>0
 return rows,y,C,indices,labels
ROWS,Y,C,BLOCKS,LABELS=read_inputs()

def distances(om,z,nint=96):
 om=np.atleast_1d(om);z=np.atleast_1d(z)
 g,w=leggauss(nint)
 zz=z[:,None]*(g+1)/2
 dm=np.sum((z[:,None]*w/2)[None,:,:]/np.sqrt(1+om[:,None,None]*((1+zz[None,:,:])**3-1)),axis=-1)
 dh=1/np.sqrt(1+om[:,None]*((1+z[None,:])**3-1))
 return dm,dh

def model_shapes(om,nint=96):
 zz=np.array([r['z'] for r in ROWS]);dm,dh=distances(om,zz,nint)
 dv=np.cbrt(zz[None,:]*dm*dm*dh)
 return np.stack([val for i,r in enumerate(ROWS) for val in ([dv[:,i]] if r['DM'] is None else [dm[:,i],dh[:,i]])],axis=1)

def logmass(a,b):
 # Stable log(Phi(b)-Phi(a)); use survival form when both endpoints positive.
 lhi=np.where(a>0,log_ndtr(-a),log_ndtr(b));llo=np.where(a>0,log_ndtr(-b),log_ndtr(a))
 return lhi+np.log(-np.expm1(llo-lhi))

def om_prior_density(om,prior):
 lo,hi=prior['om_bounds'];t=(om-lo)/(hi-lo)
 return np.ones_like(om)/(hi-lo) if prior['om_density']=='uniform' else 6*t*(1-t)/(hi-lo)

class Posterior:
 def __init__(self,model,prior_name='primary',omit=None,nodes=1024,nint=96):
  self.model=model;self.prior_name=prior_name;self.prior=PRIORS[prior_name];self.fixed=MODELS[model];self.omit=omit;self.nodes=nodes;self.nint=nint
  g,w=leggauss(nodes);lo,hi=self.prior['om_bounds'];self.om=lo+(g+1)*(hi-lo)/2;self.qw=w*(hi-lo)/2
  self.f=model_shapes(self.om,nint);self.keep=np.array([i for i in range(13) if omit is None or i not in BLOCKS[omit]])
  f=self.f[:,self.keep];y=Y[self.keep];cov=C[np.ix_(self.keep,self.keep)];inv=np.linalg.inv(cov)
  self.u=np.einsum('ni,ij,nj->n',f,inv,f);self.v=f@inv@y;self.w=float(y@inv@y)
  self.const=-.5*(len(y)*np.log(2*np.pi)+np.linalg.slogdet(cov)[1])
  if self.fixed is None:
   self.mu=self.v/self.u;self.sig=1/np.sqrt(self.u);alo,ahi=self.prior['A_bounds'];self.a=(alo-self.mu)/self.sig;self.b=(ahi-self.mu)/self.sig;self.logtr=logmass(self.a,self.b)
   self.logl=self.const-.5*(self.w-self.v*self.mu)+.5*np.log(2*np.pi/self.u)+self.logtr-np.log(ahi-alo)
   ea,var=truncnorm.stats(self.a,self.b,loc=self.mu,scale=self.sig,moments='mv');self.ea=np.array(ea);self.va=np.array(var);self.ea2=self.ea*self.ea+self.va
  else:
   self.logl=self.const-.5*(self.w-2*self.fixed*self.v+self.fixed*self.fixed*self.u)
   self.ea=np.full(nodes,self.fixed);self.va=np.zeros(nodes);self.ea2=self.ea*self.ea
  self.logunnorm=self.logl+np.log(om_prior_density(self.om,self.prior))+np.log(self.qw)
  # Normalization used only within each declared model; never emitted as evidence.
  self.lognorm=logsumexp(self.logunnorm);self.weights=np.exp(self.logunnorm-self.lognorm)
  assert abs(self.weights.sum()-1)<1e-12 and np.isfinite(self.weights).all()
 def ll_at_om(self,om):
  om=np.atleast_1d(om);f=model_shapes(om,self.nint)[:,self.keep];y=Y[self.keep];inv=np.linalg.inv(C[np.ix_(self.keep,self.keep)])
  u=np.einsum('ni,ij,nj->n',f,inv,f);v=f@inv@y
  if self.fixed is not None:return self.const-.5*(self.w-2*self.fixed*v+self.fixed**2*u)
  mu=v/u;s=1/np.sqrt(u);lo,hi=self.prior['A_bounds']
  return self.const-.5*(self.w-v*mu)+.5*np.log(2*np.pi/u)+logmass((lo-mu)/s,(hi-mu)/s)-np.log(hi-lo)
 def cdf_om(self,x):
  # Integrate continuous density on the interval instead of treating GL nodes as atoms.
  lo,hi=self.prior['om_bounds']
  if x<=lo:return 0.
  if x>=hi:return 1.
  g,w=leggauss(min(self.nodes,256));om=lo+(g+1)*(x-lo)/2
  return float(np.exp(logsumexp(self.ll_at_om(om)+np.log(om_prior_density(om,self.prior))+np.log(w*(x-lo)/2))-self.lognorm))
 @lru_cache(maxsize=16)
 def om_quantile(self,q):return float(brentq(lambda x:self.cdf_om(x)-q,*self.prior['om_bounds'],xtol=1e-12))
 def acdf(self,x,scale=None):
  # Distribution of A*scale(Omega), with positive scale. AP is treated separately.
  scale=np.ones_like(self.om) if scale is None else scale
  if self.fixed is not None:raise ValueError('Fixed-A transformation uses Omega quantiles, not quadrature point masses.')
  zz=(x/scale-self.mu)/self.sig
  c=truncnorm.cdf(zz,self.a,self.b)
  return float(self.weights@c)
 def aquantile(self,q,scale=None):
  scale=np.ones_like(self.om) if scale is None else scale;lo,hi=self.prior['A_bounds']
  return float(brentq(lambda x:self.acdf(x,scale)-q,lo*scale.min(),hi*scale.max(),xtol=1e-11))
 def parameters(self,quantiles=True):
  mo=float(self.weights@self.om);ma=float(self.weights@self.ea) if self.fixed is None else float(self.fixed)
  cov=np.array([[self.weights@((self.om-mo)**2),self.weights@((self.om-mo)*(self.ea-ma))],[self.weights@((self.om-mo)*(self.ea-ma)),self.weights@(self.va+(self.ea-ma)**2)]])
  if self.fixed is not None:cov[0,1]=cov[1,0]=cov[1,1]=0.
  out={'Omega_m':{'mean':mo,'sd':float(np.sqrt(cov[0,0]))},'A':{'mean':ma,'sd':float(np.sqrt(cov[1,1])),'fixed':self.fixed is not None},'covariance_order':['Omega_m','A'],'covariance':cov.tolist()}
  if quantiles:
   oq=[self.om_quantile(q) for q in QLEVELS];aq=[self.aquantile(q) for q in QLEVELS] if self.fixed is None else [self.fixed]*len(QLEVELS)
   for k,v in [('Omega_m',oq),('A',aq)]:out[k]['quantile_levels']=QLEVELS;out[k]['quantiles']=v
  return out
 def forecast(self,quantiles=True):
  dm,dh=distances(self.om,ZGRID,self.nint);ap=dm/dh
  # Coordinate order: all z for DM, all z for DH, all z for AP.
  lin=np.concatenate([dm,dh],axis=1);means_nodes=np.concatenate([self.ea[:,None]*lin,ap],axis=1);means=self.weights@means_nodes
  deviations=means_nodes-means
  cov=(deviations*self.weights[:,None]).T@deviations
  cov[:2*len(ZGRID),:2*len(ZGRID)]+=lin.T@((self.weights*self.va)[:,None]*lin)
  sd=np.sqrt(np.maximum(np.diag(cov),0));corr=cov/np.outer(sd,sd)
  out=[];oq=np.array([self.om_quantile(q) for q in QLEVELS]) if quantiles else None
  for oi,(obs,shapes) in enumerate([('DM_over_rd',dm),('DH_over_rd',dh),('F_AP',ap)]):
   for zi,z in enumerate(ZGRID):
    ix=oi*len(ZGRID)+zi;r={'observable':obs,'z':float(z),'mean':float(means[ix]),'sd':float(sd[ix])}
    if quantiles:
     if oi<2 and self.fixed is None:qs=[self.aquantile(q,shapes[:,zi]) for q in QLEVELS]
     else:
      # Distances decrease with Omega; AP increases. Verify throughout declared domain.
      diff=np.diff(shapes[:,zi]);assert np.all(diff<0) if oi<2 else np.all(diff>0)
      qoms=oq[::-1] if oi<2 else oq;d,h=distances(qoms,[z],self.nint)
      qs=((d[:,0] if oi==0 else h[:,0])*self.fixed if oi<2 else d[:,0]/h[:,0]).tolist()
     r['quantile_levels']=QLEVELS;r['quantiles']=qs
    out.append(r)
  return {'rows':out,'covariance_order':[{'observable':r['observable'],'z':r['z']} for r in out],'parameter_only_covariance':cov.tolist(),'parameter_only_correlation':corr.tolist()}
 def held_logscore(self):
  assert self.omit is not None
  ix=BLOCKS[self.omit];y=Y[ix];cov=C[np.ix_(ix,ix)];inv=np.linalg.inv(cov);f=self.f[:,ix]
  u=np.einsum('ni,ij,nj->n',f,inv,f);v=f@inv@y;ww=float(y@inv@y);const=-.5*(len(y)*np.log(2*np.pi)+np.linalg.slogdet(cov)[1])
  if self.fixed is None:
   s2=self.sig**2;d=ww-2*self.mu*v+self.mu**2*u
   q=d-s2*(v-self.mu*u)**2/(1+s2*u)
   u2=self.u+u;mu2=(self.v+v)/u2;s2new=1/np.sqrt(u2);lo,hi=self.prior['A_bounds']
   # Gaussian predictive density with the exact finite-A truncation correction.
   logpred=const-.5*(np.log1p(s2*u)+q)+logmass((lo-mu2)/s2new,(hi-mu2)/s2new)-self.logtr
  else:logpred=const-.5*(ww-2*self.fixed*v+self.fixed**2*u)
  logdensity=float(logsumexp(np.log(self.weights,where=self.weights>0,out=np.full_like(self.weights,-np.inf))+logpred))
  # Separate identity, computed within this model only: full integral / training integral.
  full=Posterior(self.model,self.prior_name,None,self.nodes,self.nint)
  delta=abs(logdensity-(full.lognorm-self.lognorm))
  assert delta<2e-9
  # Total posterior-predictive covariance = latent training-posterior covariance + held C.
  mn=self.weights@(self.ea[:,None]*f);dev=self.ea[:,None]*f-mn
  latent=(dev*self.weights[:,None]).T@dev+f.T@((self.weights*self.va)[:,None]*f)
  return {'omitted_tracer':ROWS[self.omit]['tracer'],'z':ROWS[self.omit]['z'],'coordinate_indices':ix,'observed':y.tolist(),'predictive_mean':mn.tolist(),'latent_parameter_covariance':latent.tolist(),'stipulated_measurement_covariance':cov.tolist(),'posterior_predictive_covariance':(latent+cov).tolist(),'negative_log_predictive_density':-logdensity,'numerical_integral_identity_abs_error':delta,'training_parameters':self.parameters()}

def run(nodes=1024,nint=96):
 result={'created_utc':stamp(),'code_sha256':hashf(Path(__file__)), 'scope':'Within-model conditional parameter inference and latent geometry; retrospective LOO predictive densities under stipulated compressed Gaussian measurement blocks. Not Euclid coverage.','source_url':'https://arxiv.org/html/2503.14738v3','source_location':'Table 4 baseline blocks; equation 17; appendix B','input_csv_sha256':hashf(SRC/'desi_dr2_table4.csv'),'coordinate_labels':LABELS,'observations':Y.tolist(),'stipulated_covariance':C.tolist(),'model_fixed_A':MODELS,'priors':PRIORS,'forecast_z_grid':ZGRID.tolist(),'quantile_levels':QLEVELS,'quadrature':{'Omega_nodes':nodes,'distance_Gauss_Legendre_order':nint},'software':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'results':{}}
 for prior in PRIORS:
  result['results'][prior]={}
  for model in MODELS:
   p=Posterior(model,prior,nodes=nodes,nint=nint);folds=[Posterior(model,prior,k,nodes,nint).held_logscore() for k in range(7)]
   scores=[x['negative_log_predictive_density'] for x in folds]
   result['results'][prior][model]={'parameters':p.parameters(),'forecast':p.forecast(),'folds':folds,'loo_score_summary':{'sum_negative_log_predictive_density':float(sum(scores)),'mean_per_block':float(np.mean(scores)),'sum_divided_by_13_coordinates':float(sum(scores)/13),'lower_is_better':True,'interpretation':'Retrospective sum of seven LOO log scores, not an independent joint likelihood, model evidence, Bayes factor or model probability.'},'posterior_quadrature_weight_sum':float(p.weights.sum())}
   print(prior,model,'done',flush=True)
 result['completed_utc']=stamp();return result

def write_exports(result,outdir):
 fields=['prior','model','observable','z','mean','sd','q025','q16','median','q84','q975']
 with (outdir/'geometry_forecasts.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fields);w.writeheader()
  for prior,models in result['results'].items():
   for model,res in models.items():
    for rr in res['forecast']['rows']:
     r={k:rr[k] for k in ['observable','z','mean','sd']};r.update({'prior':prior,'model':model});r.update(dict(zip(['q025','q16','median','q84','q975'],rr['quantiles'])));w.writerow(r)
 with (outdir/'loo_predictive_scores.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['prior','model','omitted_tracer','z','coordinates','negative_log_predictive_density'])
  for prior,models in result['results'].items():
   for model,res in models.items():
    for r in res['folds']:w.writerow([prior,model,r['omitted_tracer'],r['z'],len(r['observed']),r['negative_log_predictive_density']])

def verify_inputs():
 expected='a9f3fc66443c4268cb16bb15280b4f1d60c6e7f842f8f2a2025a36ed87a7e013'
 actual=hashf(SRC/'desi_dr2_table4.csv')
 if actual!=expected:raise ValueError('Calibration CSV hash mismatch')
 return {'verified_utc':stamp(),'copied_calibration_csv_verified':True,'sha256':actual}

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--nodes',type=int,default=1024);parser.add_argument('--distance-order',type=int,default=96);parser.add_argument('--output',default='primary_run');args=parser.parse_args()
 out=ROOT/args.output;out.mkdir(exist_ok=False)
 dump(out/'input_verification_before.json',verify_inputs())
 try:
  result=run(args.nodes,args.distance_order);dump(out/'results.json',result);write_exports(result,out);dump(out/'input_verification_after.json',verify_inputs())
 except Exception as e:
  import traceback
  (out/'FAILURE.txt').write_text(stamp()+'\n'+traceback.format_exc());raise
