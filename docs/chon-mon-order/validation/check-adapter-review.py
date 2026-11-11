"""Static review/fixture integrity; does not execute an adapter or HTTP request."""
from pathlib import Path
import json, re, hashlib
B=Path(__file__).resolve().parents[1]; root=B.parents[1]; errors=[]
def read(p): return p.read_text(encoding="utf-8")
def need(ok,msg):
    if not ok: errors.append(msg)
cat=json.loads(read(B/"api/endpoint-catalog.json")); matrix=read(B/"api/route-validation-review.md")
ids=re.findall(r"^\| (API-ORD-\d{3}) ",matrix,re.M)
need(ids==[c["id"] for c in cat],"Route order/count mismatch")
for c in cat:
    row=next((r for r in matrix.splitlines() if r.startswith("| "+c["id"]+" ")),"")
    need(c["method"]+" `"+c["path"]+"`" in row,"Method/path mismatch "+c["id"])
d=json.loads(read(B/"test/fixtures/adapter-synthetic.json"));need(d["synthetic"] is True,"Synthetic flag")
cs={c["id"]:c for c in d["cases"]};need(len(cs)==6,"Oracle variant count")
keys=["energyKcal","proteinG","fatG","carbG"]
need(all(cs["complete_zero"]["expectedNutrition"][k]=="0.00" for k in keys),"Valid zero lost")
need(all(cs["missing_source"]["expectedNutrition"][k] is None for k in keys),"Missing coerced to zero")
need(bool(cs["missing_source"]["expectedNutrition"]["missing"]),"Missing reason absent")
need(cs["unknown_allergens"]["expectedAllergenStatus"]=="UNKNOWN","Unknown allergen mislabeled")
need(cs["dependency_timeout"]["expectedError"]["code"]=="ERR-ORD-503-01","Dependency mislabeled")
need(cs["out_of_scope"]["expectedError"]["code"]=="ERR-ORD-404-01","Scope error mismatch")
need(cs["authorized_empty_list"]["expectedList"]["total"]==0,"Empty list total")
for c in cs.values():
    expected={k:v for k,v in c.items() if k.startswith("expected")}
    raw=json.dumps(expected)
    for field in ["ingredientId","breakdown","internalNote","password","qrToken"]:
        need(field not in raw,"Internal field in expected oracle "+field)
base=json.loads(read(B/"validation/adapter-baseline-sha256.json"))
protected=["review/questions.md","review/decision-review.md","review/handoff.md","review/independent-handoff.md","review/contract-handoff.md","test/decision-review-cases.md","userstories/acceptance-criteria.md","html-wireframe/order-workbench.html","api/endpoint-catalog.json"]
paths=[B/p for p in protected]+[root/p for p in ["docs/nen-tang/srs/schema.dbml","docs/cost/accounting/business-rules.md","docs/cost/review/accountant-input.md"]]
for p in paths:need(hashlib.sha256(p.read_bytes()).hexdigest()==base[p.relative_to(root).as_posix()],"Protected changed "+p.name)
preview=read(B/"preview.html")
for anchor in ["doc-api-adapter-contract-review-md","doc-api-route-validation-review-md","doc-review-adapter-handoff-md"]:need('id="'+anchor+'"' in preview,"Missing preview "+anchor)
result={"kind":"STATIC_DOCUMENT_ORACLE_ONLY","routes_reviewed":len(ids),"routes_executed":0,"oracle_variants":len(cs),"protected_files_checked":len(paths),"errors":errors}
(B/"validation/adapter-check-result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
