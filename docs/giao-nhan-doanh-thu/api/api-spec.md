---
id: DOC-E7-API-API-SPEC-MD
title: API đề xuất E7
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# API đề xuất E7

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E7-Q08 |


Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

## Ranh giới

18 endpoint đề xuất (13 luồng chính +5 đọc bổ sung); không server. Input logic không là wire shape E6. Không callback/webhook/MISA connector ngoài PRD. [Catalog](endpoint-catalog.json) · [Mapping](data-mapping.md).

Header đề xuất: Authorization theo AUTH, Content-Type application/json khi có body, requestId để tra. Lệnh ghi phải chống trùng nhưng header/key scope/TTL/replay giữ BLOCKED E7-Q08. ID chuỗi; ngày YYYY-MM-DD theo Asia/Ho_Chi_Minh; thời điểm UTC; tiền VND decimal truyền chuỗi đề xuất; số suất nguyên không âm, tiền thu dương. Limits/nullable/omit chưa freeze; không tự default0.

Resolve resource→order→point→customer/kitchen từ nguồn tin cậy, không tin scope client. Khách chỉ nhận projection phiếu/kỳ của mình; không cost/giá mua/CK nội bộ/secret. GET chỉ đọc. POST tạo bản ghi đề xuất201; quyết định/trạng thái200. Resource trả nguồn/version. Envelope E1-Q01/E7-Q08 chưa freeze, không áp template skill thay E6.

| API / method / route | FR / actor | Request logic | Xử lý / success data | Gate |
| :--- | :--- | :--- | :--- | :--- |
| API-E7-001: POST /v1/deliveries | FR-DLV-NOTE-001; Bếp trưởng / quản lý cơ sở | orderId, orderRevisionRef, planRevisionRef, số giao, bằng chứng giao | Đối chiếu scope và nguồn; giữ số chốt/số giao riêng, ghi phiếu và provenance, không sửa order E6 → Phiếu chờ khách xác nhận | E6-CG-05/06/08; E7-Q02 |
| API-E7-002: POST /v1/deliveries/{id}/confirmations | FR-DLV-ACK-001; Đại diện khách được xác minh | deliveryId, số nhận, version, bằng chứng xác nhận | Chỉ ghi khi người nhận được xác minh đúng scope theo policy đã duyệt; mở link không là xác nhận; giữ số nhận thực và dấu vết → Xác nhận nhận hoặc chênh lệch | E6-CG-01/08; E7-Q01; Q-13 |
| API-E7-003: POST /v1/delivery-discrepancies | FR-DLV-DIFF-001; Dinh dưỡng viên / vận hành được cấp quyền | deliveryId, số giao/nhận tham chiếu, mô tả, evidenceRef | Giữ bằng chứng hai phía; so sánh số giao/nhận; thiếu số nhận thì chưa xác định chênh, không điền 0 → Biên bản có version, liên kết phiếu | E7-Q02; E6-CG-08 |
| API-E7-004: POST /v1/delivery-discrepancies/{id}/resolutions | FR-DLV-RES-001; Vận hành được cấp quyền | discrepancyId, phương án giao bù/giảm trừ, evidenceRef, version | Ghi thỏa thuận hai phía; giao bù gắn phiếu gốc và số bù thực; giảm trừ giữ dòng điều chỉnh riêng; không tự cộng cả hai cách cho một phần thiếu → Thỏa thuận và nguồn số tính tiền | E7-Q02/03; CK-Q07–09 khi liên quan CK |
| API-E7-005: POST /v1/revenue-calculations | FR-FIN-REV-001; Kế toán doanh thu | orderRevisionRef, pricingSnapshotId, billableServings, basisEvidenceRef | Kiểm căn cứ số tính tiền và giá chụp đúng order/version; tính số tính tiền × giá chụp; tách phải trả, VAT/doanh thu chưa VAT và CK riêng; thiếu context thì chưa xác định → Bản tính nháp có provenance | E7-Q03/04; Q-13; E6-CG-04/05/07 |
| API-E7-006: GET /v1/revenues | FR-FIN-VIEW-001; Kế toán doanh thu | customerId, fromDate, toDate, trạng thái | Đọc bản tính có sẵn theo scope; tách dòng đủ/thiếu; không cộng dòng chưa xác định như 0 vào tổng hoàn tất → Danh sách, nguồn và tổng có nhãn đủ/thiếu | E7-Q04/08; E6-CG-08 |
| API-E7-007: POST /v1/reconciliation-periods | FR-FIN-REC-001; Kế toán doanh thu | customerId, fromDate, toDate, revenueRefs | Chụp tập nguồn/version; liệt kê dòng thiếu/tranh chấp, không bỏ dòng lỗi để báo đủ → Kỳ nháp và danh sách chặn | E7-Q05; Q-13; E6-CG-08 |
| API-E7-008: POST /v1/reconciliation-periods/{id}/agreements | FR-FIN-AGRE-001; Kế toán và đại diện khách | periodId, version, agreementEvidenceRef | Đối chiếu tổng và nguồn đúng revision với bằng chứng khách; còn chênh lệch chưa thống nhất; không tự ghi thu → Kỳ thống nhất có bằng chứng | E7-Q05; Q-13; E6-CG-01/08 |
| API-E7-009: POST /v1/reconciliation-periods/{id}/receipts | FR-FIN-RCPT-001; Kế toán doanh thu | periodId, số tiền, ngày nhận, chứng từ, version | Kiểm tiền dương, đúng khách/kỳ và chứng từ; ghi khoản thu có dấu vết; không suy đã thu từ thống nhất hoặc xuất MISA → Khoản thu và còn phải thu riêng | E7-Q06; E7-Q05 về thu sau khóa |
| API-E7-010: POST /v1/reconciliation-periods/{id}/locks | FR-FIN-LOCK-001; Kế toán doanh thu | periodId, version, nguồn quyết định | Kiểm đủ nguồn/điều kiện khóa đã được duyệt; giữ snapshot bất biến; chặn mọi đường ghi ảnh hưởng kỳ → Kỳ LOCKED và audit | E7-Q05; Q-13 |
| API-E7-011: POST /v1/reconciliation-periods/{id}/reopen-requests | FR-FIN-RREQ-001; Kế toán doanh thu | periodId, version, lý do, nội dung sửa, evidenceRef | Kỳ phải khóa; lý do ≥10 ký tự theo nền; tạo yêu cầu, không mở khóa → Yêu cầu chờ Giám đốc, kỳ vẫn khóa | E7-Q05; O-06 về ủy quyền giữ mở |
| API-E7-012: POST /v1/reopen-requests/{id}/decisions | FR-FIN-RDEC-001; Giám đốc | requestId, requestVersion, periodVersion, approve/reject, reason | Kiểm Giám đốc khác người lập/sửa cuối theo BR-SEC-008; đúng version mới mở; từ chối giữ khóa; giữ snapshot cũ, sửa sau mở phải đối soát lại → Quyết định; kỳ REOPENED hoặc LOCKED | E7-Q05; O-06 không tự cấp người thay |
| API-E7-013: POST /v1/misa-exports | FR-FIN-MISA-001; Kế toán doanh thu | periodId, revision, templateRef đã xác nhận | Kiểm quyền/nguồn kỳ và mẫu nhập/mapping được duyệt; ghi yêu cầu xuất có nguồn/trạng thái/lỗi; thiếu mẫu thì chặn, không tự tạo cột → Yêu cầu xuất; file chỉ sau mapping được duyệt | E7-Q07/08; E7-Q05 về kỳ được phép xuất |

