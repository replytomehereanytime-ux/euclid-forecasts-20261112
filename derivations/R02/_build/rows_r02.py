# R02 single source of truth. Public-facing fields contain no significance / p-value / coincidence wording; such content lives only in INTERNAL_CONTEXT_R02.md.
W = "R02/wolfram/raw_outputs_R02.txt"
R4 = "wolfram_R04/WOLFRAM_RESULTS_R04.md"
CD = "DESI_PREDICTIONS_source.md"
Q95 = "(d−m)ᵀ(C_E + C_pred)⁻¹(d−m) ≤ q95(N), with q95(N) the 0.95 quantile of the chi-square distribution with N = number of scored points (N=4: 9.4877; 6: 12.5916; 8: 15.5073; 12: 21.0261; other N computed with the same formula at scoring time; R02/wolfram raw_outputs 'Scoring quantiles')"
rows = []
def add(**k):
    base = dict(id="",kind="",readiness="",verification="",outcome="NOT_RUN",branch="n/a",title="",product="",acquisition="Not yet acquired. At scoring: record retrieval UTC, URL/DOI, arXiv version and sha256 of the file used.",
        cuts="",observable="",model="",calib="",mask="",contaminants="",estimator="",covariance="",predictive="",scoring="",abstention="",internal="",sources="",notes="")
    base.update(k); rows.append(base)

# ---------------- DESI Year-5 (prospective) ----------------
DESI_PROD = "DESI DR3 / 5-year BAO cosmology key paper(s), arXiv v1 (expected 2027; not public on 2026-11-12, see R01 §3/§0 checks)."
DESI_EXT = dict(cuts="DESI's own Y5 tracer samples (external).", mask="DESI's own footprint and veto masks (external).", contaminants="Handled inside DESI's pipeline (external): imaging systematics, fibre assignment, redshift failures.",
                estimator="DESI's official Y5 BAO + cosmology inference (external).", covariance="DESI's published Y5 posterior (external).",
                calib="Forecast text dated 2026-10-13 (DESI_PREDICTIONS_source L3); anchors DESI DR1 (2024) and DR2 (Mar 2025) only. Lyα AP update (Jul 2026) predates the text but was not used in it.")
PI68 = "Forecaster's central 68% prediction interval (R01 default; the author to confirm label). No full distribution specified; interval used as stated."
ABST = "NOT_RUN if the named combination/row is not published in a DESI Y5 key paper or companion by 2028-12-31."
def desi(id_, title, obs, model, pred, scoring, src, notes="", extra_abst=""):
    add(id=id_, kind="prospective", readiness="READY", verification="PROVISIONAL", title=title, product=DESI_PROD, observable=obs, model=model, predictive=pred, scoring=scoring, abstention=ABST+extra_abst, sources=src, notes=notes, **DESI_EXT)
desi("D-P2a","Pivot equation of state near −1","w_p (dimensionless) at DESI's published pivot z_p ≈ 0.4–0.5; single value","w0waCDM as fitted by DESI; data DESI Y5 + CMB + DES SNe (DES-Y5 row if reported, else DES-Dovekie)",
     "w_p ∈ [−1.06, −0.94] (−1.00 ± 0.06). "+PI68,"PASS iff −1.06 ≤ w_p ≤ −0.94; FAIL otherwise.",f"{CD} L19–24; R01 WOLFRAM_CHECKS W2",
     "Basis: box fit w_p = −1.044 ± 0.050 at a_p = 0.673 (desi_r01/fit_results.json). R04 §7: against expected errors alone ±0.06 is ~77% coverage.", " Also NOT_RUN if no w_p is published.")
