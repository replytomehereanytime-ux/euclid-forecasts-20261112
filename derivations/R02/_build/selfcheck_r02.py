"""R02 automated self-check. Run: python3 _build/selfcheck_r02.py  (box python, no installs)."""
import csv, json, re, hashlib, os, sys
B="/workspace/r03-out/euclid_forecast_bot/"; R=B+"R02/"
res=[]; ok=lambda name,cond,detail="": res.append((name,"PASS" if cond else "FAIL",detail))
rows=list(csv.DictReader(open(R+"FORECAST_TABLE_R02.csv")))
LAB={"prospective","retrospective fit","synthetic test","conditional theory curve"}
ok("C1 row count 43", len(rows)==43, str(len(rows)))
ok("C2 exactly one of 4 labels per row", all(r["label (exactly one)"] in LAB for r in rows))
ok("C3 unique ids", len({r["id"] for r in rows})==len(rows))
FREEZE=["product / version / schema","acquisition UTC / hash","sample and quality cuts","observable / units / redshift & scale grid","model and priors","calibration data cutoff","exposure to target outcomes","selection and mask operator","contaminants","estimator","covariance / shared calibration","predictive distribution (with uncertainty)","scoring / exclusions","abstention rule"]
empty=[(r["id"],f) for r in rows for f in FREEZE if not r[f].strip()]
ok("C4 all 14 freeze fields non-empty", not empty, str(empty[:6]))
bad=[r["id"] for r in rows if r["readiness"]=="READY" and not ("PASS" in r["scoring / exclusions"] and "FAIL" in r["scoring / exclusions"])]
ok("C5 every READY rule has PASS and FAIL", not bad, str(bad))
ok("C6 forecast outcomes NOT_RUN", all(r["outcome"]=="NOT_RUN" for r in rows if r["label (exactly one)"] in ("prospective","conditional theory curve") and r["readiness"]!="n/a"))
# forbidden wording outside INTERNAL_CONTEXT
PAT=re.compile(r"\d\s*σ|σ(?!8)|(?i:sigma)|(?<![\w])p\s*[=≥≤<>]\s*0\.|(?i:p-value)(?![- ]type|-,| or exceedance| or coincidence)|(?i:\bsignificant\b)|(?i:coincidence)(?!-type)")
hits=[]
for f in ["FORECAST_TABLE_R02.md","FORECAST_TABLE_R02.csv","UNSUPPORTED_MODELS_R02.md","UNSUPPORTED_MODELS_R02.csv","R02_NOTES.md"]:
    for i,l in enumerate(open(R+f),1):
        for m in PAT.finditer(l): hits.append(f"{f}:{i}:{l[max(0,m.start()-25):m.end()+15].strip()}")
ok("C7 no σ / p-value / significance / coincidence claims outside INTERNAL_CONTEXT (σ8 amplitude allowed)", not hits, "; ".join(hits[:8]))
ok("C8 INTERNAL_CONTEXT clearly marked", open(R+"INTERNAL_CONTEXT_R02.md").readline().startswith("# INTERNAL CONTEXT"))
# numbers: CTC Laplace rows vs Wolfram raw outputs and predcov json
raw=open(R+"wolfram/raw_outputs_R02.txt").read(); rawnums=[float(x) for x in re.findall(r"-?\d+\.\d{5,}",raw)]
pc=json.load(open(R+"wolfram/predcov_R02.json")); mism=[]; n=0
for r in rows:
    if r["id"] in pc:
        pairs=re.findall(r"(\d+\.\d+) ± (\d+\.\d+)", r["predictive distribution (with uncertainty)"])
        sig=pc[r["id"]]["predsig"]
        if len(pairs)!=8: mism.append((r["id"],"npairs",len(pairs))); continue
        for (m,s),s2 in zip(pairs,sig):
            n+=1
            if abs(float(s)-s2)>5e-5: mism.append((r["id"],s,s2))
            if not any(abs(float(m)-x)<=5e-5 for x in rawnums): mism.append((r["id"],"mean not in raw",m))
