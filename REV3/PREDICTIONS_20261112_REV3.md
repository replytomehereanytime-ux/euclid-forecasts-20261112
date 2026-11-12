# Prospective, model-conditional cosmology forecasts (12 November 2026) — REV3

**Author:** C.A.S.D.R

**Status:** REV3, a marked revision. It supersedes the BAO + compressed-CMB rows of REV1 and REV2 because the compressed CMB prior was mis-calibrated in those revisions. REV1 and REV2 are kept unchanged as frozen originals. Assembled 2026-11-12 in America/Toronto (UTC−5).

**Release framing:** Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts. The galaxy-clustering and weak-lensing products needed for the strongest tests are scheduled for mid-2027 (DR1 Complete). Distance and growth rows are for measurements built on DR1 Complete (mid-2027 or later), not Foundation.

**The forecast is the REPLACEMENT (current-information) branch.** PRIMARY is the legacy comparison only. The two branches are alternatives, not independent predictions. No statistical-test claims of any kind are made in this pack; standard deviations describe widths only. HSU, STO, Rebound and R1 remain derivation-gated and are not included.

## What changed in REV3 (summary; full list in CHANGELOG_REV3.md)

1. **CMB-prior calibration (blocking item).** At the Planck 2018 mean (Ωm 0.3166, h 0.6727, ω_b 0.02236) the REV2 pipeline gave l_A = 302.24 against the prior mean 301.4707. REV3 adopts a calibrated l_A (model l_A × 0.997452), which gives l_A = 301.4707 at the Planck mean; a prior-only flat-ΛCDM fit then returns H0 = 67.28 and Ωm h² = 0.1432 (target 67.27 and 0.1432). The Chen, Huang & Wang (2019, arXiv:1808.05724) conventions (Ω_r = Ωm/(1+z_eq), z_eq = 2.5×10⁴ Ωm h² (T/2.7)⁻⁴, z* = 1089.9) were also run: they give l_A = 301.415 at the Planck mean and prior-only H0 67.26, Ωm h² 0.1431. That variant moves the ΛCDM distances by at most 0.003 in DM/rd relative to the adopted one, so it is recorded as a cross-check.
2. **Every row that uses the compressed CMB prior was re-run:** ΛCDM, wCDM, oΛCDM and CPL distances on both branches; wCDM w; CPL w0, wa and bands; σ8, S8 and fσ8. Only the BAO-only curves CTC-1P and CTC-1B are unaffected and are carried over unchanged.
3. Widths for ΛCDM, wCDM and oΛCDM are now MCMC median ± standard deviation (REV2 used Laplace widths for the distance curves).
4. Write-up fixes: Eq. 26 Lyα labels stated as DM/rd 39.32 and DH/rd 8.600 (an earlier hand-off text had them swapped; the fit data were never swapped); the old truncated-r_s REPLACEMENT r_d is 143.4 Mpc, not 144.0; the z = 1.3 PRIMARY/REPLACEMENT shift labels were checked against the output JSON and are correct; "effective rank 5" is restated as three to four informative directions; CPL prior-edge note added; Ωk magnitude stated as not robust; 0.06 eV neutrino-variant shift added as a stated systematic.

## Status table (REV3)

Comparison reference: independent numbers from the Fable 5.2 pre-publication review (ΛCDM REPLACEMENT: Ωm 0.3009, h 0.6843, DM/rd 21.166/26.085/30.243/33.798, DH/rd 17.868/15.032/12.779/10.987; calibrated σ8 0.817, S8 0.818). PASS tolerance: |Δ| ≤ max(0.1 × predictive s.d., 0.05%) for distances; |Δ| ≤ 0.001 for Ωm and h; |Δ| ≤ 0.003 for σ8 and S8.

