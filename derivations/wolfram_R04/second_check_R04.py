"""Blank-context second check: recompute key numbers from formulas only, then compare to the Wolfram values (tolerance 1e-6 rel)."""
import numpy as np, json
from scipy.integrate import quad
from scipy.stats import chi2, norm, beta as B
c=299792.458; b=369.82/c
mine={
 'beta':b,'Dkin_CatWISE_1.529_1.122':(2+1.529*2.122)*b,'Dkin_CatWISE_1.755_1.122':(2+1.755*2.122)*b,
 'Dkin_grid_x1.0_a1.0':(2+1*2)*b,'Dkin_grid_x0.5_a0.5':(2+0.5*1.5)*b,'Dkin_grid_x2.0_a1.5':(2+2*2.5)*b,
 'CP1_95':1-0.05**(1/2000),'CP2_95':B.ppf(0.975,1,2000),
 'P1_2.7_1.5':2.7*1.5**.5,'P1_2.7_2':2.7*2**.5,'P1_3.2_1.5':3.2*1.5**.5,'P1_3.2_2':3.2*2**.5,
 'Xi0_cM1.3':np.exp(1.3*np.log(1/0.3065)/(6*0.6935)),'cM_from_Xi0_1.4':6*0.6935*np.log(1.4)/np.log(1/0.3065),
 'n_eq25':-3/np.log(0.3065),'n_alphaM':-3*0.6935/np.log(0.3065),
 'sigma_dchi2_2.18806':norm.isf(chi2.sf(2.1880571551506804,2)/2),'sigma_dchi2_1.77432':norm.isf(chi2.sf(1.7743222667005227,2)/2),
}
om=0.315191868; E=lambda z:np.sqrt(om*(1+z)**3+1-om)
mine['AP_ratio_0.51']=E(0.51)*quad(lambda t:1/E(t),0,0.51,epsabs=1e-14)[0]/0.409992
wl={'beta':0.0012335867368618058,'Dkin_CatWISE_1.529_1.122':0.006469592517767741,'Dkin_CatWISE_1.755_1.122':0.007061186176338031,
 'Dkin_grid_x1.0_a1.0':0.004934346947447223,'Dkin_grid_x0.5_a0.5':0.003392363526369966,'Dkin_grid_x2.0_a1.5':0.00863510715803264,
 'CP1_95':0.0014967448951882512,'CP2_95':0.0018427397934059897,'P1_2.7_1.5':3.3068111527572905,'P1_2.7_2':3.818376618407357,'P1_3.2_1.5':3.919183588453085,'P1_3.2_2':4.525483399593905,
 'Xi0_cM1.3':1.4469446061093594,'cM_from_Xi0_1.4':1.1839463430400998,'n_eq25':2.5369173832659473,'n_alphaM':1.7593522052949344,
 'sigma_dchi2_2.18806':0.9643614465804947,'sigma_dchi2_1.77432':0.8206894072394678,'AP_ratio_0.51':1.4479904620853583}
sc=json.load(open('crosscheck_scipy_R04_output.json'))
fitcmp={'dchi2_new':(2.1880571551506804,sc['new_lya']['dchi2']),'dchi2_old':(1.7743222667005227,sc['old_lya']['dchi2']),
 'w0_new':(-0.7674047590084129,sc['new_lya']['CPL_best'][2]),'wa_new':(-0.8243737552147912,sc['new_lya']['CPL_best'][3]),
 'LCDM_Om_new':(0.3242805186501144,sc['new_lya']['LCDM_best'][0]),
 'LCDM_DMrd_1.3':(27.31792427434365,None),'CPL_DMrd_1.3':(27.289092693673506,sc['pred_new_CPL']['1.3'][0]),'CPL_DHrd_1.3':(14.019556436233685,sc['pred_new_CPL']['1.3'][1])}
rows=[]
for k in wl:
    r=abs(mine[k]-wl[k])/abs(wl[k]); rows.append((k,wl[k],mine[k],r,'PASS' if r<1e-6 else 'FAIL'))
for k,(a,s) in fitcmp.items():
    if s is None: continue
    tol=1e-3 if k.startswith(('w0','wa')) else 1e-5
    r=abs(a-s)/abs(a); rows.append((k,a,s,r,'PASS' if r<tol else 'FAIL'))
for r in rows: print('%-26s WL=%.10g  2nd=%.10g  rel=%.2e  %s'%r)
print('ALL PASS' if all(r[4]=='PASS' for r in rows) else 'SOME FAIL')
