---
id: DOC-E11-USECASES-UC-PUR-001-MD
title: "UC-PUR-001: Lập nhu cầu nguyên liệu"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-001: Lập nhu cầu nguyên liệu

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Kế toán (PER-07).
- Bên quan tâm: người thao tác cần nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Lập nhu cầu nguyên liệu” trên UI-PUR-01.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E6 CG06, ORD-Q10/14; E11-Q01. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-01, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: planRef, planRevision, estimateRef, serviceDate, kitchenId.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đối chiếu đúng bản kế hoạch và dự toán; cộng theo nguyên liệu và đơn vị quy đổi đã có căn cứ; hiển thị nguồn thiếu, không tự trừ tồn hoặc áp hao hụt lần hai.
5. Hệ thống trả: Nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Thiếu hệ số g/kg: Chặn tổng hợp khác đơn vị; không coi hệ số là 1 (ERR-PUR-422-11).
- Bước 4: Kế hoạch đổi revision khi đang xem: Đánh dấu nguồn cũ; không dùng số cũ làm nhu cầu hiện hành.
- Bước 4: thiếu policy/nguồn tại E6 CG06, ORD-Q10/14; E11-Q01: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-PUR-DEM-001 / FEAT-074 / BR-PUR-001 / US-PUR-001 / AC-PUR-001-1, AC-PUR-001-2, AC-PUR-001-3 / API-PUR-001. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
