from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
routes=[
('GET','/v1/orders/available-meals','eater scoped','ScopeQuery','200 AvailableMeals','036,045'),
('PUT','/v1/orders/me/selections/{date}/{shift}','eater self','SelectionInput + key','201 tạo / 200 sửa Selection','036'),
('GET','/v1/orders/selection-summaries','coordinator / DDV assigned','ScopeQuery','200 Summary','038,042'),
('POST','/v1/orders/submissions','coordinator / DDV assigned','SubmissionInput + key','201 tạo / 200 cập nhật OrderReceipt','038,042'),
('POST','/v1/orders/{id}/change-requests','coordinator / DDV assigned','ChangeInput + key','201 ChangeRequest PENDING','041'),
('POST','/v1/orders/customer-access-grants','customer access administrator','GrantInput + key','201 Grant','030'),
('GET','/v1/orders/customer-access-grants','customer access administrator','customerId,page,pageSize','200 List Grant','030'),
('POST','/v1/orders/qr-registrations','valid QR + approved identity policy','RegistrationInput + key','201 RegistrationReceipt','031'),
('POST','/v1/orders/qr-sessions','valid QR + approved identity policy','QrSessionInput + key','201 QrSession (secret once)','032'),
('GET','/v1/orders/customers/{id}/eaters','coordinator assigned','status?,page,pageSize','200 List Eater','033'),
('POST','/v1/orders/customers/{id}/qr-rotations','coordinator assigned','QrRotationInput + key','201 QrReceipt (secret once)','033'),
('PATCH','/v1/orders/eaters/{id}/status','coordinator assigned','EaterStatusInput + key','200 Eater','033'),
('GET','/v1/orders/service-contexts','DDV assigned / coordinator read','customerId,pointId?,page,pageSize','200 List ServiceContext','034'),
('PUT','/v1/orders/service-contexts/{pointId}','DDV assigned','ServiceInput + key','201 tạo / 200 sửa ServiceContext','034'),
('GET','/v1/orders/customers/{id}/quotas','coordinator assigned / DDV read','effectiveDate,page,pageSize','200 List Quota','035'),
('POST','/v1/orders/customers/{id}/quotas','coordinator assigned','QuotaInput + key','201 Quota proposal; chưa tự có hiệu lực','035'),
('GET','/v1/orders/me/selections','eater self','from,to,pointId?,shift?','200 List Selection (không PII người khác)','036'),
('POST','/v1/orders/me/weekly-selections','registered eater self only','WeekInput + key','200 WeekReceipt; policy chưa chốt 503','037'),
('GET','/v1/orders/{id}/revisions','coordinator/DDV assigned','page,pageSize','200 List OrderRevision safe','038,041'),
('GET','/v1/orders/production-plans','kitchen read','kitchenId,serviceDate,shift,page,pageSize','200 List PlanSummary','040,048'),
('GET','/v1/orders/{id}/change-requests','coordinator/DDV/approver assigned','page,pageSize','200 List ChangeRequest','041'),
('POST','/v1/orders/change-requests/{id}/decisions','approved role per O-06','DecisionInput + key','200 DecisionReceipt','041'),
('GET','/v1/orders/reminder-runs','operations scoped','ScopeQuery,page,pageSize','200 List ReminderRun','043'),
('PUT','/v1/orders/customers/{id}/choice-mode','coordinator assigned','ModeInput + key','200 ChoiceMode proposal/current state','044'),
('GET','/v1/orders/production-plans/{id}','kitchen read same scope','revisionNo?; omitted=current','200 PlanRevision','048'),
]
intro='''---
id: DOC-CHON-MON-ORDER-API-API-SPEC
title: Hợp đồng API E6 để review
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Hợp đồng API E6 để review

**Draft — 25 HTTP endpoint + 2 port nội bộ. Chưa backend; không endpoint ghi sức khỏe.**

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Mở rộng 5 route gốc, bổ sung schema DTO và gate; không đổi path gốc |
| 0.1.0 | 2026-11-11 | Lát cắt 5 route chọn/chốt |

## Quy ước

Kế thừa [API nền](../../nen-tang/api/api-spec.md): prefix `/v1`, Bearer; cookie cần CSRF; `Content-Type: application/json`, `X-Request-Id`, các mutation cần `Idempotency-Key`. Success là DTO mô tả ở dưới; list `{items,page,pageSize,total}`. Lỗi `{code,message,details:[{field,reason}],requestId}` theo SRS E6. E4/E5 có envelope khác: **E1-Q01 vẫn chờ**, adapter chỉ lấy dữ liệu allowlist, không truyền nguyên envelope nội bộ ra người ăn.

Id chuỗi số dương; ngày YYYY-MM-DD theo Asia/Ho_Chi_Minh; timestamp ISO8601 UTC; shift enum MORNING/LUNCH/AFTERNOON/DINNER theo schema nền. Số suất int≥0; tiền decimal string không dấu nghìn; không NaN/Infinity. Ngày/shift/point phải có lịch phục vụ thực và cùng scope, không chỉ đúng cú pháp. `version=0` chỉ tạo; sửa phải có version hiện tại. Tất cả trường trong bảng kiểu bắt buộc trừ `?`; reject trường ngoài schema và client eaterId/actorId/approvedBy. page≥1, pageSize1..100 mặc định20 theo nền; sort id ổn định. Giới hạn mảng/chuỗi dưới đây là đề xuất kỹ thuật, không thay phạm vi nghiệp vụ.

Key đề xuất scope=(principal,method,route,key), body hash chuẩn hóa, lưu bền vững trong transaction; cùng body trả resource/receipt đã ghi theo quyền hiện tại; khác body409-02; IN_PROGRESS409-02 + Retry-After. Retention tối thiểu24h chờ E1-Q02; domain unique không hết hạn theo key. QR trước xác thực cần scope token hash + operation, chống enumeration/rate limit chờ ORD-Q11. Secret không lưu trong response replay: trả resourceId và `secretAlreadyIssued=true`, muốn token mới phải rotate. Không dùng key thay danh tính người ăn.

Tất cả route kiểm 400/401/403/404/429/500/503 theo [ma trận lỗi](../srs/operational-rules.md). Mutation kiểm409 version/key/state và422 rule tương ứng; rollback cả dữ liệu và audit khi lỗi ghi. POST tuần có 200 receipt không đồng nghĩa mọi ngày thành công. Không webhook public/provider outbound trong gói này.

## Request types

| Type | Fields / validation |
| :--- | :--- |
| ScopeQuery | servicePointId:Id,serviceDate:Date,shift:Shift; tên `point,date` trong 5 route gốc là alias tài liệu, wire contract chuẩn hóa thành servicePointId/serviceDate; ORD-Q11 review |
| SelectionInput | servicePointId,menuDayId,dishId:Id; menuVersion,quotaVersion:int≥1; version:int≥0; date/shift từ path; identity từ phiên; chỉ 1 MAIN |
| SubmissionInput | servicePointId,serviceDate,shift,totalServings:int≥0,coordinatorLines:[{dishId,qty:int≥0}] không trùng dish; version:int≥0,summaryVersion:int≥0,source:PORTAL/ZALO/PHONE; evidenceRef?:Id,reason?:string10..500; hai trường cuối bắt buộc với nhập hộ; source khác PORTAL chỉ DDV có quyền |
| ChangeInput | baseVersion:int≥1 (orders.version),baseOrderRevisionId:Id,deltaByDish:[{dishId,delta:int≠0}],reason:string10..500,evidenceRef?:Id; không trùng dish; delta sau áp không âm; snapshot recipe/portion từ server |
| GrantInput | customerId,userId:Id,servicePointIds:Id[1..100],role=COORDINATOR,version:int≥0,reason:string10..500; quyền administrator cụ thể ORD-Q11; không dùng role nội bộ client nhập |
| RegistrationInput | qrToken:string,servicePointId:Id,identityProof:opaque string,displayName:string1..120; nội dung proof/mapping account policy BLOCKED ORD-Q01; không coi email/phone chưa xác minh là identity |
| QrSessionInput | qrToken:string,servicePointId,serviceDate,shift,identityProof:opaque string; expiry do server policy ORD-Q01/11, không client nhập |
| QrRotationInput | qrId?:Id (null khi cấp lần đầu),servicePointId?:Id,version:int≥0,reason:string10..500; scope không vượt khách URL; version là delta chưa có trong QR table |
| EaterStatusInput | status=REMOVED,version:int≥1,reason:string10..500; không DELETE lịch sử; phục hồi/cross-customer transfer chưa đặc tả |
| ServiceInput | customerId,kitchenId:Id,name:string1..160,address:string1..255,schedules:[{shift,weekday:int1..7,deliveryTime:HH:mm}],version:int≥0,reason:string10..500; unique shift/weekday; pointId mới do quy ước tạo ID nền chờ ORD-Q03/11 |
| QuotaInput | mealTypeId:Id,effectiveFrom:Date,version:int≥0,reason:string10..500; giá/cơ cấu đọc từ loại suất; không nhận giá người ăn tự nhập; duyệt/effective policy ORD-Q04 |
| WeekInput | weekStart:Date thứ Hai,selections:SelectionInput+[serviceDate,shift] từ1..7 không trùng ngày/ca; mỗi ngày trong tuần; policy do server đã duyệt, chưa chốt không nhận mutation |
| DecisionInput | decision:APPROVED/REJECTED,version:int≥1,baseOrderRevisionId:Id,reason:string10..500; approver từ phiên, kiểm separation và gate |
| ModeInput | enabled:boolean,effectiveFrom:Date,version:int≥1,reason:string10..500; ORD-Q09 hiệu lực khi đã có lựa chọn |

API-ORD-014 là PUT theo id nghiệp vụ do hệ thống cấp, chưa có route cấp point id trong gói gốc. **Đề xuất** với điểm mới dùng pointId dạng client-generated UUID không phù hợp Id bigint; vì vậy thiết kế này chỉ cho **cập nhật điểm đã có**; tạo mới được đặc tả bằng API-ORD-026 bên dưới. Không để route cập nhật ngầm tạo ID tùy ý.

## Response types

| Type | Fields / invariant |
| :--- | :--- |
| AvailableMeals | scope,menuId,menuDayId,menuVersion,quotaVersion,deadlineAt,deadlineVersion,choiceEnabled,defaultDishId,mealType{priceLimitVnd,mainCount,sideCount},dishes:SafeDish[],selection:Selection?,sourceStatus; chưa có menu/định mức trả422-01 có reason, không array rỗng giả đủ điều kiện |
| SafeDish | dishId,name,role,recipePortionLabel,priceVnd nếu công bố,allergens:[{code,name}],allergenStatus:KNOWN/UNKNOWN,nutrition:{energyKcal,proteinG,fatG,carbG:decimal string hoặc null,label,missing:string[],sourceVersion},comboItemIds,comboPriceVnd,withinQuota:boolean; label “ước tính từ định lượng sống”; missing không suy0; không ingredientPrice/cost/internalNote |
| Selection | id,servicePointId,serviceDate,shift,menuDayId,dishId,version,menuVersion,quotaVersion,updatedAt; không trả eaterId của người khác |
| Summary | scope,selected:int,coordinator:int,total:int hoặc null,remaining:int hoặc null,unselectedRegisteredEaters:int hoặc null,countsByDish:[{dishId,selected,coordinator,default}],version:int; default trước khóa=0; remaining chỉ có khi total xác định |
| OrderReceipt | orderId,status:SUBMITTED,version,summaryVersion,totalServings,selected,coordinator,remaining,requestId,source; không suy locked |
| OrderRevision | orderId,revisionId,revisionNo,orderVersion,scope,totalServings,lines:[{dishId,role,recipeId,portionCode,selected,coordinator,default}],menuVersion,quotaVersion,deadlineAt,capturedAt; kế toán snapshot chỉ internal permission, không spread source_snapshot |
| ChangeRequest | id,orderId,baseOrderRevisionId,baseVersion,deltaByDish,reason,status,version,createdAt,source,evidenceRef?; evidence link qua FILE access permission |
| DecisionReceipt | changeRequestId,decision,orderRevisionId? (chỉ approved),orderVersion,planStatus:PENDING/READY,requestId; PENDING không hứa bếp đã nhận |
| Grant | id,userId,customerId,servicePointIds,role,status,version; không password/hash |
| RegistrationReceipt | eaterId,userId,customerId,servicePointId,verificationStatus; không phát token nếu verification chưa hoàn tất |
| QrSession | sessionId,scope,expiresAt,credential? chỉ lần đầu,secretAlreadyIssued:boolean; không PII khác |
| QrReceipt | qrId,status,version,qrToken? chỉ lần đầu,secretAlreadyIssued:boolean; token cũ không trả lại |
| Eater | id,displayName,servicePointId,status,version; không sức khỏe/token/login log |
| ServiceContext | servicePointId,customerId,kitchenId,name,address,schedules,version; tạo/sửa không đổi snapshot lịch sử |
| Quota | id,customerId,mealTypeId,effectiveFrom,version,reviewStatus,priceLimitVnd,mainCount,sideCount; reviewStatus là DTO đề xuất chờ ORD-Q04 |
| WeekReceipt | batchId,policy:ATOMIC/PER_DAY,status:SUCCESS/REJECTED/PARTIAL,days:[{serviceDate,shift,status,selectionId?,version?,error?}],requestId; ATOMIC không có PARTIAL |
| PlanSummary | planId,kitchenId,serviceDate,shift,currentRevisionNo,publishedAt,sourceOrderCount,hasPendingUpdates |
| PlanRevision | planId,revisionNo,previousRevisionNo?,kitchenId,serviceDate,shift,publishedAt,sources:[{orderId,revisionId,revisionNo}],lines:[{dishId,name,recipeId,portionCode,role,qty:int≥0,unit}],delta:[{dishId,recipeId,portionCode,qtyDelta:int}],isCurrent:boolean; không tên người ăn/cost |
| ReminderRun | id,scope,status:QUEUED/RUNNING/SUCCEEDED/FAILED/BLOCKED_CONFIGURATION,eligibleCount,sentCount,failedCount,eventId,channel?,createdAt; không số điện thoại raw |
| ChoiceMode | customerId,enabled,effectiveFrom,version,reviewStatus; giữ mode cũ nếu pending |

## Catalog

'''
# Add missing create contract explicitly instead of pretending an update covers creation.
routes.append(('POST','/v1/orders/service-contexts','DDV assigned','ServiceInput version=0 + key','201 ServiceContext; server cấp servicePointId','034'))
intro+='| ID | Method/path | Quyền | Input | Success | Feature |\n| :--- | :--- | :--- | :--- | :--- | :--- |\n'
cat=[]
for i,r in enumerate(routes,1):
 method,path,perm,inp,out,feat=r
 if i==14:out='200 ServiceContext; chỉ cập nhật điểm đã có'
 intro+=f'| API-ORD-{i:03} | {method} {path} | {perm} | {inp} | {out} | '+', '.join('FEAT-'+x for x in feat.split(','))+' |\n'
 cat.append(dict(id=f'API-ORD-{i:03}',method=method,path=path,features=['FEAT-'+x for x in feat.split(',')]))
