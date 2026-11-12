# CHANGELOG_REV3

**Author:** C.A.S.D.R
**Written:** 2026-11-12, America/Toronto (UTC−5). Built from REV2. REV1 and REV2 files are unchanged and remain as frozen originals.

## What REV3 supersedes

REV3 supersedes **every BAO + compressed-CMB row and every number derived from a BAO + compressed-CMB fit** in REV1 and REV2:

- Distance curves CTC-2P/2B, CTC-3P/3B, CTC-4P/4B, CTC-5P/5B (the "-R03" rows of REV2) → replaced by the "-REV3" rows.
- Model-context parameters: wCDM w (both branches), oΛCDM Ωk (both branches), CPL Ωm, h, w0, wa and ω_b (both branches).
- Growth numbers (σ8, S8, fσ8), which were held in REV2 → now published as GR-1B-REV3 and GR-5B-REV3.

**Not superseded:** BAO-only curves CTC-1P and CTC-1B (no CMB prior; carried over unchanged), and the D-P, E-CD and E-PHZ rows (not BAO + CMB fits; carried over unchanged, with NOT READY rows still NOT READY).

## 1. Blocking fix — compressed CMB prior calibration

Control: at the Planck 2018 mean (Ωm 0.3166, h 0.6727, ω_b 0.02236), the model l_A should reproduce the prior mean 301.4707 (Chen, Huang & Wang 2019, arXiv:1808.05724), and a prior-only flat-ΛCDM fit should return H0 ≈ 67.27 and Ωm h² ≈ 0.1432.

| CMB convention | l_A at Planck mean | R at Planck mean | prior-only H0 | prior-only Ωm h² | control |
|---|---|---|---|---|---|
| old | 302.2408 | 1.75034 | 67.651 | 0.14473 | FAIL |
| chen_zHS | 301.7938 | 1.75039 | 67.442 | 0.14385 | FAIL |
| chen_zfix | 301.4148 | 1.75034 | 67.256 | 0.14313 | FAIL |
| rescale | 301.4707 | 1.75034 | 67.282 | 0.14323 | PASS |

Tolerance: |lA-301.4707|<0.02 (0.22 prior sd), |H0-67.27|<0.12, |omh2-0.1432|<0.00026 (about 0.2 Planck 2018 sd each).

