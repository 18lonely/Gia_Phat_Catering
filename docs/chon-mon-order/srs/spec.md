---
id: DOC-CHON-MON-ORDER-SRS-SPEC
title: SRS E6 để review — Chọn món và Order
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# SRS E6 để review — Chọn món và Order

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |
| 0.2.1 | 2026-11-12 | BA | Làm rõ đọc/worker/gate, bỏ input thu sức khỏe khi O-03 chưa mở |

## 1. Mục đích, nguồn và trạng thái

Khởi đầu E6/R6 từ [PRD FEAT-030–048](../../gia-phat/01-prd.md), [roadmap](../../gia-phat/02-roadmap.md), D-14/D-19/D-21 và schema nền. Gói v0.2 có UC/API/data/UI/AC/test và RTM để review; nghiệp vụ còn gate nên chưa đủ điều kiện triển khai toàn bộ. FEAT-046/047 chỉ đặc tả cổng chặn, chưa đặc tả thu sức khỏe/gợi ý.

## 2. Tổng quan, quyền và số lượng

Người ăn chỉ sửa lựa chọn của chính mình; người đặt tổng chỉ công ty/điểm được gán; DDV nhập hộ có source/on_behalf; bếp đọc kế hoạch cơ sở mình. QR là cơ chế xác minh công ty, không đảm bảo một người một lựa chọn khi chưa chốt định danh ORD-Q01. Không cho client chọn eaterId tùy ý.

MVP chọn1 MAIN theo D-04, định mức chung D-21. Nếu loại suất cho nhiều MAIN thì phải chốt ORD-Q10 trước áp quy tắc tổng số suất/MAIN; schema hiện có một dishId/selection không đủ cho nhiều lựa chọn chính. Giá bán/menu/recipe chụp theo ngày phục vụ. Cost và khoản chiết khấu nội bộ không vào DTO người ăn.

T=totalServings người đặt tổng xác nhận; S=số suất có lựa chọn cá nhân; C=số nhập thêm cho người chưa chọn, không trùng danh tính đã tính ởS; D=T-S-C. Đề xuất kiểm T>=S+C, D>=0; tổng MAIN selected+coordinator+default=T chỉ trong mô hình một MAIN/suất. Số người có tài khoản không tự trở thành T. Khi T thấp hơnS+C phải hỏi/chỉnh có dấu vết, không xóa lựa chọn người ăn tự động.

## 3. Yêu cầu chức năng khởi đầu

