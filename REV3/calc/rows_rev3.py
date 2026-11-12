"""REV3 BAO+CMB rows. Model: model_rev3.py, CMBMODE given on argv (default 'rescale' = adopted). seed 20261112."""
import sys,json,time; sys.path.insert(0,'.'); import numpy as np, model_rev3 as M, emcee
from scipy.optimize import minimize
MODE=sys.argv[1] if len(sys.argv)>1 else 'rescale'; BRS=sys.argv[2].split(',') if len(sys.argv)>2 else ['REPLACEMENT','PRIMARY']
M.CMBMODE=MODE; t0=time.time(); G4=[0.9,1.2,1.5,1.8]; O={'meta':{'CMBMODE':MODE,'LA_SCALE':M.LA_SCALE,'ZSTAR_FIX':M.ZSTAR_FIX,'seed':20261112,'emcee':emcee.__version__}}
BASE=np.array([0.3,0.68,-1.0,0.0,0.0224,0.0]); NAMES=['Om','h','w0','wa','ob','Ok']
MODELS={'LCDM':[0,1,4],'wCDM':[0,1,2,4],'oLCDM':[0,1,4,5],'CPL':[0,1,2,3,4]}
def full(T,free):
    T=np.atleast_2d(T); th=np.tile(BASE,(len(T),1)); th[:,free]=T; return th
def fit(br,free,starts):
    f=lambda q: float(M.chi2(full(q,free),br)[0]) if M.inprior(full(q,free))[0] else 1e10
    b=None
    for s in starts:
        r=minimize(f,s,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-11,maxiter=40000,maxfev=40000))
        r=minimize(f,r.x,method='Nelder-Mead',options=dict(xatol=1e-11,fatol=1e-12,maxiter=40000,maxfev=40000))
        if b is None or r.fun<b.fun: b=r
    return b
def q(x): return [float(np.quantile(x,p)) for p in (0.16,0.5,0.84)]
def run(br,free,x0,scale,nw,steps,burn,thin):
    def lnp(T):
        th=full(T,free); ok=M.inprior(th); out=np.full(len(th),-np.inf)
        if ok.any(): out[ok]=-0.5*M.chi2(th[ok],br)
        return out
    rng=np.random.default_rng(20261112); p0=np.array(x0)+np.array(scale)*rng.standard_normal((nw,len(free)))
    if 3 in free: i2,i3=free.index(2),free.index(3); p0[:,i3]=np.minimum(p0[:,i3],-0.01-p0[:,i2])
    S=emcee.EnsembleSampler(nw,len(free),lnp,vectorize=True); S._random=np.random.mtrand.RandomState(20261112); S.run_mcmc(p0,steps,progress=False)
    fl=S.get_chain(discard=burn,thin=thin,flat=True)
    try: tau=S.get_autocorr_time(discard=burn,tol=0).tolist()
    except Exception as e: tau=str(e)
    return full(fl,free),{'nwalkers':nw,'steps':steps,'burn':burn,'thin':thin,'N':len(fl),'acc':float(np.mean(S.acceptance_fraction)),'tau':tau}
SC={'LCDM':([0.004,0.004,0.00005],32,5000,1000,1),'wCDM':([0.004,0.004,0.02,0.00005],32,5000,1000,1),
    'oLCDM':([0.004,0.004,0.00005,0.001],32,6000,1500,1),'CPL':([0.005,0.005,0.05,0.15,0.0001],40,10000,2500,5)}
ST={'LCDM':[[0.30,0.686,0.0225],[0.32,0.67,0.0222]],'wCDM':[[0.30,0.69,-1.03,0.02247],[0.31,0.70,-0.95,0.0223]],
    'oLCDM':[[0.30,0.686,0.0225,0.0],[0.31,0.68,0.0224,0.002]],'CPL':[[0.30,0.69,-0.9,-0.4,0.0225],[0.32,0.67,-0.6,-1.4,0.0223],[0.29,0.70,-1.0,0.0,0.0225],[0.35,0.64,-0.45,-1.6,0.02235]]}
for br in BRS:
    O[br]={}
    for mod,free in MODELS.items():
        b=fit(br,free,ST[mod]); sc,nw,steps,burn,thin=SC[mod]
        th,info=run(br,free,b.x,sc,nw,steps,burn,thin)
        res={'bestfit':{NAMES[i]:float(v) for i,v in zip(free,b.x)},'chi2_min':float(b.fun),'mcmc':info,
             'params':{NAMES[i]:{'q16_50_84':q(th[:,i]),'mean':float(th[:,i].mean()),'sd':float(th[:,i].std())} for i in free}}
        res['params']['omh2']={'q16_50_84':q(th[:,0]*th[:,1]**2),'sd':float((th[:,0]*th[:,1]**2).std())}
        if mod=='CPL':
            res['frac_wa_below_-3.5']=float(np.mean(th[:,3]<-3.5)); res['frac_wa_below_-3.9']=float(np.mean(th[:,3]<-3.9))
        D={}; vec=[]
        for z in G4:
            dm,dh=M.dist(z,*th[:,:5].T,th[:,5]); bf=M.dist(z,*full(b.x,free)[0][:5],full(b.x,free)[0][5])
            D[str(z)]={'DM/rd':{'q16_50_84':q(dm),'mean':float(dm.mean()),'sd':float(dm.std()),'bestfit':float(bf[0][0])},
                       'DH/rd':{'q16_50_84':q(dh),'mean':float(dh.mean()),'sd':float(dh.std()),'bestfit':float(bf[1][0])}}
            vec+=[dm,dh]
        C=np.cov(np.array(vec)); ev=np.linalg.eigvalsh(C/np.outer(np.sqrt(np.diag(C)),np.sqrt(np.diag(C))))
        res['dist']=D; res['pred_corr_eigs']=ev.tolist(); res['rd_median']=float(np.median(M.rdf(th[:,0],th[:,1],th[:,4])))
        res['cmb_at_bestfit']=M.cmb(*full(b.x,free)[0][:5],full(b.x,free)[0][5])[0].tolist()
        O[br][mod]=res
        if mod in ('LCDM','oLCDM'): np.save(f'chain_{mod}_{br}_{MODE}.npy',th[::4])
        if mod=='CPL': np.save(f'chain_CPL_{br}_{MODE}.npy',th)
        print(br,mod,{k:round(v['q16_50_84'][1],5) for k,v in res['params'].items()},'chi2',round(b.fun,3),'tau',info['tau'] if isinstance(info['tau'],str) else [round(t) for t in info['tau']],round(time.time()-t0),flush=True)
O['runtime_s']=time.time()-t0
json.dump(O,open(f'rows_rev3_{MODE}.json','w'),indent=1); print('DONE')
