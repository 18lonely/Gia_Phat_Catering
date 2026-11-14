# Tài liệu Yêu cầu Nghiệp vụ (BRD): Nền tảng Gia Phát

## Metadata

| Trường | Giá trị |
|---|---|
| Template | `06-brd.md` · BA-Kit v1.0 |
| Sản phẩm | Website công khai + cổng khách hàng/người ăn + quản trị nội bộ + 2 AI agent |
| Phiên bản | v0.1.1 |
| Trạng thái | **Bản nháp chờ duyệt**: chưa có số liệu tài chính (mục 8), còn 6 điểm mở (mục 11) |
| Ngày | 10/11/2026 |
| Người duyệt | Giám đốc Gia Phát (xem điểm mở O-06) |
| Tài liệu liên quan | [Kế hoạch tổng thể](00-ke-hoach-tong-the.md) · [Bảng quy tắc thực đơn](brainstorms/quy-tac-thuc-don.md) · [Phân tích bản thiết kế cũ](../../GiaPhat_PhanTich_ThietKe.md) · `GiaPhat_CMAP_CRM.html` bản 1.0 · `Yêu cầu về thực đơn và cost tp.docx` |

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
|---|---|---|---|
| 0.1.1 | 14/11/2026 | BA | Ràng buộc công nghệ mục 10 đổi sang Rust/Axum theo D-22, CR-CORE-2026-001 |
| 0.1.0 | 10/11/2026 | BA | Khởi tạo từ 21 quyết định D-01 → D-21 của kế hoạch tổng thể |

Quy ước: **[ĐÃ CHỐT D-xx]** dẫn về quyết định trong kế hoạch tổng thể · **[ĐỀ XUẤT]** chờ duyệt · **[CẦN SỐ LIỆU]** Gia Phát phải cung cấp, tài liệu này không tự ước lượng.

---

## 1. Tóm tắt điều hành

Gia Phát cung cấp suất ăn B2B từ 2 cơ sở (Hoàng Đạo Thành, Phúc Diễn). Việc vận hành hiện dựa trên Zalo cá nhân, Google Sheets và chứng từ giấy; website chỉ là một trang giới thiệu chạy WordPress.

Dự án xây một nền tảng gồm bốn mặt tiền dùng chung một lõi dữ liệu:

1. **Website công khai** viết lại bằng React, có thực đơn mẫu kèm giá, định lượng, dinh dưỡng và công cụ dựng thực đơn.
2. **Cổng khách hàng và người ăn**: công ty đặt định mức suất; từng người ăn chọn 1 trong 3 món chính mỗi ngày trong định mức đó.
3. **Trang quản trị nội bộ** trên subdomain riêng: thực đơn, định lượng, cost, order, giao nhận, doanh thu, CRM.
4. **Hai AI agent tách biệt**: Agent Dinh dưỡng viên cho khách và Agent Nội bộ cho nhân viên Gia Phát.

Lợi ích kinh doanh cốt lõi: kiểm soát được ngưỡng cost thực phẩm 52% **trước khi** chốt thực đơn, giảm phụ thuộc vào một dinh dưỡng viên, và biến website thành nguồn khách hàng tiềm năng đi thẳng vào CRM.

Tài liệu này **chưa tính được ROI** vì thiếu 9 số liệu đầu vào liệt kê ở mục 8.3.

---

## 2. Bối cảnh và bài toán

### 2.1 Hiện trạng

| # | Hiện trạng | Nguồn |
|---|---|---|
| H-01 | 1 dinh dưỡng viên kiêm CSKH tư vấn, chốt thực đơn, định lượng, số suất qua Zalo cá nhân và nhập doanh thu ngày vào Google Sheets | Bản HTML, mục 0 |
| H-02 | 2 kế toán nhập Sheets: chi phí, nhập–xuất nguyên liệu, công nợ, doanh thu, lương; MISA dùng riêng cho kế toán chính thức | Bản HTML, mục 0 |
| H-03 | 2 quản lý cơ sở ghi chi tiêu trên giấy; phần lớn nguyên liệu mua trong ngày từ tiểu thương, chứng từ viết tay | Bản HTML, chặng 4 |
| H-04 | Quy chuẩn thực đơn và ngưỡng cost 52% tồn tại dưới dạng văn bản Word, kiểm tra bằng tay | File docx |
| H-05 | Website là 1 landing page WordPress + Elementor và blog; form "Yêu cầu tư vấn" không nối với hệ thống nào | Khảo sát comgiaphat.com ngày 10/11/2026 |
| H-06 | Khách không tự chọn món; không có dữ liệu định lượng hay dinh dưỡng công khai | Bản HTML, mục 3 |

