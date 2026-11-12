# Independent audit: simultaneous latent geometry bands

**Result: PASS at the declared 1e-7 absolute probability and multiplier agreement threshold.**

All 12 unchanged old-DESI model/prior combinations were independently evaluated on both the frozen primary 15-coordinate grid and the full 33-coordinate grid. No new observations, refit, new prior, or primary selection was introduced.

## Main results

| Prior | Free-A grid | Stored bands: joint posterior mass | Multiplier for 95% joint mass |
|---|---|---:|---:|
| primary | primary15 | 0.862110673555 | 1.230595955778 |
| primary | all33 | 0.855419578096 | 1.244994219684 |
| broad_support | primary15 | 0.862110673556 | 1.230595955776 |
| broad_support | all33 | 0.855419578096 | 1.244994219682 |
| beta22_shape | primary15 | 0.862123117864 | 1.230567913990 |
| beta22_shape | all33 | 0.855424042200 | 1.244981920081 |

All 18 fixed-A/grid cases have 0.95 joint posterior mass and multiplier 1 to far better than 1e-7. The tiny stored-bound numerical deviations are reported below.

## Independent numerical route

The audit reconstructs the 13-coordinate block-diagonal Gaussian likelihood directly from the retained CSV, including within-bin DM/DH correlations. It never imports the producer or historical forecast code. It obtains dimensionless distances from an independent DOP853 ODE, uses Chebyshev interpolation in Omega only for speed, and checks that interpolation against 171 separate ODE solutions. Refinement changes polynomial degree 80 to 128, tightens ODE tolerances, and doubles the boundary-crossing scan resolution.

For free A, the likelihood is completed to a Gaussian in A at each Omega. The finite uniform-A prior remains exact. Each DM or DH band supplies an A interval; the event uses their intersection with the original A support. All AP bands restrict Omega. The probability is an adaptive Omega integral of the analytic truncated-Gaussian A mass. Every detected pairwise boundary crossing is used as a quadrature split, not just the active envelope switches. Factors are roots of the resulting deterministic joint-probability function. No Monte Carlo estimate is used.

## Fixed-A theorem

Write g(z)=(1+z)^3-1 and E(z;Omega)=sqrt(1+Omega*g(z)). For A>0 and z>0, DH=A/E decreases strictly with Omega, and DM=A*integral_0^z[1/E(u;Omega)]du also decreases strictly.

AP=E(z;Omega)*integral_0^z[1/E(u;Omega)]du. Inside its integral, the Omega derivative of sqrt((1+Omega*g(z))/(1+Omega*g(u))) is the positive integrand times one half of [g(z)/(1+Omega*g(z)) - g(u)/(1+Omega*g(u))]. This is strictly positive for u<z because g increases with redshift and g/(1+Omega*g) increases with g wherever E is real and positive. Thus AP increases strictly with Omega.

Consequently, each exact equal-tail 95% coordinate interval has the same preimage: the central [q_0.025,q_0.975] Omega interval. Their intersection retains exactly 95% posterior mass, for either finite grid and indeed for the complete positive-redshift curve in this fixed-A model. The exact common multiplier is 1. This analytic fact does not replace checking the stored numerical bounds; the audit separately checks those.

## Verification metrics

- independent_refinement: max absolute probability difference 2.156e-11; factor difference 9.422e-11.
- comparison_with_producer_higher: max absolute probability difference 3.271e-12; factor difference 1.48e-11.
- producer_refinement: max absolute probability difference 1.088e-13; factor difference 2.687e-13.
- Fixed-A stored bounds: max |mass-0.95| = 2.222e-11; max |factor-1| = 9.722e-11.
- Expanded independent bands: max |mass-0.95| = 1.644e-13.
- Export checks: 576 coordinate rows verified, including identity, original frozen bounds, medians and multiplier transformation.

## Interpretation limits

- These are within-model posterior probabilities for latent dimensionless geometry under unchanged old-DESI compressed Gaussian assumptions.
- They are not future-observation prediction intervals, measurement coverage, frequentist confidence coverage, or a Euclid performance statement.
- Free-A results establish simultaneous mass only on the named finite coordinate grid, not over every continuous redshift.
- The common median-centered multiplier defines one particular band family. It is not asserted to be unique, shortest, optimal, or an HPD region.
- Numerical convergence and independent agreement provide strong evidence at the requested tolerance. They are not a formal interval-arithmetic enclosure.

The JSON comparison records hashes of every reviewed source/result file. Audit files are confined to independent_review; original inputs and producer outputs were not changed.
