# FORECAST_TABLE_R02 — private branch on top of R01 (recorded internally at the time; nothing posted, published or timestamped)

Built 2026-11-12 from the author's handoff 8925124 (received 09:37:42 UTC) via Coordinator. R01 (`../FORECASTS_R01.md`, sha256 e27fc48e…48efb) is preserved unchanged; this is a separately dated branch. Significance-, p-value-, exceedance- and coincidence-type content appears only in `INTERNAL_CONTEXT_R02.md`.

## Counts
- Rows: 43. By label: prospective 23, conditional theory curve 11, retrospective fit 7, synthetic test 2.
- By label × readiness: conditional theory curve / NOT READY: 1; conditional theory curve / READY: 9; conditional theory curve / n/a: 1; prospective / NOT READY: 8; prospective / READY: 15; retrospective fit / n/a: 7; synthetic test / n/a: 2.
- Outcomes: all forecasts NOT_RUN (synthetic tests: PASS; retrospective fits: n/a).

## Effective independence (read before counting)
- **These rows are not independent tests.** The D-* rows are sub-rules of six DESI forecasts that share one DESI Y5 data release; a/b pairs of the same quantity are nested.
- **Distance curves:** the 9 READY conditional theory curves carry 9 × 4 redshifts × 2 distances = 72 numbers (F_AP = DM/DH is derived and never scored separately). Within one curve, every entry is a function of the fitted parameters: BAO-only ΛCDM has exactly 2 (Ωm, A); ΛCDM+CMB effectively 2 (ω_b is pinned by the prior); wCDM and oΛCDM about 3. The full predictive covariance confirms this: it has only 2–3 non-negligible eigen-directions per curve; the rest are at the 0.001 rounding level of the stored correlations (`wolfram/predcov_rank_R02.json`). PRIMARY and REPLACEMENT branches use the same data except one Lyα point, so they are near-duplicates, not two tests. All curves share the DESI DR2 BAO calibration; the CMB-based ones share Planck 2018 too.
- **Shared calibration:** A = c/(H0 rd) is exactly degenerate with a common radial/transverse calibration (handoff §3). After projecting that nuisance out, BAO-only ΛCDM keeps one identifiable direction (Ωm, through the shape/F_AP). Singular values for a real Euclid covariance cannot be computed until Euclid publishes one. Rank without that covariance is not a precision forecast.
- **The handoff's 60-entry distance package and 24-target register are NOT these rows.** Their bytes (Euclid_Candidate_Prediction_Register_20261112.zip, Geometry_Joint_Band_Addendum_20261112.zip and 7 others) are not on the box or on Drive (HANDOFF_8925124_INVENTORY.md §1–3). **No claim is made that any of the 24 register rows were run.**

