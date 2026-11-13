"""Apply accounting design extension once; outputs are review artifacts, not migration."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[3];B=ROOT/'docs/cost'
schema=ROOT/'docs/nen-tang/srs/schema.dbml'
s=schema.read_text(encoding='utf-8')
if 'Table customer_price_terms {' in s:raise SystemExit('Accounting schema already added; edit artifacts directly.')
s=s.replace('Phiên bản 0.3.0','Phiên bản 0.4.0',1).replace('erd.md v0.3.0','erd.md v0.4.0',1)
s=s.replace("  price_vnd bigint [not null, note: 'Trên 1 buy_unit. Có gồm VAT đầu vào không: điểm mở O-01']", """  price_vnd bigint [not null, note: 'Gia cost cuoi cung gom VAT phai tra / buy_unit; server tinh. Legacy chua xac minh khong tu cong VAT']
  quoted_unit_price decimal(18,6) [note: 'Gia bao goc; null voi legacy, khong suy dien nguoc']
  price_basis varchar(24) [not null, default: 'LEGACY_UNVERIFIED', note: 'INCLUSIVE | EXCLUSIVE | FINAL_CONFIRMED | LEGACY_UNVERIFIED; new write khong nhan legacy']
  vat_rate_pct decimal(9,6) [note: 'Nullable, khong mac dinh0; EXCLUSIVE can rate hoac amount, khong ca hai']
  vat_unit_amount decimal(18,6) [note: 'VAT phai tra / buy_unit, nullable; neu co rate thi server tinh amount']
  pricing_evidence varchar(1000) [note: 'Nguon xac nhan gia cuoi; FINAL_CONFIRMED bat buoc; khong phan loai thue phap ly']
  pricing_verified_at datetime(3) [note: 'Chua xac minh thi null, khong suy ra tu created_at']
  pricing_verified_by bigint [ref: > users.id]
  normalization_version varchar(32) [note: 'Thuat toan chuan hoa gia; null voi legacy']""")
addition="""
// Accounting design CR-COST-2026-001. No SQL migration is implied.
Table customer_price_terms {
  id bigint [pk, increment]
  customer_id bigint [not null, ref: > customers.id]
  meal_type_id bigint [not null, ref: > meal_types.id]
  quoted_unit_price decimal(18,6) [not null]
  sale_price_basis varchar(24) [not null, default: 'UNKNOWN', note: 'INCLUSIVE | EXCLUSIVE | FINAL_CONFIRMED | UNKNOWN']
  vat_rate_pct decimal(9,6) [note: 'Null khac0; invoiceRequested khong quyet dinh rate']
  invoice_requested boolean [note: 'Null=chua hoi; false khong nghia VAT0']
  evidence varchar(1000) [note: 'Thoa thuan va nguon xac nhan']
  effective_from date [not null]
  effective_to date [note: 'Nullable; rang buoc khong chong lan ACTIVE theo customer/meal type can transaction']
  status varchar(24) [not null, default: 'DRAFT', note: 'DRAFT | ACTIVE | CANCELLED; activation gated cho sales policy']
  version int [not null, default: 1]
  created_by bigint [not null, ref: > users.id]
  created_at datetime(3) [not null]
  updated_by bigint [ref: > users.id]
  updated_at datetime(3)
  indexes {
    (customer_id, meal_type_id, effective_from)
  }
}

Table order_pricing_snapshots {
  id bigint [pk, increment]
  order_id bigint [not null, ref: > orders.id]
  order_version int [not null]
  price_term_id bigint [ref: > customer_price_terms.id]
  quoted_unit_price decimal(18,6) [not null]
  sale_price_basis varchar(24) [not null]
  vat_rate_pct decimal(9,6)
  invoice_requested boolean
  servings int [not null]
  gross_amount_due decimal(18,6) [note: 'Khong tru khoan chiet khau rieng; null neu UNKNOWN']
  revenue_ex_vat decimal(18,6) [note: 'Null neu chua du VAT/context; khong lay gross neu invoice=false']
  context_status varchar(24) [not null, note: 'RESOLVED | UNRESOLVED | LEGACY_UNVERIFIED']
  captured_at datetime(3) [not null]
  captured_by bigint [not null, ref: > users.id]
  inputs_snapshot json [not null, note: 'Bat bien; quyen doc rieng, khong serialize cho agent khach']
  indexes {
    (order_id, order_version) [unique]
  }
}

