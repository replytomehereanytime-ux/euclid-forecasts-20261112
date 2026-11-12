# Prospective, model-conditional cosmology forecasts (12 November 2026)

**Author:** C.A.S.D.R

**Venue:** pending author confirmation

**Status:** PRIVATE DRAFT (REV2). Assembled on 2026-11-12 in America/Toronto (UTC−5), about 05:55 ET. Nothing in this folder has been posted, uploaded, timestamped, emailed or shared by the assembler. Frozen R01/R02/R03 source files were not edited. The v0 files in the parent folder and the REV1 files were not modified.

**Release framing:** Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts. The galaxy-clustering and weak-lensing products needed for the strongest tests are scheduled for mid-2027 (DR1 Complete). Today's Foundation release does not supply those measurements. Foundation covers about 1,900 sq deg and is catalogue-level; no full-mission precision is applied to it. Distance curves in this pack are for a later Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later), not for Foundation.

**Ranking rationale:** Euclid DR1 Complete (mid-2027) ΛCDM-baseline BAO distance curves first (BAO-only, then BAO+CMB), then more model-dependent wCDM / oΛCDM / CPL curves, then DESI Y5 / SH0ES parameter rows with numeric bands or thresholds, then NOT READY catalogue or method rows. **The forecast is the REPLACEMENT (current-information) branch.** PRIMARY is the legacy comparison only; it is not the current forecast. The two branches are alternatives, not independent predictions.


## REV2 checks (Claude Fable 5.2 review)

1. **REPLACEMENT Lyα labels (Eq. 26).** arXiv:2607.27410 Eq. 26 is DM/rd = 39.32 ± 0.33, DH/rd = 8.600 ± 0.066, ρ = +0.225. The official DESI mean file `/workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_mean.txt` stores the z=2.33 pair in the order **DH then DM** (0-based index 11 = `DH_over_rs` = 8.631545674846294; index 12 = `DM_over_rs` = 38.988973961958784). The REPLACEMENT assignment in `R03/calc/cplmodel_r03.py` lines 7–8 (`dNew[11]=8.600; dNew[12]=39.32` and the matching covariance) and in `R03/wolfram/common_R03_fullrs.wl` lines 4–9 (`qs` ending `"DH","DM"`; `ReplacePart[dOld,{12->8.600,13->39.32}]`, 1-based) puts 8.600 in the DH slot and 39.32 in the DM slot, with uncertainties 0.066 and 0.33 and ρ = +0.225. **The fit data were not swapped.** Description text already used the Eq. 26 labels and is kept. No REPLACEMENT row is marked NOT READY for this reason.
2. **z_eff.** Pack distance values were obtained by evaluating the model (or the chain) at the exact grid z ∈ {0.9, 1.2, 1.5, 1.8} (`zE` in `common_R03_fullrs.wl`; `pred` in `cplmodel_r03.py`). They were not linearly interpolated between nodes. No row is marked NOT READY for interpolation. At scoring, evaluate at each published z_eff; do not interpolate.
3. No new NOT READY rows were added in REV2. Existing NOT READY items remain: D-P7, E-CD-P2, E-CD-P3, E-PHZ-1 (and the excluded / held items listed below).

## How to read this pack

