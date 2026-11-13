---
id: DOC-E9-REVIEW-QUESTIONS-MD
title: Sổ câu hỏi mở E9
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# Sổ câu hỏi mở E9

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-05; E9-Q15; XC-08; E9-Q11, E8-Q05 |


Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Tất cả **CHỜ TRẢ LỜI**. Cột trả lời và nguồn/người/ngày để trống; phương án chỉ tham khảo, chưa chọn. Không gửi hỏi lại E6/E7/E8; các tham chiếu dưới là dependency, không thay sổ gốc.

| Mã | Câu hỏi | Phương án tham khảo | Nhánh BLOCKED | Nguồn liên quan | Trả lời | Nguồn / người / ngày |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| E9-Q01 | O-04: nhà cung cấp mô hình, hạ tầng, vùng/nơi xử lý dữ liệu và đường chuyển dữ liệu nào được duyệt? | So sánh phương án tự quản lý hoặc dịch vụ sau đánh giá dữ liệu; chưa chọn provider/model | Toàn bộ gọi AI thật, cấu hình chi phí, release R9 | O-04; AIO-Q01 |  |  |
| E9-Q02 | Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền? | Chỉ tài khoản hoặc thêm guest có xác minh; không lấy IP làm danh tính mặc định | Mở phiên thật, quota theo người, audit guest | CG01/08 E6; E8-Q06 |  |  |
| E9-Q03 | Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào? | Danh mục sở thích/nguyên liệu đã duyệt; nội dung ngoài danh mục dừng làm rõ; không suy luận bệnh | Nhận input thật, mapping kiêng kỵ; phạm vi sức khỏe vẫn đóng | O-03; AIO-Q05; E8-Q05 |  |  |
| E9-Q04 | Có hiển thị giá suất cho khách không, nguồn/hiệu lực/nhãn giá nào được duyệt? | Projection giá public riêng hoặc không hiển thị cho đến khi có nguồn; không dùng price_cap làm giá bán | Hiển thị giá suất; không cam kết giá | E8-Q03; O-02 |  |  |
| E9-Q05 | Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không? | Thông báo chung không phân biệt nguyên nhân kinh tế hoặc chuyển người thật; chưa chọn; không truyền cost result cho model | Nhánh vượt ngưỡng/CANH_BAO và kết quả công khai | AIO-Q02; không sửa cổng MENU |  |  |
| E9-Q06 | FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào? | Kho tiếp nhận riêng hoặc đầu nhận hiện hữu được duyệt; chỉ ACK khi ghi bền vững; tách receipt và duyệt | Ghi nháp thật, chuyển giao, hiển thị kết quả xử lý; không mở E10 | E8-Q06/07; CRM E10 dependency |  |  |
| E9-Q07 | FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần? | Đếm lượt được nhận hoặc lượt hoàn tất theo policy được duyệt; reserve theo upper bound + đối soát; không có số mặc định | Nhận lượt thật, quyết toán/hoàn lượt, trần/reset và retry | O-04; AIO-Q01 |  |  |
| E9-Q08 | Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy? | PER-08 là persona quản trị nhưng quyền cụ thể phải cấp; nếu cần duyệt áp tách người tạo/sửa cuối | Kích hoạt cấu hình; không tự trao quyền vì là Giám đốc | E1 tham số/BR-SEC-008; O-06 |  |  |
| E9-Q09 | Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì? | Duyệt manifest, dữ liệu khả thi và rubric độc lập trước chạy; từ chối/timeout không thay thực đơn đạt | Nghiệm thu R9; nội dung lời nhắc chưa xác nhận | R9; AIO-Q03 chỉ là tham khảo E5 |  |  |
| E9-Q10 | Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider? | Tối thiểu hóa; tách audit metadata khỏi nội dung; chốt quy trình xóa theo NFR-PRIV-001, không dùng retention log thay retention chat | Lưu hội thoại thật, replay, xuất log, truyền dữ liệu provider | E1 N-03; O-04; E8-Q06; AIO-Q04 |  |  |
| E9-Q11 | FEAT-057 E8 và FEAT-060 E9 dùng chung bộ dựng hay tách; contract kiểm nguồn/quy tắc và quyền public thế nào? | Có thể dùng chung port kiểm thuần, hoặc bộ dựng riêng; không dùng lại credential/quota AIO | Chốt adapter/bộ dựng và reuse; không sửa FEAT-057 | E8-Q05; AIO-Q06 |  |  |
| E9-Q12 | Nguồn nào đủ điều kiện public; stale/thu hồi/thiếu dinh dưỡng/dị ứng xử lý ra sao; tuần/ngày phục vụ và nhiều cỡ? | Projection có phiên bản nguồn, không coi thiếu là 0 hoặc không dị ứng; refresh phải kiểm lại | Kết quả thật, nhãn đầy đủ, mapping ngày/cỡ | E2-Q3; O-02; NUTR-Q01–04; E8-Q04 |  |  |
| E9-Q13 | Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9? | Key bền vững gắn chủ thể/route/body; giữ reservation khi usage chưa rõ; profile theo nền chưa chọn số quota | Freeze API/delta, fault tolerance và thử tải | AIO-Q06; E8-Q12; O-04 |  |  |
| E9-Q14 | Mở FEAT-063 cần phê duyệt nào sau O-03/FEAT-046/047; PER-04 không tài khoản có được dùng không? | Giữ gate đóng; sau quyết định mới review phạm vi persona, consent/quyền và contract FEAT-047; không xây nhánh gợi ý trước | Toàn bộ gợi ý cá nhân/đọc hồ sơ/thu hoặc suy luận sức khỏe | O-03; FR-NUTR-PROF-001/REC-001 |  |  |
| E9-Q15 | Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại? | Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. | BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. XC-05; DEC-201. Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. | XC-05; DEC-201 |  |  |

> Chờ E9-Q11, E8-Q05 — XC-08. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-08](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Chỉ cập nhật khi có phản hồi có nguồn/phạm vi; không đóng câu hỏi vì kiểm tài liệu đạt. E6 CG01/08/05/06, E7 Q-13/E7-Q01–08, E8-Q01–12 giữ CHỜ TRẢ LỜI.
