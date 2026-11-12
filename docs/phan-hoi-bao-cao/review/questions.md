---
id: DOC-E12-REVIEW-QUESTIONS-MD
title: Câu hỏi mở E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Câu hỏi mở E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; không đóng câu hỏi nguồn |

Tất cả CHỜ TRẢ LỜI. Cột Trả lời để trống; khuyến nghị chỉ để review, không phải chính sách được chọn. Không hỏi lại người dùng trong phiên.

| Mã | Câu hỏi | Phương án khuyến nghị chưa duyệt | Tác động / phần BLOCKED | Trả lời |
| :--- | :--- | :--- | :--- | :--- |
| E12-Q01 | Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì? | Dùng thang có phiên bản và nguồn quyết định; chưa chọn số mức hoặc trung bình. | FR-FB-RATE-001; nhận điểm và thống kê đánh giá thật BLOCKED. |  |
| E12-Q02 | Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao? | Kế thừa identity E6 khi được chốt; giữ nguồn và receipt, không chọn quy tắc một người một điểm thay stakeholder. | FEAT-079; E6 CG01/08 và quyền xem danh tính còn chờ. |  |
| E12-Q03 | Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào? | Tách tiếp nhận khỏi giải quyết; chưa đặt SLA hoặc người xử lý. | FR-FB-CASE-001; xử lý/đóng thật BLOCKED; không tự điều chỉnh tiền E7. |  |
| E12-Q04 | Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào? | Giữ provenance lựa chọn thật và định nghĩa có phiên bản; hiển thị chưa xác định trước khi duyệt. Không chọn sẵn một mẫu số. | FR-FB-SELR-001; R12-CHOICE và xếp hạng tỷ lệ BLOCKED. |  |
| E12-Q05 | Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao? | Người thật review căn cứ; kiểm lại E2/dị ứng/E3, không đổi thực đơn trực tiếp. | FR-FB-PROP-001; xếp hạng/tự chuyển adapter chưa có căn cứ. |  |
| E12-Q06 | Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào? | Review catalog M-FBR-01…09 theo công việc từng vai trò; không coi danh sách đề xuất là mặc định. | FR-RPT-ROLE-001; R12-DASH cần manifest chỉ số được duyệt. |  |
| E12-Q07 | Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope? | Quyền trường riêng, deny by default, projection ở server/tool/DB; không tự cấp do tên vai trò. | FR-RPT-CPCT-001, FR-AIO-DQA-001; ma trận quyền thật BLOCKED; E10-Q15 vẫn mở. |  |
| E12-Q08 | Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào? | Giữ riêng cost % thực đơn và dự toán E3; không bình quân tỷ lệ hoặc suy từ số giao. Chờ định nghĩa tổng hợp có nguồn. | FEAT-081 theo khách BLOCKED; E11-Q07/08, O-01 và E7 không tự chốt. |  |
| E12-Q09 | Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì? | Allowlist đọc theo người hỏi; mọi thay món/định lượng kiểm lại ba nguồn cùng hash; không cấp apply. | Runtime/duyệt đề xuất thật BLOCKED; kế thừa AIO-Q01–06, không trả lời lại. |  |
| E12-Q10 | Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì? | So nguồn cùng căn cứ và để ngưỡng trống; không mượn BO-02/NFR-COST-002. | FR-AIO-PDEV-001; cảnh báo chính thức BLOCKED. |  |
| E12-Q11 | FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp? | Chỉ đọc projection E10 theo quyền; không tạo task/quote, gửi hoặc cam kết giá. | FR-AIO-CRMS-001/CRMQ-001; contract đọc/review chờ, không sửa E10. |  |
| E12-Q12 | FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm? | Catalog câu hỏi/chỉ số có nguồn, kiểm từng công cụ và output; thiếu định nghĩa thì không trả số. | FR-AIO-DQA-001; rubric số liệu và kiểm suy ngược cần review. |  |
| E12-Q13 | Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì? | Mục tiêu cấp nhóm, không theo bệnh lý/cá nhân; số cụ thể chờ NUTR-Q01–04. | FR-NUTR-GRPT-001/GRPC-001; không tự đặt kcal hoặc dung sai. |  |
| E12-Q14 | Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không? | Mục tiêu nháp có phiên bản; chưa thêm cổng MENU hoặc chọn ưu tiên bản mới. | FEAT-086 activation và áp kết quả chính thức BLOCKED. |  |
| E12-Q15 | Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào? | Đồng ý tự nguyện riêng cho bữa đã ăn; không chọn sẵn, không ảnh hưởng chọn món; không hồ sơ sức khỏe. | FEAT-087 nhận thật BLOCKED; không mở O-03. |  |
| E12-Q16 | Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào? | Kế thừa xóa ≤ 72 giờ của nền; tách receipt/hoàn tất; không đặt retention hoặc xóa giao dịch nguồn. | FR-NUTR-DDEL-001; vận hành xóa/retention BLOCKED. |  |
| E12-Q17 | Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào? | Cân nhắc xác nhận tự nguyện của người ăn có scope và snapshot; chưa chọn làm chính sách. Không suy từ order/giao/chọn món. | FR-NUTR-DREC-001; nhận bữa thật BLOCKED; phần xem/xóa và ranh giới vẫn thiết kế độc lập. |  |
| E12-Q18 | Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào? | Adapter theo nguồn, quyền hiện tại và provenance; không tự đặt TTL, retry, quota hoặc chọn hạ tầng. | Freeze API, tích hợp, race và kiểm tải BLOCKED; E1-Q01–05/AIO-Q giữ nguyên. |  |

