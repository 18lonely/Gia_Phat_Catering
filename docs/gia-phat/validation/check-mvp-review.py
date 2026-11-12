"""Structural BA checks + synthetic Decimal arithmetic. Does not test any backend."""
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
import json,re

DOC=Path(__file__).resolve().parents[2]
errors=[]
def check(value,msg):
    if not value: errors.append(msg)

schema=(DOC/'nen-tang/srs/schema.dbml').read_text(encoding='utf-8')
tables=re.findall(r'^Table (\w+) \{',schema,re.M)
check(len(tables)==65 and len(set(tables))==65,'DBML table names/count')
for target in re.findall(r'ref:\s*[><-]\s*(\w+)\.',schema): check(target in tables,'unknown FK '+target)
counts={}
allroutes=[]
for mod,folder in [('NUTR','dinh-duong'),('AIO','agent-noi-bo')]:
    base=DOC/folder
    srs=(base/'srs/spec.md').read_text(encoding='utf-8')
    ac=(base/'userstories/acceptance-criteria.md').read_text(encoding='utf-8')
    tc=(base/'test/test-cases.md').read_text(encoding='utf-8')
    rtm=(base/'test/traceability.md').read_text(encoding='utf-8')
    backlog=(base/'userstories/backlog.md').read_text(encoding='utf-8')
    api=(base/'api/api-spec.md').read_text(encoding='utf-8')
    wire=(base/'ui/wireframe-ascii.md').read_text(encoding='utf-8')
    frs=set(re.findall(r'^\| (FR-[\w-]+) \|',srs,re.M))
    stories=re.findall(r'^\| (US-[\w-]+) \|',backlog,re.M)
    acs=re.findall(r'^## (AC-[\w-]+)',ac,re.M)
    tests=re.findall(r'^\| (TC-[\w-]+) \|',tc,re.M)
    check(len(stories)==len(frs),folder+' story count')
    check(len(acs)==len(stories)*3,folder+' three AC/story')
    check(len(acs)==len(set(acs)) and len(tests)==len(set(tests)),folder+' duplicate AC/TC')
    for fr in frs:
        for text,label in [(rtm,'RTM'),(backlog,'backlog'),(tc,'test'),(api,'API')]: check(fr in text,fr+' missing in '+label)
    for code in re.findall(r'^\| ((?:BR|NFR|ERR)-[\w-]+) \|',srs,re.M): check(code in tc,code+' without test')
    for aid in acs: check(aid in tc and aid in rtm,aid+' orphan')
    for story in stories: check(len(re.findall(r'^## AC-.* — '+story+r',',ac,re.M))>=3,story+' AC missing')
    for uc in re.findall(r'\[(UC-[\w-]+)\]',backlog): check((base/'usecases'/f'{uc}.md').is_file(),uc+' missing')
    catalog=json.loads((base/'api/endpoint-catalog.json').read_text(encoding='utf-8'))
    for ep in catalog:
        check(ep['id'] in api and ep['path'] in api,ep['id']+' missing contract')
        check(ep['fr'] in frs,ep['id']+' unknown FR')
        check(ep['ui'] in wire,ep['id']+' unknown screen')
        allroutes.append((ep['method'],ep['path']))
    for table in set(re.findall(r'\b(?:nutrient_value_revisions|nutrition_calculations|agent_run_contexts|agent_tool_events)\b',api+rtm)):
        check(table in tables,'missing table '+table)
    # Count statuses only on table rows defining a TC, never prose.
    testrows=[line for line in tc.splitlines() if re.match(r'^\| TC-',line)]
    counts[mod]={'fr':len(frs),'story':len(stories),'ac':len(acs),'test':len(tests),'blocked':sum('BLOCKED:' in x for x in testrows),'notRun':sum('NOT RUN' in x for x in testrows),'api':len(catalog)}
    check(counts[mod]['blocked']+counts[mod]['notRun']==len(tests),folder+' test statuses')
check(len(allroutes)==len(set(allroutes))==13,'duplicate API route/count')

changed=[DOC/'OVERVIEW.md',DOC/'gia-phat/01-prd.md',DOC/'gia-phat/02-roadmap.md',DOC/'nen-tang/srs/erd.md',DOC/'thuc-don-dinh-luong/srs/spec.md',DOC/'cost/srs/spec.md',DOC/'gia-phat/review/mvp-e4-e5-handoff.md']
files=list((DOC/'dinh-duong').rglob('*.md'))+list((DOC/'agent-noi-bo').rglob('*.md'))+changed
for p in files:
    check(p.exists(),'missing file '+str(p))
    if not p.exists(): continue
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'^[a-z]+:',target) or target.startswith('#'): continue
        target=target.split('#')[0]
        check((p.parent/target).exists(),f'broken link {p.relative_to(DOC)} -> {target}')

# Independent arithmetic check using explicitly artificial input, not a nutrition source.
D=Decimal
values=[D('100'),D('10'),D('2'),D('15')]
dish=[D('50')*D('0.8')*v/D('100') for v in values]
check(dish==[D('40'),D('4'),D('0.8'),D('6')],'synthetic dish formula')
meal=[a+b for a,b in zip(dish,map(D,['10','1','0.2','1.5']))]
check(meal==list(map(D,['50','5','1','7.5'])),'synthetic combination formula')
check(D('1.005').quantize(D('.01'),rounding=ROUND_HALF_UP)==D('1.01'),'proposed rounding fixture')

# Preserve user-confirmed accounting facts and pending question IDs in their original sources.
br=(DOC/'cost/accounting/business-rules.md').read_text(encoding='utf-8')
inp=(DOC/'cost/review/accountant-input.md').read_text(encoding='utf-8')
for n in range(1,11): check(f'CK-Q{n:02}' in br and re.search(rf'\| CK-Q{n:02} .*CHỜ XÁC NHẬN',br),'CK question changed '+str(n))
for n in range(1,7): check(f'DATA-COST-Q{n:02}' in inp,'DATA-COST question missing '+str(n))

result={'scope':'Structural document validation + synthetic Decimal only; backend tests run=0','counts':counts,'tables':len(tables),'markdownFilesChecked':len(files),'errors':errors}
(Path(__file__).parent/'mvp-check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
if errors: raise SystemExit(1)
