import sys,json; sys.path.insert(0,'.'); import numpy as np, model_rev3 as M
from scipy.optimize import minimize
Om,h,ob=0.3166,0.6727,0.02236; out={}
for mode in ['old','chen_zHS','chen_zfix','rescale']:
    M.CMBMODE=mode; v=M.cmb(Om,h,-1,0,ob)[0]
    f=lambda q: float(M.chi2([q[0],q[1],-1,0,q[2]],'REPLACEMENT',use_bao=False)[0])
    r=minimize(f,[0.31,0.68,0.0224],method='Nelder-Mead',options=dict(xatol=1e-12,fatol=1e-14,maxiter=20000))
    r=minimize(f,r.x,method='Nelder-Mead',options=dict(xatol=1e-13,fatol=1e-15,maxiter=20000))
    H0=100*r.x[1]; wm=r.x[0]*r.x[1]**2
    ok=abs(v[1]-301.4707)<0.02 and abs(H0-67.27)<0.12 and abs(wm-0.1432)<0.00026
    out[mode]={'R':v[0],'lA':v[1],'prior_only_fit':{'Om':r.x[0],'h':r.x[1],'ob':r.x[2],'H0':H0,'omh2':wm,'chi2':r.fun},'PASS':bool(ok)}
    print(f"{mode:10s} lA={v[1]:.4f} R={v[0]:.5f} | prior-only: H0={H0:.3f} Om={r.x[0]:.4f} omh2={wm:.5f} chi2={r.fun:.2e} -> {'PASS' if ok else 'FAIL'}")
out['tolerance']='|lA-301.4707|<0.02 (0.22 prior sd), |H0-67.27|<0.12, |omh2-0.1432|<0.00026 (about 0.2 Planck 2018 sd each)'
json.dump(out,open('control_rev3.json','w'),indent=1)
