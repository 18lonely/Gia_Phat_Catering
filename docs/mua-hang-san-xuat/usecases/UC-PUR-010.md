---
id: DOC-E11-USECASES-UC-PUR-010-MD
title: "UC-PUR-010: Lập phân ca nháp"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-010: Lập phân ca nháp

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Bếp trưởng (PER-06).
- Bên quan tâm: người thao tác cần phân ca draft và các điều kiện còn thiếu; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Lập phân ca nháp” trên UI-PUR-07.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q09; E6 CG06. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Phân ca DRAFT và các điều kiện còn thiếu. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-07, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: kitchenId, serviceDate, shiftRef, assignments, planRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi phân công dự kiến gắn đúng nguồn; không xác nhận đã bắt đầu sản xuất E6, không tự chốt đủ người hoặc giờ ca.
5. Hệ thống trả: Phân ca DRAFT và các điều kiện còn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Nhân sự ngoài cơ sở được phép: Từ chối gắn vào ca (ERR-PUR-422-20).
- Bước 4: Plan revision thay đổi: Đánh dấu cần rà soát phân công; không tự kế thừa xác nhận bản cũ.
- Bước 4: thiếu policy/nguồn tại E11-Q09; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PLAN-SHF-001 / FEAT-077 / BR-PUR-010 / US-PUR-010 / AC-PUR-010-1, AC-PUR-010-2, AC-PUR-010-3 / API-PUR-010. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
