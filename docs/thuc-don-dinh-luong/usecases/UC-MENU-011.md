# UC-MENU-011: Công bố và thu hồi thực đơn

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: chủ động thời điểm đưa thực đơn ra dùng.
  - Bếp, kế toán: chỉ thấy thực đơn đã chốt.
  - Khách và người ăn (từ E6): thực đơn đã thấy không tự đổi; nếu phải đổi thì có lý do.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.menu.write`.
  - Công bố: thực đơn ở trạng thái `APPROVED`. Thu hồi: thực đơn ở trạng thái `PUBLISHED`.
- **Hậu điều kiện thành công**: thực đơn `PUBLISHED` xuất hiện với mọi vai trò có quyền xem và ở dịch vụ tra cứu thực đơn đã công bố; hoặc thực đơn `WITHDRAWN` không còn xuất hiện ở đó.
- **Đảm bảo tối thiểu**: nội dung và kết quả kiểm của thực đơn đã duyệt không đổi khi công bố.
- **Kích hoạt**: Dinh dưỡng viên chọn "Công bố" trên thực đơn đã duyệt.

## Luồng sự kiện chính

1. Hệ thống kiểm ngày phục vụ đầu tiên của thực đơn sau hôm nay.
2. Hệ thống chuyển thực đơn sang `PUBLISHED`, ghi thời điểm công bố và nhật ký.
3. Hệ thống tạo thông báo cho quản lý cơ sở và bếp trưởng.
4. Hệ thống hiển thị thực đơn ở chế độ chỉ đọc với nhãn "đã công bố".

## Các luồng nhánh & ngoại lệ

- **1a. Ngày phục vụ đầu tiên là hôm nay hoặc đã qua** (`BR-MNU-009`): hệ thống báo `ERR-MENU-409-09`. Dinh dưỡng viên thu hồi về nháp, bỏ các ngày đã qua và gửi duyệt lại.
- **A1. Thu hồi thực đơn đã công bố** (`FR-MENU-APV-004`):
  - A1.1. Dinh dưỡng viên chọn "Thu hồi" và nhập lý do (từ 10 ký tự; thiếu → `ERR-SYS-422-01`).
  - A1.2. Hệ thống chuyển thực đơn sang `WITHDRAWN`, ghi nhật ký.
  - A1.3. Hệ thống phát sự kiện "thực đơn bị thu hồi" để các module khác xử lý, và thông báo cho quản lý cơ sở, bếp trưởng.
- **A2. Sửa thực đơn đã thu hồi** (`FR-MENU-APV-005`):
  - A2.1. Dinh dưỡng viên chọn "Sửa".
  - A2.2. Hệ thống chuyển thực đơn về `DRAFT`. Kết quả kiểm được tính lại theo thuộc tính món và danh mục quy tắc hiện hành.
  - A2.3. Tiếp tục theo `UC-MENU-007` → `UC-MENU-009` → `UC-MENU-010` → công bố lại.
- **A3. Công bố thực đơn chưa duyệt**: nút "Công bố" không hiện với thực đơn không ở `APPROVED`.

## Quy tắc nghiệp vụ liên quan

`BR-MNU-009`; `BR-AUD-001`.

## Điểm mở

- Thu hồi thực đơn khi đã có người ăn chọn món, hoặc khi một số ngày của tuần đã phục vụ xong: xử lý lựa chọn và order thế nào thuộc SRS E6. Trong R2 chưa có người ăn nên không phát sinh.
- Có cần thu hồi **từng ngày** thay vì cả tuần không (ví dụ đổi món thứ Năm khi thứ Hai đến thứ Tư đã phục vụ): [E2-Q8].
- Công bố do Dinh dưỡng viên bấm, hay tự công bố ngay khi duyệt xong: [E2-Q9]. SRS hiện tách hai bước.
