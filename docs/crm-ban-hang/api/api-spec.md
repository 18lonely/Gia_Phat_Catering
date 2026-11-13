---
id: DOC-E10-API-API-SPEC-MD
title: API và điểm nối đề xuất E10
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# API và điểm nối đề xuất E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E10-Q13 |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Ranh giới và quy ước

23 HTTP endpoint + 7 port logic. Hai tên port E8/E9 là tham chiếu chính tên nguồn, không endpoint mới của nguồn. Chưa triển khai hoặc cố định giao tiếp. GET chỉ đọc. POST tạo tài nguyên sự kiện/phiên bản; không DELETE. Không gọi mô hình, gửi email hoặc tạo endpoint E11–E13.

Header đề xuất: Authorization theo E1, Content-Type application/json cho body, X-Request-Id; Idempotency-Key cho lệnh ghi. Scope khóa gồm actor/service đã xác minh + thao tác + key, so bodyHash. Cùng key/body trả tài nguyên cũ theo quyền hiện tại; khác body 409. Nhận lead còn kiểm sourceSystem + sourceRef + sourceRevision để không tạo trùng khi bên gửi đổi key. Thời hạn lưu khóa và quy tắc replay quá hạn chờ E10-Q13/E1-Q02; không tự chọn số ngày.

Id là chuỗi, không ép bigint thành số JavaScript. Ngày YYYY-MM-DD; timestamp UTC. Ngữ nghĩa biên hiệu lực và múi giờ ngày kinh doanh chờ E10-Q11; không tự chọn khoảng đóng hay nửa mở. Tiền decimal string theo nguồn Cost, số suất nguyên; null khác 0, trường tùy chọn vắng khác null. Version nguyên dương cho tài nguyên đã tồn tại; revisionNo là số bản nội dung, không thay version. Không nhận field lạ hoặc actor/approvedBy/status do client tự cấp.

Envelope thành công đề xuất theo E1: {success:true,data,meta:{requestId,page?,pageSize?,total?},timestamp}. Lỗi: {code,message,details:[],requestId}; details chỉ tên trường an toàn. Khác biệt nguồn còn E1-Q01; adapter chưa được duyệt thì không tuyên bố đã thống nhất. Phân trang/giới hạn tải dữ liệu chờ Q13; không mặc định lấy toàn bộ. HTTP 200 nhóm dữ liệu thiếu không là nguồn đầy đủ.

## Danh mục HTTP

