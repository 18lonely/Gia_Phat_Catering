---
id: DOC-E13-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

| Mã lỗi | HTTP | Trigger | Thông báo người dùng | Log / localization key | Severity | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-EXP-401-01 | 401 | Chưa xác thực | Phiên làm việc không hợp lệ. | exp.err-exp-401-01: chỉ mã và requestRef, không tiền/lương | High | Đăng nhập lại. |
| ERR-EXP-403-01 | 403 | Sai vai trò/scope hoặc tự duyệt | Bạn không có quyền thực hiện. | exp.err-exp-403-01: chỉ mã và requestRef, không tiền/lương | High | Liên hệ đầu mối cấp quyền, không hiển thị giá trị bị cấm. |
| ERR-EXP-404-01 | 404 | Không tìm thấy tham chiếu trong phạm vi được phép | Không tìm thấy dữ liệu. | exp.err-exp-404-01: chỉ mã và requestRef, không tiền/lương | High | Kiểm tra tham chiếu; không tiết lộ sự tồn tại ngoài scope. |
| ERR-EXP-409-01 | 409 | Sửa kỳ khóa hoặc version bất biến | Bản này không thể ghi đè. | exp.err-exp-409-01: chỉ mã và requestRef, không tiền/lương | High | Lập điều chỉnh hoặc phiên bản mới. |
| ERR-EXP-409-02 | 409 | Version/hash thay đổi | Dữ liệu đã thay đổi. | exp.err-exp-409-02: chỉ mã và requestRef, không tiền/lương | High | Đọc lại và review lại. |
| ERR-EXP-409-03 | 409 | Trùng nguồn chi phí | Khoản này đã có trong nguồn. | exp.err-exp-409-03: chỉ mã và requestRef, không tiền/lương | High | Đối chiếu nguồn, không nhập lại. |
| ERR-EXP-422-01 | 422 | Thiếu trường hoặc chứng từ | Chưa đủ thông tin ghi chi phí. | exp.err-exp-422-01: chỉ mã và requestRef, không tiền/lương | High | Bổ sung trường được chỉ rõ. |
| ERR-EXP-422-02 | 422 | Thiếu nguồn hoặc định nghĩa | Chưa đủ căn cứ để tính. | exp.err-exp-422-02: chỉ mã và requestRef, không tiền/lương | High | Xem danh sách điều kiện còn thiếu. |
| ERR-EXP-422-03 | 422 | Thiếu phương pháp đã duyệt | Lợi nhuận theo khách đang BLOCKED. | exp.err-exp-422-03: chỉ mã và requestRef, không tiền/lương | High | Chỉ xem chi phí trực tiếp; chờ quyết định Giám đốc. |
| ERR-EXP-422-04 | 422 | Điều chỉnh thiếu lý do/duyệt | Chưa thể ghi nhận điều chỉnh. | exp.err-exp-422-04: chỉ mã và requestRef, không tiền/lương | High | Bổ sung lý do và quyết định hợp lệ. |
| ERR-EXP-503-01 | 503 | Nguồn không truy cập được | Tạm thời chưa đọc được nguồn. | exp.err-exp-503-01: chỉ mã và requestRef, không tiền/lương | High | Giữ lần cũ, thử đọc lại theo quy trình; không thay bằng 0. |

401/403/404/503 dùng chung mọi endpoint theo điều kiện. 409 dùng thao tác ghi/version. 422 không chuyển dữ liệu thiếu thành 0. Mapping HTTP là đề xuất chờ E13-Q12.
