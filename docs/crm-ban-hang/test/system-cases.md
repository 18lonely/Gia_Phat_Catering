---
id: DOC-E10-TEST-SYSTEM-CASES-MD
title: "10 ca hệ thống E10: có overlap"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# 10 ca hệ thống E10: có overlap

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

Các ca này **có overlap** với 48 ca chức năng; 5 BLOCKED, 5 NOT RUN. Không cộng vào mẫu số nghiệm thu hoặc độ phủ AC.

| TC | BR / NFR | Mục tiêu | Bước / dữ liệu | Expected | Gate | Status | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-CRM-S001 | BR-CRM-001/007; NFR-CRM-001 | Phân quyền chéo khách | Dùng phiên thiếu/hết hạn; đổi customerRef, publicationRef và cache key từ A sang B; thử truy bằng dịch vụ AIN | 401/403/404 theo ngữ cảnh, không trả dữ liệu B hoặc bản nội bộ | Không | NOT RUN |  |  |
| TC-CRM-S002 | BR-CRM-007; NFR-CRM-001 | Rò cost và margin | Đặt canary synthetic trong nested JSON, note, metadata, lỗi, cache; yêu cầu bản khách và tải tệp | Không có canary hoặc trường kinh tế nội bộ; allowlist trước serialize, không chỉ CSS | Không | NOT RUN |  |  |
| TC-CRM-S003 | BR-CRM-007/010; NFR-CRM-001 | Kế toán và projection | Fixture giá mua có VAT, invoiceRequested=false, CK riêng; rà response nội bộ/khách | Không coi VAT 0; không trừ CK vào phải trả nhà cung cấp; khách không thấy cost/margin | Không; không kiểm công thức CK còn mở | NOT RUN |  |  |
| TC-CRM-S004 | BR-CRM-003/004/011; NFR-CRM-002 | Gộp/hoàn tác và sự cố | Chèn lỗi ghi/audit trước/sau commit, kiểm ERR-CRM-500-01 và không xác nhận thành công giả; hai người duyệt cùng bản; hoàn tác khi có liên kết mới theo policy | Không gộp một phần, không mất audit, xử lý liên kết mới theo quyết định | E10-Q03/04; CG08 | BLOCKED |  |  |
| TC-CRM-S005 | BR-CRM-008/011; NFR-CRM-003 | Giá cạnh tranh | Hai giao dịch kích hoạt khoảng chồng cùng customer/mealType | Chỉ một tập khoảng hợp lệ ACTIVE, giao dịch kia 409; không ghi giá một phần | Oracle không chồng đã xác định; không tự chọn biên liền kề | NOT RUN |  |  |
| TC-CRM-S006 | BR-CRM-009; NFR-CRM-003 | Hồi tố phụ lục | Tạo phụ lục ngược ngày với đơn khóa và kỳ E7 đã khóa | Không sửa snapshot; xử lý điều chỉnh theo policy đã duyệt, không tự mở kỳ | E10-Q12; E7-Q05; CG05 | BLOCKED |  |  |
| TC-CRM-S007 | BR-CRM-002/005/012 | Nguồn thiếu và lịch ngoại lệ | Lịch nhiều điểm, ngày nghỉ, sự kiện đến muộn; đánh giá rồi đọc lại | Đúng cửa sổ/ngưỡng được duyệt; dữ liệu thiếu không nguy cơ thấp giả; GET không đánh giá lại | E10-Q05/06; CG05/06/08; Q-13 | BLOCKED |  |  |
| TC-CRM-S008 | NFR-CRM-004 | Tải và khả năng phục hồi | Chạy profile 1000 người đồng thời được duyệt với kích thước dữ liệu và thao tác thực tế | p95 đọc ≤ 300 ms, ghi ≤ 800 ms; không mất audit/receipt hoặc nhân bản giao dịch | E10-Q13; O-04 | BLOCKED |  |  |
| TC-CRM-S009 | NFR-CRM-005 | Giao diện và bàn phím | Mở đủ 9 màn ở 1440/390/360 px; Tab, đổi trạng thái, mở/đóng hộp review | Không tràn toàn trang; nhãn/focus và thông báo đọc được; không gửi mạng từ mock | Kiểm sản phẩm riêng với kiểm mock | NOT RUN |  |  |
| TC-CRM-S010 | NFR-CRM-006; BR-CRM-001/012 | Dữ liệu cá nhân | Thử quyền đọc liên hệ, yêu cầu xóa, bản sao và log theo policy được duyệt | Đúng thời gian/phạm vi được quyết định; không dùng retention audit cho liên hệ | E10-Q01; E8-Q06/E9-Q10 với dữ liệu bàn giao | BLOCKED |  |  |

Mọi mã lỗi trong [ma trận](../srs/error-matrix.md) được kiểm ở nhánh ngoại lệ UC và ca chức năng; lỗi 500/503/409 bổ sung fault tại S004. Kiểm mock không điền Evidence ca S009 sản phẩm.
