---
id: DOC-E11-TEST-R11-ACCEPTANCE-MD
title: Khung nghiệm thu R11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Khung nghiệm thu R11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

Nguồn [roadmap](../../gia-phat/02-roadmap.md) và BO-02 [PRD](../../gia-phat/01-prd.md). G-Next: ≥ 90 % order qua cổng; ≥ 70 % suất có lựa chọn trước hạn; truy cập tự nhiên sau 60 ngày ≥ 90 % mức trước chuyển đổi. Không tuyên bố cổng đạt trong phiên tài liệu. R11 còn cần R3/R6 xong.

| Mã | Tiêu chí nguyên gốc | Cách thu bằng chứng / điều kiện | Status | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| R11-AC-01 | Chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm theo ngày và cơ sở | Kế toán xác nhận tập ngày/cơ sở, phân bổ thực mua, mẫu số, dấu và công thức Q07/08; giữ snapshot dự toán và chứng từ thực mua; đo từng scope, không gộp để che ngày vượt | BLOCKED |  |  |
| R11-AC-02 | 100% bữa có mẫu lưu trên hệ thống | Có tập bữa kỳ vọng đã xác nhận từ E6, đếm bữa phân biệt có mẫu hợp lệ / tổng bữa; danh sách thiếu; Q11 quy định hợp lệ và thời hạn. Tập rỗng không tự là 100 % | BLOCKED |  |  |
| R11-AC-03 | Điều kiện bắt đầu R3/R6 và G-Next | Thu bằng chứng đã được chủ nguồn xác nhận; không lấy số file BA làm bằng chứng | BLOCKED |  |  |

NFR-COST-002 kiểm độ chính xác tính toán, không thay mục tiêu vận hành BO-02. Ví dụ 50 % so 53 % là 3 điểm phần trăm chỉ minh họa đơn vị; chưa tự chọn dấu, mẫu số hoặc kỳ đo. Không có ca sản phẩm PASS.
