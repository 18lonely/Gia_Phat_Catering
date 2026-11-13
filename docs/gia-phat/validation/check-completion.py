"""Document integrity, traceability and inventory. No product tests."""
from pathlib import Path
import re,json
D=Path(__file__).resolve().parents[2]
folders=['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo']
errors=[]
def need(ok,msg):
 if not ok:errors.append(msg)
def text(p):return p.read_text(encoding='utf-8') if p.exists() else ''
def getfr(s):return set(re.findall(r'^\|\s*`?(FR-[A-Z]+-[A-Z]+-\d{3})`?\s*\|',s,re.M))
def expand(cell):
 result=[];prefix=None;prev=None
 for m in re.finditer(r'`([^`]+)`',cell):
  x=m[1];before=cell[:m.start()]
  if x.startswith('FR-'):v=x
  elif re.fullmatch(r'[A-Z]+-\d{3}',x):v='FR-MENU-'+x
  elif re.fullmatch(r'\d{3}',x) and prefix:v=prefix+x
  else:continue
  if '→' in before[(prev[1] if prev else 0):] and prev and v.rsplit('-',1)[0]==prev[0].rsplit('-',1)[0]:
   result.extend(v.rsplit('-',1)[0]+'-'+str(i).zfill(3) for i in range(int(prev[0][-3:]),int(v[-3:])+1))
  else:result.append(v)
  prefix=v[:-3];prev=(v,m.end())
 return set(result)

# Normalize existing abbreviated MENU links into an explicit RTM, without changing its stories/AC.
base=D/'thuc-don-dinh-luong';back=text(base/'userstories/backlog.md');ac=text(base/'userstories/acceptance-criteria.md');tests=text(base/'test/test-cases.md')
menumap={}
for line in back.splitlines():
 if not re.match(r'^\| `US-MENU-',line):continue
 c=[x.strip() for x in line.split('|')[1:-1]];sid=c[0].strip('`');num=sid.split('-')[-1]
 for fr in expand(c[2]):
  menumap.setdefault(fr,[]).append({'story':sid,'uc':c[3].strip('`'),'ac':sorted(set(re.findall(r'AC-MENU-'+num+r'-\d+',ac))),'test':sorted(set(re.findall(r'TC-MENU-'+num+r'\d{2}\b',tests)))})
rtm='# RTM MENU: chuẩn hóa tham chiếu hiện có\n\nPhiên bản0.1.0 · 2026-11-11 · Draft. Sinh từ backlog/AC/test hiện có; mở rộng mã rút gọn, không tự bổ sung độ phủ. Ca quy tắc riêng nằm tại [rule-test-cases.md](rule-test-cases.md).\n\n| Phiên bản | Ngày | Nội dung |\n| :--- | :--- | :--- |\n| 0.1.0 | 2026-11-11 | Chuẩn hóa FR–story–AC–test để kiểm coverage |\n\n| FR | Story | UC | AC | TC | Trạng thái |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n'
for fr in sorted(getfr(text(base/'srs/spec.md'))):
 entries=menumap.get(fr,[])
 if not entries:rtm+=f'| {fr} | Chưa có | Chưa có | Chưa có | Chưa có | CHƯA CÓ mapping story cụ thể; review phạm vi/hoãn |\n'
 for e in entries:rtm+=f'| {fr} | {e["story"]} | {e["uc"]} | {", ".join(e["ac"]) or "CHƯA TÌM THẤY"} | {", ".join(e["test"]) or "CHƯA TÌM THẤY"} | Thiết kế; chưa chạy backend |\n'
