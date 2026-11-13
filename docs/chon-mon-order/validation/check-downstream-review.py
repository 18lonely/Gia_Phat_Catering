"""Static preservation check against this session's pre-edit snapshot; no backend."""
from pathlib import Path
import hashlib,json,re
b=Path(__file__).resolve().parents[1]; r=b.parents[1]
baseline=json.loads((b/'validation/downstream-baseline-sha256.json').read_text(encoding='utf-8'))
allowed={f'docs/chon-mon-order/{x}' for x in ['userstories/backlog.md','test/checklist.md','ui/user-flow.md','srs/flows.md','srs/usecase-diagram.md','test/evidence-protocol.md','test/fixtures/README.md','review/contract-gap-register.md','gap-analysis.md','preview.html','validation/check-result.json','validation/diagram-render-result.json','validation/contract-check-result.json','validation/dto-check-result.json','validation/adapter-check-result.json']}
allowed.update(['docs/project-dashboard.md','docs/gia-phat/review/progress-assessment.md','docs/gia-phat/review/next-session-prompt.md'])
errors=[]; changed=[]; protected=0
for rel,h in baseline.items():
 p=r/rel
 same=p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h
 if not same: changed.append(rel)
 if rel not in allowed and not rel.startswith('docs/chon-mon-order/srs/diagrams/'):
  protected+=1
  if not same: errors.append('Protected source changed: '+rel)
back=(b/'userstories/backlog.md').read_text(encoding='utf-8')
ids=re.findall(r'^\| (US-E6-\d{3}) \|',back,re.M)
if ids!=[f'US-E6-{n:03}' for n in range(1,20)]:errors.append('Story IDs/order changed')
cap=json.loads((b/'validation/capability-map.json').read_text(encoding='utf-8'))
for c in cap:
 if c['fr'] not in back: errors.append('Missing FR '+c['fr'])
# Mermaid IDs in flowcharts must not silently conflate two differently labelled actors/actions.
for f in ['ui/user-flow.md','srs/usecase-diagram.md']:
 s=(b/f).read_text(encoding='utf-8')
 labels={}
 for key,label in re.findall(r'\b([A-Za-z][A-Za-z0-9]*)\[([^\]\n]+)\]',s):
  if key in labels and labels[key]!=label:errors.append('Conflicting Mermaid node '+f+':'+key)
  labels[key]=label
new=sorted(p.relative_to(r).as_posix() for p in (r/'docs').rglob('*') if p.is_file() and p.relative_to(r).as_posix() not in baseline)
result={'kind':'DOCUMENT_PRESERVATION_ONLY','backend_tests_executed':0,'protected_files_checked':protected,'story_ids_checked':len(ids),'changed_existing_files':len(changed),'errors':errors}
(b/'validation/downstream-check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
out='# Manifest phiên hạ nguồn ngày 12/11/2026\n\nSo SHA256 trước phiên; không Git. Các file render là đầu ra tái sinh. Mọi file có trước phiên ngoài phạm vi cho phép phải giữ hash, gồm UC/API/AC/RTM, các bộ ca và evidence, schema/Cost, wireframe và snapshot handoff/report cũ.\n\n## File đã thay đổi\n\n'
for f in sorted(changed):out+=f'- [{f}]({Path(__import__("os").path.relpath(r/f,b/"validation")).as_posix()})\n'
out+='\n## File mới\n\n'
for f in new:out+=f'- [{f}]({Path(__import__("os").path.relpath(r/f,b/"validation")).as_posix()})\n'
(b/'validation/downstream-change-manifest.md').write_text(out,encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
