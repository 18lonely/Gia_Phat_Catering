# Tiêu chí evidence QA — adapter, receipt và manifest E6

11/11/2026 · Mẫu chuẩn bị, chưa chạy backend/UAT. Bổ sung [12ca INV](invariant-cases.md), [fixture](fixtures/README.md) và [delta contract](../api/delta-contract-review.md); không thêm mã TC hoặc thay trạng thái ca cũ.

## Mẫu ghi cho mỗi lần chạy

| Trường | Giá trị cần ghi |
| :--- | :--- |
| runId / caseId / variant | Mã lần chạy riêng, mã TC hiện có, biến thể; không dùng requestId thay runId |
| environment | Build, adapter/config/policy version, DB/worker version, timezone/clock; thiếu giá trị ghi UNKNOWN |
| fixture / reset | File/hash synthetic, scope/version baseline, thao tác reset; không ghi danh tính thật/credential |
| execution | Thời điểm, actor test, quyền đã cấp, requestId, idempotency reference đã che dữ liệu nhạy cảm, thứ tự fault/commit |
| expected / actual | Expected từ phiên bản tài liệu; Actual chưa có thì để NOT RUN, không sao chép expected |
| artifactRefs | Response đã lọc, snapshot trước/sau, audit/receipt/outbox/manifest; hash và quyền truy cập cho từng artifact |
| conclusion | PASS/FAIL chỉ sau thực thi và đủ evidence; INCONCLUSIVE khi mất evidence; BLOCKED khi expected phụ thuộc policy chưa chọn |

Không lưu raw QR/token/password/health vào evidence hoặc dùng body hash như credential. Công cụ thu/retention/quyền đọc evidence cần môi trường và owner xác nhận; không đưa thời hạn tự đặt thay E1-Q02.

## Oracle và tập bằng chứng tối thiểu

| Miền / TC tham chiếu | Bằng chứng cần đối chiếu | Đủ để kết luận khi | Không đủ bằng chứng |
| :--- | :--- | :--- | :--- |
| Adapter / SYS-05/09, INV-04 | Input nội bộ synthetic có trường cấm; output success/error và log hiển thị; principal/scope | Chỉ allowlist; null/missing không thành0; không lộ dữ liệu scope khác; replay vẫn kiểm quyền hiện tại | HTTP200 hoặc ảnh màn hình không chứng minh không lộ trong JSON/error |
| Receipt / INV-03/06, SYS-03/11 | Cùng key/body, response cũ/mới, count revision/counter/audit/outbox trước-sau, thời điểm fault | Commit rồi replay cùng kết quả không mutation; trước commit rollback không một phần; body khác409-02; worker retry không mở lại order | Timeout không cho biết commit hay rollback; log “success” đơn lẻ không chứng minh transaction |
| Manifest / INV-07/08 | Expected source version; E/I/M/X; order revision IDs trong I; nguồn ngoài E; snapshot plan trước-sau | Các tập rời nhau và đầy đủ; missing có reason; thay nguồn không cộng cả revision cũ/mới; UNKNOWN không thành COMPLETE | sourceOrderCount=2 không chứng minh đầy đủ nếu chưa có E |
| Delta / INV-11 và AC-E6-019-3 | Baseline và target line keys, recipe/portion/role/unit, qty, delta, provenance | Không cộng khác đơn vị; thay recipe có hai dòng +/-; không mutate bản cũ | Chỉ tổng suất100=100 không chứng minh delta0 |
| Publish/ack/start / INV-09 | Read request và state trước/sau; event audit có actor/revision riêng nếu được phép | GET không tạo ack/start; publish không tự start; ack cũ không đổi thành ack bản mới | Nhãn READY hoặc in phiếu không chứng minh bếp đã nhận |

## Chạy khi chưa đủ policy

Có thể review số học/shape fixture và traceability ngay; đó là DOCUMENT_CHECK_ONLY. Chỉ chạy invariant trên môi trường test có cấu hình và tiền điều kiện rõ, không gọi đó là nghiệm thu policy. Ca C→S, vượt T và scope một/nhiều khách tiếp tục BLOCKED theo E6-EVID-002. Chưa có endpoint tra receipt bằng requestId: evidence lấy qua vận hành được cấp quyền hoặc retry endpoint đã có, không sáng tác route kiểm thử.

## Đối chiếu giới hạn demo hiện có

| Vùng đã đọc trong HTML | Giả lập hiện có | Phần demo không chứng minh |
| :--- | :--- | :--- |
| UI09 `lock` | Tạo plan ngay cùng thao tác in-memory | Worker chậm/lỗi, PENDING, atomic persistence hoặc completeness |
| UI10 `approve` | Dùng state.revision cho cả order và plan; tăng tổng món A | Các version độc lập, nhiều nguồn/recipe/portion hoặc delta từng dòng |
| UI13 `viewPlan` | Một order synthetic, nhãn hiện hành/bản cũ, chưa xác nhận bếp nhận | Tập nguồn kỳ vọng, publish/ack/start và chuyển bếp |
| UI06 `replay` | Guard stale trước replay mock | Thứ tự receipt đã commit trước stale-check của thao tác mới; authorize hiện tại |

Không sửa hành vi wireframe trong phiên này; các giới hạn trên phải đi cùng khi dùng screenshot/demo review. Test UI cũ chỉ xác minh mock/viewport, không được dùng làm Actual cho bộ INV hoặc contract cuối.

## Review adapter — 11/11/2026

