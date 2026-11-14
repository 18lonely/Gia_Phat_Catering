---
id: DOC-THUC-DON-SRS-DATA-DICTIONARY
title: Từ điển dữ liệu E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-dictionary, e2]
author: BA
last_updated: 2026-11-16
---
# Từ điển dữ liệu E2: Thực đơn và định lượng (MENU)

Draft · 16/11/2026 · Thiết kế đề xuất, chưa migration.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách nguyên văn phần từ điển của E2 ra khỏi ERD theo khuôn chung các epic. Không đổi bảng, cột hay ràng buộc |

Sơ đồ quan hệ vẫn ở [ERD](erd.md); schema chung là [DBML 65 bảng](../../nen-tang/srs/schema.dbml). Các tiêu đề mục giữ số mục cũ của nơi gốc để đối chiếu.

Bảng dùng chung (`users`, `user_roles`, `audit_logs`, `parameters`, `change_requests`, `approvals`, `files`, `notifications`) xem [từ điển dữ liệu E1](../../nen-tang/srs/data-dictionary.md); quy ước kiểu dữ liệu chung xem [ERD tổng mục 1](../../nen-tang/srs/erd.md).

## Phần chuyển từ [ERD tổng](../../nen-tang/srs/erd.md)

### 4.1 `ingredients`: Nguyên liệu

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Mã nguyên liệu | Mã nghiệp vụ | VARCHAR | 32 | Không | Unique | Không áp dụng | Không áp dụng |
| Tên | Tên | VARCHAR | 120 | Không | Không áp dụng | Không áp dụng | Ví dụ "Thịt lợn nạc vai" |
| Nhóm nguyên liệu | group_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `ingredient_groups.id` | Không áp dụng | Lợn, gà, bò, ếch, tôm, cá… Danh sách: [H-3] |
| Đơn vị mua | buy_unit | VARCHAR | 16 | Không | Không áp dụng | `kg`, `bìa`, `quả`, `lít`, `bó`… | Đơn vị trên chứng từ |
| Đơn vị dùng | use_unit | VARCHAR | 16 | Không | Không áp dụng | `g`, `bìa`, `quả`, `ml` | Đơn vị trong công thức |
| Hệ số quy đổi | conversion_factor | DECIMAL | 12,4 | Không | Không áp dụng | > 0 | Số đơn vị dùng trong 1 đơn vị mua (1 kg = 1000 g) |
| Tỷ lệ hao hụt | waste_pct | DECIMAL | 5,2 | Có | Không áp dụng | 0–99,99; bắt buộc nếu `has_bone_or_shell` | `BR-COST-010` |
| Có xương/vỏ | has_bone_or_shell | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | Không áp dụng |
| Loại bảo quản | storage_type | VARCHAR | 24 | Không | Không áp dụng | `FRESH`, `FROZEN`, `DRY` | Quyết định ngưỡng giá cũ (`BR-COST-005`) |
| Nguồn cung ổn định | stable_supply | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | `BR-MENU-044` |
| Tính vào cost | in_cost | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | Cho phép loại khoản không tính cost; định nghĩa: [O-01] |

### 4.2 `dishes`: Món

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Mã món | Mã nghiệp vụ | VARCHAR | 32 | Không | Unique | Không áp dụng | Không áp dụng |
| Tên | Tên | VARCHAR | 160 | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Vai trò | role | VARCHAR | 24 | Không | Không áp dụng | `MAIN`, `SIDE`, `VEG`, `SOUP` | `BR-MENU-001`, `004`, `005` |
| Nhóm nguyên liệu chính | main_group_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `ingredient_groups.id` | Không áp dụng | `BR-MENU-010` → `015` |
| Phương pháp chế biến | cooking_method_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `cooking_methods.id` | Danh sách: [H-8] | `BR-MENU-020` → `023` |
| Món gốc | base_dish_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `dishes.id` | Không áp dụng | Hai món cùng món gốc tính là một khi đếm lặp (`BR-MENU-014`) |
| Healthy | is_healthy | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE; TRUE đòi hỏi phương pháp thuộc danh sách ít dầu mỡ [H-1] | `BR-MENU-002`, `003` |
| Vị chua | is_sour | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | `BR-MENU-030` |
| Kết cấu | texture | VARCHAR | 24 | Không | Không áp dụng | `DRY`, `SAUCE`, `NEUTRAL` | `BR-MENU-031`, `032` |
| Thanh nhẹ | is_light | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | `BR-MENU-033` |
| Cầu kỳ | is_complex | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | `BR-MENU-040`, `041` |
| Chịu vận chuyển | transport_ok | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | `BR-MENU-042` |
| Phù hợp bếp lớn | bulk_ok | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | `BR-MENU-043` |
| Nhóm cost | cost_tier | VARCHAR | 24 | Không | Không áp dụng | `LOW`, `HIGH` | `BR-COST-006` |
| Đặc thù | is_special | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | `BR-COST-007` |
| Ảnh | image_file_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `files.id` | Không áp dụng | Không áp dụng |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | `DRAFT`, `PENDING`, `ACTIVE`, `INACTIVE` | Chỉ `ACTIVE` vào được thực đơn và được agent dùng |
| Người duyệt | approved_by | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Khác `created_by` | `BR-SEC-008` |

