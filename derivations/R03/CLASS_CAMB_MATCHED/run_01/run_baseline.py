import json, sys, time, datetime, numpy as np, os
sys.path.insert(0,'.'); import engines as E
os.makedirs('runs',exist_ok=True)
JOBS={'camb_base':lambda:E.camb_run('base',historical_interp=True),'camb_tight':lambda:E.camb_run('tight'),
      'class_base':lambda:E.class_run('base'),'class_tight':lambda:E.class_run('tight'),
      'camb_base_interp80':lambda:E.camb_run('base',acc_mod={'k_per_logint':80}),
      'class_base_interp80':lambda:E.class_run('base',mod={'k_per_decade_for_pk':80,'k_per_decade_for_bao':140})}
sel=sys.argv[1:] or list(JOBS)
for n in sel:
    t0=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        o,a=JOBS[n](); o['start_utc']=t0; o['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat(); o['status']='OK'
        np.savez(f'runs/{n}.npz',**a)
    except Exception as e:
        o={'status':'FAILED','error':repr(e),'start_utc':t0,'end_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    json.dump(o,open(f'runs/{n}.json','w'),indent=1,default=str); print(n,o['status'],o.get('runtime_s'),o.get('error',''),flush=True)
