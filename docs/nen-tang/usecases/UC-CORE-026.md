---
id: DOC-NEN-TANG-USECASES-UC-CORE-026
title: UC-CORE-026 — Kiểm tra sức khoẻ
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-026 — Kiểm tra sức khoẻ

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Kiểm tra sức khoẻ. Tiền điều kiện: API/DB/Redis/queue hoạt động. FR: FR-SYS-HLT-001; BR: —. Thành công: Trạng thái từng thành phần. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận —.
3. Điểm kiểm tra `/v1/health` trả trạng thái API, MySQL, Redis, hàng đợi; dùng cho cân bằng tải và giám sát.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. ngắt MySQL → 503 ERR-SYS-503-01; readiness không đạt.
3b. gọi health từ Internet không có quyền nội bộ → chỉ minimal status; không lộ DSN/secret/topology chi tiết.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
