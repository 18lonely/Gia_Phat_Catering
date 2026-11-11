# Hợp đồng API — Epic E3 Cost

Phiên bản 0.2.0 · 11/11/2026 · Draft thiết kế, chưa triển khai backend.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | BA | Đồng bộ PriceInput chuẩn hóaVAT, liên kết8 giao tiếp kế toán và mô hình4 bảng mới; vẫn Draft/gated. |
| 0.1.1 | 2026-11-11 | BA | Đánh dấu tác động giá/VAT và chiết khấu riêng theo CR;37 endpoint cũ chưa bao phủ mở rộng kế toán. |
| 0.1.0 | 2026-11-11 | BA | Danh mục REST, hợp đồng dữ liệu, quyền, lỗi, retry, hook MENU và sự kiện nền; giữ các điểm mở |

## 1. Phạm vi và trạng thái quyết định

Nguồn: [SRS Cost](../srs/spec.md), [use case](../srs/usecase-diagram.md), [user flow](../ui/user-flow.md), [SRS nền tảng](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md). URL, tên JSON, cấu trúc kết quả và mã lỗi mới bên dưới là **đề xuất kỹ thuật để review**, không phải API đang chạy. Tài liệu không tự chốt VAT, công thức, quyền hoặc hành vi đang mở.

Dùng `/v1` theo SRS nền tảng; không thêm `/api` chỉ vì template dùng `/api/v1`. Lỗi kế thừa khuôn phẳng của dự án, không bọc bằng khuôn lỗi khác của template. Danh mục endpoint có cột điểm mở: chưa mở endpoint/nhánh đó cho production trước khi quyết định tương ứng được chốt. Không thêm API duyệt ngoại lệ vượt ngưỡng hoặc chặn chuyển bếp.

## 2. Quy ước giao tiếp

| Thành phần | Hợp đồng |
| :--- | :--- |
| Header | Authorization: Bearer accessToken; Accept: application/json; Content-Type: application/json với JSON; X-Request-Id (server cấp nếu thiếu, echo); lệnh tạo có Idempotency-Key |
| Success | `{success:true,data:...,error:null,meta:null,timestamp:ISO8601}`; danh sách dùng meta `{page,pageSize,total}`. Status GET/PATCH/tính thử 200; tạo tài nguyên 201. Endpoint tuần chưa chốt semantics không có success contract cuối cùng |
| Error | `{code,message,details:[{path,rowKey?,reason}],requestId}`. Không stack trace/SQL; message/details lọc theo quyền như success |
| Id | `Id` là chuỗi chữ số nguyên dương, không dùng JS number cho BIGINT; id từ path cũng kiểm quyền/scope |
| Số tiền | `IntegerMoney` là chuỗi số nguyên đồng; `Decimal` là chuỗi thập phân chính xác. Giá>0; khoản khoán≥0; delta cho phép dấu âm. Không NaN/Infinity; backend dùng decimal, không float |
| Ngày/giờ | Date YYYY-MM-DD theo Asia/Ho_Chi_Minh; Timestamp ISO8601 UTC. Ngày kiểm hồi tố lấy server, không tin đồng hồ browser |
| Query | page≥1, pageSize 1..100, mặc định20; sai trả ERR-SYS-422-03. Mọi filter phải được validate, không tự bỏ filter sai |
| Null / thiếu | `!` trong bảng kiểu là bắt buộc; `?` là tuỳ chọn. kitchenId:null ở giá = chung; kitchenId của bản tính/dự toán bắt buộc là một cơ sở cụ thể. PATCH thiếu trường = giữ, null chỉ hợp lệ với trường nullable |
| Validate | Từ chối field lạ trong lệnh ghi, enum sai, path/body ID không khớp. Không nhận createdBy/approvedBy/tổng tiền do client tự cấp |
| Đồng thời | PATCH nhận version theo SRS. Lệnh quyết định/huỷ/đóng nhận version đề xuất; khoá trạng thái trong transaction; cùng người không được tự duyệt |
| Phân quyền | Thiếu quyền 403 ERR-AUTH-403-02; ngoài phạm vi hoặc không tồn tại 404 ERR-SYS-404-01; lấy phạm vi từ token/DB, không chỉ filter client |
| Cache | Phản hồi cost/giá/tệp dùng Cache-Control: private, no-store; không cache công khai; log của budget-check không có con số cost |

### Chống gửi lặp và đối soát — kế thừa và đề xuất cho FLOW-COST-Q02

SRS nền tảng **đã chốt cơ chế thiết kế**: lệnh tạo có `Idempotency-Key`, trong 24 giờ cùng khoá trả kết quả cũ. Phần cần cụ thể hoá: dùng scope `(actorId,method,canonicalPath,key)` và hash body chuẩn hoá; lưu khoá và kết quả commit nguyên tử với nghiệp vụ (đề xuất cần Tech lead review).

1. Cùng scope/key/hash, đã commit: trả status/result gốc theo **quyền hiện tại**; không tạo bản thứ hai. Nếu đã mất quyền thì 403/404, không replay dữ liệu cũ.
2. Cùng scope/key nhưng body khác: 409 `ERR-COST-409-04` đề xuất, không ghi. Còn xử lý: 409 `ERR-COST-409-05`, Retry-After; client đối soát thay vì tạo key mới.
3. Validation thất bại trước ghi không tạo nghiệp vụ; client sửa payload dùng key mới. Lỗi/mất phản hồi không rõ kết quả phải đối soát GET requests/key; 404 quá24h không chứng minh chưa ghi, cần đối chiếu lịch sử nghiệp vụ.
4. Đề xuất mở rộng key cho các POST quyết định/huỷ/đóng. Các POST chỉ tính không ghi giá không cần key nghiệp vụ; budget-check vẫn tính quota theo lời gọi thực, không dùng replay để vượt quota.
5. Sổ request/idempotency chưa có bảng trong ERD hiện tại; cần migration hoặc kho bền vững bảo đảm nguyên tử. Không chỉ dùng Redis TTL rồi cho rằng chống trùng đã hoàn chỉnh.

## 3. Danh mục endpoint

Path `{id}` có kiểu Id; quyền ghi không tự suy ra quyền đọc mọi trường. Dấu `—` ở điểm mở chỉ nghĩa không có câu hỏi bổ sung cho cấu trúc endpoint, không nghĩa toàn bộ nghiệp vụ đã duyệt.

### API-COST-001 — Liệt kê NCC

