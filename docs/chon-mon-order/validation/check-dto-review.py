"""Checks document coverage only; does not validate live request/response payloads."""
from pathlib import Path
import json,re,hashlib
B=Path(__file__).resolve().parents[1];root=B.parents[1];errors=[]
def read(p):return p.read_text(encoding="utf-8")
def need(ok,msg):
    if not ok:errors.append(msg)
api=read(B/"api/api-spec.md");names=[]
for title,end in [("Request types","Response types"),("Response types","Catalog")]:
    section=api.split("## "+title)[1].split("## "+end)[0]
    names += [n for n in re.findall(r"^\| (\w+) \|",section,re.M) if n!="Type"]
matrix=read(B/"api/dto-presence-review.md")
covered=re.findall(r"^\| (\w+) \|",matrix,re.M);covered=[n for n in covered if n!="DTO"]
need(len(names)==34 and names==covered,"DTO coverage/order mismatch")
reg=read(B/"review/contract-gap-register.md")
ids=re.findall(r"^\| (E6-CG-\d{2}) \|",reg,re.M)
need(ids==[f"E6-CG-{i:02}" for i in range(1,15)],"Gap IDs/count mismatch")
for row in reg.splitlines():
    if row.startswith("| E6-CG-"):
        cells=[c.strip() for c in row.split("|")[1:-1]]
        need(len(cells)==5 and all(cells),"Gap row missing owner/artifact/closure")
need("0/14" in reg and "OPEN" in reg,"Gap status not explicit")
need("qrId?:Id hoặc null" in api,"Existing nullable qrId unclear")
base=json.loads(read(B/"validation/dto-baseline-sha256.json"))
protected=["review/questions.md","review/decision-review.md","review/handoff.md","review/independent-handoff.md","review/contract-handoff.md","review/adapter-handoff.md","test/decision-review-cases.md","userstories/acceptance-criteria.md","api/endpoint-catalog.json","html-wireframe/order-workbench.html"]
paths=[B/p for p in protected]+[root/p for p in ["docs/nen-tang/srs/schema.dbml","docs/cost/accounting/business-rules.md","docs/cost/review/accountant-input.md"]]
for p in paths:need(hashlib.sha256(p.read_bytes()).hexdigest()==base[p.relative_to(root).as_posix()],"Protected changed "+p.name)
preview=read(B/"preview.html")
for a in ["doc-api-dto-presence-review-md","doc-review-contract-gap-register-md","doc-review-dto-handoff-md"]:need('id="'+a+'"' in preview,"Missing preview section "+a)
result={"kind":"DOCUMENT_COVERAGE_ONLY","dto_reviewed":len(covered),"gap_groups":len(ids),"gap_groups_closed":0,"protected_files_checked":len(paths),"backend_tests_executed":0,"errors":errors}
(B/"validation/dto-check-result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
