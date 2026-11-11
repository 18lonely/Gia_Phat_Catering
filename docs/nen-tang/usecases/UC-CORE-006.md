---
id: DOC-NEN-TANG-USECASES-UC-CORE-006
title: UC-CORE-006 — Cấp lại mật khẩu
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-006 — Cấp lại mật khẩu

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Cấp lại mật khẩu. Tiền điều kiện: QUAN_TRI có quyền reset U1 và lý do10 ký tự. FR: FR-AUTH-PWD-002; BR: BR-SEC-004`, `005`, `BR-AUD-001. Thành công: Mật khẩu tạm hiển thị một lần. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, lý do.
3. QUAN_TRI` cấp mật khẩu tạm cho một tài khoản. Mật khẩu tạm hết hạn sau 24 giờ và buộc đổi ở lần đăng nhập đầu.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. reset userId không tồn tại → 404 ERR-AUTH-404-01; không trả mật khẩu.
3b. dùng mật khẩu tạm sau24 giờ → không đăng nhập; mật khẩu tạm chỉ hiển thị một lần, retry không trả lại secret.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
