# Hướng dẫn nghiệp vụ kế toán Cost

Phiên bản 0.1.0 · 11/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Quy trình kế toán nhập giá, dự toán, đối soát và ghi riêng chiết khấu |

## 1. Phân công theo quyền hiện có

Kế toán mua hàng quản lý NCC/giá, đề nghị khoản khoán và lập dự toán. Dinh dưỡng viên lập bảng món đặc thù; Giám đốc duyệt. Kế toán doanh thu có quyền xem giá/cost/dự toán trong SRS, chưa có quyền ghi giá hoặc đóng cảnh báo. Quyền lập/duyệt khoản chiết khấu theo đơn chưa chốt; không tự dùng quyền kế toán mua hàng thay thế.

## 2. Nhận và nhập giá nguyên liệu

1. Kiểm tên nguyên liệu, đơn vị mua và hệ số chuyển sang đơn vị công thức. Báo giá theo thùng/túi phải biết quy cách trước khi dùng giá trên kg/quả.
2. Xác định NCC, cơ sở riêng hay giá chung, ngày hiệu lực; kiểm NCC còn hoạt động.
3. Xác định giá báo đã gồm VAT, chưa gồm VAT hay NCC đã xác nhận số cuối phải trả. Nếu chưa rõ, hỏi nguồn báo giá trước khi dùng làm giá tham chiếu.
4. Với giá chưa VAT, xác định VAT phải trả rồi tính giá cuối. Cost dùng giá cuối theo xác nhận người dùng; giá đã gồm VAT không cộng thêm lần hai.
5. Kiểm giá mới so giá tham chiếu cùng cơ sở. Trong thiết kế hiện tại, biến động vượt ngưỡng cấu hình yêu cầu xác nhận; xác nhận khác với bước duyệt của người thứ hai.
6. Gắn chứng từ nếu có. P1 hỗ trợ ảnh/PDF; chứng từ không tự thay việc xác nhận cách ghi giá.
7. Kiểm danh sách sau lưu: NCC, đơn vị, ngày, cơ sở và giá cuối đúng. Mất phản hồi thì đối soát request/lịch sử trước gửi lại; không nhập lần thứ hai bằng khóa mới chỉ vì màn hình báo timeout.

Mở [mẫu kế toán SCR-ACC-01](html-wireframe/accounting-workbench.html) để thử giá báo/VAT. Wireframe Cost04/05 dùng giá giả định đã chuẩn hóa; mẫu mới không đọc XLSX thật.

## 3. Sửa giá và xử lý NCC ngừng

- Giá đã hiệu lực: thêm dòng giá mới theo ngày cho phép; không sửa/xóa dòng cũ hoặc bản chụp cũ.
- Giá chưa hiệu lực: có thể hủy theo luồng, cần lý do. Nếu đang là tham chiếu và còn giá khác cùng nhóm, chờ phương án thay thế Q01; không tự chọn nhà cung cấp rẻ nhất.
- NCC ngừng: không nhập giá mới; giá cũ phục vụ lịch sử giữ nguyên. Theo dõi nguyên liệu đang dùng nguồn này và lập nguồn giá thay thế theo quy trình.
- Chênh lệch giữa báo giá và chứng từ đến sau: ghi rõ căn cứ, giữ bản cũ; phạm vi hồi tố và quy đổi VAT phần lẻ phải theo quyết định được chốt.

## 4. Khoản khoán và kiểm cost thực đơn

Kế toán đề nghị từng khoản cố định trên suất với tên, số tiền, loại suất, ngày hiệu lực và lý do. Khoản PENDING chưa tính. Người khác có quyền duyệt mới cho hiệu lực. Khoản riêng loại suất ưu tiên khoản chung cùng tên, không cộng cả hai.

Không nhập chiết khấu khách vào khoản khoán. Gạo/dầu/gia vị phải thống nhất tính theo công thức hay khoán để tránh cộng hai lần; danh sách thành phần O-01 chưa được chốt toàn bộ.

Kiểm cost theo đúng ngày phục vụ/cơ sở. Thiếu giá, thiếu VAT cần thiết hoặc thiếu bảng món đặc thù không được coi là cost0. Chế độ CANH_BAO chỉ cho qua trường hợp vượt ngưỡng có đủ dữ liệu, không bỏ qua các lỗi thiếu đầu vào.

## 5. Lập và đối soát dự toán

