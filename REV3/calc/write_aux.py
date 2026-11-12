import json,csv
B=json.load(open('build_parts.json')); K=json.load(open('control_rev3.json')); GL=json.load(open('growth_like_r03_rescale.json'))
D='../../PUBLISH_20261112/REV3/'
sh='\n'.join(f"| {r} | {b} | {m} | "+' / '.join(f'{x:+.4f}' for x in dm)+' | '+' / '.join(f'{x:+.4f}' for x in dh)+' |' for r,b,m,dm,dh in B['shifts'])
gs=lambda n:', '.join(f'{k} {v:+.4f}' for k,v in GL[n]['shift_vs_R03_median'].items())
ctl='\n'.join(f"| {k} | {v['lA']:.4f} | {v['R']:.5f} | {v['prior_only_fit']['H0']:.3f} | {v['prior_only_fit']['omh2']:.5f} | {'PASS' if v['PASS'] else 'FAIL'} |" for k,v in K.items() if k!='tolerance')
cl=f"""# CHANGELOG_REV3

**Author:** C.A.S.D.R
**Written:** 2026-11-12, America/Toronto (UTC−5). Built from REV2. REV1 and REV2 files are unchanged and remain as frozen originals.

## What REV3 supersedes

REV3 supersedes **every BAO + compressed-CMB row and every number derived from a BAO + compressed-CMB fit** in REV1 and REV2:

- Distance curves CTC-2P/2B, CTC-3P/3B, CTC-4P/4B, CTC-5P/5B (the "-R03" rows of REV2) → replaced by the "-REV3" rows.
- Model-context parameters: wCDM w (both branches), oΛCDM Ωk (both branches), CPL Ωm, h, w0, wa and ω_b (both branches).
- Growth numbers (σ8, S8, fσ8), which were held in REV2 → now published as GR-1B-REV3 and GR-5B-REV3.

**Not superseded:** BAO-only curves CTC-1P and CTC-1B (no CMB prior; carried over unchanged), and the D-P, E-CD and E-PHZ rows (not BAO + CMB fits; carried over unchanged, with NOT READY rows still NOT READY).

## 1. Blocking fix — compressed CMB prior calibration

Control: at the Planck 2018 mean (Ωm 0.3166, h 0.6727, ω_b 0.02236), the model l_A should reproduce the prior mean 301.4707 (Chen, Huang & Wang 2019, arXiv:1808.05724), and a prior-only flat-ΛCDM fit should return H0 ≈ 67.27 and Ωm h² ≈ 0.1432.

| CMB convention | l_A at Planck mean | R at Planck mean | prior-only H0 | prior-only Ωm h² | control |
|---|---|---|---|---|---|
{ctl}

Tolerance: {K['tolerance']}.

- `old` = REV2 behaviour (Hu–Sugiyama z* = 1091.94, photons + 3.046 massless ν). **Before: l_A = {K['old']['lA']:.4f}; FAIL.**
- `chen_zHS` / `chen_zfix` = Chen et al. radiation convention Ω_r = Ωm/(1+z_eq), z_eq = 2.5×10⁴ Ωm h² (T/2.7)⁻⁴, with Hu–Sugiyama z* or z* = 1089.9. The z* = 1089.9 variant gets H0 and Ωm h² within tolerance but leaves l_A 0.056 low (about 0.6 of the prior's l_A width), so it is kept as a cross-check only.
- `rescale` = model l_A × 0.997452 (Fable's fallback). **After: l_A = {K['rescale']['lA']:.4f}, H0 = {K['rescale']['prior_only_fit']['H0']:.3f}, Ωm h² = {K['rescale']['prior_only_fit']['omh2']:.5f}; PASS.** This is the convention adopted for all REV3 numbers.
- Sensitivity: the `chen_zfix` re-run of the REPLACEMENT rows moves ΛCDM DM/rd by at most 0.0023 and wCDM w by 0.0014 from the adopted numbers (`rows_rev3_chen_zfix.json`).

## 2. Re-runs with the calibrated prior (all rows using the CMB prior)

Median shifts of the distance curves, REV3 − REV2, at z = 0.9 / 1.2 / 1.5 / 1.8:

| Row | Branch | Model | ΔDM/rd | ΔDH/rd |
|---|---|---|---|---|
{sh}

Parameter shifts, REV3 − REV2: wCDM w +0.0029 (REPLACEMENT), +0.0026 (PRIMARY), in line with Fable's expected ~0.003; CPL REPLACEMENT w0 +0.019, wa −0.047; CPL PRIMARY w0 +0.025, wa −0.051 (each under 0.1 of its 68% width, in line with Fable's expectation); oΛCDM Ωk +0.0007 on both branches (width unchanged at about 0.0012).

Growth (like-for-like with the R03 growth script: CAMB, massless ν, A_s marginalised), shift of medians vs R03: ΛCDM {gs('LCDM')}; CPL {gs('w0waCDM')}.

ΛCDM, wCDM and oΛCDM distance widths are now MCMC standard deviations rather than Laplace. CPL bands are 68% only, with two decimals.

## 3. Write-up fixes (Fable 5.2)

1. **DM/DH label swap.** The hand-off text listed the Eq. 26 Lyα point as "DM/rd 8.600, DH/rd 39.32". The correct labels are DM/rd 39.32 ± 0.33 and DH/rd 8.600 ± 0.066 (ρ +0.225). The fit data vector was always correct (index 11 = DH, index 12 = DM in the DESI mean-file order).
2. **Old r_d.** The old truncated-r_s REPLACEMENT best fit gives r_d = 143.41 Mpc from the fitting formula (143.42 on PRIMARY), not 144.0 as stated in the R03 HELD table and hand-off.
3. **z = 1.3 labels checked.** From `R03/calc/fullrs_r03_output.json` (flat ΛCDM, old/new − 1): PRIMARY DH/rd −1.888%, DM/DH +1.199%, DM/rd −0.711%; REPLACEMENT DH/rd −1.891%, DM/DH +1.150%, DM/rd −0.762%. Labels are correct as published. The separate "+2.06% / +0.56% / −1.46%" figures are CPL PRIMARY median shifts (new/old − 1), not ΛCDM.
4. **"Effective rank 5" restated.** The 8×8 predictive correlation matrices have two (ΛCDM, oΛCDM), two plus one small (wCDM) and three plus one small (CPL) non-negligible eigen-directions. The curves carry three to four informative directions at most, not five.
5. **CPL prior-edge note.** wa < −3.5 in 0.88% (REPLACEMENT) and 1.90% (PRIMARY) of samples; w0 + wa < 0 imposed. 68% bands only.
6. **Ωk magnitude not robust.** Stated in the pack.
7. **Neutrino variant as a systematic.** One 0.06 eV state instead of massless: DM/rd and DH/rd about −0.11% (CAMB r_drag 147.53 vs 147.36 Mpc at the ΛCDM best fit); σ8 about −0.014 at fixed A_s.

No significance-type wording was added. HSU, STO, Rebound and R1 remain derivation-gated and excluded.

## 4. Comparison with Fable 5.2's independent numbers

See the status table in PREDICTIONS_20261112_REV3.md. Flat ΛCDM REPLACEMENT: PASS (max |Δ| 0.0074 in DM/rd, 0.0019 in DH/rd; Ωm +0.0004, h −0.0004 at best fit). σ8 0.817 vs 0.817 and S8 0.819 vs 0.818: PASS. Rows without a Fable number are marked "RECOMPUTED; Fable comparison NOT_RUN".

## Files

`PREDICTIONS_20261112_REV3.md` / `.pdf`, `CHANGELOG_REV3.md`, `STATUS_REV3.csv`, `ZENODO_METADATA_20261112_REV3.json`, `calc/` (scripts and JSON outputs), `SHA256SUMS` and OpenTimestamps proofs (`*.ots`).
"""
open(D+'CHANGELOG_REV3.md','w').write(cl)
with open(D+'STATUS_REV3.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['row','branch','model','status','detail'])
    w.writerow(['CTC-1B','REPLACEMENT','LCDM BAO-only','PASS (unchanged from REV2)','no CMB prior'])
    w.writerow(['CTC-1P','PRIMARY','LCDM BAO-only','PASS (unchanged from REV2)','no CMB prior'])
    for r in B['status']: w.writerow(r)
    L=GL['LCDM']; w.writerow(['GR-1B-REV3','REPLACEMENT','LCDM growth','PASS',f"sigma8 {L['sigma8_0'][1]:.3f} S8 {L['S8_0'][1]:.3f} vs Fable 0.817/0.818"])
    w.writerow(['GR-5B-REV3','REPLACEMENT','CPL growth','RECOMPUTED; Fable comparison NOT_RUN','no Fable number'])
z={"metadata":{"title":"Prospective, model-conditional cosmology forecasts (12 November 2026) — REV3","upload_type":"publication","publication_type":"preprint",
 "creators":[{"name":"C.A.S.D.R"}],"version":"REV3",
 "description":"REV3 of dated, model-conditional cosmology forecasts by C.A.S.D.R. REV3 supersedes all BAO + compressed-CMB rows of REV1/REV2 after calibration of the compressed Planck 2018 CMB prior (l_A control at the Planck mean now 301.4707; prior-only flat-ΛCDM fit H0 67.28, Ωm h² 0.1432). BAO-only rows are unchanged. Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts; the strongest tests need DR1 Complete (mid-2027). No statistical-test claims are made.",
 "keywords":["cosmology","forecast","Euclid","BAO","DESI","CMB distance prior","dark energy"],"related_identifiers":[{"identifier":"https://github.com/replytomehereanytime-ux/euclid-forecasts-20261112","relation":"isSupplementTo"}],"license":"cc-by-4.0"}}
json.dump(z,open(D+'ZENODO_METADATA_20261112_REV3.json','w'),indent=1,ensure_ascii=False)