desi("D-P3a","w0, wa inside predicted boxes","w0, wa (dimensionless); single values","w0waCDM; DESI Y5 + CMB + DES SNe (DES-Y5 if reported, else DES-Dovekie)",
     "w0 ∈ [−0.86, −0.66]; wa ∈ [−1.15, −0.45] (−0.76 ± 0.10; −0.80 ± 0.35). "+PI68,"PASS iff both inside; FAIL otherwise.",f"{CD} L26–31; R01 W2",
     "Context (retrospective): DESI DR2 Results IV DESI+CMB+DES-Dovekie w0 = −0.821 ± 0.054, wa = −0.65 ± 0.20 (R03 L34), both inside. R04 §7: against expected errors alone ±0.10/±0.35 ≈ 97–99% / 95–98%.")
desi("D-P3b","w0–wa quadrant not abandoned","Central w0, wa","as D-P3a","Central w0 ≥ −0.95 and wa ≤ −0.2 (threshold claim).","FAIL iff central w0 < −0.95 OR central wa > −0.2; PASS otherwise.",f"{CD} L31")
desi("D-P3c","w0, wa errors shrink at least 20% from DR2","Published 68% errors e(w0), e(wa) (asymmetric errors averaged)","as D-P3a","e(w0) ≤ 0.0456 and e(wa) ≤ 0.176 (threshold).","PASS iff both hold; FAIL otherwise.",f"{CD} L28; calc_model_check_output.json C3_shrink")
desi("D-P4a","BAO-only matter density stays low","Ωm (dimensionless), flat ΛCDM, DESI Y5 BAO alone","flat ΛCDM (DESI)","Ωm ∈ [0.288, 0.308] (0.298 ± 0.010). "+PI68,"PASS iff inside; FAIL otherwise.",f"{CD} L33–38",
     "Context: box BAO-only Ωm = 0.2975 ± 0.0086 (primary) and 0.3017 ± 0.0077 (Lyα replacement branch) (R02/wolfram raw outputs).")
desi("D-P4b","BAO-only Ωm stays below the Planck value","Ωm as D-P4a","flat ΛCDM","Ωm < 0.315 (threshold).","FAIL iff Ωm ≥ 0.315; PASS otherwise.",f"{CD} L38")
desi("D-P5a","Neutrino mass limit below 0.055 eV","95% upper limit on Σmν (eV), ΛCDM, DESI Y5 + CMB, DESI baseline prior","ΛCDM + Σmν (DESI)","UL95 < 0.055 eV.","PASS iff published UL95 < 0.055 eV; FAIL otherwise (including any reported lower bound).",f"{CD} L40–45")
desi("D-P5b","No relaxed neutrino limit or detection","UL95 and any 95% lower bound on Σmν","as D-P5a","UL95 ≤ 0.08 eV and no 95% lower bound > 0.06 eV.","FAIL iff UL95 > 0.08 eV OR a 95% lower bound > 0.06 eV; PASS otherwise.",f"{CD} L45")
desi("D-P8a","Early-universe H0","H0 (km/s/Mpc), ΛCDM, DESI Y5 + CMB","ΛCDM (DESI)","H0 ∈ [67.8, 68.6] (68.2 ± 0.4). "+PI68,"PASS iff inside; FAIL otherwise.",f"{CD} L61–66")
add(id="D-P8c", kind="prospective", readiness="READY", verification="PROVISIONAL", title="Ladder H0 stays at 72.5–73.5",
    product="Latest SH0ES (Riess et al.) H0 public on or before 2027-12-31", cuts="SH0ES's own", observable="H0 (km/s/Mpc), single value", model="distance ladder (SH0ES)",
    calib="2026-10-13", mask="n/a", contaminants="SH0ES's own", estimator="SH0ES published", covariance="SH0ES published", predictive="72.5 ≤ H0 ≤ 73.5 (stated range)",
    scoring="PASS iff latest SH0ES central value on 2027-12-31 is in [72.5, 73.5]; FAIL otherwise.", abstention="Prospective only for SH0ES results first public after 2026-10-13; the latest current SH0ES value was not checked (UNVERIFIED).", sources=f"{CD} L63")
