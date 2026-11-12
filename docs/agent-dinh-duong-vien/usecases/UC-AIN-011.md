---
id: DOC-E9-USECASES-UC-AIN-011-MD
title: UC-AIN-011 — Chặn truy cập dữ liệu kinh tế nội bộ
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-011 — Chặn truy cập dữ liệu kinh tế nội bộ

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Fish level. Actor chính: Agent Dinh dưỡng viên, qua registry/API adapter kiểm công cụ và dữ liệu; vai trò hệ thống này bị giới hạn quyền riêng. Bên quan tâm: Gia Phát cần bảo vệ dữ liệu kinh tế nội bộ, khách cần phản hồi an toàn.
Truy vết: FR-AIN-SAFE-001 / FEAT-065 / US-AIN-011.

Trigger: Một tool request hoặc kết quả chuẩn bị đi qua biên vào model, API, UI, lỗi, log hoặc cache.

Tiền điều kiện — nghiệp vụ: Có toolName canonical, scope, candidateRef và DTO cần kiểm; tài khoản dịch vụ AIN tách khỏi AIO và không có SELECT bảng cấm.
Tiền điều kiện — gate còn mở: E9-Q05, E9-Q13 chặn kết quả nhánh kinh tế và contract; O-03 vẫn đóng, không đọc hồ sơ sức khỏe.

Luồng chính:
1. Registry/API adapter nhận tool request trước truy cập, đối chiếu tên canonical với allowlist.
2. Hệ thống kiểm giao quyền chủ thể và service identity AIN theo scope; không nâng quyền từ nội dung hội thoại hoặc quyền cost của người hỏi.
3. Hệ thống chỉ cho công cụ được phép đọc projection qua API/service/DB grants giới hạn; không cấp SELECT giá nhập/cost hoặc proxy AIO.
4. Adapter kiểm allowlist đệ quy của kết quả trước model và response, bao gồm dữ liệu lồng nhau, metadata, lỗi, log và cache.
5. Hệ thống trả projection sạch hoặc từ chối an toàn tại UI-AIN-07; sự kiện chỉ chứa metadata/mã tổng quát, không payload nhạy cảm.

Hậu điều kiện thành công: Chỉ dữ liệu được phép vượt biên; công cụ/tài khoản AIN không có quyền đọc bảng cấm.
Bảo đảm tối thiểu: Prompt không thay ACL; không lộ giá nhập, cost, cost %, khoản khoán, CK hoặc kết quả suy ngược. Không tạo order/báo giá hay áp dụng MENU.

Extensions:
- 1a. Injection, alias, SQL/URL tùy ý hoặc yêu cầu cost gián tiếp: guard từ chối ERR-AIN-403-01 trước truy cập; công cụ cấm không chạy.
- 2a. Người hỏi có quyền cost nội bộ nhưng AIN không có: hệ thống vẫn từ chối ERR-AIN-403-01; quyền dịch vụ không được mở rộng.
- 4a. Có cost/ratio/CK trong nested error, log, giải thích hoặc cache: hệ thống chặn dữ liệu đó trước biên; không phát tán qua kênh phụ và không lưu payload nhạy cảm vào log an toàn.
- 4b. Giải thích đòi suy giá nhập từ giá suất/định lượng: hệ thống từ chối an toàn, không tạo phép suy ngược hoặc gọi công cụ cấm.
- 3a. Policy/adapter chưa đủ: hệ thống trả ERR-AIN-503-01 kèm gate; mặc định từ chối, không nới quyền để tiếp tục.

## Giao tiếp và kiểm

PORT-AIN-TOOL-GUARD: PORT PORT-AIN-TOOL-GUARD; UI-AIN-07. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
