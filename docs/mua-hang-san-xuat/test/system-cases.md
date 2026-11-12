---
id: DOC-E11-TEST-SYSTEM-CASES-MD
title: Ca hệ thống E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ca hệ thống E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

10 ca có overlap với chức năng; không cộng vào tỷ lệ nghiệm thu.

| TC | NFR / BR | Setup và bước | Expected | Status | Gate | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-PUR-SYS-001 | NFR-PUR-001 | Gọi từng route với quyền cơ sở A nhưng đối tượng B; thử đọc ảnh và tiền | 404 ngoài scope; 403 thiếu quyền; 0 nội dung giá/ảnh bị lộ | NOT RUN |  |  |  |
| TC-PUR-SYS-002 | NFR-PUR-002 | Gửi lệnh nháp hai lần cùng khóa; mô phỏng mất phản hồi sau ghi | Một kết quả nghiệp vụ và audit; không nhân đôi công nợ/phiếu | BLOCKED | E11-Q13; E1-Q01 |  |  |
| TC-PUR-SYS-003 | NFR-PUR-002 | Hai người ghi cùng version; kiểm bản trước/sau | Một lệnh bị từ chối ERR-PUR-409-11; không lost update | BLOCKED | E11-Q13 |  |  |
| TC-PUR-SYS-004 | NFR-PUR-003 | Chuẩn bị profile E11; đo tải 1000 người theo nền | p95 đọc ≤ 300 ms, ghi ≤ 800 ms; không lấy TPS mẫu | BLOCKED | E11-Q13 |  |  |
| TC-PUR-SYS-005 | NFR-PUR-004 | Mở 9 màn tại 1440/390/360 px, dùng bàn phím và trạng thái lỗi | Không tràn ngang; có nhãn và focus; sản phẩm thật chưa chạy | NOT RUN |  |  |  |
| TC-PUR-SYS-006 | NFR-PUR-005 / NFR-COST-002 | Dùng 10 món và 10 ngày kế toán, so kết quả chuẩn đã xác nhận | Lệch cost món ≤ 1 đ; cost % ngày ≤ 0,01 điểm phần trăm | BLOCKED | DATA-COST-Q01–06 |  |  |
| TC-PUR-SYS-007 | BR-PUR-002 / BR-PUR-007 | Thử giá 100000 đ chưa VAT 8 % synthetic và 108000 đ đã gồm VAT; đổi invoiceRequested; thêm CK khách | Giá cost đều 108000 đ; không cộng VAT hai lần; không giảm phải trả NCC/khách vì CK riêng | NOT RUN |  |  |  |
| TC-PUR-SYS-008 | BR-PUR-014 / BR-PUR-015 | Sửa candidate sau kiểm; nguồn E2/E3 không sẵn sàng hoặc vi phạm rule cứng | ERR-PUR-503-11 khi nguồn lỗi; không đạt giả; luôn kiểm lại dị ứng/rule/cost và qua MENU | BLOCKED | DL-01; E11-Q12/15 |  |  |
| TC-PUR-SYS-009 | BR-PUR-001 / BR-PUR-010 | Nguồn E6 chưa có quyết định phát hành; mở màn nhu cầu/ca | Chỉ BLOCKED; GET không build/publish/ack/start hoặc sửa plan | NOT RUN |  |  |  |
| TC-PUR-SYS-010 | BR-PUR-011 / BR-PUR-012 | QC/mẫu thiếu policy; gọi cổng bàn giao hoặc cố gửi hồ sơ sức khỏe | ERR-PUR-422-99 cho policy thiếu; không tạo giao nhận/doanh thu; không nhận sức khỏe | NOT RUN |  |  |  |

