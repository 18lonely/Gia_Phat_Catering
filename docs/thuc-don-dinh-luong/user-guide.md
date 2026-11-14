---
id: DOC-THUC-DON-USER-GUIDE
title: Hướng dẫn vận hành E2
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e2]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E2: Thực đơn và định lượng

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Dinh dưỡng viên, người duyệt. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-MENU-001: Quản lý nguyên liệu

[Use case gốc](usecases/UC-MENU-001.md)

1. Dinh dưỡng viên nhập tên, chọn nhóm nguyên liệu, đơn vị mua, đơn vị dùng, hệ số quy đổi, loại bảo quản.
2. Dinh dưỡng viên đánh dấu nguyên liệu có xương hoặc vỏ hay không; nếu có thì nhập tỷ lệ hao hụt.
3. Dinh dưỡng viên đánh dấu nguồn cung ổn định hay không.
4. Dinh dưỡng viên chọn "Lưu".
5. Hệ thống kiểm tên không trùng, hệ số quy đổi hợp lệ, tỷ lệ hao hụt có khi bắt buộc.
6. Hệ thống cấp mã, lưu nguyên liệu ở trạng thái `ACTIVE`, ghi nhật ký.
7. Hệ thống hiển thị nguyên liệu vừa tạo trong danh sách.

Khi gặp nhánh rẽ hoặc lỗi:

- 5a. Tên trùng nguyên liệu chưa huỷ** (`BR-CAT-001`):
- 5b. Hệ số quy đổi ≤ 0, hoặc đơn vị mua là kg, đơn vị dùng là g mà hệ số khác 1000** (`BR-CAT-002`):
- 5c. Có xương hoặc vỏ nhưng chưa nhập tỷ lệ hao hụt** (`BR-CAT-003`):

### UC-MENU-002: Tạo món và gửi duyệt

[Use case gốc](usecases/UC-MENU-002.md)

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

Khi gặp nhánh rẽ hoặc lỗi:

- 6a. Tên trùng món chưa huỷ** (`BR-CAT-001`): hệ thống báo `ERR-MENU-409-01`; quay lại bước 1.
- 6b. Gắn Healthy nhưng phương pháp không có cờ ít dầu mỡ** (`BR-CAT-006`): hệ thống báo `ERR-MENU-422-04`; quay lại bước 2 hoặc 3.
- 6c. Món gốc khác vai trò, là chính nó, hoặc bản thân là biến thể của món khác** (`BR-CAT-007`): hệ thống báo `ERR-MENU-422-05`; quay lại bước 3.
- 10a. Món chưa có công thức** (`BR-CAT-009`): hệ thống báo `ERR-MENU-422-06`; quay lại bước 8.

### UC-MENU-003: Sửa thuộc tính món đang dùng

[Use case gốc](usecases/UC-MENU-003.md)

1. Dinh dưỡng viên sửa một hoặc nhiều thuộc tính ảnh hưởng quy tắc (danh sách ở `BR-CAT-008`).
2. Dinh dưỡng viên nhập lý do (từ 10 ký tự) và chọn "Gửi đề nghị".
3. Hệ thống kiểm giá trị mới theo đúng các ràng buộc khi tạo món (Healthy khớp phương pháp, món gốc hợp lệ).
4. Hệ thống tạo đề nghị thay đổi `PENDING`, lưu giá trị cũ và mới của từng trường; món giữ nguyên giá trị cũ.
5. Hệ thống tạo thông báo cho người có quyền `menu.catalog.approve`.
6. Hệ thống hiển thị món với nhãn "chờ duyệt thay đổi" và bảng so sánh cũ – mới.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Chỉ sửa trường không ảnh hưởng quy tắc** (tên, mô tả, ảnh, chất gây dị ứng):
- 2a. Thiếu lý do hoặc lý do dưới 10 ký tự** (`BR-AUD-001`): hệ thống báo `ERR-SYS-422-01`; quay lại bước 2.
- 3a. Giá trị mới vi phạm ràng buộc**: hệ thống báo `ERR-MENU-422-04` hoặc `ERR-MENU-422-05`; quay lại bước 1.
- 3b. Người khác vừa sửa món** (lệch phiên bản): hệ thống báo `ERR-SYS-409-02`; người dùng tải lại.

### UC-MENU-004: Lập công thức và phiên bản mới

[Use case gốc](usecases/UC-MENU-004.md)

