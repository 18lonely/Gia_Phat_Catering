---
id: DOC-E12-SRS-DATA-DICTIONARY-MD
title: Từ điển dữ liệu đề xuất E12
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Từ điển dữ liệu đề xuất E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E12-Q18 |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## Đối chiếu nguồn

[DBML nền](../../nen-tang/srs/schema.dbml) giữ 65 bảng. users/eaters/meal_selections, recipes/recipe_items, nutrient_value_revisions/nutrition_calculations, cost_estimates/menu_cost_snapshots, agent_runs/agent_run_contexts/agent_tool_events đã có; tên trong ERD khung không chứng minh bảng đã tồn tại. Không sửa hoặc tạo migration. Không đọc/ghi eater_health_profiles.

| Thực thể logic | Hiện trạng | Trường đặc thù đề xuất |
| :--- | :--- | :--- |
| feedback_rating | Đề xuất mới; ERD có khung feedbacks nhưng DBML chưa có bảng FB | mealRef, scaleRef, value, actorRef, scopeRef, receiptRef |
| feedback_case | Đề xuất mới | mealRef, categoryRef, nội dung về bữa, status, version, historyRefs |
| dish_metric_projection | Projection đề xuất, không thêm bảng source E6 | dishRef, scopeRef, choiceSourceRefs, numerator, denominatorDefinitionRef, denominator, rate, completeness |
| role_metric_projection | Projection đề xuất | metricDefinitionRef, value, unit, sourceRefs, asOf, completeness, missingReason |
| review_proposal | Tài liệu nháp đề xuất; không ghi MENU/CRM/PUR | kind, sourceRefs, sourceRevision, diff, checkRefs, reviewState |
| group_nutrition_target | Delta nhóm phi y tế đề xuất | groupRef, targets, sourceRef, version, effectiveRange, state |
| diary_consent | Delta riêng, không dùng eater_health_profiles | subjectRef, policyRef, agreedAt, withdrawnAt |
| diary_meal | Delta riêng, không liên kết hồ sơ sức khỏe | subjectRef, consumedMealRef, consumedAt, evidenceRef, nutritionSnapshotRef |
| diary_deletion_request | Delta quyền xóa đề xuất | subjectRef, scopeRef, receiptRef, state, completedEvidenceRef |

## Trường dùng chung và kiểu đề xuất

| Tên logic | Tên cột đề xuất | Kiểu | Độ dài | Null? | Khóa | Ràng buộc / mặc định | Diễn giải |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Định danh | id | Opaque reference | Chờ contract | Không | PK đề xuất | Server cấp, không chọn UUID/bigint mới | Mã E12, không suy kiểu từ schema nguồn |
| Chủ thể | subject_ref | Reference | Theo E1/E6 | Không cho nhật ký | FK logic | Server lấy từ phiên, không tin client | Chỉ chủ nhật ký được xem |
| Phạm vi | scope_ref | Object/reference | Chờ Q18 | Không | FK logic | Khách/cơ sở/điểm; giao quyền hiện tại | Không chỉ lọc UI |
| Nguồn | source_refs | Array reference | Chờ Q18 | Không khi có số | FK logic | module, recordRef, revision, asOf, scope | Không đưa tham chiếu nhạy cảm ra ngoài quyền |
| Phiên bản | version | Opaque token | Chờ Q18 | Không khi sửa | — | So khớp, không mặc định lấy mới nhất | Khác revision bất biến của nguồn |
| Giá trị | value | Decimal hoặc null | Theo producer | Có | — | Null khi missing; không default 0 | Không float tiền; tỷ lệ theo producer |
| Mẫu số | denominator | Decimal hoặc null | Theo định nghĩa được duyệt | Có | — | Chưa chọn mẫu số tỷ lệ chọn; không default | 0 không chia; cần definitionRef |
| Bốn chỉ số suất | nutrition_snapshot_ref | Reference | Theo E4 | Có khi thiếu | FK logic | energy_kcal/protein_g/fat_g/carb_g từ E4 | Không lưu bệnh, cân nặng hoặc suy lượng hấp thu |
| Đồng ý | policy_ref | Reference | Chờ Q15 | Không khi bật | FK logic | Explicit, không chọn sẵn | Đồng ý nhật ký không là đồng ý hồ sơ sức khỏe |
| Bữa đã ăn | consumed_meal_ref | Reference | Chờ Q17 | Không khi ghi | FK logic | Căn cứ đã ăn riêng; order không chứng minh | Không tự ghi từ lựa chọn |
| Mục tiêu nhóm | targets | Object nguồn | NUTR-Q01–04 | Có khi nháp thiếu | — | Không số mặc định; nguồn và phiên bản bắt buộc khi dùng | Không có subjectRef cá nhân trong mục tiêu |
| Kết quả xóa | completed_evidence_ref | Reference | Chờ Q16 | Có trước hoàn tất | FK logic | Chỉ có khi chứng minh xóa; không xóa nguồn E6/E7 | Không báo hoàn tất từ receipt |


Trường bổ sung cho từng thực thể là trường logic, chưa freeze tên vật lý, độ dài hoặc DDL. ratingScale/value, category/nội dung/SLA chờ Q01–03; targets/effectiveRange chờ Q13/14; diary consent/retention/evidence chờ Q15–17. Không lưu raw sức khỏe kể cả người dùng cố gửi thêm field: schema đầu vào theo allowlist, không nhận ghi chú sức khỏe. Không thiết kế nội dung hồ sơ FEAT-046/047.

Provenance gắn bất biến với kết quả; nguồn mới tạo bản kết quả mới, không sửa nhật ký cũ. Chính sách xóa bao gồm bản sao và nội dung cá nhân trong audit cần Q16; không tự chọn thời hạn. [Mapping](../api/data-mapping.md).

## Quy ước tài liệu liên epic — XC-04

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E12-Q18 — XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
