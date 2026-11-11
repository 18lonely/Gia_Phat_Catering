# Hiện diện và nullability34DTO E6

11/11/2026 · Rà14request +20response trong [API](api-spec.md). Đây là diễn giải contract nháp và đánh dấu gap, không JSON Schema cuối hoặc API đã chạy. [Sổ gap](../review/contract-gap-register.md) là đầu mối điều kiện đóng.

`R` là field bắt buộc theo bảng hiện tại; `?` là có thể vắng, không tự cho phép JSON null. Nullable chỉ khi type ghi null tường minh. Điều kiện theo nhánh có ưu tiên hơn câu quy ước chung, nhưng nhánh chưa đủ shape phải giữ gap. Null, vắng, chuỗi rỗng,0,false và[] không hoán đổi. Các “không nêu null” không chứng minh backend đã reject; cần validator theo contract được review. Không dùng Optional để che missing dependency. Tên scope trong bảng là nhóm field hiện có, không thêm payload object mới.

| DTO | R hiện tại / nhóm field | Optional / điều kiện | Null | Default / giới hạn diễn giải | Gap gốc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ScopeQuery | servicePointId,serviceDate,shift | Không trường optional trong type; path alias không là field thứ hai | Không nêu nullable | Không | CG-11: query ngoài type vẫn rà riêng |
| SelectionInput | servicePointId,menuDayId,dishId,menuVersion,quotaVersion,version | date/shift từ path; identity từ phiên | dishId=null không phải hủy | Không | CG-03: hủy/đổi điểm; CG-11 |
| SubmissionInput | scope,totalServings,coordinatorLines,version,summaryVersion,source | evidenceRef/reason optional với PORTAL; bắt buộc nhập hộ | ? không cấp phép null; total int≥0 | Không tự total=0 hoặc C=0 | CG-03/11: [] và max lines |
| ChangeInput | baseVersion,baseOrderRevisionId,deltaByDish,reason | evidenceRef? | Không nêu null | Không | CG-07/11: mảng rỗng/line identity |
| GrantInput | customerId,userId,servicePointIds,role,version,reason | Không optional; role=NGUOI_DAT_TONG là giá trị cố định | Không nêu null | Không suy role khi thiếu | CG-01/02/11: duplicate pointIds |
| RegistrationInput | qrToken,servicePointId,identityProof,displayName | Không optional | Proof không được thay bằng null/tên | Không | CG-01/11: proof shape/length |
| QrSessionInput | qrToken,servicePointId,serviceDate,shift,identityProof | expiry do server; không client field | Không nêu null | Không | CG-01/11: proof/expiry |
| QrRotationInput | version,reason | qrId?,servicePointId?; qrId null khi cấp lần đầu đã ghi | qrId có null tường minh; servicePointId? chưa xác nhận null | Không suy toàn khách từ point bị bỏ | CG-01/11: absent/null qrId và scope |
| EaterStatusInput | status,version,reason | status=REMOVED; không optional | Không nêu null | Không | CG-01: session/selection impact |
| ServiceInput | customerId,kitchenId,name,address,schedules,version,reason | API014 update; API026 create | Không nêu null | Tạo version0; cập nhật version hiện tại | CG-08/11: schedules []/limits/transfer |
| QuotaInput | mealTypeId,effectiveFrom,version,reason | Giá/cơ cấu server, không payload | Không nêu null | Không tự hiệu lực | CG-11/12: POST version semantics, quota approval |
| WeekInput | weekStart,selections | Mỗi entry thêm serviceDate/shift và SelectionInput | Không nêu null;1..7entries | Policy server đã duyệt | CG-12: atomic/partial |
| DecisionInput | decision,version,baseOrderRevisionId,reason | Version đề nghị; actor từ phiên | Không nêu null | Không | CG-05/07: approve/reject guards |
| ModeInput | enabled,effectiveFrom,version,reason | false là boolean hợp lệ, không thiếu field | Không nêu null | Không tự enabled=true | CG-12/11: mode đầu tiên/version |
| AvailableMeals | scope,menu/source/quota/deadline fields,choiceEnabled,mealType,dishes,sourceStatus | selection:Selection? chưa rõ omit hay null | defaultDishId thiếu nguồn chưa có null shape | Không dishes=[] giả đủ nguồn | CG-10/11: selection/default/sourceStatus enum |
| SafeDish | dishId,name,role,recipePortionLabel,allergens,allergenStatus,nutrition,comboItemIds,comboPriceVnd,withinQuota | priceVnd chỉ khi công bố; không phải luôn hiện | 4chỉ số dinh dưỡng có null; sourceVersion chưa rõ null | Không missing→0; không unknown→safe | CG-10/11: price omit/null, sourceVersion/kind/stale |
| Selection | id,scope,menuDayId,dishId,version,menuVersion,quotaVersion,updatedAt | Không optional | Không nêu null | Không | CG-01/03: identity/transfer |
| Summary | scope,selected,coordinator,total,remaining,unselectedRegisteredEaters,countsByDish,version | Không optional theo type | total/remaining/unselectedRegisteredEaters có null | default trước khóa0; total thiếu=null | CG-03/04: token và nghĩa counts |
| OrderReceipt | orderId,status,version,summaryVersion,totalServings,selected,coordinator,remaining,requestId,source | status=SUBMITTED | Không nêu null | Không suy LOCKED | CG-03/04: receipt/token |
| OrderRevision | orderId,revisionId,revisionNo,orderVersion,scope,totalServings,lines,menuVersion,quotaVersion,deadlineAt,capturedAt | Không field kế toán ngầm | Không nêu null | Không | CG-07: unit/id dòng |
| ChangeRequest | id,orderId,baseOrderRevisionId,baseVersion,deltaByDish,reason,status,version,createdAt,source | evidenceRef? | ? chưa cho phép null | Không tự source=PORTAL | CG-07/11: source enum/mapping và evidence |
| DecisionReceipt | changeRequestId,decision,orderVersion,planStatus,requestId | orderRevisionId? chỉ approved; rejected không tạo revision | Representation omit/null khi rejected chưa chốt | Không READY→publish | CG-05/06/11: reject planStatus/shape |
| Grant | id,userId,customerId,servicePointIds,role,status,version | Không secret | Không nêu null | Không | CG-01/02/11: status enum |
| RegistrationReceipt | eaterId,userId,customerId,servicePointId,verificationStatus theo bảng hiện tại | Trạng thái chưa verify có thể chưa đủ ID | userId null/omit chưa chốt; không giả ID | Không phát token trước verify | CG-01/11: pending vs verified shape |
| QrSession | sessionId,scope,expiresAt,secretAlreadyIssued | credential? chỉ lần đầu | Không trả credential=null như secret mới; representation cần review | Replay không secret | CG-01/04/11: first issuance branch |
| QrReceipt | qrId,status,version,secretAlreadyIssued | qrToken? chỉ lần đầu | Null/omit chưa chốt toàn bộ nhánh | Replay không raw token | CG-01/04/11: initial/rotation/replay |
| Eater | id,displayName,servicePointId,status,version | Không health/token/login log | Không nêu null | Không | CG-01/11: status/point lifecycle |
| ServiceContext | servicePointId,customerId,kitchenId,name,address,schedules,version | Không optional | Không nêu null | Không thay snapshot cũ | CG-08/11: schedules |
| Quota | id,customerId,mealTypeId,effectiveFrom,version,reviewStatus,priceLimitVnd,mainCount,sideCount | reviewStatus đề xuất | Không nêu null | Không proposal→effective | CG-11/12: status/approval |
| WeekReceipt | batchId,policy,status,days,requestId; day có serviceDate/shift/status | selectionId?,version?,error? theo kết quả ngày | omit/null branches chưa chuẩn hóa | ATOMIC không PARTIAL | CG-12/11: rejected/success day schema |
| PlanSummary | planId,kitchenId,serviceDate,shift,currentRevisionNo,publishedAt,sourceOrderCount,hasPendingUpdates | publishedAt hiện không có? | Chưa chốt nullable hay chỉ trả published | Không sourceOrderCount→complete | CG-06/11: visibility/null/current |
| PlanRevision | planId,revisionNo,scope,publishedAt,sources,lines,delta,isCurrent | previousRevisionNo? | First revision previous null/omit chưa chọn; publishedAt gap | Không order revision=plan revision | CG-06/07/11: unit/delta/current |
| ReminderRun | id,scope,status,eligibleCount,sentCount,failedCount,eventId,createdAt | channel? | Counts trước xử lý là0 hay unknown chưa có policy shape | Không tự gửi kênh | CG-12/11: counts/channel |
| ChoiceMode | customerId,enabled,effectiveFrom,version,reviewStatus | Không optional theo type | Không nêu null | Pending giữ mode cũ | CG-12/11: proposal/current representation |

