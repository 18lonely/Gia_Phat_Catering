---
id: DOC-E12-USECASES-UC-FBR-008-MD
title: "UC-FBR-008: Kiểm lại đề xuất đổi món hoặc định lượng"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-008: Kiểm lại đề xuất đổi món hoặc định lượng

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-082; màn UI-FBR-07.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-05, PER-08; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào candidateRef, candidateRevision, menuSourceRef. Nhánh nghiệp vụ thật cần AIO-Q02/05/06; DL-01; E11-Q15; E12-Q09. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Kiểm lại đề xuất đổi món hoặc định lượng” từ UI-FBR-07.
- **Hậu điều kiện thành công có điều kiện**: Bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp candidateRef, candidateRevision, menuSourceRef.
4. Hệ thống thực hiện: Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO.
5. Hệ thống trình bày bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Một lần thay định lượng không chạy lại kiểm dị ứng/E2/E3 → Chặn nhãn sẵn sàng review; nêu kiểm còn thiếu; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Nguồn kiểm khác hash ứng viên → Từ chối ghép kết quả; yêu cầu kiểm lại cùng revision. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-AIO-RCHK-001; BR-FBR-008; US-FBR-008; AC-FBR-008-1, AC-FBR-008-2, AC-FBR-008-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