| Row | Branch | Model | Status | Detail |
|---|---|---|---|---|
| CTC-1B | REPLACEMENT | ΛCDM BAO-only | PASS (unchanged from REV2) | no CMB prior used |
| CTC-1P | PRIMARY | ΛCDM BAO-only | PASS (unchanged from REV2) | no CMB prior used |
| CTC-2B-REV3 | REPLACEMENT | LCDM | PASS | best fit Ωm 0.3013 h 0.6839 vs Fable 0.3009/0.6843; DM/rd 21.172/26.092/30.250/33.805 vs 21.166/26.085/30.243/33.798; DH/rd 17.870/15.033/12.779/10.987 vs 17.868/15.032/12.779/10.987; max abs difference 0.0074 |
| CTC-2P-REV3 | PRIMARY | LCDM | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-3B-REV3 | REPLACEMENT | wCDM | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-3P-REV3 | PRIMARY | wCDM | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-4B-REV3 | REPLACEMENT | oLCDM | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-4P-REV3 | PRIMARY | oLCDM | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-5B-REV3 | REPLACEMENT | CPL | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| CTC-5P-REV3 | PRIMARY | CPL | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number for this row |
| GR-1B-REV3 | REPLACEMENT | ΛCDM growth | PASS | σ8 0.817, S8 0.819 vs Fable 0.817 / 0.818 |
| GR-5B-REV3 | REPLACEMENT | CPL growth | RECOMPUTED; Fable comparison NOT_RUN | no independent Fable number |
| D-P*, E-CD-*, E-PHZ-1 | n/a | non-BAO+CMB | unchanged from REV2 | not affected by the CMB prior; NOT READY rows stay NOT READY |

No row was HELD for lack of a recompute: every row that used the compressed CMB prior was recomputed.

## How to read this pack

- Every item is prospective and model-conditional. Author of every item: C.A.S.D.R.
- Distance curves are one model-conditional curve per row, not independent predictions. They are evaluated exactly at z = 0.9, 1.2, 1.5, 1.8. Do not interpolate.
- BAO + CMB widths are parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background. Two systematics are stated and not folded in: a 0.1% r_d fitting-formula floor, and about −0.11% in DM/rd and DH/rd for a 0.06 eV neutrino background instead of massless (CAMB r_drag 147.53 vs 147.36 Mpc at the ΛCDM best fit).
- CPL bands are 68% only, with two decimals.

## Model-context parameters (REV3, calibrated CMB prior; MCMC; not scored as separate forecasts)

| Parameter | Branch | REV3 | REV2 | Shift (REV3 − REV2) |
|---|---|---|---|---|
| wCDM w | REPLACEMENT (current) | -1.0261 ± 0.0402 | −1.0291 ± 0.0413 | +0.0029 |
| wCDM w | PRIMARY (legacy) | -1.0286 ± 0.0403 | −1.0312 ± 0.0405 | +0.0026 |
| oΛCDM Ωk | REPLACEMENT | +0.0027 ± 0.0012 (MCMC) | +0.00198 ± 0.00124 (Laplace) | +0.0007 |
| oΛCDM Ωk | PRIMARY | +0.0027 ± 0.0012 (MCMC) | +0.00199 ± 0.00125 (Laplace) | +0.0007 |
| CPL w0 | REPLACEMENT | -0.512 [-0.755, -0.234] | −0.5308 [−0.7623, −0.2638] | +0.019 |
| CPL wa | REPLACEMENT | -1.468 [-2.304, -0.767] | −1.4209 [−2.2372, −0.7542] | -0.047 |
| CPL w0 | PRIMARY | -0.392 [-0.635, -0.129] | −0.4167 [−0.6570, −0.1476] | +0.025 |
| CPL wa | PRIMARY | -1.811 [-2.605, -1.110] | −1.7592 [−2.5757, −1.0548] | -0.051 |
| CPL Ωm | PRIMARY | 0.3554 [0.3311, 0.3815] | 0.3555 [0.3318, 0.3820] | -0.0001 |

**Ωk is not robust.** Its sign flipped between the truncated-r_s and corrected-r_s fits (R02 → R03), and its central value moved again here (+0.0020 → +0.0027) when the CMB prior was calibrated. The compressed prior is also used outside its flat-model derivation. Only the width (about 0.0012) should be read as informative; the magnitude should not.

## Ranked predictions

