"""Shared, vectorised R03 model. Same physics as /workspace/desi_r01/fit_cpl.py and R04 (BAO + Planck2018 compressed CMB, Chen+2019;
radiation incl. N_eff=3.046; rd fitting formula with omega_nu=0.00064). Integrals: Gauss-Legendre in ln(1+z) (checked against scipy.quad)."""
import numpy as np
D='/workspace/desi_r01/'; c=299792.458; og=2.469e-5
Z=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=0); dOld=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=1)
Q=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt',usecols=2,dtype=str); cov0=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_cov.txt')
dNew=dOld.copy(); dNew[11]=8.600; dNew[12]=39.32
covNew=cov0.copy(); covNew[11,11]=0.066**2; covNew[12,12]=0.33**2; covNew[11,12]=covNew[12,11]=0.225*0.066*0.33
BR={'PRIMARY':(dOld,np.linalg.inv(cov0)),'REPLACEMENT':(dNew,np.linalg.inv(covNew))}
cm=np.array([1.750235,301.4707,0.02235976]); cs=np.array([0.004644,0.08984,0.0001462])
corr=np.array([[1,0.46,-0.66],[0.46,1,-0.33],[-0.66,-0.33,1]]); cCi=np.linalg.inv(corr*np.outer(cs,cs))
gx,gw=np.polynomial.legendre.leggauss(96)
def E(zz,Om,h,w0,wa,rad=True):
    Or=og/h**2*(1+0.2271*3.046) if rad else 0.0*h; Ode=1-Om-Or
    return np.sqrt(Om*(1+zz)**3+Or*(1+zz)**4+Ode*(1+zz)**(3*(1+w0+wa))*np.exp(-3*wa*zz/(1+zz)))
def DCh(z,Om,h,w0,wa,rad=True):
    """comoving distance * H0/c, integrated in u=ln(1+z); params broadcast as (N,), z scalar or (N,)"""
    U=np.log1p(z); u=(np.asarray(U)[...,None]*(gx+1)/2); zz=np.expm1(u)
    sh=lambda p: np.asarray(p)[...,None]
    f=(1+zz)/E(zz,sh(Om),sh(h),sh(w0),sh(wa),rad)
    return np.asarray(U)*np.sum(gw*f,axis=-1)/2
def rdf(Om,h,ob): return 55.154*np.exp(-72.3*(0.00064+0.0006)**2)/((Om*h*h-0.00064)**0.25351*ob**0.12807)
def zstar(Om,h,ob):
    g1=0.0783*ob**-0.238/(1+39.5*ob**0.763); g2=0.560/(1+21.1*ob**1.81); return 1048*(1+0.00124*ob**-0.738)*(1+g1*(Om*h*h)**g2)
def rs_star(Om,h,w0,wa,ob):
    zs=zstar(Om,h,ob); u0=np.log1p(zs); u1=np.log1p(1e5)
    u=u0[...,None]+(u1-u0)[...,None]*(gx+1)/2; zz=np.expm1(u); sh=lambda p: np.asarray(p)[...,None]
    Rb=31500*sh(ob)*(2.7255/2.7)**-4/(1+zz)
    f=(1+zz)/np.sqrt(3*(1+Rb))/E(zz,sh(Om),sh(h),sh(w0),sh(wa))
    return c/(100*h)*(u1-u0)*np.sum(gw*f,axis=-1)/2
RSMODE='trunc'   # 'trunc' = legacy upper limit z=1e5 (fit_cpl.py L29 bug, kept only to reproduce earlier outputs); 'full' = integral to z=infinity
def rs_star_full(Om,h,w0,wa,ob):
    """sound horizon at z*, integral to infinity: r_s = int_0^{a*} c_s da / (a^2 H), GL in a (smooth: a^2 E -> sqrt(Or))"""
    zs=zstar(Om,h,ob); a1=1/(1+zs); a=a1[...,None]*(gx+1)/2; zz=1/a-1; sh=lambda p: np.asarray(p)[...,None]
    Rb=31500*sh(ob)*(2.7255/2.7)**-4*a
    f=1/np.sqrt(3*(1+Rb))/(a*a*E(zz,sh(Om),sh(h),sh(w0),sh(wa)))
    return c/(100*h)*a1*np.sum(gw*f,axis=-1)/2
def bao(Om,h,w0,wa,ob):
    """(N,13) model vector"""
    Om,h,w0,wa,ob=[np.atleast_1d(np.asarray(x,float)) for x in (Om,h,w0,wa,ob)]
    rd=rdf(Om,h,ob); out=np.empty((len(Om),13))
    for i,(zi,qi) in enumerate(zip(Z,Q)):
        DM=c/(100*h)*DCh(zi,Om,h,w0,wa); DH=c/(100*h*E(zi,Om,h,w0,wa))
        out[:,i]={'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi]/rd
    return out
def cmb(Om,h,w0,wa,ob):
    Om,h,w0,wa,ob=[np.atleast_1d(np.asarray(x,float)) for x in (Om,h,w0,wa,ob)]
    zs=zstar(Om,h,ob); Dz=c/(100*h)*DCh(zs,Om,h,w0,wa)
    rs=rs_star(Om,h,w0,wa,ob) if RSMODE=='trunc' else rs_star_full(Om,h,w0,wa,ob)
    return np.stack([np.sqrt(Om*h*h)*100*Dz/c, np.pi*Dz/rs, ob],axis=1)
def chi2(th,branch,use_cmb=True):
    th=np.atleast_2d(th); Om,h,w0,wa,ob=th.T; d,Ci=BR[branch]
    r=bao(Om,h,w0,wa,ob)-d; x=np.einsum('ni,ij,nj->n',r,Ci,r)
    if use_cmb: s=cmb(Om,h,w0,wa,ob)-cm; x=x+np.einsum('ni,ij,nj->n',s,cCi,s)
    return x
def inprior(th):
    th=np.atleast_2d(th); Om,h,w0,wa,ob=th.T
    return (0.1<Om)&(Om<0.6)&(0.4<h)&(h<1)&(-3<w0)&(w0<1)&(-4<wa)&(wa<2)&(w0+wa<0)&(0.018<ob)&(ob<0.027)
ZG=[0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]
def pred(th,zs=ZG):
    th=np.atleast_2d(th); Om,h,w0,wa,ob=th.T; rd=rdf(Om,h,ob); o={}
    for z in zs:
        DM=c/(100*h)*DCh(z,Om,h,w0,wa)/rd; DH=c/(100*h*E(z,Om,h,w0,wa))/rd; o[z]=(DM,DH,DM/DH)
    return o
