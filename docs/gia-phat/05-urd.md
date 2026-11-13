# Tài liệu Yêu cầu Người dùng (URD): Nền tảng Gia Phát

## Metadata

| Trường | Giá trị |
|---|---|
| Template | `05-urd.md` · BA-Kit v1.0 |
| Phiên bản | v0.1.0 |
| Trạng thái | **Bản nháp**: dựng từ tài liệu, **chưa phỏng vấn người dùng thật** (xem mục 7) |
| Ngày | 10/11/2026 |
| Tài liệu liên quan | [BRD](06-brd.md) · [Kế hoạch tổng thể](00-ke-hoach-tong-the.md) · [Bảng quy tắc thực đơn](brainstorms/quy-tac-thuc-don.md) |

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
|---|---|---|---|
| 0.1.0 | 10/11/2026 | BA | Khởi tạo từ BRD v0.1.0 và các quyết định D-01 → D-21 |

**Giới hạn của bản này.** Chân dung và hành trình dưới đây lấy từ ba nguồn: bản thiết kế HTML 04/11/2026, file docx, và các câu trả lời của anh. Chưa có buổi phỏng vấn nào với dinh dưỡng viên, quản lý cơ sở, kế toán, người đặt tổng hay người ăn. Cột "Nguồn" ghi rõ từng ý lấy từ đâu; ý nào ghi **[CẦN PHỎNG VẤN]** là chỗ tài liệu không đủ để khẳng định.

---

## 1. Phân loại tác nhân

Theo `rules/17-actor-role-definition.md`.

| Mã | Tác nhân | Loại | Mặt tiền | Đăng nhập |
|---|---|---|---|---|
| A-01 | Khách vãng lai | Chính | Website công khai | Không |
| A-02 | Người đặt tổng | Chính | Cổng khách hàng | Tài khoản do Gia Phát cấp |
| A-03 | Người nhận | Hỗ trợ | Cổng khách hàng / link | Link hoặc tài khoản |
| A-04 | Người ăn có tài khoản | Chính | Cổng người ăn | Tự đăng ký, xác minh bằng QR công ty |
| A-05 | Người ăn qua QR | Chính | Cổng người ăn | Không |
| A-06 | Dinh dưỡng viên kiêm CSKH | Chính | Quản trị | Có |
| A-07 | Quản lý cơ sở | Chính | Quản trị | Có, theo cơ sở |
| A-08 | Bếp trưởng | Hỗ trợ | Quản trị | Có, theo cơ sở |
| A-09 | Kế toán | Chính | Quản trị | Có |
| A-10 | Giám đốc | Chính | Quản trị | Có |
| A-11 | Agent Dinh dưỡng viên | Hệ thống | Website, cổng | Tài khoản dịch vụ |
| A-12 | Agent Nội bộ | Hệ thống | Quản trị | Tài khoản dịch vụ, quyền theo người dùng |
| A-13 | Bộ hẹn giờ hệ thống | Hệ thống | Không áp dụng | Khoá số tại hạn chốt, gửi nhắc, tính nhu cầu nguyên liệu |

---

## 2. Chân dung người dùng

Chân dung theo **vai trò**, không gắn tên hay tuổi giả định.

### 2.1 A-06 · Dinh dưỡng viên kiêm CSKH

| Mục | Nội dung | Nguồn |
|---|---|---|
| Số người | 1 | Bản HTML, mục 0 |
| Việc đang làm | Tư vấn, chăm sóc khách qua Zalo cá nhân; chốt thực đơn, định lượng, số suất; nhập doanh thu ngày vào Google Sheets | Bản HTML, mục 0 |
| Việc sẽ làm | Tạo loại suất; nhập nguyên liệu, món, công thức, dữ liệu dinh dưỡng; dựng và duyệt thực đơn; duyệt đầu ra của hai agent; đặt món mặc định mỗi ngày; chăm sóc khách | D-14, D-17, D-20 |
| Mục tiêu | Thực đơn đúng quy chuẩn, cost không vượt ngưỡng, khách không rời | Docx; BRD BO-01, BO-04 |
| Khó khăn | Mọi quy tắc phải tự nhớ và tự kiểm; cost chỉ biết sau khi đã mua; là điểm duy nhất nắm lịch sử khách | BRD P-01, P-02, P-04 |
| Rủi ro với dự án | Khối lượng nhập dữ liệu gốc dồn vào một người | BRD R-01, R-02 |
| Thiết bị, thời điểm dùng | [CẦN PHỎNG VẤN] | Chưa xác định |

