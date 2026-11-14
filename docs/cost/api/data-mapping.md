---
id: DOC-COST-API-DATA-MAPPING
title: Mapping dữ liệu E3, API, schema và màn hình
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-mapping, api, e3]
author: BA
last_updated: 2026-11-16
---
# Mapping dữ liệu E3: Cost

Draft · 16/11/2026 · Thiết kế BA để review, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo mapping 3 tầng API, bảng DBML, màn hình theo khuôn chung các epic. Không đổi API hay schema |

Nguồn: [catalog API](endpoint-catalog.json), [API spec](api-spec.md), [DBML 65 bảng](../../nen-tang/srs/schema.dbml), [ERD nền](../../nen-tang/srs/erd.md). Tên bảng và cột đã đối chiếu với DBML. Không migration, không thêm bảng.

## 1. Endpoint, bảng nguồn, màn hình

| API | Method và route | FR | Bảng DBML đọc hoặc ghi | Màn hình |
| :--- | :--- | :--- | :--- | :--- |
| API-COST-001 | `GET /v1/cost/suppliers` | FR-COST-SUP-003 | suppliers | SCR-COST-01 |
| API-COST-002 | `POST /v1/cost/suppliers` | FR-COST-SUP-001 | suppliers | SCR-COST-02 |
| API-COST-003 | `PATCH /v1/cost/suppliers/{id}` | FR-COST-SUP-001, FR-COST-SUP-002 | suppliers | SCR-COST-02 |
| API-COST-004 | `GET /v1/cost/prices` | FR-COST-PRC-006 | ingredient_prices | SCR-COST-03, SCR-COST-07 |
| API-COST-005 | `POST /v1/cost/prices` | FR-COST-PRC-001, FR-COST-PRC-010, FR-COST-PRC-011 | ingredient_prices | SCR-COST-04 |
| API-COST-006 | `POST /v1/cost/price-batches` | FR-COST-PRC-004, FR-COST-PRC-010, FR-COST-PRC-011 | ingredient_prices | SCR-COST-03 |
| API-COST-007 | `POST /v1/cost/price-confirmations` | FR-COST-PRC-010 | ingredient_prices (pricing_verified_at, pricing_verified_by) | SCR-COST-03, SCR-COST-04 |
| API-COST-008 | `POST /v1/cost/prices/{id}/reference-selections` | FR-COST-PRC-002 | ingredient_prices.is_reference | SCR-COST-04 |
| API-COST-009 | `POST /v1/cost/prices/{id}/cancellations` | FR-COST-PRC-007 | ingredient_prices (cancelled_at, cancelled_reason) | SCR-COST-04 |
| API-COST-010 | `GET /v1/cost/reference-prices` | FR-COST-PRC-003 | ingredient_prices | SCR-COST-07, SCR-COST-08 |
| API-COST-011 | `GET /v1/cost/price-health` | FR-COST-PRC-008, FR-COST-PRC-009 | ingredient_prices, ingredients | SCR-COST-06 |
| API-COST-012 | `GET /v1/cost/price-import-template` | FR-COST-PRC-005 | Không đọc bảng (tệp mẫu) | SCR-COST-05 |
| API-COST-013 | `POST /v1/cost/price-import-validations` | FR-COST-PRC-005 | files, ingredient_prices | SCR-COST-05 |
| API-COST-014 | `POST /v1/cost/price-imports` | FR-COST-PRC-005 | ingredient_prices, files (source_file_id) | SCR-COST-05 |
| API-COST-015 | `POST /v1/cost/dish-calculations` | FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004 | recipes, recipe_items, ingredient_prices, ingredients.waste_pct | SCR-COST-08 |
| API-COST-016 | `POST /v1/cost/recipe-comparisons` | FR-COST-DISH-005 | recipes, recipe_items, ingredient_prices | SCR-COST-08 |
| API-COST-017 | `POST /v1/cost/dish-tier-suggestions` | FR-COST-DISH-008 | dishes.cost_tier, ingredient_prices | SCR-COST-08 |
| API-COST-018 | `GET /v1/cost/sheets` | FR-COST-DISH-006, FR-COST-DISH-007 | cost_sheets, cost_sheet_lines | SCR-COST-09, SCR-COST-10 |
| API-COST-019 | `GET /v1/cost/sheets/{id}` | FR-COST-DISH-006, FR-COST-DISH-007 | cost_sheets, cost_sheet_lines | SCR-COST-09 |
| API-COST-020 | `POST /v1/cost/sheets` | FR-COST-DISH-006 | cost_sheets, cost_sheet_lines | SCR-COST-09 |
| API-COST-021 | `POST /v1/cost/sheets/{id}/decisions` | FR-COST-DISH-007 | cost_sheets (status, approved_by), approvals | SCR-COST-10 |
| API-COST-022 | `GET /v1/cost/allowances` | FR-COST-MEAL-004 | cost_allowances | SCR-COST-11 |
| API-COST-023 | `POST /v1/cost/allowances` | FR-COST-MEAL-004 | cost_allowances | SCR-COST-11 |
| API-COST-024 | `POST /v1/cost/allowances/{id}/decisions` | FR-COST-MEAL-004 | cost_allowances (status, approved_by), approvals | SCR-COST-11 |
| API-COST-025 | `POST /v1/cost/menu-calculations` | FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003, FR-COST-RUL-001, FR-COST-RUL-002 | menus, menu_days, menu_day_items, ingredient_prices, cost_allowances, meal_types, parameters | SCR-COST-12 |
| API-COST-026 | `GET /v1/cost/menu-snapshots` | FR-COST-MEAL-006 | menu_cost_snapshots, menu_cost_snapshot_lines | SCR-COST-12 |
| API-COST-027 | `POST /v1/cost/estimates` | FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004, FR-COST-EST-006 | cost_estimates, cost_estimate_lines, cost_estimate_servings, cost_estimate_components, cost_estimate_allowances | SCR-COST-14, SCR-COST-15 |
| API-COST-028 | `POST /v1/cost/estimate-batches` | FR-COST-EST-003 | cost_estimates và các bảng con | SCR-COST-14 |
| API-COST-029 | `GET /v1/cost/estimates` | FR-COST-EST-006 | cost_estimates, cost_estimate_lines, cost_estimate_servings, cost_estimate_components, cost_estimate_allowances | SCR-COST-15 |
| API-COST-030 | `GET /v1/cost/estimates/{id}` | FR-COST-EST-004, FR-COST-EST-005 | cost_estimates, cost_estimate_lines, cost_estimate_servings, cost_estimate_components, cost_estimate_allowances | SCR-COST-15 |
| API-COST-031 | `GET /v1/cost/estimates/{id}/export` | FR-COST-EST-007 | cost_estimates, cost_estimate_lines, files | SCR-COST-15 |
| API-COST-032 | `GET /v1/cost/alerts` | FR-COST-ALR-002, FR-COST-ALR-003 | cost_alerts, cost_alert_kitchens | SCR-COST-16 |
| API-COST-033 | `GET /v1/cost/alerts/{id}` | FR-COST-ALR-002, FR-COST-ALR-003 | cost_alerts, cost_alert_kitchens | SCR-COST-17 |
| API-COST-034 | `POST /v1/cost/alerts/{id}/closures` | FR-COST-ALR-003 | cost_alerts (closed_at, closed_by, close_type), audit_logs | SCR-COST-17 |
| API-COST-035 | `POST /v1/cost/price-simulations` | FR-COST-ALR-005 | ingredient_prices, recipes (không ghi) | SCR-COST-18 |
| API-COST-036 | `POST /v1/cost/budget-checks` | FR-COST-RUL-003 | Tính tạm, không ghi, không trả số cost | SVC-COST-01 |
| API-COST-037 | `GET /v1/cost/requests/{key}` | FR-COST-PRC-001, FR-COST-PRC-004, FR-COST-EST-006 | Nơi lưu khóa chống trùng chưa chốt (FLOW-COST-Q02) | SCR-COST-03, SCR-COST-15 |

