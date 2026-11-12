"""R03 Task A: CPL old-PRIMARY (original DESI DR2 Lya) bands with a valid covariance. Box only; rs3env numpy/scipy/emcee 3.1.6; seed 20261112."""
import numpy as np, json, time, sys, hashlib; sys.path.insert(0,'.'); from cplmodel_r03 import *
from scipy.optimize import minimize
import emcee
t0=time.time(); OUT={'meta':{'seed':20261112,'emcee':emcee.__version__,'numpy':np.__version__}}
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
OUT['meta']['inputs']={p:sha(p) for p in [D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',D+'desi_gaussian_bao_ALL_GCcomb_cov.txt',D+'chain_w0waCDM.npy',D+'fit_cpl.py']}
G4=[0.9,1.2,1.5,1.8]
def wq(x,w,qs=(0.025,0.16,0.5,0.84,0.975)):
    i=np.argsort(x); cw=np.cumsum(w[i]); return [float(np.interp(q,cw,x[i])) for q in qs]
def bands(S,w=None):
    w=np.full(len(S),1/len(S)) if w is None else w/np.sum(w); P=pred(S); b={}; vec=[]
    for z in ZG:
        DM,DH,F=P[z]; b[z]={'DM/rd':wq(DM,w),'DH/rd':wq(DH,w),'DM/DH':wq(F,w)}
        if z in G4: vec+= [DM,DH]
    V=np.array(vec); mu=V@w; C=((V-mu[:,None])*w)@(V-mu[:,None]).T
    ev=np.linalg.eigvalsh(C); s=np.sqrt(np.diag(C)); R=C/np.outer(s,s)
    return b,{'order':'[DM/rd,DH/rd] at z=0.9,1.2,1.5,1.8','mean':mu.tolist(),'sd':s.tolist(),'corr':np.round(R,4).tolist(),'eig':ev.tolist(),'PD':bool(ev.min()>0),'cond':float(ev.max()/ev.min())}
def pstats(S,w=None):
    w=np.full(len(S),1/len(S)) if w is None else w/np.sum(w)
    return {n:wq(S[:,i],w) for i,n in enumerate(['Om','h','w0','wa','ob'])}
# ---- 1. original box chain (emcee, old Lya data, fit_cpl.py; 48000 samples) = PRIMARY posterior, unweighted
ch=np.load(D+'chain_w0waCDM.npy')
OUT['chain_primary']={'N':len(ch),'params':pstats(ch),'frac_wa_below_-3.5':float(np.mean(ch[:,3]<-3.5))}
OUT['chain_primary']['bands'],OUT['chain_primary']['predcov']=bands(ch)
# ---- V1. reweight the same chain to the REPLACEMENT Lya point -> must reproduce R04 §5 / R02 CTC-5B
lw=-0.5*(chi2(ch,'REPLACEMENT',False)-chi2(ch,'PRIMARY',False)); w=np.exp(lw-lw.max())
OUT['chain_reweighted_replacement']={'ESS':float(1/np.sum((w/w.sum())**2)),'params':pstats(ch,w)}
OUT['chain_reweighted_replacement']['bands'],OUT['chain_reweighted_replacement']['predcov']=bands(ch,w)
print('chain parts done',time.time()-t0,flush=True)
# ---- 3. best fits + numerical Hessian (central differences, scaled steps), PD check
def best(branch):
    f=lambda t: float(chi2(t,branch)[0]) if inprior(t)[0] else 1e10
    bb=None
    for s in ([0.345,0.683,-0.72,-1.0,0.02215],[0.31,0.68,-0.9,-0.3,0.0224],[0.33,0.67,-0.6,-1.4,0.0222],[0.36,0.67,-0.4,-2.0,0.0221]):
        r=minimize(f,s,method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-10,maxiter=20000,maxfev=20000))
        r=minimize(f,r.x,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-11,maxiter=20000,maxfev=20000))
        if bb is None or r.fun<bb.fun: bb=r
    return bb