| Mã | Method/path | FR | Quyền | Request | Success / response | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| API-CRM-001 | GET /v1/crm/customers/{id}/overview | FR-CUS-VIEW-001 | crm.read + phạm vi đối tượng | customerId, kỳ xem và phạm vi cơ sở | 200; Hồ sơ có các nhóm dữ liệu và trạng thái ĐỦ / THIẾU / CHƯA CÓ NGUỒN; không cộng phần chưa xác định thành 0 | E6-CG-01/08; E7-Q03/04/08; E10-Q01 |
| API-CRM-002 | POST /v1/crm/customer-contact-drafts | FR-CUS-CONT-001 | crm.write + quyền hành động riêng | customerRef, tên liên hệ, vai trò liên hệ, phương thức liên hệ, nguồn xác minh | 201; Bản nháp liên hệ có version và audit; khách chủ và điểm phục vụ không đổi | E10-Q01; E6-CG-08 |
| API-CRM-003 | POST /v1/crm/intakes | FR-CUS-LEAD-001 | crm.write + quyền hành động riêng | sourceSystem, sourceRef, sourceRevision, sourceHash, contactRef, consentRef, safeMenuRef nếu có | 201; Phiếu tiếp nhận và receipt của E10, chưa phải khách chủ hoặc hợp đồng; không trả dữ liệu nội bộ về E8/E9 | E8-Q06/07/12; E9-Q06/10/13; E10-Q13 |
| API-CRM-004 | POST /v1/crm/duplicate-reviews | FR-CUS-DUP-001 | crm.write + quyền hành động riêng | cặp customerRef, bằng chứng nghi trùng, nguồn và version của hai hồ sơ | 201; Đề nghị chờ duyệt với bản so sánh, nguồn và tập tham chiếu chịu tác động | E10-Q02/03; E6-CG-08 |
| API-CRM-005 | POST /v1/crm/duplicate-reviews/{id}/decisions | FR-CUS-MRG-001 | crm.write + quyền hành động riêng | reviewId, baseVersions, quyết định, lựa chọn trường và lý do | 201; Quyết định, nhật ký gộp, liên kết truy nguyên; không xóa hồ sơ gốc hoặc sửa snapshot tài chính | E10-Q03/04; E6-CG-08; O-06 |
| API-CRM-006 | POST /v1/crm/merges/{id}/reversals | FR-CUS-UNDO-001 | crm.write + quyền hành động riêng | mergeRef, versions hiện tại, lý do, bằng chứng và phân tích liên kết phát sinh sau gộp | 201; Bản hoàn tác có audit hoặc danh sách xung đột cần xử lý; hồ sơ lịch sử vẫn truy nguyên | E10-Q03/04; E6-CG-08 |
| API-CRM-007 | POST /v1/crm/customers/{id}/lifecycle-events | FR-CUS-LIFE-001 | crm.write + quyền hành động riêng | customerRef, trạng thái hiện tại, trạng thái đề nghị, evidenceRef, reason, version | 201; Sự kiện vòng đời có căn cứ và lịch sử; nhánh không đủ căn cứ giữ trạng thái cũ | E10-Q05/06; E6-CG-05/06/08 |
| API-CRM-008 | GET /v1/crm/customers/{id}/risk-signals | FR-CUS-RISK-001 | crm.read + phạm vi đối tượng | customerRef, khoảng quan sát, lịch điểm có phiên bản, sự kiện phục vụ có nguồn | 200; Tín hiệu có lý do, lịch/nguồn, hoặc CHƯA ĐỦ DỮ LIỆU; GET không chạy tác vụ đánh giá | E10-Q06; E6-CG-03/05/06/08; E7-Q02/03; Q-13 |
| API-CRM-009 | POST /v1/crm/opportunity-events | FR-SALE-OPP-001 | crm.write + quyền hành động riêng | opportunityRef nếu đã có, customerOrIntakeRef, stage đề nghị, ownerRef, evidenceRef, version | 201; Cơ hội và lịch sử giai đoạn; bảng phễu nêu định nghĩa mẫu số, thiếu thì chưa tính tỷ lệ | E10-Q07/08; E6-CG-08 |
| API-CRM-010 | POST /v1/crm/quote-revisions | FR-SALE-QUOT-001 | crm.write + quyền hành động riêng | quoteRef và baseRevision chỉ khi sửa báo giá đã có; opportunityRef, dòng loại suất/giá, điều kiện, hiệu lực đề nghị | 201; Phiên bản nháp mới; bản phát hành cũ bất biến, trạng thái duyệt không tự sao chép | E10-Q08/15; O-01; CK-Q01–10 |
| API-CRM-011 | POST /v1/crm/quotes/{id}/menu-attachments | FR-SALE-MENU-001 | crm.write + quyền hành động riêng | quoteRevision, menuRef, menuRevision, sourceHash, phạm vi dùng cho khách | 201; Tệp/nội dung thực đơn được phép và provenance; không tự sửa MENU hoặc dùng bản hiện hành động | E10-Q09; E9-Q06/12; O-02; NUTR-Q01–04; E8-Q04 |
| API-CRM-012 | POST /v1/crm/quotes/{id}/publications | FR-SALE-SAFE-001 | crm.write + quyền hành động riêng | quoteRevision, expectedHash, quyết định duyệt, evidenceRef, recipientScope | 201; Bản phát hành có hash và revision chỉ gồm trường khách được phép; lỗi không lộ cost | E10-Q08/09/13; O-06 |
| API-CRM-013 | POST /v1/crm/contracts | FR-SALE-CONT-001 | crm.write + quyền hành động riêng | customerRef, quoteRevision, acceptanceEvidenceRef, draftTerms, fileRefs | 201; Hợp đồng nháp có nguồn và các dòng giá đề nghị; chưa hiệu lực, không tạo order | E10-Q08/10/11; E6-CG-08 |
| API-CRM-014 | POST /v1/crm/contracts/{id}/activations | FR-SALE-ACTV-001 | crm.write + quyền hành động riêng | contractVersion, amendmentRef/amendmentVersion nếu kích hoạt phụ lục, signatureEvidenceRef, priceLines theo mealTypeRef, effectiveFrom, effectiveTo, salePriceBasis, vatRatePct | 201; Hợp đồng và bộ giá hiệu lực nhất quán, audit và nguồn phụ lục; không ghi giá ngược vào order đã chụp | E10-Q10/11/12; O-01; CK-Q01–10; E6-CG-08 |
| API-CRM-015 | POST /v1/crm/contracts/{id}/amendments | FR-SALE-AMND-001 | crm.write + quyền hành động riêng | contractRef, baseVersion, predecessorPriceRefs, giá đề nghị, from/to, reason, evidenceRef | 201; Phụ lục nháp và diff lịch sử; không sửa giá hoặc snapshot order cũ | E10-Q10/11/12; E6-CG-04/05/07; E7-Q05 |
| API-CRM-016 | GET /v1/crm/price-resolutions | FR-SALE-PRIC-001 | crm.read + phạm vi đối tượng | customerRef, mealTypeRef, serviceDate, sourceScope đã xác minh | 200; Một kết quả có nguồn hoặc UNRESOLVED; không dùng giá hiện tại thay snapshot lịch sử | E10-Q11/12/13; E6-CG-04/05/07/08/11; CK-Q01–10 |
| API-CRM-017 | GET /v1/crm/customers | FR-CUS-VIEW-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Danh sách tham chiếu khách thuộc quyền | E6-CG-01/08; E7-Q03/04/08; E10-Q01 |
| API-CRM-018 | GET /v1/crm/intakes/{id} | FR-CUS-LEAD-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Phiếu tiếp nhận và receipt an toàn | E8-Q06/07/12; E9-Q06/10/13; E10-Q13 |
| API-CRM-019 | GET /v1/crm/duplicate-reviews/{id} | FR-CUS-DUP-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Diff và trạng thái đề nghị | E10-Q02/03; E6-CG-08 |
| API-CRM-020 | GET /v1/crm/opportunities | FR-SALE-OPP-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Cơ hội, giai đoạn và phễu có định nghĩa | E10-Q07/08; E6-CG-08 |
| API-CRM-021 | GET /v1/crm/quotes/{id}/revisions/{revision} | FR-SALE-QUOT-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Báo giá nội bộ; cost/margin chỉ khi có quyền riêng | E10-Q08/15; O-01; CK-Q01–10 |
| API-CRM-022 | GET /v1/crm/quote-publications/{id} | FR-SALE-SAFE-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Chỉ CustomerQuoteProjection theo recipientScope | E10-Q08/09/13; O-06 |
| API-CRM-023 | GET /v1/crm/contracts/{id} | FR-SALE-CONT-001 | crm.read + phạm vi đối tượng | id/revision trong path; bộ lọc và phân trang theo Q13 | 200; Hợp đồng và lịch sử phụ lục theo quyền | E10-Q08/10/11; E6-CG-08 |