### 2.2 Bài toán

| Mã | Bài toán | Hậu quả kinh doanh |
|---|---|---|
| P-01 | Cost chỉ biết sau khi đã mua và nấu | Không ngăn được ngày vượt 52%; biên lợi nhuận phụ thuộc kinh nghiệm cá nhân |
| P-02 | Quy tắc thực đơn nằm trong đầu một người | Dinh dưỡng viên nghỉ thì không ai dựng được thực đơn đúng chuẩn |
| P-03 | Số đặt, số giao, số nhận, số tính tiền ghi ở nhiều nơi | Đối soát cuối tháng tốn công, dễ lệch |
| P-04 | Lịch sử khách nằm trong điện thoại cá nhân | Mất dữ liệu khi đổi người; không đo được phễu bán hàng |
| P-05 | Website không tạo được khác biệt và không sinh lead đo được | Không biết kênh nào mang lại hợp đồng |
| P-06 | Người ăn không có tiếng nói về món | Không có dữ liệu thật về món được ưa chuộng để cải tiến thực đơn |

---

## 3. Mục tiêu kinh doanh và chỉ số thành công

Mọi mức mục tiêu dưới đây là **[ĐỀ XUẤT]**; cột "Hiện tại" để trống ở những chỗ Gia Phát chưa đo.

| Mã | Mục tiêu | Chỉ số đo | Hiện tại | Mục tiêu | Thời điểm đo |
|---|---|---|---|---|---|
| BO-01 | Không công bố thực đơn vượt ngưỡng cost | Tỷ lệ ngày phục vụ có cost dự toán ≤ 52% | [CẦN SỐ LIỆU] | 100% | Từ ngày phân hệ COST chạy thật |
| BO-02 | Cost thực tế bám sát dự toán | Chênh lệch cost thực mua so với dự toán, theo ngày và cơ sở | Chưa đo | ≤ 3 điểm phần trăm | 3 tháng sau khi có COST-07 |
| BO-03 | Giảm thời gian dựng thực đơn tuần | Số giờ dinh dưỡng viên dùng cho một thực đơn tuần của một loại suất | [CẦN SỐ LIỆU] | Giảm ≥ 50% | 1 tháng sau khi có Agent Nội bộ (AIO-01) |
| BO-04 | Thực đơn tuân thủ quy chuẩn | Tỷ lệ thực đơn công bố không vi phạm quy tắc cứng nào | Chưa đo | 100% | Từ ngày MENU-06 chạy thật |
| BO-05 | Người ăn tự chọn món | Tỷ lệ suất có lựa chọn của người ăn trước hạn chốt ÷ tổng suất của các công ty bật tính năng | 0% | ≥ 70% | 3 tháng sau khi mở ORD-01 |
| BO-06 | Order qua hệ thống thay Zalo | Tỷ lệ order ghi nhận qua cổng ÷ tổng order | 0% | ≥ 90% | Như cổng G1 của bản HTML |
| BO-07 | Rút ngắn đối soát | Số ngày từ cuối kỳ đến khi khách ký biên bản đối soát | [CẦN SỐ LIỆU] | ≤ 5 ngày làm việc | 2 kỳ sau khi có FIN |
| BO-08 | Website sinh lead đo được | Số lead/tháng từ form và từ công cụ dựng thực đơn, có nguồn | Không đo được | 100% lead có nguồn; số lượng mục tiêu [CẦN SỐ LIỆU] | Từ ngày site mới chạy |
| BO-09 | Không mất thứ hạng tìm kiếm khi bỏ WordPress | Số phiên truy cập tự nhiên/tháng | [CẦN SỐ LIỆU] | ≥ 90% mức trước chuyển đổi, đo sau 60 ngày | 60 ngày sau chuyển đổi |
| BO-10 | Chịu được giờ cao điểm | Số người dùng đồng thời hệ thống phục vụ với p95 API ≤ 300 ms (đọc), ≤ 800 ms (ghi) | Chưa xác định | 1000 | Kiểm thử tải trước khi mở cho người ăn |

