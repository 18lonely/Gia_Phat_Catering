---
id: DOC-NEN-TANG-USECASES-UC-CORE-021
title: UC-CORE-021 — Tạo thông báo trong hệ thống
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-021 — Tạo thông báo trong hệ thống

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tạo thông báo trong hệ thống. Tiền điều kiện: Sự kiện có idE1, người nhận thuộcK1. FR: FR-SYS-NTF-001; BR: —. Thành công: Thông báo. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận sự kiện.
3. Module nghiệp vụ phát sự kiện; SYS tạo thông báo cho người nhận theo vai trò và phạm vi. Mỗi thông báo: loại, tiêu đề, nội dung, liên kết tới bản ghi, mức độ.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. payload tham chiếuK2 mà người nhận chỉ cóK1 → không tạo/hiển thị dữ liệuK2; không để link bypass scope.
3b. worker nhận lạiE1 → đề xuất một thông báo/người/event; cách lưu unique chờ E1-Q04.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
