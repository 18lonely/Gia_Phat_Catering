---
id: DOC-E11-USECASES-UC-PUR-005-MD
title: "UC-PUR-005: Ghi phiếu nhận hàng nháp"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-005: Ghi phiếu nhận hàng nháp

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Quản lý cơ sở (PER-06).
- Bên quan tâm: người thao tác cần phiếu draft có phiên bản và chênh lệch hiển thị; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Ghi phiếu nhận hàng nháp” trên UI-PUR-03.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q04/13. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Phiếu DRAFT có phiên bản và chênh lệch hiển thị. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-03, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Giữ lượng đặt, thực nhận và chấp nhận riêng theo dòng; ghi chứng cứ chênh; không tự hoàn tất đơn hay tăng công nợ chính thức.
5. Hệ thống trả: Phiếu DRAFT có phiên bản và chênh lệch hiển thị.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Chấp nhận 9 kg khi chỉ nhận 8 kg: Chặn dữ liệu mâu thuẫn, không ghi phiếu (ERR-PUR-422-15).
- Bước 4: Hai lần nhận cùng đơn: Giữ tham chiếu từng lần; chưa tự quyết hoàn tất khi policy chưa có.
- Bước 4: thiếu policy/nguồn tại E11-Q04/13: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-RCV-001 / FEAT-075 / BR-PUR-005 / US-PUR-005 / AC-PUR-005-1, AC-PUR-005-2, AC-PUR-005-3 / API-PUR-005. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