## Query, nested field và negative review

Path ID/date/shift không được bỏ vì body cùng tên tồn tại. Nested records theo type, không “object có mặt” thay cho đủ field con. Các query filter ngoài34type tiếp tục theo [26route](route-validation-review.md): page mặc định chưa được nêu rõ (không tự chọn1); pageSize mặc định20 đã nêu; effectiveDate/catalog không có? nhưng default chưa có, nên không tự dùng hôm nay khi thiếu. revisionNo bỏ qua dùng current, song current có nghĩa bản đã build hay published vẫn CG06.

Các biến thể review cho từng field: absent/null/giá trị hợp lệ/sai kiểu; thêm[]/duplicate cho mảng;false/0 để tránh coi falsy là thiếu; secret replay không có secret, conditional evidence thiếu thì không nhận nhập hộ. Đây là checklist đối chiếu schema tương lai, **không tạo thêm34ca** và không PASS khi chỉ đọc bảng.

Căn cứ sửa chắc chắn trong phiên: quy ước presence phải nhắc điều kiện tường minh; QR qrId có null ở cấp lần đầu phải ghi trong type; null dinh dưỡng/Summary không bị hiểu là field optional. Các điểm vắng/null theo nhánh chưa đủ bằng chứng giữ CG11 và gate gốc, không tự thêm defaults.