### 2.2 A-10 · Giám đốc

| Mục | Nội dung | Nguồn |
|---|---|---|
| Vai trò | Duyệt giá, hợp đồng, ngoại lệ; nhìn toàn dòng vận hành. Vai trò này là **giả định** trong bản HTML: điểm mở O-06 | Bản HTML, mục 0 |
| Mục tiêu | Biết biên lợi nhuận theo ngày và theo khách; chỉ can thiệp khi có ngoại lệ | Bản HTML, "Tháp điều hành" |
| Khó khăn | Số liệu nằm rải ở Sheets, giấy và điện thoại cá nhân | BRD H-01 → H-03 |
| Cần từ hệ thống | Dashboard cost %, doanh thu, công nợ, khách có nguy cơ rời; hỏi số liệu bằng lời | D-07 |

### 2.3 A-09 · Kế toán

| Mục | Nội dung | Nguồn |
|---|---|---|
| Số người | 2 | Bản HTML, mục 0 |
| Việc đang làm | Nhập Sheets chi phí, nhập–xuất nguyên liệu, công nợ nhà cung cấp, doanh thu, lương; dùng MISA riêng | Bản HTML, mục 0 |
| Việc sẽ làm | Nhập giá nhập theo nhà cung cấp và ngày; đặt hàng phần thiếu; đối soát, khoá kỳ, xuất file MISA | D-13; bản HTML chặng 4, 10b |
| Khó khăn | Nhập lại số liệu người khác đã ghi; đối soát cuối tháng bằng tay | BRD P-03 |
| Chia việc giữa 2 kế toán (theo mảng hay theo cơ sở) | [CẦN PHỎNG VẤN]: bản HTML cũng ghi "cần xác nhận" | Bản HTML, mục 0 |

### 2.4 A-07 · Quản lý cơ sở và A-08 · Bếp trưởng

| Mục | Nội dung | Nguồn |
|---|---|---|
| Số người | 2 quản lý cơ sở; mỗi cơ sở khoảng 10 người gồm đầu bếp, tạp vụ | Bản HTML, mục 0 |
| Việc đang làm | Điều hành bếp, lập chấm công, ghi chi tiêu trên giấy; sơ chế, chế biến, chia suất | Bản HTML, mục 0 |
| Việc sẽ làm | Xem kế hoạch theo **món** cho ngày mai; ghi số sản xuất, số giao; nhận nguyên liệu; lưu mẫu | D-04; bản HTML chặng 5–9 |
| Cần từ hệ thống | Số suất từng món chính biết trước giờ mua hàng; phiếu sản xuất xem được trên điện thoại | Bản HTML chặng 5 |
| Mối lo với việc người ăn tự chọn | Số theo món biến động, khó chuẩn bị | BRD R-07: [CẦN PHỎNG VẤN] |

### 2.5 A-02 · Người đặt tổng (kiêm A-03 Người nhận)

| Mục | Nội dung | Nguồn |
|---|---|---|
| Là ai | Đầu mối của công ty khách; thường cũng là người xác nhận nhận hàng | Bản HTML, mục 0 |
| Việc đang làm | Gửi số suất cho Gia Phát qua Zalo | Bản HTML chặng 3 |
| Việc sẽ làm | Đặt định mức suất của công ty; xem tổng lựa chọn theo món; chốt tổng số suất; xác nhận số nhận; xem đối soát; dùng Agent Dinh dưỡng viên để yêu cầu thực đơn | D-14, D-21, D-06 |
| Mục tiêu | Ít thao tác hơn nhắn Zalo; số liệu cuối tháng không tranh cãi | BRD BO-06, BO-07 |
| Có sẵn lòng chuyển từ Zalo sang cổng không | [CẦN PHỎNG VẤN]: BRD AS-02 | Chưa xác định |

