---
id: DOC-NEN-TANG-USECASES-UC-CORE-013
title: "UC-CORE-013: Uỷ quyền duyệt khi vắng"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-013: Uỷ quyền duyệt khi vắng

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Uỷ quyền duyệt khi vắng. Tiền điều kiện: O-06 đã chốt; người duyệt ủy quyền choU2 trong khoảng ngày. FR: FR-AUTH-RBAC-003; BR: BR-SEC-008`, `BR-AUD-001. Thành công: Bản ghi uỷ quyền. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận người được uỷ, quyền, từ ngày, đến ngày.
3. Người có quyền duyệt chỉ định người thay trong một khoảng ngày. Người thay nhận đúng các quyền duyệt được uỷ, hết hạn tự thu hồi. Phụ thuộc [O-06]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. ủy quyền chính mình hoặc ngày kết thúc trước ngày bắt đầu → 422 ERR-AUTH-422-03.
3b. U2 là người sửa cuối bản ghi được đề nghị duyệt → 403 ERR-SYS-403-01; ủy quyền không phá tách người tạo/sửa và duyệt.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chờ O-06
