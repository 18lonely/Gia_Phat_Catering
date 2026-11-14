---
id: DOC-DINH-DUONG-SRS-ERROR-MATRIX
title: Ma trận lỗi E4
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e4]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E4: Dinh dưỡng

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 9 dòng mã lỗi từ [SRS E4](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E4](spec.md).

| Mã | HTTP | Trigger/log kỹ thuật | Localization key | Thông báo | Severity | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-NUTR-400-01 | 400 | JSON/kiểu/field lạ không hợp lệ; log requestId, không token | nutr.400-01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa trường được chỉ ra |
| ERR-NUTR-401-01 | 401 | Phiên không hợp lệ; log requestId, không token | nutr.401-01 | Vui lòng đăng nhập lại. | High | Đăng nhập |
| ERR-NUTR-403-01 | 403 | Thiếu quyền thao tác; log requestId, không token | nutr.403-01 | Bạn không có quyền thực hiện. | High | Liên hệ quản trị |
| ERR-NUTR-404-01 | 404 | Không tồn tại hoặc ngoài scope; log requestId, không token | nutr.404-01 | Không tìm thấy dữ liệu. | High | Chọn lại dữ liệu thuộc quyền |
| ERR-NUTR-409-01 | 409 | Version hoặc trạng thái nguồn đã đổi; log requestId, không token | nutr.409-01 | Dữ liệu đã thay đổi. | High | Tải lại và tính lại |
| ERR-NUTR-422-01 | 422 | Số âm/null, nguồn thiếu hoặc số vượt precision; log requestId, không token | nutr.422-01 | Thành phần dinh dưỡng chưa hợp lệ. | Medium | Kiểm trường báo lỗi |
| ERR-NUTR-422-02 | 422 | Thiếu thành phần/quy đổi/recipe hiệu lực; log requestId, không token | nutr.422-02 | Chưa đủ dữ liệu để tính. | Medium | Bổ sung nguyên liệu được liệt kê |
| ERR-NUTR-422-03 | 422 | Tổ hợp suất sai cấu trúc/trùng món; log requestId, không token | nutr.422-03 | Tổ hợp món chưa hợp lệ. | Medium | Chọn đúng số món |
| ERR-NUTR-500-01 | 500 | Lỗi giao dịch nội bộ; log requestId, không token | nutr.500-01 | Chưa thể hoàn tất. | High | Dùng requestId để đối soát; không tự coi đã lưu |
