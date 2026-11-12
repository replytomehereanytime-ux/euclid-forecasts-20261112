# VALIDATION_R02 (private)

## A. Automated self-check: `/workspace/rs3env/bin/python _build/selfcheck_r02.py` (run 2026-11-12T09:51:38Z, i.e. 04:51 ET)
```
PASS  C1 row count 43  [43]
PASS  C2 exactly one of 4 labels per row
PASS  C3 unique ids
PASS  C4 all 14 freeze fields non-empty  [[]]
PASS  C5 every READY rule has PASS and FAIL  [[]]
PASS  C6 forecast outcomes NOT_RUN
PASS  C7 no σ / p-value / significance / coincidence claims outside INTERNAL_CONTEXT (σ8 amplitude allowed)
PASS  C8 INTERNAL_CONTEXT clearly marked
PASS  C9 CTC-1..4 means match raw_outputs_R02.txt and ± match predcov_R02.json (4 dp)  [64 pairs checked; []]
PASS  C10 q95 chi-square quantiles
PASS  C11 predictive correlation matrices symmetric, unit-diagonal, PSD within 0.001 rounding  [[]]
PASS  C12 R01 frozen files unchanged  [[]]
PASS  C13 R05 files match their SHA256SUMS  [[]]
PASS  C14 R04 results file hash
PASS  C15 counts in R02_NOTES match table  [{'prospective': 23, 'conditional theory curve': 11, 'retrospective fit': 7, 'synthetic test': 2}]
PASS  C16 no API-key-like strings in R02 files
PASS  C17 unsupported table has 10 models in the author's order

17/17 PASS
```

## B. Manual read-through (the reviewer read the files; this is not independent checking)
- I read the header, counts, independence section, summary table and these freeze blocks: D-P2a, E-CD-P1, CTC-1P/1B, CTC-2P, CTC-5B. Fixes made during the read:
  - (i) The Foundation product field said "opened … as announced". It now says the archive was announced to open and that availability was not verified.
  - (ii) The confusing phrase about the date of the Lyα update was reworded.
  - (iii) The CPL rows had been given the full-correlation covariance text by mistake. They now declare diag-only C_pred, because R04 did not save the chain cross-correlations.
  - (iv) The rows whose conditions are significance-type now carry an explicit two-valued pointer.
  - (v) Empty freeze fields in the retrospective and synthetic rows were filled with an explicit n/a.
  - (vi) The magnification response was added to the count-dipole contaminants.
- The predictive correlations are very high (|r| up to 0.999), as you would expect from 2–3 parameters. Any scorer must use the full C_pred or the dominant directions will be double-counted (handoff §3).
- Known limitations, not fixed:
  - Laplace (Gaussian) bands for wCDM and oΛCDM. FindMinimum::lstol warnings appeared at machine precision, but the minima reproduce R04 and R02 to <1e-8 in χ².
  - Compressed CMB priors outside flat ΛCDM.
  - The Gaussian approximation for CPL.
  - Equations in UNSUPPORTED_MODELS_R02 were written from standard forms, not checked against the opened papers.
- **Not done:** the post-06:00 ET Euclid archive and release-note check, and any independent check by a second reviewer.
