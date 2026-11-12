import json, numpy as np, csv, sys, subprocess
sys.path.insert(0,'../../../../euclid_20261112/source_inputs_8933784/unpacked'); 
sys.path.insert(0,'/workspace/r03-out/euclid_20261112/source_inputs_8933784/unpacked'); import verify_spectra as V
import engines as E
R={n:(json.load(open(f'runs/{n}.json')),np.load(f'runs/{n}.npz')) for n in ['camb_base','camb_tight','class_base','class_tight','camb_base_interp80','class_base_interp80']}
Z=['0','1','3']; out={}
def wcsv(fn,K,pref):
    with open(fn,'w',newline='') as f:
        w=csv.writer(f); w.writerow(['z','k_1_per_Mpc','P_camb_base_Mpc3','P_camb_tight_Mpc3','P_class_base_Mpc3','P_class_tight_Mpc3'])
        for z in Z:
            cols=[R[n][1][f'{pref}_z{z}'] for n in ['camb_base','camb_tight','class_base','class_tight']]
            for i,k in enumerate(K): w.writerow([z,repr(float(k))]+[repr(float(c[i])) for c in cols])
wcsv('comparison.csv',E.KCMP,'cmp'); wcsv('dense.csv',E.KD1,'d1'); wcsv('dense_24001.csv',E.KD2,'d2'); wcsv('historical_20pt_exact_geomspace.csv',E.KH20,'h20')
PAIRS={'CAMB base/tight':('camb_base','camb_tight'),'CLASS base/tight':('class_base','class_tight'),'cross base (CAMB/CLASS)':('camb_base','class_base'),'cross tight (CAMB/CLASS)':('camb_tight','class_tight'),
 'CAMB interp-only (k_per_logint 40->80)':('camb_base','camb_base_interp80'),'CAMB integration-only (Boost 1->2 at k_per_logint 80)':('camb_base_interp80','camb_tight'),
 'CLASS interp-only (k_per_decade 40/70->80/140)':('class_base','class_base_interp80'),'CLASS integration-only (tols+l_max_ur+sigma_k at 80/140)':('class_base_interp80','class_tight')}
pk={}; perk=[]
for lab,(a,b) in PAIRS.items():
    pk[lab]={}
    for z in Z:
        r=R[a][1][f'cmp_z{z}']/R[b][1][f'cmp_z{z}']-1; i=int(np.argmax(abs(r)))
        pk[lab][z]={'max_abs':float(abs(r).max()),'rms':float(np.sqrt(np.mean(r**2))),'mean_signed':float(r.mean()),'signed_min':float(r.min()),'signed_max':float(r.max()),'k_at_max':float(E.KCMP[i]),'signed_at_max':float(r[i])}
    allr=np.concatenate([R[a][1][f'cmp_z{z}']/R[b][1][f'cmp_z{z}']-1 for z in Z]); pk[lab]['all_z']={'max_abs':float(abs(allr).max()),'rms':float(np.sqrt(np.mean(allr**2)))}
out['Pk_201']=pk
with open('relative_differences_201.csv','w',newline='') as f:
    w=csv.writer(f); labs=list(PAIRS); w.writerow(['z','k_1_per_Mpc']+[l for l in labs])
    for z in Z:
        for i,k in enumerate(E.KCMP): w.writerow([z,'%.10g'%k]+['%.6e'%(R[PAIRS[l][0]][1][f'cmp_z{z}'][i]/R[PAIRS[l][1]][1][f'cmp_z{z}'][i]-1) for l in labs])
