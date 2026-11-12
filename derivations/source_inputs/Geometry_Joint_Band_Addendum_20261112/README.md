# Joint latent-band addendum

Read REPORT.md and inspect Joint_Latent_Bands_20261112.png first. The new envelope is a separately dated uncertainty-presentation option, not a changed primary forecast or a calibrated Euclid measurement prediction.

Reproduce in a new extracted directory with existing Python, NumPy and SciPy:

1. `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python joint_bands.py --resolution lower`
2. `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python joint_bands.py --resolution higher`
3. In that fresh directory, copy independent_review/audit.py into an independent_review subdirectory and run `OPENBLAS_NUM_THREADS=1 python independent_review/audit.py 80`, then the same command with `128`. These preserve the independent method and tighter check.
4. `python compare_and_export.py`

The producer refuses to overwrite existing RESULT_lower.json or RESULT_higher.json. To run it without deleting archived evidence, copy the code, PLAN.json and inputs directory into a fresh directory. The replay receipt describes exactly such a fresh-directory execution. No source query or installation is needed.

JOINT_BANDS.csv includes all 576 coordinate rows. SOURCE/PLAN hashes bind the unchanged old-DESI inputs. Other numerical runs, source code, an initial preflight failure and the independent audit are retained. The figure uses only the verified primary free-A 15-coordinate case and makes no continuous-redshift band claim.
