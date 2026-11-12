> **SUPERSEDED (about 05:16 ET).** This version used r_s(z*) cut at z = 1e5 (see HELD_R03.md). The current version is CPL_OLDPRIMARY_R03.md and .csv. It is kept only as a record, and its validation V1 (code path reproduces R02 CTC-5B, 150/150) is still the code-path validation.

# CPL_OLDPRIMARY_R03 — CPL (w0waCDM) bands for the frozen old-DESI PRIMARY branch (proposal recorded at the time)

Dated 2026-11-12, about 05:05 ET (10:05 UTC). This is a new R03 file. It fills the gap left by R02 row CTC-5P (NOT READY, "old-CPL bands missing") without editing R02. R02, R01 and every frozen file are unchanged. Nothing was posted or timestamped.

**Label: conditional theory curve** (as with R02 CTC-5B). The calibration data are fully public; the Euclid target does not yet exist. PROVISIONAL (simplified pipeline: compressed CMB, rd fitting formula, no SNe).

## Why R04 had no primary bands, and what R03 did
- R04's Wolfram Hessian for CPL was not positive-definite along the w0–wa degeneracy, so R04 discarded its CPL Laplace errors. R04 then produced bands only for the REPLACEMENT branch, by importance-reweighting the existing box chain.
- **The existing chain `/workspace/desi_r01/chain_w0waCDM.npy` was sampled on the old (PRIMARY) DESI data** (fit_cpl.py; emcee, 24 walkers × 3000 steps, 1000 discarded, 48,000 samples). Its unweighted samples are therefore the PRIMARY posterior. R03 computes the bands from it with the same quantile code R04 used for CTC-5B. So the PRIMARY-vs-REPLACEMENT difference comes only from the data, with no Monte Carlo noise.
- Valid covariance: the 8×8 predictive covariance is the chain's sample covariance. It is positive-definite (smallest eigenvalue 1.01e-15, largest 0.0253), but the condition number is 2.5e+13, so it has about 5 effective directions (= 5 parameters). Score with C_E + C_pred, never with C_pred alone.
- Hessian check: my Python central-difference Hessians are positive-definite at every step tried, but **not step-stable**. For steps ×1e-3 / ×3e-3 / ×1e-2, w0's s.d. is 0.253 / 0.137 / 0.045; the chain's 68% half-width is 0.297. Laplace bands are therefore NOT used. R04's conclusion stands.

## Bands: same grid and format as R02 CTC-5B (median [68%] {95%})
| z | DM/rd PRIMARY (R03) | DH/rd PRIMARY (R03) | DM/rd REPLACEMENT (R02 CTC-5B) | DH/rd REPLACEMENT (R02 CTC-5B) |
|---|---|---|---|---|
| 0.9 | 20.990 [20.912, 21.069] {20.841, 21.143} | 17.615 [17.517, 17.716] {17.419, 17.803} | 20.997 [20.923, 21.071] {20.854, 21.140} | 17.627 [17.529, 17.726] {17.434, 17.808} |
| 1.2 | 25.843 [25.767, 25.922] {25.695, 26.002} | 14.836 [14.762, 14.920] {14.693, 15.025} | 25.854 [25.781, 25.927] {25.713, 26.001} | 14.846 [14.772, 14.932] {14.702, 15.039} |
| 1.5 | 29.949 [29.873, 30.025] {29.800, 30.100} | 12.600 [12.528, 12.682] {12.470, 12.765} | 29.963 [29.889, 30.035] {29.818, 30.103} | 12.608 [12.536, 12.690] {12.477, 12.774} |
| 1.8 | 33.451 [33.375, 33.528] {33.303, 33.598} | 10.814 [10.750, 10.878] {10.699, 10.935} | 33.467 [33.391, 33.542] {33.321, 33.608} | 10.819 [10.756, 10.882] {10.705, 10.938} |

F_AP = DM/DH (derived; never scored separately): z=0.9 1.1917 [1.1842, 1.1989]; z=1.2 1.7420 [1.7302, 1.7528]; z=1.5 2.3760 [2.3602, 2.3923]; z=1.8 3.0921 [3.0744, 3.1124]. The full 10-z grid (0.9–1.8) is in `CPL_OLDPRIMARY_BANDS_R03.csv`.

Parameter posterior (PRIMARY chain; median [16, 84]): Om 0.3465 [0.3182, 0.3747]; h 0.6801 [0.6557, 0.7080]; w0 -0.7184 [-1.0149, -0.4200]; wa -0.9761 [-1.8987, -0.0991]; ob 0.0221 [0.0220, 0.0223]. 0.39% of samples have wa < −3.5 (near the −4 prior edge).

Predictive correlation (order DM,DH at z=0.9,1.2,1.5,1.8):
```
+1.000 +0.160 +0.949 -0.388 +0.821 -0.566 +0.654 -0.641
+0.160 +1.000 +0.439 +0.611 +0.583 +0.259 +0.623 +0.061
+0.949 +0.439 +1.000 -0.097 +0.953 -0.346 +0.838 -0.473
-0.388 +0.611 -0.097 +1.000 +0.205 +0.922 +0.442 +0.822
+0.821 +0.583 +0.953 +0.205 +1.000 -0.048 +0.963 -0.196
-0.566 +0.259 -0.346 +0.922 -0.048 +1.000 +0.221 +0.978
+0.654 +0.623 +0.838 +0.442 +0.963 +0.221 +1.000 +0.074
-0.641 +0.061 -0.473 +0.822 -0.196 +0.978 +0.074 +1.000
```