## DTO và validation

| DTO | Trường logic / kiểu / ràng buộc | Đầu ra / cấm |
| :--- | :--- | :--- |
| CustomerOverview | customerRef:Id; period:{from,to}; groups:{contacts,points,contracts,orders,revenue,feedback}; mỗi nhóm {state,sourceRef,sourceVersion,asOf,items} | Thiếu nguồn trả state + items null; không trộn tổng giữa kỳ hoặc nhóm quyền khác nhau. |
| ContactDraft | customerRef:Id, displayName:string, contactRole:string, channels theo Q01, sourceEvidenceRef:Id | Chỉ CRM draft; giới hạn trường/retention chưa chốt, không tạo users/customers. |
| Intake | sourceSystem:string được duyệt; sourceRef/revision/hash; contactRef/consentRef theo nguồn; safeMenuRef tùy chọn | Receipt:{intakeRef,receiptRef,receivedAt,state}; không raw hội thoại/sức khỏe/cost hoặc tự nhận đã duyệt. |
| DuplicateReview | leftRef/rightRef:Id khác nhau, baseVersions, evidenceRefs, fieldChoices, impactRefs | Không có thuật toán/score mặc định; tiêu chí phiên bản phải có quyết định Q02. |
| MergeDecision / Reversal | reviewRef/mergeRef, expectedVersions, decision, reason, evidenceRef; actor từ server | Trước/sau và link-map có scope; không xóa khách, audit hoặc giao dịch nguồn; xung đột mới chặn. |
| LifecycleEvent / RiskSignal | state/evidence/version; signal có evaluationRef, pointScheduleRefs, observationPeriod, completeness | Không có threshold/window mặc định; GET risk chỉ đọc bản đánh giá có sẵn; producer đánh giá chưa chốt Q06. |
| OpportunityEvent | customerOrIntakeRef, ownerRef, stage, evidenceRef, baseVersion; stage enum đề xuất ở states | Phễu đếm cơ hội duy nhất; denominator/cohort/asOf phải có định nghĩa Q07. |
| QuoteRevision | quoteRef/baseRevision bắt buộc khi sửa, vắng cả hai khi tạo lần đầu; lines:[{mealTypeRef,quotedPrice,salePriceBasis,vatRatePct}], terms, validity, menuAttachmentRefs | DRAFT mới; thiếu căn cứ giá/VAT giữ unresolved; không lấy giá ngưỡng meal_types làm giá bán. |
| InternalEconomics | costRef, sourceVersion, amount nullable, margin nullable, calculationDefinitionRef, status | Chỉ nội bộ có quyền economics.read; công thức margin Q15 chưa chọn, không suy từ CK. |
| CustomerQuoteProjection | publicationRef, quoteCode, revision, recipientDisplayName, permittedSaleLines, permittedTerms, validity, safeMenuAttachment | Chỉ allowlist này và các trường con đã duyệt; không InternalEconomics, source cost IDs, debug, audit, note nội bộ. |
| Contract / Amendment | customerRef, quoteRevision hoặc legacyEvidenceRef, fileRefs, status, version, predecessorRef; priceLines theo từ điển | Bằng chứng ký riêng; không có chữ ký giả. Phụ lục DRAFT không tự sửa price_terms ACTIVE. |
| PriceResolution | customerRef, mealTypeRef, serviceDate; kết quả state RESOLVED/UNRESOLVED, termRef/version, contractRef, amendmentRef, quotedPrice, salePriceBasis, vatRatePct | 0 hoặc nhiều giá khớp không resolve; không trả invoiceRequested=false thành VAT 0; không ghi order snapshot. |

