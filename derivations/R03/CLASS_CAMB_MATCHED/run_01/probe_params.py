"""Probe: does each protocol setting exist/take effect in the installed codes? No solver physics compared here."""
import json, inspect, camb, classy
from classy import Class
out={}
# CAMB
import camb.model as cm
out['camb_version']=camb.__version__
out['set_cosmology_args']=list(inspect.signature(camb.CAMBparams.set_cosmology).parameters)
out['set_classes_args']=list(inspect.signature(camb.CAMBparams.set_classes).parameters)
out['set_matter_power_args']=list(inspect.signature(camb.CAMBparams.set_matter_power).parameters)
out['set_accuracy_args']=list(inspect.signature(camb.CAMBparams.set_accuracy).parameters)
import camb.recombination as cr
out['camb_recomb_classes']=[n for n in dir(cr) if not n.startswith('_')]
p=camb.CAMBparams()
try:
    p.set_classes(recombination_model='Recfast'); out['camb_set_classes_Recfast']=type(p.Recomb).__name__
except Exception as e: out['camb_set_classes_Recfast']='ERROR '+repr(e)
out['camb_Recfast_fields']={f:getattr(p.Recomb,f) for f in ['RECFAST_fudge','RECFAST_fudge_He','RECFAST_Heswitch','RECFAST_Hswitch','AGauss1','AGauss2','zGauss1','zGauss2','wGauss1','wGauss2'] if hasattr(p.Recomb,f)}
# CLASS
base={'H0':67.5,'omega_b':0.022,'omega_cdm':0.12,'Omega_k':0.0,'N_ncdm':0,'N_ur':3.044,'T_cmb':2.7255,'YHe':0.245,'recombination':'RECFAST','reio_parametrization':'reio_none',
 'A_s':2e-9,'n_s':0.965,'alpha_s':0.0,'k_pivot':0.05,'modes':'s','ic':'ad','gauge':'synchronous','matter_source_in_current_gauge':'yes','output':'mPk','z_pk':'0,1,3','P_k_max_1/Mpc':30.0}
prec={'tol_background_integration':1e-10,'tol_thermo_integration':1e-6,'tol_perturbations_integration':1e-5,'k_per_decade_for_pk':40,'k_per_decade_for_bao':70,'l_max_ur':17,'sigma_k_per_decade':80}
out['classy_version']=classy.__version__
tests={'base_only':base,'base+prec':{**base,**prec}}
for k in prec: tests['base+'+k]={**base,k:prec[k]}
for name,d in tests.items():
    c=Class(); c.set(d)
    try: c.compute(); out['class_'+name]='OK'
    except Exception as e: out['class_'+name]='ERROR '+str(e)[:400]
    c.struct_cleanup(); c.empty()
print(json.dumps(out,indent=1))
json.dump(out,open('probe_params_output.json','w'),indent=1)
