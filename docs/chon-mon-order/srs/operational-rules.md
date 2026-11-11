---
id: DOC-E6-SRS-OPERATIONAL-RULES
title: Quy tắc vận hành và nhánh chi tiết E6
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Quy tắc vận hành và nhánh chi tiết E6

**Draft để review · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.**

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung thiết kế có điều kiện, không đóng gate |

Tài liệu này phân rã 19 FR trong [SRS](spec.md), không thay mã gốc. [Đối chiếu](../review/scope-assessment.md) phân biệt căn cứ và gate. Các chính sách mới dưới đây là **đề xuất**, không lấy sự tồn tại của API/wireframe làm bằng chứng phê duyệt.

## 1. Identity, phạm vi và quyền

| Actor | Cho phép | Giới hạn |
| :--- | :--- | :--- |
| Nhân viên cấp tài khoản được phân quyền | FEAT-030 gán người đặt tổng đúng khách | Không mặc định mọi DDV hay mọi quản trị có quyền cấp khách; ORD-Q01/ORD-Q11 |
| Người đặt tổng | QR/danh sách người ăn, định mức, tổng, chế độ, đề nghị đổi trong khách/điểm được giao | Không đọc cost; không duyệt đề nghị của chính mình; không giả DDV nhập nguồn ZALO |
| Người ăn tài khoản | Món công bố, lựa chọn bản thân; chọn tuần P1 | Identity lấy từ phiên, không chấp nhận eaterId/userId client; không đọc danh sách công ty |
| Người ăn QR guest | Món/lựa chọn bản thân trong scope phiên | Không tuần, không hồ sơ sức khỏe; cookie/IP không chứng minh duy nhất một người |
| DDV được giao khách | Dữ liệu phục vụ, nhập hộ có chứng cứ | Không mặc định được duyệt ngoại lệ; không tự ghi đè lựa chọn cá nhân |
| Bếp/quản lý cơ sở | Kế hoạch đã phát hành của cơ sở được giao | DTO kế hoạch không gồm tên người ăn hoặc sức khỏe; thao tác xác nhận nhận bản chờ ORD-Q14 |
| Scheduler/service | Khóa/nhắc/tổng hợp theo quyền service | Không mượn quyền quản trị toàn hệ thống; log actor service gắn users loại SERVICE; guest principal cần review ORD-Q11 |

Khách vãng lai FEAT-045 đọc phần công bố qua mặt tiền E8; không dùng `available-meals` có phạm vi order làm API public. Phiên QR cần company, allowedPointIds, allowedDates/shifts, eater identity, expiresAt, qrVersion; scope là giao giữa QR và phân công, không phải trường client tự gửi. QR không gắn điểm không có nghĩa được đọc toàn công ty. Chưa có policy identity/expiry cuối cùng: ORD-Q01/02/11. Token QR chỉ hash trong DB; không log raw token. Thu hồi token chặn tạo phiên mới; xử lý phiên cũ/lựa chọn chờ ORD-Q02.

## 2. Số suất và tổ hợp

- D-04: chọn 1 trong 3 MAIN. Cơm/món phụ/rau/canh cố định thuộc cơ cấu suất; giá kiểm **toàn tổ hợp**, không chỉ giá MAIN. Tổ hợp bằng định mức được phép, vượt 1đ bị chặn; dữ liệu thiếu không suy giá 0. Đổi quota/giá/menu giữa ngày chờ ORD-Q04.
- `S` đếm lựa chọn cá nhân hợp lệ trong điểm/ngày/ca; mỗi identity một suất là mô hình D-04. `C` đề xuất là số bổ sung cho người chưa có lựa chọn, không phải tổng theo món thay thế S. C chưa có identity phải có xác nhận nguồn/phạm vi; không thể tự chứng minh không trùng người — ORD-Q06.
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


## Kết quả review nhánh còn thiếu — 11/11/2026

[Bảng DR-01–04](../review/decision-review.md) dùng xác nhận có danh sách người ăn/người quản lý (E6-EVID-001) và tách phương án chưa duyệt. [E6-RV-01–08](../review/decision-findings.md) phải được xử lý trước freeze.

C có thể chuyển sang S khi người được chọn hộ tự chọn chỉ là đề xuất ORD-Q06; không tự trừ C gộp khi không biết người. Guard T>=S+C tại gửi tổng không đủ quyết định hành vi PUT khi S tăng sau đó. Kế hoạch từ các order đã khóa chưa đồng nghĩa đủ mọi điểm trong scope. Không tự chuyển IN_PRODUCTION do publish. Những điều này bổ sung nhánh cần review, chưa đổi chính sách đã duyệt.

## Bổ sung consistency độc lập — 11/11/2026

Xem [mapping consistency](../api/data-mapping.md) và [khóa/kế hoạch](lock-plan-review.md). Phân biệt token tổng, version order, revision order/plan; lock thành công không hứa plan đã sẵn sàng. Các trường completeness/ack/publish vẫn là delta review, chưa thêm vào catalog hoặc wireframe; không thay E6-EVID-001/002.