for id_, t in [("D-P1a","Evolving dark-energy preference (interval)"),("D-P1b","Evolving dark-energy preference (floor)"),("D-P2b","Pivot not far from −1 (original falsifier)"),("D-P8b","Ladder–early H0 gap (threshold)"),("D-P8d","Ladder–early H0 gap (floor)")]:
    add(id=id_, kind="prospective", readiness="READY", verification="PROVISIONAL", title=t, product=DESI_PROD, **DESI_EXT, observable="Significance-type quantity: INTERNAL CONTEXT only",
        model="see INTERNAL_CONTEXT_R02.md", predictive="INTERNAL CONTEXT only", scoring="INTERNAL CONTEXT only (two-valued rule recorded there)", abstention=ABST, internal=f"INTERNAL_CONTEXT_R02.md#{id_}", sources=f"{CD}")
add(id="D-P7", kind="prospective", readiness="NOT READY", verification="PROVISIONAL", title="No hemispheric BAO difference",
    product="DESI DR3/Y5 LSS catalogues (release TBD). DR1 catalogues are already public (not prospective).", cuts="TBD (proposed: DESI BAO tracer bins)", observable="Δα_iso = α_N − α_S (dimensionless), hemispheres split by the plane ⟂ CMB-dipole axis; one value per tracer bin or combined (TBD)",
    model="Isotropic ΛCDM BAO", calib="2026-10-13", mask="TBD: DESI footprint split by hemisphere", contaminants="TBD: hemisphere-dependent imaging depth, stellar density, extinction",
    estimator="TBD: per-hemisphere α_iso with DESI fitter", covariance="TBD: per-hemisphere mocks", predictive="95% interval for Δα_iso inside (−3×10⁻³, +3×10⁻³)",
    scoring="PROPOSED: PASS iff the published/derived 95% interval for Δα_iso lies inside (−0.003, +0.003); FAIL otherwise.", abstention="NOT_RUN if no DR3/Y5 catalogues by 2028-12-31.",
    sources=f"{CD} L54–59; COSMOLOGY_MODEL_CHECK L110", notes="Axis coordinates not in any source file (TBD).")

# ---------------- Euclid count dipole (prospective, NOT READY) ----------------
CDP = "Euclid DR1-Foundation (announced to open 2026-11-12 11:00 UTC; actual availability and contents NOT verified by this bot as of 09:55 UTC): MER final catalogue / PHZ catalogues + VMPZ HEALPix footprint/coverage/depth masks. Randoms and visibility masks only with DR1 Complete (mid-2027). Release binding (Foundation vs Complete): TBD."
FDN = " Foundation covers ~1,900 deg² (f_sky ≈ 0.046): no full-mission precision may be assumed; any uncertainty on D must come from Foundation-footprint mocks."
for id_, t, obs, pred, sc, src, internal in [
 ("E-CD-P1","Count-dipole amplitude","Number-count dipole amplitude D (dimensionless)","INTERNAL CONTEXT only (significance-type)","INTERNAL CONTEXT only","fa.txt L112–117",True),
 ("E-CD-P2","Count-dipole direction","Dipole direction (l,b), degrees, Galactic frame assumed","Best-fit direction within 30° of (l,b) = (242.28°, 37.10°)","PROPOSED: PASS iff great-circle separation ≤ 30°; FAIL otherwise.","fa.txt L119–123",False),
 ("E-CD-P3","Dipole rises with redness or redshift","D per bin (dimensionless), ≥3 bins of one variable (TBD)","Strictly increasing D with max/min ≥ 2","PROPOSED: PASS iff ≥3 bins, strictly increasing, max/min ≥ 2; FAIL otherwise.","fa.txt L125–130",False),
 ("E-CD-P4","Joint ℓ=1+3 fit raises dipole","D_joint vs D_dipole-only; octupole coefficients","INTERNAL CONTEXT only (second clause is significance-type)","INTERNAL CONTEXT only","fa.txt L132–137",True),
 ("E-CD-P5","ΛCDM mock exceedance fraction","Fraction of ≥2,000 ΛCDM mocks with D ≥ 0.01554","INTERNAL CONTEXT only (exceedance-fraction claim)","INTERNAL CONTEXT only","fa.txt L139–143",True)]:
    add(id=id_, kind="prospective", readiness="NOT READY", verification="UNVERIFIED", title=t, product=CDP, cuts="TBD (population, magnitude/PHZ cuts, star–galaxy cut) (fa.txt L145)", observable=obs,
        model="Empirical extrapolation of CatWISE fits; kinematic null D_kin = [2 + x(1+α)]β with Euclid x, α unknown (R04 §1 grid 0.0034–0.0086 is a synthetic grid, not a Euclid value)",
        calib="October freeze statements; private archive sealed 2026-11-11 01:46:02 UTC (fa.txt L13, S1). Basis (CatWISE) already spent.", mask="TBD; buildable from Foundation VMPZ maps (R03 L67)"+FDN,
        contaminants="Stars, depth/extinction gradients, ice-contamination holes, RA=0h gap, incompleteness without ground-based counterparts (RELEASE_PRIORART_REVIEW §1.3, §3.3)",
        estimator="TBD", covariance="TBD (Foundation-footprint mocks)", predictive=pred, scoring=sc, abstention="NOT_RUN until cuts/mask/estimator/covariance/kinematic null are frozen before the catalogue is opened; anything frozen after opening is not prospective.",
        internal=(f"INTERNAL_CONTEXT_R02.md#{id_}" if internal else ""), sources=src+"; Freeze Addendum (Drive 1yNjUna5…, sha256 4fb89624…6e77e)", notes="NOT READY (R02 L28; R01 L16).")
