---
id: DOC-E12-API-DATA-MAPPING-MD
title: Mapping dữ liệu và chỉ số E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Mapping dữ liệu và chỉ số E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## Catalog chỉ số đề xuất cho bốn vai trò

Danh sách là phương án review E12-Q06, chưa mặc định cho từng vai trò. Mỗi số phải có sourceRefs/revision/asOf/scope/definitionRef; chỉ được tính theo công thức đã duyệt ở producer.

| Metric | Vai trò đề xuất | Chỉ số | Nguồn / provenance | Công thức | Mẫu số | Quyền |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| M-FBR-01 | PER-05 | Lựa chọn thật theo món | E6 lựa chọn phân biệt tự chọn/mặc định; Q04 và CG | Tử số: lựa chọn thật hợp lệ theo tập đo được duyệt; tỷ lệ = tử số / mẫu số × 100 chỉ sau Q04 | CHƯA CHỌN: người được mời chọn / số suất / người đã chọn | Quyền FB đọc theo khách/cơ sở; không PII thừa |
| M-FBR-02 | PER-05 | Đánh giá và khiếu nại | FB rating/case có receipt và trạng thái | Đếm bản ghi hợp lệ theo định nghĩa Q01–03; điểm trung bình chưa tính khi thang chưa duyệt | Số đánh giá hợp lệ nếu dùng trung bình, chờ Q01/02 | FB đọc; không mặc định xem danh tính người ăn |
| M-FBR-03 | PER-06 | Nhu cầu theo món/nguyên liệu | E6 planRevision; E11 demandRef | Đọc lượng nguồn; không gộp đơn vị khác, không tự trừ tồn | Không áp dụng cho lượng tuyệt đối | Theo cơ sở, không tự cấp cost |
| M-FBR-04 | PER-07 | Dự toán và đối chiếu mua | E3 estimateRef; E11 comparisonRef | Đọc tổng dự toán/thực mua; chênh theo công thức nguồn đã duyệt Q07/08 E11 | Theo định nghĩa BO-02 nguồn, chưa chốt | cost.cost.read và quyền PUR tương ứng |
| M-FBR-05 | PER-07, PER-08 | Doanh thu và công nợ khách | E7 FR-FIN-VIEW-001 và nguồn đối soát/thu | Doanh thu theo số tính tiền × giá snapshot E7; công nợ đọc kết quả nguồn, không tự tạo phương pháp mới | Không áp dụng cho tổng tiền; tập ngày/khách phải đủ | Quyền FIN đúng scope |
| M-FBR-06 | PER-05…08 chỉ nếu có quyền | Cost % thực đơn theo ngày/cơ sở | E3 FR-COST-MEAL-001, mục 3.3.2 | Cost suất / doanh thu chưa VAT × 100, làm tròn theo E3; cost suất A+B+E theo E3 | Ngưỡng giá loại suất / (1 + VAT_PCT / 100); giữ O-01/E2-Q1 | cost.cost.read; không suy quyền từ role |
| M-FBR-07 | PER-07, PER-08 nếu có quyền | Cost % dự toán theo ngày | E3 mục 3.3.4, estimateRevision | Tổng chi phí dự toán / doanh thu chưa VAT × 100, không thay cost % thực đơn | N × ngưỡng giá / (1 + VAT_PCT / 100); N và số món chính theo E3 | cost.cost.read; nguồn thiếu thì null |
| M-FBR-08 | PER-05…08 chỉ nếu được cấp | Cost % theo khách | E3 bản tính đủ nguồn; liên kết E6/E7/E10/E11 chưa freeze | CHỜ E12-Q08; không bình quân các tỷ lệ hoặc chia cho tiền khách trả | CHỜ Q08 về tập ghép và trọng số; giữ định nghĩa E3 | cost.cost.read cộng scope khách; không mở lợi nhuận E13 |
| M-FBR-09 | PER-08 | Tổng quan khách và phễu | E10 hồ sơ/cơ hội có revision | Đọc số nguồn; tỷ lệ chuyển đổi chờ E10-Q07 | Chờ E10-Q07; không lấy phiên bản báo giá làm cơ hội | Quyền CRM; margin không hiển thị khi chưa E10-Q15 |

