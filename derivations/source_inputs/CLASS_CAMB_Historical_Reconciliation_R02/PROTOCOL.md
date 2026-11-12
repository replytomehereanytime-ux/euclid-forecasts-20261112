# Source-specific next diagnostic, not yet executed

## 0. Avoid duplicate work and protect the evidence

Check the current Forecast Bot's actual job and outputs, plus the retained October 26 matched package, before launching anything. Reuse a matching result. Keep the historical 20-point source and all old forecasts immutable. This is stock linear ΛCDM code consistency, not a survey likelihood or a test of HSU, STO, Elastic Rebound or another private model. No target-release outcomes are required or should be inspected for this diagnostic.

Use an already-working authorized environment. Do not install anything from this protocol. Before execution record UTC, exact command, interpreter/module/distribution versions, source revision if available, executable and shared-library hashes, loaded parameter dumps, thread count, hardware and package dependency versions. Record missing provenance as missing. Create a new run directory, never overwrite a prior attempt. Retain stdout, stderr, exit status, warnings and failed attempts.

## 1. Fixed common physical model

- H0=67.5 km/s/Mpc, h=0.675.
- omega_b=ombh2=0.022; omega_cdm=omch2=0.12. These are Ω_i h².
- Spatially flat, Λ with w=−1 and wa=0. Closure includes radiation.
- A_s=2e−9; n_s=0.965; scalar pivot k*=0.05/Mpc; both scalar runnings zero. Pure adiabatic scalar initial conditions; no tensor contribution.
- T_CMB=2.7255 K, total early-time N_eff=3.044, **all massless**. CAMB mnu=0, num_massive_neutrinos=0, nnu=3.044, standard_neutrino_neff=3.044. CLASS N_ncdm=0, N_ur=3.044. No extra dark radiation or interaction species.
- YHe=0.245 in both; disable BBN inference. No reionization in either for this diagnostic. Preserve this intentional simplification as distinct from observational inference.
- Explicit RECFAST-family recombination in both, recording all actual implementation/version/fudge settings. CAMB Recfast and RecFastCLASS are not identical algorithms. If residuals remain, compare x_e(z)/thermal-history outputs and make a same-HyRec-family sensitivity only if already supported, with no install.
- Linear total nonrelativistic matter density (baryons+CDM for this massless case), in synchronous gauge in both. CLASS `gauge=synchronous`, `matter_source_in_current_gauge=yes`; CAMB `delta_tot`/Transfer_tot. Do not silently compare a gauge-invariant density to a synchronous density. Record the precise definitions implemented by the installed versions; fail on unsupported parameters rather than ignore them.
- No nonlinear correction. z=0,1,3. Preserve explicit z labels: CAMB internally sorts redshifts in descending order.

For the CLASS wrapper, a candidate parameter dictionary under the inspected API is:

```python
{
 'H0':67.5, 'omega_b':0.022, 'omega_cdm':0.12,
 'Omega_k':0.0, 'N_ncdm':0, 'N_ur':3.044, 'T_cmb':2.7255,
 'YHe':0.245, 'recombination':'RECFAST', 'reio_parametrization':'reio_none',
 'A_s':2e-9, 'n_s':0.965, 'alpha_s':0.0, 'k_pivot':0.05,
 'modes':'s', 'ic':'ad', 'gauge':'synchronous',
 'matter_source_in_current_gauge':'yes', 'output':'mPk',
 'z_pk':'0,1,3', 'P_k_max_1/Mpc':30.0
}
```

Read back that Λ fills the flat closure and nonlinear mode is none; do not assume a rejected or unused key took effect. CLASS parameter spellings differ across versions, so inspect the installed parser rather than silently removing a check. No wrapper above has been run in this audit.

Under the inspected CAMB API, construct CAMBparams, set_classes(recombination_model='Recfast'), set_cosmology with all physical values above, set Reion.Reionization=False, set InitPower.set_params(As=2e-9, ns=0.965, nrun=0, nrunrun=0, r=0, pivot_scalar=0.05), set_dark_energy(w=-1,wa=0), set_matter_power(redshifts=[3,1,0],kmax=30,k_per_logint=40,nonlinear=False), and explicitly set NonLinear_none. Request Transfer_tot for both spectrum fields, `hubble_units=False` and `k_hunit=False` on the power interpolator. Record effective settings, not just requested arguments.

## 2. Grids and precision experiment

Use physical k in 1/Mpc and P in Mpc³ throughout. The comparison grid is 201 logarithmic points from 0.002 through 1/Mpc, matching the historical source's range but not its rounded 20-point interpolation. Also evaluate the exact unrounded 20-point geomspace separately for historical shape comparison, never pretending the rounded published k values were the exact original nodes.

For σ8 use a separate dense physical-k grid from 1e−5 to 30/Mpc with 12,001 logarithmic nodes, then 24,001 for quadrature refinement. Compare truncations at 10 and 30/Mpc; if the result has not stabilized to the declared tolerance, extend kmax only within the same authorized computation scope and rerun, retaining prior outputs. Do not extrapolate beyond solver coverage.

