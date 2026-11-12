# Independent re-derivation (Grok Bot reviewer, 2026-11-12) of R02 Forecast Bot fits.
# Own code: numpy/scipy; distances by numpy Gauss-Legendre in ln(1+z) (vectorised) cross-checked against scipy.quad.
# Public inputs: DESI DR2 BAO mean/cov (/workspace/desi_r01), Results IV v3 Eq.26 Lya replacement, Planck2018 compressed
# CMB (Chen, Huang & Wang 2019, arXiv:1808.05724: R, l_A, omega_b), Aubourg+2015 r_d fitting formula, Hu&Sugiyama z*.
import numpy as np, json, math, sys, time
from scipy import optimize, integrate, stats
C=299792.458; OG=2.469e-5; NEFF=3.046
D='/workspace/desi_r01/'
rows=[l.split() for l in open(D+'desi_gaussian_bao_ALL_GCcomb_mean.txt') if l.strip() and not l.startswith('#')]
Z=np.array([float(r[0]) for r in rows]); Y0=np.array([float(r[1]) for r in rows]); Q=[r[2] for r in rows]
C0=np.loadtxt(D+'desi_gaussian_bao_ALL_GCcomb_cov.txt')
iH=[i for i in range(13) if abs(Z[i]-2.33)<1e-6 and Q[i]=='DH_over_rs'][0]; iM=[i for i in range(13) if abs(Z[i]-2.33)<1e-6 and Q[i]=='DM_over_rs'][0]
def branch(name):
    y=Y0.copy(); c=C0.copy()
    if name=='REPL':
        y[iH]=8.600; y[iM]=39.32; c[iH,iH]=0.066**2; c[iM,iM]=0.33**2; c[iH,iM]=c[iM,iH]=0.225*0.066*0.33
    return y, np.linalg.inv(c)
CM=np.array([1.750235,301.4707,0.02235976]); CS=np.array([0.004644,0.08984,0.0001462])
CORR=np.array([[1,0.46,-0.66],[0.46,1,-0.33],[-0.66,-0.33,1]]); CCI=np.linalg.inv(CORR*np.outer(CS,CS))
xg,wg=np.polynomial.legendre.leggauss(96)
def E(z,om,ok,h,w0,wa):
    orr=OG/h**2*(1+0.2271*NEFF); ode=1-om-orr-ok
    return np.sqrt(om*(1+z)**3+orr*(1+z)**4+ok*(1+z)**2+ode*(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z)))
def chi_int(z,p,quad=False):
    om,ok,h,w0,wa=p[:5]
    if quad: return integrate.quad(lambda x:1/E(x,om,ok,h,w0,wa),0,z,epsabs=0,epsrel=1e-11,limit=400)[0]
    b=math.log1p(z); u=0.5*b*(xg+1); return 0.5*b*np.sum(wg*np.exp(u)/E(np.expm1(u),om,ok,h,w0,wa))
def DM(z,p,quad=False):
    om,ok,h=p[:3]; x=chi_int(z,p,quad); dh0=C/(100*h)
    if abs(ok)<1e-12: return dh0*x
    s=math.sqrt(abs(ok)); return dh0*(math.sinh(s*x)/s if ok>0 else math.sin(s*x)/s)
def rd(om,h,ob): return 55.154*math.exp(-72.3*(0.00064+0.0006)**2)/((om*h*h-0.00064)**0.25351*ob**0.12807)
def zstar(omh,ob):
    g1=0.0783*ob**-0.238/(1+39.5*ob**0.763); g2=0.560/(1+21.1*ob**1.81); return 1048*(1+0.00124*ob**-0.738)*(1+g1*omh**g2)
def rs_star(p,ob,zs,quad=False):
    om,ok,h,w0,wa=p[:5]
    f=lambda z: C/math.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4/(1+z)))/(100*h*E(z,om,ok,h,w0,wa))
    if quad: return integrate.quad(f,zs,1e5,epsrel=1e-10,limit=400)[0]
    a,b=math.log1p(zs),math.log1p(1e5); u=0.5*(b-a)*(xg+1)+a; z=np.expm1(u)
    cs=C/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4/(1+z))); return 0.5*(b-a)*np.sum(wg*np.exp(u)*cs/(100*h*E(z,om,ok,h,w0,wa)))
def bao_model(p,ob,quad=False):
    r=rd(p[0],p[2],ob); out=[]; cache={}
    for z,q in zip(Z,Q):
        if z not in cache: cache[z]=DM(z,p,quad)
        dm=cache[z]; dh=C/(100*p[2]*E(z,*p[:5]))
        out.append({'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':(z*dm*dm*dh)**(1/3)}[q]/r)
    return np.array(out)
