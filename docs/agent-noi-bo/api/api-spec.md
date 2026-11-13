# Hợp đồng API và công cụ: Agent Nội bộ MVP

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

## Quy ước chung

Hợp đồng đề xuất v0.1, chưa có server chạy. Prefix `/v1` kế thừa Cost. HTTPS; phiên Bearer từ AUTH, không đưa token vào log; nếu triển khai cookie phải có CSRF theo nền tảng. `Content-Type: application/json`; `X-Request-Id` để truy vết; id là chuỗi số nguyên dương để không mất precision bigint; ngày `YYYY-MM-DD` theo Asia/Ho_Chi_Minh, thời điểm UTC ISO 8601.

Response chuẩn: `{success:true,data:...,error:null,meta:{requestId},timestamp}`; lỗi `{success:false,data:null,error:{code,message,fields:[{field,reason}]},meta:{requestId},timestamp}`. Số decimal biểu diễn bằng chuỗi dấu chấm, không dấu phân cách nghìn; totals không có NaN/Infinity. Từ chối field ngoài schema. Response list có `items,nextCursor`; limit mặc định 20, tối đa 100 **đề xuất**; cursor opaque gắn filter/scope; không tin cursor để bỏ kiểm quyền. Sort ổn định theo id; log sort created_at/id giảm dần. 400 sai JSON/kiểu; 401 mất phiên; 403 thiếu quyền; 404 id ngoài scope/không tồn tại; 409 xung đột; 422 dữ liệu nghiệp vụ; 500 lỗi giao dịch; chi tiết mã ở SRS.

Mỗi POST ghi bền vững cần `Idempotency-Key` (chuỗi 16–128 ký tự **đề xuất**) scope=(user,route,key), hash body chuẩn hóa. Cùng body trả resource gốc theo quyền hiện tại; body khác 409; request đang xử lý trả 409 kèm Retry-After và resourceId nếu đã có. Đề xuất giữ key tối thiểu 24h, cần Tech lead review; hết hạn không chứng minh chưa ghi. Sổ key phải nằm trong kho bền vững/giao dịch cùng resource, không chỉ Redis TTL. Thiết kế dưới đây có cột request_key/request_hash và unique trong bảng đích; việc dọn key chưa được cho phép. PUT dùng version lạc quan; replay PUT sau mất phản hồi phải GET giá trị/version và revision để đối soát. Không tự retry lệnh bằng key mới khi chưa rõ kết quả.

Không có webhook công khai. Endpoint chỉ đọc hoặc kiểm độ phủ không gọi provider và không thay trạng thái MENU. Tất cả dữ liệu ví dụ dưới đây là **GIẢ ĐỊNH để review**, không phải dữ liệu thực tế Gia Phát.

## Kiểu dữ liệu

| Kiểu | Trường và ràng buộc |
| :--- | :--- |
| GenerateInput | mealTypeId:Id; weekStart:Date thứ Hai; kitchenIds:Id[1..n] không trùng, mỗi cơ sở trong scope; exclusions:{ingredientIds:Id[],dishIds:Id[]}; requestText:string1..4000 đề xuất; không nhận userId/role/status/cost do client tự gán |
| RevisionInput | instruction:string1..4000; đúng một trong {menuId,baseVersion:int≥1} hoặc {candidateRunId,candidateRevision:int≥1}; cấu hình cơ sở/tuần kế thừa nguồn, đổi scope cần yêu cầu mới |
| ApplyInput | candidateRevision:int≥1; baseVersion:int≥1 khi sửa menu hiện hữu, null khi tạo; không nhận nội dung candidate từ client |
| Run | id,status:QUEUED/RUNNING/DONE/FAILED/REJECTED; outcome:null/VALID/NEEDS_INPUT/NO_SOLUTION/BLOCKED_DATA/TIMEOUT/DEPENDENCY_ERROR; createdAt,deadlineAt,finishedAt?,questions:[],blockingReasons:[],candidate:null hoặc Candidate; error:null hoặc {code,message}; usageStatus:UNKNOWN/ESTIMATED/CONFIRMED |
| Candidate | revision:int; hash:string64; mealTypeId,weekStart,kitchenIds; days:[{date,defaultDishId,items:[{dishId,recipeId,slot,sortOrder}]}]; diff:[{date,slot,oldDishId,newDishId}]; evidence:{inputHash,menuRulesVersion,costInputVersions,checkedAt,ruleResults,costResults}; nutritionStatus:AVAILABLE/UNAVAILABLE, nutritionCalculationIds:Id[] |
| ruleResults[] | ruleId,severity,pass:boolean,scoreImpact,message; không cho model tự tạo pass |
| costResults[] | kitchenId,serviceDate,status,thresholdPct,mode,inputVersion; costPct/costAmount chỉ trả khi có cost.cost.read; nếu bị che vẫn trả pass và lý do không nhạy cảm từ COST |
| RunLog | Run metadata không tự kèm candidate; userId,agentCode,model,promptVersion,inputTokens?,outputTokens?,costVnd?:IntegerString,usageStatus,requestText đã lọc; pagination; tool detail dùng events theo quyền log |
| ToolEvent | runId,seq:int≥1,toolName,status,requestId,startedAt,finishedAt,summary,argumentHash,resultHash; arguments/result chỉ phần được phép và đã lọc; không lưu token bí mật |

## Danh mục endpoint

