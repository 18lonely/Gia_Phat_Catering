---
id: DOC-E11-USECASES-UC-PUR-012-MD
title: UC-PUR-012 — Ghi sổ mẫu lưu theo bữa
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-012 — Ghi sổ mẫu lưu theo bữa

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Quản lý cơ sở (PER-06).
- Bên quan tâm: người thao tác cần sổ mẫu nháp, danh sách bữa thiếu mẫu; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Ghi sổ mẫu lưu theo bữa” trên UI-PUR-08.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q11; E6 CG06. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Sổ mẫu nháp, danh sách bữa thiếu mẫu. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-08, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi mẫu và liên kết bữa; phân biệt đã có bản ghi với mẫu hợp lệ theo policy; không tự đặt hạn lưu hay hủy.
5. Hệ thống trả: Sổ mẫu nháp, danh sách bữa thiếu mẫu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2 — thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3 — Thiếu mã bữa hoặc cơ sở: Chặn bản ghi không truy được nguồn (ERR-PUR-422-22).
- Bước 4 — Hai mẫu cùng bữa và 1 bữa khác chưa có mẫu: Đếm bữa phân biệt, không lấy số mẫu chia số bữa để báo đủ.
- Bước 4 — thiếu policy/nguồn tại E11-Q11; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5 — kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PLAN-SMP-001 / FEAT-077 / BR-PUR-012 / US-PUR-012 / AC-PUR-012-1, AC-PUR-012-2, AC-PUR-012-3 / API-PUR-012. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