### 2.6 A-04, A-05 · Người ăn

| Mục | Nội dung | Nguồn |
|---|---|---|
| Là ai | Nhân viên công ty khách: công nhân khu công nghiệp và nhân viên văn phòng | Website; bản HTML mục 0 |
| Việc đang làm | Ăn suất được phát, không chọn | BRD H-06 |
| Việc sẽ làm | Quét QR công ty; chọn 1 trong 3 món chính mỗi ngày trong định mức; xem định lượng, dinh dưỡng, dị ứng; đánh giá bữa ăn | D-04, D-19, D-21 |
| Hai kiểu dùng | **Qua QR**: chọn món, không lưu gì. **Có tài khoản**: thêm lịch sử, đặt trước cả tuần, hồ sơ dinh dưỡng và gợi ý cá nhân | D-03, D-06 |
| Điều kiện dùng | Có điện thoại vào được web: BRD AS-01 | [CẦN PHỎNG VẤN] với nhóm công nhân |
| Thời điểm chọn món (trước mấy ngày, lúc nào trong ngày) | [CẦN PHỎNG VẤN] | Chưa xác định |

### 2.7 A-01 · Khách vãng lai

| Mục | Nội dung | Nguồn |
|---|---|---|
| Là ai | Người phụ trách hành chính, nhân sự, mua hàng của doanh nghiệp đang tìm nhà cung cấp suất ăn | Website, mục dịch vụ |
| Đến từ đâu | Facebook, website, giới thiệu | Bản HTML chặng 1 |
| Cần gì | Biết giá, thực đơn, định lượng, năng lực trước khi liên hệ | D-10 |
| Việc sẽ làm | Xem thực đơn mẫu có giá; dựng thử thực đơn; hỏi Agent Dinh dưỡng viên; gửi yêu cầu tư vấn | PUB-03 → 06 |

---

## 3. Bản đồ hành trình

Bốn chặng theo skill: Nhận biết → Xem → Thao tác → Nhận kết quả.

### 3.1 J-01 · Người ăn chọn món

| Chặng | Người ăn làm gì | Hệ thống đáp lại | Điểm dễ hỏng |
|---|---|---|---|
| Nhận biết | Thấy mã QR công ty tại nơi làm việc, hoặc nhận nhắc trước hạn chốt | Không áp dụng | Không biết có tính năng; kênh nhắc chưa chốt (Q-14) |
| Xem | Quét QR, thấy 3 món chính của ngày kèm định lượng, 4 chỉ số dinh dưỡng, dị ứng | Trang mở từ bộ nhớ đệm; hiện giờ còn lại đến hạn chốt | Mạng yếu trong xưởng |
| Thao tác | Chọn 1 món; nếu có tài khoản thì chọn luôn cho các ngày còn lại trong tuần | Ghi lựa chọn; chặn tổ hợp vượt định mức công ty (BR-COST-012) | Bấm nhiều lần; nhiều người cùng chọn sát hạn chốt |
| Nhận kết quả | Thấy xác nhận món đã chọn; đổi được trước hạn chốt | Sau hạn chốt: khoá; người chưa chọn nhận món mặc định (D-14) | Người ăn không biết mình đã bị gán món mặc định |

### 3.2 J-02 · Người đặt tổng chốt số suất

| Chặng | Người đặt tổng làm gì | Hệ thống đáp lại | Điểm dễ hỏng |
|---|---|---|---|
| Nhận biết | Nhận nhắc trước hạn chốt | Gửi nhắc kèm số người chưa chọn | Kênh nhắc chưa chốt (Q-14) |
| Xem | Mở cổng, thấy tổng theo từng món chính, số người chưa chọn, món mặc định | Số cập nhật theo lựa chọn mới nhất | Không có |
| Thao tác | Nhập tổng số suất của ngày; sửa phân bổ cho phần chưa chọn nếu muốn; bấm chốt | Kiểm tra hợp đồng, điểm phục vụ, ca còn hiệu lực | Chốt trễ sau hạn → đi luồng "đổi sau chốt" |
| Nhận kết quả | Thấy bản chốt có phiên bản; sau khi giao thì xác nhận số nhận | Phát hành kế hoạch cho cơ sở và kế toán | Số chốt nhỏ hơn số người đã chọn: cần quy tắc xử lý ở SRS |