## Summary table
| id | label | readiness | branch | title | tested by |
|---|---|---|---|---|---|
| D-P2a | prospective | READY | n/a | Pivot equation of state near −1 | DESI Y5 (2027) |
| D-P3a | prospective | READY | n/a | w0, wa inside predicted boxes | DESI Y5 (2027) |
| D-P3b | prospective | READY | n/a | w0–wa quadrant not abandoned | DESI Y5 (2027) |
| D-P3c | prospective | READY | n/a | w0, wa errors shrink at least 20% from DR2 | DESI Y5 (2027) |
| D-P4a | prospective | READY | n/a | BAO-only matter density stays low | DESI Y5 (2027) |
| D-P4b | prospective | READY | n/a | BAO-only Ωm stays below the Planck value | DESI Y5 (2027) |
| D-P5a | prospective | READY | n/a | Neutrino mass limit below 0.055 eV | DESI Y5 (2027) |
| D-P5b | prospective | READY | n/a | No relaxed neutrino limit or detection | DESI Y5 (2027) |
| D-P8a | prospective | READY | n/a | Early-universe H0 | DESI Y5 (2027) |
| D-P8c | prospective | READY | n/a | Ladder H0 stays at 72.5–73.5 | SH0ES through 2027 |
| D-P1a | prospective | READY | n/a | Evolving dark-energy preference (interval) | DESI Y5 (2027) |
| D-P1b | prospective | READY | n/a | Evolving dark-energy preference (floor) | DESI Y5 (2027) |
| D-P2b | prospective | READY | n/a | Pivot not far from −1 (original falsifier) | DESI Y5 (2027) |
| D-P8b | prospective | READY | n/a | Ladder–early H0 gap (threshold) | DESI Y5 (2027) |
| D-P8d | prospective | READY | n/a | Ladder–early H0 gap (floor) | DESI Y5 (2027) |
| D-P7 | prospective | NOT READY | n/a | No hemispheric BAO difference | DESI Y5 (2027) |
| E-CD-P1 | prospective | NOT READY | n/a | Count-dipole amplitude | Euclid Foundation catalogues (binding TBD) |
| E-CD-P2 | prospective | NOT READY | n/a | Count-dipole direction | Euclid Foundation catalogues (binding TBD) |
| E-CD-P3 | prospective | NOT READY | n/a | Dipole rises with redness or redshift | Euclid Foundation catalogues (binding TBD) |
| E-CD-P4 | prospective | NOT READY | n/a | Joint ℓ=1+3 fit raises dipole | Euclid Foundation catalogues (binding TBD) |
| E-CD-P5 | prospective | NOT READY | n/a | ΛCDM mock exceedance fraction | Euclid Foundation catalogues (binding TBD) |
| E-L-P6 | prospective | NOT READY | n/a | No shell-axis dipole in Euclid lensing | Euclid DR1 Complete (mid-2027) |
| E-PHZ-1 | prospective | NOT READY | n/a | Capped adaptive PHZ beats native PHZ (method, not cosmology) | Euclid Foundation catalogues (binding TBD) |
| CTC-1P | conditional theory curve | READY | PRIMARY | Flat ΛCDM, BAO only | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-1B | conditional theory curve | READY | REPLACEMENT | Flat ΛCDM, BAO only | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-2P | conditional theory curve | READY | PRIMARY | Flat ΛCDM, BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-2B | conditional theory curve | READY | REPLACEMENT | Flat ΛCDM, BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-3P | conditional theory curve | READY | PRIMARY | Constant-w (wCDM), BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-3B | conditional theory curve | READY | REPLACEMENT | Constant-w (wCDM), BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-4P | conditional theory curve | READY | PRIMARY | Curved ΛCDM (oΛCDM), BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-4B | conditional theory curve | READY | REPLACEMENT | Curved ΛCDM (oΛCDM), BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-5B | conditional theory curve | READY | REPLACEMENT | CPL (w0waCDM), BAO + compressed CMB | Euclid BAO on DR1 Complete (mid-2027+) |
| CTC-5P | conditional theory curve | NOT READY | PRIMARY | CPL (w0waCDM), BAO + compressed CMB, frozen primary | Euclid BAO on DR1 Complete (mid-2027+) |
| RF-1 | retrospective fit | n/a | n/a | Flat ΛCDM BAO-only parameters | — |
| RF-2 | retrospective fit | n/a | n/a | Flat ΛCDM BAO+CMB parameters | — |
| RF-3 | retrospective fit | n/a | n/a | Constant-w parameters | — |
| RF-4 | retrospective fit | n/a | n/a | Curvature parameters | — |
| RF-5 | retrospective fit | n/a | n/a | CPL parameters (R04) | — |
| RF-6 | retrospective fit | n/a | n/a | GWTC-4.0 Ξ0 ↔ c_M mapping check (R04 §6b) | — |
| RF-7 | retrospective fit | n/a | n/a | Fibonacci normalisation comparison | — |
| CTC-R | conditional theory curve | n/a | n/a | Elastic Rebound AP curve (DM/DH < z) | — |
| SYN-1 | synthetic test | n/a | n/a | Kinematic-dipole grid arithmetic | — |
| SYN-2 | synthetic test | n/a | n/a | Angular-separation regression suite (catalogue tooling) | — |

## Freeze blocks (one per row)
### D-P2a — Pivot equation of state near −1
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** w_p (dimensionless) at DESI's published pivot z_p ≈ 0.4–0.5; single value
- **model and priors:** w0waCDM as fitted by DESI; data DESI Y5 + CMB + DES SNe (DES-Y5 row if reported, else DES-Dovekie)
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** w_p ∈ [−1.06, −0.94] (−1.00 ± 0.06). Forecaster's central 68% prediction interval (R01 default; the author to confirm label). No full distribution specified; interval used as stated.
- **scoring / exclusions:** PASS iff −1.06 ≤ w_p ≤ −0.94; FAIL otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31. Also NOT_RUN if no w_p is published.
- **sources:** DESI_PREDICTIONS_source.md L19–24; R01 WOLFRAM_CHECKS W2
- **notes:** Basis: box fit w_p = −1.044 ± 0.050 at a_p = 0.673 (desi_r01/fit_results.json). R04 §7: against expected errors alone ±0.06 is ~77% coverage.

### D-P3a — w0, wa inside predicted boxes
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** w0, wa (dimensionless); single values
- **model and priors:** w0waCDM; DESI Y5 + CMB + DES SNe (DES-Y5 if reported, else DES-Dovekie)
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** w0 ∈ [−0.86, −0.66]; wa ∈ [−1.15, −0.45] (−0.76 ± 0.10; −0.80 ± 0.35). Forecaster's central 68% prediction interval (R01 default; the author to confirm label). No full distribution specified; interval used as stated.
- **scoring / exclusions:** PASS iff both inside; FAIL otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L26–31; R01 W2
- **notes:** Context (retrospective): DESI DR2 Results IV DESI+CMB+DES-Dovekie w0 = −0.821 ± 0.054, wa = −0.65 ± 0.20 (R03 L34), both inside. R04 §7: against expected errors alone ±0.10/±0.35 ≈ 97–99% / 95–98%.

