from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1]
def write(p,title,body):
 f=B/p;f.parent.mkdir(parents=True,exist_ok=True)
 f.write_text(f'---\nid: DOC-E6-{p.upper().replace("/","-").replace(".MD","")}\ntitle: {title}\nversion: 0.2.0\nphase: Specification\ndomain: Gia Phát\nauthor: BA\nlast_updated: 2026-11-11\n---\n# {title}\n\n**Draft để review · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.**\n\n| Phiên bản | Ngày | Nội dung |\n| :--- | :--- | :--- |\n| 0.2.0 | 2026-11-11 | Bổ sung thiết kế có điều kiện, không đóng gate |\n\n'+body+'\n',encoding='utf-8')
def append(p,s):
 f=B/p;f.write_text(f.read_text(encoding='utf-8')+'\n'+s+'\n',encoding='utf-8')
write('srs/operational-rules.md','Quy tắc vận hành và nhánh chi tiết E6','''Tài liệu này phân rã 19 FR trong [SRS](spec.md), không thay mã gốc. [Đối chiếu](../review/scope-assessment.md) phân biệt căn cứ và gate. Các chính sách mới dưới đây là **đề xuất**, không lấy sự tồn tại của API/wireframe làm bằng chứng phê duyệt.

## 1. Identity, phạm vi và quyền

| Actor | Cho phép | Giới hạn |
| :--- | :--- | :--- |
| Nhân viên cấp tài khoản được phân quyền | FEAT-030 gán người đặt tổng đúng khách | Không mặc định mọi DDV hay mọi quản trị có quyền cấp khách; ORD-Q01/ORD-Q11 |
| Người đặt tổng | QR/danh sách người ăn, định mức, tổng, chế độ, đề nghị đổi trong khách/điểm được giao | Không đọc cost; không duyệt đề nghị của chính mình; không giả DDV nhập nguồn ZALO |
| Người ăn tài khoản | Món công bố, lựa chọn bản thân; chọn tuần P1 | Identity lấy từ phiên, không chấp nhận eaterId/userId client; không đọc danh sách công ty |
| Người ăn QR guest | Món/lựa chọn bản thân trong scope phiên | Không tuần, không hồ sơ sức khỏe; cookie/IP không chứng minh duy nhất một người |
| DDV được giao khách | Dữ liệu phục vụ, nhập hộ có chứng cứ | Không mặc định được duyệt ngoại lệ; không tự ghi đè lựa chọn cá nhân |
| Bếp/quản lý cơ sở | Kế hoạch đã phát hành của cơ sở được giao | DTO kế hoạch không gồm tên người ăn hoặc sức khỏe; thao tác xác nhận nhận bản chờ ORD-Q14 |
| Scheduler/service | Khóa/nhắc/tổng hợp theo quyền service | Không mượn quyền quản trị toàn hệ thống; log actor service cần delta ORD-Q11 |

Khách vãng lai FEAT-045 đọc phần công bố qua mặt tiền E8; không dùng `available-meals` có phạm vi order làm API public. Phiên QR cần company, allowedPointIds, allowedDates/shifts, eater identity, expiresAt, qrVersion; scope là giao giữa QR và phân công, không phải trường client tự gửi. QR không gắn điểm không có nghĩa được đọc toàn công ty. Chưa có policy identity/expiry cuối cùng: ORD-Q01/02/11. Token QR chỉ hash trong DB; không log raw token. Thu hồi token chặn tạo phiên mới; xử lý phiên cũ/lựa chọn chờ ORD-Q02.

## 2. Số suất và tổ hợp

- D-04: chọn 1 trong 3 MAIN. Cơm/món phụ/rau/canh cố định thuộc cơ cấu suất; giá kiểm **toàn tổ hợp**, không chỉ giá MAIN. Tổ hợp bằng định mức được phép, vượt 1đ bị chặn; dữ liệu thiếu không suy giá 0. Đổi quota/giá/menu giữa ngày chờ ORD-Q04.
- `S` đếm lựa chọn cá nhân hợp lệ trong điểm/ngày/ca; mỗi identity một suất là mô hình D-04. `C` đề xuất là số bổ sung cho người chưa có lựa chọn, không phải tổng theo món thay thế S. C chưa có identity phải có xác nhận nguồn/phạm vi; không thể tự chứng minh không trùng người (ORD-Q06).
- `T` là tổng suất người đặt tổng xác nhận. `D=T-S-C` chỉ là **công thức đề xuất ORD-Q06**; không thay bằng số tài khoản đăng ký. `unselectedRegisteredEaters` và `remainingServings` là hai số khác nhau, đều có nhãn.
- Ví dụ **synthetic**: S=60,C=10,T=100 → D=30; T=70 → D=0; T=65 → đề xuất lỗi, không xóa 5 lựa chọn. T=0 chỉ hợp lệ toán học nếu S=C=0; có phải hủy bữa hay vẫn order 0 chờ ORD-Q13.
- Không cộng số MAIN với SIDE/VEG/SOUP thành tổng suất. Dữ liệu kế hoạch dùng `quantity` + `unit` + `role` + `recipe/portion/version` để tránh cộng hai định lượng khác nhau. Quy đổi món phụ chờ ORD-Q10 và O-02; FR-MENU-RCP-007 vẫn bị chặn.

## 3. Gửi tuần

FEAT-037 chỉ tài khoản. Request có 1..7 ngày trong cùng tuần (giới hạn đề xuất), date/shift không trùng; mỗi ngày có scope, menuVersion, quotaVersion, selectionVersion. Không áp dụng tổng version chung cho 5 ngày.

| Phương án chưa duyệt ORD-Q05 | Một ngày khóa | Retry |
| :--- | :--- | :--- |
| ATOMIC | Rollback toàn batch, trả lỗi có ngày; không báo 4 ngày thành công | Cùng key/body trả biên nhận cũ; sửa body phải tạo thao tác mới sau đối soát |
| PER_DAY | Trả receipt mỗi ngày SUCCESS/REJECTED, version và mã lỗi; batch PARTIAL | Retry ngày lỗi có key dẫn xuất/batch reference; không tăng lại ngày thành công |

Không cho client tự chọn policy để vượt cổng; khi policy chưa chốt API tuần bị chặn cấu hình. UI thể hiện lựa chọn đề xuất cho review, không ngầm mặc định ATOMIC là đã duyệt.

## 4. Khóa hạn và món mặc định

Deadline cấu hình theo khách/điểm/ca; lưu instant UTC và timezone Asia/Ho_Chi_Minh, nguồn tham số/version. Thứ tự override và cutoff cụ thể chờ ORD-Q07/12, Q-16; **15:00 D-1, 5%, 10 suất, 06:00 không phải giá trị đã chốt**.

Thiết kế đề xuất: writer và lock job khóa cùng scope điểm/ngày/ca. Tại kiểm tra trong transaction, `serverNow < deadline` mới cho ghi; đúng deadline từ chối. Request bắt đầu trước hạn nhưng chờ khóa tới sau hạn cũng từ chối. Không dùng clock client hoặc giờ nhận request ở gateway để bỏ qua kiểm tra. Nếu user tự chọn và DDV gửi tổng cạnh tranh, snapshot summaryVersion phải khớp; bên sau tải lại.

Tại khóa: kiểm menu còn PUBLISHED, quota/price/recipe/default còn hợp lệ, T đã gửi và D không âm; đối soát S từ lựa chọn với counter; lệch counter không âm thầm khóa. Mặc định theo MENU `defaultDishId`, không lấy món đầu danh sách. Ghi revision, dòng immutable, audit và outbox cùng giao dịch. Kế hoạch là phép tổng hợp từ revision đã commit; lỗi worker sau đó không rollback/mở khóa order đã thành công. Dedupe event bền vững, không chỉ TTL.

Thiếu total/default hoặc nguồn bị thu hồi: giữ trạng thái nghiệp vụ cũ và `lockOutcome=NEEDS_ATTENTION` trên job đề xuất, chặn ghi mới vì deadline vẫn qua, báo vận hành. Không thêm trạng thái ORDER mới vào DBML; gia hạn/quyền sửa cần ORD-Q07. Retry sau bổ sung phải có quyết định/nguồn/version; không giả rằng lần khóa đầu đã thành công.

## 5. Đổi sau khóa, nhập hộ và phiên bản kế hoạch

Đề nghị thay đổi mang `baseOrderRevisionId`, delta theo món/định lượng, lý do và chứng cứ. Delta âm không được làm quantity <0; người duyệt khác người tạo/sửa cuối theo nền tảng. Q-16/O-06/ORD-Q08 chặn ngưỡng, người duyệt và xử lý đã sản xuất. Không auto-approve theo 5%/10 suất chưa chốt. Reject không tạo order/plan revision; approve stale trả409, cần đề nghị mới.

Chấp thuận tạo revision tiếp theo trong một transaction, không sửa bản cũ. `orders.version` dùng optimistic concurrency, `revision_no` là lịch sử nghiệp vụ, `plan.revision_no` là phiên bản tổng hợp; ba số không được coi bằng nhau. Dedupe approval và outbox event ngăn tạo revision đôi.

Một plan scope=(kitchen,date,shift) lấy **đúng một revision hiệu lực cho mỗi order**. Snapshot có source order/revision, recipe/portion, quantity/unit. Khi order A từ rev1 sang rev2, thay đóng góp A; giữ B và các nguồn khác. Hai event A/B cạnh tranh phải serialize scope plan hoặc CAS retry; không làm mất một delta. UI luôn hiện plan version, thời điểm, nguồn, delta +/- so bản trước. Bếp mở bản cũ có nhãn có bản mới; không tự coi bếp đã nhận/chấp thuận bản mới. ORD-Q14 chốt acknowledgement/reprint.

Nhập hộ qua Zalo/điện thoại là ghi lại chứng cứ người dùng cung cấp, **không gửi tin nhắn ra ngoài**. Source, actor, người/khách được nhập thay, evidenceRef (file có quyền), lý do phải có; không thay nguồn thành PORTAL để né audit. Nếu C là lượng gộp, không sinh eater giả. Nhập hộ sau hạn đi qua change request giống mọi actor khác.

## 6. Quy tắc bổ sung

| BR | KHI / THÌ / ngoại lệ | Nguồn |
| :--- | :--- | :--- |
| BR-ORD-007 | KHI gửi tuần THÌ chỉ tài khoản và trả kết quả đúng từng ngày; không ngoại lệ guest | PRD FEAT-037; atomic/partial ORD-Q05 |
| BR-ORD-008 | KHI có revision mới THÌ snapshot cũ bất biến và nguồn kế hoạch không cộng trùng; không ngoại lệ retry | Thiết kế đề xuất ORD-Q10/14 |
| BR-ORD-009 | KHI tắt chọn món hoặc gỡ người THÌ không xóa lịch sử; hiệu lực tương lai cần policy | ORD-Q02/09 |
| BR-ORD-010 | KHI MENU thu hồi THÌ không nhận lựa chọn mới từ nguồn đó; xử lý lựa chọn/order cũ cần quyết định | FR-MENU-APV-004; ORD-Q12 |
| BR-ORD-011 | KHI FEAT-046/047 chưa qua O-03 THÌ không thu dữ liệu sức khỏe/không chạy gợi ý; không ngoại lệ consent giả | O-03 |
| BR-ORD-012 | KHI nhắc người THÌ dùng danh sách đủ điều kiện, kiểm lại trước gửi và dedupe event; chưa có kênh thì không gửi | Q-14, E1-Q04 |

## 7. Ma trận lỗi hợp nhất

Các mã mới prefix ORD là đề xuất adapter E6; không đổi mã AUTH/SYS gốc. Mọi lỗi log requestId, actor/scope, reason code an toàn, không QR token/PII/sức khỏe/cost. `details` không chứa dữ liệu khách khác.

| Mã | HTTP / trigger | Localization | UI message | Severity | Next action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-ORD-400-01 | 400 sai JSON, trường lạ, kiểu/ngày/enum | ord.invalid_request | Dữ liệu gửi chưa đúng định dạng. | Medium | Sửa trường được đánh dấu |
| ERR-ORD-401-01 | 401 phiên/QR hết hạn hoặc không hợp lệ | ord.session_expired | Phiên không còn hiệu lực. | High | Xác minh/đăng nhập lại |
| ERR-ORD-403-01 | 403 thiếu quyền, guest chọn tuần, tự duyệt | ord.forbidden | Bạn không được thực hiện thao tác này. | High | Kiểm phân quyền; không retry tự động |
| ERR-ORD-404-01 | 404 không tồn tại hoặc ngoài scope | ord.not_found | Không tìm thấy dữ liệu trong phạm vi của bạn. | High | Chọn lại; không tiết lộ tồn tại |
| ERR-ORD-409-01 | 409 version cũ, đã khóa, nguồn đổi, mode tắt | ord.conflict | Dữ liệu đã đổi hoặc không còn mở. | High | Tải lại và xem khác biệt |
| ERR-ORD-409-02 | 409 cùng key khác body hoặc đang xử lý | ord.request_conflict | Yêu cầu đang xử lý hoặc mã đã được dùng. | High | Đối soát request gốc; IN_PROGRESS có Retry-After |
| ERR-ORD-422-01 | 422 món/cơ cấu/giá/định mức không hợp lệ | ord.invalid_selection | Lựa chọn không hợp lệ hoặc vượt định mức. | Medium | Chọn lại hoặc bổ sung nguồn |
| ERR-ORD-422-02 | 422 T<S+C hoặc delta làm âm số món | ord.total_too_small | Tổng suất nhỏ hơn số đã phân bổ. | Medium | Rà tổng và phân bổ; không tự xóa |
| ERR-ORD-422-03 | 422 thiếu total/default/snapshot để khóa | ord.incomplete_lock | Chưa đủ dữ liệu để khóa. | High | Vận hành xử lý theo ORD-Q07 |
| ERR-ORD-422-04 | 422 quan hệ khách/điểm/lịch sai, thiếu lý do/chứng cứ | ord.invalid_context | Phạm vi hoặc bằng chứng chưa đầy đủ. | Medium | Bổ sung đúng dữ liệu |
| ERR-ORD-429-01 | 429 vượt giới hạn cấu hình | ord.rate_limit | Vui lòng thử lại sau. | Medium | Retry-After, giữ key |
| ERR-ORD-500-01 | 500 lỗi transaction | ord.write_failed | Chưa thể xác nhận kết quả. | High | Tra requestId trước retry |
| ERR-ORD-503-01 | 503 phụ thuộc gián đoạn hoặc policy chưa cấu hình | ord.unavailable | Chức năng chưa sẵn sàng. | High | Xem reason DEPENDENCY_UNAVAILABLE/POLICY_UNCONFIRMED; không tự đổi policy |

## 8. NFR và phương pháp kiểm

NFR-ORD-001/002/003 giữ [SRS](spec.md). 1000 người đồng thời trong 10 phút **không đồng nghĩa 1000 TPS**. QA cần profile arrival, tỷ lệ đọc/đổi/retry, cấu hình máy và seed 2 khách; chưa đủ đầu vào để benchmark. Kiểm tải xác nhận p95 đọc≤300ms/ghi≤800ms và 0 lựa chọn thành công mất/trùng; đối chiếu resource/audit, không chỉ HTTP200. R6 pilot 2 khách/2 tuần chưa có dữ liệu.

Thiết kế UI kiểm 360/390/1440px, bàn phím, label và thông báo aria-live; không coi kiểm viewport là chứng nhận WCAG. NFR bảo mật kế thừa nền, thử IDOR/revocation/token log/data allowlist. Không thêm SLA/TPS từ template khác thay chỉ tiêu dự án.
''')
append('review/questions.md','''## Câu hỏi phát hiện khi hoàn thiện E6: tất cả CHỜ XÁC NHẬN

| Mã | Câu hỏi | Vai trò cần xác nhận | Tác động | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| ORD-Q11 | Người đặt tổng có thể quản lý nhiều khách/điểm không; role customer scope và audit QR guest/service lưu thế nào khi user_roles/sessions/audit_logs hiện yêu cầu user? | Gia Phát, Tech lead | FEAT-030–033; schema danh tính, TTL/rate limit và phân quyền | CHỜ XÁC NHẬN |
| ORD-Q12 | MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn? | DDV, vận hành | FEAT-036/039/040/048; không tự sửa lịch sử hay phát hành plan mới | CHỜ XÁC NHẬN |
| ORD-Q13 | Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày? | Người đặt tổng, BA | Unique eater/date/shift và UI hủy/zero order chưa có write contract | CHỜ XÁC NHẬN |
| ORD-Q14 | Bếp phải xác nhận nhận phiên bản kế hoạch mới không; ai phát hành/cho IN_PRODUCTION và xử lý bản in cũ? | Bếp trưởng, vận hành | FEAT-048/041; chưa tự tạo endpoint acknowledge/production-start | CHỜ XÁC NHẬN |
| ORD-Q15 | Nếu mở O-03: consent/version, rút đồng ý, thời hạn xóa/lưu log, phạm vi bệnh lý và tiêu chí gợi ý cụ thể? | Chủ sản phẩm, phụ trách dữ liệu | FEAT-046/047; chưa schema/API sức khỏe mới | CHỜ XÁC NHẬN |

ORD-Q01–10 giữ nguyên; không câu nào được đóng trong phiên này. Các câu mới không thay Q-14/Q-16/O-02/O-03/O-06 hoặc E1-Q01/02/04. Phiếu quyết định cần: mã, phương án được chọn, ví dụ, người xác nhận, ngày và nguồn bằng chứng; sau đó sửa đồng bộ FR/UC/API/data/UI/AC/test.
''')
write('srs/data-dictionary.md','Đối chiếu schema và từ điển delta E6','''Nguồn kiểm trực tiếp: [schema DBML dùng chung](../../nen-tang/srs/schema.dbml). Hiện có **65 bảng**; file DBML không thay trong phiên E6. Có bảng không đồng nghĩa schema được phê duyệt hoặc migration đã chạy. Các thiết kế dưới đây chưa merge.

## Quan hệ hiện hữu và khoảng trống

| Bảng / cột hiện hữu | Quan hệ / invariant | Kết quả rà và tác động |
| :--- | :--- | :--- |
| users / user_roles / sessions | Quyền/phiên nền | Phải bổ sung scope khách/điểm và guest; không giả user_roles đã có customer_id; ORD-Q11 |
| customer_qr_codes | customer_id FK, service_point_id nullable FK; token_hash unique; ACTIVE/ROTATED/REVOKED | Thiếu expiry/version/rotated successor; API version và TTL là delta ORD-Q02/11 |
| eaters | customer_id,service_point_id FK; user_id nullable unique | FK riêng không đảm bảo point thuộc cùng customer; nullable unique không chặn nhiều guest cùng người |
| service_schedules | unique(service_point_id,shift,weekday), weekday1..7 | Chưa hiệu lực theo khoảng ngày/lịch nghỉ; ORD-Q03; API không hứa đã lưu được bằng bảng hiện tại |
| customer_quotas | unique(customer_id,effective_from), meal_type_id FK, approved_by | Chưa khoảng hiệu lực/status hoặc bản chụp giá/cơ cấu; tránh sửa lịch sử khi meal_type thay |
| meal_selections | unique(eater_id,service_date,shift); point/menuDay/dish FK; source SELF/DEFAULT/COORDINATOR | Một dishId/selection; không đủ nhiều MAIN. Không thêm default gộp bằng eater giả. Chuyển điểm cần ORD-Q13 |
| selection_counters | PK(menu_day_id,service_point_id,shift,dish_id) | qty chỉ cache lựa chọn thuộc scope; phải đối soát trước lock; date suy từ menu_day không từ client |
| orders | unique(point,date,shift); total_servings NOT NULL; unit_price_vnd bigint; version | Khi chưa có tổng không tự insert T=0; summary có total=null trước order gửi. Một loại suất/điểm/ngày/ca; không tự mở đa loại suất |
| order_dish_lines | unique(order_id,dish_id); selected/default/coordinator | Ghi chú tổng mọi dòng=T chỉ đúng MAIN một món/suất. Không dùng lưu tất cả SIDE/VEG/SOUP rồi áp ghi chú đó |
| change_requests, approvals | Quy trình duyệt chung | Tránh hai workflow song song: order_change_requests đề xuất là extension liên kết approvals; cách reuse cần Tech lead chốt |
| audit_logs | actor_user_id NOT NULL FK users; on_behalf_user_id | Không chứa được guest/service không user một cách tự nhiên; phải thiết kế principal/service audit, không tạo người thật giả |
| eater_health_profiles | Đã có trong DBML | Không phải căn cứ mở FEAT-046/047; O-03 vẫn chặn, không thêm form/endpoint ghi |
| customer_price_terms / order_pricing_snapshots | Snapshot unique(order_id,order_version), context_status | Liên kết order revision với order_version đã chụp; không tạo nguồn giá bán song song |
| order_discount_records / events | pricing_snapshot_id, quantity_basis và policy chưa chốt | Order đổi chỉ tạo sự kiện cần rà; không tự giảm gross_amount_due, không tính lại chiết khấu thành đã chi |

## Từ điển delta đề xuất

Mọi ID là bigint biểu diễn chuỗi qua API; thời điểm UTC; ngày phục vụ theo Asia/Ho_Chi_Minh. `required` là yêu cầu thiết kế, không phải CHECK đã triển khai.

| Thực thể đề xuất | Thuộc tính / kiểu / nullability | Khóa, quan hệ và hành vi |
| :--- | :--- | :--- |
| order_revisions | id PK; order_id FK required; revision_no int≥1 required; order_version int≥1; base_revision_id nullable FK self; total_servings int≥0; menu_day_id/menu_version/quota_version/kitchen_id/meal_type_id required; deadline_at datetime required; pricing_snapshot_id nullable FK; source_snapshot JSON required; created_by principal,created_at,reason | unique(order_id,revision_no); base phải cùng order; pricing snapshot phải cùng order/version. Immutable; chưa resolve kế toán không giả snapshot giá đã đầy đủ; ORD-Q04/08 |
| order_revision_lines | id PK; revision_id FK; dish_id FK; recipe_id FK; portion_code; role; selected/default/coordinator int≥0; all required trong mô hình MAIN | unique(revision_id,dish_id,recipe_id,portion_code); snapshot tên/đơn vị giữ lịch sử; quy tắc SIDE riêng chờ ORD-Q10 |
| order_change_requests | id PK; order_id FK; base_revision_id FK; delta_lines JSON; reason string10..500; evidence_file_id nullable FK files; status PENDING/APPROVED/REJECTED/STALE; version int; created/last_modified principal; approval_ref nullable | base cùng order; không auto-approve; actor approval khác creator/last editor; liên kết approvals cần review; delta âm không âm quantity |
| production_plan_revisions | id PK; kitchen_id FK; service_date; shift; revision_no int; previous_id nullable FK; source_order_revision_ids JSON; lines_snapshot JSON; created_at; event_set_hash | unique(kitchen,date,shift,revision_no); đúng một revision mỗi order. JSON FK không được DB cưỡng chế: app kiểm mọi ID hoặc chuẩn hóa source table trước build |
| qr_sessions / identity binding | id PK; qr_id FK; principal/eater ref; scope JSON; issued/expires_at; revoked_at nullable; credential_hash | Khóa định danh và account/guest merge chờ ORD-Q01; chỉ proposal, không tự chọn phone/employeeCode/OTP |
| idempotency_receipts / outbox | request/event id; actor scope; route; body_hash; resource_ref; status; result; created_at; attempts | Ghi cùng transaction; event dedupe bền vững; request TTL24h đề xuất E1-Q02 không thay domain unique |
| choice_mode_versions / weekly receipt | customer,effective_from,enabled,version; batchId,policy,per_day_receipts | ORD-Q05/09; chưa thêm bảng vào schema; không hứa đã có persistence |

Không migration/DDL được phát hành. Tech lead phải chọn reuse vs extension, chuẩn hóa source rows và duyệt transaction/retention trước chuyển đặc tả thành schema triển khai.

```mermaid
erDiagram
  orders ||--o{ order_revisions : proposed
  order_revisions ||--o{ order_revision_lines : immutable
  order_revisions ||--o{ order_change_requests : baseline
  order_pricing_snapshots o|--o{ order_revisions : pricing_reference
  production_plan_revisions }o--o{ order_revisions : source_set
  customers ||--o{ customer_qr_codes : existing
  customer_qr_codes ||--o{ qr_sessions : proposed
```
''')
write('ui/user-flow.md','User flow E6: chọn, chốt và phát hành','''[19 UC](../srs/usecase-diagram.md) là nguồn nhánh chi tiết; [quy tắc](../srs/operational-rules.md) chứa guard. Mọi nhánh đề xuất chờ mã câu hỏi tương ứng.

```mermaid
flowchart TD
  Q[Quét QR hoặc đăng nhập] --> I{Phiên và scope hợp lệ?}
  I -->|Không| X[Xác minh lại - không ghi]
  I -->|Có| M{Menu công bố - quota - còn mở?}
  M -->|Không| N[Hiện lý do chưa thể chọn]
  M -->|Có| C[Chọn một MAIN - xem toàn tổ hợp]
  C --> V{Giá và version hợp lệ?}
  V -->|Không| R[Hiện lỗi - tải lại]
  V -->|Có| S[Lưu lựa chọn và counter nguyên tử]
  S --> T[Người đặt tổng xem S và nhập T C]
  T --> A{T đủ và version còn đúng?}
  A -->|Không| R
  A -->|Có| U[Gửi tổng SUBMITTED]
  U --> D{Đến hạn - đủ total và default?}
  D -->|Không đủ| E[Cần vận hành - không phát hành]
  D -->|Đủ| L[Khóa revision và outbox]
  L --> P[Kế hoạch theo bếp - ca - món]
  P --> CH[Đề nghị đổi sau khóa]
  CH --> AP{Người khác duyệt - baseline đúng?}
  AP -->|Không| RE[Reject hoặc stale - giữ bản cũ]
  AP -->|Có| NE[Revision mới - delta - thông báo bếp]
```

Nhánh tuần: tài khoản → chọn từng ngày → preview kết quả → policy ORD-Q05 chưa chốt thì chặn gửi → khi được duyệt trả receipt atomic/per-day rõ. Nhánh nhập hộ: DDV chọn khách/điểm → nhập source/evidence → preview S/C/T → áp cùng validation/version/deadline; sau khóa chuyển đề nghị, không bypass.

Nhánh dữ liệu rỗng: chưa có menu/định mức → không có nút lưu khả dụng; thiếu dinh dưỡng → “Chưa có dữ liệu”, vẫn phân biệt với món không đủ điều kiện chọn. Mất mạng sau gửi → “Chưa xác nhận kết quả”, giữ request key để đối soát; không hiển thị thành công giả.
''')
append('srs/states.md','''## Bổ sung 0.2.0: job, đề nghị và kế hoạch

```mermaid
stateDiagram-v2
  [*] --> PENDING
  PENDING --> APPROVED: Người khác duyệt - baseline còn đúng
  PENDING --> REJECTED: Từ chối có lý do
  PENDING --> STALE: Order đã có revision khác
  APPROVED --> [*]
  REJECTED --> [*]
  STALE --> [*]
```

STALE là trạng thái đề xuất delta, không enum đã merge. Không sửa đề nghị đã quyết định; tạo đề nghị mới từ baseline mới. Sau APPROVED retry trả quyết định gốc, không tạo thêm revision.

Job khóa/tổng hợp đề xuất QUEUED→RUNNING→SUCCEEDED/FAILED/NEEDS_ATTENTION. FAILED/NEEDS_ATTENTION không đồng nghĩa order đã mở lại; đọc commit/receipt trước retry. Order DRAFT/SUBMITTED quá hạn nhưng thiếu dữ liệu không tự chuyển LOCKED hoặc total=0. IN_PRODUCTION và quyền phát hành chờ ORD-Q14, không có API start production trong gói này.

Kế hoạch là chuỗi snapshot bất biến v1→v2, không chuyển trạng thái v1 thành nội dung v2. Khi event cũ tới muộn, kiểm source revision và không hồi lui plan. QR ACTIVE→ROTATED/REVOKED giữ lịch sử; không có transition phục hồi token cũ. Phiên đã mở khi quay QR xử lý theo ORD-Q02.
''')
append('srs/flows.md','''## Đổi sau khóa và phát hành delta

```mermaid
sequenceDiagram
  actor C as Người đề nghị
  participant O as ORD
  actor A as Người duyệt
  participant DB as Transaction
  participant W as Outbox worker
  participant P as Kế hoạch
  C->>O: Đề nghị baseRevision và delta
  O->>DB: Lưu PENDING cùng audit
  A->>O: Quyết định với version
  O->>DB: Kiểm khác người tạo và baseline
  alt Gate đã chốt và dữ liệu hợp lệ
    DB->>DB: Revision mới - approval - outbox
    DB-->>O: Commit
    W->>DB: Đọc event bền vững
    W->>P: Thay đóng góp order bằng revision mới
    P-->>W: Plan version và delta
  else Tự duyệt hoặc stale
    DB-->>O: 403 hoặc 409 - không sửa order
  end
```
''')
append('userstories/backlog.md','''## Bổ sung 0.2.0: điều kiện review

19 mã story trên được giữ để không phá truy vết. [57 AC](acceptance-criteria.md), [19 UC](../srs/usecase-diagram.md), [RTM đầy đủ liên kết](../test/traceability.md) và [57 ca bổ sung](../test/review-test-cases.md) thay nhận định “chỉ có AC chọn/chốt”. Nội dung chi tiết mỗi story nằm ở UC/AC tương ứng số thứ tự; chưa story point hay nhãn sprint-ready. Story 017/018 chỉ đặc tả gate, chưa có happy path sức khỏe được duyệt.

Definition of Ready đề xuất: có người duyệt và nguồn quyết định cho các gate tác động; chốt API/data delta; fixture/expected được QA review; policy deadline/identity/version rõ. Definition of Done phần mềm phải gồm build, security/load test, evidence và pilot theo roadmap; tài liệu này không đạt thay phần mềm.
''')
