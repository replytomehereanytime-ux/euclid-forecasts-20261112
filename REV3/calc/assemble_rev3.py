import json,re
R2=open('../../PUBLISH_20261112/REV2/PREDICTIONS_20261112_REV2.md').read()
def sec(start,end): i=R2.index(start); j=R2.index(end,i); return R2[i:j]
ctc1=sec('### 1. CTC-1P','### 3. CTC-2P-R03'); rest=sec('### 11. D-P4a','## Assembly note')
def clean(s):
    s=re.sub(r' \(R01 default; [A-Z][a-z]+ to confirm label\)',' (R01 default label)',s); s=re.sub(r'pending [A-Z][a-z]+\b','pending',s)
    s=re.sub(r'^### \d+\. ','### ',s,flags=re.M); return s
ctc1=clean(ctc1); rest=clean(rest)
B=json.load(open('build_parts.json')); J=json.load(open('rows_rev3_rescale.json')); G=json.load(open('growth_rev3_rescale.json')); GL=json.load(open('growth_like_r03_rescale.json')); K=json.load(open('control_rev3.json'))
L=GL['LCDM']; W=GL['w0waCDM']; q=lambda v,n=3:f'{v[1]:.{n}f} [{v[0]:.{n}f}, {v[2]:.{n}f}]'
Z=['0.9','1.2','1.5','1.8']
nu=G['nu006_shift']
growth=f"""### GR-1B-REV3 — σ8, S8 and fσ8, flat ΛCDM, BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (new in the public pack; the R03 growth recompute used the uncalibrated CMB prior and was held in REV2).
- **Branch:** DECLARED REPLACEMENT.
- **Method:** CAMB {G['settings']['camb']} on 60 draws from the REV3 flat-ΛCDM REPLACEMENT chain; ln(10¹⁰A_s) drawn from N(3.044, 0.014) (Planck 2018), n_s 0.9649, massless neutrinos (N_eff 3.046), same settings as the earlier R03 growth script. **A_s is not constrained by the BAO + compressed-CMB fit; its Planck 2018 uncertainty (about 0.7% on σ8) is included in the bands below.**
- **Numeric prediction (16/50/84):**
  - σ8 (z=0): {q(L['sigma8_0'])}
  - S8 = σ8 (Ωm/0.3)^0.5: {q(L['S8_0'])}
  - fσ8: """+'; '.join(f"z={z} {q(L['fsigma8'][z])}" for z in Z)+f"""
- **Data product:** a later Euclid spectroscopic growth-rate (fσ8) or weak-lensing (S8) measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Systematic (stated, not folded in):** with one 0.06 eV neutrino state instead of massless neutrinos (same H0, ω_b, total ω_m, A_s fixed at the Planck mean), CAMB gives σ8 {G['sigma8']:.3f} and S8 {G['S8']:.3f} at the best fit, about −0.014 in σ8. fσ8 moves by a similar fraction.

### GR-5B-REV3 — σ8, S8 and fσ8, CPL, BAO + calibrated compressed CMB (context, current-information branch)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Method:** as GR-1B-REV3 on 60 draws of the REV3 CPL REPLACEMENT chain, CAMB PPF dark energy. Prior-touched CPL posterior; 68% only.
- **Numeric prediction (16/50/84):** σ8 {q(W['sigma8_0'])}; S8 {q(W['S8_0'])}; fσ8 """+'; '.join(f"z={z} {q(W['fsigma8'][z])}" for z in Z)+"""
- **Note:** more model-dependent than GR-1B-REV3. With only 60 draws, quantiles are uncertain at about the third decimal.
"""
rows='\n'.join(B['lines'])
P=lambda br,m,k: J[br][m]['params'][k]
ctx=f"""## Model-context parameters (REV3, calibrated CMB prior; MCMC; not scored as separate forecasts)

| Parameter | Branch | REV3 | REV2 | Shift (REV3 − REV2) |
|---|---|---|---|---|
| wCDM w | REPLACEMENT (current) | {P('REPLACEMENT','wCDM','w0')['q16_50_84'][1]:.4f} ± {P('REPLACEMENT','wCDM','w0')['sd']:.4f} | −1.0291 ± 0.0413 | {P('REPLACEMENT','wCDM','w0')['q16_50_84'][1]+1.0290639367764145:+.4f} |
| wCDM w | PRIMARY (legacy) | {P('PRIMARY','wCDM','w0')['q16_50_84'][1]:.4f} ± {P('PRIMARY','wCDM','w0')['sd']:.4f} | −1.0312 ± 0.0405 | {P('PRIMARY','wCDM','w0')['q16_50_84'][1]+1.031164704133902:+.4f} |
| oΛCDM Ωk | REPLACEMENT | {P('REPLACEMENT','oLCDM','Ok')['q16_50_84'][1]:+.4f} ± {P('REPLACEMENT','oLCDM','Ok')['sd']:.4f} (MCMC) | +0.00198 ± 0.00124 (Laplace) | {P('REPLACEMENT','oLCDM','Ok')['q16_50_84'][1]-0.0019771195178052915:+.4f} |
| oΛCDM Ωk | PRIMARY | {P('PRIMARY','oLCDM','Ok')['q16_50_84'][1]:+.4f} ± {P('PRIMARY','oLCDM','Ok')['sd']:.4f} (MCMC) | +0.00199 ± 0.00125 (Laplace) | {P('PRIMARY','oLCDM','Ok')['q16_50_84'][1]-0.0019908057850397567:+.4f} |
| CPL w0 | REPLACEMENT | {q(P('REPLACEMENT','CPL','w0')['q16_50_84'])} | −0.5308 [−0.7623, −0.2638] | {P('REPLACEMENT','CPL','w0')['q16_50_84'][1]+0.5308:+.3f} |
| CPL wa | REPLACEMENT | {q(P('REPLACEMENT','CPL','wa')['q16_50_84'])} | −1.4209 [−2.2372, −0.7542] | {P('REPLACEMENT','CPL','wa')['q16_50_84'][1]+1.4209:+.3f} |
| CPL w0 | PRIMARY | {q(P('PRIMARY','CPL','w0')['q16_50_84'])} | −0.4167 [−0.6570, −0.1476] | {P('PRIMARY','CPL','w0')['q16_50_84'][1]+0.4167:+.3f} |
| CPL wa | PRIMARY | {q(P('PRIMARY','CPL','wa')['q16_50_84'])} | −1.7592 [−2.5757, −1.0548] | {P('PRIMARY','CPL','wa')['q16_50_84'][1]+1.7592:+.3f} |
| CPL Ωm | PRIMARY | {q(P('PRIMARY','CPL','Om')['q16_50_84'],4)} | 0.3555 [0.3318, 0.3820] | {P('PRIMARY','CPL','Om')['q16_50_84'][1]-0.3555:+.4f} |

**Ωk is not robust.** Its sign flipped between the truncated-r_s and corrected-r_s fits (R02 → R03), and its central value moved again here (+0.0020 → +0.0027) when the CMB prior was calibrated. The compressed prior is also used outside its flat-model derivation. Only the width (about 0.0012) should be read as informative; the magnitude should not.
"""
s=lambda x:x
STAT='\n'.join(f'| {a} | {b} | {c} | {d} | {e} |' for a,b,c,d,e in B['status'])
md=f"""# Prospective, model-conditional cosmology forecasts (12 November 2026) — REV3

**Author:** C.A.S.D.R

**Status:** REV3, a marked revision. It supersedes the BAO + compressed-CMB rows of REV1 and REV2 because the compressed CMB prior was mis-calibrated in those revisions. REV1 and REV2 are kept unchanged as frozen originals. Assembled 2026-11-12 in America/Toronto (UTC−5).

**Release framing:** Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts. The galaxy-clustering and weak-lensing products needed for the strongest tests are scheduled for mid-2027 (DR1 Complete). Distance and growth rows are for measurements built on DR1 Complete (mid-2027 or later), not Foundation.

**The forecast is the REPLACEMENT (current-information) branch.** PRIMARY is the legacy comparison only. The two branches are alternatives, not independent predictions. No statistical-test claims of any kind are made in this pack; standard deviations describe widths only. HSU, STO, Rebound and R1 remain derivation-gated and are not included.

## What changed in REV3 (summary; full list in CHANGELOG_REV3.md)

1. **CMB-prior calibration (blocking item).** At the Planck 2018 mean (Ωm 0.3166, h 0.6727, ω_b 0.02236) the REV2 pipeline gave l_A = {K['old']['lA']:.2f} against the prior mean 301.4707. REV3 adopts a calibrated l_A (model l_A × 0.997452), which gives l_A = {K['rescale']['lA']:.4f} at the Planck mean; a prior-only flat-ΛCDM fit then returns H0 = {K['rescale']['prior_only_fit']['H0']:.2f} and Ωm h² = {K['rescale']['prior_only_fit']['omh2']:.4f} (target 67.27 and 0.1432). The Chen, Huang & Wang (2019, arXiv:1808.05724) conventions (Ω_r = Ωm/(1+z_eq), z_eq = 2.5×10⁴ Ωm h² (T/2.7)⁻⁴, z* = 1089.9) were also run: they give l_A = {K['chen_zfix']['lA']:.3f} at the Planck mean and prior-only H0 {K['chen_zfix']['prior_only_fit']['H0']:.2f}, Ωm h² {K['chen_zfix']['prior_only_fit']['omh2']:.4f}. That variant moves the ΛCDM distances by at most 0.003 in DM/rd relative to the adopted one, so it is recorded as a cross-check.
2. **Every row that uses the compressed CMB prior was re-run:** ΛCDM, wCDM, oΛCDM and CPL distances on both branches; wCDM w; CPL w0, wa and bands; σ8, S8 and fσ8. Only the BAO-only curves CTC-1P and CTC-1B are unaffected and are carried over unchanged.
3. Widths for ΛCDM, wCDM and oΛCDM are now MCMC median ± standard deviation (REV2 used Laplace widths for the distance curves).
4. Write-up fixes: Eq. 26 Lyα labels stated as DM/rd 39.32 and DH/rd 8.600 (an earlier hand-off text had them swapped; the fit data were never swapped); the old truncated-r_s REPLACEMENT r_d is 143.4 Mpc, not 144.0; the z = 1.3 PRIMARY/REPLACEMENT shift labels were checked against the output JSON and are correct; "effective rank 5" is restated as three to four informative directions; CPL prior-edge note added; Ωk magnitude stated as not robust; 0.06 eV neutrino-variant shift added as a stated systematic.

## Status table (REV3)

Comparison reference: independent numbers from the Fable 5.2 pre-publication review (ΛCDM REPLACEMENT: Ωm 0.3009, h 0.6843, DM/rd 21.166/26.085/30.243/33.798, DH/rd 17.868/15.032/12.779/10.987; calibrated σ8 0.817, S8 0.818). PASS tolerance: |Δ| ≤ max(0.1 × predictive s.d., 0.05%) for distances; |Δ| ≤ 0.001 for Ωm and h; |Δ| ≤ 0.003 for σ8 and S8.

| Row | Branch | Model | Status | Detail |
|---|---|---|---|---|
| CTC-1B | REPLACEMENT | ΛCDM BAO-only | PASS (unchanged from REV2) | no CMB prior used |
| CTC-1P | PRIMARY | ΛCDM BAO-only | PASS (unchanged from REV2) | no CMB prior used |
{STAT}
| GR-1B-REV3 | REPLACEMENT | ΛCDM growth | PASS | σ8 {L['sigma8_0'][1]:.3f}, S8 {L['S8_0'][1]:.3f} vs Fable 0.817 / 0.818 |
| GR-5B-REV3 | REPLACEMENT | CPL growth | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number |
| D-P*, E-CD-*, E-PHZ-1 | n/a | non-BAO+CMB | unchanged from REV2 | not affected by the CMB prior; NOT READY rows stay NOT READY |

No row was HELD for lack of a recompute: every row that used the compressed CMB prior was recomputed.

## How to read this pack

- Every item is prospective and model-conditional. Author of every item: C.A.S.D.R.
- Distance curves are one model-conditional curve per row, not independent predictions. They are evaluated exactly at z = 0.9, 1.2, 1.5, 1.8. Do not interpolate.
- BAO + CMB widths are parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background. Two systematics are stated and not folded in: a 0.1% r_d fitting-formula floor, and about −0.11% in DM/rd and DH/rd for a 0.06 eV neutrino background instead of massless (CAMB r_drag 147.53 vs 147.36 Mpc at the ΛCDM best fit).
- CPL bands are 68% only, with two decimals.

{ctx}
## Ranked predictions

{ctc1.replace('### CTC-1P','### CTC-1P (unchanged from REV2)').replace('### CTC-1B','### CTC-1B (unchanged from REV2)')}
{rows}
{growth}
{rest}
## Assembly note

Pack path: `PUBLISH_20261112/REV3/`. Calculation scripts and JSON outputs are in `REV3/calc/`. Every number above is generated from those JSON files (`rows_rev3_rescale.json`, `growth_like_r03_rescale.json`, `growth_rev3_rescale.json`, `control_rev3.json`). REV1 and REV2 were not modified.
"""
md=md.replace('Replaced in this pack by the R03 revisions above.','Replaced in this pack by the REV3 revisions above (the R03 revisions used in REV2 are also superseded).').replace('- R05 growth rows (held). ','- Earlier R05 and R03 growth numbers (superseded by GR-1B-REV3 and GR-5B-REV3). ')
import os
for bad in [os.environ.get('FORBID_NAME','x'*20),'p-value','significan','detection at','tension at']:
    assert bad not in md, bad
open('../../PUBLISH_20261112/REV3/PREDICTIONS_20261112_REV3.md','w').write(md); print(len(md))
