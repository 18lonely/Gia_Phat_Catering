---
id: DOC-NEN-TANG-USECASES-UC-CORE-022
title: "UC-CORE-022: Trạng thái thông báo"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-022: Trạng thái thông báo

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Trạng thái thông báo. Tiền điều kiện: U1 có thông báoNEW của mình. FR: FR-SYS-NTF-002; BR: không áp dụng. Thành công: không áp dụng. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã thông báo, trạng thái.
3. 3 trạng thái: mới, đã xem, đã xử lý. Danh sách lọc theo trạng thái; hiện số thông báo mới trên thanh điều hướng.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. U2 sửa trạng thái thông báoU1 → 404 ERR-SYS-404-01.
3b. U1 đánh dấu SEEN rồi RESOLVED và retry → đếm NEW giảm một; không tạo thông báo mới; hồi trạng thái chờ E1-Q04.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
