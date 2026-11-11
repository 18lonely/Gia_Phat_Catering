---
id: DOC-NEN-TANG-USECASES-UC-CORE-014
title: UC-CORE-014 — Tài khoản dịch vụ cho agent
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-014 — Tài khoản dịch vụ cho agent

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tài khoản dịch vụ cho agent. Tiền điều kiện: svc-agent-noi-bo có allowlist; người hỏi chỉ có quyềnK1. FR: FR-AUTH-SVC-001; BR: BR-SEC-009`, `010. Thành công: —. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận —.
3. Hai tài khoản tách biệt: `svc-agent-noi-bo`, `svc-agent-dinh-duong-vien`. Mỗi tài khoản có danh sách quyền gắn cứng, không đăng nhập qua giao diện.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. agent phía khách gọi cost hoặc SELECT bảng Cost bằng service DB account → 403 ở API và denied DB; không trả số trong lỗi.
3b. quyền user bị thu hồi giữa hai tool call → tool thứ hai từ chối; giao quyền service/user tính mỗi lần, không đăng nhập UI.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
