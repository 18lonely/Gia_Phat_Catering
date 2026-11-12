---
id: DOC-E9-USECASES-UC-AIN-001-MD
title: UC-AIN-001 — Mở phiên yêu cầu
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-001 — Mở phiên yêu cầu

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02) muốn lập thực đơn tập thể. Bên quan tâm: Gia Phát cần gắn phiên với đúng chủ thể và consent.
Truy vết: FR-AIN-SESS-001 / FEAT-060 / US-AIN-001.

Trigger: Khách bắt đầu yêu cầu tư vấn thực đơn tập thể trên kênh được phép sử dụng agent.

Tiền điều kiện — nghiệp vụ: Khách cung cấp kênh và bằng chứng identity/consent theo policy; không tự khai nhóm/quyền để được truy cập.
Tiền điều kiện — gate còn mở: E9-Q02, E9-Q10 chưa chốt guest/identity/consent; chưa được mở phiên thật. O-03 vẫn đóng đối với cá nhân hóa sức khỏe.

Luồng chính:
1. Khách bắt đầu yêu cầu tại UI-AIN-01 và cung cấp channelRef cùng bằng chứng xác minh/consent được policy yêu cầu.
2. Hệ thống kiểm policy truy cập của kênh và phiên bản consent đã được duyệt.
3. Hệ thống xác minh chủ thể và lấy nhóm/quyền từ server, không dùng userId/group/role do khách tự gán.
4. Khi đủ điều kiện, hệ thống cấp sessionRef opaque gắn với chủ thể và phạm vi được phép.
5. Hệ thống trả tham chiếu phiên để khách tiếp tục yêu cầu tập thể, ghi metadata an toàn cùng requestId theo quyền.

Hậu điều kiện thành công: Có sessionRef đúng chủ thể; phiên không cấp quyền cost hoặc quyền agent nội bộ.
Bảo đảm tối thiểu: Thiếu quyết định thì không tạo users/eaters mặc định cho guest, không gọi AI hoặc lưu hội thoại để vượt gate; không tạo order/báo giá.

Extensions:
- 2a. Chưa chốt loại người dùng/consent: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q02/E9-Q10; chưa mở phiên thật, không lưu hội thoại.
- 3a. Bằng chứng phiên thiếu/hết hạn/thu hồi: hệ thống trả ERR-AIN-401-01; không cấp hoặc khôi phục phiên.
- 3b. Khách đọc lại phiên của người khác: hệ thống trả ERR-AIN-404-01 đồng nhất; không phục hồi dữ liệu ngoài quyền.
- 4a. Lỗi ghi hoặc mất phản hồi: hệ thống báo ERR-AIN-500-01, yêu cầu đối soát cùng key; trạng thái tạo phiên chưa rõ, không báo hoàn tất giả.

## Giao tiếp và kiểm

API-AIN-001: POST /v1/nutrition-agent/sessions; UI-AIN-01. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
