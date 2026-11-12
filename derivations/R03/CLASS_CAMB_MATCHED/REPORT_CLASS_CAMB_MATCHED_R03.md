# CLASS vs CAMB, matched massless ΛCDM baseline, plus attribution (R03 branch, recorded internally at the time)

Run on 2026-11-12, 10:19–10:26 UTC (05:19–05:26 ET). Run directory: `run_01/` (the first attempt; nothing was overwritten).
- **Protocol:** `source_inputs_8933784/unpacked/PROTOCOL.md` (sha256 1d7bb1ef…cc1b), followed as written.
- **Inputs:** read-only.
- **Constraints:** no installs, no edits to frozen files, nothing posted.
- **Scope:** this is a code-consistency diagnostic for stock linear ΛCDM. It is not a forecast, and not a test of any private model.

## 0. Input verification and duplicate check
| Item | sha256 | Result |
|---|---|---|
| INPUTS_RECEIPT.md | bb1a31d8fa5b90032d43e011dc282703eb9735a37ae10c428dfed236cb36cf14 | MATCH (bb1a31d8…cf14), and matches the `.sha256` file |
| CLASS_CAMB_Historical_Reconciliation_20261112_R02.zip | 5bb80738e2659a5f39a5167e2839a9a8d24748cf0246ab16255c44f4a2202f40 | MATCH (5bb80738…2f40) |
| MANIFEST_R02.json, 13 files | — | 13/13 MATCH |

Duplicate check (protocol §0):
- The receipt reports the October 26 matched package as absent. A box-wide search for `camb_class_corrected*` and `frl_tools` also found nothing.
- My earlier R03 CLASS check (r_d and distances) does not match this protocol.
- So a new run was needed.

## 1. Environment (protocol §0)
- **Python:** `/workspace/r05_cosmo_env/bin/python`, CPython 3.13.5 (binary sha 889c603f…97d9). Read-only use; no installs.
- **CAMB 2.0.5:** `camb/camblib.so` sha f6e0cfb59f919ad166e801306096a723d61c6e6b73a3e1135dd2a2096f5bffcf.
- **classy 3.4.2.0 (CLASS v3.4.2):** `_classy.cpython-313-x86_64-linux-gnu.so` sha cca6c26ffc2857e40eb7922dd604d087cda9ab2203f97bf081939b46ce383185.
- **Other packages:** numpy 2.5.4, scipy 1.18.1.
- **Source revision:** MISSING. These are pip wheels with no git revision.
- **Hardware:** 8-CPU Intel Xeon, 15 GB RAM, Linux 6.12.113. OMP_NUM_THREADS = 4.
- **Commands:** stored in `run_01/*.cmd`; start/end UTC times and exit status in `*.times`; stdout in `*.log`, stderr in `*.stderr`.
- **Parameter dumps:** the full CAMB parameter dump (`params_dump`, `str(CAMBparams)`) and the full CLASS dict passed plus classy's read-back are in each `run_01/runs/<run>.json`. Raw arrays, including the native grids, are in `runs/<run>.npz`.

## 2. Protocol vs the parent's / Coordinator's summary
Every value in the summary matches PROTOCOL.md:
- H0 67.5, ω_b 0.022, ω_cdm 0.12
- N_eff 3.044, all massless
- YHe 0.245 with BBN off; no reionization; RECFAST in both codes
- synchronous-gauge total matter
- z = 0, 1, 3; 201 points from 0.002 to 1/Mpc
- four runs, then one-at-a-time attribution

The summary leaves some things out. PROTOCOL.md adds:
- the 201-point grid is **logarithmic in physical k [1/Mpc]**, with P in Mpc³
- A_s 2e-9, n_s 0.965, pivot 0.05/Mpc, zero running, T_CMB 2.7255
- the exact 20-point geomspace for the historical comparison
- dense σ8 grids (12,001 and 24,001 log nodes from 1e-5 to 30/Mpc, plus truncation at 10/Mpc)
- the predeclared screens in §5

The parent's task also asked for distance and H(z) differences, which PROTOCOL.md does not require. I added them (§4). There is no conflict.