# screens
scr={'camb_base_tight_lt_0.1pct':all(pk['CAMB base/tight'][z]['max_abs']<1e-3 for z in Z),'class_base_tight_lt_0.1pct':all(pk['CLASS base/tight'][z]['max_abs']<1e-3 for z in Z),'tight_cross_lt_0.5pct':all(pk['cross tight (CAMB/CLASS)'][z]['max_abs']<5e-3 for z in Z)}
# sigma8
s8={}; R8=8/E.H
for n in ['camb_base','camb_tight','class_base','class_tight']:
    s8[n]={}
    for z in Z:
        a=R[n][1]; s1=V.sigma_R(E.KD1,a[f'd1_z{z}'],R8); s2=V.sigma_R(E.KD2,a[f'd2_z{z}'],R8); m=E.KD1<=10; st=V.sigma_R(E.KD1[m],a[f'd1_z{z}'][m],R8)
        sh=V.sigma_R(E.KD1/E.H,E.H**3*a[f'd1_z{z}'],8.0); eng=R[n][0]['sigma8_engine'][z+'.0']
        s8[n][z]={'integrated_12001':s1,'integrated_24001':s2,'grid_refinement_rel':s2/s1-1,'truncated_k<=10':st,'tail_rel_(30 vs 10)':s1/st-1,'h_unit_invariance_rel':sh/s1-1,'engine':eng,'integrated_vs_engine_rel':s1/eng-1,
                  'screens':{'int_vs_engine_lt_0.1pct':abs(s1/eng-1)<1e-3,'grid_refinement_lt_0.01pct':abs(s2/s1-1)<1e-4,'tail_lt_0.01pct':abs(s1/st-1)<1e-4,'h_unit_lt_1e-10':abs(sh/s1-1)<1e-10}}
out['sigma8']=s8; out['sigma8_cross_tight']={z:s8['camb_tight'][z]['integrated_12001']/s8['class_tight'][z]['integrated_12001']-1 for z in Z}; out['sigma8_cross_tight_engine']={z:s8['camb_tight'][z]['engine']/s8['class_tight'][z]['engine']-1 for z in Z}
# distances, H, thermal
bg={}
for lab,(a,b) in [('cross base',('camb_base','class_base')),('cross tight',('camb_tight','class_tight')),('CAMB base/tight',('camb_base','camb_tight')),('CLASS base/tight',('class_base','class_tight'))]:
    A,B=R[a][0],R[b][0]; d={}
    for q in ['DM','Hz']:
        zs=[z for z in A[q] if float(z)>0 or q=='Hz']; rr=np.array([A[q][z]/B[q][z]-1 for z in zs]); d[q]={'per_z':{z:float(A[q][z]/B[q][z]-1) for z in zs},'max_abs':float(abs(rr).max()),'rms':float(np.sqrt(np.mean(rr**2)))}
    xe=np.array([A['x_e'][z]/B['x_e'][z]-1 for z in A['x_e']]); d['x_e']={'per_z':{z:float(A['x_e'][z]/B['x_e'][z]-1) for z in A['x_e']},'max_abs':float(abs(xe).max())}
    bg[lab]=d
out['background']=bg; out['screens']=scr
out['readback']={n:{'Omega':R[n][0]['Omega'],'early_rho_nu_over_rho_gamma':R[n][0]['early_rho_nu_over_rho_gamma'],'native_k_range':R[n][0]['native_k_range'],'native_nk':R[n][0]['native_nk']} for n in R}
out['readback']['class_tight']['derived']=R['class_tight'][0]['derived']; out['readback']['camb_tight']['YHe']=R['camb_tight'][0]['YHe_effective']; out['readback']['camb_tight']['NonLinear']=R['camb_tight'][0]['NonLinear']
json.dump(out,open('baseline_analysis.json','w'),indent=1)
for l,v in pk.items(): print('%-58s'%l,' '.join('z%s max %.3e rms %.3e (k=%.4g)'%(z,v[z]['max_abs'],v[z]['rms'],v[z]['k_at_max']) for z in Z))
print(scr); 
for n in s8: print(n,{z:(round(s8[n][z]['integrated_vs_engine_rel'],7),'%.1e'%s8[n][z]['grid_refinement_rel'],'%.1e'%s8[n][z]['tail_rel_(30 vs 10)'],'%.1e'%s8[n][z]['h_unit_invariance_rel']) for z in Z})
print('s8 cross tight',out['sigma8_cross_tight'],out['sigma8_cross_tight_engine'])
for l,d in bg.items(): print(l,'DM max %.2e rms %.2e | H max %.2e rms %.2e | x_e max %.2e'%(d['DM']['max_abs'],d['DM']['rms'],d['Hz']['max_abs'],d['Hz']['rms'],d['x_e']['max_abs']))
