---
id: DOC-E9-USECASES-UC-AIN-007-MD
title: UC-AIN-007 — Xem trạng thái đề xuất
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-007 — Xem trạng thái đề xuất

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02) đã gửi đề xuất. Bên quan tâm: khách cần biết tình trạng có bằng chứng, không hiểu nhầm đã áp dụng.
Truy vết: FR-AIN-STAT-001 / FEAT-062 / US-AIN-007.

Trigger: Sau khi nhận mã tiếp nhận, khách kiểm tra Gia Phát đã nhận/xử lý đề xuất tới đâu.

Tiền điều kiện — nghiệp vụ: Có proposalRef và phiên có quyền sở hữu đề xuất.
Tiền điều kiện — gate còn mở: E9-Q06, E9-Q13 chặn wording sau tiếp nhận, evidence đầu nhận và contract; không tự cam kết SLA. O-03 vẫn đóng.

Luồng chính:
1. Khách chọn proposalRef tại UI-AIN-04 để tra tình trạng đề xuất.
2. Hệ thống xác minh phiên và quyền sở hữu proposal; mã opaque không tự thay bằng chứng quyền.
3. Hệ thống đọc receipt tiếp nhận cùng trạng thái và evidence đã có từ nơi nhận.
4. Hệ thống phân biệt tiếp nhận bền vững, chờ bàn giao và trạng thái có evidence; không dùng thông báo làm bằng chứng bàn giao.
5. Hệ thống trả trạng thái an toàn để khách theo dõi; proposal mới tiếp nhận vẫn chờ người thật xem xét.

Hậu điều kiện thành công: Khách biết trạng thái có căn cứ của đề xuất thuộc mình; GET không thay trạng thái nghiệp vụ hoặc áp dụng thực đơn.
Bảo đảm tối thiểu: Không suy đã duyệt từ việc gửi, không lộ proposal người khác và không cam kết thời hạn chưa được duyệt.

Extensions:
- 2a. Proposal ngoài quyền hoặc không có: hệ thống trả ERR-AIN-404-01 đồng nhất; không lộ tồn tại, dữ liệu không đổi.
- 2b. Phiên hết hạn/thu hồi: hệ thống trả ERR-AIN-401-01; không phục hồi dữ liệu ngoài quyền.
- 3a. Chưa có receipt bàn giao hoặc trạng thái đến muộn: hệ thống giữ trạng thái có evidence hiện tại; không tự chuyển đã bàn giao/đã duyệt.
- 3b. Nơi nhận/policy không sẵn sàng: hệ thống trả ERR-AIN-503-01 cho phần chưa thể đọc/xác nhận; proposal không bị mất và không giả kết quả.

## Giao tiếp và kiểm

API-AIN-007: GET /v1/nutrition-agent/proposals/{id}; UI-AIN-04. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
