# HELD_R03 — rows and results HELD because of the sound-horizon truncation bug

Written 2026-11-12, about 05:15 ET (America/Toronto). Written as an internal hold record; the r_s truncation issue it documents is part of the published R03 revision. No R01, R02, R04, R05 or frozen file was edited. This file only marks those rows as HELD; the corrected values live in R03.

## The bug (confirmed by me, not just reported)
`/workspace/desi_r01/fit_cpl.py` line 29 is `rs=quad(...,zs,1e5,limit=200)[0]`. It stops the comoving sound-horizon integral r_s(z*) at z = 10^5 instead of infinity. It feeds the Planck compressed priors R and l_A (l_A = π D_M(z*)/r_s(z*)). The same cut-off appears in:
- `wolfram_R04/crosscheck_scipy_R04.py` L26
- `wolfram_R04/call_old.wl` L20 (`{z,zst,1*^5}`)
- **my R02 `R02/wolfram/common_R02.wl` line 23** (`Log[1+10.^5]`)
- my first R03 `calc/cplmodel_r03.py` (`u1=np.log1p(1e5)`; now behind a switch: `RSMODE` defaults to `'trunc'` only so the V1 R02 reproduction stays exact; every corrected run sets `RSMODE='full'` explicitly)
- my R03 `calc/check_model_r03.py`, which only compared against an equally truncated quad.

Self-audit of my R01 scripts: R01 computed no CMB fit of its own. Its E-BAO-2/3 numbers and D-P basis notes were copied from R04 and `fit_results.json`, so they inherit the bug. The R01 BAO-only checks do not.

Size (calc/rs_bug_check_r03.py and .log):
- At the R02 ΛCDM best fit, truncated r_s(z*) = 137.844 Mpc vs 140.493 Mpc to infinity, a −1.885% shortfall.
- At Coordinator's and Planck's parameters the shortfall is −1.84%.
- The 96-node Gauss–Legendre integral in a ∈ [0, a*] equals quad to infinity to 1e-15 and Wolfram NIntegrate[…, Infinity] to 2e-14 (140.4929173112).
- Convergence: cut at 1e6 gives 140.225, 1e7 gives 140.466, 1e8 gives 140.490.
- **CLASS 3.4.2 check:** with my integral evaluated at CLASS's z_rec, full r_s is +0.038% vs CLASS `rs_rec` and truncated r_s is −1.80% (calc/class_crosscheck_r03_output.json).

## HELD list (reason: computed through the truncated r_s(z*) code path)
| Item | Where | Why held | R03 replacement |
|---|---|---|---|
| E-BAO-2 (flat ΛCDM, BAO + CMB, Lyα-swapped) | R01 | numbers from R04 §5 (reweighted fit_cpl chains) | CTC-2B-R03 in RECOMPUTED_ROWS_R03.csv |
| E-BAO-3 (CPL, BAO + CMB, Lyα-swapped) | R01 | numbers from R04 §5 | CTC-5B-R03 (same file; bands in CPL_OLDPRIMARY_BANDS_R03.csv) |
| D-P2a basis note only (box w_pivot −1.0443 ± 0.0501; R04 §7 coverage "77%", "±0.098") | R01 | from fit_results.json (fit_cpl.py) | not recomputed. **the author's prediction text is unchanged**; only the box reference σ is held |
| R05 fσ8 / σ8 / S8 (all rows of xact_R05/RESULTS_R05 §3) | R05 (Coordinator) | fs8_camb_R05.py uses fit_cpl chains and R04 best fits | calc/fs8_fullrs_r03_output.json (see below) |
| CTC-2P / CTC-2B (ΛCDM BAO + CMB) | R02 | common_R02.wl | CTC-2P-R03 / CTC-2B-R03 |
| CTC-3P / CTC-3B (wCDM BAO + CMB) | R02 | common_R02.wl | CTC-3P-R03 / CTC-3B-R03 |
| CTC-4P / CTC-4B (oΛCDM BAO + CMB) | R02 | common_R02.wl | CTC-4P-R03 / CTC-4B-R03 |
| CTC-5B (CPL replacement) | R02 | R04 chains reweighted, fit_cpl.py | CTC-5B-R03 |
| CTC-5P (gap) | R02 | the first R03 rerun used the truncated chain | CTC-5P-R03 (CPL_OLDPRIMARY_R03.csv) |
| RF-2, RF-3, RF-4, RF-5 (BAO + CMB parameters) | R02 | as above | parameters in RECOMPUTED_ROWS_R03.csv |
| INTERNAL χ² values for BAO + CMB fits | R02 INTERNAL_CONTEXT, R04 §4a/§4c | as above | `chi2_INTERNAL` column in RECOMPUTED_ROWS_R03.csv (INTERNAL) |
| R04 §4 (CPL vs ΛCDM BAO + CMB fit), §4c, §5 tables | R04 (Coordinator) | fit_cpl.py and call_old.wl | as above |
| My own superseded R03 outputs | R03 | truncated r_s | renamed `*_SUPERSEDED_TRUNCRS.*`; marked in W_RECONCILE, PROPOSALS and the CPL md |

