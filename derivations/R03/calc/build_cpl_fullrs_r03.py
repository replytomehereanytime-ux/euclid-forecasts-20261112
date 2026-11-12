import json, csv, sys, numpy as np
sys.path.insert(0,'calc'); import cplmodel_r03 as M; M.RSMODE='full'
F=json.load(open('calc/fullrs_r03_output.json')); CL=json.load(open('calc/class_crosscheck_r03_output.json')); OLD=json.load(open('calc/cpl_oldprimary_r03_output.json')); V0=json.load(open('calc/cpl_validation_r03.json'))
P=F['mcmc']['CPL_PRIMARY']; B=F['mcmc']['CPL_REPLACEMENT']; G4=['0.9','1.2','1.5','1.8']; ALL=[str(z) for z in M.ZG]
def q(b,k): x=b[k]; return (x[2],x[1],x[3],x[0],x[4])
# V4: importance-reweight full-r_s PRIMARY chain to REPLACEMENT likelihood -> compare with fresh REPLACEMENT chain
th=np.load('calc/fullrs_cpl_chain_PRIMARY_R03.npy'); lw=-0.5*(M.chi2(th,'REPLACEMENT')-M.chi2(th,'PRIMARY')); w=np.exp(lw-lw.max()); w/=w.sum(); ess=1/np.sum(w**2)
pr=M.pred(th,[0.9,1.2,1.5,1.8]); v4=0
def wq(x,w,qq): i=np.argsort(x); c=np.cumsum(w[i]); return float(np.interp(qq,c/c[-1],x[i]))
for z in [0.9,1.2,1.5,1.8]:
    for j,k in enumerate(['DM/rd','DH/rd']): v4=max(v4,abs(wq(pr[z][j],w,0.5)-B['bands'][str(z)][k][2]))
# shifts truncated->full (primary medians)
Pold=OLD['chain_primary']['bands']; sh={z:{k:P['bands'][z][k][2]/Pold[z][k][2]-1 for k in ['DM/rd','DH/rd','DM/DH']} for z in ALL}
val={'V1_code_path_reproduces_R02_CTC5B_in_trunc_mode (R02 replacement numbers from that branch data)':V0['V1_reweighted_chain_reproduces_R02_CTC5B_R04s5'],
 'V2_python_vs_wolfram_fullrs_bestfit_LCDM_wCDM':'see W_RECONCILE/VALIDATION: chi2 agree to <2e-11 relative, parameters to <1e-7',
 'V3_emcee_tau':{'PRIMARY':P['tau'],'REPLACEMENT':B['tau'],'steps':P['steps'],'burn':P['burn'],'N_PRIMARY':P['N']},
 'V4_reweighted_fullrs_PRIMARY_chain_vs_fresh_REPLACEMENT_chain_max_abs_median_diff':v4,'V4_ESS':float(ess),
 'V5_CLASS_3.4.2_60_chain_points_max_abs_rel':CL['CPL_PRIMARY_chain_60pts_maxabs_rel'],
 'V5_CLASS_at_CPL_PRIMARY_bestfit':{'rd_formula_vs_CLASS_rs_d':CL['cases']['CPL_PRIM_fullrs_best']['rd_formula_vs_CLASS_rs_d'],'rs_star_full_vs_CLASS_rs_rec':CL['cases']['CPL_PRIM_fullrs_best']['rs_star_R03_vs_CLASS_rs_rec'],'rs_star_truncated_vs_CLASS_rs_rec':CL['cases']['CPL_PRIM_fullrs_best']['rs_star_trunc_vs_CLASS_rs_rec']},
 'predcov_PRIMARY':{'PD':P['predcov']['PD'],'min_eig':min(P['predcov']['eig']),'max_eig':max(P['predcov']['eig'])},
 'shift_full_over_trunc_minus1_PRIMARY_medians':sh,'params_PRIMARY_fullrs':P['params'],'params_REPLACEMENT_fullrs':B['params'],'params_PRIMARY_trunc':OLD['chain_primary']['params']}