Mọi lệnh ghi số liệu còn ghi `audit_logs` theo FR-SYS-AUD-001; bảng này không lặp lại cho từng dòng.

## 2. Trường chính

| Trường API | Cột DBML | Màn hình | Chuyển đổi / lưu ý |
| :--- | :--- | :--- | :--- |
| supplier.code, name, supplierType, status | suppliers (code, name, supplier_type, status) | SCR-COST-01, 02 | NCC ngừng: 404 hay 422 chờ QA-COST-Q01 |
| price.quotedUnitPrice, priceBasis, vatRatePct, vatUnitAmount | ingredient_prices (quoted_unit_price, price_basis, vat_rate_pct, vat_unit_amount) | SCR-COST-03, 04 | PriceInput v0.2; VAT thiếu không thành 0 |
| price.priceVnd | ingredient_prices.price_vnd | SCR-COST-03, 07 | Giá cost gồm VAT do server chuẩn hóa, không nhận từ client |
| price.pricingEvidence, pricingVerifiedAt, pricingVerifiedBy | ingredient_prices (pricing_evidence, pricing_verified_at, pricing_verified_by) | SCR-COST-04 | Cờ không yêu cầu hóa đơn không phải VAT 0% |
| price.kitchenId, supplierId, effectiveFrom, isReference | ingredient_prices (kitchen_id, supplier_id, effective_from, is_reference) | SCR-COST-03, 04 | Đổi riêng cờ tham chiếu chờ E3-Q14 |
| price.sourceFileId | ingredient_prices.source_file_id | SCR-COST-05 | Nhập từ bảng tính |
| sheet.totalCostVnd, inputsSnapshot, status | cost_sheets (total_cost_vnd, inputs_snapshot, status, approved_by) | SCR-COST-09, 10 | Món đặc thù; mốc 90 ngày chờ E3-Q16 |
| allowance.amountVnd, mealTypeId, effectiveFrom | cost_allowances (amount_vnd, meal_type_id, effective_from, status) | SCR-COST-11 | Ai đọc khoản khoán chờ FLOW-COST-Q05 |
| menuCost.costPerServingVnd, revenueExVatVnd, costPct, thresholdPct, result | menu_cost_snapshots (cùng tên cột) | SCR-COST-12 | Chụp theo vòng duyệt (approval_round_no), không ghi đè |
| estimate.servings, mainPick, mainCostMethod, totalCostVnd, costPct | cost_estimates (servings, main_pick, main_cost_method, total_cost_vnd, cost_pct) | SCR-COST-14, 15 | Có phiên bản (version_no); nguồn số suất trước order chờ E3-Q8 |
| alert.status, closeType, closeReason | cost_alerts (status, close_type, close_reason), cost_alert_kitchens | SCR-COST-16, 17 | Một cảnh báo mỗi ngày, chi tiết theo cơ sở |
| Chế độ kiểm cost | parameters (code COST_CHE_DO_KIEM) | SCR-COST-13 | CHAN hoặc CANH_BAO; đổi sang CHAN cần Giám đốc duyệt |

Phần mở rộng kế toán (VAT, chiết khấu theo đơn) có mapping riêng tại [hợp đồng kế toán](accounting-contract.md).

## 3. Quy ước chung

- ID nội bộ là BIGINT; API truyền dạng chuỗi để không mất độ chính xác.
- Tiền là số nguyên VND hoặc decimal truyền dạng chuỗi; không dùng float. Giá trị thiếu để trống, không mặc định 0.
- Phạm vi cơ sở và quyền lấy từ phiên ở server, không tin giá trị client gửi lên.
- Envelope lỗi, phân trang và idempotency chưa thống nhất giữa các epic (E1-Q01, E1-Q02).
