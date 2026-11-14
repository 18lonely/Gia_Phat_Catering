---
id: DOC-NEN-TANG-SRS-DATA-DICTIONARY
title: Từ điển dữ liệu E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-dictionary, e1]
author: BA
last_updated: 2026-11-16
---
# Từ điển dữ liệu E1: Nền tảng (AUTH, SYS)

Draft · 16/11/2026 · Thiết kế đề xuất, chưa migration.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách nguyên văn phần từ điển của E1 ra khỏi ERD theo khuôn chung các epic. Không đổi bảng, cột hay ràng buộc |

Sơ đồ quan hệ vẫn ở [ERD](erd.md); schema chung là [DBML 65 bảng](../../nen-tang/srs/schema.dbml). Các tiêu đề mục giữ số mục cũ của nơi gốc để đối chiếu.

## Phần chuyển từ [ERD tổng](erd.md)

### 3.1 `users`: Tài khoản

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã tài khoản | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | AUTO_INCREMENT | Không áp dụng |
| Loại định danh | user_type | VARCHAR | 24 | Không | Không áp dụng | `STAFF`, `CUSTOMER`, `EATER`, `SERVICE` | 4 loại theo SRS mục 2.3 |
| Tên đăng nhập | username | VARCHAR | 64 | Không | Unique | Dạng tên: [N-01] | Không áp dụng |
| Mật khẩu đã băm | password_hash | VARCHAR | 255 | Có | Không áp dụng | Argon2id; null với `SERVICE` | `NFR-SEC-002` |
| Họ tên | full_name | VARCHAR | 120 | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Số điện thoại | Điện thoại | VARCHAR | 15 | Có | Không áp dụng | Không áp dụng | Không áp dụng |
| Email | email | VARCHAR | 255 | Có | Không áp dụng | Không áp dụng | Không áp dụng |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | Mặc định `PENDING_PASSWORD`; `ACTIVE`, `TEMP_LOCKED`, `LOCKED` | Sơ đồ trạng thái ở SRS 4.1 |
| Số lần sai liên tiếp | failed_attempts | TINYINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Mặc định 0 | `BR-SEC-002` |
| Khoá tạm đến | locked_until | DATETIME(3) | Không áp dụng | Có | Không áp dụng | Không áp dụng | `BR-SEC-002` |
| Hạn mật khẩu tạm | temp_password_expires_at | DATETIME(3) | Không áp dụng | Có | Không áp dụng | Không áp dụng | `BR-SEC-004` |
| Công ty khách | customer_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `customers.id` | Bắt buộc khi `user_type` là `CUSTOMER`, `EATER` | Phạm vi dữ liệu theo công ty |

### 3.2 `user_roles`: Vai trò và phạm vi

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Tài khoản | user_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `users.id` | Không áp dụng | Không áp dụng |
| Vai trò | role_code | VARCHAR | 24 | Không | Không áp dụng | `GIAM_DOC`, `DINH_DUONG_VIEN`, `QL_CO_SO`, `BEP_TRUONG`, `KT_MUA_HANG`, `KT_DOANH_THU`, `QUAN_TRI`, `NGUOI_DAT_TONG`, `NGUOI_NHAN`, `NGUOI_AN` | Danh sách vai trò cố định |
| Cơ sở | kitchen_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `kitchens.id` | Bắt buộc với `QL_CO_SO`, `BEP_TRUONG` | `BR-SEC-007` |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`user_id`, `role_code`, `kitchen_id`) | Không áp dụng |

