---
id: DOC-NEN-TANG-USECASES-UC-CORE-018
title: "UC-CORE-018: Huỷ thay cho xoá"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# UC-CORE-018: Huỷ thay cho xoá

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mức Sea level (port kỹ thuật: Fish level). Actor: quản trị hoặc người được cấp quyền theo SRS; hệ thống hỗ trợ AUTH/SYS. Bên quan tâm: người vận hành cần đúng quyền và có audit. Trigger: Huỷ thay cho xoá. Tiền điều kiện: Bản ghi nháp không được tham chiếu và người dùng có quyền hủy. FR: FR-SYS-AUD-004; BR: BR-AUD-001. Thành công: Bản ghi ở trạng thái huỷ. Bảo đảm tối thiểu: không ghi nghiệp vụ một phần hoặc lộ bí mật.

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã bản ghi, lý do.
3. Không có API xoá cứng bản ghi nghiệp vụ. Huỷ đặt cờ, giữ dữ liệu, bản ghi huỷ không xuất hiện ở danh sách mặc định.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
3a. hủy nguyên liệu được công thức hiệu lực tham chiếu → 409 ERR-SYS-409-01; không hủy.
3b. sau hủy tìm list mặc định và history → list không có; history giữ dữ liệu/cờ hủy; không SQL DELETE nghiệp vụ.
4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

[AC](../userstories/acceptance-criteria.md) · [Test](../test/test-cases.md). Chưa chạy phần mềm.
