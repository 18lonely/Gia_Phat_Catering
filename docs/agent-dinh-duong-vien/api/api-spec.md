# API và allowlist công cụ: AIN E9

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E9-Q13 |


Draft · 12/11/2026 · Đề xuất để review, chưa freeze/triển khai; không gọi AI.

## Quy ước và ranh giới

[Catalog](endpoint-catalog.json) gồm 11 HTTP endpoint và 4 control port nội bộ. Không có endpoint ghi hồ sơ/gợi ý cá nhân hoặc áp dụng thực đơn. `GET personal-availability` chỉ trả gate đóng; không nhận body sức khỏe. Tên quyền AIN là đề xuất, không phải quyền đã được cấp. Nhóm người dùng lấy từ cơ chế xác minh server được duyệt E9-Q02, không lấy từ body hoặc chỉ từ IP.

HTTPS theo E1; ID opaque/string, không mất precision bigint; timestamp UTC ISO8601, ngày phục vụ theo lịch được duyệt; ngày ngân sách/múi giờ chờ E9-Q07. Envelope đề xuất kế thừa AIO `{success,data,error,meta:{requestId},timestamp}`; khác biệt nguồn E4 phải có adapter, không tuyên bố contract thống nhất đã freeze. Decimal biểu diễn chuỗi; không NaN/Infinity; không nhận field lạ. `fields` trong lỗi chỉ tên trường được phép, không echo giá trị. Lỗi [ma trận](../srs/error-matrix.md) áp theo điều kiện, không phải mọi route đều phát mọi lỗi.

Mọi lệnh ghi cần idempotency scope=(chủ thể đã xác minh, route, key), bodyHash; cùng key/body trả resource gốc theo quyền hiện tại, khác body trả409. Key/TTL/receipt lưu ở đâu chờ E9-Q13, không đặt số mặc định. Đang xử lý trả trạng thái hiện tại, không tự tạo run thứ hai. PUT dùng version, không ghi đè; sau mất response GET đối soát. GET không sinh candidate, không gọi provider hoặc validator. HTTP200 với run FAILED không là generation thành công. Cookie nếu được chọn cần CSRF; secret không vào browser.

## DTO đề xuất

| DTO | Trường được phép / ràng buộc | Không nhận / gate |
| :--- | :--- | :--- |
| SessionInput | channelRef; identityProof/consentVersion theo policy đã duyệt | Không tự gán userId/group/role; guest mechanism E9-Q02/10 |
| MenuRequest | sessionRef; publicMealTypeRef; servings nguyên dương; weekStart/serviceDays; tasteOptionIds; exclusionOptionIds; requestText sau lọc và giới hạn được duyệt | Giới hạn độ dài/số suất/ngày chờ Q03/12/13; không nhận healthProfile, bệnh, mục tiêu điều trị, costThreshold, model, toolName |
| RevisionInput | baseCandidateRef, baseRevision, instruction giới hạn; ngày/slot cần đổi | Không client-supplied VALID/checkResult; không đổi scope bằng text |
| SafeRun | id, status, outcome, createdAt, revision; candidate hoặc null; safeQuestions; safeError | Không prompt/tool raw, tokens, model credentials, giá nội bộ; deadline policy Q13 |
| SafeCandidate | opaqueRef, revision, hash; days/items: publicDishRef, recipeRevisionRef, slot, displayName, portion từ hệ thống; safeCheck; safeNutrition; allergenStatus/labels; sourceVersions | Chỉ nguồn đã duyệt/public. Không raw recipe JSON, recipe cost, cost rule ID/detail/threshold/score có thể suy cost |
| SafeCheck | candidateHash, checkedAt, ruleSetRef opaque; hardRulesSatisfied; publicRules: code/label/pass/warning đã được phép | Lọc cả mã/tên/thông số của quy tắc kinh tế; bảng kiểm đầy đủ ở biên tin cậy, model chỉ nhận public-safe projection; không chia số rule theo loại nhạy cảm |
| SafeNutrition | kcal, proteinG, fatG, carbG; unit; label="ước tính từ định lượng sống"; sourceRefs; status AVAILABLE/MISSING/STALE | Thiếu thì totals=null, không 0; không mục tiêu sức khỏe, không tự tính; recipeId cụ thể, không suy cỡ O-02 |
| ExplanationInput | candidateRef, revision, topic thuộc allowlist đã duyệt | Không yêu cầu trả chain/tool/raw context; giải thích phải bám evidence |
| ProposalInput | candidateRef/revision, channel/source, contact theo Q06, consentVersion, clientConfirmation | Không nội dung candidate tùy ý hoặc menuId/orderId tự cấp; trường liên hệ cụ thể chờ Q06/10 |
| ProposalReceipt | proposalRef, acceptedAt, candidateRef/revision, safeStatus, sourceRef | Chỉ sau lưu bền vững; không trả leadId CRM khi chưa receipt đầu nhận |
| LimitChange | groupRef, version, limitCount, countWindow, dailyCap, costUnit, dayTimezone, effectiveAt, reason | Tất cả giá trị/chính sách chưa chọn Q07/08; không có default/token price |
| UsageLedgerSummary | policyVersion, dayKey, groupRef, spentConfirmed, reservedOutstanding, unknownCount, unit, reconciliationState | Chỉ quyền quản trị FEAT-064, không cho model/khách; chi phí AI khác cost nguyên liệu; không raw conversation |

Giá suất: **chưa có trường price trong projection mặc định**. Chỉ bổ sung sau E9-Q04/E8-Q03 có quyết định nguồn/hiệu lực/nhãn; `meal_types.price_cap_vnd` không là giá bán. Không suy giá nhập/cost từ giá suất, ngay cả sau khi được hiển thị giá công khai.

