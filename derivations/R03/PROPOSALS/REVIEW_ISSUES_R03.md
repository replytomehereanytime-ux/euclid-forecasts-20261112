# REVIEW_ISSUES_R03 — every issue in Cosmology's R02 review, and how R03 handled it (proposal recorded at the time)

Source: `/workspace/r03-out/euclid_20261112/cosmology_review_R02/VERIFY_R02_COSMOLOGY.md`, sha256 0b26d87e24f3e96735403196f7b06811e37702943030e41c7a208cabbed831fe (verified). R02 was NOT edited. All changes are R03 files or proposals pending the author's decision.
**Overriding later finding (05:07 bug report):** every BAO+CMB result that the review checked used the truncated r_s(z*), so the review's PASS on those fits is PASS *of the reproduction*, not of the physics. See HELD_R03.md.

| # | Review issue | Review verdict | R03 handling | Status |
|---|---|---|---|---|
| 1a | Fits reproduce R02 (ΛCDM, oΛCDM, wCDM, CPL) | PASS | R03 reproduces too (χ² 29.12778 / 26.21434). All are now HELD for the r_s bug; corrected in RECOMPUTED_ROWS_R03.csv | superseded by the bug fix |
| 1b | wCDM Laplace ±0.049 depends on the Hessian step (MCMC 0.0467) | issue | Step scan done (PROPOSALS/WCDM_HESSIAN_STEP_NOTE_R03.md). The truncated model converged at 0.046; full r_s converges at 0.040, with MCMC 0.0405 / 0.0413. Proposal: quote the MCMC s.d. | proposal, pending the author |
| 2a | Freeze blocks complete | PASS | the R03 rows use the same freeze-block columns | done |
| 2b | D-P8c needs a binary rule using only an H0 published after 2026-10-13 | issue | PROPOSALS/DP8C_PROPOSAL_R03.md | proposal, pending the author |
| 2c | Naming: "PROSPECTIVE model-conditional" vs "conditional theory curve" | issue | R03 uses the four labels; rows are "conditional theory curve". Mapping noted, R02 untouched | noted; the author decides the final name |
| 2d | Pin "arXiv v1" for the Eq. 26 Lyα replacement | issue | Recorded in the proposals and here: arXiv 2607.27410 v1; values identical in v3 per Cosmology | noted |
| 3a | q95 rule: linear interpolation in z biases off-node points | FAIL as written | Scoring proposal: exact z evaluation from frozen parameters, or a Δz = 0.01 grid with cubic interpolation. Residual error: linear on 4 nodes ≈ 0.107 (DM) / 0.084 (DH); cubic spline on 4 nodes 0.0017 / 0.0007; fine-grid cubic ≤5e-10 | proposal, pending the author |
| 3b | C_pred undefined off-node | FAIL | explicit inter-point predicted covariance from parameter samples (Jacobian or sample covariance at the measured z) | proposal |
| 3c | No rule for diagonal-only errors | FAIL | fallback: per-point union bound k_N = Φ⁻¹(1 − 0.025/N) | proposal |
| 3d | Multiple data vectors / releases | FAIL | SCORING_PROPOSAL_R03 L40: if several overlapping vectors (per-tracer and combined) are published, score the combined vector only; with no combined vector the row is NOT_RUN | proposal |
| 3e | Governance R01 vs R02, P vs B | issue | SCORING_PROPOSAL_R03 L44: which rule (R01 tail rule or R02 q95) and which branch (P or B) governs is the author's choice, to be made before the data arrive. The proposal takes no position. CTC-5P now exists (CTC-5P-R03), so both branches are available | pending the author |
| 3f | External timestamp held | issue | the hold stays; nothing timestamped | held |
| 4 | Lyα ρ = +0.225 verified, so R04's "UNVERIFIED" flag was a gap | info | R03 uses +0.225 (verified) | done |
| 5 | BF-2 reconciliation | PASS | W_RECONCILE_R03: the cause is the CMB prior. The corrected BAO+CMB w is −1.027 (was −1.049); BF-2 reproduced at −0.9674 | done |
| 6 | CPL chains short (about 40τ); compare with Cosmology's primary chain | issue | Fresh full-r_s chains: 40×10,000, τ ≈ 190 (about 40τ again). Cosmology's chains used the truncated code, so direct comparison is no longer like-for-like. The truncated-mode R03 fresh chains agreed with the original to ≤0.008 | partly open: a longer chain (≥100τ) is advisable before freezing |
| 7 | Blockers list, incl. the CTC-5P decision | issue | CTC-5P-R03 is built (PROVISIONAL, private). the author must still decide whether it replaces CTC-5P, and the r_s-bug re-freeze | open — the author |
