---
id: DOC-NEN-TANG-USECASES-UC-CORE-004
title: UC-CORE-004 — Xác thực 2 bước
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-004 — Xác thực 2 bước

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: nhân viên nội bộ; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Xác thực 2 bước. Tiền điều kiện: N-04 được chốt bật MFA, tài khoản GIAM_DOC có secret đã đăng ký. FR: FR-AUTH-LGN-004; BR: —. Thành công: Như `FR-AUTH-LGN-001. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã 6 số.
3. Vai trò `GIAM_DOC`, `KT_DOANH_THU`, `QUAN_TRI` nhập thêm mã 6 số từ ứng dụng xác thực. Có làm hay không: [N-04]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. nhập mã6 số sai → 401 ERR-AUTH-401-03; không cấp phiên đầy đủ.
3b. mã đúng nhưng đã dùng trong bước xác thực trước → không cho replay; cách đăng ký/recovery chờ E1-Q03.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chờ N-04, E1-Q03