### D-P3b — w0–wa quadrant not abandoned
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Central w0, wa
- **model and priors:** as D-P3a
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** Central w0 ≥ −0.95 and wa ≤ −0.2 (threshold claim).
- **scoring / exclusions:** FAIL iff central w0 < −0.95 OR central wa > −0.2; PASS otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L31

### D-P3c — w0, wa errors shrink at least 20% from DR2
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Published 68% errors e(w0), e(wa) (asymmetric errors averaged)
- **model and priors:** as D-P3a
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** e(w0) ≤ 0.0456 and e(wa) ≤ 0.176 (threshold).
- **scoring / exclusions:** PASS iff both hold; FAIL otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L28; calc_model_check_output.json C3_shrink

### D-P4a — BAO-only matter density stays low
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Ωm (dimensionless), flat ΛCDM, DESI Y5 BAO alone
- **model and priors:** flat ΛCDM (DESI)
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** Ωm ∈ [0.288, 0.308] (0.298 ± 0.010). Forecaster's central 68% prediction interval (R01 default; the author to confirm label). No full distribution specified; interval used as stated.
- **scoring / exclusions:** PASS iff inside; FAIL otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L33–38
- **notes:** Context: box BAO-only Ωm = 0.2975 ± 0.0086 (primary) and 0.3017 ± 0.0077 (Lyα replacement branch) (R02/wolfram raw outputs).

### D-P4b — BAO-only Ωm stays below the Planck value
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Ωm as D-P4a
- **model and priors:** flat ΛCDM
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** Ωm < 0.315 (threshold).
- **scoring / exclusions:** FAIL iff Ωm ≥ 0.315; PASS otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L38

### D-P5a — Neutrino mass limit below 0.055 eV
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** 95% upper limit on Σmν (eV), ΛCDM, DESI Y5 + CMB, DESI baseline prior
- **model and priors:** ΛCDM + Σmν (DESI)
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** UL95 < 0.055 eV.
- **scoring / exclusions:** PASS iff published UL95 < 0.055 eV; FAIL otherwise (including any reported lower bound).
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L40–45

### D-P5b — No relaxed neutrino limit or detection
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** UL95 and any 95% lower bound on Σmν
- **model and priors:** as D-P5a
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** UL95 ≤ 0.08 eV and no 95% lower bound > 0.06 eV.
- **scoring / exclusions:** FAIL iff UL95 > 0.08 eV OR a 95% lower bound > 0.06 eV; PASS otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L45

### D-P8a — Early-universe H0
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** H0 (km/s/Mpc), ΛCDM, DESI Y5 + CMB
- **model and priors:** ΛCDM (DESI)
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** H0 ∈ [67.8, 68.6] (68.2 ± 0.4). Forecaster's central 68% prediction interval (R01 default; the author to confirm label). No full distribution specified; interval used as stated.
- **scoring / exclusions:** PASS iff inside; FAIL otherwise.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L61–66

### D-P8c — Ladder H0 stays at 72.5–73.5
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** Latest SH0ES (Riess et al.) H0 public on or before 2027-12-31
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** SH0ES's own
- **observable / units / redshift & scale grid:** H0 (km/s/Mpc), single value
- **model and priors:** distance ladder (SH0ES)
- **calibration data cutoff:** 2026-10-13
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** n/a
- **contaminants:** SH0ES's own
- **estimator:** SH0ES published
- **covariance / shared calibration:** SH0ES published
- **predictive distribution (with uncertainty):** 72.5 ≤ H0 ≤ 73.5 (stated range)
- **scoring / exclusions:** PASS iff latest SH0ES central value on 2027-12-31 is in [72.5, 73.5]; FAIL otherwise.
- **abstention rule:** Prospective only for SH0ES results first public after 2026-10-13; the latest current SH0ES value was not checked (UNVERIFIED).
- **sources:** DESI_PREDICTIONS_source.md L63

### D-P1a — Evolving dark-energy preference (interval)
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Significance-type quantity: INTERNAL CONTEXT only
- **model and priors:** see INTERNAL_CONTEXT_R02.md
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#D-P1a holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#D-P1a
- **sources:** DESI_PREDICTIONS_source.md

### D-P1b — Evolving dark-energy preference (floor)
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Significance-type quantity: INTERNAL CONTEXT only
- **model and priors:** see INTERNAL_CONTEXT_R02.md
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#D-P1b holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#D-P1b
- **sources:** DESI_PREDICTIONS_source.md

### D-P2b — Pivot not far from −1 (original falsifier)
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Significance-type quantity: INTERNAL CONTEXT only
- **model and priors:** see INTERNAL_CONTEXT_R02.md
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#D-P2b holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#D-P2b
- **sources:** DESI_PREDICTIONS_source.md

### D-P8b — Ladder–early H0 gap (threshold)
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Significance-type quantity: INTERNAL CONTEXT only
- **model and priors:** see INTERNAL_CONTEXT_R02.md
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#D-P8b holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#D-P8b
- **sources:** DESI_PREDICTIONS_source.md

