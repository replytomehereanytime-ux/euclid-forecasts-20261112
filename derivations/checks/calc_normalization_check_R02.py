# R02: independent check of Claude claim (c): phi^7, 29, 843/29 vs DESI DR2 BAO-only flat LCDM.
# Inputs: /workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_{mean,cov}.txt (official DESI DR2 BAO, read-only). Radiation omitted.
import numpy as np, json, math
from scipy import integrate, optimize
d='/workspace/desi_r01/'
rows=[l.split() for l in open(d+'desi_gaussian_bao_ALL_GCcomb_mean.txt') if not l.startswith('#') and l.strip()]
z=np.array([float(r[0]) for r in rows]); y=np.array([float(r[1]) for r in rows]); q=[r[2] for r in rows]
C=np.loadtxt(d+'desi_gaussian_bao_ALL_GCcomb_cov.txt'); Ci=np.linalg.inv(C)
def model(p):
    Om,A=p; E=lambda x: math.sqrt(Om*(1+x)**3+1-Om); out=[]
    for zi,qi in zip(z,q):
        DM=A*integrate.quad(lambda x:1/E(x),0,zi)[0]; DH=A/E(zi)
        out.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi])
    return np.array(out)
chi2=lambda p: float((y-model(p))@Ci@(y-model(p)))
res=optimize.minimize(chi2,[0.3,29.5],method='Nelder-Mead',options={'xatol':1e-8,'fatol':1e-10,'maxiter':4000})
p=res.x
# numerical Hessian -> covariance
h=np.array([1e-4,1e-3]); H=np.zeros((2,2))
for i in range(2):
    for j in range(2):
        ei=np.eye(2)[i]*h[i]; ej=np.eye(2)[j]*h[j]
        H[i,j]=(chi2(p+ei+ej)-chi2(p+ei-ej)-chi2(p-ei+ej)+chi2(p-ei-ej))/(4*h[i]*h[j])
cov=np.linalg.inv(H/2); sA=math.sqrt(cov[1,1]); sOm=math.sqrt(cov[0,0])
phi=(1+5**0.5)/2
out={'n_points':len(y),'Om':p[0],'sigma_Om':sOm,'A=c/(H0 rd)':p[1],'sigma_A':sA,'chi2_min':res.fun,
     'hrd_Mpc_implied':299792.458/100/p[1],
     'published_check_hrd_101.54+-0.73_gives_A':299792.458/100/101.54,
     'branches':{}}
for name,val in {'phi^7':phi**7,'29':29.0,'843/29':843/29}.items():
    # profile: chi2 with A fixed, Om free
    r2=optimize.minimize_scalar(lambda Om: chi2([Om,val]),bounds=(0.1,0.6),method='bounded')
    dchi=r2.fun-res.fun
    out['branches'][name]={'A':val,'gauss_pull_sigma':(p[1]-val)/sA,'profile_dchi2':dchi,'profile_sigma':math.sqrt(max(dchi,0))}
json.dump(out,open('calc_normalization_check_R02_output.json','w'),indent=1); print(json.dumps(out,indent=1))
