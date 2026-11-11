# Bộ mẫu QA synthetic E6

11/11/2026 · Chỉ dùng review/seed môi trường test qua adapter; không dữ liệu khách/người ăn thật, không payload API đã duyệt, không thay dữ liệu kế toán10món/10ngày.

[JSON mẫu](consistency-synthetic.json) cố ý dùng các version khác nhau: summary41, order8, order revision2, plan5 để phát hiện nhầm token. MemberRef là khóa logic synthetic, không phê duyệt khóa định danh. Mỗi biến thể chạy trên bản sao độc lập, không cộng dồn kết quả giữa các ca.

| Nhóm | Setup / oracle review | Evidence phải thu khi có môi trường |
| :--- | :--- | :--- |
| Scope | Actor test chỉ được cấp scope đầu; scope khác dùng negative test; không mặc định mọi coordinator chỉ1khách | Quyền lúc ghi, response đã che dữ liệu, audit an toàn |
| Counter |2selection, mỗi món1; counterMismatch cố ý lệch | Snapshot trước/sau, transaction trace; không khóa khi lệch |
| Version | Gửi summary40 thay41; giữ order8 không đổi |409-01 và không mutation; không nhầm order8 là summary token |
| Snapshot | Order revision2 đã commit; plan5 dùng A2+B1=100 | Bản cũ nguyên vẹn; A3 thay A2→105, không165 |
| Completeness |3điểm kỳ vọng,2điểm có revision,1điểm thiếu | Không ghi đủ nguồn bằng2/2; thiếu tập kỳ vọng→UNKNOWN |
| Retry HTTP | BEFORE_COMMIT và AFTER_COMMIT_BEFORE_RESPONSE là hai biến thể độc lập; key/body chỉ cho mutation HTTP theo route | Trước commit: rollback; sau commit mất response: replay kết quả đã commit, khác body409-02; reset và evidence riêng theo hướng dẫn dưới |
| Phục hồi worker | AFTER_OUTBOX_BEFORE_PLAN: order/outbox đã commit, worker chưa tạo plan; redeliver event nguồn | Order vẫn LOCKED; một hiệu ứng plan; không dùng key/body HTTP làm event identity hoặc tạo revision mới vì retry |
| Policy | Ba scenario BLOCKED riêng trong JSON | Không chạy expected chặn/nhận/C→S/multi-company như đã duyệt |

## Checklist chuẩn bị QA

- [ ] Duyệt adapter fixture với mapping trường/version; seed chỉ test, không credential thật.
- [ ] Ghi build/config/DB/worker version, clock/timezone, quyền actor và reset từng scenario.
- [ ] Thu requestId/latency và snapshot trước/sau; key/receipt chỉ khi áp dụng cho lệnh ghi, eventKey/eventId cho worker; source revision/manifest theo ca. GET không đòi key/receipt. Theo [evidence protocol](../evidence-protocol.md).
- [ ] Đối chiếu response ghi thành công với dữ liệu commit; GET đối chiếu nguồn và không mutation nghiệp vụ; timeout là UNKNOWN, không tự ghi FAIL nghiệp vụ hoặc PASS.
- [ ] Ghi Actual/Evidence cho từng ca; chưa có môi trường thì giữ NOT RUN hoặc BLOCKED theo policy.

## Profile tải1000CCU — phương án QA chưa duyệt/chưa chạy

Chuẩn bị1000principal synthetic đã bind trong môi trường test, chia500/500 giữa2khách; đây là phân bố test, không chốt scope người đặt tổng. Ramp5phút rồi giữ1000session đồng thời trong10phút trước hạn giả lập, cooldown2phút. Hạn giả lập phải gắn scenario/config version, không coi là cutoff vận hành.