Không dùng tỷ lệ FEAT-080 làm BO-05. Không suy tỷ lệ từ số sản xuất, số giao hoặc tổng order. Mẫu số 0/thiếu trả null, không gán 0 %. Không lấy trung bình cost % các ngày/khách.

## Mapping ba tầng

| UI / FR | API field | Dữ liệu logic / cột đề xuất | Nguồn và biến đổi |
| :--- | :--- | :--- | :--- |
| UI-FBR-01 / FR-FB-RATE-001 | API-FBR-001: mealRef, ratingScaleRef, ratingValue, sourceScope | feedback_rating | Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn. |
| UI-FBR-02 / FR-FB-CASE-001 | API-FBR-002: mealRef, complaintCategoryRef, nội dung về bữa, caseVersion | feedback_case | Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn. |
| UI-FBR-03 / FR-FB-SELR-001 | API-FBR-003: ngày, khách, điểm, ca, dishRef, selectionSourceRef | dish_metric_projection | Chỉ lấy lựa chọn thật của người ăn từ E6; phân biệt tự chọn với gán mặc định, nhập tổng và sản xuất. Chưa có mẫu số hoặc provenance đủ thì tỷ lệ null, không tự chọn trong ba mẫu số. |
| UI-FBR-04 / FR-FB-PROP-001 | API-FBR-004: dishMetricRefs, feedbackRefs, menuRef, revision, ghi chú đề xuất | review_proposal | Người dùng đọc dữ liệu có nguồn, tự chọn món cần rà; thiếu mẫu số không xếp hạng tỷ lệ. Lưu đề xuất nháp riêng, không tự đổi MENU; thay món hoặc định lượng phải qua E2, dị ứng và E3. |
| UI-FBR-05 / FR-RPT-ROLE-001 | API-FBR-005: roleView, dateRange, customerRef, kitchenRef | role_metric_projection | Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn. |
| UI-FBR-06 / FR-RPT-CPCT-001 | API-FBR-006: date, customerRef, kitchenRef, costResultRef | role_metric_projection | Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13. |
| UI-FBR-07 / FR-AIO-PRRV-001 | API-FBR-007: priceChangeRef, menuRef, menuRevision, scope | review_proposal | Chỉ đọc sự kiện giá E3 và thực đơn được phép; diễn giải ảnh hưởng và đề xuất đổi món hoặc định lượng có nguồn. Không ghi giá, công thức hay thực đơn. Không tự tính tiền. |
| UI-FBR-07 / FR-AIO-RCHK-001 | API-FBR-008: candidateRef, candidateRevision, menuSourceRef | review_proposal | Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO. |
| UI-FBR-08 / FR-AIO-ESTR-001 | API-FBR-009: estimateRef, estimateRevision, date, kitchenRef | review_proposal | Chỉ đọc dự toán E3 trong scope; giữ lượng mua, đơn vị, giá gồm VAT, khoản khoán và tổng từ hệ thống; AI chỉ giải thích, không tạo con số. |
| UI-FBR-08 / FR-AIO-DEMR-001 | API-FBR-010: demandRef, planRevisionRef, estimateRef | review_proposal | Đọc nhu cầu E11 và revision nguồn; phân biệt nhu cầu gộp với mua ròng. Chưa chốt trừ tồn/dự phòng thì không đề xuất lượng mua ròng; không tạo đơn mua hoặc chọn NCC. |
| UI-FBR-08 / FR-AIO-PDEV-001 | API-FBR-011: comparisonRef, priceSourceRefs, alertPolicyRef | review_proposal | Đọc so sánh E3/E11 cùng đơn vị, VAT, thời điểm và scope. Ngưỡng giá lệch chờ E12-Q10; không mượn BO-02 hoặc sai số NFR làm ngưỡng giá. |
| UI-FBR-09 / FR-AIO-CRMS-001 | API-FBR-012: customerRef, timeRange, CRM sourceRefs | review_proposal | Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ. |
| UI-FBR-09 / FR-AIO-CRMQ-001 | API-FBR-013: customerRef, quoteRevisionRef, menuRef, nguồn giá được phép | review_proposal | Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này. |
| UI-FBR-10 / FR-AIO-DQA-001 | API-FBR-014: câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef | review_proposal | Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược. |
| UI-FBR-11 / FR-NUTR-GRPT-001 | API-FBR-015: groupRef phi y tế, mục tiêu có sourceRef, effectiveRange, version | group_nutrition_target | Chỉ mục tiêu cấp nhóm người ăn; không danh sách bệnh lý, hồ sơ cá nhân hoặc suy nhóm từ sức khỏe. Nguồn chỉ số/công thức/ngưỡng chờ NUTR-Q01–04; chưa có thì chỉ nháp thiếu căn cứ, không kích hoạt. |
| UI-FBR-11 / FR-NUTR-GRPC-001 | API-FBR-016: groupTargetRef, targetVersion, menuRevision, nutritionCalculationRefs | group_nutrition_target | Đọc bản tính E4 cho tổ hợp suất có nguồn và mục tiêu được duyệt; thiếu công thức/ngưỡng thì chưa đánh giá. Không tự đặt mức kcal hoặc đổi kết quả thành cổng công bố MENU. |
| UI-FBR-12 / FR-NUTR-DCON-001 | API-FBR-017: consentPolicyRef, explicitAgreement | diary_consent | Tự nguyện, không chọn sẵn; nội dung chỉ bữa đã ăn và giá trị của suất. Không gọi FEAT-046/047; từ chối không ảnh hưởng chọn món. Chủ thể lấy từ phiên server; chi tiết identity E6 chưa chốt thì chặn nhận thật. |
| UI-FBR-12 / FR-NUTR-DREC-001 | API-FBR-018: consentRef, consumedMealRef, consumedAt, mealNutritionSnapshotRef | diary_meal | Chỉ nhận bữa đã ăn theo bằng chứng/chính sách E12-Q17; lựa chọn/order/giao nhận không tự chứng minh cá nhân đã ăn. Lưu liên kết tổ hợp và 4 giá trị E4, nhãn ước tính; không trường text sức khỏe, không suy lượng hấp thu. |
| UI-FBR-12 / FR-NUTR-DVIW-001 | API-FBR-019: dateRange; subject từ phiên | diary_meal | Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân. |
| UI-FBR-12 / FR-NUTR-DDEL-001 | API-FBR-020: consentRef, diaryScope, explicitDeleteConfirmation | diary_deletion_request | Xác thực chủ thể, cho xóa dữ liệu của mình theo nền ≤ 72 giờ; không xóa giao dịch nguồn E6/E7. Cơ chế bản sao/retention chờ Q16; receipt chỉ xác nhận nhận yêu cầu, không báo đã xóa khi chưa có evidence. |


