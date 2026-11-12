---
id: DOC-E8-API-DATA-MAPPING-MD
title: Mapping E8 tới schema hiện có
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Mapping E8 tới schema hiện có

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Nguồn: [DBML65 bảng](../../nen-tang/srs/schema.dbml), [ERD](../../nen-tang/srs/erd.md), [SRS E2](../../thuc-don-dinh-luong/srs/spec.md), [API E4](../../dinh-duong/api/api-spec.md). Tên trường dưới là đọc schema nháp, không contract freeze. Không sửa DBML/migration.

| API/UI | Bảng.cột hiện có | Chuyển đổi / ranh giới | Gate |
| :--- | :--- | :--- | :--- |
| publicMealType / UI03/04 | meal_types.id,name,is_public,status | ACTIVE/is_public là tín hiệu lựa chọn, chưa đủ quyền công khai mọi trường | E8-Q03/04 |
| public price / UI03 | meal_types.price_cap_vnd; dish_prices.price_vnd,status,effective_from | price_cap là ngưỡng; dish_prices là giá món. Không mapping trực tiếp thành giá suất public; cần delta/nguồn được duyệt | E8-Q03; O-02 |
| days / UI03/04 | menus.id,version,status,customer_id; menu_days.service_date; menu_day_items.dish_id,recipe_id,slot | E2 chỉ tra cứu PUBLISHED; menu theo khách không tự công khai tên/điểm/giá. Projection chỉ mẫu được cho phép | E8-Q04 |
| dish label / UI03 | dishes.name,status,image_file_id | Không cost_tier, approved_by hoặc thuộc tính nội bộ khác | E8-Q04/09 |
| quantity / UI03 | recipes.id,version_no,effective_from,status,portion_code; recipe_items.qty_std,unit | Định lượng sống theo công thức đã gắn; không suy min/max hoặc nhiều cỡ; mức chi tiết nguyên liệu công khai chờ duyệt | E8-Q04; O-02 |
| allergy / UI03 | dish_allergens.dish_id,allergen_id; allergens.code,name | Ghép tập chất gây dị ứng đúng món/version; schema chưa có cờ kiểm đầy đủ, [] không mặc định không dị ứng | E8-Q04 |
| four nutrients / UI03 | nutrition_calculations.id,menu_version,inputs_snapshot,totals,service_date; nutrient_value_revisions.version | Adapter lấy energyKcal/proteinG/fatG/carbG theo E4, không raw inputs_snapshot/scope_snapshot; schema không có approved status | E8-Q04; NUTR-Q02/03/04 |
| admin rights | users.id; user_roles; delegations | Kiểm AUTH hiện tại; quyền PUB mới đề xuất, không tự cấp role | E8-Q08 |
| audit admin | audit_logs.actor_user_id,occurred_at,entity,entity_id,action,changes,reason,request_id | Ghi revision/action bất biến; enum/action mới hoặc actor anonymous không tự sửa bảng; lead audit không dùng fake user | E8-Q08/12 |
| public image / UI01/02/09 | files.id,mime_type,size_bytes,is_public,storage_key | Dùng public URL đã kiểm quyền; không trả storage_key; file.is_public không thay phê duyệt nội dung | E8-Q09 |
| Cost gate internal | menu_cost_snapshots; cost_recalculations; ingredient_prices; cost_allowances | Chỉ tham chiếu nội bộ qua cổng MENU khi cần; tuyệt đối không truyền số/chi tiết lên public | E8-Q04/05 |
| lead / UI05/08 | Không có bảng lead/CMS/redirect trong65 bảng | customers/eaters/order_discount_records không là nơi lưu lead. Delta đề xuất riêng | E8-Q06 |

WordPress article sourceId/title/body/mediaRefs/originalPublishedAt/status → pub_content_revisions (delta) và pub_url_mappings.inventoryRef/sourceURL/targetPath; giữ provenance sourceId/hash/ngày nguồn riêng ngày chuyển. Không có bảng CMS trong65 bảng để ánh xạ vật lý đã freeze. Media thiếu hoặc trùng sourceId phải rà trước công bố; phương thức chuyển chờ E8-Q01/08/09.

[Delta dữ liệu](../srs/data-dictionary.md) · [Phụ thuộc](../review/dependencies.md).
