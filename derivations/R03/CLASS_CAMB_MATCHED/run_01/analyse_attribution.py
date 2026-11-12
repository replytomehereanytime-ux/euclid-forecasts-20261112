import json, numpy as np, csv, sys
sys.path.insert(0,'/workspace/r03-out/euclid_20261112/source_inputs_8933784/unpacked'); import verify_spectra as V
import engines as E
L=lambda n:(json.load(open(f'runs/{n}.json')),np.load(f'runs/{n}.npz') if json.load(open(f'runs/{n}.json'))['status']=='OK' and n!='A6_hist_replay_x' else None)
Z=['0','1','3']; R8=8/E.H; out={}
def cmp(a,b,pref='cmp',K=E.KCMP):
    A,B=L(a)[1],L(b)[1]; d={}
    for z in Z:
        r=A[f'{pref}_z{z}']/B[f'{pref}_z{z}']-1; i=int(np.argmax(abs(r))); d[z]={'max_abs':float(abs(r).max()),'rms':float(np.sqrt(np.mean(r**2))),'mean_signed':float(r.mean()),'signed_min':float(r.min()),'signed_max':float(r.max()),'k_at_max':float(K[i])}
    return d
def s8(n,z): a=L(n)[1]; return V.sigma_R(E.KD1,a[f'd1_z{z}'],R8)
# tighter ladder
out['ladder']={'CAMB tight/tighter':cmp('camb_tight','camb_tighter'),'CLASS tight/tighter':cmp('class_tight','class_tighter'),'cross tighter':cmp('camb_tighter','class_tighter'),'cross tight':cmp('camb_tight','class_tight')}
out['ladder_sigma8']={'cross_tighter':{z:s8('camb_tighter',z)/s8('class_tighter',z)-1 for z in Z},'CAMB tight/tighter':{z:s8('camb_tight',z)/s8('camb_tighter',z)-1 for z in Z},'CLASS tight/tighter':{z:s8('class_tight',z)/s8('class_tighter',z)-1 for z in Z}}
A1=L('A1_camb_mnu006')[0]; A2=L('A2_class_matched_massive')[0]; A3=L('A3_camb_bbn_YHe')[0]
att={}
def row(lab,a,b,note):
    d=cmp(a,b); att[lab]={'pair':f'{a} / {b}','Pk':d,'sigma8_rel':{z:s8(a,z)/s8(b,z)-1 for z in Z},'note':note}
row('A0 matched baseline (tight)','camb_tight','class_tight','reference')
row('A1 CAMB mnu=0.06 (1 massive, Neff 3.044) vs CLASS massless','A1_camb_mnu006','class_tight','deliberately unmatched; Omega_m changes to %.6f (CAMB readback), omnuh2 %.6e'%(A1['Omega']['m'],A1['omnuh2']))
row('A1 effect within CAMB (massive/massless)','A1_camb_mnu006','camb_tight','pure neutrino-mass effect in one code')
row('A2 matched massive: CAMB mnu=0.06 vs CLASS matched ncdm','A1_camb_mnu006','A2_class_matched_massive','CLASS N_ncdm=1, deg_ncdm=%.6f, T_ncdm=(4/11)^(1/3), N_ur=%.6f, omega_ncdm=CAMB omnuh2'%(A1['nu_mass_degeneracies'][0],A1['num_nu_massless']))
row('A3 CAMB BBN helium alone (YHe=%.6f) vs CAMB YHe=0.245'%A3['YHe_effective'],'A3_camb_bbn_YHe','camb_tight','CAMB-internal effect of BBN helium')
row('A3 CAMB BBN helium vs CLASS (YHe 0.245)','A3_camb_bbn_YHe','class_tight','')
row('A3b CLASS HyRec vs CLASS RECFAST (CLASS-only; CAMB HyRec unavailable)','A3b_class_hyrec','class_tight','not a same-family pair: CAMB build lacks HyRec')
row('A4 CLASS matter_source_in_current_gauge default vs yes','A4_class_matter_source_default','class_tight','definition branch')
row('A4 CAMB vs CLASS(default matter source)','camb_tight','A4_class_matter_source_default','')
out['attribution']=att
out['A2_readback']={'CAMB':{'omnuh2':A1['omnuh2'],'Omega_nu_z0':A1['Omega']['nu'],'early_rho_nu_over_rho_gamma':A1['early_rho_nu_over_rho_gamma'],'nu_mass_degeneracies':A1['nu_mass_degeneracies'],'num_nu_massless':A1['num_nu_massless'],'Omega_m':A1['Omega']['m']},
 'CLASS':{'Omega_ncdm_z0':A2['Omega']['ncdm'],'omega_ncdm_z0':A2['Omega']['ncdm']*E.H**2,'early_rho_nu_over_rho_gamma':A2['early_rho_nu_over_rho_gamma'],'Omega_m':A2['Omega']['m'],'m_ncdm_readback':A2['class_pars_readback'].get('m_ncdm','(not echoed)'),'derived':A2['derived']}}