### 3.3 J-03 · Dinh dưỡng viên dựng thực đơn tuần

| Chặng | Dinh dưỡng viên làm gì | Hệ thống đáp lại | Điểm dễ hỏng |
|---|---|---|---|
| Nhận biết | Đến kỳ dựng thực đơn, hoặc nhận cảnh báo giá nhập làm thực đơn cũ vượt ngưỡng | Cảnh báo BR-COST-011 | Giá nhập chưa cập nhật (BR-COST-005) |
| Xem | Mở loại suất, xem thực đơn các tuần trước và điểm quy tắc | Hiện lịch sử món đã dùng để tránh lặp | Không có |
| Thao tác | Yêu cầu Agent Nội bộ tạo bản nháp; đổi món bằng tay hoặc bằng lời | Agent chỉ dùng món đã duyệt; bộ kiểm quy tắc và cost chạy lại sau mỗi thay đổi | Thiếu món đã duyệt đủ thuộc tính → agent không dựng được |
| Nhận kết quả | Thấy bảng kiểm: quy tắc đạt/vi phạm, cost %, bảng dự toán; gửi duyệt; công bố | Chặn công bố khi vi phạm quy tắc cứng hoặc vượt ngưỡng | Người duyệt thứ hai chưa xác định (O-06) |

### 3.4 J-04 · Khách vãng lai trở thành lead

| Chặng | Khách làm gì | Hệ thống đáp lại | Điểm dễ hỏng |
|---|---|---|---|
| Nhận biết | Tìm kiếm trên mạng, thấy Facebook, hoặc được giới thiệu | Trang đích tải được từ kết quả tìm kiếm | Mất thứ hạng sau khi bỏ WordPress (BRD R-05) |
| Xem | Xem thực đơn mẫu có giá suất, định lượng, dinh dưỡng | Không áp dụng | Giá công khai để đối thủ xem được: đã chấp nhận ở D-10 |
| Thao tác | Dựng thử thực đơn theo mức giá và số suất; hỏi Agent Dinh dưỡng viên | Agent trả thực đơn mẫu đạt quy tắc; giới hạn số lượt | Khách hỏi ngoài phạm vi (bệnh lý, cam kết giá) |
| Nhận kết quả | Gửi yêu cầu tư vấn kèm thực đơn vừa dựng | Tạo lead trong CRM có nguồn; báo dinh dưỡng viên | Lead không ai nhận trong 24 giờ |

### 3.5 J-05 · Kế toán cập nhật giá nhập và đối soát

| Chặng | Kế toán làm gì | Hệ thống đáp lại | Điểm dễ hỏng |
|---|---|---|---|
| Nhận biết | Có chứng từ mua hàng mới, hoặc đến cuối kỳ | Cảnh báo giá quá cũ | Chứng từ viết tay từ tiểu thương |
| Xem | Xem giá hiện hành theo nguyên liệu và nhà cung cấp; xem doanh thu ngày đã ghi nhận | Không áp dụng | Không có |
| Thao tác | Nhập giá mới có ngày hiệu lực; lập biên bản đối soát | Tính lại cost các thực đơn chịu ảnh hưởng | Nhập sai đơn vị (kg, bìa, quả) |
| Nhận kết quả | Thấy thực đơn nào vượt ngưỡng; khách ký biên bản; khoá kỳ; xuất file MISA | Báo dinh dưỡng viên và Giám đốc | Định nghĩa cost chưa chốt (O-01) |

---

## 4. Danh sách nhu cầu người dùng

Mức cấp bách: **Cao** = thiếu thì người dùng không làm được việc chính · **Vừa** = làm được nhưng tốn công · **Thấp** = tiện ích thêm.