### 4.3 `recipes` và `recipe_items`: Công thức có phiên bản

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | recipes.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Món | recipes.dish_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `dishes.id` | Không áp dụng | Không áp dụng |
| Cỡ định lượng | recipes.portion_code | VARCHAR | 16 | Không | Không áp dụng | Mặc định `STD` | Xem ghi chú [O-02] bên dưới |
| Số phiên bản | recipes.version_no | INT UNSIGNED | Không áp dụng | Không | Không áp dụng | Tăng dần theo (`dish_id`, `portion_code`) | Không áp dụng |
| Hiệu lực từ | recipes.effective_from | DATE | Không áp dụng | Không | Không áp dụng | Không áp dụng | Công thức dùng cho ngày D là phiên bản `ACTIVE` có `effective_from` ≤ D lớn nhất |
| Trạng thái | recipes.status | VARCHAR | 24 | Không | Không áp dụng | `DRAFT`, `PENDING`, `ACTIVE`, `SUPERSEDED` | Không áp dụng |
| Người duyệt | recipes.approved_by | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Khác `created_by` | `BR-SEC-008` |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`dish_id`, `portion_code`, `version_no`) | Không áp dụng |
| Mã dòng | recipe_items.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Công thức | recipe_items.recipe_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `recipes.id` | Không áp dụng | Không áp dụng |
| Nguyên liệu | recipe_items.ingredient_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `ingredients.id` | Không áp dụng | Không áp dụng |
| Là nguyên liệu chính | recipe_items.is_main | BOOLEAN | Không áp dụng | Không | Không áp dụng | Không áp dụng | `BR-COST-009` |
| Định lượng tối thiểu | recipe_items.qty_min | DECIMAL | 10,3 | Không | Không áp dụng | > 0 | Docx: "65–70g" → 65 |
| Định lượng tối đa | recipe_items.qty_max | DECIMAL | 10,3 | Không | Không áp dụng | ≥ `qty_min` | → 70 |
| Định lượng tính cost | recipe_items.qty_std | DECIMAL | 10,3 | Không | Không áp dụng | Trong [`qty_min`, `qty_max`] | Giá trị dùng để tính cost và dinh dưỡng |
| Đơn vị | recipe_items.unit | VARCHAR | 16 | Không | Không áp dụng | Bằng `ingredients.use_unit` | Định lượng **sống** theo docx |

**Ghi chú [O-02].** Cột `portion_code` giữ được cả hai phương án mà không phải đổi cấu trúc: nếu mỗi món chỉ có một định lượng thì mọi công thức dùng `STD`; nếu có nhiều cỡ thì mỗi cỡ là một `portion_code` với công thức và giá bán riêng. Quyết định O-02 chỉ ảnh hưởng giao diện và quy tắc chọn món.

Công thức đã `ACTIVE` không sửa; thay đổi tạo phiên bản mới, phiên bản cũ chuyển `SUPERSEDED`.

### 4.4 `dish_prices`: Giá bán món [D-18]

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Món | dish_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `dishes.id` | Không áp dụng | Không áp dụng |
| Cỡ định lượng | portion_code | VARCHAR | 16 | Không | Không áp dụng | Mặc định `STD` | Khớp `recipes.portion_code` |
| Giá bán | price_vnd | BIGINT | Không áp dụng | Không | Không áp dụng | ≥ 0; đã gồm VAT [D-15] | Hiển thị cho khách |
| Hiệu lực từ | effective_from | DATE | Không áp dụng | Không | Không áp dụng | Không áp dụng | Giá đã hiệu lực không sửa |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | `PENDING`, `APPROVED` | Không áp dụng |
| Người duyệt | approved_by | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Khác `created_by` | Không áp dụng |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`dish_id`, `portion_code`, `effective_from`) | Không áp dụng |

### 4.5 `meal_types`: Loại suất [D-20]

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Mã loại suất | Mã nghiệp vụ | VARCHAR | 32 | Không | Unique | Không áp dụng | Không áp dụng |
| Tên | Tên | VARCHAR | 120 | Không | Không áp dụng | Không áp dụng | Ví dụ "Suất 40k" |
| Ngưỡng giá | price_cap_vnd | BIGINT | Không áp dụng | Không | Không áp dụng | > 0; đã gồm VAT | Tổng giá bán các món của một suất không vượt mức này (`BR-COST-012`) |
| Số món chính đưa ra | main_offered | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Mặc định 3 | `BR-MENU-001` |
| Số món chính được chọn | main_pick | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Mặc định 1 [D-04] | Không áp dụng |
| Số món phụ | side_count | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | ≥ 0 | `BR-MENU-005` |
| Có rau | has_veg | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | `BR-MENU-004` |
| Có canh | has_soup | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | `BR-MENU-004` |
| Công khai | is_public | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định FALSE | Hiện trên website [D-10] |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | `DRAFT`, `ACTIVE`, `INACTIVE` | Không áp dụng |

