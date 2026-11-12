"""Blank-context second check (scipy, independent code path) of the Wolfram R04 fit. Same physical model as /workspace/desi_r01/fit_cpl.py."""
import numpy as np, json
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.stats import chi2 as C2, norm
D='/workspace/desi_r01/'
c=299792.458; og=2.469e-5
z=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=0); dOld=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=1)
q=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=2,dtype=str); cov0=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_cov.txt')
dNew=dOld.copy(); dNew[11]=8.600; dNew[12]=39.32
covNew=cov0.copy(); covNew[11,11]=0.066**2; covNew[12,12]=0.33**2; covNew[11,12]=covNew[12,11]=0.225*0.066*0.33
cm=np.array([1.750235,301.4707,0.02235976]); cs=np.array([0.004644,0.08984,0.0001462])
corr=np.array([[1,0.46,-0.66],[0.46,1,-0.33],[-0.66,-0.33,1]]); cCi=np.linalg.inv(corr*np.outer(cs,cs))
def E(zz,Om,h,w0,wa):
    Or=og/h**2*(1+0.2271*3.046); Ode=1-Om-Or
    return np.sqrt(Om*(1+zz)**3+Or*(1+zz)**4+Ode*(1+zz)**(3*(1+w0+wa))*np.exp(-3*wa*zz/(1+zz)))
def DC(zz,p): return c/(100*p[1])*quad(lambda x:1/E(x,*p),0,zz,limit=200,epsrel=1e-10)[0]
def rdf(Om,h,ob): return 55.154*np.exp(-72.3*(0.00064+0.0006)**2)/((Om*h*h-0.00064)**0.25351*ob**0.12807)
def model(th):
    Om,h,w0,wa,ob=th; p=(Om,h,w0,wa); rd=rdf(Om,h,ob); out=[]
    for zi,qi in zip(z,q):
        DM=DC(zi,p); DH=c/(100*h*E(zi,*p)); out.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi]/rd)
    g1=0.0783*ob**-0.238/(1+39.5*ob**0.763); g2=0.560/(1+21.1*ob**1.81); om=Om*h*h
    zs=1048*(1+0.00124*ob**-0.738)*(1+g1*om**g2); Dz=DC(zs,p)
    Rb=lambda zz:31500*ob*(2.7255/2.7)**-4/(1+zz)
    rs=quad(lambda zz:c/np.sqrt(3*(1+Rb(zz)))/(100*h*E(zz,*p)),zs,1e5,limit=200,epsrel=1e-10)[0]
    return np.array(out),np.array([np.sqrt(om)*100*Dz/c,np.pi*Dz/rs,ob])
def chi2(th,d,Ci):
    Om,h,w0,wa,ob=th
    if not(0.1<Om<0.6 and 0.4<h<1 and ob>0.015): return 1e10
    m,cmb=model(th); r=m-d; s=cmb-cm; return float(r@Ci@r+s@cCi@s)
def fit(d,cv):
    Ci=np.linalg.inv(cv)
    l=minimize(lambda t:chi2([t[0],t[1],-1,0,t[2]],d,Ci),[0.31,0.68,0.0224],method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-7,maxiter=4000))
    best=None
    for s in ([0.345,0.683,-0.72,-1.0,0.02215],[0.31,0.68,-0.9,-0.3,0.0224],[0.33,0.67,-0.6,-1.4,0.0222]):
        w=minimize(lambda t:chi2(t,d,Ci),s,method='Nelder-Mead',options=dict(xatol=1e-7,fatol=1e-7,maxiter=8000,maxfev=8000))
        if best is None or w.fun<best.fun: best=w
    d2=l.fun-best.fun; p=C2.sf(d2,2)
    return dict(LCDM_chi2=l.fun,LCDM_best=list(l.x),CPL_chi2=best.fun,CPL_best=list(best.x),dchi2=d2,p=p,sigma=float(norm.isf(p/2)))
res={'old_lya':fit(dOld,cov0),'new_lya':fit(dNew,covNew)}
# predictions at Euclid z for best fits (new Lya)
def pred(th,zz):
    Om,h,w0,wa,ob=th; p=(Om,h,w0,wa); rd=rdf(Om,h,ob); DM=DC(zz,p); DH=c/(100*h*E(zz,*p)); return [DM/rd,DH/rd,(zz*DM*DM*DH)**(1/3)/rd,DM/DH]
L=res['new_lya']['LCDM_best']; W=res['new_lya']['CPL_best']
res['pred_new_LCDM']={zz:pred([L[0],L[1],-1,0,L[2]],zz) for zz in [0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]}
res['pred_new_CPL']={zz:pred(W,zz) for zz in [0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]}
json.dump(res,open('crosscheck_scipy_R04_output.json','w'),indent=1,default=float); print(json.dumps(res,indent=1,default=float))
