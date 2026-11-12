"""REV3 model. Derived from R03/calc/cplmodel_r03.py (frozen copy untouched).
Changes: (1) compressed-CMB conventions of Chen, Huang & Wang 2019 (arXiv:1808.05724):
  Omega_r = Omega_m/(1+z_eq), z_eq = 2.5e4 * Omega_m h^2 * (T/2.7)^-4  (used in CMB distance + r_s(z*) integrals)
  z* handled per CMBMODE; (2) optional curvature Ok (oLCDM) via sinn(); (3) r_s integral to infinity (RSMODE full).
CMBMODE: 'old'      = R03 behaviour (Hu-Sugiyama z*, photon+3.046 nu radiation) -> reproduces failing control
         'chen_zfix'= Chen radiation, z* = 1089.9 fixed (Planck 2018 chain value)
         'chen_zHS' = Chen radiation, Hu-Sugiyama z* (parameter dependent)
         'rescale'  = 'old' with l_A multiplied by LA_SCALE (fallback, 0.997452)."""
import numpy as np, sys
sys.path.insert(0,'.'); import cplmodel_r03 as M0
c=M0.c; og=M0.og; T=2.7255; gx,gw=M0.gx,M0.gw
Z,Q,BR,cm,cs,cCi,rdf,zstar_HS=M0.Z,M0.Q,M0.BR,M0.cm,M0.cs,M0.cCi,M0.rdf,M0.zstar
CMBMODE='chen_zfix'; ZSTAR_FIX=1089.9; LA_SCALE=0.997452
def Orh2(Om,h,mode):
    if mode in ('chen_zfix','chen_zHS'):
        wm=Om*h*h; zeq=2.5e4*wm*(T/2.7)**-4; return wm/(1+zeq)
    return og*(1+0.2271*3.046)+0*Om
def E(zz,Om,h,w0,wa,Ok=0.0,orh2=None):
    Or=(og*(1+0.2271*3.046) if orh2 is None else orh2)/h**2; Ode=1-Om-Or-Ok
    return np.sqrt(Om*(1+zz)**3+Or*(1+zz)**4+Ok*(1+zz)**2+Ode*(1+zz)**(3*(1+w0+wa))*np.exp(-3*wa*zz/(1+zz)))
sh=lambda p: np.asarray(p)[...,None]
def DC(z,Om,h,w0,wa,Ok=0.0,orh2=None):
    """line-of-sight comoving distance * H0/c"""
    U=np.log1p(z); u=np.asarray(U)[...,None]*(gx+1)/2; zz=np.expm1(u)
    f=(1+zz)/E(zz,sh(Om),sh(h),sh(w0),sh(wa),sh(Ok),None if orh2 is None else sh(orh2))
    return np.asarray(U)*np.sum(gw*f,axis=-1)/2
def DMt(dc,Ok):
    Ok=np.asarray(Ok,float); s=np.sqrt(np.abs(Ok))+1e-300
    return np.where(Ok>1e-12,np.sinh(s*dc)/s,np.where(Ok<-1e-12,np.sin(s*dc)/s,dc))
def zstar(Om,h,ob,mode):
    if mode=='chen_zfix': return np.full(np.shape(Om),ZSTAR_FIX,float)
    return zstar_HS(Om,h,ob)
def rs_star(Om,h,w0,wa,ob,Ok,zs,orh2):
    a1=1/(1+zs); a=sh(a1)*(gx+1)/2; zz=1/a-1
    Rb=31500*sh(ob)*(T/2.7)**-4*a
    f=1/np.sqrt(3*(1+Rb))/(a*a*E(zz,sh(Om),sh(h),sh(w0),sh(wa),sh(Ok),None if orh2 is None else sh(orh2)))
    return c/(100*h)*a1*np.sum(gw*f,axis=-1)/2
def cmb(Om,h,w0,wa,ob,Ok=0.0,mode=None):
    mode=mode or CMBMODE
    Om,h,w0,wa,ob,Ok=[np.atleast_1d(np.asarray(x,float))*np.ones(np.size(Om)) for x in (Om,h,w0,wa,ob,Ok)]
    zs=zstar(Om,h,ob,mode); orh2=Orh2(Om,h,mode)
    DMs=c/(100*h)*DMt(DC(zs,Om,h,w0,wa,Ok,orh2),Ok)
    rs=rs_star(Om,h,w0,wa,ob,Ok,zs,orh2)
    lA=np.pi*DMs/rs
    if mode=='rescale': lA=lA*LA_SCALE
    return np.stack([np.sqrt(Om*h*h)*100*DMs/c, lA, ob],axis=1)
def dist(z,Om,h,w0,wa,ob,Ok=0.0):
    Om,h,w0,wa,ob,Ok=[np.atleast_1d(np.asarray(x,float))*np.ones(np.size(Om)) for x in (Om,h,w0,wa,ob,Ok)]
    rd=rdf(Om,h,ob); DM=c/(100*h)*DMt(DC(z,Om,h,w0,wa,Ok),Ok); DH=c/(100*h*E(z,Om,h,w0,wa,Ok))
    return DM/rd,DH/rd
def bao(Om,h,w0,wa,ob,Ok=0.0):
    Om=np.atleast_1d(np.asarray(Om,float)); out=np.empty((len(Om),13))
    for i,(zi,qi) in enumerate(zip(Z,Q)):
        DM,DH=dist(zi,Om,h,w0,wa,ob,Ok)
        out[:,i]={'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi]
    return out
def chi2(th,branch,use_bao=True,use_cmb=True):
    """th columns: Om,h,w0,wa,ob[,Ok]"""
    th=np.atleast_2d(th); Om,h,w0,wa,ob=th[:,:5].T; Ok=th[:,5] if th.shape[1]>5 else 0*Om
    x=np.zeros(len(Om))
    if use_bao:
        d,Ci=BR[branch]; r=bao(Om,h,w0,wa,ob,Ok)-d; x=x+np.einsum('ni,ij,nj->n',r,Ci,r)
    if use_cmb:
        s=cmb(Om,h,w0,wa,ob,Ok)-cm; x=x+np.einsum('ni,ij,nj->n',s,cCi,s)
    return x
def inprior(th):
    th=np.atleast_2d(th); Om,h,w0,wa,ob=th[:,:5].T; Ok=th[:,5] if th.shape[1]>5 else 0*Om
    return (0.1<Om)&(Om<0.6)&(0.4<h)&(h<1)&(-3<w0)&(w0<1)&(-4<wa)&(wa<2)&(w0+wa<0)&(0.018<ob)&(ob<0.027)&(-0.3<Ok)&(Ok<0.3)