ok("C9 CTC-1..4 means match raw_outputs_R02.txt and ± match predcov_R02.json (4 dp)", not mism and n==64, f"{n} pairs checked; {mism[:5]}")
# q95 quantiles
try:
    from scipy.stats import chi2; q={2:5.9915,4:9.4877,6:12.5916,8:15.5073,12:21.0261}
    ok("C10 q95 chi-square quantiles", all(abs(chi2.ppf(.95,k)-v)<1e-4 for k,v in q.items()))
except Exception as e: ok("C10 q95 chi-square quantiles", False, "scipy unavailable: "+str(e))
# predcov sanity: symmetric, unit diag, PSD within rounding
import numpy as np; bad=[]
for k,v in pc.items():
    if k.startswith("_"): continue
    Rm=np.array(v["predcorr"]); 
    if not (np.allclose(Rm,Rm.T) and np.allclose(np.diag(Rm),1) and np.linalg.eigvalsh(Rm).min()>-5e-3): bad.append(k)
ok("C11 predictive correlation matrices symmetric, unit-diagonal, PSD within 0.001 rounding", not bad, str(bad))
# frozen files unchanged
R01={"FORECASTS_R01.md":"e27fc48ebdc6cce174f846930d46b56df74fd35a9109714d04cb9a867fd48efb","FORECAST_TABLE_R01.csv":"a36e5dde919a55bf67bc66dd81bd390eb3e98e02cc1a58670320a233228af3a3","POSTING_ABSTRACT_R01.md":"de64b48d24601aac24bf9adf3fe6a363c3771db1bdab916f560933bfc1714337","ZENODO_METADATA_DRAFT_R01.json":"3626a2574f0920bab453ee84bd84c24bea47008ff117cc869b8c6723bccd6053","WOLFRAM_CHECKS_R01.md":"b75211780592f1bfb6e01d06fb6eb1404526f9ea78d33a1e58b80699319cd259","SHA256SUMS":"41a04f023f5adc28c07db9af157b2a198e2ef4a28fc1950fb1b69f2e197d287a"}
sh=lambda p: hashlib.sha256(open(p,"rb").read()).hexdigest()
ch=[f for f,h in R01.items() if sh(B+f)!=h]
ok("C12 R01 frozen files unchanged", not ch, str(ch))
X="/workspace/r03-out/euclid_20261112/xact_R05/"; badx=[]
for l in open(X+"SHA256SUMS"):
    h,f=l.split(); 
    if sh(X+f)!=h: badx.append(f)
ok("C13 R05 files match their SHA256SUMS", not badx, str(badx))
ok("C14 R04 results file hash", sh("/workspace/r03-out/euclid_20261112/wolfram_R04/WOLFRAM_RESULTS_R04.md")=="2da105d6a7cf3830cf60fd62afc89a2eafb174cb4d57412c48569ea7f8a10ac9")
# label counts statement in notes matches table
from collections import Counter; c=Counter(r["label (exactly one)"] for r in rows)
notes=open(R+"R02_NOTES.md").read()
ok("C15 counts in R02_NOTES match table", f"prospective {c['prospective']}" in notes and f"conditional theory curve {c['conditional theory curve']}" in notes and f"retrospective fit {c['retrospective fit']}" in notes and f"synthetic test {c['synthetic test']}" in notes, str(dict(c)))
ok("C16 no API-key-like strings in R02 files", not any(re.search(r"\b[A-Z0-9]{6}-[A-Z0-9]{10}\b|api[_-]?key\s*[:=]\s*\S{8,}",open(os.path.join(dp,f),errors="ignore").read(),re.I) for dp,_,fs in os.walk(R) for f in fs if not f.endswith((".pyc",".bak_pre_cov"))))
ok("C17 unsupported table has 10 models in the author's order", [r["model"].split(" (")[0] for r in csv.DictReader(open(R+"UNSUPPORTED_MODELS_R02.csv"))]==["constant-w","CPL","spatial curvature","massive neutrinos","Hu–Sawicki f(R)","Jordan–Brans–Dicke","nDGP","k-mouflage","mixed cold + warm DM","decaying DM"])
for r in res: print(f"{r[1]}  {r[0]}" + (f"  [{r[2]}]" if r[2] else ""))
print(f"\n{sum(r[1]=='PASS' for r in res)}/{len(res)} PASS")