Vòng thao tác đề xuất:70%đọc menu/selection,20%chọn mới,10%đổi món; think time ngẫu nhiên2–5giây. Tiêm mất phản hồi vào5%write để retry cùng key/body, thống kê retry riêng ngoài tỷ lệ thao tác gốc. Tải timeout/lỗi phụ thuộc chạy lượt riêng, không trộn p95 thành công với lượt fault để che độ trễ/lỗi. Tránh C→S/vượt T bằng setup chưa gửi T và danh tính synthetic đã bind; không coi setup đó là phê duyệt ORD-Q13. Lượt deadline race riêng vẫn BLOCKED biên hạn.

Đo CCU thực tế, arrival/completion rate và TPS đạt được, không quy đổi1000CCU thành1000TPS. Báo p95 đọc≤300ms/ghi≤800ms theo NFR-ORD-001, tỷ lệ lỗi theo loại, latency timeout riêng,0 lựa chọn thành công mất/trùng qua đối soát. Không tự đặt SLA tỷ lệ lỗi chưa duyệt. Cần QA xác nhận profile, cấu hình máy/DB/network và policy để chạy; TC-E6-SYS-01 vẫn BLOCKED. Pilot2khách/2tuần cần dữ liệu và người dùng thật, fixture này không chứng minh pilot đạt.

## Fixture delta theo định lượng

[delta-synthetic.json](delta-synthetic.json) là mẫu logic review, không payload ghi API: tổng baseline/target đều100 nhưng thay recipe tạo delta-60/+60. Cùng dishId có2dòng làm request dish-only mơ hồ; mixedUnits cố ý chứa suất/g để phát hiện phép cộng sai. Không phải test backend hoặc quyết định hỗ trợ nhiều MAIN; không tăng inventory99ca.

## Review adapter — 11/11/2026

[adapter-synthetic.json](adapter-synthetic.json) gồm6biến thể oracle (không phải6ca mới) cho SYS-05/09 và AC-E6-016: zero,missing,timeout,scope,allergen unknown,list rỗng. Trường source cố ý có chi tiết nội bộ synthetic; expected không được copy chúng. Chưa chạy projection/backend.

## Đối chiếu fixture với 22 ca — 12/11/2026

DOCUMENT_CLARIFIED. Đã đọc 4/4 file trong thư mục: README và 3 JSON. JSON là mẫu logic/oracle rời, không phải một database seed nhất quán hoặc payload thực thi đầy đủ; không dùng summary có 2 selection để chứng minh plan 100 suất hay S=60 của ca khác. Không cần sửa 3 JSON: số học, version tách biệt và oracle adapter hiện tại phù hợp mục đích đã ghi. Không thêm ca/fixture; Status/Actual/Evidence của các bộ ca giữ nguyên.

Căn cứ: [10 ca gốc](../test-cases.md), [12 ca hệ thống](../system-test-cases.md), [protocol](../evidence-protocol.md), [SRS](../../srs/spec.md), [quy tắc](../../srs/operational-rules.md), [API](../../api/api-spec.md), [catalog](../../api/endpoint-catalog.json), [UC](../../review/uc-operation-review.md), [AC](../../userstories/acceptance-criteria.md) và [adapter](../../api/adapter-contract-review.md). CG bên dưới là các mục E6-CG hiện có trong [sổ gap duy nhất](../../review/contract-gap-register.md), không gap mới.

### Phạm vi dùng cho từng ca

Tên ca trong bảng là hậu tố của TC-E6-. “Một phần” chỉ khả năng dùng mẫu để review, không tỷ lệ sẵn sàng chạy backend. Thiếu setup thực thi không phải lý do ép JSON số học thành seed đầy đủ.

