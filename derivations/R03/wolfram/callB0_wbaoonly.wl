(* R02 alt-model background fits. Data/cov/CMB priors/rd formula copied verbatim from wolfram_R04/fit_cpl_R04.wl (sha256 3c5ad458...dea2). New: Gauss-Legendre in ln(1+z), curvature, constant-w, BAO-only (Om,A). *)
c=299792.458; og=2.469*^-5;
zs0={0.295,0.51,0.51,0.706,0.706,0.934,0.934,1.321,1.321,1.484,1.484,2.33,2.33};
qs={"DV","DM","DH","DM","DH","DM","DH","DM","DH","DM","DH","DH","DM"};
dOld={7.94167639,13.58758434,21.86294686,17.35069094,19.45534918,21.57563956,17.64149464,27.60085612,14.17602155,30.51190063,12.81699964,8.631545674846294,38.988973961958784};
dNew=ReplacePart[dOld,{12->8.600,13->39.32}];
cov0=SparseArray[{{1,1}->5.78998687*^-03,{2,2}->2.83473742*^-02,{2,3}->-3.26062007*^-02,{3,2}->-3.26062007*^-02,{3,3}->1.83928040*^-01,{4,4}->3.23752442*^-02,{4,5}->-2.37445646*^-02,{5,4}->-2.37445646*^-02,{5,5}->1.11469198*^-01,{6,6}->2.61732816*^-02,{6,7}->-1.12938006*^-02,{7,6}->-1.12938006*^-02,{7,7}->4.04183878*^-02,{8,8}->1.05336516*^-01,{8,9}->-2.90308418*^-02,{9,8}->-2.90308418*^-02,{9,9}->5.04233092*^-02,{10,10}->5.83020277*^-01,{10,11}->-1.95215562*^-01,{11,10}->-1.95215562*^-01,{11,11}->2.68336193*^-01,{12,12}->1.02136194*^-02,{12,13}->-2.31395216*^-02,{13,12}->-2.31395216*^-02,{13,13}->2.82685779*^-01},{13,13}]//Normal;
covNew=ReplacePart[cov0,{{12,12}->0.066^2,{13,13}->0.33^2,{12,13}->0.225*0.066*0.33,{13,12}->0.225*0.066*0.33}];
cm={1.750235,301.4707,0.02235976}; cs={0.004644,0.08984,0.0001462};
corr={{1,0.46,-0.66},{0.46,1,-0.33},{-0.66,-0.33,1}}; cCi=Inverse[corr*Outer[Times,cs,cs]];
{gx,gw}=Most[NIntegrate`GaussRuleData[48,MachinePrecision]];
gl[f_,a_,b_]:=(b-a) Total[gw f[a+(b-a) gx]];
Ef[z_,om_,ok_,h_,w0_,wa_]:=Module[{or=og/h^2 (1+0.2271*3.046)},Sqrt[om(1+z)^3+or(1+z)^4+ok(1+z)^2+(1-om-or-ok)(1+z)^(3(1+w0+wa)) Exp[-3 wa z/(1+z)]]];
xint[z_,om_,ok_,h_,w0_,wa_]:=gl[Function[u,Exp[u]/Ef[Exp[u]-1,om,ok,h,w0,wa]],0,Log[1+z]];
dmf[z_,om_,ok_,h_,w0_,wa_]:=Module[{x=xint[z,om,ok,h,w0,wa]},c/(100 h) If[Abs[ok]<10^-9,x,Re[Sinh[Sqrt[ok+0.I] x]/Sqrt[ok+0.I]]]];
rdf[om_,h_,ob_]:=55.154 Exp[-72.3 (0.00064+0.0006)^2]/((om h^2-0.00064)^0.25351 ob^0.12807);
(* R03 Task B: BF-2 setup. BAO-only, flat, no radiation, constant w, A=c/(H0 rd) free (profiled analytically: chi2 quadratic in A). *)
Enr[z_,om_,w_]:=Sqrt[om(1+z)^3+(1-om)(1+z)^(3(1+w))];
xnr[z_,om_,w_]:=gl[Function[u,Exp[u]/Enr[Exp[u]-1,om,w]],0,Log[1+z]];
uvec[om_?NumericQ,w_?NumericQ]:=Table[With[{z=zs0[[i]],dm=xnr[zs0[[i]],om,w],dh=1/Enr[zs0[[i]],om,w]},Switch[qs[[i]],"DM",dm,"DH",dh,"DV",(z dm^2 dh)^(1/3)]],{i,13}];
prof[om_?NumericQ,w_?NumericQ,d_,Ci_]:=Module[{u=uvec[om,w],a,b},a=u.Ci.u;b=u.Ci.d;d.Ci.d-b^2/a];
Ahat[om_,w_,d_,Ci_]:=Module[{u=uvec[om,w]},(u.Ci.d)/(u.Ci.u)];
r1=Module[{Ci=Inverse[Normal[covNew]],sol},sol=FindMinimum[prof[om,w,dNew,Ci],{{om,0.30,0.31},{w,-0.97,-0.96}},Method->"PrincipalAxis",AccuracyGoal->10,PrecisionGoal->10];{"REPLACEMENT",sol[[1]],om/.sol[[2]],w/.sol[[2]],Ahat[om/.sol[[2]],w/.sol[[2]],dNew,Ci]}];
r2=Module[{Ci=Inverse[Normal[cov0]],sol},sol=FindMinimum[prof[om,w,dOld,Ci],{{om,0.30,0.31},{w,-0.97,-0.96}},Method->"PrincipalAxis",AccuracyGoal->10,PrecisionGoal->10];{"PRIMARY",sol[[1]],om/.sol[[2]],w/.sol[[2]],Ahat[om/.sol[[2]],w/.sol[[2]],dOld,Ci]}];
{$Version,r1,r2}//InputForm
