"""PROPOSALS (pending the author's decision): (1) exact-z / fine-grid-cubic scoring with explicit inter-point predicted covariance; (3) wCDM Hessian step scan vs MCMC.
rs3env numpy/scipy/emcee. Seed 20261112. Uses R03/calc/cplmodel_r03.py (same physics as R02/R04)."""
import numpy as np, json, sys, time; sys.path.insert(0,'../calc'); from cplmodel_r03 import *
from scipy.optimize import minimize
from scipy.interpolate import CubicSpline
import emcee
t0=time.time(); O={}
# frozen best fits (R02 raw_outputs_R02.txt), full 5-vector (Om,h,w0,wa,ob)
FZ={'CTC-2P':[0.3239712387770484,0.6986764715110352,-1,0,0.022280652121375474],'CTC-2B':[0.32428051560186677,0.6984599622041885,-1,0,0.022279281807078617],
    'CTC-3P':[0.31674477677914953,0.708345246004449,-1.0433206173905798,0,0.02222976781269264],'CTC-3B':[0.3162078996061392,0.7092904612062401,-1.048738562433359,0,0.022221657742654256]}
def mvec(th,zs):
    p=pred(np.array(th),zs); return np.concatenate([[p[z][0][0],p[z][1][0]] for z in zs])
# (1a) interpolation error: linear on R02 4-node grid vs cubic on frozen fine grid dz=0.01 (0.85..1.85) vs exact
zt=np.round(np.arange(0.90,1.8001,0.005),3)
for k,th in FZ.items():
    ex=pred(np.array(th),list(zt)); DMx=np.array([ex[z][0][0] for z in zt]); DHx=np.array([ex[z][1][0] for z in zt])
    g4=[0.9,1.2,1.5,1.8]; p4=pred(np.array(th),g4); lin=lambda i: np.interp(zt,g4,[p4[z][i][0] for z in g4])
    zf=np.round(np.arange(0.85,1.8501,0.01),3); pf=pred(np.array(th),list(zf))
    cs=lambda i: CubicSpline(zf,[pf[z][i][0] for z in zf])(zt)
    cs4=lambda i: CubicSpline(g4,[p4[z][i][0] for z in g4])(zt)
    O.setdefault('interp',{})[k]={'linear_4node_maxabs':{'DM/rd':float(np.max(abs(lin(0)-DMx))),'DH/rd':float(np.max(abs(lin(1)-DHx)))},
        'cubic_4node_maxabs':{'DM/rd':float(np.max(abs(cs4(0)-DMx))),'DH/rd':float(np.max(abs(cs4(1)-DHx)))},
        'cubic_fine_dz0.01_maxabs':{'DM/rd':float(np.max(abs(cs(0)-DMx))),'DH/rd':float(np.max(abs(cs(1)-DHx)))},
        'test_points':len(zt)}
print('interp done',time.time()-t0,flush=True)
# (1b) explicit inter-point predicted covariance at arbitrary published z: C_pred = J Cθ Jᵀ, Cθ from converged Hessian (wCDM uses MCMC, see 3)
def hess(f,x,st):
    n=len(x); H=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            ei=np.eye(n)[i]*st[i]; ej=np.eye(n)[j]*st[j]
            H[i,j]=H[j,i]=(f(x+ei+ej)-f(x+ei-ej)-f(x-ei+ej)+f(x-ei-ej))/(4*st[i]*st[j])
    return H
