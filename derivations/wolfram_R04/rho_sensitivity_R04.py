"""Sensitivity of the corrected-Lya Delta chi2 to the UNVERIFIED DM-DH correlation rho (scipy, reuses crosscheck model)."""
import json, numpy as np, importlib.util, sys
src=open('crosscheck_scipy_R04.py').read().split("res={'old_lya'")[0]
exec(src)
out={}
for rho in [0.0,-0.43,0.5]:
    cv=covNew.copy(); cv[11,12]=cv[12,11]=rho*0.066*0.33
    r=fit(dNew,cv); out[str(rho)]={k:r[k] for k in ['LCDM_chi2','CPL_chi2','dchi2','sigma','CPL_best']}
json.dump(out,open('rho_sensitivity_R04_output.json','w'),indent=1,default=float); print(json.dumps(out,indent=1,default=float))
