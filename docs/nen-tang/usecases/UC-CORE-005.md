---
id: DOC-NEN-TANG-USECASES-UC-CORE-005
title: UC-CORE-005 — Đổi mật khẩu
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-005 — Đổi mật khẩu

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Đổi mật khẩu. Tiền điều kiện: U1 có phiênS1 vàS2, mật khẩu mới NewPass1234 chưa thuộc3 mật khẩu gần nhất. FR: FR-AUTH-PWD-001; BR: BR-SEC-001`, `005. Thành công: Xác nhận. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mật khẩu cũ, mật khẩu mới.
3. Người dùng đổi mật khẩu của mình; phải nhập đúng mật khẩu hiện tại. Sau khi đổi, mọi phiên khác bị thu hồi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. đặt mật khẩu9 ký tự hoặc thuộc3 mật khẩu gần nhất → 422 ERR-AUTH-422-01; mật khẩu không đổi.
3b. đổi thành công từS1 rồi gọi bằngS2 → S1 giữ, S2 thu hồi≤60 giây; không ghi mật khẩu/token vào audit.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
