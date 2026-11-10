# UC-MENU-012: Nhập dữ liệu từ bảng tính

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: đưa dữ liệu gốc đã chuẩn bị ngoài hệ thống (roadmap DL-03 → DL-05) vào một lần, không gõ tay từng dòng.
  - Người duyệt: dữ liệu nhập hàng loạt vẫn qua duyệt như dữ liệu gõ tay.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.import`.
  - Thứ tự nhập: nguyên liệu → món → công thức → giá bán, vì loại sau tham chiếu loại trước.
- **Hậu điều kiện thành công**: toàn bộ dòng của tệp được tạo. Nguyên liệu ở `ACTIVE`; món và công thức ở `DRAFT`; giá bán ở `PENDING`.
- **Đảm bảo tối thiểu**: tệp còn lỗi thì không dòng nào được ghi.
- **Kích hoạt**: Dinh dưỡng viên mở trang "Nhập từ bảng tính".

## Luồng sự kiện chính

1. Dinh dưỡng viên chọn loại dữ liệu (nguyên liệu, món, công thức, giá bán) và tải mẫu `.xlsx`.
2. Dinh dưỡng viên điền mẫu ngoài hệ thống. Mẫu có dòng tiêu đề, dòng ví dụ, và trang liệt kê giá trị hợp lệ của các cột liệt kê.
3. Dinh dưỡng viên tải tệp đã điền lên và chọn "Kiểm tra".
4. Hệ thống đọc tệp và kiểm từng dòng theo đúng các quy tắc của chức năng tạo tương ứng, kể cả trùng lặp giữa các dòng trong tệp.
5. Hệ thống hiển thị số dòng hợp lệ và không có lỗi nào.
6. Dinh dưỡng viên chọn "Nhập".
7. Hệ thống ghi toàn bộ dòng trong một giao dịch, cấp mã, ghi nhật ký.
8. Hệ thống báo số bản ghi đã tạo theo từng trạng thái.

## Các luồng nhánh & ngoại lệ

- **3a. Tệp vượt 10 MB**: `ERR-SYS-413-01`. **Tệp không phải `.xlsx`**: `ERR-SYS-415-01`.
- **4a. Tệp sai mẫu (thiếu hoặc sai cột tiêu đề) hoặc vượt 2.000 dòng**: hệ thống báo `ERR-MENU-422-20` và nêu lý do; quay lại bước 2.
- **4b. Có dòng lỗi**:
  - 4b1. Hệ thống báo `ERR-MENU-422-20` kèm danh sách lỗi: số dòng, cột, giá trị, lý do (dùng thông báo của mã lỗi tương ứng, ví dụ `ERR-MENU-422-01` cho hệ số quy đổi sai).
  - 4b2. Nút "Nhập" bị khoá. Dinh dưỡng viên sửa tệp và quay lại bước 3.
- **4c. Dòng tham chiếu bản ghi chưa có** (món tham chiếu nhóm nguyên liệu không tồn tại; công thức tham chiếu món hoặc nguyên liệu không tồn tại): tính là lỗi của dòng đó, xử lý như 4b.
- **4d. Dòng trùng bản ghi đã có trong hệ thống** (cùng tên): tính là lỗi; hệ thống không tự cập nhật bản ghi cũ.
- **4e. Việc kiểm mất hơn 5 giây**: hệ thống chạy qua tác vụ nền, hiện tiến độ, và thông báo khi xong (`NFR-MENU-003`).
- **7a. Dữ liệu trong hệ thống thay đổi giữa lúc kiểm và lúc nhập làm phát sinh lỗi**: hệ thống huỷ toàn bộ giao dịch, báo `ERR-MENU-422-20`; Dinh dưỡng viên kiểm lại từ bước 3.
- **A1. Sau khi nhập món và công thức**: Dinh dưỡng viên gửi duyệt hàng loạt các món `DRAFT` vừa nhập (bước 9–11 của `UC-MENU-002`).

## Quy tắc nghiệp vụ liên quan

`BR-CAT-019`; và toàn bộ quy tắc của chức năng tạo tương ứng: `BR-CAT-001` → `003`, `006`, `007`, `010` → `012`, `015`, `016`.

## Điểm mở

- Có cần nhập **cập nhật** (sửa hàng loạt bản ghi đã có) không, hay chỉ nhập mới: [E2-Q10]. SRS hiện chỉ nhập mới.
- Giới hạn 2.000 dòng là [ĐỀ XUẤT].
