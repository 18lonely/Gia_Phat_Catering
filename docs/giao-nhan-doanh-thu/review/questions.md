---
id: DOC-E7-REVIEW-QUESTIONS-MD
title: Sổ câu hỏi mở E7
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# Sổ câu hỏi mở E7

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-03; E7-Q03, E7-Q04; XC-11; E7-Q07 |


Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

Tất cả **CHỜ TRẢ LỜI**. Cột trả lời để trống, phương án tham khảo chưa được chọn; không yêu cầu trả lời trong phiên này.

| Mã | Câu hỏi | Phương án tham khảo / đánh đổi | Nhánh BLOCKED | Trả lời | Nguồn / người / ngày |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Q-13 | Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền? | Giữ chờ và xử lý thủ công có bằng chứng; hoặc suy định theo thỏa thuận khách có thời hạn/thông báo/tranh chấp. Chưa chọn. | ACK im lặng; số tính tiền và thống nhất/khóa kỳ liên quan |  |  |
| E7-Q01 | Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì? | Phiên có quyền hoặc token giới hạn scope cần review Auth; không lấy QR E6 làm quyền ký nhận. | Link; CG01/08 chờ, không đặc tả thêm producer E6 |  |  |
| E7-Q02 | Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào? | Giữ phiếu gốc + thỏa thuận/phiếu bù; cần chống đếm trùng và quyền. | RES, tổng giao/nhận sau bù, tác động kỳ khóa |  |  |
| E7-Q03 | Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào? | Căn cứ từng đơn có evidence; không mặc định số nhận/số chốt. | REV; giảm trừ khác CK riêng |  |  |
| E7-Q04 | Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể? | Hiện phải trả, VAT, doanh thu trước VAT riêng; không mượn dung sai Cost. | Tổng chính thức và R7 |  |  |
| E7-Q05 | Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào? | Snapshot từng vòng; chỉ Giám đốc duyệt mới mở. Điều kiện khác chưa chọn. | AGRE/LOCK và sửa sau REOPENED |  |  |
| E7-Q06 | Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào? | Chứng từ/phân bổ riêng; không suy CK đã bù trừ. | Thanh toán nâng cao/chống trùng nghiệp vụ |  |  |
| E7-Q07 | Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì? | Nhận mẫu có version và thử nhập môi trường được cấp; chưa giả CSV/XLSX, cột, mã thuế/tài khoản. | File bytes/mapping cột/thử nhập MISA |  |  |
| E7-Q08 | Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào? | Kế thừa an toàn nền; review kỹ thuật, không đặt TTL/retry/limits tùy ý. | Wire contract/persistence/fault/load |  |  |

> Chờ E7-Q07 — XC-11. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-11](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

> Chờ E7-Q03, E7-Q04 — XC-03. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-03](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

E6-CG-01/08/05/06 giữ CHỜ TRẢ LỜI trong [sổ E6 duy nhất](../../chon-mon-order/review/contract-gap-register.md), không hỏi lại. 14/14 CG OPEN. CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03/O-04, E6-EVID-001/002 không đổi. Chỉ đóng khi có bằng chứng/phạm vi quyết định, không vì kiểm tài liệu.
