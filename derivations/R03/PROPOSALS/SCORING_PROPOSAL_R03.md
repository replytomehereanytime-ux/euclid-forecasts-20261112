> R03 correction note (about 05:16 ET): the interpolation-error figures below use frozen parameters and are model-geometry statements, so they hold for any parameter set. Any example C_pred built from the truncated wCDM fit is SUPERSEDED. Rebuild it from calc/fullrs_r03_output.json (mcmc.wCDM_*.predcov) if the author adopts this proposal. Proposal, pending the author's decision.

---
**Everything below this line is the ORIGINAL (about 05:10 ET) text. Rows that include the CMB are SUPERSEDED (truncated r_s); BAO-only rows still stand.**

# SCORING_PROPOSAL_R03 — PROPOSAL, PENDING THE AUTHOR'S DECISION (proposal recorded at the time)

Dated 2026-11-12, about 05:10 ET (10:10 UTC). This is a separately dated proposal branch. It does **not** edit R02, where the frozen rule and its "interpolate linearly in z" step stay exactly as written. Nothing here is in force until the author chooses. It responds to Cosmology's independent review `euclid_20261112/cosmology_review_R02/VERIFY_R02_COSMOLOGY.md` (sha256 0b26d87e24f3e96735403196f7b06811e37702943030e41c7a208cabbed831fe, verified) §3.

## P1. The problem (reproduced)
Linear interpolation between the R02 nodes z = 0.9, 1.2, 1.5, 1.8 is biased. Errors were measured over 181 test redshifts in [0.9, 1.8] (Δz = 0.005) against the exact frozen model:

| curve | linear, 4 nodes (R02 as written) | cubic spline, 4 nodes | **cubic spline, frozen fine grid Δz = 0.01 on [0.85, 1.85]** |
|---|---|---|---|
| CTC-2P | DM/rd 0.1066, DH/rd 0.0842 | 0.0017, 0.0007 | 1.4e-10, 3.7e-10 |
| CTC-2B | DM/rd 0.1066, DH/rd 0.0843 | 0.0017, 0.0007 | 1.4e-10, 3.7e-10 |
| CTC-3P | DM/rd 0.1072, DH/rd 0.0833 | 0.0016, 0.0005 | 1.3e-10, 5.1e-10 |
| CTC-3B | DM/rd 0.1073, DH/rd 0.0833 | 0.0016, 0.0005 | 1.3e-10, 5.3e-10 |

This confirms the review's 0.107 (DM/rd) and 0.084 (DH/rd). A cubic spline on the 4 nodes still leaves up to 0.0017. The fine-grid cubic leaves at most about 5e-10, far below any predictive spread (≥0.005).

## P2. Proposed replacement text for the CTC rows (Option A preferred; Option B equivalent)
**Option A: exact evaluation.** For every published z_eff in [0.9, 1.8], compute m(z_eff) = model(θ̂, z_eff) with the frozen model code (R02 `wolfram/common_R02.wl`, or R03 `calc/cplmodel_r03.py`, which reproduces it to 2e-15) at the frozen parameter point θ̂. Use the R02 best fit for the Laplace rows (CTC-1..4) and the chain median prediction for the CPL rows. Compute C_pred(z_i, z_j) = J(z_i) C_θ J(z_j)ᵀ, where J is the model Jacobian at θ̂ and C_θ is the frozen parameter covariance. For the CPL rows, C_pred is the sample covariance of the frozen chain's predictions evaluated at the published z values. There is **no interpolation** of m, s or R.
**Option B: frozen fine grid.** Freeze, before data, a table of m and C_pred on z = 0.85, 0.86, …, 1.85. Use cubic-spline interpolation of m and of every C_pred element. The residual error is ≤ 5e-10 (P1).
Either option makes the inter-point predicted covariance explicit. Example for CTC-3B (wCDM, replacement branch; C_θ from the MCMC in P3) at a hypothetical published set z = 0.95, 1.05, 1.35, 1.65 (these are z values only, not Euclid data):

| z | m DM/rd | m DH/rd | s DM/rd | s DH/rd |
|---|---|---|---|---|
| 0.95 | 21.9043 | 17.1324 | 0.0637 | 0.0782 |
| 1.05 | 23.5673 | 16.1416 | 0.0631 | 0.0720 |
| 1.35 | 28.0128 | 13.5958 | 0.0638 | 0.0522 |
| 1.65 | 31.7787 | 11.5894 | 0.0660 | 0.0360 |

Its correlation matrix is in `proposals_calc_r03_output.json`. It has rank ≈ 3 (the eigenvalues beyond the third are ≤ 3e-14), so C_E + C_pred must be used, never C_pred alone.

## P3. When Euclid publishes only per-point errors (no covariance) — fallback
Two choices. the author picks one before data:
- **F1 (recommended, conservative bound; needs no assumed correlation).** Compute per-point standardized residuals t_i = (d_i − m_i)/√(e_i² + C_pred,ii). PASS iff max_i |t_i| ≤ k_N, where k_N is the standard-normal quantile at 1 − 0.025/N. FAIL otherwise. Under the model this accepts with probability ≥ 0.95 whatever the true correlations are (union bound). Values: N=2: 2.2414, N=4: 2.4977, N=6: 2.6383, N=8: 2.7344, N=12: 2.8653.
- **F2 (assumed correlation).** Build C_E = diag(e²), assuming zero correlation between redshift bins and a DM–DH correlation ρ = −0.4 within each bin (the typical DESI DR2 value, e.g. −0.40 to −0.50 in Table 4). Then apply the q95 rule. This is **not** conservative. If the true correlation differs, the coverage is not 0.95. It is listed only so the author can reject it explicitly.
- In both cases record that the covariance was absent. If Euclid publishes several overlapping vectors (per-tracer and combined), score the combined vector only. If there is no combined vector, the row is NOT_RUN.

## P4. Other review items the proposal covers
- C_pred at off-node z was undefined. It is now defined by P2.
- Which rule governs (R01 tail rule or R02 q95) and which branch (PRIMARY or REPLACEMENT) is the author's choice and must be made before data. This proposal takes no position.
- Pin the target document version: "first Euclid spectroscopic BAO paper, arXiv v1; record sha256".
- "Fixed before data" currently rests on local hashes only. An external timestamp stays HELD (the author's approval needed).