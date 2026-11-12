# R02_NOTES — private branch status (proposal recorded at the time)

Written 2026-11-12, about 04:50–05:00 ET (09:50–10:00 UTC) by Forecast Bot (Grok Bot executor), from the author's handoff 8925124 (received 09:37:42 UTC) as relayed by Coordinator. **Nothing was posted, published, uploaded or timestamped, Zenodo included. Nobody was contacted. Nothing was installed or paid for, and no access was changed.** No R01 or other frozen file was modified. R01 hashes were re-verified (see VALIDATION_R02.md).

## 1. HOLDS
- **POSTING PACKAGE: ON HOLD.**
- `../POSTING_ABSTRACT_R01.md` (sha256 de64b48d…4337) is **ON HOLD**. Line 9 contains two significance-type phrases (quoted only in INTERNAL_CONTEXT_R02.md § "R01 hold items"), so it must not be used as public text. A significance-free replacement is NOT drafted, because posting is on hold. A personal name in that file stays on hold.
- `../ZENODO_METADATA_DRAFT_R01.json` (sha256 3626a257…6053) is **ON HOLD**. It contains no significance-type wording, but its description says the forecasts were recorded "before the Euclid DR1-Foundation archive opening (12 November 2026, 11:00 UTC)". That cites the announced time, not a verified one (see §3). No external timestamp was made.

## 2. What these files are
| file | content |
|---|---|
| FORECAST_TABLE_R02.md / .csv | 43 rows, each with a full freeze block (product…abstention), one label, readiness, verification, outcome |
| INTERNAL_CONTEXT_R02.md | the **only** place holding significance-type, tail-probability or exceedance-type rules (frozen R01 wording, repeated for traceability; nothing new generated) |
| UNSUPPORTED_MODELS_R02.md / .csv | the 10 alternative models in the author's readiness order, with exact missing equations and data |
| VALIDATION_R02.md, _build/selfcheck_r02.py | automated self-check output plus the manual read-through |
| wolfram/ | common_R02.wl, call*.wl, raw_outputs_R02.txt (verbatim kernel output), predcov_R02.json (full predictive correlations), predcov_rank_R02.json |
| SHA256SUMS | hashes of everything above, plus the source and R04/R05 files used |

Counts by label: prospective 23 (READY 15, NOT READY 8); conditional theory curve 11 (READY 9, NOT READY 1, n/a 1 = Rebound AP); retrospective fit 7; synthetic test 2 (both PASS). All forecast outcomes are NOT_RUN.

Scoring change from R01: the R01 joint rule (a tail-probability threshold; quoted in INTERNAL_CONTEXT_R02.md) is replaced in R02 by a fixed acceptance region: PASS iff (d−m)ᵀ(C_E+C_pred)⁻¹(d−m) ≤ q95(N), where q95 is the chi-square 0.95 quantile (Wolfram). This is a **new dated rule, not a restatement**. the author must choose whether the R01 or R02 rule governs. R01 itself remains frozen.

## 3. Euclid release status (what was actually inspected)
- 03:38–03:50 ET (08:38–08:50 UTC): the ESA Data Space notice said the archive was unavailable "until November 12 at 12:00 CET" (R01 record). ESA and Caltech pages used the future tense. The EC press page returned HTTP 504 and was not opened.
- **The post-06:00 ET (11:00 UTC) check of the archive and release notes has NOT been done yet** at the time of writing. The announced time is not evidence that the products exist. Until that check is recorded, every Euclid row keeps "product not acquired". Rows that depend on Foundation (E-CD, E-PHZ) stay NOT READY in any case. No Euclid data were opened for scoring.
- Foundation covers about 1,900 deg² and contains MER/PHZ/SPE catalogues and VMPZ masks (R03 L47). It has no SHE/WL/GC products and no randoms (Complete, mid-2027). No row applies full-mission precision. A footprint/depth map is not selected-galaxy completeness.

## 4. Effective independence and the handoff's register
- See the FORECAST_TABLE_R02.md "Effective independence" section. In short:
  - The 9 READY theory curves carry 72 numbers but only about 2–3 constrained directions each.
  - PRIMARY and REPLACEMENT are near-duplicates.
  - F_AP is never scored separately.
  - After the common-calibration nuisance is projected out, BAO-only ΛCDM has **one** identifiable direction (Ωm). This follows analytically: ∂d/∂ln A = d is exactly the common-calibration template.
