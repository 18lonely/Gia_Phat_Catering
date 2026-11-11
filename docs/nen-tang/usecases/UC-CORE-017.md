---
id: DOC-NEN-TANG-USECASES-UC-CORE-017
title: UC-CORE-017 — Bắt buộc lý do
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-017 — Bắt buộc lý do

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Bắt buộc lý do. Tiền điều kiện: Thao tác sửa vai trò yêu cầu reason. FR: FR-SYS-AUD-003; BR: BR-AUD-001. Thành công: —. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận lý do.
3. Thao tác thuộc danh sách ở `BR-AUD-001` bị từ chối nếu thiếu lý do từ 10 ký tự.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. reason chỉ có9 ký tự sau trim → 422 ERR-SYS-422-01; không ghi.
3b. reason đủ10 ký tự có chuỗi HTML → lưu chuỗi văn bản; UI escape; không chạy script.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