## 3. Settings actually used (read back, not just requested)
**CAMB:**
- `set_classes(recombination_model='Recfast')`. Read-back: Recfast with RECFAST_fudge 1.125, fudge_He 0.8472367977, Hswitch True, He_rate_correction True; Gaussian-correction parameters are in the json.
- `set_cosmology(H0=67.5, ombh2=0.022, omch2=0.12, omk=0, mnu=0, num_massive_neutrinos=0, nnu=3.044, standard_neutrino_neff=3.044, YHe=0.245, TCMB=2.7255)`.
- `Reion.Reionization=False` (read back False). InitPower is As 2e-9, ns 0.965, nrun 0, nrunrun 0, r 0, pivot 0.05. Dark energy w = −1, wa = 0. WantTensors False.
- `set_matter_power(redshifts=[3,1,0], kmax=30, k_per_logint=40|80, nonlinear=False)`, and NonLinear_none is read back.
- Transfer.kmax read back as 30.0. Transfer redshift order is [3, 1, 0], and z labels were mapped explicitly.
- Spectra come from `get_matter_power_interpolator(var1=var2='delta_tot', hubble_units=False, k_hunit=False, nonlinear=False)`.
- Native k range: 7.05e-6 to 30.34/Mpc (base) and 3.5e-6 to 30.17/Mpc (tight). That covers [1e-5, 30], so nothing was extrapolated.
- Accuracy: base AccuracyBoost/lAccuracyBoost/lSampleBoost = 1/1/1; tight = 2/2/2.

**CLASS:**
- The protocol dictionary, verbatim, including `recombination='RECFAST'`, `reio_parametrization='reio_none'`, `gauge='synchronous'`, `matter_source_in_current_gauge='yes'`, `P_k_max_1/Mpc=30`, plus the base or tight precision keys.
- classy 3.4.2 accepted every key. All seven precision keys were checked one at a time in `probe_params.*`, and CLASS errors on keys it does not read.
- Read-back:
  - Ω_m 0.3116598079561042, Ω_Λ 0.6882483931709501 (flat closure sum = 1.0), N_eff 3.044, YHe 0.245, tau_reio 0
  - no non_linear key, so the CLASS default is none
  - native k range 7.05e-6 to 30.54/Mpc
- Spectra come from `pk_lin(k, z)`, which is total matter in the current (synchronous) gauge.

**Not echoed:** RecFastCLASS's internal fudge parameters are not exposed by classy and are recorded as MISSING. They sit at the installed CLASS defaults. CAMB Recfast and RecFastCLASS are different algorithms, and §4 shows the x_e comparison.

**Matched densities:**
- Ω_r: CAMB 9.17987262e-5 vs CLASS 9.17988729e-5.
- Early ρ_ν/ρ_γ = 0.6913146750 in both.
- Ω_m is equal to all digits.

## 4. Baseline results, comparison grid (201 log points, 0.002 to 1/Mpc), relative P(k) difference
The full per-z, per-k table is `run_01/relative_differences_201.csv`; the spectra are in `run_01/comparison.csv`.