---

## 4. Phạm vi

### 4.1 Trong phạm vi

| # | Hạng mục | Căn cứ |
|---|---|---|
| S-01 | Viết lại comgiaphat.com bằng React, chuyển toàn bộ bài viết cũ | [ĐÃ CHỐT D-01] |
| S-02 | Trang thực đơn mẫu công khai có giá suất, định lượng, dinh dưỡng, dị ứng | [ĐÃ CHỐT D-10] |
| S-03 | Danh mục nguyên liệu, món, công thức có phiên bản, loại suất do dinh dưỡng viên tự tạo | [ĐÃ CHỐT D-20] |
| S-04 | Bộ kiểm quy tắc thực đơn theo docx, phân loại cứng/mềm | [ĐÃ CHỐT D-08, D-16] |
| S-05 | Giá nhập nguyên liệu do nội bộ nhập; tính cost món, cost suất; chặn khi vượt ngưỡng | [ĐÃ CHỐT D-13] |
| S-06 | Dinh dưỡng 4 chỉ số (năng lượng, đạm, béo, bột đường) từ Bảng thành phần thực phẩm Việt Nam | [ĐÃ CHỐT D-17] |
| S-07 | Công ty đặt định mức suất; người ăn chọn 1 trong 3 món chính trong định mức; món mặc định cho người không chọn | [ĐÃ CHỐT D-04, D-14, D-21] |
| S-08 | Giá bán riêng từng món; hệ thống chặn lựa chọn vượt định mức | [ĐÃ CHỐT D-12, D-18] |
| S-09 | Đăng ký người ăn xác minh bằng mã QR công ty; chọn món qua QR không cần tài khoản | [ĐÃ CHỐT D-03, D-19] |
| S-10 | Agent Dinh dưỡng viên: thực đơn tập thể và gợi ý cá nhân | [ĐÃ CHỐT D-05, D-06] |
| S-11 | Agent Nội bộ: dựng thực đơn + kiểm cost, mua hàng, CRM, hỏi đáp số liệu | [ĐÃ CHỐT D-07] |
| S-12 | Trang quản trị nội bộ phủ các phân hệ M1–M10 của bản HTML, đã sửa theo bản phân tích | [ĐÃ CHỐT D-02, D-09] |
| S-13 | 2 cơ sở Hoàng Đạo Thành và Phúc Diễn | [ĐÃ CHỐT D-09] |

### 4.2 Ngoài phạm vi

| # | Hạng mục | Lý do |
|---|---|---|
| X-01 | Căn tin bệnh viện Quảng Ninh | Đã loại từ quyết định 04/11/2026 |
| X-02 | Thay thế MISA | MISA vẫn là sổ kế toán chính thức; hệ thống chỉ xuất file |
| X-03 | Người ăn tự thanh toán, ví, cổng thanh toán | Công ty trả toàn bộ theo định mức [ĐÃ CHỐT D-21] |
| X-04 | Ứng dụng di động cài từ kho ứng dụng | Web chạy trên điện thoại; không phát triển app riêng trong tài liệu này |
| X-05 | Tư vấn y khoa, chẩn đoán, phác đồ ăn điều trị | Agent chỉ gợi ý trong phạm vi thực đơn Gia Phát |
| X-06 | Đồng bộ tự động với Zalo cá nhân | Không có cách kết nối hợp lệ |
| X-07 | Ghi lượng thức ăn bỏ thừa | Gia Phát chưa thu thập; để sau |

Trường học, bệnh viện và tiệc cỗ: chưa xác định trong hay ngoài phạm vi bản đầu, điểm mở O-05.

---

## 5. Bên liên quan