- Every item is worded **prospective, model-conditional**. Author of every item: **C.A.S.D.R**.
- Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts. It does not supply galaxy-clustering or weak-lensing measurements. Those products, needed for the strongest tests, are scheduled for **DR1 Complete (mid-2027)**. Foundation covers about 1,900 sq deg (catalogue-level); no full-mission precision. Distance curves below are for a BAO measurement built on DR1 Complete (mid-2027 or later), not for today's Foundation release.
- Distance grids report DM/rd and DH/rd at four redshifts, on more than one model and two Lyα branches. Those numbers are not independent predictions. The handoff's 60 distance entries are not 60 independent predictions.
- Rows held for the r_s integral truncation are not quoted from the frozen originals. Where a held row has an R03 recompute, this pack uses the R03 revision and labels it **R03-recomputed (r_s integral corrected)**. Frozen originals remain untouched.
- Verification label, unless noted, is PROVISIONAL; outcome is not run.
- Pass/fail rules stay in the cited source rows and are not restated here.
- **The forecast is the REPLACEMENT (current-information) branch.** PRIMARY is marked **legacy comparison only** throughout. They are not independent predictions.
- Distance numbers in this pack were evaluated **exactly at z = 0.9, 1.2, 1.5, 1.8**, not by linear interpolation between nodes. At scoring, evaluate the model at each published z_eff. The R02 source-row instruction to interpolate linearly in z is withdrawn and is not to be used. A review-reported interpolation bias (~0.107 in DM/rd, ~0.084 in DH/rd) was not recomputed here and is UNVERIFIED in this pack.
- Flat ΛCDM BAO+CMB predictive widths are **parameter-only, conditional on the compressed CMB prior and massless-neutrino background**. A 0.1% systematic floor is noted (r_d fitting formula versus CLASS `rs_d`: +0.0861% on LCDM_REPL_fullrs, +0.0866% on wCDM_REPL_fullrs, +0.0889% on CPL_PRIM_fullrs_best, from `R03/calc/class_crosscheck_r03_output.json`).
- CPL predictive bands in this pack are **68% only**. The CPL posterior is prior-touched (see the CTC-5 notes).


## Model-context parameters (conditional fits, not scored as separate forecasts)

These figures are conditional-fit parameters, not additional prospective rows. Each value names its branch. For wCDM, this pack publishes only the MCMC median and standard deviation (Laplace figures that appeared in REV1 are not published here).

- **wCDM, FROZEN PRIMARY branch (CTC-3P-R03), legacy comparison only:** w = −1.0312 ± 0.0405 (MCMC median and s.d.). Unrounded, from `R03/calc/fullrs_r03_output.json` key `mcmc.wCDM_PRIMARY.w`: median −1.031164704133902, std 0.04050591320847352; 68% [−1.0722202260695506, −0.9917768165294115]. Sampler: emcee 32 walkers × 5,000 steps, burn 1,000, thin 1, N = 128,000, seed 20261112. No separate wCDM chain `.npy` was saved; the verification is against that JSON, which was written by `R03/calc/fullrs_r03.py` from the chain.
- **wCDM, DECLARED REPLACEMENT branch (CTC-3B-R03), current-information forecast:** w = −1.0291 ± 0.0413 (MCMC median and s.d.). Unrounded, from the same JSON key `mcmc.wCDM_REPLACEMENT.w`: median −1.0290639367764145, std 0.04127348192832676; 68% [−1.0705046565941894, −0.9887030477270878]. Same sampler settings, N = 128,000.

- **oΛCDM, FROZEN PRIMARY branch (CTC-4P-R03), legacy comparison only:** Ωk = +0.00199 ± 0.00125. The width is shown as 0.00125 because it sits on a 4-decimal rounding boundary (0.00125 would become 0.0013 at 4 decimals). Unrounded Wolfram Laplace: central 0.0019908057850397567, width 0.001253061073170205, from `R03/wolfram/fullrs_fits_R03.json`. The csv already prints 0.00199 ± 0.00125.
- **oΛCDM, DECLARED REPLACEMENT branch (CTC-4B-R03), current-information forecast:** Ωk = +0.00198 ± 0.00124 (csv). Unrounded Wolfram: central 0.0019771195178052915, width 0.0012407872583701455. Listed for branch completeness.

## Ranked predictions

### 1. CTC-1P — Flat ΛCDM, BAO only (frozen primary, legacy comparison only)

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

### 2. CTC-1B — Flat ΛCDM, BAO only (Lyα replacement branch, current-information forecast)

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

