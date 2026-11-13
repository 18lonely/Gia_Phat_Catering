# Phiếu cung cấp dữ liệu đối soát của kế toán

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-01; ACC-CONF-02 |


Phiên bản 0.1.1 · 11/11/2026 · Trạng thái: Chưa nhận dữ liệu thực tế.

Mục đích: chuẩn bị đầu vào cho NFR-COST-002 và TC-COST-010-06. Cần 10 món và 10 ngày mẫu có kết quả tính tay độc lập. Không dùng kết quả do script hoặc backend đang kiểm tự sinh làm expected. [Bộ số giả định](../test/fixtures/README.md) chỉ là ví dụ cách tính, chưa thay thế dữ liệu này.

## Thông tin bộ dữ liệu

| Trường | Giá trị cần điền |
| :--- | :--- |
| Mã bộ dữ liệu / phiên bản | Chưa cung cấp |
| Kế toán lập / người review / ngày xác nhận | Chưa cung cấp |
| Nguồn bảng tính tay/chứng từ | Chưa cung cấp; ghi tên file, phiên bản và vị trí lưu |
| Cơ sở / khoảng ngày tính | Chưa cung cấp |
| Giá nhập bao gồm khoản gì, VAT đầu vào xử lý thế nào | Cost nguyên liệu gồm VAT phải trả NCC theo [ACC-CONF-02](../accounting/business-rules.md); XC-01. Thành phần cost khác vẫn chờ O-01 |
| Giá suất đã gồm VAT / VAT bán ra / ngưỡng Cost | Chưa cung cấp; ghi nguồn quyết định và thời gian hiệu lực |
| Phương pháp món chính / K / món mặc định | Chưa cung cấp; gắn E3-Q1/Q12/Q15 |
| Áp hao hụt hay không; định lượng đã gồm phần bỏ chưa | Chờ E3-Q2 |
| Danh sách khoản khoán và nguyên liệu không tính cost | Chờ O-01 |

## Danh sách nhận dữ liệu

| Mẫu | Món/ngày thực tế và cơ sở | File nguồn | Expected tính tay | Người xác nhận | Tình trạng |
| :--- | :--- | :--- | :--- | :--- | :--- |
| REAL-DISH-01 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-02 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-03 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-04 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-05 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-06 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-07 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-08 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-09 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DISH-10 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-01 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-02 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-03 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-04 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-05 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-06 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-07 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-08 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-09 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |
| REAL-DAY-10 | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa nhận |

## Phiếu chi tiết mỗi món: sao chép cho 10 mẫu

Mã mẫu: …; mã/tên món: …; cỡ định lượng: …; mã/phiên bản công thức: …; ngày hiệu lực công thức: …; ngày tính: …; cơ sở: …; trạng thái thực đơn nếu công thức đã gắn: …

| Nguyên liệu | Chính/phụ | Định lượng chuẩn | Đơn vị dùng | Đơn vị mua | Hệ số mua→dùng | Hao hụt% | Tính cost? | NCC | Giá/đơn vị mua | Ngày hiệu lực giá | Riêng/chung | Nguồn |
| :--- | :--- | ---: | :--- | :--- | ---: | ---: | :--- | :--- | ---: | :--- | :--- | :--- |
| Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có | Chưa có |

Expected từng dòng trước làm tròn: …; tổng cost chính xác: …; số hiển thị sau làm tròn: …; cách tính tay/file ô nguồn: …; người kiểm: …

Không điền giá 0 cho nguyên liệu thiếu giá. Tách rõ nguyên liệu không tính cost và nguyên liệu cần tính nhưng chưa có giá. Với hao hụt, ghi rõ đã áp vào định lượng hay chưa để tránh áp hai lần.

## Phiếu chi tiết mỗi ngày: sao chép cho 10 mẫu

Mã mẫu: …; ngày phục vụ/cơ sở: …; loại suất/giá: …; VAT: …; K: …; phương pháp chính: …; món mặc định: …; ngưỡng có hiệu lực: …

| Vai trò món/khoản | Mã món hoặc tên khoản | Công thức/phiên bản | Cost chưa làm tròn | Nguồn cost | Phạm vi khoản khoán/ngày hiệu lực |
| :--- | :--- | :--- | ---: | :--- | :--- |
| Món chính (liệt kê tất cả, kể cả Healthy) | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có |
| Món phụ | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có |
| Rau | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có |
| Canh | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có |
| Khoản khoán (mỗi khoản một dòng) | Chưa cung cấp | Chưa có | Chưa có | Chưa có | Chưa có |

Expected: phần chính A=…; phụ/rau/canh B=…; khoán E=…; cost suất=…; doanh thu chưa VAT=…; cost% chưa làm tròn=…; cost% sau làm tròn=…; đạt/vượt=…; dư/vượt tiền=…

Nếu cung cấp thêm dự toán, ghi số suất theo từng món, N suy ra từ K, lượng từng nguyên liệu trước/sau làm tròn mua và khoản khoán ×N. Phân biệt cost% kiểm thực đơn với cost% dự toán.

## Cổng tiếp nhận và ghi chênh lệch

QA chỉ đánh dấu bộ dữ liệu sẵn sàng khi đủ nguồn, đơn vị, cấu hình và xác nhận kế toán. Sai khác phải ghi expected/actual/delta và nguyên nhân: dữ liệu, chọn giá/công thức, VAT, hao hụt hoặc làm tròn. Không sửa expected chỉ để khớp phần mềm.

Theo NFR-COST-002: lệch cost món không quá 1đ và cost% không quá 0,01 điểm phần trăm. Các ca ranh giới làm tròn/quy tắc dùng expected cụ thể trong AC; mức dung sai này không cho phép đổi nhãn đạt/vượt sai quy tắc. Chưa có người ký, ngày ký hay số liệu thực tế trong phiếu này.

## Điều chỉnh khi cung cấp dữ liệu thực tế

Theo xác nhận mới, cost nguyên liệu gồm VAT phải trả. Với mỗi giá, bổ sung giá báo, đã/chưa gồm VAT, VAT phải trả và giá cuối; không để giá trướcVAT đi vào cột giá cost. Với khách, tách cờ yêu cầu hóa đơn khỏi cách ghi giá/VAT. Nếu có chiết khấu, ghi khoản riêng liên kết đơn, không trừ tiền phải trả; bổ sung điều kiện%, tiền/suất và trạng thái xử lý. Xem [nghiệp vụ kế toán](../accounting/business-rules.md).

## Câu hỏi dữ liệu thực tế: CHỜ CUNG CẤP

Người dùng xác nhận trong phiên11/11/2026: **chưa có dữ liệu, đặt câu hỏi trong tài liệu**. Đã kiểm workspace D:/BA, chưa có bảng giá/chứng từ/bảng tính10 món10 ngày thực tế. Không thay thế bằng dữ liệu giả để đóng NFR-COST-002.

| Mã | Câu hỏi cần trả lời | Trạng thái |
| :--- | :--- | :--- |
| DATA-COST-Q01 | Ai phụ trách cung cấp và xác nhận10 món/10 ngày thực tế? Khi nào có dữ liệu? | CHỜ CUNG CẤP |
| DATA-COST-Q02 | File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào? | CHỜ CUNG CẤP |
| DATA-COST-Q03 | Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào? | CHỜ CUNG CẤP |
| DATA-COST-Q04 | Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào? | CHỜ CUNG CẤP |
| DATA-COST-Q05 | Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập? | CHỜ CUNG CẤP |
| DATA-COST-Q06 | Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào? | CHỜ CUNG CẤP |