| Pair | z | max \|ΔP/P\| | RMS | mean signed | k at max [1/Mpc] |
|---|---|---|---|---|---|
| CAMB base/tight | 0 | 7.975e-04 | 2.314e-04 | -3.988e-05 | 0.03711 |
| CAMB base/tight | 1 | 7.975e-04 | 2.314e-04 | -3.986e-05 | 0.03711 |
| CAMB base/tight | 3 | 7.975e-04 | 2.313e-04 | -3.968e-05 | 0.03711 |
| CLASS base/tight | 0 | 1.665e-04 | 5.126e-05 | -2.844e-05 | 1 |
| CLASS base/tight | 1 | 1.665e-04 | 5.116e-05 | -2.751e-05 | 1 |
| CLASS base/tight | 3 | 1.665e-04 | 5.112e-05 | -2.722e-05 | 1 |
| cross base (CAMB/CLASS) | 0 | 7.088e-04 | 2.568e-04 | -8.042e-05 | 0.03711 |
| cross base (CAMB/CLASS) | 1 | 7.094e-04 | 2.575e-04 | -8.192e-05 | 0.03711 |
| cross base (CAMB/CLASS) | 3 | 7.100e-04 | 2.570e-04 | -8.254e-05 | 0.03711 |
| cross tight (CAMB/CLASS) | 0 | 8.764e-04 | 1.944e-04 | -6.896e-05 | 0.06493 |
| cross tight (CAMB/CLASS) | 1 | 8.773e-04 | 1.946e-04 | -6.955e-05 | 0.06493 |
| cross tight (CAMB/CLASS) | 3 | 8.777e-04 | 1.947e-04 | -7.007e-05 | 0.06493 |
| CAMB interp-only (k_per_logint 40->80) | 0 | 2.215e-04 | 1.711e-05 | 1.821e-06 | 0.01006 |
| CAMB interp-only (k_per_logint 40->80) | 1 | 2.214e-04 | 1.710e-05 | 1.816e-06 | 0.01006 |
| CAMB interp-only (k_per_logint 40->80) | 3 | 2.215e-04 | 1.710e-05 | 1.819e-06 | 0.01006 |
| CAMB integration-only (Boost 1->2 at k_per_logint 80) | 0 | 7.966e-04 | 2.308e-04 | -4.170e-05 | 0.03711 |
| CAMB integration-only (Boost 1->2 at k_per_logint 80) | 1 | 7.966e-04 | 2.308e-04 | -4.168e-05 | 0.03711 |
| CAMB integration-only (Boost 1->2 at k_per_logint 80) | 3 | 7.967e-04 | 2.307e-04 | -4.149e-05 | 0.03711 |
| CLASS interp-only (k_per_decade 40/70->80/140) | 0 | 6.147e-05 | 1.167e-05 | 3.422e-07 | 0.307 |
| CLASS interp-only (k_per_decade 40/70->80/140) | 1 | 6.147e-05 | 1.172e-05 | 3.253e-07 | 0.307 |
| CLASS interp-only (k_per_decade 40/70->80/140) | 3 | 6.147e-05 | 1.173e-05 | 3.210e-07 | 0.307 |
| CLASS integration-only (tols+l_max_ur+sigma_k at 80/140) | 0 | 1.532e-04 | 5.041e-05 | -2.878e-05 | 0.9694 |
| CLASS integration-only (tols+l_max_ur+sigma_k at 80/140) | 1 | 1.532e-04 | 5.029e-05 | -2.783e-05 | 0.9694 |
| CLASS integration-only (tols+l_max_ur+sigma_k at 80/140) | 3 | 1.532e-04 | 5.026e-05 | -2.754e-05 | 0.9694 |

**Tighter level (added because CAMB base/tight came to 0.080%, close to the 0.1% screen).** CAMB tighter is Boost 3/3/3 with k_per_logint 160; CLASS tighter uses tolerances 1e-12/1e-8/1e-7, k_per_decade 160/280, l_max_ur 68 and sigma_k 320. Both are retained as separate runs.

| Pair | z | max | RMS |
|---|---|---|---|
| CAMB tight/tighter | 0 | 9.492e-05 | 2.276e-05 |
| CAMB tight/tighter | 1 | 9.486e-05 | 2.275e-05 |
| CAMB tight/tighter | 3 | 9.498e-05 | 2.268e-05 |
| CLASS tight/tighter | 0 | 2.431e-05 | 4.026e-06 |
| CLASS tight/tighter | 1 | 2.432e-05 | 4.003e-06 |
| CLASS tight/tighter | 3 | 2.433e-05 | 4.007e-06 |
| cross tighter | 0 | 8.415e-04 | 1.998e-04 |
| cross tighter | 1 | 8.418e-04 | 1.999e-04 |
| cross tighter | 3 | 8.419e-04 | 2.000e-04 |
| cross tight | 0 | 8.764e-04 | 1.944e-04 |
| cross tight | 1 | 8.773e-04 | 1.946e-04 |
| cross tight | 3 | 8.777e-04 | 1.947e-04 |

How to read these:
- **Interpolation vs integration.** Interpolation-only changes (output-grid density) are ≤2.2e-4 for CAMB and ≤6.1e-5 for CLASS. The integration-accuracy change dominates the CAMB base/tight difference (8.0e-4 at the BAO scale, k ≈ 0.037).
- **Convergence.** CAMB tight-to-tighter is 9.5e-5; CLASS tight-to-tighter is 2.4e-5.
- **Cross-code.** The difference is about 0.084–0.088% at k ≈ 0.065 at all three z, and is stable under tightening. It is a code-level residual, not a convergence artefact. The October 26 ledger's figure (0.0863043%) is of the same size, but that run was not available for verification.

**σ8 (dense grids, R = 8/h Mpc, protocol checker `verify_spectra.py`, sha 32e1fccc…):**

