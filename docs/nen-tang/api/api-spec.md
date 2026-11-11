---
id: DOC-NEN-TANG-API-API-SPEC
title: Hợp đồng API nền tảng E1
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Hợp đồng API nền tảng E1

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Nguyên tắc và kiểu dùng chung

Kế thừa SRS nền: `/v1`, Bearer access15 phút, refresh cookie HttpOnly/Secure/SameSite=Strict7 ngày; rotation và reuse revocation. Endpoint cookie kiểm Origin và CSRF; credential không vào URL/log/localStorage. Id là chuỗi số nguyên dương; Date theo Asia/Ho_Chi_Minh; timestamps UTC ISO8601. `page>=1,pageSize=1..100` mặc định20; ngoài khoảng422 ERR-SYS-422-03, vượt trang cuối trả rỗng/total. Không chuyển sang cursor cho E1/E2.

Response thành công `{success:true,data,meta:{requestId,page?,pageSize?,total?},timestamp}`. Error body theo SRS `{code,message,details:[],requestId}`. Nội dung error không chứa bí mật; HTTP tương ứng ma trận SRS. Chỗ các hợp đồng E3/E4/E5 đang dùng envelope lỗi/cursor khác được ghi E1-Q01, chưa tự coi thống nhất toàn hệ thống.

Tạo mới cần Idempotency-Key scope=(actor,route,key) trong24h; cùng body replay cùng resource theo quyền hiện tại; body khác409 ERR-SYS-409-02 với details.reason=KEY_REUSE (mapping đề xuất E1-Q02). Lệnh sửa gửi version; stale409. Với secret chỉ-hiện-một-lần (mật khẩu tạm), replay trả resourceId và secretDelivered=true, không secret; phải reset mới có lý do nếu người nhận chưa lấy được. Login/refresh không replay credential từ cache; double refresh bị xử lý reuse theo SRS. Không hard-delete, không API công khai ghi audit/cấp quyền dịch vụ.

| Type | Trường và validation |
| :--- | :--- |
| LoginInput | username:string1..120 (format N-01 mở),password:string; không trim/normalize mật khẩu; chặn body quá kích thước cấu hình, không ghi raw request |
| Session | accessToken,expiresAt,user:User; refresh chỉ Set-Cookie, không trong JSON; khi mật khẩu tạm chỉ quyền changePassword |
| UserInput | fullName:string1..120,username:string1..120,roles:RoleScope[1..n]; vai trò cố định theo SRS; mật khẩu tạm sinh server |
| RoleScope | roleCode enum SRS, kitchenIds:Id[]; QL_CO_SO/BEP_TRUONG ít nhất1 cơ sở; QUAN_TRI không suy toàn quyền nghiệp vụ |
| User | id,fullName,username,status,roles,version; tuyệt đối không passwordHash/refreshHash |
| DecisionInput | decision?:APPROVE/RETURN, version:int>=1,reason:string10..500; với reset/retry không gửi decision |
| DelegationInput | delegateUserId,permissions:code[],validFrom,validTo,reason; không self, khoảng hợp lệ, chỉ quyền duyệt đang có; chờ O-06 |
| ParameterInput | code:string,typedValue:number/string/boolean theo registry,scopeType:GLOBAL/KITCHEN/CUSTOMER/SERVICE_POINT,scopeId:null nếu GLOBAL, effectiveFrom:Date>=hôm nay,reason:string10..500; không tự đặt VAT |
| ParameterVersion | id,code,typedValue,scopeType,scopeId,effectiveFrom,approvalStatus,version,createdBy,approvedBy? |
| AuditEntry | id,entity,entityId,action,actorId,onBehalfUserId?,changedAt,reason,before,after,requestId; mask secrets và scope tại serializer |
| LoginLog | id,userId?,attemptedUsernameMasked,result,ip,device,createdAt; thời gian lưu chờ N-03 |
| Notification | id,type,title,body,targetRef,status:NEW/SEEN/RESOLVED,version,createdAt; link vẫn kiểm quyền khi mở |
| Job | id,type,status,attempts,maxAttempts,nextAttemptAt?,safeError?,requestId; không secret/payload nhạy cảm |
| Health | status:OK/UNAVAILABLE; internal diagnostics chỉ internal access, không DSN/key |

## Endpoint