Các trường trên là logic, không xác nhận DDL. Ngày API theo ngày nguồn ISO, UI dd/MM/yyyy; thời điểm kèm múi giờ, không tự dịch ngày phục vụ. Decimal tiền/định lượng theo producer, không tự làm tròn lại. Đơn vị kcal/g giữ E4; nhãn “ước tính từ định lượng sống”. Source refs nội bộ phải projection an toàn, không lộ định danh khách khác. Xem [từ điển](../srs/data-dictionary.md) cho trường và nullability.

## Quyền

PER-05: phản hồi, phân tích món, thực đơn, mục tiêu nhóm và CRM được cấp. PER-06: vận hành tại cơ sở; không tự cấp cost. PER-07: nguồn kế toán được cấp. PER-08: tổng quan trong scope; quyền cost/log vẫn kiểm riêng. PER-02/03/04 chỉ phản hồi trong phạm vi được xác minh; PER-03 chỉ nhật ký của mình. Chưa có ma trận Q07 thì nhánh chưa được cấp từ chối theo mặc định.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm số phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02 ≤ 3 điểm phần trăm là mục tiêu R11, không phải sai số tính toán. FR-MENU-RCP-007 chặn O-02; FEAT-046/047/063 chặn O-03.

## Mapping trường trọng yếu tường minh

