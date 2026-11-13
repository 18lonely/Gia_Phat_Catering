---
id: DOC-E12-API-API-SPEC-MD
title: Hợp đồng API đề xuất E12
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Hợp đồng API đề xuất E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E12-Q18 |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## Ranh giới

Không endpoint nào đã triển khai hoặc freeze. [Catalog JSON](endpoint-catalog.json). Prefix /api/v1/e12 chỉ đặt chỗ cho consumer E12; không tạo route E2–E11 hoặc đóng gap producer.

| API | Method / Path | FR / màn | Request | Response data | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-FBR-001 | POST /api/v1/e12/feedback/ratings | FR-FB-RATE-001 / UI-FBR-01 | mealRef, ratingScaleRef, ratingValue, sourceScope | Đánh giá có receipt và trạng thái tiếp nhận | E12-Q01/02; E6 CG01/08 |
| API-FBR-002 | POST /api/v1/e12/feedback/cases | FR-FB-CASE-001 / UI-FBR-02 | mealRef, complaintCategoryRef, nội dung về bữa, caseVersion | Hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách | E12-Q02/03; E6 CG01/08; E7-Q02 |
| API-FBR-003 | GET /api/v1/e12/feedback/dish-selection-metrics | FR-FB-SELR-001 / UI-FBR-03 | ngày, khách, điểm, ca, dishRef, selectionSourceRef | Số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định | E12-Q04; E6 CG01–14, ORD-Q01–15, E6-EVID-001/002 |
| API-FBR-004 | POST /api/v1/e12/feedback/menu-proposals | FR-FB-PROP-001 / UI-FBR-04 | dishMetricRefs, feedbackRefs, menuRef, revision, ghi chú đề xuất | Đề xuất nháp cùng căn cứ và điều kiện kiểm lại | E12-Q04/05; DL-01; O-02 |
| API-FBR-005 | GET /api/v1/e12/reports/role-dashboards | FR-RPT-ROLE-001 / UI-FBR-05 | roleView, dateRange, customerRef, kitchenRef | Bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng | E12-Q06/07/08; E7-Q03/04; E10-Q07; E11-Q07/08 |
| API-FBR-006 | GET /api/v1/e12/reports/cost-percentages | FR-RPT-CPCT-001 / UI-FBR-06 | date, customerRef, kitchenRef, costResultRef | Cost % ngày có nguồn E3; ô theo khách chưa xác định khi thiếu công thức | E12-Q07/08; O-01; DATA-COST-Q01–06; E11-Q07/08 |
| API-FBR-007 | POST /api/v1/e12/assistant/price-review-proposals | FR-AIO-PRRV-001 / UI-FBR-07 | priceChangeRef, menuRef, menuRevision, scope | Đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn | AIO-Q01–06; E12-Q09; O-01/O-02 |
| API-FBR-008 | POST /api/v1/e12/assistant/menu-proposal-checks | FR-AIO-RCHK-001 / UI-FBR-07 | candidateRef, candidateRevision, menuSourceRef | Bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật | AIO-Q02/05/06; DL-01; E11-Q15; E12-Q09 |
| API-FBR-009 | POST /api/v1/e12/assistant/estimate-proposals | FR-AIO-ESTR-001 / UI-FBR-08 | estimateRef, estimateRevision, date, kitchenRef | Nháp diễn giải dự toán chờ người thật rà | AIO-Q01–06; E12-Q09; DATA-COST-Q01–06 |
| API-FBR-010 | POST /api/v1/e12/assistant/demand-proposals | FR-AIO-DEMR-001 / UI-FBR-08 | demandRef, planRevisionRef, estimateRef | Nháp diễn giải nhu cầu với thiếu nguồn rõ ràng | E11-Q01/03/13; E6 CG06; AIO-Q01–06 |
| API-FBR-011 | POST /api/v1/e12/assistant/price-deviation-proposals | FR-AIO-PDEV-001 / UI-FBR-08 | comparisonRef, priceSourceRefs, alertPolicyRef | Nháp giải thích; cảnh báo chính thức chưa xác định | E12-Q10; E11-Q07/08/14; AIO-Q01–06 |
| API-FBR-012 | POST /api/v1/e12/assistant/crm-summary-proposals | FR-AIO-CRMS-001 / UI-FBR-09 | customerRef, timeRange, CRM sourceRefs | Nháp tóm tắt và danh sách việc cần người thật rà | E10-Q01/05/06/13; AIO-Q01–06; E12-Q11 |
| API-FBR-013 | POST /api/v1/e12/assistant/quote-content-proposals | FR-AIO-CRMQ-001 / UI-FBR-09 | customerRef, quoteRevisionRef, menuRef, nguồn giá được phép | Nháp báo giá có nguồn và nhãn chưa phát hành | E10-Q08/09/13/15; AIO-Q01–06; E12-Q11 |
| API-FBR-014 | POST /api/v1/e12/assistant/data-answer-proposals | FR-AIO-DQA-001 / UI-FBR-10 | câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef | Câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu | AIO-Q01–06; E12-Q06/07/08/12; E10-Q15 |
| API-FBR-015 | POST /api/v1/e12/nutrition/group-targets | FR-NUTR-GRPT-001 / UI-FBR-11 | groupRef phi y tế, mục tiêu có sourceRef, effectiveRange, version | Mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu | NUTR-Q01–04; E12-Q13/14 |
| API-FBR-016 | POST /api/v1/e12/nutrition/group-menu-checks | FR-NUTR-GRPC-001 / UI-FBR-11 | groupTargetRef, targetVersion, menuRevision, nutritionCalculationRefs | So sánh có phiên bản hoặc chưa xác định | NUTR-Q01–04; E12-Q13/14; DL-01 |
| API-FBR-017 | POST /api/v1/e12/nutrition/diary-consents | FR-NUTR-DCON-001 / UI-FBR-12 | consentPolicyRef, explicitAgreement | Đồng ý có phiên bản hoặc nhật ký chưa bật | E12-Q15/16; E6 CG01/08; E1 NFR-PRIV-001 |
| API-FBR-018 | POST /api/v1/e12/nutrition/diary-meals | FR-NUTR-DREC-001 / UI-FBR-12 | consentRef, consumedMealRef, consumedAt, mealNutritionSnapshotRef | Bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng | E12-Q15/17; NUTR-Q01–04; E6 CG01/08/10 |
| API-FBR-019 | GET /api/v1/e12/nutrition/diary-meals | FR-NUTR-DVIW-001 / UI-FBR-12 | dateRange; subject từ phiên | Danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực | E12-Q15/16; E6 CG01/08; NUTR-Q03/04 |
| API-FBR-020 | POST /api/v1/e12/nutrition/diary-deletion-requests | FR-NUTR-DDEL-001 / UI-FBR-12 | consentRef, diaryScope, explicitDeleteConfirmation | Receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút | E12-Q15/16; E1 NFR-PRIV-001 |


