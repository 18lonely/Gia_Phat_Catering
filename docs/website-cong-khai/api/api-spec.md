---
id: DOC-E8-API-API-SPEC-MD
title: API đề xuất E8
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# API đề xuất E8

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E8-Q12 |


Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

## Quy ước và ranh giới

16 HTTP endpoint đề xuất, không server chạy. REST/JSON UTF-8, prefix /v1, HTTPS; admin AUTH nền và quyền theo thao tác, chưa gán role. Không mở HTTP CRM public. GET không ghi domain (ngoại trừ access telemetry tối thiểu theo policy), preview không cache công khai. Catalog là thiết kế route, URL frontend cũ không phải /v1: handler website ánh xạ nguyên URL và trả200/301 thực ở URL truy cập; API-PUB-004 là giao diện logic cần adapter review E8-Q12.

ID chuỗi opaque ở public; id nội bộ không đủ làm quyền. Decimal có đơn vị, không tự chuyển missing thành0. Lệnh sửa có version; tạo có chống gửi lặp theo nền nhưng scope anonymous/TTL/receipt E8-Q12 chưa freeze. E1 dùng page/pageSize/error trực tiếp, E4 dùng cursor/envelope khác: không bê nguyên sang E8; wire envelope/phân trang chờ E8-Q12. Đầu vào không khai báo bị từ chối.

## Catalog

| ID | Method / path | FR | Request | Response | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-PUB-001 | GET /v1/public/pages/{slug} | FR-PUB-PAGE-001 | slug trang | Trang nội dung hoặc không tìm thấy | E8-Q08 |
| API-PUB-002 | GET /v1/public/articles/{slug} | FR-PUB-BLOG-001 | bộ lọc, page, slug bài | Danh sách/chi tiết và metadata công khai | E8-Q01/08 |
| API-PUB-003 | POST /v1/admin/public/url-maps | FR-PUB-URLM-001 | inventoryRef, URL nguồn, target, KEEP/REDIRECT, revision | Bảng mapping nháp và danh sách chặn | E8-Q01/02 |
| API-PUB-004 | GET /v1/public/legacy-resolution | FR-PUB-URLR-001 | URL cũ từ mapping đã duyệt | HTTP 200 hoặc 301 với Location | E8-Q01/02 |
| API-PUB-005 | GET /v1/public/menu-samples/{id} | FR-PUB-MENU-001 | publicSampleId, ngày hiển thị | Tuần mẫu, giá suất, định lượng, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính | E8-Q03/04 |
| API-PUB-006 | POST /v1/public/menu-trials | FR-PUB-TRY-001 | loại suất công khai, số suất nguyên dương, lựa chọn kiêng nguyên liệu | Kết quả mẫu/không tìm thấy phương án hoặc BLOCKED | E8-Q05/04 |
| API-PUB-007 | POST /v1/public/leads | FR-PUB-LEAD-001 | thông tin liên hệ tối thiểu, consent, nguồn, trialRef nếu có | Mã tiếp nhận an toàn; CRM chưa đồng nghĩa đã nhận | E8-Q06/07 |
| API-PUB-008 | GET /v1/admin/public/lead-handoffs/{id} | FR-PUB-RELY-001 | leadRef, trạng thái bàn giao, receiptRef khi có | Tình trạng chờ bàn giao/lỗi/đã có receipt | E8-Q06/07/11 |
| API-PUB-009 | PUT /v1/admin/public/contents/{id} | FR-PUB-EDIT-001 | loại trang/bài/banner, title, body, slug, mediaRefs, version | Bản nháp với version mới | E8-Q08/09 |
| API-PUB-010 | GET /v1/admin/public/contents/{id}/preview | FR-PUB-PREV-001 | contentId, revision | Bản xem trước có nhãn nháp | E8-Q08 |
| API-PUB-011 | POST /v1/admin/public/contents/{id}/publication | FR-PUB-PUBL-001 | contentId, revision, action, lý do | Revision công khai hoặc trạng thái thu hồi | E8-Q08/09/02 |
| API-PUB-012 | POST /v1/admin/public/media | FR-PUB-MEDI-001 | fileRef, altText, vị trí banner, quyền sử dụng, version | Media metadata nháp và các vị trí sử dụng | E8-Q09/08 |
| API-PUB-013 | GET /v1/public/articles | FR-PUB-BLOG-001 | bộ lọc/phân trang theo nền; E8-Q12 | items và thông tin phân trang đã duyệt | E8-Q01/08 |
| API-PUB-014 | GET /v1/public/menu-samples | FR-PUB-MENU-001 | bộ lọc/phân trang theo nền; E8-Q12 | items và thông tin phân trang đã duyệt | E8-Q03/04 |
| API-PUB-015 | GET /v1/admin/public/contents | FR-PUB-EDIT-001 | bộ lọc/phân trang theo nền; E8-Q12 | items và thông tin phân trang đã duyệt | E8-Q08/09 |
| API-PUB-016 | POST /v1/admin/public/contents | FR-PUB-EDIT-001 | Nội dung nháp mới; chưa có id/version trước tạo | id và revision nháp mới | E8-Q08/09 |

