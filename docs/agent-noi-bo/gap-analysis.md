---
id: DOC-AGENT-NOI-BO-GAP-ANALYSIS
title: Rà khoảng trống — agent-noi-bo
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Rà khoảng trống — agent-noi-bo

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Kết quả rà tài liệu, không phải nghiệm thu. DESIGN_ADDED chỉ nghĩa có thiết kế bổ sung.

| Mã | Khoảng trống | Xử lý / còn thiếu | Trạng thái |
| :--- | :--- | :--- | :--- |
| E5-G01 | Thiếu epic/sơ đồ/checklist/preview/HTML | Đã bổ sung; run chỉ mô phỏng, không gọi model | DESIGN_ADDED |
| E5-G02 | Chế độ CANH_BAO và đầu ra VALID | AIO-Q02 chưa chốt; không thay cổng MENU/COST | BLOCKED |
| E5-G03 | Model/quota/20 yêu cầu/baseline | AIO-Q01/Q03 vàO-04 chưa chốt; không tự đặt ngân sách | BLOCKED |
| E5-G04 | Giao dịch apply/outbox/lease | AIO-Q06 cần Tech lead review; schema note chưa bảo đảm triển khai | OPEN |
| E5-G05 | Ký tự đầu<=5giây khác polling | Ghi E1-Q01/AIO-Q01; đề xuất progress phản hồi nhưng chưa thay NFR | OPEN |

Hủy trước ghi, lỗi mạng, lỗi phụ thuộc, XSS và scope được nêu ở flow/test/wireframe; vẫn cần kiểm trên backend/UI thật. Chủ sở hữu và hạn xử lý cụ thể chưa phân công; câu hỏi không được đóng chỉ vì đã ghi phương án.
