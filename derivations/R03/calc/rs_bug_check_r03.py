"""Confirm the r_s(z*) truncation bug (fit_cpl.py L29: quad(..., zs, 1e5)) and validate the R03 full integral."""
import numpy as np, json, sys; sys.path.insert(0,'.'); import cplmodel_r03 as M
from scipy.integrate import quad
O={}
for lab,th in [('R02_LCDM_PRIMARY_best',(0.3239712387770484,0.6986764715110352,-1,0,0.022280652121375474)),('Coordinator_corrected',(0.3039,0.6856,-1,0,0.02237)),('Planck18',(0.3153,0.6736,-1,0,0.02237))]:
    Om,h,w0,wa,ob=th; zs=float(M.zstar(Om,h,ob))
    f=lambda zz: M.c/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4/(1+zz)))/(100*h*float(M.E(zz,Om,h,w0,wa)))
    tr=quad(f,zs,1e5,limit=400,epsrel=1e-12)[0]
    fa=lambda a: M.c/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4*a))/(a*a*100*h*float(M.E(1/a-1,Om,h,w0,wa)))
    full=quad(fa,0,1/(1+zs),limit=400,epsrel=1e-12)[0]
    tail=quad(f,1e5,np.inf,limit=400,epsrel=1e-10)[0]
    gl_tr=float(M.rs_star(np.atleast_1d(Om),np.atleast_1d(h),w0,wa,np.atleast_1d(ob))[0]); gl_full=float(M.rs_star_full(np.atleast_1d(Om),np.atleast_1d(h),w0,wa,np.atleast_1d(ob))[0])
    for zmax in (1e5,1e6,1e7,1e8): O.setdefault(lab,{}).setdefault('convergence',{})[f'{zmax:.0e}']=quad(f,zs,zmax,limit=800,epsrel=1e-12)[0]
    O[lab].update({'z_star':zs,'rs_trunc_1e5':tr,'rs_full':full,'tail_1e5_inf':tail,'rel_shortfall':tr/full-1,'GL_trunc':gl_tr,'GL_full':gl_full,'GL_full_vs_quad':gl_full/full-1})
    print(lab,{k:v for k,v in O[lab].items()})
json.dump(O,open('rs_bug_check_r03_output.json','w'),indent=1)