Run four distinct calculations: CAMB/base, CAMB/tight, CLASS/base, CLASS/tight. These levels are not asserted to be mathematically equivalent between codes:

- CAMB/base: AccuracyBoost=1, lAccuracyBoost=1, lSampleBoost=1, k_per_logint=40.
- CAMB/tight: AccuracyBoost=2, lAccuracyBoost=2, lSampleBoost=2, k_per_logint=80.
- CLASS/base: tol_background_integration=1e−10, tol_thermo_integration=1e−6, tol_perturbations_integration=1e−5, k_per_decade_for_pk=40, k_per_decade_for_bao=70, l_max_ur=17, sigma_k_per_decade=80.
- CLASS/tight: tol_background_integration=1e−11, tol_thermo_integration=1e−7, tol_perturbations_integration=1e−6, k_per_decade_for_pk=80, k_per_decade_for_bao=140, l_max_ur=34, sigma_k_per_decade=160.

Use identical physical settings at both levels; archive every other effective numerical default. If the comparison is near a threshold, add a separately retained tighter level rather than call two-level agreement asymptotic convergence. Independently densify the output/interpolation grid and separate interpolation effects from integration effects.

## 3. σ8 integration and output checks

For R=8/h=11.85185185185185 Mpc:

σ_R² = [1/(2π²)] integral d ln k k³ P(k,z) W(kR)²,

W(x)=3(sin x−x cos x)/x³, using its Taylor series near zero. The provided checker does this. Compare the result against CAMB's stored sigma8 at explicitly mapped redshifts and CLASS sigma(R,z) with R in physical Mpc. Confirm actual API unit flags rather than assume them.

In h units the equivalent test uses k_h=k_phys/h, P_h=h³ P_phys and R_h=8. Calculate both representations from the same arrays; they must agree numerically. Never integrate the sparse historical 20-point table and call that an independent σ8 check.

Predeclare these diagnostic screens, not universal accuracy guarantees:

- Each solver's base/tight max |P_base/P_tight−1| < 0.1% on the specified 201-point grid, at every redshift.
- Tight cross-code max |P_CAMB/P_CLASS−1| < 0.5% on that grid. Report mean/max/signed differences and k,z of maxima, even on failure.
- Integrated vs each engine's own σ8 relative difference < 0.1%; grid and tail refinements individually < 0.01% in σ8.
- Physical/h-unit integral invariance to 1e−10 relative; positivity/finiteness and grid-range assertions.

Failure is retained and investigated, not discarded or averaged away. Passing verifies this bounded calculation, not observations or a private cosmology. The provided checker computes some screens; the engine-σ8 and refinement comparisons still require the retained runtime outputs and explicit manual/driver checks.

Save CSVs with columns:
`z,k_1_per_Mpc,P_camb_base_Mpc3,P_camb_tight_Mpc3,P_class_base_Mpc3,P_class_tight_Mpc3`.

Keep comparison and dense-integral CSVs separate. Preserve raw native grids, transferred/interpolated grids, per-engine sigma8 and derived Ωm/Ωr/ΩΛ/N_eff, and background/thermal histories. The checker does not authenticate their provenance.

```sh
python verify_spectra.py --self-test
python verify_spectra.py comparison.csv > comparison_audit.json
python verify_spectra.py dense.csv --dense > sigma8_audit.json
```

## 4. Attribute the historical residual only after the matched baseline

Do not conflate a new matched diagnostic with a historical replay. First obtain the original script/log bytes if available and compare their bytes to the source-stated hashes; a hash printed in a report is not verification. If the exact old versions are not already available, label results as current-version sensitivity, not historical reproduction.

From the successful massless matched baseline, vary one item at a time while freezing everything else:

1. CAMB-only mnu=0.06 eV, one massive species, fixed total early N_eff=3.044 and fixed omega_b/omega_cdm. This deliberately unmatched branch tests the leading source explanation. Compare its residual's shape and amplitude with the source and record its changed Ωm.
2. A matched massive-neutrino branch in both solvers, if needed. Match not merely summed mass and nominal N_eff but the phase-space distribution, temperature, physical multiplicity, relativistic energy density and nonrelativistic density. CAMB/CLASS default temperature/conversion conventions differ; recover CAMB's actual degeneracy/temperature convention and choose CLASS T_ncdm, degeneracy and N_ur accordingly. Require early rho_nu/rho_gamma and late omega_nu readback agreement before P(k) comparison. Do not assume CLASS N_ur=2.044 or 2.0328 is universally correct.
3. Restore CAMB's BBN helium treatment alone; record actual YHe rather than label it 'default'. Then change recombination alone if required.
4. Change gauge/output definition, primordial pivot/running or radiation conventions only as separate logged branches where old-version evidence warrants them.
5. Reproduce the source's 200-point h-unit CAMB sampling plus log-log interpolation as a final interpolation-only sensitivity. Compare against direct physical-unit evaluation.

Use the changes in the full spectra and integrated variance, not one fitted offset. Only attribute the full historical residual when the actual old configuration is known and its retained output is reproduced within rounding and numerical tolerances. Otherwise retain a well-supported hypothesis and a quantified current-version sensitivity.
