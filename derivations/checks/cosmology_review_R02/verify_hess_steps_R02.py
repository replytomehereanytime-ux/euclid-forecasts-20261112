# Step-size sensitivity of the Laplace sigma for wCDM/oLCDM (own code), plus R02 step set.
import numpy as np, json
from verify_fits_R02 import *
out={}
for model,R02st in [('wCDM',[0.004,0.004,0.02,0.00006]),('oLCDM',[0.002,0.001,0.0015,0.00006]),('LCDM',[0.002,0.0015,0.00006])]:
    y,Ci=branch('PRIM'); r=fit(model,'PRIM'); q=r['_q']; f=lambda x:chi2(np.asarray(x),model,y,Ci)
    out[model]={}
    for lab,st in [('R02_steps',np.array(R02st)),('R02_steps/4',np.array(R02st)/4),('R02_steps/10',np.array(R02st)/10),('R02_steps*2',np.array(R02st)*2)]:
        H=hessian(f,q,st); Cq=2*np.linalg.inv(H); out[model][lab]=np.sqrt(np.diag(Cq)).round(5).tolist()
    print(model,out[model],flush=True)
json.dump(out,open('verify_hess_steps_R02_output.json','w'),indent=1)
