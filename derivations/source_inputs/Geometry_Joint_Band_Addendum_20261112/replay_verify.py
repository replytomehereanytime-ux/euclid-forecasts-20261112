from pathlib import Path
import json,subprocess,tempfile,shutil,os,hashlib,datetime
ROOT=Path(__file__).resolve().parent
T=Path(tempfile.mkdtemp(prefix='geometry_joint_replay_',dir=ROOT.parent))
(T/'inputs').mkdir();(T/'independent_review').mkdir()
for n in ['joint_bands.py','compare_and_export.py','PLAN.json']:shutil.copyfile(ROOT/n,T/n)
for f in (ROOT/'inputs').iterdir():shutil.copyfile(f,T/'inputs'/f.name)
shutil.copyfile(ROOT/'independent_review/audit.py',T/'independent_review/audit.py')
env={**os.environ,'OPENBLAS_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'}
for args in [['joint_bands.py','--resolution','lower'],['joint_bands.py','--resolution','higher'],['independent_review/audit.py','128'],['compare_and_export.py']]:
 with (T/(Path(args[0]).stem+'_'+args[-1]+'.log')).open('w') as log:subprocess.run(['python3',*args],cwd=T,env=env,stdout=log,stderr=subprocess.STDOUT,check=True)
checks=[]
for n,exclude in [('RESULT_lower.json',['created_utc','completed_utc']),('RESULT_higher.json',['created_utc','completed_utc']),('independent_review/audit_results_degree128.json',['elapsed_seconds']),('SUMMARY.json',[])]:
 old=json.load(open(ROOT/n));new=json.load(open(T/n))
 for k in exclude:old.pop(k);new.pop(k)
 assert old==new,n
 checks.append({'file':n,'all_other_fields_exactly_equal':True,'excluded_fields':exclude})
assert (ROOT/'JOINT_BANDS.csv').read_bytes()==(T/'JOINT_BANDS.csv').read_bytes()
checks.append({'file':'JOINT_BANDS.csv','byte_identical':True})
r={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS_FRESH_DIRECTORY_SCIENCE_REPLAY','replay_directory':str(T),'checks':checks,'scope':'Full producer lower/higher and independent tighter audit rerun without original absolute source paths. Timestamps and independent elapsed time excluded exactly as listed. No approximate comparisons used for these equalities.','joint_csv_sha256':hashlib.sha256((ROOT/'JOINT_BANDS.csv').read_bytes()).hexdigest()}
(ROOT/'REPLAY.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
