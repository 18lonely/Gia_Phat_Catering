---
id: DOC-E7-USECASES-UC-FIN-007-MD
title: "UC-FIN-007: Lập kỳ đối soát"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-007: Lập kỳ đối soát

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-REC-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-05.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: đại diện khách cần biết tập giao nhận được đối soát; kế toán cần giữ nguồn từng dòng.

Trigger: Kế toán bắt đầu đối soát doanh thu của một khách cho khoảng ngày cần kiểm tra.

Tiền điều kiện (nghiệp vụ): Kế toán có quyền tại khách; các nguồn doanh thu có thể có dòng thiếu hoặc tranh chấp cần liệt kê.
Tiền điều kiện (gate còn mở): E7-Q05, Q-13 và E6-CG-08 chưa chốt phạm vi/điều kiện kỳ và nguồn; không tự chọn cách chống chồng kỳ.

Luồng chính:
1. Kế toán chọn khách, fromDate, toDate và revenueRefs tại UI-E7-05.
2. Hệ thống kiểm phiên, quyền theo khách và thứ tự ngày bắt đầu/kết thúc.
3. Hệ thống đọc tập doanh thu cùng version nguồn trong phạm vi được chọn, kiểm khả năng sử dụng nguồn theo gate.
4. Hệ thống lập danh sách dòng đủ, thiếu và tranh chấp; phiếu chờ khách xác nhận vẫn nằm trong tập cần rà.
5. Hệ thống chụp tập nguồn/version và tổng có căn cứ vào kỳ nháp, ghi dấu vết tạo kỳ.
6. Hệ thống trả kỳ nháp cùng danh sách chặn để kế toán chuẩn bị đối chiếu với khách.

Hậu điều kiện thành công: Kỳ nháp giữ tập nguồn và các dòng cần xử lý; chưa được tự chuyển thành thống nhất.
Bảo đảm tối thiểu: Hệ thống không bỏ dòng lỗi để báo đủ và không sửa nguồn E6/kỳ khóa; lỗi không tạo kỳ một phần.

Extensions:
- 2a. fromDate sau toDate: hệ thống trả ERR-FIN-422-02, yêu cầu sửa khoảng ngày; không tạo kỳ.
- 4a. Có phiếu chưa được khách xác nhận: hệ thống hiển thị BLOCKED Q-13 khi chuẩn bị chốt; dòng chờ được giữ, kỳ chưa được coi là đủ để chốt.
- 2b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không tạo kỳ hoặc lộ nguồn khách khác.
- 3a. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; không tạo kết quả đủ giả.
- 5a. Mất phản hồi tạo kỳ: hệ thống báo chưa rõ kết quả; kế toán đối chiếu kỳ/version trước lệnh mới. Trạng thái lưu chưa xác định, replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-007-1, AC-E7-007-2, AC-E7-007-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
