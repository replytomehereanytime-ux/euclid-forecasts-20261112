# A joint-band companion to the frozen geometry forecast

12 November 2026. Separately dated postprocessing of the unchanged old-DESI posterior. No new observations, model fit, primary choice or historical forecast bytes are changed.

## Result and publication choice

The original forecast correctly labels its 95% intervals as **pointwise latent-parameter intervals**. They need no correction on that basis. If the morning figure is instead meant to contain all plotted primary-grid coordinates together with 95% posterior probability, the free-normalization model needs a different envelope.

For the unchanged **free-A flat ΛCDM primary with its primary prior**:

- The original intervals jointly contain **86.211067%** of the retained posterior across the 15 primary-grid coordinates: D_M/r_d, D_H/r_d and F_AP at z = 0.9, 1.0, 1.2, 1.5 and 1.8.
- Multiplying both side-widths around each unchanged stored median by **1.230595955778** gives **95% joint posterior mass** over that grid. The side-widths increase by approximately **23.06%**.
- Across all 33 frozen coordinates, the corresponding original joint mass is **85.541958%**, and the required common factor is **1.244994219683**, approximately **24.50%** wider.

The 33-coordinate context grid additionally contains z = 0.295, 0.510, 0.706, 0.934, 1.321 and 2.330. It is a different, larger simultaneous event, so its factor is separate. Do not apply the 15-coordinate factor while claiming the 33-coordinate result.

**Concrete choice:** retain the original figure with its explicit pointwise label, or use the new companion figure and machine-readable envelope for an explicit finite-grid joint statement. Do not silently relabel the old bands as joint 95%, and do not replace the original frozen forecast with this later addendum. This change concerns uncertainty presentation, not the ranking of cosmological models.

Neither envelope is a Euclid measurement-error forecast, frequentist confidence band, estimate of empirical coverage, probability that ΛCDM is true, or completed Foundation catalogue prediction. The free-A calculation does not certify a continuous-redshift envelope between the frozen grid points.

## Definition of the new envelope

For coordinate j, retain the source's median m_j and its 2.5th and 97.5th percentiles l_j and u_j. Define the nested band family

B_j(t) = [m_j + t(l_j − m_j), m_j + t(u_j − m_j)].

At t = 1 these are exactly the stored source intervals. The new factor solves

P(all selected latent coordinates lie in B_j(t) | retained DESI data, model, prior) = 0.95.

The same factor is used for every selected coordinate. The original medians, asymmetry of the intervals, posterior distribution and calibration data are unchanged. This is one transparent envelope convention, not a uniquely optimal or minimum-volume credible region. Every unrounded interval is supplied in JOINT_BANDS.csv; rounded prose values are summaries rather than an exact machine-level probability specification.

The figure Joint_Latent_Bands_20261112.png shows the 15-coordinate primary case as individual error bars, without connecting them into a claimed continuous-redshift band. The SVG and plotting script are included. All 576 coordinate-band rows, covering 24 model/prior/grid cases, are retained.

## All declared prior sensitivities

For the free-A model:

| Prior | Grid coordinates | Original joint posterior mass | Common factor for joint 95% |
|---|---:|---:|---:|
| Primary | 15 | 0.862110673555 | 1.230595955778 |
| Primary | 33 | 0.855419578096 | 1.244994219683 |
| Broad support | 15 | 0.862110673556 | 1.230595955775 |
| Broad support | 33 | 0.855419578096 | 1.244994219681 |
| Beta(2,2) Ω shape | 15 | 0.862123117864 | 1.230567913990 |
| Beta(2,2) Ω shape | 33 | 0.855424042200 | 1.244981920080 |

The original primary prior is Ω_m uniform on [0.1,0.5] and A independently uniform on [20,40]. The broad sensitivity uses [0.05,0.6] and [15,45]. The shape sensitivity uses the original scaled Beta(2,2) Ω prior on [0.1,0.5] and uniform A on [20,40]. These are the already retained sensitivities, not new choices selected to improve this result.

For all three fixed-A branches, every prior and both grids have joint mass 0.95 and factor 1 within numerical precision. Across the 18 fixed-A cases, the largest stored-band mass deviation from 0.95 is 1.97×10^−11; the largest factor deviation from one is 8.56×10^−11. That agreement has a mathematical explanation, not a presumption that 33 marginal intervals are independent.

## Why the fixed-A bands are already simultaneous

Write g(z) = (1+z)^3 − 1 and E(z;Ω)^2 = 1 + Ωg(z). In the stipulated flat late-time background, for fixed A > 0,

