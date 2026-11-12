"""Matched CLASS/CAMB engines per PROTOCOL.md (source_inputs_8933784, sha 1d7bb1ef...). Physical k [1/Mpc], P [Mpc^3]."""
import numpy as np, json, copy, time
import camb, classy
from classy import Class
from camb import model
H=0.675; ZS=[0.0,1.0,3.0]
KCMP=np.geomspace(0.002,1.0,201); KH20=np.geomspace(0.002,1.0,20)
KD1=np.geomspace(1e-5,30.0,12001); KD2=np.geomspace(1e-5,30.0,24001)
ZBG=np.array([0.0,0.5,1.0,1.5,2.0,3.0]); ZTH=np.array([200.,400.,600.,800.,900.,1000.,1050.,1089.,1100.,1200.,1400.,1600.,2000.,2500.,3000.,5000.])
CAMB_LEVEL={'base':dict(AccuracyBoost=1,lAccuracyBoost=1,lSampleBoost=1,k_per_logint=40),'tight':dict(AccuracyBoost=2,lAccuracyBoost=2,lSampleBoost=2,k_per_logint=80)}
CLASS_LEVEL={'base':dict(tol_background_integration=1e-10,tol_thermo_integration=1e-6,tol_perturbations_integration=1e-5,k_per_decade_for_pk=40,k_per_decade_for_bao=70,l_max_ur=17,sigma_k_per_decade=80),
             'tight':dict(tol_background_integration=1e-11,tol_thermo_integration=1e-7,tol_perturbations_integration=1e-6,k_per_decade_for_pk=80,k_per_decade_for_bao=140,l_max_ur=34,sigma_k_per_decade=160)}
CLASS_BASE={'H0':67.5,'omega_b':0.022,'omega_cdm':0.12,'Omega_k':0.0,'N_ncdm':0,'N_ur':3.044,'T_cmb':2.7255,'YHe':0.245,'recombination':'RECFAST','reio_parametrization':'reio_none',
 'A_s':2e-9,'n_s':0.965,'alpha_s':0.0,'k_pivot':0.05,'modes':'s','ic':'ad','gauge':'synchronous','matter_source_in_current_gauge':'yes','output':'mPk','z_pk':'0,1,3','P_k_max_1/Mpc':30.0}
CAMB_COSMO=dict(H0=67.5,ombh2=0.022,omch2=0.12,omk=0.0,mnu=0.0,num_massive_neutrinos=0,nnu=3.044,standard_neutrino_neff=3.044,YHe=0.245,TCMB=2.7255)

def camb_run(level='base',cosmo_mod=None,acc_mod=None,recomb='Recfast',reion=False,kmax=30.0,historical_interp=False):
    a=dict(CAMB_LEVEL[level]); a.update(acc_mod or {}); cos=dict(CAMB_COSMO); cos.update(cosmo_mod or {})
    t0=time.time(); p=camb.CAMBparams(); p.set_classes(recombination_model=recomb)
    p.set_cosmology(**cos)
    p.Reion.Reionization=bool(reion)
    p.InitPower.set_params(As=2e-9,ns=0.965,nrun=0,nrunrun=0,r=0,pivot_scalar=0.05)
    p.set_dark_energy(w=-1.0,wa=0.0)
    p.WantTensors=False; p.WantScalars=True
    p.set_accuracy(AccuracyBoost=a['AccuracyBoost'],lSampleBoost=a['lSampleBoost'],lAccuracyBoost=a['lAccuracyBoost'])
    p.set_matter_power(redshifts=[3.0,1.0,0.0],kmax=kmax,k_per_logint=a['k_per_logint'],nonlinear=False)
    p.NonLinear=model.NonLinear_none
    r=camb.get_results(p)
    PK=r.get_matter_power_interpolator(nonlinear=False,var1='delta_tot',var2='delta_tot',hubble_units=False,k_hunit=False,log_interp=True)
    kn,zn,pn=r.get_linear_matter_power_spectrum(var1='delta_tot',var2='delta_tot',hubble_units=False,k_hunit=False)
    zr=list(r.transfer_redshifts); s8=r.get_sigma8()
    out={'engine':'CAMB','version':camb.__version__,'level':level,'accuracy':a,'cosmo_args':cos,'recomb':recomb,'reion':reion,'kmax_requested':kmax,
         'params_dump':str(p),'Transfer_kmax_effective':p.Transfer.kmax,'Transfer_high_precision':p.Transfer.high_precision,
         'transfer_redshifts_order':zr,'native_k_range':[float(kn[0]),float(kn[-1])],'native_nk':len(kn),'native_z':list(map(float,zn)),
         'YHe_effective':p.YHe,'omnuh2':p.omnuh2,'num_nu_massless':p.num_nu_massless,'num_nu_massive':p.num_nu_massive,'nu_mass_degeneracies':list(p.nu_mass_degeneracies[:max(1,p.nu_mass_eigenstates)]),
         'nu_mass_fractions':list(p.nu_mass_fractions[:max(1,p.nu_mass_eigenstates)]),'nu_mass_eigenstates':p.nu_mass_eigenstates,'NonLinear':str(p.NonLinear),'Reionization':p.Reion.Reionization,
         'recomb_fields':{f:getattr(p.Recomb,f) for f in dir(p.Recomb) if f.startswith(('RECFAST','AGauss','zGauss','wGauss','min_a','max_a'))},
         'sigma8_engine':{str(z):float(s8[zr.index(z)]) for z in ZS},'derived':{k:float(v) for k,v in r.get_derived_params().items()},
         'Omega':{v:float(r.get_Omega(v)) for v in ['cdm','baryon','photon','neutrino','nu','de','K']},
         'DM':{str(z):float(r.comoving_radial_distance(z)) for z in ZBG},'Hz':{str(z):float(r.hubble_parameter(z)) for z in ZBG}}
    out['Omega']['m']=out['Omega']['cdm']+out['Omega']['baryon']+out['Omega']['nu']; out['Omega']['r']=out['Omega']['photon']+out['Omega']['neutrino']
    xe=r.get_background_redshift_evolution(ZTH,['x_e','T_b']); out['x_e']={str(z):float(v) for z,v in zip(ZTH,xe['x_e'])}; out['T_b']={str(z):float(v) for z,v in zip(ZTH,xe['T_b'])}
    aa=np.array([1e-7,1e-6]); bd=r.get_background_densities(aa,['photon','neutrino','nu']); out['early_rho_nu_over_rho_gamma']={str(x):float((bd['neutrino'][i]+bd['nu'][i])/bd['photon'][i]) for i,x in enumerate(aa)}
    arr={}
    for z in ZS:
        for nm,K in [('cmp',KCMP),('h20',KH20),('d1',KD1),('d2',KD2)]: arr[f'{nm}_z{z:g}']=PK.P(z,K)
    arr['native_k']=kn; arr['native_z']=zn; arr['native_P']=pn
    if historical_interp:
        kh,zz,pk=r.get_matter_power_spectrum(minkh=1e-4,maxkh=1.5,npoints=200,var1='delta_tot',var2='delta_tot')
        arr['hist_kh']=kh; arr['hist_z']=np.array(zz); arr['hist_pk_h']=pk; out['hist_spectrum_z']=list(map(float,zz))
    out['runtime_s']=time.time()-t0
    return out,arr

