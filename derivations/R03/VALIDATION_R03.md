# VALIDATION_R03 — job and output receipt, environment, cross-code checks, exposure record (proposal recorded at the time)

Dated 2026-11-12, about 05:20 ET (America/Toronto). All times below are UTC (ET = UTC − 5).
Nothing was posted, published, timestamped, uploaded, e-mailed, or paid for, and nobody was contacted.
No R01, R02, R04, R05 or frozen file was edited. /workspace/r05_cosmo_env was used read-only and was not modified. No installs.
Disk: 7.1 GB free on / (above the 2 GB floor).

## 1. Inputs (sha256 verified this session)
| Input | sha256 |
|---|---|
| /workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_mean.txt | 9ac154ab583ce759c0f7eef3c978c7c70a6ead2d18774caceadf1a350a640585 |
| /workspace/desi_r01/desi_gaussian_bao_ALL_GCcomb_cov.txt | 252a143274c8a07c78694c119617d36594f6d7965d00319ca611c6ffb886e509 |
| /workspace/desi_r01/fit_cpl.py (bug at L29) | d12a165a0b1dc107b9c2ef8fe64e2a39a34c741428fa0d79f4aa07c28e7cd313 |
| /workspace/desi_r01/chain_w0waCDM.npy | 846a5546f3b59f428ff7fb7cf2bcf591a158d50f854ee8cbbdfc9e6ba7322d91 |
| /workspace/desi_r01/fit_results.json | 3ed00d18632aad3a8ec23d3060c37d0164b4e331f748d27b4ceed46c026c6dd3 |
| R02/wolfram/common_R02.wl (bug at L23) | 1a2970c5cd6f58d1ee25e18a4f10b22746497b388554d97e7a45d15f57f7aadd |
| R02/SHA256SUMS (R02 unchanged) | 6669a31e6b4685531a3cf63c717d2f6bf898360c91c492597fb989cbcba890b0 |
| wolfram_R04/crosscheck_scipy_R04.py (bug L26) | 26687dcd89cc23dcd24b7e9848276b2b68b5fc57dd1406c243fd253cd43be5e4 |
| wolfram_R04/call_old.wl (bug L20) | d0280dae224aded7227cdf0ed264d9327240f49e614e22ed941a341467cc4b5b |
| xact_R05/fs8_camb_R05.py | b1f403aa8e97021cc471eb52c37465958bcd826640ce6612171ed3d52b3f4ccd |
| best_forecasts_handoff_20261112/HANDOFF.md (BF-2) | aa80bb856b6616259eb1b11eeb928c9c798325868f601475d4507d8b1340bde7 |
| best_forecasts_handoff_20261112_R02/HANDOFF_R02.md (bug report) | e92369e24982b78829aa729d64d0d3959d04437def3f463a2d619211fec58577 |
| cosmology_review_R02/VERIFY_R02_COSMOLOGY.md | 0b26d87e24f3e96735403196f7b06811e37702943030e41c7a208cabbed831fe |
| increment_8929251/INCREMENT_8929251.md | 246e2ef055c8b67fc1ddc71bfc7666370f18356ad489c2b3f143d81950965f45 |

The Best_Defensible MANIFEST (13/13) was verified earlier; see INCREMENT_8929251/INCREMENT_R03.md. HSU, STO, Rebound and R1 input packages are not included in this public folder.

