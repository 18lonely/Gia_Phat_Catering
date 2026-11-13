---
id: DOC-CHON-MON-ORDER-TEST-TEST-CASES
title: Ca kiểm trọng yếu E6
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ca kiểm trọng yếu E6

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |
| 0.1.1 | 2026-11-12 | BA | DOCUMENT_CLARIFIED: ranh giới thực thi/evidence; giữ mã và trạng thái |

Bộ10 ca trọng yếu ban đầu, chưa đủ19story. Mọi dữ liệu minh họa là synthetic, chưa chạy phần mềm. Actual/Evidence chưa có.

| TC | FR | Given | When | Then | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TC-E6-SEL-01 | FR-ORD-SEL-001 | eaterE1 chọnA ở version1, trước deadline | người ăn PUT API-ORD-002 đổi sangB version1 rồi replay cùng key/body | version2; counterA giảm1,B tăng1; replay không tăng lầnhai | NOT RUN |
| TC-E6-SEL-02 | FR-ORD-SEL-001 | tổ hợp giá bằng định mức | tăng giá tổng vượt1đ và gọi chọn | 422 ERR-ORD-422-01; selection/counter không đổi | BLOCKED ORD-Q04 |
| TC-E6-SEL-03 | FR-ORD-SEL-001 | hai writer cùngversion1 và scheduler đếndeadline | chạy đồng thời3 tác vụ, ghi thứ tự commit | không write sau LOCKED; writer thua409; tổngcounter=snapshot hợp lệ | BLOCKED Q-16/ORD-Q07 |
| TC-E6-SUB-01 | FR-ORD-SUB-001 | S=60,C=10,T=100 | người đặt tổng POST API-ORD-004; sau đó scheduler/service principal gọi PORT-LOCK với defaultA hợp lệ | POST chỉ SUBMITTED; khi khóa đủ điều kiện D=30,MAIN tổng100 trong cùng transaction UC010/011; không tạo30eater giả | BLOCKED ORD-Q06 |
| TC-E6-SUB-02 | FR-ORD-SUB-001 | S=60,C=10,T=65 | gửi tổng | 422 ERR-ORD-422-02; không xóa5 lựa chọn | BLOCKED ORD-Q06 |
| TC-E6-DEF-01 | FR-ORD-DEF-001 | chưa có total hoặc default không còn hợp lệ | scheduler/service principal gọi PORT-LOCK theo lịch, không mở UI | ERR-ORD-422-03; không coi total=registered eaters | BLOCKED ORD-Q07 |
| TC-E6-CHG-01 | FR-ORD-CHG-001 | orderLOCKED revision1 | gửi delta rồi người tạo tự duyệt | giữ revision1; tựduyệt403; không đổi plan trước người khác duyệt | BLOCKED Q-16/O-06 |
| TC-E6-SEC-01 | FR-NUTR-DSP-001 | menu A công bố; principal thử nghiệm có quyền A, không có quyền B | người ăn GET API-ORD-001 trong A rồi yêu cầu scope B | DTO khôngcost/giá nhập; ngoài scope404; GET không tạo Calculation/receipt hoặc commit nghiệp vụ | NOT RUN |
| TC-E6-QR-01 | FR-AUTH-QSES-001 | hai thiết bị cùng người quaQR | gửi hai lựa chọn | expected cụ thể chỉ được chốt sau ORD-Q01; không tuyên bố cookie đã chống trùng | BLOCKED ORD-Q01 |
| TC-E6-PLAN-01 | FR-PLAN-MEAL-001 | hai event cùng order revision đã khóa | redeliver cảhai tới worker/service principal; lưu event/source refs và snapshot trước/sau | một hiệu ứng plan; snapshot nguồn và delta giữ version | BLOCKED ORD-Q10 |

## Hướng dẫn thực thi đã đối chiếu ngày 12/11/2026

Áp dụng [evidence protocol](evidence-protocol.md), [catalog](../api/endpoint-catalog.json), [UC](../review/uc-operation-review.md) và [AC](../userstories/acceptance-criteria.md). Đây là DOCUMENT_CLARIFIED, không evidence chạy backend.

- SEL-03, SUB-01 và DEF-01: scheduler dùng service principal; UC010/011 cùng PORT-LOCK, cùng eventKey và một transaction khóa/default/revision/audit/receipt/outbox theo contract. Không có lần khóa thứ hai; eventKey không là Idempotency-Key HTTP. Với SUB-01 lưu evidence POST và khóa riêng trong cùng mã ca; summaryVersion khác order version. Plan có thể chưa có sau khóa.
- PLAN-01: kiểm producer từ event đã commit; không dùng GET để tạo plan. Nếu đọc kiểm kết quả, bếp dùng principal riêng GET020/025, lưu evidence read trước/sau riêng và nối source/plan revision trong cùng caseId. GET không publish/ack/start-production.
- SEC-01: quyền A/không B là fixture synthetic của lần thử, không chốt tài khoản chỉ thuộc một công ty. GET không dùng Idempotency-Key; đọc lại không là replay lệnh ghi.
- Mọi bước ghi actor/principal, trigger, quyền/scope, dữ liệu trước/sau và artifactRefs theo protocol; quyền seed/đọc evidence tách quyền nghiệp vụ. Không tự thêm route tra receipt, retry/retention, envelope hoặc policy.
- Expected phụ thuộc ORD-Q/Q-16/O-06 vẫn là thiết kế có điều kiện; giữ nguyên BLOCKED. SEL-02, SEL-03, SUB-02, CHG-01, QR-01 không có mâu thuẫn cần sửa Given/When/Then; áp dụng hướng dẫn chung trên. Mock/viewport/kiểm tài liệu không chứng minh backend, quyền, transaction hoặc nghiệm thu.