### D-P8d — Ladder–early H0 gap (floor)
**prospective · READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** DESI's own Y5 tracer samples (external).
- **observable / units / redshift & scale grid:** Significance-type quantity: INTERNAL CONTEXT only
- **model and priors:** see INTERNAL_CONTEXT_R02.md
- **calibration data cutoff:** Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** DESI's own footprint and veto masks (external).
- **contaminants:** Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.
- **estimator:** DESI's official Y5 BAO + cosmology inference (external).
- **covariance / shared calibration:** DESI's published Y5 posterior (external).
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#D-P8d holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#D-P8d
- **sources:** DESI_PREDICTIONS_source.md

### D-P7 — No hemispheric BAO difference
**prospective · NOT READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** DESI DR3/Y5 LSS catalogues (release TBD). DR1 catalogues are already public (not prospective).
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (proposed: DESI BAO tracer bins)
- **observable / units / redshift & scale grid:** Δα_iso = α_N − α_S (dimensionless), hemispheres split by the plane ⟂ CMB-dipole axis; one value per tracer bin or combined (TBD)
- **model and priors:** Isotropic ΛCDM BAO
- **calibration data cutoff:** 2026-10-13
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD: DESI footprint split by hemisphere
- **contaminants:** TBD: hemisphere-dependent imaging depth, stellar density, extinction
- **estimator:** TBD: per-hemisphere α_iso with DESI fitter
- **covariance / shared calibration:** TBD: per-hemisphere mocks
- **predictive distribution (with uncertainty):** 95% interval for Δα_iso inside (−3×10⁻³, +3×10⁻³)
- **scoring / exclusions:** PROPOSED: PASS iff the published/derived 95% interval for Δα_iso lies inside (−0.003, +0.003); FAIL otherwise.
- **abstention rule:** NOT_RUN if no DR3/Y5 catalogues by 2028-12-31.
- **sources:** DESI_PREDICTIONS_source.md L54–59; COSMOLOGY_MODEL_CHECK L110
- **notes:** Axis coordinates not in any source file (TBD).

### E-CD-P1 — Count-dipole amplitude
**prospective · NOT READY · UNVERIFIED · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)
- **observable / units / redshift & scale grid:** Number-count dipole amplitude D (dimensionless)
- **model and priors:** Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)
- **calibration data cutoff:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD; buildable from Foundation VMPZ maps (R03 L67) Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks.
- **contaminants:** Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3); magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)
- **estimator:** TBD
- **covariance / shared calibration:** TBD (Foundation-footprint mocks)
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only (significance-type)
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#E-CD-P1 holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#E-CD-P1
- **sources:** fa.txt L112–117; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)
- **notes:** NOT READY (R02 L28; R01 L16).

### E-CD-P2 — Count-dipole direction
**prospective · NOT READY · UNVERIFIED · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)
- **observable / units / redshift & scale grid:** Dipole direction (l,b), degrees, Galactic frame assumed
- **model and priors:** Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)
- **calibration data cutoff:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD; buildable from Foundation VMPZ maps (R03 L67) Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks.
- **contaminants:** Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3); magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)
- **estimator:** TBD
- **covariance / shared calibration:** TBD (Foundation-footprint mocks)
- **predictive distribution (with uncertainty):** Best-fit direction within 30° of (l,b) = (242.28°, 37.10°)
- **scoring / exclusions:** PROPOSED: PASS iff great-circle separation ≤ 30°; FAIL otherwise.
- **abstention rule:** NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.
- **sources:** fa.txt L119–123; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)
- **notes:** NOT READY (R02 L28; R01 L16).

### E-CD-P3 — Dipole rises with redness or redshift
**prospective · NOT READY · UNVERIFIED · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)
- **observable / units / redshift & scale grid:** D per bin (dimensionless), ≥3 bins of one variable (TBD)
- **model and priors:** Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)
- **calibration data cutoff:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD; buildable from Foundation VMPZ maps (R03 L67) Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks.
- **contaminants:** Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3); magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)
- **estimator:** TBD
- **covariance / shared calibration:** TBD (Foundation-footprint mocks)
- **predictive distribution (with uncertainty):** Strictly increasing D with max/min ≥ 2
- **scoring / exclusions:** PROPOSED: PASS iff ≥3 bins, strictly increasing, max/min ≥ 2; FAIL otherwise.
- **abstention rule:** NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.
- **sources:** fa.txt L125–130; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)
- **notes:** NOT READY (R02 L28; R01 L16).

### E-CD-P4 — Joint ℓ=1+3 fit raises dipole
**prospective · NOT READY · UNVERIFIED · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)
- **observable / units / redshift & scale grid:** D_joint vs D_dipole-only; octupole coefficients
- **model and priors:** Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)
- **calibration data cutoff:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD; buildable from Foundation VMPZ maps (R03 L67) Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks.
- **contaminants:** Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3); magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)
- **estimator:** TBD
- **covariance / shared calibration:** TBD (Foundation-footprint mocks)
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only (second clause is significance-type)
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#E-CD-P4 holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#E-CD-P4
- **sources:** fa.txt L132–137; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)
- **notes:** NOT READY (R02 L28; R01 L16).