## 2. Job and output receipt
| Job | Command / tool | Env | Start → end (UTC) | Outputs |
|---|---|---|---|---|
| Model check | `rs3env/bin/python calc/check_model_r03.py` | rs3env: Python 3.13.5, numpy 2.5.4, scipy 1.17.1 | → 09:54:45 | check_model_r03.log |
| CPL rerun (truncated, SUPERSEDED) | `calc/cpl_oldprimary_r03.py` | rs3env + emcee 3.1.6 | → 09:56:08 | cpl_oldprimary_r03_output.json, fresh_chain_*_R03.npy |
| W reconcile (BAO-only rows valid; CMB rows superseded) | `calc/w_reconcile_r03.py`; Wolfram `wolfram/callB0_wbaoonly.wl` | rs3env; Wolfram MCP 15.0.1 | → 09:57:44; → 10:03:16 | w_reconcile_r03_output.json; raw_outputs_R03.txt |
| Proposals calc (wCDM numbers superseded) | `PROPOSALS/proposals_calc_r03.py` | rs3env | → 10:02:51 | proposals_calc_r03_output.json |
| Increment (a)–(c) | `INCREMENT_8929251/*.py` | rs3env | 10:00:28 → 10:05:14 | *_inc_output.json |
| the author's geometry check | `independent_geometry_check.py` | rs3env (sympy 1.14.0) | 10:04:17.054 | byte-identical NUMERICAL_CHECK.json (source_runs/run_log.txt) |
| r_s bug check | `calc/rs_bug_check_r03.py` | rs3env | → 10:07:55 | rs_bug_check_r03_output.json |
| Corrected Wolfram fits ΛCDM/wCDM/oΛCDM ×2 branches | `wolfram/callfix_{LCDM,wCDM,oLCDM}.wl` (= common_R03_fullrs.wl + call) | Wolfram MCP kernel "15.0.1 for Linux x86 (64-bit) (July 2, 2026)" | ≈10:07 → 10:08 | transcribed to wolfram/fullrs_fits_R03.json |
| Corrected Python fits + emcee (wCDM, CPL) + shifts | `OMP_NUM_THREADS=4 rs3env/bin/python calc/fullrs_r03.py` (seed 20261112) | rs3env | ≈10:09:20 → 10:11:05 (104 s) | fullrs_r03_output.json, fullrs_cpl_chain_{PRIMARY,REPLACEMENT}_R03.npy |
| CLASS cross-check | `r05_cosmo_env/bin/python calc/class_crosscheck_r03.py` | r05_cosmo_env: classy v3.4.2, numpy 2.5.4 | 10:11:20 → 10:11:22 | class_crosscheck_r03_output.json |
| CPL rows | `python3 calc/build_cpl_fullrs_r03.py` | rs3env | → 10:13:32 | CPL_OLDPRIMARY_R03.csv, _BANDS_R03.csv, cpl_validation_fullrs_r03.json |
| wCDM step scan | `calc/wcdm_stepscan_fullrs_r03.py` | rs3env | → 10:13:56 | wcdm_stepscan_fullrs_r03_output.json |
| Recomputed rows | `calc/build_recomputed_r03.py` | python3 | → 10:14:31 | RECOMPUTED_ROWS_R03.csv |
| fσ8 recompute (R05 held rows) | `OMP_NUM_THREADS=4 rs3env/bin/python calc/fs8_fullrs_r03.py` | rs3env, CAMB 2.0.5 | 10:12:43 → 10:14:44 | fs8_fullrs_r03_output.json |

All output hashes are in R03/SHA256SUMS.

## 3. CLASS cross-check settings (exact)
Settings passed to classy 3.4.2 (`calc/class_crosscheck_r03.py`):
- `h`, `omega_b`, and `omega_cdm` = Ωm h² − ω_b
- `N_ur = 3.046`, and **no `N_ncdm`**, so there are no massive neutrinos and no `m_ncdm`
- `T_cmb = 2.7255`, `YHe = 0.245` (fixed)
- `output = ''` (background and thermodynamics only)
- for wCDM/CPL points: `Omega_Lambda = 0`, `w0_fld`, `wa_fld`, `use_ppf = 'yes'`
- **No precision parameters were set; CLASS defaults throughout.** Reionisation is left at its default.
- Quantities compared: `rs_d`, `z_d`, `rs_rec`, `z_rec`, `ra_rec`, `angular_distance(z)·(1+z)` and `1/Hubble(z)`.

Model mismatch to note: the R03/R02/R04 r_d fitting formula assumes ω_ν = 0.00064 (massive ν), while the CLASS run is massless. This explains most of the +0.09% r_d offset. **This receipt is not a matched-neutrino CLASS-vs-CAMB benchmark** and does not cover the comparison in the 8933784 ZIP. Per the 5:13 steering, no CLASS-vs-CAMB run was started. A matched rerun needs that ZIP's neutrino content, YHe and precision settings, and would run only in /workspace/r05_cosmo_env.

Results:

| Case | r_d formula / CLASS rs_d − 1 | r_s* full / CLASS rs_rec − 1 | r_s* truncated / CLASS − 1 | max \|ΔDM/DM\|, \|ΔDH/DH\| (z 0.9–1.8) |
|---|---|---|---|---|
| ΛCDM REPL corrected | +8.6e-4 | +3.8e-4 | −1.80e-2 | 2.5e-7, 5.9e-7 |
| wCDM REPL corrected | +8.7e-4 | +3.8e-4 | −1.80e-2 | 2.6e-7, 5.9e-7 |
| CPL PRIM best fit | +8.9e-4 | +3.8e-4 | −1.80e-2 | 2.7e-6, 1.7e-6 |
| ΛCDM PRIM R02-old best fit | +1.5e-3 | +3.7e-4 | −1.85e-2 | 2.3e-7, 5.4e-7 |
| CPL PRIM chain, 60 points | max 9.6e-4 | — | — | 4.9e-4, 2.4e-4 (PPF vs fluid at w crossing −1) |

