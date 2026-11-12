"""R03 corrected rerun (r_s(z*) integrated to infinity). rs3env numpy/scipy/emcee 3.1.6; seed 20261112."""
import numpy as np, json, sys, time; sys.path.insert(0,'.'); import cplmodel_r03 as M
from scipy.optimize import minimize
import emcee
M.RSMODE='full'; t0=time.time(); O={'meta':{'RSMODE':M.RSMODE,'seed':20261112,'emcee':emcee.__version__}}
G4=[0.9,1.2,1.5,1.8]
def wq(x,qs=(0.025,0.16,0.5,0.84,0.975)): return [float(np.quantile(x,q)) for q in qs]
def bands(S):
    P=M.pred(S); b={}; vec=[]
    for z in M.ZG:
        DM,DH,F=P[z]; b[str(z)]={'DM/rd':wq(DM),'DH/rd':wq(DH),'DM/DH':wq(F)}
        if z in G4: vec+=[DM,DH]
    V=np.array(vec); C=np.cov(V); ev=np.linalg.eigvalsh(C); s=np.sqrt(np.diag(C))
    return b,{'sd':s.tolist(),'corr':np.round(C/np.outer(s,s),4).tolist(),'eig':ev.tolist(),'PD':bool(ev.min()>0)}
def fit(br,free,start):
    def f(q):
        th=np.array([0.3,0.68,-1.0,0.0,0.0224]); th[free]=q
        if not (0.1<th[0]<0.6 and 0.4<th[1]<1 and 0.015<th[4]<0.03 and -4<th[3]<2 and th[2]+th[3]<0): return 1e10
        return float(M.chi2(th,br)[0])
    b=None
    for s in start:
        r=minimize(f,s,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-11,maxiter=40000,maxfev=40000)); r=minimize(f,r.x,method='Nelder-Mead',options=dict(xatol=1e-11,fatol=1e-12,maxiter=40000,maxfev=40000))
        if b is None or r.fun<b.fun: b=r
    return b
O['fits']={}
for br in ['PRIMARY','REPLACEMENT']:
    l=fit(br,[0,1,4],[[0.30,0.686,0.0225],[0.32,0.70,0.0222]]); w=fit(br,[0,1,2,4],[[0.30,0.69,-1.03,0.02247],[0.31,0.70,-0.95,0.0223]])
    c=fit(br,[0,1,2,3,4],[[0.30,0.69,-0.9,-0.4,0.0225],[0.32,0.67,-0.6,-1.4,0.0223],[0.29,0.70,-1.0,0.0,0.0225]])
    O['fits'][br]={'LCDM':{'chi2':l.fun,'x':l.x.tolist()},'wCDM':{'chi2':w.fun,'x':w.x.tolist()},'CPL':{'chi2':c.fun,'x':c.x.tolist()}}
    print(br,O['fits'][br],time.time()-t0,flush=True)
def run(br,nd,free,x0,scale,nw,steps,burn,thin):
    def lnp(T):
        T=np.atleast_2d(T); th=np.tile([0.3,0.68,-1.0,0.0,0.0224],(len(T),1)); th[:,free]=T
        ok=M.inprior(th); out=np.full(len(T),-np.inf)
        if ok.any(): out[ok]=-0.5*M.chi2(th[ok],br)
        return out
    rng=np.random.default_rng(20261112); p0=np.array(x0)+np.array(scale)*rng.standard_normal((nw,nd))
    if nd==5: p0[:,3]=np.minimum(p0[:,3],-0.01-p0[:,2])
    S=emcee.EnsembleSampler(nw,nd,lnp,vectorize=True); S._random=np.random.mtrand.RandomState(20261112); S.run_mcmc(p0,steps,progress=False)
    fl=S.get_chain(discard=burn,thin=thin,flat=True)
    try: tau=S.get_autocorr_time(discard=burn,tol=0).tolist()
    except Exception as e: tau=str(e)
    th=np.tile([0.3,0.68,-1.0,0.0,0.0224],(len(fl),1)); th[:,free]=fl
    return th,{'nwalkers':nw,'steps':steps,'burn':burn,'thin':thin,'N':len(fl),'acc':float(np.mean(S.acceptance_fraction)),'tau':tau}
O['mcmc']={}
for br in ['PRIMARY','REPLACEMENT']:
    x=O['fits'][br]['wCDM']['x']; th,info=run(br,4,[0,1,2,4],x,[0.004,0.004,0.02,0.00005],32,5000,1000,1)
    info['w']={'median':float(np.median(th[:,2])),'std':float(th[:,2].std()),'q16_84':[float(np.quantile(th[:,2],.16)),float(np.quantile(th[:,2],.84))]}
    info['bands'],info['predcov']=bands(th); O['mcmc'][f'wCDM_{br}']=info; print('wCDM',br,info['w'],info['tau'],time.time()-t0,flush=True)
    x=O['fits'][br]['CPL']['x']; th,info=run(br,5,[0,1,2,3,4],x,[0.005,0.005,0.05,0.15,0.0001],40,10000,2500,5)
    info['params']={n:wq(th[:,i]) for i,n in enumerate(['Om','h','w0','wa','ob'])}; info['frac_wa_below_-3.5']=float(np.mean(th[:,3]<-3.5))
    info['bands'],info['predcov']=bands(th); O['mcmc'][f'CPL_{br}']=info; np.save(f'fullrs_cpl_chain_{br}_R03.npy',th); print('CPL',br,info['params']['w0'],info['tau'],time.time()-t0,flush=True)
# shifts old (truncated, R02 frozen best fits) vs corrected best fits, z=1.3 and grid
R02={'LCDM_PRIMARY':[0.3239712387770484,0.6986764715110352,-1,0,0.022280652121375474],'LCDM_REPLACEMENT':[0.32428051560186677,0.6984599622041885,-1,0,0.022279281807078617]}
O['shifts']={}
for k,old in R02.items():
    br=k.split('_')[1]; x=O['fits'][br]['LCDM']['x']; new=[x[0],x[1],-1,0,x[2]]
    po=M.pred(np.array(old),[0.9,1.3,1.8]); pn=M.pred(np.array(new),[0.9,1.3,1.8])
    O['shifts'][k]={str(z):{'DM/rd_old_over_new-1':float(po[z][0][0]/pn[z][0][0]-1),'DH/rd_old_over_new-1':float(po[z][1][0]/pn[z][1][0]-1),'F_AP_old_over_new-1':float(po[z][2][0]/pn[z][2][0]-1)} for z in [0.9,1.3,1.8]}
O['runtime_s']=time.time()-t0
json.dump(O,open('fullrs_r03_output.json','w'),indent=1); print(json.dumps(O['shifts'],indent=1)); print('DONE')