| Ca hiện có | Fixture/oracle áp dụng và giới hạn tiền điều kiện |
| :--- | :--- |
| SEL-01 | consistency.selections/counters minh họa đổi và đối soát; selection đầu version3 không phải Given version1 của ca. Khi có môi trường, chuẩn bị baseline riêng đúng ca; không gửi nguyên JSON làm PUT. CG01/04 |
| SEL-02 | Không có fixture giá tổ hợp/quota; lấy điều kiện bằng định mức rồi vượt1đ từ ca/SRS. Không suy từ qty hoặc nutrition; CG10/11 và ORD-Q04 |
| SEL-03 | consistency.counterMismatch/version chỉ hỗ trợ oracle; không có writer/scheduler/clock runtime. Cần thứ tự commit, biên hạn vẫn CG04/05 |
| SUB-01 | summary.total=null không là setup S60/C10/T100; ca dùng setup riêng đã nêu. POST SUBMITTED rồi PORT-LOCK, D30 chỉ có điều kiện CG03/05; không lấy plan.qty thay T |
| SUB-02 | policyScenarios.EXCEEDS_T ghi chặn, không dữ liệu seed T65 hoặc quyết định xử lý; CG03 |
| DEF-01 | missingSourceVariants TOTAL_NULL/DEFAULT_MISSING là nhãn biến thể, không payload null/default đã duyệt. Một PORT-LOCK; CG05/11 |
| CHG-01 | order/delta hỗ trợ snapshot và định danh dòng; không có grant người tạo/người duyệt. Tự duyệt bị từ chối, không đổi plan; CG05/07 |
| SEC-01 | scope/otherScope + adapter.out_of_scope hỗ trợ negative oracle; phải chuẩn bị menu PUBLISHED và principal quyền A/không B. Không có credential/grant runtime; CG01/02/09/10 |
| QR-01 | memberRef không là proof/binding hoặc credential; không có fixture chứng minh hai thiết bị cùng người. Giữ chặn CG01 |
| PLAN-01 | plan.sources/planReplacement hỗ trợ oracle revision; chưa có event runtime trùng. Worker nhận cùng revision nguồn, GET chỉ đọc; CG04/06/07 |
| SYS-01 | Profile1000CCU ở trên chỉ phương án chưa duyệt; JSON không có1000identity. GET không key, PUT replay riêng; CG01/04/14 |
| SYS-02 | counter/version hỗ trợ đối soát; thiếu lịch/clock/transaction runtime, không chứng minh race. Cùng PORT-LOCK của UC010/011; CG04/05 |
| SYS-03 | retry.stages AFTER_OUTBOX_BEFORE_PLAN hỗ trợ điểm fault; order/outbox đã commit rồi worker tạo plan. Không chứng minh publish/completeness; CG04/06 |
| SYS-04 | plan A2+B1→A3+B1=105 minh họa thay nguồn, không đúng setup A2/B2 đồng thời và A1 đến muộn của ca. Cần baseline sự kiện riêng theo ca; không đổi JSON thành lịch sự kiện; CG06 |
| SYS-05 | scope/otherScope + adapter.out_of_scope chỉ oracle; cần grant, guest/day và request scope thực tế. Scope A không quyết toàn tài khoản; CG01/02/09 |
| SYS-06 | missingSourceVariants.MENU_WITHDRAWN chỉ nhãn; cần source/version trước GET và sau thu hồi trước PUT/lock. Không dùng missing NUTR thay MENU thu hồi; CG05/10 |
| SYS-07 | BEFORE_COMMIT hỗ trợ vị trí fault audit khi POST022; cần người duyệt hợp lệ khác người tạo và snapshot order/approval/outbox. Không dùng replay đã commit để chứng minh rollback; CG04/05 |
| SYS-08 | Không có fixture eligibility/provider/dedupe; dùng PORT-REM eventId rồi GET023 theo dõi riêng. Không tạo policy kênh/retention hoặc gửi thật; CG12 |
| SYS-09 | adapter.complete_zero/missing_source/dependency_timeout hỗ trợ oracle SafeDish; nguồn phải được chuẩn bị trước bởi principal được phép. Incomplete khác timeout/thiếu cache; CG09/10/11 |
| SYS-10 | order/delta chỉ tham chiếu revision, không có pricing snapshot/discount record. Không suy amountDue hoặc sửa Cost; CK-Q07, CG07/14 |
| SYS-11 | BEFORE_COMMIT và AFTER_COMMIT_BEFORE_RESPONSE là hai biến thể reset riêng; key/body chỉ PUT, quyền hiện tại vẫn kiểm lúc replay; CG04 |
| SYS-12 | Không có fixture thay pilot2khách2tuần; synthetic chỉ chuẩn bị đối soát, dữ liệu thật/môi trường vẫn chặn CG14 |