1. Dinh dưỡng viên chọn ngày hiệu lực.
2. Dinh dưỡng viên thêm từng dòng: chọn nguyên liệu, đánh dấu có phải nguyên liệu chính, nhập định lượng tối thiểu, tối đa và chuẩn. Hệ thống tự điền đơn vị theo đơn vị dùng của nguyên liệu.
3. Dinh dưỡng viên chọn "Lưu nháp".
4. Hệ thống kiểm cấu trúc công thức, khoảng định lượng, và nguyên liệu chính khớp nhóm của món.
5. Hệ thống lưu công thức `DRAFT` với số phiên bản kế tiếp của món và cỡ định lượng, ghi nhật ký.
6. Dinh dưỡng viên chọn "Gửi duyệt".
7. Hệ thống chuyển công thức sang `PENDING`, tạo thông báo cho người có quyền `menu.catalog.approve`.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Không có dòng nào, không có nguyên liệu chính, lặp nguyên liệu, hoặc nguyên liệu không còn `ACTIVE`** (`BR-CAT-010`): hệ thống báo `ERR-MENU-422-08`; quay lại bước 2.
- 4b. Định lượng không thoả tối thiểu ≤ chuẩn ≤ tối đa, hoặc ≤ 0** (`BR-CAT-011`): hệ thống báo `ERR-MENU-422-09` tại dòng sai; quay lại bước 2.
- 4c. Món chính hoặc món phụ mà không có nguyên liệu chính nào thuộc nhóm của món** (`BR-CAT-012`): hệ thống báo `ERR-MENU-422-10`; quay lại bước 2.
- 4d. Ngày hiệu lực ở quá khứ, hoặc không sau ngày hiệu lực của phiên bản đang hiệu lực hay đang chờ duyệt** (`BR-CAT-022`): hệ thống báo `ERR-MENU-422-21`; quay lại bước 1.
- 4e. Định lượng có quá 3 chữ số thập phân** (`BR-CAT-021`): hệ thống báo `ERR-MENU-422-09`; quay lại bước 2.

### UC-MENU-005: Đặt giá bán món

[Use case gốc](usecases/UC-MENU-005.md)

1. Dinh dưỡng viên nhập giá bán (đã gồm VAT) và ngày hiệu lực.
2. Dinh dưỡng viên chọn "Gửi duyệt".
3. Hệ thống kiểm giá là số nguyên không âm, bội số của 100 đồng, và ngày hiệu lực sau hôm nay.
4. Hệ thống kiểm chưa có giá nào cho cùng món, cùng cỡ, cùng ngày hiệu lực.
5. Hệ thống lưu giá ở trạng thái `PENDING`, ghi nhật ký, tạo thông báo cho người có quyền `menu.price.approve`.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Giá không hợp lệ hoặc ngày hiệu lực không sau hôm nay** (`BR-CAT-015`, `016`): hệ thống báo `ERR-MENU-422-11`; quay lại bước 1.
- 4a. Đã có giá cho ngày hiệu lực đó**: hệ thống báo `ERR-MENU-409-04`; quay lại bước 1.

### UC-MENU-006: Tạo loại suất

[Use case gốc](usecases/UC-MENU-006.md)

1. Dinh dưỡng viên nhập tên và ngưỡng giá (đã gồm VAT).
2. Dinh dưỡng viên nhập số món chính đưa ra để chọn (mặc định 3), số món chính mỗi người được chọn (mặc định 1), số món phụ.
3. Dinh dưỡng viên chọn suất có rau, có canh hay không.
4. Dinh dưỡng viên chọn "Lưu".
5. Hệ thống kiểm tên không trùng và cấu hình hợp lệ.
6. Hệ thống cấp mã, lưu loại suất ở trạng thái `DRAFT`, ghi nhật ký.
7. Dinh dưỡng viên chọn "Kích hoạt".
8. Hệ thống chuyển loại suất sang `ACTIVE`.

Khi gặp nhánh rẽ hoặc lỗi:

- 5a. Tên trùng** (`BR-CAT-001`): hệ thống báo `ERR-MENU-409-01`; quay lại bước 1.
- 5b. Ngưỡng giá ≤ 0, số món chính được chọn lớn hơn số đưa ra hoặc nhỏ hơn 1, số món phụ ngoài 0–5** (`BR-CAT-017`): hệ thống báo `ERR-MENU-422-12`; quay lại bước 1–3.

### UC-MENU-007: Dựng thực đơn tuần

