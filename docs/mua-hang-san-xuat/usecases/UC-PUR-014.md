---
id: DOC-E11-USECASES-UC-PUR-014-MD
title: "UC-PUR-014: Kiểm lại ứng viên thay món"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-014: Kiểm lại ứng viên thay món

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Dinh dưỡng viên (PER-05).
- Bên quan tâm: người thao tác cần bộ kết quả hoặc trạng thái blocked kèm nguồn thiếu; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Kiểm lại ứng viên thay món” trên UI-PUR-09.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: DL-01; E11-Q15; O-01/O-02; CK/DATA-COST. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Bộ kết quả hoặc trạng thái BLOCKED kèm nguồn thiếu. Bản nháp có version và dấu vết; chưa đồng nghĩa duyệt hoặc có hiệu lực.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: candidateRef, candidateVersion, menuSourceRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Mỗi lần thay đều yêu cầu kiểm lại dị ứng, quy tắc E2 và cost E3 trên cùng phiên bản; chỉ hiển thị kết quả có provenance; không dùng lại kết quả món cũ.
5. Hệ thống trả: Bộ kết quả hoặc trạng thái BLOCKED kèm nguồn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Thiếu giá hoặc thiếu căn cứ dị ứng: BLOCKED; không trả đạt dù quy tắc khác đạt (ERR-PUR-422-24).
- Bước 4: Người dùng đổi ứng viên sau lần kiểm: Kết quả cũ không hợp lệ; chạy lại cả ba kiểm.
- Bước 4: thiếu policy/nguồn tại DL-01; E11-Q15; O-01/O-02; CK/DATA-COST: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-MENU-SCK-001 / FEAT-078 / BR-PUR-014 / US-PUR-014 / AC-PUR-014-1, AC-PUR-014-2, AC-PUR-014-3 / API-PUR-014. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
