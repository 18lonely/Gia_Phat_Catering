"""Structural/traceability checks only; does not run product acceptance tests."""
from pathlib import Path
import json,re

B=Path(__file__).resolve().parents[1]
d=json.loads((B/'test/scenario-catalog.json').read_text(encoding='utf-8'))
api=json.loads((B/'api/endpoint-catalog.json').read_text(encoding='utf-8'))
srs=(B/'srs/spec.md').read_text(encoding='utf-8')
frs=set(re.findall(r'^\| `(FR-COST-[A-Z]+-\d{3})`',srs,re.M))
actual={f for s in d['stories'] for f in s['fr']}
assert len(frs)==45 and len(actual)==43
assert actual.isdisjoint(d['deferred']) and actual|set(d['deferred'])==frs
cases=[c for s in d['stories'] for c in s['cases']]
refs={r for c in cases for r in c['refs']}
local_rules=set(re.findall(r'^\| `(BR-(?:PRC|CALC|EST)-\d{3})`',srs,re.M))
errors=set(re.findall(r'^\| `(ERR-COST-\d{3}-\d{2})`',srs,re.M))
nfr=set(re.findall(r'^\| `(NFR-COST-\d{3})`',srs,re.M))
assert len(local_rules)==24 and local_rules<=refs,local_rules-refs
assert len(errors)==14 and errors<=refs,errors-refs
assert len(nfr)==8 and nfr<=refs,nfr-refs
api_spec=(B/'api/api-spec.md').read_text(encoding='utf-8')
proposed=set(re.findall(r'^\| (ERR-COST-\d{3}-\d{2}) \|',api_spec,re.M))
assert len(proposed)==6 and proposed<=refs,proposed-refs
for key in ['ac','tc']:assert len({c[key] for c in cases})==len(cases)
assert len({s['id'] for s in d['stories']})==len(d['stories'])
priorities={}
for line in srs.splitlines():
    if re.match(r'\| `FR-COST-',line):
        cells=line.split('|');priorities[cells[1].strip(' `')]=cells[3].strip()
api_ids={e['id'] for e in api['endpoints']}
for s in d['stories']:
    assert len(s['cases'])>=3
    assert all(priorities[f]==s['priority'] for f in s['fr']),(s['id'],s['priority'])
    assert set(s['apis'])<=api_ids
    for c in s['cases']:
        assert all(c[k].strip() for k in ['given','when','then','title'])
        assert c['status'].startswith(('BLOCKED','NOT RUN'))
ac=(B/'userstories/acceptance-criteria.md').read_text(encoding='utf-8')
tc=(B/'test/test-cases.md').read_text(encoding='utf-8')
assert ac.count('Scenario: ')==len(cases)
for c in cases:
    assert f"### {c['ac']} " in ac and f"### {c['tc']} " in tc
    assert c['tc'] in (B/'test/traceability.md').read_text(encoding='utf-8')
for p in [* (B/'userstories').glob('*.md'),* (B/'test').glob('*.md')]:
    for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('#'):continue
        assert (p.parent/target.split('#')[0]).exists(),(p,target)
print(json.dumps(dict(stories=len(d['stories']),scenarios=len(cases),activeFR=len(actual),deferredFR=len(d['deferred']),localBR=len(local_rules),srsErrors=len(errors),proposedApiErrors=len(proposed),nfr=len(nfr),blocked=sum(c['status'].startswith('BLOCKED') for c in cases),notRun=sum(c['status'].startswith('NOT RUN') for c in cases),executedProductTests=0),ensure_ascii=False))
