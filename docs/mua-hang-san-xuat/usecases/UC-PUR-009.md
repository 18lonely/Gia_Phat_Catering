---
id: DOC-E11-USECASES-UC-PUR-009-MD
title: "UC-PUR-009: Giải thích nguồn chênh lệch"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-009: Giải thích nguồn chênh lệch

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Giám đốc/Kế toán (PER-08/07).
- Bên quan tâm: người thao tác cần chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Giải thích nguồn chênh lệch” trên UI-PUR-06.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q07/08/14. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn. Không thay trạng thái nghiệp vụ, không ghi dữ liệu qua GET.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-06, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: comparisonRef, ingredientId.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Truy về dòng dự toán, dòng nhận/mua và giá gồm VAT; hiển thị lượng/giá/đơn vị và nguồn. Không tự phân rã tác động giá/lượng nếu chưa chốt phương pháp.
5. Hệ thống trả: Chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Người không có cost.cost.read yêu cầu tiền: Không trả tiền hoặc cost trong body/lỗi/log hiển thị (ERR-PUR-403-11).
- Bước 4: Giá E3 mới có hiệu lực sau bản dự toán: Giữ giá snapshot dự toán; giá mới không sửa lịch sử.
- Bước 4: thiếu policy/nguồn tại E11-Q07/08/14: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-COST-BEX-001 / FEAT-076 / BR-PUR-009 / US-PUR-009 / AC-PUR-009-1, AC-PUR-009-2, AC-PUR-009-3 / API-PUR-009. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