| Run | z | σ8 integrated (12,001) | engine σ8 | integrated/engine − 1 | 24,001/12,001 − 1 | (k≤30)/(k≤10) − 1 | h-unit/physical − 1 |
|---|---|---|---|---|---|---|---|
| camb_base | 0 | 0.8059152719 | 0.8059152210 | 6.312e-08 | 7.545e-13 | 6.162e-08 | 0.000e+00 |
| camb_base | 1 | 0.4899208072 | 0.4899207774 | 6.074e-08 | 7.530e-13 | 6.162e-08 | 0.000e+00 |
| camb_base | 3 | 0.2548987322 | 0.2548987156 | 6.506e-08 | 7.458e-13 | 6.162e-08 | 0.000e+00 |
| camb_tight | 0 | 0.8059283579 | 0.8059284105 | -6.526e-08 | -4.617e-13 | 6.160e-08 | 0.000e+00 |
| camb_tight | 1 | 0.4899287679 | 0.4899287992 | -6.390e-08 | -4.440e-13 | 6.160e-08 | 0.000e+00 |
| camb_tight | 3 | 0.2549028715 | 0.2549028877 | -6.380e-08 | -4.055e-13 | 6.160e-08 | 0.000e+00 |
| class_base | 0 | 0.8059439210 | 0.8059442309 | -3.846e-07 | -4.174e-14 | 6.160e-08 | 0.000e+00 |
| class_base | 1 | 0.4899385864 | 0.4899387748 | -3.846e-07 | -4.408e-14 | 6.160e-08 | 0.000e+00 |
| class_base | 3 | 0.2549080573 | 0.2549081553 | -3.845e-07 | -4.419e-14 | 6.160e-08 | 0.000e+00 |
| class_tight | 0 | 0.8059537106 | 0.8059537139 | -4.112e-09 | -6.072e-13 | 6.163e-08 | 0.000e+00 |
| class_tight | 1 | 0.4899442665 | 0.4899442685 | -4.103e-09 | -6.148e-13 | 6.163e-08 | 0.000e+00 |
| class_tight | 3 | 0.2549109644 | 0.2549109654 | -4.103e-09 | -6.292e-13 | 6.163e-08 | 0.000e+00 |

Cross-code σ8, tight (CAMB/CLASS − 1, integrated): z=0: -3.146e-05, z=1: -3.163e-05, z=3: -3.175e-05. Tighter: z=0: -3.631e-05, z=1: -3.644e-05, z=3: -3.651e-05.

**Distances and H(z), CAMB/CLASS − 1, at z = 0.5, 1, 1.5, 2, 3 (H also at z = 0):**

| Pair | D_M max | D_M RMS | H max | H RMS | x_e max (z 200–5000) |
|---|---|---|---|---|---|
| cross base | 1.182e-09 | 5.491e-10 | 9.057e-10 | 5.222e-10 | 2.457e-03 |
| cross tight | 3.547e-10 | 2.403e-10 | 9.057e-10 | 5.222e-10 | 2.457e-03 |
| CAMB base/tight | 2.016e-10 | 9.014e-11 | 0.000e+00 | 0.000e+00 | 1.163e-05 |
| CLASS base/tight | 9.278e-10 | 4.933e-10 | 0.000e+00 | 0.000e+00 | 2.306e-06 |

The x_e difference between CAMB Recfast and RecFastCLASS is ≤8.6e-4 for z 200–1600, and −2.5e-3 at z = 2000 (He recombination). That is the expected difference between the two RECFAST variants.

## 5. Predeclared screens (PROTOCOL §3)
| Screen | Threshold | Result | Verdict |
|---|---|---|---|
| CAMB base/tight max \|P_b/P_t − 1\|, every z | < 0.1% | 0.0798% | **PASS** (margin 20%, hence the tighter level: tight/tighter 0.0095%) |
| CLASS base/tight, every z | < 0.1% | 0.0167% | **PASS** |
| Tight cross-code max \|P_CAMB/P_CLASS − 1\| | < 0.5% | 0.0878% (k 0.0649, CAMB low) | **PASS** |
| Integrated vs engine σ8 | < 0.1% | ≤ 3.846e-07 | **PASS** |
| Grid refinement (24,001 vs 12,001) | < 0.01% | ≤ 7.545e-13 | **PASS** |
| Tail (kmax 30 vs 10) | < 0.01% | ≤ 6.163e-08 | **PASS** |
| Physical vs h-unit invariance | 1e-10 | ≤ 0.000e+00 | **PASS** |
| Positivity, finiteness, grid range (checker) | — | `comparison_audit.json`: numerical_screen_pass true at z = 0, 1, 3; `sigma8_audit.json` and `sigma8_audit_24001.json` ran without error; `--self-test` PASS (7 checks) | **PASS** |

