---
id: DOC-E9-USECASES-UC-AIN-008-MD
title: "UC-AIN-008: Từ chối gợi ý cá nhân khi gate đóng"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-008: Từ chối gợi ý cá nhân khi gate đóng

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level (GATE-ONLY). Actor chính: Người ăn có tài khoản (PER-03) hoặc người ăn qua QR (PER-04) muốn biết tính năng có khả dụng hay không. Bên quan tâm: người ăn không bị yêu cầu hồ sơ khi phạm vi chưa được duyệt.
Truy vết: FR-AIN-GATE-001 / FEAT-063 / US-AIN-008.

Trigger: Người ăn tìm chức năng gợi ý cá nhân và kiểm tra khả năng sử dụng.

Tiền điều kiện (nghiệp vụ): O-03 còn đóng và FEAT-047 chỉ gate; yêu cầu chỉ xem khả dụng, không có profile hoặc consent sức khỏe.
Tiền điều kiện (gate còn mở): E9-Q14 và quyết định O-03 chưa có căn cứ mở. Không giả các gate đã được duyệt; đây chỉ là luồng chặn an toàn.

Luồng chính:
1. Người ăn yêu cầu xem khả dụng của gợi ý cá nhân tại UI-AIN-07.
2. Hệ thống kiểm yêu cầu chỉ thuộc đường đọc khả dụng, không nhận trường hồ sơ/sức khỏe.
3. Hệ thống đọc trạng thái gate từ server, xác định O-03 chưa mở và FEAT-047 chưa có luồng được phép.
4. Hệ thống trả CLOSED cùng lý do khả dụng chung; không gọi recommendation hoặc đọc hồ sơ.
5. Giao diện hiển thị tính năng chưa khả dụng, không có biểu mẫu hồ sơ hay thao tác nhận gợi ý.

Hậu điều kiện thành công: Gate vẫn CLOSED và người ăn biết tính năng chưa khả dụng; không phát sinh gợi ý hoặc hồ sơ.
Bảo đảm tối thiểu: Không thu, đọc hoặc suy luận sức khỏe; không thay lựa chọn/order và không mở gate bằng chat hoặc flag client.

Extensions:
- 2a. Client gửi trường bệnh lý/hồ sơ hoặc gọi đường không hỗ trợ: hệ thống từ chối yêu cầu sai schema bằng ERR-AIN-400-01; không lưu hoặc chuyển payload tới tool/model.
- 3a. Client tự khai gate đã mở: hệ thống bỏ tuyên bố quyền từ client và giữ CLOSED; không tạo gợi ý hay quyền mới.
- 3b. Không đọc được điều kiện khả dụng: hệ thống trả ERR-AIN-503-01 an toàn; tính năng không được mở, không dùng thiếu dữ liệu làm quyết định cho phép.

Điều kiện xem xét mở chỉ là quyết định có nguồn về O-03, đặc tả/consent/quyền/xóa và contract của FEAT-047 cùng phần hồ sơ liên quan, xác nhận persona và review E9-Q14. Chưa điều kiện nào được coi đã đạt; không mô tả luồng mở trong UC này.

## Giao tiếp và kiểm

API-AIN-008: GET /v1/nutrition-agent/personal-availability; UI-AIN-07. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
