"""Constant-w BAO-only free-A on the July Table-4 replacement input (and the box cov file): posterior mean/SD of w, to tie Task B to the author's audit. Grid 241x241 in (Om,w), A analytic over U(20,40)."""
import numpy as np, json, sys; sys.path.insert(0,'.'); sys.path.insert(0,'../calc')
import freeA_lcdm_table4_old_inc as T  # builds T4 data (runs that module's main block: OK, deterministic)
from scipy.special import erf
F=T.F; gx,gw=F.gx,F.gw
def u_shape(om,w):
    out=[]
    for z,q in zip(F.Z,F.Q):
        U=np.log1p(z); zz=np.expm1(U*(gx+1)/2); E=lambda x: np.sqrt(om[:,None]*(1+x)**3+(1-om[:,None])*(1+x)**(3*(1+w)))
        dm=U/2*np.sum(gw*(1+zz)/E(zz),axis=1); dh=1/np.sqrt(om*(1+z)**3+(1-om)*(1+z)**(3*(1+w)))
        out.append({'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':(z*dm*dm*dh)**(1/3)}[q])
    return np.array(out).T
O={}
for lab,(d,Ci) in [('T4_NEW(July replacement)',F.BR['T4_NEW']),('T4_OLD',F.BR['T4_OLD']),('boxcov_REPLACEMENT',F.BR['REPLACEMENT'])]:
    oms=np.linspace(0.1,0.5,481); ws=np.linspace(-1.5,-0.5,481); LP=np.zeros((481,481))
    for j,w in enumerate(ws):
        u=u_shape(oms,w); a=np.einsum('ni,ij,nj->n',u,Ci,u); b=u@Ci@d; Ah=b/a; c2=d@Ci@d-b*b/a; s=1/np.sqrt(a)
        mass=0.5*(erf((40-Ah)/(np.sqrt(2)*s))-erf((20-Ah)/(np.sqrt(2)*s)))*s; LP[:,j]=-0.5*c2+np.log(mass)
    P=np.exp(LP-LP.max()); P/=P.sum(); pw=P.sum(0); m=(pw*ws).sum(); sd=np.sqrt((pw*(ws-m)**2).sum()); cw=np.cumsum(pw)
    O[lab]={'w_mean':float(m),'w_sd':float(sd),'w_median':float(np.interp(0.5,cw,ws))}
    print(lab,O[lab],flush=True)
json.dump(O,open('wcdm_table4_inc_output.json','w'),indent=1)
