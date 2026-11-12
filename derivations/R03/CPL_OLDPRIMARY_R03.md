# CPL_OLDPRIMARY_R03 — Task A: CPL old-DESI-primary bands, corrected r_s (proposal recorded at the time)

Dated 2026-11-12, about 05:17 ET (America/Toronto). Label: **conditional theory curve**. Status: PROVISIONAL and NOT_RUN. Nothing posted or timestamped; the posting hold is in force.
This supersedes CPL_OLDPRIMARY_R03_SUPERSEDED_TRUNCRS.md.

## Row
- **Row:** `CPL_OLDPRIMARY_R03.csv`, one row, `CTC-5P-R03`, in the same columns and format as R02 CTC-5B. It contains the full freeze block: product, acquisition, cuts, observable, model and priors, calibration cutoff, exposure, mask, contaminants, estimator, covariance, predictive, scoring, abstention and sources.
- **Bands:** `CPL_OLDPRIMARY_BANDS_R03.csv` covers z = 0.9…1.8 in steps of 0.1. It gives the median, 16/84 and 2.5/97.5 quantiles for DM/rd, DH/rd and DM/DH.
- **Corrected replacement branch:** the same file also carries `REPLACEMENT_fullrs_emcee_R03` (CTC-5B-R03), plus the superseded truncated primary for comparison.

## Method
- **Model:** flat CPL with N_eff = 3.046 radiation and the r_d fitting formula. r_s(z*) is integrated **to infinity** using 96-node Gauss–Legendre in a ∈ [0, a*]; it equals quad and Wolfram NIntegrate to ∞ within 2e-14.
- **Data:** DESI DR2 BAO, 13 points with the ORIGINAL Lyα pair (/workspace/desi_r01 mean sha 9ac154ab…, cov 252a1432…), plus Planck 2018 compressed priors (R, l_A, ω_b).
- **Priors:** as in fit_cpl.py L35.
- **Sampling:** emcee 3.1.6, 40 walkers × 10,000 steps, burn 2,500, thin 5. This gives 60,000 samples. τ = 188/191/180/166/91, so the chain spans about 40τ. Acceptance 0.44, seed 20261112.
- **Code:** `calc/fullrs_r03.py` produces `calc/fullrs_r03_output.json` and the chain `calc/fullrs_cpl_chain_PRIMARY_R03.npy`. `calc/build_cpl_fullrs_r03.py` produces the CSVs.
- **Covariance:** the full 8×8 predictive sample covariance (DM, DH at 4 z). It is positive-definite (eigenvalues 1.2e-15 to 2.5e-2), but its effective rank is 5. The shared calibration A = c/(H0 rd) is common to all eight numbers.
- **Why not Laplace:** the Laplace/Hessian covariance is step-dependent for CPL (non-Gaussian w0–wa posterior), so it is NOT used. The MCMC covariance is used.

## Bands, PRIMARY (old Lyα), median [68%] {95%}
| z | DM/rd | DH/rd |
|---|---|---|
| 0.9 | 21.049 [20.977, 21.122] {20.908, 21.191} | 17.761 [17.661, 17.860] {17.561, 17.960} |
| 1.2 | 25.968 [25.897, 26.040] {25.827, 26.109} | 15.106 [15.024, 15.197] {14.948, 15.288} |
| 1.5 | 30.161 [30.088, 30.232] {30.016, 30.301} | 12.904 [12.829, 12.983] {12.763, 13.061} |
| 1.8 | 33.753 [33.677, 33.828] {33.603, 33.901} | 11.106 [11.047, 11.165] {10.991, 11.215} |

Parameter medians [68%]:
- Ωm 0.332 [0.310, 0.356]
- h 0.638 [0.617, 0.660]
- w0 −0.417 [−0.657, −0.148]
- wa −1.759 [−2.576, −1.055]
- 2.0% of samples have wa < −3.5, near the −4 prior edge.

## REPLACEMENT (Eq. 26 Lyα), corrected CTC-5B-R03, median [68%]
| z | DM/rd | DH/rd |
|---|---|---|
| 0.9 | 21.087 [21.016, 21.157] | 17.789 [17.689, 17.887] |
| 1.2 | 26.007 [25.938, 26.076] | 15.093 [15.012, 15.182] |
| 1.5 | 30.193 [30.123, 30.262] | 12.877 [12.805, 12.959] |
| 1.8 | 33.777 [33.704, 33.851] | 11.080 [11.021, 11.143] |

Parameters: w0 −0.531 [−0.762, −0.264], wa −1.421 [−2.237, −0.754].

## Shift from the truncated version (PRIMARY medians, new/old − 1)
| z | DM/rd | DH/rd | DM/DH |
|---|---|---|---|
| 0.9 | +0.28% | +0.83% | −0.55% |
| 1.3 | +0.56% | +2.06% | −1.46% |
| 1.8 | +0.90% | +2.69% | −1.72% |

## Validation (calc/cpl_validation_fullrs_r03.json)
- **V1, code-path validation against R02's replacement numbers on that branch's data:** with `RSMODE='trunc'`, the R03 code reweighting the R04 chain to the REPLACEMENT likelihood reproduces R02 CTC-5B / R04 §5 exactly. That is 150/150 numbers, max |diff| 0 after rounding. **PASS.** The R02 numbers being reproduced are themselves HELD; this proves the R03 code equals the R02 code apart from the one fixed line.
- **V2:** Python full-r_s best fits equal the Wolfram fits (common_R03_fullrs.wl) for ΛCDM and wCDM to ≤1e-7 in parameters and 1e-11 in χ². **PASS.**
- **V3:** independent consistency check. Importance-reweighting the full-r_s PRIMARY chain to the REPLACEMENT likelihood (ESS 42,000) reproduces the fresh REPLACEMENT chain's DM/rd and DH/rd medians at all 4 z to ≤0.0036 (MC level). **PASS.**
- **V4: CLASS 3.4.2 as second code**, over 60 random PRIMARY chain points at z = 0.9, 1.2, 1.3, 1.5, 1.8:
  - max |ΔDM/DM| = 4.9e-4
  - max |ΔDH/DH| = 2.4e-4
  - r_d fitting formula vs CLASS rs_d: max 9.6e-4
  - DM/rd (formula r_d) vs CLASS DM/rs_d: max 9.2e-4
  - At the best fit, r_s(z*) is +0.038% vs CLASS rs_rec (truncated: −1.80%).
  - All differences are far below the band half-widths (about 0.35% in DM/rd).
  - The CLASS settings are listed in VALIDATION_R03.md §3.
- **V5:** τ is about 1/40 of the chain length. That is adequate for medians and 68% bands. The 95% tails carry roughly 1–2% Monte Carlo error.

## Scoring (as in the row; R02 rule unchanged)
- **Rule:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N).
- **Interpolation:** this row's m is linear in z, as in R02. Cosmology's review found that linear interpolation biases off-node points. The scoring proposal (PROPOSALS/SCORING_PROPOSAL_R03.md, pending the author's decision) would replace it with exact evaluation or a fine-grid cubic. This row has NOT been retuned to that proposal.