## Validation
| check | result |
|---|---|
| V0 vectorised model vs scipy.quad (distances, z*, r_s) | max relative difference 2.1e-15; χ² at R02/R04 best fits reproduces 29.12778 / 26.21434 (`calc/check_model_r03.log`) |
| **V1 rerun given the REPLACEMENT data reproduces R02 CTC-5B** (same chain reweighted to Eq. 26) | **PASS: all 150 numbers (10 z × 3 quantities × 5 quantiles) match R04 §5 / R02 exactly after rounding (max diff 0)** |
| V2 independent fresh emcee (seeded 20261112, 40 walkers × 8000 steps, 2000 discarded, thin 5) on REPLACEMENT vs R02 CTC-5B | max median difference 0.0077; 68% widths within 6% |
| V3 fresh emcee on PRIMARY vs original chain PRIMARY | max median difference 0.0037; 68% widths within 8% |
| V4 Cosmology's independent PRIMARY chain (VERIFY_R02_COSMOLOGY.md §1) | z=0.9 DM/rd 20.988 (R03 20.990), DH/rd 17.603 (R03 17.615); z=1.8 33.445 / 10.812 (R03 33.451 / 10.814): agreement ≤ 0.012 |
| autocorrelation (fresh runs) | τ ≈ 193, 193, 184, 175, 90 steps: about 30τ per walker after burn-in, below emcee's 50τ guidance. The original chain is shorter (~10τ). Medians agree to ≤0.004 across chains; treat bands as ±0.01-level Monte Carlo accurate |
| predictive covariance | positive-definite; near rank-5 (expected) |

## Freeze block — CTC-5P-R03

- **label:** conditional theory curve
- **readiness:** READY
- **verification:** PROVISIONAL
- **outcome:** NOT_RUN
- **branch:** PRIMARY
- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8}. NOT Foundation (Foundation has no BAO/clustering products).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / grid:** DM/rd, DH/rd (dimensionless) on z = 0.9, 1.2, 1.5, 1.8; F_AP = DM/DH derived, not scored separately; scale grid: n/a (BAO distances)
- **model and priors:** Flat CPL w(a)=w0+wa(1−a); radiation with N_eff=3.046; rd fitting formula (ω_ν=0.00064); priors exactly as the chain was sampled (fit_cpl.py L35): 0.1<Ωm<0.6, 0.4<h<1, −3<w0<1, −4<wa<2, w0+wa<0, 0.018<ω_b<0.027
- **calibration data cutoff:** DESI DR2 BAO 13 points with the ORIGINAL Lyα pair (old-DESI primary, /workspace/desi_r01 mean/cov) + Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019). No SNe. Chain file chain_w0waCDM.npy predates 2026-11-12.
- **exposure to target outcomes:** Calibration data fully exposed by construction; the Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 sample covariance of the chain predictions (R03/calc/cpl_oldprimary_r03_output.json chain_primary.predcov; positive-definite, but its condition number is about 2.5e13, so it carries only about 5 independent directions = the 5 parameters). Shared calibration: A = c/(H0 rd) is common to all 8 numbers. s.d. by element: 0.0781, 0.0989, 0.0783, 0.0821, 0.0762, 0.0759, 0.0765, 0.0617
- **predictive distribution:** Posterior median, 68% interval [ ] and 95% interval { } from the original box emcee chain (fit_cpl.py, old DESI DR2 Lyα data, 48,000 samples, unweighted): z=0.9: DM/rd 20.990 [20.912, 21.069] {20.841, 21.143}, DH/rd 17.615 [17.517, 17.716] {17.419, 17.803}; z=1.2: DM/rd 25.843 [25.767, 25.922] {25.695, 26.002}, DH/rd 14.836 [14.762, 14.920] {14.693, 15.025}; z=1.5: DM/rd 29.949 [29.873, 30.025] {29.800, 30.100}, DH/rd 12.600 [12.528, 12.682] {12.470, 12.765}; z=1.8: DM/rd 33.451 [33.375, 33.528] {33.303, 33.598}, DH/rd 10.814 [10.750, 10.878] {10.699, 10.935}. s_pred = half-width of the 68% interval.
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073); FAIL otherwise. m = chain medians, interpolated linearly in z.
- **abstention:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]; points outside the grid are not scored.
- **sources:** /workspace/desi_r01/chain_w0waCDM.npy, fit_cpl.py; R03/calc/cpl_oldprimary_r03.py and output JSON
- **notes:** Non-Gaussian posterior (w0–wa degeneracy; wa reaches the −4 prior edge for 0.4% of samples). Numerical Hessians are positive-definite but step-dependent (w0 s.d. 0.25/0.14/0.045 for steps 1e-3/3e-3/1e-2), so Laplace bands are NOT valid. The MCMC covariance is used; an independent seeded emcee rerun agrees (see validation). Same chain as R02 CTC-5B, but unweighted: the primary-to-replacement difference therefore contains no Monte Carlo noise.

**Scoring caveat (from Cosmology's review):** R02's "interpolate linearly in z" step is biased. R03 does not repeat it. Off-node z_eff must be handled by the proposal in `PROPOSALS/SCORING_PROPOSAL_R03.md` (pending the author's decision). Until the author decides, this row is scored only at the four nodes, or exactly from the frozen chain at the published z_eff.

**Open for the author:** freeze this row as the filled CTC-5P, or keep CTC-5P NOT READY. Note also that R02 CTC-5B's model field states the priors as "−3<w0<1, −5<wa<3; 0.015<ω_b<0.03", but the chain behind it was sampled with −4<wa<2, w0+wa<0 and 0.018<ω_b<0.027 (fit_cpl.py L35). That is a wording error in R02, which R03 records but does not edit.