Table order_discount_records {
  id bigint [pk, increment]
  order_id bigint [not null, ref: > orders.id]
  pricing_snapshot_id bigint [not null, ref: > order_pricing_snapshots.id]
  proposal_key varchar(64) [not null, note: 'Khong phai key TTL; unique proposal trong order']
  calculation_type varchar(24) [not null, note: 'PERCENT | FIXED_PER_SERVING']
  rate_pct decimal(9,6) [note: 'Chi PERCENT; base chua chot thi draft only']
  amount_per_serving decimal(18,6) [note: 'Chi FIXED_PER_SERVING; rounding CK-Q03']
  percent_basis varchar(24) [not null, default: 'UNRESOLVED', note: 'GROSS | NET | UNRESOLVED; ghi gia dinh draft khong dong CK-Q01']
  eligible_servings int [note: 'CK-Q02; khong lay qty dish lines thay so suat']
  quantity_basis varchar(24) [not null, default: 'UNRESOLVED', note: 'ORDERED | DELIVERED | CONFIRMED | UNRESOLVED']
  base_amount decimal(18,6) [note: 'Server-derived, null neu chua xac dinh']
  calculated_amount decimal(18,6) [note: 'So tinh thu, khong phai paid amount; null neu thieu base']
  status varchar(24) [not null, default: 'DRAFT', note: 'DRAFT | NEEDS_REVIEW | CONFIRMED | CANCELLED; confirm/cancel da xu ly gated CK-Q04-09']
  calculation_snapshot json [not null, note: 'Gia dinh, gates, ruleVersion; khong ghi len amountDue cua order']
  version int [not null, default: 1]
  created_by bigint [not null, ref: > users.id]
  created_at datetime(3) [not null]
  updated_by bigint [ref: > users.id]
  updated_at datetime(3)
  indexes {
    (order_id, proposal_key) [unique]
    (order_id, status)
  }
}

Table order_discount_events {
  id bigint [pk, increment]
  discount_id bigint [not null, ref: > order_discount_records.id]
  event_key varchar(64) [not null, note: 'Event replay chi ghi mot lan']
  event_type varchar(32) [not null, note: 'DRAFT_CREATED | DRAFT_UPDATED | ORDER_CHANGED | REVIEW_REQUESTED; khong settlement event']
  actor_id bigint [ref: > users.id, note: 'Nullable cho worker; event phai co actor hoac system source']
  source varchar(32) [not null]
  payload json [not null, note: 'Before/after va reason, version; khong luu token']
  created_at datetime(3) [not null]
  indexes {
    (discount_id, event_key) [unique]
  }
}