def cmb_model(p,ob,quad=False):
    omh=p[0]*p[2]**2; zs=zstar(omh,ob); dmz=DM(zs,p,quad)
    return np.array([math.sqrt(omh)*100*dmz/C, math.pi*dmz/rs_star(p,ob,zs,quad), ob])
MAPS={'LCDM':lambda q:([q[0],0,q[1],-1,0],q[2]),'wCDM':lambda q:([q[0],0,q[1],q[2],0],q[3]),
      'oLCDM':lambda q:([q[0],q[1],q[2],-1,0],q[3]),'CPL':lambda q:([q[0],0,q[1],q[2],q[3]],q[4])}
START={'LCDM':[0.32,0.69,0.0224],'wCDM':[0.32,0.69,-1.0,0.0224],'oLCDM':[0.32,0.0,0.69,0.0224],'CPL':[0.32,0.68,-0.8,-0.8,0.0224]}
def inprior(p,ob): return 0.1<p[0]<0.6 and -0.3<p[1]<0.3 and 0.4<p[2]<1 and 0.015<ob<0.03 and -3<p[3]<1 and -5<p[4]<3
def chi2(q,model,y,Ci,quad=False):
    p,ob=MAPS[model](q)
    if not inprior(p,ob): return 1e10
    r=bao_model(p,ob,quad)-y; s=cmb_model(p,ob,quad)-CM; return float(r@Ci@r+s@CCI@s)
def hessian(f,x,h):
    n=len(x); H=np.zeros((n,n))
    for i in range(n):
        for j in range(i,n):
            ei=np.eye(n)[i]*h[i]; ej=np.eye(n)[j]*h[j]
            H[i,j]=H[j,i]=(f(x+ei+ej)-f(x+ei-ej)-f(x-ei+ej)+f(x-ei-ej))/(4*h[i]*h[j])
    return H
ZE=[0.9,1.2,1.5,1.8]
def predvec(q,model):
    p,ob=MAPS[model](q); r=rd(p[0],p[2],ob); v=[]
    for z in ZE: v+= [DM(z,p)/r, C/(100*p[2]*E(z,*p[:5]))/r]
    return np.array(v)
def fit(model,br):
    y,Ci=branch(br); f=lambda q:chi2(np.asarray(q),model,y,Ci)
    res=optimize.minimize(f,START[model],method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-10,'maxiter':40000,'maxfev':40000})
    res=optimize.minimize(f,res.x,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-11,'maxiter':40000,'maxfev':40000})
    q=res.x; st=np.maximum(np.abs(q)*2e-3,np.array([1e-3]*len(q))); 
    if model=='oLCDM': st[1]=5e-4
    st[-1]=3e-5
    H=hessian(f,q,st); Cq=2*np.linalg.inv(H)
    J=np.array([(predvec(q+np.eye(len(q))[i]*st[i]/2,model)-predvec(q-np.eye(len(q))[i]*st[i]/2,model))/st[i] for i in range(len(q))]).T
    Pc=J@Cq@J.T; m=predvec(q,model)
    chk=chi2(q,model,y,Ci,quad=True)
    return {'model':model,'branch':br,'chi2':res.fun,'chi2_quadcheck':chk,'best':q.tolist(),'sig':np.sqrt(np.diag(Cq)).tolist(),
            'posdef':bool(np.all(np.linalg.eigvalsh(Cq)>0)),'pred_mean':m.tolist(),'pred_sig':np.sqrt(np.diag(Pc)).tolist(),
            'pred_corr_eig':np.linalg.eigvalsh(Pc/np.sqrt(np.outer(np.diag(Pc),np.diag(Pc)))).tolist(),'_Pc':Pc,'_q':q,'_Cq':Cq}
if __name__=='__main__':
    out={}
    for model in ['LCDM','wCDM','oLCDM','CPL']:
        for br in ['PRIM','REPL']:
            t=time.time(); r=fit(model,br); r['sec']=round(time.time()-t,1)
            out[f'{model}_{br}']={k:v for k,v in r.items() if not k.startswith('_')}
            print(model,br,'chi2=%.5f quad=%.5f'%(r['chi2'],r['chi2_quadcheck']),'best',np.round(r['best'],5),'sig',np.round(r['sig'],5),'posdef',r['posdef'],flush=True)
    out['q95']={N:float(stats.chi2.ppf(0.95,N)) for N in (2,4,6,8,12)}
    json.dump(out,open('verify_fits_R02_output.json','w'),indent=1)
