# UC-MENU-009: Gửi duyệt thực đơn

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: chuyển thực đơn cho người duyệt mà không phải giải thích lại từng cảnh báo.
  - Người duyệt: chỉ nhận thực đơn đủ món, không vi phạm quy tắc cứng, và có lý do cho mọi cảnh báo mức nặng.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.menu.write`.
  - Thực đơn ở trạng thái `DRAFT` hoặc `CHECKED`.
- **Hậu điều kiện thành công**: thực đơn ở trạng thái `PENDING`; nội dung bị khoá; người duyệt nhận thông báo.
- **Đảm bảo tối thiểu**: thực đơn không đạt điều kiện ở lại trạng thái cũ, kèm danh sách việc còn thiếu.
- **Kích hoạt**: Dinh dưỡng viên chọn "Gửi duyệt" trên thực đơn.

## Luồng sự kiện chính

1. Hệ thống chạy lại `UC-MENU-008` để có kết quả kiểm mới nhất.
2. Hệ thống kiểm mọi ô của mọi ngày đã có món, mọi ngày có món mặc định, mọi món còn `ACTIVE`.
3. Hệ thống kiểm không còn quy tắc cứng nào không đạt.
4. Hệ thống kiểm mọi quy tắc mềm mức nặng không đạt đều có lý do chấp nhận.
5. Hệ thống chạy các bộ kiểm khác đã đăng ký (R2: không có; R3: kiểm cost).
6. Hệ thống xác định số người duyệt cần có: 1, hoặc 2 nếu điểm quy tắc dưới tham số `QUY_TAC_DIEM_TOI_THIEU`.
7. Hệ thống chuyển thực đơn sang `PENDING`, tăng số vòng duyệt, ghi nhật ký.
8. Hệ thống tạo thông báo cho những người có quyền `menu.menu.approve`.
9. Hệ thống hiển thị thực đơn ở chế độ chỉ đọc kèm trạng thái "chờ duyệt (0/1)" hoặc "(0/2)".

## Các luồng nhánh & ngoại lệ

- **2a. Còn ô trống, thiếu món mặc định, hoặc có món không còn `ACTIVE`** (`BR-MNU-005`): hệ thống báo `ERR-MENU-422-17` kèm danh sách; thực đơn về `DRAFT`.
- **3a. Còn vi phạm quy tắc cứng** (`BR-MNU-005`): hệ thống báo `ERR-MENU-422-18` kèm số vi phạm; thực đơn về `DRAFT`.
- **4a. Vi phạm mềm mức nặng chưa có lý do** (`BR-MNU-006`): hệ thống báo `ERR-MENU-422-19`; Dinh dưỡng viên ghi lý do rồi gửi lại.
- **5a. Bộ kiểm đăng ký thêm báo không đạt** (từ R3): thực đơn ở lại trạng thái cũ kèm thông báo của bộ kiểm đó.
- **A1. Người duyệt trả lại** (từ `UC-MENU-010`): thực đơn về `DRAFT`; Dinh dưỡng viên nhận thông báo kèm lý do, sửa theo `UC-MENU-007` và gửi lại. Vòng duyệt mới bắt đầu từ 0.
- **A2. Dinh dưỡng viên muốn sửa khi đang `PENDING`**: không sửa trực tiếp được (`ERR-MENU-409-07`); phải chờ kết quả duyệt.

## Quy tắc nghiệp vụ liên quan

`BR-MNU-005`, `006`, `008`; `BR-SEC-008`.

## Điểm mở

- Có cho Dinh dưỡng viên rút lại thực đơn đang `PENDING` để sửa không? SRS hiện không cho; nêu để người duyệt nghiệp vụ quyết: [E2-Q6].
- Ngưỡng điểm 80 là [ĐỀ XUẤT].
