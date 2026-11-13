# UC-MENU-013: Sửa danh mục quy tắc

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: điều chỉnh được con số của quy tắc khi thực tế thay đổi, không cần sửa phần mềm.
  - Người duyệt: quy chuẩn thực đơn không bị nới lỏng mà không ai biết.
  - Agent (R5, R9): luôn dùng đúng bộ quy tắc hiện hành.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.rule.write`.
  - Quy tắc cần sửa không có đề nghị nào đang chờ duyệt.
- **Hậu điều kiện thành công**: có 1 đề nghị thay đổi `PENDING` cho quy tắc; quy tắc giữ giá trị cũ cho đến khi duyệt.
- **Đảm bảo tối thiểu**: bộ kiểm tiếp tục chạy bằng giá trị cũ.
- **Kích hoạt**: Dinh dưỡng viên mở danh mục quy tắc và chọn "Sửa" trên một quy tắc.

## Luồng sự kiện chính

1. Hệ thống hiển thị quy tắc: mã, tên, câu gốc trong file quy chuẩn, loại (cứng/mềm), điểm phạt, phạm vi (ngày/tuần), tham số, trạng thái bật/tắt.
2. Dinh dưỡng viên sửa một hoặc nhiều mục: bật/tắt, loại, điểm phạt, giá trị tham số.
3. Dinh dưỡng viên nhập lý do (từ 10 ký tự) và chọn "Gửi đề nghị".
4. Hệ thống kiểm giá trị mới hợp lệ.
5. Hệ thống tạo đề nghị thay đổi `PENDING` với giá trị cũ – mới, ghi nhật ký.
6. Hệ thống tạo thông báo cho người có quyền `menu.rule.approve`.

## Các luồng nhánh & ngoại lệ

- **3a. Thiếu lý do hoặc lý do dưới 10 ký tự** (`BR-AUD-001`): `ERR-SYS-422-01`; quay lại bước 3.
- **4a. Điểm phạt quy tắc mềm ngoài 1–3, quy tắc cứng có điểm phạt khác 0, hoặc tham số số học âm** (`BR-MNU-007`): `ERR-MENU-422-16`; quay lại bước 2.
- **A1. Đề nghị được duyệt** (từ `UC-MENU-010`):
  - A1.1. Hệ thống ghi giá trị mới vào quy tắc.
  - A1.2. Thực đơn `DRAFT` và `CHECKED` dùng quy tắc mới từ lần kiểm kế tiếp; thực đơn `CHECKED` có thể rơi về `DRAFT` nếu phát sinh vi phạm cứng.
  - A1.3. Thực đơn từ `PENDING` trở đi giữ kết quả đã có.
- **A2. Đề nghị bị trả lại**: quy tắc không đổi; Dinh dưỡng viên nhận thông báo kèm lý do.
- **A3. Người đề nghị cố tự duyệt** (`BR-SEC-008`): `ERR-SYS-403-01`.

## Quy tắc nghiệp vụ liên quan

`BR-MNU-007`; `BR-SEC-008`; `BR-AUD-001`.

## Ghi chú

- Không có chức năng **thêm quy tắc mới** qua giao diện: mỗi quy tắc là một đoạn mã kiểm; giao diện chỉ đổi được bật/tắt, loại, điểm phạt và tham số của quy tắc đã có. Thêm quy tắc mới là một thay đổi phần mềm.
- Danh mục ban đầu được nạp từ bảng quy tắc sau khi DL-01 duyệt.

## Điểm mở

- Thực đơn đang `PENDING` có nên kiểm lại khi quy tắc đổi không: SRS hiện giữ kết quả cũ. Nêu để người duyệt nghiệp vụ quyết: [E2-Q11].
