---
id: DOC-NEN-TANG-USECASES-UC-CORE-009
title: "UC-CORE-009: Sửa vai trò và cơ sở"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-009: Sửa vai trò và cơ sở

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Sửa vai trò và cơ sở. Tiền điều kiện: QUAN_TRI đổi U1 từ BEP_TRUONG K1 sangK2. FR: FR-AUTH-ACC-003; BR: BR-SEC-006`, `007`, `BR-AUD-001. Thành công: Tài khoản đã cập nhật. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, vai trò, cơ sở, lý do.
3. Thay đổi có hiệu lực ở yêu cầu kế tiếp của người dùng, không cần đăng nhập lại.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. gửi version cũ → 409 ERR-SYS-409-02; không ghi đè.
3b. U1 gọi API K1 ngay yêu cầu kế tiếp → 404 ERR-SYS-404-01; quyền mới có hiệu lực, không cần đăng nhập lại.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