| FR | Feature / Ưu tiên | Chức năng / Actor | Input | Xử lý | Output | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-AUTH-EXT-001 | FEAT-030 / P0 | Cấp tài khoản người đặt tổng; Gia Phát | customerId,userId,role,reason | Chỉ cấp trong công ty có quyền; quyền người đặt tổng theo company/service point. Không kế thừa quyền nội bộ; log cấp/thu hồi và kiểm scope mỗi request. | tài khoản công ty | ORD-Q01 |
| FR-AUTH-QREG-001 | FEAT-031 / P0 | Đăng ký người ăn qua QR công ty; Người ăn | qrToken,thông tin định danh được chốt | QR xác minh công ty theo D-19, không tự chứng minh duy nhất một người. Chỉ tạo/link eater sau kiểm QR ACTIVE và chính sách định danh ORD-Q01; không suy QR công khai là quyền đọc toàn công ty. | user/eater đã liên kết | ORD-Q01 |
| FR-AUTH-QSES-001 | FEAT-032 / P0 | Mở phiên QR không tài khoản; Người ăn qua QR | qrToken,serviceDate,định danh phiên | Phiên giới hạn một công ty/ngày/phạm vi; chống chọn trùng phụ thuộc định danh thật, không chỉ cookie/IP. Chưa chốt ORD-Q01 thì không tuyên bố giải quyết duplicate người. | phiên có scope và expiry | ORD-Q01 |
| FR-AUTH-QRM-001 | FEAT-033 / P0 | Quản lý QR và người ăn; Người đặt tổng | qrId/eaterId,action,version,reason | Đổi QR vô hiệu token cũ; gỡ người ăn không xóa lịch sử order/lựa chọn. Tác động phiên đang mở/lựa chọn trước chốt chờ ORD-Q02; quyền chỉ công ty mình. | QR/người ăn trạng thái mới | ORD-Q02 |
| FR-CUS-SVC-001 | FEAT-034 / P0 | Quản lý dữ liệu phục vụ tối thiểu; Dinh dưỡng viên | customer,servicePoint,kitchen,schedule | Điểm thuộc đúng khách; lịch theo ngày trong tuần/ca; cơ sở phục vụ xác định. Không tự mở CRM360/hợp đồng Later; thay đổi không sửa snapshot đã khóa. | dữ liệu phục vụ có version | ORD-Q03 |
| FR-ORD-QTA-001 | FEAT-035 / P0 | Đặt định mức công ty; Người đặt tổng | customerId,mealTypeId,effectiveFrom,version | Định mức chung theo D-21, giá và cơ cấu có hiệu lực; không người ăn tự trả chênh. Ai duyệt/thời điểm áp dụng khi đang chọn chờ ORD-Q04; thiếu định mức chặn chọn. | quota version | ORD-Q04 |
| FR-ORD-SEL-001 | FEAT-036 / P0 | Chọn hoặc đổi món trong ngày; Người ăn | menuDayId,dishId,servicePointId,date,shift,version,key | Chỉ menu PUBLISHED, món MAIN thuộc ngày, recipe/giá hiệu lực và tổ hợp trong định mức. Identity từ phiên; unique eater+date+shift; trước deadline server; sửa counter giảm món cũ/tăng món mới cùng transaction. | selection/version và tổng đúng | ORD-Q01, ORD-Q04 |
| FR-ORD-WEEK-001 | FEAT-037 / P1 | Chọn trước cả tuần; Người ăn có tài khoản | selections[],perDayVersion,key | Chỉ ngày có thực đơn công bố và còn mở; QR guest không dùng. Atomic cả tuần hay kết quả từng ngày chờ ORD-Q05; không báo cả tuần thành công nếu một ngày lỗi. | kết quả từng ngày có trạng thái | ORD-Q05 |
| FR-ORD-SUB-001 | FEAT-038 / P0 | Tổng hợp và chốt số suất; Người đặt tổng | point,date,shift,totalServings,coordinatorLines,version,key | Tách số tự chọn và số nhập thêm cho người chưa chọn. Đề xuất T>=S+C, dư T-S-C gán mặc định lúc khóa; T<S+C trả xung đột cần xử lý tường minh, không xóa lựa chọn cá nhân tự động. | order SUBMITTED và breakdown | ORD-Q06 |
| FR-ORD-DEF-001 | FEAT-039 / P0 | Gán phần chưa chọn về mặc định; Scheduler | scopeLock,deadline,menu/default snapshot | D-14: gán phần còn lại về default MAIN hợp lệ; không tạo người ăn giả cho suất chưa có định danh. Tổng số từ người đặt tổng, không dùng số người đăng ký làm total. Thiếu total/default thì trạng thái cần xử lý theo ORD-Q07. | qty_default và snapshot | ORD-Q06, ORD-Q07 |
| FR-ORD-LOCK-001 | FEAT-040 / P0 | Khóa số tại hạn chốt; Scheduler | point,date,shift,deadlineVersion | Dùng clock server; khóa cạnh tranh với selection/submission; snapshot order/line, audit và outbox nguyên tử; worker tạo kế hoạch riêng. Retry event không tạo v2. Ngưỡng15:00 D-1 là giả định Q-16 chưa duyệt. | order LOCKED + revision/outbox; plan có thể PENDING | Q-16, ORD-Q07 |
| FR-ORD-CHG-001 | FEAT-041 / P0 | Đề nghị đổi sau chốt; Người đặt tổng/nội bộ | orderId,baseVersion,deltaByDish,reason,evidence | Không sửa trực tiếp snapshot khóa. Đề nghị có delta +/-; đánh giá ngưỡng theo Q-16; duyệt khác người tạo/sửa cuối; nếu được duyệt tạo version mới và thông báo bếp. Không tự sửa số đã giao/đối soát của E7. | change request và revision nếu duyệt | Q-16, O-06, ORD-Q08 |
| FR-ORD-PXY-001 | FEAT-042 / P0 | Nhập hộ order; Dinh dưỡng viên | customer,point,date,shift,total,source,evidenceRef,reason | Ghi nguồn ZALO/PHONE theo quyền, người nhập thay và bằng chứng; không gửi Zalo. Áp cùng version/deadline/định mức; không tự ghi đè lựa chọn cá nhân. | order có nguồn nhập hộ | ORD-Q06 |
| FR-ORD-REM-001 | FEAT-043 / P1 | Nhắc người chưa chọn; Scheduler | scope,date,shift,eventId | Chỉ người đủ điều kiện chưa chọn; lọc scope/dedupe; kênh ngoài Q-14 chưa chốt. Không tự gửi SMS/Zalo/email khi chưa có cấu hình và quyền. | notification/integration outcome | Q-14 |
| FR-ORD-MODE-001 | FEAT-044 / P1 | Tắt chọn món theo khách; Người đặt tổng | customerId,enabled,effectiveFrom,version,reason | Khi tắt người đặt tổng nhập cho công ty. Đã có lựa chọn xử lý thế nào/hiệu lực giữa ngày chờ ORD-Q09; không âm thầm xóa lịch sử. | mode version | ORD-Q09 |
| FR-NUTR-DSP-001 | FEAT-045 / P0 | Hiển thị thông tin món cho người ăn; Người ăn | published menu/day/dish | Chỉ dữ liệu công bố: định lượng,4 chỉ số có nhãn ước tính,dị ứng và phạm vi tổ hợp; thiếu dữ liệu ghi chưa có, không điền0. DTO allowlist không có Cost/giá nhập/note nội bộ. | public-safe meal DTO | NUTR-Q03 |
| FR-NUTR-PROF-001 | FEAT-046 / P1 | Hồ sơ dinh dưỡng tự nguyện; Người ăn có tài khoản | Không nhận dữ liệu sức khỏe khi O-03 chưa mở | GATED O-03: chưa chốt phạm vi bệnh lý nên chưa xác định schema chi tiết/contract ghi sức khỏe. Không bật thu thập mặc định; tuân yêu cầu nền về consent,mã hóa và xóa khi thiết kế tiếp. | chưa mở contract triển khai | O-03 |
| FR-NUTR-REC-001 | FEAT-047 / P1 | Gợi ý món theo hồ sơ; Người ăn có tài khoản | Không nhận hồ sơ/consent hoặc yêu cầu tính gợi ý khi O-03 chưa mở | GATED O-03,FEAT-046: gợi ý không tự đổi lựa chọn/đặt suất; không tư vấn điều trị. Phải thiết kế riêng tiêu chí gợi ý, lý do và xử lý dữ liệu thiếu trước build. | gợi ý chưa đặc tả thuật toán | O-03 |
| FR-PLAN-MEAL-001 | FEAT-048 / P0 | Kế hoạch sản xuất theo món; Bếp trưởng/quản lý cơ sở | locked order version,kitchen,date,shift | Tổng hợp theo cơ sở/ca/món từ snapshot order đã khóa; hiển thị version và delta sau thay đổi. Không tính số món phụ bằng quy tắc tổng MAIN nếu suất có nhiều thành phần; quy đổi toàn cơ cấu theo ORD-Q10. | phiếu sản xuất theo món | ORD-Q10 |

