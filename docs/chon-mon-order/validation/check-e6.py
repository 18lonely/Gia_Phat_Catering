"""Static documentation validation only. Does not test product behavior."""
from pathlib import Path
import re,json,hashlib
B=Path(__file__).resolve().parents[1];D=B.parent
errors=[]
def need(ok,msg):
 if not ok:errors.append(msg)
def read(p):return p.read_text(encoding='utf-8')
mapping=json.loads(read(B/'validation/capability-map.json'))
catalog=json.loads(read(B/'api/endpoint-catalog.json'))
need(len(mapping)==19,'19 features required');need(sum(x['priority']=='P0' for x in mapping)==14,'P0 mismatch')
need([x['feature'] for x in mapping]==[f'FEAT-{n:03}' for n in range(30,49)],'Feature sequence')
rtm=read(B/'test/traceability.md');ac=read(B/'userstories/acceptance-criteria.md');tc=read(B/'test/review-test-cases.md');ui=read(B/'html-wireframe/order-workbench.html')
for i,m in enumerate(mapping,1):
 for key in ['feature','fr','uc','story','screen']:need(m[key] in rtm,'RTM missing '+m[key])
 need((B/f'usecases/{m["uc"]}.md').exists(),'UC absent')
 for j in range(1,4):
  a=f'AC-E6-{i:03}-{j}';t=f'TC-E6-{i:03}-{j}'
  need(a in ac and a in rtm and a in tc,'AC link '+a)
  need(t in rtm and t in tc,'TC link '+t)
need(len(re.findall(r'^### AC-E6-',ac,re.M))==57,'AC count')
need(len(re.findall(r'^\| TC-E6-',tc,re.M))==57,'test count')
need(len(catalog)==26,'API count');need(len({(x['method'],x['path']) for x in catalog})==len(catalog),'duplicate route')
for x in catalog:need(x['id'] in read(B/'api/api-spec.md'),'catalog mismatch')
need(len(re.findall(r'<section data-screen=',ui))==13,'screen count')
for n in range(1,16):need(f'ORD-Q{n:02}' in read(B/'review/questions.md'),'missing question')
for n in (46,47):need(not any(f'FEAT-{n:03}' in x['features'] for x in catalog),'Health route opened')
# Validate local Markdown file links, including outside E6. Markdown anchors separately checked for explicit headings only by reviewer.
for f in B.rglob('*.md'):
 if 'diagrams' in f.parts:continue
 for dest in re.findall(r'\]\(([^)]+)\)',read(f)):
  if dest.startswith(('http','mailto:','#')):continue
  target=dest.split('#')[0]
  need((f.parent/target).exists(),f'Broken link {f.relative_to(D)} -> {dest}')
baseline=json.loads(read(B/'validation/baseline-sha256.json'))
schema=D/'nen-tang/srs/schema.dbml'
need(hashlib.sha256(schema.read_bytes()).hexdigest()==baseline['docs/nen-tang/srs/schema.dbml'],'Shared DBML changed')
need(len(re.findall(r'^Table \w+ \{',read(schema),re.M))==65,'Shared table count')
protected=['docs/cost/accounting/business-rules.md','docs/cost/review/accountant-input.md']
for p in protected:
 f=D.parent/p;need(hashlib.sha256(f.read_bytes()).hexdigest()==baseline[p],'Protected source changed '+p)
statuses=re.findall(r'\| (NOT RUN|BLOCKED[^|\n]*) \|',tc)
result={'kind':'DOCUMENT_CHECK_ONLY','features':19,'P0':14,'P1':5,'usecases':19,'AC':57,'new_test_cases':57,'legacy_tests':10,'NOT_RUN':sum(s=='NOT RUN' for s in statuses),'BLOCKED':sum(s.startswith('BLOCKED') for s in statuses),'http_endpoints':26,'ports':2,'gate_features':['FEAT-046','FEAT-047'],'wireframe_screens':13,'schema_tables':65,'schema_unchanged':True,'backend_tests_executed':0,'errors':errors}
(B/'validation/check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
