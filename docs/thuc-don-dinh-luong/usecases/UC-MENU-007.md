# UC-MENU-007: Dựng thực đơn tuần

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ, phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: thấy vi phạm ngay khi đang xếp món, không phải tự rà (URD UN-01).
  - Người duyệt: nhận thực đơn đã qua kiểm tự động.
  - Bếp trưởng: thực đơn chỉ gồm món bếp làm được.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.menu.write`.
  - Có loại suất `ACTIVE`; có món `ACTIVE` đủ các vai trò, có công thức và giá bán hiệu lực cho các ngày của tuần.
- **Hậu điều kiện thành công**: thực đơn ở trạng thái `CHECKED` (đủ món, đủ món mặc định, không còn vi phạm quy tắc cứng), sẵn sàng gửi duyệt.
- **Đảm bảo tối thiểu**: mọi thay đổi đã lưu đều có kết quả kiểm tương ứng; thực đơn chưa đạt ở lại `DRAFT`.
- **Kích hoạt**: Dinh dưỡng viên chọn "Tạo thực đơn tuần".

## Luồng sự kiện chính

1. Dinh dưỡng viên chọn loại suất, tuần (ngày thứ Hai) và các ngày phục vụ trong tuần.
2. Hệ thống kiểm chưa có thực đơn cho loại suất và tuần đó, rồi tạo thực đơn `DRAFT` với các ngày trống. Mỗi ngày có số ô theo cấu hình loại suất.
3. Dinh dưỡng viên chọn một ô của một ngày.
4. Hệ thống liệt kê các món `ACTIVE` có vai trò khớp ô đó, kèm thuộc tính chính và (P1) các ngày món đã xuất hiện trong 4 tuần gần nhất.
5. Dinh dưỡng viên chọn món.
6. Hệ thống gắn công thức hiệu lực tại ngày phục vụ, lưu, rồi chạy `UC-MENU-008`.
7. Hệ thống hiển thị kết quả kiểm: điểm quy tắc, danh sách vi phạm cứng và mềm, mỗi vi phạm chỉ rõ ngày và món.
8. Dinh dưỡng viên lặp bước 3–7 cho đến khi mọi ô có món.
9. Dinh dưỡng viên chọn món mặc định cho từng ngày trong các món chính của ngày.
10. Khi mọi ô đã có món, mọi ngày có món mặc định và không còn vi phạm cứng, hệ thống chuyển thực đơn sang `CHECKED`.

## Các luồng nhánh & ngoại lệ

- **1a. Ngày bắt đầu không phải thứ Hai, hoặc không chọn ngày phục vụ nào**: hệ thống báo `ERR-MENU-422-13`; quay lại bước 1.
- **2a. Đã có thực đơn cho loại suất và tuần đó** (`BR-MNU-001`): hệ thống báo `ERR-MENU-409-06` và mở thực đơn đã có.
- **5a. Món không còn `ACTIVE`, sai vai trò, vượt số ô, hoặc đã có trong ngày** (`BR-MNU-002`, `003`): hệ thống báo `ERR-MENU-422-14`; quay lại bước 4.
- **6a. Món không có công thức hiệu lực tại ngày phục vụ**: hệ thống báo `ERR-MENU-404-01`; món không được xếp.
- **6b. Món không có giá bán hiệu lực tại ngày phục vụ**: hệ thống báo `ERR-MENU-404-02`; món không được xếp.
- **7a. Còn vi phạm quy tắc cứng**: thực đơn ở lại `DRAFT`; Dinh dưỡng viên đổi món (bước 3).
- **7b. Có vi phạm quy tắc mềm mức nặng mà Dinh dưỡng viên muốn giữ**: Dinh dưỡng viên ghi lý do chấp nhận (từ 10 ký tự) cho từng vi phạm (`FR-MENU-RUL-004`). Lý do ngắn hơn → `ERR-SYS-422-01`.
- **9a. Chọn món mặc định không phải món chính của ngày** (`BR-MNU-004`): hệ thống báo `ERR-MENU-422-15`.
- **9b. Bỏ khỏi ngày món đang là mặc định**: hệ thống xoá món mặc định của ngày đó; thực đơn về `DRAFT`.
- **10a. Sửa thực đơn `CHECKED`**: mọi thay đổi chạy lại bước 6–7; nếu phát sinh vi phạm cứng hoặc ô trống, thực đơn về `DRAFT`.
- **A1. Sao chép từ tuần khác** (P1, thay bước 1–2):
  - A1.1. Dinh dưỡng viên chọn thực đơn nguồn cùng loại suất và tuần đích.
  - A1.2. Hệ thống tạo bản `DRAFT`; món không còn `ACTIVE` để trống và được liệt kê. Tiếp tục từ bước 3.
- **A2. Sửa thực đơn không ở `DRAFT` hoặc `CHECKED`**: hệ thống báo `ERR-MENU-409-07`.
- **A3. Huỷ thực đơn nháp**: Dinh dưỡng viên nhập lý do; hệ thống huỷ. Thực đơn đã gửi duyệt trở đi → `ERR-MENU-409-08`.
- **A4. Xuất PDF** (P1): hệ thống tạo tệp ngày × vị trí × tên món.

## Quy tắc nghiệp vụ liên quan

`BR-MNU-001` → `004`; toàn bộ `BR-MENU` và `BR-COST-012` qua `UC-MENU-008`; `BR-AUD-001`.

## Yêu cầu đặc biệt

- Kết quả kiểm hiện trong ≤ 2 giây sau mỗi thay đổi (`NFR-MENU-001`).

## Điểm mở

- Tuần phục vụ gồm những ngày nào: [E2-Q3].
- Một loại suất có một thực đơn chung hay riêng theo khách: [E2-Q4].
- Cách kiểm ngưỡng giá suất ở bước 6: [E2-Q1].