### CTC-1P (unchanged from REV2) — Flat ΛCDM, BAO only (frozen primary, legacy comparison only)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** Flat ΛCDM, radiation omitted, params (Ωm, A = c/(H0 rd))
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)
- **Numeric prediction:**
  - z=0.9: DM/rd 21.0789 ± 0.0710, DH/rd 17.8273 ± 0.0666
  - z=1.2: DM/rd 25.9885 ± 0.0760, DH/rd 15.0084 ± 0.0736
  - z=1.5: DM/rd 30.1415 ± 0.0837, DH/rd 12.7642 ± 0.0739
  - z=1.8: DM/rd 33.6928 ± 0.0944, DH/rd 10.9785 ± 0.0704
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian)
- **Date frozen:** R02 table file mtime 2026-11-12 04:51 ET (America/Toronto) for FORECAST_TABLE_R02.csv; calibration field: DESI DR2 BAO (13 points, official mean/cov; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `CTC-1P`
- **Note:** Not affected by the r_s truncation (BAO-only, no CMB sound-horizon integral). These 8 distance numbers are one model-conditional curve, not 8 independent predictions. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). Legacy comparison only. Widths are parameter-only (BAO-only Laplace; no compressed CMB prior).

### CTC-1B (unchanged from REV2) — Flat ΛCDM, BAO only (Lyα replacement branch, current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** Flat ΛCDM, radiation omitted, params (Ωm, A = c/(H0 rd)) (as CTC-1P)
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; DESI DR2 Results IV v3 Eq. 26 Lyα: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 — replaces, not added). Alternative to the legacy CTC-1P row, not an independent prediction. The Eq. 26 labels were checked against the fit data vector: they are not swapped (see SOURCES).
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1067 ± 0.0689, DH/rd 17.8121 ± 0.0617
  - z=1.2: DM/rd 26.0102 ± 0.0750, DH/rd 14.9844 ± 0.0663
  - z=1.5: DM/rd 30.1554 ± 0.0828, DH/rd 12.7373 ± 0.0658
  - z=1.8: DM/rd 33.6987 ± 0.0927, DH/rd 10.9516 ± 0.0624
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian)
- **Date frozen:** R02 table file mtime 2026-11-12 04:51 ET (America/Toronto) for FORECAST_TABLE_R02.csv; calibration field: DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `CTC-1B`
- **Note:** Not affected by the r_s truncation. R02 sources field states these central values equal R01 E-BAO-1 (R01 W1). Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). This is the current-information forecast for this model. Widths are parameter-only (BAO-only Laplace; no compressed CMB prior).