| ID | Method/path | Quyền | Request | Thành công / lỗi riêng | FR / UI |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-AIO-001 | POST /v1/internal-agent/runs | aio.run.create + MENU read scope + svc intersection | GenerateInput + key | 202 Run; retry cùng key trả 200 run gốc; 429 quota,503 queue,400 input | FR-AIO-GEN-001 / UI-AIO-01 |
| API-AIO-002 | GET /v1/internal-agent/runs/{id} | aio.run.read của mình hoặc aio.logs.read; vẫn check scope và field quyền cost | Không body | 200 Run; khi DONE không phải VALID thì candidate=null; 404 ngoài scope | FR-AIO-CHK-001 / UI-AIO-02 |
| API-AIO-003 | POST /v1/internal-agent/revisions | aio.run.create + quyền đọc nguồn | RevisionInput + key | 202 Run con có parentRunId nếu nguồn là candidate; không sửa menu;409 nguồn cũ | FR-AIO-EDIT-001 / UI-AIO-02 |
| API-AIO-004 | POST /v1/internal-agent/runs/{id}/applications | aio.apply + MENU write scope + svc intersection | ApplyInput + key | 201 {menuId,menuVersion,status:DRAFT,runId}; replay200;422 nếu không VALID;409 version/state/evidence đổi | FR-AIO-APLY-001 / UI-AIO-02 |
| API-AIO-005 | GET /v1/internal-agent/run-logs | aio.logs.read | from,to UTC; userId?,status?,cursor?,limit? | 200 List RunLog; không trả prompt/cost ngoài quyền | FR-AIO-LOG-001 / UI-AIO-03 |
| API-AIO-006 | GET /v1/internal-agent/runs/{id}/events | chủ run có aio.run.read hoặc aio.logs.read, scope hiện tại | cursor?,limit? | 200 List ToolEvent sort seq tăng; nextCursor; trạng thái run đi kèm; không SSE/webhook | FR-AIO-OPS-001 / UI-AIO-03 |

Poll đề xuất mỗi 2 giây, dừng khi terminal hoặc offline; Retry-After được ưu tiên. 60 giây là deadline toàn run, không phải timeout mỗi lần poll. HTTP200 cho run FAILED phản ánh truy vấn thành công, không phải generation thành công. Lỗi worker ghi `error.code=ERR-AIO-503-01` cho dependency; timeout ghi outcome TIMEOUT, không dùng HTTP504 cho GET đã thành công. Mã lỗi còn lại theo SRS, replay luôn kiểm quyền hiện tại. Nếu thu hồi quyền giữa run thì dừng tool tiếp theo, run REJECTED, không trả dữ liệu cũ.

## Hợp đồng công cụ nội bộ (port đề xuất, không phải endpoint MENU đã có)

| Tool / owner | Input | Output / side effect |
| :--- | :--- | :--- |
| catalog.read / MENU | effectiveDate,mealTypeId,scope,exclusions | Danh mục ACTIVE + recipeId có hiệu lực, nguyên liệu chính/phụ; chỉ đọc; không đưa đơn giá nhập nếu thiếu quyền |
| menu.validate / MENU | Candidate.days, mealTypeId, weekStart, inputHash | FR-MENU-RUL-002: kết quả theo ruleId và tuần/ngày, ruleSetVersion; không lưu MENU |
| cost.validate / COST | Adapter Candidate → MenuQuery, cùng ngày/cơ sở/clientRevision | [API-COST-025](../../cost/api/api-spec.md), POST /v1/cost/menu-calculations; trả MenuCost/Redacted; không tính bằng model; không được dùng API-COST-036 của agent khách |
| nutrition.calculate / NUTR | recipeId hoặc tổ hợp tường minh; serviceDate; key | API-NUTR-003/004; output có nhãn ước tính; không có dependency thì nutritionStatus=UNAVAILABLE, không tự điền số |
| menu.applyDraft / MENU + orchestrator | runId,candidateHash,baseVersion,actor,svc,scope | Server kiểm lại nguồn/evidence, khóa menu hoặc khóa duy nhất tuần, ghi toàn tuần DRAFT + audit + applied marker nguyên tử. Model không được trực tiếp gọi port này |

Port cost.validate phải dùng đúng MenuQuery trong Cost; adapter không sửa công thức, VAT hoặc chế độ. Bằng chứng đầu vào gắn cùng candidateHash; nếu validator không cung cấp version thì adapter phải chụp version đọc trong cùng consistent view, không tự tuyên bố fresh. AIO-Q06 chặn chốt transaction/locking/outbox, không chặn viết hợp đồng nháp.

## Ví dụ

```json
{"mealTypeId":"10","weekStart":"2026-11-16","kitchenIds":["1"],"exclusions":{"ingredientIds":["20"],"dishIds":[]},"requestText":"Dựng tuần, không dùng nguyên liệu 20"}
```

```json
{"success":true,"data":{"id":"501","status":"QUEUED","outcome":null,"candidate":null,"questions":[],"blockingReasons":[],"createdAt":"2026-11-11T03:00:00Z","deadlineAt":"2026-11-11T03:01:00Z","finishedAt":null,"error":null,"usageStatus":"UNKNOWN"},"error":null,"meta":{"requestId":"example-only"},"timestamp":"2026-11-11T03:00:00Z"}
```

Sau timeout GET vẫn HTTP200, data.status=FAILED, outcome=TIMEOUT, candidate=null. POST apply run đó trả422 ERR-AIO-422-01, không tạo menu. Các con số nguồn Cost giữ xác nhận VAT gồm phải trả NCC, hóa đơn là cờ riêng, chiết khấu ghi riêng không giảm phải trả; không cho prompt thay đổi chúng.
