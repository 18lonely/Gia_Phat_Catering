---
id: DOC-E9-USECASES-UC-AIN-005-MD
title: "UC-AIN-005: Chỉnh thực đơn và kiểm lại"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-005: Chỉnh thực đơn và kiểm lại

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02). Bên quan tâm: khách cần sửa đúng ngày/món và biết kết quả kiểm của bản mới.
Truy vết: FR-AIN-EDIT-001 / FEAT-061 / US-AIN-005.

Trigger: Sau khi xem phương án, khách muốn đổi món hoặc vị trí món trong một ngày của tuần.

Tiền điều kiện (nghiệp vụ): Có candidateRef và baseRevision thuộc phiên; chỉ dẫn chỉ rõ ngày/vị trí/món cần đổi.
Tiền điều kiện (gate còn mở): E9-Q03, E9-Q05, E9-Q12, E9-Q13 chặn đầu vào, nhánh kinh tế, nguồn và contract. O-03 không mở cá nhân hóa sức khỏe.

Luồng chính:
1. Khách gửi candidateRef, baseRevision và chỉ dẫn chỉnh ngày/vị trí/món tại UI-AIN-03.
2. Hệ thống kiểm quyền sở hữu và baseRevision, đối chiếu chỉ dẫn với các vị trí/món được phép.
3. Khi yêu cầu rõ và đủ điều kiện quyền/hạn mức, hệ thống tạo revision candidate mới cùng diff từ bản gốc.
4. Worker kiểm lại máy E2 trên toàn tuần và kiểm phiên bản nguồn cho candidate mới, không dùng kết quả pass của bản cũ.
5. Hệ thống gắn evidence đúng revision/hash vào kết quả, lọc bảng kiểm trước khi cho model/UI đọc.
6. Hệ thống trả diff và bản mới đã kiểm hoặc trạng thái không đạt; bản cũ chỉ được giữ làm lịch sử.

Hậu điều kiện thành công: Chỉ revision mới đạt kiểm toàn phương án được ghi đã kiểm; không có MENU/order được áp dụng.
Bảo đảm tối thiểu: Không dùng chỉnh một ngày để bỏ kiểm phần còn lại; không tự nhận dữ liệu sức khỏe hoặc lộ nguyên nhân cost.

Extensions:
- 2a. Chỉ dẫn mơ hồ: hệ thống yêu cầu làm rõ qua ERR-AIN-422-01/NEEDS_INPUT; chưa tự đổi món, không hỏi thêm bệnh lý.
- 2b. Hai tab gửi cùng baseRevision: một revision tiến; lệnh cũ nhận ERR-AIN-409-01, không ghi đè bản mới.
- 4a. Bản đổi vi phạm quy tắc cứng: hệ thống ghi không đạt theo ERR-AIN-422-01; bản mới bị chặn, không trình bày hợp lệ hoặc thay bằng pass cũ.
- 4b. Máy kiểm/nguồn/policy chưa sẵn sàng: hệ thống trả ERR-AIN-503-01; bản mới chưa có evidence đạt.
- 3a. Mất phản hồi ghi revision: hệ thống báo ERR-AIN-500-01 và yêu cầu đối soát cùng key; chưa xác định đã ghi hay chưa, không tạo bản sửa trùng.

## Giao tiếp và kiểm

API-AIN-005: POST /v1/nutrition-agent/requests/{id}/revisions; UI-AIN-03. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
