"""INCREMENT 8929251 (a)/(b): free-A flat LCDM (no radiation) from the author's stated equations. rs3env numpy. Grid posterior, priors Om U(0.1,0.5), A U(20,40)."""
import numpy as np, json, sys; sys.path.insert(0,'../calc'); from cplmodel_r03 import Z,Q,BR,DCh,E
gx,gw=np.polynomial.legendre.leggauss(96)
def Ef(z,om): return np.sqrt(om*(1+z)**3+1-om)
def I(z,om):  # int_0^z du/E, GL in ln(1+z) ; om array
    U=np.log1p(z); zz=np.expm1(U*(gx+1)/2); return U/2*np.sum(gw*(1+zz)/Ef(zz,om[:,None]),axis=1)
def u_shape(om):
    out=np.empty((len(om),13))
    for i,(z,q) in enumerate(zip(Z,Q)):
        dm=I(z,om); dh=1/Ef(z,om); out[:,i]={'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':(z*dm*dm*dh)**(1/3)}[q]
    return out
ZH=[0.9,1.0,1.2,1.5,1.8]
def post(branch,n_om=4001,n_A=4001):
    d,Ci=BR[branch]; om=np.linspace(0.1,0.5,n_om); A=np.linspace(20,40,n_A); u=u_shape(om)
    a=np.einsum('ni,ij,nj->n',u,Ci,u); b=u@Ci@d; c0=d@Ci@d
    chi=c0-2*np.outer(b,A)+np.outer(a,A**2); L=np.exp(-0.5*(chi-chi.min())); L/=L.sum()
    pO=L.sum(1); pA=L.sum(0)
    mo=(pO*om).sum(); mA=(pA*A).sum(); so=np.sqrt((pO*(om-mo)**2).sum()); sA=np.sqrt((pA*(A-mA)**2).sum())
    cOA=(L*np.outer(om-mo,A-mA)).sum()
    # latent geometry: DM/rd=A*I, DH/rd=A/E ; integrated posterior moments using factorisation over grid
    rows={}; lat=[]; 
    EA=(pA*A).sum()  # not separable in general; do full 2D
    for z in ZH:
        Iz=I(z,om); Ez=Ef(z,om)
        DM=np.outer(Iz,A); DH=np.outer(1/Ez,A); F=np.outer(Iz*Ez,np.ones_like(A))
        st=lambda X: (float((L*X).sum()), float(np.sqrt((L*(X-(L*X).sum())**2).sum())))
        def med(X):
            x=X.ravel(); w=L.ravel(); i=np.argsort(x); cw=np.cumsum(w[i]); return float(np.interp(0.5,cw,x[i]))
        at_mean=(mA*float(I(z,np.array([mo]))[0]), mA/float(Ef(z,mo)), float(I(z,np.array([mo]))[0]*Ef(z,mo)))
        rows[z]={'post_mean_sd':{'DM/rd':st(DM),'DH/rd':st(DH),'F_AP':st(F)},'post_median':{'DM/rd':med(DM),'DH/rd':med(DH),'F_AP':med(F)},'at_mean_params':dict(zip(['DM/rd','DH/rd','F_AP'],at_mean))}
        lat+=[DM,DH,F]
    # full 15x15 parameter-only latent covariance (shared across rows)
    M=np.array([(L*X).sum() for X in lat]); Cl=np.array([[(L*(X-M[i])*(Y-M[j])).sum() for j,Y in enumerate(lat)] for i,X in enumerate(lat)])
    return {'branch':branch,'grid':[n_om,n_A],'Om_mean_sd':[mo,so],'A_mean_sd':[mA,sA],'cov_Om_A':cOA,'chi2_min':float(chi.min()),'rows':rows,
            'latent_order':[f'{q}@{z}' for z in ZH for q in ('DM/rd','DH/rd','F_AP')],'latent_mean':M.tolist(),'latent_cov':Cl.tolist(),'latent_cov_eig':np.linalg.eigvalsh(Cl).tolist()}
if __name__=='__main__':
  O={'REPLACEMENT':post('REPLACEMENT'),'PRIMARY':post('PRIMARY')}
  # resolution check
  O['res_check_REPLACEMENT_2001']={k:v for k,v in post('REPLACEMENT',2001,2001).items() if k in ('Om_mean_sd','A_mean_sd')}
  json.dump(O,open('freeA_lcdm_inc_output.json','w'),indent=1)
  for br in ['REPLACEMENT','PRIMARY']:
      o=O[br]; print(br,'Om',o['Om_mean_sd'],'A',o['A_mean_sd'],'chi2min',o['chi2_min'])
      for z in ZH:
          r=o['rows'][z]; print(' ',z,{k:[round(x,5) for x in v] for k,v in r['post_mean_sd'].items()}, {k:round(v,5) for k,v in r['post_median'].items()}, {k:round(v,5) for k,v in r['at_mean_params'].items()})
  print(O['res_check_REPLACEMENT_2001'])
