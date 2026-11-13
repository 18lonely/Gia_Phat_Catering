---
id: DOC-E8-SRS-SPEC-MD
title: "SRS E8: Website công khai"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# SRS E8: Website công khai

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

## 1. Giới thiệu

[Phạm vi 6 feature](../epic-spec.md); [nguồn và trạng thái](../review/dependencies.md). Public projection là tập dữ liệu đã lọc được phép công khai, không phải bảng nội bộ. Revision là bản nội dung/nguồn; version là token chống ghi đè. Lead là yêu cầu tư vấn, chưa phải customer CRM.

## 2. Tổng quan

Khách không cần tài khoản để xem nội dung/form; người quản trị dùng AUTH nền, quyền chi tiết chờ E8-Q08. Môi trường web desktop/mobile; HTML phiên này chạy offline, không kết nối dịch vụ. CMS/hosting/analytics/chống spam chưa chọn. DL-08 và R4 chưa có bằng chứng xong. E2/E3/E4 là SRS nháp, không contract freeze. [Điểm mở](../review/questions.md).

## 3.1 Functional requirements

| FR / feature | Ưu tiên / Actor | Tên | Input | Processing | Output | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-PUB-PAGE-001 / FEAT-054 | P0 / Khách truy cập | Xem trang giới thiệu | slug trang | Đọc đúng revision được phép xuất bản; chỉ trả trường công khai; liên kết dịch vụ/dự án/đối tác | Trang nội dung hoặc không tìm thấy | E8-Q08 |
| FR-PUB-BLOG-001 / FEAT-055 | P0 / Khách truy cập | Xem tin và bài viết | bộ lọc, page, slug bài | Danh sách chỉ bài công khai; mở chi tiết theo slug; không có bài thì danh sách rỗng | Danh sách/chi tiết và metadata công khai | E8-Q01/08 |
| FR-PUB-URLM-001 / FEAT-055 | P0 / Người quản trị nội dung có quyền | Chuẩn bị mapping WordPress | inventoryRef, URL nguồn, target, KEEP/REDIRECT, revision | Đối chiếu từng URL thuộc DL-08; phát hiện trùng, đích không công khai, vòng lặp; chưa có inventory không báo đủ | Bảng mapping nháp và danh sách chặn | E8-Q01/02 |
| FR-PUB-URLR-001 / FEAT-055 | P0 / Khách truy cập | Phục vụ URL cũ | URL cũ từ mapping đã duyệt | KEEP trả nội dung đúng; REDIRECT trả 301 đến đích công khai được duyệt, không open redirect; GET không kích hoạt mapping | HTTP 200 hoặc 301 với Location | E8-Q01/02 |
| FR-PUB-MENU-001 / FEAT-056 | P0 / Khách truy cập | Xem thực đơn mẫu có giá | publicSampleId, ngày hiển thị | Đọc projection đã cho phép công khai; đối chiếu menu/recipe/nutrition revision; không lấy price_cap làm giá bán; thiếu nguồn không hiện đầy đủ giả | Tuần mẫu, giá suất, định lượng, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính | E8-Q03/04 |
| FR-PUB-TRY-001 / FEAT-057 | P1 / Khách truy cập | Dựng thử thực đơn tuần | loại suất công khai, số suất nguyên dương, lựa chọn kiêng nguyên liệu | Kiểm đầu vào; chỉ yêu cầu bộ dựng khi policy được duyệt; không ghi menus/order, không gọi Agent E9; đầu ra là mẫu chưa áp dụng | Kết quả mẫu/không tìm thấy phương án hoặc BLOCKED | E8-Q05/04 |
| FR-PUB-LEAD-001 / FEAT-058 | P0 / Khách truy cập | Gửi form tư vấn | thông tin liên hệ tối thiểu, consent, nguồn, trialRef nếu có | Kiểm consent theo bản nội dung đã duyệt và trường bắt buộc; chỉ thành công khi có bản ghi bền vững kèm nguồn; không lưu hồ sơ sức khỏe | Mã tiếp nhận an toàn; CRM chưa đồng nghĩa đã nhận | E8-Q06/07 |
| FR-PUB-RELY-001 / FEAT-058 | P0 / Người được cấp quyền xử lý lead | Theo dõi điểm nối lead | leadRef, trạng thái bàn giao, receiptRef khi có | Đọc bản ghi cùng nguồn; chỉ đánh dấu đã bàn giao khi có receipt của bên nhận; không mở hồ sơ/phễu CRM E10 | Tình trạng chờ bàn giao/lỗi/đã có receipt | E8-Q06/07/11 |
| FR-PUB-EDIT-001 / FEAT-059 | P0 / Người soạn được cấp quyền | Soạn và sửa nội dung | loại trang/bài/banner, title, body, slug, mediaRefs, version | Kiểm quyền, slug, nội dung an toàn; ghi revision nháp và audit; không sửa ngầm revision đang công khai | Bản nháp với version mới | E8-Q08/09 |
| FR-PUB-PREV-001 / FEAT-059 | P0 / Người soạn được cấp quyền | Xem trước nội dung | contentId, revision | Xác thực quyền, render an toàn đúng revision; không public cache/index; GET không xuất bản | Bản xem trước có nhãn nháp | E8-Q08 |
| FR-PUB-PUBL-001 / FEAT-059 | P0 / Người được cấp quyền công bố | Yêu cầu công bố hoặc thu hồi | contentId, revision, action, lý do | Kiểm quyền/policy duyệt, media/URL và revision; đủ mới công bố/thu hồi và audit; policy chưa chọn giữ BLOCKED; cache phải phản ánh quyết định | Revision công khai hoặc trạng thái thu hồi | E8-Q08/09/02 |
| FR-PUB-MEDI-001 / FEAT-059 | P0 / Người quản trị nội dung có quyền | Quản lý ảnh và banner | fileRef, altText, vị trí banner, quyền sử dụng, version | Chỉ dùng file an toàn đúng quyền công khai; kiểm nơi đang dùng trước thay/gỡ; không lộ storage_key hoặc file riêng | Media metadata nháp và các vị trí sử dụng | E8-Q09/08 |