- **HTTP:** `GET /v1/cost/suppliers`.
- **Quyền:** cost.supplier.read.
- **Request:** Query: page,pageSize,q?,supplierType?,status?.
- **Response:** Page<Supplier> (khuôn mục 2, trừ binary).
- **Hành vi:** Lọc tên/loại/trạng thái; phân trang nền tảng.
- **Truy vết:** `FR-COST-SUP-003`; UC-COST hậu tố 001; màn Cost 01.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-002 — Tạo NCC

- **HTTP:** `POST /v1/cost/suppliers`.
- **Quyền:** cost.supplier.write.
- **Request:** SupplierInput.
- **Response:** Supplier (khuôn mục 2, trừ binary).
- **Hành vi:** 201; chuẩn hoá tên, trùng trả ERR-COST-409-01; ACTIVE; audit.
- **Truy vết:** `FR-COST-SUP-001`; UC-COST hậu tố 001; màn Cost 02.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-003 — Sửa hoặc ngừng NCC

- **HTTP:** `PATCH /v1/cost/suppliers/{id}`.
- **Quyền:** cost.supplier.write.
- **Request:** SupplierPatch.
- **Response:** Supplier (khuôn mục 2, trừ binary).
- **Hành vi:** 200; version bắt buộc; INACTIVE cần lý do, không huỷ giá; NCC ngừng và còn giá tham chiếu phải sinh cảnh báo.
- **Truy vết:** `FR-COST-SUP-001`, `FR-COST-SUP-002`; UC-COST hậu tố 001; màn Cost 02.
- **Điểm mở:** FLOW-COST-Q03: cách lưu cảnh báo nguyên liệu.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-004 — Bảng giá và lịch sử

- **HTTP:** `GET /v1/cost/prices`.
- **Quyền:** cost.price.read.
- **Request:** Query: page,pageSize,ingredientId?,supplierId?,kitchenId?,effectiveFrom?,effectiveTo?,referenceOnly?.
- **Response:** Page<Price> (khuôn mục 2, trừ binary).
- **Hành vi:** kitchenId=GLOBAL chỉ giá chung; bỏ filter là danh sách trong quyền, không có nghĩa GLOBAL.
- **Truy vết:** `FR-COST-PRC-006`; UC-COST hậu tố 002,005; màn Cost 03,07.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-005 — Nhập một giá

- **HTTP:** `POST /v1/cost/prices`.
- **Quyền:** cost.price.write.
- **Request:** PriceInput.
- **Response:** Price (khuôn mục 2, trừ binary).
- **Hành vi:** 201; >0 nguyên đồng; ngày trong khoảng; giá lệch cần confirmationToken; không có bước duyệt; một tham chiếu/phạm vi/ngày.
- **Truy vết:** `FR-COST-PRC-001`, `FR-COST-PRC-010`, `FR-COST-PRC-011`; UC-COST hậu tố 002; màn Cost 04.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-006 — Lưu lưới giá

- **HTTP:** `POST /v1/cost/price-batches`.
- **Quyền:** cost.price.write.
- **Request:** PriceBatchInput.
- **Response:** PriceBatchResult (khuôn mục 2, trừ binary).
- **Hành vi:** 201; toàn lô nguyên tử, bỏ dòng không đổi; lỗi phải trả rowKey/path; không lưu một phần.
- **Truy vết:** `FR-COST-PRC-004`, `FR-COST-PRC-010`, `FR-COST-PRC-011`; UC-COST hậu tố 003; màn Cost 03.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-007 — Kiểm giá lệch trước lưu

- **HTTP:** `POST /v1/cost/price-confirmations`.
- **Quyền:** cost.price.write.
- **Request:** PriceBatchInput không có confirmationToken.
- **Response:** PriceConfirmation (khuôn mục 2, trừ binary).
- **Hành vi:** 200; kiểm payload nhưng chưa ghi giá; token đề xuất ràng buộc actor, hash dòng và giá nền, hết hạn 5 phút; giá nền đổi phải xác nhận lại.
- **Truy vết:** `FR-COST-PRC-010`; UC-COST hậu tố 002,003; màn Cost 03,04.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-008 — Chọn tham chiếu

- **HTTP:** `POST /v1/cost/prices/{id}/reference-selections`.
- **Quyền:** cost.price.write.
- **Request:** VersionReason.
- **Response:** Price (khuôn mục 2, trừ binary).
- **Hành vi:** 201; khoá nhóm giá, bỏ cờ cũ/đặt cờ mới cùng giao dịch; không sửa tiền.
- **Truy vết:** `FR-COST-PRC-002`; UC-COST hậu tố 002; màn Cost 04.
- **Điểm mở:** E3-Q14: giá đã hiệu lực chưa chốt quyền đổi cờ.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-009 — Huỷ giá tương lai

- **HTTP:** `POST /v1/cost/prices/{id}/cancellations`.
- **Quyền:** cost.price.write.
- **Request:** VersionReason.
- **Response:** Price (khuôn mục 2, trừ binary).
- **Hành vi:** 201; không DELETE; giá đã hiệu lực trả ERR-COST-409-03; giữ lịch sử.
- **Truy vết:** `FR-COST-PRC-007`; UC-COST hậu tố 002; màn Cost 04.
- **Điểm mở:** FLOW-COST-Q01 nếu huỷ dòng tham chiếu còn báo giá khác.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-010 — Tra giá theo ngày/cơ sở

- **HTTP:** `GET /v1/cost/reference-prices`.
- **Quyền:** cost.price.read.
- **Request:** Query bắt buộc: ingredientId,kitchenId,date.
- **Response:** Price (khuôn mục 2, trừ binary).
- **Hành vi:** Ưu tiên giá riêng có ngày mới nhất ≤ date, rồi mới fallback GLOBAL; không có trả ERR-COST-404-02.
- **Truy vết:** `FR-COST-PRC-003`; UC-COST hậu tố 002,006; màn Cost 07,08.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-011 — Theo dõi thiếu/cũ

- **HTTP:** `GET /v1/cost/price-health`.
- **Quyền:** cost.price.read.
- **Request:** Query: page,pageSize,kitchenId,kind=MISSING|STALE.
- **Response:** Page<PriceHealth> (khuôn mục 2, trừ binary).
- **Hành vi:** Chỉ nguyên liệu trong công thức ACTIVE, dùng hôm nay nghiệp vụ; API đọc không tự tạo cảnh báo; worker riêng.
- **Truy vết:** `FR-COST-PRC-008`, `FR-COST-PRC-009`; UC-COST hậu tố 005; màn Cost 06.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-012 — Tải mẫu XLSX

- **HTTP:** `GET /v1/cost/price-import-template`.
- **Quyền:** cost.price.write.
- **Request:** Không body.
- **Response:** Tệp XLSX (khuôn mục 2, trừ binary).
- **Hành vi:** 200 binary application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; mẫu giá nhập, không phải mẫu giá bán.
- **Truy vết:** `FR-COST-PRC-005`; UC-COST hậu tố 004; màn Cost 05.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-013 — Kiểm file nhập

