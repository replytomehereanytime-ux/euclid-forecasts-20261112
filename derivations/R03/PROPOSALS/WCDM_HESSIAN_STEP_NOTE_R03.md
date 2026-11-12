# Proposal, pending the author's decision: R03 correction block (about 05:16 ET)
The numbers below this block used the truncated r_s(z*), so they are SUPERSEDED. The step-scan conclusion stands; the numbers change.

With full r_s (calc/wcdm_stepscan_fullrs_r03.py and .log; step in units of the parameter s.d.):

| step | s.d.(w) PRIM | s.d.(w) REPL |
|---|---|---|
| 0.003 | 0.04021 | 0.04039 |
| 0.01 | 0.04021 | 0.04038 |
| 0.03 | 0.04016 | 0.04033 |
| 0.1 | 0.03961 | 0.03978 |
| 0.3 | 0.03559 | 0.03574 |
| 1.0 | 0.02036 | 0.02043 |
| MCMC s.d. (emcee 32×5000) | 0.0405 | 0.0413 |
| Wolfram fitm (R02 step rule) | 0.0422 | 0.0423 |

Reading:
- The converged Laplace width is 0.040. The MCMC width is 0.041. Large steps underestimate the width.
- The corrected best-fit w is −1.028 (PRIM) and −1.027 (REPL), with MCMC medians −1.031 and −1.029.
- Cosmology's 0.0467 was computed with the truncated code path, so it is not directly comparable any more.
- **Proposal:** quote the MCMC s.d. and record the step.


---
**Everything below this line is the ORIGINAL (about 05:10 ET) text. Rows that include the CMB are SUPERSEDED (truncated r_s); BAO-only rows still stand.**

# WCDM_HESSIAN_STEP_NOTE_R03 — PROPOSAL / NOTE, PENDING THE AUTHOR'S DECISION (proposal recorded at the time)

R02 CTC-3P/3B quote w ± 0.0485 (Laplace) from a mixed 3-point/4-point Wolfram Hessian. R02 is unchanged. R03 scan: 4-point central differences at the R02 best fits, with base steps (Ωm, h, w, ω_b) = (0.004, 0.004, 0.02, 6e-5) × factor. All Hessians are positive-definite.

| step factor | CTC-3P s.d.(w) | CTC-3B s.d.(w) |
|---|---|---|
| 2 | 0.02426 | 0.02440 |
| 1 | 0.03562 | 0.03576 |
| 0.5 | 0.04257 | 0.04266 |
| 0.25 | 0.04508 | 0.04515 |
| 0.1 | 0.04586 | 0.04593 |
| 0.05 | 0.04598 | 0.04604 |
| 0.025 | 0.04601 | 0.04607 |

| MCMC (emcee, seed 20261112, 32 walkers × 5000, 1000 discarded) | median -1.0461, std 0.04569, [16,84] [-1.0928, -1.0019]; τ ≈ 47/47/47/37 | median -1.0524, std 0.04662, [16,84] [-1.0994, -1.0070]; τ ≈ 46/45/44/44 |

Reading: the Laplace s.d. converges to about 0.0460 as the step shrinks. The R02 base step (factor 1) gives 0.036, and R02's mixed formula gave 0.0485. The posterior std is 0.0457 (PRIMARY) and 0.0466 (REPLACEMENT); Cosmology's chain gave 0.0467 and 0.0458. **R02's ±0.0485 is about 4–6% wider than the posterior, i.e. slightly conservative.** The posterior median sits about 0.003–0.004 more negative than the best fit.
**Proposal:** if CTC-3P/3B are re-frozen, quote the converged Laplace value (0.046) or the MCMC std, and record the step. Until then R02 stands as written. ΛCDM and oΛCDM are step-insensitive (Cosmology review §1).