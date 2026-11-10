# Gia Phát — Phân tích bản thiết kế C-MAP/CRM so với mục tiêu mới

Ngày: 10/11/2026 · Nguồn đối chiếu: `GiaPhat_CMAP_CRM.html` (bản 1.0, 04/11/2026), `Yêu cầu về thực đơn và cost tp.docx`, website comgiaphat.com (WordPress + Elementor, 1 landing + blog, form "Yêu cầu tư vấn").

Mức độ: **A** = chặn thiết kế, phải quyết trước · **B** = sai lệch logic, cần sửa trong thiết kế · **C** = tối ưu.

---

## 1. Kết luận ngắn

Bản HTML là một thiết kế **vận hành nội bộ + CRM B2B** khá chặt (7 loại số lượng, phiên bản kế hoạch, giá snapshot, khoá kỳ). Nhưng nó **không phủ 3 thứ anh đang muốn làm** và có một số điểm tự mâu thuẫn:

1. Không có lớp **cost / định lượng theo mức giá suất** — trong khi file docx coi đây là cổng kiểm soát bắt buộc trước khi chốt thực đơn.
2. Không có mô hình dữ liệu cho **quy tắc xây thực đơn** (cơ cấu món, nguyên liệu chính, phương pháp chế biến, vị…) nên AI agent không có gì để dựa vào.
3. Không có **kiến trúc kỹ thuật** (chỉ có kiến trúc chức năng), và giả định quy mô của nó (vài chục người dùng) lệch hẳn với mục tiêu 1000 người dùng đồng thời.

---

## 2. Mâu thuẫn giữa bản thiết kế và mục tiêu mới

| # | Mức | Điểm bất hợp lý | Dẫn chứng | Hệ quả |
|---|---|---|---|---|
| 2.1 | A | **Ai là "1000 user đồng thời"?** Thiết kế chốt "mỗi công ty một người đặt tổng", người ăn chỉ đánh giá QR ẩn danh, không có tài khoản. Website ghi 125+ đối tác; dashboard mẫu ~2.100 suất/ngày. Với mô hình này đồng thời thực tế chỉ vài chục. | Mục 0 "Quyết định đã chốt"; mục 3 "Thu thập & lưu trữ hồ sơ" | 1000 CCU chỉ có nghĩa nếu **người ăn tự chọn món** hoặc tính năng dinh dưỡng mở **công khai**. Cả hai đều phá vỡ mô hình order hiện tại (số đặt không còn do 1 người nhập). |
| 2.2 | A | **Cost bị đẩy về giai đoạn 3**, còn docx yêu cầu "kiểm tra tổng cost trước khi chốt thực đơn", ngưỡng 52% doanh thu. | HTML: M10 = GĐ3; "giá dưới giá sàn (khi có dữ liệu chi phí — GĐ3)". Docx: phần Cost mục I, IV | Tính năng chọn menu theo định lượng + AI tạo menu **không làm được ở GĐ1** nếu giữ lộ trình cũ. Cost phải lên GĐ1. |
| 2.3 | A | **Không có bảng giá nguyên liệu theo thời gian.** ERD có NCC & công nợ, có công thức (định lượng, hao hụt) nhưng không có thực thể giá nhập theo NCC/ngày. | ERD mục 4 | Không tính được cost/suất, không lập được "bảng dự toán" như docx mục IV. Biểu đồ "nhu cầu ròng vs thực mua (triệu đồng)" trong dashboard không có nguồn dữ liệu. |
| 2.4 | A | **Thiếu khái niệm "suất" (combo).** Phụ lục giá tính theo *loại suất · đơn giá*, nhưng dòng order lại theo *món* và có "đơn giá snapshot". Không có thực thể nối suất ↔ các món trong suất. | ERD: `Phụ lục giá hiệu lực` vs `Order & dòng order` | Không biết doanh thu tính theo suất hay theo món; cost % (cost các món / giá suất) không có mẫu số. |
| 2.5 | A | **Định lượng chỉ có một giá trị**, trong khi docx quy định định lượng thay đổi theo đơn giá suất (bảng chuẩn ở 40k) và theo kiểu món (thịt kho trứng 65–70g, chiên/rang thuần thịt 85–90g). | Docx: Bảng định lượng, mục III | Công thức phiên bản cần thêm chiều **mức giá suất** và khoảng min–max, đơn vị không phải gram (bìa, quả). |
| 2.6 | A | **Món thiếu thuộc tính để áp quy tắc.** Thực thể Món chỉ có ảnh, mô tả, dinh dưỡng, dị ứng, nhãn mục tiêu. Docx cần: vai trò (chính/phụ/rau/canh), nguyên liệu chính, phương pháp chế biến, vị (chua…), khô/sốt, cờ Healthy, độ cầu kỳ sơ chế, chịu được vận chuyển, mùa, nhóm cost. | ERD `Món (đã duyệt)` | Không kiểm tra tự động được "không 2 món cùng chiên", "không lặp nguyên liệu ngày liền kề", "1 món luộc Healthy". AI agent chỉ còn đoán. |
| 2.7 | B | **"Dinh dưỡng" chưa có chuẩn nào.** Docx chỉ nói định lượng sống và cost, không có kcal/đạm/béo/bột. Thiết kế ghi "DDV nạp toàn bộ dữ liệu dinh dưỡng" nhưng không nói nguồn (bảng thành phần thực phẩm nào). | Docx mục III (thực đơn) chỉ định tính | Tính năng dinh dưỡng cho khách chưa có dữ liệu gốc lẫn tiêu chuẩn để so. |
| 2.8 | B | **Website và form tư vấn không nối vào CRM** ("nhập tay; form nhúng cần khảo sát"). | Mục 4 bảng tích hợp | Lead từ kênh chính vẫn rơi rụng — đúng vấn đề thiết kế muốn giải quyết. Site là WordPress nên nối form → API là việc nhỏ. |
| 2.9 | B | **Không có yêu cầu phi chức năng**: tải, thời gian phản hồi, sao lưu, bảo mật, đăng nhập, triển khai, giám sát. "Một cơ sở dữ liệu" là toàn bộ mô tả kỹ thuật. | Mục 4 | Không có căn cứ chọn hạ tầng; mục tiêu 1000 CCU chưa được đặt vào đâu. |
| 2.10 | B | **Lộ trình không chứa tính năng mới.** 10 phân hệ trong 10 tháng cho "đội tự xây nhỏ", chưa gồm site công khai, dinh dưỡng, AI. | Mục 5 | Phải xếp lại ưu tiên, không cộng thêm được. |

