---
id: DOC-NEN-TANG-GAP-ANALYSIS
title: "Rà khoảng trống: nen-tang"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Rà khoảng trống: nen-tang

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Kết quả rà tài liệu, không phải nghiệm thu. DESIGN_ADDED chỉ nghĩa có thiết kế bổ sung.

| Mã | Khoảng trống | Xử lý / còn thiếu | Trạng thái |
| :--- | :--- | :--- | :--- |
| E1-G01 | Thiếu bộ UC/API/story/test riêng | Đã bổ sung26 UC/story,25 HTTP endpoint và port; kiểm cấu trúc chưa phải bảo mật thực thi | DESIGN_ADDED |
| E1-G02 | Envelope/pagination khác các extension | E1-Q01 ghi rõ chưa thống nhất; cần quyết định Tech lead | OPEN |
| E1-G03 | MFA/ủy quyền/kênh ngoài | P1 giữ gated N-04/O-06/Q-14; không triển khai nửa quy trình | BLOCKED |
| E1-G04 | Event dedupe/version thông báo và job store | Cần delta schema/migration, chưa coi mock là dữ liệu bền vững | OPEN |
| E1-G05 | NFR và retention | Có ca kiểm, chưa môi trường/tải/diễn tập; N-03 giữ mở | BLOCKED |

Hủy trước ghi, lỗi mạng, lỗi phụ thuộc, XSS và scope được nêu ở flow/test/wireframe; vẫn cần kiểm trên backend/UI thật. Chủ sở hữu và hạn xử lý cụ thể chưa phân công; câu hỏi không được đóng chỉ vì đã ghi phương án.
