---
id: DOC-E11-USECASES-UC-PUR-004-MD
title: UC-PUR-004 — Kiểm phạm vi quản lý lô
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-004 — Kiểm phạm vi quản lý lô

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Quản lý cơ sở (PER-06).
- Bên quan tâm: người thao tác cần kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Kiểm phạm vi quản lý lô” trên UI-PUR-03.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q03. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật. Không thay trạng thái nghiệp vụ, không ghi dữ liệu qua GET.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-03, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: ingredientId, storageType, receiptRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đọc phân loại E2; chỉ FROZEN hoặc DRY thuộc phạm vi lô; quy tắc mã/hạn/xuất còn chờ.
5. Hệ thống trả: Kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2 — thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3 — Hàng tươi được gửi yêu cầu quản lý lô: Không tạo lô cho hàng tươi (ERR-PUR-422-14).
- Bước 4 — Thiếu loại bảo quản: Không suy là hàng khô; hiển thị chưa xác định.
- Bước 4 — thiếu policy/nguồn tại E11-Q03: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5 — kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-LOT-001 / FEAT-074 / BR-PUR-004 / US-PUR-004 / AC-PUR-004-1, AC-PUR-004-2, AC-PUR-004-3 / API-PUR-004. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