### 3.1 Business rules đề xuất / kế thừa

| Mã | KHI / THÌ | Nguồn / trạng thái |
| :--- | :--- | :--- |
| BR-ORD-001 | KHI chọn món THÌ identity lấy từ phiên, dữ liệu thuộc scope, menu PUBLISHED, tổ hợp trong định mức | D-21; kiểm chi tiết ORD-Q04 |
| BR-ORD-002 | KHI ghi/đổi lựa chọn THÌ unique eater+date+shift, counter giảm cũ/tăng mới cùng transaction và version | Kế thừa schema; policy QR ORD-Q01 mở |
| BR-ORD-003 | KHI gửi tổng THÌ T>=S+C và D=T-S-C, không tự bỏ lựa chọn | ĐỀ XUẤT ORD-Q06 |
| BR-ORD-004 | KHI đến hạn chốt THÌ clock server quyết định, khóa cùng scope với writer, tạo snapshot/version một lần | Q-16/ORD-Q07 mở; không mặc định15:00 là đã duyệt |
| BR-ORD-005 | KHI đổi sau chốt THÌ lập đề nghị/delta, không sửa snapshot cũ; người duyệt khác người tạo/sửa cuối | Duyệt theo O-06/Q-16, ngưỡng chưa chốt |
| BR-ORD-006 | KHI trả dữ liệu người ăn THÌ allowlist chỉ trường công bố, không Cost/giá nhập/chiết khấu nội bộ | NFR-COST-006 và D-21 |

