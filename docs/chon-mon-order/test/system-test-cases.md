---
id: DOC-E6-TEST-SYSTEM-TEST-CASES
title: Ca hệ thống và tích hợp E6
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ca hệ thống và tích hợp E6

Draft · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.

Toàn bộ fixture synthetic; **Actual/Evidence: chưa có**. Các bước chạy cần môi trường backend và quyền đọc evidence test, không chạy trên dữ liệu thật. Mã NFR/BR/lỗi tham chiếu [SRS](../srs/spec.md) và [quy tắc chi tiết](../srs/operational-rules.md).

| TC | Truy vết | Tiền điều kiện / bước thực hiện | Expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-SYS-01 | NFR-ORD-001; FR-ORD-SEL-001 | Seed 1000 identity hợp lệ/2 khách; chạy GET đọc và PUT chọn/đổi trong10phút trước deadline; replay key/body chỉ cho PUT, đọc lại GET không Idempotency-Key; lưu response latency và đối chiếu DB | p95 đọc≤300ms/ghi≤800ms;0 lựa chọn thành công mất/trùng; không đồng nhất CCU với TPS | BLOCKED profile tải/ORD-Q01/Q-16/môi trường |
| TC-E6-SYS-02 | NFR-ORD-002; BR-ORD-002/004 | Hai PUT của người ăn cùng version + scheduler/service principal gọi PORT-LOCK cùng scope tại deadline; ghi thứ tự transaction | Một writer hợp lệ hoặc job thắng; không write sau guard khóa; sum counter=selection; snapshot một lần | BLOCKED ORD-Q07 |
| TC-E6-SYS-03 | NFR-ORD-002; PORT-LOCK | Crash sau commit order/outbox trước worker tạo plan; khởi động worker/service principal và replay event nguồn đã commit | Order vẫn LOCKED; plan được tạo một lần; không mở lại order hoặc tạo v2 do retry | NOT RUN |
| TC-E6-SYS-04 | BR-ORD-008; FR-PLAN-MEAL-001 | A rev2 và B rev2 phát đồng thời; replay A rev1 đến muộn | Plan giữ revision mới nhất của cả A/B; không lost update, không rollback bởi event cũ | BLOCKED ORD-Q10/14 |
| TC-E6-SYS-05 | NFR-ORD-003; BR-ORD-006 | Principal thử nghiệm có quyền A, không quyền B; đổi id/filter từ A sang B; thử guest/day khác; kiểm JSON,error và log hiển thị | 404/403 theo scope;0 cost,giá nhập,chiết khấu/PII ngoài quyền | NOT RUN |
| TC-E6-SYS-06 | BR-ORD-010; FR-ORD-SEL-001 | MENU WITHDRAWN sau GET trước PUT; thử lock order cũ | PUT409; không dùng nguồn thu hồi cho lock; lịch sử giữ, workflow xử lý chờ policy | BLOCKED ORD-Q12 |
| TC-E6-SYS-07 | BR-ORD-005; FR-ORD-CHG-001 | Lỗi ghi audit giữa approve; đọc order,approval,outbox | Rollback tất cả; không revision/plan giả thành công; retry cùng key đối soát | NOT RUN |
| TC-E6-SYS-08 | BR-ORD-012; FR-ORD-REM-001 | Scheduler/service principal gọi PORT-REM; người ăn chọn sau khi job lập recipient trước gửi; kênh tắt hoặc duplicate event; vận hành đọc GET API-ORD-023 với evidence riêng | Kiểm lại điều kiện trước gửi; không nhắc sai/không gửi khi kênh tắt; dedupe; GET chỉ theo dõi, không enqueue/gửi lại; không giả rollback provider | BLOCKED Q-14/E1-Q04 |
| TC-E6-SYS-09 | FR-NUTR-DSP-001; BR-ORD-006 | Nguồn NUTR synthetic đã chuẩn bị trước: incomplete hoặc có internal breakdown; người ăn GET API-ORD-001, adapter chiếu SafeDish; ghi source/provenance và snapshot trước/sau đọc | Khi incomplete, cả4chỉ số null + missing theo SafeDish (totals=null là mô tả AC, không thêm wire field); không suy0 hoặc coi timeout là thiếu nguồn; allowlist không lộ breakdown giá/cost; nhãn ước tính; GET không tạo Calculation/plan/receipt | NOT RUN |
| TC-E6-SYS-10 | FR-ORD-CHG-001; Cost CK-Q07 | Order đổi số suất sau khóa, có pricing snapshot và discount record synthetic | Giữ snapshot cũ; liên kết revision mới rõ; khoản chiết khấu cần review, không tự trừ amountDue | BLOCKED CK-Q07/ORD-Q08 |
| TC-E6-SYS-11 | FR-ORD-SEL-001; ERR-ORD-409-02/500-01 | PUT đã commit nhưng mất response; retry key/body cũ rồi key cũ/body khác, crash trước commit | Replay resource cũ; khác body409-02; trước commit không lưu dữ liệu một phần | NOT RUN |
| TC-E6-SYS-12 | R6 / FR-ORD-SUB-001/DEF-001/PLAN-MEAL-001 | Pilot2 khách2tuần; ghi tổng, lựa chọn, mặc định, khóa, thay đổi và phiếu bếp hàng ngày | 100% phần chưa chọn về default khi đủ điều kiện; vượt định mức bị chặn; đối chiếu nguồn/revision; exception không bị che | BLOCKED G-Now/dữ liệu thật/môi trường |