TableGroup accounting_extension {
  customer_price_terms
  order_pricing_snapshots
  order_discount_records
  order_discount_events
}
"""
s+='\n'+addition
schema.write_text(s,encoding='utf-8')
erd=ROOT/'docs/nen-tang/srs/erd.md';e=erd.read_text(encoding='utf-8').replace('| Phiên bản | 0.3.0 |','| Phiên bản | 0.4.0 |').replace('| 0.3.0 | 2026','| 0.4.0 | 2026-11-11 | BA | Thêm4 bảng thiết kế kế toán và metadata giá mua; giữ thao tác phụ thuộc CK ở trạng thái gated; chưa migration. |\n| 0.3.0 | 2026',1)
e+='''
## Bổ sung mô hình kế toán (CR-COST-2026-001)

Thiết kế nháp được đồng bộ vào DBML v0.4.0; **không phải migration đã chạy**. Tổng61 bảng,15 bảng Cost hiện có và4 bảng mở rộng kế toán liên kết CUS/ORD. [Hợp đồng](../../cost/api/accounting-contract.md), [backlog](../../cost/userstories/accounting-backlog.md), [nhánh mở](../../cost/review/cost-branch-decisions.md).

```mermaid
erDiagram
  customers ||--o{ customer_price_terms : agrees
  meal_types ||--o{ customer_price_terms : prices
  orders ||--o{ order_pricing_snapshots : captures
  customer_price_terms o|--o{ order_pricing_snapshots : sources
  orders ||--o{ order_discount_records : tracks_separately
  order_pricing_snapshots ||--o{ order_discount_records : bases
  order_discount_records ||--o{ order_discount_events : audits
```

Orders hiện là một loại suất mỗi điểm/ngày/ca; order_dish_lines là lựa chọn món, không phải dòng hóa đơn tính tiền. Chiết khấu dựa trên số suất và snapshot của order, không tự mở rộng sang đơn nhiều loại suất.

### Ràng buộc áp dụng trong transaction/service

- Giá mới bắt buộc basis được xác minh; legacy giữ nguyên price_vnd và null metadata, không tự cộng VAT hoặc sửa snapshot. Thiếu VAT ở EXCLUSIVE không tạo giá; kết quả không nguyên đồng bị chặn chờ rounding, không làm tròn ngầm.
- PERCENT chỉ có rate_pct; FIXED_PER_SERVING chỉ có amount_per_serving; số không âm, qty nguyên không âm. Tỷ lệ vượt100 và khoản vượt base không cho xác nhận trước khi chốt mức trần; chỉ lưu giả định draft nếu hợp đồng cho phép.
- pricing_snapshot.order_id phải bằng discount.order_id; kiểm bằng transaction hoặc composite FK bổ sung trong migration. Không tin customer/scope client; đọc từ order→service_point→customer.
- Bản chụp bất biến; (order,order_version) duy nhất. Khi order đổi, thêm snapshot; khoản liên quan NEEDS_REVIEW và audit một lần theo event_key. Không tự sửa số phải trả hoặc settlement.
- Một order có nhiều draft không đồng nghĩa nhiều chương trình được cộng dồn. CONFIRMED/CANCELLED dành cho thiết kế tương lai; không mở API quyết định/chi trả trước CK-Q04–Q10. Không có cột paid mặc định0 để nhầm với đã đối soát.
- Quyền đọc/ghi extension chưa được cấp theo vai trò mặc định. Agent phía khách không đọc bảng giá, snapshot kế toán hoặc chiết khấu. Grant DB và allowlist serializer phải review cùng NFR-COST-006.
- customer_price_terms ACTIVE không chồng khoảng hiệu lực cho cùng khách/loại suất; effective_to>=effective_from. Cách duyệt activation còn mở; API đợt này chỉ draft.

### Từ điển dữ liệu bổ sung
'''
blocks=[('ingredient_prices: cột bổ sung',s.split('Table ingredient_prices {',1)[1].split('\n}',1)[0])]+re.findall(r'Table (\w+) \{([\s\S]*?)\n\}',addition)
for name,body in blocks:
    e+=f'\n#### `{name}`\n\n| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |\n| :--- | :--- | :--- | :--- | :--- |\n'
    for line in body.splitlines():
        m=re.match(r'  (\w+) ([\w(),]+)(?: \[(.*)\])?$',line)
        if not m:continue
        field,typ,attrs=m.groups();attrs=attrs or ''
        if name.startswith('ingredient_prices') and field not in ['price_vnd','quoted_unit_price','price_basis','vat_rate_pct','vat_unit_amount','pricing_evidence','pricing_verified_at','pricing_verified_by','normalization_version']:continue
        note=re.search(r"note: '([^']*)'",attrs);desc=note.group(1).replace('|','/') if note else field
        constraints=re.sub(r",? ?note: '[^']*'",'',attrs)
        e+=f"| {field} | {typ} | {'Không' if 'not null' in attrs or 'pk' in attrs else 'Có'} | {constraints or 'Không áp dụng'} | {desc} |\n"
erd.write_text(e,encoding='utf-8')

catalog=B/'api/endpoint-catalog.json';a=json.loads(catalog.read_text(encoding='utf-8'));a['version']='0.2.0';a['accountingExtension']='accounting-contract.md';a['types']['PriceInput']='ingredientId:Id!, supplierId:Id!, kitchenId:Id|null!, quotedUnitPrice:Decimal!, priceBasis:INCLUSIVE|EXCLUSIVE|FINAL_CONFIRMED!, vatRatePct:Decimal? hoặc vatUnitAmount:Decimal? (EXCLUSIVE đúng một), pricingEvidence:string(1..1000)!, effectiveFrom:Date!, isReference:boolean!, sourceFileId:Id?, confirmationToken:string?; không nhận priceVnd từ client, server chuẩn hóa; kết quả phải nguyên đồng theo baseline, phần lẻ gate rounding'
a['types']['Price']+='; quotedUnitPrice:Decimal|null, priceBasis:INCLUSIVE|EXCLUSIVE|FINAL_CONFIRMED|LEGACY_UNVERIFIED, vatRatePct:Decimal|null, vatUnitAmount:Decimal|null, pricingEvidence:string|null, pricingVerifiedAt:Timestamp|null, normalizationVersion:string|null; priceVnd=giá cost cuối gồm VAT phải trả'
for ep in a['endpoints']:
    if ep['id'] in ['API-COST-005','API-COST-006','API-COST-007','API-COST-012','API-COST-013','API-COST-014']:
        ep['rule']+=' Chuẩn hóa theo accounting-contract.md trước kiểm lệch/lưu; import/lưới chung PriceInput v0.2; lỗi một dòng không ghi cả lô.'
catalog.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Schema61 tables, accounting dictionaries and PriceInput catalog v0.2.0 updated')
