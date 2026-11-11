"""Validate BA document references and traceability; no product tests are run."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[3]
B=ROOT/'docs/cost'
sources=[B/'srs/spec.md',ROOT/'docs/nen-tang/srs/spec.md',ROOT/'docs/thuc-don-dinh-luong/srs/spec.md',ROOT/'docs/gia-phat/brainstorms/quy-tac-thuc-don.md']
code=r'(?:(?:FR|BR|NFR)-[A-Z][A-Z0-9-]*-\d{3}|ERR-[A-Z][A-Z0-9-]*-\d{3}-\d{2})'
definitions=set()
for p in sources:
 definitions.update(re.findall(r'^\|\s*`?('+code+r')`?\s*\|',p.read_text(encoding='utf-8'),re.M))
spec=(B/'srs/spec.md').read_text(encoding='utf-8')
frs=set(re.findall(r'^\| `(FR-COST-[A-Z]+-\d{3})` \|',spec,re.M))
assert len(frs)==45
files=sorted((B/'usecases').glob('UC-COST-*.md'))
assert len(files)==16
expected={f'UC-COST-{n:03}' for n in range(1,17)}
covered=set()
for p in files:
 s=p.read_text(encoding='utf-8')
 assert s.startswith('# '+p.stem+':')
 for label in ['Tác nhân chính','Tiền điều kiện','Kích hoạt','Hậu điều kiện','Đảm bảo tối thiểu','Luồng sự kiện chính','Luồng nhánh và ngoại lệ','Quy tắc và điểm mở']:
  assert label in s,(p.name,label)
 mapping=re.search(r'\*\*Truy vết FR:\*\* (.+)',s).group(1)
 mapped=set(re.findall(r'FR-COST-[A-Z]+-\d{3}',mapping))
 assert mapped and mapped<=frs,p.name
 covered |= mapped
 main=s.split('## Luồng sự kiện chính')[1].split('## Luồng nhánh')[0]
 steps=[int(n) for n in re.findall(r'^(\d+)\. ',main,re.M)]
 assert steps==list(range(1,len(steps)+1)),p.name
 for step in re.findall(r'^- \*\*(\d+)[a-z]\.',s,re.M):
  assert int(step) in steps,(p.name,step)
assert frs-covered=={'FR-COST-MEAL-007','FR-COST-ALR-004'},frs-covered
docs=files+[B/'srs/usecase-diagram.md',B/'ui/user-flow.md']
alltext='\n'.join(p.read_text(encoding='utf-8') for p in docs)
unknown=set(re.findall(code,alltext))-definitions
assert not unknown,sorted(unknown)
assert set(re.findall(r'UC-COST-\d{3}',alltext))==expected
for p in docs:
 s=p.read_text(encoding='utf-8')
 assert s.count('```')%2==0,p.name
 for target in re.findall(r'\]\(([^)]+)\)',s):
  if target.startswith(('http:','https:')):continue
  loc,_,anchor=target.partition('#')
  dest=(p.parent/loc).resolve() if loc else p
  assert dest.is_file(),(p.name,target)
  if anchor:assert f'id="{anchor}"' in dest.read_text(encoding='utf-8'),(p.name,target)
questions=set(re.findall(r'^\| (FLOW-COST-Q\d{2}) \|',(B/'ui/user-flow.md').read_text(encoding='utf-8'),re.M))
assert set(re.findall(r'FLOW-COST-Q\d{2}',alltext))==questions
matrix=(B/'srs/usecase-diagram.md').read_text(encoding='utf-8')
rows=re.findall(r'^\| `(FR-COST-[A-Z]+-\d{3})` \|',matrix,re.M)
assert len(rows)==45 and set(rows)==frs
print('PASS: 16 use cases; 43 FR with flows + 2 explicitly deferred; 45 unique matrix rows.')
print('PASS: FR/BR/ERR/NFR definitions, numbered branches, UC IDs, links, anchors, 10 open questions.')
