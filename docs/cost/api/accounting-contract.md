# Hợp đồng bổ sung kế toán: v0.2.0

Ngày11/11/2026 · Draft thiết kế, chưa triển khai. Nguồn: [nghiệp vụ đã xác nhận](../accounting/business-rules.md), [CR](../cr/CR-COST-2026-001.md), [DBML v0.4.0](../../nen-tang/srs/schema.dbml).

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Chuẩn hóa PriceInput,8 giao tiếp extension, trạng thái draft và gate CK; đồng bộ dữ liệu/UI/backlog |

## 1. Quy ước và quyền

Dùng headers, success envelope, flat error, Id dạng chuỗi, decimal dạng chuỗi, scope và idempotency24h của [API Cost](api-spec.md). GET/preview200; tạo draft201; PATCH200. Lệnh tạo/PATCH ghi phải có X-Request-Id và Idempotency-Key theo thiết kế; PATCH có version. Thiếu key/schema400; thiếu auth401; thiếu quyền403; ngoài phạm vi404; version cũ409; dữ liệu nghiệp vụ sai422. Không trả stack/SQL hoặc dữ liệu tiền ngoài quyền.

Chuẩn hóa giá dùng `cost.price.write`; người chỉ đọc giá không được lưu. Các quyền mới `accounting.context.read`, `accounting.discount.read`, `accounting.discount.draft`, `accounting.terms.read`, `accounting.terms.draft` là **đề xuất**, chưa cấp cho vai trò nào trước CK-Q04 và quyết định quyền kế toán. Mặc định deny. Bếp/agent phía khách không được nhận phản hồi kế toán chỉ vì có quyền xem đơn. Phạm vi khách suy từ order→service_point→customer; không tin customerId/số phải trả client.

Không có endpoint xác nhận chiết khấu, thanh toán, bù trừ hay hủy khoản đã xử lý trong extension này. Enum trạng thái dự kiến trong schema không đồng nghĩa có quyền chuyển trạng thái. Không có webhook công khai; sự kiện order nội bộ phải được xác thực bởi worker tin cậy và chống lặp eventKey.

## 2. PriceInput v0.2: thay hợp đồng nhập giá cũ

Áp dụng API-COST-005/006/007 và mẫu nhập/kiểm/commit012–014; không phát sinh endpoint tạo giá thứ hai. Không nhận `priceVnd` từ client để tránh ghi giá trướcVAT như giá cuối. Catalog37 endpoint đã đổi sang PriceInput mới; payload cũ chỉ có priceVnd bị400, không tự gán basis. Đây là thay đổi hợp đồng thiết kế, chưa có client production để migration trong workspace.

| Trường | Kiểu / bắt buộc | Quy tắc |
| :--- | :--- | :--- |
| ingredientId / supplierId / kitchenId | Id / Id / Id hoặc null; bắt buộc | Quyền, ACTIVE, null cơ sở=chung như SRS |
| quotedUnitPrice | Decimal>0, tối đa6 số lẻ; bắt buộc | Giá báo trên buy_unit, không tự đổi quy cách thùng/kg |
| priceBasis | INCLUSIVE / EXCLUSIVE / FINAL_CONFIRMED; bắt buộc | UNKNOWN/LEGACY_UNVERIFIED chỉ dùng đọc/migration, không tạo giá mới |
| vatRatePct hoặc vatUnitAmount | Decimal>=0, tối đa6 số lẻ | EXCLUSIVE đúng một trường. Rate giới hạn kỹ thuật0..100 ở thiết kế để review; không chọn thuế suất thay kế toán |
| pricingEvidence | string1..1000; bắt buộc | Nguồn xác nhận cách ghi và giá cuối; không tự coi không hóa đơn=khôngVAT |
| effectiveFrom / isReference | Date / boolean; bắt buộc | Quy tắc ngày/tham chiếu hiện có |
| sourceFileId / confirmationToken | Id / string; tùy chọn | Quyền file, hash token bao gồm cả quote/basis/VAT/evidence |

INCLUSIVE và FINAL_CONFIRMED không nhận VAT điều chỉnh; metadata phân rã thuế không nằm trong lệnh này. EXCLUSIVE có rate: gross=quote×(1+rate/100); có amount: gross=quote+amount. Server tính decimal, không float; không làm tròn trung gian. Để giữ `ingredient_prices.price_vnd` nguyên đồng hiện có, kết quả phần lẻ **không lưu** và trả rounding-unresolved; chưa tự quyết CK-Q03 (chiết khấu) hoặc chính sách rounding giá mua. Không biến UNKNOWN thành0VAT.

Response Price giữ `priceVnd` là gross cuối, kèm quotedUnitPrice,basis,VAT,evidence,verifiedBy/At,normalizationVersion. Lịch sử cũ có LEGACY_UNVERIFIED: đọc giữ giá cũ và gắn cờ; không tự sửa snapshot, không dùng làm nguồn giá mới đã xác minh. Lộ trình xác minh legacy cần kế toán, không backfill bằng suy đoán.

