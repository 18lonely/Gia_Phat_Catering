---
id: DOC-THUC-DON-API-DATA-MAPPING
title: Mapping dữ liệu E2, API, schema và màn hình
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-mapping, api, e2]
author: BA
last_updated: 2026-11-16
---
# Mapping dữ liệu E2: Thực đơn và định lượng

Draft · 16/11/2026 · Thiết kế BA để review, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo mapping 3 tầng API, bảng DBML, màn hình theo khuôn chung các epic. Không đổi API hay schema |

Nguồn: [catalog API](endpoint-catalog.json), [API spec](api-spec.md), [DBML 65 bảng](../../nen-tang/srs/schema.dbml), [ERD nền](../../nen-tang/srs/erd.md). Tên bảng và cột đã đối chiếu với DBML. Không migration, không thêm bảng.

## 1. Endpoint, bảng nguồn, màn hình

| API | Method và route | FR | Bảng DBML đọc hoặc ghi | Màn hình |
| :--- | :--- | :--- | :--- | :--- |
| API-MENU-001 | `POST /v1/menu/ingredients` | FR-MENU-ING-001 | ingredients | SCR-MENU-01, 02 |
| API-MENU-002 | `PATCH /v1/menu/ingredients/{id}` | FR-MENU-ING-002 | ingredients | SCR-MENU-01, 02 |
| API-MENU-003 | `POST /v1/menu/ingredients/{id}/status-changes` | FR-MENU-ING-003 | ingredients.status, audit_logs | SCR-MENU-01, 02 |
| API-MENU-004 | `GET /v1/menu/ingredients` | FR-MENU-ING-004 | ingredients | SCR-MENU-01, 02 |
| API-MENU-005 | `GET /v1/menu/ingredient-groups` | FR-MENU-ING-005 | ingredient_groups | SCR-MENU-03 |
| API-MENU-006 | `POST /v1/menu/ingredient-groups` | FR-MENU-ING-005 | ingredient_groups | SCR-MENU-03 |
| API-MENU-007 | `PATCH /v1/menu/ingredient-groups/{id}` | FR-MENU-ING-005 | ingredient_groups | SCR-MENU-03 |
| API-MENU-008 | `PUT /v1/menu/ingredients/{id}/seasons` | FR-MENU-ING-006 | ingredient_seasons | SCR-MENU-01, 02 |
| API-MENU-009 | `POST /v1/menu/dishes` | FR-MENU-DISH-001 | dishes, dish_allergens | SCR-MENU-04, 05 |
| API-MENU-010 | `PATCH /v1/menu/dishes/{id}` | FR-MENU-DISH-002 | dishes, dish_allergens | SCR-MENU-04, 05 |
| API-MENU-011 | `POST /v1/menu/dishes/{id}/submissions` | FR-MENU-DISH-003 | dishes.status, approvals | SCR-MENU-04, 05 |
| API-MENU-012 | `POST /v1/menu/dishes/{id}/decisions` | FR-MENU-DISH-004 | approvals, dishes.approved_by, dishes.approved_at | SCR-MENU-13, 14 |
| API-MENU-013 | `POST /v1/menu/dishes/{id}/deactivations` | FR-MENU-DISH-005 | dishes.status, audit_logs | SCR-MENU-04, 05 |
| API-MENU-014 | `GET /v1/menu/dishes` | FR-MENU-DISH-006 | dishes, dish_allergens | SCR-MENU-04, 05 |
| API-MENU-015 | `GET /v1/menu/cooking-methods` | FR-MENU-DISH-007 | cooking_methods | SCR-MENU-03 |
| API-MENU-016 | `POST /v1/menu/cooking-methods` | FR-MENU-DISH-007 | cooking_methods | SCR-MENU-03 |
| API-MENU-017 | `PATCH /v1/menu/cooking-methods/{id}` | FR-MENU-DISH-007 | cooking_methods | SCR-MENU-03 |
| API-MENU-018 | `GET /v1/menu/dish-conflicts` | FR-MENU-DISH-008 | dish_conflicts | SCR-MENU-03 |
| API-MENU-019 | `POST /v1/menu/dish-conflicts` | FR-MENU-DISH-008 | dish_conflicts | SCR-MENU-03 |
| API-MENU-020 | `POST /v1/menu/dishes/{id}/images` | FR-MENU-DISH-009 | files, dishes.image_file_id | SCR-MENU-04, 05 |
| API-MENU-021 | `POST /v1/menu/recipes` | FR-MENU-RCP-001 | recipes, recipe_items | SCR-MENU-06 |
| API-MENU-022 | `PATCH /v1/menu/recipes/{id}` | FR-MENU-RCP-002 | recipes, recipe_items | SCR-MENU-06 |
| API-MENU-023 | `POST /v1/menu/recipes/{id}/transitions` | FR-MENU-RCP-003 | recipes.status, approvals | SCR-MENU-06, 14 |
| API-MENU-024 | `POST /v1/menu/recipes/{id}/versions` | FR-MENU-RCP-004 | recipes (version_no, effective_from), recipe_items | SCR-MENU-06 |
| API-MENU-025 | `GET /v1/menu/effective-recipes` | FR-MENU-RCP-005 | recipes, recipe_items | SCR-MENU-05 |
| API-MENU-026 | `GET /v1/menu/recipe-comparisons` | FR-MENU-RCP-006 | recipes, recipe_items | SCR-MENU-07 |
| API-MENU-027 | `POST /v1/menu/dish-prices` | FR-MENU-PRC-001 | dish_prices | SCR-MENU-05 |
| API-MENU-028 | `POST /v1/menu/dish-prices/{id}/decisions` | FR-MENU-PRC-002 | approvals, dish_prices.status | SCR-MENU-14 |
| API-MENU-029 | `GET /v1/menu/effective-dish-prices` | FR-MENU-PRC-003 | dish_prices | SCR-MENU-05 |
| API-MENU-030 | `GET /v1/menu/dishes/{id}/price-history` | FR-MENU-PRC-004 | dish_prices | SCR-MENU-04, 05 |
| API-MENU-031 | `POST /v1/menu/meal-types` | FR-MENU-MTY-001 | meal_types | SCR-MENU-08 |
| API-MENU-032 | `POST /v1/menu/meal-types/{id}/status-changes` | FR-MENU-MTY-002 | meal_types.status | SCR-MENU-08 |
| API-MENU-033 | `PATCH /v1/menu/meal-types/{id}` | FR-MENU-MTY-003 | meal_types | SCR-MENU-08 |
| API-MENU-034 | `PATCH /v1/menu/meal-types/{id}/visibility` | FR-MENU-MTY-004 | meal_types.is_public | SCR-MENU-08 |
| API-MENU-035 | `POST /v1/menu/menus` | FR-MENU-MNU-001 | menus, menu_days | SCR-MENU-09, 12 |
| API-MENU-036 | `PUT /v1/menu/menu-days/{id}/items` | FR-MENU-MNU-002 | menu_day_items | SCR-MENU-10 |
| API-MENU-037 | `PUT /v1/menu/menu-days/{id}/default-dish` | FR-MENU-MNU-003 | menu_days.default_dish_id | SCR-MENU-10 |
| API-MENU-038 | `POST /v1/menu/menus/{id}/copies` | FR-MENU-MNU-005 | menus, menu_days, menu_day_items | SCR-MENU-09 |
| API-MENU-039 | `GET /v1/menu/dish-usage` | FR-MENU-MNU-006 | menu_day_items, menu_days | SCR-MENU-10 |
| API-MENU-040 | `GET /v1/menu/menus` | FR-MENU-MNU-007 | menus, menu_days | SCR-MENU-09, 12 |
| API-MENU-041 | `POST /v1/menu/menus/{id}/exports` | FR-MENU-MNU-008 | menus, menu_days, menu_day_items, files | SCR-MENU-12 |
| API-MENU-042 | `POST /v1/menu/menus/{id}/cancellations` | FR-MENU-MNU-009 | menus.status, audit_logs | SCR-MENU-09 |
| API-MENU-043 | `POST /v1/menu/menus/{id}/checks` | FR-MENU-RUL-001 | menu_rule_results, menu_rules, menus.rule_score | SCR-MENU-10 |
| API-MENU-044 | `POST /v1/menu/menu-validations` | FR-MENU-RUL-002 | menu_rules (không ghi kết quả) | Không có màn (port cho agent) |
| API-MENU-045 | `GET /v1/menu/menus/{id}/rule-results` | FR-MENU-RUL-003 | menu_rule_results | SCR-MENU-10 |
| API-MENU-046 | `PUT /v1/menu/rule-results/{id}/acceptance-reasons` | FR-MENU-RUL-004 | menu_rule_results.waiver_reason | SCR-MENU-10 |
| API-MENU-047 | `GET /v1/menu/menu-rules` | FR-MENU-RUL-005 | menu_rules | SCR-MENU-15 |
| API-MENU-048 | `POST /v1/menu/menu-rule-changes` | FR-MENU-RUL-006 | change_requests, menu_rules | SCR-MENU-15 |
| API-MENU-049 | `POST /v1/menu/menus/{id}/submissions` | FR-MENU-APV-001 | menus.status, approvals, menu_rule_results, menu_cost_snapshots (hook Cost) | SCR-MENU-10 |
| API-MENU-050 | `POST /v1/menu/menus/{id}/decisions` | FR-MENU-APV-002 | approvals, menus.approved_by, menus.approved_at | SCR-MENU-13, 14 |
| API-MENU-051 | `POST /v1/menu/menus/{id}/publications` | FR-MENU-APV-003 | menus.published_at, menus.status | SCR-MENU-12 |
| API-MENU-052 | `POST /v1/menu/menus/{id}/withdrawals` | FR-MENU-APV-004 | menus.status, audit_logs | SCR-MENU-12 |
| API-MENU-053 | `POST /v1/menu/menus/{id}/reopenings` | FR-MENU-APV-005 | menus.status, audit_logs | SCR-MENU-12 |
| API-MENU-054 | `GET /v1/menu/import-templates/{type}` | FR-MENU-IMP-001 | Không đọc bảng (tệp mẫu) | SCR-MENU-16 |
| API-MENU-055 | `POST /v1/menu/import-validations` | FR-MENU-IMP-002 | files; bảng đích theo loại nhập | SCR-MENU-16 |
| API-MENU-056 | `POST /v1/menu/imports` | FR-MENU-IMP-003 | ingredients, dishes, recipes, recipe_items (chỉ tạo mới, E2-Q10) | SCR-MENU-16 |
| API-MENU-057 | `GET /v1/menu/menus/{id}` | FR-MENU-MNU-007 | menus, menu_days | SCR-MENU-09, 12 |
| API-MENU-058 | `GET /v1/menu/dishes/{id}` | FR-MENU-DISH-006 | dishes, dish_allergens | SCR-MENU-04, 05 |
| API-MENU-059 | `GET /v1/menu/ingredients/{id}` | FR-MENU-ING-004 | ingredients | SCR-MENU-01, 02 |
| API-MENU-060 | `GET /v1/menu/recipes/{id}` | FR-MENU-RCP-005 | recipes, recipe_items | SCR-MENU-06 |

