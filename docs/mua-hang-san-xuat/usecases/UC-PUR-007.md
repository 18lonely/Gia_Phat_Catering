---
id: DOC-E11-USECASES-UC-PUR-007-MD
title: "UC-PUR-007: Xem công nợ nhà cung cấp"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-007: Xem công nợ nhà cung cấp

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Kế toán (PER-07).
- Bên quan tâm: người thao tác cần bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Xem công nợ nhà cung cấp” trên UI-PUR-05.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q06/04. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu. Không thay trạng thái nghiệp vụ, không ghi dữ liệu qua GET.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-05, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: supplierId, kitchenId, fromDate, toDate.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đọc số dư và nguồn được xác nhận; thiếu đầu kỳ/ghi nhận/thanh toán thì trả chưa xác định, không biến phiếu nhận thành đã trả.
5. Hệ thống trả: Bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Thiếu số dư đầu kỳ: Không báo tổng công nợ hoàn chỉnh (ERR-PUR-422-17).
- Bước 4: Đơn có CK khách 5 %: Không trừ 5 % khỏi phải trả NCC; không tự giảm số khách phải trả.
- Bước 4: thiếu policy/nguồn tại E11-Q06/04: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-APV-001 / FEAT-075 / BR-PUR-007 / US-PUR-007 / AC-PUR-007-1, AC-PUR-007-2, AC-PUR-007-3 / API-PUR-007. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
