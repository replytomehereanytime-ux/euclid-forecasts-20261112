# Derivations behind the REV2 forecasts

**Author:** C.A.S.D.R

**Repository:** [euclid-forecasts-20261112](https://github.com/replytomehereanytime-ux/euclid-forecasts-20261112)

**Tag:** `freeze-20261112-derivations`

This folder holds the fit scripts, Wolfram notebooks, chains, CSVs, summaries and run outputs used to produce the ranked forecasts in `PREDICTIONS_20261112_REV2.md` at the repository root. It is a supporting archive for REV2, not a new set of predictions.

Text files were lightly sanitized before publication: the author's first name was replaced with author-neutral wording, and a few path names were renamed to match (`cole_runs` → `source_runs`, `compare_cole_csv_*` → `compare_source_csv_*`). Scientific numbers were not changed by that wording pass. Binary chains, spectra and most CSVs are unmodified copies of the 12 November 2026 (America/Toronto) run products. Because some text files were edited, their SHA-256 values here differ from internal originals; `derivations/SHA256SUMS` is the checksum list for the files as published.

## How this maps to the published REV2 rows

The source map in `SOURCES_20261112_REV2.md` is the authority for which file supplied each published number. The short version:

| REV2 ranks | Item ids | Primary numeric sources in this folder |
|---|---|---|
| 1–2 | CTC-1P, CTC-1B | `R02/FORECAST_TABLE_R02.csv` (and `.md`); BAO-only Wolfram fits in `R02/wolfram/` |
| 3–8 | CTC-2P/2B/3P/3B/4P/4B-R03 | `R03/RECOMPUTED_ROWS_R03.csv`; fits in `R03/calc/fullrs_r03.py` and `R03/wolfram/common_R03_fullrs.wl` plus `callfix_*.wl` |
| 9–10 | CTC-5P-R03, CTC-5B-R03 | `R03/RECOMPUTED_ROWS_R03.csv`, `R03/CPL_OLDPRIMARY_*.csv`; chains `R03/calc/fullrs_cpl_chain_{PRIMARY,REPLACEMENT}_R03.npy`; model `R03/calc/cplmodel_r03.py` |
| 11–21 | D-P4a, D-P4b, D-P8a, D-P8c, D-P2a, D-P3a/b/c, D-P5a/b, D-P7 | `R02/FORECAST_TABLE_R02.csv`; supporting checks in `checks/` and increment scripts in `R03/INCREMENT_8929251/` |
| 22–24 | E-CD-P2, E-CD-P3, E-PHZ-1 | `R02/FORECAST_TABLE_R02.csv`; dipole calibration under `source_inputs/R02_Gaussian_Dipole_Calibration_20261112/` |

R03 is the revision that corrects the truncated sound-horizon integral \(r_s(z_*)\) used in earlier BAO+CMB fits. BAO-only rows (CTC-1P/1B and the DESI-only D-P geometry rows) were not affected by that bug. See `R03/HELD_R03.md` and `R03/calc/rs_bug_check_r03.py`.

## Layout

### `R02/` — frozen R02 forecast table and BAO-only fits

- `FORECAST_TABLE_R02.csv` / `FORECAST_TABLE_R02.md` — frozen table from which REV2 copied CTC-1P/1B and the D-P / E-CD / E-PHZ rows.
- `VALIDATION_R02.md`, `R02_NOTES.md`, `UNSUPPORTED_MODELS_R02.csv` / `.md` — validation notes and the list of models that were not run.
- `_build/` — scripts that built the R02 table (`build_r02.py`, `rows_r02.py`, `selfcheck_r02.py`).
- `wolfram/` — shared model `common_R02.wl`; BAO-only and BAO+CMB call files (`call1_baoonly_lcdm.wl`, `call1b_baoonly.wl`, `call2_lcdm_wcdm.wl`, `call3_olcdm.wl`, `callcov_*.wl`); `raw_outputs_R02.txt`, `predcov_R02.json`, `predcov_rank_R02.json`. The BAO+CMB calls in this folder still use the truncated \(r_s\) integral; REV2 does not quote those BAO+CMB numbers (the R03 revision is used instead).

The frozen table still contains a few rows that were **not** copied into the public pack (including CTC-R and INTERNAL-CONTEXT items). Those rows are left in the table so the frozen source stays intact. Their derivation files are not in this folder.

### `R03/` — corrected BAO+CMB fits used for CTC-2…5

- `calc/cplmodel_r03.py` — shared Python background / BAO / compressed-CMB model, including the Lyα replacement slots and the `RSMODE='full'` sound-horizon integral.
- `calc/fullrs_r03.py` and `fullrs_r03_output.json` — corrected Python fits and MCMC (including the published wCDM \(w\) medians and s.d.).
- `calc/fullrs_cpl_chain_PRIMARY_R03.npy`, `fullrs_cpl_chain_REPLACEMENT_R03.npy` — saved CPL chains behind CTC-5P-R03 and CTC-5B-R03.
- `calc/fresh_chain_*_R03.npy` — earlier truncated-chain reruns, kept only as the superseded products marked in the CPL `*_SUPERSEDED_TRUNCRS.*` files.
- `calc/build_recomputed_r03.py` → `RECOMPUTED_ROWS_R03.csv`; `build_cpl_fullrs_r03.py` → `CPL_OLDPRIMARY_R03.csv` / `CPL_OLDPRIMARY_BANDS_R03.csv`.
- `calc/rs_bug_check_r03.py`, `class_crosscheck_r03.py`, `fs8_fullrs_r03.py`, `w_reconcile_r03.py`, `wcdm_stepscan_fullrs_r03.py` and their JSON/log outputs.
- `wolfram/common_R03_fullrs.wl` — shared Wolfram model with the integral to infinity; `callfix_LCDM.wl`, `callfix_wCDM.wl`, `callfix_oLCDM.wl`, `callB0_wbaoonly.wl`; `fullrs_fits_R03.json`, `raw_outputs_R03.txt`.
- `CLASS_CAMB_MATCHED/` — CLASS vs CAMB matched-settings comparison (scripts, reports, spectra `.npz` / `.json`, dense CSVs). Supports the background/CMB implementation, not a separate published prediction row.
- `INCREMENT_8929251/` — free-\(A\) flat ΛCDM and Table-4 increment scripts and outputs that cross-check the BAO-only geometry (CTC-1 and related D-P rows). `source_runs/` holds the independent geometry check (STO clock-kink scripts were not copied).
- `PROPOSALS/` — dated notes on scoring, the wCDM Hessian step, and D-P8c; several of these choices were adopted in REV2 (MCMC \(w\), exact-\(z\) evaluation).
- `HELD_R03.md`, `W_RECONCILE_R03.md`, `VALIDATION_R03.md` — hold list, constant-\(w\) reconcile, and the R03 run receipt.

### `checks/` — independent R02/R03 numerical checks

- `calc_lya_replace_exact_R03.py` / `_output.json` and `calc_lya_replace_sensitivity_R02.py` / `_output.json` — Lyα official vs Eq. 26 replacement, supporting the PRIMARY vs REPLACEMENT split.
- `calc_normalization_check_R02.py` / `_output.json` — normalization check used in the R02 review.
- `calc_model_check.py` / `_output.json` — model/consistency checks (including shrink projections used near D-P3c).
- `cosmology_review_R02/` — verifier scripts and outputs for the R02 fits, BAO-only predictions, MCMC, Hessian steps and band comparisons (`verify_fits_R02.py`, `verify_mcmc_R02.py`, `verify_baoonly_pred_R02.py`, and related files). STO clock-kink files from this review were not copied.

### `wolfram_R04/` — earlier CPL/ΛCDM fit scripts (partly superseded)

Wolfram and scipy fit scripts and raw outputs that first carried the CPL BAO+CMB numbers. The CMB-using fits here inherit the truncated \(r_s\) integral and were superseded by `R03/calc` and `R03/wolfram` for published BAO+CMB rows. They are included because they document that earlier pipeline and the cross-checks (`crosscheck_scipy_R04.py`, `fit_cpl_R04.wl`, `call_new.wl`, `call_old.wl`, `reweight_chain_R04.py`, `second_check_R04.py`). Key-probe and API logs were not copied.

### `data/desi_dr2_bao/`

Official DESI DR2 Gaussian BAO mean and covariance (`desi_gaussian_bao_ALL_GCcomb_mean.txt`, `desi_gaussian_bao_ALL_GCcomb_cov.txt`) used as the calibration data for the BAO fits. These are public DESI products, not forecast text.

### `source_inputs/` — input packages behind geometry / dipole / CLASS–CAMB work

- `Best_Defensible_Forecast_Handoff_20261112/` — geometry CSVs and the independent geometry check used in the increment comparison. STO clock-kink files listed in that package's `MANIFEST.json` were not copied.
- `Geometry_Joint_Band_Addendum_20261112/` — joint latent-band scripts, CSVs, figures and review for the distance-band forecasts.
- `R02_Gaussian_Dipole_Calibration_20261112/` — Gaussian dipole calibration supporting the E-CD rows.
- `CLASS_CAMB_Historical_Reconciliation_R02/` — protocol, verifier and official CLASS/CAMB source excerpts behind `R03/CLASS_CAMB_MATCHED/`.

## What was not included, and why

- **HSU, STO, Rebound and R1 / R01** derivation files, including the Rebound Bianchi package, STO clock-kink scripts, R01 forecast tables and abstracts, and the R01 DESI/angular scratch trees. A few frozen R02 table rows still *name* those models; the models' own derivation files are not here.
- **Bruni materials and reviews whose subject is that prior work**, including named audit files and narrative reviews that discuss them.
- **Secrets, credentials and personal contact details.** Files matching `sk-or`, `@gmail`, `API_KEY`, bearer/token or similar patterns were excluded (OpenRouter runners, input receipts with email addresses, Wolfram key-probe logs, scraped HTML with site auth tokens).
- **Private forecast-addendum inputs** under the Forecast Bot `_inputs/` tree, including a file marked private.
- **`R02/INTERNAL_CONTEXT_R02.md`** — marked not for public-facing text (significance-type scoring rules). The published repository makes no significance claims.
- **Third-party papers and scraped HTML** under `evidence/` and Lyman-α source HTML (copyright; not fit scripts).
- **Files larger than 50 MB** — none of the candidate files exceeded this limit; nothing was dropped for size.
- **Bytecode / empty stderr captures**, zip archives of trees that were unpacked here instead, and source `SHA256SUMS` files that listed excluded or personal-named paths (replaced by this folder's `SHA256SUMS`).
- **Held fσ8 work in `xact_R05/`**, which is not a source of any published REV2 row.
- Inventory packages that were not sources of the published REV2 numbers and that mix excluded models (candidate register, eleven-arm prototype, alternative-background arms, Hubble-volume audit).

## Verify

```bash
sha256sum -c SHA256SUMS
```

`SHA256SUMS.ots` is an OpenTimestamps proof over `SHA256SUMS`.
