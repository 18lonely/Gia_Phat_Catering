---
id: DOC-E10-SRS-DATA-DICTIONARY-MD
title: Từ điển dữ liệu và đề xuất E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Từ điển dữ liệu và đề xuất E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

[Schema 65 bảng](../../nen-tang/srs/schema.dbml) được đọc, không sửa. Không có bảng contracts, quotes, opportunities hay contacts đã được chứng minh trong schema hiện tại. Tên dưới chỉ là **đề xuất**, chưa quyết định số bảng vật lý, không DDL/migration.

## Nguồn hiện hữu

| Thực thể / trường | Kiểu / độ dài / null / khóa | Ý nghĩa / ràng buộc |
| :--- | :--- | :--- |
| customers.id/code/name/tax_code/lifecycle_status/version | bigint PK; varchar 32 unique; varchar 200; varchar 14 nullable; varchar 24; int | Mã khách chủ; không E10 tự tạo/thay quyền sở hữu CG08. lifecycle_status có bảy giá trị theo states. |
| service_points.customer_id/kitchen_id/name/address | bigint FK; bigint FK; varchar 160; varchar 255; không null | Điểm thuộc khách và cơ sở; E10 đọc theo scope, không đổi master. |
| service_schedules.service_point_id/shift/weekday | bigint FK; varchar 16; tinyint 1–7; unique bộ ba | Chưa có đủ mô hình ngoại lệ/nghỉ/hiệu lực theo kỳ; không suy thứ trong tuần là lịch đủ cho churn. |
| customer_price_terms.customer_id/meal_type_id/quoted_unit_price | bigint FK; bigint FK; decimal(18,6), không null | Nguồn giá hiện hữu; phạm vi không chồng ACTIVE theo customer + mealType. |
| customer_price_terms.effective_from/effective_to | date không null / date nullable | Có từ–đến; null chưa tự nghĩa vô hạn nếu Q11 chưa duyệt. |
| customer_price_terms.sale_price_basis/vat_rate_pct/invoice_requested | varchar 24; decimal(9,6) nullable; boolean nullable | INCLUSIVE/EXCLUSIVE/FINAL_CONFIRMED/UNKNOWN; null khác 0; invoice=false không là VAT 0. |
| customer_price_terms.status/version | varchar 24 DRAFT/ACTIVE/CANCELLED; int | Kích hoạt đang gate sales policy; E10 không coi đã có workflow hợp đồng. |
| order_pricing_snapshots.order_id/order_version/price_term_id | bigint; int; FK nullable; unique(order_id,order_version) | Bản chụp bất biến của nguồn; E10 không ghi ngược sau phụ lục hoặc gộp. |
| audit_logs.actor_user_id/changes/reason/request_id | FK không null; JSON; varchar 500; char 36 | Audit bất biến; action gộp/hoàn tác cần mapping được duyệt, không tự thêm enum vào schema. |

## Cấu trúc đề xuất

Mọi mã đề xuất truyền API dưới dạng chuỗi; khóa nội bộ và độ dài vật lý cuối chờ Q13. Không tự gán UUID hoặc khóa số cho bảng chưa được duyệt. Với trường string chưa có giới hạn nguồn, giới hạn cụ thể BLOCKED Q01/Q13; không triển khai kiểm runtime bằng số tùy ý.

| Tên đề xuất | Trường logic | Kiểu / null / khóa | Ràng buộc |
| :--- | :--- | :--- | :--- |
| crm_contact_drafts | id, customerRef, displayName, contactRole, channels, sourceEvidenceRef, version | Id PK; customer FK logic; string; object theo Q01; Id; int; required theo policy | Chỉ nháp liên hệ; không đồng bộ master khi CG08 mở. |
| crm_intakes | id, sourceSystem, sourceRef, sourceRevision, sourceHash, safeMenuRef, contactRef, consentRef, receiptRef | Id PK; strings required; safeMenuRef nullable; consent/contact theo nguồn | Unique(sourceSystem,sourceRef,sourceRevision); khác hash cùng khóa là xung đột; không raw chat. |
| crm_merge_reviews/events | id, leftRef, rightRef, versions, fieldChoices, beforeImage, linkMap, decisionRef, reversalOf | Id; hai FK khách; JSON có schema; decisionRef nullable khi nháp; reversalOf nullable | Không xóa nguồn; ảnh trước có scope và quyền; quyết định/hoàn tác bất biến. |
| crm_lifecycle_events/risk_evaluations | customerRef, previousState, nextState, evidenceRef, scheduleRefs, evaluationRef, completeness | FK; enum theo states; Id[]; state | Lịch ngoại lệ và ngưỡng chưa có; không lấy thiếu dữ liệu thành zero. |
| sale_opportunities/events | id, customerOrIntakeRef, ownerRef, stage, evidenceRef, version | Id PK; FK logic; stage theo Q07; evidence nullable ở nháp | Một cơ hội nhiều báo giá; lịch sử sự kiện không ghi đè. |
| sale_quote_revisions/publications | quoteRef, revisionNo, version, baseRevision, lines, terms, attachments, contentHash, publishedProjection | Id; int; int; FK logic nullable; JSON có schema; hash; projection nullable trước phát hành | Unique(quoteRef,revisionNo); revision đã phát hành bất biến; cost tách riêng. |
| sale_contracts/amendments | id, customerRef, quoteRevisionRef, legacyEvidenceRef, signatureEvidenceRef, predecessorRef, status, version | Id PK; FK; quote/legacy ít nhất một nguồn; signature nullable khi nháp; predecessor nullable cho bản đầu | Hợp đồng nhiều phụ lục; phụ lục nhiều dòng loại suất; liên kết nguồn không mất khi gộp. |
| sale_contract_price_links / hiệu lực lịch sử | contractRef, amendmentRef, priceTermRef, predecessorTermRef, effectiveFrom, effectiveTo, approvalRef | FK logic; date/date nullable theo Q11; approval nullable trước duyệt | Đề xuất nối vào customer_price_terms; không tự tạo bảng giá cạnh tranh. Mọi thay khoảng có lịch sử và quyết định Q12. |

Quan hệ: customer → nhiều contact/điểm/cơ hội/hợp đồng; opportunity → nhiều quote, quote → nhiều revision; contract → nhiều amendment → nhiều price line theo loại suất; merge event nối hồ sơ và reversal. Không có FK từ E10 tới hồ sơ sức khỏe. [Mapping](../api/data-mapping.md).
