import csv, os, sys, collections, re
sys.path.insert(0, os.path.dirname(__file__)); import rows_r02 as R
OUT = "/workspace/r03-out/euclid_forecast_bot/R02/"
F = [("id","id"),("kind","label (exactly one)"),("readiness","readiness"),("verification","verification"),("outcome","outcome"),("branch","Lyα branch"),("title","title"),
     ("product","product / version / schema"),("acquisition","acquisition UTC / hash"),("cuts","sample and quality cuts"),("observable","observable / units / redshift & scale grid"),
     ("model","model and priors"),("calib","calibration data cutoff"),("exposure","exposure to target outcomes"),("mask","selection and mask operator"),("contaminants","contaminants"),
     ("estimator","estimator"),("covariance","covariance / shared calibration"),("predictive","predictive distribution (with uncertainty)"),("scoring","scoring / exclusions"),
     ("abstention","abstention rule"),("internal","internal-context pointer"),("sources","sources"),("notes","notes")]
with open(OUT+"FORECAST_TABLE_R02.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow([h for _,h in F])
    for r in R.rows: w.writerow([r[k] for k,_ in F])
c_kind=collections.Counter(r["kind"] for r in R.rows); c_kr=collections.Counter((r["kind"],r["readiness"]) for r in R.rows)
L=["# FORECAST_TABLE_R02 — private branch on top of R01 (recorded internally at the time; nothing posted, published or timestamped)","",
"Built 2026-11-12 from the author's handoff 8925124 (received 09:37:42 UTC) via Coordinator. R01 (`../FORECASTS_R01.md`, sha256 e27fc48e…48efb) is preserved unchanged; this is a separately dated branch. Significance-, p-value-, exceedance- and coincidence-type content appears only in `INTERNAL_CONTEXT_R02.md`.","",
"## Counts",f"- Rows: {len(R.rows)}. By label: "+", ".join(f"{k} {v}" for k,v in c_kind.items())+".",
"- By label × readiness: "+"; ".join(f"{k[0]} / {k[1]}: {v}" for k,v in sorted(c_kr.items()))+".",
"- Outcomes: all forecasts NOT_RUN (synthetic tests: PASS; retrospective fits: n/a).","",
"## Effective independence (read before counting)",
"- **These rows are not independent tests.** The D-* rows are sub-rules of six DESI forecasts that share one DESI Y5 data release; a/b pairs of the same quantity are nested.",
"- **Distance curves:** the 9 READY conditional theory curves carry 9 × 4 redshifts × 2 distances = 72 numbers (F_AP = DM/DH is derived and never scored separately). Within one curve, every entry is a function of the fitted parameters: BAO-only ΛCDM has exactly 2 (Ωm, A); ΛCDM+CMB effectively 2 (ω_b is pinned by the prior); wCDM and oΛCDM about 3. The full predictive covariance confirms this: it has only 2–3 non-negligible eigen-directions per curve; the rest are at the 0.001 rounding level of the stored correlations (`wolfram/predcov_rank_R02.json`). PRIMARY and REPLACEMENT branches use the same data except one Lyα point, so they are near-duplicates, not two tests. All curves share the DESI DR2 BAO calibration; the CMB-based ones share Planck 2018 too.",
"- **Shared calibration:** A = c/(H0 rd) is exactly degenerate with a common radial/transverse calibration (handoff §3). After projecting that nuisance out, BAO-only ΛCDM keeps one identifiable direction (Ωm, through the shape/F_AP). Singular values for a real Euclid covariance cannot be computed until Euclid publishes one. Rank without that covariance is not a precision forecast.",
"- **The handoff's 60-entry distance package and 24-target register are NOT these rows.** Their bytes (Euclid_Candidate_Prediction_Register_20261112.zip, Geometry_Joint_Band_Addendum_20261112.zip and 7 others) are not on the box or on Drive (HANDOFF_8925124_INVENTORY.md §1–3). **No claim is made that any of the 24 register rows were run.**","",
"## Summary table","| id | label | readiness | branch | title | tested by |","|---|---|---|---|---|---|"]
for r in R.rows:
    tb = "DESI Y5 (2027)" if r["id"].startswith("D-") else ("Euclid BAO on DR1 Complete (mid-2027+)" if r["id"].startswith("CTC-") and r["id"]!="CTC-R" else ("Euclid DR1 Complete (mid-2027)" if r["id"]=="E-L-P6" else ("Euclid Foundation catalogues (binding TBD)" if r["id"].startswith("E-") else "—")))
    if r["id"]=="D-P8c": tb="SH0ES through 2027"
    L.append(f"| {r['id']} | {r['kind']} | {r['readiness']} | {r['branch']} | {r['title']} | {tb} |")
L += ["","## Freeze blocks (one per row)"]
for r in R.rows:
    L.append(f"### {r['id']} — {r['title']}"); L.append(f"**{r['kind']} · {r['readiness']} · {r['verification']} · {r['outcome']} · branch {r['branch']}**"); L.append("")
    for k,h in F[7:]:
        if r[k]: L.append(f"- **{h}:** {r[k]}")
    L.append("")
open(OUT+"FORECAST_TABLE_R02.md","w").write("\n".join(L))
print(len(R.rows), dict(c_kind), dict(c_kr))
