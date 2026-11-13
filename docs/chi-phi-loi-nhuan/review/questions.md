---
id: DOC-E13-REVIEW-QUESTIONS-MD
title: Câu hỏi mở E13
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Câu hỏi mở E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-02; E13-Q08; XC-07; E13-Q10, O-06; XC-09; E13-Q09; XC-11; E13-Q12 |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

Tất cả CHỜ TRẢ LỜI. Cột Trả lời để trống. Phương án khuyến nghị chỉ để review, không là mặc định hoặc quyết định. Không yêu cầu trả lời trong phiên.

| Mã | Câu hỏi | Phương án khuyến nghị chưa duyệt | Tác động / phần BLOCKED | Trả lời |
| :--- | :--- | :--- | :--- | :--- |
| E13-Q01 | Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì? | Duyệt danh mục có phiên bản; mỗi khoản chỉ thuộc một nguồn và một nhóm trong cùng báo cáo. | Ghi nhận chính thức và tổng chi phí; FR-EXP-COST-001. |  |
| E13-Q02 | Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào? | Chốt cùng scope đối soát; không mặc định tháng hoặc người khóa. | Khóa kỳ và đồng bộ kỳ E7; FR-EXP-PER-001. |  |
| E13-Q03 | Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì? | Giữ tham chiếu phân ca E11 riêng với giờ thực tế có chứng cứ; không mặc định phần mềm chấm công. | Chấm công chính thức; E11-Q09; FR-EXP-TIME-001. |  |
| E13-Q04 | Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao? | Tham chiếu phiên bản nguồn được duyệt; không xây quy trình tính lương. | Chi phí nhân công; FR-EXP-LAB-001. |  |
| E13-Q05 | Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao? | Trình các lựa chọn theo suất/doanh thu/giờ công/diện tích/kết hợp cùng dữ liệu đối chiếu; không chọn sẵn. | Phân bổ và lợi nhuận khách BLOCKED; FR-EXP-METH-001, FR-EXP-APRV-001, FR-EXP-ALLOC-001. |  |
| E13-Q06 | Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào? | Tách pool cấp công ty, chưa phân bổ không giấu vào cơ sở hoặc khách; chỉ dùng sau quyết định. | Tổng cơ sở và tổng công ty; FR-EXP-RECON-001. |  |
| E13-Q07 | Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào? | Giữ customerRef gốc, kitchenRef và revision nguồn; tổng hợp sau đối chiếu từng cơ sở. | Tổng theo khách nhiều cơ sở; FR-EXP-PROF-001. |  |
| E13-Q08 | Kết quả kinh doanh cơ sở gồm khoản nào, nguồn chuẩn nào, ghi nhận điều chỉnh và CK ra sao? | Cần manifest thành phần và định nghĩa có phiên bản; không suy lợi nhuận bằng doanh thu trừ riêng cost nguyên liệu. | Kết quả chính thức, công thức lợi nhuận; O-01, CK-Q01–10, E10-Q15; FR-EXP-RECON-001. |  |
| E13-Q09 | Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào? | Đối chiếu số gốc decimal; phần dư hiện riêng, không tự dồn cho khách cuối; chặn nếu chưa có quy tắc. | Phân bổ thực và biên lợi nhuận; không mượn dung sai Cost. |  |
| E13-Q10 | Ai duyệt điều chỉnh sau khóa, ghi vào kỳ nào và bằng chứng nào bắt buộc? | Bút toán riêng gắn bản gốc, lý do và người duyệt khác người lập/sửa cuối; không mở khóa tại E13. | Ghi nhận điều chỉnh chính thức; O-06; FR-EXP-ADJ-001. |  |
| E13-Q11 | Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào? | Deny by default; chỉ cấp từng quyền cần dùng cho hai persona, không suy mọi kế toán đều thấy mọi cơ sở. | Cấp quyền thật/lưu trữ; FR-EXP-SAFE-001; E1-Q01–05. |  |
| E13-Q12 | Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào? | Nguồn không đầy đủ thì BLOCKED; chụp manifest và không ghi lại snapshot cũ; chưa đặt TTL, SLA, định dạng xuất. | Freeze API/tích hợp/tải; E7-Q08, E10-Q13, E11-Q13, E12-Q18. |  |
| E13-Q13 | Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào? | Đề xuất chỉ đọc tổng hợp có version và trạng thái; không thay cost % E12, không chốt E10-Q15. | Biên lợi nhuận và kết nối dashboard; E12-Q06/07/08. |  |
| E13-Q14 | Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu? | Lập bộ chứng từ cùng kỳ/cơ sở, số chuẩn độc lập; Giám đốc xác nhận phương pháp rồi đối chiếu. | R13 chưa nghiệm thu; không dùng kiểm mock thay dữ liệu thật. |  |

> Chờ E13-Q12 — XC-11. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-11](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

> Chờ E13-Q09 — XC-09. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-09](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

> Chờ E13-Q10, O-06 — XC-07. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-07](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

> Chờ E13-Q08 — XC-02. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-02](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Giữ nguyên các câu đang chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp phần producer phụ thuộc các câu này.