### CTC-2B-REV3 — Flat ΛCDM, BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-2B-R03.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; DESI DR2 BAO with Lyα z=2.33 replaced by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ +0.225)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1724 ± 0.0615, DH/rd 17.8695 ± 0.0183
  - z=1.2: DM/rd 26.0918 ± 0.0648, DH/rd 15.0329 ± 0.0070
  - z=1.5: DM/rd 30.2504 ± 0.0653, DH/rd 12.7784 ± 0.0049
  - z=1.8: DM/rd 33.8051 ± 0.0645, DH/rd 10.9867 ± 0.0062
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×5000, burn 1000, N = 128000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.3013 ± 0.0038, h 0.6840 ± 0.0029, Ωm h² 0.1409
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 0 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-2P-REV3 — Flat ΛCDM, BAO + calibrated compressed CMB (legacy comparison only)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-2P-R03.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1545 ± 0.0627, DH/rd 17.8646 ± 0.0186
  - z=1.2: DM/rd 26.0730 ± 0.0660, DH/rd 15.0315 ± 0.0070
  - z=1.5: DM/rd 30.2316 ± 0.0665, DH/rd 12.7790 ± 0.0049
  - z=1.8: DM/rd 33.7865 ± 0.0656, DH/rd 10.9882 ± 0.0063
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×5000, burn 1000, N = 128000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.3002 ± 0.0038, h 0.6848 ± 0.0030, Ωm h² 0.1408
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 0 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-3B-REV3 — Flat wCDM (constant w), BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-3B-R03.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; DESI DR2 BAO with Lyα z=2.33 replaced by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ +0.225)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1601 ± 0.0644, DH/rd 17.9200 ± 0.0787
  - z=1.2: DM/rd 26.0937 ± 0.0645, DH/rd 15.0734 ± 0.0618
  - z=1.5: DM/rd 30.2627 ± 0.0671, DH/rd 12.8079 ± 0.0445
  - z=1.8: DM/rd 33.8245 ± 0.0698, DH/rd 11.0073 ± 0.0310
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×5000, burn 1000, N = 128000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.2970 ± 0.0075, h 0.6899 ± 0.0096, Ωm h² 0.1414, w -1.0261 ± 0.0402 (MCMC median ± s.d.)
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 1 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-3P-REV3 — Flat wCDM (constant w), BAO + calibrated compressed CMB (legacy comparison only)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-3P-R03.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1385 ± 0.0661, DH/rd 17.9186 ± 0.0787
  - z=1.2: DM/rd 26.0721 ± 0.0657, DH/rd 15.0757 ± 0.0619
  - z=1.5: DM/rd 30.2424 ± 0.0679, DH/rd 12.8114 ± 0.0446
  - z=1.8: DM/rd 33.8053 ± 0.0704, DH/rd 11.0109 ± 0.0312
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×5000, burn 1000, N = 128000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.2954 ± 0.0076, h 0.6914 ± 0.0098, Ωm h² 0.1412, w -1.0286 ± 0.0403 (MCMC median ± s.d.)
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 1 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-4B-REV3 — oΛCDM (free Ωk), BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-4B-R03.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; DESI DR2 BAO with Lyα z=2.33 replaced by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ +0.225)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1127 ± 0.0667, DH/rd 17.7859 ± 0.0420
  - z=1.2: DM/rd 26.0121 ± 0.0738, DH/rd 14.9562 ± 0.0353
  - z=1.5: DM/rd 30.1541 ± 0.0783, DH/rd 12.7105 ± 0.0310
  - z=1.8: DM/rd 33.6951 ± 0.0813, DH/rd 10.9271 ± 0.0276
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×6000, burn 1500, N = 144000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.3035 ± 0.0039, h 0.6868 ± 0.0032, Ωm h² 0.1431, Ωk +0.0027 ± 0.0012 (MCMC median ± s.d.; **magnitude not robust**, see notes)
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 0 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-4P-REV3 — oΛCDM (free Ωk), BAO + calibrated compressed CMB (legacy comparison only)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-4P-R03.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.0945 ± 0.0687, DH/rd 17.7803 ± 0.0421
  - z=1.2: DM/rd 25.9930 ± 0.0756, DH/rd 14.9545 ± 0.0354
  - z=1.5: DM/rd 30.1344 ± 0.0799, DH/rd 12.7104 ± 0.0313
  - z=1.8: DM/rd 33.6758 ± 0.0827, DH/rd 10.9278 ± 0.0279
- **Band:** MCMC posterior median ± standard deviation (parameter-only, conditional on the calibrated compressed CMB prior and the stated neutrino background). emcee 32×6000, burn 1500, N = 144000, seed 20261112. Laplace widths from REV2 are not used.
- **Conditional-fit parameters (not scored):** Ωm 0.3024 ± 0.0040, h 0.6876 ± 0.0033, Ωm h² 0.1430, Ωk +0.0027 ± 0.0012 (MCMC median ± s.d.; **magnitude not robust**, see notes)
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 2 large and 0 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-5B-REV3 — CPL w0waCDM, BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-5B-R03.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; DESI DR2 BAO with Lyα z=2.33 replaced by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ +0.225)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.10 [21.03, 21.17], DH/rd 17.81 [17.71, 17.91]
  - z=1.2: DM/rd 26.03 [25.96, 26.10], DH/rd 15.12 [15.04, 15.21]
  - z=1.5: DM/rd 30.23 [30.15, 30.30], DH/rd 12.91 [12.84, 12.99]
  - z=1.8: DM/rd 33.82 [33.74, 33.89], DH/rd 11.11 [11.05, 11.18]
- **Band:** MCMC posterior median and 68% interval only (two decimals). emcee 40×10000, burn 2500, thin 5, N = 60000, seed 20261112. No 95% band is published.
- **CPL prior-edge note:** the posterior touches the wa > −4 prior edge: 0.88% of samples have wa < −3.5; w0 + wa < 0 is imposed. The 68% bands depend on these priors.
- **Conditional-fit parameters (16/50/84, not scored):** Ωm 0.3458 [0.3217, 0.3734], h 0.6430 [0.6201, 0.6655], w0 -0.512 [-0.755, -0.234], wa -1.468 [-2.304, -0.767], ω_b 0.02236 [0.02223, 0.02250]
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 3 large and 1 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### CTC-5P-REV3 — CPL w0waCDM, BAO + calibrated compressed CMB (legacy comparison only)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (CMB prior calibrated; r_s integral to infinity). Supersedes the REV2 row CTC-5P-R03.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO, official Lyα)
- **Observable:** DM/rd and DH/rd (dimensionless), evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated)
- **Data product:** a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.06 [20.99, 21.13], DH/rd 17.78 [17.68, 17.88]
  - z=1.2: DM/rd 25.98 [25.91, 26.05], DH/rd 15.14 [15.05, 15.23]
  - z=1.5: DM/rd 30.19 [30.11, 30.26], DH/rd 12.94 [12.86, 13.02]
  - z=1.8: DM/rd 33.79 [33.71, 33.86], DH/rd 11.14 [11.08, 11.20]
