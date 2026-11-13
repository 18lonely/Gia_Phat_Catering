---
id: DOC-NEN-TANG-USECASES-UC-CORE-008
title: "UC-CORE-008: Khoá / mở khoá tài khoản"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-008: Khoá / mở khoá tài khoản

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Khoá / mở khoá tài khoản. Tiền điều kiện: QUAN_TRI, U1 đang ACTIVE có phiên đang dùng. FR: FR-AUTH-ACC-002; BR: BR-SEC-005`, `BR-AUD-001. Thành công: Trạng thái mới. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, lý do.
3. Khoá làm tài khoản không đăng nhập được và thu hồi mọi phiên trong ≤ 60 giây.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. bỏ lý do hoặc nhập9 ký tự → 422 ERR-SYS-422-01; trạng thái không đổi.
3b. khóa rồi thử API ở giây60 → mọi phiên bị thu hồi; mở khóa không hồi sinh phiên cũ.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