### E-CD-P5 — ΛCDM mock exceedance fraction
**prospective · NOT READY · UNVERIFIED · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)
- **observable / units / redshift & scale grid:** Fraction of ≥2,000 ΛCDM mocks with D ≥ 0.01554
- **model and priors:** Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)
- **calibration data cutoff:** October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD; buildable from Foundation VMPZ maps (R03 L67) Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks.
- **contaminants:** Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3); magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)
- **estimator:** TBD
- **covariance / shared calibration:** TBD (Foundation-footprint mocks)
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only (exceedance-fraction claim)
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#E-CD-P5 holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#E-CD-P5
- **sources:** fa.txt L139–143; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)
- **notes:** NOT READY (R02 L28; R01 L16).

### E-L-P6 — No shell-axis dipole in Euclid lensing
**prospective · NOT READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1 Complete (mid-2027): SHE shear catalogues and 2D-MASS-WL convergence maps. Not in Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD
- **observable / units / redshift & scale grid:** Kinematic-subtracted convergence dipole (dimensionless)
- **model and priors:** ΛCDM kinematic only, β = 1.23×10⁻³ (scaling factors TBD)
- **calibration data cutoff:** 2026-10-13
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD
- **contaminants:** PSF/shear calibration modes, depth anisotropy (fa.txt L174–179)
- **estimator:** TBD
- **covariance / shared calibration:** TBD
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only (detection-threshold claim)
- **scoring / exclusions:** Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#E-L-P6 holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type.
- **abstention rule:** NOT_RUN until floor, tolerance, mask, estimator, covariance are numeric.
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#E-L-P6
- **sources:** DESI_PREDICTIONS_source.md L47–52

### E-PHZ-1 — Capped adaptive PHZ beats native PHZ (method, not cosmology)
**prospective · NOT READY · PROVISIONAL · NOT_RUN · branch n/a**

- **product / version / schema:** Euclid DR1-Foundation PHZ catalogue (DpdPhzPfOutputCatalog) + independent truth set (TBD)
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** TBD: cohort not bound (fa.txt L96–98)
- **observable / units / redshift & scale grid:** Mean five-class Brier score (dimensionless); classes [0,1),[1,2),[2,3),[3,6),[6,∞)
- **model and priors:** q = (1−α)p + αu, fixed adaptive α rule (fa.txt L86–92)
- **calibration data cutoff:** Rule fixed before 2026-11-12 (Freeze Addendum)
- **exposure to target outcomes:** No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.
- **selection and mask operator:** TBD
- **contaminants:** Truth-set dependence on shared calibration; outliers
- **estimator:** Mean Brier difference
- **covariance / shared calibration:** TBD (paired bootstrap)
- **predictive distribution (with uncertainty):** mean Brier(q) < mean Brier(p)
- **scoring / exclusions:** PROPOSED: PASS iff mean Brier(q) < mean Brier(p) on the frozen cohort; FAIL otherwise.
- **abstention rule:** Prospective only if the cohort is frozen before the PHZ outputs are opened.
- **sources:** fa.txt L85–98; COSMOLOGY_MODEL_CHECK L134–138

### CTC-1P — Flat ΛCDM, BAO only
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch PRIMARY**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** Flat ΛCDM, radiation omitted, params (Ωm, A = c/(H0 rd)), no priors beyond 0.1<Ωm<0.6
- **calibration data cutoff:** DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.0789 ± 0.0710, DH/rd 17.8273 ± 0.0666; z=1.2: DM/rd 25.9885 ± 0.0760, DH/rd 15.0084 ± 0.0736; z=1.5: DM/rd 30.1415 ± 0.0837, DH/rd 12.7642 ± 0.0739; z=1.8: DM/rd 33.6928 ± 0.0944, DH/rd 10.9785 ± 0.0704
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call1b PRIMARY; reproduces calc_normalization_check_R02_output.json (Ωm 0.29746, A 29.5246)

### CTC-1B — Flat ΛCDM, BAO only
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch REPLACEMENT**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** as CTC-1P
- **calibration data cutoff:** DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added)
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.1067 ± 0.0689, DH/rd 17.8121 ± 0.0617; z=1.2: DM/rd 26.0102 ± 0.0750, DH/rd 14.9844 ± 0.0663; z=1.5: DM/rd 30.1554 ± 0.0828, DH/rd 12.7373 ± 0.0658; z=1.8: DM/rd 33.6987 ± 0.0927, DH/rd 10.9516 ± 0.0624
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call1b BRANCH; = R01 E-BAO-1 central values (R01 W1)