[Catalog JSON](endpoint-catalog.json) có auth/error/UI. [Ma trận lỗi](../srs/error-matrix.md).

## DTO logic và allowlist

| DTO | Trường logic | Presence / nguồn |
| :--- | :--- | :--- |
| PublicContent | publicId, slug, title, sanitizedBody, publicMedia, canonicalPath | Chỉ revision đã cho phép; không author login/audit/raw HTML/private file |
| PublicSample | publicId, label, days, publishedPrice, quantities, nutrients, allergens, estimateLabel, sourceLabel | Giá + định lượng +4 chỉ số +dị ứng bắt buộc để coi trang mẫu đủ; missing/stale không báo đủ |
| PublishedPrice | amount, currency, displayBasis, authorizationRef nội bộ, effectiveRange nếu policy chọn | Chưa có source chuẩn E8-Q03; authorizationRef không ra client |
| Nutrients | energyKcal, proteinG, fatG, carbG | Decimal/string≥0 với kcal/g; thiếu bất kỳ chỉ số không trả tổng một phần như đủ |
| TrialInput | publicMealTypeId, servings, excludedIngredientCodes | servings nguyên dương; giới hạn trên/danh mục E8-Q05; không tên người ăn, bệnh, sức khỏe/free text y khoa |
| TrialResult | trialRef, days, publicSummary, label, validationSummary | Không trả breakdown cost/rule detail nhạy cảm; expiry/storage E8-Q05/12 |
| LeadInput | contact fields, consent, consentTextVersion, source, trialRef? | Field bắt buộc chưa chọn E8-Q06; source là provenance server kiểm, trialRef optional khi chưa dựng, không giữ raw referer chứa PII |
| LeadReceipt | receiptRef, receivedStatus | Không trả contact/source nội bộ hoặc CRM id; receipt không đồng nghĩa CRM đã nhận |
| ContentDraft | type, title, body, slug, mediaRefs, version | type trang/bài/banner; quyền và duyệt E8-Q08; không mass assignment status/public flag |
| URLMapping | sourceURL, targetPublicPath, action, inventoryRef, revision | Required cho rà mapping; target theo host/path được duyệt, không arbitrary URL |
| MediaDraft | fileRef, altText, usageRightsRef, placements, version | fileRef thuộc files nền; không public storage_key; lịch/kích thước E8-Q09 |

Required/optional cuối, giới hạn chuỗi và serialization/nullability chờ E8-Q12; chưa freeze DTO. Chỉ giá được phép và dữ liệu public projection được truyền ra client; không gửi nguyên object E2/E3/E4 rồi ẩn UI. Response lỗi không có stack/raw query.

## Điểm nối E10 tối thiểu

PORT-PUB-LEAD-HANDOFF (chưa triển khai): leadRef + nguồn đã chuẩn hóa + thông tin liên hệ/consent được cho phép + trialRef/snapshot public nếu có → receiptRef + trạng thái bên nhận. Chưa có contract E10, nơi lưu tạm E8-Q06; trạng thái mặc định tài liệu là BLOCKED, không tự chọn queue/CRM/provider. Quyền nhận, dedup/retry/retention và kênh thông báo E8-Q06/07/12. Không gửi cost, giá hợp đồng, thông tin sức khỏe.

### Chuyển bài WordPress trong phạm vi URLM

API-PUB-003 chuẩn bị inventory/mapping và kết quả đối chiếu nội dung; content nháp tạo qua API-PUB-016, không tự công bố. sourceId/sourceHash/originalPublishedAt/mediaRefs cần giữ trong provenance delta, wire fields/import format chờ E8-Q01/08/09/12. Không thiết kế endpoint importer/chuyển đổi thật khi chưa có export và CMS. TC-PUB-S05 kiểm nội dung lẫn URL; RTM URLM bổ sung API-PUB-016/UI-PUB-06 cùng UC-PUB-003.

## Cache / fault / publication

Key public cache chỉ projection công khai đúng revision; không lẫn auth preview hoặc lead. Thu hồi phải ngăn trả bản cũ; cơ chế/p95 purge TTL E8-Q12. Lỗi ghi/audit không được trả thành công một phần; timeout cần đối soát receipt, không giả lưu rồi gửi lại bằng key mới. Lỗi notification độc lập kết quả lưu; không sửa producer E1–E7.

## Quy ước tài liệu liên epic — XC-04

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E8-Q12 — XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
