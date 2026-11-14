---
id: DOC-COST-SRS-DATA-DICTIONARY
title: Từ điển dữ liệu E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-dictionary, e3]
author: BA
last_updated: 2026-11-16
---
# Từ điển dữ liệu E3: Cost (COST và mở rộng kế toán)

Draft · 16/11/2026 · Thiết kế đề xuất, chưa migration.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách nguyên văn phần từ điển của E3 ra khỏi ERD theo khuôn chung các epic. Không đổi bảng, cột hay ràng buộc |

Sơ đồ quan hệ vẫn ở [ERD](erd.md); schema chung là [DBML 65 bảng](../../nen-tang/srs/schema.dbml). Các tiêu đề mục giữ số mục cũ của nơi gốc để đối chiếu.

Bảng dùng chung (`users`, `user_roles`, `audit_logs`, `parameters`, `change_requests`, `approvals`, `files`, `notifications`) xem [từ điển dữ liệu E1](../../nen-tang/srs/data-dictionary.md); quy ước kiểu dữ liệu chung xem [ERD tổng mục 1](../../nen-tang/srs/erd.md).

## Phần chuyển từ [ERD tổng](../../nen-tang/srs/erd.md)

### 5.1 `ingredient_prices`: Giá nhập [D-13]

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Nguyên liệu | ingredient_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `ingredients.id` | Không áp dụng | Không áp dụng |
| Nhà cung cấp | supplier_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `suppliers.id` | Không áp dụng | Không áp dụng |
| Cơ sở | kitchen_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `kitchens.id` | Null = áp dụng cả 2 cơ sở | Hai cơ sở có thể mua giá khác nhau |
| Giá nhập | price_vnd | BIGINT | Không áp dụng | Không | Không áp dụng | > 0; trên 1 `buy_unit` | Giá dùng tính cost gồm VAT phải trả NCC theo [ACC-CONF-02](../accounting/business-rules.md); XC-01. O-01 vẫn mở về thành phần cost và VAT bán ra |
| Hiệu lực từ | effective_from | DATE | Không áp dụng | Không | Không áp dụng | Không áp dụng | `BR-COST-004` |
| Là giá dùng tính cost | is_reference | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mỗi (`ingredient_id`, `kitchen_id`, `effective_from`) có đúng 1 dòng TRUE | Khi một nguyên liệu có nhiều nhà cung cấp |
| Chứng từ | source_file_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `files.id` | Không áp dụng | Ảnh chứng từ |

Tất cả bảng thuộc `TableGroup cost` đều bị chặn SELECT với Agent Dinh dưỡng viên (`BR-SEC-010`, `NFR-COST-006`), gồm cả bản chụp và cảnh báo; xem mục 5.4.


### 5.4 Bổ sung mô hình COST v0.3.0

**Thiết kế đề xuất, chưa phải migration đã chạy.** Dùng chung [schema DBML](../../nen-tang/srs/schema.dbml). Phần dưới thay thế các mô tả cost cũ nếu có khác biệt; các điểm mở O-01, E3-Q1 → Q13, E2-Q1, DL-01 vẫn mở.

#### Ràng buộc và tính nhất quán

