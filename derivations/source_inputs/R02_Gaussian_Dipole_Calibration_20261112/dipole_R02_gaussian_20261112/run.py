import json,hashlib,sys
from pathlib import Path
import numpy as np
from scipy.stats import chi2
P=Path(__file__).resolve().parent;p=json.loads((P/'protocol.json').read_text());ph=hashlib.sha256((P/'protocol.json').read_bytes()).hexdigest();assert ph=='3dff031adf5820e6cdae3b3768302c0697e7624607701568443b398266593401'
def sphere(N):
 i=np.arange(N);z=1-2*(i+.5)/N;v=i*np.pi*(3-np.sqrt(5));return np.c_[np.sqrt(1-z*z)*np.cos(v),np.sqrt(1-z*z)*np.sin(v),z]
def templates(n):return np.c_[n[:,0],(3*n[:,2]**2-1)/2,n[:,0]*n[:,2]]
n=sphere(512);n=n[(n[:,2]>.55)|((n[:,2]<-.4)&(n[:,0]>0))];T=templates(n);nc=sphere(32);Tc=templates(nc);ns=len(n)
Xs=np.c_[np.ones(ns),n,T];Xc=np.c_[np.zeros((32,4)),Tc];X=np.vstack((Xs,Xc));eta=np.array([.02,.03,-.02]);threshold=chi2.ppf(.95,3)
rng=np.random.default_rng(p['seed']);rows=[];checks=[]
def ck(k,v):checks.append({'name':k,'pass':bool(v)})
def estimator(cs,ss):
 C=np.zeros((ns+32,ns+32));C[:ns,:ns]=.04**2*np.eye(ns)+ss**2*n@n.T;C[ns:,ns:]=cs**2*np.eye(32)
 W=np.linalg.solve(C,X);F=X.T@W;V=np.linalg.inv(F);L=V@W.T
 return L,V,C,F
ck('full_rank',np.linalg.matrix_rank(X)==7);ck('science_without_calibration_rank6',np.linalg.matrix_rank(Xs)==6)
null=np.zeros(7);null[1]=1;null[4]=-1;ck('exact_shared_null',np.max(abs(Xs@null))==0)
ck('efficiency_physical',np.max(.4*np.exp(T@eta))<1)
for k,g in enumerate(p['grid']):
 cs,ss=g['cal_sd'],g['sky_sd'];d=np.array(g['d']);beta=np.r_[np.log(800),d,eta];L,V,C,F=estimator(cs,ss)
 # Calibration observations have known log(0.4) subtracted, science same offset.
 noise=np.vstack((.04*rng.normal(size=(ns,2000))+ss*n@rng.normal(size=(3,2000)),cs*rng.normal(size=(32,2000))))
 Y=X@beta[:,None]+noise;b=L@Y;err=b[1:4]-d[:,None];cov=V[1:4,1:4];score=np.sum(err*np.linalg.solve(cov,err),axis=0);coverage=np.mean(score<=threshold)
 rb=np.mean(err,axis=1)/np.sqrt(np.diag(cov));emp=np.cov(err);rel=np.linalg.norm(emp-cov)/np.linalg.norm(cov)
 # Direct whitened least squares independent numerical solve for first observation.
 chol=np.linalg.cholesky(C);bw=np.linalg.lstsq(np.linalg.solve(chol,X),np.linalg.solve(chol,Y[:,0]),rcond=None)[0]
 ck(f'{k}_solver',max(abs(bw-b[:,0]))<1e-10);ck(f'{k}_finite',np.isfinite(b).all());ck(f'{k}_bias',max(abs(rb))<.10);ck(f'{k}_coverage',.93<=coverage<=.97);ck(f'{k}_covariance',rel<.12)
 # Profile normalization and calibration nuisance with actual weighted Fisher.
 ix=[1,2,3];nu=[0,4,5,6];S=F[np.ix_(ix,ix)]-F[np.ix_(ix,nu)]@np.linalg.solve(F[np.ix_(nu,nu)],F[np.ix_(nu,ix)])
 row={'stratum':g,'joint_coverage':float(coverage),'coverage_mc_se':float(np.sqrt(coverage*(1-coverage)/2000)),'normalized_bias':rb.tolist(),'coordinate_sd':np.sqrt(np.diag(cov)).tolist(),'covariance_relative_error':float(rel),'profile_fisher_eigenvalues':np.linalg.eigvalsh(S).tolist(),'profile_condition':float(np.linalg.cond(S))}
 if ss:
  Lbad,Vbad,_,_=estimator(cs,0);eb=(Lbad@Y)[1:4]-d[:,None];row['omit_sky_joint_coverage']=float(np.mean(np.sum(eb*np.linalg.solve(Vbad[1:4,1:4],eb),axis=0)<=threshold))
 # Same exact model but calibration systematically biased; cannot claim robustness.
 Ybias=Y.copy();Ybias[ns:]+=.03*Tc[:,0,None];eb=(L@Ybias)[1:4]-d[:,None]
 row['biased_calibration_mean_error']=eb.mean(1).tolist();row['biased_calibration_joint_coverage']=float(np.mean(np.sum(eb*np.linalg.solve(cov,eb),axis=0)<=threshold))
 rows.append(row)
result={'label':p['version'],'protocol_sha256':ph,'python':sys.version.split()[0],'numpy':np.__version__,'science_cells':ns,'calibration_cells':32,'regions':'fixed joint Gaussian reference; known covariance, no oracle interval calibration','rows':rows,'checks':checks}
(P/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