**Overall: all predeclared screens PASS.** As PROTOCOL.md says, this verifies only this bounded calculation; it says nothing about observations or a private cosmology.

## 6. Attribution, one change at a time (PROTOCOL §4), all at tight level, z = 0 shown (z = 1, 3 in json)
| Branch | Pair | max \|ΔP/P\| | RMS | mean signed | k at max | σ8 rel | Note |
|---|---|---|---|---|---|---|---|
| A0 matched baseline (tight) | camb_tight / class_tight | 8.764e-04 | 1.944e-04 | -6.896e-05 | 0.06493 | -3.146e-05 | reference |
| A1 CAMB mnu=0.06 (1 massive, Neff 3.044) vs CLASS massless | A1_camb_mnu006 / class_tight | 2.942e-02 | 2.424e-02 | -2.311e-02 | 1 | -1.420e-02 | deliberately unmatched; Omega_m changes to 0.313075 (CAMB readback), omnuh2 6.448994e-04 |
| A1 effect within CAMB (massive/massless) | A1_camb_mnu006 / camb_tight | 2.914e-02 | 2.416e-02 | -2.305e-02 | 1 | -1.417e-02 | pure neutrino-mass effect in one code |
| A2 matched massive: CAMB mnu=0.06 vs CLASS matched ncdm | A1_camb_mnu006 / A2_class_matched_massive | 1.079e-03 | 5.919e-04 | 4.837e-04 | 0.08588 | 3.407e-04 | CLASS N_ncdm=1, deg_ncdm=1.014667, T_ncdm=(4/11)^(1/3), N_ur=2.029333, omega_ncdm=CAMB omnuh2 |
| A3 CAMB BBN helium alone (YHe=0.245496) vs CAMB YHe=0.245 | A3_camb_bbn_YHe / camb_tight | 1.226e-05 | 3.878e-06 | 2.117e-06 | 0.1502 | 1.493e-06 | CAMB-internal effect of BBN helium |
| A3 CAMB BBN helium vs CLASS (YHe 0.245) | A3_camb_bbn_YHe / class_tight | 8.672e-04 | 1.924e-04 | -6.685e-05 | 0.06493 | -2.996e-05 |  |
| A3b CLASS HyRec vs CLASS RECFAST (CLASS-only; CAMB HyRec unavailable) | A3b_class_hyrec / class_tight | 3.139e-05 | 9.742e-06 | 3.648e-06 | 0.1327 | 2.179e-06 | not a same-family pair: CAMB build lacks HyRec |
| A4 CLASS matter_source_in_current_gauge default vs yes | A4_class_matter_source_default / class_tight | 6.665e-09 | 3.732e-09 | 2.549e-09 | 0.002 | 1.753e-10 | definition branch |
| A4 CAMB vs CLASS(default matter source) | camb_tight / A4_class_matter_source_default | 8.764e-04 | 1.944e-04 | -6.897e-05 | 0.06493 | -3.146e-05 |  |

**A2 read-back match.** This is required before comparing P(k). CAMB's actual convention is one massive eigenstate with degeneracy 1.014667, T_ν = (4/11)^(1/3) T_CMB, 2.029333 massless species, and ω_ν = 6.4489937542e-04. For CLASS I set:
- N_ncdm = 1, deg_ncdm = 1.014667, T_ncdm = (4/11)^(1/3)
- N_ur = 2.029333, omega_ncdm equal to CAMB's ω_ν

This is not a "CLASS N_ur = 2.044/2.0328" default. Read-back:
- late ω_ν relative difference -2.220e-16
- early ρ_ν/ρ_γ relative difference -1.121e-06
- Ω_m equal (0.3130752250)
- CLASS N_eff 3.0439966

Neutrino transfer settings: CAMB `accurate_massive_neutrino_transfers` was left at False, and CLASS's ncdm fluid approximation at its defaults. That is a residual numerical difference between the two codes. The matched-massive cross-code residual is 0.108% max.