1. Bỏ `menu_days.cost_pct`; tra bản chụp theo ngày, cơ sở và vòng duyệt. Duyệt lại tạo vòng mới. Chỉ khi người duyệt cuối hoàn tất mới ghi bản chụp cùng giao dịch với `menus.APPROVED`. Với mỗi cơ sở cần kiểm phải có bản chụp; thiếu giá/VAT thì chưa đủ điều kiện duyệt, không thay bằng cost 0.
2. Các bảng snapshot, sheet lines, recalculation và dự toán là bất biến sau khi lưu. Chỉ trạng thái duyệt bảng tính, trạng thái khoản khoán và vòng đời cảnh báo được cập nhật, có audit. Bản trả lại được lập mới. Không cascade delete dữ liệu đã chụp.
3. Giá và khoản khoán cùng phạm vi phải được xử lý bằng giao dịch. MySQL unique có cột NULL **không** chặn trùng giá chung: migration phải dùng khoá scope sinh `COALESCE(kitchen_id,0)` cho giá và `COALESCE(meal_type_id,0)` cho khoản khoán (ID hợp lệ > 0). Với giá, unique `(ingredient_id,supplier_id,scope,effective_from)`; thêm khoá tham chiếu có điều kiện cho dòng chưa huỷ, `is_reference=true`. Khoá hàng nguyên liệu trước đổi tham chiếu; bảo đảm đúng một dòng tham chiếu khi nhóm còn giá. Không thay số tiền/ngày của giá đã hiệu lực. SRS chưa rõ có được đổi cờ tham chiếu của giá đã hiệu lực hay không: ghi nhận tại mục 4.5 SRS Cost; không tự cấp quyền này.
4. Khoản khoán: unique có điều kiện `(tên chuẩn hoá,scope,effective_from)` cho dòng APPROVED. Chọn bản APPROVED có ngày hiệu lực lớn nhất ≤ ngày tính cho mỗi tên/phạm vi; khoản riêng loại suất thắng khoản chung cùng tên. Giá trị, tên, phạm vi và ngày của bản APPROVED không sửa đè.
5. `cost_alerts` có đúng tối đa một OPEN cho mỗi `menu_day_id` (thực đơn đã suy ra qua FK). Migration dùng unique trên generated key `CASE WHEN status='OPEN' THEN menu_day_id ELSE NULL END`. Một đầu mục chứa các cơ sở tại `cost_alert_kitchens`; không tạo hai cảnh báo cùng ngày khi cả hai cơ sở vượt. Đóng do giá phục hồi chỉ khi mọi cơ sở liên quan tính được và đạt; kết quả không xác định không được coi là đã phục hồi. Chi tiết phải trỏ đến snapshot/recalculation cùng ngày và cùng cơ sở. Giữ lịch sử tính lại; worker xử lý có thứ tự theo ngày để kết quả cũ không ghi đè liên kết mới.
6. Khi giá đổi, tạo `cost_recalculations` theo sự kiện, unique `(snapshot_id,event_key)` chống retry trùng. Chỉ tính các ngày từ hôm nay thuộc thực đơn APPROVED/PUBLISHED theo FR-COST-ALR-001; dùng vòng duyệt hiện hành. Chi tiết nguyên liệu/giá gây thay đổi lưu trong JSON. Phân quyền chặn đọc toàn bộ TableGroup cost với agent phía khách; thông báo và bảng kiểm cũng phải lọc trường nhạy cảm ở API.
7. Dự toán có `version_no` tăng trong phạm vi (ngày,cơ sở); cấp số dưới khoá giao dịch. `batch_key` gắn các bản của một lần lập tuần; gộp tuần đúng batch/cơ sở, giữ phân rã ngày và giá từng ngày, không lấy một giá tuỳ ý nhân cả tuần. Một dòng nguyên liệu/ngày chứa nhiều component theo món; cộng lượng trước khi làm tròn mua. Khoản khoán lưu riêng. Tổng lượt chọn món chính / `main_pick` phải là số nguyên > 0; kiểm trước ghi. Đây là ràng buộc kỹ thuật theo BR-EST-001, cần xác nhận nếu mở loại suất chọn nhiều món.
8. Giá nhập và khoản khoán là số nguyên đồng. Phép chia như giá/1000 không được ép BIGINT. Kết quả lưu DECIMAL(24,8), cost % DECIMAL(12,2). Tính trung gian bằng decimal/rational đủ chính xác, không làm tròn mỗi bước; chỉ lượng mua làm tròn lên 2 số và cost % nửa lên 2 số theo SRS. Kiểm tràn số, không cắt âm thầm. DECIMAL lưu 8 số là lựa chọn lưu trữ đề xuất, không phải thay đổi BR-CALC-006.
9. CHECK trong migration: giá > 0; khoản khoán, chi phí, số suất và cost % >= 0; main_pick và conversion_factor > 0; 0 <= waste_pct < 100; trạng thái thuộc tập nêu ở DBML. FK phải khớp dữ liệu cha (món/công thức/nguyên liệu, ngày/cơ sở). Với dòng `in_cost=true`, bắt buộc đủ giá/NCC/ngày giá; `false` cho phép giá null, cost dòng = 0 nhưng vẫn giữ lượng nguyên liệu trong dự toán. Các CHECK, generated key và điều kiện liên bảng này chưa được thực thi chỉ bằng import DBML.

#### Hợp đồng JSON bản chụp

`inputs_snapshot` là object có `schema_version=1`, lưu **giá trị** cùng ID nguồn, không chỉ liên kết tới dữ liệu sống:

- `parameters`: `{code, value, parameter_id, effective_from}` cho cách tính món chính, hao hụt, chế độ kiểm, VAT, ngưỡng, tuổi hiệu lực bảng tính; VAT phải có giá trị khi ghi snapshot/dự toán.
- `meal_type`: `{id, name, price_cap_vnd, main_pick}`; `service_date`; `menu_version`; `default_dish_id`.
- `dishes`: `{dish_id, name, role, recipe_id, portion_code, cost_vnd, special_sheet_id}`. Chụp cả món chính được và không được chọn trong phép lấy lớn nhất/bình quân.
- `allowances`: `{allowance_id, name, meal_type_id, effective_from, amount_vnd}` đã giải quyết ưu tiên phạm vi, không tính trùng.
- `calculation`: `{formula_version, main_cost_method, main_cost_vnd, other_dishes_cost_vnd, allowance_cost_vnd, revenue_ex_vat_vnd, threshold_pct}`. Bảng tính món chỉ cần parameters liên quan và món/công thức của nó; không bắt buộc meal_type/VAT.
- Riêng tính lại: thêm `lines` chứa toàn bộ trường dữ liệu giá/định lượng tương đương `menu_cost_snapshot_lines`, và `trigger_prices` là danh sách ID giá gây tác vụ. Bảng tính, snapshot và dự toán khác dùng các bảng con để lưu dòng chi tiết.

Số decimal trong JSON mã hoá bằng chuỗi thập phân, không dùng float của JSON client. Mỗi payload kiểm schema trước lưu. Tên bảng/cột và hợp đồng này là đề xuất thiết kế; danh sách khoản khoán thực tế và giá trị VAT vẫn chờ O-01.


#### Từ điển dữ liệu COST

Các bảng dưới liệt kê toàn bộ trường mới và trường dự toán thay đổi; DBML là bản import. `id` tự tăng. Trường không có default không được tự suy ra giá trị 0. FK tới users của người tạo/người tính là bắt buộc nếu ghi bởi người dùng; worker dùng tài khoản dịch vụ có định danh. Các bảng chụp không có bộ cột sửa/xoá thông thường: đây là ngoại lệ có chủ đích của mục 1.