json.dump(val,open('calc/cpl_validation_fullrs_r03.json','w'),indent=1)
pv=lambda b,z: "z=%s: DM/rd %.3f [%.3f, %.3f] {%.3f, %.3f}, DH/rd %.3f [%.3f, %.3f] {%.3f, %.3f}"%((z,)+q(b[z],'DM/rd')+q(b[z],'DH/rd'))
row=json.load(open('calc/cpl_row_r03_SUPERSEDED_TRUNCRS.json'))
row.update(id='CTC-5P-R03',verification='PROVISIONAL',
 title='CPL (w0waCDM), BAO + compressed CMB, frozen old-DESI primary (R03 rerun with r_s(z*) integrated to infinity; fills the R02 CTC-5P gap)',
 model='Flat CPL w(a)=w0+wa(1−a); radiation with N_eff=3.046; r_d fitting formula (ω_ν=0.00064); r_s(z*) = ∫ c_s/H dz from z* to ∞ (R03 fix; the R01/R02/R04 code stopped at z=10^5); priors as fit_cpl.py L35: 0.1<Ωm<0.6, 0.4<h<1, −3<w0<1, −4<wa<2, w0+wa<0, 0.018<ω_b<0.027',
 calib='DESI DR2 BAO 13 points with the ORIGINAL Lyα pair (old-DESI primary, /workspace/desi_r01 mean/cov) + Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019). No SNe. Fresh R03 chain (emcee 3.1.6, 40 walkers × 10,000 steps, burn 2,500, thin 5, seed 20261112).',
 covariance='C_E = Euclid published covariance; C_pred = full 8×8 sample covariance of the chain predictions (R03/calc/fullrs_r03_output.json mcmc.CPL_PRIMARY.predcov; positive-definite, rank effectively 5). Shared calibration: A = c/(H0 rd) is common to all 8 numbers. s.d. by element: '+', '.join('%.4f'%x for x in P['predcov']['sd']),
 predictive="Posterior median, 68%% interval [ ] and 95%% interval { } from the R03 full-r_s emcee chain (old DESI DR2 Lyα data, %d samples): "%P['N']+"; ".join(pv(P['bands'],z) for z in G4)+". s_pred = half-width of the 68% interval.",
 sources='/workspace/desi_r01 mean/cov (sha in VALIDATION_R03.md); R03/calc/cplmodel_r03.py (RSMODE=full), fullrs_r03.py, fullrs_r03_output.json, fullrs_cpl_chain_PRIMARY_R03.npy',
 notes='Non-Gaussian posterior (w0–wa degeneracy). Hessians step-dependent, so Laplace bands are NOT used; MCMC covariance used. Supersedes the truncated-r_s version (CPL_OLDPRIMARY_R03_SUPERSEDED_TRUNCRS.csv). CLASS 3.4.2 cross-check: see validation.')
with open('CPL_OLDPRIMARY_R03.csv','w',newline='') as f: w_=csv.DictWriter(f,fieldnames=list(row)); w_.writeheader(); w_.writerow(row)
with open('CPL_OLDPRIMARY_BANDS_R03.csv','w',newline='') as f:
    w_=csv.writer(f); w_.writerow(['source','z','quantity','median','q16','q84','q2.5','q97.5'])
    for lab,b in [('PRIMARY_fullrs_emcee_R03',P['bands']),('REPLACEMENT_fullrs_emcee_R03',B['bands']),('PRIMARY_TRUNCRS_original_chain_SUPERSEDED',Pold)]:
        for z in ALL:
            for k in ['DM/rd','DH/rd','DM/DH']: w_.writerow([lab,z,k]+['%.5f'%x for x in q(b[z],k)])
json.dump(row,open('calc/cpl_row_r03.json','w'),indent=1)
print(json.dumps({k:v for k,v in val.items() if k not in('shift_full_over_trunc_minus1_PRIMARY_medians',)},indent=1)); print({z:sh[z] for z in ['0.9','1.3','1.8']})
for z in G4: print(pv(P['bands'],z)); print('  B',pv(B['bands'],z))