### CTC-2P — Flat ΛCDM, BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch PRIMARY**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** Flat ΛCDM; Flat priors 0.1<Ωm<0.6, 0.4<h<1, 0.015<ω_b<0.03; radiation from h with N_eff=3.046; rd fitting formula (fit_cpl.py / R04)
- **calibration data cutoff:** DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY; Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.0534 ± 0.0617, DH/rd 17.5713 ± 0.0162; z=1.2: DM/rd 25.8812 ± 0.0643, DH/rd 14.7263 ± 0.0058; z=1.5: DM/rd 29.9497 ± 0.0642, DH/rd 12.4863 ± 0.0056; z=1.8: DM/rd 33.4201 ± 0.0630, DH/rd 10.7174 ± 0.0073
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call1 3rd element; best fit reproduces R04 old-Lyα ΛCDM (Ωm 0.32397)

### CTC-2B — Flat ΛCDM, BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch REPLACEMENT**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** as CTC-2P
- **calibration data cutoff:** DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added); Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.0581 ± 0.0604, DH/rd 17.5726 ± 0.0159; z=1.2: DM/rd 25.8862 ± 0.0629, DH/rd 14.7267 ± 0.0057; z=1.5: DM/rd 29.9547 ± 0.0629, DH/rd 12.4863 ± 0.0056; z=1.8: DM/rd 33.4250 ± 0.0617, DH/rd 10.7171 ± 0.0072
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call2 LCDM BRANCH; matches R04 §5 / wolfram_raw_02_fit.txt Laplace values

### CTC-3P — Constant-w (wCDM), BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch PRIMARY**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** Flat wCDM, prior −3<w<1; Flat priors 0.1<Ωm<0.6, 0.4<h<1, 0.015<ω_b<0.03; radiation from h with N_eff=3.046; rd fitting formula (fit_cpl.py / R04)
- **calibration data cutoff:** DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY; Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.0317 ± 0.0679, DH/rd 17.6460 ± 0.0837; z=1.2: DM/rd 25.8798 ± 0.0650, DH/rd 14.7854 ± 0.0650; z=1.5: DM/rd 29.9634 ± 0.0658, DH/rd 12.5285 ± 0.0462; z=1.8: DM/rd 33.4442 ± 0.0675, DH/rd 10.7460 ± 0.0320
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call2 wCDM PRIMARY
- **notes:** Best fit w = −1.043 ± 0.049 (retrospective).

### CTC-3B — Constant-w (wCDM), BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch REPLACEMENT**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** as CTC-3P
- **calibration data cutoff:** DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added); Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.0346 ± 0.0662, DH/rd 17.6567 ± 0.0836; z=1.2: DM/rd 25.8854 ± 0.0636, DH/rd 14.7930 ± 0.0646; z=1.5: DM/rd 29.9709 ± 0.0646, DH/rd 12.5333 ± 0.0457; z=1.8: DM/rd 33.4529 ± 0.0665, DH/rd 10.7490 ± 0.0315
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call2 wCDM BRANCH
- **notes:** Best fit w = −1.049 ± 0.049 (retrospective).

### CTC-4P — Curved ΛCDM (oΛCDM), BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch PRIMARY**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** ΛCDM + Ωk, prior −0.3<Ωk<0.3; Flat priors 0.1<Ωm<0.6, 0.4<h<1, 0.015<ω_b<0.03; radiation from h with N_eff=3.046; rd fitting formula (fit_cpl.py / R04). Compressed CMB priors are used outside their flat-model derivation (caveat).
- **calibration data cutoff:** DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY; Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.1308 ± 0.0681, DH/rd 17.6763 ± 0.0423; z=1.2: DM/rd 25.9836 ± 0.0747, DH/rd 14.8220 ± 0.0361; z=1.5: DM/rd 30.0731 ± 0.0789, DH/rd 12.5710 ± 0.0320; z=1.8: DM/rd 33.5604 ± 0.0818, DH/rd 10.7916 ± 0.0286
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call3 oLCDM PRIMARY
- **notes:** Best fit Ωk = −0.0034 ± 0.0013 (retrospective; compressed-prior caveat).

### CTC-4B — Curved ΛCDM (oΛCDM), BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch REPLACEMENT**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately); scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** as CTC-4P
- **calibration data cutoff:** DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added); Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).
- **predictive distribution (with uncertainty):** Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: z=0.9: DM/rd 21.1426 ± 0.0672, DH/rd 17.6840 ± 0.0420; z=1.2: DM/rd 25.9972 ± 0.0739, DH/rd 14.8276 ± 0.0357; z=1.5: DM/rd 30.0877 ± 0.0782, DH/rd 12.5753 ± 0.0316; z=1.8: DM/rd 33.5759 ± 0.0811, DH/rd 10.7950 ± 0.0282
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** R02/wolfram/raw_outputs_R02.txt call3 oLCDM BRANCH
- **notes:** Best fit Ωk = −0.0036 ± 0.0012 (retrospective).