| Mã | Tác nhân | Nhu cầu | Cấp bách | Yêu cầu nghiệp vụ |
|---|---|---|---|---|
| UN-01 | A-06 | Biết thực đơn có vi phạm quy tắc nào ngay khi đang dựng, không phải tự rà | Cao | BN-04 |
| UN-02 | A-06 | Biết cost % của từng ngày trước khi chốt thực đơn | Cao | BN-04, BN-06 |
| UN-03 | A-06 | Có bản nháp thực đơn tuần đúng chuẩn để sửa, thay vì dựng từ đầu | Cao | BN-14 |
| UN-04 | A-06 | Tự tạo loại suất với ngưỡng giá và số món riêng cho từng khách | Cao | BN-03 |
| UN-05 | A-06 | Được báo khi giá nhập đổi làm thực đơn đã duyệt vượt ngưỡng | Vừa | BN-21 |
| UN-06 | A-06 | Xem toàn bộ lịch sử một khách ở một chỗ | Vừa | BN-13 |
| UN-07 | A-07, A-08 | Biết số suất từng món chính của ngày mai ngay sau hạn chốt | Cao | BN-11 |
| UN-08 | A-07, A-08 | Xem phiếu sản xuất trên điện thoại | Vừa | BN-11 |
| UN-09 | A-09 | Nhập giá nhập một lần, hệ thống tự tính lại cost | Cao | BN-05 |
| UN-10 | A-09 | Doanh thu tự sinh từ số đã xác nhận, không nhập lại | Cao | BN-12 |
| UN-11 | A-09 | So được cost dự toán với tiền thực mua theo ngày | Vừa | BN-22 |
| UN-12 | A-10 | Xem cost %, doanh thu, công nợ theo ngày và theo khách | Cao | BN-06, BN-12 |
| UN-13 | A-10 | Hỏi số liệu bằng lời | Thấp | BN-23 |
| UN-14 | A-02 | Đặt định mức suất một lần cho cả công ty | Cao | BN-08 |
| UN-15 | A-02 | Thấy tổng lựa chọn theo món và số người chưa chọn trước khi chốt | Cao | BN-09 |
| UN-16 | A-02 | Xác nhận số nhận bằng một thao tác trên điện thoại | Cao | BN-12 |
| UN-17 | A-02 | Yêu cầu thực đơn theo khẩu vị và kiêng kỵ của công ty | Vừa | BN-15 |
| UN-18 | A-04, A-05 | Chọn món trong tối đa 3 lần chạm kể từ khi quét QR | Cao | BN-08, BN-10 |
| UN-19 | A-04, A-05 | Biết món có gì, bao nhiêu gram, năng lượng bao nhiêu, có chất gây dị ứng nào | Cao | BN-07 |
| UN-20 | A-04 | Chọn trước cho cả tuần | Vừa | BN-08 |
| UN-21 | A-04 | Được gợi ý nên chọn món nào theo mục tiêu cá nhân | Thấp | BN-20 |
| UN-22 | A-04 | Xoá được dữ liệu cá nhân đã khai | Cao (khi mở UN-21) | BN-19 |
| UN-23 | A-04, A-05 | Biết mình được gán món mặc định nếu không chọn | Vừa | BN-09 |
| UN-24 | A-01 | Thấy giá suất và thực đơn mẫu mà không phải để lại thông tin | Cao | BN-07 |
| UN-25 | A-01 | Dựng thử thực đơn theo ngân sách của mình | Vừa | BN-15 |
| UN-26 | A-01 | Gửi yêu cầu tư vấn kèm thực đơn đã dựng | Cao | BN-13 |

---

## 5. Ma trận phân quyền mức cao

`X` xem · `T` tạo/sửa · `D` duyệt · `–` không truy cập. Ma trận chi tiết theo từng chức năng viết ở SRS nền tảng.