**Not affected (no sound horizon at z*, so no CMB):**
- CTC-1P/1B and RF-1 (BAO-only free-A)
- E-BAO-1
- the BF-2 reproduction (−0.9674)
- INCREMENT_8929251 (a)–(c) and the author's scripts (d)
- R04 §1–3 and §6
- the dipole and lensing rows

D-P3a and D-P4a use projected published-DR2 σ, not a box CMB fit, so they are not held. Flagged for the author to confirm the source of 0.0456/0.0399 and 0.00688/0.0086.

## Shift sizes (old truncated → corrected)
**Best fits, BAO + compressed CMB.** Wolfram for ΛCDM, wCDM and oΛCDM; Python agrees to ≤1e-7 in parameters.

| Fit | Old (R02/R04) | Corrected R03 |
|---|---|---|
| ΛCDM PRIMARY Ωm, h | 0.32397, 0.69868 | **0.30274 ± 0.00388, 0.68644 ± 0.00302** |
| ΛCDM REPLACEMENT Ωm, h, Ωm h², r_d | 0.32428, 0.69846, 0.15820, 144.0 | **0.30387, 0.68559, 0.14283, 147.03 Mpc** (Coordinator: 0.3039, 0.6856, 0.1428, 147.0 → **matches**) |
| wCDM w (P / B), Laplace | −1.043 / −1.049 ± 0.049 | **−1.0280 / −1.0270 ± 0.042** (MCMC −1.0312 ± 0.0405 / −1.0291 ± 0.0413) |
| oΛCDM Ωk (P / B) | −0.0034 ± 0.0013 / −0.0036 ± 0.0012 | **+0.00199 ± 0.00125 / +0.00198 ± 0.00124** (sign flips) |
| CPL w0, wa median (P) | −0.718, −0.976 | **−0.417, −1.759** |
| CPL w0, wa median (B) | −0.700, −1.069 (R04 reweighted) | **−0.531, −1.421** |

**z = 1.3, flat ΛCDM, old/new − 1** (calc/fullrs_r03_output.json `shifts`):
- PRIMARY: DH/rd −1.888%, F_AP = DM/DH +1.199%, DM/rd −0.711%.
- REPLACEMENT: DH/rd −1.891%, F_AP +1.150%, DM/rd −0.762%.
- **This matches Coordinator's expectation (DH about 1.9% low and F_AP about 1.2% high).**
- At z = 0.9 the shifts are DH −1.45%/−1.48% and F_AP +1.05%/+1.01%; at z = 1.8 they are DH −2.19%/−2.18% and F_AP +1.26%/+1.20%.

**CPL PRIMARY medians, new/old − 1:**
- z = 1.3: DH +2.06%, DM +0.56%, F_AP −1.46%
- z = 1.8: DH +2.69%, F_AP −1.72%

These are of the same order as the band widths, so every BAO + CMB row really does change.

**R05 growth (recomputed, REPLACEMENT branch, same CAMB settings as R05):** see calc/fs8_fullrs_r03_output.json. ΛCDM σ8(0) is now 0.826 [0.820, 0.832] and S8 is 0.832, against R05's 0.896 and 0.931. The R05 caveat "σ8 ≈ 0.90, S8 ≈ 0.93, well above Planck" was caused mostly by this bug (Ωm 0.324 → 0.304). Other values are in VALIDATION_R03.md.

## What is still HELD after recompute
- The R03 recomputed rows are PROVISIONAL, pending the author's review at the time of writing.
- The R02, R01 and R04 originals stay HELD; they were not edited.
- D-P2a's box reference σ was not recomputed (it needs a full-r_s DESI-pivot calculation, which is outside this scope).
