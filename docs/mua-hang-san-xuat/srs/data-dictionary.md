---
id: DOC-E11-SRS-DATA-DICTIONARY-MD
title: Từ điển dữ liệu và delta đề xuất E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Từ điển dữ liệu và delta đề xuất E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Đối chiếu schema hiện hành

[Schema 65 bảng](../../nen-tang/srs/schema.dbml) có kitchens, users, suppliers, ingredients, recipes, recipe_items, menus, cost_estimates, cost_estimate_lines, ingredient_prices, files, approvals và audit_logs. [ERD mục 7](../../nen-tang/srs/erd.md) mới nêu khung purchase_orders, goods_receipts, stock_lots, production_plans; chúng chưa là bảng vật lý trong DBML. Không coi ERD khung là hợp đồng triển khai.

## Trường chung cho thực thể đề xuất

Tên physical dưới đây chỉ là đề xuất để review, chưa migration. Không thêm bảng/trường vào schema nguồn.

| Logical | Physical đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Mã | id | Id | Theo E1 | Không | PK đề xuất | Cấp bởi hệ thống; chưa chọn kiểu mới | Định danh |
| Cơ sở | kitchen_id | Id | Theo E1 | Không | FK logic kitchens | Scope từ quyền hiện tại | Không tin cơ sở client tự khai |
| Ngày phục vụ | service_date | Date | ISO date | Tùy thực thể | — | Không mặc định hôm nay | Tách ngày nhận và ngày phục vụ |
| Phiên bản | version | Integer | Chờ contract | Không | — | Token kiểm khi ghi | Không tráo revision nguồn |
| Nguồn | source_refs | Reference[] | Chờ contract | Không | FK logic | Giữ loại, id, revision nguồn | Thiếu thì BLOCKED |
| Lượng | quantity | Decimal string | Chờ độ chính xác | Có khi chưa biết | — | Kèm unit; không âm; null không là 0 | Không cộng kg với suất |
| Giá nguồn | quoted_unit_price | Decimal string | Theo PriceInput E3 | Có khi thiếu | — | Không dùng trực tiếp tính cost | Giá báo |
| Cơ sở giá | price_basis | Enum | Theo E3 | Có khi thiếu | — | INCLUSIVE / EXCLUSIVE / FINAL_CONFIRMED | Không dùng UNKNOWN như đã chuẩn hóa |
| VAT | vat_rate_pct / vat_unit_amount | Decimal string | Theo E3 | Theo basis | — | EXCLUSIVE cần đúng một căn cứ hợp lệ | Không tự mặc định 0 |
| Giá cost | effective_cost_unit_price | Integer money | Theo E3 | Có khi chưa xác định | — | Server chuẩn hóa gồm VAT; phần lẻ chờ | Không nhận số tin cậy từ client |
| Nguồn giá | pricing_evidence | Text/reference | Theo E3 | Không khi xác định giá | — | Giữ chứng từ/xác nhận | Không suy từ cờ hóa đơn |
| Tệp | file_ref | Id | Theo E1 | Có ở bản nháp | FK logic files | Quyền theo chủ thể, không public URL | Ảnh chứng từ |
| Trạng thái | status | Enum | Theo states | Không | — | DRAFT khi tạo nháp | Không suy được duyệt |
| Người/thời điểm | actor_id / recorded_at | Id / Timestamp | Theo E1 | Không khi ghi | FK logic users | Do phiên/server xác định | Audit |
| Lý do | reason | Text | Theo E1 / chờ Q13 | Không khi sửa số | — | Không ghi đè lịch sử | Căn cứ thay đổi |

## Thực thể đề xuất và trường riêng

| Thực thể logic / physical đề xuất | Trường riêng (kiểu; null; khóa/ràng buộc) | Nguồn / sử dụng / gate |
| :--- | :--- | :--- |
| demand / purchase_demands | planRef, estimateRef (Reference; không null khi tính); lines (Array); grossQty (Decimal); netBuyQty (Decimal nullable) | FR-PUR-DEM-001; Q01 và CG06; netBuyQty chưa tính |
| purchaseOrder / purchase_orders | supplierId (Id; bắt buộc khi lưu); demandRef (Reference); lines (Array không rỗng); approvalRef (Reference nullable) | FR-PUR-POD-001/POG; Q02; NCC do người lập chọn |
| lotScope / stock_lots | ingredientId (Id); storageType (Enum FROZEN/DRY); lotCode/expiry (chưa đặc tả theo Q03) | Chỉ ranh giới, không bắt buộc lô hàng tươi |
| goodsReceipt / goods_receipts | purchaseOrderRef (Reference); receivedQty, acceptedQty (Decimal; không âm; accepted ≤ received); receivedAt (Timestamp) | Q04; nhận nhiều lần không ghi đè lần cũ |
| receiptEvidence / receipt_evidence | receiptRef, fileRef (Reference; không null; unique logic cặp tham chiếu đề xuất) | Q05/Q13; liên kết không xác nhận giá |
| supplierBalance / supplier_balance_views | opening, obligations, payments, adjustments, closing (Decimal nullable); completeness (Enum) | Projection đọc; nguồn ghi nhận/kỳ Q06; không tạo sổ cái |
| comparison / purchase_comparisons | estimateRef, allocationRefs, measurementBasisRef (Reference); estimatedPct, actualPct, deltaPp (Decimal nullable) | Q07/08; ngày và cơ sở cùng phạm vi |
| comparisonLine / purchase_comparison_lines | ingredientId, estimateLineRef, receiptLineRef (Reference); quantity/unit/price hai phía | Không tự phân bổ hoặc sửa snapshot |
| productionShift / production_shifts | shiftRef, planRef (Reference); assignments (Array mã nhân sự/công việc) | Q09/CG06; không timestamp bắt đầu E6 tự sinh |
| qualityCheck / pre_delivery_checks | shiftRef, checklistRef (Reference); results (mục/kết quả/chứng cứ) | Q10; chưa định nghĩa checklist thực |
| retainedSample / retained_samples | mealRef (Reference); sampleCode (Text); evidenceRef (Reference nullable ở nháp) | Q11; chưa có hạn lưu/lượng mẫu/nhiệt độ |
| substitution / substitution_candidates | menuRef, menuVersion, originalDishId, replacementDishId, role (Reference/Enum); reason | Cùng vai trò; Q12; không ghi menu công bố |
| substitutionCheck / substitution_checks | candidateRef, candidateVersion; allergenResultRef, ruleResultRef, costResultRef (Reference nullable khi thiếu) | Ba kiểm đúng nguồn; thiếu một thì BLOCKED |


Mọi độ dài/precision chưa có nguồn đều chờ E11-Q13, không tự lấy từ mẫu. Giữ nguyên invoiceRequested riêng và khoản chiết khấu theo đơn ở E3/E6; không sao chép hồ sơ sức khỏe. Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02/R11 dùng ≤ 3 điểm phần trăm, không phải sai số tính toán. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chặn O-03, không thu dữ liệu sức khỏe.