add(id="E-L-P6", kind="prospective", readiness="NOT READY", verification="PROVISIONAL", title="No shell-axis dipole in Euclid lensing",
    product="Euclid DR1 Complete (mid-2027): SHE shear catalogues and 2D-MASS-WL convergence maps. Not in Foundation.", cuts="TBD", observable="Kinematic-subtracted convergence dipole (dimensionless)",
    model="ΛCDM kinematic only, β = 1.23×10⁻³ (scaling factors TBD)", calib="2026-10-13", mask="TBD", contaminants="PSF/shear calibration modes, depth anisotropy (fa.txt L174–179)", estimator="TBD", covariance="TBD",
    predictive="INTERNAL CONTEXT only (detection-threshold claim)", scoring="INTERNAL CONTEXT only", abstention="NOT_RUN until floor, tolerance, mask, estimator, covariance are numeric.", internal="INTERNAL_CONTEXT_R02.md#E-L-P6", sources=f"{CD} L47–52")
add(id="E-PHZ-1", kind="prospective", readiness="NOT READY", verification="PROVISIONAL", title="Capped adaptive PHZ beats native PHZ (method, not cosmology)",
    product="Euclid DR1-Foundation PHZ catalogue (DpdPhzPfOutputCatalog) + independent truth set (TBD)", cuts="TBD: cohort not bound (fa.txt L96–98)", observable="Mean five-class Brier score (dimensionless); classes [0,1),[1,2),[2,3),[3,6),[6,∞)",
    model="q = (1−α)p + αu, fixed adaptive α rule (fa.txt L86–92)", calib="Rule fixed before 2026-11-12 (Freeze Addendum)", mask="TBD", contaminants="Truth-set dependence on shared calibration; outliers", estimator="Mean Brier difference", covariance="TBD (paired bootstrap)",
    predictive="mean Brier(q) < mean Brier(p)", scoring="PROPOSED: PASS iff mean Brier(q) < mean Brier(p) on the frozen cohort; FAIL otherwise.", abstention="Prospective only if the cohort is frozen before the PHZ outputs are opened.", sources="fa.txt L85–98; COSMOLOGY_MODEL_CHECK L134–138")

# ---------------- Conditional theory curves at Euclid BAO bins ----------------
EUC_BAO_PROD = "First Euclid spectroscopic BAO measurement built on DR1 Complete (mid-2027 or later); bins z ∈ {0.9, 1.2, 1.5, 1.8} (arXiv:2605.03446; R03 L46, L66). NOT Foundation."
EUC_EXT = dict(cuts="Euclid Consortium's published BAO sample (external)", mask="Euclid's (external; randoms/visibility masks are Complete-era)", contaminants="Line interlopers, redshift failures, purity/completeness (Euclid's; external)",
               estimator="Euclid's published BAO fit (external)", covariance="C_E = Euclid published covariance; C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl)")
