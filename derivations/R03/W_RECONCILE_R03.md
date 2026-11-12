# W_RECONCILE_R03, R03 correction block (added about 05:16 ET, 2026-11-12) (proposal recorded at the time)

**Why:** the sound-horizon truncation bug (HELD_R03.md). Rows R4, R5 and R5′ below used r_s(z*) cut at z = 1e5. Corrected with r_s integrated to infinity:

| # | setup | Lyα | estimator | w (corrected) | old (truncated) |
|---|---|---|---|---|---|
| R4c | BAO + compressed CMB | PRIM | best fit (Wolfram, Python agree to 2e-8) | **−1.02805 ± 0.0422** (Laplace, Wolfram step) | −1.04332 |
| R5c | BAO + compressed CMB | REPL | best fit | **−1.02695 ± 0.0423** | −1.04874 |
| R4c′ | same | PRIM | emcee median, s.d. (32×5000) | −1.0312, 0.0405 | −1.0461, 0.0457 |
| R5c′ | same | REPL | emcee median, s.d. | **−1.0291, 0.0413** | −1.0524, 0.0466 |
| R1 (BF-2 setup) | BAO only | REPL | grid median | **−0.9674**: unchanged (no r_s(z*) in BAO-only fits) | — |

**Does the BF-2 reconciliation change?**
- **The verdict does not change.** The CMB prior is still the only cause.
- The size of the gap does change. On the REPLACEMENT branch it shrinks from −0.083 (−0.966 → −1.049) to **−0.061** (−0.966 → −1.027) in best fits.
- For PRIM it shrinks from −0.131 to −0.116.
- Reproducing BF-2 under its own setup still gives −0.9674 (BF-2: −0.9668).
- The bug also contributed to how far the BAO+CMB w sat from −1. The corrected value is −1.027 ± 0.042.
- In descriptive terms, the BAO-only and BAO+CMB w now overlap more within their stated widths. No significance is claimed.

Sources:
- wolfram/fullrs_fits_R03.json (Wolfram MCP kernel 15.0.1; common_R03_fullrs.wl)
- calc/fullrs_r03_output.json (rs3env Python 3.13.5, scipy 1.17.1, emcee 3.1.6, seed 20261112)
- calc/wcdm_stepscan_fullrs_r03_output.json

Note on the Laplace width:
- Python's converged step scan gives s.d.(w) = 0.0402 (PRIM) and 0.0404 (REPL), against 0.0405 and 0.0413 from MCMC.
- Wolfram fitm's Laplace (its fixed step) gives 0.0422.
- Use the MCMC s.d.


---
**Everything below this line is the ORIGINAL (about 05:10 ET) text. Rows that include the CMB are SUPERSEDED (truncated r_s); BAO-only rows still stand.**

# W_RECONCILE_R03 — constant-w: R02 (w = −1.0433 / −1.0487 ± 0.0485) vs BF-2 (w = −0.967) (proposal recorded at the time)

Dated 2026-11-12, about 05:10 ET (10:10 UTC). R02 and the BF-2 handoff are unchanged. Every fit statistic below is descriptive.

## Verdict
**The cause is the CMB prior.** BF-2 is a BAO-only fit (13 DESI points with the Eq. 26 Lyα replacement, flat wCDM, A = c/(H0 rd) free, no CMB, no SNe, no radiation). R02 CTC-3P/3B add the Planck 2018 compressed CMB prior (R, l_A, ω_b) and compute rd from the fitting formula, which breaks the A–w degeneracy. Rerunning under BF-2's stated setup reproduces BF-2. Rerunning under R02's setup reproduces R02. Neither fit uses SNe, there is no sign or definition difference (both use w = p/ρ, constant), and Ωk = 0 in both.

