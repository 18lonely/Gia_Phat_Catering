---
id: DOC-E11-USECASES-UC-PUR-011-MD
title: UC-PUR-011 — Ghi kiểm tra trước giao
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-011 — Ghi kiểm tra trước giao

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Bếp trưởng (PER-06).
- Bên quan tâm: người thao tác cần phiếu qc nháp và cổng chưa sẵn sàng; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Ghi kiểm tra trước giao” trên UI-PUR-08.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q10; E7-Q02; E6 CG06. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Phiếu QC nháp và cổng chưa sẵn sàng. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-08, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: shiftRef, checklistRef, results, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi kết quả theo mục đã được duyệt; thiếu checklist hoặc còn mục chưa kiểm thì chưa đủ căn cứ giao. QC không ghi số khách nhận hoặc doanh thu.
5. Hệ thống trả: Phiếu QC nháp và cổng chưa sẵn sàng.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2 — thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3 — Client bỏ mục không đạt khỏi yêu cầu: Không kết luận đủ dựa trên tập mục thiếu (ERR-PUR-422-21).
- Bước 4 — Tất cả mục mẫu được đánh đạt nhưng policy chưa duyệt: Vẫn BLOCKED E11-Q10; không phát sinh phiếu giao.
- Bước 4 — thiếu policy/nguồn tại E11-Q10; E7-Q02; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5 — kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PLAN-QCG-001 / FEAT-077 / BR-PUR-011 / US-PUR-011 / AC-PUR-011-1, AC-PUR-011-2, AC-PUR-011-3 / API-PUR-011. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
