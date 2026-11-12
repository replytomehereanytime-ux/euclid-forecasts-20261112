"""R03 recompute of R05 fσ8/σ8/S8 (held: R05 used truncated-r_s chains/best fits). Same CAMB settings as R05 fs8_camb_R05.py
(CAMB in rs3env, PPF for CPL, mnu=0, Neff 3.046, ln1e10As~N(3.044,0.014), ns 0.9649). Corrected (full r_s) REPLACEMENT-branch posteriors:
CPL = R03 fresh full-r_s emcee chain (150 draws); ΛCDM = fresh full-r_s emcee (24x3000, 150 draws). Seed 20261112."""
import numpy as np, json, sys, camb, emcee
sys.path.insert(0,'.'); import cplmodel_r03 as M; M.RSMODE='full'
ZS=[0.9,1.2,1.3,1.5,1.8]; ZZ=sorted(ZS+[0.0],reverse=True)
def run(Om,h,w0,wa,ob,lnAs):
    p=camb.set_params(H0=100*h,ombh2=ob,omch2=Om*h*h-ob,mnu=0,nnu=3.046,As=np.exp(lnAs)*1e-10,ns=0.9649,w=w0,wa=wa,dark_energy_model='ppf' if (w0,wa)!=(-1,0) else 'fluid')
    p.set_matter_power(redshifts=ZZ,kmax=2.0); r=camb.get_results(p); zr=list(r.transfer_redshifts); fs=r.get_fsigma8(); s8=r.get_sigma8()
    return {z:(float(fs[zr.index(z)]),float(s8[zr.index(z)])) for z in ZZ}
rng=np.random.default_rng(20261112); F=json.load(open('fullrs_r03_output.json'))
def lnp(T):
    T=np.atleast_2d(T); th=np.tile([0.3,0.68,-1.0,0.0,0.0224],(len(T),1)); th[:,[0,1,4]]=T; ok=M.inprior(th); o=np.full(len(T),-np.inf)
    if ok.any(): o[ok]=-0.5*M.chi2(th[ok],'REPLACEMENT')
    return o
x=F['fits']['REPLACEMENT']['LCDM']['x']; S=emcee.EnsembleSampler(24,3,lnp,vectorize=True); S._random=np.random.mtrand.RandomState(20261112)
S.run_mcmc(np.array(x)+np.array([0.003,0.003,0.0001])*rng.standard_normal((24,3)),3000,progress=False); L=S.get_chain(discard=800,flat=True)
chains={'LCDM':np.column_stack([L[:,0],L[:,1],-np.ones(len(L)),np.zeros(len(L)),L[:,2]]),'w0waCDM':np.load('fullrs_cpl_chain_REPLACEMENT_R03.npy')}
best={'LCDM':(x[0],x[1],-1.0,0.0,x[2]),'w0waCDM':tuple(F['fits']['REPLACEMENT']['CPL']['x'])}
q=lambda a:[float(np.quantile(a,t)) for t in (0.16,0.5,0.84,0.025,0.975)]
out={'LCDM_chain_Om_h':[q(L[:,0]),q(L[:,1])]}
for n in ['LCDM','w0waCDM']:
    C=chains[n]; idx=rng.choice(len(C),150,replace=False); lnAs=rng.normal(3.044,0.014,150)
    res=[run(*map(float,C[i]),float(lnAs[k])) for k,i in enumerate(idx)]; bf=run(*best[n],3.044)
    s80=np.array([r[0.0][1] for r in res]); out[n]={'N':150,'sigma8_0':q(s80),'S8_0':q(s80*np.sqrt(C[idx,0]/0.3)),'bestfit_sigma8_0':bf[0.0][1],'bestfit_S8_0':bf[0.0][1]*np.sqrt(best[n][0]/0.3),
      'fsigma8':{str(z):{'q16_50_84_2.5_97.5':q(np.array([r[z][0] for r in res])),'bestfit':bf[z][0]} for z in ZS}}
    print(n,'s8_0',out[n]['sigma8_0'][:3],'S8',out[n]['S8_0'][1],'fs8(1.3)',out[n]['fsigma8']['1.3']['q16_50_84_2.5_97.5'][:3],flush=True)
R=json.load(open('/workspace/r03-out/euclid_20261112/xact_R05/fs8_camb_R05_output.json'))
out['shift_vs_R05_median']={n:{'sigma8_0':out[n]['sigma8_0'][1]/R[n]['sigma8_z0 [16,50,84,2.5,97.5]'][1]-1,'S8_0':out[n]['S8_0'][1]/R[n]['S8_z0 median']-1,
   **{f'fsigma8_{z}':out[n]['fsigma8'][str(z)]['q16_50_84_2.5_97.5'][1]/R[n]['pred'][str(z)]['fsigma8 [16,50,84,2.5,97.5]'][1]-1 for z in [0.9,1.2,1.5,1.8]}} for n in ['LCDM','w0waCDM']}
json.dump(out,open('fs8_fullrs_r03_output.json','w'),indent=1); print(json.dumps(out['shift_vs_R05_median'],indent=1))
