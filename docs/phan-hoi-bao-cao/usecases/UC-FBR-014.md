---
id: DOC-E12-USECASES-UC-FBR-014-MD
title: "UC-FBR-014: Hỏi đáp số liệu theo quyền"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-014: Hỏi đáp số liệu theo quyền

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-085; màn UI-FBR-10.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-07, PER-08; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef. Nhánh nghiệp vụ thật cần AIO-Q01–06; E12-Q06/07/08/12; E10-Q15. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Hỏi đáp số liệu theo quyền” từ UI-FBR-10.
- **Hậu điều kiện thành công có điều kiện**: Câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef.
4. Hệ thống thực hiện: Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược.
5. Hệ thống trình bày câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Câu hỏi yêu cầu cập nhật doanh thu hoặc dò cost ngoài quyền → Không có công cụ ghi; từ chối dữ liệu cấm trước khi đưa vào bộ diễn giải; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Quyền bị thu hồi giữa hai lần gọi công cụ → Lần gọi sau và kết quả cuối bị chặn; không dùng cache quyền cũ. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-AIO-DQA-001; BR-FBR-014; US-FBR-014; AC-FBR-014-1, AC-FBR-014-2, AC-FBR-014-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