---

## 3. Điểm chưa hợp lý bên trong bản thiết kế

### 3.1 Tổ chức & kiểm soát

| # | Mức | Vấn đề | Đề xuất |
|---|---|---|---|
| 3.1.1 | B | **DDV là điểm nghẽn đơn.** Một người làm đầu mối chặng 1, 2, 3, 10a, nạp toàn bộ dữ liệu dinh dưỡng, duyệt công thức, duyệt món thay thế, gọi xác nhận khách, xử lý chênh lệch. Nghỉ 1 ngày là dừng dòng. | Người dự phòng cho từng quyền duyệt; AI agent và cổng tự đặt phải **giảm** việc của DDV chứ không thêm bước duyệt. |
| 3.1.2 | B | **Tự tạo – tự duyệt.** Bảng phân quyền cho DDV cả `T · D` ở công thức/dinh dưỡng và ở đề xuất/công bố thực đơn. Thiết kế tự nêu nguyên tắc tách nhiệm vụ nhưng vi phạm ở đây. | Cost & định lượng do người thứ hai duyệt (GĐ hoặc kế toán) — vì nó quyết định biên lợi nhuận. |
| 3.1.3 | B | **Kế toán vừa đặt NCC, vừa ghi công nợ NCC, vừa thanh toán**; mở lại kỳ đã khoá chỉ cần "thông báo" GĐ. Tách nhiệm vụ mới chỉ có giữa đặt và nhận. | Mở lại kỳ cần GĐ duyệt; hai kế toán chéo nhau giữa đặt hàng và thanh toán. |
| 3.1.4 | B | **Vai trò Giám đốc là "giả định"** nhưng mọi ngoại lệ đều dồn về đây (giá, điều chuyển, vượt ngưỡng, giảm trừ, gộp hồ sơ). | Xác nhận người thật và người uỷ quyền khi vắng. |

### 3.2 Quy trình & số liệu

| # | Mức | Vấn đề | Đề xuất |
|---|---|---|---|
| 3.2.1 | B | **Doanh thu treo vô thời hạn.** "Không coi im lặng là đồng ý", nhắc 2 lần rồi DDV gọi — không có trạng thái kết thúc. Kênh nhắc là link + email trong khi khách dùng Zalo; Zalo OA "cần khảo sát". | Điều khoản HĐ: quá N ngày không phản đối thì lấy số giao làm số tạm tính, chốt lại ở đối soát tháng. Zalo OA/ZNS là phụ thuộc chặn, khảo sát ngay. |
| 3.2.2 | B | **Ngưỡng đổi sau chốt mơ hồ**: "≤ 5% hoặc ≤ 10 suất". Điểm 20 suất đổi 10 suất = 50% vẫn "trong ngưỡng"; điểm 1.000 suất đổi 50 suất cũng vậy. | Viết rõ `min(5%, 10 suất)` hay `max(...)`, có sàn/trần. |
| 3.2.3 | B | **Mốc thời gian chồng nhau.** Nhận nguyên liệu 05:30 nhưng cửa sổ đổi thường mở đến 06:00. Đặt NCC 16:30 D-1 trong khi hiện trạng "phần lớn mua trong ngày từ tiểu thương". | Cửa sổ đổi đóng trước giờ đặt/mua; tách mốc theo nhóm NL (đông lạnh đặt trước, tươi mua sáng). |
| 3.2.4 | B | **Số theo món hay theo suất?** Bảy loại số lượng không nói rõ độ chi tiết. Nếu theo món thì người nhận phải xác nhận từng món — không khả thi; nếu theo suất thì dòng order theo món là thừa. | Chốt: đặt/giao/nhận/tính tiền theo **suất**; món chỉ dùng cho kế hoạch sản xuất. |
| 3.2.5 | C | **Phân bổ tồn theo lô** cho bếp mua hằng ngày bằng phiếu viết tay là quá nặng so với ~10 người/cơ sở. | Chỉ quản lý lô cho hàng đông lạnh/khô; hàng tươi coi như mua–dùng trong ngày. |
| 3.2.6 | C | **Tiệc cỗ đi chung workflow suất ăn**: tiệc tính theo mâm, có đặt cọc, thực đơn riêng, không có hạn chốt D-1 kiểu ca trưa. | Chung hồ sơ khách và doanh thu, tách loại đơn. |
| 3.2.7 | C | Số liệu lệch nhau: website "125+ đối tác", dashboard mẫu "26 khách" đối soát; website nêu trường học, bệnh viện còn phạm vi thiết kế chỉ có công nghiệp/văn phòng. | Xác nhận quy mô thật để định cỡ. |

