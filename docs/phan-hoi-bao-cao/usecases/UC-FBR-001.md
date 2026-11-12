---
id: DOC-E12-USECASES-UC-FBR-001-MD
title: UC-FBR-001 — Gửi đánh giá bữa ăn
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-001 — Gửi đánh giá bữa ăn

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-079; màn UI-FBR-01.
- **Cấp độ**: Sea level — mục tiêu người dùng.
- **Tác nhân chính**: PER-02, PER-03, PER-04, PER-05; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần đánh giá có receipt và trạng thái tiếp nhận; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào mealRef, ratingScaleRef, ratingValue, sourceScope. Nhánh nghiệp vụ thật cần E12-Q01/02; E6 CG01/08. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Gửi đánh giá bữa ăn” từ UI-FBR-01.
- **Hậu điều kiện thành công có điều kiện**: Đánh giá có receipt và trạng thái tiếp nhận.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp mealRef, ratingScaleRef, ratingValue, sourceScope.
4. Hệ thống thực hiện: Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn.
5. Hệ thống trình bày đánh giá có receipt và trạng thái tiếp nhận, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Giá trị ngoài thang đã duyệt → Từ chối giá trị, không ghi đánh giá; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Gửi lại cùng yêu cầu sau mất phản hồi → Chỉ một đánh giá theo receipt; chính sách số lần đánh giá vẫn chờ Q02. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-FB-RATE-001; BR-FBR-001; US-FBR-001; AC-FBR-001-1, AC-FBR-001-2, AC-FBR-001-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
