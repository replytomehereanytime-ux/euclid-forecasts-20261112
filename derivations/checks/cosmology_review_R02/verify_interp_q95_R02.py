# (a) chi-square 0.95 quantiles; (b) size of the 'linear interpolation in z between grid nodes' error vs predictive sigma.
import numpy as np, json
from scipy import stats
from verify_fits_R02 import *
out={'q95':{N:float(stats.chi2.ppf(0.95,N)) for N in range(1,13)}}
res={}
for model,br in [('LCDM','PRIM'),('wCDM','PRIM'),('oLCDM','PRIM')]:
    r=fit(model,br); q=r['_q']; p,ob=MAPS[model](q); rr=rd(p[0],p[2],ob)
    ex=lambda z:(DM(z,p)/rr, C/(100*p[2]*E(z,*p[:5]))/rr)
    nodes={z:ex(z) for z in ZE}; rows=[]
    for z in [1.05,1.35,1.65]:
        a,b=max(n for n in ZE if n<z),min(n for n in ZE if n>z); t=(z-a)/(b-a)
        lin=[(1-t)*nodes[a][k]+t*nodes[b][k] for k in (0,1)]; e=ex(z)
        rows.append({'z':z,'DM_exact':e[0],'DM_lin':lin[0],'DM_err':lin[0]-e[0],'DH_exact':e[1],'DH_lin':lin[1],'DH_err':lin[1]-e[1]})
    res[f'{model}_{br}']={'rows':rows,'pred_sig_nodes':r['pred_sig']}
out['interp']=res
json.dump(out,open('verify_interp_q95_R02_output.json','w'),indent=1)
print(json.dumps(out['q95'],indent=0)); 
for k,v in res.items():
    print(k,[ (x['z'],round(x['DM_err'],4),round(x['DH_err'],4)) for x in v['rows']],'sig',np.round(v['pred_sig_nodes'],4).tolist())
