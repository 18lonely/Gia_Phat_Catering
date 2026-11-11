# SRS — Agent Nội bộ E5

Phiên bản 0.1.1 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 2026-11-11 | BA | Liên kết hồ sơ bổ sung E1–E5/E6 khởi đầu; giữ quy tắc và điểm mở |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

## 1. Giới thiệu

E5/R5 bao phủ FEAT-021–023 của [PRD](../../gia-phat/01-prd.md) và [roadmap](../../gia-phat/02-roadmap.md). Agent Nội bộ dựng/chỉnh bản nháp và ghi nhật ký. Không bao gồm agent khách R9, CRM, mua hàng, hỏi đáp báo cáo FEAT-082–085; không thêm khả năng gửi thông điệp bên ngoài, sửa giá, duyệt hoặc công bố.

## 2. Tổng quan và phụ thuộc

DINH_DUONG_VIEN dùng aio.run/create/apply và đọc run của mình; GIAM_DOC đọc log qua aio.logs.read (đề xuất chờ AIO-Q04). Người có MENU write vẫn phải có aio.apply. Quyền hữu hiệu là giao quyền tài khoản svc-agent-noi-bo và người dùng theo BR-SEC-009; kiểm lại mỗi tool call và trước apply. Không tái sử dụng service account/queue/prompt/quota của agent khách. Nền tảng AUTH/SYS cung cấp phiên, audit và phạm vi cơ sở.

MENU sở hữu danh mục ACTIVE, quy tắc và lifecycle duyệt; COST sở hữu con số, VAT, ngưỡng và evidence; NUTR tính 4 chỉ số nếu được gọi. AI chỉ lựa chọn/diễn giải kết quả công cụ, không tạo công thức hay tự tính tiền. R5 theo roadmap phụ thuộc R2/R3, không tự thêm R4 làm cổng mới: khi NUTR chưa sẵn sàng chỉ ghi dinh dưỡng chưa có, không bịa số và không gắn nhãn đầy đủ MVP.

### Trạng thái và kiểm soát

`QUEUED → RUNNING → DONE | FAILED`; đầu vào bị từ chối quyền/chính sách có thể ghi `REJECTED` sau xác thực. DONE có outcome `VALID | NEEDS_INPUT | NO_SOLUTION | BLOCKED_DATA`; FAILED có `TIMEOUT | DEPENDENCY_ERROR`. DONE không đồng nghĩa thực đơn đạt. Chỉ VALID có candidate áp dụng; không có kết quả một phần được gắn VALID. Mỗi run cố định input revision, nguồn/validator version và candidateHash; response đến muộn không mở lại trạng thái cuối.

Đầu ra R5 phải không vượt cost theo roadmap. Đề xuất chặn nhãn VALID của agent kể cả Cost ở CANH_BAO; không sửa cổng MENU vốn cho phép cảnh báo (AIO-Q02 chờ duyệt). Thiếu giá/VAT/bảng tính món đặc thù trả BLOCKED_DATA. Không tìm được tổ hợp trong giới hạn gọi tool hoặc 60 giây: NO_SOLUTION hoặc TIMEOUT; không nới quy tắc cứng, ngưỡng hay kiêng kỵ. Cảnh báo mềm được giữ nguyên, người dùng giải trình qua MENU.

Áp dụng là hành động tường minh của người dùng; ghi DRAFT nguyên tử, không đồng nghĩa gửi duyệt. Sau đó FEAT-013 kiểm lại theo cổng MENU/Cost. Nguồn PENDING/APPROVED/PUBLISHED không sửa qua agent; người dùng theo quy trình MENU để có bản DRAFT hợp lệ. Một run VALID chỉ áp dụng một lần; sửa tiếp tạo run mới. Trùng loại suất/tuần dùng quy tắc duy nhất của MENU, không tự tạo bản thứ hai.

