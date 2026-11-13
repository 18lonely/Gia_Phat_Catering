# Tiêu chí nghiệm thu bổ sung nghiệp vụ kế toán

Phiên bản 0.1.0 · 11/11/2026 · Draft bổ sung cho [CR-COST-2026-001](../cr/CR-COST-2026-001.md).

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | 12 ca bổ sung giá mua/VAT/chiết khấu riêng; chưa chạy backend |

12 ca này nằm ngoài108 ca baseline. Tiền/VAT là fixture giả định. NOT RUN nghĩa chưa chạy phần mềm; BLOCKED nghĩa còn thiếu quyết định hoặc hợp đồng. Kiểm script số học không đổi trạng thái các ca này thành PASS.

| Mã | Given (dữ liệu/tiền điều kiện) | When (thao tác) | Then (kết quả mong đợi) | Truy vết | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-ACC-001 | Giá báo100000/kg chưa VAT; VAT xác nhận trong fixture8% | Chuẩn hóa giá rồi tính70g | Giá cost108000/kg; dòng cost7560 | ACC-CONF-01/02; PRC001, DISH001 | NOT RUN |
| TC-ACC-002 | Giá báo108000/kg đã gồm VAT | Chuẩn hóa rồi tính70g | Giữ108000, không thành116640; cost7560 | ACC-CONF-02 | NOT RUN |
| TC-ACC-003 | Giá cuối100000/kg được NCC xác nhận không cộng thêm khoản VAT | Tính70g | Cost7000; không tự tạo phân loại thuế từ câu xác nhận | ACC-CONF-01/02 | NOT RUN |
| TC-ACC-004 | Giá báo100000 nhưng chưa biết cách ghi/VAT phải trả | Thử dùng làm giá tham chiếu | Không tự coi100000 là giá cuối; yêu cầu xác nhận, không tính cost đạt dựa trên giá chưa rõ | ACC-CONF-01/02 | BLOCKED: trạng thái lưu nháp/mã lỗi API |
| TC-ACC-005 | Giá nguyên liệu đã hiệu lực và có snapshot; bổ sung cách ghi VAT sau đó | Cập nhật nguồn giá cho ngày tương lai | Snapshot cũ không đổi, không cộng VAT hồi tố hàng loạt | BR-CALC-010; CR | NOT RUN |
| TC-ACC-006 | Hai đơn có cùng giá/VAT đã xác định, chỉ khác invoiceRequested | Tính tiền và doanh thu dùng kiểm cost | Cờ hóa đơn không tự thay giá hoặc VAT | ACC-CONF-03 | NOT RUN |
| TC-ACC-007 | Khách không yêu cầu hóa đơn, cách ghi giá suất/VAT chưa rõ | Tính doanh thu chưa VAT | Không tự gánVAT0; đánh dấu thiếu context và chưa kết luận cost% | ACC-CONF-03 | BLOCKED: sales context/mã lỗi |
| TC-ACC-008 | Đơn100 suất giá40000, cơ sở% giả định là4000000, chiết khấu5% | Ghi khoản riêng theo đơn | Khoản riêng200000; đơn phải trả4000000; chưa có giao dịch chi tiền | ACC-CONF-04/05 | BLOCKED: cơ sở% và quyền ghi nhận |
| TC-ACC-009 | Đơn100 suất giá40000, chiết khấu2000/suất | Ghi khoản riêng | Khoản riêng200000; đơn vẫn4000000; không sửa đơn giá thành38000 | ACC-CONF-04/05 | NOT RUN |
| TC-ACC-010 | Đơn có cả điều kiện% và tiền/suất, chưa có quy định cộng dồn | Yêu cầu tính khoản | Không tự cộng hai khoản; yêu cầu xác định chương trình/cách tính áp dụng | ACC-CONF-04 | BLOCKED: quy tắc nhiều điều kiện |
| TC-ACC-011 | Khoản riêng đã xác nhận; đơn đổi100 thành80 suất hoặc bị hủy | Ghi thay đổi đơn | Giữ lịch sử, đánh dấu khoản cần rà lại; cách điều chỉnh/đảo/chi trả theo quyết định, không tự thanh toán | CR | BLOCKED: vòng đời điều chỉnh |
| TC-ACC-012 | Đơn100×40000, khoản riêng200000; ngưỡng Cost52% theo baseline | Xem tiền đơn, khoản riêng và Cost% | Không tự giảm số phải trả, trừ mẫu số Cost hoặc cộng vào cost nguyên liệu; nếu cần chỉ số sau chiết khấu phải tách riêng và chốt | ACC-CONF-05; E2-Q1 | BLOCKED: tác động chỉ số sau chiết khấu |

Cách chạy khi có backend: tạo fixture riêng mỗi ca; gọi endpoint/UI theo hợp đồng đã review; lưu requestId, payload, kết quả, bản ghi đơn/khoản riêng/giá trước-sau và audit; ghi actual/evidence/defect. Các ca trên chưa chỉ định URL mới vì hợp đồng bổ sung chưa được chốt. Quyền, giới hạn giá trị, rounding và concurrency cần thêm kiểm tích hợp khi thiết kế đủ chi tiết.
