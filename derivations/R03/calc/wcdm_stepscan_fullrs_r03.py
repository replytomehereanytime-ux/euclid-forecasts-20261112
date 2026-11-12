"""wCDM Laplace sigma_w vs Hessian step (central differences in parameters scaled by Wolfram-fit sigma), full r_s."""
import numpy as np, json, sys; sys.path.insert(0,'.'); import cplmodel_r03 as M; M.RSMODE='full'
F=json.load(open('fullrs_r03_output.json')); out={}
for br in ['PRIMARY','REPLACEMENT']:
    x0=np.array(F['fits'][br]['wCDM']['x']); s=np.array([0.008,0.010,0.042,0.00013])
    def f(q): th=np.array([q[0],q[1],q[2],0.0,q[3]]); return float(M.chi2(th,br)[0])
    r={}
    for st in [3e-3,1e-2,3e-2,0.1,0.3,1.0]:
        H=np.zeros((4,4)); d=st*s
        for i in range(4):
            for j in range(4):
                e=np.zeros(4); g=np.zeros(4); e[i]=d[i]; g[j]=d[j]
                H[i,j]=(f(x0+e+g)-f(x0+e-g)-f(x0-e+g)+f(x0-e-g))/(4*d[i]*d[j])
        C=np.linalg.inv(H/2); ev=np.linalg.eigvalsh(H); r[str(st)]={'sigma_w':float(np.sqrt(C[2,2])),'PD':bool(ev.min()>0)}
    out[br]={'best_w':x0[2],'scan(step in units of param sigma)':r,'MCMC':F['mcmc'][f'wCDM_{br}']['w']}
    print(br,{k:round(v['sigma_w'],5) for k,v in r.items()},'MCMC std %.4f'%out[br]['MCMC']['std'])
json.dump(out,open('wcdm_stepscan_fullrs_r03_output.json','w'),indent=1)
