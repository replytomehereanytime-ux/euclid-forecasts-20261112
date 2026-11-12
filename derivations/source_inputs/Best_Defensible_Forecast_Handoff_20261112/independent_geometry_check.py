import csv,json,math,pathlib,hashlib
from scipy.integrate import quad
P=pathlib.Path(__file__).parent
src=P/'prototype_geometry.csv'
checks=[]
for r in csv.DictReader(src.open()):
 z=float(r['z']);om=float(r['Omega_m']);A=float(r['A']);E=lambda x:math.sqrt(om*(1+x)**3+1-om)
 dm=A*quad(lambda x:1/E(x),0,z,epsabs=1e-12,epsrel=1e-12)[0];dh=A/E(z)
 for k,v in [('DM_over_rd',dm),('DH_over_rd',dh),('F_AP',dm/dh)]:checks.append(abs(v-float(r[k])))
 # independent growth integral in a
 ea=lambda a:math.sqrt(om/a**3+1-om)
 g=lambda a:ea(a)*quad(lambda x:x**1.5/(om+(1-om)*x**3)**1.5,0,a,epsabs=1e-12,epsrel=1e-12)[0]
 checks.append(abs(g(1/(1+z))/g(1)-float(r['D_normalized_today'])))
out={'scope':'Direct adaptive quadrature checks of all 55 deterministic prototype rows; not a likelihood or source audit','scalar_comparisons':len(checks),'max_absolute_error':max(checks),'pass_tolerance_1e-10':max(checks)<1e-10,'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(P/'NUMERICAL_CHECK.json').write_text(json.dumps(out,indent=2));print(out)
