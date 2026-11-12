---
id: DOC-E13-SRS-DATA-DICTIONARY-MD
title: Từ điển dữ liệu đề xuất E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Từ điển dữ liệu đề xuất E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

Schema nền giữ **65 bảng**. Không tạo DBML, SQL hay migration. Tên physical dưới đây chỉ đề xuất, không khẳng định bảng đã tồn tại. kitchens, customers và users đã có trong nền; chấm công không tự coi personRef là users.id. E7/E11 dùng tham chiếu logic, không giả có bảng vật lý.

Mọi thực thể đề xuất có id BIGINT UNSIGNED (20 chữ số tối đa, PK, không null), version INTEGER (không null), createdBy/createdAt và auditRef (không null); Khóa mới đề xuất kế thừa BIGINT UNSIGNED của nền; API truyền định danh dạng chuỗi để không mất chính xác. Trường liệt kê là enum logic, physical đề xuất VARCHAR(24) + CHECK theo nền, không phải MySQL ENUM. Thời điểm lưu UTC, ngày nghiệp vụ theo giờ Việt Nam; biên kỳ cụ thể vẫn chờ Q02. Độ dài trường chưa có căn cứ và lưu trữ chi tiết chờ Q12. Các trường lương không vào log thông thường. Không chọn precision hoặc retention từ ví dụ.

## expense_periods

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| kitchen ref | kitchen_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK kitchens | Scope cơ sở |
| from date / to date | from_date / to_date | DATE | — | Không | — | Biên ngày chờ Q02 |
| status | status | ENUM | — | Không | — | OPEN / LOCKED |
| locked snapshot ref | locked_snapshot_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK đề xuất | Bắt buộc khi khóa |

## expense_entries

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| period ref | period_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Kỳ mở |
| type version ref | type_version_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Danh mục Q01 chưa chọn |
| amount | amount | DECIMAL | Chờ Q09 | Không | — | Tiền có đơn vị và căn cứ; không float |
| customer ref | customer_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK customers | Bắt buộc với trực tiếp; null với chung |
| source key / evidence ref | source_key / evidence_ref | STRING | Chờ Q12 | Không | Unique scope | Chống trùng với E3/E11 |

## attendance_sheets

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| person ref | person_ref | STRING | Chờ Q03 | Không | Tham chiếu nguồn | Không mặc định người lao động có tài khoản users |
| shift revision ref | shift_revision_ref | STRING | Chờ E11 | Không | Nguồn E11 | Phân ca không chứng minh đã làm |
| kitchen ref / work date | kitchen_ref / work_date | BIGINT UNSIGNED / DATE | 20 chữ số / — | Không | FK kitchens | Theo cơ sở/ca |
| hours | hours | DECIMAL | Chờ Q03 | Có | — | Null khi thiếu; 0 chỉ khi có xác nhận 0 giờ |
| evidence ref / status | evidence_ref / status | STRING / ENUM | Chờ Q03 | Không | — | DRAFT / SUBMITTED / CONFIRMED / RETURNED |

## labor_cost_refs

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| attendance version ref | attendance_version_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Bản công xác nhận |
| rate version ref / payroll amount ref | rate_version_ref / payroll_amount_ref | STRING | Chờ Q04 | Có | Nguồn lương | Một cách tính được duyệt; không cộng hai nguồn |
| amount | amount | DECIMAL | Chờ Q09 | Có | — | Null nếu thiếu nguồn; dữ liệu nhạy cảm |

## allocation_method_versions

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| method ref / revision | method_ref / revision | BIGINT UNSIGNED / INTEGER | 20 chữ số / — | Không | Unique cặp | Phiên bản bất biến sau duyệt |
| proposed basis / driver definition refs | proposed_basis / driver_definition_refs | JSON | Chờ Q05 | Có | — | Dữ liệu mô tả; không có default hoặc code thực thi |
| scope / effective range | scope / effective_range | JSON | Chờ Q05 | Không | — | Cơ sở/kỳ; không tự xử lý chồng hiệu lực |
| status | status | ENUM | — | Không | — | DRAFT / SUBMITTED / APPROVED / RETURNED |
| approver ref / approved at / approval evidence ref / content hash | approver_ref / approved_at / approval_evidence_ref / content_hash | BIGINT UNSIGNED / TIME / STRING | Chờ Q12 | Có | Tham chiếu duyệt | Bắt buộc đủ khi APPROVED; khác lập/sửa cuối |

## profit_runs

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| period snapshot ref / source manifest ref | period_snapshot_ref / source_manifest_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Cùng phạm vi, nguồn có version |
| method version ref | method_version_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK đề xuất | Null chỉ khi BLOCKED vì chưa có duyệt |
| status / blocked reasons | status / blocked_reasons | ENUM / JSON | — | Không | — | DRAFT / BLOCKED / READY / RECONCILED |
| facility result ref / definition version ref | facility_result_ref / definition_version_ref | STRING | Chờ Q08 | Có | Nguồn chuẩn | Không dùng tổng khách tự tạo làm số chuẩn |
| customer results / unallocated effect / reconciliation delta | customer_results / unallocated_effect / reconciliation_delta | JSON / DECIMAL | Chờ Q09 | Có | — | Null nếu BLOCKED; tách từng cơ sở/khách; không gộp thiếu nguồn |

## expense_adjustments

| Tên logic | Cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| original entry ref / locked snapshot ref | original_entry_ref / locked_snapshot_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Giữ nguồn gốc bất biến |
| adjustment amount / target period ref | adjustment_amount / target_period_ref | DECIMAL / BIGINT UNSIGNED | Chờ Q09/10 | Có | FK đề xuất | Dấu tăng/giảm; kỳ đích chưa chọn |
| reason / evidence ref / approver ref | reason / evidence_ref / approver_ref | STRING / BIGINT UNSIGNED | Chờ Q10 | Có | — | Bắt buộc đủ trước POSTED |
| status | status | ENUM | — | Không | — | PENDING / REJECTED / POSTED |

Danh mục loại chi phí có version/effectiveRange/decisionRef đề xuất kèm Q01, chưa điền loại thực tế. Manifest nguồn tối thiểu gồm producer, sourceRef, revision/hash, kitchenRef, periodRange, customerRef nếu có, kind (dự toán/thực mua/doanh thu đối soát), completeness và capturedAt. Không dùng estimate thay actual.