Prompt, tên món và văn bản tool đều là dữ liệu không đáng tin. Công cụ allowlist chỉ đọc catalog, kiểm quy tắc, kiểm cost, tính dinh dưỡng tùy quyền; ghi MENU chỉ ở apply do server điều phối. Không cho model SQL, URL tùy ý, token dịch vụ, quyền phê duyệt hoặc điều chỉnh quota. Kiêng kỵ được kiểm trên cả nguyên liệu chính/phụ; dữ liệu không đủ thì hỏi lại/chặn, không cam kết an toàn dị ứng hoặc tư vấn điều trị.

## 3. Yêu cầu chi tiết

### 3.1 Chức năng P0

| FR | Tên | PRD | Input | Xử lý | Output | BR | Lỗi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-AIO-GEN-001 | Yêu cầu dựng thực đơn tuần | FEAT-021 | mealTypeId, weekStart, kitchenIds, exclusions{ingredientIds,dishIds}, requestText, idempotency key | Kiểm quyền giao giữa người dùng và dịch vụ; tuần bắt đầu thứ Hai; chỉ dùng danh mục ACTIVE và công thức hiệu lực. Đăng ký run bền vững trước gọi mô hình; ngữ nghĩa chưa rõ chuyển NEEDS_INPUT, không đoán kiêng kỵ. | 202 Run QUEUED; sau đó RUNNING rồi DONE/REJECTED/FAILED | BR-AIO-001 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-AIO-CHK-001 | Kiểm phương án bằng hệ thống | FEAT-021 | candidate với recipeId, ngày, cơ sở; revision và phiên bản tham số | Gọi FR-MENU-RUL-002 và API-COST-025 cho cùng hash phương án; hệ thống tính số, mô hình chỉ diễn giải. Chỉ VALID khi không vi phạm cứng, đủ đầu vào, không vượt ngưỡng từng ngày/cơ sở và không chứa món ngoài danh mục; giữ cảnh báo mềm, không tự viết lý do thay người duyệt. | Run outcome VALID/NO_SOLUTION/BLOCKED_DATA, bảng kiểm và evidence | BR-AIO-002 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-AIO-EDIT-001 | Chỉnh thực đơn bằng lời | FEAT-022 | menuId, baseVersion, instruction; hoặc candidateRunId, candidateRevision; đúng một nguồn | Diễn giải yêu cầu thành patch có ngày/slot/món cũ/mới; giữ phần ngoài mục tiêu; đọc toàn tuần để kiểm ảnh hưởng lặp và cost. Yêu cầu mơ hồ hỏi lại; thay đổi chỉ là candidate mới, không ghi menu. | 202 run con; diff và bảng kiểm mới | BR-AIO-003 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-AIO-APLY-001 | Áp dụng phương án thành bản nháp | FEAT-022 | runId, candidateRevision, baseVersion nếu sửa, idempotency key | Kiểm lại quyền, trạng thái nguồn DRAFT/CHECKED, version, danh mục, quy tắc và cost hiện hành. Nếu nguồn khác evidence: 409 yêu cầu chạy lại. Cùng giao dịch ghi toàn tuần DRAFT, source=AGENT_INTERNAL, agent_run_id, audit và applied_menu_id; không gửi duyệt/công bố. | 201 Menu DRAFT hoặc replay 200 cùng menu/version | BR-AIO-004 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-AIO-LOG-001 | Tra cứu nhật ký agent | FEAT-023 | runId hoặc cursor, khoảng ngày, userId, status | Chỉ đọc theo quyền log và cơ sở; lưu model/promptVersion, input/output tokens, chi phí ước tính/thực ghi nhận, outcome, tool event requestId và thời gian. Chi phí chưa biết là null + UNKNOWN, không phải 0; lọc token/bí mật và nội dung ngoài quyền. | RunLog phân trang, ToolEvent[], usage | BR-AIO-005 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-AIO-OPS-001 | Theo dõi và kết thúc lượt chạy lỗi | FEAT-023 | runId; deadline, quota và worker event | Tổng thời gian tính từ nhận yêu cầu gồm hàng đợi; deadline tối đa 60 giây theo roadmap. Lỗi provider/validator kết thúc FAILED; timeout không nhận kết quả đến muộn. Hạn mức riêng agent nội bộ do O-04/AIO-Q01 xác nhận; không dùng API-COST-036 dành cho agent khách. | Run FAILED/outcome TIMEOUT hoặc DEPENDENCY_ERROR; reject 429 khi hết quota | BR-AIO-006 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |

### 3.2 Quy tắc

| Mã | KHI / THÌ | Ngoại lệ |
| :--- | :--- | :--- |
| BR-AIO-001 | KHI thực hiện “Yêu cầu dựng thực đơn tuần” THÌ Kiểm quyền giao giữa người dùng và dịch vụ; tuần bắt đầu thứ Hai; chỉ dùng danh mục ACTIVE và công thức hiệu lực. Đăng ký run bền vững trước gọi mô hình; ngữ nghĩa chưa rõ chuyển NEEDS_INPUT, không đoán kiêng kỵ. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-AIO-002 | KHI thực hiện “Kiểm phương án bằng hệ thống” THÌ Gọi FR-MENU-RUL-002 và API-COST-025 cho cùng hash phương án; hệ thống tính số, mô hình chỉ diễn giải. Chỉ VALID khi không vi phạm cứng, đủ đầu vào, không vượt ngưỡng từng ngày/cơ sở và không chứa món ngoài danh mục; giữ cảnh báo mềm, không tự viết lý do thay người duyệt. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-AIO-003 | KHI thực hiện “Chỉnh thực đơn bằng lời” THÌ Diễn giải yêu cầu thành patch có ngày/slot/món cũ/mới; giữ phần ngoài mục tiêu; đọc toàn tuần để kiểm ảnh hưởng lặp và cost. Yêu cầu mơ hồ hỏi lại; thay đổi chỉ là candidate mới, không ghi menu. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-AIO-004 | KHI thực hiện “Áp dụng phương án thành bản nháp” THÌ Kiểm lại quyền, trạng thái nguồn DRAFT/CHECKED, version, danh mục, quy tắc và cost hiện hành. Nếu nguồn khác evidence: 409 yêu cầu chạy lại. Cùng giao dịch ghi toàn tuần DRAFT, source=AGENT_INTERNAL, agent_run_id, audit và applied_menu_id; không gửi duyệt/công bố. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-AIO-005 | KHI thực hiện “Tra cứu nhật ký agent” THÌ Chỉ đọc theo quyền log và cơ sở; lưu model/promptVersion, input/output tokens, chi phí ước tính/thực ghi nhận, outcome, tool event requestId và thời gian. Chi phí chưa biết là null + UNKNOWN, không phải 0; lọc token/bí mật và nội dung ngoài quyền. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-AIO-006 | KHI thực hiện “Theo dõi và kết thúc lượt chạy lỗi” THÌ Tổng thời gian tính từ nhận yêu cầu gồm hàng đợi; deadline tối đa 60 giây theo roadmap. Lỗi provider/validator kết thúc FAILED; timeout không nhận kết quả đến muộn. Hạn mức riêng agent nội bộ do O-04/AIO-Q01 xác nhận; không dùng API-COST-036 dành cho agent khách. | Không; điểm chưa chốt xem sổ câu hỏi |

### 3.3 Phi chức năng và giao diện

| Mã | Yêu cầu / phương pháp kiểm | Trạng thái |
| :--- | :--- | :--- |
| NFR-AIO-001 | R5: 20 yêu cầu thử khả thi, 100% thực đơn trả về đạt quy tắc cứng và không vượt cost, 0 món ngoài ACTIVE; mỗi thực đơn ≤60 giây từ lúc nhận gồm queue và tools. Timeout/từ chối không tính là mẫu đạt | BLOCKED bởi O-04, DL-01, AIO-Q03 và dữ liệu Cost |
| NFR-AIO-002 | Thời gian dựng tuần giảm ≥50% so trước MVP, bao gồm sửa và kiểm của người dùng; ghi thời gian từng mẫu trước/sau cùng độ khó, không thay bằng latency model | BLOCKED bởi AIO-Q03; chưa có baseline |
| NFR-AIO-003 | 100% run nhận hợp lệ có log bền vững kể cả timeout/crash; apply một lần, tuần/audit nguyên tử; kiểm mất response, worker lặp và fault injection | Chưa chạy |
| NFR-AIO-004 | 0 thao tác vượt giao quyền; 0 secret trong response/log hiển thị; thử prompt injection, IDOR, thu hồi quyền giữa run và apply | Chưa chạy |

