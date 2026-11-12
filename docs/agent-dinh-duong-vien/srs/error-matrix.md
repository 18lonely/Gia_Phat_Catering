---
id: DOC-E9-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi AIN
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi AIN

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

| Mã | HTTP | Trigger kỹ thuật (không payload) | Localization key | Thông báo an toàn đề xuất | Severity | Next action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-AIN-400-01 | 400 | JSON/kiểu/trường ngoài schema | ain.400.01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa trường được chỉ ra |
| ERR-AIN-401-01 | 401 | Phiên thiếu/hết hạn/thu hồi | ain.401.01 | Phiên chưa hợp lệ. | High | Xác minh theo cơ chế được duyệt |
| ERR-AIN-403-01 | 403 | Tool/quyền bị từ chối | ain.403.01 | Không được thực hiện yêu cầu này. | High | Không thử vượt quyền |
| ERR-AIN-404-01 | 404 | Tài nguyên không tồn tại hoặc ngoài scope | ain.404.01 | Không tìm thấy dữ liệu. | High | Kiểm mã thuộc phiên của bạn |
| ERR-AIN-409-01 | 409 | Revision/source/evidence đổi | ain.409.01 | Phương án cần kiểm lại. | High | Tải lại và kiểm trước gửi |
| ERR-AIN-409-02 | 409 | Key trùng body khác | ain.409.02 | Mã yêu cầu đã được sử dụng. | Medium | Đối soát yêu cầu gốc |
| ERR-AIN-422-01 | 422 | Ngữ nghĩa chưa rõ hoặc candidate chưa đạt | ain.422.01 | Chưa có phương án hợp lệ cho yêu cầu này. | Medium | Làm rõ/chỉnh yêu cầu không kèm sức khỏe |
| ERR-AIN-429-01 | 429 | Quota hoặc ngân sách admission chặn | ain.429.01 | Hiện chưa thể nhận thêm yêu cầu. | High | Xem thời điểm khả dụng nếu policy có; không đổi identity |
| ERR-AIN-503-01 | 503 | Policy/gate/nguồn/validator/đầu nhận chưa sẵn sàng | ain.503.01 | Chức năng hiện chưa khả dụng. | High | Giữ mã yêu cầu để kiểm lại; không coi đã tiếp nhận |
| ERR-AIN-500-01 | 500 | Lỗi ghi run/receipt/audit | ain.500.01 | Chưa thể xác nhận hoàn tất. | High | Đối soát cùng key trước thử lại |

Log chỉ requestId, actor/scope tham chiếu an toàn, mã tổng quát và thời điểm; không echo input, rule cost, SQL, stack, giá, token hoặc sức khỏe. GET thành công trả HTTP200 cho run FAILED/BLOCKED không là tạo thực đơn thành công. Lỗi policy/gate dùng503; nhánh bệnh lý runtime đóng trước Q09, không dùng thông báo đề xuất này như lời nhắc đã duyệt.
