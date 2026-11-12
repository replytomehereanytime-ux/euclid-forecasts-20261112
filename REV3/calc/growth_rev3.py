"""sigma8, S8, f*sigma8 via CAMB at the REV3 REPLACEMENT flat-LCDM BAO+CMB posterior. A_s from Planck 2018 (ln10^10As=3.044+-0.014, ns=0.9649, tau=0.0544).
Also: 0.06 eV neutrino-variant background shift of DM/rd, DH/rd (CAMB rdrag, same H0, omega_b, total omega_m)."""
import sys,json; sys.path.insert(0,'.'); import numpy as np, camb
MODE=sys.argv[1] if len(sys.argv)>1 else 'rescale'
R=json.load(open(f'rows_rev3_{MODE}.json'))['REPLACEMENT']['LCDM']; ch=np.load(f'chain_LCDM_REPLACEMENT_{MODE}.npy')
LNAS,LNAS_SD,NS,TAU=3.044,0.014,0.9649,0.0544; ZS=[0.9,1.2,1.5,1.8]
def run(Om,h,ob,mnu=0.06,lnas=LNAS,want_fs8=True):
    onu=mnu/93.14; p=camb.CAMBparams(); p.set_cosmology(H0=100*h,ombh2=ob,omch2=Om*h*h-ob-onu,mnu=mnu,num_massive_neutrinos=1 if mnu>0 else 0,tau=TAU)
    p.InitPower.set_params(As=np.exp(lnas)/1e10,ns=NS); p.set_matter_power(redshifts=[0.0]+ZS[::-1],kmax=1.2); p.WantTransfer=True
    r=camb.get_results(p); s8=r.get_sigma8_0(); fs8=r.get_fsigma8()[::-1][1:] if want_fs8 else None
    d=r.get_derived_params(); DM=r.comoving_radial_distance(np.array(ZS)); DH=299792.458/r.hubble_parameter(np.array(ZS))
    return s8,s8*np.sqrt(Om/0.3),fs8,d['rdrag'],DM/d['rdrag'],DH/d['rdrag']
bf=R['bestfit']; Om,h,ob=bf['Om'],bf['h'],bf['ob']
s8,S8,fs8,rd6,DMr6,DHr6=run(Om,h,ob)
# A_s uncertainty: sigma8 ∝ sqrt(As) => d ln s8 = 0.5 d lnAs
sA=0.5*LNAS_SD
# parameter scatter from chain (fixed As), 200 draws
rng=np.random.default_rng(20261112); idx=rng.choice(len(ch),60,replace=False); S=[]
for i in idx:
    o,hh,bb=ch[i,0],ch[i,1],ch[i,4]; a=run(o,hh,bb,want_fs8=True); S.append([a[0],a[1]]+list(a[2]))
S=np.array(S)
# Planck-mean reference for calibration check
p8,pS8,pfs8,_,_,_=run(0.3166,0.6727,0.02236)
# neutrino variant: massless vs 0.06 eV at same H0, omega_b, total omega_m
_,_,_,rd0,DMr0,DHr0=run(Om,h,ob,mnu=0.0,want_fs8=False)
O={'bestfit':bf,'sigma8':s8,'S8':S8,'fsigma8':dict(zip(map(str,ZS),map(float,fs8))),
   'param_sd':{'sigma8':float(S[:,0].std()),'S8':float(S[:,1].std()),'fsigma8':dict(zip(map(str,ZS),map(float,S[:,2:].std(0))))},
   'As_frac_sd_on_sigma8':sA,'As_sd':{'sigma8':s8*sA,'S8':S8*sA},
   'total_sd':{'sigma8':float(np.hypot(S[:,0].std(),s8*sA)),'S8':float(np.hypot(S[:,1].std(),S8*sA)),'fsigma8':dict(zip(map(str,ZS),[float(np.hypot(a,b*sA)) for a,b in zip(S[:,2:].std(0),fs8)]))},
   'planck_mean_reference':{'sigma8':p8,'S8':pS8},
   'calibrated_to_planck_0.8111':{'factor':0.8111/p8,'sigma8':s8*0.8111/p8,'S8':S8*0.8111/p8},
   'nu006_shift':{'rdrag_massless':rd0,'rdrag_0.06':rd6,'DM/rd_frac(0.06/0 -1)':dict(zip(map(str,ZS),map(float,DMr6/DMr0-1))),'DH/rd_frac(0.06/0 -1)':dict(zip(map(str,ZS),map(float,DHr6/DHr0-1)))},
   'settings':{'lnAs':LNAS,'lnAs_sd':LNAS_SD,'ns':NS,'tau':TAU,'mnu':0.06,'camb':camb.__version__,'draws':60}}
json.dump(O,open(f'growth_rev3_{MODE}.json','w'),indent=1,default=float); print(json.dumps(O,indent=1,default=float))