### CTC-5B — CPL (w0waCDM), BAO + compressed CMB
**conditional theory curve · READY · PROVISIONAL · NOT_RUN · branch REPLACEMENT**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** DM/rd, DH/rd on z = 0.9, 1.2, 1.5, 1.8; scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** CPL; prior −3<w0<1, −5<wa<3; Flat priors 0.1<Ωm<0.6, 0.4<h<1, 0.015<ω_b<0.03; radiation from h with N_eff=3.046; rd fitting formula (fit_cpl.py / R04)
- **calibration data cutoff:** DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added); Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = diag(s_pred²) from chain half-widths; chain cross-correlations were not saved in R04, so they are ignored (declared approximation). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent.
- **predictive distribution (with uncertainty):** Posterior median and 68% interval from importance-reweighted box chains (R04 §5): z=0.9 DM/rd 20.997 [20.923, 21.071], DH/rd 17.627 [17.529, 17.726]; z=1.2 25.854 [25.781, 25.927], 14.846 [14.772, 14.932]; z=1.5 29.963 [29.889, 30.035], 12.608 [12.536, 12.690]; z=1.8 33.467 [33.391, 33.542], 10.819 [10.756, 10.882]. s_pred = half-width of the 68% interval.
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise.
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** wolfram_R04/WOLFRAM_RESULTS_R04.md L117–129
- **notes:** R04 labels ρ=+0.225 UNVERIFIED; R03 L24 verified it. Non-Gaussian posterior (w0–wa degeneracy): Gaussian scoring is an approximation.

### CTC-5P — CPL (w0waCDM), BAO + compressed CMB, frozen primary
**conditional theory curve · NOT READY · UNVERIFIED · NOT_RUN · branch PRIMARY**

