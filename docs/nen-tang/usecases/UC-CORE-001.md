---
id: DOC-NEN-TANG-USECASES-UC-CORE-001
title: "UC-CORE-001: Đăng nhập nội bộ"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-001: Đăng nhập nội bộ

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Đăng nhập nội bộ. Tiền điều kiện: Tài khoản ACTIVE U1; mật khẩu hợp lệ; chưa đủ5 lần sai. FR: FR-AUTH-LGN-001; BR: BR-SEC-001`, `002`, `003. Thành công: access token, refresh token (cookie `HttpOnly`), hồ sơ người dùng, danh sách vai trò và phạm vi. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận tên đăng nhập, mật khẩu.
3. Xác thực nhân viên bằng tên đăng nhập và mật khẩu. Kiểm tra tài khoản đang hoạt động, chưa bị khoá. Ghi nhật ký đăng nhập cả khi thành công lẫn thất bại. Dạng tên đăng nhập: [N-01]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. sai mật khẩu lần5 → 423 ERR-AUTH-423-01; khóa15 phút; log thất bại.
3b. gửi11 lần/phút từ cùng IP → 429 ERR-AUTH-429-01; không xác thực vượt giới hạn.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
