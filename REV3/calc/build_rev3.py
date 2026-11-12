import json,csv
J=json.load(open('rows_rev3_rescale.json')); C=json.load(open('rows_rev3_chen_zfix.json'))['REPLACEMENT']
G=json.load(open('growth_rev3_rescale.json')); GL=json.load(open('growth_like_r03_rescale.json')); K=json.load(open('control_rev3.json'))
O3=json.load(open('../../R03/calc/fullrs_r03_output.json'))
Z=['0.9','1.2','1.5','1.8']
FAB={'Om':0.3009,'h':0.6843,'DM':[21.166,26.085,30.243,33.798],'DH':[17.868,15.032,12.779,10.987],'s8':0.817,'S8':0.818}
REV2={'CTC-2P':([21.1420,26.0500,30.1982,33.7434],[17.8307,14.9964,12.7452,10.9570]),'CTC-2B':([21.1601,26.0691,30.2173,33.7622],[17.8358,14.9977,12.7447,10.9555]),
 'CTC-3P':([21.1264,26.0490,30.2083,33.7614],[17.8837,15.0394,12.7765,10.9786]),'CTC-3B':([21.1458,26.0687,30.2276,33.7800],[17.8867,15.0389,12.7746,10.9762]),
 'CTC-4P':([21.0984,25.9919,30.1279,33.6631],[17.7697,14.9403,12.6954,10.9131]),'CTC-4B':([21.1152,26.0096,30.1458,33.6808],[17.7749,14.9421,12.6954,10.9122]),
 'CTC-5P':([21.049,25.968,30.161,33.753],[17.761,15.106,12.904,11.106]),'CTC-5B':([21.087,26.007,30.193,33.777],[17.789,15.093,12.877,11.080])}
ROWS=[('CTC-2B','REPLACEMENT','LCDM','Flat ΛCDM, BAO + calibrated compressed CMB'),('CTC-2P','PRIMARY','LCDM','Flat ΛCDM, BAO + calibrated compressed CMB'),
 ('CTC-3B','REPLACEMENT','wCDM','Flat wCDM (constant w), BAO + calibrated compressed CMB'),('CTC-3P','PRIMARY','wCDM','Flat wCDM (constant w), BAO + calibrated compressed CMB'),
 ('CTC-4B','REPLACEMENT','oLCDM','oΛCDM (free Ωk), BAO + calibrated compressed CMB'),('CTC-4P','PRIMARY','oLCDM','oΛCDM (free Ωk), BAO + calibrated compressed CMB'),
 ('CTC-5B','REPLACEMENT','CPL','CPL w0waCDM, BAO + calibrated compressed CMB'),('CTC-5P','PRIMARY','CPL','CPL w0waCDM, BAO + calibrated compressed CMB')]
f4=lambda x:f'{x:.4f}'; f2=lambda x:f'{x:.2f}'
def eff(e):
    big=[x for x in e if x>0.01]; small=[x for x in e if 1e-3<x<=0.01]; return len(big),len(small)
