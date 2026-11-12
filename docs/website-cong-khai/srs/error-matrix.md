---
id: DOC-E8-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi E8

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

| Mã | HTTP | Trigger / log kỹ thuật | Localization key | Thông báo UI | Xử lý | Severity |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-PUB-400-01 | 400 | JSON/kiểu/trường ngoài allowlist sai; log requestId và mã, không body/PII/cost | pub.400.01 | Yêu cầu chưa đúng định dạng. | Sửa trường được chỉ ra | Medium |
| ERR-PUB-401-01 | 401 | Phiên quản trị thiếu/hết hạn; log requestId và mã, không body/PII/cost | pub.401.01 | Vui lòng đăng nhập. | Đăng nhập rồi mở lại | High |
| ERR-PUB-403-01 | 403 | Không có quyền thao tác hoặc đọc lead; log requestId và mã, không body/PII/cost | pub.403.01 | Bạn không có quyền thực hiện. | Liên hệ quản trị quyền | High |
| ERR-PUB-404-01 | 404 | Không có resource công khai hoặc ngoài scope; log requestId và mã, không body/PII/cost | pub.404.01 | Không tìm thấy nội dung. | Quay lại danh sách | Medium |
| ERR-PUB-409-01 | 409 | Version/revision thay đổi hoặc key trùng khác payload; log requestId và mã, không body/PII/cost | pub.409.01 | Nội dung đã thay đổi hoặc yêu cầu trùng. | Tải lại/đối soát trước gửi tiếp | Medium |
| ERR-PUB-422-01 | 422 | Input không đạt: số suất không nguyên dương, consent/field bắt buộc thiếu; log requestId và mã, không body/PII/cost | pub.422.01 | Vui lòng kiểm tra thông tin nhập. | Sửa trường có lỗi | Medium |
| ERR-PUB-422-02 | 422 | Nguồn/giá/quyền công khai hoặc policy chưa đủ; log requestId và mã, không body/PII/cost | pub.422.02 | Chưa đủ điều kiện cung cấp nội dung này. | Giữ chờ, quản trị rà gate | High |
| ERR-PUB-422-03 | 422 | URL loop/đích không công khai/trùng nguồn; log requestId và mã, không body/PII/cost | pub.422.03 | Mapping URL chưa hợp lệ. | Sửa mapping, rà DL-08 | High |
| ERR-PUB-415-01 | 415 | Media không thuộc loại ảnh an toàn được cho phép; log requestId và mã, không body/PII/cost | pub.415.01 | Định dạng ảnh chưa được hỗ trợ. | Chọn ảnh phù hợp chính sách | Medium |
| ERR-PUB-429-01 | 429 | Vượt giới hạn công khai nền hoặc chống spam đã duyệt; log requestId và mã, không body/PII/cost | pub.429.01 | Bạn thao tác quá nhanh. | Chờ theo phản hồi; không tự retry tạo mới | Low |
| ERR-PUB-500-01 | 500 | Lỗi ghi/audit, kết quả commit chưa rõ; log requestId và mã, không body/PII/cost | pub.500.01 | Chưa thể xác nhận đã hoàn tất. | Giữ mã yêu cầu, đối soát trước gửi lại | Critical |
| ERR-PUB-503-01 | 503 | Nguồn/dịch vụ không khả dụng; log requestId và mã, không body/PII/cost | pub.503.01 | Dịch vụ tạm chưa sẵn sàng. | Thử lại sau; không giả kết quả | High |

HTTP đề xuất; UI thông báo an toàn không tiết lộ giá trị nội bộ hoặc sự tồn tại bản nháp. HTTP301 là kết quả chuyển hướng, không mã lỗi.