- **HTTP:** `POST /v1/cost/price-import-validations`.
- **Quyền:** cost.price.write.
- **Request:** multipart/form-data: file XLSX.
- **Response:** ImportValidation (khuôn mục 2, trừ binary).
- **Hành vi:** 201 bản kiểm tạm; ≤2.000 dòng; chưa ghi giá; lỗi 422 ERR-MENU-422-20, 413/415 theo khung MENU; không dùng upload chứng từ SYS để từ chối XLSX hợp lệ.
- **Truy vết:** `FR-COST-PRC-005`; UC-COST hậu tố 004; màn Cost 05.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-014 — Thực hiện nhập

- **HTTP:** `POST /v1/cost/price-imports`.
- **Quyền:** cost.price.write.
- **Request:** ImportCommit.
- **Response:** ImportResult (khuôn mục 2, trừ binary).
- **Hành vi:** 201; kiểm lại dữ liệu và hash bản kiểm; hết lỗi mới ghi cả lô. Giá nhập không vào PENDING như giá bán E2.
- **Truy vết:** `FR-COST-PRC-005`; UC-COST hậu tố 004; màn Cost 05.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-015 — Tính/phân rã món

- **HTTP:** `POST /v1/cost/dish-calculations`.
- **Quyền:** cost.cost.read; chi tiết giá yêu cầu cost.price.read.
- **Request:** DishQuery.
- **Response:** DishCost (khuôn mục 2, trừ binary).
- **Hành vi:** 200; chỉ tính, không lưu; thiếu giá ERR-COST-422-03; dùng cỡ/ngày/cơ sở; API danh mục MENU gọi nội bộ cho cột cost, không N+1 bắt buộc phía client.
- **Truy vết:** `FR-COST-DISH-001`, `FR-COST-DISH-002`, `FR-COST-DISH-003`, `FR-COST-DISH-004`; UC-COST hậu tố 006; màn Cost 08.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-016 — So sánh công thức P1

- **HTTP:** `POST /v1/cost/recipe-comparisons`.
- **Quyền:** cost.cost.read; chi tiết giá yêu cầu cost.price.read.
- **Request:** RecipeComparisonInput.
- **Response:** RecipeComparison (khuôn mục 2, trừ binary).
- **Hành vi:** 200; cùng ngày/cơ sở; thiếu một bên không trả chênh lệch; chia 0 không tạo Infinity.
- **Truy vết:** `FR-COST-DISH-005`; UC-COST hậu tố 006; màn Cost 08.
- **Điểm mở:** FLOW-COST-Q04: null tỷ lệ là đề xuất.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-017 — Gợi ý nhóm cost P1

- **HTTP:** `POST /v1/cost/dish-tier-suggestions`.
- **Quyền:** cost.cost.read.
- **Request:** DishQuery.
- **Response:** TierSuggestion (khuôn mục 2, trừ binary).
- **Hành vi:** 200 chỉ gợi ý, không sửa món.
- **Truy vết:** `FR-COST-DISH-008`; UC-COST hậu tố 006; màn Cost 08.
- **Điểm mở:** E3-Q7: ngưỡng chưa chốt, có thể trả NOT_CONFIGURED.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-018 — Danh sách bảng tính

- **HTTP:** `GET /v1/cost/sheets`.
- **Quyền:** cost.cost.read hoặc cost.sheet.approve trong phạm vi.
- **Request:** Query: page,pageSize,status?,dishId?,kitchenId?.
- **Response:** Page<SheetSummary> (khuôn mục 2, trừ binary).
- **Hành vi:** Danh sách không tự mở quyền đọc giá; chi tiết theo API kế tiếp.
- **Truy vết:** `FR-COST-DISH-006`, `FR-COST-DISH-007`; UC-COST hậu tố 007; màn Cost 09,10.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-019 — Chi tiết bảng đã chụp

- **HTTP:** `GET /v1/cost/sheets/{id}`.
- **Quyền:** cost.cost.read và cost.price.read cho giá.
- **Request:** Không body.
- **Response:** Sheet (khuôn mục 2, trừ binary).
- **Hành vi:** 200 dữ liệu chụp, không tính lại từ giá mới; scope cả món và cơ sở.
- **Truy vết:** `FR-COST-DISH-006`, `FR-COST-DISH-007`; UC-COST hậu tố 007; màn Cost 09.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-020 — Lập và gửi bảng đặc thù

- **HTTP:** `POST /v1/cost/sheets`.
- **Quyền:** cost.sheet.write.
- **Request:** SheetInput.
- **Response:** Sheet (khuôn mục 2, trừ binary).
- **Hành vi:** 201 PENDING; server tính rồi chụp, không tin total client; không phải đặc thù ERR-COST-422-04.
- **Truy vết:** `FR-COST-DISH-006`; UC-COST hậu tố 007; màn Cost 09.
- **Điểm mở:** E3-Q16 chỉ ảnh hưởng kiểm hiệu lực khi dùng bảng.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-021 — Duyệt/trả lại bảng tính

- **HTTP:** `POST /v1/cost/sheets/{id}/decisions`.
- **Quyền:** cost.sheet.approve.
- **Request:** DecisionInput.
- **Response:** SheetSummary (khuôn mục 2, trừ binary).
- **Hành vi:** 201; khoá trạng thái PENDING; người tạo/sửa không tự duyệt; REJECTED cần lý do; approvals + trạng thái cùng giao dịch.
- **Truy vết:** `FR-COST-DISH-007`; UC-COST hậu tố 007; màn Cost 10.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-022 — Xem khoản khoán

- **HTTP:** `GET /v1/cost/allowances`.
- **Quyền:** Đề xuất: cost.allowance.write hoặc cost.allowance.approve; chưa chốt.
- **Request:** Query: page,pageSize,mealTypeId?,status?,date?.
- **Response:** Page<Allowance> (khuôn mục 2, trừ binary).
- **Hành vi:** Không suy ra quyền quản trị danh mục từ cost.cost.read.
- **Truy vết:** `FR-COST-MEAL-004`; UC-COST hậu tố 008; màn Cost 11.
- **Điểm mở:** FLOW-COST-Q05: quyền đọc.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-023 — Đề nghị khoản khoán

