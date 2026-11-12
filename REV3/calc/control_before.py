import sys; sys.path.insert(0,'.'); import numpy as np, cplmodel_r03 as M
M.RSMODE='full'
Om,h,ob=0.3166,0.6727,0.02236
r=M.cmb(Om,h,-1,0,ob)[0]; print('BEFORE R, l_A, ob =',r.tolist(),' z*=',M.zstar(np.array([Om]),np.array([h]),np.array([ob])))
print('prior mean',M.cm.tolist(),' ratio',M.cm[1]/r[1])
M.RSMODE='trunc'; print('trunc l_A',M.cmb(Om,h,-1,0,ob)[0][1])
