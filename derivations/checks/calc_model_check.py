# EUCLID-OVERNIGHT-20261112-R01 model/equation check. Inputs only from cited artifacts/published sources.
import json, math
import numpy as np
from scipy import integrate, stats
out={}
# C1: DESI box fit significance (desi_r01/fit_results.json): delta_chi2=1.6527973488095853, 2 extra params
d=1.6527973488095853
p=stats.chi2.sf(d,2); out['C1_desi_box_fit']={'delta_chi2':d,'dof':2,'p':p,'sigma_two_sided':stats.norm.isf(p/2)}
# C2: P1 volume scaling claim: 3.1 sigma * sqrt(V ratio 1.5..2)
out['C2_P1_sqrtV']={'1.5x':3.1*math.sqrt(1.5),'2.0x':3.1*math.sqrt(2.0)}
# C3: P3/P4 error-shrink consistency: DR2 1sigma w0 0.057, wa 0.22 (+DESY5 row, as quoted in DESI_PREDICTIONS_source) shrunk 20-30%
out['C3_shrink']={'w0_sigma_after_20pct':0.057*0.8,'w0_sigma_after_30pct':0.057*0.7,'wa_sigma_after_20pct':0.22*0.8,'wa_sigma_after_30pct':0.22*0.7,
  'stated_P3_w0_pm':0.10,'stated_P3_wa_pm':0.35,'Om_DR2_sigma':0.0086,'Om_after_20pct':0.0086*0.8,'stated_P4_Om_pm':0.010}
# C4: kinematic count dipole D=[2+x(1+alpha)]beta with CatWISE inputs quoted in X04 audit
beta=369.82/299792.458
out['C4_Dkin_CatWISE']={'beta':beta,'x1.529_a1.122':(2+1.529*(1+1.122))*beta,'x1.755_a1.122':(2+1.755*(1+1.122))*beta,
  'note':'Euclid x (count slope) and alpha (spectral/flux index) for any Foundation selection are NOT in any artifact -> Euclid D_kin not computable'}
# C5: P5 mock bound: 0 exceedances in 2000 -> exact one-sided 95% Clopper-Pearson upper limit
out['C5_P5_0of2000']={'CP95_upper':1-0.05**(1/2000),'rule_of_three':3/2000}
# C6: freeze-addendum z=1 latent moments internal consistency (ratio-of-means vs stated means)
DM,DH,FAP,DV=22.81099854,16.81529378,1.35658181,20.60614078
out['C6_geometry_z1']={'DM/DH_from_means':DM/DH,'stated_F_AP':FAP,'DV_from_means':(1*DM**2*DH)**(1/3),'stated_DV':DV}
DMg,DHg,FAPg=22.893376,16.847829,1.358831
out['C6b_cmb_gaussian_z1']={'DM/DH_from_means':DMg/DHg,'stated_F_AP':FAPg}
# C7: flat LCDM F_AP=DM/DH vs Elastic Rebound conditional AP (Forecast Record), Om=0.315191868 from same record
Om=0.315191868
E=lambda z: math.sqrt(Om*(1+z)**3+1-Om)
reb={0.295:0.270264,0.51:0.409992,0.706:0.439783}
c7={}
for z,ap in reb.items():
    chi=integrate.quad(lambda x:1/E(x),0,z)[0]
    F=E(z)*chi
    c7[str(z)]={'F_AP_flatLCDM':F,'Rebound_AP':ap,'ratio_LCDM_over_Rebound':F/ap,'Rebound_AP_lt_z':ap<z,'LCDM_F_AP_gt_z':F>z}
out['C7_AP']=c7
# C8: LCDM baseline at DESI DR2 Table-4 z=0.51 using box file values (DM/rs, DH/rs) -> observed F_AP
out['C8_DESI_DR2_FAP_obs']={'0.51':13.58758434/21.86294686,'0.706':17.35069094/19.45534918,'0.934':21.57563956/17.64149464}
# C9: HSU distance-inversion illustration (HSU_Distance_Growth_Audit F3): eps=0.05
e=0.05
out['C9_HSU_inverse']={'pos_pole':1/(1+e),'neg_pole':1/(1-e),'mean_atanh':math.atanh(e)/e}
json.dump(out,open('calc_model_check_output.json','w'),indent=1)
print(json.dumps(out,indent=1))
