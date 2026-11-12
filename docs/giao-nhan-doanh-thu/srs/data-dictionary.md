---
id: DOC-E7-SRS-DATA-DICTIONARY-MD
title: Delta dữ liệu E7 — đề xuất chưa merge
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Delta dữ liệu E7 — đề xuất chưa merge

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

65 bảng chung giữ nguyên. DBML có orders.status DELIVERED/CONFIRMED/DISPUTED/RECONCILED nhưng chưa có thực thể phiếu/kỳ/thu/MISA, không đủ làm bằng chứng persistence. Không sửa orders.status từ E7 khi chưa có contract tác động nguồn. [Mapping](../api/data-mapping.md).

| Thực thể delta | Trường logic / kiểu đề xuất | Quan hệ / ràng buộc / null | Gate |
| :--- | :--- | :--- | :--- |
| e7_delivery_notes | id ID; orderId ID; orderRevisionRef/planRevisionRef opaque; deliveredServings int; state; version int; evidenceRef | PK id; orderId→orders; số giao≥0; nguồn bắt buộc theo policy đã xác nhận; không dùng thiếu=0 | CG05/06/08; Q02 |
| e7_receipt_confirmations | id; deliveryId; receivedServings int; actorRef; confirmedAt UTC; evidenceRef; version | Gắn phiếu/version; chưa có xác nhận thì chưa có số nhận, không default0. Sửa xác nhận cần policy, giữ lịch sử | CG01; Q01/02/13 |
| e7_discrepancies / resolutions | id; deliveryId; description; evidenceRef; resolutionType; linkedSupplementRef; adjustmentBasis | Mỗi thỏa thuận gắn phần chênh và bằng chứng; không tự cả bù+giảm trừ. Chưa field tiền tự tính khi thiếu basis | Q02/03 |
| e7_revenue_snapshots | id; orderId; orderRevisionRef; pricingSnapshotId; billableServings; basisEvidenceRef; grossAmountDue/revenueExVat decimal; contextStatus | Giữ nguồn bất biến; cùng order/version; kết quả chưa xác định nullable logic, không0. Số gốc snapshot không ghi đè | Q03/04/08 |
| e7_reconciliation_periods / lines | id; customerId; fromDate/toDate; revision; state; sourceRefs; totals; completeness | Một tập nguồn có version; phạm vi/chồng kỳ và tái chụp cần duyệt; snapshot khóa bất biến | Q05 |
| e7_cash_receipts | id; periodId; amount decimal; receivedDate; evidenceRef; version | Tiền dương, chứng từ/scope hợp lệ; uniqueness nghiệp vụ và allocation chưa freeze | Q06/08 |
| Reuse change_requests / approvals + liên kết kỳ | entityRef; requestVersion; periodVersion; creator/lastEditor; reason; decision | Đề xuất dùng workflow nền, không tạo hai nguồn duyệt; Giám đốc khác người lập/sửa cuối; lý do≥10 ký tự; yêu cầu không mở khóa | Q05/08; O-06 |
| e7_export_runs | id; periodRef/revision; templateRef; status; errorSummary; fileRef; sourceFingerprint | FileRef chỉ có khi thật sự tạo; template chưa biết; giữ bytes/revision cũ khi kỳ mở lại | Q07/08 |

Trường tối thiểu dùng kiểm toán: actor/time/before-after/reason/resourceVersion và request reference, kế thừa audit nền; độ dài, nullability vật lý, unique/index, precision và retention chưa quyết → BLOCKED E7-Q08. ID logic theo nền bigint qua API dạng chuỗi. Không có DDL hoặc bảng được merge. Các enum trong state diagram là nhãn đề xuất.

Quan hệ logic: customer→period→lines→revenue snapshot→order/pricing snapshot; order→delivery→confirmation/discrepancy→resolution; period→receipt/reopen/export. Order/plan revision phụ thuộc delta E6 chưa freeze, không coi FK đó đã triển khai.
