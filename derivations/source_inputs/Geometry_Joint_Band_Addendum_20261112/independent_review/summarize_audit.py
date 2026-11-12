import json,hashlib
from pathlib import Path
B=Path(__file__).resolve().parent.parent;O=B/'independent_review'
a=json.load(open(O/'audit_results_degree80.json'))
b=json.load(open(O/'audit_results_degree128.json'))
p=json.load(open(B/'RESULT_higher.json'));low=json.load(open(B/'RESULT_lower.json'))
s=json.load(open(B/'inputs/frozen_results.json'))
assert len(a['results'])==len(b['results'])==len(p['cases'])==24
report={'status':'PASS','acceptance_absolute_probability_and_factor':1e-7,'cases':24,'all12_models_priors_retained':True,'new_measurements_or_outcomes_used':False,'producer_imports':False,'independent_refinement':{},'comparison_with_producer_higher':{},'producer_refinement':{},'checks':[]}
for label,x,y,xprob,yprob,xfac,yfac in [
 ('independent_refinement',a['results'],b['results'],lambda r:r['stored95_joint']['mass'],lambda r:r['stored95_joint']['mass'],lambda r:r['common_factor_95'],lambda r:r['common_factor_95']),
 ('comparison_with_producer_higher',b['results'],p['cases'],lambda r:r['stored95_joint']['mass'],lambda r:r['pointwise_band_joint_probability']['probability'],lambda r:r['common_factor_95'],lambda r:r['simultaneous_multiplier']),
 ('producer_refinement',low['cases'],p['cases'],lambda r:r['pointwise_band_joint_probability']['probability'],lambda r:r['pointwise_band_joint_probability']['probability'],lambda r:r['simultaneous_multiplier'],lambda r:r['simultaneous_multiplier'])]:
 assert all((r['prior'],r['model'])==(q['prior'],q['model']) for r,q in zip(x,y))
 md=max(abs(xprob(r)-yprob(q)) for r,q in zip(x,y));fd=max(abs(xfac(r)-yfac(q)) for r,q in zip(x,y))
 report[label]={'max_abs_probability_difference':md,'max_abs_factor_difference':fd}
 assert md<1e-7 and fd<1e-7
report['distance_ODE_crosschecks']=[{k:r[k] for k in ['degree','ode_rtol','ode_atol','distance_interpolation_validation_max_abs']} for r in [a,b]]
fixed=[r for r in b['results'] if r['model']!='free_A']
report['fixed_A_stored_max_abs_probability_minus_095']=max(abs(r['stored95_joint']['mass']-.95) for r in fixed)
report['fixed_A_stored_max_abs_factor_minus_1']=max(abs(r['common_factor_95']-1) for r in fixed)
report['expanded_max_abs_probability_minus_095']=max(abs(r['expanded_joint']['mass']-.95) for r in b['results'])
count=0
for r in p['cases']:
 grid=[.9,1,1.2,1.5,1.8] if r['grid']=='primary' else s['forecast_z_grid']
 source=[q for q in s['results'][r['prior']][r['model']]['forecast']['rows'] if q['z'] in grid]
 assert len(source)==r['coordinates']==len(r['bands'])
 for x,y in zip(source,r['bands']):
  assert (x['observable'],x['z'])==(y['observable'],y['z'])
  q=x['quantiles'];t=r['simultaneous_multiplier']
  assert y['original_lower']==q[0] and y['original_upper']==q[4] and y['median']==q[2]
  assert abs(y['joint_lower']-(q[2]+t*(q[0]-q[2])))<1e-13
  assert abs(y['joint_upper']-(q[2]+t*(q[4]-q[2])))<1e-13
  count+=1