BR-PUB-001/010/012 áp mọi FR; quy tắc còn lại ghi phạm vi trong bảng dưới. Lỗi theo [ma trận](error-matrix.md); mỗi route có lỗi trong [catalog](../api/endpoint-catalog.json). Không dùng BLOCKED như HTTP chuẩn: đó là trạng thái tài liệu; runtime đề xuất lỗi nguồn/policy ERR-PUB-422-02 hoặc503-01 tùy nguyên nhân.

### Làm rõ chuyển bài cũ (FR-PUB-URLM-001 / FEAT-055)

Ngoài URL, gói DL-08 cần đối chiếu nội dung bài: mã bài gốc, tiêu đề, body, media tham chiếu, ngày công bố gốc, trạng thái và URL nguồn. Không tự lấy dữ liệu từ website thật trong phiên. Quy trình đề xuất: nhận bản xuất có provenance → lập inventory → chuyển body/media sang nháp E8, làm sạch HTML → so nội dung/ảnh/liên kết với bản nguồn → rà slug/canonical và mapping KEEP/301 → người có quyền xác nhận → chờ cutover. Cách import CMS hoặc thao tác thủ công chờ E8-Q01/08/09; không viết importer hay migration.

Mỗi bài cần bảng đối chiếu sourceId → contentRef/revision → targetPath; giữ nguồn/ngày gốc riêng thời điểm chuyển. Không dùng ngày chuyển thay ngày bài gốc. Media thiếu, bài trùng hoặc đã xóa tạo dòng ngoại lệ BLOCKED, không bỏ khỏi mẫu số100% URL. Kiểm lại lần chuyển phải phát hiện sourceId đã có, không nhân đôi bài. Nội dung mới chỉ là nháp cho đến khi qua FR-PUB-PUBL-001; không tự công bố vì import thành công. Xử lý ngày/metadata/slug và tài nguyên ngoài còn cần E8-Q01/02/09 xác nhận.

## 3.2 Business rules

| Mã | KHI → THÌ / ngoại lệ | Căn cứ và phạm vi |
| :--- | :--- | :--- |
| BR-PUB-001 | KHI phục vụ công khai THÌ dùng allowlist trường; không trả cost, giá nhập, cost %, khoản khoán, chiết khấu, dữ liệu khách/order/nội bộ qua HTML/JSON/meta/cache/error/media. Không ngoại lệ. | Yêu cầu người dùng; mọi FR |
| BR-PUB-002 | KHI hiển thị giá suất THÌ chỉ dùng giá có căn cứ cho phép công khai; price_cap, giá món và giá hợp đồng không tự thành giá công khai. Không ngoại lệ. | D-10; E8-Q03; MENU/TRY |
| BR-PUB-003 | KHI hiển thị mẫu THÌ giữ source/version/date, đủ 4 chỉ số và đơn vị với nhãn “ước tính từ định lượng sống”; thiếu không thành 0, danh sách dị ứng rỗng chưa chứng minh không dị ứng. | E2/E4 nháp; E8-Q04; MENU/TRY |
| BR-PUB-004 | KHI nhận URL cũ THÌ đối chiếu inventory DL-08; chỉ đích hợp lệ mới kích hoạt KEEP/301; chặn loop, đích nháp và open redirect. Bài xóa/trùng chưa có policy giữ BLOCKED. | FEAT-055/R8; URLM/URLR |
| BR-PUB-005 | KHI dựng thử THÌ đầu vào chỉ nhu cầu suất tập thể/kiêng nguyên liệu, không bệnh lý/hồ sơ cá nhân; kết quả mẫu không đặt hàng, báo giá cam kết hay công bố menu. Không nới quy tắc cứng để có kết quả. | FEAT-057; E8-Q05; TRY |
| BR-PUB-006 | KHI nhận form THÌ chỉ báo tiếp nhận sau bản ghi bền vững kèm nguồn; consent chưa đủ thì không ghi; thiếu trialRef không bịa mẫu đã dựng. | R8/FEAT-058; E8-Q06; LEAD |
| BR-PUB-007 | KHI bàn giao lead THÌ giữ source/trialRef và identity bàn giao; chưa receipt thì chưa chuyển thành đã vào CRM. Không tự tạo hồ sơ E10. | FEAT-058; E8-Q06/07; RELY |
| BR-PUB-008 | KHI quản trị THÌ xác thực quyền từng thao tác, không suy quyền từ PER-05; dùng version và audit người/thời điểm/trước-sau/lý do; GET không sửa. | E1; E8-Q08; URLM/RELY/EDIT/PREV/PUBL/MEDI |
| BR-PUB-009 | KHI công bố THÌ đúng revision được cho phép và ảnh an toàn; chỉnh sửa tạo nháp; không phát tán draft/preview vào public cache/index. Nếu có duyệt áp nguyên tắc nền không tự duyệt. | E1; E8-Q08/09/12; EDIT/PREV/PUBL/MEDI |
| BR-PUB-010 | KHI thiếu quyết định hoặc nguồn THÌ giữ BLOCKED kèm mã; không lấy dữ liệu synthetic làm evidence thật. | Tất cả FR |
| BR-PUB-011 | KHI đo BO-09 THÌ giữ công cụ/định nghĩa organic/kỳ so sánh tương đương; chưa có baseline không tuyên bố đạt; URL test không chứng minh lưu lượng. | G-Next; E8-Q10 |
| BR-PUB-012 | KHI tham chiếu kế toán THÌ cost nguyên liệu gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn không là VAT 0%; CK %/tiền suất ghi khoản riêng theo đơn, không giảm phải trả. Không đưa các khoản nội bộ lên public. | Kế toán đã xác nhận; không thay CK/DATA-COST/NFR-COST-002 |

