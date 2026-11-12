---
id: DOC-E12-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

| Mã | HTTP | Trigger / log kỹ thuật | Localization key | Thông báo | Mức | Hành động |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-FBR-400-01 | 400 | Đầu vào sai kiểu hoặc chứa trường ngoài danh sách cho phép; log requestId và mã, không raw nội dung/secret | fbr.400.01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa trường được chỉ ra |
| ERR-FBR-401-01 | 401 | Phiên không hợp lệ; log requestId và mã, không raw nội dung/secret | fbr.401.01 | Vui lòng đăng nhập lại. | High | Đăng nhập |
| ERR-FBR-403-01 | 403 | Thiếu quyền hành động hoặc trường dữ liệu; log requestId và mã, không raw nội dung/secret | fbr.403.01 | Bạn không có quyền thực hiện thao tác này. | High | Kiểm quyền đã được cấp |
| ERR-FBR-404-01 | 404 | Tham chiếu không tồn tại hoặc ngoài scope; log requestId và mã, không raw nội dung/secret | fbr.404.01 | Không tìm thấy dữ liệu được phép xem. | High | Chọn lại nguồn |
| ERR-FBR-409-01 | 409 | Revision thay đổi hoặc khóa yêu cầu khác nội dung; log requestId và mã, không raw nội dung/secret | fbr.409.01 | Nguồn đã thay đổi. Vui lòng rà lại. | High | Tải lại, không ghi đè |
| ERR-FBR-422-01 | 422 | Thiếu căn cứ hoặc chính sách bắt buộc; log requestId và mã, không raw nội dung/secret | fbr.422.01 | Chưa đủ căn cứ để thực hiện. | High | Xem mã câu hỏi hoặc nguồn thiếu |
| ERR-FBR-500-01 | 500 | Lỗi lưu receipt/audit hoặc xử lý nội bộ; log requestId và mã, không raw nội dung/secret | fbr.500.01 | Chưa thể hoàn tất yêu cầu. | High | Đối soát bằng requestId, không coi đã thành công |
| ERR-FBR-503-01 | 503 | Nguồn phụ thuộc gián đoạn; log requestId và mã, không raw nội dung/secret | fbr.503.01 | Nguồn dữ liệu đang gián đoạn. | High | Giữ trạng thái chưa xác định |

BLOCKED là trạng thái ca/thiết kế, không HTTP status. Với GET hợp lệ nhưng chỉ số chưa có, trả 200 cùng value=null, availability và missingReason; không thay lỗi quyền bằng số 0. Nguồn ngoài scope trả 404 an toàn; thiếu quyền hành động trả 403.