- **product / version / schema:** First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation.
- **acquisition UTC / hash:** Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.
- **sample and quality cuts:** Euclid Consortium's published BAO sample (external)
- **observable / units / redshift & scale grid:** as CTC-5B; scale grid: n/a (BAO distances, no k-dependence)
- **model and priors:** as CTC-5B
- **calibration data cutoff:** DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY; Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** Euclid's (external; randoms/visibility masks are Complete-era)
- **contaminants:** Line interlopers, redshift failures, purity/completeness (Euclid's; external)
- **estimator:** Euclid's published BAO fit (external)
- **covariance / shared calibration:** C_E = Euclid published covariance; C_pred = diag(s_pred²) from chain half-widths; chain cross-correlations were not saved in R04, so they are ignored (declared approximation). Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent.
- **predictive distribution (with uncertainty):** MISSING: R04 ran the old-Lyα CPL fit (best fit w0 −0.774, wa −0.791) but its Hessian was not positive-definite and no chain bands were produced for the primary. The original box chain (desi_r01/chain_w0waCDM.npy) was fit to the primary data and could supply them.
- **scoring / exclusions:** PASS iff (d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles'); FAIL otherwise (once predictive bands exist).
- **abstention rule:** NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes.
- **sources:** wolfram_R04/WOLFRAM_RESULTS_R04.md L75, L80

### RF-1 — Flat ΛCDM BAO-only parameters
**retrospective fit · n/a · VERIFIED · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** Primary Ωm 0.29746 ± 0.00862, A 29.525 ± 0.214 (corr 0.924); replacement Ωm 0.30171 ± 0.00770, A 29.633 ± 0.196 (corr 0.910)
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** R02/wolfram/raw_outputs_R02.txt call1b
- **notes:** Two code paths agree: R02 Wolfram reproduces R02/R03 Python JSON (RF-1) and R04 (RF-2).

### RF-2 — Flat ΛCDM BAO+CMB parameters
**retrospective fit · n/a · VERIFIED · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** Primary Ωm 0.32397 ± 0.00429, h 0.69868 ± 0.00311; replacement Ωm 0.32428 ± 0.00421, h 0.69846 ± 0.00304
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** R02/wolfram/raw_outputs_R02.txt call1, call2
- **notes:** Two code paths agree: R02 Wolfram reproduces R02/R03 Python JSON (RF-1) and R04 (RF-2).

### RF-3 — Constant-w parameters
**retrospective fit · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** Primary w −1.043 ± 0.049, Ωm 0.3167 ± 0.0093; replacement w −1.049 ± 0.049, Ωm 0.3162 ± 0.0092
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** R02/wolfram/raw_outputs_R02.txt call2
- **notes:** Fit statistics are in INTERNAL CONTEXT only.

### RF-4 — Curvature parameters
**retrospective fit · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** Primary Ωk −0.0034 ± 0.0013; replacement Ωk −0.0036 ± 0.0012 (compressed-CMB caveat)
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** R02/wolfram/raw_outputs_R02.txt call3
- **notes:** Fit statistics are in INTERNAL CONTEXT only.

### RF-5 — CPL parameters (R04)
**retrospective fit · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** Replacement best fit w0 −0.767, wa −0.824; reweighted-chain w0 −0.700 ± 0.291, wa −1.069 ± 0.883
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** wolfram_R04/WOLFRAM_RESULTS_R04.md L75–77
- **notes:** Fit statistics are in INTERNAL CONTEXT only.

### RF-6 — GWTC-4.0 Ξ0 ↔ c_M mapping check (R04 §6b)
**retrospective fit · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** c_M = 1.3 → Ξ0 = 1.447 vs published 1.4^{+1.0}_{−0.4} (consistent)
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **sources:** wolfram_R04/WOLFRAM_RESULTS_R04.md §6b
- **notes:** Fit statistics are in INTERNAL CONTEXT only.

### RF-7 — Fibonacci normalisation comparison
**retrospective fit · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)
- **acquisition UTC / hash:** Box files hashed in SHA256SUMS
- **sample and quality cuts:** n/a (retrospective fit to already-published values; see sources)
- **observable / units / redshift & scale grid:** Model parameters
- **model and priors:** see title
- **calibration data cutoff:** Data public before the fit
- **exposure to target outcomes:** Fully exposed: these are fits to already-public data.
- **selection and mask operator:** n/a (retrospective fit to already-published values; see sources)
- **contaminants:** n/a (retrospective fit to already-published values; see sources)
- **estimator:** n/a (retrospective fit to already-published values; see sources)
- **covariance / shared calibration:** n/a (retrospective fit to already-published values; see sources)
- **predictive distribution (with uncertainty):** INTERNAL CONTEXT only (coincidence-type claim)
- **scoring / exclusions:** Not a forecast; not scored.
- **abstention rule:** n/a
- **internal-context pointer:** INTERNAL_CONTEXT_R02.md#RF-7
- **sources:** R03 L60–62
- **notes:** Fit statistics are in INTERNAL CONTEXT only.

### CTC-R — Elastic Rebound AP curve (DM/DH < z)
**conditional theory curve · n/a · PROVISIONAL · n/a · branch n/a**

- **product / version / schema:** none (illustrative observer epoch)
- **acquisition UTC / hash:** n/a
- **sample and quality cuts:** n/a (see notes)
- **observable / units / redshift & scale grid:** AP = DM/DH at z = 0.295, 0.51, 0.706
- **model and priors:** closed periodic-scalar branch, illustrative parameters
- **calibration data cutoff:** DESI values already read (retrospective comparison)
- **exposure to target outcomes:** Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.
- **selection and mask operator:** n/a (see notes)
- **contaminants:** n/a (see notes)
- **estimator:** n/a (see notes)
- **covariance / shared calibration:** n/a (see notes)
- **predictive distribution (with uncertainty):** 0.270264, 0.409992, 0.439783
- **scoring / exclusions:** Not scored (no likelihood; domain z ≤ 0.706 cannot reach Euclid bins).
- **abstention rule:** n/a
- **sources:** COSMOLOGY_MODEL_CHECK L140–150

### SYN-1 — Kinematic-dipole grid arithmetic
**synthetic test · n/a · VERIFIED · PASS · branch n/a**

- **product / version / schema:** none (synthetic grid)
- **acquisition UTC / hash:** n/a
- **sample and quality cuts:** n/a (synthetic engineering test; no observational data)
- **observable / units / redshift & scale grid:** D_kin = [2 + x(1+α)]β on x ∈ [0.5, 2], α ∈ [0.5, 1.5]
- **model and priors:** kinematic dipole formula
- **calibration data cutoff:** n/a
- **exposure to target outcomes:** No observational data involved.
- **selection and mask operator:** n/a (synthetic engineering test; no observational data)
- **contaminants:** n/a (synthetic engineering test; no observational data)
- **estimator:** n/a (synthetic engineering test; no observational data)
- **covariance / shared calibration:** n/a (synthetic engineering test; no observational data)
- **predictive distribution (with uncertainty):** Grid 0.0034–0.0086; CatWISE-like point 0.0064696
- **scoring / exclusions:** PASS = Wolfram and Python agree to 1e-16 (R04 §1)
- **abstention rule:** Not a Euclid prediction.
- **sources:** wolfram_R04/WOLFRAM_RESULTS_R04.md L24–44

### SYN-2 — Angular-separation regression suite (catalogue tooling)
**synthetic test · n/a · VERIFIED · PASS · branch n/a**

- **product / version / schema:** Euclid angular-separation candidate package R01
- **acquisition UTC / hash:** zip sha256 f47e6a28…50fd
- **sample and quality cuts:** n/a (synthetic engineering test; no observational data)
- **observable / units / redshift & scale grid:** Great-circle separation errors (deg)
- **model and priors:** n/a
- **calibration data cutoff:** Suite fixed 2026-10-24/26
- **exposure to target outcomes:** No observational data involved.
- **selection and mask operator:** n/a (synthetic engineering test; no observational data)
- **contaminants:** n/a (synthetic engineering test; no observational data)
- **estimator:** n/a (synthetic engineering test; no observational data)
- **covariance / shared calibration:** n/a (synthetic engineering test; no observational data)
- **predictive distribution (with uncertainty):** max random error 4.26e-14 deg
- **scoring / exclusions:** Table-3 suite all PASS (NUMERICAL_REVIEW §7)
- **abstention rule:** n/a
- **sources:** NUMERICAL_REVIEW.md §4, §7
