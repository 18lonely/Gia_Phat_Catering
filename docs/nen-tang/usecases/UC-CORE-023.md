---
id: DOC-NEN-TANG-USECASES-UC-CORE-023
title: "UC-CORE-023: Gửi qua kênh ngoài"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-023: Gửi qua kênh ngoài

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Gửi qua kênh ngoài. Tiền điều kiện: Q-14 đã chốt adapter và thông báo chờ gửi. FR: FR-SYS-NTF-003; BR: không áp dụng. Thành công: Trạng thái gửi. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận người nhận, mẫu, dữ liệu.
3. Giao diện gửi chung cho mọi kênh; gửi qua hàng đợi, thử lại tối đa 3 lần, lưu kết quả từng lần gửi. Kênh cụ thể: [Q-14]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. provider lỗi cả3 lần → trạng thái failed; ERR-SYS-502-01 ở job; không tự gửi lần4.
3b. retry sau provider đã nhận nhưng callback mất → cần provider messageId/idempotency; nếu chưa đối soát không phát lặp mù.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chờ Q-14
