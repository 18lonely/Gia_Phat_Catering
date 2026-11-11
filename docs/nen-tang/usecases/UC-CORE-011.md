---
id: DOC-NEN-TANG-USECASES-UC-CORE-011
title: UC-CORE-011 — Kiểm quyền mỗi yêu cầu
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-011 — Kiểm quyền mỗi yêu cầu

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Kiểm quyền mỗi yêu cầu. Tiền điều kiện: U1 có quyền read trênK1, tài nguyênR1 thuộcK1. FR: FR-AUTH-RBAC-001; BR: BR-SEC-006`, `007. Thành công: Cho phép / từ chối. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận token, tài nguyên.
3. Mỗi API khai báo quyền cần có. Hệ thống kiểm (1) tài khoản có quyền đó qua vai trò, (2) bản ghi được yêu cầu nằm trong phạm vi dữ liệu của tài khoản. Thiếu (1) → 403. Thiếu (2) → 404, để không lộ sự tồn tại của bản ghi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. U1 đọc id thuộcK2 → 404 ERR-SYS-404-01; không lộ tồn tại.
3b. U1 có hai vai trò, bỏ quyền ở một vai trò còn vai trò khác cấp → hợp quyền vai trò được áp dụng cùng phạm vi; không tự mở scopeK2.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
