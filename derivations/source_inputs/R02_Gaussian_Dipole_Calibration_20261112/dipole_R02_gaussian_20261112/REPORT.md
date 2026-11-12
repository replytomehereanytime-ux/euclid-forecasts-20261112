# R02-G: finite-calibration, fitted-normalization reference

## Findings in order of importance
The oracle interval problem is removed in this EXACT GAUSSIAN LOG-INTENSITY reference: one fixed joint three-dimensional confidence ellipsoid is computed from observations without the injected dipole entering its construction. Normalization and selection coefficients are jointly fitted. Independent finite calibration observations are regenerated for every replicate, so their noise is propagated rather than treated as a perfect selection map.

All 34 declared implementation/engineering checks passed in six strata, with 2,000 repetitions each. Joint containment ranged 0.938–0.9555. This does not validate a Poisson-count analysis or a Euclid forecast. The reference uses a different observation likelihood and log-intensity dipole from R01; neither has been silently substituted for real galaxy counts.

Correlated-sky and biased-calibration controls fail strongly, as they should: ignoring correlated sky gives joint containment only 0.5365–0.6675. A coherent +0.03*x calibration bias induces approximately -0.03 in fitted physical dx. Independently noisy calibration is not necessarily independently unbiased calibration.

## Frozen protocol and execution
Protocol JSON hash 3dff031adf5820e6cdae3b3768302c0697e7624607701568443b398266593401 was recorded before execution at local 2026-11-12 09:19:33 UTC and sent to the independent reviewer. Code SHA256 468458198e5ee549371a73f20ad7bd8755b79b5b4f79c1fc7e45d2f525793646 was recorded before running. No public timestamp, registration or witnessed blinding is claimed. R01 and prior fixtures remain unchanged.

Reproduce with `OPENBLAS_NUM_THREADS=1 python run.py`. Requires existing Python, NumPy and SciPy only. No downloads or installations. The fixed rules involve no learned interval quantile and need no development calibration partition. All simulations are evaluation repetitions under a fully specified rule; random truths and outcomes are not analyst-blinded. Protocol, simulator, gates and seed were fixed before this run; thresholds were not retuned.

## Exact model, estimator and calculations
Retain 192 of 512 Fibonacci directions with an arbitrary two-cap mask. Thirty-two separate full-sky directions supply independent calibration observations. For science observations, known log(0.4) is subtracted and

Y = alpha + n.d + T.eta + epsilon + n.g,

where alpha is log normalization, T=[x,P2(z),x*z], eta=(0.02,0.03,-0.02), epsilon has independent Gaussian standard deviation 0.04, and g is a three-component Gaussian random sky dipole with prescribed component standard deviation 0 or 0.008. Calibration observes Tcal.eta plus independent Gaussian noise of standard deviation 0.01 or 0.05. Science and calibration are regenerated each repetition. The exact correlated covariance is 0.04^2 I + sky_sd^2*n*n-transpose. Calibration is an additional likelihood, not a prior.

Joint GLS fits [alpha,dx,dy,dz,eta_x,eta_quad,eta_xz]. Its analytic marginal 3x3 dipole covariance defines the fixed nominal 95% Gaussian ellipsoid. This is exact under the assumed Gaussian model and known covariance, not an approximate Hessian region for Poisson counts. Whitened least squares independently checks the numerical GLS solve. Nuisance profiling uses the actual weighted Fisher Schur complement.

The physical target is deterministic d in log intensity after marginalizing random sky g, not the total realized-sky dipole d+g. If exp(log intensity) is used, the dipole parameter enters exponentially and induces higher angular orders; it is not exactly R01's linear fractional count amplitude. No estimator comparison treats these distinct targets as identical.

Full combined design rank is seven. Science alone has rank six: physical x and selection x are exactly duplicate columns. With finite calibration the profile Fisher has three positive eigenvalues; its condition numbers span approximately 1.82–11.54. Losing calibration removes identification of dx and requires abstention. Weaker calibration broadens the expected dx uncertainty rather than mysteriously adding information.

Across the six primary strata, joint containment estimates have Monte Carlo standard errors 0.00461–0.00539. Maximum absolute bias normalized by estimator coordinate standard deviation is about 0.0716. Empirical covariance relative discrepancies are 0.0280–0.0531, within the fixed 0.12 gate. The 0.93–0.97 per-stratum engineering coverage gate is NOT a familywise bound or precise finite-sample certification; raw outcomes and Monte Carlo error are retained. No cosmological significance inference is made.

## Alternative explanations and explicit failures
The correlated-sky omission control applies the same realized data to an estimator that incorrectly drops the sky term. Its severe undercoverage illustrates why count noise alone is insufficient for a cosmological prediction. The sky is a deliberately simple rank-three stochastic field, not a realistic angular spectrum.

The biased-calibration control shifts all calibration measurements coherently by +0.03*x while inference assumes the calibration likelihood is unbiased. Physical dx shifts by roughly -0.03. Joint containment ranges 0.06–0.7795 across strata. Larger stated uncertainty can partly hide calibration bias; passing a broad region does not establish unbiased calibration.

Exact model-selection degeneracy without calibration is demonstrated by equal and opposite changes to physical dx and selection eta_x leaving science means identical. With no external calibration these hypotheses cannot be ranked by the counts. This is elementary identifiability logic, not evidence for HSU, Lambda-CDM or new physics.

## Limitations and remaining work
This is deliberately labeled R02-G, a Gaussian reference branch, not completed R02 Poisson validation. Log-intensity Gaussian observations are simulated directly. Taking a logarithm of noisy galaxy counts does NOT produce this exact experiment, especially with zeros or low counts. Noise/correlation scales and templates are known by construction. Finite calibration uncertainty is propagated but calibration model uncertainty is not covered by the positive strata. True selection efficiency is physical, but unconstrained Gaussian fitted parameter tails are not a globally bounded efficiency model.

No boundary changes, contamination, realistic correlated sky, unknown covariance, redshift/flux response, HSU count-response equation or real mask has been tested. Fitted normalization refers to alpha=log(mu); exponentiating alpha has finite-noise bias and is not evaluated here. Mean normalization 800 is used only to generate alpha, never as an estimator input. No model-specific forecast or novelty claim follows.

No Foundation data or target outcomes were opened. Prior official metadata check remains the only source-status input and does not establish downloadable products or exact selected samples.

## Next bounded action
Port the now-auditable observation/calibration separation to a positivity-safe Poisson plus independent calibration likelihood, fit normalization, and validate a single truth-independent joint inference procedure under sparse counts, uncertain calibration response and covariance. Preserve a Gaussian-limit cross-check against R02-G; predeclare new gates and seeds before testing. Failed model or covariance strata should trigger abstention or a separately labeled revised model, not post-hoc retuning of this run.