Lưới/import: mẫu thêm quotedUnitPrice,priceBasis,vatRatePct,vatUnitAmount,pricingEvidence; parse theo tên cột; lỗi schema/basis ở bất kỳ dòng nào không commit cả lô. Chỉ khi giá chuẩn hóa xong mới so biến động30%; token có hash input/giá nền/version. Một lần commit giữ cùng normalizationVersion cho cả batch. File cũ thiếu cột bắt buộc trả lỗi import, không âm thầm hiểu gross.

Ví dụ request (VAT8% chỉ thử):

```json
{"ingredientId":"101","supplierId":"201","kitchenId":"1","quotedUnitPrice":"100000","priceBasis":"EXCLUSIVE","vatRatePct":"8","pricingEvidence":"Báo giá mẫu A ghi chưa VAT","effectiveFrom":"2026-11-16","isReference":true}
```

Response data có `priceVnd:"108000"`, `quotedUnitPrice:"100000"`; số70g tính7560đ. Client không gửi người xác minh hoặc gross tự tính để thay server.

## 3. Danh mục extension

| ID | HTTP/path | Quyền đề xuất/hiện có | Request | Response | Ghi dữ liệu |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-ACC-001 | POST /v1/cost/prices/normalizations | cost.price.write | QuoteInput = quote/basis/VAT/evidence của PriceInput | NormalizedQuote | Không |
| API-ACC-002 | GET /v1/orders/{orderId}/accounting-context | accounting.context.read | Path orderId | OrderAccountingContext | Không |
| API-ACC-003 | POST /v1/orders/{orderId}/discount-previews | accounting.discount.draft | DiscountInput | DiscountPreview | Không |
| API-ACC-004 | POST /v1/orders/{orderId}/discount-drafts | accounting.discount.draft | DiscountInput + proposalKey | DiscountDraft | Tạo DRAFT và event nguyên tử |
| API-ACC-005 | PATCH /v1/orders/{orderId}/discount-drafts/{id} | accounting.discount.draft | DiscountInput + version + reason | DiscountDraft | Chỉ DRAFT/NEEDS_REVIEW; không tự xác nhận |
| API-ACC-006 | GET /v1/orders/{orderId}/discount-drafts | accounting.discount.read | page/pageSize theo API chung | Page<DiscountDraft> | Không |
| API-ACC-007 | POST /v1/customers/{customerId}/price-term-drafts | accounting.terms.draft | PriceTermDraftInput | PriceTermDraft | Chỉ DRAFT, không tự kích hoạt |
| API-ACC-008 | GET /v1/customers/{customerId}/price-term-drafts | accounting.terms.read | mealTypeId?,page,pageSize | Page<PriceTermDraft> | Không |

### Kiểu dữ liệu

- **NormalizedQuote:** quotedUnitPrice,basis,vatRatePct|null,vatUnitAmount|null,priceVnd:string nguyên đồng,normalizationVersion. Preview không có id giá, không tạo giá tham chiếu.
- **OrderAccountingContext:** orderId,orderVersion,pricingSnapshotId,mealTypeId,servings,quotedUnitPrice,salePriceBasis,invoiceRequested:boolean|null,vatRatePct|null,amountDue:Decimal|null,revenueExVat:Decimal|null,contextStatus,blockingQuestions[]. Cờ hóa đơn không tham gia công thức VAT. Thiếu context trả UNRESOLVED và số chưa biết=null, không mặc định0.
- **DiscountInput:** orderVersion:int!, pricingSnapshotId:Id!, calculationType:PERCENT/FIXED_PER_SERVING!, ratePct:Decimal? hoặc amountPerServing:Decimal?, eligibleServings:int>=0!, quantityBasis:ORDERED/DELIVERED/CONFIRMED/UNRESOLVED!, percentBasis:GROSS/NET/UNRESOLVED!, note:string<=1000?. PERCENT chỉ rate; FIXED chỉ amount. Đây là giả định draft; CK-Q01/02/03/04 chưa được đóng do nhập enum. Rate0..100 là giới hạn prototype/thiết kế, mức trần nghiệp vụ chưa duyệt. Giá trị âm hoặc nhập hai cách cùng lúc422. server lấy amountDue/base từ snapshot, không nhận orderTotal hoặc calculatedAmount client.
- **DiscountPreview:** orderId,orderVersion,amountDueUnchanged,calculatedAmount:Decimal|null,baseAmount:Decimal|null,calculationAssumptions,blockingQuestions[],canConfirm:false,settlementStatus:"NOT_IN_SCOPE". GROSS dùng gross snapshot; NET cần revenueExVat đã biết; thiếu base vẫn có preview UNRESOLVED, không lấy0. Không làm tròn số tiền draft thành khoản đã chốt.
- **DiscountDraft:** id,proposalKey,status:DRAFT/NEEDS_REVIEW,version + DiscountInput + DiscountPreview + createdBy/At,updatedBy/At. Lưu null calculatedAmount nếu basis unresolved. Unique(orderId,proposalKey); cùng key/body replay không tạo lần hai; cùng proposalKey body khác trả409.
- **PriceTermDraftInput:** mealTypeId:Id!,quotedUnitPrice:Decimal>0!,salePriceBasis:INCLUSIVE/EXCLUSIVE/FINAL_CONFIRMED/UNKNOWN!,vatRatePct:Decimal|null!,invoiceRequested:boolean|null!,effectiveFrom:Date!,effectiveTo:Date?,evidence:string<=1000?. Nullable cho draft chưa đủ thông tin, không kích hoạt. PriceTermDraft thêm id,status:DRAFT,version,createdBy/At. Danh mục customer và mealType phải tồn tại, đúng scope.

