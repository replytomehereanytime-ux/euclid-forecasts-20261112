# VERIFY_R02_COSMOLOGY — independent review of Euclid Forecast Bot package R02 (PRIVATE)

Reviewer: Grok Bot (executor), for Coordinator / the author task EUCLID-OVERNIGHT-20261112-R01 (4:37 AM ET email). Written 2026-11-12, about 05:00–05:10 ET (10:00–10:10 UTC).
Nothing was posted, published, uploaded, timestamped externally, or sent. Nobody was contacted. No existing file was edited; everything here is new, in this folder only. Nothing was installed (emcee, scipy and CAMB were already in /workspace/rs3env). No significance or p-value claims are made below: only fit values, bands and differences.

## 0. Package integrity
- `R02/SHA256SUMS` sha256 = **6669a31e6b4685531a3cf63c717d2f6bf898360c91c492597fb989cbcba890b0** (matches the expected prefix `6669a31e`).
- `sha256sum -c SHA256SUMS`: **35/35 OK** (23 R02 files + R01, R04, R05, inventory and DESI_PREDICTIONS_source sources).
- Coordinator handoff `best_forecasts_handoff_20261112/SHA256SUMS`: all entries OK.

## Verdicts
| # | item | verdict | one-line reason |
|---|---|---|---|
| 1 | Constant-w, Ωk and CPL-replacement fits and bands | **PASS** (with caveats) | 8 fits re-derived with my own code: all best fits match R02 to ≤1e-4. Bands agree with my MCMC to within about 10% (R02 is slightly wider for wCDM). |
| 2 | 43 freeze blocks: completeness and labels | **PASS, with one fix needed** | 34/43 are complete. All 9 incomplete blocks are correctly marked NOT READY. Foundation/Complete labels are correct. D-P8c can resolve on an already-public SH0ES value (label risk). |
| 3 | Fixed acceptance-region (q95) rule | **FAIL as written** | q95 values and the PASS/FAIL/NOT_RUN logic are correct. But the "interpolate linearly in z" step shifts m by up to 0.11 in DM/rd and 0.08 in DH/rd (1–15× the predictive σ). Off-node C_pred, a missing Euclid covariance, and which rule (R01 vs R02) governs are all unspecified. |
| 4 | Lyα ρ (R03 vs R04) | **PASS for R03: ρ = +0.225 is correct** | Eq. 26 of arXiv:2607.27410 gives ρ(DM/rd, DH/rd) = 0.225 verbatim in both v1 and v3 (latest). R04's "UNVERIFIED" was an unchecked flag (it read only the abstract), not a conflicting value. |
| 5 | BF-2 −0.967 vs R02 −1.043 | **PASS (explained and reproduced)** | BF-2 is BAO-only with A free and no CMB; R02 adds Planck compressed CMB. The CMB prior moves w by about −0.08. The Lyα swap moves the BAO-only w by −0.054 but the BAO+CMB w by only −0.006. SNe are used in neither. |

---
## 1. Fits and predictive bands (item 1)

**Method.** I wrote my own code (`verify_fits_R02.py`, numpy/scipy). It uses the same public inputs as R02:
- DESI DR2 BAO mean and covariance (`/workspace/desi_r01`).
- The Results IV Eq. 26 Lyα replacement.
- The Planck 2018 compressed CMB prior (R, l_A, ω_b) from Chen, Huang & Wang 2019 (arXiv:1808.05724).
- The Aubourg+2015 r_d fitting formula and Hu–Sugiyama z*.

The implementation is independent: a 96-node numpy Gauss–Legendre integral, checked against scipy.quad (χ² agrees to <1e-5 in every fit). Optimisation is Nelder–Mead, run twice. The Laplace covariance comes from a 4-point Hessian. On top of this I ran an emcee posterior with the same flat priors (`verify_mcmc_R02.py`: 40 walkers; 4000 steps for wCDM/oΛCDM, 8000 for CPL; burn-in 1000). The Wolfram kernel (`user-wolfram`) cross-checked the q95 quantiles, the BAO-only DM/rd and DH/rd at z = 0.9, and the interpolation error.

