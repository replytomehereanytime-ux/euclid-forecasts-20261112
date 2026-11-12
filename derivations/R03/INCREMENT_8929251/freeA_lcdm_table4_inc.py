"""Test: does using DESI DR2 Table 4 rounded values/errors/rho (the July input, from the v2.1 audit inputs) instead of the box mean/cov file explain the small offset from the author's posterior means?"""
import numpy as np, json, sys, csv; sys.path.insert(0,'.'); sys.path.insert(0,'../calc')
import cplmodel_r03 as M
P='/workspace/r03-out/best_forecasts_handoff_20261112/drive_candidates/x/screened_forecast_review_v2_1/Constant_w_Numerical_Audit_Addendum_20261112_v1_x/constant_w_audit_addendum_v1/inputs/desi_dr2_table4.csv'
rows=list(csv.DictReader(open(P))); d=[]; C=np.zeros((13,13)); k=0
for r in rows:
    if r['tracer']=='BGS': d.append(float(r['DV'])); C[k,k]=float(r['DV_error'])**2; k+=1; continue
    if r['tracer']=='Lya': dm,dme,dh,dhe,rho=39.32,0.33,8.600,0.066,0.225
    else: dm,dme,dh,dhe,rho=[float(r[x]) for x in ('DM','DM_error','DH','DH_error','rho_MH')]
    if r['tracer']=='Lya':  # box ordering at z=2.33 is DH then DM
        d+=[dh,dm]; C[k,k]=dhe**2; C[k+1,k+1]=dme**2; C[k,k+1]=C[k+1,k]=rho*dme*dhe
    else:
        d+=[dm,dh]; C[k,k]=dme**2; C[k+1,k+1]=dhe**2; C[k,k+1]=C[k+1,k]=rho*dme*dhe
    k+=2
M.BR['TABLE4_REPLACEMENT']=(np.array(d),np.linalg.inv(C))
import freeA_lcdm_inc as F  # re-run would recompute everything; instead import functions only
F.BR=M.BR
o=F.post('TABLE4_REPLACEMENT',2001,2001)
json.dump(o,open('freeA_lcdm_table4_inc_output.json','w'),indent=1)
print('Om',o['Om_mean_sd'],'A',o['A_mean_sd'],'chi2min',o['chi2_min'])
for z in F.ZH: print(z,{k:[round(x,5) for x in v] for k,v in o['rows'][z]['post_mean_sd'].items()})
