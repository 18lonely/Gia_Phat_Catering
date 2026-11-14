---
id: DOC-DINH-DUONG-API-DATA-MAPPING
title: Mapping dữ liệu E4, API, schema và màn hình
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-mapping, api, e4]
author: BA
last_updated: 2026-11-16
---
# Mapping dữ liệu E4: Dinh dưỡng

Draft · 16/11/2026 · Thiết kế BA để review, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo mapping 3 tầng API, bảng DBML, màn hình theo khuôn chung các epic. Không đổi API hay schema |

Nguồn: [catalog API](endpoint-catalog.json), [API spec](api-spec.md), [DBML 65 bảng](../../nen-tang/srs/schema.dbml), [ERD nền](../../nen-tang/srs/erd.md). Tên bảng và cột đã đối chiếu với DBML. Không migration, không thêm bảng.

## 1. Endpoint, bảng nguồn, màn hình

| API | Method và route | FR | Bảng DBML đọc hoặc ghi | Màn hình |
| :--- | :--- | :--- | :--- | :--- |
| API-NUTR-001 | `PUT /v1/nutrition/ingredients/{id}` | FR-NUTR-REF-001 | nutrient_values, nutrient_value_revisions | UI-NUTR-01 |
| API-NUTR-002 | `POST /v1/nutrition/coverage-checks` | FR-NUTR-REF-002 | nutrient_values, recipe_items | UI-NUTR-01 |
| API-NUTR-003 | `POST /v1/nutrition/dish-calculations` | FR-NUTR-CALC-001 | nutrition_calculations, recipe_items, nutrient_values | UI-NUTR-02 |
| API-NUTR-004 | `POST /v1/nutrition/meal-calculations` | FR-NUTR-CALC-002 | nutrition_calculations, menu_day_items, meal_types | UI-NUTR-03 |
| API-NUTR-005 | `GET /v1/nutrition/calculations/{id}` | FR-NUTR-SNAP-001 | nutrition_calculations | UI-NUTR-02 |
| API-NUTR-006 | `GET /v1/nutrition/ingredients` | FR-NUTR-REF-001 | nutrient_values, nutrient_value_revisions | UI-NUTR-01 |
| API-NUTR-007 | `GET /v1/nutrition/ingredients/{id}/revisions` | FR-NUTR-SNAP-001 | nutrient_value_revisions | UI-NUTR-02 |

Mọi lệnh ghi số liệu còn ghi `audit_logs` theo FR-SYS-AUD-001; bảng này không lặp lại cho từng dòng.

## 2. Trường chính

| Trường API | Cột DBML | Màn hình | Chuyển đổi / lưu ý |
| :--- | :--- | :--- | :--- |
| energyKcal, proteinG, fatG, carbG | nutrient_values (energy_kcal, protein_g, fat_g, carb_g) | UI-NUTR-01 | Theo 100 g phần ăn được; thiếu không thành 0 |
| ediblePct, gramsPerUnit | nutrient_values.edible_pct, grams_per_unit | UI-NUTR-01 | Ý nghĩa định lượng sống chờ NUTR-Q |
| source, sourceEdition, sourceLocator | nutrient_values (source, source_edition, source_locator) | UI-NUTR-01 | Nguồn có ấn bản và trang (DP-03) |
| version | nutrient_values.version | UI-NUTR-01 | Chống ghi đè |
| revision | nutrient_value_revisions (version, value_snapshot, reason, changed_by, changed_at) | UI-NUTR-02 | Lịch sử bất biến |
| calculation.kind, recipeId, menuId, menuVersion, serviceDate | nutrition_calculations (kind, recipe_id, menu_id, menu_version, service_date) | UI-NUTR-02, 03 | Món hoặc tổ hợp suất |
| calculation.totals, inputsSnapshot, scopeSnapshot | nutrition_calculations (totals, inputs_snapshot, scope_snapshot) | UI-NUTR-02, 03 | Không trả nguyên inputs_snapshot cho kênh khách |
| requestKey | nutrition_calculations (request_key, request_hash) | Không hiện | Chống gửi trùng |
| label | Không lưu | UI-NUTR-02, 03 | Luôn ghi "ước tính từ định lượng sống" |

## 3. Quy ước chung

- ID nội bộ là BIGINT; API truyền dạng chuỗi để không mất độ chính xác.
- Tiền là số nguyên VND hoặc decimal truyền dạng chuỗi; không dùng float. Giá trị thiếu để trống, không mặc định 0.
- Phạm vi cơ sở và quyền lấy từ phiên ở server, không tin giá trị client gửi lên.
- Envelope lỗi, phân trang và idempotency chưa thống nhất giữa các epic (E1-Q01, E1-Q02).