- **HTTP:** `POST /v1/cost/allowances`.
- **Quyền:** cost.allowance.write.
- **Request:** AllowanceInput.
- **Response:** Allowance (khuôn mục 2, trừ binary).
- **Hành vi:** 201 PENDING, thêm phiên bản mới; tiền nguyên ≥0, ngày và lý do bắt buộc; không tự áp dụng.
- **Truy vết:** `FR-COST-MEAL-004`; UC-COST hậu tố 008; màn Cost 11.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-024 — Duyệt khoản khoán

- **HTTP:** `POST /v1/cost/allowances/{id}/decisions`.
- **Quyền:** cost.allowance.approve.
- **Request:** DecisionInput.
- **Response:** Allowance (khuôn mục 2, trừ binary).
- **Hành vi:** 201; không tự duyệt; check duy nhất tên chuẩn hoá/phạm vi/ngày của APPROVED; khoản riêng thắng chung.
- **Truy vết:** `FR-COST-MEAL-004`; UC-COST hậu tố 008; màn Cost 11.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-025 — Kiểm ngân sách nội bộ

- **HTTP:** `POST /v1/cost/menu-calculations`.
- **Quyền:** Quyền MENU xem nội dung; con số chỉ khi cost.cost.read.
- **Request:** MenuQuery.
- **Response:** MenuCost hoặc MenuCostRedacted (khuôn mục 2, trừ binary).
- **Hành vi:** 200 cho nội dung hợp lệ; kết quả theo ngày/cơ sở; clientRevision echo tránh hiển thị kết quả cũ. Thiếu giá/VAT trả 422 nếu không tính được tổng; phần hiển thị từng ngày có status. Không dành cho agent phía khách.
- **Truy vết:** `FR-COST-MEAL-001`, `FR-COST-MEAL-002`, `FR-COST-MEAL-003`, `FR-COST-RUL-001`, `FR-COST-RUL-002`; UC-COST hậu tố 009; màn Cost 12.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-026 — Xem cost lúc duyệt

- **HTTP:** `GET /v1/cost/menu-snapshots`.
- **Quyền:** cost.cost.read.
- **Request:** Query: menuId,kitchenId?,approvalRoundNo?.
- **Response:** List<MenuSnapshot> (khuôn mục 2, trừ binary).
- **Hành vi:** Chỉ bản APPROVED đã ghi bởi hook MENU, không có POST cho client tự tạo snapshot; lọc quyền từng cơ sở.
- **Truy vết:** `FR-COST-MEAL-006`; UC-COST hậu tố 010; màn Cost 12.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-027 — Lập dự toán ngày

- **HTTP:** `POST /v1/cost/estimates`.
- **Quyền:** cost.estimate.write.
- **Request:** EstimateInput.
- **Response:** EstimateFull (khuôn mục 2, trừ binary).
- **Hành vi:** 201; version_no mới theo ngày/cơ sở; server tính số lượng/giá; all-or-nothing một ngày; không ghi đè.
- **Truy vết:** `FR-COST-EST-001`, `FR-COST-EST-002`, `FR-COST-EST-004`, `FR-COST-EST-006`; UC-COST hậu tố 012; màn Cost 14,15.
- **Điểm mở:** E3-Q15 khi main_pick >1.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-028 — Lập tuần

- **HTTP:** `POST /v1/cost/estimate-batches`.
- **Quyền:** cost.estimate.write.
- **Request:** EstimateBatchInput.
- **Response:** EstimateBatch (khuôn mục 2, trừ binary).
- **Hành vi:** Hợp đồng body draft; không cam kết status thành công hay lưu một phần khi Q07 chưa chốt.
- **Truy vết:** `FR-COST-EST-003`; UC-COST hậu tố 012; màn Cost 14.
- **Điểm mở:** FLOW-COST-Q07: transaction/status toàn tuần.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-029 — Lịch sử dự toán

- **HTTP:** `GET /v1/cost/estimates`.
- **Quyền:** cost.estimate.read hoặc cost.estimate.qty.
- **Request:** Query: page,pageSize,menuDayId?,kitchenId?,batchKey?.
- **Response:** Page<EstimateSummary> (khuôn mục 2, trừ binary).
- **Hành vi:** Chỉ metadata cho quyền qty: id, ngày, cơ sở, version, số suất, thời điểm/người lập; không tiền trong summary.
- **Truy vết:** `FR-COST-EST-006`; UC-COST hậu tố 013; màn Cost 15.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-030 — Xem phiên bản

- **HTTP:** `GET /v1/cost/estimates/{id}`.
- **Quyền:** cost.estimate.read hoặc cost.estimate.qty.
- **Request:** Không body.
- **Response:** EstimateFull hoặc EstimateQuantity (khuôn mục 2, trừ binary).
- **Hành vi:** Server chọn projection theo quyền; không nhận includePrices=true để mở quyền; snapshot không đổi.
- **Truy vết:** `FR-COST-EST-004`, `FR-COST-EST-005`; UC-COST hậu tố 013; màn Cost 15.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-031 — Xuất dự toán P1

- **HTTP:** `GET /v1/cost/estimates/{id}/export`.
- **Quyền:** cost.estimate.read hoặc cost.estimate.qty.
- **Request:** Query: format=xlsx|pdf.
- **Response:** Tệp theo quyền (khuôn mục 2, trừ binary).
- **Hành vi:** 200 binary; kiểm lại quyền lúc tải; Cache-Control private,no-store; XLSX không chứa sheet/cột tiền ẩn ở bản qty; xuất không tính lại.
- **Truy vết:** `FR-COST-EST-007`; UC-COST hậu tố 013; màn Cost 15.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-032 — Liệt kê cảnh báo thực đơn

- **HTTP:** `GET /v1/cost/alerts`.
- **Quyền:** cost.alert.read.
- **Request:** Query: page,pageSize,status?,menuId?.
- **Response:** Page<CostAlert> (khuôn mục 2, trừ binary).
- **Hành vi:** Một đầu mục/ngày; cost chỉ theo quyền. Không dùng bảng này cho cảnh báo nguyên liệu thiếu/cũ.
- **Truy vết:** `FR-COST-ALR-002`, `FR-COST-ALR-003`; UC-COST hậu tố 014; màn Cost 16.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-033 — Chi tiết cảnh báo

- **HTTP:** `GET /v1/cost/alerts/{id}`.
- **Quyền:** cost.alert.read; con số cost cần cost.cost.read.
- **Request:** Không body.
- **Response:** CostAlertDetail (khuôn mục 2, trừ binary).
- **Hành vi:** Có snapshot gốc và lần tính lại mới nhất từng cơ sở; không làm thay đổi cảnh báo.
- **Truy vết:** `FR-COST-ALR-002`, `FR-COST-ALR-003`; UC-COST hậu tố 014; màn Cost 17.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-034 — Đóng tay cảnh báo

