---
id: DOC-E11-TEST-CHECKLIST-MD
title: Checklist kiểm thử E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Checklist kiểm thử E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

Khung review chưa được QA/stakeholder phê duyệt; việc viết ca dưới đây không tự coi bước review đã xong.

| FR / BR | Thành công | Lỗi | Biên | Gate |
| :--- | :--- | :--- | :--- | :--- |
| FR-PUR-DEM-001 / BR-PUR-001 | Nhu cầu gộp 7000 g = 7 kg; lượng mua ròng chưa xác định | Thiếu hệ số g/kg | Kế hoạch đổi revision khi đang xem | E6 CG06, ORD-Q10/14; E11-Q01 |
| FR-PUR-POD-001 / BR-PUR-002 | Nháp có tiền hàng 216000 đ khi căn cứ giá đủ; chưa phát hành | Số lượng âm hoặc thiếu NCC | Giá UNKNOWN hoặc chưa rõ VAT phải trả | E11-Q01/02/13/14 |
| FR-PUR-POG-001 / BR-PUR-003 | Trả BLOCKED kèm E11-Q02; đơn giữ DRAFT | Client tự gắn APPROVED | Tải lại cổng nhiều lần | E11-Q02; O-06 |
| FR-PUR-LOT-001 / BR-PUR-004 | Hiển thị thuộc phạm vi lô; chi tiết lô còn chờ | Hàng tươi được gửi yêu cầu quản lý lô | Thiếu loại bảo quản | E11-Q03 |
| FR-PUR-RCV-001 / BR-PUR-005 | Hiện riêng 10/8/7 kg; 1 kg chưa chấp nhận, 2 kg chưa nhận; chưa tự trả hàng | Chấp nhận 9 kg khi chỉ nhận 8 kg | Hai lần nhận cùng đơn | E11-Q04/13 |
| FR-PUR-DOC-001 / BR-PUR-006 | Gắn được tham chiếu ảnh; không chuyển phiếu sang đã nhận chính thức | File của cơ sở ngoài scope | Liên kết ảnh hết hạn 15 phút theo E1 | E11-Q05/13; E1-Q01 |
| FR-PUR-APV-001 / BR-PUR-007 | Dư 116000 đ theo fixture đã đủ căn cứ; không giảm bởi CK khách | Thiếu số dư đầu kỳ | Đơn có CK khách 5 % | E11-Q06/04 |
| FR-COST-BUY-001 / BR-PUR-008 | Chênh hiển thị 3 điểm phần trăm; không gọi tăng tương đối 6 % là tiêu chí R11 | Thực mua của cơ sở khác hoặc ngày chưa phân bổ | Mẫu số bằng 0 hoặc chưa biết | E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04 |
| FR-COST-BEX-001 / BR-PUR-009 | Hiện lượng và giá hai phía, liên kết chứng từ; không ghi đè dự toán | Người không có cost.cost.read yêu cầu tiền | Giá E3 mới có hiệu lực sau bản dự toán | E11-Q07/08/14 |
| FR-PLAN-SHF-001 / BR-PUR-010 | Giữ bản nháp; trạng thái bắt đầu sản xuất E6 không đổi | Nhân sự ngoài cơ sở được phép | Plan revision thay đổi | E11-Q09; E6 CG06 |
| FR-PLAN-QCG-001 / BR-PUR-011 | Hiện chưa đủ căn cứ giao; không tự chuyển E7 sang giao thành công | Client bỏ mục không đạt khỏi yêu cầu | Tất cả mục mẫu được đánh đạt nhưng policy chưa duyệt | E11-Q10; E7-Q02; E6 CG06 |
| FR-PLAN-SMP-001 / BR-PUR-012 | Độ phủ bản ghi 90 %, liệt kê 1 bữa thiếu; chưa đạt mục tiêu 100 % R11 | Thiếu mã bữa hoặc cơ sở | Hai mẫu cùng bữa và 1 bữa khác chưa có mẫu | E11-Q11; E6 CG06 |
| FR-MENU-SUB-001 / BR-PUR-013 | Tạo ứng viên DRAFT; thực đơn công bố không đổi | Đổi món MAIN sang SOUP | Món có tên giống nhưng vai trò khác | E11-Q12/15; O-02 |
| FR-MENU-SCK-001 / BR-PUR-014 | Có đủ ba kết quả đúng candidateVersion; vẫn chưa được công bố | Thiếu giá hoặc thiếu căn cứ dị ứng | Người dùng đổi ứng viên sau lần kiểm | DL-01; E11-Q15; O-01/O-02; CK/DATA-COST |
| FR-MENU-SGT-001 / BR-PUR-015 | Hiện cần qua cổng MENU; không tự công bố hoặc sửa kế hoạch | Quy tắc cứng vi phạm hoặc thiếu cost | Nguồn thay đổi giữa kiểm và chuyển | E11-Q12/13; DL-01; E6 CG05/06/07 |

Kiểm chung: quyền cơ sở; redaction giá/ảnh; version; retry; audit; NFR-COST-002; R11; cổng MENU; không thu sức khỏe. Ca hệ thống có overlap, không cộng thành mục tiêu nghiệm thu độc lập.