- **Band:** MCMC posterior median and 68% interval only (two decimals). emcee 40×10000, burn 2500, thin 5, N = 60000, seed 20261112. No 95% band is published.
- **CPL prior-edge note:** the posterior touches the wa > −4 prior edge: 1.90% of samples have wa < −3.5; w0 + wa < 0 is imposed. The 68% bands depend on these priors.
- **Conditional-fit parameters (16/50/84, not scored):** Ωm 0.3554 [0.3311, 0.3815], h 0.6341 [0.6133, 0.6561], w0 -0.392 [-0.635, -0.129], wa -1.811 [-2.605, -1.110], ω_b 0.02237 [0.02224, 0.02251]
- **Note:** the 8 distance numbers are one model-conditional curve, not 8 independent predictions; the 8×8 predictive correlation matrix has 3 large and 1 small non-negligible eigen-directions (three to four informative directions at most across the models; shared calibration via c/(H0 r_d)). Systematic: switching the background from massless neutrinos to one 0.06 eV state shifts DM/rd and DH/rd by about −0.11% (CAMB r_drag, same H0, ω_b, total ω_m); a 0.1% r_d-formula floor also applies.

### GR-1B-REV3 — σ8, S8 and fσ8, flat ΛCDM, BAO + calibrated compressed CMB (current-information forecast)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Revision label:** REV3-recomputed (new in the public pack; the R03 growth recompute used the uncalibrated CMB prior and was held in REV2).
- **Branch:** DECLARED REPLACEMENT.
- **Method:** CAMB 2.0.5 on 60 draws from the REV3 flat-ΛCDM REPLACEMENT chain; ln(10¹⁰A_s) drawn from N(3.044, 0.014) (Planck 2018), n_s 0.9649, massless neutrinos (N_eff 3.046), same settings as the earlier R03 growth script. **A_s is not constrained by the BAO + compressed-CMB fit; its Planck 2018 uncertainty (about 0.7% on σ8) is included in the bands below.**
- **Numeric prediction (16/50/84):**
  - σ8 (z=0): 0.817 [0.813, 0.823]
  - S8 = σ8 (Ωm/0.3)^0.5: 0.819 [0.810, 0.828]
  - fσ8: z=0.9 0.445 [0.442, 0.449]; z=1.2 0.412 [0.410, 0.415]; z=1.5 0.379 [0.377, 0.382]; z=1.8 0.348 [0.346, 0.350]
- **Data product:** a later Euclid spectroscopic growth-rate (fσ8) or weak-lensing (S8) measurement built on DR1 Complete (mid-2027 or later). Not Foundation.
- **Systematic (stated, not folded in):** with one 0.06 eV neutrino state instead of massless neutrinos (same H0, ω_b, total ω_m, A_s fixed at the Planck mean), CAMB gives σ8 0.803 and S8 0.804 at the best fit, about −0.014 in σ8. fσ8 moves by a similar fraction.

### GR-5B-REV3 — σ8, S8 and fσ8, CPL, BAO + calibrated compressed CMB (context, current-information branch)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Method:** as GR-1B-REV3 on 60 draws of the REV3 CPL REPLACEMENT chain, CAMB PPF dark energy. Prior-touched CPL posterior; 68% only.
- **Numeric prediction (16/50/84):** σ8 0.803 [0.788, 0.817]; S8 0.862 [0.845, 0.885]; fσ8 z=0.9 0.439 [0.430, 0.449]; z=1.2 0.410 [0.402, 0.419]; z=1.5 0.377 [0.371, 0.385]; z=1.8 0.346 [0.340, 0.353]
- **Note:** more model-dependent than GR-1B-REV3. With only 60 draws, quantiles are uncertain at about the third decimal.

