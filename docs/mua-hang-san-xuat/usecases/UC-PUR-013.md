---
id: DOC-E11-USECASES-UC-PUR-013-MD
title: UC-PUR-013 — Lập ứng viên món thay thế
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-013 — Lập ứng viên món thay thế

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Dinh dưỡng viên (PER-05).
- Bên quan tâm: người thao tác cần ứng viên nháp có món cũ/mới và vai trò; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Lập ứng viên món thay thế” trên UI-PUR-09.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q12/15; O-02. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Ứng viên nháp có món cũ/mới và vai trò. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: menuRef, menuVersion, originalDishId, replacementDishId, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Người dùng chọn món cùng vai trò từ danh mục được phép; ghi thiếu hàng và nguồn; tạo ứng viên DRAFT, không thay thực đơn công bố.
5. Hệ thống trả: Ứng viên nháp có món cũ/mới và vai trò.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2 — thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3 — Đổi món MAIN sang SOUP: Chặn khác vai trò, không tạo thay thế hợp lệ (ERR-PUR-422-23).
- Bước 4 — Món có tên giống nhưng vai trò khác: So mã vai trò, không so chuỗi tên món.
- Bước 4 — thiếu policy/nguồn tại E11-Q12/15; O-02: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5 — kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-MENU-SUB-001 / FEAT-078 / BR-PUR-013 / US-PUR-013 / AC-PUR-013-1, AC-PUR-013-2, AC-PUR-013-3 / API-PUR-013. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