## Allowlist model-callable: đề xuất, mặc định từ chối ngoài danh mục

| Tool | Input được phép | Output được phép | Điều kiện / side effect |
| :--- | :--- | :--- | :--- |
| ain.catalog.read | publicMealTypeRef, ngày phục vụ, optionIds đã chuẩn hóa; scope do server gắn | món/công thức hiệu lực đã duyệt/public, định lượng được phép, dị ứng có trạng thái nguồn | Chỉ đọc projection E2; không SELECT rộng; Q03/12 |
| ain.menu.validateDraft | candidateRef/hash, revision; server lấy nội dung canonical | SafeCheck trên đúng hash/nguồn | Adapter FR-MENU-RUL-002 không ghi MENU; không trả rule cost chi tiết; mọi revision phải kiểm |
| ain.nutrition.readOrCalculate | candidateRef/hash, tổ hợp món tường minh, ngày | SafeNutrition/provenance đã lọc | Phép tính thuộc E4, không model tự cộng; không tạo MENU để ép vừa API; adapter candidate chưa lưu chờ Q11/12/13 |

Ba tool trên chỉ được bật khi policy/nguồn đủ và quyền giao hợp lệ. Đối tượng được đọc phải do adapter kiểm lại, không tin ref do model tạo. Không có tool tự gửi nháp: FEAT-062 là lệnh UI có xác nhận của khách qua API-AIN-006, do ứng dụng kiểm và ghi. Không có tool lấy usage/quota chi tiết hoặc log quản trị; control plane tự kiểm trước mỗi bước có chi phí.

## Control port: không model-callable

| Port | Người gọi / trách nhiệm | Hợp đồng tối thiểu |
| :--- | :--- | :--- |
| PORT-AIN-ADMISSION | Orchestrator trước nhận lượt và bước tính phí | principal/group đã xác minh, policyVersion, requestKey, upperBound → reservationRef/decision; không trả số nội bộ cho khách |
| PORT-AIN-TOOL-GUARD | Registry/API adapter trước mọi tool và trước serialize | toolName canonical + scope + candidateRef → allow/deny; xử lý projection trước model, lọc lỗi; không tin câu lệnh trong text |
| PORT-AIN-SAFETY | Biên tiếp nhận và xuất trả lời | Không thu hồ sơ; phát hiện ngoài phạm vi chuyển từ chối; nội dung nhắc chờ E9-Q09; dữ liệu thô sức khỏe không được lưu/chuyển provider |
| PORT-AIN-HANDOFF | Ứng dụng sau lệnh gửi và lưu đề xuất | proposalRef, source, candidateRef/revision/hash, contact/consent được duyệt → receiptRef của đầu nhận hoặc pending/error; nơi nhận Q06, không CRM CRUD |

PORT-AIN-HANDOFF là điểm nối tối thiểu thuộc FR-AIN-SEND-001, bổ sung cho ba port ADMISSION, TOOL-GUARD, SAFETY có dòng FR trực tiếp. Không coi port là HTTP đã chạy.

## Công cụ và dữ liệu bị cấm

- Không `cost.validate`, API-COST-025/036 trực tiếp cho model, price/cost lookup, estimate, allowance, discount, SQL/query builder, shell, arbitrary HTTP/URL, browser/search, export/log dump hoặc proxy AIO. Không gọi `menu.applyDraft`, duyệt/công bố MENU, tạo order/báo giá/hợp đồng, CRM CRUD.
- Không đọc TableGroup cost hoặc extension kế toán: giá nhập/NCC, costAmount/costPct, threshold/margin suy cost, khoản khoán, dự toán, customer_price_terms, order_pricing_snapshots, order_discount_records/events. Không đọc log AIO có request_text/tool_calls/result_summary/cost; không đọc health profile.
- Cấm cả bản chụp/JSON lồng nhau/error/detail/stack/log/cache/metadata/giải thích/URL và dữ liệu của khách khác. Không dùng điều kiện UNION quyền của user để nới quyền tài khoản dịch vụ AIN. DB account không SELECT bảng cấm, kể cả tool registry bị đánh lừa.

Nếu kiểm quy tắc E2 cần cổng Cost nội bộ, E2/orchestrator tin cậy xử lý ngoài model. AIN không được nhận số, ratio, nguyên nhân cost hoặc nhãn phân biệt có thể dùng dò ngưỡng. Nhánh vượt ngưỡng/CANH_BAO giữ BLOCKED E9-Q05/AIO-Q02; không lấy endpoint cost-redacted hiện có làm giấy phép đọc và không thay nguyên tắc E3.

## Admission và quyết toán: invariant, chưa chọn policy

Trước phát sinh chi phí phải có upper bound thực sự cưỡng chế được cho bước đang nhận (bao gồm chi phí retry/tool phụ nếu provider tính). `confirmed + reservedOutstanding + proposedUpperBound ≤ cap` trong cùng ngày/policy. Không thể xác định/cưỡng chế upper bound thì **không nhận**; chỉ đối soát sau khi chạy không đủ bảo đảm R9. Khi phát sinh xác nhận, chuyển reserve sang confirmed một lần theo eventId; phần chưa rõ giữ chỗ. Timeout không đồng nghĩa provider không tính tiền. Rollover không xóa debt/reserve cũ; ngày hạch toán và xử lý xuyên ngày chờ Q07/13.

Sửa cap không hồi tố; cap mới thấp hơn committed/reserved chặn lượt mới và báo quản trị, không giả tạo hoàn tiền. Không chuyển sang queue/quota AIO hoặc đổi identity/key để vượt trần. Không chọn model, giá token, số lượt, ngân sách, concurrency, TTL hoặc số lần retry trong gói này.

## Quy ước tài liệu liên epic (XC-04)

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E9-Q13: XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
