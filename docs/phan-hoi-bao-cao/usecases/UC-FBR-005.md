---
id: DOC-E12-USECASES-UC-FBR-005-MD
title: UC-FBR-005 — Xem dashboard theo bốn vai trò
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-005 — Xem dashboard theo bốn vai trò

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-081; màn UI-FBR-05.
- **Cấp độ**: Sea level — mục tiêu người dùng.
- **Tác nhân chính**: PER-05, PER-06, PER-07, PER-08; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào roleView, dateRange, customerRef, kitchenRef. Nhánh nghiệp vụ thật cần E12-Q06/07/08; E7-Q03/04; E10-Q07; E11-Q07/08. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Xem dashboard theo bốn vai trò” từ UI-FBR-05.
- **Hậu điều kiện thành công có điều kiện**: Bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp roleView, dateRange, customerRef, kitchenRef.
4. Hệ thống thực hiện: Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn.
5. Hệ thống trình bày bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Đổi roleView thành giám đốc khi không có quyền → Từ chối; roleView không cấp thêm quyền; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Một nguồn lỗi trong nhiều chỉ số → Ô lỗi hiện thiếu nguồn, ô độc lập vẫn có nguồn; không cộng thiếu như 0. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-RPT-ROLE-001; BR-FBR-005; US-FBR-005; AC-FBR-005-1, AC-FBR-005-2, AC-FBR-005-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
