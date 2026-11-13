# UC-MENU-005: Đặt giá bán món

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: mỗi món có giá bán để kiểm ngưỡng giá của loại suất [D-18].
  - Người duyệt: giá bán hiển thị công khai cho khách nên phải qua duyệt.
  - Khách hàng: giá đã áp dụng cho một ngày không bị đổi ngược về trước.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.price.write`.
  - Món tồn tại và có công thức cho cỡ định lượng tương ứng.
- **Hậu điều kiện thành công**: có một giá `PENDING` cho món; người duyệt nhận thông báo.
- **Đảm bảo tối thiểu**: giá đang hiệu lực không bị thay đổi.
- **Kích hoạt**: Dinh dưỡng viên mở một món và chọn "Đặt giá bán".

## Luồng sự kiện chính

1. Dinh dưỡng viên nhập giá bán (đã gồm VAT) và ngày hiệu lực.
2. Dinh dưỡng viên chọn "Gửi duyệt".
3. Hệ thống kiểm giá là số nguyên không âm, bội số của 100 đồng, và ngày hiệu lực sau hôm nay.
4. Hệ thống kiểm chưa có giá nào cho cùng món, cùng cỡ, cùng ngày hiệu lực.
5. Hệ thống lưu giá ở trạng thái `PENDING`, ghi nhật ký, tạo thông báo cho người có quyền `menu.price.approve`.

## Các luồng nhánh & ngoại lệ

- **3a. Giá không hợp lệ hoặc ngày hiệu lực không sau hôm nay** (`BR-CAT-015`, `016`): hệ thống báo `ERR-MENU-422-11`; quay lại bước 1.
- **4a. Đã có giá cho ngày hiệu lực đó**: hệ thống báo `ERR-MENU-409-04`; quay lại bước 1.
- **A1. Giá được duyệt** (từ `UC-MENU-010`): giá chuyển `APPROVED` và được dùng từ ngày hiệu lực.
- **A2. Giá bị trả lại**: Dinh dưỡng viên nhận thông báo kèm lý do; tạo giá mới nếu cần.
- **A3. Sửa hoặc huỷ giá đã hiệu lực** (`BR-CAT-016`): hệ thống báo `ERR-MENU-409-10`; Dinh dưỡng viên tạo giá mới với ngày hiệu lực sau hôm nay.
- **A4. Xem lịch sử giá** (P1): hệ thống liệt kê các giá của món theo ngày hiệu lực.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-015`, `016`; `BR-SEC-008`; quyết định [D-15] (giá gồm VAT), [D-18] (giá riêng từng món).

## Điểm mở

- Vai trò của giá món khi công ty đã đặt định mức chung: [E2-Q1].
- Nếu có nhiều cỡ định lượng [O-02], mỗi cỡ một giá.