##### `suppliers`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Mã nghiệp vụ | `code` | VARCHAR | 32 | Không | Unique | Theo mục 5.4 | Mã nghiệp vụ |
| Tên | `name` | VARCHAR | 160 | Không | Không áp dụng | Theo mục 5.4 | Tên |
| Điện thoại | `phone` | VARCHAR | 15 | Có | Không áp dụng | Theo mục 5.4 | Điện thoại |
| REGULAR / MARKET_VENDOR | `supplier_type` | VARCHAR | 24 | Không | Không áp dụng | Theo mục 5.4 | REGULAR / MARKET_VENDOR |
| ACTIVE / INACTIVE | `status` | VARCHAR | 24 | Không | Không áp dụng | Mặc định 'ACTIVE' | ACTIVE / INACTIVE |
| Ghi chú nhà cung cấp | `note` | VARCHAR | 1000 | Có | Không áp dụng | Theo mục 5.4 | Ghi chú nhà cung cấp |
| Thời điểm tạo | `created_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tạo |
| Người tạo | `created_by` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Người tạo |
| Thời điểm sửa | `updated_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm sửa |
| Người sửa | `updated_by` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Người sửa |
| Phiên bản khoá lạc quan | `version` | INT | Không áp dụng | Không | Không áp dụng | Mặc định 1 | Phiên bản khoá lạc quan |
| Thời điểm huỷ | `cancelled_at` | DATETIME | 3 | Có | Không áp dụng | Theo mục 5.4 | Thời điểm huỷ |
| Lý do huỷ | `cancelled_reason` | VARCHAR | 500 | Có | Không áp dụng | Theo mục 5.4 | Lý do huỷ |

##### `ingredient_prices`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Nguyên liệu | `ingredient_id` | BIGINT | Không áp dụng | Không | FK → ingredients.id | Theo mục 5.4 | Nguyên liệu |
| Nhà cung cấp | `supplier_id` | BIGINT | Không áp dụng | Không | FK → suppliers.id | Theo mục 5.4 | Nhà cung cấp |
| Null = áp dụng cả 2 cơ sở | `kitchen_id` | BIGINT | Không áp dụng | Có | FK → kitchens.id | Theo mục 5.4 | Null = áp dụng cả 2 cơ sở |
| Trên 1 buy_unit. Có gồm VAT đầu vào không: điểm mở O-01 | `price_vnd` | BIGINT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Trên 1 buy_unit. Có gồm VAT đầu vào không: điểm mở O-01 |
| BR-COST-004 | `effective_from` | DATE | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | BR-COST-004 |
| Đặt bằng giao dịch theo BR-PRC-005 | `is_reference` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định false | Đặt bằng giao dịch theo BR-PRC-005; dòng đầu tiên tự được chọn |
| source file id | `source_file_id` | BIGINT | Không áp dụng | Có | FK → files.id | Theo mục 5.4 | source file id |
| Thời điểm tạo | `created_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tạo |
| Người tạo | `created_by` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Người tạo |
| Thời điểm sửa | `updated_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm sửa |
| Người sửa | `updated_by` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Người sửa |
| Phiên bản khoá lạc quan | `version` | INT | Không áp dụng | Không | Không áp dụng | Mặc định 1 | Phiên bản khoá lạc quan |
| Thời điểm huỷ | `cancelled_at` | DATETIME | 3 | Có | Không áp dụng | Theo mục 5.4 | Thời điểm huỷ |
| Lý do huỷ | `cancelled_reason` | VARCHAR | 500 | Có | Không áp dụng | Theo mục 5.4 | Lý do huỷ |

##### `cost_estimates`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Ngày thực đơn | `menu_day_id` | BIGINT | Không áp dụng | Không | FK → menu_days.id | Theo mục 5.4 | Ngày thực đơn |
| Cơ sở | `kitchen_id` | BIGINT | Không áp dụng | Không | FK → kitchens.id | Theo mục 5.4 | Cơ sở |
| Tăng theo ngày thực đơn và cơ sở, không ghi đè bản cũ | `version_no` | INT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Tăng theo ngày thực đơn và cơ sở, không ghi đè bản cũ |
| Cùng mã cho lần lập dự toán tuần | `batch_key` | CHAR | 36 | Không | Không áp dụng | Theo mục 5.4 | Cùng mã cho lần lập dự toán tuần; dùng gộp đúng bộ phiên bản |
| Tổng lượt chọn món chính / main_pick | `servings` | INT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Tổng lượt chọn món chính / main_pick; nguyên > 0 |
| Số món chính chọn trên suất đã chụp | `main_pick` | TINYINT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Số món chính chọn trên suất đã chụp; > 0 |
| DAT_NHAT / BINH_QUAN / MAC_DINH | `main_cost_method` | VARCHAR | 24 | Không | Không áp dụng | Theo mục 5.4 | DAT_NHAT / BINH_QUAN / MAC_DINH |
| Đồng, giá trị tính trước làm tròn hiển thị | `total_cost_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Đồng, giá trị tính trước làm tròn hiển thị | `cost_per_serving_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Đồng, giá trị tính trước làm tròn hiển thị | `revenue_ex_vat_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Theo số suất từng món, nửa lên 2 chữ số | `cost_pct` | DECIMAL | 12,2 | Không | Không áp dụng | Theo mục 5.4 | Theo số suất từng món, nửa lên 2 chữ số; có thể > 100 |
| Cost % theo phương pháp kiểm thực đơn | `menu_cost_pct` | DECIMAL | 12,2 | Không | Không áp dụng | Theo mục 5.4 | Cost % theo phương pháp kiểm thực đơn; không nhầm cost_pct dự toán |
| Ngưỡng cost | `threshold_pct` | DECIMAL | 5,2 | Không | Không áp dụng | Theo mục 5.4 | Ngưỡng cost |
| Ngày lấy giá nhập | `price_as_of` | DATE | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Ngày lấy giá nhập |
| Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4 | `inputs_snapshot` | JSON | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống |
| Thời điểm tính | `computed_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tính |
| Người tính | `computed_by` | BIGINT | Không áp dụng | Không | FK → users.id | Theo mục 5.4 | Người tính |