ABST_B = "NOT_RUN if Euclid publishes no DM/rd, DH/rd (or convertible α parameters with fiducial rd) at z_eff within [0.9, 1.8]. Points outside the grid are not scored. Interpolate linearly in z between grid nodes."
def ctc(id_, branch, title, model, calib, vals, src, notes=""):
    pd = "; ".join(f"z={z}: DM/rd {a:.4f} ± {sa:.4f}, DH/rd {b:.4f} ± {sb:.4f}" for z,(a,b,sa,sb) in vals.items())
    add(id=id_, kind="conditional theory curve", readiness="READY", verification="PROVISIONAL", branch=branch, title=title, product=EUC_BAO_PROD,
        observable="DM/rd and DH/rd (dimensionless) on grid z = 0.9, 1.2, 1.5, 1.8 (DM/DH derived, not scored separately)", model=model, calib=calib, **EUC_EXT,
        predictive="Gaussian N(m, C_pred), Laplace (Hessian) ±1 standard deviation (68.3% central for Gaussian) on the fit: "+pd, scoring="PASS iff "+Q95+"; FAIL otherwise.", abstention=ABST_B, sources=src, notes=notes)
OLD = "DESI DR2 BAO (13 points, official mean/cov on box; Lyα z=2.33 DM/rd 38.989, DH/rd 8.632, r = −0.431) — FROZEN PRIMARY"
NEW = "DESI DR2 BAO with DECLARED REPLACEMENT of the Lyα point by DR2 Results IV v3 Eq. 26: DM/rd 39.32 ± 0.33, DH/rd 8.600 ± 0.066, ρ = +0.225 (replaces, not added)"
CMB = "; Planck 2018 compressed CMB (R, l_A, ω_b; Chen+2019) as in R04"
P_L = "Flat priors 0.1<Ωm<0.6, 0.4<h<1, 0.015<ω_b<0.03; radiation from h with N_eff=3.046; rd fitting formula (fit_cpl.py / R04)"
ctc("CTC-1P","PRIMARY","Flat ΛCDM, BAO only","Flat ΛCDM, radiation omitted, params (Ωm, A = c/(H0 rd)), no priors beyond 0.1<Ωm<0.6",OLD,
    {0.9:(21.0789,17.8273,0.0710,0.0666),1.2:(25.9885,15.0084,0.0760,0.0736),1.5:(30.1415,12.7642,0.0837,0.0739),1.8:(33.6928,10.9785,0.0944,0.0704)}, f"{W} call1b PRIMARY; reproduces calc_normalization_check_R02_output.json (Ωm 0.29746, A 29.5246)")
ctc("CTC-1B","REPLACEMENT","Flat ΛCDM, BAO only","as CTC-1P",NEW,
    {0.9:(21.1067,17.8121,0.0689,0.0617),1.2:(26.0102,14.9844,0.0750,0.0663),1.5:(30.1554,12.7373,0.0828,0.0658),1.8:(33.6987,10.9516,0.0927,0.0624)}, f"{W} call1b BRANCH; = R01 E-BAO-1 central values (R01 W1)")
ctc("CTC-2P","PRIMARY","Flat ΛCDM, BAO + compressed CMB","Flat ΛCDM; "+P_L,OLD+CMB,
    {0.9:(21.0534,17.5713,0.0617,0.0162),1.2:(25.8812,14.7263,0.0643,0.0058),1.5:(29.9497,12.4863,0.0642,0.0056),1.8:(33.4201,10.7174,0.0630,0.0073)}, f"{W} call1 3rd element; best fit reproduces R04 old-Lyα ΛCDM (Ωm 0.32397)")
