"""Preservation for the 2026-11-12 case review, never a backend test."""
from pathlib import Path
import hashlib, json, re

b = Path(__file__).resolve().parents[1]
r = b.parents[1]
v = b / 'validation'
baseline = json.loads((v/'case-review-baseline-sha256.json').read_text(encoding='utf-8'))
original = json.loads((v/'case-review-original.json').read_text(encoding='utf-8'))
allowed = {
    'docs/chon-mon-order/test/test-cases.md',
    'docs/chon-mon-order/test/system-test-cases.md',
    'docs/chon-mon-order/review/contract-gap-register.md',
    'docs/chon-mon-order/gap-analysis.md',
    'docs/chon-mon-order/preview.html',
    'docs/chon-mon-order/validation/check-result.json',
    'docs/chon-mon-order/validation/diagram-render-result.json',
    'docs/project-dashboard.md',
    'docs/gia-phat/review/progress-assessment.md',
    'docs/gia-phat/review/next-session-prompt.md',
}
# Renderer may rewrite only its already existing diagram artifacts.
allowed.update(p for p in baseline if p.startswith('docs/chon-mon-order/srs/diagrams/') and p.endswith(('.html','.svg')))
errors, changed, protected = [], [], 0
for rel, digest in baseline.items():
    p = r/rel
    same = p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == digest
    if not same:
        changed.append(rel)
    if rel not in allowed:
        protected += 1
        if not same:
            errors.append('Protected file changed: '+rel)

def rows(s):
    return [[x.strip() for x in line.strip('|').split('|')] for line in s.splitlines() if line.startswith('| TC-E6-')]

counts = {}
for rel, before in original.items():
    after = (r/rel).read_text(encoding='utf-8')
    old, new = rows(before), rows(after)
    if [(x[0],x[1],x[-1]) for x in old] != [(x[0],x[1],x[-1]) for x in new]:
        errors.append('Case ID/trace/status changed: '+rel)
    if '**Actual/Evidence: chưa có**' in before and '**Actual/Evidence: chưa có**' not in after:
        errors.append('Actual/Evidence changed: '+rel)
    counts[rel] = {'cases':len(new), 'NOT_RUN':sum(x[-1]=='NOT RUN' for x in new), 'BLOCKED':sum(x[-1].startswith('BLOCKED') for x in new)}
new_files = sorted(p.relative_to(r).as_posix() for p in r.rglob('*') if p.is_file() and '.git' not in p.parts and 'node_modules' not in p.parts and p.relative_to(r).as_posix() not in baseline)
result = {'kind':'DOCUMENT_PRESERVATION_ONLY','backend_tests_executed':0,'protected_files_checked':protected,'case_counts':counts,'changed_existing_files':sorted(changed),'new_files':new_files,'errors':errors}
(v/'case-review-check-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
