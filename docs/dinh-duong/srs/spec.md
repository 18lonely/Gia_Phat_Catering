# SRS: Dinh dưỡng E4

Phiên bản 0.1.2 · 2026-11-14 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.2 | 2026-11-14 | BA | Đổi tên công nghệ backend sang Rust/Axum theo D-22, CR-CORE-2026-001; không đổi FR |
| 0.1.1 | 2026-11-11 | BA | Liên kết hồ sơ bổ sung E1–E5/E6 khởi đầu; giữ quy tắc và điểm mở |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

## 1. Giới thiệu

E4/R4 bao phủ FEAT-019 và FEAT-020. Mục đích: quản lý nguồn thành phần và tính 4 chỉ số cho món, tổ hợp suất. Nguồn: [PRD](../../gia-phat/01-prd.md), [roadmap](../../gia-phat/02-roadmap.md), [ERD nền](../../nen-tang/srs/erd.md) mục 5.2–5.3. D-17 chỉ xác nhận loại nguồn, không cung cấp sẵn ấn bản hoặc số liệu dinh dưỡng.

Ngoài MVP: hồ sơ sức khỏe, mục tiêu nhóm người ăn FEAT-086, nhật ký cá nhân FEAT-087, tư vấn bệnh lý, tính dinh dưỡng thực phẩm chín hoặc tự tra cứu Internet bằng AI. `eater_health_profiles` có trong schema nhưng không thuộc gói này.

## 2. Tổng quan và phụ thuộc

Web nội bộ theo nền tảng Rust/Axum, MySQL (D-22, [CR-CORE-2026-001](../../nen-tang/cr/CR-CORE-2026-001.md)); tên API là thiết kế, không phải xác nhận stack đã chạy. Dùng recipe_items.qty_std (không tự chọn min/max); recipe ACTIVE hiệu lực theo ngày; O-02 về nhiều cỡ vẫn mở, đầu vào phải chỉ rõ recipeId. Gram phần ăn được khác lượng mua có hao hụt trong Cost.

Quyền **đề xuất chờ NUTR-Q01**: DINH_DUONG_VIEN có nutr.read/write/calculate; GIAM_DOC có nutr.read; vai trò khác chưa cấp mới. Agent chỉ gọi calculate/read qua giao quyền người dùng–dịch vụ; không tự sửa bảng thành phần. Phạm vi menu/cơ sở do quyền nền tảng kiểm, không tin kitchenId client. Mọi sửa số liệu có audit, lý do và version. Chưa thêm cổng chặn công bố MENU vì thiếu dinh dưỡng khi chưa có quyết định nghiệp vụ cho cổng đó.

### Công thức và thuật ngữ

`grams = qty_std × (1 nếu use_unit=g; grams_per_unit nếu khác g)`.
`edibleGrams = grams × edible_pct / 100`.
`component = edibleGrams × nutrientPer100g / 100`.
Món = tổng component; suất = tổng các món trong tổ hợp cụ thể. Công thức kế thừa ERD, cần NUTR-Q02 để áp dữ liệu thật. Không nhân thêm tỷ lệ hao hụt Cost; không tự đổi kcal từ macro; không áp hệ số mất chất khi nấu. Với gram thì bỏ qua gramsPerUnit; với kg/bìa/quả phải có quy đổi được xác nhận, không suy từ đơn vị mua.

Thiết kế tính Decimal và làm tròn HALF_UP 2 chữ số ở tổng cuối **đề xuất** (NUTR-Q04). UI/API luôn ghi **“ước tính từ định lượng sống”**, đơn vị kcal và g; thiếu một chỉ số/nguồn/quy đổi thì trả missing[] và totals=null, không trình bày tổng một phần như đầy đủ. Nguồn mới không ghi đè kết quả cũ. Chỉ số 0 hợp lệ khác dữ liệu thiếu; ediblePct=0 hợp lệ về miền số nhưng phải hiển thị cảnh báo để dinh dưỡng viên rà.

## 3. Yêu cầu chi tiết

### 3.1 Chức năng P0

