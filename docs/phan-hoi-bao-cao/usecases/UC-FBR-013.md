---
id: DOC-E12-USECASES-UC-FBR-013-MD
title: "UC-FBR-013: Soạn nội dung báo giá nháp để review"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-FBR-013: Soạn nội dung báo giá nháp để review

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

- **Phạm vi**: E12, FEAT-084; màn UI-FBR-09.
- **Cấp độ**: Sea level (mục tiêu người dùng).
- **Tác nhân chính**: PER-05, PER-08; quyền phải được cấp theo scope.
- **Các bên quan tâm**: người yêu cầu cần nháp báo giá có nguồn và nhãn chưa phát hành; chủ nguồn cần dữ liệu gốc không bị sửa; người review cần truy lại căn cứ.
- **Tiền điều kiện**: phiên hợp lệ, có quyền trên nguồn; đầu vào customerRef, quoteRevisionRef, menuRef, nguồn giá được phép. Nhánh nghiệp vụ thật cần E10-Q08/09/13/15; AIO-Q01–06; E12-Q11. Các gate chưa được coi là đạt.
- **Kích hoạt**: người dùng chọn “Soạn nội dung báo giá nháp để review” từ UI-FBR-09.
- **Hậu điều kiện thành công có điều kiện**: Nháp báo giá có nguồn và nhãn chưa phát hành.
- **Bảo đảm tối thiểu**: không lộ dữ liệu ngoài quyền; lỗi không được báo thành công; giữ nguồn gốc, không tự đóng câu hỏi.

## Luồng chính

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp customerRef, quoteRevisionRef, menuRef, nguồn giá được phép.
4. Hệ thống thực hiện: Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này.
5. Hệ thống trình bày nháp báo giá có nguồn và nhãn chưa phát hành, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

## Nhánh và ngoại lệ

- **2a**: hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- **2b**: thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- **3a**: sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- **4a**: Yêu cầu gửi báo giá hoặc sửa giá hợp đồng → Từ chối hành động ghi/gửi; chỉ trả nháp; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- **4b**: Báo giá nguồn đã có revision mới → Ghi cũ nguồn và yêu cầu review; không thay snapshot cũ. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- **4c**: nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- **5a**: lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## Yêu cầu đặc biệt và biến thể

FR-AIO-CRMQ-001; BR-FBR-013; US-FBR-013; AC-FBR-013-1, AC-FBR-013-2, AC-FBR-013-3. Kênh QR ở FEAT-079 cần CG01/08 riêng, không mượn danh tính tài khoản khác. Đầu ra chưa có evidence không gọi hoàn tất. Không chọn tần suất, SLA, giới hạn hoặc retry mới. [RTM](../test/traceability.md).