Max relative difference, DM/rd and DH/rd (formula r_d vs CLASS rs_d) over the 60 CPL points: 9.2e-4.

## 4. Other cross-code checks
- **r_s(z*) integral:** GL96 in a vs scipy quad to ∞ agree to 1e-15; vs Wolfram NIntegrate (WorkingPrecision 30) to 2e-14.
- **Best fits:** Wolfram and Python full-r_s agree for ΛCDM and wCDM in both branches, to ≤1e-7 in parameters and ≤2e-11 relative in χ².
- **Coordinator's corrected ΛCDM:** Ωm 0.3039, h 0.6856, Ωm h² 0.1428, r_d 147.0. Reproduced as 0.30387, 0.68559, 0.14283 and 147.03 Mpc.
- **Coordinator's expected z = 1.3 shifts:** reproduced (HELD_R03.md). Old code DH −1.89% and F_AP +1.15% (B) / +1.20% (P).
- **fσ8 (CAMB, same settings as R05, REPLACEMENT branch, full r_s, 150 draws each):**
  - ΛCDM: σ8(0) 0.826 [0.820, 0.832], S8 0.832; fσ8 at z = 0.9/1.2/1.5/1.8 = 0.450/0.416/0.382/0.351 (R05: shifts −8.0/−7.6/−7.3/−7.0%).
  - CPL: σ8(0) 0.811 [0.795, 0.832], S8 0.877; fσ8 = 0.444/0.416/0.382/0.350.
  - Labelled PROVISIONAL. The absolute fσ8 depends on the A_s prior.

## 5. Exposure record
- **Calibration data:** DESI DR2 BAO (old and Eq. 26 Lyα), Planck 2018 compressed priors, and CAMB/CLASS defaults. All were fully exposed, by construction.
- **Target outcomes:** no Euclid BAO, clustering or WL target outcome exists yet, and none was inspected.
- **Euclid archive:** the post-06:00 ET archive check from R02 is still open; not done in R03.
- **Inputs not used for any number:** the author's register ZIP (a5aa81fc…) is present. R02's register claims were not rerun (all 24 rows `activated_foundation_forecast=False`). Foundation precision rules unchanged.


## 6. Missing-input status by unsupported family (updates R02 UNSUPPORTED_MODELS_R02)
| # | Family | Status after R03 | Exact blocker |
|---|---|---|---|
| 1 | wCDM | recomputed (CTC-3P/3B-R03) | none (PROVISIONAL) |
| 2 | CPL | recomputed (CTC-5P/5B-R03) | longer chain advisable |
| 3 | oΛCDM | recomputed (CTC-4P/4B-R03); Ωk sign flipped vs R02 | none (PROVISIONAL) |
| 4 | massive ν (Σmν free) | NOT RUN | compressed CMB priors invalid when Σmν varies; needs a full CMB likelihood or public DESI+CMB Σmν chains. CLASS now present (N_ncdm possible), but no CMB likelihood is on the box |
| 5 | Hu–Sawicki f(R) | NOT RUN | needs MGCAMB/hi_class (not installed; installs need the author's approval) and DR1-Complete fσ8 or P(k) data |
| 6 | Jordan–Brans–Dicke | NOT RUN | needs hi_class or the declared ODE, plus a CMB-treatment decision; hi_class absent |
| 7 | nDGP | NOT RUN | needs the author's Ω_rc prior and an fσ8 data choice |
| 8 | k-mouflage | NOT RUN | needs the author's K(χ), β, A(φ) specification |
| 9 | mixed C+WDM | NOT RUN | needs (m_WDM, f_WDM) and a small-scale data product; none on the box |
| 10 | decaying DM | NOT RUN | needs the author's daughter type, Γ prior and fraction; CLASS can do the background, but the run was not requested |

## 7. Word check
New R03 files contain:
- no significance figures
- no p-values
- no coincidence claims

The INTERNAL χ² values are only in the `chi2_INTERNAL` column of RECOMPUTED_ROWS_R03.csv.
"σ8" and "S8" are the names of physical parameters, not significance statements. Standard deviations are written "s.d.".
