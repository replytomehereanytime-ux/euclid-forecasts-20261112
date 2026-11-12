# INCREMENT_8929251 — R03 branch for the author's increment msg 8929251 (proposal recorded at the time)

Dated 2026-11-12, about 05:12 ET (10:12 UTC). This is a separately dated branch. No frozen output was retuned. R01, R02 and the author's inputs were not edited. Nothing was posted or timestamped.

## Inputs (verified this session)
- `euclid_20261112/increment_8929251/INCREMENT_8929251.md`: sha256 246e2ef055c8b67fc1ddc71bfc7666370f18356ad489c2b3f143d81950965f45 (starts 246e2ef0 as stated).
- `euclid_20261112/source_inputs_8930243/INPUTS_RECEIPT.md`: sha256 cddf33b2e58db8b13603f2914aff6fd5f058e3d0a117bfb2d653ab9d06d525a7 (cddf33b2…25a7 as stated). R03 recomputed all 8 ZIP hashes and they equal the receipt values.
- `Best_Defensible_Forecast_Handoff_20261112.zip`: sha256 5b5f138feb22e57d8b7eff90963967349002347c9d78f4a9036d795e50f4b0a4. **PRESENT** (the earlier MISSING mark is dropped). All 13 members match its MANIFEST.json. Per-file hashes used are in `compare_source_csv_inc_output.json` (inputs_sha256).
- July Table-4 input: `best_forecasts_handoff_20261112/drive_candidates/x/…/constant_w_audit_addendum_v1/inputs/desi_dr2_table4.csv`, sha256 a9f3fc66443c4268cb16bb15280b4f1d60c6e7f842f8f2a2025a36ed87a7e013. Eq. 26 replaces the Lyα row.
- **The handoff artifacts R02 recorded as missing are now present** and hash-matched, including the R02 Gaussian dipole calibration and the Joint-Band addendum (copied under `derivations/source_inputs/`). Canonical v2.1 and nested v2 were already hash-matched on the box. Inventory rows that were not activated remain un-run; **R02's statement that those inventory rows were not run is unchanged, and R03 did not run them.** HSU, STO, Rebound and R1 materials from that inventory are not included in this public derivations folder.

## (a) Free-A flat ΛCDM, July replacement: reproduction
the author's equations: E² = Ωm(1+z)³ + 1 − Ωm, no radiation, A free; priors Ωm U(0.1, 0.5), A U(20, 40). Exact 2-D grid posterior (2001², resolution-checked against 4001²). **Two different quantities are computed:** the integrated posterior mean ± parameter-only SD (what the author's table reports), and the formulas evaluated once at the mean parameters.

Result with the July Table-4 input: Ωm = 0.30194023839057 ± 0.007644, A = 29.635459200211 ± 0.192406. the author: 0.30194023839055434 and 29.635459200210903. Maximum absolute difference over all 15 rows × (mean, SD): **1.4e-13**.

| z | obs | the author integrated mean ± SD | R03 integrated mean ± SD | diff (mean, SD) | R03 at mean params | at-mean − integrated | R03 with box DESI cov file |
|---|---|---|---|---|---|---|---|
| 0.9 | DM/rd | 21.10595 ± 0.06621 | 21.10595 ± 0.06621 | 8.2e-14, -7.1e-14 | 21.10574 | -0.00021 | 21.10789 ± 0.06888 |
| 0.9 | DH/rd | 17.81011 ± 0.06013 | 17.81011 ± 0.06013 | -9.2e-14, -6.8e-14 | 17.80922 | -0.00089 | 17.81030 ± 0.06177 |
| 0.9 | F_AP | 1.18506 ± 0.00460 | 1.18506 ± 0.00460 | 1.0e-14, -1.4e-14 | 1.18510 | +0.00004 | 1.18516 ± 0.00464 |
| 1.0 | DM/rd | 22.83564 ± 0.06794 | 22.83564 ± 0.06794 | 7.8e-14, -5.7e-14 | 22.83534 | -0.00031 | 22.83758 ± 0.07085 |
| 1.0 | DH/rd | 16.79606 ± 0.06244 | 16.79606 ± 0.06244 | -1.0e-13, -8.9e-14 | 16.79506 | -0.00100 | 16.79607 ± 0.06387 |
| 1.0 | F_AP | 1.35960 ± 0.00553 | 1.35960 ± 0.00553 | 1.2e-14, -1.6e-14 | 1.35965 | +0.00005 | 1.35971 ± 0.00558 |
| 1.2 | DM/rd | 26.00890 ± 0.07165 | 26.00890 ± 0.07165 | 6.4e-14, -3.3e-14 | 26.00837 | -0.00052 | 26.01081 ± 0.07499 |
| 1.2 | DH/rd | 14.98248 ± 0.06514 | 14.98248 ± 0.06514 | -1.2e-13, -1.2e-13 | 14.98132 | -0.00116 | 14.98223 ± 0.06630 |
| 1.2 | F_AP | 1.73598 ± 0.00756 | 1.73598 ± 0.00756 | 1.7e-14, -2.2e-14 | 1.73605 | +0.00007 | 1.73614 ± 0.00762 |
| 1.5 | DM/rd | 30.15359 ± 0.07901 | 30.15359 ± 0.07901 | 2.8e-14, -1.1e-14 | 30.15270 | -0.00089 | 30.15540 ± 0.08282 |
| 1.5 | DH/rd | 12.73562 ± 0.06487 | 12.73562 ± 0.06487 | -1.2e-13, -1.3e-13 | 12.73437 | -0.00125 | 12.73517 ± 0.06579 |
| 1.5 | F_AP | 2.36771 ± 0.01086 | 2.36771 ± 0.01086 | 2.5e-14, -3.2e-14 | 2.36782 | +0.00012 | 2.36793 ± 0.01095 |
| 1.8 | DM/rd | 33.69635 ± 0.08858 | 33.69635 ± 0.08858 | -7.1e-15, -1.0e-14 | 33.69508 | -0.00127 | 33.69801 ± 0.09266 |
| 1.8 | DH/rd | 10.95016 ± 0.06160 | 10.95016 ± 0.06160 | -1.3e-13, -1.4e-13 | 10.94891 | -0.00125 | 10.94963 ± 0.06238 |
| 1.8 | F_AP | 3.07732 ± 0.01441 | 3.07732 ± 0.01441 | 3.5e-14, -4.2e-14 | 3.07748 | +0.00016 | 3.07762 ± 0.01453 |

