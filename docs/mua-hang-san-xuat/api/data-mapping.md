---
id: DOC-E11-API-DATA-MAPPING-MD
title: "Mapping API, dữ liệu và màn E11"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Mapping API, dữ liệu và màn E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

Các tên physical đều là đề xuất trong [data dictionary](../srs/data-dictionary.md), không có migration. Mã và revision nguồn giữ riêng; ngày ISO chỉ là định dạng, không chốt quy tắc phân bổ theo ngày.

| API / FR | Trường API logic | Dữ liệu logic / physical đề xuất | Màn / nhãn | Chuyển đổi và thiếu nguồn |
| :--- | :--- | :--- | :--- | :--- |
| API-PUR-001 / FR-PUR-DEM-001 | planRef, planRevision, estimateRef, serviceDate, kitchenId | demand; xem trường chung và riêng trong từ điển | UI-PUR-01 / Lập nhu cầu nguyên liệu | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E6 CG06, ORD-Q10/14; E11-Q01 |
| API-PUR-002 / FR-PUR-POD-001 | demandRef, supplierId, lines, reason | purchaseOrder; xem trường chung và riêng trong từ điển | UI-PUR-02 / Lập đơn mua nháp | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q01/02/13/14 |
| API-PUR-003 / FR-PUR-POG-001 | purchaseOrderRef, version | purchaseOrder; xem trường chung và riêng trong từ điển | UI-PUR-02 / Kiểm cổng phát hành đơn mua | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q02; O-06 |
| API-PUR-004 / FR-PUR-LOT-001 | ingredientId, storageType, receiptRef | lotScope; xem trường chung và riêng trong từ điển | UI-PUR-03 / Kiểm phạm vi quản lý lô | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q03 |
| API-PUR-005 / FR-PUR-RCV-001 | purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason | goodsReceipt; xem trường chung và riêng trong từ điển | UI-PUR-03 / Ghi phiếu nhận hàng nháp | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q04/13 |
| API-PUR-006 / FR-PUR-DOC-001 | receiptRef, fileRef, version | receiptEvidence; xem trường chung và riêng trong từ điển | UI-PUR-04 / Gắn ảnh chứng từ vào phiếu | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q05/13; E1-Q01 |
| API-PUR-007 / FR-PUR-APV-001 | supplierId, kitchenId, fromDate, toDate | supplierBalance; xem trường chung và riêng trong từ điển | UI-PUR-05 / Xem công nợ nhà cung cấp | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q06/04 |
| API-PUR-008 / FR-COST-BUY-001 | estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef | comparison; xem trường chung và riêng trong từ điển | UI-PUR-06 / Đối chiếu dự toán và thực mua | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04 |
| API-PUR-009 / FR-COST-BEX-001 | comparisonRef, ingredientId | comparisonLine; xem trường chung và riêng trong từ điển | UI-PUR-06 / Giải thích nguồn chênh lệch | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q07/08/14 |
| API-PUR-010 / FR-PLAN-SHF-001 | kitchenId, serviceDate, shiftRef, assignments, planRef | productionShift; xem trường chung và riêng trong từ điển | UI-PUR-07 / Lập phân ca nháp | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q09; E6 CG06 |
| API-PUR-011 / FR-PLAN-QCG-001 | shiftRef, checklistRef, results, reason | qualityCheck; xem trường chung và riêng trong từ điển | UI-PUR-08 / Ghi kiểm tra trước giao | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q10; E7-Q02; E6 CG06 |
| API-PUR-012 / FR-PLAN-SMP-001 | mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef | retainedSample; xem trường chung và riêng trong từ điển | UI-PUR-08 / Ghi sổ mẫu lưu theo bữa | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q11; E6 CG06 |
| API-PUR-013 / FR-MENU-SUB-001 | menuRef, menuVersion, originalDishId, replacementDishId, reason | substitution; xem trường chung và riêng trong từ điển | UI-PUR-09 / Lập ứng viên món thay thế | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q12/15; O-02 |
| API-PUR-014 / FR-MENU-SCK-001 | candidateRef, candidateVersion, menuSourceRef | substitutionCheck; xem trường chung và riêng trong từ điển | UI-PUR-09 / Kiểm lại ứng viên thay món | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate DL-01; E11-Q15; O-01/O-02; CK/DATA-COST |
| API-PUR-015 / FR-MENU-SGT-001 | candidateRef, candidateVersion, checkRefs | substitution; xem trường chung và riêng trong từ điển | UI-PUR-09 / Kiểm cổng chuyển duyệt MENU | Id giữ dạng nguồn; Decimal dạng chuỗi; null là chưa biết. Gate E11-Q12/13; DL-01; E6 CG05/06/07 |

## Mapping trường trọng yếu

| API field | Dữ liệu đề xuất | UI | Quy tắc |
| :--- | :--- | :--- | :--- |
| serviceDate / kitchenId | service_date / kitchen_id | Ngày phục vụ / cơ sở | Không lấy ngày nhận làm ngày phục vụ; Q07 |
| planRef / planRevision | source_refs.plan | Nguồn nhu cầu / ca | Không GET tạo kế hoạch; CG06 |
| quotedUnitPrice / priceBasis | quoted_unit_price / price_basis | Giá báo / cách báo giá | Dùng PriceInput; không tự coi đã gồm VAT |
| vatRatePct / vatUnitAmount | vat_rate_pct / vat_unit_amount | Căn cứ VAT | EXCLUSIVE cần căn cứ, không suy từ cờ hóa đơn |
| effectiveCostUnitPrice | effective_cost_unit_price | Giá gồm VAT phải trả NCC | Server chuẩn hóa; không cộng VAT lần hai |
| receivedQty / acceptedQty | goods_receipts.lines | Thực nhận / chấp nhận | Decimal và cùng đơn vị, 0 ≤ accepted ≤ received |
| fileRef | receipt_evidence.file_ref | Ảnh nội bộ | Không lưu URL công khai, kiểm scope tệp |
| deltaPp | purchase_comparisons.delta_pp | Chênh điểm phần trăm | Không chênh tương đối; định nghĩa dấu và mẫu số Q08 |
| mealRef / sampleCode | retained_samples.meal_ref / sample_code | Bữa / mã mẫu | Đếm bữa phân biệt, mẫu hợp lệ Q11 |
| replacementDishId / role | substitution_candidates.replacement_dish_id / role | Món thay / vai trò | Cùng vai trò E2; kiểm lại ba nhóm đúng version |