ctc("CTC-2B","REPLACEMENT","Flat ΛCDM, BAO + compressed CMB","as CTC-2P",NEW+CMB,
    {0.9:(21.0581,17.5726,0.0604,0.0159),1.2:(25.8862,14.7267,0.0629,0.0057),1.5:(29.9547,12.4863,0.0629,0.0056),1.8:(33.4250,10.7171,0.0617,0.0072)}, f"{W} call2 LCDM BRANCH; matches R04 §5 / wolfram_raw_02_fit.txt Laplace values")
ctc("CTC-3P","PRIMARY","Constant-w (wCDM), BAO + compressed CMB","Flat wCDM, prior −3<w<1; "+P_L,OLD+CMB,
    {0.9:(21.0317,17.6460,0.0679,0.0837),1.2:(25.8798,14.7854,0.0650,0.0650),1.5:(29.9634,12.5285,0.0658,0.0462),1.8:(33.4442,10.7460,0.0675,0.0320)}, f"{W} call2 wCDM PRIMARY", "Best fit w = −1.043 ± 0.049 (retrospective).")
ctc("CTC-3B","REPLACEMENT","Constant-w (wCDM), BAO + compressed CMB","as CTC-3P",NEW+CMB,
    {0.9:(21.0346,17.6567,0.0662,0.0836),1.2:(25.8854,14.7930,0.0636,0.0646),1.5:(29.9709,12.5333,0.0646,0.0457),1.8:(33.4529,10.7490,0.0665,0.0315)}, f"{W} call2 wCDM BRANCH", "Best fit w = −1.049 ± 0.049 (retrospective).")
ctc("CTC-4P","PRIMARY","Curved ΛCDM (oΛCDM), BAO + compressed CMB","ΛCDM + Ωk, prior −0.3<Ωk<0.3; "+P_L+". Compressed CMB priors are used outside their flat-model derivation (caveat).",OLD+CMB,
    {0.9:(21.1308,17.6763,0.0681,0.0423),1.2:(25.9836,14.8220,0.0747,0.0361),1.5:(30.0731,12.5710,0.0789,0.0320),1.8:(33.5604,10.7916,0.0818,0.0286)}, f"{W} call3 oLCDM PRIMARY", "Best fit Ωk = −0.0034 ± 0.0013 (retrospective; compressed-prior caveat).")
ctc("CTC-4B","REPLACEMENT","Curved ΛCDM (oΛCDM), BAO + compressed CMB","as CTC-4P",NEW+CMB,
    {0.9:(21.1426,17.6840,0.0672,0.0420),1.2:(25.9972,14.8276,0.0739,0.0357),1.5:(30.0877,12.5753,0.0782,0.0316),1.8:(33.5759,10.7950,0.0811,0.0282)}, f"{W} call3 oLCDM BRANCH", "Best fit Ωk = −0.0036 ± 0.0012 (retrospective).")
add(id="CTC-5B", kind="conditional theory curve", readiness="READY", verification="PROVISIONAL", branch="REPLACEMENT", title="CPL (w0waCDM), BAO + compressed CMB", product=EUC_BAO_PROD,
    observable="DM/rd, DH/rd on z = 0.9, 1.2, 1.5, 1.8", model="CPL; prior −3<w0<1, −5<wa<3; "+P_L, calib=NEW+CMB, **EUC_EXT,
    predictive="Posterior median and 68% interval from importance-reweighted box chains (R04 §5): z=0.9 DM/rd 20.997 [20.923, 21.071], DH/rd 17.627 [17.529, 17.726]; z=1.2 25.854 [25.781, 25.927], 14.846 [14.772, 14.932]; z=1.5 29.963 [29.889, 30.035], 12.608 [12.536, 12.690]; z=1.8 33.467 [33.391, 33.542], 10.819 [10.756, 10.882]. s_pred = half-width of the 68% interval.",
    scoring="PASS iff "+Q95+"; FAIL otherwise.", abstention=ABST_B, sources=f"{R4} L117–129", notes="R04 labels ρ=+0.225 UNVERIFIED; R03 L24 verified it. Non-Gaussian posterior (w0–wa degeneracy): Gaussian scoring is an approximation.")