lines=[]; status=[]; shifts=[]
for rid,br,mod,title in ROWS:
    r=J[br][mod]; d=r['dist']; cpl=mod=='CPL'; brl='DECLARED REPLACEMENT (current-information forecast; DESI DR2 BAO with Lyα z=2.33 replaced by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ +0.225)' if br=='REPLACEMENT' else 'FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)'
    L=[f'### {rid}-REV3 — {title} ({"current-information forecast" if br=="REPLACEMENT" else "legacy comparison only"})','',
       '- **Author:** C.A.S.D.R','- **Wording:** prospective, model-conditional','- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row '+rid+'-R03.',
       f'- **Branch:** {brl}','- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)',
       '- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.','- **Numeric prediction:**']
    for i,z in enumerate(Z):
        if cpl:
            a=d[z]['DM/rd']['q16_50_84']; b=d[z]['DH/rd']['q16_50_84']
            L.append(f'  - z={z}: DM/rd {f2(a[1])} [{f2(a[0])}, {f2(a[2])}], DH/rd {f2(b[1])} [{f2(b[0])}, {f2(b[2])}]')
        else:
            L.append(f'  - z={z}: DM/rd {f4(d[z]["DM/rd"]["q16_50_84"][1])} ± {f4(d[z]["DM/rd"]["sd"])}, DH/rd {f4(d[z]["DH/rd"]["q16_50_84"][1])} ± {f4(d[z]["DH/rd"]["sd"])}')
    P=r['params']; pm=lambda k,n=4: f'{P[k]["q16_50_84"][1]:.{n}f} [{P[k]["q16_50_84"][0]:.{n}f}, {P[k]["q16_50_84"][2]:.{n}f}]'
    mc=r['mcmc']
    if cpl:
        L.append(f'- **Band:** MCMC posterior median and 68% interval only (two decimals). emcee {mc["nwalkers"]}×{mc["steps"]}, burn {mc["burn"]}, thin {mc["thin"]}, N = {mc["N"]}, seed 20261112. No 95% band is published.')
        L.append(f'- **CPL prior-edge note:** the posterior touches the wa > −4 prior edge: {100*r["frac_wa_below_-3.5"]:.2f}% of samples have wa < −3.5; w0 + wa < 0 is imposed. The 68% bands depend on these priors.')
        L.append(f'- **Conditional-fit parameters (16/50/84, not scored):** Ωm {pm("Om")}, h {pm("h")}, w0 {pm("w0",3)}, wa {pm("wa",3)}, ω_b {pm("ob",5)}')
    else:
        L.append(f'- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee {mc["nwalkers"]}×{mc["steps"]}, burn {mc["burn"]}, N = {mc["N"]}, seed 20261112. Laplace widths from REV2 are not used.')
        extra=''
        if mod=='wCDM': extra=f', w {P["w0"]["q16_50_84"][1]:.4f} ± {P["w0"]["sd"]:.4f} (MCMC median ± s.d.)'
        if mod=='oLCDM': extra=f', Ωk {P["Ok"]["q16_50_84"][1]:+.4f} ± {P["Ok"]["sd"]:.4f} (MCMC median ± s.d.; **magnitude not robust**, see notes)'
        L.append(f'- **Conditional-fit parameters (not scored):** Ωm {P["Om"]["q16_50_84"][1]:.4f} ± {P["Om"]["sd"]:.4f}, h {P["h"]["q16_50_84"][1]:.4f} ± {P["h"]["sd"]:.4f}, Ωm h² {P["omh2"]["q16_50_84"][1]:.4f}{extra}')
    nb,ns=eff(r['pred_corr_eigs'])
    L.append(f'- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has {nb} large and {ns} small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.')
    L.append(''); lines+=L
    o2=REV2[rid]; md=[d[z]['DM/rd']['q16_50_84'][1] for z in Z]; mh=[d[z]['DH/rd']['q16_50_84'][1] for z in Z]
    shifts.append((rid,br,mod,[m-o for m,o in zip(md,o2[0])],[m-o for m,o in zip(mh,o2[1])]))
    if rid=='CTC-2B':
        bf=r['bestfit']; dm=[d[z]['DM/rd']['bestfit'] for z in Z]; dh=[d[z]['DH/rd']['bestfit'] for z in Z]
        sd=[d[z]['DM/rd']['sd'] for z in Z]+[d[z]['DH/rd']['sd'] for z in Z]
        diffs=[a-b for a,b in zip(dm+dh,FAB['DM']+FAB['DH'])]
        ok=all(abs(x)<=max(0.1*s,0.0005*v) for x,s,v in zip(diffs,sd,FAB['DM']+FAB['DH'])) and abs(bf['Om']-FAB['Om'])<0.001 and abs(bf['h']-FAB['h'])<0.001
        status.append([rid+'-REV3',br,mod,'PASS' if ok else 'FAIL',f'best fit Ωm {bf["Om"]:.4f} h {bf["h"]:.4f} vs Fable 0.3009/0.6843; DM/rd {"/".join(f"{x:.3f}" for x in dm)} vs 21.166/26.085/30.243/33.798; DH/rd {"/".join(f"{x:.3f}" for x in dh)} vs 17.868/15.032/12.779/10.987; max abs difference {max(map(abs,diffs)):.4f}'])
    else:
        status.append([rid+'-REV3',br,mod,'RECOMPUTED; Fable comparison NOT_RUN','no independent Fable number for this row'])
json.dump({'lines':lines,'status':status,'shifts':shifts},open('build_parts.json','w'),indent=1,ensure_ascii=False)
for s in status: print(s)
for s in shifts: print(s[0],s[1],[round(x,4) for x in s[3]],[round(x,4) for x in s[4]])
print('chen vs rescale LCDM DM max diff',max(abs(C['LCDM']['dist'][z]['DM/rd']['q16_50_84'][1]-J['REPLACEMENT']['LCDM']['dist'][z]['DM/rd']['q16_50_84'][1]) for z in Z))
