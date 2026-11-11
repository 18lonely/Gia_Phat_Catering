---
id: DOC-NEN-TANG-USECASES-UC-CORE-007
title: UC-CORE-007 — Tạo tài khoản nội bộ
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-007 — Tạo tài khoản nội bộ

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tạo tài khoản nội bộ. Tiền điều kiện: QUAN_TRI tạo Unew vai trò BEP_TRUONG cơ sởK1. FR: FR-AUTH-ACC-001; BR: BR-SEC-004`, `006`, `007. Thành công: Tài khoản ở trạng thái "chờ đổi mật khẩu". Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận họ tên, tên đăng nhập, vai trò, cơ sở.
3. QUAN_TRI` tạo tài khoản, gán ít nhất 1 vai trò; vai trò `QL_CO_SO`, `BEP_TRUONG` bắt buộc gán ít nhất 1 cơ sở.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. bỏ kitchenIds hoặc roles rỗng → 422 ERR-AUTH-422-02; không tạo user/role một phần.
3b. hai request tạo cùng tên đăng nhập → một tài khoản được tạo; request còn lại409 ERR-AUTH-409-01.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