D_H/r_d = A/E(z;Ω),
D_M/r_d = A∫_0^z du/E(u;Ω),
F_AP = E(z;Ω)∫_0^z du/E(u;Ω).

For z > 0, the first two functions strictly decrease with Ω. The AP function can be written as the integral of sqrt[(1+Ωg(z))/(1+Ωg(u))]. Its derivative with respect to Ω is positive because g(z) > g(u) for 0 ≤ u < z, and all denominators are positive on the declared Ω support. Thus AP strictly increases.

Let Ω_L and Ω_U be the posterior 2.5th and 97.5th percentiles. For a decreasing coordinate its exact equal-tail band is [f(Ω_U),f(Ω_L)], while an increasing coordinate uses [f(Ω_L),f(Ω_U)]. In either case its preimage is the **same** event Ω_L ≤ Ω ≤ Ω_U. Intersecting any number of these events does not change the event or its posterior mass.

Accordingly, the exact fixed-A bands are simultaneous for any nonempty set of positive redshifts and, mathematically, for the whole positive-redshift curve of this stipulated background. That theorem does not expand the physical validity of the late-time approximation or certify finite rounded printed bounds. This calculation separately checks the actual stored numerical intervals. No analogous one-parameter conclusion follows for free A; its distance curves depend on two posterior parameters even though AP itself is independent of A at fixed Ω.

The narrow fixed-A envelopes do not establish better accuracy or physical support for their normalization hypotheses. The retained free-A primary and all earlier retrospective rankings remain unchanged.

## Computation and independent verification

The producer constructs the unchanged 13-coordinate compressed Gaussian likelihood from the retained CSV, preserving all seven blocks and their within-pair correlations. At fixed Ω, free A has a Gaussian conditional density truncated to its original proper uniform-prior bounds. AP interval restrictions first restrict Ω. Every distance interval supplies an A interval; their intersection gives the permitted conditional A mass. Adaptive integration over Ω then gives the joint posterior mass. Fixed-A bands reduce to an intersection of monotone Ω intervals.

The producer uses Gauss–Legendre distance integration orders 96 and 192, adaptive integration tolerances 2×10^−8 and 2×10^−10, and two scans for splitting active-envelope changes and feasibility crossings. The comparison tolerance was fixed at 10^−7 absolute probability or multiplier before these numerical outputs.

An independent implementation imports no producer scientific functions. It reconstructs the CSV likelihood, solves the distance ODE with DOP853, checks a Chebyshev interpolation against separate ODE evaluations, integrates after splitting band-boundary crossings, and repeats at a tighter ODE/interpolation setting. Both implementations verify all 24 cases and all 576 exported coordinate bounds.

Final checks:

- Maximum producer refinement change in joint mass: 1.09×10^−13.
- Maximum producer refinement change in multiplier: 2.69×10^−13.
- Maximum independent disagreement in joint mass: 3.28×10^−12.
- Maximum independent disagreement in multiplier: 1.48×10^−11.
- Maximum expanded-band mass residual from 0.95: 1.36×10^−13.
- All three input files are hash-verified unchanged.

These are numerical convergence and independent implementation checks, not formal interval-arithmetic error bounds, external peer review or empirical coverage validation. Reproduction details and failures are retained.

## Failure retained and source boundaries

The first producer preflight stopped before integration because it demanded byte-exact covariance equality while evaluating two products in a different floating-point order. The maximum discrepancy was 3.47×10^−18. The amendment matched the source's rho×sigma_M×sigma_H evaluation order and retained the exact equality assertion. Initial code and traceback remain in history/. No model, input, tolerance or previously computed science result changed.

The underlying source is the retained [DESI DR2 Table 4 transcription, arXiv:2503.14738v3](https://arxiv.org/html/2503.14738v3), not the later July Ly-alpha replacement or Pantheon+ joint update. Calibration CSV SHA-256: a9f3fc66443c4268cb16bb15280b4f1d60c6e7f842f8f2a2025a36ed87a7e013. Frozen result SHA-256: e5a1473fceb69f1d92b66055dc2808026ab5c60730bca63e3191088b33336967. The unchanged source archive was recovered and hash-verified from the existing private review collection; no scientific source was fetched again.

Rounded public data, a compressed Gaussian likelihood, zero cross-tracer covariance, fixed expansion-family assumptions and missing survey-selection/systematic uncertainty remain the original qualifications. A = c/(H_0 r_d) does not separately identify H_0 or r_d. The fixed normalizations remain phenomenological hypotheses, not completed HSU or Elastic Rebound physics.

No Foundation outcome, protected cohort, new reference label or future measurement was accessed. No publication, contact, payment, installation or access grant occurred. The original source package and forecast remain untouched.