- **HTTP:** `POST /v1/cost/alerts/{id}/closures`.
- **Quyền:** cost.alert.read theo SRS hiện hành.
- **Request:** VersionReason.
- **Response:** CostAlert (khuôn mục 2, trừ binary).
- **Hành vi:** 201; OPEN→CLOSED, audit lý do ≥10 ký tự; không thay cost thành DAT, không cho quyền sửa MENU.
- **Truy vết:** `FR-COST-ALR-003`; UC-COST hậu tố 014; màn Cost 17.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-035 — Mô phỏng giá P2

- **HTTP:** `POST /v1/cost/price-simulations`.
- **Quyền:** Đề xuất: cost.price.read + cost.cost.read.
- **Request:** SimulationInput.
- **Response:** SimulationResult (khuôn mục 2, trừ binary).
- **Hành vi:** 200 không lưu nghiệp vụ; giá giả định tách bảng thật.
- **Truy vết:** `FR-COST-ALR-005`; UC-COST hậu tố 016; màn Cost 18.
- **Điểm mở:** FLOW-COST-Q10: quyền/phạm vi ngày và trạng thái.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-036 — Dịch vụ ngân sách agent

- **HTTP:** `POST /v1/cost/budget-checks`.
- **Quyền:** Chỉ svc-agent-dinh-duong-vien; allowlist công cụ.
- **Request:** BudgetInput.
- **Response:** BudgetResult (khuôn mục 2, trừ binary).
- **Hành vi:** 200 đúng một trạng thái; không con số/ngày lỗi; ≤30 lời gọi/phiên do server xác thực, không tin session tự cấp từ client.
- **Truy vết:** `FR-COST-RUL-003`; UC-COST hậu tố 015; màn Cost SVC-COST-01.
- **Điểm mở:** FLOW-COST-Q09 khi vừa vượt vừa thiếu dữ liệu.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

### API-COST-037 — Đối soát lệnh ghi

- **HTTP:** `GET /v1/cost/requests/{key}`.
- **Quyền:** Đúng actor đã gửi; kiểm lại quyền endpoint gốc.
- **Request:** Path key: Idempotency-Key.
- **Response:** RequestStatus (khuôn mục 2, trừ binary).
- **Hành vi:** Đề xuất Q02: trả PENDING/COMPLETED/FAILED và resourceRefs đã lọc quyền; không lộ kết quả actor khác; ngoài cửa sổ lưu trả 404, không chứng minh lệnh chưa chạy.
- **Truy vết:** `FR-COST-PRC-001`, `FR-COST-PRC-004`, `FR-COST-EST-006`; UC-COST hậu tố 002,003,012; màn Cost 03,15.
- **Điểm mở:** —.
- **Lỗi:** áp ma trận mục 6 theo điều kiện; 401/403/404/500/503 chung, lỗi validation đúng miền. Không trả lỗi không có điều kiện tương ứng.

## 4. Hợp đồng kiểu dữ liệu

Ký hiệu `A + field` là mở rộng cấu trúc A. `Page<T>` là success data Array<T> với meta phân trang; `List<T>` không phân trang chỉ dùng tập snapshot nhỏ theo một thực đơn. Các kiểu phản hồi liệt kê trường được phép; field cost không được rò qua JSON mở rộng. Kiểu inputsSnapshot chỉ cho người có quyền cost/giá, nội dung theo ERD5.4.

### SupplierInput

name:string(1..160)!, supplierType:REGULAR|MARKET_VENDOR!, phone:string(≤15)?, note:string(≤1000)?.

### SupplierPatch

version:int≥1!, name?,supplierType?,phone?,note?, status:INACTIVE?,reason:string≥10 nếu đổi trạng thái; không cho sửa id/code.

### Supplier

id:Id, code:string, name:string, supplierType:enum, phone:string|null, note:string|null, status:ACTIVE|INACTIVE, version:int.

### PriceInput

ingredientId:Id!, supplierId:Id!, kitchenId:Id|null!, quotedUnitPrice:Decimal!, priceBasis:INCLUSIVE|EXCLUSIVE|FINAL_CONFIRMED!, vatRatePct:Decimal? hoặc vatUnitAmount:Decimal? (EXCLUSIVE đúng một), pricingEvidence:string(1..1000)!, effectiveFrom:Date!, isReference:boolean!, sourceFileId:Id?, confirmationToken:string?; không nhận priceVnd từ client, server chuẩn hóa; kết quả phải nguyên đồng theo baseline, phần lẻ gate rounding.

### Price

id:Id, ingredientId:Id, supplierId:Id, kitchenId:Id|null, priceVnd:IntegerMoney, effectiveFrom:Date, isReference:boolean, version:int, cancelledAt:Timestamp|null, sourceFileId:Id|null; quotedUnitPrice:Decimal|null, priceBasis:INCLUSIVE|EXCLUSIVE|FINAL_CONFIRMED|LEGACY_UNVERIFIED, vatRatePct:Decimal|null, vatUnitAmount:Decimal|null, pricingEvidence:string|null, pricingVerifiedAt:Timestamp|null, normalizationVersion:string|null; priceVnd=giá cost cuối gồm VAT phải trả.

### PriceBatchInput

rows:Array<{rowKey:string!, ...PriceInput}>!, sourceFileId:Id?, confirmationToken:string?; rowKey duy nhất; body rỗng không tạo giá; giới hạn lô cần kiểm tải, chưa đặt con số mới.

### PriceBatchResult

createdCount:int, skippedCount:int, items:Array<{rowKey:string,price:Price}>, batchId:Id.

### PriceConfirmation

requiresConfirmation:boolean, token:string|null, expiresAt:Timestamp|null, deviations:Array<{rowKey,previousPriceId,oldPriceVnd,newPriceVnd,changePct:Decimal}>; chỉ người có quyền giá.

### VersionReason

version:int≥1!, reason:string(10..500)!.

### PriceHealth

ingredientId:Id, ingredientName:string, kitchenId:Id, kind:MISSING|STALE, affectedDishCount:int, effectiveFrom:Date|null, ageDays:int|null.

### ImportValidation

id:Id, fileHash:string, expiresAt:Timestamp, rowCount:int, validCount:int, errors:Array<{row:int,column:string,code,message}>, confirmation:PriceConfirmation|null; không có error thì mới cho commit.

### ImportCommit

validationId:Id!, fileHash:string!, confirmationToken:string?; không nhận dữ liệu thay thế bản kiểm.

### ImportResult

id:Id, validationId:Id, createdCount:int, priceIds:Array<Id>.

### DishQuery

dishId:Id!, portionCode:string(≤16)!, date:Date!, kitchenId:Id!.

