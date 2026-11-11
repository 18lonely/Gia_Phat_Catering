"""Fixture arithmetic/oracle and preservation only; no backend execution.
Writes only fixture-review-check-result.json; historical checkers are not run.
"""
from pathlib import Path
import hashlib, json, re
b=Path(__file__).resolve().parents[1]; r=b.parents[1]; v=b/'validation'
base=json.loads((v/'fixture-review-baseline-sha256.json').read_text(encoding='utf-8'))
allowed={f'docs/chon-mon-order/{x}' for x in ['test/fixtures/README.md','review/contract-gap-register.md','gap-analysis.md','preview.html','validation/check-result.json','validation/diagram-render-result.json']}
allowed.update(['docs/project-dashboard.md','docs/gia-phat/review/progress-assessment.md','docs/gia-phat/review/next-session-prompt.md'])
allowed.update(p for p in base if p.startswith('docs/chon-mon-order/srs/diagrams/') and p.endswith(('.html','.svg')))
new_allowed={f'docs/chon-mon-order/validation/{x}' for x in ['fixture-review-baseline-sha256.json','check-fixture-review.py','fixture-review-check-result.json','fixture-review-report.md']}
errors=[];changed=[];protected=0
def need(ok,msg):
 if not ok: errors.append(msg)
def read(p):return p.read_text(encoding='utf-8')
def fixture(name):
 d=json.loads(read(b/'test/fixtures'/name));need(d['synthetic'] is True,name+' synthetic');return d
for rel,h in base.items():
 p=r/rel;same=p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h
 if not same:changed.append(rel)
 if rel not in allowed:
  protected+=1;need(same,'Protected changed '+rel)
new=sorted(p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and '.git' not in p.parts and 'node_modules' not in p.parts and p.relative_to(r).as_posix() not in base)
need(set(new)<=new_allowed,'Unexpected new files '+str(set(new)-new_allowed))
d=fixture('consistency-synthetic.json')
counts={}
for x in d['selections']:counts[x['dishId']]=counts.get(x['dishId'],0)+1
need(counts==d['counters'] and counts!=d['counterMismatch'],'Counter oracle')
need(len({d['summary']['version'],d['order']['version'],d['order']['revisionNo'],d['plan']['revisionNo']})==4,'Independent versions')
plan=d['plan'];rep=d['planReplacement']
need(sum(x['qty'] for x in plan['sources'])==100,'Plan baseline')
need(sum(x['qty'] for x in plan['sources'] if x['orderId']!=rep['orderId'])+rep['qty']==rep['expectedQty']==105,'Replacement arithmetic')
sets=[set(plan[k]) for k in ['includedPointIds','missingPointIds','excludedPointIds']]
need(set.union(*sets)==set(plan['expectedPointIds']) and all(not sets[i]&sets[j] for i in range(3) for j in range(i+1,3)),'Manifest partition')
need(d['retry']['stages']==['BEFORE_COMMIT','AFTER_COMMIT_BEFORE_RESPONSE','AFTER_OUTBOX_BEFORE_PLAN'],'Fault labels')
d=fixture('delta-synthetic.json'); fields=('dishId','recipeId','portionCode','role','unit')
def keyed(xs):return {tuple(x[k] for k in fields):x['qty'] for x in xs}
a=keyed(d['baseline']);z=keyed(d['target'])
actual={k[1]:z.get(k,0)-a.get(k,0) for k in a.keys()|z.keys() if z.get(k,0)!=a.get(k,0)}
need(actual=={x['recipeId']:x['qtyDelta'] for x in d['expectedDelta']},'Recipe delta')
need(sum(a.values())==sum(z.values())==100,'Delta totals')
need(len({x['unit'] for x in d['mixedUnits']})==2,'Mixed unit distinction')
d=fixture('adapter-synthetic.json');cs={x['id']:x for x in d['cases']};need(len(cs)==6,'Six oracle variants')
for k in ['energyKcal','proteinG','fatG','carbG']:
 need(cs['complete_zero']['expectedNutrition'][k]=='0.00','Valid zero '+k)
 need(cs['missing_source']['expectedNutrition'][k] is None,'Incomplete '+k)
need(bool(cs['missing_source']['expectedNutrition']['missing']),'Safe missing')
need(cs['dependency_timeout']['expectedError']['code']=='ERR-ORD-503-01','Timeout oracle')
need(cs['out_of_scope']['expectedError']['code']=='ERR-ORD-404-01','Scope oracle')
need(cs['unknown_allergens']['expectedAllergenStatus']=='UNKNOWN','Unknown allergen')
need(cs['authorized_empty_list']['expectedList']['total']==0,'Empty total')
for c in cs.values():
 raw=json.dumps({k:x for k,x in c.items() if k.startswith('expected')})
 for f in ['ingredientId','breakdown','internalNote','password','qrToken']:need(f not in raw,'Unsafe expected '+f)
counts={};ids=[]
for name in ['test-cases.md','system-test-cases.md']:
 rows=[line.strip('|').split('|') for line in read(b/'test'/name).splitlines() if line.startswith('| TC-E6-')]
 ids.extend(x[0].strip().removeprefix('TC-E6-') for x in rows)
 counts[name]={'cases':len(rows),'NOT_RUN':sum(x[-1].strip()=='NOT RUN' for x in rows),'BLOCKED':sum(x[-1].strip().startswith('BLOCKED') for x in rows)}
readme=read(b/'test/fixtures/README.md')
mapped=re.findall(r'^\| ((?:SEL|SUB|DEF|CHG|SEC|QR|PLAN|SYS)-\d{2}) \|',readme,re.M)
need(len(mapped)==22 and set(mapped)==set(ids),'22 case fixture mapping')
need('Đối chiếu fixture với 22 ca' in read(b/'preview.html'),'Preview fixture update absent')
result={'kind':'DOCUMENT_AND_SYNTHETIC_CHECK_ONLY','backend_tests_executed':0,'fixture_files_read':4,'json_fixtures_checked':3,'case_mappings':len(mapped),'case_counts':counts,'protected_files_checked':protected,'changed_existing_files':sorted(changed),'new_files':sorted(set(new)|{'docs/chon-mon-order/validation/fixture-review-check-result.json'}),'errors':errors}
(v/'fixture-review-check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