Mọi lệnh ghi số liệu còn ghi `audit_logs` theo FR-SYS-AUD-001; bảng này không lặp lại cho từng dòng.

## 2. Trường chính

| Trường API | Cột DBML | Màn hình | Chuyển đổi / lưu ý |
| :--- | :--- | :--- | :--- |
| ingredient.buyUnit, useUnit, conversionFactor | ingredients.buy_unit, use_unit, conversion_factor | SCR-MENU-02 | Khóa đơn vị khi nguyên liệu đã dùng |
| ingredient.wastePct, hasBoneOrShell | ingredients.waste_pct, has_bone_or_shell | SCR-MENU-02 | Định lượng sống đã gồm xương, vỏ chưa: E3-Q2, NUTR-Q |
| ingredient.storageType | ingredients.storage_type | SCR-MENU-02 | E11 dùng để xét phạm vi lô |
| dish 12 thuộc tính | dishes (role, main_group_id, cooking_method_id, is_healthy, is_sour, texture, is_light, is_complex, transport_ok, bulk_ok, cost_tier, is_special) | SCR-MENU-05 | Đủ 12 thuộc tính là tiêu chí R2 |
| allergens | dish_allergens | SCR-MENU-05 | Danh sách rỗng không có nghĩa là không dị ứng |
| recipe.versionNo, effectiveFrom, status | recipes.version_no, effective_from, status | SCR-MENU-06 | Người tạo không tự duyệt |
| recipe.items[].qtyMin, qtyMax, qtyStd, unit, isMain | recipe_items (qty_min, qty_max, qty_std, unit, is_main) | SCR-MENU-06 | Nhiều cỡ (portion_code) chờ O-02 |
| dishPrice.priceVnd, effectiveFrom | dish_prices.price_vnd, effective_from, portion_code | SCR-MENU-05 | Giá gồm VAT; trả lại hay hủy chờ MENU-API-Q02 |
| mealType.priceCapVnd, mainOffered, mainPick, sideCount, hasVeg, hasSoup, isPublic | meal_types (cùng tên cột) | SCR-MENU-08 | price_cap không phải giá bán công khai |
| menu.weekStart, customerId, status, ruleScore, source, agentRunId | menus (week_start, customer_id, status, rule_score, source, agent_run_id) | SCR-MENU-09, 10 | source cho biết bản do agent áp dụng |
| menuDay.serviceDate, defaultDishId | menu_days.service_date, default_dish_id | SCR-MENU-10 | Ngày phục vụ trong tuần chờ E2-Q3 |
| items[].dishId, recipeId, slot | menu_day_items (dish_id, recipe_id, slot, sort_order) | SCR-MENU-10 | Công thức đúng ngày hiệu lực |
| ruleResult.ruleCode, passed, detail, waiverReason | menu_rule_results (rule_code, passed, detail, waiver_reason) | SCR-MENU-10 | Quy tắc cứng không có lý do chấp nhận |
| rule.ruleType, penalty, params, isActive | menu_rules (rule_type, penalty, params, is_active) | SCR-MENU-15 | Số liệu từng quy tắc chờ DL-01 |

## 3. Quy ước chung

- ID nội bộ là BIGINT; API truyền dạng chuỗi để không mất độ chính xác.
- Tiền là số nguyên VND hoặc decimal truyền dạng chuỗi; không dùng float. Giá trị thiếu để trống, không mặc định 0.
- Phạm vi cơ sở và quyền lấy từ phiên ở server, không tin giá trị client gửi lên.
- Envelope lỗi, phân trang và idempotency chưa thống nhất giữa các epic (E1-Q01, E1-Q02).
