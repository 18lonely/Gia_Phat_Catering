---
id: DOC-E11-USECASES-UC-PUR-002-MD
title: "UC-PUR-002: Lập đơn mua nháp"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-002: Lập đơn mua nháp

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Kế toán (PER-07).
- Bên quan tâm: người thao tác cần đơn draft, nguồn nhu cầu và giá được giữ; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Lập đơn mua nháp” trên UI-PUR-02.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q01/02/13/14. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Đơn DRAFT, nguồn nhu cầu và giá được giữ. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-02, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: demandRef, supplierId, lines, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Người lập chọn NCC từ danh mục E3, không có tự chọn; nhập lượng/đơn vị và PriceInput có nguồn; tổng tiền chỉ khi giá đã xác định.
5. Hệ thống trả: Đơn DRAFT, nguồn nhu cầu và giá được giữ.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Số lượng âm hoặc thiếu NCC: Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập (ERR-PUR-422-12).
- Bước 4: Giá UNKNOWN hoặc chưa rõ VAT phải trả: Giữ chưa xác định, không coi giá hoặc VAT bằng 0.
- Bước 4: thiếu policy/nguồn tại E11-Q01/02/13/14: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-POD-001 / FEAT-074 / BR-PUR-002 / US-PUR-002 / AC-PUR-002-1, AC-PUR-002-2, AC-PUR-002-3 / API-PUR-002. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