def class_run(level='base',mod=None,drop=()):
    d=dict(CLASS_BASE); d.update(CLASS_LEVEL[level]); d.update(mod or {})
    for k in drop: d.pop(k,None)
    t0=time.time(); c=Class(); c.set(d); c.compute()
    out={'engine':'CLASS','version':classy.__version__,'level':level,'class_dict_passed':copy.deepcopy(d),'class_pars_readback':{k:(str(v)) for k,v in c.pars.items()}}
    der=['Omega_m','Omega_Lambda','Neff','h','YHe','z_rec','rs_drag','z_reio','tau_reio','Omega0_ncdm_tot','sigma8','omega_ncdm_tot' ]
    dd={}
    for n in der:
        try: dd[n]=float(c.get_current_derived_parameters([n])[n])
        except Exception as e: dd[n]='unavailable: '+str(e)[:80]
    out['derived']=dd
    bg=c.get_background(); z=bg['z']; rc=bg['(.)rho_crit']; i0=np.argmin(abs(z))
    out['Omega']={'g':float(bg['(.)rho_g'][i0]/rc[i0]),'ur':float(bg['(.)rho_ur'][i0]/rc[i0]) if '(.)rho_ur' in bg else 0.0,'lambda':float(bg['(.)rho_lambda'][i0]/rc[i0]) if '(.)rho_lambda' in bg else 0.0,
       'cdm':float(bg['(.)rho_cdm'][i0]/rc[i0]),'b':float(bg['(.)rho_b'][i0]/rc[i0]),'ncdm':float(sum(bg[k][i0] for k in bg if k.startswith('(.)rho_ncdm'))/rc[i0])}
    out['Omega']['m']=out['Omega']['cdm']+out['Omega']['b']+out['Omega']['ncdm']; out['Omega']['r']=out['Omega']['g']+out['Omega']['ur']
    out['closure_sum_z0']=sum(v for k,v in out['Omega'].items() if k in('g','ur','lambda','cdm','b','ncdm'))
    ie=np.argmax(z); rnu=bg['(.)rho_ur'][ie] if '(.)rho_ur' in bg else 0.0; rnu=rnu+sum(bg[k][ie] for k in bg if k.startswith('(.)rho_ncdm'))
    out['early_rho_nu_over_rho_gamma']={'z=%g'%z[ie]:float(rnu/bg['(.)rho_g'][ie])}
    out['nonlinear_readback']=str(d.get('non_linear','not set (CLASS default: none)'))
    out['sigma8_engine']={str(zz):float(c.sigma(8/H,zz)) for zz in ZS}; out['sigma8_class_attr']=float(c.sigma8())
    out['DM']={str(zz):float(c.angular_distance(zz)*(1+zz)) for zz in ZBG}; out['Hz']={str(zz):float(c.Hubble(zz)*299792.458) for zz in ZBG}
    th=c.get_thermodynamics(); zt=th['z']; o=np.argsort(zt); out['x_e']={str(zz):float(np.interp(zz,zt[o],th['x_e'][o])) for zz in ZTH}; out['T_b']={str(zz):float(np.interp(zz,zt[o],th['Tb [K]'][o])) for zz in ZTH} if 'Tb [K]' in th else {}
    arr={}
    for zz in ZS:
        for nm,K in [('cmp',KCMP),('h20',KH20),('d1',KD1),('d2',KD2)]: arr[f'{nm}_z{zz:g}']=np.array([c.pk_lin(k,zz) for k in K])
    pk,kk,zz=c.get_pk_and_k_and_z(nonlinear=False); arr['native_k']=kk; arr['native_z']=zz; arr['native_P']=pk
    out['native_k_range']=[float(kk[0]),float(kk[-1])]; out['native_nk']=len(kk)
    c.struct_cleanup(); c.empty(); out['runtime_s']=time.time()-t0
    return out,arr
