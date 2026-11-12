import json,csv
W=json.load(open('wolfram/fullrs_fits_R03.json')); F=json.load(open('calc/fullrs_r03_output.json'))
G=['0.9','1.2','1.5','1.8']; pn={'LCDM':['Om','h','ob'],'wCDM':['Om','h','w','ob'],'oLCDM':['Om','Ok','h','ob']}
tit={'LCDM':'Flat ΛCDM, BAO + compressed CMB','wCDM':'Constant-w (wCDM), BAO + compressed CMB','oLCDM':'Curved ΛCDM (oΛCDM), BAO + compressed CMB'}
ids={'LCDM':'CTC-2','wCDM':'CTC-3','oLCDM':'CTC-4'}
rows=[]
for m in ['LCDM','wCDM','oLCDM']:
    for br,s in [('PRIMARY','P'),('REPLACEMENT','B')]:
        d=W[m][br]; ps=', '.join('%s %.5f ± %.5f'%(n,b,e) for n,b,e in zip(pn[m],d['best'],d['sig']))
        pred='; '.join('z=%s: DM/rd %.4f ± %.4f, DH/rd %.4f ± %.4f'%(z,d['pred'][z][0],d['predsig'][2*i],d['pred'][z][1],d['predsig'][2*i+1]) for i,z in enumerate(G))
        extra=''
        if m=='wCDM':
            w=F['mcmc'][f'wCDM_{br}']['w']; extra=' MCMC (emcee 32×5000, full r_s): w median %.4f, s.d. %.4f, 68%% [%.4f, %.4f].'%(w['median'],w['std'],*w['q16_84'])
        rows.append({'id':ids[m]+s+'-R03','replaces_held':ids[m]+s,'label':'conditional theory curve','branch':br,'title':tit[m]+' (R03, r_s to ∞)','chi2_INTERNAL':'%.4f'%d['chi2'],
          'best_fit_laplace':ps,'predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))':pred,'notes':'Wolfram MCP kernel 15.0.1, R03/wolfram/common_R03_fullrs.wl (R02 common with one line changed); Hessian positive-definite = True (kernel output).'+extra})
for br,s in [('PRIMARY','P'),('REPLACEMENT','B')]:
    b=F['mcmc'][f'CPL_{br}']['bands']; pr=F['mcmc'][f'CPL_{br}']['params']
    rows.append({'id':'CTC-5%s-R03'%s,'replaces_held':'CTC-5'+s,'label':'conditional theory curve','branch':br,'title':'CPL (w0waCDM), BAO + compressed CMB (R03 fresh emcee, r_s to ∞)','chi2_INTERNAL':'%.4f'%F['fits'][br]['CPL']['chi2'],
      'best_fit_laplace':'posterior medians [68%]: '+', '.join('%s %.4f [%.4f, %.4f]'%(n,v[2],v[1],v[3]) for n,v in pr.items()),
      'predictive (Laplace ±1 s.d., Gaussian N(m,C_pred))':'MCMC median [68%] {95%}: '+'; '.join('z=%s: DM/rd %.3f [%.3f, %.3f] {%.3f, %.3f}, DH/rd %.3f [%.3f, %.3f] {%.3f, %.3f}'%(z,b[z]['DM/rd'][2],b[z]['DM/rd'][1],b[z]['DM/rd'][3],b[z]['DM/rd'][0],b[z]['DM/rd'][4],b[z]['DH/rd'][2],b[z]['DH/rd'][1],b[z]['DH/rd'][3],b[z]['DH/rd'][0],b[z]['DH/rd'][4]) for z in G),
      'notes':'emcee 40×10000, burn 2500, thin 5; Laplace NOT used (step-dependent Hessian). Full 8×8 C_pred in calc/fullrs_r03_output.json.'})
with open('RECOMPUTED_ROWS_R03.csv','w',newline='') as f: w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r['id'],r['chi2_INTERNAL'],r['best_fit_laplace'][:120])
