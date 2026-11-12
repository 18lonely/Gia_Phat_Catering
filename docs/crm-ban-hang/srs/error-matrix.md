---
id: DOC-E10-SRS-ERROR-MATRIX-MD
title: Ma trận lỗi E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ma trận lỗi E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

| Mã | HTTP | Điều kiện kỹ thuật | Khóa thông báo | Thông báo người dùng | Mức | Hành động |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-CRM-400-01 | 400 | Sai kiểu JSON hoặc trường ngoài schema | crm.400.01 | Yêu cầu chưa đúng định dạng. | Trung bình | Sửa trường được chỉ ra |
| ERR-CRM-401-01 | 401 | Thiếu/hết/thu hồi phiên | crm.401.01 | Phiên làm việc chưa hợp lệ. | Cao | Xác thực lại |
| ERR-CRM-403-01 | 403 | Không có quyền hành động hoặc tự duyệt bị cấm | crm.403.01 | Bạn chưa được phép thực hiện thao tác này. | Cao | Liên hệ người quản lý quyền |
| ERR-CRM-404-01 | 404 | Không tồn tại hoặc ngoài phạm vi | crm.404.01 | Không tìm thấy dữ liệu. | Cao | Kiểm lại tham chiếu thuộc quyền |
| ERR-CRM-409-01 | 409 | Version/hash thay đổi | crm.409.01 | Dữ liệu đã thay đổi, cần rà lại. | Cao | Tải bản mới và đối chiếu |
| ERR-CRM-409-02 | 409 | Khóa/nguồn trùng nhưng nội dung khác | crm.409.02 | Yêu cầu đã được dùng với nội dung khác. | Cao | Đối soát bản gốc |
| ERR-CRM-409-03 | 409 | Khoảng giá chồng lấn hoặc nhiều giá khớp | crm.409.03 | Có khoảng giá chồng lấn cần xử lý. | Cao | Rà các khoảng của cùng khách và loại suất |
| ERR-CRM-422-01 | 422 | Thiếu bằng chứng hoặc vi phạm invariant | crm.422.01 | Chưa đủ điều kiện nghiệp vụ. | Cao | Bổ sung nguồn hoặc sửa đề nghị |
| ERR-CRM-500-01 | 500 | Không xác định được kết quả ghi/audit | crm.500.01 | Chưa thể xác nhận thao tác hoàn tất. | Cao | Giữ khóa cũ để đối soát |
| ERR-CRM-503-01 | 503 | Gate hoặc nguồn bắt buộc chưa sẵn sàng | crm.503.01 | Chức năng đang chờ điều kiện đầu vào. | Cao | Theo dõi gate; không thử vượt quyền |

Không echo dữ liệu liên hệ, cost, margin, SQL hoặc stack. Log chỉ mã lỗi, requestId, actor/scope được phép và thời điểm. 404 đồng nhất không tồn tại/ngoài quyền. BLOCKED là trạng thái ca/gate, không mã HTTP. GET hồ sơ có thể trả 200 với nhóm thiếu được ghi nhãn; không coi đó là đầy đủ.
