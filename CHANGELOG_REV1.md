# CHANGELOG_REV1 — PUBLISH_20261112

Author: C.A.S.D.R

Written 2026-11-12, about 05:40 ET (America/Toronto). PRIVATE ONLY. Nothing was posted, uploaded, timestamped, emailed or shared. The v0 files in `/workspace/r03-out/euclid_forecast_bot/PUBLISH_20261112/` and that folder's `SHA256SUMS` were not modified. This REV1 set lives only in `PUBLISH_20261112/REV1/`.

## Sol/Astra review note (UNVERIFIED by us)

Per the Sol/Astra review, all 8 recomputed distance central values were reproduced independently and the CPL median pairs PASS (as reported by the reviewer, UNVERIFIED by us).

## 1. wCDM w, with the branch named, and Ωk PRIMARY width

- Added a **model-context** section (not new scored prediction items). wCDM and Ωk appear in R03 as conditional-fit parameters of the CTC-3 / CTC-4 distance curves, not as separate prospective rows.
- **wCDM, FROZEN PRIMARY (CTC-3P-R03):** w = −1.028 ± 0.042. **wCDM, DECLARED REPLACEMENT (CTC-3B-R03):** w = −1.027 ± 0.042. The same figures, with the branch named, were added on the CTC-3P-R03 and CTC-3B-R03 model lines and on the corresponding X posts.
- Verified against `R03/RECOMPUTED_ROWS_R03.csv` (Laplace w −1.02805 ± 0.04219 PRIMARY; −1.02695 ± 0.04234 REPLACEMENT), `R03/wolfram/fullrs_fits_R03.json`, and `R03/calc/fullrs_r03_output.json`. The displayed values are the csv Laplace figures rounded as requested. No mismatch requiring a silent overwrite.
- **Flag (not overwritten):** R03 MCMC medians differ (PRIMARY −1.0312, s.d. 0.0405; REPLACEMENT −1.0291, s.d. 0.0413). `W_RECONCILE_R03.md` records the Laplace vs MCMC width difference. REV1 keeps the Laplace display values and lists the MCMC figures in the model-context section and in SOURCES.
- **Ωk, FROZEN PRIMARY (CTC-4P-R03):** shown as +0.00199 ± 0.00125, because the width sits on a 4-decimal rounding boundary. Unrounded Wolfram Laplace width: **0.001253061073170205** (central value 0.0019908057850397567) from `R03/wolfram/fullrs_fits_R03.json`. The csv already printed 0.00199 ± 0.00125. REPLACEMENT Ωk +0.00198 ± 0.00124 is listed for branch completeness (unrounded width 0.0012407872583701455). The CTC-4 model lines and X posts carry the same figures.

## 2. Release framing

Euclid DR1-Foundation (12 November 2026) only timestamps these forecasts. The galaxy-clustering and weak-lensing products needed for the strongest tests are scheduled for mid-2027 (DR1 Complete). Today's Foundation release does not supply those measurements.

Wording changes (each one):

- **PREDICTIONS header.** Replaced the v0 status line that led with “before the announced Euclid DR1-Foundation opening at 06:00 ET.” REV1 status identifies this as a PRIVATE DRAFT (REV1) and states that v0 was not modified. Added a dedicated **Release framing** paragraph with the timestamp-only / mid-2027 clustering and lensing language.
- **PREDICTIONS “How to read this pack” Foundation bullet.** Rewritten so Foundation only timestamps the forecasts; it does not supply galaxy-clustering or weak-lensing measurements; those products are scheduled for DR1 Complete (mid-2027); distance curves are for a later BAO measurement, not for today's Foundation release.
- **E-CD-P2, E-CD-P3 and E-PHZ-1 product lines.** Reworded from language that could be read as Foundation supplying the test today, to: if scored, Foundation catalogues; Foundation only timestamps the forecast and does not complete the test; not a galaxy-clustering or weak-lensing product.
- **E-CD-P2, E-CD-P3 and E-PHZ-1 notes.** Removed “Foundation-testable in principle.” Replaced with catalogue-level / method wording and the timestamp-only / mid-2027 caveat.
- **METADATA abstract and notes.** Abstract now opens with the timestamp-only sentence and states that galaxy-clustering and weak-lensing products for the strongest tests are scheduled for mid-2027 (DR1 Complete) and that today's Foundation release does not supply those measurements. Notes updated the same way.
- **ZENODO json description, notes, and draft note.** Same release-framing sentences as the metadata abstract. Version string set to PUBLISH_20261112_REV1.
- **X post 1/35.** Rewritten to say Foundation (12 Nov 2026) only timestamps these forecasts, and that galaxy clustering and weak lensing for the strongest tests are due mid-2027 (DR1 Complete). Posts 33–35 (E-CD-P2, E-CD-P3, E-PHZ-1) were reworded in the same sense. No re-split of the CTC pairs was required; numbering stays 1/35–35/35.
- **Assembly note.** Path now points at `PUBLISH_20261112/REV1/`. States that v0 and its SHA256SUMS were left untouched.
- **SOURCES.** Added a REV1 verification table for wCDM w and Ωk, including unrounded values and the MCMC flag.

Distance-curve product lines already said “DR1 Complete (mid-2027 or later). NOT Foundation” and were left in that form.

## What was not changed

- Author remains C.A.S.D.R.
- No v0 file and no v0 SHA256SUMS entry was edited.
- Frozen R01/R02/R03 sources were not edited.
- No posting, upload, or external timestamp.
- Ranked prediction set (24 items) and the CTC DM/rd–DH/rd split in the X thread are unchanged, except for the added branch-labelled w and Ωk context and the release-framing wording above.
