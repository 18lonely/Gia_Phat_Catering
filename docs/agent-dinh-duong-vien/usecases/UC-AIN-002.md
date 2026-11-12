---
id: DOC-E9-USECASES-UC-AIN-002-MD
title: UC-AIN-002 — Yêu cầu thực đơn tập thể
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-002 — Yêu cầu thực đơn tập thể

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02). Bên quan tâm: khách cần phương án tập thể đúng đầu vào; Giám đốc cần lượt chạy nằm trong hạn mức.
Truy vết: FR-AIN-GEN-001 / FEAT-060 / US-AIN-002.

Trigger: Khách đã xác định nhu cầu suất ăn và gửi yêu cầu dựng thực đơn cho tuần/ngày phục vụ.

Tiền điều kiện — nghiệp vụ: Có sessionRef hợp lệ và loại suất/số suất/ngày, khẩu vị/kiêng kỵ theo danh mục được phép.
Tiền điều kiện — gate còn mở: E9-Q01, E9-Q03, E9-Q07, E9-Q11, E9-Q12, E9-Q13 chặn provider, đầu vào, quota, bộ dựng và nguồn/contract. O-03 không mở nhánh sức khỏe.

Luồng chính:
1. Khách gửi sessionRef, loại suất, số suất nguyên dương, tuần/ngày và lựa chọn khẩu vị/kiêng kỵ tại UI-AIN-01.
2. Hệ thống xác minh chủ thể/scope và kiểm các trường đầu vào, làm rõ phần chưa có nghĩa xác định.
3. Hệ thống kiểm policy, nguồn đã duyệt và giữ hạn mức lượt/ngân sách trước khi nhận lượt có chi phí.
4. Hệ thống ghi run bền vững theo key/body của yêu cầu và trả tham chiếu theo dõi.
5. Worker dựng candidate qua công cụ được phép, chỉ dùng món/công thức đã duyệt; phép tính dinh dưỡng/cost không do model tự tính.
6. Worker gắn candidate revision/hash và nguồn vào trạng thái chờ CHK; hệ thống chưa trình bày candidate chưa kiểm là hợp lệ.

Hậu điều kiện thành công: Run tồn tại bền vững, candidate chờ kiểm trước trình bày; không có MENU/order chính thức.
Bảo đảm tối thiểu: Không tự đoán kiêng kỵ, không thu/suy luận sức khỏe, không dùng quota AIO hoặc phát tán cost; ACK không thay kết quả kiểm.

Extensions:
- 2a. Sai kiểu/trường hoặc số suất âm/lẻ: hệ thống trả ERR-AIN-400-01/ERR-AIN-422-01 theo nguyên nhân; chưa dựng candidate.
- 2b. Kiêng kỵ chưa rõ: hệ thống trả NEEDS_INPUT để khách làm rõ nhu cầu không kèm sức khỏe; không tự đoán phương án.
- 3a. Thiếu policy/nguồn: hệ thống trả ERR-AIN-503-01 kèm gate; không gọi provider.
- 3b. Không đủ hạn mức/ngân sách: hệ thống trả ERR-AIN-429-01; chưa nhận lượt có chi phí.
- 4a. Gửi lại cùng key/body sau mất mạng: hệ thống trả cùng run theo quyền hiện tại; không reserve hoặc tính lượt lần hai. Cùng key khác body trả ERR-AIN-409-02, không tạo run mới.
- 4b. Lỗi ghi/mất phản hồi chưa đối soát được: hệ thống báo ERR-AIN-500-01; kết quả lưu chưa rõ, khách giữ key gốc.

## Giao tiếp và kiểm

API-AIN-002: POST /v1/nutrition-agent/requests; UI-AIN-01. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
