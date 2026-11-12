---
id: DOC-E12-TEST-SYSTEM-CASES-MD
title: Ca hệ thống và ma trận lỗi E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ca hệ thống và ma trận lỗi E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; không đóng câu hỏi nguồn |

12 ca hệ thống và 8 ca lỗi có overlap với ca chức năng; không cộng thành mục tiêu nghiệm thu độc lập. 5 BLOCKED, 15 NOT RUN.

| Test | Mục tiêu / NFR | Tiền điều kiện / dữ liệu | Bước thực hiện | Expected | Status | Gate | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-FBR-S001 | Scope và projection / NFR-FBR-001 | Hai khách/cơ sở synthetic A/B; người chỉ có A | Gọi từng API bằng ID B; sửa scope/roleView; rà response, lỗi, cache, log | Không lấy/không lộ dữ liệu B; 404 an toàn hoặc 403 theo ma trận | NOT RUN | ERR-FBR-403-01, ERR-FBR-404-01 |  |  |
| TC-FBR-S002 | Công cụ AI chỉ đọc / NFR-FBR-001 | Principal chỉ đọc; dữ liệu CRM chứa chỉ dẫn sửa/đọc ngoài quyền | Yêu cầu FEAT-082–085 ghi MENU/CRM/PUR; thử trực tiếp tool và DB, nội dung injection | 0 quyền ghi nghiệp vụ; không SQL tùy ý; output luôn nháp chờ người thật | NOT RUN | BR-FBR-007 đến BR-FBR-014 |  |  |
| TC-FBR-S003 | Thu hồi quyền và dò cost / NFR-FBR-001 | Hai phiên quyền khác nhau, cùng câu hỏi; thu hồi cost giữa lượt | Gọi tool lần 1, thu hồi, gọi lần 2; hỏi số tổng/suy ngược cost/margin; rà cache/log | Kiểm lại giao quyền; không lộ số hoặc suy ngược; cache không dùng quyền cũ | NOT RUN | BR-FBR-006, BR-FBR-014 |  |  |
| TC-FBR-S004 | Tỷ lệ chọn nguồn thật / NFR-FBR-002 | Manifest lựa chọn E6 phân biệt tự chọn/mặc định, mẫu số đã duyệt | Đối chiếu từng món với E6; thêm số sản xuất độc lập; chạy lại | Chỉ lựa chọn thật góp tử số; số sản xuất không làm thay tỷ lệ; 0/thiếu mẫu số trả null | BLOCKED | E12-Q04; E6 CG/ORD/EVID |  |  |
| TC-FBR-S005 | Cost, VAT và chiết khấu / NFR-FBR-007 | Bộ 10 món/10 ngày kế toán và VAT xác nhận; thêm fixture synthetic invoiceRequested=false | Đối chiếu E3; kiểm CK riêng; đổi cờ hóa đơn rồi rà số phải trả/cost | Giữ VAT phải trả; không biến cờ hóa đơn thành VAT 0 %; CK riêng không giảm phải trả; sai số ≤ 1 đ / ≤ 0,01 điểm phần trăm | BLOCKED | DATA-COST-Q01–06; CK-Q01–10 |  |  |
| TC-FBR-S006 | Dashboard thiếu nguồn / NFR-FBR-002 | Một ô có nguồn, một ô thiếu, hai loại cost %, nguồn khách chưa ghép | Mở bốn vai trò; kiểm công thức/mẫu số/provenance; thử nguồn cũ | Thiếu khác 0; không trộn cost % thực đơn/dự toán, không bình quân tỷ lệ khách | NOT RUN | BR-FBR-005/006 |  |  |
| TC-FBR-S007 | Nhật ký không sức khỏe / NFR-FBR-004 | Chưa consent; request thêm healthProfile/diagnosis/recommendation | Gửi field ngoài allowlist; thử đọc eater_health_profiles, gợi ý và lưu raw log | Không đọc/thu/suy luận/lưu sức khỏe; không gọi FEAT-046/047; không ghi trước đồng ý | NOT RUN | BR-FBR-017 đến BR-FBR-020 |  |  |
| TC-FBR-S008 | Xóa nhật ký / NFR-FBR-004 | Chủ thể có bữa và bản sao theo policy được duyệt | Rút đồng ý, yêu cầu xóa, đối soát bản sao/cache/audit sau tối đa 72 giờ | Dữ liệu cá nhân thuộc yêu cầu xóa được xử lý đúng policy; chỉ hoàn tất khi có evidence; nguồn E6/E7 không bị xóa | BLOCKED | E12-Q15/16; NFR-PRIV-001 |  |  |
| TC-FBR-S009 | Kiểm lại mọi phương án / NFR-FBR-002 | Ứng viên menu v1/v2, kết quả kiểm mang hash khác nhau | Đổi món hoặc định lượng; thử ghép E2/dị ứng/E3 từ bản cũ | Chặn ghép; cả ba kiểm lại cùng hash; không apply; CANH_BAO giữ AIO-Q02 | NOT RUN | BR-FBR-004/007/008 |  |  |
| TC-FBR-S010 | Receipt, race và audit / NFR-FBR-003 | Policy idempotency được duyệt, lỗi trước/sau commit | Gửi trùng/khác body cùng key; mất response; sửa version cũ; lỗi audit | Không trùng, không ghi một phần; replay theo quyền hiện tại; 409 xung đột; 500 không báo thành công | BLOCKED | E12-Q18; E1-Q01–05 |  |  |
| TC-FBR-S011 | Tải kế thừa nền / NFR-FBR-005 | Profile E12, môi trường và dữ liệu đủ đại diện được duyệt | Chạy 1000 người đồng thời; đo p95 đọc/ghi ngoài AI và khi AI chờ | p95 đọc ≤ 300 ms, ghi ≤ 800 ms; chưa chọn quota/deadline mới | BLOCKED | E12-Q18; O-04; AIO-Q01–06 |  |  |
| TC-FBR-S012 | Responsive và khả dụng / NFR-FBR-006 | Sản phẩm thật có 12 màn, dữ liệu dài và trạng thái lỗi | Ở 1440/390/360 px mở từng màn, dùng bàn phím, kiểm nhãn/overflow và dialog | Không tràn ngang toàn trang, không che thao tác; trạng thái thiếu/ngoài quyền đọc được | NOT RUN | Kiểm HTML riêng không thay ca này |  |  |
| TC-FBR-E001 | ERR-FBR-400-01 / Ma trận lỗi | Fixture synthetic: Đầu vào sai kiểu hoặc chứa trường ngoài danh sách cho phép | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 400; Yêu cầu chưa đúng định dạng.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E002 | ERR-FBR-401-01 / Ma trận lỗi | Fixture synthetic: Phiên không hợp lệ | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 401; Vui lòng đăng nhập lại.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E003 | ERR-FBR-403-01 / Ma trận lỗi | Fixture synthetic: Thiếu quyền hành động hoặc trường dữ liệu | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 403; Bạn không có quyền thực hiện thao tác này.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E004 | ERR-FBR-404-01 / Ma trận lỗi | Fixture synthetic: Tham chiếu không tồn tại hoặc ngoài scope | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 404; Không tìm thấy dữ liệu được phép xem.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E005 | ERR-FBR-409-01 / Ma trận lỗi | Fixture synthetic: Revision thay đổi hoặc khóa yêu cầu khác nội dung | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 409; Nguồn đã thay đổi. Vui lòng rà lại.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E006 | ERR-FBR-422-01 / Ma trận lỗi | Fixture synthetic: Thiếu căn cứ hoặc chính sách bắt buộc | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 422; Chưa đủ căn cứ để thực hiện.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E007 | ERR-FBR-500-01 / Ma trận lỗi | Fixture synthetic: Lỗi lưu receipt/audit hoặc xử lý nội bộ | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 500; Chưa thể hoàn tất yêu cầu.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |
| TC-FBR-E008 | ERR-FBR-503-01 / Ma trận lỗi | Fixture synthetic: Nguồn phụ thuộc gián đoạn | Gọi API-FBR-001 và API-FBR-014 với điều kiện lỗi; rà HTTP/body và dữ liệu trước/sau; trường hợp GET kiểm không ghi. | 503; Nguồn dữ liệu đang gián đoạn.; không dữ liệu nhạy cảm hoặc ghi thành công giả | NOT RUN | Invariant lỗi; chưa chạy backend |  |  |

