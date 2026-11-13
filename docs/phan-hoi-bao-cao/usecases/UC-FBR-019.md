---
id: DOC-E12-USECASES-UC-FBR-019-MD
title: "UC-FBR-019: Xem nhật ký dinh dưỡng của mình"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-019: Xem nhật ký dinh dưỡng của mình

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-087; màn UI-FBR-12.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-03; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào dateRange; subject từ phiên. Nhánh nghiệp vụ thật cần E12-Q15/16; E6 CG01/08; NUTR-Q03/04. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Xem nhật ký dinh dưỡng của mình” từ UI-FBR-12.
- **Hậu điều kiện thành công có điều kiện**: Danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp dateRange; subject từ phiên.
4. Hệ thống thực hiện: Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân.
5. Hệ thống trình bày danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Sửa subjectRef sang người khác → Không trả bữa hoặc tiết lộ tồn tại của nhật ký khác; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Nguồn dinh dưỡng đổi sau ngày ăn → Giữ snapshot lịch sử và nhãn nguồn cũ, không viết lại. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-NUTR-DVIW-001; BR-FBR-019; US-FBR-019; AC-FBR-019-1, AC-FBR-019-2, AC-FBR-019-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
