"""Document-only proposal scope/preservation check.
Reads the new session baseline, protects all baseline files except the six named
current documents/preview; writes only preservation-result.json in this folder.
Does not execute fixtures, backend, UI, or historical checkers.
"""
from pathlib import Path
import hashlib,json,re
v=Path(__file__).resolve().parent
r=v.parents[3]
b=json.loads((v/'baseline-sha256.json').read_text(encoding='utf-8'))
allowed={'docs/chon-mon-order/review/contract-gap-register.md','docs/chon-mon-order/gap-analysis.md','docs/chon-mon-order/preview.html','docs/project-dashboard.md','docs/gia-phat/review/progress-assessment.md','docs/gia-phat/review/next-session-prompt.md'}
new_allowed={str((v/n).relative_to(r)).replace(chr(92),'/') for n in ['baseline-sha256.json','check-e6-result.json','diagram-render-result.json','check-proposal.py','preservation-result.json']}
files={p.relative_to(r).as_posix():p for p in r.rglob('*') if p.is_file() and '.git' not in p.parts and 'node_modules' not in p.parts}
hashes={k:hashlib.sha256(p.read_bytes()).hexdigest() for k,p in files.items()}
changed=sorted(k for k,h in b.items() if hashes.get(k)!=h)
new=sorted(set(files)-set(b))
errors=[]
if set(changed)-allowed:errors.append('Protected changes: '+str(set(changed)-allowed))
if set(new)-new_allowed:errors.append('Unexpected new files: '+str(set(new)-new_allowed))
reg=(r/'docs/chon-mon-order/review/contract-gap-register.md').read_text(encoding='utf-8')
proposal=reg.split('## Đề xuất trình người dùng duyệt ngày 12/11/2026')[1]
for phrase in ['CHỜ DUYỆT, chưa có hiệu lực','14/14 OPEN','CG02','CG03','E6-EVID-002','Không ghi tất cả CG CLOSED','thời gian cache','retention','scope người đặt tổng một/nhiều công ty']:
 if phrase not in proposal:errors.append('Missing proposal guard: '+phrase)
rows=[line for line in proposal.splitlines() if re.match(r'^\| CG[0-9]{2}:',line)]
if len(rows)!=10:errors.append('Expected ten proposal rows')
if 'Đề xuất trình người dùng duyệt' not in (r/'docs/chon-mon-order/preview.html').read_text(encoding='utf-8'):errors.append('Preview missing proposal')
check=json.loads((v/'check-e6-result.json').read_text(encoding='utf-8'))
render=json.loads((v/'diagram-render-result.json').read_text(encoding='utf-8'))
if check['errors']:errors.append('check-e6 errors')
if len(render)!=8 or any(x['status']!='RENDERED' for x in render):errors.append('Render incomplete')
result={'kind':'DOCUMENT_PROPOSAL_AND_PRESERVATION_ONLY','backend_tests_executed':0,'baseline_files':len(b),'protected_files_unchanged':sum(k not in allowed and hashes.get(k)==h for k,h in b.items()),'changed_files':{k:hashes.get(k) for k in changed},'new_files_excluding_this_result':{k:hashes[k] for k in new if k!= (v/'preservation-result.json').relative_to(r).as_posix()},'proposal_rows':len(rows),'CG_OPEN':14,'CG_CLOSED':0,'errors':errors}
(v/'preservation-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