### 3.3 `audit_logs`: Nhật ký thay đổi

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Thời điểm | occurred_at | DATETIME(3) | Không áp dụng | Không | Không áp dụng | Chỉ mục | Không áp dụng |
| Người thực hiện | actor_user_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `users.id` | Không áp dụng | Có thể là tài khoản dịch vụ |
| Thay mặt | on_behalf_user_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Không áp dụng | Người dùng đang dùng agent |
| Thực thể | entity | VARCHAR | 48 | Không | Không áp dụng | Chỉ mục cùng `entity_id` | Tên bảng nghiệp vụ |
| Mã bản ghi | entity_id | BIGINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Hành động | action | VARCHAR | 24 | Không | Không áp dụng | `CREATE`, `UPDATE`, `CANCEL`, `APPROVE`, `REJECT`, `PUBLISH`, `LOCK`, `REOPEN` | Không áp dụng |
| Thay đổi | changes | JSON | Không áp dụng | Có | Không áp dụng | Mảng `{field, old, new}` | Giá trị cũ → mới |
| Lý do | reason | VARCHAR | 500 | Có | Không áp dụng | ≥ 10 ký tự với thao tác ở `BR-AUD-001` | Không áp dụng |
| Mã yêu cầu | request_id | CHAR | 36 | Không | Không áp dụng | Không áp dụng | Nối với log ứng dụng |

Bảng này không có các cột chuẩn `updated_*`, `cancelled_*`; tài khoản MySQL của ứng dụng chỉ có `INSERT`, `SELECT` (`BR-AUD-002`). Phân vùng theo tháng của `occurred_at`; thời gian lưu: [N-03].

### 3.4 `parameters`: Tham số

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | Không áp dụng | Không áp dụng |
| Mã tham số | Mã nghiệp vụ | VARCHAR | 48 | Không | Không áp dụng | Danh mục ở SRS 4.3 | Không áp dụng |
| Loại phạm vi | scope_type | VARCHAR | 24 | Không | Không áp dụng | `GLOBAL`, `KITCHEN`, `CUSTOMER`, `SERVICE_POINT` | Không áp dụng |
| Mã phạm vi | scope_id | BIGINT UNSIGNED | Không áp dụng | Có | Không áp dụng | Null khi `GLOBAL` | Không áp dụng |
| Giá trị | value | VARCHAR | 255 | Không | Không áp dụng | Kiểm theo kiểu của tham số | Không áp dụng |
| Hiệu lực từ | effective_from | DATE | Không áp dụng | Không | Không áp dụng | ≥ ngày tạo (`BR-SYS-001`) | Không áp dụng |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | `PENDING`, `APPROVED`, `REJECTED` | `FR-SYS-PRM-002` |
| Người duyệt | approved_by | BIGINT UNSIGNED | Không áp dụng | Có | FK → `users.id` | Khác `created_by` | `BR-SEC-008` |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`code`, `scope_type`, `scope_id`, `effective_from`) | Không áp dụng |

`sessions`, `login_logs`, `delegations`, `notifications`, `files`, `agent_runs`, `kitchens`: cấu trúc như sơ đồ; từ điển đầy đủ bổ sung khi thiết kế kỹ thuật R1.

### 3.5 `change_requests` và `approvals`: Đề nghị thay đổi và lượt duyệt (thêm ở v0.2.0)

Hai bảng dùng chung cho mọi phân hệ, không gắn khoá ngoại cứng tới bảng nghiệp vụ (tham chiếu bằng cặp `entity` + `entity_id`, giống `audit_logs`).



**`change_requests`**: giá trị đề nghị cho một bản ghi đang hiệu lực, chờ duyệt. Bản ghi gốc giữ nguyên giá trị cũ cho đến khi đề nghị được duyệt.

