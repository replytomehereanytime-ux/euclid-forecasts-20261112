# R02 sensitivity: REPLACE (not add) DESI DR2 Lya BAO point with DR2 Results IV joint Lya AP+BAO values
# (arXiv:2607.27410 abstract: DH/rd=8.600+-0.066, DM/rd=39.32+-0.33 at z=2.33). Their DM-DH correlation is NOT in the
# abstract -> ASSUMPTION: scan r in {old-file r, 0, -0.5}. Labelled sensitivity only, not a result.
import numpy as np, json, math
from scipy import integrate, optimize
d='/workspace/desi_r01/'
rows=[l.split() for l in open(d+'desi_gaussian_bao_ALL_GCcomb_mean.txt') if not l.startswith('#') and l.strip()]
z=np.array([float(r[0]) for r in rows]); y0=np.array([float(r[1]) for r in rows]); q=[r[2] for r in rows]
C0=np.loadtxt(d+'desi_gaussian_bao_ALL_GCcomb_cov.txt')
iDH=[i for i in range(len(z)) if abs(z[i]-2.33)<1e-6 and q[i]=='DH_over_rs'][0]
iDM=[i for i in range(len(z)) if abs(z[i]-2.33)<1e-6 and q[i]=='DM_over_rs'][0]
r_old=C0[iDH,iDM]/math.sqrt(C0[iDH,iDH]*C0[iDM,iDM])
phi=(1+5**0.5)/2
def run(r):
    y=y0.copy(); C=C0.copy()
    y[iDH]=8.600; y[iDM]=39.32
    C[iDH,iDH]=0.066**2; C[iDM,iDM]=0.33**2; C[iDH,iDM]=C[iDM,iDH]=r*0.066*0.33
    Ci=np.linalg.inv(C)
    def model(p):
        Om,A=p; E=lambda x: math.sqrt(Om*(1+x)**3+1-Om); out=[]
        for zi,qi in zip(z,q):
            DM=A*integrate.quad(lambda x:1/E(x),0,zi)[0]; DH=A/E(zi)
            out.append({'DM_over_rs':DM,'DH_over_rs':DH,'DV_over_rs':(zi*DM*DM*DH)**(1/3)}[qi])
        return np.array(out)
    chi2=lambda p: float((y-model(p))@Ci@(y-model(p)))
    res=optimize.minimize(chi2,[0.3,29.5],method='Nelder-Mead',options={'xatol':1e-8,'fatol':1e-10})
    o={'r_assumed':r,'Om':res.x[0],'A':res.x[1],'chi2':res.fun,'branches':{}}
    for n,v in {'phi^7':phi**7,'29':29.0,'843/29':843/29}.items():
        r2=optimize.minimize_scalar(lambda Om: chi2([Om,v]),bounds=(0.1,0.6),method='bounded')
        o['branches'][n]=math.sqrt(max(r2.fun-res.fun,0))
    return o
out={'old_lya':{'DH':float(y0[iDH]),'DM':float(y0[iDM]),'r_old':r_old},'runs':[run(r) for r in (r_old,0.0,-0.5)]}
json.dump(out,open('calc_lya_replace_sensitivity_R02_output.json','w'),indent=1); print(json.dumps(out,indent=1))
