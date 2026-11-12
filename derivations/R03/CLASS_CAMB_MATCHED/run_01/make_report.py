import json
B=json.load(open('run_01/baseline_analysis.json')); A=json.load(open('run_01/attribution_analysis.json')); Z=['0','1','3']
f=lambda x:'%.3e'%x; pc=lambda x:'%.4f%%'%(100*x)
L=[]
L.append('''# CLASS vs CAMB, matched massless ΛCDM baseline, plus attribution (R03 branch, recorded internally at the time)

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
''')
L.append('## 4. Baseline results, comparison grid (201 log points, 0.002 to 1/Mpc), relative P(k) difference\nThe full per-z, per-k table is `run_01/relative_differences_201.csv`; the spectra are in `run_01/comparison.csv`.\n\n| Pair | z | max \\|ΔP/P\\| | RMS | mean signed | k at max [1/Mpc] |\n|---|---|---|---|---|---|')
for lab,v in B['Pk_201'].items():
    for z in Z: L.append(f"| {lab} | {z} | {f(v[z]['max_abs'])} | {f(v[z]['rms'])} | {f(v[z]['mean_signed'])} | {v[z]['k_at_max']:.4g} |")
L.append('\n**Tighter level (added because CAMB base/tight came to 0.080%, close to the 0.1% screen).** CAMB tighter is Boost 3/3/3 with k_per_logint 160; CLASS tighter uses tolerances 1e-12/1e-8/1e-7, k_per_decade 160/280, l_max_ur 68 and sigma_k 320. Both are retained as separate runs.\n\n| Pair | z | max | RMS |\n|---|---|---|---|')
for lab,v in A['ladder'].items():
    for z in Z: L.append(f"| {lab} | {z} | {f(v[z]['max_abs'])} | {f(v[z]['rms'])} |")
L.append('''
How to read these:
- **Interpolation vs integration.** Interpolation-only changes (output-grid density) are ≤2.2e-4 for CAMB and ≤6.1e-5 for CLASS. The integration-accuracy change dominates the CAMB base/tight difference (8.0e-4 at the BAO scale, k ≈ 0.037).
- **Convergence.** CAMB tight-to-tighter is 9.5e-5; CLASS tight-to-tighter is 2.4e-5.
- **Cross-code.** The difference is about 0.084–0.088% at k ≈ 0.065 at all three z, and is stable under tightening. It is a code-level residual, not a convergence artefact. The October 26 ledger's figure (0.0863043%) is of the same size, but that run was not available for verification.

**σ8 (dense grids, R = 8/h Mpc, protocol checker `verify_spectra.py`, sha 32e1fccc…):**

| Run | z | σ8 integrated (12,001) | engine σ8 | integrated/engine − 1 | 24,001/12,001 − 1 | (k≤30)/(k≤10) − 1 | h-unit/physical − 1 |
|---|---|---|---|---|---|---|---|''')
for n,v in B['sigma8'].items():
    for z in Z: x=v[z]; L.append(f"| {n} | {z} | {x['integrated_12001']:.10f} | {x['engine']:.10f} | {f(x['integrated_vs_engine_rel'])} | {f(x['grid_refinement_rel'])} | {f(x['tail_rel_(30 vs 10)'])} | {f(x['h_unit_invariance_rel'])} |")