Giao diện: [API](../api/api-spec.md), [wireframe ASCII](../ui/wireframe-ascii.md), [user flow](../ui/user-flow.md). Không có giao tiếp phần cứng hoặc webhook công khai trong MVP. [ERD](erd.md) xác định dữ liệu; [RTM](../test/traceability.md) nối đến AC/test.

### 3.4 Ma trận lỗi

| Mã | HTTP | Trigger/log kỹ thuật | Localization key | Thông báo | Severity | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-AIO-400-01 | 400 | Sai kiểu, tuần hoặc hai nguồn revision cùng lúc; log requestId, không token | aio.400-01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa đầu vào |
| ERR-AIO-401-01 | 401 | Phiên không hợp lệ; log requestId, không token | aio.401-01 | Vui lòng đăng nhập lại. | High | Đăng nhập |
| ERR-AIO-403-01 | 403 | Thiếu quyền/vi phạm allowlist; log requestId, không token | aio.403-01 | Không được thực hiện thao tác này. | High | Kiểm quyền |
| ERR-AIO-404-01 | 404 | Run/menu ngoài scope hoặc không tồn tại; log requestId, không token | aio.404-01 | Không tìm thấy lượt chạy. | High | Chọn lại |
| ERR-AIO-409-01 | 409 | Nguồn hoặc candidate cũ/trạng thái không cho apply; log requestId, không token | aio.409-01 | Phương án cần được kiểm lại. | High | Chạy lại trước khi áp dụng |
| ERR-AIO-409-02 | 409 | Idempotency key dùng body khác; log requestId, không token | aio.409-02 | Mã yêu cầu đã được sử dụng. | High | Đối soát request gốc |
| ERR-AIO-422-01 | 422 | Input ngữ nghĩa không hợp lệ; run chưa VALID; log requestId, không token | aio.422-01 | Chưa có phương án hợp lệ để áp dụng. | Medium | Bổ sung dữ liệu hoặc chọn lại |
| ERR-AIO-429-01 | 429 | Hết quota/concurrency cấu hình; log requestId, không token | aio.429-01 | Đã đạt giới hạn lượt chạy. | High | Theo Retry-After; không đổi key để vượt quota |
| ERR-AIO-500-01 | 500 | Ghi run/audit/apply thất bại; log requestId, không token | aio.500-01 | Chưa thể hoàn tất. | High | Đối soát bằng key/runId |
| ERR-AIO-503-01 | 503 | Không nhận được tác vụ vào hàng đợi bền vững; log requestId, không token | aio.503-01 | Dịch vụ đang gián đoạn. | High | Thử lại cùng key |

## 4. Điểm mở và bàn giao

[Sổ câu hỏi](../review/questions.md) là nguồn trạng thái; tất cả câu mới CHỜ XÁC NHẬN. [Gói review](../../gia-phat/review/mvp-e4-e5-handoff.md) có giới hạn kiểm tra và phần còn thiếu.

## Hồ sơ bổ sung để review — 11/11/2026

[Preview toàn hồ sơ](../preview.html) · [API](../api/api-spec.md) · [Luồng tuần tự](flows.md) · [Trạng thái](states.md) · [Gap](../gap-analysis.md). Gói bổ sung không tự đóng câu hỏi, thay quy tắc nghiệp vụ hoặc chứng minh backend đã triển khai. [Bàn giao](../../gia-phat/review/ba-completion-handoff.md).

## Liên kết phụ thuộc E6 — bổ sung 11/11/2026

[Gói E6 để review](../../chon-mon-order/preview.html) · [Hợp đồng phụ thuộc](../../chon-mon-order/review/dependencies.md) · [Đối chiếu schema](../../chon-mon-order/srs/data-dictionary.md). E6 giữ nguồn công bố/quyền và quy tắc của phân hệ này; delta chưa merge, không thay gate hoặc chứng minh phần mềm đã triển khai.
