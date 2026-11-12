---
id: DOC-E9-USECASES-UC-AIN-013-MD
title: UC-AIN-013 — Đối soát lượt và chi phí AI
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-013 — Đối soát lượt và chi phí AI

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Giám đốc (PER-08) có quyền xem/đối soát usage AIN được cấp. Actor hỗ trợ: Bộ xử lý sự kiện usage. Bên quan tâm: Gia Phát cần tổng chi phí AI có provenance và biết phần chưa xác định.
Truy vết: FR-AIN-LOG-001 / FEAT-064 / US-AIN-013.

Trigger: Có sự kiện usage cần đối soát hoặc Giám đốc rà tình trạng lượt/ngân sách AI theo ngày và nhóm.

Tiền điều kiện — nghiệp vụ: Có runRef, sự kiện usage có provenance và policyVersion để đối chiếu; người xem có quyền quản trị.
Tiền điều kiện — gate còn mở: E9-Q07, E9-Q08, E9-Q10, E9-Q13 chưa chốt ngày/đơn vị, quyền, lưu dữ liệu và ledger; O-03 không mở quyền đọc sức khỏe.

Luồng chính:
1. Bộ xử lý usage đối chiếu sự kiện theo run/eventId duy nhất với reservation và policyVersion tương ứng.
2. Bộ xử lý tách confirmed, estimated, unknown và reserved; chỉ chuyển reserve sang confirmed một lần khi có bằng chứng xác nhận.
3. Bộ xử lý giữ phần chưa rõ và gắn ngày/đơn vị theo policy được duyệt; không xóa debt qua ranh giới ngày.
4. Giám đốc chọn ngày/group và runRef cần rà tại UI-AIN-05; hệ thống kiểm quyền đọc báo cáo AIN.
5. Hệ thống đọc ledger đã có và trả tổng chi phí AI, reservation cùng sai lệch chưa xử lý; GET không thực hiện lại quyết toán hay gọi provider.
6. Giám đốc đối chiếu báo cáo với provenance được phép đọc, không xem raw hội thoại hoặc log AIO.

Hậu điều kiện thành công: Báo cáo thể hiện đúng ledger/đơn vị/policyVersion và tách phần chưa rõ; chi phí AI không bị nhầm với cost nguyên liệu.
Bảo đảm tối thiểu: Unknown không thành 0, sự kiện trùng không tính hai lần; thao tác GET không ghi ledger hoặc khôi phục dữ liệu ngoài quyền.

Extensions:
- 1a. Sự kiện trùng: bộ xử lý nhận diện eventId đã có và không cộng lại; tổng confirmed/reserved không tăng lần hai.
- 2a. Usage thiếu/provider lỗi hoặc timeout: hệ thống giữ UNKNOWN cùng reservation; không báo còn đủ tiền giả hoặc tự hoàn chỗ.
- 3a. Sự kiện đến muộn qua ngày: hệ thống đối chiếu theo ngày của policy được duyệt; debt cũ còn nguyên, chưa có policy thì BLOCKED E9-Q07/E9-Q13.
- 4a. Thiếu quyền: hệ thống trả ERR-AIN-403-01; báo cáo không lộ cho khách/model và ledger không đổi.
- 5a. Nguồn/policy không khả dụng: hệ thống trả ERR-AIN-503-01; không dựng tổng giả hoặc lấy log AIO thay nguồn AIN.

## Giao tiếp và kiểm

API-AIN-013: GET /v1/nutrition-agent/admin/usage; UI-AIN-05. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
