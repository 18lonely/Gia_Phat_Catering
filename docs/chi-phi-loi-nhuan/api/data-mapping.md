---
id: DOC-E13-API-DATA-MAPPING-MD
title: Mapping ba tầng EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Mapping ba tầng EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

| API field | Dữ liệu logic đề xuất / nguồn | UI | Chuyển đổi / quyền |
| :--- | :--- | :--- | :--- |
| kitchenRef | kitchens.id | UI-EXP-01..08 / cơ sở | Giữ khóa; kiểm scope server, không nhận cơ sở từ nhãn. |
| periodRef/fromDate/toDate | expense_periods | UI-EXP-01 / kỳ | Không tự quy tháng; biên ngày Q02. |
| typeVersionRef/amount/evidenceRef | expense_entries | UI-EXP-02 / loại, tiền, chứng từ | Decimal string, hiển thị đ; không bỏ VAT nguồn. |
| customerRef | customers.id + revision E10 | UI-EXP-02/06 / khách | Giữ ref lịch sử khi E10 gộp; không ghi lại snapshot. |
| personRef/hours/shiftRevisionRef | attendance_sheets + E11 | UI-EXP-03 / người, giờ, ca | Chỉ PER-07/PER-08 có scope; phân ca không sinh giờ. |
| rateVersionRef/payrollAmountRef | labor_cost_refs + nguồn chờ Q04 | UI-EXP-03 / nguồn tiền công | Không tính hai lần; không có nguồn → null. |
| methodVersionRef/proposedBasis | allocation_method_versions | UI-EXP-04/05/06/07 | Không mặc định driver; giữ version được duyệt. |
| approverRef/approvedAt/approvalEvidenceRef/contentHash | Quyết định gắn methodVersion | UI-EXP-04 / duyệt | Kiểm Giám đốc, tách tạo/duyệt; không điền tên giả làm duyệt thật. |
| reconciledRevenueRef | E7 snapshot + revision | UI-EXP-05/06 / doanh thu | Chỉ đọc nguồn đã đối soát; VAT/CK giữ theo nguồn, không số giao × giá. |
| materialCostRefs | E3/E11 manifest | UI-EXP-05 / nguyên liệu | Không cộng dự toán và thực mua, không cộng lại khoản khoán. |
| profit/definitionVersionRef | profit_runs, Q08 | UI-EXP-06/07 / kết quả | Không có định nghĩa/phương pháp → null; margin chờ Q13/E10-Q15. |
| unallocatedCost/unallocatedEffect/reconciliationDelta | Pool + profit_runs | UI-EXP-07 / cầu nối | Hiện chi phí dương, tác động âm và delta riêng; không dồn khách cuối. |
| originalEntryRef/adjustmentAmount/reason/approvalRef | expense_adjustments | UI-EXP-08 / điều chỉnh | Thêm bản riêng, không UPDATE gốc; kỳ đích Q10. |
| sourceManifestRef/status/blockedReasons | profit_runs | UI-EXP-05/06/07 | Giữ nguồn thiếu, không thay số 0; projection E12 còn chờ. |

Các tên cột là đề xuất trong [từ điển](../srs/data-dictionary.md), không là mapping vật lý đã triển khai. Không thay schema nền.
