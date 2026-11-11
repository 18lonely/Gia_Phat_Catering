---
id: DOC-NEN-TANG-USECASES-UC-CORE-016
title: UC-CORE-016 — Tra cứu nhật ký
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-016 — Tra cứu nhật ký

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tra cứu nhật ký. Tiền điều kiện: Người đọc có quyền entityK1 và lọc thời gian. FR: FR-SYS-AUD-002; BR: BR-SEC-007. Thành công: Danh sách phân trang. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận bộ lọc.
3. Lọc theo thực thể, mã bản ghi, người, khoảng ngày, hành động. Xem lịch sử của một bản ghi theo thứ tự thời gian.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. truy vấn history entityK2 → 404 ERR-SYS-404-01 hoặc list rỗng theo scope; không lộ dữ liệu.
3b. hai bản ghi cùng timestamp → thứ tự ổn định timestamp,id; kiểm trang tiếp không mất/lặp dòng.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
