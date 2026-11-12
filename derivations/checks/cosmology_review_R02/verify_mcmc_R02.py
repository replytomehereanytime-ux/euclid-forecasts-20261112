# emcee posterior (flat priors as in R02/R04) for the BAO+compressed-CMB fits; posterior medians/68% of params and of
# predictive DM/rd, DH/rd at z=0.9,1.2,1.5,1.8. Independent of R02's Laplace bands and R04's reweighted chains.
import numpy as np, json, sys, time, emcee
from verify_fits_R02 import *
NW,NS,BURN=40,int(sys.argv[2]) if len(sys.argv)>2 else 4000,1000
jobs=sys.argv[1].split(',')
out={}
for job in jobs:
    model,br=job.split('_'); y,Ci=branch(br); r=fit(model,br); q0=r['_q']; Cq=r['_Cq']
    lp=lambda q: -0.5*chi2(q,model,y,Ci)
    rng=np.random.default_rng(12); p0=rng.multivariate_normal(q0,Cq*0.25,NW)
    t=time.time(); S=emcee.EnsembleSampler(NW,len(q0),lp); S.run_mcmc(p0,NS,progress=False)
    ch=S.get_chain(discard=BURN,thin=5,flat=True)
    try: tau=S.get_autocorr_time(discard=BURN,quiet=True).tolist()
    except Exception as e: tau=str(e)
    pct=lambda a: np.percentile(a,[16,50,84],axis=0)
    sub=ch[rng.choice(len(ch),min(3000,len(ch)),replace=False)]
    P=np.array([predvec(s,model) for s in sub])
    out[job]={'n':len(ch),'tau':tau,'accept':float(np.mean(S.acceptance_fraction)),'sec':round(time.time()-t,1),
      'param_p16_50_84':pct(ch).T.tolist(),'param_mean':ch.mean(0).tolist(),'param_std':ch.std(0).tolist(),
      'pred_p16_50_84':pct(P).T.tolist(),'pred_std':P.std(0).tolist(),'pred_corr':np.corrcoef(P.T).round(4).tolist()}
    print(job,'sec',out[job]['sec'],'tau',tau,'\n params p16/50/84:',np.round(pct(ch).T,5).tolist(),'\n std',np.round(ch.std(0),5).tolist(),flush=True)
    json.dump(out,open(f'verify_mcmc_R02_{sys.argv[1].replace(",","+")}.json','w'),indent=1)