- The handoff's distance package (4 branches × 5 z × 3 = 60 entries, or 132 across 11 z) and the **24-target register were not recovered**. Their bytes (register zip a5aa81fc…, eleven-arm, alternative-background arms, R02 Gaussian dipole, Hubble-volume audit, Rebound Bianchi, Joint-Band addendum, canonical v2.1, nested v2) are MISSING per HANDOFF_8925124_INVENTORY.md. **No R02 row is a register row, and none of the 24 were run.** The HSU targets, the conditional Hubble-volume E⁵ reconstruction, the Elastic Rebound/STO targets and the R02-G Gaussian dipole are therefore absent. The only exception is the Rebound AP conditional curve (CTC-R) carried from R01.
- HSU: no HSU likelihood is claimed. Count dipole: counts are not HSU convergence. The (5s−2)κ magnification response is required and is not modelled, which is part of why E-CD rows are NOT READY. Gaussian dipole tests are not Poisson validation (SYN-1 is a kinematic-formula grid check only).
- DESI normalization-comparison: the handoff says Grok's revised scripts were not supplied. Box copies of calc_*_R02/R03 scripts and outputs exist in ../../euclid_20261112/, but their significance claims are not transplanted anywhere public.

## 5. Engine status (posted / acknowledged / running / returned / independently checked)
| engine | status | evidence |
|---|---|---|
| Wolfram MCP kernel | **TESTED**: version 15.0.1 for Linux x86 (64-bit) (July 2, 2026), LicenseType Professional, task tests passed (Integrate check True; 48-pt Gauss–Legendre error 1.2×10⁻¹⁴) | raw_outputs_R02.txt |
| xAct | **TESTED in cloud kernel only, by R05** (xTensor 1.3.0, xPert 1.0.6, xCoba 0.8.6, GPL; native xperm FAILS, pure-WL canonicaliser PASSES a δR test). Not available persistently. xPand FAIL. xTras/xAlpha/xIST NOT_RUN | xact_R05/wolfram_raw_01_xact_load.txt |
| CAG / Agent One | REPORTED (HTTP 200 as Wolfram|Alpha app IDs in R04; no version, licence or task test) | R04, R05 §0 |
| Mathematica (local / 15-day trial) | REPORTED; not used | R05 §0 |
| CAMB 2.0.5 (pre-existing /workspace/rs3env) | used by R05 only | R05 §2 |

Job ledger:
- R01: returned 03:51 ET, acknowledged and hash-checked (inventory).
- R02 (this): returned with this report. Nobody has checked it independently.
- R05: returned 04:45 ET. Hashes re-verified here (all 10 OK). Its fσ8 tables are NOT READY, so no R02 row was created from them (not duplicated).
- Nothing was posted.
- Note from R05 §5: before the 04:37 limit, a venv /workspace/r05_cosmo_env (330 MB) was created with pip packages. It was not used and not deleted; deleting it needs the author's approval.

## 6. Decisions that need the author
1. **Which scoring rule governs the DESI/Euclid joint rows:** R01 (frozen) or the R02 q95 region?
2. **ρ = +0.225 for the replacement Lyα point:** R03 L24 says VERIFIED, R04 says UNVERIFIED. R02 follows R03 and flags the conflict.
3. **Supply the register bytes** (zip a5aa81fc… and the other 8 artifacts) if the 24 targets are to be frozen or run.
4. **CPL primary-branch bands** (CTC-5P): approve a box-only rerun of the R04 importance weights for the old Lyα branch.
5. **Posting hold:** confirm it stays in place. Decide whether a significance-free abstract should be drafted later, and settle prior-work wording and personal names.
6. **External timestamp (Zenodo or other):** held. the author decides whether and when.
7. **Alternative models:** supply priors/specifications for nDGP (Ω_rc), decaying DM (daughter type, Γ), k-mouflage (K0, m, β) and mixed DM (m_WDM, f_WDM). For massive neutrinos, f(R) and JBD, decide whether a full CMB likelihood or a Boltzmann-code install is allowed (installs need his yes).
8. **Post-06:00 ET archive check:** it needs a follow-up run after 11:00 UTC (not done in this pass).
9. **R05 venv** /workspace/r05_cosmo_env: keep or delete.