##### `cost_estimate_lines`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Mã dự toán | `estimate_id` | BIGINT | Không áp dụng | Không | FK → cost_estimates.id | Theo mục 5.4 | Mã dự toán |
| Nguyên liệu | `ingredient_id` | BIGINT | Không áp dụng | Không | FK → ingredients.id | Theo mục 5.4 | Nguyên liệu |
| Null khi nguyên liệu ngoài cost | `ingredient_price_id` | BIGINT | Không áp dụng | Có | FK → ingredient_prices.id | Theo mục 5.4 | Null khi nguyên liệu ngoài cost |
| Nhà cung cấp | `supplier_id` | BIGINT | Không áp dụng | Có | FK → suppliers.id | Theo mục 5.4 | Nhà cung cấp |
| Tên nguyên liệu đã chụp | `ingredient_name` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Tên nguyên liệu đã chụp |
| Tên nhà cung cấp đã chụp | `supplier_name` | VARCHAR | 160 | Có | Không áp dụng | Theo mục 5.4 | Tên nhà cung cấp đã chụp |
| Ngày hiệu lực giá đã chụp | `price_effective_from` | DATE | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Ngày hiệu lực giá đã chụp |
| Tính vào cost | `in_cost` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Tính vào cost |
| Đơn vị dùng | `use_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị dùng |
| Đơn vị mua | `buy_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị mua |
| > 0, đã chụp | `conversion_factor` | DECIMAL | 12,4 | Không | Không áp dụng | Theo mục 5.4 | > 0, đã chụp |
| Tổng định lượng sau hao hụt từ các component | `total_use_qty` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Tổng định lượng sau hao hụt từ các component |
| Làm tròn lên 2 chữ số sau gộp theo nguyên liệu | `buy_qty` | DECIMAL | 18,2 | Không | Không áp dụng | Theo mục 5.4 | Làm tròn lên 2 chữ số sau gộp theo nguyên liệu |
| > 0 khi in_cost | `price_per_buy_unit_vnd` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | > 0 khi in_cost; null khi ngoài cost |
| Đồng, giá trị tính trước làm tròn hiển thị | `amount_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |

##### `cost_sheets`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Món đặc thù | `dish_id` | BIGINT | Không áp dụng | Không | FK → dishes.id | Theo mục 5.4 | Món đặc thù |
| Phiên bản công thức đã tính | `recipe_id` | BIGINT | Không áp dụng | Không | FK → recipes.id | Theo mục 5.4 | Phiên bản công thức đã tính |
| Cơ sở tính giá | `kitchen_id` | BIGINT | Không áp dụng | Không | FK → kitchens.id | Theo mục 5.4 | Cơ sở tính giá |
| Ngày lấy công thức và giá | `calculation_date` | DATE | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Ngày lấy công thức và giá |
| PENDING / APPROVED / REJECTED | `status` | VARCHAR | 24 | Không | Không áp dụng | Mặc định 'PENDING' | PENDING / APPROVED / REJECTED |
| Đồng, giá trị tính trước làm tròn hiển thị | `total_cost_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4 | `inputs_snapshot` | JSON | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống |
| Ghi chú người lập | `note` | VARCHAR | 1000 | Có | Không áp dụng | Theo mục 5.4 | Ghi chú người lập |
| Người duyệt cuối, khác người lập | `approved_by` | BIGINT | Không áp dụng | Có | FK → users.id | Theo mục 5.4 | Người duyệt cuối, khác người lập |
| Thời điểm duyệt UTC | `approved_at` | DATETIME | 3 | Có | Không áp dụng | Theo mục 5.4 | Thời điểm duyệt UTC |
| Thời điểm tạo, UTC | `created_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tạo, UTC |
| Người lập | `created_by` | BIGINT | Không áp dụng | Không | FK → users.id | Theo mục 5.4 | Người lập |

##### `cost_sheet_lines`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Bảng tính cha | `sheet_id` | BIGINT | Không áp dụng | Không | FK → cost_sheets.id | Theo mục 5.4 | Bảng tính cha |
| Công thức nguồn | `recipe_id` | BIGINT | Không áp dụng | Không | FK → recipes.id | Theo mục 5.4 | Công thức nguồn |
| Nguyên liệu nguồn | `ingredient_id` | BIGINT | Không áp dụng | Không | FK → ingredients.id | Theo mục 5.4 | Nguyên liệu nguồn |
| Null chỉ khi in_cost = false | `ingredient_price_id` | BIGINT | Không áp dụng | Có | FK → ingredient_prices.id | Theo mục 5.4 | Null chỉ khi in_cost = false |
| Nhà cung cấp đã chọn | `supplier_id` | BIGINT | Không áp dụng | Có | FK → suppliers.id | Theo mục 5.4 | Nhà cung cấp đã chọn; null nếu không tính cost |
| Tên nguyên liệu tại lúc chụp | `ingredient_name` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Tên nguyên liệu tại lúc chụp |
| Tên nhà cung cấp tại lúc chụp | `supplier_name` | VARCHAR | 160 | Có | Không áp dụng | Theo mục 5.4 | Tên nhà cung cấp tại lúc chụp |
| Ngày hiệu lực của giá đã dùng | `price_effective_from` | DATE | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Ngày hiệu lực của giá đã dùng |
| Cờ tính vào cost tại lúc chụp | `in_cost` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Cờ tính vào cost tại lúc chụp |
| Nguyên liệu chính trong công thức | `is_main` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Nguyên liệu chính trong công thức |
| Định lượng chuẩn trước hao hụt | `qty_std` | DECIMAL | 10,3 | Không | Không áp dụng | Theo mục 5.4 | Định lượng chuẩn trước hao hụt; > 0 |
| Đơn vị dùng đã chụp | `use_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị dùng đã chụp |
| Đơn vị mua đã chụp | `buy_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị mua đã chụp |
| Số đơn vị dùng trên đơn vị mua | `conversion_factor` | DECIMAL | 12,4 | Không | Không áp dụng | Theo mục 5.4 | Số đơn vị dùng trên đơn vị mua; > 0 |
| Hao hụt đã chụp, 0 <= giá trị < 100 | `waste_pct` | DECIMAL | 5,2 | Không | Không áp dụng | Theo mục 5.4 | Hao hụt đã chụp, 0 <= giá trị < 100 |
| Giá trên đơn vị mua | `price_per_buy_unit_vnd` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Giá trên đơn vị mua; > 0 khi in_cost = true |
| Đồng, giá trị tính trước làm tròn hiển thị | `line_cost_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |

##### `cost_allowances`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Tên khoản khoán | `name` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Tên khoản khoán; chuẩn hoá như BR-CAT-001 |
| Null = mọi loại suất | `meal_type_id` | BIGINT | Không áp dụng | Có | FK → meal_types.id | Theo mục 5.4 | Null = mọi loại suất |
| Số nguyên đồng trên suất | `amount_vnd` | BIGINT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Số nguyên đồng trên suất; >= 0 |
| Ngày bắt đầu hiệu lực | `effective_from` | DATE | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Ngày bắt đầu hiệu lực |
| PENDING / APPROVED / REJECTED | `status` | VARCHAR | 24 | Không | Không áp dụng | Mặc định 'PENDING' | PENDING / APPROVED / REJECTED |
| Lý do đề nghị | `reason` | VARCHAR | 500 | Không | Không áp dụng | Theo mục 5.4 | Lý do đề nghị; ít nhất 10 ký tự |
| Khác người lập | `approved_by` | BIGINT | Không áp dụng | Có | FK → users.id | Theo mục 5.4 | Khác người lập |
| Thời điểm duyệt | `approved_at` | DATETIME | 3 | Có | Không áp dụng | Theo mục 5.4 | Thời điểm duyệt |
| Thời điểm tạo, UTC | `created_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tạo, UTC |
| Người lập | `created_by` | BIGINT | Không áp dụng | Không | FK → users.id | Theo mục 5.4 | Người lập |

##### `menu_cost_snapshots`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Ngày của thực đơn được duyệt | `menu_day_id` | BIGINT | Không áp dụng | Không | FK → menu_days.id | Theo mục 5.4 | Ngày của thực đơn được duyệt |
| Một bản cho mỗi cơ sở được kiểm | `kitchen_id` | BIGINT | Không áp dụng | Không | FK → kitchens.id | Theo mục 5.4 | Một bản cho mỗi cơ sở được kiểm |
| Vòng duyệt của menus, khớp approvals.round_no | `approval_round_no` | SMALLINT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Vòng duyệt của menus, khớp approvals.round_no |
| Ngày phục vụ được chụp | `service_date` | DATE | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Ngày phục vụ được chụp |
| Đồng, giá trị tính trước làm tròn hiển thị | `cost_per_serving_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Đồng, giá trị tính trước làm tròn hiển thị | `revenue_ex_vat_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |
| Làm tròn nửa lên 2 chữ số | `cost_pct` | DECIMAL | 12,2 | Không | Không áp dụng | Theo mục 5.4 | Làm tròn nửa lên 2 chữ số; >= 0, có thể > 100 |
| Ngưỡng đã dùng | `threshold_pct` | DECIMAL | 5,2 | Không | Không áp dụng | Theo mục 5.4 | Ngưỡng đã dùng |
| DAT / KHONG_DAT | `result` | VARCHAR | 24 | Không | Không áp dụng | Theo mục 5.4 | DAT / KHONG_DAT; cảnh báo cho phép duyệt bản KHONG_DAT |
| Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4 | `inputs_snapshot` | JSON | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống |
| Thời điểm tạo, UTC | `created_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tạo, UTC |
| Người lập | `created_by` | BIGINT | Không áp dụng | Không | FK → users.id | Theo mục 5.4 | Người lập |

##### `menu_cost_snapshot_lines`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Bản chụp ngày/cơ sở | `snapshot_id` | BIGINT | Không áp dụng | Không | FK → menu_cost_snapshots.id | Theo mục 5.4 | Bản chụp ngày/cơ sở |
| Món đã dùng | `dish_id` | BIGINT | Không áp dụng | Không | FK → dishes.id | Theo mục 5.4 | Món đã dùng |
| Công thức nguồn | `recipe_id` | BIGINT | Không áp dụng | Không | FK → recipes.id | Theo mục 5.4 | Công thức nguồn |
| Nguyên liệu nguồn | `ingredient_id` | BIGINT | Không áp dụng | Không | FK → ingredients.id | Theo mục 5.4 | Nguyên liệu nguồn |
| Null chỉ khi in_cost = false | `ingredient_price_id` | BIGINT | Không áp dụng | Có | FK → ingredient_prices.id | Theo mục 5.4 | Null chỉ khi in_cost = false |
| Nhà cung cấp đã chọn | `supplier_id` | BIGINT | Không áp dụng | Có | FK → suppliers.id | Theo mục 5.4 | Nhà cung cấp đã chọn; null nếu không tính cost |
| Tên nguyên liệu tại lúc chụp | `ingredient_name` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Tên nguyên liệu tại lúc chụp |
| Tên nhà cung cấp tại lúc chụp | `supplier_name` | VARCHAR | 160 | Có | Không áp dụng | Theo mục 5.4 | Tên nhà cung cấp tại lúc chụp |
| Ngày hiệu lực của giá đã dùng | `price_effective_from` | DATE | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Ngày hiệu lực của giá đã dùng |
| Cờ tính vào cost tại lúc chụp | `in_cost` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Cờ tính vào cost tại lúc chụp |
| Nguyên liệu chính trong công thức | `is_main` | BOOLEAN | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Nguyên liệu chính trong công thức |
| Định lượng chuẩn trước hao hụt | `qty_std` | DECIMAL | 10,3 | Không | Không áp dụng | Theo mục 5.4 | Định lượng chuẩn trước hao hụt; > 0 |
| Đơn vị dùng đã chụp | `use_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị dùng đã chụp |
| Đơn vị mua đã chụp | `buy_unit` | VARCHAR | 16 | Không | Không áp dụng | Theo mục 5.4 | Đơn vị mua đã chụp |
| Số đơn vị dùng trên đơn vị mua | `conversion_factor` | DECIMAL | 12,4 | Không | Không áp dụng | Theo mục 5.4 | Số đơn vị dùng trên đơn vị mua; > 0 |
| Hao hụt đã chụp, 0 <= giá trị < 100 | `waste_pct` | DECIMAL | 5,2 | Không | Không áp dụng | Theo mục 5.4 | Hao hụt đã chụp, 0 <= giá trị < 100 |
| Giá trên đơn vị mua | `price_per_buy_unit_vnd` | BIGINT | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Giá trên đơn vị mua; > 0 khi in_cost = true |
| Đồng, giá trị tính trước làm tròn hiển thị | `line_cost_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |

##### `cost_recalculations`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Bản duyệt gốc dùng so sánh | `snapshot_id` | BIGINT | Không áp dụng | Không | FK → menu_cost_snapshots.id | Theo mục 5.4 | Bản duyệt gốc dùng so sánh |
| Khoá sự kiện giá để retry không trùng | `event_key` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Khoá sự kiện giá để retry không trùng |
| DAT / KHONG_DAT / KHONG_XAC_DINH | `result` | VARCHAR | 24 | Không | Không áp dụng | Theo mục 5.4 | DAT / KHONG_DAT / KHONG_XAC_DINH |
| Null khi không tính được | `cost_per_serving_vnd` | DECIMAL | 24,8 | Có | Không áp dụng | Theo mục 5.4 | Null khi không tính được |
| Null khi không tính được | `cost_pct` | DECIMAL | 12,2 | Có | Không áp dụng | Theo mục 5.4 | Null khi không tính được; không gán 0 |
| Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4 | `inputs_snapshot` | JSON | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống |
| Danh sách nguyên liệu thiếu giá nếu có | `missing_ingredient_ids` | JSON | Không áp dụng | Có | Không áp dụng | Theo mục 5.4 | Danh sách nguyên liệu thiếu giá nếu có |
| Thời điểm tính lại UTC | `computed_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm tính lại UTC |

##### `cost_alerts`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Duy nhất một cảnh báo mở theo ngày thực đơn | `menu_day_id` | BIGINT | Không áp dụng | Không | FK → menu_days.id | Theo mục 5.4 | Duy nhất một cảnh báo mở theo ngày thực đơn |
| OPEN / CLOSED | `status` | VARCHAR | 16 | Không | Không áp dụng | Mặc định 'OPEN' | OPEN / CLOSED |
| Thời điểm mở | `opened_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm mở |
| Thời điểm sửa | `updated_at` | DATETIME | 3 | Không | Không áp dụng | Theo mục 5.4 | Thời điểm sửa |
| Thời điểm đóng | `closed_at` | DATETIME | 3 | Có | Không áp dụng | Theo mục 5.4 | Thời điểm đóng |
| Null nếu đóng tự động | `closed_by` | BIGINT | Không áp dụng | Có | FK → users.id | Theo mục 5.4 | Null nếu đóng tự động |
| Bắt buộc khi đóng tay | `close_reason` | VARCHAR | 500 | Có | Không áp dụng | Theo mục 5.4 | Bắt buộc khi đóng tay; ít nhất 10 ký tự |
| MENU_REVISED / PRICE_RECOVERED / MANUAL | `close_type` | VARCHAR | 24 | Có | Không áp dụng | Theo mục 5.4 | MENU_REVISED / PRICE_RECOVERED / MANUAL |
| Khoá lạc quan | `version` | INT | Không áp dụng | Không | Không áp dụng | Mặc định 1 | Khoá lạc quan |

##### `cost_alert_kitchens`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Cảnh báo ngày | `alert_id` | BIGINT | Không áp dụng | Không | FK → cost_alerts.id | Theo mục 5.4 | Cảnh báo ngày |
| Cơ sở bị ảnh hưởng | `kitchen_id` | BIGINT | Không áp dụng | Không | FK → kitchens.id | Theo mục 5.4 | Cơ sở bị ảnh hưởng |
| Cost lúc duyệt | `snapshot_id` | BIGINT | Không áp dụng | Không | FK → menu_cost_snapshots.id | Theo mục 5.4 | Cost lúc duyệt |
| Cost hiện tại và giá gây thay đổi | `latest_recalculation_id` | BIGINT | Không áp dụng | Không | FK → cost_recalculations.id | Theo mục 5.4 | Cost hiện tại và giá gây thay đổi |

##### `cost_estimate_servings`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Mã dự toán | `estimate_id` | BIGINT | Không áp dụng | Không | FK → cost_estimates.id | Theo mục 5.4 | Mã dự toán |
| Món chính thuộc ngày dự toán | `dish_id` | BIGINT | Không áp dụng | Không | FK → dishes.id | Theo mục 5.4 | Món chính thuộc ngày dự toán |
| Tên món đã chụp | `dish_name` | VARCHAR | 160 | Không | Không áp dụng | Theo mục 5.4 | Tên món đã chụp |
| Số lượt chọn món | `servings` | INT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Số lượt chọn món; nguyên >= 0 |