### 4.6 `menus`, `menu_days`, `menu_day_items`: Thực đơn kỳ

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | menus.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Loại suất | menus.meal_type_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `meal_types.id` | Không áp dụng | Không áp dụng |
| Công ty khách | menus.customer_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `customers.id` | Null = thực đơn chung của loại suất | Không áp dụng |
| Tuần bắt đầu | menus.week_start | DATE | Không áp dụng | Không | Không áp dụng | Là thứ Hai | Không áp dụng |
| Trạng thái | menus.status | VARCHAR | 24 | Không | Không áp dụng | `DRAFT`, `CHECKED`, `PENDING`, `APPROVED`, `PUBLISHED`, `WITHDRAWN` | `FEAT-013` |
| Điểm quy tắc | menus.rule_score | SMALLINT | Không áp dụng | Có | Không áp dụng | 0–100 | 100 trừ điểm phạt quy tắc mềm |
| Nguồn tạo | menus.source | VARCHAR | 24 | Không | Không áp dụng | `MANUAL`, `AGENT_INTERNAL`, `AGENT_CUSTOMER` | Không áp dụng |
| Lượt chạy agent | menus.agent_run_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `agent_runs.id` | Không áp dụng | Truy vết thực đơn do AI tạo |
| Người duyệt | menus.approved_by | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Khác `created_by` | BN-17 |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`meal_type_id`, `customer_id`, `week_start`) với bản không huỷ | Không áp dụng |
| Mã ngày | menu_days.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Thực đơn | menu_days.menu_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `menus.id` | Không áp dụng | Không áp dụng |
| Ngày phục vụ | menu_days.service_date | DATE | Không áp dụng | Không | Không áp dụng | Unique cùng `menu_id` | Không áp dụng |
| Món mặc định | menu_days.default_dish_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `dishes.id` | Phải là một món `MAIN` của ngày; bắt buộc trước khi công bố | [D-14] |
| Cost theo cơ sở | `menu_cost_snapshots` | Quan hệ | Không áp dụng | Không áp dụng | FK → `menu_days.id` | Một bản/ngày/cơ sở/vòng duyệt | Thay `menu_days.cost_pct` từ v0.3.0; không còn số cost duy nhất cho cả ngày |
| Mã dòng | menu_day_items.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Ngày | menu_day_items.menu_day_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `menu_days.id` | Không áp dụng | Không áp dụng |
| Món | menu_day_items.dish_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `dishes.id` | `status` = `ACTIVE` | Không áp dụng |
| Công thức | menu_day_items.recipe_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `recipes.id` | Phiên bản hiệu lực tại ngày phục vụ | Chụp lại để cost không đổi khi công thức đổi sau |
| Vị trí | menu_day_items.slot | VARCHAR | 24 | Không | Không áp dụng | `MAIN`, `SIDE`, `VEG`, `SOUP`; khớp `dishes.role` | Không áp dụng |
| Thứ tự | menu_day_items.sort_order | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |

### 4.7 `menu_rules` và `menu_rule_results`: Bộ kiểm quy tắc

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã quy tắc | menu_rules.code | VARCHAR | 16 | Không | PK | `BR-MENU-xxx`, `BR-COST-xxx` | Khớp bảng quy tắc |
| Loại | menu_rules.rule_type | VARCHAR | 24 | Không | Không áp dụng | `HARD`, `SOFT` | Cứng chặn, mềm trừ điểm |
| Điểm phạt | menu_rules.penalty | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | 0 với `HARD`; 1, 2, 3 với `SOFT` | Nhẹ / vừa / nặng |
| Tham số | menu_rules.params | JSON | Không áp dụng | Có | Không áp dụng | Ví dụ `{"max_consecutive_days": 2}` | Con số được duyệt ở DL-01; đổi không cần sửa mã |
| Đang áp dụng | menu_rules.is_active | BOOLEAN | Không áp dụng | Không | Không áp dụng | Mặc định TRUE | Quy tắc bị đánh dấu "bỏ" khi duyệt |
| Mã kết quả | menu_rule_results.id | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Thực đơn | menu_rule_results.menu_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `menus.id` | Không áp dụng | Không áp dụng |
| Ngày | menu_rule_results.menu_day_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `menu_days.id` | Null với quy tắc cấp tuần | Không áp dụng |
| Quy tắc | menu_rule_results.rule_code | VARCHAR | 16 | Không | FK → `menu_rules.code` | Không áp dụng | Không áp dụng |
| Đạt | menu_rule_results.passed | BOOLEAN | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Chi tiết | menu_rule_results.detail | VARCHAR | 500 | Có | Không áp dụng | Không áp dụng | Ví dụ "Thịt lợn xuất hiện 3 ngày liền: T2, T3, T4" |
| Lý do chấp nhận | menu_rule_results.waiver_reason | VARCHAR | 500 | Có | Không áp dụng | Bắt buộc với quy tắc mềm–nặng không đạt | Không áp dụng |

Kết quả kiểm được tính lại và ghi đè mỗi lần thực đơn thay đổi khi còn ở trạng thái `DRAFT`; đóng băng từ `APPROVED`.

---

