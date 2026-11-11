---
id: DOC-NEN-TANG-USECASES-UC-CORE-015
title: UC-CORE-015 — Ghi nhật ký thay đổi
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-015 — Ghi nhật ký thay đổi

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Ghi nhật ký thay đổi. Tiền điều kiện: Thao tác sửa giá có actor/service và requestId. FR: FR-SYS-AUD-001; BR: BR-AUD-002. Thành công: Bản ghi nhật ký. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận — (tự động).
3. Mọi lệnh tạo, sửa, huỷ, duyệt trên bảng nghiệp vụ sinh 1 bản ghi nhật ký trong cùng giao dịch cơ sở dữ liệu: ai, lúc nào, thực thể, mã bản ghi, hành động, giá trị cũ → mới của từng trường đổi, lý do, mã yêu cầu. Nếu thao tác do agent thực hiện: ghi cả tài khoản dịch vụ và người dùng đang dùng agent.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. gây lỗi ghi audit sau bước update → rollback cả update; không thay đổi nghiệp vụ không audit.
3b. gửi retry cùng idempotency key → chỉ một thay đổi và một audit nghiệp vụ; ghi đủ before/after và on_behalf.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
