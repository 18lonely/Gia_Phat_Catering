---
id: DOC-NEN-TANG-USECASES-UC-CORE-025
title: UC-CORE-025 — Tác vụ nền
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-025 — Tác vụ nền

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tác vụ nền. Tiền điều kiện: JobJ1 có eventId và khóa lịch. FR: FR-SYS-JOB-001; BR: —. Thành công: —. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận —.
3. Hàng đợi có: thử lại với khoảng cách tăng dần, tối đa 5 lần; hàng đợi lỗi cho tác vụ hỏng hẳn; khoá chống chạy trùng cho tác vụ định giờ. `QUAN_TRI` xem được trạng thái và chạy lại tác vụ lỗi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. worker lỗi đủ5 lần → chuyển hàng đợi lỗi; log từng lần; không retry vô hạn.
3b. hai worker claim cùng job định giờ → chỉ một hiệu ứng nghiệp vụ; admin replay không nhân đôi effect đã commit.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
