# UC-MENU-002: Tạo món và gửi duyệt

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: đưa món mới vào danh mục để xếp thực đơn.
  - Người duyệt: món được gắn thuộc tính đúng trước khi dùng, vì thuộc tính sai làm bộ kiểm quy tắc cho kết quả sai.
  - Bếp trưởng: món đưa vào là món bếp làm được với số lượng lớn.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.catalog.write`.
  - Đã có nhóm nguyên liệu và phương pháp chế biến (`FR-MENU-ING-005`, `FR-MENU-DISH-007`).
- **Hậu điều kiện thành công**: món ở trạng thái `PENDING`, có ít nhất 1 công thức `PENDING` hoặc `ACTIVE`; người duyệt nhận thông báo.
- **Đảm bảo tối thiểu**: món chưa duyệt không chọn được khi xếp thực đơn và không được agent dùng.
- **Kích hoạt**: Dinh dưỡng viên chọn "Thêm món".

## Luồng sự kiện chính

1. Dinh dưỡng viên nhập tên, mô tả, chọn vai trò (món chính, món phụ, rau, canh).
2. Dinh dưỡng viên chọn nhóm nguyên liệu chính và phương pháp chế biến.
3. Dinh dưỡng viên khai các thuộc tính còn lại: món gốc (nếu là biến thể), Healthy, vị chua, kết cấu, thanh nhẹ, cầu kỳ, chịu vận chuyển, phù hợp bếp lớn, nhóm cost, đặc thù. Mỗi thuộc tính có chú giải và ví dụ trên màn hình (`NFR-MENU-006`).
4. Dinh dưỡng viên chọn các chất gây dị ứng của món.
5. Dinh dưỡng viên chọn "Lưu nháp".
6. Hệ thống kiểm tên không trùng, cờ Healthy khớp phương pháp, món gốc hợp lệ.
7. Hệ thống cấp mã, lưu món ở trạng thái `DRAFT`, ghi nhật ký.
8. Dinh dưỡng viên lập công thức cho món (`UC-MENU-004`, đến bước gửi duyệt công thức).
9. Dinh dưỡng viên chọn "Gửi duyệt" trên món.
10. Hệ thống kiểm món đủ thuộc tính bắt buộc và có công thức `PENDING` hoặc `ACTIVE`.
11. Hệ thống chuyển món sang `PENDING`, tạo thông báo cho người có quyền `menu.catalog.approve`.

## Các luồng nhánh & ngoại lệ

- **6a. Tên trùng món chưa huỷ** (`BR-CAT-001`): hệ thống báo `ERR-MENU-409-01`; quay lại bước 1.
- **6b. Gắn Healthy nhưng phương pháp không có cờ ít dầu mỡ** (`BR-CAT-006`): hệ thống báo `ERR-MENU-422-04`; quay lại bước 2 hoặc 3.
- **6c. Món gốc khác vai trò, là chính nó, hoặc bản thân là biến thể của món khác** (`BR-CAT-007`): hệ thống báo `ERR-MENU-422-05`; quay lại bước 3.
- **10a. Món chưa có công thức** (`BR-CAT-009`): hệ thống báo `ERR-MENU-422-06`; quay lại bước 8.
- **A1. Người duyệt trả lại món** (sau bước 11, từ `UC-MENU-010`):
  - A1.1. Hệ thống chuyển món về `DRAFT`, thông báo cho Dinh dưỡng viên kèm lý do.
  - A1.2. Dinh dưỡng viên sửa và tiếp tục từ bước 9.
- **A2. Khai cặp món kỵ nhau** (`FR-MENU-DISH-008`):
  - A2.1. Dinh dưỡng viên chọn 2 món và ghi chú.
  - A2.2. Hai món giống nhau → `ERR-MENU-422-07`. Cặp đã tồn tại → `ERR-MENU-409-01`.
- **A3. Thêm phương pháp chế biến mới** (`FR-MENU-DISH-007`): Dinh dưỡng viên nhập tên và 2 cờ (chiên/rán; ít dầu mỡ). Tên trùng → `ERR-MENU-409-01`. Bỏ cờ ít dầu mỡ khi còn món Healthy đang dùng phương pháp đó → `ERR-SYS-409-01` kèm danh sách món (`BR-CAT-020`).
- **A4. Gắn ảnh món** (P1): tệp vượt 10 MB → `ERR-SYS-413-01`; sai loại → `ERR-SYS-415-01`.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-001`, `006`, `007`, `009`; `BR-MENU-003`, `014`; `BR-SEC-008`.

## Điểm mở

- Phương pháp nào được tính là ít dầu mỡ: [H-1]. Danh sách phương pháp chế biến: [H-8]. Danh sách cặp kỵ: [H-4].
- Ai là người duyệt: [O-06].