## Reproduction (R03 code `calc/w_reconcile_r03.py` → `calc/w_reconcile_r03_output.json`; Wolfram `wolfram/callB0_wbaoonly.wl` → `wolfram/raw_outputs_R03.txt`; Table-4 input `INCREMENT_8929251/wcdm_table4_inc.py`)
| # | data / priors | Lyα | free parameters | rd | estimator | w |
|---|---|---|---|---|---|---|
| BF-2 (handoff) | BAO only, no radiation | REPL (Eq. 26) | Ωm, w, A | absorbed in A | grid posterior median [68%] | −0.9668 [−1.0416, −0.8967] |
| R1 | same as BF-2, box DESI mean/cov file | REPL | Ωm, w, A | in A | grid posterior median [68%] (401², A marginalised analytically over U(20,40)) | **−0.9674 [−1.0413, −0.8961]** |
| R1′ | same, box file | REPL | Ωm, w, A | in A | best fit (Python and Wolfram agree) | −0.96562 (Ωm 0.30297, A 29.856; χ² 12.4683) |
| R1″ | same, **July Table-4 input** (the author's audit `desi_dr2_table4.csv`) | REPL | Ωm, w, A | in A | posterior mean ± SD | **−0.968075 ± 0.071614**: matches the author's audit value −0.9680754395 ± 0.0716143831 to 1e-10 |
| R2 | BAO only | **PRIM** | Ωm, w, A | in A | median / best fit | −0.9141 / −0.91190 (Wolfram −0.91190) |
| R3 | BAO only, radiation on | REPL | Ωm, h, w, ω_b | formula | best fit | −0.96464 (ω_b at its bound: in BAO-only fits h, ω_b are degenerate with A) |
| R4 | **BAO + compressed CMB** (R02 setup) | PRIM | Ωm, h, w, ω_b | formula | best fit | **−1.04332** = R02 CTC-3P |
| R5 | BAO + compressed CMB | REPL | Ωm, h, w, ω_b | formula | best fit | **−1.04874** = R02 CTC-3B |
| R5′ | BAO + compressed CMB | REPL | same | formula | MCMC median, std | −1.0524, 0.0466 (PROPOSALS/WCDM_HESSIAN_STEP_NOTE_R03.md) |

## Attribution of the difference (REPLACEMENT branch: −0.967 → −1.049)
| cause tested | effect on w | conclusion |
|---|---|---|
| data branch (PRIM vs REPL) | BAO-only: −0.912 → −0.966 (Δ −0.054); BAO+CMB: −1.043 → −1.049 (Δ −0.005) | not the cause of the BF-2/R02 gap (both quoted values are REPL-vs-REPL or PRIM-vs-PRIM) |
| **CMB prior included** | BAO-only −0.966 → BAO+CMB −1.049 (Δ **−0.083**); PRIM −0.912 → −1.043 (Δ −0.131) | **the cause** |
| SN prior | none in either fit | not a cause |
| free parameters (A free vs h, ω_b + rd formula) | BAO-only: −0.9656 vs −0.9646 | negligible: in BAO-only fits only A is constrained |
| rd treatment | only matters once the CMB fixes ω_b and ω_m; it is part of the "CMB prior" effect | part of the cause, inseparable from the CMB prior |
| radiation (off vs on) | −0.96562 vs −0.96486 | negligible (≤0.001) |
| estimator (median vs best fit) | ≤0.004 (BAO-only); about 0.004 (BAO+CMB) | negligible |
| sign or definition | identical E(z) form in both codes | none |
| uncertainty: R02 ±0.0485 | converged Laplace 0.0460, MCMC 0.0457 / 0.0466 | R02 ± is step-dependent and slightly wide (PROPOSALS/WCDM_HESSIAN_STEP_NOTE_R03.md) |
| input file (box mean/cov vs July Table 4 rounded errors/ρ) | posterior mean −0.96749 vs −0.96808 | ≤0.0006 |

**The two numbers answer different questions.** BF-2 is BAO + Lyα-AP only; R02 CTC-3 is BAO + Planck compressed CMB. They should never be listed as one "constant-w forecast". Caveat (Coordinator's BF handoff §0.5): the box BAO+CMB pipeline gives Ωm h² ≈ 0.158, against a Planck-like ≈ 0.143. That pipeline issue has not been audited, so the CMB-including w carries an extra, unquantified caveat.

## Link to the author's audit (increment 8929251 item (c))
- the author's audit (v2.1, `Constant_w_Numerical_Audit_Addendum_20261112_v1/SUMMARY.json` sha256 04b84bcc…7ff2; `RESULT_n160_A1601.json` sha256 5cf9af33…0808) is BAO + Lyα AP **without CMB**. Its w posteriors:
  - −0.96808 ± 0.07161 (no SN)
  - −0.94024 ± 0.03932 (published SN covariance)
  - −0.95822 ± 0.05850 (fixed evolution stress)
- R03 reproduces the no-SN value exactly from the same Table-4 input (row R1″). **So R03 agrees with the audit's constant-w posterior.**
- The audit's seven-held-block summed negative log predictive density values (3.807866826995 no SN; 1.973249602335 published SN covariance; 2.625319348006 evolution stress) were **not recomputed** in R03. They need the held-block fold definitions and the 1,300-row Pantheon+ inputs, and R03 did not rerun the audit. They are recorded as the author states them.
  - Free-A ΛCDM stays lower by about 1.0887 and 1.9188 nats in the two joint cases (SUMMARY.json negative_controls). SN improves constant-w's own sum but does not beat free-A ΛCDM.
  - ELG2 and QSO worsen.
- Consistent descriptive fact from R03: on the 13 BAO points, constant-w lowers the minimum fit statistic only from 12.688 (free-A ΛCDM) to 12.468, with one extra parameter.
- **None of this is a significance or model-odds statement.**
- R02's BAO+CMB constant-w (−1.04/−1.05) is a different calibration from the audit's. It cannot be compared with the audit numbers on equal terms.
