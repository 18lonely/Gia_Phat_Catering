"""Document/fixture checks only; no backend or policy execution."""
from pathlib import Path
import hashlib, json, re
B = Path(__file__).resolve().parents[1]
root = B.parents[1]
errors = []
def need(ok, msg):
    if not ok: errors.append(msg)
def read(p): return p.read_text(encoding="utf-8")
d = json.loads(read(B / "test/fixtures/delta-synthetic.json"))
need(d["synthetic"] is True, "Fixture must be synthetic")
fields = ("dishId", "recipeId", "portionCode", "role", "unit")
def key(line): return tuple(line[f] for f in fields)
before = {key(x): x["qty"] for x in d["baseline"]}
after = {key(x): x["qty"] for x in d["target"]}
delta = {k: after.get(k, 0)-before.get(k, 0) for k in before.keys() | after.keys()}
actual = {k[1]: v for k,v in delta.items() if v}
need(actual == {x["recipeId"]: x["qtyDelta"] for x in d["expectedDelta"]}, "Recipe delta mismatch")
need(sum(before.values()) == sum(after.values()) == 100, "Synthetic total mismatch")
need(len([x for x in d["baseline"] if x["dishId"] == d["ambiguousRequest"]["dishId"]]) == 2, "Ambiguity fixture mismatch")
need(len({key(x) for x in d["mixedUnits"]}) == 2, "Unit/role distinction missing")
inv = read(B / "test/invariant-cases.md")
need(len(re.findall(r"^\| TC-E6-INV-", inv, re.M)) == 12, "INV count")
need(inv.count("| NOT RUN |") == 12, "INV status")
findings = read(B / "review/decision-findings.md")
need(not re.search(r"E6-RV\d", inv), "Noncanonical finding ID")
for code in re.findall(r"E6-RV-\d{2}", inv): need(code in findings, "Unknown finding " + code)
cap = json.loads(read(B / "validation/capability-map.json"))
for code in re.findall(r"FR-[A-Z]+-[A-Z]+-\d+", inv): need(code in {x["fr"] for x in cap}, "Unknown FR " + code)
base = json.loads(read(B / "validation/contract-baseline-sha256.json"))
protected = ["review/questions.md", "review/decision-review.md", "review/handoff.md", "review/independent-handoff.md", "test/decision-review-cases.md", "userstories/acceptance-criteria.md", "html-wireframe/order-workbench.html", "api/endpoint-catalog.json"]
paths = [B / p for p in protected] + [root / p for p in ["docs/nen-tang/srs/schema.dbml", "docs/cost/accounting/business-rules.md", "docs/cost/review/accountant-input.md"]]
for p in paths:
    need(hashlib.sha256(p.read_bytes()).hexdigest() == base[p.relative_to(root).as_posix()], "Protected changed " + p.name)
preview = read(B / "preview.html")
for anchor in ["doc-api-delta-contract-review-md", "doc-test-evidence-protocol-md", "doc-review-contract-handoff-md"]:
    need('id="'+anchor+'"' in preview, "Preview missing " + anchor)
result = {"kind":"DOCUMENT_AND_SYNTHETIC_CHECK_ONLY", "backend_tests_executed":0, "invariant_cases":12, "protected_files_checked":len(paths), "errors":errors}
(B / "validation/contract-check-result.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