| API đọc bổ sung | GET route | FR / UI | Output logic |
| :--- | :--- | :--- | :--- |
| API-E7-014 | /v1/deliveries | FR-DLV-NOTE-001 / UI-E7-01 | Danh sách phiếu theo scope/ngày, có empty và missing source |
| API-E7-015 | /v1/deliveries/{id} | FR-DLV-ACK-001 / UI-E7-02 | Chi tiết theo quyền/link đã xác minh; không tự xác nhận |
| API-E7-016 | /v1/delivery-discrepancies/{id} | FR-DLV-DIFF-001 / UI-E7-03 | Biên bản/bằng chứng, không tự thống nhất |
| API-E7-017 | /v1/reconciliation-periods/{id} | FR-FIN-REC-001 / UI-E7-05 | Kỳ/nguồn/thu tiền/yêu cầu mở lại theo quyền; không chốt |
| API-E7-018 | /v1/misa-exports/{id} | FR-FIN-MISA-001 / UI-E7-08 | Trạng thái/fileRef khi có file thật; không tạo file |

GET list yêu cầu scope/khoảng ngày rõ; phân trang/giới hạn chờ E7-Q08, không mặc định lấy tất cả. Detail dùng id trong path; không ghi ngầm. UI01/02/03/05/08 dùng GET014–018 tương ứng; POST output phục vụ UI rồi đọc lại có quyền.

## DTO logic và validation

Delivery: id, orderRef, sourceRevisionRefs, số chốt tham chiếu, số giao, số nhận chưa xác định khi chưa xác nhận, trạng thái/version. Confirmation: deliveryId/version, receivedServings/evidence; actor resolve theo policy được duyệt, không tin actorId client. Link auth chưa đặc tả tiếp vì CG01/E7-Q01.

Discrepancy: phiếu/version/mô tả/evidence. Resolution: thỏa thuận/loại xử lý, phiếu bù hoặc căn cứ giảm trừ; công thức ảnh hưởng tiền E7-Q02/03. Không route sửa order E6.

RevenueCalculation: order revision/pricing snapshot, số tính tiền/căn cứ; giá lấy server; grossAmountDue/revenueExVat/discountSeparate riêng; chưa xác định không0. Không tin tổng tiền client. Period: customer/from/to, tập nguồn/version, completeness/gates, tổng phải trả/đã thu/trạng thái. Agreement: periodVersion/evidence đúng nguồn.

Receipt: tiền dương/chứng từ/ngày nhận/periodVersion; đa kỳ/thu thừa/sửa hủy E7-Q06. Lock: kỳ/version/evidence điều kiện; ReopenRequest: lý do≥10 ký tự/nội dung; Decision: approve/reject/reason/requestVersion/periodVersion; Giám đốc khác creator/lastEditor. Admin không tự có quyền duyệt.

ExportRequest: period/version/templateRef; thiếu mẫu → BLOCKED. Chưa biết extension/encoding/delimiter/headers/tài khoản/mã thuế. Result đề xuất trạng thái/source revision/error summary/fileRef khi thực sự có; fileRef không chứng minh nhập MISA đạt.

## Lỗi / retry / atomicity

Lỗi chung401/403/404/stale409/dependency503/unknown500 và lỗi miền422 theo [matrix](../srs/error-matrix.md). Kỳ khóa409-02 chặn mọi POST ảnh hưởng snapshot, không chỉ disable nút. Ghi dữ liệu/audit/receipt nguyên tử là đề xuất cần persistence E7-Q08; chưa chọn lock strategy. Mất response=UNKNOWN; đối chiếu trước lệnh mới, không tự retry. Cùng chứng từ không cộng thu hai lần. Không trả token trong log/danh sách.

## Quy ước tài liệu liên epic (XC-04)

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E7-Q08: XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
