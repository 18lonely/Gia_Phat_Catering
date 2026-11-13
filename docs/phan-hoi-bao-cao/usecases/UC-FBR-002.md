---
id: DOC-E12-USECASES-UC-FBR-002-MD
title: "UC-FBR-002: Tiếp nhận và theo dõi khiếu nại"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-002: Tiếp nhận và theo dõi khiếu nại

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-079; màn UI-FBR-02.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-02, PER-03, PER-04, PER-05; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào mealRef, complaintCategoryRef, nội dung về bữa, caseVersion. Nhánh nghiệp vụ thật cần E12-Q02/03; E6 CG01/08; E7-Q02. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Tiếp nhận và theo dõi khiếu nại” từ UI-FBR-02.
- **Hậu điều kiện thành công có điều kiện**: Hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp mealRef, complaintCategoryRef, nội dung về bữa, caseVersion.
4. Hệ thống thực hiện: Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn.
5. Hệ thống trình bày hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Yêu cầu đóng hồ sơ khi thiếu chính sách xử lý → Giữ hồ sơ chưa kết thúc; báo thiếu chính sách; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Khách gửi nội dung trùng nhưng chưa có receipt xác định → Không tự gộp hoặc xóa; nêu cần rà trùng theo Q02. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-FB-CASE-001; BR-FBR-002; US-FBR-002; AC-FBR-002-1, AC-FBR-002-2, AC-FBR-002-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