### 3. CTC-2P-R03 — Flat ΛCDM, BAO + compressed CMB (frozen primary, legacy comparison only) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** Flat ΛCDM; BAO + Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019)
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** FROZEN PRIMARY (legacy comparison only; DESI DR2 BAO official Lyα). Replaces held R02 row CTC-2P.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1420 ± 0.0625, DH/rd 17.8307 ± 0.0184
  - z=1.2: DM/rd 26.0500 ± 0.0657, DH/rd 14.9964 ± 0.0069
  - z=1.5: DM/rd 30.1982 ± 0.0661, DH/rd 12.7452 ± 0.0049
  - z=1.8: DM/rd 33.7434 ± 0.0652, DH/rd 10.9570 ± 0.0064
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred)). These ΛCDM predictive widths are parameter-only, conditional on the compressed CMB prior and massless-neutrino background. A 0.1% systematic floor is noted (r_d fitting formula versus CLASS `rs_d` offset +0.0861% on the LCDM_REPL_fullrs case in `R03/calc/class_crosscheck_r03_output.json`).
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-2P-R03`
- **Note:** R03 revision of held CTC-2P. Frozen R02 original untouched. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). Legacy comparison only.

### 4. CTC-2B-R03 — Flat ΛCDM, BAO + compressed CMB (Lyα replacement branch, current-information forecast) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** Flat ΛCDM; BAO + Planck 2018 compressed CMB (as CTC-2P-R03)
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; Eq. 26). Replaces held R02 row CTC-2B and the held R01 E-BAO-2 numbers. Alternative to the legacy CTC-2P-R03 row, not an independent prediction.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1601 ± 0.0612, DH/rd 17.8358 ± 0.0180
  - z=1.2: DM/rd 26.0691 ± 0.0643, DH/rd 14.9977 ± 0.0068
  - z=1.5: DM/rd 30.2173 ± 0.0648, DH/rd 12.7447 ± 0.0049
  - z=1.8: DM/rd 33.7622 ± 0.0639, DH/rd 10.9555 ± 0.0064
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred)). These ΛCDM predictive widths are parameter-only, conditional on the compressed CMB prior and massless-neutrino background. A 0.1% systematic floor is noted (r_d fitting formula versus CLASS `rs_d` offset +0.0861% on the LCDM_REPL_fullrs case in `R03/calc/class_crosscheck_r03_output.json`).
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-2B-R03`
- **Note:** R03 revision of held CTC-2B / E-BAO-2. Frozen originals untouched. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). This is the current-information forecast for this model.

### 5. CTC-3P-R03 — Constant-w (wCDM), BAO + compressed CMB (frozen primary, legacy comparison only) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** Flat wCDM, FROZEN PRIMARY branch (legacy comparison only); BAO + Planck 2018 compressed CMB. Conditional-fit MCMC w = −1.0312 ± 0.0405 (median and s.d.; see model-context section).
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** FROZEN PRIMARY (legacy comparison only). Replaces held R02 row CTC-3P.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1264 ± 0.0685, DH/rd 17.8837 ± 0.0805
  - z=1.2: DM/rd 26.0490 ± 0.0665, DH/rd 15.0394 ± 0.0640
  - z=1.5: DM/rd 30.2083 ± 0.0677, DH/rd 12.7765 ± 0.0465
  - z=1.8: DM/rd 33.7614 ± 0.0696, DH/rd 10.9786 ± 0.0327
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-3P-R03`
- **Note:** R03 revision of held CTC-3P. Frozen R02 original untouched. More model-dependent than the ΛCDM baselines above. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). Legacy comparison only.

### 6. CTC-3B-R03 — Constant-w (wCDM), BAO + compressed CMB (Lyα replacement branch, current-information forecast) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** Flat wCDM, DECLARED REPLACEMENT branch (current-information forecast); BAO + Planck 2018 compressed CMB (as CTC-3P-R03). Conditional-fit MCMC w = −1.0291 ± 0.0413 (median and s.d.; see model-context section).
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; Eq. 26). Replaces held R02 row CTC-3B. Alternative to the legacy CTC-3P-R03 row, not an independent prediction.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1458 ± 0.0668, DH/rd 17.8867 ± 0.0807
  - z=1.2: DM/rd 26.0687 ± 0.0650, DH/rd 15.0389 ± 0.0641
  - z=1.5: DM/rd 30.2276 ± 0.0665, DH/rd 12.7746 ± 0.0465
  - z=1.8: DM/rd 33.7800 ± 0.0687, DH/rd 10.9762 ± 0.0326
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-3B-R03`
- **Note:** R03 revision of held CTC-3B. Frozen R02 original untouched. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). This is the current-information forecast for this model.

