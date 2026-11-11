---
id: DOC-E6-TEST-TRACEABILITY
title: Ma trận truy vết E6
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Ma trận truy vết E6

**Draft để review · 11/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |

Mỗi dòng là liên kết tài liệu, không chứng minh tính năng hoàn tất. 17 capability có thiết kế luồng có điều kiện; 2 capability chỉ đặc tả gate O-03. P1 không tự được đưa lên P0.

| Feature / ưu tiên | FR | UC | API / port / gate | Data | UI | Story | AC | Test | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-030 / P0 | FR-AUTH-EXT-001 | [UC-ORD-001](../usecases/UC-ORD-001.md) | API-ORD-006, API-ORD-007 | users,user_roles,customers | [UI-ORD-01](../ui/screen-catalog.md) | US-E6-001 | AC-E6-001-1, AC-E6-001-2, AC-E6-001-3 | TC-E6-001-1, TC-E6-001-2, TC-E6-001-3 | ORD-Q01 |
| FEAT-031 / P0 | FR-AUTH-QREG-001 | [UC-ORD-002](../usecases/UC-ORD-002.md) | API-ORD-008 | customer_qr_codes,eaters,users | [UI-ORD-02](../ui/screen-catalog.md) | US-E6-002 | AC-E6-002-1, AC-E6-002-2, AC-E6-002-3 | TC-E6-002-1, TC-E6-002-2, TC-E6-002-3 | ORD-Q01 |
| FEAT-032 / P0 | FR-AUTH-QSES-001 | [UC-ORD-003](../usecases/UC-ORD-003.md) | API-ORD-009 | customer_qr_codes,eaters; delta qr_sessions | [UI-ORD-02](../ui/screen-catalog.md) | US-E6-003 | AC-E6-003-1, AC-E6-003-2, AC-E6-003-3 | TC-E6-003-1, TC-E6-003-2, TC-E6-003-3 | ORD-Q01 |
| FEAT-033 / P0 | FR-AUTH-QRM-001 | [UC-ORD-004](../usecases/UC-ORD-004.md) | API-ORD-010, API-ORD-011, API-ORD-012 | customer_qr_codes,eaters | [UI-ORD-03](../ui/screen-catalog.md) | US-E6-004 | AC-E6-004-1, AC-E6-004-2, AC-E6-004-3 | TC-E6-004-1, TC-E6-004-2, TC-E6-004-3 | ORD-Q02 |
| FEAT-034 / P0 | FR-CUS-SVC-001 | [UC-ORD-005](../usecases/UC-ORD-005.md) | API-ORD-013, API-ORD-014, API-ORD-026 | customers,service_points,service_schedules,eaters | [UI-ORD-04](../ui/screen-catalog.md) | US-E6-005 | AC-E6-005-1, AC-E6-005-2, AC-E6-005-3 | TC-E6-005-1, TC-E6-005-2, TC-E6-005-3 | ORD-Q03 |
| FEAT-035 / P0 | FR-ORD-QTA-001 | [UC-ORD-006](../usecases/UC-ORD-006.md) | API-ORD-015, API-ORD-016 | customer_quotas,meal_types,dish_prices | [UI-ORD-05](../ui/screen-catalog.md) | US-E6-006 | AC-E6-006-1, AC-E6-006-2, AC-E6-006-3 | TC-E6-006-1, TC-E6-006-2, TC-E6-006-3 | ORD-Q04 |
| FEAT-036 / P0 | FR-ORD-SEL-001 | [UC-ORD-007](../usecases/UC-ORD-007.md) | API-ORD-001, API-ORD-002, API-ORD-017 | meal_selections,selection_counters,menu_days | [UI-ORD-06](../ui/screen-catalog.md) | US-E6-007 | AC-E6-007-1, AC-E6-007-2, AC-E6-007-3 | TC-E6-007-1, TC-E6-007-2, TC-E6-007-3 | ORD-Q01, ORD-Q04 |
| FEAT-037 / P1 | FR-ORD-WEEK-001 | [UC-ORD-008](../usecases/UC-ORD-008.md) | API-ORD-018 | meal_selections; delta weekly submission receipt | [UI-ORD-07](../ui/screen-catalog.md) | US-E6-008 | AC-E6-008-1, AC-E6-008-2, AC-E6-008-3 | TC-E6-008-1, TC-E6-008-2, TC-E6-008-3 | ORD-Q05 |
| FEAT-038 / P0 | FR-ORD-SUB-001 | [UC-ORD-009](../usecases/UC-ORD-009.md) | API-ORD-003, API-ORD-004, API-ORD-019 | orders,order_dish_lines,selection_counters | [UI-ORD-08](../ui/screen-catalog.md) | US-E6-009 | AC-E6-009-1, AC-E6-009-2, AC-E6-009-3 | TC-E6-009-1, TC-E6-009-2, TC-E6-009-3 | ORD-Q06 |
| FEAT-039 / P0 | FR-ORD-DEF-001 | [UC-ORD-010](../usecases/UC-ORD-010.md) | PORT-LOCK | order_revisions,order_revision_lines (delta) | [UI-ORD-09](../ui/screen-catalog.md) | US-E6-010 | AC-E6-010-1, AC-E6-010-2, AC-E6-010-3 | TC-E6-010-1, TC-E6-010-2, TC-E6-010-3 | ORD-Q06, ORD-Q07 |
| FEAT-040 / P0 | FR-ORD-LOCK-001 | [UC-ORD-011](../usecases/UC-ORD-011.md) | PORT-LOCK, API-ORD-020 | orders,order_revisions,production_plan_revisions (delta) | [UI-ORD-09](../ui/screen-catalog.md) | US-E6-011 | AC-E6-011-1, AC-E6-011-2, AC-E6-011-3 | TC-E6-011-1, TC-E6-011-2, TC-E6-011-3 | Q-16, ORD-Q07 |
| FEAT-041 / P0 | FR-ORD-CHG-001 | [UC-ORD-012](../usecases/UC-ORD-012.md) | API-ORD-005, API-ORD-021, API-ORD-022 | order_change_requests,order_revisions,approvals (delta/existing) | [UI-ORD-10](../ui/screen-catalog.md) | US-E6-012 | AC-E6-012-1, AC-E6-012-2, AC-E6-012-3 | TC-E6-012-1, TC-E6-012-2, TC-E6-012-3 | Q-16, O-06, ORD-Q08 |
| FEAT-042 / P0 | FR-ORD-PXY-001 | [UC-ORD-013](../usecases/UC-ORD-013.md) | API-ORD-003, API-ORD-004 | orders,order_dish_lines,files,audit_logs | [UI-ORD-11](../ui/screen-catalog.md) | US-E6-013 | AC-E6-013-1, AC-E6-013-2, AC-E6-013-3 | TC-E6-013-1, TC-E6-013-2, TC-E6-013-3 | ORD-Q06 |
| FEAT-043 / P1 | FR-ORD-REM-001 | [UC-ORD-014](../usecases/UC-ORD-014.md) | PORT-REM, API-ORD-023 | notifications; delta outbox/dedupe | [UI-ORD-09](../ui/screen-catalog.md) | US-E6-014 | AC-E6-014-1, AC-E6-014-2, AC-E6-014-3 | TC-E6-014-1, TC-E6-014-2, TC-E6-014-3 | Q-14 |
| FEAT-044 / P1 | FR-ORD-MODE-001 | [UC-ORD-015](../usecases/UC-ORD-015.md) | API-ORD-024 | customers; delta choice_mode_versions | [UI-ORD-05](../ui/screen-catalog.md) | US-E6-015 | AC-E6-015-1, AC-E6-015-2, AC-E6-015-3 | TC-E6-015-1, TC-E6-015-2, TC-E6-015-3 | ORD-Q09 |
| FEAT-045 / P0 | FR-NUTR-DSP-001 | [UC-ORD-016](../usecases/UC-ORD-016.md) | API-ORD-001 | menu_day_items,recipes,dish_allergens,nutrition_calculations | [UI-ORD-06](../ui/screen-catalog.md) | US-E6-016 | AC-E6-016-1, AC-E6-016-2, AC-E6-016-3 | TC-E6-016-1, TC-E6-016-2, TC-E6-016-3 | NUTR-Q03 |
| FEAT-046 / P1 | FR-NUTR-PROF-001 | [UC-ORD-017](../usecases/UC-ORD-017.md) | GATE-046 | eater_health_profiles tồn tại nhưng gated | [UI-ORD-12](../ui/screen-catalog.md) | US-E6-017 | AC-E6-017-1, AC-E6-017-2, AC-E6-017-3 | TC-E6-017-1, TC-E6-017-2, TC-E6-017-3 | O-03 |
| FEAT-047 / P1 | FR-NUTR-REC-001 | [UC-ORD-018](../usecases/UC-ORD-018.md) | GATE-047 | không thêm dữ liệu hồ sơ/gợi ý | [UI-ORD-12](../ui/screen-catalog.md) | US-E6-018 | AC-E6-018-1, AC-E6-018-2, AC-E6-018-3 | TC-E6-018-1, TC-E6-018-2, TC-E6-018-3 | O-03 |
| FEAT-048 / P0 | FR-PLAN-MEAL-001 | [UC-ORD-019](../usecases/UC-ORD-019.md) | API-ORD-020, API-ORD-025 | production_plan_revisions,order_revisions (delta) | [UI-ORD-13](../ui/screen-catalog.md) | US-E6-019 | AC-E6-019-1, AC-E6-019-2, AC-E6-019-3 | TC-E6-019-1, TC-E6-019-2, TC-E6-019-3 | ORD-Q10 |