[Use case gốc](usecases/UC-MENU-007.md)

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

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Ngày bắt đầu không phải thứ Hai, hoặc không chọn ngày phục vụ nào**: hệ thống báo `ERR-MENU-422-13`; quay lại bước 1.
- 2a. Đã có thực đơn cho loại suất và tuần đó** (`BR-MNU-001`): hệ thống báo `ERR-MENU-409-06` và mở thực đơn đã có.
- 5a. Món không còn `ACTIVE`, sai vai trò, vượt số ô, hoặc đã có trong ngày** (`BR-MNU-002`, `003`): hệ thống báo `ERR-MENU-422-14`; quay lại bước 4.
- 6a. Món không có công thức hiệu lực tại ngày phục vụ**: hệ thống báo `ERR-MENU-404-01`; món không được xếp.
- 6b. Món không có giá bán hiệu lực tại ngày phục vụ**: hệ thống báo `ERR-MENU-404-02`; món không được xếp.
- 7a. Còn vi phạm quy tắc cứng**: thực đơn ở lại `DRAFT`; Dinh dưỡng viên đổi món (bước 3).
- 7b. Có vi phạm quy tắc mềm mức nặng mà Dinh dưỡng viên muốn giữ**: Dinh dưỡng viên ghi lý do chấp nhận (từ 10 ký tự) cho từng vi phạm (`FR-MENU-RUL-004`). Lý do ngắn hơn → `ERR-SYS-422-01`.
- 9a. Chọn món mặc định không phải món chính của ngày** (`BR-MNU-004`): hệ thống báo `ERR-MENU-422-15`.
- 9b. Bỏ khỏi ngày món đang là mặc định**: hệ thống xoá món mặc định của ngày đó; thực đơn về `DRAFT`.
- 10a. Sửa thực đơn `CHECKED`**: mọi thay đổi chạy lại bước 6–7; nếu phát sinh vi phạm cứng hoặc ô trống, thực đơn về `DRAFT`.

### UC-MENU-008: Kiểm quy tắc thực đơn

[Use case gốc](usecases/UC-MENU-008.md)

1. Hệ thống nạp thực đơn: loại suất, các ngày phục vụ, món ở từng ô kèm thuộc tính hiện hành của món.
2. Hệ thống nạp danh mục quy tắc đang bật cùng tham số.
3. Hệ thống nạp các ngày phục vụ liền trước tuần đó của cùng loại suất, nếu quy tắc cần.
4. Với mỗi ngày, hệ thống chạy các quy tắc cấp ngày.
5. Hệ thống chạy các quy tắc cấp tuần trên toàn thực đơn.
6. Với mỗi quy tắc không đạt, hệ thống ghi: mã, tên, loại, ngày liên quan, món liên quan, giá trị đo được, giới hạn.
7. Hệ thống tính điểm: 100 trừ tổng điểm phạt của các quy tắc mềm không đạt, sàn là 0. Quy tắc cấp ngày không đạt ở nhiều ngày bị trừ mỗi ngày một lần.
8. Hệ thống đặt cờ "còn vi phạm cứng" nếu có ít nhất một quy tắc cứng không đạt.
9. Hệ thống ghi kết quả (nếu thực đơn đã lưu) và trả về cho nơi gọi.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Ngày chưa đủ món**: các quy tắc về cơ cấu (`BR-MENU-001`, `002`, `004`, `005`) báo không đạt; các quy tắc khác chỉ xét món đã có. Use case tiếp tục.
- 1b. Lời gọi cho thực đơn chưa lưu chứa món không tồn tại, không `ACTIVE`, hoặc sai vai trò**: hệ thống báo `ERR-MENU-422-14`; kết thúc.
- 1c. Món không có giá bán hiệu lực tại ngày phục vụ** (cần cho `BR-COST-012`): quy tắc đó báo không đạt kèm `ERR-MENU-404-02`. Use case tiếp tục.
- 3a. Không có thực đơn tuần trước**: quy tắc xét ngày liền trước chỉ tính trong tuần hiện tại.
- 9a. Lần kiểm này làm một quy tắc mềm mức nặng chuyển từ không đạt sang đạt**: hệ thống xoá lý do chấp nhận đã ghi cho quy tắc đó.
- 9b. Thực đơn ở trạng thái `PENDING`, `APPROVED`, `PUBLISHED` hoặc `WITHDRAWN`**: hệ thống trả kết quả đã có lúc gửi duyệt, không chạy lại ([E2-Q11]).

### UC-MENU-009: Gửi duyệt thực đơn