| Màn / nhãn | JSON E12 đề xuất | Thực thể.cột logic đề xuất | Nguồn / chuyển đổi / gate |
| :--- | :--- | :--- | :--- |
| UI-FBR-01 / thang và điểm | ratingScaleRef, ratingValue | feedback_rating.scale_ref, value | Q01; không mặc định 5 mức, không đổi điểm về % |
| UI-FBR-02 / trạng thái | status, caseVersion | feedback_case.status, version | Q03; RECEIVED không là RESOLVED |
| UI-FBR-03 / lựa chọn | numerator, sourceRefs | dish_metric_projection.numerator, source_refs | Chỉ E6 lựa chọn thật; CG/ORD/EVID còn chờ |
| UI-FBR-03 / tỷ lệ | rate, denominatorDefinitionRef, denominator | dish_metric_projection.rate, denominator_definition_ref, denominator | Q04 chưa chọn; trả null, không dùng productionServings |
| UI-FBR-05 / ô chỉ số | metricDefinitionRef, value, asOf | role_metric_projection.definition_ref, value, as_of | Công thức/mẫu số/quyền theo catalog; không mặc định 0 |
| UI-FBR-06 / cost % ngày | costPct, calculationBasis, sourceRefs | role_metric_projection.value, basis, source_refs | E3 MEAL-001 hoặc dự toán, nhãn tách riêng; cost.cost.read |
| UI-FBR-06 / cost % khách | value, missingReason | role_metric_projection.value, missing_reason | Q08 chưa có công thức tổng hợp; null |
| UI-FBR-07…10 / nội dung nháp | proposalContent, sourceRevision, reviewRequired | review_proposal.content, source_revision, review_state | Không ghi vào menus/quotes/purchase_orders; dữ liệu ngoài quyền loại trước diễn giải |
| UI-FBR-07 / bảng kiểm | candidateHash, checkRefs | review_proposal.candidate_hash, check_refs | Cùng hash cho E2/dị ứng/E3; mismatch chặn |
| UI-FBR-11 / mục tiêu | groupRef, targets, sourceRef | group_nutrition_target.group_ref, targets, source_ref | Chỉ nhóm phi y tế; nguồn và ngưỡng chờ NUTR-Q01–04 |
| UI-FBR-12 / đồng ý | consentPolicyRef, explicitAgreement | diary_consent.policy_ref, agreed_at | Server ghi thời điểm khi đồng ý tường minh; không chọn sẵn |
| UI-FBR-12 / bữa đã ăn | consumedMealRef, consumedAt, evidenceRef | diary_meal.consumed_meal_ref, consumed_at, evidence_ref | Q17; không tự chuyển meal_selection thành đã ăn |
| UI-FBR-12 / dinh dưỡng suất | nutritionSnapshotRef | diary_meal.nutrition_snapshot_ref | E4 MEAL snapshot; không ghi lại giá trị khi nguồn đổi; không suy hấp thu |
| UI-FBR-12 / xóa | receiptRef, state, completedEvidenceRef | diary_deletion_request.receipt_ref, state, completed_evidence_ref | Q16; receipt khác hoàn tất, không xóa giao dịch nguồn |

Tên cột ở bảng này là đề xuất cho review, không phải migration hoặc contract nguồn được phê duyệt.