##### `cost_estimate_components`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Dòng nguyên liệu dự toán | `estimate_line_id` | BIGINT | Không áp dụng | Không | FK → cost_estimate_lines.id | Theo mục 5.4 | Dòng nguyên liệu dự toán |
| Món | `dish_id` | BIGINT | Không áp dụng | Không | FK → dishes.id | Theo mục 5.4 | Món |
| Công thức | `recipe_id` | BIGINT | Không áp dụng | Không | FK → recipes.id | Theo mục 5.4 | Công thức |
| Tên món đã chụp | `dish_name` | VARCHAR | 160 | Không | Không áp dụng | Theo mục 5.4 | Tên món đã chụp |
| Định lượng sau áp hao hụt đúng một lần | `qty_per_serving` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Định lượng sau áp hao hụt đúng một lần |
| Số suất món | `servings` | INT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Số suất món; >= 0 |
| qty_per_serving x servings | `total_use_qty` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | qty_per_serving x servings |
| qty_std, use_unit, in_cost, waste_pct, conversion_factor đã dùng | `recipe_item_snapshot` | JSON | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | qty_std, use_unit, in_cost, waste_pct, conversion_factor đã dùng |

##### `cost_estimate_allowances`

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã bản ghi | `id` | BIGINT | Không áp dụng | Không | PK | Theo mục 5.4 | Mã bản ghi |
| Mã dự toán | `estimate_id` | BIGINT | Không áp dụng | Không | FK → cost_estimates.id | Theo mục 5.4 | Mã dự toán |
| Khoản khoán | `allowance_id` | BIGINT | Không áp dụng | Không | FK → cost_allowances.id | Theo mục 5.4 | Khoản khoán |
| Tên khoản tại lúc lập | `name` | VARCHAR | 120 | Không | Không áp dụng | Theo mục 5.4 | Tên khoản tại lúc lập |
| Đồng trên suất | `amount_per_serving_vnd` | BIGINT | Không áp dụng | Không | Không áp dụng | Theo mục 5.4 | Đồng trên suất; >= 0 |
| Đồng, giá trị tính trước làm tròn hiển thị | `total_amount_vnd` | DECIMAL | 24,8 | Không | Không áp dụng | Theo mục 5.4 | Đồng, giá trị tính trước làm tròn hiển thị; >= 0 |

---


### Ràng buộc áp dụng trong transaction/service

- Giá mới bắt buộc basis được xác minh; legacy giữ nguyên price_vnd và null metadata, không tự cộng VAT hoặc sửa snapshot. Thiếu VAT ở EXCLUSIVE không tạo giá; kết quả không nguyên đồng bị chặn chờ rounding, không làm tròn ngầm.
- PERCENT chỉ có rate_pct; FIXED_PER_SERVING chỉ có amount_per_serving; số không âm, qty nguyên không âm. Tỷ lệ vượt100 và khoản vượt base không cho xác nhận trước khi chốt mức trần; chỉ lưu giả định draft nếu hợp đồng cho phép.
- pricing_snapshot.order_id phải bằng discount.order_id; kiểm bằng transaction hoặc composite FK bổ sung trong migration. Không tin customer/scope client; đọc từ order→service_point→customer.
- Bản chụp bất biến; (order,order_version) duy nhất. Khi order đổi, thêm snapshot; khoản liên quan NEEDS_REVIEW và audit một lần theo event_key. Không tự sửa số phải trả hoặc settlement.
- Một order có nhiều draft không đồng nghĩa nhiều chương trình được cộng dồn. CONFIRMED/CANCELLED dành cho thiết kế tương lai; không mở API quyết định/chi trả trước CK-Q04–Q10. Không có cột paid mặc định0 để nhầm với đã đối soát.
- Quyền đọc/ghi extension chưa được cấp theo vai trò mặc định. Agent phía khách không đọc bảng giá, snapshot kế toán hoặc chiết khấu. Grant DB và allowlist serializer phải review cùng NFR-COST-006.
- customer_price_terms ACTIVE không chồng khoảng hiệu lực cho cùng khách/loại suất; effective_to>=effective_from. Cách duyệt activation còn mở; API đợt này chỉ draft.

### Từ điển dữ liệu bổ sung

#### `ingredient_prices: cột bổ sung`

| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- |
| price_vnd | bigint | Không | not null | Gia cost cuoi cung gom VAT phai tra / buy_unit; server tinh. Legacy chua xac minh khong tu cong VAT |
| quoted_unit_price | decimal(18,6) | Có | Không áp dụng | Gia bao goc; null voi legacy, khong suy dien nguoc |
| price_basis | varchar(24) | Không | not null, default: 'LEGACY_UNVERIFIED' | INCLUSIVE / EXCLUSIVE / FINAL_CONFIRMED / LEGACY_UNVERIFIED; new write khong nhan legacy |
| vat_rate_pct | decimal(9,6) | Có | Không áp dụng | Nullable, khong mac dinh0; EXCLUSIVE can rate hoac amount, khong ca hai |
| vat_unit_amount | decimal(18,6) | Có | Không áp dụng | VAT phai tra / buy_unit, nullable; neu co rate thi server tinh amount |
| pricing_evidence | varchar(1000) | Có | Không áp dụng | Nguon xac nhan gia cuoi; FINAL_CONFIRMED bat buoc; khong phan loai thue phap ly |
| pricing_verified_at | datetime(3) | Có | Không áp dụng | Chua xac minh thi null, khong suy ra tu created_at |
| pricing_verified_by | bigint | Có | ref: > users.id | pricing_verified_by |
| normalization_version | varchar(32) | Có | Không áp dụng | Thuat toan chuan hoa gia; null voi legacy |

#### `customer_price_terms`

| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- |
| id | bigint | Không | pk, increment | id |
| customer_id | bigint | Không | not null, ref: > customers.id | customer_id |
| meal_type_id | bigint | Không | not null, ref: > meal_types.id | meal_type_id |
| quoted_unit_price | decimal(18,6) | Không | not null | quoted_unit_price |
| sale_price_basis | varchar(24) | Không | not null, default: 'UNKNOWN' | INCLUSIVE / EXCLUSIVE / FINAL_CONFIRMED / UNKNOWN |
| vat_rate_pct | decimal(9,6) | Có | Không áp dụng | Null khac0; invoiceRequested khong quyet dinh rate |
| invoice_requested | boolean | Có | Không áp dụng | Null=chua hoi; false khong nghia VAT0 |
| evidence | varchar(1000) | Có | Không áp dụng | Thoa thuan va nguon xac nhan |
| effective_from | date | Không | not null | effective_from |
| effective_to | date | Có | Không áp dụng | Nullable; rang buoc khong chong lan ACTIVE theo customer/meal type can transaction |
| status | varchar(24) | Không | not null, default: 'DRAFT' | DRAFT / ACTIVE / CANCELLED; activation gated cho sales policy |
| version | int | Không | not null, default: 1 | version |
| created_by | bigint | Không | not null, ref: > users.id | created_by |
| created_at | datetime(3) | Không | not null | created_at |
| updated_by | bigint | Có | ref: > users.id | updated_by |
| updated_at | datetime(3) | Có | Không áp dụng | updated_at |

#### `order_pricing_snapshots`

| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- |
| id | bigint | Không | pk, increment | id |
| order_id | bigint | Không | not null, ref: > orders.id | order_id |
| order_version | int | Không | not null | order_version |
| price_term_id | bigint | Có | ref: > customer_price_terms.id | price_term_id |
| quoted_unit_price | decimal(18,6) | Không | not null | quoted_unit_price |
| sale_price_basis | varchar(24) | Không | not null | sale_price_basis |
| vat_rate_pct | decimal(9,6) | Có | Không áp dụng | vat_rate_pct |
| invoice_requested | boolean | Có | Không áp dụng | invoice_requested |
| servings | int | Không | not null | servings |
| gross_amount_due | decimal(18,6) | Có | Không áp dụng | Khong tru khoan chiet khau rieng; null neu UNKNOWN |
| revenue_ex_vat | decimal(18,6) | Có | Không áp dụng | Null neu chua du VAT/context; khong lay gross neu invoice=false |
| context_status | varchar(24) | Không | not null | RESOLVED / UNRESOLVED / LEGACY_UNVERIFIED |
| captured_at | datetime(3) | Không | not null | captured_at |
| captured_by | bigint | Không | not null, ref: > users.id | captured_by |
| inputs_snapshot | json | Không | not null | Bat bien; quyen doc rieng, khong serialize cho agent khach |

#### `order_discount_records`

| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- |
| id | bigint | Không | pk, increment | id |
| order_id | bigint | Không | not null, ref: > orders.id | order_id |
| pricing_snapshot_id | bigint | Không | not null, ref: > order_pricing_snapshots.id | pricing_snapshot_id |
| proposal_key | varchar(64) | Không | not null | Khong phai key TTL; unique proposal trong order |
| calculation_type | varchar(24) | Không | not null | PERCENT / FIXED_PER_SERVING |
| rate_pct | decimal(9,6) | Có | Không áp dụng | Chi PERCENT; base chua chot thi draft only |
| amount_per_serving | decimal(18,6) | Có | Không áp dụng | Chi FIXED_PER_SERVING; rounding CK-Q03 |
| percent_basis | varchar(24) | Không | not null, default: 'UNRESOLVED' | GROSS / NET / UNRESOLVED; ghi gia dinh draft khong dong CK-Q01 |
| eligible_servings | int | Có | Không áp dụng | CK-Q02; khong lay qty dish lines thay so suat |
| quantity_basis | varchar(24) | Không | not null, default: 'UNRESOLVED' | ORDERED / DELIVERED / CONFIRMED / UNRESOLVED |
| base_amount | decimal(18,6) | Có | Không áp dụng | Server-derived, null neu chua xac dinh |
| calculated_amount | decimal(18,6) | Có | Không áp dụng | So tinh thu, khong phai paid amount; null neu thieu base |
| status | varchar(24) | Không | not null, default: 'DRAFT' | DRAFT / NEEDS_REVIEW / CONFIRMED / CANCELLED; confirm/cancel da xu ly gated CK-Q04-09 |
| calculation_snapshot | json | Không | not null | Gia dinh, gates, ruleVersion; khong ghi len amountDue cua order |
| version | int | Không | not null, default: 1 | version |
| created_by | bigint | Không | not null, ref: > users.id | created_by |
| created_at | datetime(3) | Không | not null | created_at |
| updated_by | bigint | Có | ref: > users.id | updated_by |
| updated_at | datetime(3) | Có | Không áp dụng | updated_at |

#### `order_discount_events`

| Cột vật lý | Kiểu | Null? | Khóa / ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- |
| id | bigint | Không | pk, increment | id |
| discount_id | bigint | Không | not null, ref: > order_discount_records.id | discount_id |
| event_key | varchar(64) | Không | not null | Event replay chi ghi mot lan |
| event_type | varchar(32) | Không | not null | DRAFT_CREATED / DRAFT_UPDATED / ORDER_CHANGED / REVIEW_REQUESTED; khong settlement event |
| actor_id | bigint | Có | ref: > users.id | Nullable cho worker; event phai co actor hoac system source |
| source | varchar(32) | Không | not null | source |
| payload | json | Không | not null | Before/after va reason, version; khong luu token |
| created_at | datetime(3) | Không | not null | created_at |