### 7. CTC-4P-R03 — Curved ΛCDM (oΛCDM), BAO + compressed CMB (frozen primary, legacy comparison only) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** ΛCDM + Ωk, FROZEN PRIMARY branch (legacy comparison only); BAO + Planck 2018 compressed CMB (compressed priors are used outside their flat-model derivation — caveat in the R02 source row). Conditional-fit Laplace Ωk = +0.00199 ± 0.00125 (width kept at 0.00125; unrounded 0.001253061073170205; see model-context section).
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** FROZEN PRIMARY (legacy comparison only). Replaces held R02 row CTC-4P.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.0984 ± 0.0681, DH/rd 17.7697 ± 0.0423
  - z=1.2: DM/rd 25.9919 ± 0.0750, DH/rd 14.9403 ± 0.0357
  - z=1.5: DM/rd 30.1279 ± 0.0794, DH/rd 12.6954 ± 0.0316
  - z=1.8: DM/rd 33.6631 ± 0.0823, DH/rd 10.9131 ± 0.0282
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-4P-R03`
- **Note:** R03 revision of held CTC-4P. Frozen R02 original untouched. More model-dependent (free curvature). Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). Legacy comparison only.

### 8. CTC-4B-R03 — Curved ΛCDM (oΛCDM), BAO + compressed CMB (Lyα replacement branch, current-information forecast) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** ΛCDM + Ωk, DECLARED REPLACEMENT branch (current-information forecast); BAO + Planck 2018 compressed CMB (as CTC-4P-R03). Conditional-fit Laplace Ωk = +0.00198 ± 0.00124 (see model-context section).
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; Eq. 26). Replaces held R02 row CTC-4B. Alternative to the legacy CTC-4P-R03 row, not an independent prediction.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.1152 ± 0.0672, DH/rd 17.7749 ± 0.0420
  - z=1.2: DM/rd 26.0096 ± 0.0742, DH/rd 14.9421 ± 0.0354
  - z=1.5: DM/rd 30.1458 ± 0.0786, DH/rd 12.6954 ± 0.0312
  - z=1.8: DM/rd 33.6808 ± 0.0816, DH/rd 10.9122 ± 0.0278
- **Band / coverage level (as stated in the source):** Laplace (Hessian) ±1 standard deviation (68.3% central for a Gaussian), as stated in RECOMPUTED_ROWS_R03.csv column header: predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 original of the replaced row was not edited and is not used here.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-4B-R03`
- **Note:** R03 revision of held CTC-4B. Frozen R02 original untouched. Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). This is the current-information forecast for this model.

### 9. CTC-5P-R03 — CPL (w0waCDM), BAO + compressed CMB (frozen primary, legacy comparison only) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** R03 revision supplies bands (R02 was NOT READY / missing bands); PROVISIONAL, pending review / PROVISIONAL
- **Model:** CPL (w0waCDM); BAO + Planck 2018 compressed CMB
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** FROZEN PRIMARY (legacy comparison only). Replaces held/missing R02 row CTC-5P (R02 had no primary bands).
- **Numeric prediction:**
  - z=0.9: DM/rd 21.049 [20.977, 21.122], DH/rd 17.761 [17.661, 17.860]
  - z=1.2: DM/rd 25.968 [25.897, 26.040], DH/rd 15.106 [15.024, 15.197]
  - z=1.5: DM/rd 30.161 [30.088, 30.232], DH/rd 12.904 [12.829, 12.983]
  - z=1.8: DM/rd 33.753 [33.677, 33.828], DH/rd 11.106 [11.047, 11.165]
