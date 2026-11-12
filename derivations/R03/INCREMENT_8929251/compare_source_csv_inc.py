"""Compare R03 independent computations with the author's Best_Defensible_Forecast_Handoff CSVs (read-only inputs; hashes recorded)."""
import csv, json, hashlib
S='/workspace/r03-out/euclid_20261112/source_inputs_8930243/unpacked/Best_Defensible_Forecast_Handoff_20261112/'
sha=lambda p: hashlib.sha256(open(p,'rb').read()).hexdigest()
IN={f:sha(S+f) for f in ['july_replacement_geometry.csv','july_replacement_parameters.csv','geometry_forecasts.csv','july_joint_geometry.csv','july_joint_parameters.csv','BEST_FORECAST_HANDOFF.md']}
rep=json.load(open('freeA_lcdm_table4_inc_output.json')); old=json.load(open('freeA_lcdm_table4_old_inc_output.json'))
box=json.load(open('freeA_lcdm_inc_output.json'))
K={'DM_over_rd':'DM/rd','DH_over_rd':'DH/rd','F_AP':'F_AP'}; ZH=['0.9','1.0','1.2','1.5','1.8']
def zkey(z): return str(float(z))
out={'inputs_sha256':IN,'rows':[]}
G=list(csv.DictReader(open(S+'july_replacement_geometry.csv')))
for r in G:
    if r['model']!='LCDM_free_A' or r['observable'] not in K: continue
    z=zkey(r['z'])
    if z not in ZH: continue
    src={'replacement_AP_BAO':rep,'old_BAO':old['T4_OLD']}[r['calibration']]
    m,s=src['rows'][z]['post_mean_sd'][K[r['observable']]]
    bx=(box['REPLACEMENT'] if r['calibration']=='replacement_AP_BAO' else box['PRIMARY'])['rows'][z]['post_mean_sd'][K[r['observable']]]
    am=src['rows'][z]['at_mean_params'][K[r['observable']]]
    out['rows'].append({'file':'july_replacement_geometry.csv','calibration':r['calibration'],'obs':r['observable'],'z':z,'source_mean':float(r['latent_mean']),'source_sd':float(r['parameter_only_SD']),
        'r03_table4_mean':m,'r03_table4_sd':s,'d_mean':m-float(r['latent_mean']),'d_sd':s-float(r['parameter_only_SD']),'r03_boxcov_mean':bx[0],'r03_boxcov_sd':bx[1],'r03_at_mean_params':am,'at_mean_minus_integrated':am-m})
# historical primary medians (geometry_forecasts.csv, prior=primary, model=free_A)
for r in csv.DictReader(open(S+'geometry_forecasts.csv')):
    if r['prior']!='primary' or r['model']!='free_A' or r['observable'] not in K: continue
    z=zkey(r['z'])
    if z not in ZH: continue
    me=old['T4_OLD']['rows'][z]['post_median'][K[r['observable']]]
    out['rows'].append({'file':'geometry_forecasts.csv','calibration':'primary(old_BAO)','obs':r['observable'],'z':z,'source_median':float(r['median']),'r03_median':me,'d_median':me-float(r['median']),'source_mean':float(r['mean']),'r03_mean':old['T4_OLD']['rows'][z]['post_mean_sd'][K[r['observable']]][0]})
# parameters
P=list(csv.DictReader(open(S+'july_replacement_parameters.csv')))
out['params']=[r for r in P if r['model'] in ('LCDM_free_A','wCDM_free_A')]
json.dump(out,open('compare_source_csv_inc_output.json','w'),indent=1)
mx=lambda key,f: max(abs(x[key]) for x in out['rows'] if x['file']==f and key in x)
print('max |d_mean| july_replacement_geometry (table4 input):',mx('d_mean','july_replacement_geometry.csv'),' max |d_sd|:',mx('d_sd','july_replacement_geometry.csv'))
print('max |d_median| historical primary:',mx('d_median','geometry_forecasts.csv'))
print('max |at_mean - integrated|:',mx('at_mean_minus_integrated','july_replacement_geometry.csv'))
for p in out['params']: print(p)