### D-P4a — BAO-only matter density stays low

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** flat ΛCDM (DESI Y5 BAO alone)
- **Observable and units:** Ωm (dimensionless)
- **Redshift (z) / grid:** n/a (single parameter; DESI Y5 BAO-only ΛCDM)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - Ωm ∈ [0.288, 0.308] (0.298 ± 0.010)
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P4a`
- **Note:** Not held (BAO-only projected interval). Box-fit context numbers from the R02 notes field are not repeated here.

### D-P4b — BAO-only Ωm stays below the Planck value

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** flat ΛCDM
- **Observable and units:** Ωm (dimensionless), as D-P4a
- **Redshift (z) / grid:** n/a (single parameter; DESI Y5 BAO-only ΛCDM)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - Ωm < 0.315 (threshold)
- **Band / coverage level (as stated in the source):** Threshold claim (no interval coverage level).
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P4b`

### D-P8a — Early-universe H0

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** ΛCDM (DESI Y5 + CMB)
- **Observable and units:** H0 (km/s/Mpc)
- **Redshift (z) / grid:** n/a (single parameter; ΛCDM, DESI Y5 + CMB)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - H0 ∈ [67.8, 68.6] (68.2 ± 0.4)
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P8a`

### D-P8c — Ladder H0 stays at 72.5–73.5

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** distance ladder (SH0ES)
- **Observable and units:** H0 (km/s/Mpc), single value
- **Redshift (z) / grid:** n/a (local distance-ladder H0)
- **Data product / release:** Latest SH0ES (Riess et al.) H0 public on or before 2027-12-31
- **Numeric prediction:**
  - 72.5 ≤ H0 ≤ 73.5 (stated range)
- **Band / coverage level (as stated in the source):** Stated range (no separate coverage label in the source).
- **Date frozen:** Calibration data cutoff field: 2026-10-13 (R02/FORECAST_TABLE_R02.csv). Prospective only for SH0ES results first public after 2026-10-13; the latest current SH0ES value was not checked (UNVERIFIED).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P8c`
- **Note:** Not a Euclid or DESI BAO row.

### D-P2a — Pivot equation of state near −1

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** w0waCDM as fitted by DESI; data DESI Y5 + CMB + DES SNe (DES-Y5 row if reported, else DES-Dovekie)
- **Observable and units:** w_p (dimensionless)
- **Redshift (z) / grid:** DESI's published pivot z_p ≈ 0.4–0.5; single value
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - w_p ∈ [−1.06, −0.94] (−1.00 ± 0.06)
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P2a`
- **Note:** Prediction text is the R02/R01 interval, which HELD_R03.md says is unchanged. The box-reference width in the R02 notes field is held and is not reproduced here.

### D-P3a — w0, wa inside predicted boxes

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** w0waCDM; DESI Y5 + CMB + DES SNe (DES-Y5 if reported, else DES-Dovekie)
- **Observable and units:** w0, wa (dimensionless); single values
- **Redshift (z) / grid:** n/a (single parameter pair)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - w0 ∈ [−0.86, −0.66]; wa ∈ [−1.15, −0.45] (−0.76 ± 0.10; −0.80 ± 0.35)
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P3a`
- **Note:** Not held (HELD_R03.md: uses projected published-DR2 widths, not a box CMB fit). Retrospective DR2 context in the R02 notes field is not repeated here.

### D-P3b — w0–wa quadrant not abandoned

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** as D-P3a (w0waCDM; DESI Y5 + CMB + DES SNe)
- **Observable and units:** Central w0, wa
- **Redshift (z) / grid:** n/a (central values; same data combination as D-P3a)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - Central w0 ≥ −0.95 and wa ≤ −0.2 (threshold claim)
- **Band / coverage level (as stated in the source):** Threshold claim (no interval coverage level).
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P3b`

### D-P3c — w0, wa errors shrink at least 20% from DR2

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** as D-P3a (w0waCDM; DESI Y5 + CMB + DES SNe)
- **Observable and units:** Published 68% errors e(w0), e(wa) (asymmetric errors averaged)
- **Redshift (z) / grid:** n/a (error widths on w0, wa)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - e(w0) ≤ 0.0456 and e(wa) ≤ 0.176 (threshold)
- **Band / coverage level (as stated in the source):** Threshold on published 68% errors.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P3c`
- **Note:** HELD_R03.md flags the source of 0.0456 / 0.176 for confirmation; the row itself is not held. Wording follows the R02 table (published 68% errors), not the R01 error-column heading.