add(id="CTC-5P", kind="conditional theory curve", readiness="NOT READY", verification="UNVERIFIED", branch="PRIMARY", title="CPL (w0waCDM), BAO + compressed CMB, frozen primary", product=EUC_BAO_PROD,
    observable="as CTC-5B", model="as CTC-5B", calib=OLD+CMB, **EUC_EXT, predictive="MISSING: R04 ran the old-Lyα CPL fit (best fit w0 −0.774, wa −0.791) but its Hessian was not positive-definite and no chain bands were produced for the primary. The original box chain (desi_r01/chain_w0waCDM.npy) was fit to the primary data and could supply them.",
    scoring="PASS iff "+Q95+"; FAIL otherwise (once predictive bands exist).", abstention=ABST_B, sources=f"{R4} L75, L80", notes="")

# ---------------- Retrospective fits (parameters; not forecasts) ----------------
for id_, t, v, src in [
 ("RF-1","Flat ΛCDM BAO-only parameters","Primary Ωm 0.29746 ± 0.00862, A 29.525 ± 0.214 (corr 0.924); replacement Ωm 0.30171 ± 0.00770, A 29.633 ± 0.196 (corr 0.910)",f"{W} call1b"),
 ("RF-2","Flat ΛCDM BAO+CMB parameters","Primary Ωm 0.32397 ± 0.00429, h 0.69868 ± 0.00311; replacement Ωm 0.32428 ± 0.00421, h 0.69846 ± 0.00304",f"{W} call1, call2"),
 ("RF-3","Constant-w parameters","Primary w −1.043 ± 0.049, Ωm 0.3167 ± 0.0093; replacement w −1.049 ± 0.049, Ωm 0.3162 ± 0.0092",f"{W} call2"),
 ("RF-4","Curvature parameters","Primary Ωk −0.0034 ± 0.0013; replacement Ωk −0.0036 ± 0.0012 (compressed-CMB caveat)",f"{W} call3"),
 ("RF-5","CPL parameters (R04)","Replacement best fit w0 −0.767, wa −0.824; reweighted-chain w0 −0.700 ± 0.291, wa −1.069 ± 0.883",f"{R4} L75–77"),
 ("RF-6","GWTC-4.0 Ξ0 ↔ c_M mapping check (R04 §6b)","c_M = 1.3 → Ξ0 = 1.447 vs published 1.4^{+1.0}_{−0.4} (consistent)",f"{R4} §6b"),
 ("RF-7","Fibonacci normalisation comparison","INTERNAL CONTEXT only (coincidence-type claim)","R03 L60–62")]:
    add(id=id_, kind="retrospective fit", readiness="n/a", verification="VERIFIED" if id_ in ("RF-1","RF-2") else "PROVISIONAL", outcome="n/a", title=t, product="Public DESI DR2 BAO / Planck 2018 compressed / GWTC-4.0 (already public)",
        acquisition="Box files hashed in SHA256SUMS", observable="Model parameters", model="see title", calib="Data public before the fit", predictive=v, scoring="Not a forecast; not scored.",
        abstention="n/a", internal=("INTERNAL_CONTEXT_R02.md#RF-7" if id_=="RF-7" else ""), sources=src,
        notes=("Two code paths agree: R02 Wolfram reproduces R02/R03 Python JSON (RF-1) and R04 (RF-2)." if id_ in ("RF-1","RF-2") else "Fit statistics are in INTERNAL CONTEXT only."))
add(id="CTC-R", kind="conditional theory curve", readiness="n/a", verification="PROVISIONAL", outcome="n/a", title="Elastic Rebound AP curve (DM/DH < z)", product="none (illustrative observer epoch)", acquisition="n/a",
    observable="AP = DM/DH at z = 0.295, 0.51, 0.706", model="closed periodic-scalar branch, illustrative parameters", calib="DESI values already read (retrospective comparison)", predictive="0.270264, 0.409992, 0.439783",
    scoring="Not scored (no likelihood; domain z ≤ 0.706 cannot reach Euclid bins).", abstention="n/a", sources="COSMOLOGY_MODEL_CHECK L140–150")
