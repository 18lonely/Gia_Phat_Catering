# UC-MENU-006: Tạo loại suất

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: tự định nghĩa suất theo ngưỡng giá và số món [D-20].
  - Công ty khách: chọn một loại suất làm định mức chung ở E6 [D-21].
  - Bếp: cơ cấu suất đã có thực đơn không đổi giữa chừng.
- **Tiền điều kiện**: người dùng có quyền `menu.catalog.write`.
- **Hậu điều kiện thành công**: loại suất ở trạng thái `ACTIVE`, chọn được khi tạo thực đơn.
- **Đảm bảo tối thiểu**: loại suất đã có thực đơn gửi duyệt không bị đổi cơ cấu.
- **Kích hoạt**: Dinh dưỡng viên chọn "Thêm loại suất".

## Luồng sự kiện chính

1. Dinh dưỡng viên nhập tên và ngưỡng giá (đã gồm VAT).
2. Dinh dưỡng viên nhập số món chính đưa ra để chọn (mặc định 3), số món chính mỗi người được chọn (mặc định 1), số món phụ.
3. Dinh dưỡng viên chọn suất có rau, có canh hay không.
4. Dinh dưỡng viên chọn "Lưu".
5. Hệ thống kiểm tên không trùng và cấu hình hợp lệ.
6. Hệ thống cấp mã, lưu loại suất ở trạng thái `DRAFT`, ghi nhật ký.
7. Dinh dưỡng viên chọn "Kích hoạt".
8. Hệ thống chuyển loại suất sang `ACTIVE`.

## Các luồng nhánh & ngoại lệ

- **5a. Tên trùng** (`BR-CAT-001`): hệ thống báo `ERR-MENU-409-01`; quay lại bước 1.
- **5b. Ngưỡng giá ≤ 0, số món chính được chọn lớn hơn số đưa ra hoặc nhỏ hơn 1, số món phụ ngoài 0–5** (`BR-CAT-017`): hệ thống báo `ERR-MENU-422-12`; quay lại bước 1–3.
- **A1. Sửa loại suất**:
  - A1.1. Sửa tên hoặc cờ công khai: lưu ngay.
  - A1.2. Sửa cơ cấu khi đã có thực đơn từ `PENDING` trở đi: hệ thống báo `ERR-MENU-409-05` và gợi ý tạo loại suất mới (`BR-CAT-018`).
- **A2. Ngừng loại suất**: chuyển `INACTIVE`; thực đơn đã công bố không bị ảnh hưởng; không tạo được thực đơn mới cho loại suất này.
- **A3. Đánh dấu công khai** (P1): loại suất hiện trên website ở E8.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-001`, `017`, `018`; `BR-MENU-001`, `004`, `005`; `BR-COST-012`.

## Điểm mở

- Ngưỡng giá được kiểm thế nào khi dựng thực đơn: [E2-Q1].
- Giới hạn số món phụ 0–5 là [ĐỀ XUẤT].