[Use case gốc](usecases/UC-MENU-009.md)

1. Hệ thống chạy lại `UC-MENU-008` để có kết quả kiểm mới nhất.
2. Hệ thống kiểm mọi ô của mọi ngày đã có món, mọi ngày có món mặc định, mọi món còn `ACTIVE`.
3. Hệ thống kiểm không còn quy tắc cứng nào không đạt.
4. Hệ thống kiểm mọi quy tắc mềm mức nặng không đạt đều có lý do chấp nhận.
5. Hệ thống chạy các bộ kiểm khác đã đăng ký (R2: không có; R3: kiểm cost).
6. Hệ thống xác định số người duyệt cần có: 1, hoặc 2 nếu điểm quy tắc dưới tham số `QUY_TAC_DIEM_TOI_THIEU`.
7. Hệ thống chuyển thực đơn sang `PENDING`, tăng số vòng duyệt, ghi nhật ký.
8. Hệ thống tạo thông báo cho những người có quyền `menu.menu.approve`.
9. Hệ thống hiển thị thực đơn ở chế độ chỉ đọc kèm trạng thái "chờ duyệt (0/1)" hoặc "(0/2)".

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Còn ô trống, thiếu món mặc định, hoặc có món không còn `ACTIVE`** (`BR-MNU-005`): hệ thống báo `ERR-MENU-422-17` kèm danh sách; thực đơn về `DRAFT`.
- 3a. Còn vi phạm quy tắc cứng** (`BR-MNU-005`): hệ thống báo `ERR-MENU-422-18` kèm số vi phạm; thực đơn về `DRAFT`.
- 4a. Vi phạm mềm mức nặng chưa có lý do** (`BR-MNU-006`): hệ thống báo `ERR-MENU-422-19`; Dinh dưỡng viên ghi lý do rồi gửi lại.
- 5a. Bộ kiểm đăng ký thêm báo không đạt** (từ R3): thực đơn ở lại trạng thái cũ kèm thông báo của bộ kiểm đó.

### UC-MENU-010: Duyệt nội dung chờ duyệt

[Use case gốc](usecases/UC-MENU-010.md)

1. Hệ thống liệt kê các mục chờ duyệt mà người dùng có quyền duyệt, nhóm theo loại: món, công thức, giá bán, đề nghị thay đổi (thuộc tính món, quy tắc), thực đơn.
2. Người duyệt mở một mục.
3. Hệ thống hiển thị nội dung theo loại:

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Người duyệt chọn "Trả lại"**:
- 4b. Duyệt nhiều mục một lần**: Người duyệt chọn nhiều mục cùng loại trong danh sách rồi chọn "Duyệt". Hệ thống xử lý từng mục theo bước 5–8 và báo số mục thành công, số mục lỗi kèm lý do từng mục.
- 5a. Người duyệt là người tạo hoặc người sửa cuối** (`BR-SEC-008`): hệ thống báo `ERR-SYS-403-01`; mục không đổi.
- 5b. Uỷ quyền đã hết hạn hoặc không gồm quyền này**: hệ thống báo `ERR-AUTH-403-02`.
- 7a. Duyệt món mà món chưa có công thức `ACTIVE` và không có công thức nào được duyệt cùng lần** (`BR-CAT-009`): hệ thống báo `ERR-MENU-422-06`; món không đổi.
- 7b. Thực đơn cần 2 người duyệt và đây là người thứ nhất** (`BR-MNU-008`): thực đơn ở lại `PENDING` với trạng thái "đã duyệt 1/2"; người duyệt thứ nhất không duyệt lần hai được.
- 7c. Đề nghị thay đổi đã lỗi thời** (bản ghi gốc đã đổi sau khi đề nghị): hệ thống chuyển đề nghị sang `STALE`, thông báo người đề nghị gửi lại.
- 7d. Mục đã được người khác xử lý trong lúc đang xem**: hệ thống báo `ERR-SYS-409-02` và tải lại trạng thái hiện tại.

### UC-MENU-011: Công bố và thu hồi thực đơn

[Use case gốc](usecases/UC-MENU-011.md)

