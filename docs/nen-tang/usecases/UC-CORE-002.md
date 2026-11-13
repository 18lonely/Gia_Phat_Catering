---
id: DOC-NEN-TANG-USECASES-UC-CORE-002
title: "UC-CORE-002: Làm mới phiên"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-002: Làm mới phiên

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Làm mới phiên. Tiền điều kiện: U1 có refresh R1 chưa dùng và chưa hết7 ngày. FR: FR-AUTH-LGN-002; BR: BR-SEC-003`, `005. Thành công: access token mới, refresh token mới. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận refresh token.
3. Đổi refresh token còn hạn lấy access token mới; refresh token cũ bị vô hiệu ngay (xoay vòng). Dùng lại refresh token đã vô hiệu → thu hồi mọi phiên của tài khoản.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. dùng lại R1 sau khi xoay thành R2 → 401 ERR-AUTH-401-02; thu hồi các phiên trong≤60 giây.
3b. hai request đồng thời dùng R1 → chỉ một refresh thành công; lần reuse kích hoạt thu hồi; client không gửi refresh song song.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
