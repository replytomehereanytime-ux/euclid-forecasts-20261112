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
model[{om_,ok_,h_,w0_,wa_,ob_}]:=Module[{rd=rdf[om,h,ob],uz,dms,out,g1,g2,omh,zst,dz,rs},
 uz=Union[zs0]; dms=AssociationThread[uz->(dmf[#,om,ok,h,w0,wa]&/@uz)];
 out=MapThread[Function[{z,q},With[{dm=dms[z],dh=c/(100 h Ef[z,om,ok,h,w0,wa])},Switch[q,"DM",dm,"DH",dh,"DV",(z dm^2 dh)^(1/3)]/rd]],{zs0,qs}];
 g1=0.0783 ob^-0.238/(1+39.5 ob^0.763); g2=0.560/(1+21.1 ob^1.81); omh=om h^2;
 zst=1048(1+0.00124 ob^-0.738)(1+g1 omh^g2); dz=dmf[zst,om,ok,h,w0,wa];
 rs=gl[Function[u,Exp[u] c/Sqrt[3(1+31500 ob (2.7255/2.7)^-4 Exp[-u])]/(100 h Ef[Exp[u]-1,om,ok,h,w0,wa])],Log[1+zst],Log[1+10.^5]];
 {out,{Sqrt[omh] 100 dz/c,Pi dz/rs,ob}}];
chi2[p_,d_,Ci_]:=If[0.1<p[[1]]<0.6&&-0.3<p[[2]]<0.3&&0.4<p[[3]]<1&&0.015<p[[6]]<0.03&&-3<p[[4]]<1&&-5<p[[5]]<3,Module[{m=model[p],r,s},r=m[[1]]-d; s=m[[2]]-cm; r.Ci.r+s.cCi.s],10.^10];
pred[{om_,ok_,h_,w0_,wa_,ob_},z_]:=Module[{rd=rdf[om,h,ob],dm=dmf[z,om,ok,h,w0,wa],dh=c/(100 h Ef[z,om,ok,h,w0,wa])},{dm/rd,dh/rd,dm/dh}];
hess[f_,p_,st_]:=Module[{n=Length[p],e=IdentityMatrix[Length[p]]},Table[If[i==j,(f[p+st[[i]] e[[i]]]-2 f[p]+f[p-st[[i]] e[[i]]])/st[[i]]^2,(f[p+st[[i]] e[[i]]+st[[j]] e[[j]]]-f[p+st[[i]] e[[i]]-st[[j]] e[[j]]]-f[p-st[[i]] e[[i]]+st[[j]] e[[j]]]+f[p-st[[i]] e[[i]]-st[[j]] e[[j]]])/(4 st[[i]] st[[j]])],{i,n},{j,n}]];
jac[g_,p_,st_]:=Transpose@Table[(g[p+st[[i]] UnitVector[Length[p],i]]-g[p-st[[i]] UnitVector[Length[p],i]])/(2 st[[i]]),{i,Length[p]}];
zE={0.9,1.2,1.5,1.8};
(* map: free params q -> full vector {om,ok,h,w0,wa,ob} *)
maps=<|"LCDM"->Function[q,{q[[1]],0,q[[2]],-1,0,q[[3]]}],"wCDM"->Function[q,{q[[1]],0,q[[2]],q[[3]],0,q[[4]]}],"oLCDM"->Function[q,{q[[1]],q[[2]],q[[3]],-1,0,q[[4]]}]|>;
starts=<|"LCDM"->{0.324,0.6985,0.02228},"wCDM"->{0.324,0.6985,-1.0,0.02228},"oLCDM"->{0.324,0.0,0.6985,0.02228}|>;
steps=<|"LCDM"->{0.002,0.0015,0.00006},"wCDM"->{0.004,0.004,0.02,0.00006},"oLCDM"->{0.002,0.001,0.0015,0.00006}|>;
fitm[name_,d_,cv_]:=Module[{Ci=Inverse[cv],mp=maps[name],q0=starts[name],st=steps[name],vars,f,sol,qb,H,C,ev,pr},
 vars=Table[Unique["x"],{Length[q0]}];
 f=Function[q,chi2[mp[q],d,Ci]];
 sol=FindMinimum[f[q0+st*vars],Transpose[{vars,ConstantArray[0.,Length[q0]]}],Method->"PrincipalAxis"];
 qb=q0+st*(vars/.sol[[2]]);
 sol2=FindMinimum[f[qb+st*vars],Transpose[{vars,ConstantArray[0.,Length[q0]]}]];
 If[sol2[[1]]<sol[[1]],sol=sol2;qb=qb+st*(vars/.sol2[[2]])];
 H=hess[f,qb,st]; C=2 Inverse[H]; ev=Eigenvalues[C];
 pr=Table[With[{J=jac[pred[mp[#],z]&,qb,st/4]},{z,pred[mp[qb],z],Sqrt[Abs[Diagonal[J.C.Transpose[J]]]]}],{z,zE}];
 <|"model"->name,"chi2"->sol[[1]],"best"->qb,"sig"->Sqrt[Abs[Diagonal[C]]],"posdef"->(Min[ev]>0),"pred"->pr|>];
(* BAO-only flat LCDM, no radiation, params {Om, A=c/(H0 rd)} *)
baoOnly[d_,cv_]:=Module[{Ci=Inverse[cv],mod,f,sol,qb,H,C,st={0.002,0.02},pr,e},
 e[z_,om_]:=Sqrt[om(1+z)^3+1-om];
 mod[{om_,a_}]:=MapThread[Function[{z,q},With[{dm=a gl[Function[u,Exp[u]/e[Exp[u]-1,om]],0,Log[1+z]],dh=a/e[z,om]},Switch[q,"DM",dm,"DH",dh,"DV",(z dm^2 dh)^(1/3)]]],{zs0,qs}];
 f=Function[q,With[{r=mod[q]-d},r.Ci.r]];
 sol=FindMinimum[f[{om,a}],{{om,0.30},{a,29.5}}]; qb={om,a}/.sol[[2]];
 H=hess[f,qb,st]; C=2 Inverse[H];
 pr=Table[With[{g=Function[q,{q[[2]] gl[Function[u,Exp[u]/e[Exp[u]-1,q[[1]]]],0,Log[1+z]],q[[2]]/e[z,q[[1]]]}]},With[{J=jac[g,qb,st/4]},{z,g[qb],Sqrt[Diagonal[J.C.Transpose[J]]]}]],{z,zE}];
 <|"chi2"->sol[[1]],"best"->qb,"sig"->Sqrt[Diagonal[C]],"corr"->C[[1,2]]/Sqrt[C[[1,1]]C[[2,2]]],"pred"->pr|>];
N[{baoOnly[dOld,cov0],baoOnly[dNew,covNew],fitm["LCDM",dOld,cov0]},8]//InputForm
