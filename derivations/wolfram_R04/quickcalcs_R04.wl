c=299792.458; beta=369.82/c; dk[x_,a_]:=(2+x(1+a))beta;
cat={"beta"->beta,"CatWISE_x1.529_a1.122"->dk[1.529,1.122],"CatWISE_x1.755_a1.122"->dk[1.755,1.122]};
grid=Table[{x,a,NumberForm[dk[x,a],{6,5}]},{x,{0.5,0.75,1.0,1.25,1.5,1.75,2.0}},{a,{0.5,0.75,1.0,1.25,1.5}}];
cp1=1-0.05^(1/2000.); cp2=1-0.025^(1/2000.); cp99=1-0.01^(1/2000.);
cpchk=Quiet@InverseCDF[BetaDistribution[1,2000],0.95];
p1=Table[{b,f,b Sqrt[f]},{b,{2.7,3.2,3.1}},{f,{1.5,2.0}}];
E0[z_,om_]:=Sqrt[om(1+z)^3+1-om]; fap[z_,om_]:=E0[z,om] NIntegrate[1/E0[t,om],{t,0,z},WorkingPrecision->20,PrecisionGoal->12];
om=0.315191868; reb={0.295->0.270264,0.51->0.409992,0.706->0.439783};
ap=Table[{zz,fap[zz,om],fap[zz,om]/(zz/.reb)},{zz,{0.295,0.51,0.706}}];
Om=0.3065; OL=1-Om; xi[cm_]:=Exp[cm Log[1/Om]/(6 OL)]; cmOf[x_]:=6 OL Log[x]/Log[1/Om];
(* xiT table as in raw_01 *)
(* second call: coverage *)
cov[half_,s_]:=2 CDF[NormalDistribution[],half/s]-1;