# ---------------- Synthetic tests ----------------
add(id="SYN-1", kind="synthetic test", readiness="n/a", verification="VERIFIED", outcome="PASS", title="Kinematic-dipole grid arithmetic", product="none (synthetic grid)", acquisition="n/a",
    observable="D_kin = [2 + x(1+α)]β on x ∈ [0.5, 2], α ∈ [0.5, 1.5]", model="kinematic dipole formula", calib="n/a", predictive="Grid 0.0034–0.0086; CatWISE-like point 0.0064696",
    scoring="PASS = Wolfram and Python agree to 1e-16 (R04 §1)", abstention="Not a Euclid prediction.", sources=f"{R4} L24–44")
add(id="SYN-2", kind="synthetic test", readiness="n/a", verification="VERIFIED", outcome="PASS", title="Angular-separation regression suite (catalogue tooling)", product="Euclid angular-separation candidate package R01", acquisition="zip sha256 f47e6a28…50fd",
    observable="Great-circle separation errors (deg)", model="n/a", calib="Suite fixed 2026-10-24/26", predictive="max random error 4.26e-14 deg", scoring="Table-3 suite all PASS (NUMERICAL_REVIEW §7)", abstention="n/a", sources="NUMERICAL_REVIEW.md §4, §7")

EXPO = {"prospective":"No target outcome exists or was inspected (DESI Y5 unpublished; Euclid DR1 products not opened by this bot). Release publicity is not a target outcome.",
        "conditional theory curve":"Calibration data (DESI DR2, Planck 2018) fully exposed by construction; Euclid BAO target outcome does not exist yet and was not inspected.",
        "retrospective fit":"Fully exposed: these are fits to already-public data.",
        "synthetic test":"No observational data involved."}
for r in rows:
    r["exposure"] = EXPO[r["kind"]]
    if r["id"].startswith("CTC-") and r["id"]!="CTC-R":
        r["covariance"] += ". Shared calibration: A = c/(H0 rd) is exactly degenerate with a common radial+transverse distance calibration (handoff 8925124 §3); a Euclid rd-convention or fiducial-cosmology offset common to DM and DH cannot be told apart from A. F_AP = DM/DH is A-independent. Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters)."
        r["observable"] += "; scale grid: n/a (BAO distances, no k-dependence)"

for r in rows:
    if r["id"] in ("CTC-5B","CTC-5P"):
        r["covariance"] = r["covariance"].replace("C_pred = full 8×8 Laplace predictive covariance diag(s)·R·diag(s), s = the ± values below and R from R02/wolfram/predcov_R02.json (computed 2026-11-12, callcov_*.wl)", "C_pred = diag(s_pred²) from chain half-widths; chain cross-correlations were not saved in R04, so they are ignored (declared approximation)").replace(" Predictive correlations: R02/wolfram/predcov_R02.json (near-rank-deficient; effective directions ≈ number of fitted parameters).","")

for r in rows:
    if r["scoring"].startswith("INTERNAL CONTEXT only"):
        r["scoring"] = "Two-valued: PASS iff the frozen condition in INTERNAL_CONTEXT_R02.md#" + r["id"] + " holds; FAIL otherwise (no grey zone). Condition text kept internal because it is significance-type."
    for f in ["cuts","mask","contaminants","estimator","covariance","calib","acquisition","product","observable","model","predictive","scoring","abstention"]:
        if not str(r.get(f,"")).strip():
            r[f] = {"retrospective fit":"n/a (retrospective fit to already-published values; see sources)","synthetic test":"n/a (synthetic engineering test; no observational data)"}.get(r["kind"],"n/a (see notes)")

for r in rows:
    if r["id"].startswith("E-CD-"):
        r["contaminants"] += "; magnification response (5s−2)κ not modelled (counts are not HSU convergence; handoff §5)"