## 3.3 Giao diện ngoài

[API](../api/api-spec.md) · [mapping](../api/data-mapping.md) · [UI](../ui/screens.md). WordPress chỉ đầu vào inventory/nội dung được cung cấp, không kết nối trực tiếp phiên này. CRM chỉ port nhận lead tối thiểu, chưa mở E10. Không giao tiếp phần cứng.

## 3.4 NFR

| Mã | Nhóm | Chỉ tiêu / phương pháp | Test |
| :--- | :--- | :--- | :--- |
| NFR-PUB-001 | Bảo mật | 0 trường/dòng nội bộ lộ qua public response, SSR, meta/JSON-LD, cache, lỗi, ảnh hoặc thông báo; thử allowlist lồng nhau và truy cập trực tiếp, không chỉ ẩn UI | TC-PUB-S01/02 |
| NFR-PUB-002 | Toàn vẹn | 100% lead đã báo tiếp nhận có record+source; retry/fault không tạo mất hoặc trùng; 100% công bố/sửa có audit; wire policy chờ E8-Q12 | TC-PUB-S03/04 |
| NFR-PUB-003 | Bảo toàn URL | 100% URL bài viết thuộc DL-08 đúng trang hoặc 301 theo R8; crawl nguồn/đích và so inventory, không tính synthetic làm nghiệm thu | TC-PUB-S05 |
| NFR-PUB-004 | Hiệu năng | Kế thừa mục tiêu nền 1000 người đồng thời p95 đọc ≤300ms/ghi ≤800ms, không phải1000TPS; profile public/cache cold-hot/generation cần E8-Q12 | TC-PUB-S06 |
| NFR-PUB-005 | Sử dụng | 360/390/1440px không tràn toàn trang; nhãn/focus/lỗi đọc được, bàn phím thao tác được; mục tiêu WCAG2.1AA theo nền, chưa audit đầy đủ | TC-PUB-S07 |
| NFR-PUB-006 | Riêng tư | Không thu dữ liệu sức khỏe; consent chưa tick không tạo lead; không PII trong URL/query/analytics/log; chỉ quyền được cấp đọc lead; thời hạn lưu/xóa chờ E8-Q06 | TC-PUB-S08 |
| NFR-PUB-007 | An toàn nội dung | 0 script thực thi từ body/upload; không preview public; chặn CSRF khi dùng cookie, kiểm quyền/IDOR; TLS theo nền, không secret client | TC-PUB-S09 |
| NFR-PUB-008 | Đo lường | BO-09: phiên organic sau60 ngày ≥90% trước chuyển đổi, công cụ và cửa sổ E8-Q10; không kết luận khi baseline thiếu/0 | TC-PUB-S10 |

Các con số nền được kế thừa theo SRS dự án, không lấy1000TPS/SLA template để tự đổi. Public site24/7, RPO/RTO/cutover/caching cần review E8-Q11/12, chưa cam kết profile mới. NFR-PUB-001/006 là ràng buộc bắt buộc; còn implementation chờ kỹ thuật.

## 3.5 Lỗi và 4. Phụ lục

[Ma trận lỗi](error-matrix.md) · [state diagrams](states.md) · [delta dữ liệu](data-dictionary.md) · [UC](../usecases/index.md) · [RTM](../test/traceability.md).