### Principal, nguồn và evidence theo biến thể

- Quyền A/không B là phân quyền synthetic của lần thử; không kết luận tài khoản chỉ thuộc một công ty. Tách principal người ăn, người đặt tổng, người duyệt, scheduler/worker, bếp và vận hành theo bước; quyền seed/đọc evidence không cấp quyền nghiệp vụ. Chưa có binding/grant hợp lệ thì ghi thiếu theo CG01/02/08, không tự tạo credential.
- consistency.summary.version=41 ánh xạ logic vào summaryVersion của submission; order.version=8, order.revisionNo=2 và plan.revisionNo=5 độc lập. capturedOrderVersion là alias logic, không tự thêm wire field. Các số này không thay version1/revision1 của Given ca. Snapshot/manifest phải ghi nguồn/version thực tế; chưa có tập E không suy COMPLETE (CG04/06/07).
- Với SYS-11, reset baseline riêng trước mỗi biến thể, ghi runId/caseId/variant + fixture hash/reset, quyền, snapshot trước/sau và thứ tự fault/commit. BEFORE_COMMIT: đối soát không ghi một phần trước replay; AFTER_COMMIT_BEFORE_RESPONSE: giữ receipt và dữ liệu đã commit trong cùng biến thể để replay cùng key/body, rồi khác body409-02. Không reset giữa commit và replay. SYS-07 tiêm fault audit trước commit tương tự; persistence/retention chưa chốt giữ CG04.
- retry.key/sameBodyHash/changedBodyHash là nhãn synthetic cho ghi HTTP; không có ý nghĩa credential hoặc event identity. AFTER_OUTBOX_BEFORE_PLAN cần snapshot order/outbox đã commit, giữ event nguồn để redeliver tới worker; không dùng Idempotency-Key HTTP. UC010/011 chung PORT-LOCK, eventKey và một transaction default/khóa/revision/audit/receipt/outbox, không khóa hai lần. Thiếu contract event/persistence giữ CG04/05.
- PLAN-01, SYS-03/04/07/12 khi có bước đọc plan: cùng caseId nhưng producer có event/commit/source/plan revision và snapshot riêng; bếp GET020/025 có principal/request/response và snapshot ngay trước/sau riêng. Correlation phân biệt mutation nền; thiếu quan sát ghi INCONCLUSIVE cho lần chạy. GET không tạo plan/publish/ack/start-production (CG06).
- SYS-08: PORT-REM dùng eventId, eligibility và outcome/provider result; vận hành GET023 reminder-runs chỉ theo dõi với evidence riêng. GET không enqueue/gửi lại; chưa có fixture runtime không tự tạo kênh/retry/retention (CG12).
- Mọi GET không tạo Calculation/plan/receipt hoặc commit nghiệp vụ, không dùng Idempotency-Key; key/receipt ghi N/A có lý do theo protocol. Không lấy response200 hay ảnh mock làm bằng chứng không mutation.
- adapter.missing_source là incomplete đã xác định: cả4chỉ số null + missing an toàn; complete_zero giữ0thật, không tổng một phần. dependency_timeout là oracle503 đề xuất hiện có, không thiếu nguyên liệu; thiếu cache không chứng minh incomplete. Source/version, kind/freshness/nullability và envelope chưa chốt giữ CG09/10/11, không suy pageSize20 là default. Đây là các fragment oracle, không SafeDish response đầy đủ; không thêm field totals hay provenance giả.

GATE-046/047 không có ca riêng trong22ca; giữ bộ57ca/protocol, không thêm fixture profile/consent, thu sức khỏe hoặc chạy thuật toán. Các điểm mở E6-EVID-001/002, Cost/VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002 và O-02/O-03 giữ nguyên.
