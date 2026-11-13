---
id: DOC-E6-TEST-CHECKLIST
title: Checklist review và kiểm thử E6
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Checklist review và kiểm thử E6

Draft · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.

- [ ] BA xác nhận nguồn D-04/D-14/D-19/D-21 và 14P0/5P1; không mở rộng E7–E13.
- [ ] Đối chiếu evidence cho ORD-Q01–15, Q-14/Q-16/O-06 và giữ O-03 chặn FEAT-046/047. Giữ E6-EVID-001/002: không hỏi lại hoặc tự chốt scope một/nhiều công ty, C→S và S+C vượt T.
- [ ] Tech lead review scope user/guest/service, token revocation, persistent dedupe, envelope E1-Q01, schema delta.
- [ ] QA review [57 AC/test](review-test-cases.md), [10 ca gốc](test-cases.md) và [ca hệ thống](system-test-cases.md); loại trùng mục tiêu khi lập test run.
- [ ] Kiểm S/C/T/D và toàn tổ hợp; không dùng registered count làm total, không dùng số món làm số suất.
- [ ] Race writer/lock/approval; rollback; mất response ghi; duplicate/out-of-order event; nguồn MENU bị thu hồi. UC010/011 cùng PORT-LOCK và một transaction khóa, không tính hai lần khóa.
- [ ] UI desktop/mobile, keyboard, dialog, empty/error/loading/unknown result, old plan version và missing nutrition.
- [ ] Security IDOR/guest scope/allowlist; không lộ cost/PII/token; không thu sức khỏe gated.
- [ ] Regression VAT phải trả/không hóa đơn/chiết khấu riêng; NFR-COST-002; CK và DATA-COST giữ nguyên.
- [ ] Khi có backend: 1000 CCU trong10 phút,0 mất/trùng; pilot2 khách/2tuần theo roadmap. Chưa đánh dấu đạt.

## Evidence theo thao tác ngày 12/11/2026

- [ ] Dùng [evidence protocol](evidence-protocol.md) ghi actor/principal, trigger và snapshot trước/sau; mọi fixture là synthetic; đây là outline, không thêm TC.
- [ ] GET menu/plan/kết quả vận hành không tạo Calculation, plan, receipt hoặc commit nghiệp vụ; không Idempotency-Key/retry lệnh ghi.
- [ ] Worker/service không mở UI; PORT-REM gửi nhắc tách GET reminder-runs theo dõi; GET không enqueue/retry job.
- [ ] TC-E6-019-1/3 tách producer rồi read trong cùng ca; đọc không publish/ack/start-production; đối chiếu revision ở cả hai giai đoạn.
- [ ] GATE-046/047 không nhận profile/consent, thu sức khỏe hoặc chạy thuật toán; grant A synthetic không quyết scope toàn tài khoản.
- [ ] Khi lập run, đối chiếu thêm [12 INV](invariant-cases.md) và [8 DR](decision-review-cases.md);99mô tả có overlap, không cộng thành99mục tiêu độc lập. Không đổi status vì review tài liệu.
