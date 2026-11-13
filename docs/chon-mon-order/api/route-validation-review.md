# Validation26route E6: review độc lập

11/11/2026 · Phủ26/26route trong catalog hiện có, không phải26route đã chạy hoặc được duyệt. Không thêm field/giới hạn tưởng tượng; cột Gap giữ việc chưa thể freeze. [API](api-spec.md) · [Adapter](adapter-contract-review.md).

## Guard chung

GET không body/không mutation, authorize mỗi lần. Mutation dùng key và version theo contract; receipt replay đã commit vẫn kiểm quyền hiện tại. ID chuỗi số nguyên dương, ngày hợp lệ theo lịch, enum exact, integer không nhận decimal/NaN; reject field lạ/actorId/approvedBy/eaterId client. Các giới hạn size/rate/array chưa có không được tự ghi thành đã duyệt. Lỗi input400, phiên401, thiếu quyền403, resource ngoài scope404; không dùng422 quan hệ để tiết lộ resource mà actor chưa được xem.

Pagination E1 nêu ngoài khoảng422 ERR-SYS-422-03, E6 có400 sai kiểu: phân biệt sai kiểu400 với numeric out-of-range; mapping range sang mã E6 chưa có riêng, giữ E1-Q01/contract review, không tự chốt cùng một400 cho mọi trường. Không tính total trước scope filter. Danh sách rỗng chỉ khi truy vấn hợp lệ và dependency trả kết quả xác định, không dùng để che timeout.

