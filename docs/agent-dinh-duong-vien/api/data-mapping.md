# Mapping dữ liệu E9 → schema hiện có

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-05; E9-Q15 |


Draft · 12/11/2026 · [DBML 65 bảng](../../nen-tang/srs/schema.dbml) và [ERD](../../nen-tang/srs/erd.md) chỉ đọc. Mọi mapping/adapter là đề xuất chưa freeze; không migration.

| Field API / UI | Nguồn hiện có | Quy tắc chuyển / khoảng trống |
| :--- | :--- | :--- |
| publicMealTypeRef / UI01 | meal_types.id, name, is_public, status, version | ACTIVE + public theo nguồn; token tham chiếu public đề xuất; không expose price_cap_vnd làm giá bán |
| publicDishRef, displayName / UI02 | dishes.id/name/status; recipes.id/status/version và hiệu lực | Đúng recipe của ngày, O-02 chưa chốt nhiều cỡ; không dùng recipe ngoài duyệt |
| portion / UI02 | recipe_items.qty_std, đơn vị dùng/quy đổi đã xác nhận | Chỉ projection định lượng được phép; không kèm purchase price/hao hụt cost nội bộ |
| allergenStatus/labels / UI02 | dish_allergens, allergens | [] chưa được xác nhận không là không dị ứng; trạng thái nguồn chờ E9-Q12 |
| safeCheck / UI02/03 | menu_rules; phép FR-MENU-RUL-002 không lưu | Không dùng menu_rule_results của MENU khác; gắn candidate hash/ruleSetVersion trong delta; loại cả rule kinh tế và detail nhạy cảm |
| safeNutrition / UI02 | nutrition_calculations.id/totals/inputs_snapshot/client_revision; nutrient_value_revisions | Chỉ totals/nguồn đã lọc; không serialize nguyên inputs_snapshot; E4 thiếu adapter candidate chưa lưu thì BLOCKED, không ghi menus lách |
| sessionRef / UI01 | agent_runs.session_ref; users.id/user_type khi có tài khoản | Nullable user_id có sẵn không chứng minh guest được duyệt; Q02/10 cần lifecycle/consent; users/eaters không phải lead |
| runRef/status / UI02 | agent_runs.id/agent_code/status/created_at | agent_code DINH_DUONG_VIEN; metadata có thể dùng, không cho model SELECT raw bảng runs |
| candidate/evidence / UI02/03 | agent_run_contexts có candidate_revision/hash/snapshot/evidence_snapshot | actor_id NOT NULL và applied_menu_id thiết kế E5; không khẳng định reuse được guest. Tách delta AIN, không ghi applied_menu_id |
| tool event an toàn / nội bộ | agent_tool_events.run_id/seq/tool_name/status/request_id/safe_summary | Unique(run_id,seq); chỉ metadata đã lọc; không raw cost/sức khỏe; không endpoint log cho khách |
| AI usage / UI05 | agent_runs.input_tokens/output_tokens/cost_vnd; contexts.usage_status | cost_vnd hiện bigint không quyết định đơn vị/provider; không đủ ledger/reservation/ngày/group. Không coi null=0; cần delta Q07/13 |
| hạn mức / UI05 | parameters.code/scope_type/scope_id/value/effective_from/status/version | GLOBAL/KITCHEN/CUSTOMER/SERVICE_POINT không có USER_GROUP; không giả định thêm scope sẵn; đề xuất policy riêng hoặc extension sau duyệt |
| audit cấu hình / nội bộ | audit_logs.actor_user_id/on_behalf_user_id/changes/reason/request_id | Audit nền bất biến; actor service cho hành động hệ thống, guest attribution còn Q02; nội dung chat không nhét vào changes |
| proposal/source/contact/receipt / UI04 | Chưa có bảng proposal/lead E9 được duyệt trong65 bảng | Delta riêng; không ghi customers/eaters/orders; E8 lead cũng nháp chưa contract |
| price / UI02 | Không mapping hiện hành được chọn | E9-Q04/E8-Q03 BLOCKED; không lấy price_cap/dish_prices/hợp đồng mặc định |

## Delta đề xuất, không merge

| Tên tạm | Khóa/trường tối thiểu | Invariant / gate |
| :--- | :--- | :--- |
| ain_sessions | id, principalRef, identityPolicyVersion, consentRef, state, createdAt, expiresAt | Identity/retention Q02/10; không raw sức khỏe; không tự tạo users guest |
| ain_candidates | id, sessionRef, runRef, revision, parentRevision, canonicalHash, safeContent, evidenceRefs, sourceVersions, state | Unique(sessionRef,id,revision); evidence phải cùng hash; không official MENU |
| ain_proposals | id, ownerRef, candidateRef/revision/hash, source, contactRef, consentRef, requestKey/bodyHash, state, receiptRef | ACK chỉ khi lưu bền vững; unique(owner,route,key); Q06/10/13; không lead CRM giả |
| ain_limit_policies | id, groupRef, version, countPolicy, dailyCap, unit, timezone, effectiveAt, approvalRef | Giá trị chưa chọn; không ghi quá khứ; duyệt theo Q08 và E1 |
| ain_budget_reservations | id, principal/group, dayKey, policyRef, runRef, upperBound, state, requestKey | Admission atomic; không release UNKNOWN; Q07/13 |
| ain_usage_events | id, runRef, providerEventRef, dayKey, usageState, amount/unit, reservationRef, sourceHash | Unique event; không sửa mất lịch sử; confirmed/reserved reconciliation, unknown khác0 |

> Chờ E9-Q15: XC-05. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-05](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Sáu tên là delta sơ bộ để thảo luận, không cam kết sáu bảng vật lý hay schema mở rộng chính thức. Quan hệ proposal→candidate→run/session và reservation→policy/run→usage phải kiểm ownership/scope; không có quan hệ health profile. Encryption, retention/xóa/ẩn danh và audit guest chờ Q10; không lưu raw input chỉ vì agent_runs.request_text hiện NOT NULL. Cần adapter/tách kho an toàn trước reuse.