### 3.3 Dữ liệu (ERD)

Thiếu các thực thể: **Người dùng/vai trò**, **Cơ sở (bếp)**, **Nguyên liệu** (danh mục chủ), **Giá nhập theo NCC/ngày**, **Loại suất/combo**, **Lịch phục vụ của điểm** (được dùng trong tín hiệu "nguy cơ rời" nhưng không có bảng), **Sự cố/phiếu phối hợp**, **Khoản thu** tách khỏi đối soát. Quan hệ `Order → Kế hoạch` ghi "gộp" nhưng không nói khoá gộp (cơ sở · ngày · ca).

---

## 4. Vấn đề của chính file docx khi đưa vào hệ thống / AI

| # | Vấn đề | Cần làm |
|---|---|---|
| 4.1 | Phần lớn quy tắc là định tính: "hạn chế tối đa", "không nên", "hài hòa", "cân đối". Máy không kiểm được. | Phân loại từng quy tắc thành **cứng** (vi phạm = chặn) / **mềm** (trừ điểm), kèm con số: "nhiều ngày liên tiếp" = mấy ngày, "lặp trong tuần" = mấy lần. |
| 4.2 | Bảng định lượng chỉ có mức 40k. | Cần bảng cho các mức giá đang bán, hoặc quy tắc nội suy. |
| 4.3 | "52% doanh thu suất ăn" chưa rõ: trước/sau VAT; có gồm gạo, gia vị, dầu, gas, hộp/khay không. | Định nghĩa công thức cost chính thức. |
| 4.4 | "01 món chính là món luộc Healthy" — cố định là luộc, hay hấp/áp chảo ít dầu cũng tính? | Chốt danh sách phương pháp được coi là Healthy. |
| 4.5 | 3 món chính/ngày: mỗi người ăn chọn 1 trong 3, hay công ty chọn 1 cho tất cả, hay cả 3 cùng có trong suất? | Quyết định này định hình cả cổng đặt lẫn kế hoạch sản xuất. |
| 4.6 | Không có chỉ tiêu dinh dưỡng nào (kcal, đạm, béo, bột, muối). | Nếu muốn "dinh dưỡng cho khách" thì phải có chuẩn và nguồn dữ liệu thành phần. |

---

## 5. Hướng tối ưu
- **Tách 3 mặt tiền, 1 lõi**: site công khai (comgiaphat.com) · cổng khách hàng/dinh dưỡng · subdomain quản trị — dùng chung một API NestJS + MySQL.
- **Đưa "Thực đơn – Định lượng – Cost" lên làm phân hệ lõi GĐ1**: nguyên liệu + giá nhập theo thời gian → công thức theo mức giá suất → cost/suất → kiểm tra 52% → thực đơn tuần đã kiểm quy tắc.
- **AI agent không tự tính số.** Mô hình ngôn ngữ chỉ hiểu yêu cầu và đề xuất tổ hợp món; cost, định lượng, kiểm quy tắc do code xác định (tool) thực hiện; kết quả luôn kèm danh sách quy tắc đạt/vi phạm; chạy qua hàng đợi để không kéo sập API khi đông người.
- **1000 CCU** với NestJS + MySQL không khó nếu: API stateless chạy nhiều bản, Redis cho cache thực đơn/phiên, đọc–ghi tách, hàng đợi cho AI và thông báo. Điểm nghẽn thật là **giờ chốt order** (ghi dồn) và **lời gọi AI** (chậm, tốn tiền) — thiết kế tập trung vào hai chỗ đó.
- **Minh bạch** nên chia 2 lớp: lớp cho khách (định lượng, thành phần, dinh dưỡng, dị ứng, lịch sử giao–nhận, đối soát) và lớp nội bộ (giá nhập, cost %, biên lợi nhuận) — không lộ lớp sau ra cổng khách.