Phạm vi ba bộ này:57 ca theo AC +10 ca gốc +12 ca hệ thống = **79 mô tả test**, có overlap. Inventory hiện hành gồm thêm8DR +12INV = **99 mô tả ca có overlap**, không phải99 mục tiêu độc lập. Không có test backend đã chạy, không dùng kết quả kiểm HTML làm actual các ca trên.


## Hướng dẫn thực thi đã đối chiếu — 12/11/2026

DOCUMENT_CLARIFIED, v0.2.1. Dùng [evidence protocol](evidence-protocol.md), [API](../api/api-spec.md), [catalog](../api/endpoint-catalog.json), [UC](../review/uc-operation-review.md) và [AC](../userstories/acceptance-criteria.md); giữ12mã ca và Status/Actual/Evidence.

- SYS-01/05/09: GET không tạo Calculation, plan, receipt hoặc commit nghiệp vụ; không retry bằng Idempotency-Key. Nguồn cho SYS-09 do principal được phép chuẩn bị trước, không cấp người ăn quyền tính nội bộ; phần provenance/freshness còn mở theo CG10. Quyền A/không B ở SYS-05 là fixture synthetic, không policy toàn tài khoản.
- SYS-02/03/06: UC010/011 dùng một PORT-LOCK và một transaction khóa; scheduler/worker dùng service principal, không mở UI. Tách eventKey khóa, event nguồn của worker và key HTTP. SYS-03 kiểm phục hồi tạo plan, không chứng minh publish/ack/start hoặc đủ tập nguồn. Không đồng nhất order version, order revision và plan revision.
- SYS-03/04/07/12: nếu có đọc kế hoạch, giữ một caseId và hai phần evidence: producer có event/commit/source revision/manifest cùng snapshot trước/sau; bếp GET020/025 có principal và snapshot ngay trước/sau read riêng. Nối bằng revision đã quan sát; GET không tạo plan/publish/ack/start-production. Mutation nền cạnh tranh phải phân biệt bằng correlation; thiếu evidence ghi INCONCLUSIVE cho lần chạy.
- SYS-07: người duyệt hợp lệ khác người tạo gọi POST022; inject fault audit trước commit rồi đối soát rollback trước replay cùng key/body. Quyền đọc order/approval/outbox qua công cụ test được cấp không tạo thêm HTTP route. SYS-11 tách biến thể đã commit/mất phản hồi và crash trước commit, reset baseline và lưu evidence riêng dưới cùng caseId. Replay vẫn kiểm quyền hiện tại.
- SYS-08: lưu eventId, eligibility và outcome/provider result của PORT-REM riêng với request/response GET023 của vận hành; đọc không kích hoạt job. Kênh, retry/retention còn chờ CG12; không gửi thông báo thật trong phiên BA.
- SYS-12: kế hoạch pilot vẫn cần dữ liệu thật và môi trường được phép; synthetic chỉ chuẩn bị, không thay bằng chứng pilot. Bước producer và đọc phiếu bếp tách evidence, không đồng nhất xem/in với bếp đã nhận.
- Không có ca gate sức khỏe trong22ca này, không thêm ca trùng: tham chiếu bộ57ca và protocol. GATE-046/047 không nhận profile/consent, không thu sức khỏe/chạy thuật toán.
- SYS-04/06/07/10/12 không cần đổi expected nghiệp vụ; hướng dẫn trên chỉ làm rõ thực thi. Giữ policy/gate mở và mọi Status; mock/viewport hay kiểm tài liệu không chứng minh backend, quyền, transaction hoặc nghiệm thu.
