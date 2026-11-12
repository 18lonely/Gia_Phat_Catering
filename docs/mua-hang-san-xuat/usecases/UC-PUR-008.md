---
id: DOC-E11-USECASES-UC-PUR-008-MD
title: UC-PUR-008 — Đối chiếu dự toán và thực mua
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-008 — Đối chiếu dự toán và thực mua

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Kế toán (PER-07).
- Bên quan tâm: người thao tác cần hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Đối chiếu dự toán và thực mua” trên UI-PUR-06.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-06, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Giữ tiền dự toán và thực mua riêng; chỉ so tỷ lệ khi cùng scope, đủ nguồn và có định nghĩa BO-02 được duyệt; thiếu thì không trả đạt.
5. Hệ thống trả: Hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2 — thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3 — Thực mua của cơ sở khác hoặc ngày chưa phân bổ: Không ghép với dự toán để kết luận đạt (ERR-PUR-422-18).
- Bước 4 — Mẫu số bằng 0 hoặc chưa biết: Tỷ lệ và chênh null; kết luận chưa xác định.
- Bước 4 — thiếu policy/nguồn tại E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5 — kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-COST-BUY-001 / FEAT-076 / BR-PUR-008 / US-PUR-008 / AC-PUR-008-1, AC-PUR-008-2, AC-PUR-008-3 / API-PUR-008. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
