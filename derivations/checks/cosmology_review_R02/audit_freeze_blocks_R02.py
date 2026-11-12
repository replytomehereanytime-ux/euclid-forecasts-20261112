# Per-block completeness + label audit of the 43 R02 freeze blocks (six required elements). Heuristic flags + reviewer notes.
import csv, re, json
T=list(csv.DictReader(open('/workspace/r03-out/euclid_forecast_bot/R02/FORECAST_TABLE_R02.csv')))
EL={'observable+units':['observable / units / redshift & scale grid'],'cuts':['sample and quality cuts'],
    'model+params':['model and priors'],'uncertainty/cov':['predictive distribution (with uncertainty)','covariance / shared calibration'],
    'selection':['selection and mask operator'],'scoring/failure':['scoring / exclusions','abstention rule']}
NOTE={
 'D-P8c':'LABEL RISK: if no new SH0ES H0 is published after 2026-10-13 by 2027-12-31, rule scores an already-public value (R22 73.04 lies inside [72.5,73.5]); abstention field is a note, not a rule. Needs explicit NOT_RUN for no post-forecast SH0ES result.',
 'D-P1a':'Observable/prediction internal-only (significance-type); complete in INTERNAL_CONTEXT, two-valued.',
 'D-P1b':'as D-P1a','D-P2b':'as D-P1a; needs sigma(w_p) definition if asymmetric','D-P8b':'as D-P1a; T needs which DESI combination (stated in DESI_PREDICTIONS_source, not in table)','D-P8d':'as D-P8b',
 'D-P2a':'68% label pending the author (stated).','D-P3a':'68% label pending the author (stated).','D-P4a':'68% label pending the author.','D-P8a':'68% label pending the author.',
 'D-P7':'NOT READY correctly: hemisphere axis coordinates TBD.',
 'E-CD-P1':'NOT READY correctly (cuts/mask/estimator/cov TBD; Foundation binding TBD).','E-CD-P2':'as E-CD-P1','E-CD-P3':'as E-CD-P1; binning variable TBD','E-CD-P4':'as E-CD-P1','E-CD-P5':'as E-CD-P1',
 'E-L-P6':'NOT READY correctly; DR1 Complete label correct.','E-PHZ-1':'NOT READY correctly; Foundation PHZ label consistent with Foundation contents; truth set TBD.',
 'CTC-5B':'Complete but C_pred diag-only (declared). Reviewer MCMC supplies full 8x8 correlation if the author wants it.',
 'CTC-5P':'NOT READY correctly (no band). Reviewer MCMC band available (not inserted).',
 'CTC-R':'Not scored; illustrative; label OK.',
}
rows=[]
for r in T:
    rid=r['id']; lab=r['label (exactly one)']; rd=r['readiness']; st={}
    for k,cols in EL.items():
        txt=' '.join(r[c] for c in cols)
        if lab in ('retrospective fit','synthetic test') or rid=='CTC-R': st[k]='n/a-ok'
        elif 'TBD' in txt or 'MISSING' in txt: st[k]='TBD'
        elif 'INTERNAL CONTEXT' in txt or 'INTERNAL_CONTEXT' in txt: st[k]='internal'
        elif '(external' in txt or "DESI's" in txt or 'Euclid' in txt and 'external' in txt: st[k]='external-delegated'
        else: st[k]='present'
    rel='Complete' if 'DR1 Complete' in r['product / version / schema'] and 'NOT Foundation' in r['product / version / schema'] or 'Not in Foundation' in r['product / version / schema'] else ('Foundation' if 'Foundation' in r['product / version / schema'] else '-')
    complete = all(v!='TBD' for v in st.values())
    ok_ready = (complete or rd!='READY')
    rows.append({'id':rid,'label':lab,'readiness':rd,'release':rel,**st,'complete':complete,'readiness_consistent':ok_ready,'reviewer_note':NOTE.get(rid,'')})
with open('audit_freeze_blocks_R02.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(sum(r['complete'] for r in rows),'complete;',sum(not r['readiness_consistent'] for r in rows),'READY-but-incomplete')
for r in rows: print(r['id'],r['label'][:12],r['readiness'],r['release'],'complete' if r['complete'] else 'INCOMPLETE',[k for k in EL if r[k]=='TBD'])
