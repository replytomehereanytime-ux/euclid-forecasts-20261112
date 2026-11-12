# Reviewer BAO-only flat LCDM (Om, A) fit + predictive DM/rd, DH/rd at Euclid grid (CTC-1P/1B check). Own code (scipy.quad).
import numpy as np, json, math
from scipy import integrate, optimize
from verify_fits_R02 import Z,Q,branch
def mod(p,zs,qs):
    om,A=p; E=lambda x: math.sqrt(om*(1+x)**3+1-om); o=[]
    for z,q in zip(zs,qs):
        dm=A*integrate.quad(lambda x:1/E(x),0,z,epsrel=1e-12)[0]; dh=A/E(z)
        o.append({'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':(z*dm*dm*dh)**(1/3)}[q])
    return np.array(o)
out={}
for br in ('PRIM','REPL'):
    y,Ci=branch(br); f=lambda p:float((mod(p,Z,Q)-y)@Ci@(mod(p,Z,Q)-y))
    r=optimize.minimize(f,[0.3,29.5],method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-12,'maxiter':5000}); p=r.x
    h=np.array([1e-4,1e-3]); H=np.zeros((2,2))
    for i in range(2):
        for j in range(2):
            ei=np.eye(2)[i]*h[i]; ej=np.eye(2)[j]*h[j]; H[i,j]=(f(p+ei+ej)-f(p+ei-ej)-f(p-ei+ej)+f(p-ei-ej))/(4*h[i]*h[j])
    Cp=2*np.linalg.inv(H); zz=[z for z in (0.9,1.2,1.5,1.8) for _ in (0,1)]; qq=['DM_over_rs','DH_over_rs']*4
    g=lambda p: mod(p,zz,qq); J=np.array([(g(p+np.eye(2)[i]*h[i])-g(p-np.eye(2)[i]*h[i]))/(2*h[i]) for i in range(2)]).T
    Pc=J@Cp@J.T
    out[br]={'chi2':r.fun,'Om':p[0],'A':p[1],'sig':np.sqrt(np.diag(Cp)).tolist(),'pred':g(p).tolist(),'pred_sig':np.sqrt(np.diag(Pc)).tolist()}
    print(br,round(r.fun,5),np.round(p,5),np.round(np.sqrt(np.diag(Cp)),5),np.round(g(p),4).tolist(),np.round(np.sqrt(np.diag(Pc)),4).tolist())
json.dump(out,open('verify_baoonly_pred_R02_output.json','w'),indent=1)