(base/'test/traceability.md').write_text(rtm,encoding='utf-8')
inventory=[]
required=['epic-spec.md','srs/spec.md','srs/usecase-diagram.md','srs/flows.md','srs/states.md','srs/erd.md','api/api-spec.md','ui/user-flow.md','userstories/backlog.md','userstories/acceptance-criteria.md','test/checklist.md','test/test-cases.md','gap-analysis.md','preview.html']
for f in folders:
 b=D/f;srs=text(b/'srs/spec.md');fr=getfr(srs);bk=text(b/'userstories/backlog.md');tc=text(b/'test/test-cases.md');rt=text(b/'test/traceability.md')
 for p in required:need((b/p).exists(),f+' missing '+p)
 cat=json.loads(text(b/'api/endpoint-catalog.json'))
 if isinstance(cat,dict):cat=cat['endpoints']
 routes=[(e['method'],e['path']) for e in cat]
 need(len(routes)==len(set(routes)),f+' duplicate routes')
 if f=='nen-tang':
  for code in fr:need(code in bk and code in tc and code in rt,'CORE orphan '+code)
  for code in re.findall(r'^\| `(BR-[\w-]+|ERR-[\w-]+|NFR-[\w-]+)`',srs,re.M):need(code in tc,'CORE untested '+code)
  a=text(b/'userstories/acceptance-criteria.md');need(len(re.findall(r'^## AC-CORE-',a,re.M))==78,'CORE AC count')
 if f=='thuc-don-dinh-luong':
  sf={x for e in cat for x in e['fr']};ports={'FR-MENU-MNU-004','FR-MENU-RUL-007','FR-MENU-APV-006','FR-MENU-RCP-007'}
  need(fr==sf|ports,'MENU API/port coverage mismatch')
  rul=text(b/'test/rule-test-cases.md');need(len(re.findall(r'^\| TC-RULE-',rul,re.M))==86,'MENU rule cases')
 # Counts are lexical structural coverage, explicitly not acceptance coverage.
 storyrefs=set().union(*(expand(l) for l in bk.splitlines() if l.startswith('|'))) if f=='thuc-don-dinh-luong' else set(re.findall(r'FR-[A-Z]+-[A-Z]+-\d{3}',bk))
 if f=='thuc-don-dinh-luong':testrefs={k for k,v in menumap.items() if any(e['test'] for e in v)}
 elif f=='cost':
  scenarios=json.loads(text(b/'test/scenario-catalog.json'))
  storyrefs={code for story in scenarios['stories'] for code in story['fr']}
  testrefs=storyrefs.copy()
 else:testrefs=set(re.findall(r'FR-[A-Z]+-[A-Z]+-\d{3}',tc))
 ui=text(b/'ui/user-flow.md')+'\n'+'\n'.join(text(p) for p in (b/'html-wireframe').glob('*.html'))
 uirefs=set(re.findall(r'FR-[A-Z]+-[A-Z]+-\d{3}',ui))
 if f in ['nen-tang','dinh-duong','agent-noi-bo']:
  uirefs={code for line in rt.splitlines() if re.search(r'UI-(CORE|NUTR|AIO)-\d+',line) for code in re.findall(r'FR-[A-Z]+-[A-Z]+-\d{3}',line)}
 inventory.append(dict(folder=f,fr=len(fr),storyLinked=len(fr&storyrefs),testLinked=len(fr&testrefs),uiExplicitLinked=len(fr&uirefs),httpEndpoints=len(cat),stories=len(set(re.findall(r'US-[A-Z]+-\d+',bk))),ucFiles=len(list((b/'usecases').glob('UC-*.md'))),htmlFiles=len(list((b/'html-wireframe').glob('*.html')))))

# Check links in all modules and the current shared deliverables, excluding historical reports/scripts.
files=[]
for f in folders+['chon-mon-order']:
 files += [p for p in (D/f).rglob('*.md') if 'validation' not in p.parts]
files += [D/'OVERVIEW.md',D/'project-dashboard.md',D/'gia-phat/00-ke-hoach-tong-the.md',D/'gia-phat/brainstorms/pham-vi-san-pham.md',D/'gia-phat/review/ba-completion-handoff.md']
broken=[]
for p in files:
 need(p.exists(),'missing shared '+str(p))
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text(p)):
  if re.match(r'^[a-z]+:',target) or target.startswith('#'):continue
  target=target.split('#')[0]
  if not (p.parent/target).exists():broken.append(str(p.relative_to(D))+' -> '+target)
need(not broken,'broken links: '+json.dumps(broken,ensure_ascii=False))
# Preserve pending accounting questions and core threshold source; no new accounting data fabricated.
account=text(D/'cost/accounting/business-rules.md');inp=text(D/'cost/review/accountant-input.md')
for i in range(1,11):need(bool(re.search(rf'\| CK-Q{i:02} .*CHỜ XÁC NHẬN',account)),'CK status '+str(i))
for i in range(1,7):need(f'DATA-COST-Q{i:02}' in inp,'missing DATA-COST question')
e6=text(D/'chon-mon-order/srs/spec.md');need(len(getfr(e6))==19,'E6 FR count');need('GATED O-03' in e6,'E6 health gate')
result={'scope':'Structural BA validation only; backend tests=0','inventory':inventory,'markdownFilesChecked':len(files),'errors':errors,'menuUnmappedFR':sorted(getfr(text(base/'srs/spec.md'))-set(menumap))}
(Path(__file__).parent/'completion-check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
