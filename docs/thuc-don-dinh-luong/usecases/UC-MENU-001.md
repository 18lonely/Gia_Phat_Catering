# UC-MENU-001: Quản lý nguyên liệu

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: có danh mục nguyên liệu đúng đơn vị để lập công thức.
  - Kế toán: đơn vị mua khớp với chứng từ để nhập giá ở E3.
  - Bếp trưởng: tỷ lệ hao hụt phản ánh đúng thực tế sơ chế.
- **Tiền điều kiện**:
  - Người dùng đã đăng nhập và có quyền `menu.catalog.write`.
  - Đã có ít nhất 1 nhóm nguyên liệu (`FR-MENU-ING-005`).
- **Hậu điều kiện thành công**: nguyên liệu ở trạng thái `ACTIVE`, chọn được khi lập công thức; có bản ghi nhật ký.
- **Đảm bảo tối thiểu**: nếu thất bại, không có nguyên liệu nào được tạo hoặc thay đổi.
- **Kích hoạt**: Dinh dưỡng viên mở danh sách nguyên liệu và chọn "Thêm nguyên liệu".

## Luồng sự kiện chính

1. Dinh dưỡng viên nhập tên, chọn nhóm nguyên liệu, đơn vị mua, đơn vị dùng, hệ số quy đổi, loại bảo quản.
2. Dinh dưỡng viên đánh dấu nguyên liệu có xương hoặc vỏ hay không; nếu có thì nhập tỷ lệ hao hụt.
3. Dinh dưỡng viên đánh dấu nguồn cung ổn định hay không.
4. Dinh dưỡng viên chọn "Lưu".
5. Hệ thống kiểm tên không trùng, hệ số quy đổi hợp lệ, tỷ lệ hao hụt có khi bắt buộc.
6. Hệ thống cấp mã, lưu nguyên liệu ở trạng thái `ACTIVE`, ghi nhật ký.
7. Hệ thống hiển thị nguyên liệu vừa tạo trong danh sách.

## Các luồng nhánh & ngoại lệ

- **5a. Tên trùng nguyên liệu chưa huỷ** (`BR-CAT-001`):
  - 5a1. Hệ thống báo `ERR-MENU-409-01` và hiện nguyên liệu trùng.
  - 5a2. Quay lại bước 1.
- **5b. Hệ số quy đổi ≤ 0, hoặc đơn vị mua là kg, đơn vị dùng là g mà hệ số khác 1000** (`BR-CAT-002`):
  - 5b1. Hệ thống báo `ERR-MENU-422-01` tại ô hệ số.
  - 5b2. Quay lại bước 1.
- **5c. Có xương hoặc vỏ nhưng chưa nhập tỷ lệ hao hụt** (`BR-CAT-003`):
  - 5c1. Hệ thống báo `ERR-MENU-422-02`.
  - 5c2. Quay lại bước 2.
- **A1. Sửa nguyên liệu** (thay cho bước 1–7):
  - A1.1. Dinh dưỡng viên mở nguyên liệu, sửa trường, chọn "Lưu".
  - A1.2. Nếu sửa đơn vị dùng hoặc hệ số quy đổi của nguyên liệu đang nằm trong công thức `ACTIVE`: hệ thống báo `ERR-MENU-409-02` kèm số công thức; không lưu (`BR-CAT-004`).
  - A1.3. Nếu người khác vừa sửa cùng nguyên liệu: hệ thống báo `ERR-SYS-409-02`; người dùng tải lại.
- **A2. Ngừng dùng hoặc huỷ nguyên liệu**:
  - A2.1. Dinh dưỡng viên chọn "Ngừng dùng" và nhập lý do.
  - A2.2. Nếu nguyên liệu đang nằm trong công thức `ACTIVE`: hệ thống báo `ERR-SYS-409-01` kèm danh sách công thức; không đổi trạng thái (`BR-CAT-005`).
  - A2.3. Nếu không: hệ thống chuyển `INACTIVE`, ghi nhật ký.
- **A3. Khai mùa vụ** (P1): Dinh dưỡng viên thêm khoảng tháng; tháng ngoài 1–12 → `ERR-MENU-422-03`.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-001` → `005`, `BR-COST-010`, `BR-AUD-001`.

## Điểm mở

- Danh sách nhóm nguyên liệu khởi tạo: [H-3].