- **Band / coverage level:** MCMC posterior median and 68% interval only. The 95% interval reported in the source is not published here: the CPL posterior is prior-touched (1.9917% of PRIMARY samples and 0.6767% of REPLACEMENT samples have wa < −3.5 against the −4 edge, from the saved 60,000-sample chains and `fullrs_r03_output.json`; w0+wa<0 is imposed in `R03/calc/cplmodel_r03.py` function `inprior`). emcee 40×10000, burn 2500, thin 5; Laplace not used.
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv (bands also in CPL_OLDPRIMARY_R03.csv / CPL_OLDPRIMARY_BANDS_R03.csv). This is an R03 revision; the frozen R02 CTC-5P row was not edited.
- **Conditional-fit parameters (not a scored forecast; 16/50/84 percent points):** Ωm 0.3555 [0.3318, 0.3820], h 0.6385 [0.6171, 0.6599], w0 −0.4167 [−0.6570, −0.1476], wa −1.7592 [−2.5757, −1.0548], ω_b 0.0223 [0.0222, 0.0225]. Copied from `R03/RECOMPUTED_ROWS_R03.csv` row CTC-5P-R03 and verified this turn from the saved chain `R03/calc/fullrs_cpl_chain_PRIMARY_R03.npy` (60,000 samples after burn 2,500, thin 5). **revision: md quantile error corrected from chain**
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-5P-R03`; chain `R03/calc/fullrs_cpl_chain_PRIMARY_R03.npy`
- **Note:** R03 revision filling the R02 CTC-5P gap. Most model-dependent of the distance curves (two dark-energy parameters). Frozen originals untouched. `CPL_OLDPRIMARY_R03.md` was left untouched; its PRIMARY Ωm line used the 16/2.5/50 percent points as if they were the 50/16/84 band. This pack uses the chain-verified 50/16/84 value above (0.3555 [0.3318, 0.3820]) and does not use that md line. 68% bands only (prior-touched; see coverage). Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). Legacy comparison only.

### 10. CTC-5B-R03 — CPL (w0waCDM), BAO + compressed CMB (Lyα replacement branch, current-information forecast) — R03 revision

- **Author:** C.A.S.D.R
- **Wording:** prospective, model-conditional
- **Label in source:** conditional theory curve
- **Revision label:** R03-recomputed (r_s integral corrected)
- **Readiness / verification:** READY (R03 revision; PROVISIONAL, pending review) / PROVISIONAL
- **Model:** CPL (w0waCDM); BAO + Planck 2018 compressed CMB (as CTC-5P-R03)
- **Observable and units:** DM/rd and DH/rd (dimensionless)
- **Redshift (z) / grid:** z = 0.9, 1.2, 1.5, 1.8
- **Data product / release:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later). NOT Foundation.
- **Branch:** DECLARED REPLACEMENT (current-information forecast; Eq. 26). Replaces held R02 row CTC-5B and the held R01 E-BAO-3 numbers. Alternative to the legacy CTC-5P-R03 row, not an independent prediction.
- **Numeric prediction:**
  - z=0.9: DM/rd 21.087 [21.016, 21.157], DH/rd 17.789 [17.689, 17.887]
  - z=1.2: DM/rd 26.007 [25.938, 26.076], DH/rd 15.093 [15.012, 15.182]
  - z=1.5: DM/rd 30.193 [30.123, 30.262], DH/rd 12.877 [12.805, 12.959]
  - z=1.8: DM/rd 33.777 [33.704, 33.851], DH/rd 11.080 [11.021, 11.143]
- **Band / coverage level:** MCMC posterior median and 68% interval only. The 95% interval reported in the source is not published here: the CPL posterior is prior-touched (1.9917% of PRIMARY samples and 0.6767% of REPLACEMENT samples have wa < −3.5 against the −4 edge, from the saved 60,000-sample chains and `fullrs_r03_output.json`; w0+wa<0 is imposed in `R03/calc/cplmodel_r03.py` function `inprior`). emcee 40×10000, burn 2500, thin 5; Laplace not used.
- **Date frozen:** R03 revision file mtime 2026-11-12 05:14 ET (America/Toronto) for R03/RECOMPUTED_ROWS_R03.csv. This is an R03 revision; the frozen R02 CTC-5B original was not edited and is not used here.
- **Conditional-fit parameters (not a scored forecast; 16/50/84 percent points):** Ωm 0.3463 [0.3234, 0.3720], h 0.6469 [0.6254, 0.6682], w0 −0.5308 [−0.7623, −0.2638], wa −1.4209 [−2.2372, −0.7542], ω_b 0.0223 [0.0222, 0.0225]. Copied from `R03/RECOMPUTED_ROWS_R03.csv` row CTC-5B-R03 and verified this turn from the saved chain `R03/calc/fullrs_cpl_chain_REPLACEMENT_R03.npy` (60,000 samples after burn 2,500, thin 5). No quantile-index error found on this branch.
- **Source:** `R03/RECOMPUTED_ROWS_R03.csv` row `CTC-5B-R03`; chain `R03/calc/fullrs_cpl_chain_REPLACEMENT_R03.npy`
- **Note:** R03 revision of held CTC-5B / E-BAO-3. Frozen originals untouched. 68% bands only (prior-touched; see coverage). Evaluated exactly at z = 0.9, 1.2, 1.5, 1.8 (not interpolated). This is the current-information forecast for this model.

### 11. D-P4a — BAO-only matter density stays low

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
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default; author to confirm label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P4a`
- **Note:** Not held (BAO-only projected interval). Box-fit context numbers from the R02 notes field are not repeated here.

