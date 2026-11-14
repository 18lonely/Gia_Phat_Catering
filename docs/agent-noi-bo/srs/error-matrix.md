---
id: DOC-AGENT-NOI-BO-SRS-ERROR-MATRIX
title: Ma trận lỗi E5
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e5]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E5: Agent Nội bộ

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 10 dòng mã lỗi từ [SRS E5](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E5](spec.md).

| Mã | HTTP | Trigger/log kỹ thuật | Localization key | Thông báo | Severity | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-AIO-400-01 | 400 | Sai kiểu, tuần hoặc hai nguồn revision cùng lúc; log requestId, không token | aio.400-01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa đầu vào |
| ERR-AIO-401-01 | 401 | Phiên không hợp lệ; log requestId, không token | aio.401-01 | Vui lòng đăng nhập lại. | High | Đăng nhập |
| ERR-AIO-403-01 | 403 | Thiếu quyền/vi phạm allowlist; log requestId, không token | aio.403-01 | Không được thực hiện thao tác này. | High | Kiểm quyền |
| ERR-AIO-404-01 | 404 | Run/menu ngoài scope hoặc không tồn tại; log requestId, không token | aio.404-01 | Không tìm thấy lượt chạy. | High | Chọn lại |
| ERR-AIO-409-01 | 409 | Nguồn hoặc candidate cũ/trạng thái không cho apply; log requestId, không token | aio.409-01 | Phương án cần được kiểm lại. | High | Chạy lại trước khi áp dụng |
| ERR-AIO-409-02 | 409 | Idempotency key dùng body khác; log requestId, không token | aio.409-02 | Mã yêu cầu đã được sử dụng. | High | Đối soát request gốc |
| ERR-AIO-422-01 | 422 | Input ngữ nghĩa không hợp lệ; run chưa VALID; log requestId, không token | aio.422-01 | Chưa có phương án hợp lệ để áp dụng. | Medium | Bổ sung dữ liệu hoặc chọn lại |
| ERR-AIO-429-01 | 429 | Hết quota/concurrency cấu hình; log requestId, không token | aio.429-01 | Đã đạt giới hạn lượt chạy. | High | Theo Retry-After; không đổi key để vượt quota |
| ERR-AIO-500-01 | 500 | Ghi run/audit/apply thất bại; log requestId, không token | aio.500-01 | Chưa thể hoàn tất. | High | Đối soát bằng key/runId |
| ERR-AIO-503-01 | 503 | Không nhận được tác vụ vào hàng đợi bền vững; log requestId, không token | aio.503-01 | Dịch vụ đang gián đoạn. | High | Thử lại cùng key |
