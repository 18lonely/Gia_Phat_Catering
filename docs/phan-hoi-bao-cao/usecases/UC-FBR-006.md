---
id: DOC-E12-USECASES-UC-FBR-006-MD
title: UC-FBR-006 — Đọc cost % ngày và theo khách
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-006 — Đọc cost % ngày và theo khách

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-081; màn UI-FBR-06.
- **Cấp độ**: Sea level — mục tiêu người dùng.
- **Tác nhân chính**: PER-05, PER-06, PER-07, PER-08 theo quyền riêng; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần cost % ngày có nguồn e3; ô theo khách chưa xác định khi thiếu công thức; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào date, customerRef, kitchenRef, costResultRef. Nhánh nghiệp vụ thật cần E12-Q07/08; O-01; DATA-COST-Q01–06; E11-Q07/08. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Đọc cost % ngày và theo khách” từ UI-FBR-06.
- **Hậu điều kiện thành công có điều kiện**: Cost % ngày có nguồn E3; ô theo khách chưa xác định khi thiếu công thức.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp date, customerRef, kitchenRef, costResultRef.
4. Hệ thống thực hiện: Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13.
5. Hệ thống trình bày cost % ngày có nguồn e3; ô theo khách chưa xác định khi thiếu công thức, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Không có cost.cost.read → Loại số cost khỏi API, UI, lỗi, log và cache; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Khách có nhiều loại suất hoặc ngày không doanh thu → Không bình quân tỷ lệ hay dùng số giao làm mẫu số; giữ chưa xác định. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-RPT-CPCT-001; BR-FBR-006; US-FBR-006; AC-FBR-006-1, AC-FBR-006-2, AC-FBR-006-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
