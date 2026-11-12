#!/usr/bin/env python3
"""Offline spectrum checker; never installs packages or launches a Boltzmann solver.

CSV columns: z,k_1_per_Mpc,P_camb_base_Mpc3,P_camb_tight_Mpc3,
             P_class_base_Mpc3,P_class_tight_Mpc3
Every z must have the identical positive ascending k grid. For sigma8 use a
separate dense CSV with broad k support; do not use the historical 20 rows.
"""
import argparse
import json
import math
from pathlib import Path
import numpy as np
from scipy.integrate import simpson

H = 0.675
KEYS = ['P_camb_base_Mpc3', 'P_camb_tight_Mpc3',
        'P_class_base_Mpc3', 'P_class_tight_Mpc3']

def top_hat(x):
    x = np.asarray(x, dtype=float)
    out = np.empty_like(x)
    small = abs(x) < 0.05
    y = x[small]**2
    out[small] = 1-y/10+y*y/280-y*y*y/15120+y**4/1330560
    t=x[~small]
    out[~small]=3*(np.sin(t)-t*np.cos(t))/t**3
    return out

def sigma_R(k, power, R):
    k=np.asarray(k,dtype=float);power=np.asarray(power,dtype=float)
    if k.ndim!=1 or power.shape!=k.shape or len(k)<3:
        raise ValueError('Need same-length one-dimensional arrays with at least 3 points')
    if not np.all(np.isfinite(k)) or not np.all(np.isfinite(power)):
        raise ValueError('Nonfinite input')
    if R<=0 or not np.all(k>0) or not np.all(np.diff(k)>0) or not np.all(power>0):
        raise ValueError('R, k and P must be positive and k strictly increasing')
    variance=simpson(k**3*power*top_hat(k*R)**2,x=np.log(k))/(2*math.pi**2)
    return float(np.sqrt(variance))

def stats(a,b):
    signed=a/b-1
    return {'mean_abs':float(np.mean(abs(signed))),
            'max_abs':float(np.max(abs(signed))),
            'signed_min':float(np.min(signed)),
            'signed_max':float(np.max(signed))}

def check(path,dense=False):
    data=np.genfromtxt(path,delimiter=',',names=True)
    required=['z','k_1_per_Mpc']+KEYS
    if data.ndim!=1 or not all(x in data.dtype.names for x in required):
        raise ValueError('CSV schema or row shape mismatch')
    if sorted(np.unique(data['z']).tolist())!=[0,1,3]:
        raise ValueError('Require exactly z=0,1,3; never infer array order')
    result={'status':'NUMERICAL_CSV_AUDIT_NOT_PROVENANCE_AUTHENTICATION',
            'h':H,'R_Mpc':8/H,'redshifts':{}}
    reference=None
    for z in [0,1,3]:
        block=data[data['z']==z];k=block['k_1_per_Mpc']
        if reference is not None and not np.array_equal(k,reference):
            raise ValueError('Redshift grids differ')
        reference=k
        for key in KEYS:
            sigma_R(k,block[key],8/H)  # input validation only
        row={'n':len(k),'kmin':float(k[0]),'kmax':float(k[-1]),
             'camb_self':stats(block[KEYS[0]],block[KEYS[1]]),
             'class_self':stats(block[KEYS[2]],block[KEYS[3]]),
             'tight_cross':stats(block[KEYS[1]],block[KEYS[3]])}
        if not dense:
            expected=np.geomspace(0.002,1.0,201)
            if len(k)!=201 or not np.allclose(k,expected,rtol=1e-10,atol=0):
                raise ValueError('Comparison screen requires the specified 201-point grid')
            row['numerical_screen_pass']=(row['camb_self']['max_abs']<0.001
                and row['class_self']['max_abs']<0.001
                and row['tight_cross']['max_abs']<0.005)
        else:
            row['cross_stats_scope']='Descriptive full dense grid; not the comparison-grid pass criterion'
        if dense:
            if k[0]>1e-5 or k[-1]<30 or len(k)<12001:
                raise ValueError('Dense sigma8 data require k<=1e-5 through >=30 and >=12001 points')
            row['sigma8_integrated']={key:sigma_R(k,block[key],8/H) for key in KEYS}
            row['sigma8_truncated_at_10']={key:sigma_R(k[k<=10],block[key][k<=10],8/H) for key in KEYS}
        result['redshifts'][str(z)]=row
    return result

def self_test():
    # P=A/k^2 has sigma_R^2=3A/(10*pi*R) for a real-space spherical top hat.
    # This analytic toy is not a cosmological power spectrum.
    A=2.7;R=8/H;k=np.geomspace(1e-7/R,1e3/R,65537);p=A/k**2
    exact=math.sqrt(3*A/(10*math.pi*R));actual=sigma_R(k,p,R)
    assert abs(actual/exact-1)<1e-6
    assert abs(sigma_R(k/H,H**3*p,8)/actual-1)<1e-12
    assert abs(sigma_R(k,4*p,R)/actual-2)<1e-12
    assert np.allclose(top_hat([0,1e-9]),[1,1],atol=1e-15)
    for badk,badp in [(k[::-1],p), (k,-p), (k,p*float('nan'))]:
        try: sigma_R(badk,badp,R)
        except ValueError: pass
        else: raise AssertionError('Invalid input accepted')
    return {'status':'PASS_HELPER_ONLY_NO_BOLTZMANN_SOLVER',
            'analytic_power_A_over_k2_sigma':exact,'computed_sigma':actual,
            'relative_error':actual/exact-1,'passed_checks':7,
            'checks':['analytic_integral','h_unit_invariance','amplitude_scaling',
                      'small_x_window','reject_reversed_k','reject_negative_power','reject_nan']}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv',nargs='?')
    parser.add_argument('--dense',action='store_true')
    parser.add_argument('--self-test',action='store_true')
    args=parser.parse_args()
    if args.self_test: print(json.dumps(self_test(),indent=2))
    elif args.csv: print(json.dumps(check(Path(args.csv),args.dense),indent=2))
    else: parser.error('Use --self-test or pass a CSV')
