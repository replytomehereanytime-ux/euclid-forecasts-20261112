# Decompose handoff BF-2 (w=-0.967) vs R02 CTC-3P/RF-3 (w=-1.043). Own code.
# BF-2 setup per HANDOFF.md L82-85,104: 13 DESI DR2 points with Lya REPLACED (Eq.26, rho=+0.225), flat wCDM, radiation omitted,
# free A=c/(H0 rd), no CMB, no SNe; flat priors Om U(0.1,0.5) (grid 0.18-0.42), A U(20,40) (grid 28-31), w U(-1.5,-0.5); posterior medians.
import numpy as np, json, math
from verify_fits_R02 import Z,Q,branch,fit
from scipy import optimize
xg,wg=np.polynomial.legendre.leggauss(64)
def shape(om,w):  # BAO observables / A  (radiation omitted)
    E=lambda z: np.sqrt(om*(1+z)**3+(1-om)*(1+z)**(3*(1+w)))
    out=[]
    for z,q in zip(Z,Q):
        u=0.5*z*(xg+1); dm=0.5*z*np.sum(wg/E(u)); dh=1/E(z)
        out.append({'DM_over_rs':dm,'DH_over_rs':dh,'DV_over_rs':(z*dm*dm*dh)**(1/3)}[q])
    return np.array(out)
def grid_post(br, omg=np.linspace(0.18,0.42,241), wg_=np.linspace(-1.5,-0.5,401), Ag=np.linspace(28,31,301)):
    y,Ci=branch(br); L=np.zeros((len(omg),len(wg_),len(Ag))); chimin=1e9; best=None
    for i,om in enumerate(omg):
        for j,w in enumerate(wg_):
            s=shape(om,w); a=s@Ci@s; b=s@Ci@y; c=y@Ci@y
            ch=a*Ag**2-2*b*Ag+c; L[i,j]=-0.5*ch
            Ab=b/a; cm=c-b*b/a
            if cm<chimin: chimin=cm; best=(om,w,Ab)
    P=np.exp(L-L.max()); P/=P.sum()
    def med(axis_vals, marg):
        cdf=np.cumsum(marg); return [float(np.interp(p,cdf,axis_vals)) for p in (0.16,0.5,0.84)]
    return {'chi2_min_grid':float(chimin),'best_grid':best,
            'Om':med(omg,P.sum((1,2))),'w':med(wg_,P.sum((0,2))),'A':med(Ag,P.sum((0,1)))}
def bao_only_best(br):
    y,Ci=branch(br)
    f=lambda p: (lambda r: float(r@Ci@r))(p[2]*shape(p[0],p[1])-y)
    r=optimize.minimize(f,[0.30,-0.95,29.8],method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-11,'maxiter':20000})
    return {'chi2':r.fun,'Om,w,A':r.x.tolist()}
out={}
for br in ('REPL','PRIM'):
    out[f'BAOonly_{br}_gridposterior']=grid_post(br); out[f'BAOonly_{br}_bestfit']=bao_only_best(br)
    rr=fit('wCDM',br); out[f'BAO+CMB_{br}_bestfit']={'chi2':rr['chi2'],'Om,h,w,wb':rr['best'],'sig':rr['sig']}
    print(br,json.dumps({k:v for k,v in out.items() if br in k},default=float),flush=True)
json.dump(out,open('verify_bf2_decomp_R02_output.json','w'),indent=1,default=float)