# (3) wCDM step scan (free: Om,h,w,ob; wa=0) + MCMC
base=np.array([0.004,0.004,0.02,0.00006])
for k in ['CTC-3P','CTC-3B']:
    br='PRIMARY' if k.endswith('P') else 'REPLACEMENT'; x0=np.array([FZ[k][0],FZ[k][1],FZ[k][2],FZ[k][4]])
    f=lambda q: float(chi2([q[0],q[1],q[2],0.0,q[3]],br)[0])
    scan={}
    for fac in [2,1,0.5,0.25,0.1,0.05,0.025]:
        H=hess(f,x0,base*fac)/2; ev=np.linalg.eigvalsh(H)
        scan[str(fac)]={'PD':bool(ev.min()>0),'sd':np.sqrt(np.diag(np.linalg.inv(H))).tolist() if ev.min()>0 else None}
    # MCMC
    def lnp(T):
        T=np.atleast_2d(T); ok=(0.1<T[:,0])&(T[:,0]<0.6)&(0.4<T[:,1])&(T[:,1]<1)&(-3<T[:,2])&(T[:,2]<1)&(0.018<T[:,3])&(T[:,3]<0.027); out=np.full(len(T),-np.inf)
        if ok.any(): Tk=T[ok]; out[ok]=-0.5*chi2(np.column_stack([Tk[:,0],Tk[:,1],Tk[:,2],np.zeros(len(Tk)),Tk[:,3]]),br)
        return out
    rng=np.random.default_rng(20261112); nw=32; p0=x0+np.array([0.003,0.003,0.02,0.00005])*rng.standard_normal((nw,4))
    S=emcee.EnsembleSampler(nw,4,lnp,vectorize=True); S._random=np.random.mtrand.RandomState(20261112); S.run_mcmc(p0,5000,progress=False)
    fl=S.get_chain(discard=1000,flat=True)
    try: tau=S.get_autocorr_time(discard=1000,tol=0).tolist()
    except Exception as e: tau=str(e)
    wq=np.percentile(fl[:,2],[16,50,84])
    Cth=np.cov(fl.T)
    O.setdefault('wcdm_step_scan',{})[k]={'branch':br,'base_steps(Om,h,w,ob)':base.tolist(),'scan_factor->(PD, sd)':scan,'mcmc':{'N':len(fl),'tau':tau,'w_median':float(wq[1]),'w_q16_q84':[float(wq[0]),float(wq[2])],'w_std':float(fl[:,2].std()),'param_mean':fl.mean(0).tolist(),'param_cov':Cth.tolist()}}
    print(k,'scan+mcmc done',time.time()-t0,flush=True)
# (1b) demo: explicit C_pred at a hypothetical published z set (not Euclid values; z only) for CTC-3B (MCMC Cθ) and CTC-2B (Hessian Cθ)
zdemo=[0.95,1.05,1.35,1.65]
def jac(th5,free,zs,st):
    J=[]
    for i,(idx,s) in enumerate(zip(free,st)):
        e=np.zeros(5); e[idx]=s; J.append((mvec(np.array(th5)+e,zs)-mvec(np.array(th5)-e,zs))/(2*s))
    return np.array(J).T
th=FZ['CTC-3B']; Cth=np.array(O['wcdm_step_scan']['CTC-3B']['mcmc']['param_cov'])
J=jac(th,[0,1,2,4],zdemo,[1e-4,1e-4,1e-3,1e-6]); Cp=J@Cth@J.T
O['demo_Cpred_CTC-3B_MCMCtheta']={'z':zdemo,'order':'[DM/rd,DH/rd] per z','m':mvec(np.array(th),zdemo).tolist(),'sd':np.sqrt(np.diag(Cp)).tolist(),'corr':np.round(Cp/np.outer(np.sqrt(np.diag(Cp)),np.sqrt(np.diag(Cp))),4).tolist(),'eig':np.linalg.eigvalsh(Cp).tolist()}
f2=lambda q: float(chi2([q[0],q[1],-1,0.0,q[2]],'REPLACEMENT')[0]); x2=np.array([th[0] for th in [FZ['CTC-2B']]]+[FZ['CTC-2B'][1],FZ['CTC-2B'][4]])
H2=hess(f2,x2,np.array([0.002,0.0015,0.00006])*0.25)/2; C2=np.linalg.inv(H2); J2=jac(FZ['CTC-2B'],[0,1,4],zdemo,[1e-4,1e-4,1e-6]); Cp2=J2@C2@J2.T
O['demo_Cpred_CTC-2B_Hessiantheta']={'z':zdemo,'m':mvec(np.array(FZ['CTC-2B']),zdemo).tolist(),'sd':np.sqrt(np.diag(Cp2)).tolist(),'param_sd':np.sqrt(np.diag(C2)).tolist()}
O['runtime_s']=time.time()-t0
json.dump(O,open('proposals_calc_r03_output.json','w'),indent=1); print(json.dumps({k:v for k,v in O.items() if k!='wcdm_step_scan'},indent=1)[:3000])
for k,v in O['wcdm_step_scan'].items(): print(k,{f:(s['PD'],round(s['sd'][2],5) if s['sd'] else None) for f,s in v['scan_factor->(PD, sd)'].items()}, v['mcmc']['w_median'],v['mcmc']['w_std'],v['mcmc']['tau'])
