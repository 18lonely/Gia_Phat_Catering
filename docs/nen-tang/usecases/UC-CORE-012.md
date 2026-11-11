---
id: DOC-NEN-TANG-USECASES-UC-CORE-012
title: UC-CORE-012 — Xem ma trận vai trò – quyền
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-012 — Xem ma trận vai trò – quyền

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Xem ma trận vai trò – quyền. Tiền điều kiện: Người có quyền xem matrix nội bộ. FR: FR-AUTH-RBAC-002; BR: —. Thành công: Ma trận. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận —.
3. Hiển thị vai trò nào có quyền nào. Bản đầu chỉ đọc; thay đổi ma trận qua bản phát hành.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. thử PATCH ma trận vai trò → không có endpoint ghi; 405 hoặc không route; không sửa dữ liệu.
3b. vai trò QUAN_TRI mở Cost không được cấp → không suy QUAN_TRI có toàn quyền nghiệp vụ;403 ERR-AUTH-403-02.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
