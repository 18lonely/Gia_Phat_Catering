---
id: DOC-E11-REVIEW-QUESTIONS-MD
title: Câu hỏi mở E11
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Câu hỏi mở E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-02; E11-Q08; XC-07; E11-Q02, O-06 |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

Trạng thái tất cả: CHỜ TRẢ LỜI. Cột Trả lời để trống. Khuyến nghị là phương án để review, không mặc định nghiệp vụ. Không hỏi lại hay tự trả lời các câu nguồn.

| Mã | Câu hỏi | Phương án khuyến nghị | Tác động / phần BLOCKED | Trả lời |
| :--- | :--- | :--- | :--- | :--- |
| E11-Q01 | Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng? | Tách nhu cầu gộp khỏi lượng đề nghị mua; chưa tự trừ tồn hoặc đặt mức tối thiểu. | FEAT-074; không tính lượng mua ròng khi thiếu chính sách. |  |
| E11-Q02 | Ai lập, duyệt, phát hành đơn mua; xử lý sửa/hủy và người thay thế thế nào? | Dùng tách tạo/duyệt của E1; chưa gán vai trò duyệt hoặc hạn mức. | Đơn mua chỉ nháp; phát hành và sửa đơn đã duyệt BLOCKED; O-06 giữ mở. |  |
| E11-Q03 | Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào? | Chỉ quản lý lô FROZEN/DRY; chưa chọn FIFO/FEFO hay bắt buộc hạn dùng. | Ghi lô chi tiết, phân bổ và xuất kho BLOCKED. |  |
| E11-Q04 | Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao? | Giữ lượng đặt, lượng thực nhận, lượng chấp nhận riêng; cần quyết định trước ghi nhận chính thức. | Công nợ và đối chiếu thực mua còn thiếu căn cứ. |  |
| E11-Q05 | Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không? | Dùng tệp nội bộ E1 và ảnh gắn đúng phiếu; không OCR, không tự chọn thời hạn lưu. | Chứng từ thực và điều kiện hoàn tất phiếu BLOCKED. |  |
| E11-Q06 | Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào? | Tách phiếu nhận, nghĩa vụ phải trả và chứng từ thanh toán; chưa suy đã trả từ đã nhận. | Không tự tạo lịch trả nợ hoặc bù trừ; số dư/kỳ chính thức BLOCKED. |  |
| E11-Q07 | Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung? | Giữ nguồn mua và phân bổ riêng, chưa chọn phương pháp phân bổ. | FEAT-076 không có tỷ lệ chính thức cho dòng chưa phân bổ. |  |
| E11-Q08 | BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào? | Đề nghị so hai tỷ lệ cùng phạm vi và cùng mẫu số đã duyệt; không thay mục tiêu ≤ 3 điểm phần trăm. | R11 BLOCKED tới khi có công thức đo và dữ liệu thật; không dùng chênh tương đối 3 %. |  |
| E11-Q09 | Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào? | Lưu phân công nháp theo cơ sở/ca; chưa đặt số người hoặc giờ ca. | Kiểm đủ nhân lực và phân ca chính thức BLOCKED. |  |
| E11-Q10 | Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi? | Tách kết quả QC khỏi phiếu giao E7; mục không đạt/thiếu không tự coi đạt. | Cổng sẵn sàng giao và bàn giao E7 BLOCKED. |  |
| E11-Q11 | Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì? | Có mã mẫu gắn bữa/cơ sở, người ghi và thời điểm; không tự đặt hạn hoặc định lượng mẫu. | R11 cần 100% bữa có mẫu lưu, nhưng xác nhận mẫu hợp lệ còn BLOCKED. |  |
| E11-Q12 | Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào? | Chỉ tạo ứng viên nháp; nguồn đổi phải kiểm lại, không sửa trực tiếp order/plan. | Áp dụng thay đổi xuống E6/E7 BLOCKED; không quyết CG05/06/07. |  |
| E11-Q13 | Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt? | Đề nghị version kiểm khi ghi, audit và chống lặp; không chọn TTL, retry hoặc SLA mới. | Kiểm tích hợp/độ bền và profile tải BLOCKED; E1-Q01–05 giữ mở. |  |
| E11-Q14 | Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào? | Đối chiếu PriceInput; không ghi đè giá hiệu lực hoặc tự đặt giá tham chiếu. | Port giá chỉ ranh giới; CK/DATA-COST và rounding chưa chốt. |  |
| E11-Q15 | Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân? | Dùng nhãn chất gây dị ứng của món và ràng buộc thực đơn đã được phép; thiếu căn cứ thì chặn. | Không tạo form sức khỏe; kiểm thay món thực BLOCKED khi thiếu dữ liệu/rule đã duyệt. |  |

> Chờ E11-Q02, O-06 — XC-07. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-07](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

> Chờ E11-Q08 — XC-02. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-02](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

