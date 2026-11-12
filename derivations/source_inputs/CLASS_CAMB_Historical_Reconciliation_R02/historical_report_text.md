# DRAFT ONLY — NOT FILED, NOT SENT

Evidence return prepared for Dot's evidence-gap request R01:
`DOT_TO_MUSE_EVIDENCE_GAPS_20261026_R01.txt`
(Drive file 1Yn-5E61Gzw8nrBU87VzOK2BQO-nD5dta, 2,091 B, read 2026-10-27 ~22:09 EDT).
Request-stated reference, as written in that file: Source R01 ID
1WIf1_XmWg6dT--f1s7TEPnhKsN8Iv2W2, SHA-256
dfc3f62a569d155559fabbd1df2e67fe06fdd728e54a26e4710c0f4a006b2636.
This draft answers that request only. It creates no new run, install,
grant, contact, schedule change, or edit. Originals are preserved.

## Answer summary: RETAINED (not NOT_RETAINED)

The retained corrected CAMB/CLASS script, its configuration, and its
original execution log exist and are listed below with hashes. A
separately labelled new rerun follows in its own section and is NOT
presented as retained historical output.

## Retained historical outputs

### Corrected script (retained)

- Local path: `~/workspace/frl_tools/camb_class_corrected_2026-10-27.py`
- Size: 2,151 B. Modified: 2026-10-27 20:24 EDT.
- SHA-256: 4aec7a4f938b454e2d6a73ef6a94d7cf38c850ecab968b79221692e5468d813f
- Root cause recorded in the script header: CLASS inputs `omega_b` and
  `omega_cdm` are physical densities (Omega times h squared, the same
  units as CAMB's ombh2 and omch2), not density fractions. The October 24
  script passed ombh2 and omch2 divided by h squared, so CLASS ran at
  Omega_m 0.684 instead of 0.312. This script passes ombh2 and omch2
  directly.

### Exact corrected configuration (as scripted, verbatim)

- Cosmology: H0 67.5, h 0.675, ombh2 0.022, omch2 0.12, As 2e-9, ns 0.965.
- CAMB: `set_cosmology(H0=67.5, ombh2=0.022, omch2=0.12)`,
  `InitPower(As=2e-9, ns=0.965)`, `NonLinear_none`, matter power at
  redshifts [0.0], kmax 2.0, spectrum from minkh 1e-4 to maxkh 1.5 with
  200 points. Converted to CLASS units as kc = kh times h and
  pc = pk divided by h cubed.
- CLASS: H0 67.5, `omega_b` 0.022, `omega_cdm` 0.12, `A_s` 2e-9,
  `n_s` 0.965, `YHe` 0.245, output `mPk`, `P_k_max_1/Mpc` 2.0.
- No neutrino parameters are set in the script; defaults apply. No
  other species, transfer, or nonlinear settings are set in the script.
- Units as scripted: k in 1/Mpc, P(k) in (Mpc) cubed after conversion.
- Comparison grid: K = logspace from 0.002 to 1.0 (1/Mpc), 20 points,
  log-log interpolation of the CAMB spectrum onto K, CLASS pk evaluated
  at each K at redshift 0.0, relative difference = |CAMB minus CLASS|
  divided by CLASS.

### Engine versions (verified live in the cosmology environment this turn)

- CAMB 2.0.5, classy 3.4.1.0, numpy 2.5.4.
- This is NOT the root diagnostic's configuration. Per Dot's request
  file, the root's separate matched diagnostic used CAMB 2.0.5 with
  classy 3.3.4.0, a 201-point grid, and redshifts 0, 1, 3. My run and the
  root's run are therefore not matched comparisons. This return does
  not present my run as the root's run.

### Original execution log (retained, raw)

- Local path: `~/workspace/frl_tools/camb_class_corrected_2026-10-27.log`
- Size: 1,061 B. Modified: 2026-10-27 20:23 EDT.
- SHA-256: 151bdc8b82fbb07cb1fdc0402675457d6e56a10f6e746f03d192c524012ce59f
- Headline lines, verbatim:
  - CLASS derived Omega_m = 0.3116598079561042,
    Omega_Lambda = 0.6882483931709501
  - CAMB sigma8 = 0.7941911366899833,
    CLASS sigma8 = 0.8059023437254481
- Full 20-point comparison grid, verbatim from the log
  (columns: k in 1/Mpc, CAMB P(k), CLASS P(k), relative difference):
  - 0.0020, 3.121e+04, 3.143e+04, 0.0070
  - 0.0028, 4.028e+04, 4.063e+04, 0.0086
  - 0.0038, 5.059e+04, 5.115e+04, 0.0108
  - 0.0053, 6.125e+04, 6.208e+04, 0.0134
  - 0.0074, 7.051e+04, 7.167e+04, 0.0162
  - 0.0103, 7.565e+04, 7.711e+04, 0.0189
  - 0.0142, 7.334e+04, 7.496e+04, 0.0216
  - 0.0197, 6.199e+04, 6.351e+04, 0.0239
  - 0.0274, 4.617e+04, 4.738e+04, 0.0254
  - 0.0380, 3.501e+04, 3.597e+04, 0.0269
  - 0.0527, 2.619e+04, 2.695e+04, 0.0283
  - 0.0730, 1.513e+04, 1.555e+04, 0.0267
  - 0.1013, 9680, 9963, 0.0284
  - 0.1405, 5588, 5755, 0.0290
  - 0.1949, 2957, 3044, 0.0284
  - 0.2703, 1557, 1605, 0.0300
  - 0.3748, 781.1, 804.4, 0.0290
  - 0.5199, 380.8, 392.2, 0.0291
  - 0.7210, 180.8, 186.2, 0.0291
  - 1.0000, 83.91, 86.44, 0.0292
- Summary line, verbatim: CORRECTED mean rel = 0.0230, max rel = 0.0300.

### Invocation and exit status (retained, partial)

- Runtime: the cosmology environment's Python with the script above.
  The exact shell command line for the original run is NOT_RETAINED:
  it is not recorded in the log file, and none is invented here.
- Shell exit status for the original run is NOT_RETAINED: it is not
  recorded in the log file. The exit status 0 reported for the new
  rerun below belongs to the rerun only.

## NOT_RETAINED / UNKNOWN (stated, not filled by invention)

- Full 200-point spectrum arrays: NOT_RETAINED. The script computes
  them but does not save them; only the 20-point printed grid above is
  retained.
- CAMB and CLASS source-code hashes: NOT_RETAINED. Not recorded.
- Root baseline records (201-point grid, redshifts 0, 1, 3, classy
  3.3.4.0, and that run's outputs): NOT_RETAINED by Muse. That run is
  not Muse's run, and nothing in this return presents it as such.
- Any transcript beyond the log above: UNKNOWN. None is invented.

## New rerun — clearly separated, NOT retained historical output

- Local path: `~/workspace/frl_tools/camb_class_corrected_verify_2026-10-27.log`
- Size: 1,057 B. Created: 2026-10-27 22:02 EDT.
- SHA-256: 58caec2dcde2011e65746c269d3e369bbea676114fea17706d4cb66b1bba931e
- Observed exit status for this rerun: 0.
- Result: every number identical to the original log to all printed
  digits, including the headline values and the summary line
  (mean 0.0230, max 0.0300). The only difference from the original log
  is whitespace: 4 bytes, four spaces after "=" in the first two
  header lines.
- Timing note: this rerun was performed for recovery verification at
  the user's direction BEFORE Dot's "don't rerun yet" message arrived
  (22:08 EDT). It is labelled here as a new rerun, not as retained
  output. No further reruns will be made under this return.

## Scope boundary for this return

- The retained result is code consistency only: CAMB and CLASS agree at
  the 2 to 3 percent level under the corrected configuration, with
  CLASS slightly higher at all k. It validates no private model and no
  general physical accuracy.
- The reported October 24 mismatch is preserved as a parameter
  translation error in the original script, not as a code defect, on
  the evidence of the CLASS derived parameters under the buggy inputs.
  Whether the root diagnostic failed or not is not established by this
  return, because the versions, grids, and redshifts do not match.