| Bên liên quan | Vai trò trong dự án | Quan tâm chính | Tham gia |
|---|---|---|---|
| Giám đốc | Nhà tài trợ, duyệt BRD, duyệt ngưỡng cost và giá | Biên lợi nhuận, khách hàng, chi phí dự án | Duyệt |
| Dinh dưỡng viên kiêm CSKH | Chủ nghiệp vụ thực đơn, định lượng, dinh dưỡng; duyệt đầu ra AI | Giảm việc tay, thực đơn đúng chuẩn | Duyệt bảng quy tắc, nhập dữ liệu gốc |
| Bếp trưởng / quản lý cơ sở | Người dùng kế hoạch sản xuất | Số theo món chính xác, đúng giờ | Góp ý quy tắc khả thi bếp |
| Kế toán | Chủ nghiệp vụ giá nhập, doanh thu, đối soát | Định nghĩa cost, VAT, khớp MISA | Trả lời H-6, H-7 của bảng quy tắc |
| Người đặt tổng (công ty khách) | Đặt định mức, chốt tổng số suất | Ít thao tác, số liệu đối soát rõ | Thử nghiệm |
| Người ăn | Chọn món, đánh giá | Được chọn, biết mình ăn gì | Thử nghiệm |
| Khách vãng lai | Xem thực đơn mẫu, dùng công cụ | Giá và chất lượng minh bạch | Không áp dụng |
| Đội phát triển | Xây và vận hành | Yêu cầu rõ, dữ liệu gốc sẵn | Điểm mở O-04 |

---

## 6. Yêu cầu nghiệp vụ mức cao

Mã phân hệ và mã tính năng lấy từ mục 4 và 5 của kế hoạch tổng thể. Yêu cầu chức năng chi tiết (`FR-…`) được viết ở SRS từng epic.

| Mã | Yêu cầu nghiệp vụ | Phục vụ mục tiêu | Tính năng | Ưu tiên |
|---|---|---|---|---|
| BN-01 | Mỗi món phải có đủ thuộc tính để máy kiểm quy tắc: vai trò, nhóm nguyên liệu chính, phương pháp chế biến, vị chua, sốt/khô, cờ Healthy, mức cầu kỳ, mức chịu vận chuyển, giá bán | BO-04 | MENU-01, 02 | P0 |
| BN-02 | Công thức có phiên bản, có người duyệt khác người tạo, có ngày hiệu lực | BO-01, BO-04 | MENU-03 | P0 |
| BN-03 | Dinh dưỡng viên tạo được loại suất với 3 tham số: ngưỡng giá, số món chính, số món phụ | BO-05 | MENU-04 | P0 |
| BN-04 | Thực đơn chỉ được công bố khi không vi phạm quy tắc cứng nào và cost ≤ ngưỡng | BO-01, BO-04 | MENU-06, 07; COST-03 | P0 |
| BN-05 | Giá nhập lưu theo nguyên liệu × nhà cung cấp × ngày hiệu lực | BO-01, BO-02 | COST-01 | P0 |
| BN-06 | Hệ thống lập được bảng dự toán: nguyên liệu, giá nhập, định lượng/suất, số suất, tổng chi phí | BO-01 | COST-04 | P0 |
| BN-07 | Khách và người ăn thấy định lượng, 4 chỉ số dinh dưỡng, dị ứng của từng món; không thấy giá nhập và cost | BO-05, BO-08 | NUTR-01 → 03 | P0 |
| BN-08 | Công ty đặt một định mức suất chung; người ăn chỉ chọn được tổ hợp có tổng giá bán ≤ định mức | BO-05 | MENU-10, ORD-01 | P0 |
| BN-09 | Tại hạn chốt, người chưa chọn nhận món mặc định của ngày; tổng số suất do người đặt tổng chốt | BO-05, BO-06 | ORD-02 → 04 | P0 |
| BN-10 | Người ăn đăng ký phải quét mã QR của công ty mình; một mã QR chỉ gắn với một công ty | BO-05 | AUTH-03, 04 | P0 |
| BN-11 | Kế hoạch sản xuất tính theo món; giao, nhận, tính tiền tính theo suất | BO-06, BO-07 | PLAN, DLV, FIN | P0 |
| BN-12 | Doanh thu sinh ra từ số đã xác nhận × giá chụp tại thời điểm order; không nhập tay lại | BO-07 | FIN | P0 |
| BN-13 | Lead từ form và từ công cụ dựng thực đơn tự vào CRM, kèm nguồn và thực đơn khách đã dựng | BO-08 | PUB-06, CUS | P0 |
| BN-14 | Agent Nội bộ dựng thực đơn tuần đạt BN-04 từ 3 đầu vào: loại suất, tuần, danh sách kiêng kỵ | BO-03 | AIO-01 | P0 |
| BN-15 | Agent Dinh dưỡng viên tạo thực đơn tuần cho tập thể và gửi về Gia Phát ở trạng thái nháp | BO-08 | AIN-01 → 04 | P0 |
| BN-16 | Agent phía khách không truy cập được bảng giá nhập và cost; kiểm soát ở tầng công cụ và quyền cơ sở dữ liệu | Không áp dụng (kiểm soát) | AIN | P0 |
| BN-17 | Mọi thực đơn do AI tạo phải qua người duyệt trước khi công bố | BO-04 | MENU-07 | P0 |
| BN-18 | Toàn bộ bài viết cũ giữ nguyên URL hoặc chuyển hướng 301 | BO-09 | PUB-02 | P0 |
| BN-19 | Dữ liệu sức khoẻ cá nhân chỉ thu khi người ăn đồng ý bằng thao tác rõ ràng; người ăn xoá được dữ liệu của mình | Không áp dụng (pháp lý) | AUTH-05, NUTR-04 | P1 |
| BN-20 | Gợi ý cá nhân: nên chọn món nào trong 3 món theo hồ sơ đã khai | BO-05 | AIN-05, NUTR-05 | P1 |
| BN-21 | Cảnh báo khi giá nhập đổi làm thực đơn đã duyệt vượt ngưỡng | BO-01 | COST-06, AIO-02 | P1 |
| BN-22 | Đối chiếu cost dự toán với thực mua theo ngày và cơ sở | BO-02 | COST-07, AIO-04 | P1 |
| BN-23 | Hỏi đáp số liệu bằng lời, giới hạn theo quyền của người hỏi, chỉ đọc | Không áp dụng | AIO-06 | P2 |