### D-P5a — Neutrino mass limit below 0.055 eV

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** ΛCDM plus the sum of neutrino masses (DESI); DESI Y5 + CMB, DESI baseline prior
- **Observable and units:** 95% upper limit on the sum of neutrino masses (eV)
- **Redshift (z) / grid:** n/a (limit on the sum of neutrino masses; ΛCDM, DESI Y5 + CMB)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - UL95 < 0.055 eV
- **Band / coverage level (as stated in the source):** The observable is a 95% upper limit, as stated in the source.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P5a`

### D-P5b — No relaxed neutrino limit or detection

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** READY / PROVISIONAL
- **Model:** as D-P5a (ΛCDM plus the sum of neutrino masses, DESI Y5 + CMB)
- **Observable and units:** UL95 and any 95% lower bound on the sum of neutrino masses
- **Redshift (z) / grid:** n/a (limits on the sum of neutrino masses)
- **Data product / release:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12). Not a Euclid test.
- **Numeric prediction:**
  - UL95 ≤ 0.08 eV and no 95% lower bound > 0.06 eV
- **Band / coverage level (as stated in the source):** Thresholds on the published 95% upper limit and on any 95% lower bound, as stated in the source.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P5b`

### D-P7 — No hemispheric BAO difference

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** NOT READY / PROVISIONAL
- **Model:** Isotropic ΛCDM BAO
- **Observable and units:** Δα_iso = α_N − α_S (dimensionless), hemispheres split by the plane ⟂ CMB-dipole axis; one value per tracer bin or combined (TBD)
- **Redshift (z) / grid:** TBD (DESI tracer bins)
- **Data product / release:** DESI DR3/Y5 LSS catalogues (release TBD). DR1 catalogues are already public (not prospective).
- **Numeric prediction:**
  - 95% interval for Δα_iso inside (−3×10⁻³, +3×10⁻³)
