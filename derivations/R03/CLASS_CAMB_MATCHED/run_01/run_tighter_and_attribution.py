import json, sys, datetime, numpy as np, os
sys.path.insert(0,'.'); import engines as E, camb, classy
from classy import Class
E.CAMB_LEVEL['tighter']=dict(AccuracyBoost=3,lAccuracyBoost=3,lSampleBoost=3,k_per_logint=160)
E.CLASS_LEVEL['tighter']=dict(tol_background_integration=1e-12,tol_thermo_integration=1e-8,tol_perturbations_integration=1e-7,k_per_decade_for_pk=160,k_per_decade_for_bao=280,l_max_ur=68,sigma_k_per_decade=320)
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(n,f):
    t0=now()
    try: o,a=f(); o['status']='OK'; np.savez(f'runs/{n}.npz',**a)
    except Exception as e: o={'status':'FAILED','error':repr(e)}
    o['start_utc']=t0; o['end_utc']=now(); json.dump(o,open(f'runs/{n}.json','w'),indent=1,default=str); print(n,o['status'],o.get('error','')[:300],flush=True); return o
save('camb_tighter',lambda:E.camb_run('tighter'))
save('class_tighter',lambda:E.class_run('tighter'))
# A1: CAMB-only massive nu (deliberately unmatched)
A1=save('A1_camb_mnu006',lambda:E.camb_run('tight',cosmo_mod=dict(mnu=0.06,num_massive_neutrinos=1,nnu=3.044,standard_neutrino_neff=3.044)))
# A2: matched massive in CLASS using CAMB's actual readback
if A1['status']=='OK':
    deg=A1['nu_mass_degeneracies'][0]; nur=A1['num_nu_massless']; om=A1['omnuh2']; T=(4/11)**(1/3)
    save('A2_class_matched_massive',lambda:E.class_run('tight',mod={'N_ncdm':1,'deg_ncdm':deg,'T_ncdm':T,'N_ur':nur,'omega_ncdm':om}))
# A3: CAMB BBN helium alone
save('A3_camb_bbn_YHe',lambda:E.camb_run('tight',cosmo_mod=dict(YHe=None)))
# A3b: same-HyRec-family recombination sensitivity, only if supported by both installed builds
save('A3b_camb_hyrec',lambda:E.camb_run('tight',recomb='HyRec'))
save('A3b_class_hyrec',lambda:E.class_run('tight',mod={'recombination':'HyRec'}))
# A4: CLASS matter-source gauge definition left at its default (key removed), warranted because the historical script used defaults
save('A4_class_matter_source_default',lambda:E.class_run('tight',drop=('matter_source_in_current_gauge',)))
# A6: historical-configuration replay with CURRENT versions (current-version sensitivity, NOT historical reproduction)
def hist_camb():
    p=camb.CAMBparams(); p.set_cosmology(H0=67.5,ombh2=0.022,omch2=0.12); p.InitPower.set_params(As=2e-9,ns=0.965); p.NonLinear=camb.model.NonLinear_none
    p.set_matter_power(redshifts=[0.0],kmax=2.0); r=camb.get_results(p); kh,zz,pk=r.get_matter_power_spectrum(minkh=1e-4,maxkh=1.5,npoints=200)
    kc=kh*E.H; pc=pk[0]/E.H**3; P20=np.exp(np.interp(np.log(E.KH20),np.log(kc),np.log(pc)))
    o={'engine':'CAMB','version':camb.__version__,'params_dump':str(p),'sigma8':float(r.get_sigma8()[0]),'YHe':p.YHe,'mnu_omnuh2':p.omnuh2,'nnu':p.num_nu_massless+p.num_nu_massive,'num_massive':p.num_nu_massive,
       'Reionization':p.Reion.Reionization,'optical_depth':p.Reion.optical_depth if hasattr(p.Reion,'optical_depth') else None,'Omega_m':float(r.get_Omega('cdm')+r.get_Omega('baryon')+r.get_Omega('nu')),'Recomb':type(p.Recomb).__name__}
    return o,{'kh':kh,'pk_h':pk,'P20':P20}
def hist_class():
    d={'H0':67.5,'omega_b':0.022,'omega_cdm':0.12,'A_s':2e-9,'n_s':0.965,'YHe':0.245,'output':'mPk','P_k_max_1/Mpc':2.0}
    c=Class(); c.set(d); c.compute(); P20=np.array([c.pk_lin(k,0.0) for k in E.KH20])
    o={'engine':'CLASS','version':classy.__version__,'class_dict_passed':d,'sigma8':float(c.sigma8()),'Omega_m':float(c.Omega_m()),'Omega_Lambda':float(c.Omega_Lambda()),'readback':{k:str(v) for k,v in c.pars.items()}}
    c.struct_cleanup(); c.empty(); return o,{'P20':P20}
save('A6_hist_replay_camb',hist_camb); save('A6_hist_replay_class',hist_class)
