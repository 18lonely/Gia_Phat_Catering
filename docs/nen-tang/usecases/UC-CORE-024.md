---
id: DOC-NEN-TANG-USECASES-UC-CORE-024
title: "UC-CORE-024: Tải tệp lên"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-024: Tải tệp lên

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Tải tệp lên. Tiền điều kiện: Tệp PNG thật dưới10MB, entity thuộc quyền. FR: FR-SYS-FILE-001; BR: không áp dụng. Thành công: Mã tệp. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận tệp, thực thể gắn kèm.
3. Nhận JPG, PNG, WEBP, PDF; tối đa 10 MB mỗi tệp. Kiểm tra loại tệp theo nội dung, không theo đuôi tên. Tệp nội bộ chỉ truy cập qua liên kết có chữ ký, hết hạn sau 15 phút.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. đổi đuôi exe thành png hoặc tệp lớn hơn10MB → 415 ERR-SYS-415-01 hoặc413 ERR-SYS-413-01.
3b. mở signed URL sau15 phút hoặc actor khác entity → URL hết hạn/không được cấp; không công khai object storage.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
