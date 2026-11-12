import json, csv
O=json.load(open('calc/cpl_oldprimary_r03_output.json')); P=O['chain_primary']; RW=O['chain_reweighted_replacement']; FP=O['fresh_emcee']['PRIMARY']; FR=O['fresh_emcee']['REPLACEMENT']
G4=['0.9','1.2','1.5','1.8']; ALL=['0.9','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8']
# R04 §5 CPL replacement (= R02 CTC-5B) median [68%] {95%} values, verbatim
R04={'0.9':((20.997,20.923,21.071,20.854,21.140),(17.627,17.529,17.726,17.434,17.808),(1.1914,1.1838,1.1985,1.1765,1.2058)),
'1.0':((22.709,22.634,22.784,22.567,22.855),(16.637,16.551,16.723,16.469,16.812),(1.3654,1.3569,1.3730,1.3475,1.3808)),
'1.1':((24.326,24.252,24.401,24.184,24.473),(15.710,15.631,15.793,15.558,15.896),(1.5487,1.5386,1.5576,1.5271,1.5660)),
'1.2':((25.854,25.781,25.927,25.713,26.001),(14.846,14.772,14.932,14.702,15.039),(1.7415,1.7298,1.7520,1.7167,1.7614)),
'1.3':((27.299,27.227,27.372,27.157,27.443),(14.043,13.971,14.130,13.904,14.233),(1.9435,1.9306,1.9558,1.9162,1.9663)),
'1.4':((28.667,28.594,28.740,28.524,28.809),(13.299,13.226,13.384,13.164,13.479),(2.1550,2.1407,2.1690,2.1257,2.1810)),
'1.5':((29.963,29.889,30.035,29.818,30.103),(12.608,12.536,12.690,12.477,12.774),(2.3757,2.3604,2.3913,2.3451,2.4047)),
'1.6':((31.192,31.118,31.264,31.046,31.331),(11.967,11.897,12.043,11.841,12.117),(2.6054,2.5895,2.6225,2.5743,2.6375)),
'1.7':((32.358,32.283,32.431,32.213,32.498),(11.372,11.305,11.442,11.251,11.507),(2.8444,2.8279,2.8627,2.8131,2.8791)),
'1.8':((33.467,33.391,33.542,33.321,33.608),(10.819,10.756,10.882,10.705,10.938),(3.0921,3.0753,3.1114,3.0614,3.1290))}
def q(b,k): x=b[k]; return (x[2],x[1],x[3],x[0],x[4])  # median,16,84,2.5,97.5
maxdiff=0; worst=None
for z in ALL:
    for k,ref,dp in zip(['DM/rd','DH/rd','DM/DH'],R04[z],[3,3,4]):
        for a,b in zip(q(RW['bands'][z],k),ref):
            d=abs(round(a,dp)-b)
            if d>maxdiff: maxdiff,worst=d,(z,k,a,b)
V1={'compared':len(ALL)*3*5,'max_abs_diff_after_rounding':maxdiff,'worst':worst,'PASS':maxdiff<=1.01e-3}
# V2 fresh emcee replacement vs R04 (MC-level)
v2=max(abs(q(FR['bands'][z],k)[0]-R04[z][i][0]) for z in G4 for i,k in enumerate(['DM/rd','DH/rd']))
v2w=max(abs((q(FR['bands'][z],k)[2]-q(FR['bands'][z],k)[1])/(R04[z][i][2]-R04[z][i][1])-1) for z in G4 for i,k in enumerate(['DM/rd','DH/rd']))
# V3 fresh primary vs original-chain primary
v3=max(abs(q(FP['bands'][z],k)[0]-q(P['bands'][z],k)[0]) for z in G4 for k in ['DM/rd','DH/rd'])
v3w=max(abs((q(FP['bands'][z],k)[2]-q(FP['bands'][z],k)[1])/(q(P['bands'][z],k)[2]-q(P['bands'][z],k)[1])-1) for z in G4 for k in ['DM/rd','DH/rd'])
val={'V1_reweighted_chain_reproduces_R02_CTC5B_R04s5':V1,'V2_fresh_emcee_REPLACEMENT_vs_R02_CTC5B':{'max_abs_median_diff':v2,'max_rel_68width_diff':v2w},'V3_fresh_emcee_PRIMARY_vs_original_chain_PRIMARY':{'max_abs_median_diff':v3,'max_rel_68width_diff':v3w},
     'predcov_PRIMARY':{'PD':P['predcov']['PD'],'min_eig':min(P['predcov']['eig']),'max_eig':max(P['predcov']['eig']),'cond':P['predcov']['cond']},
     'hessian':{br:{k:{'PD':O['hessian'][br][k]['PD'],'w0_sd':O['hessian'][br][k].get('param_sd',[None]*5)[2],'wa_sd':O['hessian'][br][k].get('param_sd',[None]*5)[3]} for k in ['step_1e-3','step_3e-3','step_1e-2']} for br in ['PRIMARY','REPLACEMENT']},
     'chain_wa_sd_PRIMARY_68halfwidth':(P['params']['wa'][3]-P['params']['wa'][1])/2,'chain_w0_68halfwidth':(P['params']['w0'][3]-P['params']['w0'][1])/2,
     'fresh_emcee_tau':{'PRIMARY':FP['tau'],'REPLACEMENT':FR['tau']}}