---

## 7. Quy tắc nghiệp vụ chủ chốt

Danh sách đầy đủ 43 quy tắc nằm ở [bảng quy tắc thực đơn](brainstorms/quy-tac-thuc-don.md), đang chờ người soạn docx duyệt. Các quy tắc quyết định biên lợi nhuận:

| Mã | Quy tắc | Trạng thái |
|---|---|---|
| BR-COST-001 | Cost thực phẩm mỗi ngày ÷ doanh thu suất ăn ≤ 52% | Từ docx |
| BR-COST-002 | Doanh thu làm mẫu số là giá suất đã trừ VAT | [ĐỀ XUẤT]: xem ví dụ dưới |
| BR-COST-003 | Thành phần tính vào cost | **Chưa chốt**: điểm mở O-01 |
| BR-COST-012 | Tổng giá bán các món người ăn chọn ≤ định mức suất của công ty | [ĐÃ CHỐT D-12, D-21] |
| BR-MENU-001, 002 | Mỗi ngày đúng số món chính của loại suất, trong đó đúng 1 món Healthy | Từ docx |

**Vì sao BR-COST-002 cần chốt sớm.** Giá 40.000đ đã gồm VAT [ĐÃ CHỐT D-15]. Mức nguyên liệu tối đa cho một suất thay đổi theo cách tính:

| Cách tính | Doanh thu làm mẫu số | Cost tối đa/suất |
|---|---|---|
| Tính thẳng trên 40.000đ | 40.000đ | 20.800đ |
| Trừ VAT 8% | 37.037đ | 19.259đ |
| Trừ VAT 10% | 36.364đ | 18.909đ |

Chênh giữa cách thứ nhất và cách thứ ba là 1.891đ mỗi suất. Thuế suất thực tế do kế toán xác nhận (câu H-6 của bảng quy tắc).

---

## 8. Chi phí, lợi ích và ROI

Phần này mới có **khung tính**. Chưa có con số tổng vì thiếu các đầu vào ở 8.3.

### 8.1 Hạng mục chi phí

