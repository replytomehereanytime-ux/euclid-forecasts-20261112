# RECEIPT, CLASS_CAMB_MATCHED run_01 (UTC)

| Run | status | start UTC | end UTC | engine version |
|---|---|---|---|---|
| A1_camb_mnu006 | OK | 2026-11-12T10:24:54.875770+00:00 | 2026-11-12T10:25:06.788974+00:00 | CAMB 2.0.5 |
| A2_class_matched_massive | OK | 2026-11-12T10:25:06.789624+00:00 | 2026-11-12T10:25:12.876695+00:00 | CLASS v3.4.2 |
| A3_camb_bbn_YHe | OK | 2026-11-12T10:25:12.876996+00:00 | 2026-11-12T10:25:19.744158+00:00 | CAMB 2.0.5 |
| A3b_camb_hyrec | FAILED — CAMBValueError('Class not found: HyRec') | 2026-11-12T10:25:19.744466+00:00 | 2026-11-12T10:25:19.744548+00:00 |   |
| A3b_class_hyrec | OK | 2026-11-12T10:25:19.744600+00:00 | 2026-11-12T10:25:22.441748+00:00 | CLASS v3.4.2 |
| A4_class_matter_source_default | OK | 2026-11-12T10:25:22.442119+00:00 | 2026-11-12T10:25:25.120703+00:00 | CLASS v3.4.2 |
| A6_hist_replay_camb | OK | 2026-11-12T10:25:25.121030+00:00 | 2026-11-12T10:25:25.570861+00:00 | CAMB 2.0.5 |
| A6_hist_replay_class | OK | 2026-11-12T10:25:25.571042+00:00 | 2026-11-12T10:25:25.665272+00:00 | CLASS v3.4.2 |
| camb_base | OK | 2026-11-12T10:22:49.910323+00:00 | 2026-11-12T10:22:51.812266+00:00 | CAMB 2.0.5 |
| camb_base_interp80 | OK | 2026-11-12T10:23:02.386906+00:00 | 2026-11-12T10:23:05.865121+00:00 | CAMB 2.0.5 |
| camb_tight | OK | 2026-11-12T10:22:51.813899+00:00 | 2026-11-12T10:22:58.636419+00:00 | CAMB 2.0.5 |
| camb_tighter | OK | 2026-11-12T10:24:26.475529+00:00 | 2026-11-12T10:24:48.521094+00:00 | CAMB 2.0.5 |
| class_base | OK | 2026-11-12T10:22:58.638082+00:00 | 2026-11-12T10:22:59.732058+00:00 | CLASS v3.4.2 |
| class_base_interp80 | OK | 2026-11-12T10:23:05.867011+00:00 | 2026-11-12T10:23:07.846730+00:00 | CLASS v3.4.2 |
| class_tight | OK | 2026-11-12T10:22:59.733534+00:00 | 2026-11-12T10:23:02.385116+00:00 | CLASS v3.4.2 |
| class_tighter | OK | 2026-11-12T10:24:48.521483+00:00 | 2026-11-12T10:24:54.874038+00:00 | CLASS v3.4.2 |

Commands are in run_01/*.cmd; per-script start/end/exit are in run_01/*.times:
- `run_01/probe_params.times`: 2026-11-12T10:20:01.786Z / exit=0 / 2026-11-12T10:20:05.049Z
- `run_01/run_baseline.times`: 2026-11-12T10:22:49.608Z / exit=0 / 2026-11-12T10:23:07.919Z
- `run_01/run_tighter_and_attribution.times`: 2026-11-12T10:24:26.186Z / exit=0 / 2026-11-12T10:25:25.754Z
- Analysis: `/workspace/r05_cosmo_env/bin/python run_01/analyse_baseline.py`, `run_01/analyse_attribution.py`, `run_01/make_report.py`; checker: `python verify_spectra.py --self-test | comparison.csv | dense.csv --dense | dense_24001.csv --dense`, all exit 0.
- Probe runs: probe_params.py (first launch interrupted at 10:19:53Z with no output, retained as noted; relaunched 10:20:01Z → 10:20:05Z, exit 0).
- Each run json has the full CAMB `params_dump` and the CLASS `class_dict_passed` plus `class_pars_readback`. Raw native and interpolated arrays are in the matching .npz. All output hashes are in ../SHA256SUMS (this branch).