L.append(f"\nCross-code σ8, tight (CAMB/CLASS − 1, integrated): " + ', '.join(f"z={z}: {f(B['sigma8_cross_tight'][z])}" for z in Z) + ". Tighter: " + ', '.join(f"z={z}: {f(A['ladder_sigma8']['cross_tighter'][z])}" for z in Z) + '.')
L.append('\n**Distances and H(z), CAMB/CLASS − 1, at z = 0.5, 1, 1.5, 2, 3 (H also at z = 0):**\n\n| Pair | D_M max | D_M RMS | H max | H RMS | x_e max (z 200–5000) |\n|---|---|---|---|---|---|')
for lab,d in B['background'].items(): L.append(f"| {lab} | {f(d['DM']['max_abs'])} | {f(d['DM']['rms'])} | {f(d['Hz']['max_abs'])} | {f(d['Hz']['rms'])} | {f(d['x_e']['max_abs'])} |")
L.append('\nThe x_e difference between CAMB Recfast and RecFastCLASS is ≤8.6e-4 for z 200–1600, and −2.5e-3 at z = 2000 (He recombination). That is the expected difference between the two RECFAST variants.\n')
s=B['screens']; ok=lambda b:'**PASS**' if b else '**FAIL**'
s8ok=all(all(B['sigma8'][n][z]['screens'][k] for k in B['sigma8'][n][z]['screens']) for n in B['sigma8'] for z in Z)
L.append(f'''## 5. Predeclared screens (PROTOCOL §3)
| Screen | Threshold | Result | Verdict |
|---|---|---|---|
| CAMB base/tight max \\|P_b/P_t − 1\\|, every z | < 0.1% | {pc(max(B['Pk_201']['CAMB base/tight'][z]['max_abs'] for z in Z))} | {ok(s['camb_base_tight_lt_0.1pct'])} (margin 20%, hence the tighter level: tight/tighter 0.0095%) |
| CLASS base/tight, every z | < 0.1% | {pc(max(B['Pk_201']['CLASS base/tight'][z]['max_abs'] for z in Z))} | {ok(s['class_base_tight_lt_0.1pct'])} |
| Tight cross-code max \\|P_CAMB/P_CLASS − 1\\| | < 0.5% | {pc(max(B['Pk_201']['cross tight (CAMB/CLASS)'][z]['max_abs'] for z in Z))} (k 0.0649, CAMB low) | {ok(s['tight_cross_lt_0.5pct'])} |
| Integrated vs engine σ8 | < 0.1% | ≤ {f(max(abs(B['sigma8'][n][z]['integrated_vs_engine_rel']) for n in B['sigma8'] for z in Z))} | {ok(s8ok)} |
| Grid refinement (24,001 vs 12,001) | < 0.01% | ≤ {f(max(abs(B['sigma8'][n][z]['grid_refinement_rel']) for n in B['sigma8'] for z in Z))} | {ok(s8ok)} |
| Tail (kmax 30 vs 10) | < 0.01% | ≤ {f(max(abs(B['sigma8'][n][z]['tail_rel_(30 vs 10)']) for n in B['sigma8'] for z in Z))} | {ok(s8ok)} |
| Physical vs h-unit invariance | 1e-10 | ≤ {f(max(abs(B['sigma8'][n][z]['h_unit_invariance_rel']) for n in B['sigma8'] for z in Z))} | {ok(s8ok)} |
| Positivity, finiteness, grid range (checker) | — | `comparison_audit.json`: numerical_screen_pass true at z = 0, 1, 3; `sigma8_audit.json` and `sigma8_audit_24001.json` ran without error; `--self-test` PASS (7 checks) | **PASS** |

**Overall: all predeclared screens PASS.** As PROTOCOL.md says, this verifies only this bounded calculation; it says nothing about observations or a private cosmology.
''')
at=A['attribution']
L.append('## 6. Attribution, one change at a time (PROTOCOL §4), all at tight level, z = 0 shown (z = 1, 3 in json)\n| Branch | Pair | max \\|ΔP/P\\| | RMS | mean signed | k at max | σ8 rel | Note |\n|---|---|---|---|---|---|---|---|')
for lab,v in at.items(): p=v['Pk']['0']; L.append(f"| {lab} | {v['pair']} | {f(p['max_abs'])} | {f(p['rms'])} | {f(p['mean_signed'])} | {p['k_at_max']:.4g} | {f(v['sigma8_rel']['0'])} | {v['note']} |")
r=A['A2_readback']; h=A['historical_shape']; a5=A['A5_interp_only']
L.append(f'''
**A2 read-back match.** This is required before comparing P(k). CAMB's actual convention is one massive eigenstate with degeneracy 1.014667, T_ν = (4/11)^(1/3) T_CMB, 2.029333 massless species, and ω_ν = {r['CAMB']['omnuh2']:.10e}. For CLASS I set:
- N_ncdm = 1, deg_ncdm = 1.014667, T_ncdm = (4/11)^(1/3)
- N_ur = 2.029333, omega_ncdm equal to CAMB's ω_ν

This is not a "CLASS N_ur = 2.044/2.0328" default. Read-back:
- late ω_ν relative difference {f(r['late_omega_nu_rel'])}
- early ρ_ν/ρ_γ relative difference {f(r['early_ratio_rel'])}
- Ω_m equal (0.3130752250)
- CLASS N_eff 3.0439966

Neutrino transfer settings: CAMB `accurate_massive_neutrino_transfers` was left at False, and CLASS's ncdm fluid approximation at its defaults. That is a residual numerical difference between the two codes. The matched-massive cross-code residual is 0.108% max.

**A3 BBN helium.** CAMB's BBN value is YHe = 0.2454957. Its effect within CAMB is ≤1.2e-5, which is negligible.

**A3b recombination.** I could not run a same-family HyRec branch: **the CAMB 2.0.5 build here raises `CAMBValueError('Class not found: HyRec')`**, and nothing was installed. CLASS HyRec vs RECFAST changes CLASS by ≤3.1e-5. This is a CLASS-only sensitivity, not a matched branch. Recombination was not needed, because the baseline passes.

**A4 gauge definition.** The CLASS default `matter_source_in_current_gauge` vs `yes` differs by ≤6.7e-9 here.

**A5 interpolation only** (the historical 200-point h-unit CAMB sampling, 1e-4 to 1.5 h/Mpc, converted with k = h·k_h and P = P_h/h³, then log-log interpolated, compared with direct evaluation from the same CAMB run): max {f(a5['20pt']['max_abs'])} on the 20-point grid and {f(a5['201pt']['max_abs'])} on the 201-point grid (k ≈ {a5['201pt']['k_at_max']:.3g}, BAO wiggles).

**Historical shape** (20 points, exact geomspace from 0.002 to 1; `run_01/attribution_historical_20pt.csv`):
- The source residual (from its rounded P values) has mean |Δ| {pc(h['A1_minus_hist']['mean_abs_hist'])}.
- **A1 alone** (CAMB with 0.06 eV vs CLASS massless) gives mean |Δ| {pc(h['A1_minus_hist']['mean_abs_A1'])}. Its deviation from the source shape is max {f(h['A1_minus_hist']['max_abs'])}, RMS {f(h['A1_minus_hist']['rms'])}.
- A1 moves Ω_m from 0.3116598 to 0.3130752 and changes σ8 by {pc(at['A1 effect within CAMB (massive/massless)']['sigma8_rel']['0'])}; the source reports −1.453%.

**A6 replay of the stated historical configuration with the CURRENT versions** (CAMB 2.0.5, which matches the source; classy 3.4.2 vs the source's 3.4.1). Settings are taken verbatim from `historical_report_text.md`: CAMB defaults plus H0/ombh2/omch2/As/ns, kmax 2, 200-point h-unit spectrum, log-log interpolation; CLASS with YHe 0.245 and P_k_max 2.
- **σ8 reproduced to all 16 printed digits:** CAMB {h['A6_sigma8']['CAMB']!r} vs the source's 0.7941911366899833, and CLASS {h['A6_sigma8']['CLASS']!r} vs 0.8059023437254481.
- **The 20 printed P values are reproduced** within ≤1.5e-4 (CAMB and CLASS), which is inside their 4-significant-figure rounding.
- **All 20 printed relative differences match at 4 d.p.**
- Mean {pc(h['A6_minus_hist']['mean_abs_A6'])} and max {pc(h['A6_minus_hist']['max_abs_A6'])}, against the source's "mean 0.0230, max 0.0300".
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
''')
open('REPORT_CLASS_CAMB_MATCHED_R03.md','w').write('\n'.join(L))