r=out['A2_readback']; r['late_omega_nu_rel']=r['CLASS']['omega_ncdm_z0']/r['CAMB']['omnuh2']-1; r['early_ratio_rel']=list(r['CLASS']['early_rho_nu_over_rho_gamma'].values())[0]/list(r['CAMB']['early_rho_nu_over_rho_gamma'].values())[0]-1
# A5 interpolation-only: historical 200-pt h-unit CAMB sampling + log-log interp vs direct physical evaluation (same camb_base run)
cb=L('camb_base')[1]; kh=cb['hist_kh']; pkh=cb['hist_pk_h']; zh=list(cb['hist_z']); iz=zh.index(0.0) if 0.0 in zh else int(np.argmin(np.abs(np.array(zh))))
kc=kh*E.H; pc=pkh[iz]/E.H**3
P20=np.exp(np.interp(np.log(E.KH20),np.log(kc),np.log(pc))); P201=np.exp(np.interp(np.log(E.KCMP),np.log(kc),np.log(pc)))
r20=P20/cb['h20_z0']-1; r201=P201/cb['cmp_z0']-1
out['A5_interp_only']={'hist_spectrum_z_order':list(map(float,zh)),'20pt':{'max_abs':float(abs(r20).max()),'rms':float(np.sqrt(np.mean(r20**2)))},'201pt':{'max_abs':float(abs(r201).max()),'rms':float(np.sqrt(np.mean(r201**2))),'k_at_max':float(E.KCMP[np.argmax(abs(r201))])}}
# Historical comparison: source rel diff (|CAMB-CLASS|/CLASS) at 20 pts vs A1 and A6
H=np.genfromtxt('/workspace/r03-out/euclid_20261112/source_inputs_8933784/unpacked/historical_rounded_table.csv',delimiter=',',names=True)
hist_rel=H['P_CAMB_Mpc3']/H['P_CLASS_Mpc3']-1
a1=L('A1_camb_mnu006')[1]['h20_z0']/L('class_tight')[1]['h20_z0']-1
h6c=L('A6_hist_replay_camb'); h6l=L('A6_hist_replay_class'); a6=h6c[1]['P20']/h6l[1]['P20']-1
out['historical_shape']={'k':E.KH20.tolist(),'hist_signed_from_rounded_P':hist_rel.tolist(),'A1_signed':a1.tolist(),'A6_replay_signed':a6.tolist(),
  'A1_minus_hist':{'max_abs':float(abs(a1-hist_rel).max()),'rms':float(np.sqrt(np.mean((a1-hist_rel)**2))),'mean_abs_A1':float(abs(a1).mean()),'mean_abs_hist':float(abs(hist_rel).mean())},
  'A6_minus_hist':{'max_abs':float(abs(a6-hist_rel).max()),'rms':float(np.sqrt(np.mean((a6-hist_rel)**2))),'mean_abs_A6':float(abs(a6).mean()),'max_abs_A6':float(abs(a6).max())},
  'A6_CAMB_P_vs_hist_printed':(h6c[1]['P20']/H['P_CAMB_Mpc3']-1).tolist(),'A6_CLASS_P_vs_hist_printed':(h6l[1]['P20']/H['P_CLASS_Mpc3']-1).tolist(),
  'A6_sigma8':{'CAMB':h6c[0]['sigma8'],'CLASS':h6l[0]['sigma8'],'hist_CAMB':0.7941911366899833,'hist_CLASS':0.8059023437254481},
  'A6_camb_effective':{k:h6c[0][k] for k in ['YHe','mnu_omnuh2','nnu','num_massive','Reionization','optical_depth','Omega_m','Recomb']},'A6_class_Omega_m':h6l[0]['Omega_m']}
with open('attribution_historical_20pt.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['k_1_per_Mpc_exact_geomspace','hist_signed_rel_from_rounded_P','A1_camb_mnu006_over_class_tight_minus1','A6_replay_current_versions_minus1','A6_CAMB_P_over_hist_printed_minus1','A6_CLASS_P_over_hist_printed_minus1'])
    for i,k in enumerate(E.KH20): w.writerow(['%.10g'%k,'%.6e'%hist_rel[i],'%.6e'%a1[i],'%.6e'%a6[i],'%.4e'%out['historical_shape']['A6_CAMB_P_vs_hist_printed'][i],'%.4e'%out['historical_shape']['A6_CLASS_P_vs_hist_printed'][i]])
out['A3b_camb_hyrec']=json.load(open('runs/A3b_camb_hyrec.json'))
json.dump(out,open('attribution_analysis.json','w'),indent=1,default=str)
for k,v in out['ladder'].items(): print(k,{z:('%.3e'%v[z]['max_abs'],'%.3e'%v[z]['rms']) for z in Z})
print('ladder s8',out['ladder_sigma8'])
for k,v in att.items(): print(k,'| z0 max %.4e rms %.4e mean %.4e k@max %.4g | s8 %.4e'%(v['Pk']['0']['max_abs'],v['Pk']['0']['rms'],v['Pk']['0']['mean_signed'],v['Pk']['0']['k_at_max'],v['sigma8_rel']['0']))
print('A2 readback',json.dumps(out['A2_readback'],default=str)[:900]); print('A5',out['A5_interp_only']); print('hist',json.dumps({k:out['historical_shape'][k] for k in ['A1_minus_hist','A6_minus_hist','A6_sigma8','A6_camb_effective','A6_class_Omega_m']},default=str))
