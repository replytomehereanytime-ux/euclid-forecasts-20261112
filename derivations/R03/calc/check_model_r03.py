import numpy as np, json, sys; sys.path.insert(0,'.'); from cplmodel_r03 import *
from scipy.integrate import quad
# compare vectorised integrals with scipy.quad (same formulae as fit_cpl.py)
out={}
for th in [(0.3425,0.6840,-0.767,-0.824,0.02215),(0.32428,0.69846,-1,0,0.022279),(0.30,0.70,-0.4,-2.5,0.0224)]:
    Om,h,w0,wa,ob=th
    dq=lambda zz: c/(100*h)*quad(lambda x:1/E(x,Om,h,w0,wa),0,zz,limit=200,epsrel=1e-12)[0]
    zs=zstar(Om,h,ob); rq=quad(lambda zz:c/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4/(1+zz)))/(100*h*E(zz,Om,h,w0,wa)),zs,1e5,limit=400,epsrel=1e-12)[0]
    rel=[abs(c/(100*h)*float(DCh(z,Om,h,w0,wa))/dq(z)-1) for z in [0.3,0.9,1.8,2.33]]+[abs(c/(100*h)*float(DCh(zs,Om,h,w0,wa))/dq(zs)-1), abs(float(rs_star(np.atleast_1d(Om),np.atleast_1d(h),w0,wa,np.atleast_1d(ob))[0])/rq-1)]
    out[str(th)]=max(rel)
print(json.dumps(out,indent=1)); assert max(out.values())<1e-7
# reproduce R04 chi2 at R04 CPL best fits
print('chi2 R04 CPL best (replacement) ->',chi2([0.3425,0.6840,-0.767,-0.824,0.02215],'REPLACEMENT'), ' (R04: 26.9397, rounded params)')
print('chi2 R04 LCDM best (replacement) ->',chi2([0.32428051560186677,0.6984599622041885,-1,0,0.022279281807078617],'REPLACEMENT'),' (R04/R02: 29.12778)')
print('chi2 R02 LCDM best (primary) ->',chi2([0.3239712387770484,0.6986764715110352,-1,0,0.022280652121375474],'PRIMARY'),' (R02: 26.21434)')