### 3.2 Lỗi hợp đồng ban đầu

| Mã | HTTP / trigger | Thông báo / xử lý |
| :--- | :--- | :--- |
| ERR-ORD-409-01 | 409 version/deadline snapshot đã đổi | “Dữ liệu đã thay đổi hoặc đã khóa. Tải lại trước khi chọn.” Không ghi selection/counter một phần |
| ERR-ORD-422-01 | 422 tổ hợp/món/định mức không hợp lệ | “Lựa chọn không thuộc thực đơn hoặc vượt định mức.” Chọn lại |
| ERR-ORD-422-02 | 422 T<S+C | “Tổng suất nhỏ hơn số đã phân bổ.” Người đặt tổng giải quyết, không xóa tự động |
| ERR-ORD-422-03 | 422 thiếu total/default/định mức tại lúc khóa | “Chưa đủ dữ liệu để khóa.” Chuyển xử lý vận hành theo ORD-Q07 |

Lỗi phiên401, quyền403, ngoài scope404, hệ thống500/503 kế thừa AUTH/SYS. Localization key đề xuất tương ứng ord.conflict/invalid_selection/total_too_small/incomplete_lock; severity Medium với422, High với409 khóa. Ma trận hợp nhất nằm tại [quy tắc vận hành mục7](operational-rules.md).

### 3.3 NFR / interfaces

| Mã | Chỉ tiêu / phương pháp |
| :--- | :--- |
| NFR-ORD-001 | R6:1000 người đồng thời trong10 phút trước chốt;0 lựa chọn thành công bị mất/trùng; p95 đọc≤300ms,ghi≤800ms theo nền; profile dữ liệu cần QA duyệt |
| NFR-ORD-002 | Tắt worker/API sau response thành công, retry cùngkey và race deadline: snapshot/counter/order không lệch; không tạo plan revision trùng |
| NFR-ORD-003 | Thử cross-company và QR token revoked;0 dữ liệu Cost/giá nhập lộ trong JSON,error,log hiển thị |

API ban đầu: [contract luồng chọn/chốt](../api/api-spec.md); mô hình [ERD](erd.md); [sequence](flows.md); [trạng thái](states.md). Mọi endpoint/schema là thiết kế, chưa code.

## 4. Câu hỏi và gate tiếp theo

[ORD-Q01–10](../review/questions.md), O-02/O-03/O-06,Q-14/Q-16. Chưa bắt đầu triển khai. Chi tiết bổ sung: [quy tắc vận hành](operational-rules.md), [UC](usecase-diagram.md), [data dictionary](data-dictionary.md), [RTM](../test/traceability.md), [wireframe](../html-wireframe/order-workbench.html), [AC](../userstories/acceptance-criteria.md). Các câu hỏi mở vẫn chặn baseline/triển khai; không lấy số liên kết làm độ hoàn tất nghiệp vụ.

## Bổ sung consistency độc lập — 11/11/2026

Xem [mapping consistency](../api/data-mapping.md) và [khóa/kế hoạch](lock-plan-review.md). Phân biệt token tổng, version order, revision order/plan; lock thành công không hứa plan đã sẵn sàng. Các trường completeness/ack/publish vẫn là delta review, chưa thêm vào catalog hoặc wireframe; không thay E6-EVID-001/002.

## Ranh giới thực thi UC — 12/11/2026

[Ma trận 19 UC](../review/uc-operation-review.md) phân loại theo catalog. FR-ORD-DEF-001 là bước trong PORT-LOCK của FR-ORD-LOCK-001, không commit/job thứ hai. FR-ORD-REM-001 do scheduler/worker khởi tạo; GET reminder-runs chỉ theo dõi. FR-PLAN-MEAL-001 tách worker tạo snapshot từ event với GET của bếp: đọc không build/publish/ack/start-production. FR-NUTR-DSP-001 không tạo Calculation qua GET; hai FR sức khỏe chỉ hiển thị gate. Input ở bảng là mô tả nghiệp vụ, wire shape theo API và mapping, không defaults/nullability mới. Grant cho A là phạm vi yêu cầu synthetic, không kết luận người đặt tổng chỉ thuộc một công ty.