### DishLine

ingredientId:Id, ingredientName:string, isMain:boolean, qty:Decimal, unit:string, pricePerUseUnitVnd:Decimal, amountVnd:Decimal, sharePct:Decimal|null, supplierId:Id, priceEffectiveFrom:Date.

### DishCost

dishId:Id, recipeId:Id, portionCode:string, date:Date, kitchenId:Id, totalCostVnd:Decimal, displayCostVnd:IntegerMoney, lines:Array<DishLine>, calculationVersion:string; không phải bản đã chụp.

### RecipeComparisonInput

currentRecipeId:Id!, proposedRecipeId:Id!, date:Date!, kitchenId:Id!; hai công thức cùng món/cỡ.

### RecipeComparison

current:DishCost, proposed:DishCost, deltaVnd:Decimal, deltaPct:Decimal|null; delta là số có dấu, null nếu mẫu số 0 (đề xuất Q04).

### TierSuggestion

status:READY|NOT_CONFIGURED, suggestedTier:LOW|HIGH|null, sourceRuleVersion:string|null.

### SheetInput

dishId:Id!, portionCode:string!, calculationDate:Date!, kitchenId:Id!, note:string(≤1000)?; không nhận tổng tiền tính sẵn.

### SheetSummary

id:Id, dishId:Id, kitchenId:Id, calculationDate:Date, status:PENDING|APPROVED|REJECTED, createdBy:Id, createdAt:Timestamp, version:int; version là đề xuất API concurrency cần bổ sung schema hoặc token trạng thái.

### Sheet

SheetSummary + snapshot:DishCost, inputsSnapshot:object, decisions:Array<{actorId,decision,reason,at}>; version chỉ thay đổi metadata/trạng thái, nội dung snapshot bất biến.

### DecisionInput

version:int≥1!, decision:APPROVED|REJECTED!, reason:string(10..500)! khi REJECTED; không nhận approverId, lấy từ token.

### AllowanceInput

name:string(1..120)!, amountVnd:IntegerMoney≥0!, mealTypeId:Id|null!, effectiveFrom:Date!, reason:string(10..500)!.

### Allowance

id:Id, name:string, amountVnd:IntegerMoney, mealTypeId:Id|null, effectiveFrom:Date, status:PENDING|APPROVED|REJECTED, createdBy:Id, version:int; yêu cầu concurrency tương tự SheetSummary.

### MenuQuery

clientRevision:string!, kitchenIds:Array<Id>?, một trong menuId:Id hoặc draft:{mealTypeId:Id,weekStart:Date,days:Array<{date,items:Array<{dishId,portionCode,slot}>,defaultDishId:Id|null}>}; cơ sở kiểm phải do server xác định từ phạm vi thực đơn, client không được bỏ cơ sở bất lợi.

### MenuCost

clientRevision:string, status:DAT|KHONG_DAT|KHONG_XAC_DINH, days:Array<{date,kitchenId,completeness:COMPLETE|PARTIAL,status,costPerServingVnd:Decimal|null,revenueExVatVnd:Decimal|null,costPct:Decimal|null,thresholdPct:Decimal,method,mode,lines,allowances,errors}>; tổng status hỗn hợp chờ Q09 nếu dùng cùng bộ tổng hợp.

### MenuCostRedacted

clientRevision:string, days:Array<{date,kitchenId,status,completeness}>; không cost/price/threshold/inputs/detail; dùng ở MENU nội bộ, không phải BudgetResult.

### MenuSnapshot

id:Id, menuDayId:Id, kitchenId:Id, approvalRoundNo:int, serviceDate:Date, costPct:Decimal, thresholdPct:Decimal, costPerServingVnd:Decimal, inputsSnapshot:object, capturedAt:Timestamp; không trường mutable.

### EstimateInput

menuDayId:Id!, kitchenId:Id!, servings:Array<{dishId:Id!,count:int≥0!}>!; không trùng dishId, chỉ món chính của ngày, tổng>0; main_pick lấy từ loại suất; server tính toàn bộ giá và tổng.

### EstimateBatchInput

menuId:Id!, kitchenId:Id!, days:Array<{menuDayId:Id,servings:Array<{dishId,count}>}>!; không trùng ngày, ngày phải thuộc menu; semantics commit chờ Q07.

### EstimateSummary

id:Id, menuDayId:Id, kitchenId:Id, versionNo:int, batchKey:string, servings:int, computedBy:Id, computedAt:Timestamp; không tiền với quyền qty.

### EstimateQuantity

EstimateSummary + lines:Array<{ingredientId,ingredientName,useUnit,buyUnit,totalUseQty:Decimal,buyQty:Decimal,components:Array<{dishName,qtyPerServing:Decimal,servings:int}>}>; allowlist nghiêm ngặt không trả inputsSnapshot hoặc khoản tiền.

### EstimateFull

EstimateQuantity + lines bổ sung supplierName,priceEffectiveFrom,pricePerBuyUnitVnd:IntegerMoney,amountVnd:Decimal; allowances:Array<{name,amountVnd}>,totalCostVnd:Decimal,revenueExVatVnd:Decimal,costPct:Decimal,menuCostPct:Decimal,method:string,thresholdPct:Decimal,inputsSnapshot:object.

### EstimateBatch

batchKey:string, items:Array<EstimateSummary>, totals theo cơ sở; trạng thái/atomicity cần Q07, chưa có ví dụ thành công tuần.

### CostAlert

id:Id, menuDayId:Id, menuId:Id, status:OPEN|CLOSED, openedAt:Timestamp, version:int, closeReason:string|null; không con số trong summary.

### CostAlertDetail

CostAlert + kitchens:Array<{kitchenId,snapshotId,recalculationId,result,originalCostPct:Decimal,currentCostPct:Decimal|null,triggerPrices}>; lọc con số/triggerPrices nếu thiếu quyền giá/cost; không cập nhật snapshot gốc.

### SimulationInput

ingredientId:Id!, kitchenId:Id!, priceVnd:IntegerMoney!, dateFrom:Date!, dateTo:Date!; phạm vi trạng thái/day window chờ Q10.

### SimulationResult

simulation:true, affectedDays:Array<{menuDayId,kitchenId,result,costPct:Decimal|null}>, unknownDays:Array<Id>; chỉ phạm vi được mô phỏng, không ghi bảng thật.

### BudgetInput

conversationToken:string!, menu:{mealTypeId:Id,weekStart:Date,days:Array<{date,items:Array<{dishId,portionCode,slot}>,defaultDishId:Id|null}>}!; server xác thực phiên/quota, loại bỏ mọi trường cost client gửi.

### BudgetResult