## Quy ước request/response đề xuất

Header: phiên xác thực theo E1; Content-Type application/json cho POST; correlation requestId; version token khi có sửa; khóa chống lặp cho lệnh tạo/yêu cầu xóa theo Q18. Không chọn TTL, số retry hoặc cơ chế khóa. GET nhận filter trong query, không body, không ghi; phân trang/giới hạn và envelope cuối chờ E1-Q01 và Q18.

Nhánh thành công GET: 200 với success/data/meta/timestamp; data gồm kết quả đúng quyền, availability, provenance(sourceRefs, revision, asOf, scope), missingReason khi thiếu. POST nghiệp vụ nháp: 201 khi đã lưu và có receipt; đề nghị xử lý: 202 chỉ khi được nhận bền vững, không coi đã có kết quả. AI POST là yêu cầu đề xuất, không endpoint ghi nghiệp vụ; payload kết quả luôn reviewRequired=true, businessApplied=false. Không API tự áp dụng, tạo task CRM, tạo đơn mua, đổi công thức hoặc gửi báo giá.

Ví dụ **synthetic**, không phải contract nguồn:

```json
{"success":true,"data":{"metricDefinitionRef":"pending-selection-denominator","value":null,"availability":"MISSING_DEFINITION","missingReason":"E12-Q04","provenance":{"sourceRefs":[],"revision":null,"asOf":null,"scope":"synthetic-A"}},"meta":{},"timestamp":"2026-11-12T00:00:00Z"}
```

Lỗi 400/401/403/404/409/422/500/503 theo [ma trận](../srs/error-matrix.md), body gồm error.code/message/requestId và details đã lọc. Không trả raw upstream payload, SQL, token, dữ liệu khác scope hoặc cost ngoài quyền. Revision khác phải tải lại; retry cùng request không tạo bản trùng, mất phản hồi cần đối soát. Chưa có policy không tự cấu hình mặc định.

## Công cụ/port chỉ đọc

| Port logic đề xuất | Nguồn | Cho phép | Cấm / gate |
| :--- | :--- | :--- | :--- |
| PORT-FBR-MENU | E2 | Đọc catalog/recipe/menu theo revision; kiểm thuần FR-MENU-RUL-002 | Không ghi/duyệt/công bố; DL-01/O-02 |
| PORT-FBR-COST | E3 | Đọc kết quả cost/dự toán/giá đúng quyền; kiểm thuần trên ứng viên | Không sửa giá; AIO-Q06/CK/DATA-COST |
| PORT-FBR-NUTR | E4 | Đọc bản tính suất có sourceVersion | Không tự tạo nguồn/ngưỡng; NUTR-Q01–04 |
| PORT-FBR-CHOICE | E6 | Chỉ nhận lựa chọn thật phân biệt nguồn và revision khi contract được duyệt | CG/ORD/EVID chưa chốt; không thiết kế tiếp DTO nguồn |
| PORT-FBR-FIN | E7 | Đọc số doanh thu/công nợ đã có căn cứ | Không tính từ số giao; Q-13/E7-Q |
| PORT-FBR-CRM | E10 | Đọc hồ sơ, lịch, báo giá projection đúng quyền | Không CRUD, task, gửi; E10-Q01–15 |
| PORT-FBR-PUR | E11 | Đọc nhu cầu/đối chiếu mua có nguồn | Không PO, trừ tồn hoặc phân bổ mới; E11-Q01–15 |


Allowlist này là đề xuất contract, không xác nhận công cụ hiện hữu. FEAT-082 dùng MENU/COST; FEAT-083 dùng COST/PUR và tham chiếu E6; FEAT-084 chỉ CRM và nguồn E10 được phép; FEAT-085 dùng chỉ số được duyệt từ các port đọc. E5 kiểm giao quyền từng tool call, thu hồi giữa lượt và trước output; DB/service grants không cấp quyền ghi nghiệp vụ. E9/AIN không dùng quyền hoặc cache của AIO. Không webhook/callback công khai trong phạm vi; chưa có nhu cầu nên không đặt chữ ký giả.

Review người thật không đồng nghĩa ghi nghiệp vụ. Muốn chuyển sang E2/E10/E11 phải đi quy trình nguồn riêng sau các gate, chưa đặc tả adapter apply.

## Quy ước tài liệu liên epic (XC-04)

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E12-Q18: XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