## Quyền và bảo vệ dữ liệu

Quyền logic crm.read/write, crm.merge.approve, crm.merge.reverse, sale.quote.approve, sale.contract.activate, economics.read là đề xuất. E1 kiểm actor và scope server; Q03/08/10 quyết định người được cấp. Nhân viên soạn không mặc nhiên tự duyệt. Khách chỉ truy API-CRM-022 sau cơ chế recipientScope được duyệt, không lấy route nội bộ rồi ẩn cost. AIN và website không được đọc cost/biên lợi nhuận qua quyền người dùng.

Projection khách phải dựng từ allowlist mới, áp cho JSON, HTML/tệp xuất, tên tệp, metadata, URL và lỗi/cache; kiểm cả chuỗi ghi chú có số nội bộ trước phát hành. Không nhúng InternalEconomics vào DOM hoặc script rồi ẩn. Bản phát hành lưu hash riêng, cache tách theo scope và revision; thu hồi quyền kiểm lại khi tải. Cơ chế tải/tệp cụ thể chưa chốt Q13, không chọn URL công khai mặc định.

## Port và tích hợp

| Port | Chiều | FR / UI | Thông tin tối thiểu | BLOCKED |
| :--- | :--- | :--- | :--- | :--- |
| PORT-PUB-LEAD-HANDOFF | E8 → E10 | FR-CUS-LEAD-001 / UI-CRM-02 | leadRef, nguồn, contact/consent được phép, trialRef → receipt hoặc pending/error | E8-Q06/07/12; E10-Q13 |
| PORT-AIN-HANDOFF | E9 → E10 | FR-CUS-LEAD-001 / UI-CRM-02 | proposalRef, candidate revision/hash, contact/consent được phép → receipt hoặc pending/error | E9-Q06/10/13; E10-Q13 |
| PORT-CRM-ORDERS | E6 → E10 | FR-CUS-VIEW-001 / UI-CRM-01 | customer/point scope, kỳ → order refs, revision, số suất, nguồn và độ đầy đủ | E6-CG-01/03/04/05/06/08/11 |
| PORT-CRM-REVENUE | E7 → E10 | FR-CUS-VIEW-001 / UI-CRM-01 | customer scope, kỳ → số giao/nhận/tính tiền, revenue refs, trạng thái và nguồn | Q-13; E7-Q02/03/04/05/08 |
| PORT-CRM-MENU | MENU → E10 | FR-SALE-MENU-001 / UI-CRM-06 | menuRef/revision → projection được phép, hash, quyền chia sẻ và trạng thái nguồn | E10-Q09; O-02; E8-Q04; NUTR-Q01–04 |
| PORT-CRM-COST | Cost → nội bộ E10 | FR-SALE-QUOT-001 / UI-CRM-06 | tham chiếu thực đơn/cơ sở/ngày → cost có nguồn hoặc unresolved; không truyền khách | O-01; CK-Q01–10; DATA-COST-Q01–06; E10-Q15 |
| PORT-CRM-PRICING | E10 → E6/Cost | FR-SALE-PRIC-001 / UI-CRM-09 | customer/mealType/serviceDate → priceTerm/version/contract/amendment và căn cứ giá | E10-Q11/12/13; E6-CG-04/05/07/08/11 |