result:DAT|KHONG_DAT|KHONG_XAC_DINH; additional fields không cho phép, không nested breakdown.

### RequestStatus

key:string, status:PENDING|COMPLETED|FAILED, originalStatus:int|null, resourceRefs:Array<{type,id}>, errorCode:string|null; không trả cached payload nhạy cảm nếu quyền đã đổi.

### Ví dụ thành công và lỗi

Nhập giá (ngày và giá minh hoạ, không phải dữ liệu Gia Phát):

```json
{"ingredientId":"101","supplierId":"201","kitchenId":"1","quotedUnitPrice":"120000","priceBasis":"INCLUSIVE","pricingEvidence":"Báo giá mẫu đã gồmVAT","effectiveFrom":"2026-11-16","isReference":true}
```

Response 201 (kèm header Location `/v1/cost/prices/301`):

```json
{"success":true,"data":{"id":"301","ingredientId":"101","supplierId":"201","kitchenId":"1","priceVnd":"120000","effectiveFrom":"2026-11-16","isReference":true,"version":1,"cancelledAt":null,"sourceFileId":null,"quotedUnitPrice":"120000","priceBasis":"INCLUSIVE","vatRatePct":null,"vatUnitAmount":null,"pricingEvidence":"Báo giá mẫu đã gồmVAT","pricingVerifiedAt":"2026-11-11T04:00:00Z","normalizationVersion":"gross-v1"},"error":null,"meta":null,"timestamp":"2026-11-11T04:00:00Z"}
```

Lỗi 422 theo ô (lưới không được lưu dòng còn lại):

```json
{"code":"ERR-COST-422-01","message":"Giá nhập phải là số nguyên lớn hơn 0.","details":[{"path":"rows[1].quotedUnitPrice","rowKey":"r2","reason":"positive_quote_required"}],"requestId":"req-demo-1"}
```

Lỗi 400 JSON sai/thiếu field dùng `ERR-COST-400-01` đề xuất; không dùng lỗi 500 cho lỗi input. Lỗi 401 dùng ERR-AUTH-401-02; 404 ngoài scope dùng ERR-SYS-404-01 dù client đoán đúng id. Bộ mã mới ở mục6 phải được review trước code.

BudgetResult success chỉ có `data:{"result":"DAT"}` trong khuôn chung; không gửi danh sách ngày/món/cơ sở hoặc ngưỡng. Metadata chung chỉ timestamp/requestId, không thêm duration/breakdown giúp dò dữ liệu.

## 5. Hợp đồng nội bộ và sự kiện

| Hợp đồng | Gọi bởi | Input/output và ranh giới |
| :--- | :--- | :--- |
| `checkMenuCost` | Hook FR-MENU-APV-006 | menuId, menuVersion, server-resolved kitchens; trả permittedToSubmit, lỗi hoặc cảnh báo đã lọc quyền. Bao phủ FR-COST-MEAL-005; CHAN chặn vượt, CANH_BAO chỉ cảnh báo; thiếu giá/VAT/bảng đặc thù vẫn chặn |
| `captureApprovedCost` | Giao dịch duyệt cuối MENU | menuId, approvalRoundNo, phiên bản đầu vào; ghi snapshot từng ngày/cơ sở cùng chuyển APPROVED. Bao phủ FR-COST-MEAL-006; client không có POST trực tiếp. Giá đổi trong PENDING vẫn cần Q06 |
| Tham số SYS | Màn13 | Tái sử dụng FR-SYS-PRM-001/002, body code,value,scope,effectiveFrom,reason,version. Chưa có URL SYS chuẩn trong dự án nên không tự phát minh endpoint Cost thứ hai. Bao phủ FR-COST-MEAL-008 |
| File SYS | Màn04 | Upload chứng từ theo FR-SYS-FILE-001, trả fileId, rồi tham chiếu PriceInput; không public URL lâu dài. Hợp đồng SYS xác nhận MIME theo nội dung, 10MB |
| `referencePrice.effective` | Giá mới hoặc scheduler tới ngày hiệu lực | eventId,priceId,ingredientId,kitchenId|null,effectiveFrom,occurredAt; không cần mang con số giá trong bus envelope. Worker Cost đọc theo quyền, tính lại FR-COST-ALR-001/002 |
| `priceHealth.daily` | Scheduler SYS | jobDate,runId; tra giá cũ FR-COST-PRC-009, chỉ một cảnh báo mở/nguyên liệu. Kho lưu cảnh báo nguyên liệu chờ Q03 |

Sự kiện nội bộ không phải webhook công khai. **R3 không có webhook/callback từ đối tác**, vì giá do nội bộ nhập. Vì vậy không đặt endpoint nhận webhook hoặc bí mật HMAC không có nhu cầu. Nếu sau này mở tích hợp ngoài, phải bổ sung hợp đồng chữ ký, timestamp, chống replay và quản lý khoá riêng trước khi mở.

Đề xuất outbox ghi cùng transaction giá, worker at-least-once chống trùng eventId/snapshot. Sự kiện giá tương lai lên lịch đến ngày hiệu lực, không tính lại bằng giá chưa hiệu lực. Retry theo FR-SYS-JOB-001: backoff tối đa5 lần, sau đó hàng đợi lỗi, quản trị xem/chạy lại. Tính lại ≤5 phút theo NFR; không ghi đè snapshot và không để kết quả cũ cập nhật cảnh báo mới. Cấu trúc outbox cần triển khai/migration, chưa có trong DBML này.

## 6. Ma trận lỗi và phục hồi

Tái sử dụng 14 mã Cost và mã AUTH/SYS/MENU được định nghĩa trong SRS. Các nhóm áp dụng:

| Điều kiện | HTTP / mã | Phục hồi |
| :--- | :--- | :--- |
| Giá sai, ngày sai, nguồn không còn dùng | 422 ERR-COST-422-01/02 hoặc 404 ERR-COST-404-01 theo SRS | Sửa đúng field, không tự đổi ngày |
| Không có giá tham chiếu | 404 ERR-COST-404-02 khi tra giá; 422 ERR-COST-422-03 khi không tính được | Bổ sung giá, không thay bằng 0 |
| Trùng NCC/giá | 409 ERR-COST-409-01/02 | Đối chiếu bản hiện có |
| Giá đã hiệu lực bị sửa/huỷ | 409 ERR-COST-409-03 | Thêm giá mới đúng chính sách hồi tố |
| Bảng đặc thù/VAT/khoản khoán/số suất sai | 422 ERR-COST-422-04/05/06/08 | Bổ sung đầu vào; không cho CANH_BAO bỏ qua |
| Vượt ngân sách ở cổng CHAN | 422 ERR-COST-422-07 | Sửa thực đơn; lỗi theo quyền, không lộ % cho người thiếu quyền |
| Tự duyệt / thiếu lý do / version cũ | 403 ERR-SYS-403-01 / 422 ERR-SYS-422-01 / 409 ERR-SYS-409-02 | Người khác duyệt, nhập lý do, tải lại |
| XLSX/tệp không hợp lệ | ERR-MENU-422-20 hoặc ERR-SYS-413-01/415-01 theo điều kiện | Hiện lỗi dòng/ô; không lưu một phần |
| Vượt quota budget | 429 ERR-COST-429-01 | Agent dừng gọi, hướng dẫn gửi Gia Phát |

