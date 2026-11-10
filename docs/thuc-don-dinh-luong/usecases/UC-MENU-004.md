# UC-MENU-004: Lập công thức và phiên bản mới

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Dinh dưỡng viên.
- **Phạm vi**: Trang quản trị nội bộ — phân hệ MENU.
- **Cấp độ**: Sea level.
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: ghi lại định lượng sống của từng món theo bảng chuẩn.
  - Người duyệt: định lượng quyết định cost, nên không ai tự duyệt công thức của mình.
  - Kế toán, bếp trưởng: công thức đã dùng cho một ngày không đổi về sau, để dự toán và sản xuất đối chiếu được.
- **Tiền điều kiện**:
  - Người dùng có quyền `menu.catalog.write`.
  - Món đã tồn tại (`DRAFT`, `PENDING` hoặc `ACTIVE`); nguyên liệu cần dùng ở trạng thái `ACTIVE`.
- **Hậu điều kiện thành công**: công thức ở trạng thái `PENDING` với số phiên bản kế tiếp; người duyệt nhận thông báo.
- **Đảm bảo tối thiểu**: công thức `ACTIVE` hiện có không bị thay đổi.
- **Kích hoạt**: Dinh dưỡng viên mở một món và chọn "Thêm công thức", hoặc chọn "Tạo phiên bản mới" trên công thức đang hiệu lực.

## Luồng sự kiện chính

1. Dinh dưỡng viên chọn ngày hiệu lực.
2. Dinh dưỡng viên thêm từng dòng: chọn nguyên liệu, đánh dấu có phải nguyên liệu chính, nhập định lượng tối thiểu, tối đa và chuẩn. Hệ thống tự điền đơn vị theo đơn vị dùng của nguyên liệu.
3. Dinh dưỡng viên chọn "Lưu nháp".
4. Hệ thống kiểm cấu trúc công thức, khoảng định lượng, và nguyên liệu chính khớp nhóm của món.
5. Hệ thống lưu công thức `DRAFT` với số phiên bản kế tiếp của món và cỡ định lượng, ghi nhật ký.
6. Dinh dưỡng viên chọn "Gửi duyệt".
7. Hệ thống chuyển công thức sang `PENDING`, tạo thông báo cho người có quyền `menu.catalog.approve`.

## Các luồng nhánh & ngoại lệ

- **4a. Không có dòng nào, không có nguyên liệu chính, lặp nguyên liệu, hoặc nguyên liệu không còn `ACTIVE`** (`BR-CAT-010`): hệ thống báo `ERR-MENU-422-08`; quay lại bước 2.
- **4b. Định lượng không thoả tối thiểu ≤ chuẩn ≤ tối đa, hoặc ≤ 0** (`BR-CAT-011`): hệ thống báo `ERR-MENU-422-09` tại dòng sai; quay lại bước 2.
- **4c. Món chính hoặc món phụ mà không có nguyên liệu chính nào thuộc nhóm của món** (`BR-CAT-012`): hệ thống báo `ERR-MENU-422-10`; quay lại bước 2.
- **4d. Ngày hiệu lực ở quá khứ, hoặc không sau ngày hiệu lực của phiên bản đang hiệu lực hay đang chờ duyệt** (`BR-CAT-022`): hệ thống báo `ERR-MENU-422-21`; quay lại bước 1.
- **4e. Định lượng có quá 3 chữ số thập phân** (`BR-CAT-021`): hệ thống báo `ERR-MENU-422-09`; quay lại bước 2.
- **A1. Tạo phiên bản mới từ công thức đang hiệu lực** (thay bước 1–2):
  - A1.1. Dinh dưỡng viên chọn "Tạo phiên bản mới", nhập lý do và ngày hiệu lực.
  - A1.2. Hệ thống sao chép các dòng sang bản `DRAFT` mới. Tiếp tục từ bước 2.
- **A2. Sửa công thức đã gửi duyệt hoặc đã duyệt** (`BR-CAT-013`): hệ thống báo `ERR-MENU-409-03` và gợi ý tạo phiên bản mới.
- **A3. Công thức được duyệt** (từ `UC-MENU-010`):
  - A3.1. Nếu ngày hiệu lực ≤ hôm nay: công thức mới chuyển `ACTIVE`; phiên bản `ACTIVE` trước đó cùng món, cùng cỡ chuyển `SUPERSEDED`.
  - A3.2. Nếu ngày hiệu lực ở tương lai: cả hai cùng `ACTIVE`; bộ hẹn giờ chuyển phiên bản cũ sang `SUPERSEDED` vào ngày hiệu lực.
  - A3.3. Thực đơn đã gắn phiên bản cũ giữ nguyên phiên bản đó.
- **A4. Công thức bị trả lại**: công thức về `DRAFT`, Dinh dưỡng viên sửa được và gửi lại.
- **A5. So sánh hai phiên bản** (P1): hệ thống hiện dòng thêm, bớt, đổi định lượng.

## Quy tắc nghiệp vụ liên quan

`BR-CAT-010` → `014`; `BR-COST-008`, `009`; `BR-SEC-008`; `BR-AUD-001`.

## Điểm mở

- Một món có một hay nhiều cỡ định lượng: [O-02]. Nếu nhiều cỡ, bước 1 thêm việc chọn cỡ.
- Khoảng định lượng chuẩn và mức chất độn cho phép lấy từ đâu: [E2-Q5]. Nếu có bảng chuẩn bắt buộc, bước 4 thêm một nhánh kiểm.
- Tỷ lệ hao hụt có cộng vào định lượng khi tính cost không: chờ xác nhận (ERD mục 5.3).