Ví dụ preview200 trong success envelope chung:

```json
{"success":true,"data":{"orderId":"701","orderVersion":1,"amountDueUnchanged":"4000000","calculatedAmount":"200000","baseAmount":"4000000","calculationAssumptions":{"calculationType":"PERCENT","ratePct":"5","percentBasis":"GROSS","quantityBasis":"ORDERED","eligibleServings":100},"blockingQuestions":["CK-Q01","CK-Q02","CK-Q03","CK-Q04"],"canConfirm":false,"settlementStatus":"NOT_IN_SCOPE"},"error":null,"meta":null,"timestamp":"2026-11-11T05:00:00Z"}
```

FIXED2000×100 cũng ra200000 nhưng amountDue vẫn4000000. Không có trường netPayable=3800000. Snapshot order/term không đổi do preview hoặc lưu khoản riêng.

## 4. Lỗi và xử lý

| Mã đề xuất | HTTP | Điều kiện | Xử lý |
| :--- | :---: | :--- | :--- |
| ERR-ACC-400-01 | 400 | Thiếu field, field lạ, sai schema, client tự gửi số phải trả hoặc gross | details.path; sửa request, không ghi |
| ERR-ACC-422-01 | 422 | Basis/VAT của giá mua chưa rõ, hai nguồn VAT, giá âm/không hợp lệ | Xác minh báo giá; không coi VAT0 |
| ERR-ACC-422-02 | 422 | Giá gross sau chuẩn hóa không nguyên đồng | Chờ quy tắc rounding giá mua; không tự cắt số |
| ERR-ACC-422-03 | 422 | Giá trị discount/qty/basis không hợp lệ | Sửa field; không sửa tiền đơn |
| ERR-ACC-409-01 | 409 | Order/snapshot/version đã đổi, proposalKey trùng khác payload | Tải lại, đối soát và lưu draft mới đúng version |
| ERR-ACC-409-02 | 409 | Yêu cầu trạng thái vượt gate chính sách | Trả blockingQuestions; không tự cấp quyền duyệt |

Lỗi chung401/403/404/409 version dùng nền tảng. Lỗi500 trước commit không ghi một phần; mất phản hồi sau gửi chưa biết kết quả thì đối soát cùng key, không hứa rollback. Import báo theo dòng/cột và mã lỗi import của MENU, giữ nguyên nguyên nhân ACC trong details nếu có quyền. Mã ACC là bổ sung đề xuất, không giả đã có trong14 lỗi Cost gốc.

## 5. Sự kiện và chuyển dữ liệu

Order change worker ghi NEEDS_REVIEW + event nguyên tử, không tính lại rồi tự chi tiền. pricingSnapshotId phải thuộc đúng order và đúng version. Draft xác nhận bằng tay không có endpoint cho tới CK-Q04. Settlement, bù trừ và reversal CK-Q05–09 chưa có API nên không có callback cần công khai.

Migration cần dry-run số bản ghi legacy, schema nullable trước, kế toán xác minh giá, backfill có log nguồn; không đổi gross cũ/snapshot quá khứ. Kiểm DB grants cho4 bảng mới. DDL sinh từ DBML chỉ là kiểm cú pháp, không được dùng như kế hoạch chuyển dữ liệu đã nghiệm thu.

### Tương thích lỗi và ca baseline

API-COST ghi giá giữ ERR-COST-422-01 cho giá báo không dương và các lỗi Cost về ngày/NCC/trùng. Preview normalization dùng ERR-ACC-422-01 cho đầu vào normalization không hợp lệ; basis/VAT thiếu dùng ACC; gross phần lẻ dùng ERR-ACC-422-02. Giá đầu vào engine trong ca baseline là giá cost cuối, không phải payload PriceInput v0.2. Khi chạy108 ca cũ qua HTTP phải dựng quote/basis/evidence hợp lệ; test giá gross1.5 cần đối chiếu lỗi normalization mới, không cố ép giữ mã lỗi ở lớp khác. 18 ca thiết kế bổ sung đặc tả hành vi mới, chưa có kết quả backend.