| FR | Tên | PRD | Input | Xử lý | Output | BR | Lỗi |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-NUTR-REF-001 | Quản lý bảng thành phần | FEAT-019 | ingredientId, 4 chỉ số/100 g phần ăn được, ediblePct, gramsPerUnit, sourceEdition, sourceLocator, version, lý do | Kiểm kiểu và miền giá trị; bắt buộc nguồn D-17 có ấn bản và trang/mã thực phẩm; ghi giá trị hiện hành, bản lịch sử và audit trong một giao dịch; không ngầm dùng mặc định 100 khi chưa được người nhập xác nhận. | NutrientValue với version mới | BR-NUTR-001 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-NUTR-REF-002 | Kiểm độ phủ nguyên liệu | FEAT-019 | recipeIds của danh mục 30 món đã duyệt | Lấy tập nguyên liệu duy nhất từ đúng phiên bản công thức; đếm đủ 4 chỉ số, nguồn, đơn vị và tỷ lệ; chỉ số 0 hợp lệ khác null; trả thiếu theo nguyên liệu và món bị ảnh hưởng, không tự điền số. | Coverage: complete/total, missing[], recipeVersions | BR-NUTR-002 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-NUTR-CALC-001 | Tính dinh dưỡng món | FEAT-020 | recipeId ACTIVE, serviceDate, clientRevision | Theo từng dòng qty_std × hệ số gram × edible_pct/100 × chỉ số/100; cộng Decimal chưa làm tròn; không áp COST_AP_HAO_HUT, không suy năng lượng bằng 4-4-9; trả phân rã và nguồn. Recipe phải có hiệu lực ngày phục vụ. | Calculation DISH, 4 totals, breakdown, provenance, label | BR-NUTR-003 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-NUTR-CALC-002 | Tính dinh dưỡng tổ hợp suất | FEAT-020 | menuId, menuVersion, serviceDate, selectedItemIds, clientRevision | Kiểm món thuộc ngày và đủ số món theo meal_type; chỉ cộng món chọn và món cố định đúng một lần; không cộng tất cả lựa chọn chính, không lấy món đắt nhất của COST; gắn recipeId/version và nguồn vào kết quả. | Calculation MEAL theo tổ hợp tường minh | BR-NUTR-004 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |
| FR-NUTR-SNAP-001 | Xem kết quả và nguồn lịch sử | FEAT-020 | calculationId; quyền hiện tại | Kết quả tính thành công lưu bất biến inputs_snapshot và totals; GET trả bản cũ cùng isStale nếu nguồn hiện tại khác. Tính lại tạo id mới; không thay lịch sử hay biến bản tính thành bản duyệt thực đơn. | Calculation, sourceVersions, isStale, label | BR-NUTR-005 | Ma trận 3.4 theo điều kiện; tất cả API kiểm 400/401/403/404/500 |

### 3.2 Quy tắc

| Mã | KHI / THÌ | Ngoại lệ |
| :--- | :--- | :--- |
| BR-NUTR-001 | KHI thực hiện “Quản lý bảng thành phần” THÌ Kiểm kiểu và miền giá trị; bắt buộc nguồn D-17 có ấn bản và trang/mã thực phẩm; ghi giá trị hiện hành, bản lịch sử và audit trong một giao dịch; không ngầm dùng mặc định 100 khi chưa được người nhập xác nhận. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-NUTR-002 | KHI thực hiện “Kiểm độ phủ nguyên liệu” THÌ Lấy tập nguyên liệu duy nhất từ đúng phiên bản công thức; đếm đủ 4 chỉ số, nguồn, đơn vị và tỷ lệ; chỉ số 0 hợp lệ khác null; trả thiếu theo nguyên liệu và món bị ảnh hưởng, không tự điền số. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-NUTR-003 | KHI thực hiện “Tính dinh dưỡng món” THÌ Theo từng dòng qty_std × hệ số gram × edible_pct/100 × chỉ số/100; cộng Decimal chưa làm tròn; không áp COST_AP_HAO_HUT, không suy năng lượng bằng 4-4-9; trả phân rã và nguồn. Recipe phải có hiệu lực ngày phục vụ. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-NUTR-004 | KHI thực hiện “Tính dinh dưỡng tổ hợp suất” THÌ Kiểm món thuộc ngày và đủ số món theo meal_type; chỉ cộng món chọn và món cố định đúng một lần; không cộng tất cả lựa chọn chính, không lấy món đắt nhất của COST; gắn recipeId/version và nguồn vào kết quả. | Không; điểm chưa chốt xem sổ câu hỏi |
| BR-NUTR-005 | KHI thực hiện “Xem kết quả và nguồn lịch sử” THÌ Kết quả tính thành công lưu bất biến inputs_snapshot và totals; GET trả bản cũ cùng isStale nếu nguồn hiện tại khác. Tính lại tạo id mới; không thay lịch sử hay biến bản tính thành bản duyệt thực đơn. | Không; điểm chưa chốt xem sổ câu hỏi |

### 3.3 Phi chức năng và giao diện