Reading:
- Evaluating at the mean parameters differs from the integrated mean by up to 0.0016 (DM/rd at z = 1.8). That is small next to the SD, but not zero, as the author notes.
- The box DESI mean/cov file (full-precision covariance) gives slightly different values (Ωm 0.30210, SDs about 4% larger) than the rounded Table-4 errors and ρ. **The input-file choice is a real, documented sensitivity.**
- These are parameter-only SDs, not Euclid measurement uncertainties. The full 15×15 shared latent covariance is in `freeA_lcdm_table4_inc_output.json` (latent_cov; eigenvalues show rank 2 = Ωm, A).
- R03 also ran the author's `independent_geometry_check.py` on a copy. It reproduces NUMERICAL_CHECK.json byte-identically (220 comparisons, max abs diff 2.22e-16; `source_runs/run_log.txt`).

## (b) Separate blocks: frozen old-DESI primary and current-input sensitivities
### B1. Old-DESI historical primary: FROZEN (the author's values, verbatim; not retuned)
| z | DM/rd median [joint bounds] | DH/rd median [joint bounds] | F_AP median [joint bounds] |
|---|---|---|---|
| 0.9 | 21.07957 [20.91482, 21.24430] | 17.82571 [17.66849, 17.98137] | 1.18253 [1.17020, 1.19519] |
| 1.0 | 22.81101 [22.64324, 22.97869] | 16.81545 [16.65021, 16.97919] | 1.35654 [1.34167, 1.37178] |
| 1.2 | 25.98864 [25.81370, 26.16351] | 15.00660 [14.83193, 15.18037] | 1.73181 [1.71145, 1.75260] |
| 1.5 | 30.14104 [29.94875, 30.33333] | 12.76235 [12.58706, 12.93782] | 2.36172 [2.33235, 2.39157] |
| 1.8 | 33.69187 [33.47434, 33.90937] | 10.97676 [10.80983, 11.14465] | 3.06939 [3.03034, 3.10895] |
Historical grid z = 0.9, 1.0, 1.2, 1.5, 1.8. **The prototype grid (0.9, 1.1, 1.3, 1.5, 1.8) is NOT substituted.**
- R03 check: posterior means reproduce exactly from Table 4 with the original Lyα row (Ωm 0.2978140059790, A 29.53095249744; the author 0.2978140059789888 / 29.530952497437177). Medians agree within 1.7e-04 (grid-median interpolation).
- Joint bounds: the author's construction is called "finite-grid simultaneous bounds" and the method is not stated in the increment text. One construction R03 tested (max over the 15 coordinates of |x − median|/SD, at 0.95) gives z = 0.9 DM/rd [20.91485, 21.24452] and DH/rd [17.66867, 17.98298]. These are close to the author's (within 0.002; this construction is symmetric, the author's bounds are not), but **not claimed to be the same method**. the author's bounds stand as frozen.
### B2. Current-input sensitivities at z = 1.5: NOT Euclid results; NOT a probability envelope
| variant | DM/rd | DH/rd | source |
|---|---|---|---|
| July replacement, no SN (baseline) | 30.15359 ± 0.07901 | 12.73562 ± 0.06487 | july_joint_geometry.csv BAO_only |
| retained SN calibration (published SN cov) | 30.15720 ± 0.07897 | 12.70397 ± 0.06217 | july_joint_geometry.csv joint_stress_0.0 (the author's values; matches the CSV) |
| fixed evolution stress | 30.15452 ± 0.07900 | 12.72765 ± 0.06430 | july_joint_geometry.csv joint_stress_0.1 |
R03 did **not** recompute the SN variants. They need the 1,300-row Pantheon+ data and covariance (in the v2.1 audit inputs, not rerun here, to avoid duplicating the author's completed audit). Their complete correlated outputs stay in the author's CSV under separate labels.

## (c) Constant-w vs the author's audit: see `../W_RECONCILE_R03.md` §"Link to the author's audit"
- R03 reproduces the audit's no-SN constant-w posterior w = −0.968075 ± 0.071614 to 1e-10 (`wcdm_table4_inc_output.json`).
- The NLPD sums (3.807866826995 / 1.973249602335 / 2.625319348006) are recorded as stated, **not recomputed**. the author's finding stands: SN improves constant-w's own sum, but constant-w does not beat free-A ΛCDM on common inputs, and the ELG2 and QSO blocks worsen.
- R02's BAO+CMB constant-w (−1.043 / −1.049) uses a different calibration (compressed CMB), which is why it differs.


## Job and output receipt
- Every script, command and hash is in `../VALIDATION_R03.md` and `../SHA256SUMS`. the author's scripts were run only on copies in `source_runs/` (log with UTC start/end times and output hashes in `source_runs/run_log.txt`).