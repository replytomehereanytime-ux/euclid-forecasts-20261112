# Compare R02 table predictive bands (CTC rows) with reviewer Laplace (verify_fits) and reviewer MCMC (verify_mcmc).
import csv, re, json, numpy as np
T={r['id']:r for r in csv.DictReader(open('/workspace/r03-out/euclid_forecast_bot/R02/FORECAST_TABLE_R02.csv'))}
L=json.load(open('verify_fits_R02_output.json'))
M={}; [M.update(json.load(open(f))) for f in ('verify_mcmc_R02_wCDM_PRIM+wCDM_REPL+oLCDM_PRIM+oLCDM_REPL.json','verify_mcmc_R02_CPL_REPL+CPL_PRIM.json')]
rowmap={'CTC-2P':'LCDM_PRIM','CTC-2B':'LCDM_REPL','CTC-3P':'wCDM_PRIM','CTC-3B':'wCDM_REPL','CTC-4P':'oLCDM_PRIM','CTC-4B':'oLCDM_REPL','CTC-5B':'CPL_REPL','CTC-5P':'CPL_PRIM'}
lab=[f'{q}@{z}' for z in (0.9,1.2,1.5,1.8) for q in ('DM/rd','DH/rd')]
out={}; lines=[]
for rid,key in rowmap.items():
    txt=T[rid]['predictive distribution (with uncertainty)']
    pm=[(float(a),float(b)) for a,b in re.findall(r'(\d+\.\d+) ± (\d+\.\d+)',txt)]
    if not pm:
        iv=re.findall(r'(\d+\.\d+) \[(\d+\.\d+), (\d+\.\d+)\]',txt); pm=[(float(a),(float(c)-float(b))/2) for a,b,c in iv]
    lm=L[key]['pred_mean']; ls=L[key]['pred_sig']
    mm=[x[1] for x in M[key]['pred_p16_50_84']] if key in M else [None]*8
    ms=[(x[2]-x[0])/2 for x in M[key]['pred_p16_50_84']] if key in M else [None]*8
    rec=[]
    for i in range(8):
        r02=pm[i] if i<len(pm) else (None,None)
        rec.append({'q':lab[i],'R02_mean':r02[0],'R02_sig':r02[1],'rev_laplace_mean':lm[i],'rev_laplace_sig':ls[i],'rev_mcmc_median':mm[i],'rev_mcmc_halfwidth68':ms[i]})
    out[rid]=rec
    if pm:
        dmax=max(abs(rec[i]['R02_mean']-lm[i]) for i in range(len(pm)))
        sr=[rec[i]['R02_sig']/ls[i] for i in range(len(pm))]
        mr=[ (rec[i]['R02_mean']-mm[i])/rec[i]['R02_sig'] for i in range(len(pm))] if mm[0] else []
        hr=[rec[i]['R02_sig']/ms[i] for i in range(len(pm))] if ms[0] else []
        lines.append(f"{rid} ({key}): max|R02 mean - rev Laplace mean|={dmax:.4f}; R02 sig / rev Laplace sig in [{min(sr):.3f},{max(sr):.3f}]"+(f"; (R02 mean - MCMC median)/R02 sig in [{min(mr):.2f},{max(mr):.2f}]; R02 sig / MCMC halfwidth in [{min(hr):.3f},{max(hr):.3f}]" if mr else ''))
    else: lines.append(f"{rid}: R02 has no band (MISSING); reviewer MCMC median/68% supplied in compare_bands_R02_output.json")
json.dump(out,open('compare_bands_R02_output.json','w'),indent=1)
print('\n'.join(lines))
for rid in ('CTC-5P',):
    print(rid,[ (r['q'],round(r['rev_mcmc_median'],3),round(r['rev_mcmc_halfwidth68'],3)) for r in out[rid]])