1. Chọn ngày, cơ sở và đúng bản thực đơn. Nhập số suất theo từng món chính; K>1 còn chờ Q15.
2. Kiểm giá cuối đã gồm VAT phải trả cho từng nguyên liệu, công thức và khoản khoán đã duyệt.
3. Kiểm lượng dùng → lượng mua sau làm tròn lên; hao hụt chỉ áp một lần.
4. Lưu thành phiên bản có người/thời điểm; lập lại tạo bản mới, không đè bản cũ.
5. So bảng kế toán tại cùng thời điểm/cơ sở/cấu hình; tách nguyên nhân chênh lệch thành giá, quy đổi, định lượng, hao hụt, khoản khoán hoặc mẫu số doanh thu.
6. Ghi expected/actual/delta và nguồn. Dùng [phiếu kế toán](review/accountant-input.md); không sửa expected để làm số của hệ thống khớp.

Đây là đối soát cách tính dự toán với kế toán. Đối chiếu dự toán với nhận hàng, thực mua và công nợ thuộc R11, chưa phải chức năng đã có ở Cost R3.

## 6. Ghi chiết khấu cho đơn khách

1. Chọn đúng đơn và khách; giữ nguyên số tiền phải trả của đơn.
2. Xác định dòng suất được hưởng và số suất đủ điều kiện, cách tính % hoặc tiền/suất.
3. Ghi cơ sở % theo thỏa thuận; khi chưa chốt cơ sở VAT không xác nhận khoản tự tính.
4. Lập khoản riêng, ghi điều kiện/nguồn, người lập, thời điểm và liên kết đơn. Trạng thái/duyệt theo thiết kế sẽ được xác nhận.
5. Đối chiếu:100 suất giá40000 → phải trả4000000; khoản riêng200000 không làm phải trả thành3800000.
6. Nếu đơn đổi/hủy, rà lại khoản liên quan. Không tự sửa khoản đã xử lý thanh toán; cơ chế điều chỉnh/đảo cần đặc tả riêng.

Khách không yêu cầu hóa đơn: ghi cờ nhu cầu hóa đơn, không đổi giá hay VAT chỉ từ cờ đó. Ghi nhận khoản chiết khấu không có nghĩa đã chi tiền, đã bù trừ hoặc hoàn tất nghĩa vụ thanh toán.

## 7. Tra cứu sự cố

| Hiện tượng / mã theo SRS | Cách xử lý |
| :--- | :--- |
| ERR-COST-409-01: NCC trùng | Tìm NCC hiện có sau chuẩn hóa tên, không tạo biến thể tên để lách |
| ERR-COST-409-02: trùng giá cùng tuple | Kiểm lịch sử ngày/NCC/cơ sở; đối soát xem lần trước đã lưu chưa |
| ERR-COST-409-03: giá đã hiệu lực | Thêm giá mới, không sửa dòng cũ |
| ERR-COST-422-01: giá không nguyên dương | Kiểm đơn vị mua và số tiền; giá quy đổi VAT có phần lẻ cần chốt quy tắc, không tự cắt phần lẻ |
| ERR-COST-422-02: ngày sai/NCC ngừng | Chọn ngày trong phạm vi cho phép hoặc NCC hoạt động; mã NCC ngừng còn cần thống nhất với404-01 |
| ERR-COST-422-03: thiếu giá | Bổ sung nguồn giá hợp lệ; không nhập0 để qua lỗi |
| ERR-COST-422-05: thiếu VAT/doanh thu0 | Xác minh điều kiện giá; không dùng nhu cầu hóa đơn làm giá trị VAT |
| ERR-COST-422-06: khoản khoán sai | Kiểm tiền nguyên không âm và ngày hiệu lực |
| ERR-COST-422-07: vượt ở CHAN | Phối hợp DD điều chỉnh món; không tự hạ VAT/giá hoặc dùng chiết khấu để lách |
| ERR-COST-422-08: số suất sai | Sửa số nguyên không âm và tổng lớn hơn0 |
| ERR-SYS-403-01: tự duyệt | Chuyển người có thẩm quyền khác người tạo/người sửa cuối |
| Timeout sau gửi | Đối soát; chưa biết đã lưu hay chưa. Giữ mã yêu cầu và payload, tránh tạo trùng |

Mã lỗi mới cho giá/VAT/chiết khấu bổ sung chưa được cấp trong hợp đồng API; không tái sử dụng mã cũ có ý nghĩa khác chỉ để hiển thị thông báo.
