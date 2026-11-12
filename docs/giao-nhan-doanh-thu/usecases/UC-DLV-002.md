---
id: DOC-E7-USECASES-UC-DLV-002-MD
title: UC-DLV-002 — Xác nhận số nhận qua link
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-DLV-002 — Xác nhận số nhận qua link

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-DLV-ACK-001 · FEAT-049 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-02.

Level: Sea level. Actor chính: Người đặt tổng kiêm người nhận của khách, được xác minh quyền xác nhận. Bên quan tâm: bếp cần số nhận thực; kế toán cần bằng chứng khách xác nhận.

Trigger: Sau khi nhận hàng, đại diện khách bấm link của phiếu giao để xác nhận số suất đã nhận.

Tiền điều kiện — nghiệp vụ: Phiếu giao tồn tại và thuộc phạm vi khách; người nhận có bằng chứng số nhận thực tế.
Tiền điều kiện — gate còn mở: E6-CG-01/08, E7-Q01 và Q-13 chưa được chốt. Luồng dưới chỉ áp dụng khi cơ chế xác minh/quyền đã được duyệt; không chọn loại token hay thời hạn link.

Luồng chính:
1. Đại diện khách truy cập link; hệ thống kiểm điều kiện xác minh và phạm vi phiếu trước khi hiển thị UI-E7-02.
2. Hệ thống hiển thị nguồn phiếu, số giao và version; việc xem phiếu chưa ghi số nhận.
3. Đại diện khách nhập số suất nhận thực, cung cấp bằng chứng xác nhận và gửi deliveryId cùng version đang xem.
4. Hệ thống kiểm quyền xác nhận hiện tại, số nhận và version của phiếu theo hợp đồng API.
5. Hệ thống lưu số nhận, bằng chứng, người xác nhận và thời điểm, giữ riêng số giao và số chốt.
6. Hệ thống trả xác nhận đã ghi cùng trạng thái nhận hoặc chênh lệch để đại diện khách kiểm tra.

Hậu điều kiện thành công: Số nhận thực và dấu vết xác nhận gắn với đúng phiếu/version; chênh lệch không bị tự xóa.
Bảo đảm tối thiểu: Mở link không làm phát sinh xác nhận. Lỗi không ghi một phần; hệ thống không sửa E6 hoặc kỳ khóa, không suy số nhận từ sự im lặng.

Extensions:
- 1a. Link bị thu hồi hoặc không đủ quyền: hệ thống trả ERR-E7-403-01; số nhận chưa được ghi và không lộ secret link.
- 1b. Phiên không hợp lệ hoặc phiếu ngoài phạm vi: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-404-01 tương ứng; không hiển thị dữ liệu phiếu và không ghi xác nhận.
- 1c. Cơ chế xác minh/nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 và mã gate; xác nhận vẫn bị chặn.
- 3a. Khách không gửi xác nhận: hệ thống giữ chờ, đánh dấu nhánh xử lý BLOCKED Q-13; không lấy số giao/chốt làm số nhận và không tự đặt thời hạn.
- 5a. Mất phản hồi sau khi gửi: hệ thống báo chưa rõ kết quả; đại diện khách đối chiếu xác nhận/version trước lệnh mới. Chưa kết luận đã lưu hay chưa, replay E7-Q08 vẫn BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-002-1, AC-E7-002-2, AC-E7-002-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