**Best-fit parameters (reviewer vs R02).**
| fit | reviewer best fit | reviewer Laplace σ | reviewer posterior median [16, 84] | R02 |
|---|---|---|---|---|
| ΛCDM BAO-only, PRIM | Ωm 0.29746, A 29.5246; χ² 10.27104 | 0.00862, 0.2139 | — | 0.29746 ± 0.00862, 29.525 ± 0.214 ✔ |
| ΛCDM BAO-only, REPL | Ωm 0.30171, A 29.6329; χ² 12.68825 | 0.00770, 0.1959 | — | 0.30171 ± 0.00770, 29.633 ± 0.196 ✔ |
| ΛCDM BAO+CMB, PRIM | Ωm 0.32397, h 0.69868 | 0.00428, 0.00310 | — | 0.32397 ± 0.00429, 0.69868 ± 0.00311 ✔ |
| **wCDM BAO+CMB, PRIM** | **w −1.04332**, Ωm 0.31674, h 0.70835 | w 0.0453 | **w −1.048 [−1.096, −1.003]** (std 0.0467) | **w −1.043 ± 0.049** ✔ (σ about 4–7% wider than the posterior) |
| wCDM BAO+CMB, REPL | w −1.04874, Ωm 0.31621 | 0.0453 | w −1.053 [−1.100, −1.008] (std 0.0458) | w −1.049 ± 0.049 ✔ |
| **oΛCDM BAO+CMB, PRIM** | **Ωk −0.00342**, Ωm 0.32105 | Ωk 0.00126 | Ωk −0.00336 [−0.00462, −0.00211] | **Ωk −0.0034 ± 0.0013** ✔ |
| oΛCDM BAO+CMB, REPL | Ωk −0.00360 | 0.00125 | Ωk −0.00357 [−0.00480, −0.00233] | −0.0036 ± 0.0012 ✔ |
| **CPL BAO+CMB, REPL** | **w0 −0.76736, wa −0.82450**; χ² 26.93972 | 0.277, 0.830 | **w0 −0.695 [−0.979, −0.377], wa −1.057 [−2.039, −0.212]** | best fit −0.767, −0.824 ✔; R04 chain −0.700 ± 0.291, −1.069 ± 0.883 ✔ |
| CPL BAO+CMB, PRIM | w0 −0.77351, wa −0.79085 | 0.284, 0.851 (Hessian positive-definite with my steps) | w0 −0.711 [−1.006, −0.385], wa −0.988 [−1.983, −0.127] | R04 best fit −0.774, −0.791 ✔ (R04: Hessian not PD) |

The χ² minima also match R02's internal values exactly: 26.21434 / 29.12778, 25.28350 / 27.94402, 18.97219 / 20.90584. These are fit statistics only and are reported for reproducibility.

**Predictive bands at z = 0.9, 1.2, 1.5, 1.8** (`compare_bands_R02.py` → `compare_bands_R02_output.json`).
| row | R02 mean vs reviewer Laplace mean (max abs diff) | R02 σ / reviewer Laplace σ | (R02 mean − MCMC median) / R02 σ | R02 σ / MCMC 68% half-width |
|---|---|---|---|---|
| CTC-1P / 1B | 0.0000 (all 8 values and σ to 4 dp) | 1.000 | — | — |
| CTC-2P / 2B | 0.0000 | 0.993–1.005 | — | — |
| CTC-3P | 0.0000 | 0.995–1.085 | −0.07 to +0.05 | 1.00–1.10 |
| CTC-3B | 0.0000 | 0.995–1.084 | −0.11 to −0.01 | 0.98–1.09 |
| CTC-4P | 0.0000 | 0.999–1.003 | +0.06 to +0.07 | 1.00–1.04 |
| CTC-4B | 0.0000 | 1.000–1.002 | 0.00 to +0.04 | 0.99–1.00 |
| CTC-5B (chain bands) | 0.026 (best fit vs median; expected) | 0.98–1.09 | −0.02 to +0.06 | 0.94–1.09 |
| CTC-5P | R02: MISSING | — | — | — |

