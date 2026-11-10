# UC-MENU-003: Sửa thuộc tính món đang dùng

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: sửa được thuộc tính gắn sai mà không làm món biến mất khỏi danh mục.
  - Người duyệt: mọi thay đổi ảnh hưởng tới bộ kiểm quy tắc đều qua duyệt.
  - Người dùng thực đơn đã công bố: thực đơn đang chạy không đổi kết quả giữa chừng.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.catalog.write`.
  - Món ở trạng thái `ACTIVE` và không có đề nghị thay đổi nào đang chờ.
- **Hậu điều kiện thành công**: có 1 đề nghị thay đổi `PENDING` cho món; món vẫn `ACTIVE` với giá trị cũ và hiện nhãn "chờ duyệt thay đổi".
- **Đảm bảo tối thiểu**: giá trị của món không đổi cho đến khi đề nghị được duyệt.
- **Kích hoạt**: Dinh dưỡng viên mở một món `ACTIVE` và chọn "Sửa".

## Luồng sự kiện chính

1. Dinh dưỡng viên sửa một hoặc nhiều thuộc tính ảnh hưởng quy tắc (danh sách ở `BR-CAT-008`).
2. Dinh dưỡng viên nhập lý do (từ 10 ký tự) và chọn "Gửi đề nghị".
3. Hệ thống kiểm giá trị mới theo đúng các ràng buộc khi tạo món (Healthy khớp phương pháp, món gốc hợp lệ).
4. Hệ thống tạo đề nghị thay đổi `PENDING`, lưu giá trị cũ và mới của từng trường; món giữ nguyên giá trị cũ.
5. Hệ thống tạo thông báo cho người có quyền `menu.catalog.approve`.
6. Hệ thống hiển thị món với nhãn "chờ duyệt thay đổi" và bảng so sánh cũ – mới.

## Các luồng nhánh & ngoại lệ

- **1a. Chỉ sửa trường không ảnh hưởng quy tắc** (tên, mô tả, ảnh, chất gây dị ứng):
  - 1a1. Hệ thống lưu ngay, ghi nhật ký; không tạo đề nghị. Kết thúc.
- **2a. Thiếu lý do hoặc lý do dưới 10 ký tự** (`BR-AUD-001`): hệ thống báo `ERR-SYS-422-01`; quay lại bước 2.
- **3a. Giá trị mới vi phạm ràng buộc**: hệ thống báo `ERR-MENU-422-04` hoặc `ERR-MENU-422-05`; quay lại bước 1.
- **3b. Người khác vừa sửa món** (lệch phiên bản): hệ thống báo `ERR-SYS-409-02`; người dùng tải lại.
- **A1. Đề nghị được duyệt** (từ `UC-MENU-010`):
  - A1.1. Hệ thống ghi giá trị mới vào món, ghi nhật ký, bỏ nhãn.
  - A1.2. Thực đơn `DRAFT`, `CHECKED` có món này được kiểm lại bằng giá trị mới ở lần kiểm kế tiếp. Thực đơn từ `PENDING` trở đi giữ kết quả lúc gửi duyệt ([E2-Q11]).
- **A2. Đề nghị bị trả lại**: hệ thống chuyển đề nghị sang `REJECTED`, thông báo cho Dinh dưỡng viên kèm lý do; món không đổi.
- **A3. Dinh dưỡng viên rút đề nghị**: đề nghị chuyển `WITHDRAWN`; món không đổi.
- **A4. Ngừng dùng món** (`FR-MENU-DISH-005`):
  - A4.1. Dinh dưỡng viên chọn "Ngừng dùng" và nhập lý do.
  - A4.2. Nếu món nằm trong thực đơn `PUBLISHED` có ngày phục vụ từ hôm nay trở đi: hệ thống báo `ERR-SYS-409-01` kèm danh sách thực đơn; không đổi (`BR-CAT-005`).
  - A4.3. Nếu không: món chuyển `INACTIVE`.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-005`, `006`, `007`, `008`; `BR-SEC-008`; `BR-AUD-001`.

## Ghi chú thiết kế

Giá trị đề nghị lưu ở bảng `change_requests` (ERD v0.2.0 mục 3.5). Nếu món bị thay đổi bằng đường khác trong lúc đề nghị đang chờ, đề nghị chuyển `STALE` và phải gửi lại.