| Mã | Hạng mục | Loại | Cách ước lượng | Giá trị |
|---|---|---|---|---|
| C-01 | Phát triển phần mềm (13 epic) | Một lần | Số người × số tháng × đơn giá, sau khi có ước lượng từ backlog | [CẦN SỐ LIỆU] |
| C-02 | Nhập dữ liệu gốc: nguyên liệu, món, công thức, giá nhập, thành phần dinh dưỡng (ước 100–150 nguyên liệu) | Một lần | Giờ công dinh dưỡng viên + kế toán | [CẦN SỐ LIỆU] |
| C-03 | Chuyển nội dung WordPress, kiểm tra chuyển hướng | Một lần | Số bài viết × thời gian/bài | [CẦN SỐ LIỆU] |
| C-04 | Hạ tầng: máy chủ API ≥ 2 bản, MySQL primary + replica, Redis, lưu trữ tệp, CDN | Hằng tháng | Theo nhà cung cấp được chọn | [CẦN SỐ LIỆU] |
| C-05 | Mô hình AI | Hằng tháng, theo lượt dùng | Số lượt/ngày × chi phí/lượt, có trần ngân sách theo ngày | [CẦN SỐ LIỆU] |
| C-06 | Kênh thông báo (Zalo ZNS, SMS, email) | Hằng tháng, theo tin | Số tin/tháng × đơn giá | [CẦN SỐ LIỆU] |
| C-07 | Vận hành, bảo trì, sao lưu | Hằng tháng | Giờ công người vận hành | [CẦN SỐ LIỆU] |
| C-08 | Đào tạo người dùng nội bộ và người đặt tổng | Một lần | Số buổi × số người | [CẦN SỐ LIỆU] |

### 8.2 Hạng mục lợi ích

| Mã | Lợi ích | Công thức | Gắn với |
|---|---|---|---|
| B-01 | Giảm cost thực phẩm vượt ngưỡng | Số suất/tháng × giá suất chưa VAT × số điểm phần trăm cost giảm được | BO-01, BO-02 |
| B-02 | Tiết kiệm giờ công dựng thực đơn, nhập Sheets, đối soát | Số giờ tiết kiệm/tháng × chi phí giờ công | BO-03, BO-07 |
| B-03 | Hợp đồng mới từ lead website | Số lead/tháng × tỷ lệ thắng × giá trị hợp đồng trung bình × biên lợi nhuận | BO-08 |
| B-04 | Giữ khách nhờ người ăn được chọn món và cảnh báo nguy cơ rời | Số khách giữ được/năm × doanh thu trung bình/khách × biên lợi nhuận | BO-05 |
| B-05 | Giảm chênh lệch và giảm trừ khi đối soát | Giá trị giảm trừ/tháng hiện tại × tỷ lệ giảm | BO-07 |

**Đơn vị quy đổi cho B-01** (không phải dự báo): với 1.000 suất/ngày, 26 ngày phục vụ/tháng, giá 40.000đ gồm VAT 8%, mỗi **1 điểm phần trăm** cost giảm được tương đương 1.000 × 26 × 37.037đ × 1% ≈ **9,6 triệu đồng/tháng**. Thay số suất thực tế của Gia Phát vào để có con số thật.

### 8.3 Số liệu Gia Phát cần cung cấp để tính ROI

| # | Số liệu | Dùng cho |
|---|---|---|
| 1 | Tổng số suất/ngày của 2 cơ sở, số công ty khách, số điểm giao | B-01, C-04, C-06 |
| 2 | Tỷ lệ cost thực phẩm thực tế 3 tháng gần nhất, theo tháng | B-01, cột "Hiện tại" của BO-01 |
| 3 | Thuế suất VAT đang xuất hoá đơn | B-01, BR-COST-002 |
| 4 | Số giờ/tuần dinh dưỡng viên dựng thực đơn; số giờ/tháng kế toán đối soát | B-02, BO-03, BO-07 |
| 5 | Số lead/tháng hiện tại, tỷ lệ thành hợp đồng, giá trị hợp đồng trung bình | B-03, BO-08 |
| 6 | Số khách rời trong 12 tháng gần nhất | B-04 |
| 7 | Giá trị giảm trừ/tháng khi đối soát | B-05 |
| 8 | Quy mô, đơn giá đội phát triển; nhà cung cấp hạ tầng | C-01, C-04 |
| 9 | Ngân sách AI tối đa mỗi tháng; nhà cung cấp mô hình | C-05 |

### 8.4 Công thức