| ID | Method/path | FR | Quyền | Request | Response |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-CORE-001 | POST /v1/auth/sessions | FR-AUTH-LGN-001 | public rate-limited | LoginInput | 201 Session |
| API-CORE-002 | POST /v1/auth/session-refreshes | FR-AUTH-LGN-002 | refresh cookie + Origin/CSRF | Cookie only | 200 Session |
| API-CORE-003 | POST /v1/auth/session-revocations | FR-AUTH-LGN-003 | self | {allSessions:boolean} | 200 {revoked:true} |
| API-CORE-004 | POST /v1/auth/mfa-verifications | FR-AUTH-LGN-004 | preauth challenge | {challengeId:Id,otp:string6} | 200 Session; gated N-04 |
| API-CORE-005 | PUT /v1/auth/me/password | FR-AUTH-PWD-001 | self kể cả mật khẩu tạm | {oldPassword,newPassword} | 200 {changed:true} |
| API-CORE-006 | POST /v1/auth/users/{id}/password-resets | FR-AUTH-PWD-002 | QUAN_TRI | DecisionInput | 201 {temporaryPassword,expiresAt}; một lần |
| API-CORE-007 | POST /v1/auth/users | FR-AUTH-ACC-001 | QUAN_TRI | UserInput | 201 User |
| API-CORE-008 | PATCH /v1/auth/users/{id}/status | FR-AUTH-ACC-002 | QUAN_TRI | {status:LOCKED/ACTIVE,version,reason} | 200 User |
| API-CORE-009 | PUT /v1/auth/users/{id}/roles | FR-AUTH-ACC-003 | QUAN_TRI | {roles:RoleScope[],version,reason} | 200 User |
| API-CORE-010 | GET /v1/auth/login-logs | FR-AUTH-ACC-004 | QUAN_TRI | userId?,from?,to?,result?,page,pageSize | 200 List LoginLog |
| API-CORE-011 | GET /v1/auth/permission-matrix | FR-AUTH-RBAC-002 | authenticated internal | none | 200 RolePermission[] |
| API-CORE-012 | POST /v1/auth/delegations | FR-AUTH-RBAC-003 | quyền duyệt đang sở hữu | DelegationInput | 201 Delegation; gated O-06 |
| API-CORE-013 | GET /v1/auth/me | FR-AUTH-RBAC-001 | self | none | 200 User + effectivePermissions + scopes |
| API-CORE-014 | GET /v1/auth/users | FR-AUTH-ACC-001 | QUAN_TRI | query?,status?,page,pageSize | 200 List User |
| API-CORE-015 | GET /v1/sys/audit-logs | FR-SYS-AUD-002 | audit.read + entity scope | entity?,entityId?,actorId?,from?,to?,page,pageSize | 200 List AuditEntry |
| API-CORE-016 | GET /v1/sys/parameters | FR-SYS-PRM-001 | parameter.read | code?,scopeType?,scopeId?,businessDate,page,pageSize | 200 List ParameterVersion |
| API-CORE-017 | POST /v1/sys/parameter-changes | FR-SYS-PRM-001 | parameter.propose | ParameterInput | 201 ParameterChange; PENDING nếu cần duyệt |
| API-CORE-018 | POST /v1/sys/parameter-changes/{id}/decisions | FR-SYS-PRM-002 | GIAM_DOC + separation | DecisionInput | 200 ParameterChange |
| API-CORE-019 | GET /v1/sys/notifications | FR-SYS-NTF-002 | self | status?,page,pageSize | 200 List Notification + unreadCount |
| API-CORE-020 | PATCH /v1/sys/notifications/{id} | FR-SYS-NTF-002 | self owner | {status:SEEN/RESOLVED,version} | 200 Notification |
| API-CORE-021 | POST /v1/sys/files | FR-SYS-FILE-001 | file.upload + entity write | multipart file,entity,entityId | 201 {fileId,mime,size} |
| API-CORE-022 | POST /v1/sys/files/{id}/access-links | FR-SYS-FILE-001 | entity read | none | 200 {url,expiresAt}; không cache |
| API-CORE-023 | GET /v1/sys/jobs | FR-SYS-JOB-001 | QUAN_TRI | status?,page,pageSize | 200 List Job |
| API-CORE-024 | POST /v1/sys/jobs/{id}/retries | FR-SYS-JOB-001 | QUAN_TRI | DecisionInput | 202 Job; chỉ job failed |
| API-CORE-025 | GET /v1/health | FR-SYS-HLT-001 | public minimal; internal detail | none | 200/503 Health |

## Port nội bộ, không phải HTTP endpoint

| FR | Port | Contract / side effect |
| :--- | :--- | :--- |
| FR-AUTH-RBAC-001, FR-AUTH-SVC-001 | authorize(actor,service?,permission,resourceScope) | Giao quyền service/user; 403 thiếu quyền,404 ngoài scope; gọi mỗi request/tool; cấp key qua hạ tầng O-04, không UI |
| FR-SYS-AUD-001, FR-SYS-AUD-003 | appendAudit(tx,actor,onBehalf,entity,before,after,reason,requestId) | Cùng transaction nghiệp vụ, lỗi thì rollback; thiếu lý do422; chỉ INSERT/SELECT audit |
| FR-SYS-AUD-004 | cancelEntity(tx,id,version,reason) | Mỗi module định nghĩa điều kiện tham chiếu; không endpoint `/delete-anything`; trả409 nếu đang dùng |
| FR-SYS-NTF-001 | notify(eventId,type,recipientScope,targetRef,safePayload) | Chọn người nhận theo scope; event idempotency đề xuất E1-Q04; persistence/outbox chưa thiết kế DB migration |
| FR-SYS-NTF-003 | sendExternal(notificationId,channel,template,recipient) | Q-14 mở; max3 attempts; chưa endpoint/provider webhook, không tự gửi ra ngoài |

Tệp upload chỉ JPG/PNG/WEBP/PDF theo FILE-001; đường import Excel của MENU là hợp đồng riêng, không tự mở XLSX cho `/sys/files`. Presigned link15 phút phải kiểm quyền entity trước cấp. Upload lỗi không để metadata thành công trỏ tới object thiếu; cleanup orphan là thiết kế cần review.

## Ví dụ và lỗi

POST parameter-changes: `{"code":"COST_NGUONG_PCT","typedValue":52,"scopeType":"GLOBAL","scopeId":null,"effectiveFrom":"2026-11-12","reason":"Đề nghị thử trên môi trường test"}` →201 PENDING, không có hiệu lực trước duyệt/ngày. Đây là fixture giả định, không quyết định thay tham số.

Lỗi: `{"code":"ERR-SYS-403-01","message":"Bạn không thể duyệt nội dung do chính mình tạo hoặc sửa.","details":[],"requestId":"test-only"}` với HTTP403; rollback không đổi trạng thái. Mỗi endpoint áp mã lỗi đúng trigger [SRS](../srs/spec.md), không trả401 cho mọi lỗi nghiệp vụ.