- **Band / coverage level (as stated in the source):** 95% interval (as stated in the source prediction).
- **Date frozen:** Calibration data cutoff field: 2026-10-13 (R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P7`
- **Note:** NOT READY: axis coordinates not in any source file (TBD). Pass/fail rule in the source is marked PROPOSED.

### E-CD-P2 — Count-dipole direction

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** NOT READY / UNVERIFIED
- **Model:** Empirical extrapolation of CatWISE fits; kinematic null inputs for Euclid not frozen
- **Observable and units:** Dipole direction (l,b), degrees, Galactic frame assumed
- **Redshift (z) / grid:** photometric/catalogue sample (cuts TBD)
- **Data product / release:** If scored, Euclid DR1-Foundation catalogues (MER/PHZ + VMPZ masks). Foundation (12 November 2026) only timestamps this forecast; it does not complete the test. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding TBD. Foundation covers ~1,900 sq deg; no full-mission precision. Not a galaxy-clustering or weak-lensing product.
- **Numeric prediction:**
  - Best-fit direction within 30° of (l,b) = (242.28°, 37.10°)
- **Band / coverage level (as stated in the source):** Angular threshold (great-circle separation ≤ 30°); no interval coverage level.
- **Date frozen:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `E-CD-P2`
- **Note:** NOT READY (cuts/mask/estimator/covariance/kinematic null not frozen). This is a catalogue-level item, not a galaxy-clustering or weak-lensing test. Foundation (12 November 2026) only timestamps the forecast; it does not complete this test and does not supply those mid-2027 products. Foundation covers ~1,900 sq deg (f_sky ≈ 0.046 in the source): no full-mission precision may be assumed.

### E-CD-P3 — Dipole rises with redness or redshift

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** NOT READY / UNVERIFIED
- **Model:** Empirical extrapolation of CatWISE fits; kinematic null inputs for Euclid not frozen
- **Observable and units:** D per bin (dimensionless), ≥3 bins of one variable (TBD)
- **Redshift (z) / grid:** bins of redness or redshift (TBD)
- **Data product / release:** If scored, Euclid DR1-Foundation catalogues (MER/PHZ + VMPZ masks). Foundation (12 November 2026) only timestamps this forecast; it does not complete the test. Randoms only with DR1 Complete. Release binding TBD. Foundation covers ~1,900 sq deg; no full-mission precision. Not a galaxy-clustering or weak-lensing product.
- **Numeric prediction:**
  - Strictly increasing D with max/min ≥ 2
- **Band / coverage level (as stated in the source):** Threshold claim (strictly increasing; max/min ≥ 2).
- **Date frozen:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `E-CD-P3`
- **Note:** NOT READY. Catalogue-level item, not a galaxy-clustering or weak-lensing test. Foundation (12 November 2026) only timestamps the forecast; it does not complete this test and does not supply those mid-2027 products. Foundation covers ~1,900 sq deg; no full-mission precision.

### E-PHZ-1 — Capped adaptive PHZ beats native PHZ (method, not cosmology)

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** prospective
- **Readiness / verification:** NOT READY / PROVISIONAL
- **Model:** q = (1−α)p + αu, fixed adaptive α rule (fa.txt L86–92)
- **Observable and units:** Mean five-class Brier score (dimensionless); classes [0,1),[1,2),[2,3),[3,6),[6,∞)
- **Redshift (z) / grid:** PHZ class bins as above (not a cosmological z-grid)
- **Data product / release:** If scored, Euclid DR1-Foundation PHZ catalogue (DpdPhzPfOutputCatalog) + independent truth set (TBD). Foundation (12 November 2026) only timestamps this forecast; it does not complete the test. Method item, not galaxy clustering or weak lensing.
- **Numeric prediction:**
  - mean Brier(q) < mean Brier(p)
- **Band / coverage level (as stated in the source):** Point inequality (no interval coverage level).
- **Date frozen:** Rule fixed before 2026-11-12 (Freeze Addendum) — calibration data cutoff field in R02/FORECAST_TABLE_R02.csv. Prospective only if the cohort is frozen before the PHZ outputs are opened.
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `E-PHZ-1`
- **Note:** NOT READY: cohort/truth set TBD. Method forecast, not a cosmology prediction, and not a galaxy-clustering or weak-lensing test. Foundation (12 November 2026) only timestamps the forecast; it does not complete this test.

## Excluded (by name; no numbers)

### Derivation-gated — excluded

Listed by name only, as instructed. No numeric values from these items are reproduced.

- HSU
- STO
- Rebound (including Elastic Rebound / Rebound Bianchi, and the R02 row CTC-R Elastic Rebound AP curve)
- R1

### Other exclusions

- Retrospective fits (R02): RF-1, RF-2, RF-3, RF-4, RF-5, RF-6, RF-7.
- Synthetic tests (R02): SYN-1, SYN-2.
- Prospective rows whose predictive text is INTERNAL CONTEXT only (not reproduced): D-P1a, D-P1b, D-P2b, D-P8b, D-P8d, E-CD-P1, E-CD-P4, E-CD-P5, E-L-P6.
- Held frozen originals of BAO+CMB distance rows, not used: CTC-2P, CTC-2B, CTC-3P, CTC-3B, CTC-4P, CTC-4B, CTC-5B, CTC-5P, and R01 E-BAO-2, E-BAO-3. Replaced in this pack by the REV3 revisions above (the R03 revisions used in REV2 are also superseded).
- Earlier R05 and R03 growth numbers (superseded by GR-1B-REV3 and GR-5B-REV3). Unsupported / not-run alternative models in R02/UNSUPPORTED_MODELS_R02.md (massive neutrinos as a fitted model, Hu–Sawicki f(R), JBD, nDGP, k-mouflage, mixed cold/warm DM, decaying DM).
- Items listed in FORECASTS_R01.md §6 as deliberately not forecasts (including Fibonacci normalisations, GW/BAO siren ratio, geometry latent moments, DESI P9, and published GWTC values), names only.


## Assembly note

Pack path: `PUBLISH_20261112/REV3/`. Calculation scripts and JSON outputs are in `REV3/calc/`. Every number above is generated from those JSON files (`rows_rev3_rescale.json`, `growth_like_r03_rescale.json`, `growth_rev3_rescale.json`, `control_rev3.json`). REV1 and REV2 were not modified.