Dùng cho: sửa thuộc tính ảnh hưởng quy tắc của món `ACTIVE` (`FR-MENU-DISH-002`); sửa danh mục quy tắc (`FR-MENU-RUL-006`). Các epic sau dùng lại cho mọi trường hợp "sửa bản ghi đang hiệu lực cần duyệt".

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | AUTO_INCREMENT | Không áp dụng |
| Thực thể | entity | VARCHAR | 48 | Không | Không áp dụng | Ví dụ `dishes`, `menu_rules` | Tên bảng nghiệp vụ |
| Khoá bản ghi | entity_key | VARCHAR | 32 | Không | Không áp dụng | Không áp dụng | `id` dạng chuỗi, hoặc `code` với bảng có khoá chính là mã (`menu_rules`) |
| Thay đổi đề nghị | proposed_changes | JSON | Không áp dụng | Không | Không áp dụng | Mảng `{field, old, new}` | `old` là giá trị lúc đề nghị, để phát hiện bản ghi gốc đã đổi |
| Lý do | reason | VARCHAR | 500 | Không | Không áp dụng | ≥ 10 ký tự | `BR-AUD-001` |
| Trạng thái | status | VARCHAR | 24 | Không | Không áp dụng | Mặc định `PENDING`; `APPROVED`, `REJECTED`, `WITHDRAWN`, `STALE` | `STALE` = bản ghi gốc đã đổi sau khi đề nghị, phải đề nghị lại |
| Người đề nghị | requested_by | BIGINT UNSIGNED | Không áp dụng | Không | FK → `users.id` | Không áp dụng | Không áp dụng |
| Thời điểm đề nghị | requested_at | DATETIME(3) | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Thời điểm áp dụng | applied_at | DATETIME(3) | Không áp dụng | Có | Không áp dụng | Không áp dụng | Lúc giá trị mới được ghi vào bản ghi gốc |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Chỉ mục | (`entity`, `entity_key`, `status`) | Mỗi bản ghi có tối đa 1 đề nghị `PENDING`: kiểm ở tầng ứng dụng |

**`approvals`**: mỗi dòng là một quyết định của một người duyệt. Thay cho việc chỉ có một cột `approved_by`, để ghi được nhiều người duyệt (`BR-MNU-008`) và giữ lịch sử các lần trả lại.

| Tên trường | Tên cột | Kiểu | Độ dài | Null? | Khoá | Ràng buộc / Mặc định | Diễn giải nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | Mã bản ghi | BIGINT UNSIGNED | Không áp dụng | Không | PK | AUTO_INCREMENT | Không áp dụng |
| Thực thể | entity | VARCHAR | 48 | Không | Không áp dụng | Ví dụ `menus`, `recipes`, `dish_prices`, `change_requests` | Không áp dụng |
| Mã bản ghi | entity_id | BIGINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Vòng duyệt | round_no | SMALLINT UNSIGNED | Không áp dụng | Không | Không áp dụng | Mặc định 1; tăng mỗi lần gửi duyệt lại | Phân biệt các lần gửi duyệt của cùng bản ghi |
| Người duyệt | approver_user_id | BIGINT UNSIGNED | Không áp dụng | Không | FK → `users.id` | Khác người tạo và người sửa cuối của bản ghi (`BR-SEC-008`) | Không áp dụng |
| Duyệt thay | delegation_id | BIGINT UNSIGNED | Không áp dụng | Có | FK → `delegations.id` | Không áp dụng | Có giá trị khi người duyệt dùng quyền được uỷ (`FR-AUTH-RBAC-003`) |
| Quyết định | decision | VARCHAR | 16 | Không | Không áp dụng | `APPROVED`, `REJECTED` | Không áp dụng |
| Lý do | reason | VARCHAR | 500 | Có | Không áp dụng | Bắt buộc khi `REJECTED` | Không áp dụng |
| Thời điểm | decided_at | DATETIME(3) | Không áp dụng | Không | Không áp dụng | Không áp dụng | Không áp dụng |
| Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Unique | (`entity`, `entity_id`, `round_no`, `approver_user_id`) | Một người chỉ duyệt một lần mỗi vòng |

Hai bảng này không có cột chuẩn `updated_*`, `cancelled_*`: dòng `approvals` không sửa sau khi ghi; `change_requests` chỉ đổi `status` và `applied_at`.

**Quan hệ với các cột `approved_by` đã có.** Các cột `approved_by`, `approved_at` trên `dishes`, `recipes`, `dish_prices`, `menus`, `parameters`, `customer_quotas` được giữ, mang nghĩa **người duyệt cuối cùng làm bản ghi có hiệu lực**, để truy vấn nhanh. Nguồn đầy đủ là `approvals`. Hai nơi được ghi trong cùng một giao dịch.

**Số người duyệt cần có** của một thực đơn: 1, hoặc 2 khi điểm quy tắc < `QUY_TAC_DIEM_TOI_THIEU`. Thực đơn chuyển `APPROVED` khi số dòng `APPROVED` của vòng hiện tại đạt số cần có; một dòng `REJECTED` đưa thực đơn về `DRAFT`.

---

