# CHANGELOG_REV2

**Author:** C.A.S.D.R
**Status:** PRIVATE DRAFT. Nothing posted, uploaded or timestamped.
**Written:** 2026-11-12, about 05:55 ET (America/Toronto). Built from REV1. v0 and REV1 were not modified.

Fixes from the Claude Fable 5.2 review, as relayed by Coordinator:

## 1. REPLACEMENT label swap — fit data were not swapped

arXiv:2607.27410 Eq. 26: DM/rd = 39.32 ± 0.33, DH/rd = 8.600 ± 0.066, ρ = +0.225.

The official DESI mean file stores the z=2.33 pair as **DH then DM** (0-based index 11 = `DH_over_rs` = 8.631545674846294; index 12 = `DM_over_rs` = 38.988973961958784) in `/workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_mean.txt`.

The REPLACEMENT assignment puts 8.600 in the DH slot and 39.32 in the DM slot:

- `R03/calc/cplmodel_r03.py` lines 7–8
- `R03/wolfram/common_R03_fullrs.wl` lines 4–9 (`qs` ending `"DH","DM"`; 1-based `ReplacePart` on indices 12 and 13)

**The fit was not swapped.** Description text already matched Eq. 26 and is retained (with current-information labelling). No REPLACEMENT row is marked NOT READY for this reason. PRIMARY remains the legacy comparison only; REPLACEMENT remains the current-information forecast.

## 2. CPL Ωm

Only 0.3555 [0.3318, 0.3820] is published as PRIMARY CPL Ωm. Re-verified this turn from `R03/calc/fullrs_cpl_chain_PRIMARY_R03.npy` (60,000 samples; 50 [16, 84] csv rounding).

## 3. wCDM w — MCMC only

Published values, verified against `R03/calc/fullrs_r03_output.json` (N = 128,000; no wCDM `.npy` was saved):

- PRIMARY (legacy): −1.0312 ± 0.0405 (unrounded median −1.031164704133902, std 0.04050591320847352)
- REPLACEMENT (current): −1.0291 ± 0.0413 (unrounded median −1.0290639367764145, std 0.04127348192832676)

Every REV1 Laplace rounded-width display figure for w (the two-decimal 0.042 width) was dropped. Distance-curve widths such as DH/rd 17.7697 ± 0.0423 were kept (they are not the dropped w figure).

## 4. ΛCDM predictive widths

CTC-2P-R03 and CTC-2B-R03 widths are labelled “parameter-only, conditional on the compressed CMB prior and massless-neutrino background”, with a 0.1% systematic floor. The floor is the r_d formula versus CLASS `rs_d` offset in `class_crosscheck_r03_output.json` (LCDM_REPL_fullrs +0.0861%, wCDM_REPL_fullrs +0.0866%, CPL_PRIM_fullrs_best +0.0889%). CTC-1 (BAO-only) is labelled parameter-only without the CMB-prior clause.

## 5. No N-standard-deviation wording

REV1 already had none. REV2 was grepped after writing for the usual significance tokens and digit-times-s.d. patterns.

## 6. REPLACEMENT is the forecast; PRIMARY is legacy

Stated in the ranking rationale, the how-to list, every CTC branch/title line, the X intro and CTC posts, metadata and Zenodo drafts. Because fix 1 did not make REPLACEMENT NOT READY, PRIMARY is legacy only and the forecast is the REPLACEMENT (current-information) branch.

## 7. CPL 68% bands only (prior-touched)

95% braces were removed from the published CTC-5 numeric lines. Coverage text now states 68% only, with prior-touch fractions computed this turn from the saved chains: PRIMARY 1.9917% (0.019916666666666666) and REPLACEMENT 0.6767% (0.0067666666666666665) of samples at wa < −3.5 against the −4 edge; w0+wa<0 imposed in `cplmodel_r03.py` `inprior`.

## 8. Exact z_eff

Pack values were already evaluations at exact z ∈ {0.9, 1.2, 1.5, 1.8}, not interpolations (Wolfram `zE`; Python `pred`). No recomputation was required and no row is NOT READY for interpolation. The R02 “interpolate linearly” scoring instruction is withdrawn. The review-reported interpolation bias (~0.107 DM/rd, ~0.084 DH/rd) is cited as UNVERIFIED (not recomputed here).

## Other

Release framing from REV1 is kept. Author remains C.A.S.D.R. X posts are ≤280 characters. Existing NOT READY rows are unchanged: D-P7, E-CD-P2, E-CD-P3, E-PHZ-1.
