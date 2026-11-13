---
id: DOC-E11-USECASES-UC-PUR-015-MD
title: "UC-PUR-015: Kiểm cổng chuyển duyệt MENU"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-PUR-015: Kiểm cổng chuyển duyệt MENU

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Bối cảnh

- Phạm vi: E11; cấp độ Sea level.
- Actor chính: Dinh dưỡng viên (PER-05).
- Bên quan tâm: người thao tác cần readiness và lý do chặn; việc chuyển thật chờ adapter nguồn; kế toán cần truy nguồn số; quản lý cơ sở cần đúng phạm vi.
- Trigger: người dùng chọn “Kiểm cổng chuyển duyệt MENU” trên UI-PUR-09.
- Tiền điều kiện: có phiên/quyền cơ sở; nguồn đúng bản và điều kiện liên quan được xác nhận cho nhánh thực thi. Gate đang mở: E11-Q12/13; DL-01; E6 CG05/06/07. Nhánh phụ thuộc chỉ kiểm cổng, không giả lập chính sách nguồn.
- Hậu điều kiện thành công: Readiness và lý do chặn; việc chuyển thật chờ adapter nguồn. Không thay trạng thái nghiệp vụ, không ghi dữ liệu qua GET.
- Bảo đảm tối thiểu: lỗi không thay số liệu cũ; không lộ giá/ảnh ngoài quyền.

## Luồng chính

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: candidateRef, candidateVersion, checkRefs.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Kiểm đủ kết quả đúng nguồn và cổng MENU hiện hành. CHAN chặn vượt cost; CANH_BAO giữ cảnh báo và vẫn qua MENU; thiếu đầu vào luôn chặn. Không ghi duyệt/công bố hoặc cập nhật E6.
5. Hệ thống trả: Readiness và lý do chặn; việc chuyển thật chờ adapter nguồn.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

## Ngoại lệ

- Bước 2: thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3: Quy tắc cứng vi phạm hoặc thiếu cost: Không được chuyển như đã đạt; giữ ứng viên (ERR-PUR-422-25).
- Bước 4: Nguồn thay đổi giữa kiểm và chuyển: Từ chối dùng kết quả cũ; yêu cầu kiểm lại, không bỏ qua MENU.
- Bước 4: thiếu policy/nguồn tại E11-Q12/13; DL-01; E6 CG05/06/07: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5: kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## Yêu cầu đặc biệt và truy vết

FR-MENU-SGT-001 / FEAT-078 / BR-PUR-015 / US-PUR-015 / AC-PUR-015-1, AC-PUR-015-2, AC-PUR-015-3 / API-PUR-015. [RTM](../test/traceability.md). Tần suất và tải chưa có căn cứ, chờ E11-Q13.