| API / method/path hiện có | Input cần kiểm | Quan hệ/scope/guard | Lỗi/kết quả cần phân biệt | Gap chưa chốt |
| :--- | :--- | :--- | :--- | :--- |
| API-ORD-001 GET `/v1/orders/available-meals` | ScopeQuery; ngày thực, shift enum | menuDay đúng point/date/mealType; published/quota/source version | 422-01 nguồn thiếu;404 ngoài scope;503 dependency | sourceVersion/kind/stale DTO chưa đủ |
| API-ORD-002 PUT `/v1/orders/me/selections/{date}/{shift}` | SelectionInput; path date/shift; version0chỉ tạo | identity từ phiên; dish thuộc menuDay/MAIN; quota và counter nguyên tử | 409-01 stale;422-01 tổ hợp; replay không tăng counter | policy vượtT/C→S, identity vẫn mở |
| API-ORD-003 GET `/v1/orders/selection-summaries` | ScopeQuery | scope summary cùng point/date/shift, counts từ cùng snapshot | total=null khi chưa gửi; không suy bằng số người | summary token persistence |
| API-ORD-004 POST `/v1/orders/submissions` | SubmissionInput; coordinatorLines không trùng dish | version order và summaryVersion riêng; nguồn ZALO/PHONE có evidence/lý do | 409 stale;422-02 theo phương án tổng; không xóa selection | max lines, C gộp và vượtT chưa chốt |
| API-ORD-005 POST `/v1/orders/{id}/change-requests` | ChangeInput; delta nguyên khác0 | baseRevision cùng order; resolve dòng; không tự chọn recipe mới | 422-02 âm;409 stale; chưa commit không PENDING giả | min/max deltaLines, món mới và ambiguity |
| API-ORD-006 POST `/v1/orders/customer-access-grants` | GrantInput;1..100pointIds | user/customer có sẵn, từng point thuộc customer; actor có quyền grant | 404/403 an toàn; retry không cấp role rộng | duplicate pointIds chưa nêu; scope một/nhiều khách mở |
| API-ORD-007 GET `/v1/orders/customer-access-grants` | customerId,page,pageSize | authorize customer trước list/count | 200rỗng trong scope;404 ngoài scope; total scoped | filter/sort chi tiết chưa freeze |
| API-ORD-008 POST `/v1/orders/qr-registrations` | RegistrationInput; displayName1..120 | QR hợp lệ + identity proof đã được duyệt | 401 QR invalid;503 policy chưa cấu hình; không phát secret khi chưa verify | proof schema/length; userId nullable khi chưa account |
| API-ORD-009 POST `/v1/orders/qr-sessions` | QrSessionInput; ngày/ca/point | QR scope giao lịch/phân công; expiry server | secret lần đầu; replay không credential | proof/TTL/revocation policy |
| API-ORD-010 GET `/v1/orders/customers/{id}/eaters` | path customerId; status?,page,pageSize | scope và quyền xem danh sách | không trả health/token;200rỗng trong scope | status filter enum chưa nêu |
| API-ORD-011 POST `/v1/orders/customers/{id}/qr-rotations` | QrRotationInput; version;reason | path customer và optional point cùng scope; qrId nếu có thuộc scope | secret once; replay không token;409 stale | null/absent qrId cần thống nhất; session cũ policy |
| API-ORD-012 PATCH `/v1/orders/eaters/{id}/status` | EaterStatusInput; REMOVED;version≥1 | eater thuộc scope; không DELETE lịch sử | 404 ngoài scope;409 stale; giữ snapshot | tác động selection/phiên ORD-Q02 |
| API-ORD-013 GET `/v1/orders/service-contexts` | customerId,pointId?,page,pageSize | point filter thuộc customer và actor scope | list rỗng khác invalid scope; không tự tạo context | effective schedule và alias pointId |
| API-ORD-014 PUT `/v1/orders/service-contexts/{pointId}` | path pointId;ServiceInput;version≥1 | point hiện hữu; customer relation; schedule unique shift/weekday | 409 stale;422-04 relation; không upsert tạo điểm | schedules min/max; chuyển customer/đổi bếp policy |
| API-ORD-015 GET `/v1/orders/customers/{id}/quotas` | path customerId;effectiveDate,page,pageSize | quyền khách; trả quota nguồn/version đúng ngày | 200rỗng nếu chưa có quota; API001 vẫn422thiếu quota | effectiveDate required/optional cần rõ |
| API-ORD-016 POST `/v1/orders/customers/{id}/quotas` | QuotaInput; mealTypeId,date,version | giá/cơ cấu server; không nhận giá tự nhập | proposal không tự hiệu lực; stale409 | POST create/update version semantics; approval ORD-Q04 |
| API-ORD-017 GET `/v1/orders/me/selections` | from,to,pointId?,shift?; from≤to | identity từ phiên; lọc chỉ lựa chọn bản thân | không PII khác; list rỗng hợp lệ | max khoảng ngày/pagination chưa được nêu trong catalog |
| API-ORD-018 POST `/v1/orders/me/weekly-selections` | WeekInput;1..7,thứHai,không trùng ngày/ca | account-only; mỗi ngày source/version/scope riêng | guest403; policy503; không200nghĩa mọi ngày thành công | atomic/partial ORD-Q05 |
| API-ORD-019 GET `/v1/orders/{id}/revisions` | path orderId,page,pageSize | scope hiện tại; revision immutable thuộc order | safe snapshot; không source_snapshot nguyên khối | giá kế toán chỉ internal permission |
| API-ORD-020 GET `/v1/orders/production-plans` | kitchenId,date,shift,page,pageSize | bếp được giao; nguồn kế hoạch đúng scope | list rỗng không chứng minh không có bữa; không false COMPLETE | publishedAt nullable/visibility và completeness |
| API-ORD-021 GET `/v1/orders/{id}/change-requests` | path orderId,page,pageSize | coordinator/DDV/approver đúng scope | evidenceRef không bypass FILE permission | reason free-text có thể PII; chưa policy redaction |
| API-ORD-022 POST `/v1/orders/change-requests/{id}/decisions` | DecisionInput;version≥1;reason | version của đề nghị; baseRevision và order baseline; separation creator/last-editor | 403 tự duyệt;409 stale; replay quyết định cũ | role/ngưỡng O-06/Q16; READY definition |
| API-ORD-023 GET `/v1/orders/reminder-runs` | ScopeQuery,page,pageSize | operations scoped; no external send | không phone raw; channel thiếu=BLOCKED_CONFIGURATION | retention/dedupe Q14/E1-Q04 |
| API-ORD-024 PUT `/v1/orders/customers/{id}/choice-mode` | ModeInput; boolean,date,version≥1 | quyền khách; hiệu lực không sửa snapshot lịch sử | proposal/current state; không tự xóa lựa chọn | mode chưa tồn tại dùng version gì; ORD-Q09 |
| API-ORD-025 GET `/v1/orders/production-plans/{id}` | path planId;revisionNo? int≥1 | bếp đúng scope; revision thuộc plan; omit=current | 404 không tồn tại/ngoài scope; GET không ack/start | current=buildhaypublished chưa chốt; delta role/unit |
| API-ORD-026 POST `/v1/orders/service-contexts` | ServiceInput;version=0 | customer/kitchen tồn tại và có quyền; server cấp pointId | 201 context; không tạo customer master; replay cùng id | schedules min/max và lịch hiệu lực |

## Kết quả review

Catalog vẫn26HTTP/2port. Các dòng ghi guard hiện có và gap, không quyết định identity/scope/ORD-Q06. Cần bổ sung schema validation được duyệt cho limits, nullability, pagination, phiên bản tạo mới và response projection trước freeze. Không sửa endpoint-catalog.json chỉ vì có review mới. Phủ route là kiểm tài liệu, không coverage thực thi API.

Truy vết feature/FR/UC/AC theo [RTM](../test/traceability.md); matrix không tạo26test case mới. Bộ57AC và99mô tả ca tổng không đổi. Cổng O-03 vẫn không có route ghi; PORT-LOCK/REM là nội bộ, không suy endpoint public từ ma trận này.

## Hợp nhất gap/DTO ngày 11/11/2026

[Ma trận34DTO](dto-presence-review.md) bổ sung required/optional/null; [sổ gap](../review/contract-gap-register.md) quản lý điều kiện đóng. Bảng26route vẫn là review theo từng giao tiếp, không tự đổi contract theo cột gap.
