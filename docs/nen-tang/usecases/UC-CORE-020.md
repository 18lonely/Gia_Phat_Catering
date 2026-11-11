---
id: DOC-NEN-TANG-USECASES-UC-CORE-020
title: UC-CORE-020 — Duyệt thay đổi tham số
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-020 — Duyệt thay đổi tham số

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Duyệt thay đổi tham số. Tiền điều kiện: NgườiA đề nghị COST_NGUONG_PCT, GIAM_DOC B duyệt. FR: FR-SYS-PRM-002; BR: BR-SYS-002`, `BR-SEC-008. Thành công: Trạng thái đề nghị. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-04 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã đề nghị, quyết định, lý do.
3. Tham số gắn cờ "cần duyệt" chỉ có hiệu lực sau khi người có quyền duyệt chấp thuận; người đề nghị không tự duyệt.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. A hoặc người sửa cuối tự duyệt → 403 ERR-SYS-403-01; giữ trạng thái chờ.
3b. B duyệt rồi truy giá trị ngày trước hiệu lực → chỉ có hiệu lực từ ngày đã khai; audit bất biến.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
