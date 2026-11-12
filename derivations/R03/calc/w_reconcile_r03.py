"""R03 Task B: reconcile R02 constant-w (BAO + compressed CMB) with BF-2 (BAO-only, A free). rs3env numpy/scipy."""
import numpy as np, json, sys; sys.path.insert(0,'.'); from cplmodel_r03 import *
from scipy.optimize import minimize
from scipy.special import erf
O={}
def u_vec(Om,w,rad=False,h=0.68):
    """shape vector u with model = A*u (no radiation: exact; BF-2 convention)"""
    out=[]
    for zi,qi in zip(Z,Q):
        DM=float(DCh(zi,Om,h,w,0.0,rad)); DH=1/float(E(zi,Om,h,w,0.0,rad))
        out.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi])
    return np.array(out)
def prof_A(u,d,Ci):
    a=u@Ci@u; b=u@Ci@d; A=b/a; return A, float(d@Ci@d-b*b/a), a
# ---- B0/B1: BF-2 setup exactly as stated in HANDOFF.md §2.0 (13 DESI points, Lya branch, no CMB, no SNe, no radiation,
#      flat, E^2=Om(1+z)^3+(1-Om)(1+z)^{3(1+w)}, A=c/(H0 rd) free U(20,40), Om U(0.1,0.5), w U(-1.5,-0.5); grid posterior)
Oms=np.linspace(0.10,0.50,401); Ws=np.linspace(-1.5,-0.5,401)
for br in ['REPLACEMENT','PRIMARY']:
    d,Ci=BR[br]; LP=np.zeros((len(Oms),len(Ws))); best=(1e9,None)
    for i,om in enumerate(Oms):
        for j,w in enumerate(Ws):
            u=u_vec(om,w); A,c2,a=prof_A(u,d,Ci); s=1/np.sqrt(a)
            # exact marginal over A ~ U(20,40): chi2(A)=c2+a(A-Ahat)^2
            mass=0.5*(erf((40-A)/(np.sqrt(2)*s))-erf((20-A)/(np.sqrt(2)*s)))*s
            LP[i,j]=-0.5*c2+np.log(max(mass,1e-300))
            if c2<best[0]: best=(c2,(om,w,A))
    P=np.exp(LP-LP.max()); P/=P.sum(); pw=P.sum(0); cw=np.cumsum(pw)
    q=[float(np.interp(x,cw,Ws)) for x in (0.16,0.5,0.84)]
    po=P.sum(1); co=np.cumsum(po); qo=[float(np.interp(x,co,Oms)) for x in (0.16,0.5,0.84)]
    # refine best fit
    f=lambda t: prof_A(u_vec(t[0],t[1]),d,Ci)[1]
    r=minimize(f,best[1][:2],method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-10))
    O[f'B_BAOonly_noRad_Afree_{br}']={'w_median_68':[q[1],q[0],q[2]],'Om_median_68':[qo[1],qo[0],qo[2]],'bestfit_Om_w':r.x.tolist(),'bestfit_A':float(prof_A(u_vec(*r.x),d,Ci)[0]),'chi2_min':float(r.fun),'grid':'401x401, A marginalised analytically over U(20,40)'}
    print(br,O[f'B_BAOonly_noRad_Afree_{br}'],flush=True)
# ---- B2: BAO-only in the R02 parametrisation (h, omega_b, rd formula, radiation on): A is then effectively free -> should match B0 best fit
for br in ['REPLACEMENT','PRIMARY']:
    f=lambda t: float(chi2([t[0],t[1],t[2],0.0,t[3]],br,use_cmb=False)[0]) if (0.1<t[0]<0.6 and 0.4<t[1]<1 and 0.015<t[3]<0.03) else 1e10
    bb=None
    for s in ([0.30,0.68,-0.97,0.0224],[0.30,0.70,-1.05,0.0222],[0.31,0.66,-0.9,0.0226]):
        r=minimize(f,s,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-11,maxiter=20000,maxfev=20000))
        if bb is None or r.fun<bb.fun: bb=r
    O[f'B_BAOonly_R02param_{br}']={'best_Om_h_w_ob':bb.x.tolist(),'chi2_min':float(bb.fun),'note':'h and omega_b are degenerate with A in BAO-only; only A=c/(H0 rd) is constrained'}
    print(br,'R02param BAO-only',bb.x,bb.fun,flush=True)
# ---- B3: R02 setup (BAO + compressed CMB), best fit -> should reproduce -1.0433 / -1.0487
for br in ['REPLACEMENT','PRIMARY']:
    f=lambda t: float(chi2([t[0],t[1],t[2],0.0,t[3]],br)[0]) if (0.1<t[0]<0.6 and 0.4<t[1]<1 and 0.015<t[3]<0.03) else 1e10
    bb=None
    for s in ([0.317,0.708,-1.04,0.02222],[0.30,0.70,-0.97,0.0224]):
        r=minimize(f,s,method='Nelder-Mead',options=dict(xatol=1e-10,fatol=1e-11,maxiter=20000,maxfev=20000))
        if bb is None or r.fun<bb.fun: bb=r
    O[f'B_BAO+CMB_R02setup_{br}']={'best_Om_h_w_ob':bb.x.tolist(),'chi2_min':float(bb.fun)}
    print(br,'BAO+CMB',bb.x,bb.fun,flush=True)
# ---- B4: radiation on/off in the BF-2 setup (replacement) -> isolates the radiation convention
d,Ci=BR['REPLACEMENT']
f=lambda t: prof_A(u_vec(t[0],t[1],rad=True,h=0.68),d,Ci)[1]
r=minimize(f,[0.30,-0.97],method='Nelder-Mead',options=dict(xatol=1e-9,fatol=1e-10))
O['B_BAOonly_Rad_on_h0.68_REPLACEMENT']={'bestfit_Om_w':r.x.tolist(),'chi2_min':float(r.fun)}
# ---- B5: CMB-only constraint direction: where does the compressed CMB pull w at fixed BAO? (best fit CMB+BAO already in B3)
json.dump(O,open('w_reconcile_r03_output.json','w'),indent=1); print('DONE')