1. Hệ thống kiểm ngày phục vụ đầu tiên của thực đơn sau hôm nay.
2. Hệ thống chuyển thực đơn sang `PUBLISHED`, ghi thời điểm công bố và nhật ký.
3. Hệ thống tạo thông báo cho quản lý cơ sở và bếp trưởng.
4. Hệ thống hiển thị thực đơn ở chế độ chỉ đọc với nhãn "đã công bố".

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Ngày phục vụ đầu tiên là hôm nay hoặc đã qua** (`BR-MNU-009`): hệ thống báo `ERR-MENU-409-09`. Dinh dưỡng viên thu hồi về nháp, bỏ các ngày đã qua và gửi duyệt lại.

### UC-MENU-012: Nhập dữ liệu từ bảng tính

[Use case gốc](usecases/UC-MENU-012.md)

1. Dinh dưỡng viên chọn loại dữ liệu (nguyên liệu, món, công thức, giá bán) và tải mẫu `.xlsx`.
2. Dinh dưỡng viên điền mẫu ngoài hệ thống. Mẫu có dòng tiêu đề, dòng ví dụ, và trang liệt kê giá trị hợp lệ của các cột liệt kê.
3. Dinh dưỡng viên tải tệp đã điền lên và chọn "Kiểm tra".
4. Hệ thống đọc tệp và kiểm từng dòng theo đúng các quy tắc của chức năng tạo tương ứng, kể cả trùng lặp giữa các dòng trong tệp.
5. Hệ thống hiển thị số dòng hợp lệ và không có lỗi nào.
6. Dinh dưỡng viên chọn "Nhập".
7. Hệ thống ghi toàn bộ dòng trong một giao dịch, cấp mã, ghi nhật ký.
8. Hệ thống báo số bản ghi đã tạo theo từng trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Tệp vượt 10 MB**: `ERR-SYS-413-01`. **Tệp không phải `.xlsx`**: `ERR-SYS-415-01`.
- 4a. Tệp sai mẫu (thiếu hoặc sai cột tiêu đề) hoặc vượt 2.000 dòng**: hệ thống báo `ERR-MENU-422-20` và nêu lý do; quay lại bước 2.
- 4b. Có dòng lỗi**:
- 4c. Dòng tham chiếu bản ghi chưa có** (món tham chiếu nhóm nguyên liệu không tồn tại; công thức tham chiếu món hoặc nguyên liệu không tồn tại): tính là lỗi của dòng đó, xử lý như 4b.
- 4d. Dòng trùng bản ghi đã có trong hệ thống** (cùng tên): tính là lỗi; hệ thống không tự cập nhật bản ghi cũ.
- 4e. Việc kiểm mất hơn 5 giây**: hệ thống chạy qua tác vụ nền, hiện tiến độ, và thông báo khi xong (`NFR-MENU-003`).
- 7a. Dữ liệu trong hệ thống thay đổi giữa lúc kiểm và lúc nhập làm phát sinh lỗi**: hệ thống huỷ toàn bộ giao dịch, báo `ERR-MENU-422-20`; Dinh dưỡng viên kiểm lại từ bước 3.

### UC-MENU-013: Sửa danh mục quy tắc

[Use case gốc](usecases/UC-MENU-013.md)