- Lợi ích ròng năm = (B-01 + B-02 + B-03 + B-04 + B-05) × 12 − (C-04 + C-05 + C-06 + C-07) × 12
- ROI năm đầu = (Lợi ích ròng năm − (C-01 + C-02 + C-03 + C-08)) ÷ (C-01 + C-02 + C-03 + C-08)
- Thời gian hoàn vốn (tháng) = (C-01 + C-02 + C-03 + C-08) ÷ lợi ích ròng tháng

---

## 9. Rủi ro

Thang điểm: khả năng và tác động từ 1 (thấp) đến 3 (cao).

| Mã | Rủi ro | Khả năng | Tác động | Giảm thiểu | Chủ rủi ro |
|---|---|---|---|---|---|
| R-01 | Dữ liệu gốc (công thức, giá nhập, thành phần dinh dưỡng) nhập chậm hoặc sai → cost và dinh dưỡng sai | 3 | 3 | Nhập trước 30 món dùng nhiều nhất; người thứ hai duyệt công thức; không mở cổng khách trước khi đủ dữ liệu cho thực đơn 4 tuần | Dinh dưỡng viên |
| R-02 | Một dinh dưỡng viên gánh nhập liệu, duyệt AI và việc hằng ngày | 3 | 3 | Làm Agent Nội bộ ở đợt đầu; chỉ định người dự phòng quyền duyệt | Giám đốc |
| R-03 | Agent phía khách trả lời sai về dinh dưỡng, bệnh lý, hoặc để lộ cost | 2 | 3 | BN-16, BN-17; bộ kiểm thử riêng cho agent; ghi lại mọi lượt chạy | Đội phát triển |
| R-04 | Vi phạm quy định bảo vệ dữ liệu cá nhân khi thu dữ liệu sức khoẻ (Nghị định 13/2023/NĐ-CP và luật liên quan) | 2 | 3 | BN-19; lấy ý kiến pháp lý trước khi mở NUTR-04 | Giám đốc |
| R-05 | Mất thứ hạng tìm kiếm khi bỏ WordPress | 2 | 2 | BN-18; kiểm tra chuyển hướng 100% URL trước khi đổi tên miền; theo dõi BO-09 | Đội phát triển |
| R-06 | Chi phí AI vượt ngân sách do lượt dùng công khai | 2 | 2 | Trần ngân sách theo ngày; giới hạn lượt cho khách vãng lai; lưu sẵn kết quả thực đơn mẫu | Đội phát triển |
| R-07 | Người ăn không chọn món → tỷ lệ món mặc định cao, bếp nấu lệch nhu cầu thật | 2 | 2 | Nhắc trước hạn chốt; theo dõi BO-05 theo từng công ty | Dinh dưỡng viên |
| R-08 | Mã QR công ty bị chia sẻ ra ngoài → người lạ đăng ký được | 2 | 2 | Người đặt tổng xem và gỡ được tài khoản; đổi được mã QR | Đội phát triển |
| R-09 | Phạm vi 13 epic quá lớn so với đội phát triển | 3 | 3 | Làm theo đợt Now / Next / Later; không mở đợt sau khi đợt trước chưa đạt chỉ số | Giám đốc |
| R-10 | Khách công ty không muốn nhân viên tự chọn món | 2 | 1 | ORD-08: tắt chọn món theo từng khách, quay về một người đặt | Dinh dưỡng viên |

---

## 10. Giả định, ràng buộc, phụ thuộc

**Ràng buộc** (đã chốt)

- Công nghệ: ReactJS, Rust/Axum, MySQL [D-22, thay NodeJS/NestJS theo [CR-CORE-2026-001](../nen-tang/cr/CR-CORE-2026-001.md)].
- Tải: 1000 người dùng đồng thời.
- Không tuyển thêm nhân sự vận hành; giữ cơ cấu tổ chức hiện có (bản HTML, mục 0).
- MISA vẫn là hệ thống kế toán chính thức.

**Giả định** (sai thì phải xem lại BRD)

| Mã | Giả định |
|---|---|
| AS-01 | Người ăn có điện thoại vào được web để chọn món |
| AS-02 | Các công ty khách chấp nhận cho nhân viên quét QR và tự chọn món |
| AS-03 | Dinh dưỡng viên có thời gian nhập dữ liệu gốc trước khi mở cổng |
| AS-04 | Mỗi công ty khách có một người đặt tổng chịu trách nhiệm chốt tổng số suất |