Đối với [adapter review](../api/adapter-contract-review.md), lưu provenance đủ để đối chiếu kind DISH/MEAL, menu/recipe versions, ngày và source freshness trong artifact có quyền; không đưa raw breakdown vào response người ăn. Dùng [6oracle synthetic](fixtures/adapter-synthetic.json), Actual vẫn chưa có. Schema/expected kiểm được không chứng minh adapter đã lọc ở runtime.

## Bằng chứng theo loại thao tác — 12/11/2026

DOCUMENT_CLARIFIED. Dùng cùng caseId hiện có, không thêm ca hoặc đổi NOT RUN/BLOCKED. Đối chiếu [UC](../review/uc-operation-review.md), [catalog](../api/endpoint-catalog.json) và [hướng dẫn57ca](review-test-cases.md). Mọi dữ liệu minh họa/fixture là synthetic.

Mỗi bước ghi actor nghiệp vụ, principal thực thi (user/guest/service theo contract đã review), scope/quyền tại thời điểm chạy, trigger thực tế (request, lịch/event, mở màn gate), correlation tới bước trước và artifactRefs. Ghi N/A có lý do cho key/receipt không áp dụng; UNKNOWN khi chưa biết, không tạo giá trị thay thế. Quyền seed/đọc evidence không được coi là quyền actor nghiệp vụ; binding/principal còn thiếu giữ chặn theo CG01/04/08.

| Loại / ca tham chiếu | Trigger và principal | Trước → sau cần đối chiếu | Evidence tối thiểu khi có môi trường |
| :--- | :--- | :--- | :--- |
| GET; TC-E6-016,019, nhánh đọc001/004/005/006/007/009/012/013 | User/guest/bếp đúng route/scope gửi GET; không Idempotency-Key | Snapshot nguồn/version và dữ liệu nghiệp vụ trước/sau: không tạo Calculation/plan/receipt hoặc commit nghiệp vụ | Request/response đã lọc + provenance/source refs + quan sát mutation có quyền. Log truy cập kỹ thuật không là commit nghiệp vụ; HTTP200 đơn lẻ không đủ |
| Ghi HTTP; các TC có POST/PUT/PATCH theo UC | Actor gửi lệnh; key/version chỉ khi route yêu cầu | Resource/version/counter/audit/receipt/outbox liên quan; ghi bị từ chối không mutation một phần | Request/response, quyền lúc ghi, transaction/receipt refs; fault trước/sau commit và replay theo contract; không đòi mọi route có cùng loại dữ liệu |
| PORT-LOCK; TC-E6-010/011, INV05/06/10 | Scheduler/service principal, lịch và eventKey cùng scope | T/default/nguồn/counter → một revision khóa + audit/receipt/outbox; default trong cùng transaction; plan có thể chưa có | Event input/outcome, commit refs và số revision trước/sau; retry không thành lần khóa thứ hai. Khi dùng cùng run cho010/011, tham chiếu chung event/commit, không cộng hai lần |
| Producer plan; giai đoạn đầu TC-E6-019-1/3, INV07/08/11 | Worker/service principal xử lý event từ nguồn đã commit | Revision nguồn, manifest và plan trước → snapshot/delta mới theo contract; bản cũ nguyên vẹn | Event/source refs, worker outcome, manifest và plan revision; chưa có E thì không suy COMPLETE |
| PORT-REM; nhánh gửi TC-E6-014 | Scheduler/service principal theo lịch nhắc, eventId | Eligibility/dedupe/outcome trước → kết quả attempt; không giả rollback provider | Event và provider result đã lọc nếu có; outcome nội bộ không tự chứng minh người nhận đã đọc; kênh/retention/retry chưa chốt giữ CG12 |
| Theo dõi vận hành; nhánh đọc011/014 | Vận hành có quyền gửi GET020/023 | Kết quả producer đã có hoặc chưa có → không enqueue, gửi lại hoặc retry job | Response + correlation tới event/outcome đã tạo trước; quan sát không có job mới do read. Job nền cạnh tranh phải phân biệt bằng correlation, không kết luận từ count tổng |
| Gate; TC-E6-017/018 | Người ăn mở GATE-046/047; không HTTP contract sức khỏe | Không có profile/consent đầu vào; không thay dữ liệu sức khỏe hoặc chạy thuật toán | Ảnh trạng thái gate + network/quan sát có quyền chứng minh không gửi dữ liệu sức khỏe; chỉ ảnh mock không chứng minh backend |

### Ca liên thông producer rồi read

Với TC-E6-019-1/3 giữ một ca và hai bước evidence: (1) worker nhận event, ghi outcome/source revision/plan revision cùng snapshot trước/sau; (2) bếp dùng principal riêng GET020/025, lưu response và snapshot ngay trước/sau read. Nối bằng plan/source revision đã quan sát, không giả order version bằng plan revision. Có thể kiểm riêng trạng thái chưa có plan theo contract hiện hành, không invent status/envelope hoặc timeout chờ worker. Publish/ack/start-production cần trigger, actor và evidence riêng khi policy được duyệt; GET không thay các bước đó.

Nếu có producer nền chạy trong khoảng đọc, ghi thứ tự/correlation để quy mutation về đúng trigger; không đủ quan sát thì INCONCLUSIVE cho lần chạy, không tự đổi status thiết kế ca. TC-E6-001-1 chỉ chứng minh grant scope A synthetic của yêu cầu, không chứng minh toàn tài khoản chỉ một công ty. Bộ ca phụ thuộc E6-EVID-002 tiếp tục BLOCKED. Evidence thu thực tế chưa có trong phiên này.