1. Hệ thống hiển thị quy tắc: mã, tên, câu gốc trong file quy chuẩn, loại (cứng/mềm), điểm phạt, phạm vi (ngày/tuần), tham số, trạng thái bật/tắt.
2. Dinh dưỡng viên sửa một hoặc nhiều mục: bật/tắt, loại, điểm phạt, giá trị tham số.
3. Dinh dưỡng viên nhập lý do (từ 10 ký tự) và chọn "Gửi đề nghị".
4. Hệ thống kiểm giá trị mới hợp lệ.
5. Hệ thống tạo đề nghị thay đổi `PENDING` với giá trị cũ – mới, ghi nhật ký.
6. Hệ thống tạo thông báo cho người có quyền `menu.rule.approve`.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Thiếu lý do hoặc lý do dưới 10 ký tự** (`BR-AUD-001`): `ERR-SYS-422-01`; quay lại bước 3.
- 4a. Điểm phạt quy tắc mềm ngoài 1–3, quy tắc cứng có điểm phạt khác 0, hoặc tham số số học âm** (`BR-MNU-007`): `ERR-MENU-422-16`; quay lại bước 2.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| `ERR-MENU-404-01` | "Món {tên} chưa có công thức hiệu lực cho ngày {ngày}." | Tạo hoặc duyệt công thức |
| `ERR-MENU-404-02` | "Món {tên} chưa có giá bán hiệu lực cho ngày {ngày}." | Đặt và duyệt giá bán |
| `ERR-MENU-409-01` | "Tên này đã tồn tại." | Đổi tên hoặc dùng bản ghi có sẵn |
| `ERR-MENU-409-02` | "Không sửa được đơn vị vì nguyên liệu đang dùng trong {n} công thức." | Tạo nguyên liệu mới |
| `ERR-MENU-409-03` | "Công thức đã gửi duyệt không sửa được. Hãy tạo phiên bản mới." | Tạo phiên bản mới |
| `ERR-MENU-409-04` | "Đã có giá bán cho ngày hiệu lực này." | Chọn ngày khác |
| `ERR-MENU-409-05` | "Loại suất đã có thực đơn nên không sửa được cơ cấu. Hãy tạo loại suất mới." | Tạo loại suất mới |
| `ERR-MENU-409-06` | "Tuần này đã có thực đơn cho loại suất đã chọn." | Mở thực đơn đã có |
| `ERR-MENU-409-07` | "Thực đơn đang ở trạng thái {trạng thái} nên không sửa được." | Thu hồi hoặc chờ kết quả duyệt |
| `ERR-MENU-409-08` | "Chỉ huỷ được thực đơn nháp." | Thu hồi nếu đã công bố |
| `ERR-MENU-409-09` | "Thực đơn có ngày phục vụ đã qua hoặc là hôm nay nên không công bố được." | Bỏ các ngày đã qua, gửi duyệt lại |
| `ERR-MENU-409-10` | "Giá đã hiệu lực không sửa hoặc huỷ được. Hãy đặt giá mới với ngày hiệu lực từ ngày mai." | Đặt giá mới |
| `ERR-MENU-422-01` | "Hệ số quy đổi không hợp lệ." | Sửa hệ số |
| `ERR-MENU-422-02` | "Nguyên liệu có xương hoặc vỏ cần khai tỷ lệ hao hụt." | Nhập tỷ lệ |
| `ERR-MENU-422-03` | "Tháng phải từ 1 đến 12." | Sửa tháng |
| `ERR-MENU-422-04` | "Món Healthy phải dùng phương pháp chế biến ít dầu mỡ." | Đổi phương pháp hoặc bỏ cờ |
| `ERR-MENU-422-05` | "Món gốc phải cùng vai trò và không phải là biến thể của món khác." | Chọn món gốc khác |
| `ERR-MENU-422-06` | "Món cần có công thức trước khi duyệt." | Tạo công thức |
| `ERR-MENU-422-07` | "Hai món của cặp phải khác nhau." | Chọn lại |
| `ERR-MENU-422-08` | "Công thức cần ít nhất một nguyên liệu chính và không lặp nguyên liệu." | Sửa các dòng |
| `ERR-MENU-422-09` | "Định lượng phải thoả: tối thiểu ≤ chuẩn ≤ tối đa." | Sửa định lượng |
| `ERR-MENU-422-10` | "Công thức cần có nguyên liệu chính thuộc nhóm {nhóm} của món." | Sửa công thức hoặc nhóm của món |
| `ERR-MENU-422-11` | "Giá bán phải là bội số của 100 đồng và có hiệu lực từ ngày mai trở đi." | Sửa giá hoặc ngày |
| `ERR-MENU-422-12` | "Cấu hình loại suất không hợp lệ." | Sửa cấu hình |
| `ERR-MENU-422-13` | "Tuần phải bắt đầu từ thứ Hai và có ít nhất một ngày phục vụ." | Chọn lại |
| `ERR-MENU-422-14` | "Không xếp được món {tên} vào vị trí này." | Chọn món khác |
| `ERR-MENU-422-15` | "Món mặc định phải là một món chính của ngày." | Chọn lại |
| `ERR-MENU-422-16` | "Giá trị quy tắc không hợp lệ." | Sửa giá trị |
| `ERR-MENU-422-17` | "Thực đơn chưa đủ: {danh sách}." | Bổ sung |
| `ERR-MENU-422-18` | "Thực đơn còn {n} vi phạm quy tắc bắt buộc." | Sửa thực đơn |
| `ERR-MENU-422-19` | "Cần ghi lý do cho {n} cảnh báo mức nặng." | Ghi lý do |
| `ERR-MENU-422-20` | "Tệp còn {n} lỗi. Xem danh sách lỗi theo dòng." | Sửa tệp, nhập lại |
| `ERR-MENU-422-21` | "Ngày hiệu lực phải từ hôm nay và sau ngày hiệu lực của phiên bản hiện có ({ngày})." | Chọn ngày muộn hơn |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
