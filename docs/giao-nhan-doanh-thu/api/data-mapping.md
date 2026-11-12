---
id: DOC-E7-API-DATA-MAPPING-MD
title: Mapping API → schema hiện có → UI
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Mapping API → schema hiện có → UI

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

Nguồn [DBML65 bảng](../../nen-tang/srs/schema.dbml) và [ERD nền](../../nen-tang/srs/erd.md), [delta E6](../../chon-mon-order/srs/data-dictionary.md). Tên cột hiện hữu dưới đây đã đối chiếu; bảng/cột E7 chưa tồn tại, chỉ delta đề xuất. Không migration/merge.

| API logical field | Schema hiện có / delta đề xuất | UI | Chuyển đổi / gate |
| :--- | :--- | :--- | :--- |
| customerId | customers.id; service_points.customer_id | 01/04/05 | Resolve qua điểm/order; không tin client; CG08 |
| servicePointId / kitchenId | orders.service_point_id → service_points.id/kitchen_id | 01 | FK hiện hữu không chứng minh scope đã cấp; CG08 |
| serviceDate / shift | orders.service_date / shift | 01 | Ngày nghiệp vụ Asia/Ho_Chi_Minh; không default ca E7 từ DB |
| orderedServings | orders.total_servings; bản khóa tại delta order_revisions E6 | 01/03 | Suất, không tổng dòng món; thiếu nguồn không0; CG03/05 |
| orderVersion | orders.version; order_pricing_snapshots.order_version | 01/04 | Phân biệt version live và version chụp; CG04/05 |
| orderRevisionRef | Delta E6 order_revisions.id/revision_no, chưa trong65 bảng | 01/04 | Opaque source ref; không tự xác định revision hiện hành; CG04/05/07 |
| planRevisionRef | Delta E6 production_plan_revisions; chưa trong65 bảng | 01 | Không bằng order revision; không suy READY là được giao; CG06 |
| pricingSnapshotId | order_pricing_snapshots.id/order_id/order_version | 04 | Cùng order và version với nguồn; không chọn snapshot mới nhất tùy ý |
| quotedUnitPrice / salePriceBasis | order_pricing_snapshots.quoted_unit_price / sale_price_basis | 04 | VND decimal; giá tại order, không đọc giá hiện tại |
| vatRatePct / invoiceRequested | order_pricing_snapshots.vat_rate_pct / invoice_requested | 04 | Null khác0; invoice=false không đổi VAT |
| pricingContextStatus | order_pricing_snapshots.context_status | 04 | UNRESOLVED/LEGACY_UNVERIFIED không biến RESOLVED bằng mock |
| originalAmountDue / originalRevenueExVat | order_pricing_snapshots.gross_amount_due / revenue_ex_vat | 04 | Số gốc từ snapshot; KHÔNG ghi đè khi E7 xác định số tính tiền khác |
| discountSeparate | order_discount_records.calculated_amount/status/pricing_snapshot_id | 04 nội bộ | Khoản riêng; không giảm E7 amountDue hoặc suy đã chi; CK giữ mở |
| deliveredServings / receivedServings | Delta e7_delivery_notes/e7_receipt_confirmations | 01/02/03 | Suất nguyên≥0; received chưa biết không0; zero nghiệp vụ Q02/Q13 |
| billableServings / basisEvidenceRef | Delta e7_revenue_snapshots | 04 | Căn cứ E7-Q03; không mặc định ordered/delivered/received hoặc pricing.servings |
| grossAmountDue / revenueExVat | Delta e7_revenue_snapshots | 04/05 | Tính từ căn cứ và giá chụp; rounding E7-Q04; không giảm vì CK |
| periodId / sourceRevision / totals | Delta e7_reconciliation_periods/lines | 05/07 | Snapshot kỳ có lineage; nguồn thiếu gắn gate, không bỏ dòng |
| receiptAmount / receiptEvidenceRef | Delta e7_cash_receipts; files.id cho bằng chứng | 06 | Tiền dương VND, chứng từ theo scope; phân bổ/dup Q06/08 |
| reopenRequest / decision | change_requests/approvals hiện hữu + delta liên kết kỳ | 07 | Reuse cần review entity/snapshot/type, không khẳng định đã hỗ trợ E7 |
| actor / audit / attachment | users.id, audit_logs, files.id | Mọi màn có quyền | Actor guest chưa có audit binding CG01; không tạo người giả |
| templateRef / exportSourceRevision / fileRef | Delta e7_export_runs; files.id nếu file được tạo | 08 | Chưa mapping cột MISA; định dạng/file bytes BLOCKED Q07 |

API đọc bổ sung014–018 dùng cùng mapping, không tạo dữ liệu. DTO tiền dùng chuỗi decimal đề xuất, số suất int; ID chuỗi. Kiểu/length/nullability wire chi tiết E7-Q08 chưa freeze. Không serialize inputs_snapshot/secret/cost vào projection khách.
