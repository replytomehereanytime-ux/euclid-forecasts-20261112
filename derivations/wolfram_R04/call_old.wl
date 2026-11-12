(* R04 Wolfram CPL/LCDM fit: DESI DR2 BAO (box file) + Planck18 compressed CMB (Chen+2019), same model as /workspace/desi_r01/fit_cpl.py *)
c=299792.458; og=2.469*^-5;
zs0={0.295,0.51,0.51,0.706,0.706,0.934,0.934,1.321,1.321,1.484,1.484,2.33,2.33};
qs={"DV","DM","DH","DM","DH","DM","DH","DM","DH","DM","DH","DH","DM"};
dOld={7.94167639,13.58758434,21.86294686,17.35069094,19.45534918,21.57563956,17.64149464,27.60085612,14.17602155,30.51190063,12.81699964,8.631545674846294,38.988973961958784};
dNew=ReplacePart[dOld,{12->8.600,13->39.32}];
cov0=SparseArray[{{1,1}->5.78998687*^-03,{2,2}->2.83473742*^-02,{2,3}->-3.26062007*^-02,{3,2}->-3.26062007*^-02,{3,3}->1.83928040*^-01,{4,4}->3.23752442*^-02,{4,5}->-2.37445646*^-02,{5,4}->-2.37445646*^-02,{5,5}->1.11469198*^-01,{6,6}->2.61732816*^-02,{6,7}->-1.12938006*^-02,{7,6}->-1.12938006*^-02,{7,7}->4.04183878*^-02,{8,8}->1.05336516*^-01,{8,9}->-2.90308418*^-02,{9,8}->-2.90308418*^-02,{9,9}->5.04233092*^-02,{10,10}->5.83020277*^-01,{10,11}->-1.95215562*^-01,{11,10}->-1.95215562*^-01,{11,11}->2.68336193*^-01,{12,12}->1.02136194*^-02,{12,13}->-2.31395216*^-02,{13,12}->-2.31395216*^-02,{13,13}->2.82685779*^-01},{13,13}]//Normal;
covNew=ReplacePart[cov0,{{12,12}->0.066^2,{13,13}->0.33^2,{12,13}->0.225*0.066*0.33,{13,12}->0.225*0.066*0.33}];
cm={1.750235,301.4707,0.02235976}; cs={0.004644,0.08984,0.0001462};
corr={{1,0.46,-0.66},{0.46,1,-0.33},{-0.66,-0.33,1}}; cCi=Inverse[corr*Outer[Times,cs,cs]];
Ef[z_,om_,h_,w0_,wa_]:=Module[{or=og/h^2 (1+0.2271*3.046)},Sqrt[om(1+z)^3+or(1+z)^4+(1-om-or)(1+z)^(3(1+w0+wa)) Exp[-3 wa z/(1+z)]]];
dcf[z_,om_,h_,w0_,wa_]:=c/(100 h) NIntegrate[1/Ef[x,om,h,w0,wa],{x,0,z},PrecisionGoal->9,AccuracyGoal->12];
rdf[om_,h_,ob_]:=55.154 Exp[-72.3 (0.00064+0.0006)^2]/((om h^2-0.00064)^0.25351 ob^0.12807);
model[om_,h_,w0_,wa_,ob_]:=Module[{uz,dcs,out,g1,g2,omh,zst,dz,rb,rs,rd=rdf[om,h,ob]},
 uz=Union[zs0]; dcs=AssociationThread[uz->(dcf[#,om,h,w0,wa]&/@uz)];
 out=MapThread[Function[{z,q},With[{dm=dcs[z],dh=c/(100 h Ef[z,om,h,w0,wa])},Switch[q,"DM",dm,"DH",dh,"DV",(z dm^2 dh)^(1/3)]/rd]],{zs0,qs}];
 g1=0.0783 ob^-0.238/(1+39.5 ob^0.763); g2=0.560/(1+21.1 ob^1.81); omh=om h^2;
 zst=1048(1+0.00124 ob^-0.738)(1+g1 omh^g2); dz=dcf[zst,om,h,w0,wa];
 rb[z_]:=31500 ob (2.7255/2.7)^-4/(1+z);
 rs=NIntegrate[c/Sqrt[3(1+rb[z])]/(100 h Ef[z,om,h,w0,wa]),{z,zst,1*^5},PrecisionGoal->9];
 {out,{Sqrt[omh] 100 dz/c,Pi dz/rs,ob}}];
chi2[om_?NumericQ,h_?NumericQ,w0_?NumericQ,wa_?NumericQ,ob_?NumericQ,d_,Ci_]:=If[0.1<om<0.6&&0.4<h<1&&0.015<ob<0.03&&-3<w0<1&&-5<wa<3,Module[{m=model[om,h,w0,wa,ob],r,s},r=m[[1]]-d; s=m[[2]]-cm; r.Ci.r+s.cCi.s],10.^10];
pred[{om_,h_,w0_,wa_,ob_},z_]:=Module[{rd=rdf[om,h,ob],dm=dcf[z,om,h,w0,wa],dh=c/(100 h Ef[z,om,h,w0,wa])},{dm/rd,dh/rd,(z dm^2 dh)^(1/3)/rd,dm/dh}];
hess[f_,p_,st_]:=Module[{n=Length[p],e=IdentityMatrix[Length[p]]},Table[If[i==j,(f[p+st[[i]] e[[i]]]-2 f[p]+f[p-st[[i]] e[[i]]])/st[[i]]^2,(f[p+st[[i]] e[[i]]+st[[j]] e[[j]]]-f[p+st[[i]] e[[i]]-st[[j]] e[[j]]]-f[p-st[[i]] e[[i]]+st[[j]] e[[j]]]+f[p-st[[i]] e[[i]]-st[[j]] e[[j]]])/(4 st[[i]] st[[j]])],{i,n},{j,n}]];
jac[g_,p_,st_]:=Transpose@Table[(g[p+st[[i]] UnitVector[Length[p],i]]-g[p-st[[i]] UnitVector[Length[p],i]])/(2 st[[i]]),{i,Length[p]}];
zgrid={0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8};
run[d_,cv_]:=Module[{Ci=Inverse[cv],l,w,pl,pw,fl,fw,Hl,Hw,Cl,Cw,stl,stw,predl,predw,sig},
 l=FindMinimum[chi2[0.31+0.01 a,0.68+0.01 b,-1,0,0.0224+0.0001 e,d,Ci],{{a,0.},{b,0.},{e,0.}}];
 w=FindMinimum[chi2[0.31+0.01 a,0.68+0.01 b,w0,wa,0.0224+0.0001 e,d,Ci],{{a,3.5},{b,0.3},{w0,-0.72},{wa,-1.0},{e,-1.8}}];
 pl={0.31+0.01 a,0.68+0.01 b,0.0224+0.0001 e}/.l[[2]]; pw={0.31+0.01 a,0.68+0.01 b,w0,wa,0.0224+0.0001 e}/.w[[2]];
 fl=chi2[#[[1]],#[[2]],-1,0,#[[3]],d,Ci]&; fw=chi2[Sequence@@#,d,Ci]&;
 stl={0.002,0.0015,0.00006}; stw={0.01,0.01,0.05,0.15,0.00008};
 Hl=hess[fl,pl,stl]; Hw=hess[fw,pw,stw]; Cl=2 Inverse[Hl]; Cw=2 Inverse[Hw];
 predl=Table[With[{J=jac[pred[{#[[1]],#[[2]],-1,0,#[[3]]},z]&,pl,stl/4]},{z,pred[{pl[[1]],pl[[2]],-1,0,pl[[3]]},z],Sqrt[Diagonal[J.Cl.Transpose[J]]]}],{z,zgrid}];
 predw=Table[With[{J=jac[pred[#,z]&,pw,stw/4]},{z,pred[pw,z],Sqrt[Diagonal[J.Cw.Transpose[J]]]}],{z,zgrid}];
 sig=InverseCDF[NormalDistribution[],1-SurvivalFunction[ChiSquareDistribution[2],l[[1]]-w[[1]]]/2];
 <|"LCDM_chi2"->l[[1]],"LCDM_best"->pl,"LCDM_sig"->Sqrt[Diagonal[Cl]],"CPL_chi2"->w[[1]],"CPL_best"->pw,"CPL_sig"->Sqrt[Diagonal[Cw]],"CPL_corr_w0wa"->Cw[[3,4]]/Sqrt[Cw[[3,3]] Cw[[4,4]]],
  "dchi2"->l[[1]]-w[[1]],"p"->SurvivalFunction[ChiSquareDistribution[2],l[[1]]-w[[1]]],"sigma"->sig,"pred_LCDM"->predl,"pred_CPL"->predw|>];
KeyTake[run[dOld,cov0],{"LCDM_chi2","LCDM_best","CPL_chi2","CPL_best","CPL_sig","dchi2","p","sigma"}]//InputForm