---
id: DOC-NEN-TANG-USECASES-UC-CORE-019
title: UC-CORE-019 — Quản lý tham số
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-019 — Quản lý tham số

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Quản lý tham số. Tiền điều kiện: QUAN_TRI tạo tham số cùng mã ở scopeK1, ngàyD+1. FR: FR-SYS-PRM-001; BR: BR-SYS-001. Thành công: Phiên bản tham số mới. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-04 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã, giá trị, phạm vi, ngày hiệu lực, lý do.
3. Mỗi tham số có: mã, kiểu, giá trị, phạm vi áp dụng (toàn hệ thống / cơ sở / công ty khách / điểm phục vụ), ngày hiệu lực từ. Giá trị dùng cho một ngày nghiệp vụ là giá trị có hiệu lực tại ngày đó ở phạm vi hẹp nhất. Danh mục khởi tạo ở Phụ lục 4.3.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. effectiveFrom=D-1 hoặc value sai kiểu → 422 ERR-SYS-422-02; không sửa giá quá khứ.
3b. tra ngàyD vàD+1 có tham số toàn hệ thống vàK1 → D dùng bản cũ; D+1 dùng phạm vi hẹp nhất đã được duyệt; thiếu VAT vẫn null.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