def hess(f,x,st):
    n=len(x); H=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            ei=np.eye(n)[i]*st[i]; ej=np.eye(n)[j]*st[j]
            H[i,j]=H[j,i]=(f(x+ei+ej)-f(x+ei-ej)-f(x-ei+ej)+f(x-ei-ej))/(4*st[i]*st[j])
    return H
HS={}
for br in ['PRIMARY','REPLACEMENT']:
    b=best(br); f=lambda t: float(chi2(t,br)[0]); res={'chi2_min':float(b.fun),'best':b.x.tolist()}
    for k,fac in [('step_1e-3',1e-3),('step_3e-3',3e-3),('step_1e-2',1e-2)]:
        st=np.array([0.01,0.01,0.1,0.3,0.0002])*fac/1e-3*0.1  # base steps scaled
        H=hess(f,b.x,st)/2  # Fisher = Hessian of chi2 / 2
        ev=np.linalg.eigvalsh(H); res[k]={'steps':st.tolist(),'fisher_eig':ev.tolist(),'PD':bool(ev.min()>0)}
        if ev.min()>0:
            Cp=np.linalg.inv(H); res[k]['param_sd']=np.sqrt(np.diag(Cp)).tolist()
            # Laplace predictive bands via finite-difference Jacobian
            J=[]; m0=np.concatenate([[pred(b.x,[z])[z][0][0],pred(b.x,[z])[z][1][0]] for z in G4])
            for i in range(5):
                e=np.eye(5)[i]*st[i]; mp=np.concatenate([[pred(b.x+e,[z])[z][0][0],pred(b.x+e,[z])[z][1][0]] for z in G4]); mm=np.concatenate([[pred(b.x-e,[z])[z][0][0],pred(b.x-e,[z])[z][1][0]] for z in G4]); J.append((mp-mm)/(2*st[i]))
            J=np.array(J).T; Cpred=J@Cp@J.T; res[k]['laplace_mean']=m0.tolist(); res[k]['laplace_sd']=np.sqrt(np.diag(Cpred)).tolist(); res[k]['laplace_pred_eig']=np.linalg.eigvalsh(Cpred).tolist()
    HS[br]=res; print(br,'hessian done',time.time()-t0,flush=True)
OUT['hessian']=HS
# ---- 2. fresh independent emcee runs (seeded), both branches
def lnp(T,br):
    T=np.atleast_2d(T); ok=inprior(T); out=np.full(len(T),-np.inf)
    if ok.any(): out[ok]=-0.5*chi2(T[ok],br)
    return out
FR={}
for br in ['PRIMARY','REPLACEMENT']:
    rng=np.random.default_rng(20261112); nw=40
    p0=np.array(HS[br]['best'])+np.array([0.005,0.005,0.05,0.15,0.0001])*rng.standard_normal((nw,5))
    p0[:,3]=np.minimum(p0[:,3],-0.01-p0[:,2]); 
    S=emcee.EnsembleSampler(nw,5,lambda T: lnp(T,br),vectorize=True,seed=20261112) if False else emcee.EnsembleSampler(nw,5,lambda T: lnp(T,br),vectorize=True)
    np.random.seed(20261112); S._random=np.random.mtrand.RandomState(20261112)
    S.run_mcmc(p0,8000,progress=False)
    try: tau=S.get_autocorr_time(discard=2000,tol=0).tolist()
    except Exception as e: tau=str(e)
    fl=S.get_chain(discard=2000,thin=5,flat=True)
    r={'nwalkers':nw,'steps':8000,'discard':2000,'thin':5,'N':len(fl),'acc':float(np.mean(S.acceptance_fraction)),'tau':tau,'params':pstats(fl),'chi2_min_sample':float(-2*S.get_log_prob(discard=2000,flat=True).max())}
    r['bands'],r['predcov']=bands(fl); FR[br]=r; np.save(f'fresh_chain_{br}_R03.npy',fl); print(br,'emcee done',time.time()-t0,flush=True)
OUT['fresh_emcee']=FR
OUT['meta']['runtime_s']=time.time()-t0
json.dump(OUT,open('cpl_oldprimary_r03_output.json','w'),indent=1)
print('DONE',time.time()-t0)
