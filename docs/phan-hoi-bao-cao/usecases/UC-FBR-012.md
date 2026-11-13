---
id: DOC-E12-USECASES-UC-FBR-012-MD
title: "UC-FBR-012: Tóm tắt khách và đề xuất nhắc việc"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-012: Tóm tắt khách và đề xuất nhắc việc

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-084; màn UI-FBR-09.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-05, PER-08; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần nháp tóm tắt và danh sách việc cần người thật rà; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào customerRef, timeRange, CRM sourceRefs. Nhánh nghiệp vụ thật cần E10-Q01/05/06/13; AIO-Q01–06; E12-Q11. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Tóm tắt khách và đề xuất nhắc việc” từ UI-FBR-09.
- **Hậu điều kiện thành công có điều kiện**: Nháp tóm tắt và danh sách việc cần người thật rà.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp customerRef, timeRange, CRM sourceRefs.
4. Hệ thống thực hiện: Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ.
5. Hệ thống trình bày nháp tóm tắt và danh sách việc cần người thật rà, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Văn bản CRM yêu cầu đọc khách ngoài scope → Coi là dữ liệu, chặn tại công cụ/DB trước lấy dữ liệu; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Nguồn phản hồi mới chưa sẵn sàng → Ghi thiếu nguồn; không bịa khiếu nại hoặc nguy cơ rời. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-AIO-CRMS-001; BR-FBR-012; US-FBR-012; AC-FBR-012-1, AC-FBR-012-2, AC-FBR-012-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