Caveats for item 1:
- **wCDM Laplace σ depends on the step size.** With R02's physical steps (0.004, 0.004, 0.02, 6e-5), a 4-point Hessian gives σ_w = 0.036. Steps of 1/4 to 1/10 converge to 0.045–0.046. R02's mixed 3-point/4-point Hessian gives 0.0485. The χ² valley is curved on R02's step scale (`verify_hess_steps_R02_output.json`). The posterior (MCMC std 0.0467) sits between these values, so R02's bands are slightly conservative (≤10% wide). oΛCDM and ΛCDM do not depend on the step size.
- **CPL chains are short.** They run 8000 steps with τ ≈ 175–200, about 40τ instead of the recommended 50τ. Treat the CPL MCMC numbers as PROVISIONAL. They still agree with R04's reweighted chains to ≤0.02 in the parameters and ≤0.05 R02-σ in the bands.
- **Possible input for CTC-5P (the author decision #4 in R02_NOTES).** My PRIMARY-Lyα CPL chain gives median [68% half-width] DM/rd, DH/rd of:
  - z = 0.9: 20.988 [0.077], 17.603 [0.100]
  - z = 1.2: 25.840 [0.075], 14.828 [0.082]
  - z = 1.5: 29.942 [0.072], 12.596 [0.080]
  - z = 1.8: 33.445 [0.073], 10.812 [0.066]

  The full 8×8 predictive correlation is in `verify_mcmc_R02_CPL_REPL+CPL_PRIM.json`. **Not inserted into R02**: whether it may be frozen is the author's decision.
- The physics caveats are shared with R02 and R04, not checked further: the r_d fitting formula; compressed CMB priors used outside flat ΛCDM (oΛCDM, wCDM, CPL); no SNe.

## 2. The 43 freeze blocks (item 2)
Full per-block table: `audit_freeze_blocks_R02.csv` (script `audit_freeze_blocks_R02.py`). Six elements were checked: observable+units, cuts, model+params, uncertainty/cov, selection, and scoring/failure.
- **Counts verified:** 43 rows, unique IDs. Labels: prospective 23 (READY 15, NOT READY 8), conditional theory curve 11, retrospective fit 7, synthetic test 2. This matches R02_NOTES.
- **Complete: 34/43.** Every READY row is complete. For the 15 READY DESI rows, cuts, selection and covariance are delegated to DESI's published inference; that is acceptable because the observables are DESI-published parameters. For 5 of them (D-P1a/b, D-P2b, D-P8b/d), the condition is kept in INTERNAL_CONTEXT, where it is two-valued and complete.
- **Incomplete: 9/43, all correctly NOT READY:**
  - D-P7: hemisphere axis TBD.
  - E-CD-P1 to P5: cuts, mask, estimator, covariance and kinematic null TBD; Foundation binding TBD.
  - E-L-P6: floor, tolerance, mask and covariance TBD.
  - E-PHZ-1: truth set and cohort TBD.
  - CTC-5P: no predictive band.
- **Release labels: correct.** All CTC rows say "DR1 Complete (mid-2027+), NOT Foundation". E-L-P6 says Complete. E-CD and E-PHZ say Foundation with binding TBD, which is consistent with Foundation containing MER/PHZ/SPE catalogues and VMPZ masks but no SHE/GC or randoms. No row claims Foundation can test a BAO or WL quantity.
- **Prospective/retrospective labels: correct, except one row:**
  - **D-P8c (fix needed).** The rule is "PASS iff the latest SH0ES central value on 2027-12-31 is in [72.5, 73.5]". If SH0ES publishes nothing new after 2026-10-13, this scores an already-public value, and the known SH0ES 2022 value of 73.04 lies inside the window. The "abstention rule" field holds a note, not a rule. Fix: add "NOT_RUN if no SH0ES H0 first public after 2026-10-13 exists by 2027-12-31".
  - D-P2a, P3a, P4a and P8a carry "68% label pending the author". This is stated honestly in the rows; it is not an error.
  - Naming difference with the Coordinator handoff: the handoff labels its BF-1/BF-2 geometry predictions "PROSPECTIVE, model-conditional", while R02 labels the equivalent rows "conditional theory curve". Both are defensible. the author should pick one term before freezing so the two packages do not disagree.
- Minor: the CTC rows say "first Euclid spectroscopic BAO measurement" but do not fix the arXiv version to score (the D rows say "v1"). Suggest "arXiv v1".

## 3. Fixed acceptance-region rule (item 3)
The rule: PASS iff (d−m)ᵀ(C_E+C_pred)⁻¹(d−m) ≤ q95(N); otherwise FAIL; NOT_RUN if there is no DM/rd or DH/rd point (or convertible α) in [0.9, 1.8].

**What is correct:**
- **q95 values.** 9.4877 (N=4), 12.5916 (6), 15.5073 (8) and 21.0261 (12) match both scipy and the Wolfram kernel (`verify_interp_q95_R02_output.json`).
- **The outcome logic.** PASS, FAIL and NOT_RUN cover every case once m, C_pred and C_E exist. The boundary (≤) is assigned.
- **Matrix stability.** C_pred is near rank-deficient (rank 2–3), but C_E+C_pred is positive-definite whenever C_E is.
- **The rule has no free threshold.**
- **Timing.** It is dated 2026-11-12 ~09:51 UTC, before any Euclid BAO product exists (DR1 Complete is mid-2027 at the earliest).

**What fails:**
1. **Linear z-interpolation of m is biased.** Exact model values compared with linear interpolation between the 0.3-spaced nodes (Wolfram confirms) give mid-node errors at z = 1.05 / 1.35 / 1.65 of:
   - DM/rd: −0.107 / −0.084 / −0.066
   - DH/rd: +0.084 / +0.067 / +0.051

   The same errors appear for ΛCDM, wCDM and oΛCDM. In comparison:
   - The BAO-only predictive σ is about 0.07, so the error is about 1–1.5σ.
   - For the CMB-calibrated curves, the DH/rd predictive σ is 0.006–0.08, so the error is up to about 15σ.

   Against a percent-level Euclid error (DH/rd ~0.15–0.3), it is a 0.3–0.5σ_E shift. This is a systematic bias that would be built into the frozen rule.
2. **C_pred at off-node z_eff is not defined.** The rule says to interpolate m, but not s or R.
3. **There is no rule if Euclid publishes only per-point errors** (no covariance), or several combined/per-tracer vectors.
4. **Governance is open.** R01 (tail-probability) vs R02 (q95), and PRIMARY vs REPLACEMENT branch, are left to the author. Until they are fixed before data, choosing after the data would be a tunable choice.
5. **"Fixed before data" rests only on local hashes.** There is no external timestamp, which is held pending the author.

**Minimal fix** (proposed text; I did not apply it to R02). Replace "Interpolate linearly in z" with: "m and C_pred at each published z_eff are computed exactly from the frozen parameter mean and covariance (Laplace or chain, as frozen) using the frozen model code and hash. Equivalently, use a frozen dense grid with Δz ≤ 0.01 and cubic interpolation, which keeps the error below 1e-4 of σ." Also add:
- "If C_E is not published, use diag(σ_E²) and record that fact."
- "Score the combined vector if published; else NOT_RUN."
- "This rule supersedes R01 for CTC rows from <date>", once the author chooses.

Freezing the parameter mean and covariance per curve is cheap: they are in my JSON outputs and in R02's Wolfram runs.

## 4. Lyα ρ (item 4)
Source: DESI DR2 Results IV, arXiv:2607.27410. Its versions are v1 (29 Jul 2026), v2 (31 Jul) and v3 (4 Aug, the latest). I fetched the HTML of v1 and v3 as metadata/text only. Saved copies:
- `sources/lya_v1.html`, sha256 121bd2e0…2e14
- `sources/lya_v3.html`, sha256 3865ec6a…9c59a

Both versions say, verbatim: "DESI Lyα full-shape { D_M(z_eff)/r_d = 39.32 ± 0.33, D_H(z_eff)/r_d = 8.600 ± 0.066, ρ(D_M/r_d, D_H/r_d) = 0.225 } (26), where ρ is the correlation coefficient between the two parameters."

- **R03 (ρ = +0.225, VERIFIED) is correct.**
- R04 (WOLFRAM_RESULTS_R04.md L64) used the same +0.225 but labelled it "UNVERIFIED, not in the abstract". That label was a gap in what R04 checked, not a different value. R04's sensitivity table (§4c) can now be read at its +0.225 row.
- The off-diagonal entry is ρ·σ_DM·σ_DH = 0.225 × 0.33 × 0.066 = 0.0049005, placed symmetrically. R02's `common_R02.wl` L8 and my code both implement this correctly.
- Caveat already noted by the handoff: Eq. 26 includes AP/full-shape information. The REPLACEMENT branch is therefore "BAO + Lyα AP compression", and its zero cross-covariance with the other DESI blocks is an assumption.

## 5. Why BF-2 is −0.967 and R02 is −1.043 (item 5)
Script: `verify_bf2_decomp_R02.py` → `verify_bf2_decomp_R02_output.json`. I reproduced BF-2 with its stated set-up: 13 DESI points with the Lyα pair replaced (ρ = +0.225); flat wCDM; radiation omitted; A = c/(H0 r_d) free; no CMB, no SNe; flat priors Ωm U(0.1, 0.5), A U(20, 40) [grid 28–31], w U(−1.5, −0.5); marginal posterior medians on a 241×401×301 grid.

| step | data | Lyα | estimator | w |
|---|---|---|---|---|
| BF-2 (handoff) | BAO only, A free | REPL | grid posterior median [68%] | −0.9668 [−1.0416, −0.8967] |
| reviewer reproduction | BAO only, A free | REPL | grid posterior median [68%] | **−0.9684 [−1.0418, −0.8988]**; Ωm 0.3020, A 29.849 (BF-2: 0.3024, 29.855) |
| reviewer | BAO only, A free | REPL | best fit | −0.9656 (Ωm 0.3030, A 29.856) |
| reviewer | BAO only, A free | **PRIM** | best fit / median | **−0.9119** / −0.9170 [−0.9948, −0.8457] |
| reviewer = R02 CTC-3P | **BAO + Planck compressed CMB**, r_d from formula | PRIM | best fit | **−1.0433** |
| reviewer = R02 CTC-3B | BAO + compressed CMB | REPL | best fit | −1.0487 |

**Explanation:**
- **(i) The CMB prior is the main driver.** It shifts w by about −0.08 (−0.966 → −1.049 on REPL; −0.912 → −1.043 on PRIM). It fixes r_d through ω_b and ω_m, which removes the free-A degeneracy, and it adds the distance to last scattering.
- **(ii) The Lyα point matters only without the CMB.** In BAO-only fits, replacing it moves w by −0.054. With the CMB the move is only −0.005.
- **(iii) Estimator.** Posterior median vs best fit differs by ≤0.005.
- **(iv) SN sets.** Neither fit uses supernovae, so the SN choice plays no part.
- **(v) Radiation.** It is omitted in BF-2 and included in R02. Its effect is negligible at these redshifts, and it is absorbed by A in the BAO-only case.

The handoff also notes Claude's July BAO-only constant-w of −0.968 ± 0.072, which agrees with BF-2 because it is the same BAO-only, free-A set-up. **The two numbers answer different questions** (BAO-only vs BAO+CMB). They should not be listed as the same "constant-w forecast". R02's CTC-3P/3B and the handoff's BF-2 should each carry their data combination in the row title.

---
## Blockers / needs the author
1. Choose the governing rule for the CTC rows (R01 tail rule vs R02 q95), and approve the interpolation and covariance fix in §3 before any Euclid BAO data appear.
2. Fix D-P8c (add a NOT_RUN for no post-2026-10-13 SH0ES result).
3. Decide whether the reviewer CPL-PRIMARY bands (§1) may populate CTC-5P, perhaps after a longer chain run of about 15 min on the box.
4. Pick one label term for the model-conditional geometry predictions so the handoff and R02 agree.
5. External timestamp: still held (the author's approval needed).
6. Not done here: the post-11:00 UTC Euclid archive check (out of scope for this review).

## Files written (all new, this folder)
verify_fits_R02.py (+_output.json); verify_hess_steps_R02.py (+_output.json); verify_mcmc_R02.py (+ two JSON outputs, mcmc_A.log, mcmc_B.log); verify_bf2_decomp_R02.py (+_output.json); verify_interp_q95_R02.py (+_output.json); verify_baoonly_pred_R02.py (+_output.json); compare_bands_R02.py (+_output.json); audit_freeze_blocks_R02.py (+ audit_freeze_blocks_R02.csv); sources/lya_v1.html, sources/lya_v3.html; INPUTS_SHA256.txt; OUTPUTS_SHA256.txt; this report.

## Inputs read (sha256 in INPUTS_SHA256.txt)
- R02: all files listed in R02/SHA256SUMS (verified 35/35).
- best_forecasts_handoff_20261112/HANDOFF.md.
- euclid_20261112/HANDOFF_8925124.md.
- euclid_20261112/wolfram_R04/WOLFRAM_RESULTS_R04.md.
- /workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_mean.txt and _cov.txt.
- arXiv:2607.27410 v1 and v3 HTML (saved in sources/).
