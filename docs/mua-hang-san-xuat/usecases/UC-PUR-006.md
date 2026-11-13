---
id: DOC-E11-USECASES-UC-PUR-006-MD
title: "UC-PUR-006: Gắn ảnh chứng từ vào phiếu"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-006: Gắn ảnh chứng từ vào phiếu

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Quản lý cơ sở (PER-06).
- Bên quan tâm: người thao tác cần liên kết ảnh nội bộ; trạng thái chứng từ riêng; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Gắn ảnh chứng từ vào phiếu” trên UI-PUR-04.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q05/13; E1-Q01. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Liên kết ảnh nội bộ; trạng thái chứng từ riêng. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-04, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: receiptRef, fileRef, version.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Kiểm quyền tệp E1 và cùng phạm vi phiếu; giữ nguồn ảnh và người gắn; mở ảnh không phải xác nhận giá hoặc nhận hàng.
5. Hệ thống trả: Liên kết ảnh nội bộ; trạng thái chứng từ riêng.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: File của cơ sở ngoài scope: Không lộ nội dung/URL tệp, không gắn chéo (ERR-PUR-422-16).
- Bước 4: Liên kết ảnh hết hạn 15 phút theo E1: Kiểm quyền để cấp lại liên kết; không công khai ảnh lâu dài.
- Bước 4: thiếu policy/nguồn tại E11-Q05/13; E1-Q01: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-DOC-001 / FEAT-075 / BR-PUR-006 / US-PUR-006 / AC-PUR-006-1, AC-PUR-006-2, AC-PUR-006-3 / API-PUR-006. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
