"""CLASS (classy 3.4.2.0, /workspace/r05_cosmo_env, read-only use) cross-check of R03 distances and sound horizons at the same parameters."""
import numpy as np, json, sys, time; sys.path.insert(0,'.'); import cplmodel_r03 as M
from classy import Class
import classy
M.RSMODE='full'
F=json.load(open('fullrs_r03_output.json')); W=json.load(open('../wolfram/fullrs_fits_R03.json'))
def run(th):
    Om,h,w0,wa,ob=th; c=Class()
    p={'h':h,'omega_b':ob,'omega_cdm':Om*h*h-ob,'N_ur':3.046,'T_cmb':2.7255,'output':'','YHe':0.245}
    if not (w0==-1 and wa==0): p.update({'Omega_Lambda':0.0,'w0_fld':w0,'wa_fld':wa,'use_ppf':'yes'})
    c.set(p); c.compute(); d=c.get_current_derived_parameters(['rs_d','z_d','rs_rec','z_rec','ra_rec'])
    out={'derived':d,'z':{}}
    for z in [0.9,1.2,1.3,1.5,1.8]:
        DMc=c.angular_distance(z)*(1+z); DHc=1/c.Hubble(z)
        p5=M.pred(np.array(th),[z])[z]; rdf=float(M.rdf(Om,h,ob)); DMm=p5[0][0]*rdf; DHm=p5[1][0]*rdf
        out['z'][str(z)]={'DM_rel':DMm/DMc-1,'DH_rel':DHm/DHc-1,'DMrd_formula_vs_CLASS_rsd':p5[0][0]/(DMc/d['rs_d'])-1,'DHrd_formula_vs_CLASS_rsd':p5[1][0]/(DHc/d['rs_d'])-1}
    rdf=float(M.rdf(Om,h,ob)); out['rd_formula']=rdf; out['rd_formula_vs_CLASS_rs_d']=rdf/d['rs_d']-1
    # my r_s(z*) integral evaluated at CLASS z_rec (like-for-like)
    zs=d['z_rec']; a1=1/(1+zs); x,wg=np.polynomial.legendre.leggauss(96); a=a1*(x+1)/2
    f=1/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4*a))/(a*a*M.E(1/a-1,Om,h,w0,wa)); rsm=M.c/(100*h)*a1*np.sum(wg*f)/2
    out['rs_star_R03_at_CLASS_zrec']=rsm; out['rs_star_R03_vs_CLASS_rs_rec']=rsm/d['rs_rec']-1
    # truncated version at same z for reference
    u0=np.log1p(zs); u1=np.log1p(1e5); u=u0+(u1-u0)*(x+1)/2; zz=np.expm1(u); ft=(1+zz)/np.sqrt(3*(1+31500*ob*(2.7255/2.7)**-4/(1+zz)))/M.E(zz,Om,h,w0,wa); rst=M.c/(100*h)*(u1-u0)*np.sum(wg*ft)/2
    out['rs_star_trunc_vs_CLASS_rs_rec']=rst/d['rs_rec']-1
    c.struct_cleanup(); return out
O={'classy':getattr(classy,'__version__','3.4.2.0'),'cases':{}}
L=W['LCDM']['REPLACEMENT']['best']; O['cases']['LCDM_REPL_fullrs']=run([L[0],L[1],-1,0,L[2]])
Wc=W['wCDM']['REPLACEMENT']['best']; O['cases']['wCDM_REPL_fullrs']=run([Wc[0],Wc[1],Wc[2],0,Wc[3]])
x=F['fits']['PRIMARY']['CPL']['x']; O['cases']['CPL_PRIM_fullrs_best']=run(x)
O['cases']['LCDM_PRIM_R02_old_best']=run([0.3239712387770484,0.6986764715110352,-1,0,0.022280652121375474])
# CPL bands: 60 chain points, max rel diff of DM, DH (CLASS vs R03), and DM/rd with formula rd vs CLASS rs_d
ch=np.load('fullrs_cpl_chain_PRIMARY_R03.npy'); idx=np.random.default_rng(20261112).choice(len(ch),60,replace=False); mx={'DM':0,'DH':0,'rd':0,'DMrd':0}
for i in idx:
    o=run(list(ch[i])); mx['DM']=max(mx['DM'],max(abs(v['DM_rel']) for v in o['z'].values())); mx['DH']=max(mx['DH'],max(abs(v['DH_rel']) for v in o['z'].values()))
    mx['rd']=max(mx['rd'],abs(o['rd_formula_vs_CLASS_rs_d'])); mx['DMrd']=max(mx['DMrd'],max(abs(v['DMrd_formula_vs_CLASS_rsd']) for v in o['z'].values()))
O['CPL_PRIMARY_chain_60pts_maxabs_rel']=mx
json.dump(O,open('class_crosscheck_r03_output.json','w'),indent=1)
for k,v in O['cases'].items(): print(k,'rd_formula/CLASS-1 %.2e'%v['rd_formula_vs_CLASS_rs_d'],'rs*(R03 full)/CLASS-1 %.2e'%v['rs_star_R03_vs_CLASS_rs_rec'],'trunc %.2e'%v['rs_star_trunc_vs_CLASS_rs_rec'],'max DM %.1e DH %.1e'%(max(abs(x['DM_rel']) for x in v['z'].values()),max(abs(x['DH_rel']) for x in v['z'].values())))
print(mx)