**A3 BBN helium.** CAMB's BBN value is YHe = 0.2454957. Its effect within CAMB is ≤1.2e-5, which is negligible.

**A3b recombination.** I could not run a same-family HyRec branch: **the CAMB 2.0.5 build here raises `CAMBValueError('Class not found: HyRec')`**, and nothing was installed. CLASS HyRec vs RECFAST changes CLASS by ≤3.1e-5. This is a CLASS-only sensitivity, not a matched branch. Recombination was not needed, because the baseline passes.

**A4 gauge definition.** The CLASS default `matter_source_in_current_gauge` vs `yes` differs by ≤6.7e-9 here.

**A5 interpolation only** (the historical 200-point h-unit CAMB sampling, 1e-4 to 1.5 h/Mpc, converted with k = h·k_h and P = P_h/h³, then log-log interpolated, compared with direct evaluation from the same CAMB run): max 1.682e-03 on the 20-point grid and 3.142e-03 on the 201-point grid (k ≈ 0.137, BAO wiggles).

**Historical shape** (20 points, exact geomspace from 0.002 to 1; `run_01/attribution_historical_20pt.csv`):
- The source residual (from its rounded P values) has mean |Δ| 2.3012%.
- **A1 alone** (CAMB with 0.06 eV vs CLASS massless) gives mean |Δ| 2.2850%. Its deviation from the source shape is max 1.386e-03, RMS 5.208e-04.
- A1 moves Ω_m from 0.3116598 to 0.3130752 and changes σ8 by -1.4174%; the source reports −1.453%.

**A6 replay of the stated historical configuration with the CURRENT versions** (CAMB 2.0.5, which matches the source; classy 3.4.2 vs the source's 3.4.1). Settings are taken verbatim from `historical_report_text.md`: CAMB defaults plus H0/ombh2/omch2/As/ns, kmax 2, 200-point h-unit spectrum, log-log interpolation; CLASS with YHe 0.245 and P_k_max 2.
- **σ8 reproduced to all 16 printed digits:** CAMB 0.7941911366899833 vs the source's 0.7941911366899833, and CLASS 0.8059023437254481 vs 0.8059023437254481.
- **The 20 printed P values are reproduced** within ≤1.5e-4 (CAMB and CLASS), which is inside their 4-significant-figure rounding.
- **All 20 printed relative differences match at 4 d.p.**
- Mean 2.2980% and max 2.9986%, against the source's "mean 0.0230, max 0.0300".
- CAMB's effective defaults in that replay:
  - 1 massive ν with ω_ν 6.449e-4, N_eff 3.044 (2.029333 massless + 1.014667 massive). Note: the `nnu` field in the A6 json, 3.0293, is a labelling slip in my script (massless + integer count). The true value is 3.044.
  - YHe 0.2454957 from BBN; reionization on with optical_depth 0; Recfast.
  - Ω_m 0.3130752 vs CLASS 0.3116598.

**Attribution verdict, bounded:**
1. The matched massless baseline agrees to 0.088%.
2. Changing only the neutrino mass in CAMB (A1) reproduces the source's ~2.3% shape and amplitude to ≤0.14%.
3. The full stated configuration, replayed with current versions, reproduces the retained printed output, σ8 included, within rounding.

So **the historical 2–3% residual is explained by the unmatched massive-neutrino default** (CAMB 0.06 eV vs CLASS massless), with BBN helium contributing ~1e-5. It is not a solver defect. Two provenance limits remain: the original script and log bytes were not recovered, so their source hashes (4aec7a4f…, 151bdc8b…) are UNVERIFIED; and CLASS here is 3.4.2, not 3.4.1. The finding is therefore labelled "**current-version replay reproducing the retained output**", not an authenticated historical re-execution. Branch A4 (gauge) and the pivot, running and radiation branches were not warranted beyond A4, since the stated configuration uses the same pivot (0.05) and no running.

## 7. Blockers and missing provenance
- CAMB HyRec is not in this build, so the same-family HyRec sensitivity was not run (see A3b).
- CLASS RecFast internal fudge values, source git revisions, and the historical script/log bytes are MISSING.
- The October 26 matched package is still absent and was not authenticated.
- Nothing was installed, and no prior attempt was overwritten.
