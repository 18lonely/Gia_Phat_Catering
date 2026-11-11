---
id: DOC-NEN-TANG-USECASES-UC-CORE-010
title: UC-CORE-010 — Xem nhật ký đăng nhập
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-010 — Xem nhật ký đăng nhập

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Xem nhật ký đăng nhập. Tiền điều kiện: QUAN_TRI lọc login_logs U1 trong ngày thử. FR: FR-AUTH-ACC-004; BR: —. Thành công: Danh sách phân trang. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận bộ lọc.
3. Lọc theo tài khoản, khoảng ngày, kết quả. Mỗi dòng: thời điểm, kết quả, địa chỉ IP, thiết bị.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. pageSize=101 → 422 ERR-SYS-422-03; không tự cắt về100.
3b. trang lớn hơn trang cuối → items rỗng,total đúng; không có mật khẩu/token trong log.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