json.dump(val,open('calc/cpl_validation_r03.json','w'),indent=1); print(json.dumps(val,indent=1))
pv=lambda b,z: "z=%s: DM/rd %.3f [%.3f, %.3f] {%.3f, %.3f}, DH/rd %.3f [%.3f, %.3f] {%.3f, %.3f}"%((z,)+q(b[z],'DM/rd')+q(b[z],'DH/rd'))
predictive="Posterior median, 68% interval [ ] and 95% interval { } from the original box emcee chain (fit_cpl.py, old DESI DR2 Lyα data, 48,000 samples, unweighted): "+"; ".join(pv(P['bands'],z) for z in G4)+". s_pred = half-width of the 68% interval."
sd=P['predcov']['sd']
row=dict(id='CTC-5P-R03',kind='conditional theory curve',readiness='READY',verification='PROVISIONAL',outcome='NOT_RUN',branch='PRIMARY',title='CPL (w0waCDM), BAO + compressed CMB, frozen old-DESI primary (R03 rerun; replaces nothing, fills the R02 CTC-5P gap)',
product='First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8}. NOT Foundation (Foundation has no BAO/clustering products).',
acquisition='Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.',
cuts="Euclid Consortium's published BAO sample (external)",observable='DM/rd, DH/rd (dimensionless) on z = 0.9, 1.2, 1.5, 1.8; F_AP = DM/DH derived, not scored separately; scale grid: n/a (BAO distances)',
model='Flat CPL w(a)=w0+wa(1−a); radiation with N_eff=3.046; rd fitting formula (ω_ν=0.00064); priors exactly as the chain was sampled (fit_cpl.py L35): 0.1<Ωm<0.6, 0.4<h<1, −3<w0<1, −4<wa<2, w0+wa<0, 0.018<ω_b<0.027',
calib='DESI DR2 BAO 13 points with the ORIGINAL Lyα pair (old-DESI primary, /workspace/desi_r01 mean/cov) + Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019). No SNe. Chain file chain_w0waCDM.npy predates 2026-11-12.',
exposure='Calibration data fully exposed by construction; the Euclid BAO target outcome does not exist yet and was not inspected.',
mask="Euclid's (external; randoms/visibility masks are Complete-era)",contaminants='Line interlopers, redshift failures, purity/completeness (Euclid; external)',estimator="Euclid's published BAO fit (external)",
covariance='C_E = Euclid published covariance; C_pred = full 8×8 sample covariance of the chain predictions (R03/calc/cpl_oldprimary_r03_output.json chain_primary.predcov; positive-definite, but its condition number is about 2.5e13, so it carries only about 5 independent directions = the 5 parameters). Shared calibration: A = c/(H0 rd) is common to all 8 numbers. s.d. by element: '+', '.join('%.4f'%x for x in sd),
predictive=predictive,
scoring='PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073); FAIL otherwise. m = chain medians, interpolated linearly in z.',
abstention='NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]; points outside the grid are not scored.',
internal='',sources='/workspace/desi_r01/chain_w0waCDM.npy, fit_cpl.py; R03/calc/cpl_oldprimary_r03.py and output JSON',
notes='Non-Gaussian posterior (w0–wa degeneracy; wa reaches the −4 prior edge for 0.4% of samples). Numerical Hessians are positive-definite but step-dependent (w0 s.d. 0.25/0.14/0.045 for steps 1e-3/3e-3/1e-2), so Laplace bands are NOT valid. The MCMC covariance is used; an independent seeded emcee rerun agrees (see validation). Same chain as R02 CTC-5B, but unweighted: the primary-to-replacement difference therefore contains no Monte Carlo noise.')
with open('CPL_OLDPRIMARY_R03.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(row)); w.writeheader(); w.writerow(row)
with open('CPL_OLDPRIMARY_BANDS_R03.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['source','z','quantity','median','q16','q84','q2.5','q97.5'])
    for lab,b in [('PRIMARY_original_chain',P['bands']),('PRIMARY_fresh_emcee_R03',FP['bands']),('REPLACEMENT_reweighted_chain(=R02 CTC-5B recomputed)',RW['bands']),('REPLACEMENT_fresh_emcee_R03',FR['bands'])]:
        for z in ALL:
            for k in ['DM/rd','DH/rd','DM/DH']: w.writerow([lab,z,k]+['%.5f'%x for x in q(b[z],k)])
json.dump(row,open('calc/cpl_row_r03.json','w'),indent=1)
