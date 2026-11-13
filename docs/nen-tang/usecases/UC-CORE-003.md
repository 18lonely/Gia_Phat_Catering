---
id: DOC-NEN-TANG-USECASES-UC-CORE-003
title: "UC-CORE-003: Đăng xuất"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-003: Đăng xuất

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Đăng xuất. Tiền điều kiện: U1 có hai phiên S1/S2. FR: FR-AUTH-LGN-003; BR: không áp dụng. Thành công: Phiên bị vô hiệu. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Thu hồi phiên hiện tại; tuỳ chọn thu hồi mọi phiên của mình.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. dùng lại access token của phiên vừa logout sau thời hạn thu hồi → 401 ERR-AUTH-401-02; không đọc nghiệp vụ.
3b. chọn allSessions=true → cảS1/S2 bị thu hồi, logout lại không tạo tác dụng phụ.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
