# Adapter E6 — dữ liệu công bố, provenance và lỗi

11/11/2026 · Draft BA. Nguồn đối chiếu: [E1](../../nen-tang/api/api-spec.md), [MENU](../../thuc-don-dinh-luong/api/api-spec.md), [NUTR](../../dinh-duong/api/api-spec.md), [API E6](api-spec.md). Không thống nhất envelope thay E1-Q01; không cấp người ăn quyền API tính nội bộ.

## Envelope tại ranh giới

| Miền | Success / error hiện có | E6 xử lý đề xuất |
| :--- | :--- | :--- |
| E1 | success/data/meta/timestamp; lỗi code/message/details/requestId | Chỉ dùng trường cần cho authorize/scope; không copy User/session đầy đủ |
| MENU | DTO theo nhóm; lỗi code/message/details/requestId; list page/pageSize | Chỉ menu PUBLISHED, đúng ngày/loại suất/scope; không copy cost/rule evidence |
| NUTR | success/data/error/meta/timestamp; lỗi error.fields và error.missing; list cursor | Đọc Calculation đủ provenance; adapter không truyền envelope/breakdown/error.missing raw |
| E6 | DTO trực tiếp; list items/page/pageSize/total; lỗi code/message/details/requestId | Đây là hình thức nháp E6, **không phải đã kế thừa thống nhất success envelope E1**; E1-Q01 còn mở |

Không chuyển cursor NUTR thành số trang E6 bằng phỏng đoán; SafeDish là projection theo nguồn xác định, không proxy nguyên danh sách nội bộ. RequestId E6 là correlation của lần gọi ngoài; upstream correlation chỉ phục vụ log vận hành có quyền. Không đưa stack/SQL/raw body/token vào details.

## Allowlist và provenance

| E6 output | Nguồn và điều kiện | Không được suy / không truyền |
| :--- | :--- | :--- |
| dishId/name/role/recipePortionLabel | Món thuộc menuDay/version PUBLISHED được phép đọc; định lượng gắn recipe đúng ngày | Không lấy recipe mới nhất thay snapshot; không đưa công thức/giá nguyên liệu vào label |
| priceVnd/comboPriceVnd/withinQuota | Giá bán công bố và đủ tổ hợp/định mức cùng phiên bản; tiền MENU integer đồng → E6 decimal string chính xác | Không dùng cost hoặc giá nhập thay giá bán; thiếu giá không suy0/withinQuota=true |
| allergens/allergenStatus | Danh mục dị ứng đã công bố; trạng thái có bằng chứng nguồn | Mảng rỗng không chứng minh an toàn; chưa có bằng chứng đầy đủ→UNKNOWN; tiêu chí KNOWN vẫn cần owner dữ liệu review |
| nutrition bốn chỉ số | Calculation đúng DISH hoặc MEAL, recipe/menuVersion/serviceDate và tổ hợp tương ứng | Không gắn tổng MEAL vào món DISH hoặc cộng cả3MAIN; không tính lại theo4-4-9 |
| nutrition.label | “ước tính từ định lượng sống” theo NUTR | Không biến thành giá trị dinh dưỡng sau nấu đã đo |
| nutrition.missing | Nhãn thiếu dữ liệu đã lọc, ví dụ chưa đủ nguồn/quy đổi | Không ingredientId, recipe nội bộ, giá hoặc nguyên văn message upstream |
| nutrition.sourceVersion | Tham chiếu logic tới provenance calculation + recipe/nutrient/menu/method versions | E6 chưa quy định kiểu/format/nullability; không giả một menuVersion đại diện toàn nguồn |

NUTR.sourceVersions gồm nhiều revision; SafeDish.sourceVersion đơn chưa có mapping hoàn chỉnh. Cần chọn opaque reference hoặc object allowlist và lưu provenance phía server trước freeze. SafeDish chưa biểu diễn calculation kind, isStale và calculatedAt; đây là gap review, không tự thêm field vào DTO. Thời điểm tính mới không tự chứng minh nguồn còn hiệu lực.