## Lớp truy vết review quyết định

[8 ca TC-E6-DR-01–08](decision-review-cases.md) nối findings→feature/FR→UC→API/port tại từng dòng. Đây là bộ bổ sung riêng, không thay57AC/test hoặc tự chuyển BLOCKED sang PASS. [DR-01–04](../review/decision-review.md) nối schema/UI/gate tương ứng.

## Lớp invariant độc lập

[12ca INV](invariant-cases.md) nối RV→FR→UC→API/data/UI→AC gốc tại từng dòng; tất cả NOT RUN. [Fixture/checklist/profile tải](fixtures/README.md). Không tăng57AC, không đóng8ca DR; inventory99mô tả có overlap (10+57+12+8+12), không99mục tiêu độc lập.

## Liên kết contract/evidence tiếp nối

E6-RV-07 → FR-ORD-CHG-001/FR-PLAN-MEAL-001 → UC-ORD-012/019 → API-ORD-005/022/025 + delta_lines/order_revision_lines → UI-ORD-10/13 → AC-E6-012-2/3, AC-E6-019-3 → INV-08/11. [Review delta](../api/delta-contract-review.md) nêu gap chưa duyệt; [evidence](evidence-protocol.md) nối thêm RV04/05/06 với receipt/manifest. Không tăng số AC/test hoặc chuyển trạng thái.

## Review adapter — 11/11/2026

FR-NUTR-DSP-001/FR-ORD-SEL-001 → UC-ORD-016/007 → API-ORD-001/002 → SafeDish/sourceVersion → UI-ORD-06 → AC-E6-016-1/2/3 → SYS-05/09. [Adapter](../api/adapter-contract-review.md), [26route](../api/route-validation-review.md) và [oracle](fixtures/adapter-synthetic.json) bổ sung review, không thêm AC/TC;99mô tả ca có overlap giữ nguyên.

## Hợp nhất gap/DTO — 11/11/2026

[34DTO presence](../api/dto-presence-review.md) và [14gap](../review/contract-gap-register.md) tham chiếu contract/route và gate gốc. Review negative absent/null/0/false/[] là tiêu chí so schema tương lai, không thêm34TC;57AC/99mô tả ca có overlap giữ nguyên.
