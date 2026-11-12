# Historical CLASS–CAMB discrepancy: source reconciliation

Prepared 12 November 2026. Status: **historical configuration mismatch identified; no new Boltzmann-solver comparison executed**.

## Findings

The [historical evidence return](https://drive.google.com/file/d/1TlmaQmPk6AcD3VrJo_tDoi6VJGg_iG9M/view) is readable. Its nominal shared parameters do not specify the same cosmology in the two codes. It explicitly leaves neutrinos at defaults and fixes CLASS's helium fraction at 0.245, while leaving CAMB's helium at its default. It also uses different solver versions from the separate October 26 matched benchmark.

The leading explanation for its lower CAMB power is a massive-neutrino mismatch, not an established solver defect. The inspected official CAMB source defaults to one massive neutrino with summed mass 0.06 eV. CLASS's inspected official default is zero massive species. Furthermore, the historical CLASS value Ωm=0.3116598079561042 is exactly (0.022+0.12)/0.675². This is consistent with no massive-neutrino matter in that CLASS run. The direction and scale dependence of its reported suppression are qualitatively consistent with the neutrino hypothesis. **This is not causal attribution of the full 2–3% residual:** historical installed defaults, source binaries, and exact script/log bytes were not recovered; current official source does not authenticate an old environment.

Independent arithmetic on the report's rounded table gives:

- Mean absolute relative P(k) difference, divided by CLASS: 2.3012317%.
- Maximum from rounded P values: 2.9906542%.
- Mean of the separately printed relative-difference column: 2.2995%.
- All 20 printed CAMB powers are below CLASS.
- The reported σ8 pair, CAMB 0.7941911366899833 and CLASS 0.8059023437254481, implies a 1.4531794% amplitude deficit and a 2.8852415% variance deficit.

Rounding explains why recomputing the table does not reproduce every last printed relative digit. These are report-arithmetic checks, not fresh P(k) or σ8 computations. Integrating its sparse 20-point table would not independently validate σ8.

The corrected unit conversion described in the report is right: k_phys=h·k_h and P_phys=P_h/h³. Its requested CAMB maximum 1.5 h/Mpc is 1.0125/Mpc, so the stated comparison ending at 1/Mpc is within the stated interpolation domain. The earlier physical-density bug is also arithmetically reproduced: dividing physical densities by h² before handing them to CLASS produces Ωb+cdm≈0.684027 instead of 0.311660. That earlier baseline remains distinct from this residual.

## Keep the existing evidence objects separate

1. **October 24 Muse baseline:** withdrawn for the physical-density translation error. Do not reuse its dependent baryon-isolation result.
2. **October 26 local matched benchmark:** the existing ledger records four runs, massless-neutrino flat-ΛCDM, z=0,1,3 and 201 k values, with tight cross-engine discrepancy 0.0863043%. Its archived runtime and exact original bundle are absent in the current checked locations. This audit neither reruns nor newly authenticates it, and does not withdraw it because of the different Muse result.
3. **October 27/28 Muse evidence return:** the source audited here, with CAMB 2.0.5/classy 3.4.1.0 reported, unmatched defaults, a 20-point printed grid and missing full arrays. Its asserted rerun is not independently authenticated by this audit.
4. **November 10 G09:** prior reconciliation records CAMB convergence, but CLASS installation denied and CLASS unrun. This is not a failed scientific cross-code comparison. No installation was attempted here.
5. **November 12 forecast work:** a separate existing Coordinator/Forecast Bot handoff requests CLASS/CCL execution. Its job completion is not verified here. No duplicate forecast job, external contact, new installation, or forecast retuning was started.

## Exact current execution gap

At the recorded check, the selected connected cloud executor's Python 3.12.14 could not find either `camb` or `classy`; neither `camb` nor `class` was on PATH. A bounded search of workspace/temporary/home locations found no candidate solver installation, and the known October 26 virtual-environment location was absent. NumPy and SciPy were usable. The environment catalog listed one connected cloud executor, not another verified solver host.

Therefore the requested new matched z=0,1,3 run is **not run because both solvers are unavailable in this checked executor**. This is a missing-runtime gap, not scientific failure. No claim is made about every external-provider host. The retained environment receipt states the check scope. Existing external work should first return its actual executable/version/configuration/output receipt; if it has the same diagnostic, reuse it rather than start another.

## What remains unverified about the historical source

The report lists script and two log hashes, but provides their contents only partially. The actual original `.py` and `.log` files were not retrieved or hashed here. It says the original invocation/exit status, 200-point arrays and solver source hashes were not retained. A newly executed test cannot reconstruct that missing provenance. The preserved `historical_report_text.md` is connector-returned readable report text, not a claim of original-byte identity with the script or logs.

Other material confounders to freeze are radiation temperature/N_eff, helium/BBN treatment, primordial pivot and running, recombination implementation, gauge and matter-field definition, k/P units, interpolation and numerical precision. The latest inspected CLASS documentation makes matter-source gauge handling configurable; its gauge-invariant/default setting must not be assumed identical to CAMB's synchronous-gauge density output. The next protocol uses explicit synchronous total matter for both, and tests any gauge change as a separate branch. RECFAST-family choices also do not guarantee identical thermal histories.

## Deliverables and next action

`PROTOCOL.md` supplies a fixed, massless-neutrino diagnostic and an ordered single-change attribution sequence. This is a new diagnostic specification, not a recreation of unknown historical defaults and not a forecast.

`verify_spectra.py` audits saved full-precision spectra and integrates σ8 in physical units. Its seven helper checks passed, including the exact analytic toy P(k)=A/k², h-unit invariance, amplitude scaling and invalid-input rejection. The analytic integral relative error was −2.69×10⁻⁸. **These helper checks are not solver execution, physics validation, or validation of any private model.** Real-spectrum and convergence checks remain unrun.

The smallest useful next step is to obtain the already-authorized existing executor's actual matched stock-model files, or the retained October 26 package. If new execution is needed, use an already-working authorized CAMB/CLASS environment and the protocol below. This packet does not authorize installation, new access, spending, public posting or external distribution.

## Inspected public references

- [CAMB parameter/default implementation](https://github.com/cmbant/CAMB/blob/master/camb/model.py): mnu=0.06, num_massive_neutrinos=1, YHe=None with BBN prediction; physical kmax.
- [CAMB primordial spectrum implementation](https://github.com/cmbant/CAMB/blob/master/camb/initialpower.py): scalar pivot 0.05/Mpc.
- [CLASS explanatory input](https://github.com/lesgourg/class_public/blob/master/explanatory.ini): density convention, N_ncdm=0, N_ur=3.044, T_cmb=2.7255 K, neutrino-temperature conventions, gauge controls, recombination and pivot.
- [CLASS numerical precision definitions](https://github.com/lesgourg/class_public/blob/master/include/precisions.h).

These are snapshots of the public default branch retrieved for this audit, not verified historical version tags. Their retrieved text and computed hashes are preserved. Attempts to enumerate GitHub tags were rejected by the connector's supported-endpoint check; no alternate route was used to bypass it. The first source read selected the wrong connected Drive account and returned 404; the verified Primary source read succeeded. Neither event is a scientific negative result.