| Mã | Yêu cầu / phương pháp kiểm | Trạng thái |
| :--- | :--- | :--- |
| NFR-NUTR-001 | R4: đủ 4 chỉ số cho 100% nguyên liệu của 30 món; đối soát 5 suất với số tính tay độc lập; lưu input/source và chênh lệch từng chỉ số | BLOCKED bởi DATA-NUTR-Q01 và NUTR-Q04, chưa tự gán dung sai |
| NFR-NUTR-002 | Kế thừa mục tiêu PRD p95 đọc ≤300ms, ghi ≤800ms, 1000 người đồng thời; tách báo cáo tính toán theo kích thước món/suất và cache lạnh/nóng | Profile tải/tổng dữ liệu cần QA duyệt; chưa đo |
| NFR-NUTR-003 | 100% request ngoài scope không lộ dữ liệu; audit và revision nguyên tử với cập nhật; fault injection rollback và thử IDOR | Chưa chạy |
| NFR-NUTR-004 | 100% nơi hiển thị tổng có nhãn ước tính, đơn vị và trạng thái thiếu/cũ; kiểm bàn phím và màn hình 390px/1440px | Wireframe ASCII là thiết kế, chưa test UI |

Giao diện: [API](../api/api-spec.md), [wireframe ASCII](../ui/wireframe-ascii.md), [user flow](../ui/user-flow.md). Không có giao tiếp phần cứng hoặc webhook công khai trong MVP. [ERD](erd.md) xác định dữ liệu; [RTM](../test/traceability.md) nối đến AC/test.

### 3.4 Ma trận lỗi

| Mã | HTTP | Trigger/log kỹ thuật | Localization key | Thông báo | Severity | Xử lý |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ERR-NUTR-400-01 | 400 | JSON/kiểu/field lạ không hợp lệ; log requestId, không token | nutr.400-01 | Yêu cầu chưa đúng định dạng. | Medium | Sửa trường được chỉ ra |
| ERR-NUTR-401-01 | 401 | Phiên không hợp lệ; log requestId, không token | nutr.401-01 | Vui lòng đăng nhập lại. | High | Đăng nhập |
| ERR-NUTR-403-01 | 403 | Thiếu quyền thao tác; log requestId, không token | nutr.403-01 | Bạn không có quyền thực hiện. | High | Liên hệ quản trị |
| ERR-NUTR-404-01 | 404 | Không tồn tại hoặc ngoài scope; log requestId, không token | nutr.404-01 | Không tìm thấy dữ liệu. | High | Chọn lại dữ liệu thuộc quyền |
| ERR-NUTR-409-01 | 409 | Version hoặc trạng thái nguồn đã đổi; log requestId, không token | nutr.409-01 | Dữ liệu đã thay đổi. | High | Tải lại và tính lại |
| ERR-NUTR-422-01 | 422 | Số âm/null, nguồn thiếu hoặc số vượt precision; log requestId, không token | nutr.422-01 | Thành phần dinh dưỡng chưa hợp lệ. | Medium | Kiểm trường báo lỗi |
| ERR-NUTR-422-02 | 422 | Thiếu thành phần/quy đổi/recipe hiệu lực; log requestId, không token | nutr.422-02 | Chưa đủ dữ liệu để tính. | Medium | Bổ sung nguyên liệu được liệt kê |
| ERR-NUTR-422-03 | 422 | Tổ hợp suất sai cấu trúc/trùng món; log requestId, không token | nutr.422-03 | Tổ hợp món chưa hợp lệ. | Medium | Chọn đúng số món |
| ERR-NUTR-500-01 | 500 | Lỗi giao dịch nội bộ; log requestId, không token | nutr.500-01 | Chưa thể hoàn tất. | High | Dùng requestId để đối soát; không tự coi đã lưu |

## 4. Điểm mở và bàn giao

[Sổ câu hỏi](../review/questions.md) là nguồn trạng thái; tất cả câu mới CHỜ XÁC NHẬN. [Gói review](../../gia-phat/review/mvp-e4-e5-handoff.md) có giới hạn kiểm tra và phần còn thiếu.

## Hồ sơ bổ sung để review ngày 11/11/2026

[Preview toàn hồ sơ](../preview.html) · [API](../api/api-spec.md) · [Luồng tuần tự](flows.md) · [Trạng thái](states.md) · [Gap](../gap-analysis.md). Gói bổ sung không tự đóng câu hỏi, thay quy tắc nghiệp vụ hoặc chứng minh backend đã triển khai. [Bàn giao](../../gia-phat/review/ba-completion-handoff.md).

## Liên kết phụ thuộc E6: bổ sung 11/11/2026

[Gói E6 để review](../../chon-mon-order/preview.html) · [Hợp đồng phụ thuộc](../../chon-mon-order/review/dependencies.md) · [Đối chiếu schema](../../chon-mon-order/srs/data-dictionary.md). E6 giữ nguồn công bố/quyền và quy tắc của phân hệ này; delta chưa merge, không thay gate hoặc chứng minh phần mềm đã triển khai.
