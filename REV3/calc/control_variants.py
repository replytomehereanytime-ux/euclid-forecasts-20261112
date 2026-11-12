import sys; sys.path.insert(0,'.'); import numpy as np, cplmodel_r03 as M
c=M.c; gx,gw=M.gx,M.gw; T=2.7255
Om,h,ob=0.3166,0.6727,0.02236
def Erad(zz,Om,h,w0,wa,Orh2):
    Or=Orh2/h**2; Ode=1-Om-Or
    return np.sqrt(Om*(1+zz)**3+Or*(1+zz)**4+Ode*(1+zz)**(3*(1+w0+wa))*np.exp(-3*wa*zz/(1+zz)))
def lA(Om,h,ob,zs,Orh2):
    U=np.log1p(zs); u=U*(gx+1)/2; zz=np.expm1(u)
    Dz=c/(100*h)*U*np.sum(gw*(1+zz)/Erad(zz,Om,h,-1,0,Orh2))/2
    a1=1/(1+zs); a=a1*(gx+1)/2; zz=1/a-1; Rb=31500*ob*(T/2.7)**-4*a
    rs=c/(100*h)*a1*np.sum(gw/np.sqrt(3*(1+Rb))/(a*a*Erad(zz,Om,h,-1,0,Orh2)))/2
    return np.sqrt(Om*h*h)*100*Dz/c, np.pi*Dz/rs, rs
zHS=float(M.zstar(np.array([Om]),np.array([h]),np.array([ob]))[0])
Or_std=M.og*(1+0.2271*3.046)
zeq=2.5e4*Om*h*h*(T/2.7)**-4; Or_chen=Om*h*h/(1+zeq)
for name,zs,Or in [('old: HS z*, std Or',zHS,Or_std),('Chen Or, HS z*',zHS,Or_chen),('std Or, z*=1089.9',1089.9,Or_std),('Chen Or, z*=1089.9',1089.9,Or_chen)]:
    R,l,rs=lA(Om,h,ob,zs,Or); print(f'{name:24s} R={R:.6f} lA={l:.4f} rs*={rs:.3f}  Orh2={Or:.4e}')
