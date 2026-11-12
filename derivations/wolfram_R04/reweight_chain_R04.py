"""Importance-reweight the existing box emcee chains (old Lya, /workspace/desi_r01/chain_*.npy) to the corrected Lya z=2.33 point.
Only the Lya block of the likelihood changes, so w = exp(-0.5*(chi2_lya_new - chi2_lya_old)). numpy only (Gauss-Legendre, 64 nodes)."""
import numpy as np, json
c=299792.458; og=2.469e-5
gx,gw=np.polynomial.legendre.leggauss(64); gx=(gx+1)/2; gw=gw/2
def E(z,Om,h,w0,wa):
    Or=og/h**2*(1+0.2271*3.046); return np.sqrt(Om*(1+z)**3+Or*(1+z)**4+(1-Om-Or)*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z)))
def DC(z,Om,h,w0,wa):
    zz=z*gx[:,None]; return c/(100*h)*z*np.sum(gw[:,None]/E(zz,Om,h,w0,wa),axis=0)
def rd(Om,h,ob): return 55.154*np.exp(-72.3*(0.00064+0.0006)**2)/((Om*h*h-0.00064)**0.25351*ob**0.12807)
def obs(z,Om,h,w0,wa,ob):
    r=rd(Om,h,ob); DM=DC(z,Om,h,w0,wa); DH=c/(100*h*E(z,Om,h,w0,wa)); return DM/r,DH/r
cov_old=np.array([[1.02136194e-02,-2.31395216e-02],[-2.31395216e-02,2.82685779e-01]]); m_old=np.array([8.631545674846294,38.988973961958784])
cov_new=np.array([[0.066**2,0.225*0.066*0.33],[0.225*0.066*0.33,0.33**2]]); m_new=np.array([8.600,39.32])
def c2(DH,DM,m,C):
    r=np.vstack([DH-m[0],DM-m[1]]); Ci=np.linalg.inv(C); return np.einsum('in,ij,jn->n',r,Ci,r)
out={}
for name in ['w0waCDM','LCDM']:
    ch=np.load(f'/workspace/desi_r01/chain_{name}.npy')
    if name=='LCDM': Om,h,ob=ch.T; w0=-np.ones_like(Om); wa=np.zeros_like(Om)
    else: Om,h,w0,wa,ob=ch.T
    DM,DH=obs(2.33,Om,h,w0,wa,ob)
    lw=-0.5*(c2(DH,DM,m_new,cov_new)-c2(DH,DM,m_old,cov_old)); w=np.exp(lw-lw.max()); w/=w.sum()
    ess=1/np.sum(w**2)
    def wq(x,qs=(0.16,0.5,0.84,0.025,0.975)):
        i=np.argsort(x); cw=np.cumsum(w[i]); return [float(np.interp(q,cw,x[i])) for q in qs]
    res={'N':len(w),'ESS':float(ess)}
    for n,x in [('Om',Om),('h',h),('w0',w0),('wa',wa),('ob',ob)]:
        res[n+'_mean']=float(np.sum(w*x)); res[n+'_std']=float(np.sqrt(np.sum(w*(x-np.sum(w*x))**2)))
    if name=='w0waCDM':
        res['P(w0>-1)_new']=float(np.sum(w[w0>-1])); res['P(w0>-1)_old_unweighted']=float(np.mean(w0>-1))
        res['P(w0>-1 & wa<0)_new']=float(np.sum(w[(w0>-1)&(wa<0)]))
        res['corr_w0wa']=float(np.sum(w*(w0-res['w0_mean'])*(wa-res['wa_mean']))/(res['w0_std']*res['wa_std']))
    pz={}
    for z in [0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8]:
        a,b=obs(z,Om,h,w0,wa,ob); pz[z]={'DM/rd [16,50,84,2.5,97.5]':wq(a),'DH/rd [16,50,84,2.5,97.5]':wq(b),'DM/DH [16,50,84,2.5,97.5]':wq(a/b)}
    res['pred']=pz; out[name]=res
json.dump(out,open('reweight_chain_R04_output.json','w'),indent=1); print(json.dumps({k:{kk:vv for kk,vv in v.items() if kk!='pred'} for k,v in out.items()},indent=1))
print(json.dumps({k:v['pred'][1.3] for k,v in out.items()},indent=1))
