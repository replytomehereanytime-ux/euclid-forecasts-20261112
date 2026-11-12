"""(b) Old-DESI historical primary from Table 4 (original Lya row). Reproduce medians; test a simultaneous-band construction. Frozen values are NOT changed."""
import numpy as np, json, sys, csv; sys.path.insert(0,'.'); sys.path.insert(0,'../calc')
import cplmodel_r03 as M, freeA_lcdm_inc as F
P='/workspace/r03-out/best_forecasts_handoff_20261112/drive_candidates/x/screened_forecast_review_v2_1/Constant_w_Numerical_Audit_Addendum_20261112_v1_x/constant_w_audit_addendum_v1/inputs/desi_dr2_table4.csv'
def build(replace):
    rows=list(csv.DictReader(open(P))); d=[]; C=np.zeros((13,13)); k=0
    for r in rows:
        if r['tracer']=='BGS': d.append(float(r['DV'])); C[k,k]=float(r['DV_error'])**2; k+=1; continue
        dm,dme,dh,dhe,rho=[float(r[x]) for x in ('DM','DM_error','DH','DH_error','rho_MH')]
        if r['tracer']=='Lya' and replace: dm,dme,dh,dhe,rho=39.32,0.33,8.600,0.066,0.225
        if r['tracer']=='Lya': d+=[dh,dm]; C[k,k]=dhe**2; C[k+1,k+1]=dme**2
        else: d+=[dm,dh]; C[k,k]=dme**2; C[k+1,k+1]=dhe**2
        C[k,k+1]=C[k+1,k]=rho*dme*dhe; k+=2
    return np.array(d),np.linalg.inv(C)
F.BR['T4_OLD']=build(False); F.BR['T4_NEW']=build(True)
O={}
for br in ['T4_OLD','T4_NEW']:
    o=F.post(br,2001,2001); O[br]=o
# at-mean-parameter evaluation (the author's stated means) vs integrated means
gx=F.gx
def at(om,A,z): I=float(F.I(z,np.array([om]))[0]); E=float(F.Ef(z,om)); return A*I, A/E, I*E
O['at_source_means_REPLACEMENT']={z:at(0.30194023839055434,29.635459200210903,z) for z in F.ZH}
O['at_source_means_OLD']={z:at(0.2978140059789888,29.530952497437177,z) for z in F.ZH}
# simultaneous-band test on old branch: sample posterior grid, 15 latent coords, max standardized deviation
d,Ci=F.BR['T4_OLD']; om=np.linspace(0.1,0.5,2001); A=np.linspace(20,40,2001); u=F.u_shape(om)
a=np.einsum('ni,ij,nj->n',u,Ci,u); b=u@Ci@d; c0=d@Ci@d; chi=c0-2*np.outer(b,A)+np.outer(a,A**2); L=np.exp(-0.5*(chi-chi.min())); L/=L.sum()
rng=np.random.default_rng(20261112); idx=rng.choice(L.size,200000,p=L.ravel()); io,ia=np.unravel_index(idx,L.shape)
oms=om[io]+rng.uniform(-1e-4,1e-4,len(io)); As=A[ia]+rng.uniform(-5e-3,5e-3,len(ia))
X=np.column_stack([v for z in F.ZH for v in (As*F.I(z,oms), As/F.Ef(z,oms), F.I(z,oms)*F.Ef(z,oms))])
med=np.median(X,0); sd=X.std(0); T=np.max(np.abs(X-med)/sd,axis=1)
sim={}
for lev in (0.68,0.90,0.95,0.99):
    t=np.quantile(T,lev); sim[str(lev)]={'t':float(t),'lo':(med-t*sd).tolist(),'hi':(med+t*sd).tolist()}
O['sim_band_test_OLD']={'method':'max over 15 coords of |x-median|/sd, posterior samples (200k, seed 20261112); symmetric; one possible construction, NOT necessarily the author\'s','median':med.tolist(),'levels':sim,'order':[f'{q}@{z}' for z in F.ZH for q in ('DM/rd','DH/rd','F_AP')]}
json.dump(O,open('freeA_lcdm_table4_old_inc_output.json','w'),indent=1)
o=O['T4_OLD']; print('OLD Om',o['Om_mean_sd'],'A',o['A_mean_sd'])
for z in F.ZH: print(z,{k:round(v,5) for k,v in o['rows'][z]['post_median'].items()})
for lev,s in sim.items(): print(lev,'t=%.3f'%s['t'],'z0.9 DM [%.5f, %.5f]'%(s['lo'][0],s['hi'][0]),'DH [%.5f,%.5f]'%(s['lo'][1],s['hi'][1]))
