# UC-MENU-010: Duyệt nội dung chờ duyệt

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Người duyệt (vai trò `GIAM_DOC` hoặc người được uỷ quyền).
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Người duyệt: thấy mọi thứ chờ mình ở một chỗ, duyệt được nhiều mục một lần, không trở thành điểm nghẽn (rủi ro E2-R4).
  - Dinh dưỡng viên: biết kết quả và lý do ngay.
  - Kiểm soát nội bộ: người tạo không tự duyệt; mọi quyết định truy vết được.
- **Tiền điều kiện**:
  - Người dùng có quyền duyệt tương ứng với loại nội dung (`menu.catalog.approve`, `menu.price.approve`, `menu.menu.approve`, `menu.rule.approve`), trực tiếp hoặc qua uỷ quyền còn hạn.
  - Có ít nhất một mục ở trạng thái chờ duyệt.
- **Hậu điều kiện thành công**: mục được duyệt chuyển sang trạng thái có hiệu lực, hoặc mục bị trả lại quay về người tạo kèm lý do; có một dòng quyết định cho mỗi mục; người tạo nhận thông báo.
- **Đảm bảo tối thiểu**: không mục nào đổi trạng thái nếu quyết định không hợp lệ.
- **Kích hoạt**: Người duyệt mở thông báo hoặc mở trang "Chờ duyệt".

## Luồng sự kiện chính

1. Hệ thống liệt kê các mục chờ duyệt mà người dùng có quyền duyệt, nhóm theo loại: món, công thức, giá bán, đề nghị thay đổi (thuộc tính món, quy tắc), thực đơn.
2. Người duyệt mở một mục.
3. Hệ thống hiển thị nội dung theo loại:
   - Món: thuộc tính và công thức đi kèm.
   - Công thức: các dòng định lượng; nếu là phiên bản mới thì kèm so sánh với phiên bản đang hiệu lực.
   - Giá bán: giá mới, ngày hiệu lực, giá đang hiệu lực.
   - Đề nghị thay đổi: bảng giá trị cũ – mới và lý do.
   - Thực đơn: lưới ngày × vị trí, điểm quy tắc, danh sách cảnh báo kèm lý do chấp nhận.
4. Người duyệt chọn "Duyệt".
5. Hệ thống kiểm người duyệt khác người tạo và khác người sửa cuối của mục.
6. Hệ thống ghi một dòng quyết định (người duyệt, vòng duyệt, thời điểm; kèm uỷ quyền nếu dùng).
7. Hệ thống chuyển trạng thái theo loại:
   - Món: `PENDING` → `ACTIVE`.
   - Công thức: `PENDING` → `ACTIVE` (phiên bản cũ xử lý theo `UC-MENU-004` nhánh A3).
   - Giá bán: `PENDING` → `APPROVED`.
   - Đề nghị thay đổi: ghi giá trị mới vào bản ghi gốc; đề nghị → `APPROVED`.
   - Thực đơn: `PENDING` → `APPROVED` khi đủ số người duyệt; kết quả kiểm và công thức đã gắn bị đóng băng.
8. Hệ thống ghi nhật ký và tạo thông báo cho người tạo.

## Các luồng nhánh & ngoại lệ

- **4a. Người duyệt chọn "Trả lại"**:
  - 4a1. Người duyệt nhập lý do (bắt buộc; thiếu → `ERR-SYS-422-01`).
  - 4a2. Hệ thống ghi dòng quyết định từ chối. Món, công thức, thực đơn về `DRAFT`; giá bán và đề nghị thay đổi chuyển `REJECTED`.
  - 4a3. Hệ thống thông báo cho người tạo kèm lý do.
- **4b. Duyệt nhiều mục một lần**: Người duyệt chọn nhiều mục cùng loại trong danh sách rồi chọn "Duyệt". Hệ thống xử lý từng mục theo bước 5–8 và báo số mục thành công, số mục lỗi kèm lý do từng mục.
- **5a. Người duyệt là người tạo hoặc người sửa cuối** (`BR-SEC-008`): hệ thống báo `ERR-SYS-403-01`; mục không đổi.
- **5b. Uỷ quyền đã hết hạn hoặc không gồm quyền này**: hệ thống báo `ERR-AUTH-403-02`.
- **7a. Duyệt món mà món chưa có công thức `ACTIVE` và không có công thức nào được duyệt cùng lần** (`BR-CAT-009`): hệ thống báo `ERR-MENU-422-06`; món không đổi.
- **7b. Thực đơn cần 2 người duyệt và đây là người thứ nhất** (`BR-MNU-008`): thực đơn ở lại `PENDING` với trạng thái "đã duyệt 1/2"; người duyệt thứ nhất không duyệt lần hai được.
- **7c. Đề nghị thay đổi đã lỗi thời** (bản ghi gốc đã đổi sau khi đề nghị): hệ thống chuyển đề nghị sang `STALE`, thông báo người đề nghị gửi lại.
- **7d. Mục đã được người khác xử lý trong lúc đang xem**: hệ thống báo `ERR-SYS-409-02` và tải lại trạng thái hiện tại.

## Quy tắc nghiệp vụ liên quan

`BR-SEC-008`; `BR-CAT-009`, `013`, `014`, `016`; `BR-MNU-008`; `BR-AUD-001`.

## Ghi chú thiết kế

Dòng quyết định lưu ở bảng `approvals`; đề nghị thay đổi ở `change_requests` (ERD v0.2.0 mục 3.5).

## Điểm mở

- Ai là người duyệt và ai thay khi vắng: [O-06]. Nếu Gia Phát chỉ có một người duyệt, quy tắc 2 người duyệt (`BR-MNU-008`) không thực hiện được và cần bỏ hoặc đổi.
- Có cần phân biệt người duyệt nghiệp vụ (món, công thức, thực đơn) với người duyệt giá không: [E2-Q7].