### 12. D-P4b — BAO-only Ωm stays below the Planck value

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

### 13. D-P8a — Early-universe H0

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
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default; author to confirm label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P8a`

### 14. D-P8c — Ladder H0 stays at 72.5–73.5

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

### 15. D-P2a — Pivot equation of state near −1

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
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default; author to confirm label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P2a`
- **Note:** Prediction text is the R02/R01 interval, which HELD_R03.md says is unchanged. The box-reference width in the R02 notes field is held and is not reproduced here.

### 16. D-P3a — w0, wa inside predicted boxes

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
- **Band / coverage level (as stated in the source):** Forecaster's central 68% prediction interval (R01 default; author to confirm label). No full distribution specified; interval used as stated.
- **Date frozen:** Forecast text dated 2026-10-13 (calibration data cutoff field in R02/FORECAST_TABLE_R02.csv). R02 table file mtime 2026-11-12 04:51 ET (America/Toronto).
- **Source:** `R02/FORECAST_TABLE_R02.csv` row `D-P3a`
- **Note:** Not held (HELD_R03.md: uses projected published-DR2 widths, not a box CMB fit). Retrospective DR2 context in the R02 notes field is not repeated here.

### 17. D-P3b — w0–wa quadrant not abandoned

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

### 18. D-P3c — w0, wa errors shrink at least 20% from DR2

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

### 19. D-P5a — Neutrino mass limit below 0.055 eV

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

### 20. D-P5b — No relaxed neutrino limit or detection

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

### 21. D-P7 — No hemispheric BAO difference

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

### 22. E-CD-P2 — Count-dipole direction

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

### 23. E-CD-P3 — Dipole rises with redness or redshift

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

### 24. E-PHZ-1 — Capped adaptive PHZ beats native PHZ (method, not cosmology)

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
- Held frozen originals of BAO+CMB distance rows, not used: CTC-2P, CTC-2B, CTC-3P, CTC-3B, CTC-4P, CTC-4B, CTC-5B, CTC-5P, and R01 E-BAO-2, E-BAO-3. Replaced in this pack by the R03 revisions above.
- R05 growth rows (held). Unsupported / not-run alternative models in R02/UNSUPPORTED_MODELS_R02.md (massive neutrinos as a fitted model, Hu–Sawicki f(R), JBD, nDGP, k-mouflage, mixed cold/warm DM, decaying DM).
- Items listed in FORECASTS_R01.md §6 as deliberately not forecasts (including Fibonacci normalisations, GW/BAO siren ratio, geometry latent moments, DESI P9, and published GWTC values), names only.

## Assembly note

Pack path: `/workspace/r03-out/euclid_forecast_bot/PUBLISH_20261112/REV2/`. REV2 written 2026-11-12, about 05:55 ET (America/Toronto), from REV1. The v0 files in the parent folder and the REV1 files were left untouched. Every numeric value above is copied from the cited source file and row, or computed from the saved chains / `fullrs_r03_output.json` / `class_crosscheck_r03_output.json` named in SOURCES_20261112_REV2.md. No number was invented. Nothing was posted, uploaded or timestamped.