- `old` = REV2 behaviour (Hu–Sugiyama z* = 1091.94, photons + 3.046 massless ν). **Before: l_A = 302.2408; FAIL.**
- `chen_zHS` / `chen_zfix` = Chen et al. radiation convention Ω_r = Ωm/(1+z_eq), z_eq = 2.5×10⁴ Ωm h² (T/2.7)⁻⁴, with Hu–Sugiyama z* or z* = 1089.9. The z* = 1089.9 variant gets H0 and Ωm h² within tolerance but leaves l_A 0.056 low (about 0.6 of the prior's l_A width), so it is kept as a cross-check only.
- `rescale` = model l_A × 0.997452 (Fable's fallback). **After: l_A = 301.4707, H0 = 67.282, Ωm h² = 0.14323; PASS.** This is the convention adopted for all REV3 numbers.
- Sensitivity: the `chen_zfix` re-run of the REPLACEMENT rows moves ΛCDM DM/rd by at most 0.0023 and wCDM w by 0.0014 from the adopted numbers (`rows_rev3_chen_zfix.json`).

## 2. Re-runs with the calibrated prior (all rows using the CMB prior)

Median shifts of the distance curves, REV3 − REV2, at z = 0.9 / 1.2 / 1.5 / 1.8:

| Row | Branch | Model | ΔDM/rd | ΔDH/rd |
|---|---|---|---|---|
| CTC-2B | REPLACEMENT | LCDM | +0.0123 / +0.0227 / +0.0331 / +0.0429 | +0.0337 / +0.0352 / +0.0337 / +0.0312 |
| CTC-2P | PRIMARY | LCDM | +0.0125 / +0.0230 / +0.0334 / +0.0431 | +0.0339 / +0.0351 / +0.0338 / +0.0312 |
| CTC-3B | REPLACEMENT | wCDM | +0.0143 / +0.0250 / +0.0351 / +0.0445 | +0.0333 / +0.0345 / +0.0333 / +0.0311 |
| CTC-3P | PRIMARY | wCDM | +0.0121 / +0.0231 / +0.0341 / +0.0439 | +0.0349 / +0.0363 / +0.0349 / +0.0323 |
| CTC-4B | REPLACEMENT | oLCDM | -0.0025 / +0.0025 / +0.0083 / +0.0143 | +0.0110 / +0.0141 / +0.0151 / +0.0149 |
| CTC-4P | PRIMARY | oLCDM | -0.0039 / +0.0011 / +0.0065 / +0.0127 | +0.0106 / +0.0142 / +0.0150 / +0.0147 |
| CTC-5B | REPLACEMENT | CPL | +0.0149 / +0.0226 / +0.0326 / +0.0434 | +0.0196 / +0.0320 / +0.0345 / +0.0334 |
| CTC-5P | PRIMARY | CPL | +0.0083 / +0.0156 / +0.0244 / +0.0352 | +0.0161 / +0.0318 / +0.0349 / +0.0342 |

Parameter shifts, REV3 − REV2: wCDM w +0.0029 (REPLACEMENT), +0.0026 (PRIMARY), in line with Fable's expected ~0.003; CPL REPLACEMENT w0 +0.019, wa −0.047; CPL PRIMARY w0 +0.025, wa −0.051 (each under 0.1 of its 68% width, in line with Fable's expectation); oΛCDM Ωk +0.0007 on both branches (width unchanged at about 0.0012).

Growth (like-for-like with the R03 growth script: CAMB, massless ν, A_s marginalised), shift of medians vs R03: ΛCDM sigma8_0 -0.0093, S8_0 -0.0137, fsigma8_0.9 -0.0052, fsigma8_1.2 -0.0044, fsigma8_1.3 -0.0042, fsigma8_1.5 -0.0038, fsigma8_1.8 -0.0034; CPL sigma8_0 -0.0079, S8_0 -0.0147, fsigma8_0.9 -0.0057, fsigma8_1.2 -0.0058, fsigma8_1.3 -0.0057, fsigma8_1.5 -0.0049, fsigma8_1.8 -0.0038.

ΛCDM, wCDM and oΛCDM distance widths are now MCMC standard deviations rather than Laplace. CPL bands are 68% only, with two decimals.

## 3. Write-up fixes (Fable 5.2)

1. **DM/DH label swap.** The hand-off text listed the Eq. 26 Lyα point as "DM/rd 8.600, DH/rd 39.32". The correct labels are DM/rd 39.32 ± 0.33 and DH/rd 8.600 ± 0.066 (ρ +0.225). The fit data vector was always correct (index 11 = DH, index 12 = DM in the DESI mean-file order).
2. **Old r_d.** The old truncated-r_s REPLACEMENT best fit gives r_d = 143.41 Mpc from the fitting formula (143.42 on PRIMARY), not 144.0 as stated in the R03 HELD table and hand-off.
3. **z = 1.3 labels checked.** From `R03/calc/fullrs_r03_output.json` (flat ΛCDM, old/new − 1): PRIMARY DH/rd −1.888%, DM/DH +1.199%, DM/rd −0.711%; REPLACEMENT DH/rd −1.891%, DM/DH +1.150%, DM/rd −0.762%. Labels are correct as published. The separate "+2.06% / +0.56% / −1.46%" figures are CPL PRIMARY median shifts (new/old − 1), not ΛCDM.
4. **"Effective rank 5" restated.** The 8×8 predictive correlation matrices have two (ΛCDM, oΛCDM), two plus one small (wCDM) and three plus one small (CPL) non-negligible eigen-directions. The curves carry three to four informative directions at most, not five.
5. **CPL prior-edge note.** wa < −3.5 in 0.88% (REPLACEMENT) and 1.90% (PRIMARY) of samples; w0 + wa < 0 imposed. 68% bands only.
6. **Ωk magnitude not robust.** Stated in the pack.
7. **Neutrino variant as a systematic.** One 0.06 eV state instead of massless: DM/rd and DH/rd about −0.11% (CAMB r_drag 147.53 vs 147.36 Mpc at the ΛCDM best fit); σ8 about −0.014 at fixed A_s.

No significance-type wording was added. HSU, STO, Rebound and R1 remain derivation-gated and excluded.

## 4. Comparison with Fable 5.2's independent numbers

See the status table in PREDICTIONS_20261112_REV3.md. Flat ΛCDM REPLACEMENT: PASS (max |Δ| 0.0074 in DM/rd, 0.0019 in DH/rd; Ωm +0.0004, h −0.0004 at best fit). σ8 0.817 vs 0.817 and S8 0.819 vs 0.818: PASS. Rows without a Fable number are marked "RECOMPUTED; Fable comparison NOT_RUN".

## Files

`PREDICTIONS_20261112_REV3.md` / `.pdf`, `CHANGELOG_REV3.md`, `STATUS_REV3.csv`, `ZENODO_METADATA_20261112_REV3.json`, `calc/` (scripts and JSON outputs), `SHA256SUMS` and OpenTimestamps proofs (`*.ots`).