intro+='''
## Port và gate

| ID | Input → output | Guard / lỗi |
| :--- | :--- | :--- |
| PORT-LOCK | lock(servicePointId,serviceDate,shift,deadlineVersion,eventKey) → orderRevisionId,outboxId hoặc NEEDS_ATTENTION | Service quyền scoped; serialize writers; BR-ORD-003/004; 409-01 stale;422-03 thiếu total/default; không public HTTP |
| PORT-REM | remind(scope,scheduledAt,eventId) → ReminderRun | Service scope, Q-14 channel gate; kiểm người chưa chọn trước gửi; dedupe event; không tự gửi ra ngoài trong phiên tài liệu |
| GATE-046 / GATE-047 | Chưa có endpoint | O-03 đóng; không thu profile, không tạo recommendation; không coi mã gate là API đã thiết kế nghiệp vụ |

Worker tạo plan dùng event source revision bền vững từ PORT-LOCK hoặc decision. Không có endpoint POST plan nhận số món tùy ý từ client. Quyền chuyển IN_PRODUCTION/acknowledgement chờ ORD-Q14. Hủy lựa chọn/hủy bữa chờ ORD-Q13, không âm thầm coi PUT dishId=null là xóa.

## Ví dụ synthetic và lỗi

PUT /v1/orders/me/selections/2026-11-16/LUNCH, key=`synthetic-request-001`:

```json
{"servicePointId":"101","menuDayId":"201","dishId":"301","menuVersion":2,"quotaVersion":1,"version":0}
```

201 Selection (minh họa synthetic):

```json
{"id":"401","servicePointId":"101","serviceDate":"2026-11-16","shift":"LUNCH","menuDayId":"201","dishId":"301","version":1,"menuVersion":2,"quotaVersion":1,"updatedAt":"2026-11-15T06:00:00Z"}
```

409 khi nguồn đổi, không ghi selection/counter:

```json
{"code":"ERR-ORD-409-01","message":"Dữ liệu đã đổi hoặc không còn mở.","details":[{"field":"menuVersion","reason":"SOURCE_CHANGED"}],"requestId":"synthetic-request-001"}
```

503 policy tuần chưa được duyệt:

```json
{"code":"ERR-ORD-503-01","message":"Chức năng chưa sẵn sàng.","details":[{"field":"weeklyPolicy","reason":"POLICY_UNCONFIRMED"}],"requestId":"synthetic-week-001"}
```

## Tích hợp phụ thuộc

AUTH authorize/audit cùng transaction; MENU chỉ bản PUBLISHED và event WITHDRAWN; NUTR qua adapter server safe projection, không cấp người ăn quyền API tính nội bộ; Cost chỉ kiểm giá tổ hợp/định mức và tham chiếu pricing snapshot được phép. Agent Nội bộ chỉ tạo DRAFT MENU, không chọn/chốt thay người ăn, không gọi PORT-LOCK. Không outbound webhook. Contract tích hợp sự kiện/retry/retention còn ORD-Q11/12/14 và E1-Q02/04.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn không suy VAT0%; chiết khấu khách theo % hoặc tiền/suất là khoản riêng theo order, không giảm amountDue. CK-Q01–10 và DATA-COST-Q01–06 không đổi; không dùng order_dish_lines làm số suất thanh toán. NFR-COST-002 vẫn ≤1đ cho món và ≤0,01 điểm phần trăm cho cost% ngày.
'''
intro=intro.replace('25 HTTP endpoint','26 HTTP endpoint')
(B/'api/api-spec.md').write_text(intro,encoding='utf-8')
(B/'api/endpoint-catalog.json').write_text(json.dumps(cat,ensure_ascii=False,indent=2),encoding='utf-8')
# Keep creation trace explicit across artifacts.
for p in ['test/traceability.md','usecases/UC-ORD-005.md','test/review-test-cases.md']:
 f=B/p;s=f.read_text(encoding='utf-8');s=s.replace('API-ORD-013, API-ORD-014','API-ORD-013, API-ORD-014, API-ORD-026');f.write_text(s,encoding='utf-8')