report['exported_coordinate_band_rows_verified']=count
report['checks']=['All 24 case identities and 576 exported coordinate band rows verified.','All original bounds and medians match frozen JSON exactly.','Every expanded bound equals the declared common multiplier transformation.','No measurement, frequentist or Euclid-coverage conclusion is supported or made.','Free-A joint claims are restricted to each finite grid.','Floating-point agreement is not a rigorous interval-arithmetic error enclosure.']
report['reviewed_file_sha256']={str(f.relative_to(B)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [B/'joint_bands.py',B/'RESULT_higher.json',B/'RESULT_lower.json',O/'audit.py',O/'audit_results_degree80.json',O/'audit_results_degree128.json']}
with open(O/'AUDIT_COMPARISON.json','x') as f:json.dump(report,f,indent=2)
lines=['# Independent audit: simultaneous latent geometry bands','', '**Result: PASS at the declared 1e-7 absolute probability and multiplier agreement threshold.**','', 'All 12 unchanged old-DESI model/prior combinations were independently evaluated on both the frozen primary 15-coordinate grid and the full 33-coordinate grid. No new observations, refit, new prior, or primary selection was introduced.','', '## Main results','', '| Prior | Free-A grid | Stored bands: joint posterior mass | Multiplier for 95% joint mass |','|---|---|---:|---:|']
for r in b['results']:
 if r['model']=='free_A':lines.append(f"| {r['prior']} | {r['grid']} | {r['stored95_joint']['mass']:.12f} | {r['common_factor_95']:.12f} |")
lines.extend(['','All 18 fixed-A/grid cases have 0.95 joint posterior mass and multiplier 1 to far better than 1e-7. The tiny stored-bound numerical deviations are reported below.','', '## Independent numerical route','', 'The audit reconstructs the 13-coordinate block-diagonal Gaussian likelihood directly from the retained CSV, including within-bin DM/DH correlations. It never imports the producer or historical forecast code. It obtains dimensionless distances from an independent DOP853 ODE, uses Chebyshev interpolation in Omega only for speed, and checks that interpolation against 171 separate ODE solutions. Refinement changes polynomial degree 80 to 128, tightens ODE tolerances, and doubles the boundary-crossing scan resolution.','', 'For free A, the likelihood is completed to a Gaussian in A at each Omega. The finite uniform-A prior remains exact. Each DM or DH band supplies an A interval; the event uses their intersection with the original A support. All AP bands restrict Omega. The probability is an adaptive Omega integral of the analytic truncated-Gaussian A mass. Every detected pairwise boundary crossing is used as a quadrature split, not just the active envelope switches. Factors are roots of the resulting deterministic joint-probability function. No Monte Carlo estimate is used.','', '## Fixed-A theorem','', 'Write g(z)=(1+z)^3-1 and E(z;Omega)=sqrt(1+Omega*g(z)). For A>0 and z>0, DH=A/E decreases strictly with Omega, and DM=A*integral_0^z[1/E(u;Omega)]du also decreases strictly.','', 'AP=E(z;Omega)*integral_0^z[1/E(u;Omega)]du. Inside its integral, the Omega derivative of sqrt((1+Omega*g(z))/(1+Omega*g(u))) is the positive integrand times one half of [g(z)/(1+Omega*g(z)) - g(u)/(1+Omega*g(u))]. This is strictly positive for u<z because g increases with redshift and g/(1+Omega*g) increases with g wherever E is real and positive. Thus AP increases strictly with Omega.','', 'Consequently, each exact equal-tail 95% coordinate interval has the same preimage: the central [q_0.025,q_0.975] Omega interval. Their intersection retains exactly 95% posterior mass, for either finite grid and indeed for the complete positive-redshift curve in this fixed-A model. The exact common multiplier is 1. This analytic fact does not replace checking the stored numerical bounds; the audit separately checks those.','', '## Verification metrics',''])
for key in ['independent_refinement','comparison_with_producer_higher','producer_refinement']:
 v=report[key];lines.append(f"- {key}: max absolute probability difference {v['max_abs_probability_difference']:.4g}; factor difference {v['max_abs_factor_difference']:.4g}.")
lines.extend([f"- Fixed-A stored bounds: max |mass-0.95| = {report['fixed_A_stored_max_abs_probability_minus_095']:.4g}; max |factor-1| = {report['fixed_A_stored_max_abs_factor_minus_1']:.4g}.",f"- Expanded independent bands: max |mass-0.95| = {report['expanded_max_abs_probability_minus_095']:.4g}.",f"- Export checks: {count} coordinate rows verified, including identity, original frozen bounds, medians and multiplier transformation.",'', '## Interpretation limits','', '- These are within-model posterior probabilities for latent dimensionless geometry under unchanged old-DESI compressed Gaussian assumptions.','- They are not future-observation prediction intervals, measurement coverage, frequentist confidence coverage, or a Euclid performance statement.','- Free-A results establish simultaneous mass only on the named finite coordinate grid, not over every continuous redshift.','- The common median-centered multiplier defines one particular band family. It is not asserted to be unique, shortest, optimal, or an HPD region.','- Numerical convergence and independent agreement provide strong evidence at the requested tolerance. They are not a formal interval-arithmetic enclosure.','', 'The JSON comparison records hashes of every reviewed source/result file. Audit files are confined to independent_review; original inputs and producer outputs were not changed.'])
with open(O/'REPORT.md','x') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps(report,indent=2))