Khi NUTR thiếu dữ liệu, SRS NUTR yêu cầu totals=null, không trình bày tổng một phần. Trong DTO SafeDish đang làm phẳng, cả4chỉ số để null và missing có nội dung an toàn; không điền0. Giá trị0 từ Calculation đầy đủ là0thật. UC/AC dùng “totals=null” là nghĩa nghiệp vụ; không yêu cầu thêm trường totals trái DTO. Chính sách dùng Calculation stale hoặc fallback khi NUTR gián đoạn còn NUTR-Q03/ORD-Q04/12: không trả bản cũ như hiện hành hoặc tự bật degraded mode.

GET available-meals không tự gọi POST tính NUTR để ghi Calculation mới. Cách chuẩn bị/cache calculation, principal service và refresh nguồn cần dependency contract được review; không triển khai một luồng ghi ẩn dưới GET. Thiếu cache không đồng nghĩa thiếu nguyên liệu đã được xác nhận.

## Phân biệt kết quả và lỗi

| Tình huống đã authorize | E6 outcome đề xuất / đang có | Guard và thông điệp |
| :--- | :--- | :--- |
| Resource không tồn tại/ngoài scope |404 ERR-ORD-404-01 | Cùng thông điệp không tiết lộ khách khác; không tra chi tiết nguồn để trả lỗi có PII |
| Scope hợp lệ nhưng chưa có MENU/quota |422 ERR-ORD-422-01 theo AvailableMeals | Không trả dishes=[] như menu hợp lệ; thiếu nguồn được xác định khác timeout |
| NUTR trả422-02 thiếu dữ liệu đã xác định | Menu hợp lệ vẫn hiển thị trường dinh dưỡng null/missing theo UC016 | Không trả nguyên error.missing nội bộ; không tạo Calculation giả thành công |
| NUTR trả422-03 sai tổ hợp hoặc409 nguồn đổi | Không dùng số tổng đó; review mapping422-01/409-01 theo trigger E6 | Không coi sai tổ hợp là thiếu dữ liệu dinh dưỡng thông thường |
| Upstream timeout/5xx hoặc payload không đúng schema |503 ERR-ORD-503-01, reason DEPENDENCY_UNAVAILABLE đề xuất | Không kết luận không có menu/khách; không dùng giá0; retry GET có giới hạn cấu hình chưa chốt |
| E6 session hết hạn |401 ERR-ORD-401-01 | Xác minh lại; không nhầm401 của service gọi upstream là phiên người ăn hết hạn |
| Service upstream bị403/401 trong khi người ăn hợp lệ | Lỗi dependency/configuration, không yêu cầu người ăn cấp quyền nutr.calculate | Không nâng quyền người ăn; log kỹ thuật có quyền; mapping503 cần review |
| List trong scope hợp lệ không có kết quả |200 items=[] và total đúng phạm vi | Không bỏ scope khi đếm total; không dùng rỗng để che dependency lỗi |

Các mapping mới chỉ là đề xuất adapter; không thay mã ERR-NUTR/MENU/SYS hoặc ngầm chốt E1-Q01. Thứ tự kiểm: parse input an toàn → auth/scope → resolve nguồn → validate dependency → projection. Không công bố nguồn chi tiết trước kiểm quyền. Read retry không cần Idempotency-Key hoặc receipt ghi; mỗi lần vẫn authorize và kiểm source mới.

## Truy vết

FR-NUTR-DSP-001/FR-ORD-SEL-001, BR-ORD-006/010 → UC-ORD-016/007 → API-ORD-001/002 → UI-ORD-06 → AC-E6-016-1/2/3, TC-E6-SYS-05/09. [Evidence protocol](../test/evidence-protocol.md) áp dụng. Không thêm ca vào inventory99; provenance/fallback/envelope vẫn gap, không đóng RV hoặc NUTR-Q.