| Tài nguyên | A-01 Vãng lai | A-05 QR | A-04 Người ăn | A-02 Đặt tổng | A-06 DDV | A-07/08 Cơ sở | A-09 Kế toán | A-10 Giám đốc |
|---|---|---|---|---|---|---|---|---|
| Thực đơn mẫu, giá suất công khai | X | X | X | X | T | X | X | X |
| Thực đơn kỳ của công ty | – | X | X | X | T · D | X | X | X |
| Định lượng, dinh dưỡng, dị ứng của món | X | X | X | X | T | X | X | X |
| Công thức, thuộc tính món | – | – | – | – | T | X | X | D |
| Giá nhập, cost, bảng dự toán | – | – | – | – | X | X (cơ sở mình) | T | X · D ngưỡng |
| Giá bán từng món | X | X | X | X | T | – | X | D |
| Loại suất | X (đã công bố) | – | – | X (của công ty) | T | – | X | D |
| Định mức suất của công ty | – | – | X | T | X | – | X | – |
| Lựa chọn món của bản thân | – | T | T | T | – | – | – | – |
| Tổng lựa chọn, chốt số suất | – | – | – | T | T (nhập hộ) | X | X | X |
| Hồ sơ dinh dưỡng cá nhân | – | – | T (của mình) | – | – | – | – | – |
| Kế hoạch sản xuất theo món | – | – | – | – | X | T (cơ sở mình) | X | X |
| Giao, xác nhận nhận | – | – | – | T (xác nhận) | T (ghi hộ) | T (giao) | X | X |
| Doanh thu, đối soát, khoá kỳ | – | – | – | X · T (ký đối soát) | X | – | T | X · D mở kỳ |
| Lead, cơ hội, hợp đồng | T (gửi form) | – | – | X (HĐ mình) | T | – | X | D giá |
| Agent Dinh dưỡng viên | Dùng, giới hạn lượt | Dùng | Dùng | Dùng | – | – | – | – |
| Agent Nội bộ | – | – | – | – | Dùng | Dùng (cơ sở mình) | Dùng | Dùng |

Hai điểm khác bản HTML: công thức do dinh dưỡng viên tạo nhưng **người khác duyệt** (bản cũ cho tự tạo – tự duyệt), và hồ sơ dinh dưỡng cá nhân **không ai ngoài chính người ăn** xem được. Người duyệt cụ thể phụ thuộc O-06.

---

## 6. Điểm mở

Giữ nguyên trạng thái mở theo yêu cầu ngày 10/11/2026; ảnh hưởng của từng điểm lên URD:

| Mã | Điểm mở | Ai trả lời | Phần URD bị ảnh hưởng |
|---|---|---|---|
| O-01 | Cost gồm những khoản nào; thuế suất VAT | Kế toán | J-05, UN-02, UN-09 |
| O-02 | Một món một định lượng hay nhiều cỡ định lượng | Dinh dưỡng viên | J-01 (người ăn có chọn cỡ không), UN-19 |
| O-03 | Gợi ý cá nhân có xét bệnh lý không | Giám đốc | Chân dung 2.6, UN-21, UN-22 |
| O-04 | Đội phát triển, hạ tầng, nhà cung cấp AI, ngân sách | Giám đốc | Không ảnh hưởng URD |
| O-05 | Trường học, bệnh viện, tiệc cỗ có trong bản đầu không | Giám đốc | Thêm chân dung và hành trình nếu có |
| O-06 | Ai duyệt ngoại lệ và ai thay khi vắng | Giám đốc | Chân dung 2.2, ma trận mục 5, J-03 |

---

## 7. Việc cần phỏng vấn để lên v1.0.0

| # | Hỏi ai | Cần biết |
|---|---|---|
| 1 | Dinh dưỡng viên | Một tuần dựng thực đơn hiện mất bao nhiêu giờ, làm trên công cụ gì, thiết bị gì |
| 2 | Quản lý cơ sở, bếp trưởng | Cần biết số theo món trước giờ nào để kịp mua hàng; chấp nhận biến động số theo món đến mức nào |
| 3 | Kế toán | Hai người đang chia việc thế nào; chứng từ giá nhập về theo nhịp nào |
| 4 | 2–3 người đặt tổng của khách hiện tại | Có sẵn lòng dùng cổng thay Zalo; có đồng ý cho nhân viên tự chọn món |
| 5 | 5–10 người ăn ở cả hai nhóm công nhân và văn phòng | Có điện thoại vào web tại nơi làm việc không; muốn chọn món trước mấy ngày |