Không webhook công khai được chọn; không tự đặt chữ ký webhook, queue, retry, timeout hoặc SLA của nguồn. Nếu chọn webhook sau này cần chủ nguồn duyệt xác thực/replay và mapping trước mở. [Phụ thuộc](../review/dependencies.md).

## Lỗi và nguyên tử

400 sai cấu trúc, 401 phiên, 403 quyền, 404 ngoài scope/không tồn tại, 409 version/key/khoảng giá, 422 bằng chứng hoặc invariant, 503 gate/nguồn, 500 kết quả ghi chưa rõ. Mã chi tiết trong [ma trận](../srs/error-matrix.md). Ghi dữ liệu + audit + receipt phải cùng giao dịch; lỗi không báo thành công một phần. Kích hoạt giá kiểm chồng lấn trong cùng vùng khóa giao dịch. Timeout sau commit đối soát cùng khóa, không dùng key mới để né trùng.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.

## Các hành động chuyển trạng thái chưa có wire contract riêng

Ma trận trạng thái thể hiện các sự kiện nghiệp vụ để review, không khẳng định mọi cạnh đã có route runtime. Gửi/trả duyệt, chấp thuận/thu hồi/hết hạn báo giá và chấm dứt hợp đồng còn E10-Q08/10/13; không tự tạo endpoint hoặc chọn tác vụ nền khi chưa có quyết định. API-CRM-012 chỉ tạo bản phát hành sau kiểm bằng chứng duyệt, không thay toàn bộ quy trình duyệt. API-CRM-014 nhận amendmentRef/amendmentVersion khi kích hoạt một phụ lục thuộc hợp đồng; áp cùng kiểm nguyên tử và hiệu lực với bộ giá đầu. Phần workflow chưa đủ contract giữ BLOCKED, không tính route chưa tồn tại vào catalog.

## Quy ước tài liệu liên epic (XC-04)

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E10-Q13: XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
