from pathlib import Path
import json,csv,hashlib
ROOT=Path(__file__).resolve().parent
A=json.loads((ROOT/'RESULT_lower.json').read_text());B=json.loads((ROOT/'RESULT_higher.json').read_text())
assert len(A['cases'])==len(B['cases'])==24
keys=lambda c:(c['prior'],c['model'],c['grid'])
low={keys(c):c for c in A['cases']};hi={keys(c):c for c in B['cases']};assert set(low)==set(hi)
maxima={name:0. for name in ['producer_joint_mass_change','producer_factor_change','expanded_mass_error','fixed_A_stored_mass_error','fixed_A_factor_from_one']}
for k,c in hi.items():
 d=low[k]
 maxima['producer_joint_mass_change']=max(maxima['producer_joint_mass_change'],abs(c['pointwise_band_joint_probability']['probability']-d['pointwise_band_joint_probability']['probability']))
 maxima['producer_factor_change']=max(maxima['producer_factor_change'],abs(c['simultaneous_multiplier']-d['simultaneous_multiplier']))
 maxima['expanded_mass_error']=max(maxima['expanded_mass_error'],abs(c['expanded_band_joint_probability']['probability']-.95))
 assert c['coordinates']==(15 if c['grid']=='primary' else 33)
 if c['model']!='free_A':
  maxima['fixed_A_stored_mass_error']=max(maxima['fixed_A_stored_mass_error'],abs(c['pointwise_band_joint_probability']['probability']-.95))
  maxima['fixed_A_factor_from_one']=max(maxima['fixed_A_factor_from_one'],abs(c['simultaneous_multiplier']-1))
 for band in c['bands']:
  assert band['original_lower']<band['median']<band['original_upper']
  assert abs((band['joint_upper']-band['median'])/(band['original_upper']-band['median'])-c['simultaneous_multiplier'])<1e-11
  assert abs((band['median']-band['joint_lower'])/(band['median']-band['original_lower'])-c['simultaneous_multiplier'])<1e-11
ind=json.loads((ROOT/'independent_review/audit_results_degree128.json').read_text())
indkeys=lambda c:(c['prior'],c['model'],{'primary15':'primary','all33':'all_frozen'}[c['grid']])
im={indkeys(c):c for c in ind['results']};assert set(im)==set(hi)
maxima['independent_joint_mass_difference']=max(abs(c['pointwise_band_joint_probability']['probability']-im[k]['stored95_joint']['mass']) for k,c in hi.items())
maxima['independent_factor_difference']=max(abs(c['simultaneous_multiplier']-im[k]['common_factor_95']) for k,c in hi.items())
assert all(v<1e-7 for v in maxima.values()),maxima
summary={'status':'PASS_ALL_24_FROZEN_CASES','cases':24,'numerical_tolerance':1e-7,'maximum_absolute_differences':maxima,'source_preservation':{},'free_A':[],'fixed_A':'All18 model/prior/grid cases agree with joint0.95 and multiplier1 within reported numerical residuals. Exact monotonicity theorem concerns unrounded exact quantiles.','scope':'Joint latent posterior mass only; no empirical/frequentist/Euclid coverage.'}
plan=json.loads((ROOT/'PLAN.json').read_text())
for n,d in plan['source_files'].items():
 actual=hashlib.sha256((ROOT/n).read_bytes()).hexdigest();assert actual==d['sha256'];summary['source_preservation'][n]=actual
for k,c in hi.items():
 if c['model']=='free_A':summary['free_A'].append({'prior':c['prior'],'grid':c['grid'],'coordinates':c['coordinates'],'original_joint_mass':c['pointwise_band_joint_probability']['probability'],'factor':c['simultaneous_multiplier'],'relative_halfwidth_increase_percent':100*(c['simultaneous_multiplier']-1),'new_joint_mass':c['expanded_band_joint_probability']['probability']})
(ROOT/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
fields=['prior','model','grid','observable','z','median','original_lower','original_upper','joint_lower','joint_upper','common_multiplier']
with (ROOT/'JOINT_BANDS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for c in B['cases']:
  for b in c['bands']:w.writerow({'prior':c['prior'],'model':c['model'],'grid':c['grid'],**b,'common_multiplier':c['simultaneous_multiplier']})
print(json.dumps(summary,indent=2))