Mã **mới đề xuất trong API**, chưa bổ sung như quyết định nghiệp vụ vào SRS:

| Mã | HTTP | Điều kiện | Hành vi |
| :--- | :--- | :--- | :--- |
| ERR-COST-400-01 | 400 | JSON/schema/enum/required field sai hoặc field lạ | details.path, không ghi |
| ERR-COST-409-04 | 409 | Cùng idempotency key, body khác | Không ghi, dùng key mới sau đối soát |
| ERR-COST-409-05 | 409 | Request key đang xử lý | Retry-After và đối soát cùng key |
| ERR-COST-409-06 | 409 | Thiếu/hết hạn token xác nhận giá lệch hoặc giá nền đổi | Chạy kiểm xác nhận lại, không bỏ qua cảnh báo |
| ERR-COST-409-07 | 409 | Đã quyết định, bản import hết hạn/đổi hash hoặc trạng thái không cho phép | Tải lại trạng thái/bản kiểm, không replay bằng key mới vô điều kiện |
| ERR-COST-409-08 | 409 | Khoản khoán APPROVED trùng tên chuẩn hoá/phạm vi/ngày | Review đề nghị, không ghi hai khoản hiệu lực |

Không dùng các mã này để che giấu nhánh nghiệp vụ chưa chốt; điểm mở là cổng thiết kế, không phải lỗi runtime giả lập đã triển khai.

## 7. Giới hạn hoàn thiện và tác động dữ liệu

- Q02 đã có phương án kỹ thuật cụ thể kế thừa nền tảng; còn review cách lưu bền vững, claim request và schema migration. Không coi toàn bộ câu hỏi là đã được người dùng phê duyệt.
- `version` trên bảng tính/khoản khoán là đề xuất API để xử lý concurrent decisions. ERD hiện chưa có cột này; Tech lead chọn bổ sung cột hoặc opaque revision token tương đương, sau đó đồng bộ DBML. Không giả vờ cột đã tồn tại.
- Q01/Q03/Q05/Q06/Q07/Q08/Q09/Q10 và E3-Q14–16 giữ mở. Endpoint/nhánh phụ thuộc được gắn nhãn, wireframe chỉ cho xem mô phỏng hoặc khoá thao tác cần quyết định.
- Các endpoint chỉ tính không lưu business snapshot nhưng có thể có telemetry đã lọc; budget-check tuyệt đối không log cost. Không gọi FR-COST-ALR-004/MEAL-007 như đã triển khai.
- Chưa có OpenAPI thực thi, controller, migration hoặc test backend. Tài liệu này là hợp đồng review với field/rule/permission cụ thể, không phải bằng chứng có dịch vụ chạy.

## 8. Truy vết toàn bộ FR

| FR | REST / nội bộ | Trạng thái |
| :--- | :--- | :--- |
| `FR-COST-SUP-001` | API-COST-002, API-COST-003 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-SUP-002` | API-COST-003 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-SUP-003` | API-COST-001 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-001` | API-COST-005, API-COST-037 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-002` | API-COST-008 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-003` | API-COST-010 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-004` | API-COST-006, API-COST-037 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-005` | API-COST-012, API-COST-013, API-COST-014 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-006` | API-COST-004 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-007` | API-COST-009 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-008` | API-COST-011 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-009` | API-COST-011, priceHealth.daily worker | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-010` | API-COST-005, API-COST-006, API-COST-007 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-PRC-011` | API-COST-005, API-COST-006 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-001` | API-COST-015 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-002` | API-COST-015 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-003` | API-COST-015 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-004` | API-COST-015 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-005` | API-COST-016 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-006` | API-COST-018, API-COST-019, API-COST-020 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-007` | API-COST-018, API-COST-019, API-COST-021 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-DISH-008` | API-COST-017 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-001` | API-COST-025 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-002` | API-COST-025 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-003` | API-COST-025 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-004` | API-COST-022, API-COST-023, API-COST-024 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-005` | checkMenuCost | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-006` | API-COST-026, captureApprovedCost | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-MEAL-007` | Hoãn, không mở endpoint | E3-Q9/Q10 chưa quyết |
| `FR-COST-MEAL-008` | Tham số SYS FR-SYS-PRM-001/002 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-RUL-001` | API-COST-025 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-RUL-002` | API-COST-025 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-RUL-003` | API-COST-036 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-001` | API-COST-027 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-002` | API-COST-027 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-003` | API-COST-028 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-004` | API-COST-027, API-COST-030 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-005` | API-COST-030 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-006` | API-COST-027, API-COST-029, API-COST-037 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-EST-007` | API-COST-031 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-ALR-001` | referencePrice.effective worker | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-ALR-002` | API-COST-032, API-COST-033 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-ALR-003` | API-COST-032, API-COST-033, API-COST-034 | Nháp, xem điểm mở từng hợp đồng |
| `FR-COST-ALR-004` | Hoãn, không mở endpoint | E3-Q9/Q10 chưa quyết |
| `FR-COST-ALR-005` | API-COST-035 | Nháp, xem điểm mở từng hợp đồng |

## Bổ sung trạng thái hợp đồng kế toán

Catalog37 endpoint đã cập nhật PriceInput v0.2.0: giá báo/basis/VAT bắt buộc trước chuẩn hóa; không nhận priceVnd từ client. [Hợp đồng kế toán](accounting-contract.md) bổ sung8 giao tiếp API-ACC-001–008,6 mã lỗi đề xuất, context khách/đơn và bản nháp khoản riêng. [Catalog extension](accounting-endpoints.json) tách khỏi37 endpoint Cost để không tăng giả độ phủ45 FR gốc.

Schema DBML v0.4.0 đã mô tả4 bảng extension và metadata giá. API vẫn Draft, chưa OpenAPI/controller/migration; quyền mới deny trước review CK-Q04; không có endpoint duyệt/chi trả. Nhánh Cost còn mở theo [phương án thiết kế](../review/cost-branch-decisions.md), không tự coi đã phê duyệt.
