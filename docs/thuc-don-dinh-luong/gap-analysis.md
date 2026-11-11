---
id: DOC-THUC-DON-DINH-LUONG-GAP-ANALYSIS
title: Rà khoảng trống — thuc-don-dinh-luong
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Rà khoảng trống — thuc-don-dinh-luong

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Kết quả rà tài liệu, không phải nghiệm thu. DESIGN_ADDED chỉ nghĩa có thiết kế bổ sung.

| Mã | Khoảng trống | Xử lý / còn thiếu | Trạng thái |
| :--- | :--- | :--- | :--- |
| E2-G01 | Thiếu API riêng | Catalog và typed request/response đã bổ sung;3 câu MENU-API-Q chờ review | DESIGN_ADDED |
| E2-G02 | Test từng quy tắc chưa có | 86 ca giả định đạt/vi phạm; toàn bộ chờ DL-01, không thay khoảng140 ca dự kiến bằng số đã PASS | BLOCKED |
| E2-G03 | Vòng đời giá và import | MENU-API-Q02/Q03; chưa migration validation store | OPEN |
| E2-G04 | Nhiều cỡ định lượng | O-02; FR-MENU-RCP-007 không tự đưa vào scope | BLOCKED |
| E2-G05 | Backend/UAT chưa có | Các kiểm HTML/cú pháp không phải kiểm thuật toán engine | BLOCKED |

Hủy trước ghi, lỗi mạng, lỗi phụ thuộc, XSS và scope được nêu ở flow/test/wireframe; vẫn cần kiểm trên backend/UI thật. Chủ sở hữu và hạn xử lý cụ thể chưa phân công; câu hỏi không được đóng chỉ vì đã ghi phương án.