**Phụ thuộc**

| Mã | Phụ thuộc | Chặn |
|---|---|---|
| DP-01 | Người soạn docx duyệt bảng 43 quy tắc | SRS epic thực đơn |
| DP-02 | Kế toán xác nhận thuế suất VAT và thành phần cost | SRS epic cost |
| DP-03 | Có bản "Bảng thành phần thực phẩm Việt Nam" để nhập | Epic dinh dưỡng |
| DP-04 | Chọn nhà cung cấp mô hình AI và hạ tầng | SRS nền tảng, hai epic agent |
| DP-05 | Quyền quản trị tên miền comgiaphat.com và WordPress hiện tại | Epic website |

---

## 11. Điểm mở

| Mã | Điểm mở | Ai trả lời | Chặn |
|---|---|---|---|
| O-01 | Cost gồm những khoản nào (gạo, gia vị, dầu ăn, tráng miệng, hộp/khay, gas); thuế suất VAT | Kế toán | BR-COST-002, 003; mục 8 |
| O-02 | Một món có một định lượng duy nhất hay nhiều cỡ định lượng với giá bán khác nhau | Dinh dưỡng viên | Mô hình dữ liệu công thức và giá món |
| O-03 | Gợi ý cá nhân có xét bệnh lý (tiểu đường, huyết áp, gout…) hay chỉ mục tiêu chung và dị ứng | Giám đốc | BN-19, BN-20, R-04 |
| O-04 | Quy mô đội phát triển, nhà cung cấp hạ tầng và mô hình AI, ngân sách | Giám đốc | Mục 8, lộ trình |
| O-05 | Trường học, bệnh viện, tiệc cỗ có trong phạm vi bản đầu không | Giám đốc | Mục 4 |
| O-06 | Ai giữ vai trò duyệt ngoại lệ (bản HTML ghi "Giám đốc" là giả định) và ai thay khi vắng | Giám đốc | Phân quyền |

Các câu hỏi vận hành kế thừa bản HTML (hạn chốt, ngưỡng đổi sau chốt, Zalo OA, quy tắc khi khách không xác nhận) không chặn BRD; chúng nằm ở mục 9 của kế hoạch tổng thể và được chốt ở SRS từng epic.

---

## 12. Tác động thay đổi so với bản thiết kế 04/11/2026

Theo `rules/15-change-request-impact-matrix.md`, bốn góc độ:

| Góc độ | Tác động |
|---|---|
| Tài liệu | Bản HTML cần cập nhật: mục 0 (bỏ "mỗi công ty một người đặt tổng nhập số"), mục 2 (thang 7 loại số lượng: thêm cấp món/suất), mục 3 (người ăn không còn ẩn danh), mục 4 (kiến trúc phân hệ, ERD), mục 5 (lộ trình). Bản HTML hiện **không còn là nguồn đúng** cho các phần này. |
| Kỹ thuật | Thêm 8 nhóm thực thể: người dùng/vai trò, cơ sở, nguyên liệu, giá nhập, loại suất, giá bán món, người ăn + lựa chọn món, thành phần dinh dưỡng. Thêm hàng đợi và worker cho AI. Thêm site công khai có SSR. |
| Kiểm thử | Chưa có test case nào từ bản cũ nên không có gì bị vô hiệu. Phát sinh 3 nhóm kiểm thử mới: kiểm thử tải 1000 người dùng đồng thời, kiểm thử bộ quy tắc (43 quy tắc), kiểm thử hành vi 2 agent. |
| Kế hoạch & rủi ro | Lộ trình 4 giai đoạn của bản HTML bị thay bằng 13 epic chia 3 đợt. Cost chuyển từ giai đoạn 3 lên đợt đầu. Thời lượng chưa ước tính được (O-04). |

---

## 13. Điều kiện duyệt BRD

BRD chuyển sang v1.0.0 khi:

- [ ] Giám đốc xác nhận mục tiêu và mức mục tiêu ở mục 3.
- [ ] Giám đốc xác nhận phạm vi mục 4, gồm cả O-05.
- [ ] Kế toán trả lời O-01.
- [ ] Có đủ 9 số liệu ở mục 8.3 và bảng ROI được điền.
- [ ] O-03, O-04, O-06 có câu trả lời.
