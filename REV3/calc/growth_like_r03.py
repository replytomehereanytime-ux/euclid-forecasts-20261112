"""Like-for-like rerun of R03 fs8_fullrs_r03.py settings (CAMB, mnu=0, Neff 3.046, PPF for CPL, lnAs~N(3.044,0.014), ns 0.9649)
on the REV3 calibrated-prior REPLACEMENT chains, 60 draws each, to report shifts vs R03 (REV2-era) growth numbers."""
import sys,json; sys.path.insert(0,'.'); import numpy as np, camb
MODE='rescale'; ZS=[0.9,1.2,1.3,1.5,1.8]; ZZ=sorted(ZS+[0.0],reverse=True)
def run(Om,h,w0,wa,ob,lnAs):
    p=camb.set_params(H0=100*h,ombh2=ob,omch2=Om*h*h-ob,mnu=0,nnu=3.046,As=np.exp(lnAs)*1e-10,ns=0.9649,w=w0,wa=wa,dark_energy_model='ppf' if (w0,wa)!=(-1,0) else 'fluid')
    p.set_matter_power(redshifts=ZZ,kmax=1.2); r=camb.get_results(p); zr=list(r.transfer_redshifts); fs=r.get_fsigma8(); s8=r.get_sigma8()
    return {z:(float(fs[zr.index(z)]),float(s8[zr.index(z)])) for z in ZZ}
q=lambda a:[float(np.quantile(a,t)) for t in (0.16,0.5,0.84)]
rng=np.random.default_rng(20261112); R=json.load(open(f'rows_rev3_{MODE}.json'))['REPLACEMENT']; old=json.load(open('../../R03/calc/fs8_fullrs_r03_output.json'))
out={}
for n,ch,key in [('LCDM',np.load(f'chain_LCDM_REPLACEMENT_{MODE}.npy'),'LCDM'),('w0waCDM',np.load(f'chain_CPL_REPLACEMENT_{MODE}.npy'),'CPL')]:
    idx=rng.choice(len(ch),60,replace=False); lnAs=rng.normal(3.044,0.014,60)
    res=[run(*map(float,ch[i,:5]),float(lnAs[k])) for k,i in enumerate(idx)]
    s80=np.array([r[0.0][1] for r in res]); S8=s80*np.sqrt(ch[idx,0]/0.3)
    o={'N':60,'sigma8_0':q(s80),'S8_0':q(S8),'fsigma8':{str(z):q(np.array([r[z][0] for r in res])) for z in ZS}}
    o['shift_vs_R03_median']={'sigma8_0':o['sigma8_0'][1]-old[n]['sigma8_0'][1],'S8_0':o['S8_0'][1]-old[n]['S8_0'][1],**{f'fsigma8_{z}':o['fsigma8'][str(z)][1]-old[n]['fsigma8'][str(z)]['q16_50_84_2.5_97.5'][1] for z in ZS}}
    out[n]=o; print(n,json.dumps(o),flush=True)
json.dump(out,open('growth_like_r03_rescale.json','w'),indent=1)
