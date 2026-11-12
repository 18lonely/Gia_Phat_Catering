---
id: DOC-E9-USECASES-UC-AIN-003-MD
title: UC-AIN-003 — Kiểm và xem phương án
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-003 — Kiểm và xem phương án

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02) xem phương án của mình. Actor hỗ trợ: Worker/orchestrator thực hiện kiểm trước khi khách đọc. Bên quan tâm: khách cần biết nháp nào đã có evidence hợp lệ.
Truy vết: FR-AIN-CHK-001 / FEAT-060 / US-AIN-003.

Trigger: Candidate của lượt dựng/chỉnh sẵn sàng để worker kiểm, sau đó khách tra kết quả của lượt đó.

Tiền điều kiện — nghiệp vụ: Có runRef, candidateRevision/hash và phiên bản nguồn; khách có quyền sở hữu lượt chạy.
Tiền điều kiện — gate còn mở: E9-Q05, E9-Q12, E9-Q13 chặn kết quả nhánh kinh tế, nguồn và adapter; O-03 không mở cá nhân hóa sức khỏe.

Luồng chính:
1. Worker lấy candidate canonical của run, revision/hash và phiên bản nguồn cần kiểm.
2. Orchestrator gọi FR-MENU-RUL-002 để kiểm toàn phương án không lưu MENU, đối chiếu hash và ruleVersion của evidence.
3. Worker xác định kết quả kiểm từ nguồn/evidence; không đánh dấu hợp lệ nếu có vi phạm cứng, thiếu nguồn hoặc máy kiểm lỗi.
4. Adapter lọc kết quả nhạy cảm trước model/UI, giữ bảng kiểm public an toàn gắn với candidate revision.
5. Khách tra runRef tại UI-AIN-02; hệ thống kiểm quyền sở hữu rồi đọc trạng thái và evidence đã có.
6. Hệ thống trả nháp đã kiểm cùng version/bảng kiểm an toàn hoặc trạng thái chặn; GET không gọi model/validator hay sinh candidate.

Hậu điều kiện thành công: Khách xem nháp có evidence cùng hash/nguồn/ruleVersion; việc đọc không tạo một lượt kiểm mới.
Bảo đảm tối thiểu: Không dùng HTTP 200 của GET để kết luận generation thành công; không lộ rule/lý do cost hoặc cho gửi nháp chưa đạt.

Extensions:
- 2a. Máy kiểm lỗi/không khả dụng: hệ thống giữ trạng thái chặn, lỗi nguyên nhân ERR-AIN-503-01; candidate không VALID và không được gửi.
- 3a. Vi phạm quy tắc cứng: hệ thống ghi kết quả không đạt theo ERR-AIN-422-01; không trình bày candidate như phương án hợp lệ.
- 5a. Nguồn/ruleVersion đổi sau kiểm: hệ thống đánh dấu stale, báo ERR-AIN-409-01 khi cần kiểm lại; không dùng evidence cũ cho bản mới, GET không tự chạy kiểm.
- 5b. Run ngoài quyền: hệ thống trả ERR-AIN-404-01; không lộ phương án của chủ thể khác.
- 4a. Chưa chốt cách phản hồi nhánh kinh tế: hệ thống giữ BLOCKED E9-Q05; không đưa lý do/giá trị cost ra model hoặc khách.

## Giao tiếp và kiểm

API-AIN-003: GET /v1/nutrition-agent/requests/{id}; UI-AIN-02. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
