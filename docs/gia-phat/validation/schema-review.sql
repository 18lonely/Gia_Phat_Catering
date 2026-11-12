-- REVIEW ONLY: exported from DBML v0.5.0 on 2026-11-11. Not executed; not a migration.
-- Business CHECK/atomicity and legacy backfill require design review before implementation.
CREATE TABLE `kitchens` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(120) NOT NULL,
  `address` varchar(255),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `users` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `user_type` varchar(24) NOT NULL COMMENT 'STAFF | CUSTOMER | EATER | SERVICE',
  `username` varchar(64) UNIQUE NOT NULL COMMENT 'Dạng tên đăng nhập: điểm mở N-01',
  `password_hash` varchar(255) COMMENT 'Argon2id; null với SERVICE',
  `full_name` varchar(120) NOT NULL,
  `phone` varchar(15),
  `email` varchar(255),
  `status` varchar(24) NOT NULL DEFAULT 'PENDING_PASSWORD' COMMENT 'PENDING_PASSWORD | ACTIVE | TEMP_LOCKED | LOCKED',
  `failed_attempts` tinyint NOT NULL DEFAULT 0 COMMENT 'BR-SEC-002',
  `locked_until` datetime(3),
  `temp_password_expires_at` datetime(3) COMMENT 'BR-SEC-004',
  `customer_id` bigint COMMENT 'Bắt buộc khi user_type là CUSTOMER, EATER',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `user_roles` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `role_code` varchar(24) NOT NULL COMMENT 'GIAM_DOC | DINH_DUONG_VIEN | QL_CO_SO | BEP_TRUONG | KT_MUA_HANG | KT_DOANH_THU | QUAN_TRI | NGUOI_DAT_TONG | NGUOI_NHAN | NGUOI_AN',
  `kitchen_id` bigint COMMENT 'Bắt buộc với QL_CO_SO, BEP_TRUONG (BR-SEC-007)',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `sessions` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `refresh_token_hash` char(64) UNIQUE NOT NULL,
  `issued_at` datetime(3) NOT NULL,
  `expires_at` datetime(3) NOT NULL COMMENT 'BR-SEC-003: 7 ngày',
  `revoked_at` datetime(3),
  `replaced_by_id` bigint COMMENT 'Phiên thay thế khi xoay vòng refresh token',
  `ip` varchar(45),
  `user_agent` varchar(255)
);

CREATE TABLE `login_logs` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `occurred_at` datetime(3) NOT NULL,
  `username` varchar(64) NOT NULL,
  `user_id` bigint,
  `result` varchar(24) NOT NULL COMMENT 'SUCCESS | WRONG_PASSWORD | LOCKED | RATE_LIMITED',
  `ip` varchar(45),
  `user_agent` varchar(255)
);

CREATE TABLE `delegations` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `from_user_id` bigint NOT NULL,
  `to_user_id` bigint NOT NULL COMMENT 'Khác from_user_id',
  `permission_code` varchar(64) NOT NULL,
  `valid_from` date NOT NULL,
  `valid_to` date NOT NULL COMMENT '>= valid_from',
  `reason` varchar(500) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `audit_logs` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `occurred_at` datetime(3) NOT NULL,
  `actor_user_id` bigint NOT NULL,
  `on_behalf_user_id` bigint COMMENT 'Người dùng đang dùng agent',
  `entity` varchar(48) NOT NULL,
  `entity_id` bigint NOT NULL,
  `action` varchar(24) NOT NULL COMMENT 'CREATE | UPDATE | CANCEL | APPROVE | REJECT | PUBLISH | LOCK | REOPEN',
  `changes` json COMMENT 'Mảng {field, old, new}',
  `reason` varchar(500) COMMENT '>= 10 ký tự với thao tác thuộc BR-AUD-001',
  `request_id` char(36) NOT NULL
);

CREATE TABLE `parameters` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(48) NOT NULL COMMENT 'Danh mục ở SRS nền tảng phụ lục 4.3',
  `scope_type` varchar(24) NOT NULL COMMENT 'GLOBAL | KITCHEN | CUSTOMER | SERVICE_POINT',
  `scope_id` bigint COMMENT 'Null khi GLOBAL',
  `value` varchar(255) NOT NULL,
  `effective_from` date NOT NULL COMMENT 'BR-SYS-001: không sửa quá khứ',
  `status` varchar(24) NOT NULL DEFAULT 'PENDING' COMMENT 'PENDING | APPROVED | REJECTED',
  `approved_by` bigint COMMENT 'Khác created_by (BR-SEC-008)',
  `approved_at` datetime(3),
  `reason` varchar(500) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `notifications` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `type` varchar(48) NOT NULL,
  `severity` varchar(16) NOT NULL DEFAULT 'INFO' COMMENT 'INFO | WARN | ALERT',
  `title` varchar(200) NOT NULL,
  `body` varchar(1000),
  `entity` varchar(48),
  `entity_id` bigint,
  `status` varchar(16) NOT NULL DEFAULT 'NEW' COMMENT 'NEW | SEEN | DONE',
  `created_at` datetime(3) NOT NULL,
  `seen_at` datetime(3),
  `done_at` datetime(3)
);

CREATE TABLE `files` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `storage_key` varchar(255) UNIQUE NOT NULL,
  `original_name` varchar(255) NOT NULL,
  `mime_type` varchar(64) NOT NULL COMMENT 'image/jpeg | image/png | image/webp | application/pdf',
  `size_bytes` int NOT NULL COMMENT '<= 10 MB (FR-SYS-FILE-001)',
  `is_public` boolean NOT NULL DEFAULT false,
  `entity` varchar(48),
  `entity_id` bigint,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint
);

CREATE TABLE `agent_runs` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `agent_code` varchar(32) NOT NULL COMMENT 'NOI_BO | DINH_DUONG_VIEN',
  `user_id` bigint COMMENT 'Null với khách vãng lai',
  `session_ref` varchar(64) COMMENT 'Phiên ẩn danh của khách vãng lai',
  `request_text` text NOT NULL,
  `tool_calls` json COMMENT 'Công cụ đã gọi và tham số',
  `result_summary` text,
  `status` varchar(16) NOT NULL COMMENT 'QUEUED | RUNNING | DONE | FAILED | REJECTED',
  `input_tokens` int,
  `output_tokens` int,
  `cost_vnd` bigint,
  `started_at` datetime(3),
  `finished_at` datetime(3),
  `created_at` datetime(3) NOT NULL
);

CREATE TABLE `change_requests` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `entity` varchar(48) NOT NULL COMMENT 'Tên bảng nghiệp vụ, ví dụ dishes, menu_rules',
  `entity_key` varchar(32) NOT NULL COMMENT 'id dạng chuỗi, hoặc code với bảng có khoá chính là mã',
  `proposed_changes` json NOT NULL COMMENT 'Mảng {field, old, new}',
  `reason` varchar(500) NOT NULL COMMENT '>= 10 ký tự (BR-AUD-001)',
  `status` varchar(24) NOT NULL DEFAULT 'PENDING' COMMENT 'PENDING | APPROVED | REJECTED | WITHDRAWN | STALE',
  `requested_by` bigint NOT NULL,
  `requested_at` datetime(3) NOT NULL,
  `applied_at` datetime(3)
);

CREATE TABLE `approvals` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `entity` varchar(48) NOT NULL COMMENT 'menus, recipes, dishes, dish_prices, change_requests...',
  `entity_id` bigint NOT NULL,
  `round_no` smallint NOT NULL DEFAULT 1 COMMENT 'Tăng mỗi lần gửi duyệt lại',
  `approver_user_id` bigint NOT NULL COMMENT 'Khác người tạo và người sửa cuối (BR-SEC-008)',
  `delegation_id` bigint COMMENT 'Khi duyệt bằng quyền được uỷ',
  `decision` varchar(16) NOT NULL COMMENT 'APPROVED | REJECTED',
  `reason` varchar(500) COMMENT 'Bắt buộc khi REJECTED',
  `decided_at` datetime(3) NOT NULL
);

CREATE TABLE `ingredient_groups` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(80) NOT NULL COMMENT 'Lợn, gà, bò, ếch, tôm, cá... Danh sách: điểm mở H-3',
  `protein_source` varchar(24) COMMENT 'MEAT | FISH | EGG | SEAFOOD | BEAN — dùng cho BR-MENU-050',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `ingredients` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(120) NOT NULL,
  `group_id` bigint NOT NULL,
  `buy_unit` varchar(16) NOT NULL COMMENT 'kg, bìa, quả, lít, bó...',
  `use_unit` varchar(16) NOT NULL COMMENT 'g, bìa, quả, ml',
  `conversion_factor` decimal(12,4) NOT NULL COMMENT 'Số đơn vị dùng trong 1 đơn vị mua; > 0',
  `waste_pct` decimal(5,2) COMMENT 'Bắt buộc nếu has_bone_or_shell (BR-COST-010)',
  `has_bone_or_shell` boolean NOT NULL DEFAULT false,
  `storage_type` varchar(24) NOT NULL COMMENT 'FRESH | FROZEN | DRY',
  `stable_supply` boolean NOT NULL DEFAULT true COMMENT 'BR-MENU-044',
  `in_cost` boolean NOT NULL DEFAULT true COMMENT 'Định nghĩa cost: điểm mở O-01',
  `status` varchar(24) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE | INACTIVE',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `ingredient_seasons` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `ingredient_id` bigint NOT NULL,
  `month_from` tinyint NOT NULL COMMENT '1-12',
  `month_to` tinyint NOT NULL COMMENT '1-12'
);

CREATE TABLE `cooking_methods` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(80) NOT NULL COMMENT 'Luộc, hấp, kho, rang, xào, sốt, chiên... Danh sách: điểm mở H-8',
  `is_fried` boolean NOT NULL DEFAULT false COMMENT 'BR-MENU-021, 022',
  `is_low_fat` boolean NOT NULL DEFAULT false COMMENT 'Được dùng cho món Healthy: điểm mở H-1',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `allergens` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(80) NOT NULL
);

CREATE TABLE `dishes` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(160) NOT NULL,
  `description` varchar(1000),
  `role` varchar(24) NOT NULL COMMENT 'MAIN | SIDE | VEG | SOUP',
  `main_group_id` bigint NOT NULL COMMENT 'BR-MENU-010 -> 015',
  `cooking_method_id` bigint NOT NULL COMMENT 'BR-MENU-020 -> 023',
  `base_dish_id` bigint COMMENT 'Món gốc (BR-MENU-014)',
  `is_healthy` boolean NOT NULL DEFAULT false COMMENT 'BR-MENU-002, 003',
  `is_sour` boolean NOT NULL DEFAULT false COMMENT 'BR-MENU-030',
  `texture` varchar(24) NOT NULL DEFAULT 'NEUTRAL' COMMENT 'DRY | SAUCE | NEUTRAL (BR-MENU-031, 032)',
  `is_light` boolean NOT NULL DEFAULT false COMMENT 'BR-MENU-033',
  `is_complex` boolean NOT NULL DEFAULT false COMMENT 'BR-MENU-040, 041',
  `transport_ok` boolean NOT NULL DEFAULT true COMMENT 'BR-MENU-042',
  `bulk_ok` boolean NOT NULL DEFAULT true COMMENT 'BR-MENU-043',
  `cost_tier` varchar(24) NOT NULL COMMENT 'LOW | HIGH (BR-COST-006)',
  `is_special` boolean NOT NULL DEFAULT false COMMENT 'BR-COST-007',
  `image_file_id` bigint,
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | PENDING | ACTIVE | INACTIVE',
  `approved_by` bigint COMMENT 'Khác created_by',
  `approved_at` datetime(3),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `dish_allergens` (
  `dish_id` bigint NOT NULL,
  `allergen_id` bigint NOT NULL,
  PRIMARY KEY (`dish_id`, `allergen_id`)
);

CREATE TABLE `dish_conflicts` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `dish_a_id` bigint NOT NULL,
  `dish_b_id` bigint NOT NULL COMMENT 'dish_a_id < dish_b_id',
  `note` varchar(255),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `recipes` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `dish_id` bigint NOT NULL,
  `portion_code` varchar(16) NOT NULL DEFAULT 'STD' COMMENT 'Cỡ định lượng: điểm mở O-02',
  `version_no` int NOT NULL,
  `effective_from` date NOT NULL,
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | PENDING | ACTIVE | SUPERSEDED',
  `approved_by` bigint COMMENT 'Khác created_by (BR-SEC-008)',
  `approved_at` datetime(3),
  `note` varchar(500),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `recipe_items` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `recipe_id` bigint NOT NULL,
  `ingredient_id` bigint NOT NULL,
  `is_main` boolean NOT NULL COMMENT 'BR-COST-009',
  `qty_min` decimal(10,3) NOT NULL COMMENT '> 0',
  `qty_max` decimal(10,3) NOT NULL COMMENT '>= qty_min',
  `qty_std` decimal(10,3) NOT NULL COMMENT 'Trong [qty_min, qty_max]; dùng tính cost và dinh dưỡng',
  `unit` varchar(16) NOT NULL COMMENT 'Bằng ingredients.use_unit. Định lượng SỐNG theo docx'
);

CREATE TABLE `dish_prices` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `dish_id` bigint NOT NULL,
  `portion_code` varchar(16) NOT NULL DEFAULT 'STD',
  `price_vnd` bigint NOT NULL COMMENT 'Giá bán, đã gồm VAT (D-15, D-18)',
  `effective_from` date NOT NULL,
  `status` varchar(24) NOT NULL DEFAULT 'PENDING' COMMENT 'PENDING | APPROVED',
  `approved_by` bigint COMMENT 'Khác created_by',
  `approved_at` datetime(3),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `meal_types` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(120) NOT NULL,
  `price_cap_vnd` bigint NOT NULL COMMENT 'Ngưỡng giá suất, đã gồm VAT (BR-COST-012)',
  `main_offered` tinyint NOT NULL DEFAULT 3 COMMENT 'BR-MENU-001',
  `main_pick` tinyint NOT NULL DEFAULT 1 COMMENT 'D-04',
  `side_count` tinyint NOT NULL COMMENT 'BR-MENU-005',
  `has_veg` boolean NOT NULL DEFAULT true,
  `has_soup` boolean NOT NULL DEFAULT true,
  `is_public` boolean NOT NULL DEFAULT false COMMENT 'Hiện trên website (D-10)',
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | ACTIVE | INACTIVE',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `menus` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `meal_type_id` bigint NOT NULL,
  `customer_id` bigint COMMENT 'Null = thực đơn chung của loại suất',
  `week_start` date NOT NULL COMMENT 'Là thứ Hai',
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | CHECKED | PENDING | APPROVED | PUBLISHED | WITHDRAWN',
  `rule_score` smallint COMMENT '0-100',
  `source` varchar(24) NOT NULL DEFAULT 'MANUAL' COMMENT 'MANUAL | AGENT_INTERNAL | AGENT_CUSTOMER',
  `agent_run_id` bigint,
  `approved_by` bigint COMMENT 'Khác created_by (BN-17)',
  `approved_at` datetime(3),
  `published_at` datetime(3),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `menu_days` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_id` bigint NOT NULL,
  `service_date` date NOT NULL,
  `default_dish_id` bigint COMMENT 'Món mặc định (D-14); bắt buộc trước khi công bố'
);

CREATE TABLE `menu_day_items` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_day_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL,
  `recipe_id` bigint NOT NULL COMMENT 'Phiên bản hiệu lực tại ngày phục vụ, chụp lại',
  `slot` varchar(24) NOT NULL COMMENT 'MAIN | SIDE | VEG | SOUP; khớp dishes.role',
  `sort_order` tinyint NOT NULL DEFAULT 0
);

CREATE TABLE `menu_rules` (
  `code` varchar(16) PRIMARY KEY COMMENT 'BR-MENU-xxx, BR-COST-xxx',
  `name` varchar(200) NOT NULL,
  `rule_type` varchar(24) NOT NULL COMMENT 'HARD | SOFT',
  `penalty` tinyint NOT NULL DEFAULT 0 COMMENT '0 với HARD; 1, 2, 3 với SOFT',
  `scope` varchar(16) NOT NULL COMMENT 'DAY | WEEK',
  `params` json COMMENT 'Con số được duyệt ở DL-01',
  `is_active` boolean NOT NULL DEFAULT true,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint
);

CREATE TABLE `menu_rule_results` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_id` bigint NOT NULL,
  `menu_day_id` bigint COMMENT 'Null với quy tắc cấp tuần',
  `rule_code` varchar(16) NOT NULL,
  `passed` boolean NOT NULL,
  `detail` varchar(500),
  `waiver_reason` varchar(500) COMMENT 'Bắt buộc với quy tắc mềm-nặng không đạt',
  `checked_at` datetime(3) NOT NULL
);

CREATE TABLE `suppliers` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(160) NOT NULL,
  `phone` varchar(15),
  `supplier_type` varchar(24) NOT NULL COMMENT 'REGULAR | MARKET_VENDOR',
  `status` varchar(24) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE | INACTIVE',
  `note` varchar(1000) COMMENT 'Ghi chú nhà cung cấp',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `ingredient_prices` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `ingredient_id` bigint NOT NULL,
  `supplier_id` bigint NOT NULL,
  `kitchen_id` bigint COMMENT 'Null = áp dụng cả 2 cơ sở',
  `price_vnd` bigint NOT NULL COMMENT 'Gia cost cuoi cung gom VAT phai tra / buy_unit; server tinh. Legacy chua xac minh khong tu cong VAT',
  `quoted_unit_price` decimal(18,6) COMMENT 'Gia bao goc; null voi legacy, khong suy dien nguoc',
  `price_basis` varchar(24) NOT NULL DEFAULT 'LEGACY_UNVERIFIED' COMMENT 'INCLUSIVE | EXCLUSIVE | FINAL_CONFIRMED | LEGACY_UNVERIFIED; new write khong nhan legacy',
  `vat_rate_pct` decimal(9,6) COMMENT 'Nullable, khong mac dinh0; EXCLUSIVE can rate hoac amount, khong ca hai',
  `vat_unit_amount` decimal(18,6) COMMENT 'VAT phai tra / buy_unit, nullable; neu co rate thi server tinh amount',
  `pricing_evidence` varchar(1000) COMMENT 'Nguon xac nhan gia cuoi; FINAL_CONFIRMED bat buoc; khong phan loai thue phap ly',
  `pricing_verified_at` datetime(3) COMMENT 'Chua xac minh thi null, khong suy ra tu created_at',
  `pricing_verified_by` bigint,
  `normalization_version` varchar(32) COMMENT 'Thuat toan chuan hoa gia; null voi legacy',
  `effective_from` date NOT NULL COMMENT 'BR-COST-004',
  `is_reference` boolean NOT NULL DEFAULT false COMMENT 'Đặt bằng giao dịch theo BR-PRC-005; dòng đầu tiên tự được chọn',
  `source_file_id` bigint,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `cost_estimates` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_day_id` bigint NOT NULL,
  `kitchen_id` bigint NOT NULL,
  `version_no` int NOT NULL COMMENT 'Tăng theo ngày thực đơn và cơ sở, không ghi đè bản cũ',
  `batch_key` char(36) NOT NULL COMMENT 'Cùng mã cho lần lập dự toán tuần; dùng gộp đúng bộ phiên bản',
  `servings` int NOT NULL COMMENT 'Tổng lượt chọn món chính / main_pick; nguyên > 0',
  `main_pick` tinyint NOT NULL COMMENT 'Số món chính chọn trên suất đã chụp; > 0',
  `main_cost_method` varchar(24) NOT NULL COMMENT 'DAT_NHAT | BINH_QUAN | MAC_DINH',
  `total_cost_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `cost_per_serving_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `revenue_ex_vat_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `cost_pct` decimal(12,2) NOT NULL COMMENT 'Theo số suất từng món, nửa lên 2 chữ số; có thể > 100',
  `menu_cost_pct` decimal(12,2) NOT NULL COMMENT 'Cost % theo phương pháp kiểm thực đơn; không nhầm cost_pct dự toán',
  `threshold_pct` decimal(5,2) NOT NULL,
  `price_as_of` date NOT NULL COMMENT 'Ngày lấy giá nhập',
  `inputs_snapshot` json NOT NULL COMMENT 'Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống',
  `computed_at` datetime(3) NOT NULL,
  `computed_by` bigint NOT NULL
);

CREATE TABLE `cost_estimate_lines` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `estimate_id` bigint NOT NULL,
  `ingredient_id` bigint NOT NULL,
  `ingredient_price_id` bigint COMMENT 'Null khi nguyên liệu ngoài cost',
  `supplier_id` bigint,
  `ingredient_name` varchar(120) NOT NULL,
  `supplier_name` varchar(160),
  `price_effective_from` date,
  `in_cost` boolean NOT NULL,
  `use_unit` varchar(16) NOT NULL,
  `buy_unit` varchar(16) NOT NULL,
  `conversion_factor` decimal(12,4) NOT NULL COMMENT '> 0, đã chụp',
  `total_use_qty` decimal(24,8) NOT NULL COMMENT 'Tổng định lượng sau hao hụt từ các component',
  `buy_qty` decimal(18,2) NOT NULL COMMENT 'Làm tròn lên 2 chữ số sau gộp theo nguyên liệu',
  `price_per_buy_unit_vnd` bigint COMMENT '> 0 khi in_cost; null khi ngoài cost',
  `amount_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0'
);

CREATE TABLE `cost_sheets` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `dish_id` bigint NOT NULL COMMENT 'Món đặc thù',
  `recipe_id` bigint NOT NULL COMMENT 'Phiên bản công thức đã tính',
  `kitchen_id` bigint NOT NULL COMMENT 'Cơ sở tính giá',
  `calculation_date` date NOT NULL COMMENT 'Ngày lấy công thức và giá',
  `status` varchar(24) NOT NULL DEFAULT 'PENDING' COMMENT 'PENDING | APPROVED | REJECTED',
  `total_cost_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `inputs_snapshot` json NOT NULL COMMENT 'Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống',
  `note` varchar(1000) COMMENT 'Ghi chú người lập',
  `approved_by` bigint COMMENT 'Người duyệt cuối, khác người lập',
  `approved_at` datetime(3) COMMENT 'Thời điểm duyệt UTC',
  `created_at` datetime(3) NOT NULL COMMENT 'Thời điểm tạo, UTC',
  `created_by` bigint NOT NULL COMMENT 'Người lập'
);

CREATE TABLE `cost_sheet_lines` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `sheet_id` bigint NOT NULL COMMENT 'Bảng tính cha',
  `recipe_id` bigint NOT NULL COMMENT 'Công thức nguồn',
  `ingredient_id` bigint NOT NULL COMMENT 'Nguyên liệu nguồn',
  `ingredient_price_id` bigint COMMENT 'Null chỉ khi in_cost = false',
  `supplier_id` bigint COMMENT 'Nhà cung cấp đã chọn; null nếu không tính cost',
  `ingredient_name` varchar(120) NOT NULL COMMENT 'Tên nguyên liệu tại lúc chụp',
  `supplier_name` varchar(160) COMMENT 'Tên nhà cung cấp tại lúc chụp',
  `price_effective_from` date COMMENT 'Ngày hiệu lực của giá đã dùng',
  `in_cost` boolean NOT NULL COMMENT 'Cờ tính vào cost tại lúc chụp',
  `is_main` boolean NOT NULL COMMENT 'Nguyên liệu chính trong công thức',
  `qty_std` decimal(10,3) NOT NULL COMMENT 'Định lượng chuẩn trước hao hụt; > 0',
  `use_unit` varchar(16) NOT NULL COMMENT 'Đơn vị dùng đã chụp',
  `buy_unit` varchar(16) NOT NULL COMMENT 'Đơn vị mua đã chụp',
  `conversion_factor` decimal(12,4) NOT NULL COMMENT 'Số đơn vị dùng trên đơn vị mua; > 0',
  `waste_pct` decimal(5,2) NOT NULL COMMENT 'Hao hụt đã chụp, 0 <= giá trị < 100',
  `price_per_buy_unit_vnd` bigint COMMENT 'Giá trên đơn vị mua; > 0 khi in_cost = true',
  `line_cost_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0'
);

CREATE TABLE `cost_allowances` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(120) NOT NULL COMMENT 'Tên khoản khoán; chuẩn hoá như BR-CAT-001',
  `meal_type_id` bigint COMMENT 'Null = mọi loại suất',
  `amount_vnd` bigint NOT NULL COMMENT 'Số nguyên đồng trên suất; >= 0',
  `effective_from` date NOT NULL COMMENT 'Ngày bắt đầu hiệu lực',
  `status` varchar(24) NOT NULL DEFAULT 'PENDING' COMMENT 'PENDING | APPROVED | REJECTED',
  `reason` varchar(500) NOT NULL COMMENT 'Lý do đề nghị; ít nhất 10 ký tự',
  `approved_by` bigint COMMENT 'Khác người lập',
  `approved_at` datetime(3),
  `created_at` datetime(3) NOT NULL COMMENT 'Thời điểm tạo, UTC',
  `created_by` bigint NOT NULL COMMENT 'Người lập'
);

CREATE TABLE `menu_cost_snapshots` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_day_id` bigint NOT NULL COMMENT 'Ngày của thực đơn được duyệt',
  `kitchen_id` bigint NOT NULL COMMENT 'Một bản cho mỗi cơ sở được kiểm',
  `approval_round_no` smallint NOT NULL COMMENT 'Vòng duyệt của menus, khớp approvals.round_no',
  `service_date` date NOT NULL COMMENT 'Ngày phục vụ được chụp',
  `cost_per_serving_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `revenue_ex_vat_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0',
  `cost_pct` decimal(12,2) NOT NULL COMMENT 'Làm tròn nửa lên 2 chữ số; >= 0, có thể > 100',
  `threshold_pct` decimal(5,2) NOT NULL COMMENT 'Ngưỡng đã dùng',
  `result` varchar(24) NOT NULL COMMENT 'DAT | KHONG_DAT; cảnh báo cho phép duyệt bản KHONG_DAT',
  `inputs_snapshot` json NOT NULL COMMENT 'Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống',
  `created_at` datetime(3) NOT NULL COMMENT 'Thời điểm tạo, UTC',
  `created_by` bigint NOT NULL COMMENT 'Người lập'
);

CREATE TABLE `menu_cost_snapshot_lines` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `snapshot_id` bigint NOT NULL COMMENT 'Bản chụp ngày/cơ sở',
  `dish_id` bigint NOT NULL COMMENT 'Món đã dùng',
  `recipe_id` bigint NOT NULL COMMENT 'Công thức nguồn',
  `ingredient_id` bigint NOT NULL COMMENT 'Nguyên liệu nguồn',
  `ingredient_price_id` bigint COMMENT 'Null chỉ khi in_cost = false',
  `supplier_id` bigint COMMENT 'Nhà cung cấp đã chọn; null nếu không tính cost',
  `ingredient_name` varchar(120) NOT NULL COMMENT 'Tên nguyên liệu tại lúc chụp',
  `supplier_name` varchar(160) COMMENT 'Tên nhà cung cấp tại lúc chụp',
  `price_effective_from` date COMMENT 'Ngày hiệu lực của giá đã dùng',
  `in_cost` boolean NOT NULL COMMENT 'Cờ tính vào cost tại lúc chụp',
  `is_main` boolean NOT NULL COMMENT 'Nguyên liệu chính trong công thức',
  `qty_std` decimal(10,3) NOT NULL COMMENT 'Định lượng chuẩn trước hao hụt; > 0',
  `use_unit` varchar(16) NOT NULL COMMENT 'Đơn vị dùng đã chụp',
  `buy_unit` varchar(16) NOT NULL COMMENT 'Đơn vị mua đã chụp',
  `conversion_factor` decimal(12,4) NOT NULL COMMENT 'Số đơn vị dùng trên đơn vị mua; > 0',
  `waste_pct` decimal(5,2) NOT NULL COMMENT 'Hao hụt đã chụp, 0 <= giá trị < 100',
  `price_per_buy_unit_vnd` bigint COMMENT 'Giá trên đơn vị mua; > 0 khi in_cost = true',
  `line_cost_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0'
);

CREATE TABLE `cost_recalculations` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `snapshot_id` bigint NOT NULL COMMENT 'Bản duyệt gốc dùng so sánh',
  `event_key` varchar(120) NOT NULL COMMENT 'Khoá sự kiện giá để retry không trùng',
  `result` varchar(24) NOT NULL COMMENT 'DAT | KHONG_DAT | KHONG_XAC_DINH',
  `cost_per_serving_vnd` decimal(24,8) COMMENT 'Null khi không tính được',
  `cost_pct` decimal(12,2) COMMENT 'Null khi không tính được; không gán 0',
  `inputs_snapshot` json NOT NULL COMMENT 'Bản chụp đầu vào theo hợp đồng JSON ở ERD mục 5.4; không đọc lại dữ liệu sống',
  `missing_ingredient_ids` json COMMENT 'Danh sách nguyên liệu thiếu giá nếu có',
  `computed_at` datetime(3) NOT NULL COMMENT 'Thời điểm tính lại UTC'
);

CREATE TABLE `cost_alerts` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `menu_day_id` bigint NOT NULL COMMENT 'Duy nhất một cảnh báo mở theo ngày thực đơn',
  `status` varchar(16) NOT NULL DEFAULT 'OPEN' COMMENT 'OPEN | CLOSED',
  `opened_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `closed_at` datetime(3),
  `closed_by` bigint COMMENT 'Null nếu đóng tự động',
  `close_reason` varchar(500) COMMENT 'Bắt buộc khi đóng tay; ít nhất 10 ký tự',
  `close_type` varchar(24) COMMENT 'MENU_REVISED | PRICE_RECOVERED | MANUAL',
  `version` int NOT NULL DEFAULT 1 COMMENT 'Khoá lạc quan'
);

CREATE TABLE `cost_alert_kitchens` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `alert_id` bigint NOT NULL COMMENT 'Cảnh báo ngày',
  `kitchen_id` bigint NOT NULL COMMENT 'Cơ sở bị ảnh hưởng',
  `snapshot_id` bigint NOT NULL COMMENT 'Cost lúc duyệt',
  `latest_recalculation_id` bigint NOT NULL COMMENT 'Cost hiện tại và giá gây thay đổi'
);

CREATE TABLE `cost_estimate_servings` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `estimate_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL COMMENT 'Món chính thuộc ngày dự toán',
  `dish_name` varchar(160) NOT NULL COMMENT 'Tên món đã chụp',
  `servings` int NOT NULL COMMENT 'Số lượt chọn món; nguyên >= 0'
);

CREATE TABLE `cost_estimate_components` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `estimate_line_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL,
  `recipe_id` bigint NOT NULL,
  `dish_name` varchar(160) NOT NULL COMMENT 'Tên món đã chụp',
  `qty_per_serving` decimal(24,8) NOT NULL COMMENT 'Định lượng sau áp hao hụt đúng một lần',
  `servings` int NOT NULL COMMENT 'Số suất món; >= 0',
  `total_use_qty` decimal(24,8) NOT NULL COMMENT 'qty_per_serving x servings',
  `recipe_item_snapshot` json NOT NULL COMMENT 'qty_std, use_unit, in_cost, waste_pct, conversion_factor đã dùng'
);

CREATE TABLE `cost_estimate_allowances` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `estimate_id` bigint NOT NULL,
  `allowance_id` bigint NOT NULL,
  `name` varchar(120) NOT NULL COMMENT 'Tên khoản tại lúc lập',
  `amount_per_serving_vnd` bigint NOT NULL COMMENT 'Đồng trên suất; >= 0',
  `total_amount_vnd` decimal(24,8) NOT NULL COMMENT 'Đồng, giá trị tính trước làm tròn hiển thị; >= 0'
);

CREATE TABLE `nutrient_values` (
  `ingredient_id` bigint PRIMARY KEY,
  `energy_kcal` decimal(7,2) NOT NULL COMMENT 'Trên 100 g phần ăn được',
  `protein_g` decimal(6,2) NOT NULL,
  `fat_g` decimal(6,2) NOT NULL,
  `carb_g` decimal(6,2) NOT NULL,
  `edible_pct` decimal(5,2) NOT NULL DEFAULT 100,
  `grams_per_unit` decimal(8,2) COMMENT 'Bắt buộc khi use_unit không phải g',
  `source` varchar(120) NOT NULL DEFAULT 'Bảng thành phần thực phẩm Việt Nam' COMMENT 'D-17',
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `source_edition` varchar(120) NOT NULL COMMENT 'NUTR-Q01: phai co an ban, khong tu dien cho legacy',
  `source_locator` varchar(120) NOT NULL COMMENT 'Trang hoac ma thuc pham trong nguon'
);

CREATE TABLE `eater_health_profiles` (
  `user_id` bigint PRIMARY KEY,
  `encrypted_payload` blob NOT NULL COMMENT 'AES-256 (NFR-SEC-003). Nội dung: điểm mở O-03',
  `consent_at` datetime(3) NOT NULL,
  `consent_version` varchar(16) NOT NULL,
  `updated_at` datetime(3) NOT NULL
);

CREATE TABLE `customers` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `name` varchar(200) NOT NULL,
  `tax_code` varchar(14),
  `lifecycle_status` varchar(24) NOT NULL DEFAULT 'PROSPECT' COMMENT 'PROSPECT | NEW | SERVING | AT_RISK | PAUSED | CHURNED | REACTIVATED',
  `eater_choice_enabled` boolean NOT NULL DEFAULT true COMMENT 'FEAT-044',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `service_points` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `kitchen_id` bigint NOT NULL COMMENT 'Cơ sở mặc định',
  `name` varchar(160) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `service_schedules` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `service_point_id` bigint NOT NULL,
  `shift` varchar(16) NOT NULL COMMENT 'LUNCH | MORNING | AFTERNOON | DINNER',
  `weekday` tinyint NOT NULL COMMENT '1 = thứ Hai ... 7 = Chủ nhật',
  `delivery_time` time NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `customer_quotas` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `meal_type_id` bigint NOT NULL,
  `effective_from` date NOT NULL,
  `approved_by` bigint,
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `customer_qr_codes` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `service_point_id` bigint,
  `token_hash` char(64) UNIQUE NOT NULL,
  `status` varchar(16) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE | ROTATED | REVOKED',
  `rotated_at` datetime(3),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint
);

CREATE TABLE `eaters` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `service_point_id` bigint NOT NULL,
  `user_id` bigint UNIQUE COMMENT 'Null với người ăn qua QR',
  `display_name` varchar(120),
  `status` varchar(16) NOT NULL DEFAULT 'ACTIVE' COMMENT 'ACTIVE | REMOVED',
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `meal_selections` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `eater_id` bigint NOT NULL,
  `service_date` date NOT NULL,
  `shift` varchar(16) NOT NULL DEFAULT 'LUNCH',
  `service_point_id` bigint NOT NULL,
  `menu_day_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL COMMENT 'Thuộc các món MAIN của menu_day_id (D-04)',
  `portion_code` varchar(16) NOT NULL DEFAULT 'STD' COMMENT 'Điểm mở O-02',
  `source` varchar(24) NOT NULL DEFAULT 'SELF' COMMENT 'SELF | DEFAULT | COORDINATOR',
  `idempotency_key` char(36),
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `version` int NOT NULL DEFAULT 1
);

CREATE TABLE `selection_counters` (
  `menu_day_id` bigint NOT NULL,
  `service_point_id` bigint NOT NULL,
  `shift` varchar(16) NOT NULL,
  `dish_id` bigint NOT NULL,
  `qty` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`menu_day_id`, `service_point_id`, `shift`, `dish_id`)
);

CREATE TABLE `orders` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `code` varchar(32) UNIQUE NOT NULL,
  `service_point_id` bigint NOT NULL,
  `service_date` date NOT NULL,
  `shift` varchar(16) NOT NULL DEFAULT 'LUNCH',
  `meal_type_id` bigint NOT NULL,
  `menu_day_id` bigint NOT NULL,
  `total_servings` int NOT NULL COMMENT 'Do người đặt tổng chốt (D-14)',
  `unit_price_vnd` bigint NOT NULL COMMENT 'Giá suất chụp tại thời điểm order',
  `source` varchar(24) NOT NULL DEFAULT 'PORTAL' COMMENT 'PORTAL | ZALO | PHONE (nhập hộ)',
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | SUBMITTED | LOCKED | IN_PRODUCTION | DELIVERED | CONFIRMED | DISPUTED | RECONCILED',
  `locked_at` datetime(3),
  `created_at` datetime(3) NOT NULL,
  `created_by` bigint,
  `updated_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `version` int NOT NULL DEFAULT 1,
  `cancelled_at` datetime(3),
  `cancelled_reason` varchar(500)
);

CREATE TABLE `order_dish_lines` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `order_id` bigint NOT NULL,
  `dish_id` bigint NOT NULL,
  `qty_selected` int NOT NULL DEFAULT 0 COMMENT 'Người ăn tự chọn',
  `qty_default` int NOT NULL DEFAULT 0 COMMENT 'Gán món mặc định',
  `qty_coordinator` int NOT NULL DEFAULT 0 COMMENT 'Người đặt tổng nhập'
);

CREATE TABLE `customer_price_terms` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `customer_id` bigint NOT NULL,
  `meal_type_id` bigint NOT NULL,
  `quoted_unit_price` decimal(18,6) NOT NULL,
  `sale_price_basis` varchar(24) NOT NULL DEFAULT 'UNKNOWN' COMMENT 'INCLUSIVE | EXCLUSIVE | FINAL_CONFIRMED | UNKNOWN',
  `vat_rate_pct` decimal(9,6) COMMENT 'Null khac0; invoiceRequested khong quyet dinh rate',
  `invoice_requested` boolean COMMENT 'Null=chua hoi; false khong nghia VAT0',
  `evidence` varchar(1000) COMMENT 'Thoa thuan va nguon xac nhan',
  `effective_from` date NOT NULL,
  `effective_to` date COMMENT 'Nullable; rang buoc khong chong lan ACTIVE theo customer/meal type can transaction',
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | ACTIVE | CANCELLED; activation gated cho sales policy',
  `version` int NOT NULL DEFAULT 1,
  `created_by` bigint NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `updated_at` datetime(3)
);

CREATE TABLE `order_pricing_snapshots` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `order_id` bigint NOT NULL,
  `order_version` int NOT NULL,
  `price_term_id` bigint,
  `quoted_unit_price` decimal(18,6) NOT NULL,
  `sale_price_basis` varchar(24) NOT NULL,
  `vat_rate_pct` decimal(9,6),
  `invoice_requested` boolean,
  `servings` int NOT NULL,
  `gross_amount_due` decimal(18,6) COMMENT 'Khong tru khoan chiet khau rieng; null neu UNKNOWN',
  `revenue_ex_vat` decimal(18,6) COMMENT 'Null neu chua du VAT/context; khong lay gross neu invoice=false',
  `context_status` varchar(24) NOT NULL COMMENT 'RESOLVED | UNRESOLVED | LEGACY_UNVERIFIED',
  `captured_at` datetime(3) NOT NULL,
  `captured_by` bigint NOT NULL,
  `inputs_snapshot` json NOT NULL COMMENT 'Bat bien; quyen doc rieng, khong serialize cho agent khach'
);

CREATE TABLE `order_discount_records` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `order_id` bigint NOT NULL,
  `pricing_snapshot_id` bigint NOT NULL,
  `proposal_key` varchar(64) NOT NULL COMMENT 'Khong phai key TTL; unique proposal trong order',
  `calculation_type` varchar(24) NOT NULL COMMENT 'PERCENT | FIXED_PER_SERVING',
  `rate_pct` decimal(9,6) COMMENT 'Chi PERCENT; base chua chot thi draft only',
  `amount_per_serving` decimal(18,6) COMMENT 'Chi FIXED_PER_SERVING; rounding CK-Q03',
  `percent_basis` varchar(24) NOT NULL DEFAULT 'UNRESOLVED' COMMENT 'GROSS | NET | UNRESOLVED; ghi gia dinh draft khong dong CK-Q01',
  `eligible_servings` int COMMENT 'CK-Q02; khong lay qty dish lines thay so suat',
  `quantity_basis` varchar(24) NOT NULL DEFAULT 'UNRESOLVED' COMMENT 'ORDERED | DELIVERED | CONFIRMED | UNRESOLVED',
  `base_amount` decimal(18,6) COMMENT 'Server-derived, null neu chua xac dinh',
  `calculated_amount` decimal(18,6) COMMENT 'So tinh thu, khong phai paid amount; null neu thieu base',
  `status` varchar(24) NOT NULL DEFAULT 'DRAFT' COMMENT 'DRAFT | NEEDS_REVIEW | CONFIRMED | CANCELLED; confirm/cancel da xu ly gated CK-Q04-09',
  `calculation_snapshot` json NOT NULL COMMENT 'Gia dinh, gates, ruleVersion; khong ghi len amountDue cua order',
  `version` int NOT NULL DEFAULT 1,
  `created_by` bigint NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_by` bigint,
  `updated_at` datetime(3)
);

CREATE TABLE `order_discount_events` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `discount_id` bigint NOT NULL,
  `event_key` varchar(64) NOT NULL COMMENT 'Event replay chi ghi mot lan',
  `event_type` varchar(32) NOT NULL COMMENT 'DRAFT_CREATED | DRAFT_UPDATED | ORDER_CHANGED | REVIEW_REQUESTED; khong settlement event',
  `actor_id` bigint COMMENT 'Nullable cho worker; event phai co actor hoac system source',
  `source` varchar(32) NOT NULL,
  `payload` json NOT NULL COMMENT 'Before/after va reason, version; khong luu token',
  `created_at` datetime(3) NOT NULL
);

CREATE TABLE `nutrient_value_revisions` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `ingredient_id` bigint NOT NULL,
  `version` int NOT NULL,
  `value_snapshot` json NOT NULL,
  `reason` varchar(500) NOT NULL,
  `changed_by` bigint NOT NULL,
  `changed_at` datetime(3) NOT NULL
);

CREATE TABLE `nutrition_calculations` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `kind` varchar(8) NOT NULL,
  `recipe_id` bigint,
  `menu_id` bigint,
  `menu_version` int,
  `service_date` date NOT NULL,
  `scope_snapshot` json NOT NULL,
  `inputs_snapshot` json NOT NULL,
  `totals` json NOT NULL,
  `client_revision` int NOT NULL,
  `created_by` bigint NOT NULL,
  `request_route` varchar(80) NOT NULL,
  `request_key` varchar(128) NOT NULL,
  `request_hash` varchar(64) NOT NULL,
  `created_at` datetime(3) NOT NULL
);

CREATE TABLE `agent_run_contexts` (
  `run_id` bigint PRIMARY KEY,
  `parent_run_id` bigint,
  `actor_id` bigint NOT NULL,
  `request_route` varchar(80) NOT NULL,
  `request_key` varchar(128) NOT NULL,
  `request_hash` varchar(64) NOT NULL,
  `scope_snapshot` json NOT NULL,
  `input_snapshot` json NOT NULL,
  `base_menu_id` bigint,
  `base_version` int,
  `candidate_revision` int,
  `candidate_hash` varchar(64),
  `candidate_snapshot` json,
  `evidence_snapshot` json,
  `outcome` varchar(24),
  `questions` json,
  `deadline_at` datetime(3) NOT NULL,
  `model_code` varchar(120),
  `prompt_version` varchar(40),
  `usage_status` varchar(16) NOT NULL DEFAULT 'UNKNOWN',
  `applied_menu_id` bigint,
  `applied_menu_version` int,
  `application_key` varchar(128),
  `application_hash` varchar(64),
  `applied_at` datetime(3)
);

CREATE TABLE `agent_tool_events` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `run_id` bigint NOT NULL,
  `seq` int NOT NULL,
  `tool_name` varchar(80) NOT NULL,
  `status` varchar(24) NOT NULL,
  `request_id` varchar(64) NOT NULL,
  `argument_hash` varchar(64),
  `result_hash` varchar(64),
  `safe_summary` json NOT NULL,
  `started_at` datetime(3) NOT NULL,
  `finished_at` datetime(3)
);

CREATE INDEX `users_index_0` ON `users` (`customer_id`);

CREATE INDEX `users_index_1` ON `users` (`user_type`, `status`);

CREATE UNIQUE INDEX `user_roles_index_2` ON `user_roles` (`user_id`, `role_code`, `kitchen_id`);

CREATE INDEX `sessions_index_3` ON `sessions` (`user_id`, `revoked_at`);

CREATE INDEX `login_logs_index_4` ON `login_logs` (`user_id`, `occurred_at`);

CREATE INDEX `login_logs_index_5` ON `login_logs` (`occurred_at`);

CREATE INDEX `delegations_index_6` ON `delegations` (`to_user_id`, `valid_from`, `valid_to`);

CREATE INDEX `audit_logs_index_7` ON `audit_logs` (`entity`, `entity_id`, `occurred_at`);

CREATE INDEX `audit_logs_index_8` ON `audit_logs` (`actor_user_id`, `occurred_at`);

CREATE INDEX `audit_logs_index_9` ON `audit_logs` (`occurred_at`);

CREATE UNIQUE INDEX `parameters_index_10` ON `parameters` (`code`, `scope_type`, `scope_id`, `effective_from`);

CREATE INDEX `notifications_index_11` ON `notifications` (`user_id`, `status`, `created_at`);

CREATE INDEX `files_index_12` ON `files` (`entity`, `entity_id`);

CREATE INDEX `agent_runs_index_13` ON `agent_runs` (`agent_code`, `created_at`);

CREATE INDEX `agent_runs_index_14` ON `agent_runs` (`user_id`, `created_at`);

CREATE INDEX `change_requests_index_15` ON `change_requests` (`entity`, `entity_key`, `status`);

CREATE INDEX `change_requests_index_16` ON `change_requests` (`status`, `requested_at`);

CREATE UNIQUE INDEX `approvals_index_17` ON `approvals` (`entity`, `entity_id`, `round_no`, `approver_user_id`);

CREATE INDEX `approvals_index_18` ON `approvals` (`approver_user_id`, `decided_at`);

CREATE INDEX `ingredients_index_19` ON `ingredients` (`group_id`);

CREATE INDEX `dishes_index_20` ON `dishes` (`role`, `status`);

CREATE INDEX `dishes_index_21` ON `dishes` (`main_group_id`);

CREATE INDEX `dishes_index_22` ON `dishes` (`base_dish_id`);

CREATE UNIQUE INDEX `dish_conflicts_index_23` ON `dish_conflicts` (`dish_a_id`, `dish_b_id`);

CREATE UNIQUE INDEX `recipes_index_24` ON `recipes` (`dish_id`, `portion_code`, `version_no`);

CREATE INDEX `recipes_index_25` ON `recipes` (`dish_id`, `portion_code`, `status`, `effective_from`);

CREATE UNIQUE INDEX `recipe_items_index_26` ON `recipe_items` (`recipe_id`, `ingredient_id`);

CREATE UNIQUE INDEX `dish_prices_index_27` ON `dish_prices` (`dish_id`, `portion_code`, `effective_from`);

CREATE INDEX `menus_index_28` ON `menus` (`meal_type_id`, `customer_id`, `week_start`);

CREATE INDEX `menus_index_29` ON `menus` (`status`, `week_start`);

CREATE UNIQUE INDEX `menu_days_index_30` ON `menu_days` (`menu_id`, `service_date`);

CREATE INDEX `menu_days_index_31` ON `menu_days` (`service_date`);

CREATE UNIQUE INDEX `menu_day_items_index_32` ON `menu_day_items` (`menu_day_id`, `dish_id`);

CREATE INDEX `menu_day_items_index_33` ON `menu_day_items` (`dish_id`);

CREATE INDEX `menu_rule_results_index_34` ON `menu_rule_results` (`menu_id`, `rule_code`, `menu_day_id`);

CREATE INDEX `ingredient_prices_index_35` ON `ingredient_prices` (`ingredient_id`, `kitchen_id`, `effective_from`);

CREATE UNIQUE INDEX `ingredient_prices_index_36` ON `ingredient_prices` (`ingredient_id`, `supplier_id`, `kitchen_id`, `effective_from`);

CREATE UNIQUE INDEX `cost_estimates_index_37` ON `cost_estimates` (`menu_day_id`, `kitchen_id`, `version_no`);

CREATE INDEX `cost_estimates_index_38` ON `cost_estimates` (`batch_key`);

CREATE UNIQUE INDEX `cost_estimate_lines_index_39` ON `cost_estimate_lines` (`estimate_id`, `ingredient_id`);

CREATE INDEX `cost_sheets_index_40` ON `cost_sheets` (`dish_id`, `kitchen_id`, `calculation_date`, `status`);

CREATE UNIQUE INDEX `cost_sheet_lines_index_41` ON `cost_sheet_lines` (`sheet_id`, `ingredient_id`);

CREATE INDEX `cost_allowances_index_42` ON `cost_allowances` (`name`, `meal_type_id`, `effective_from`);

CREATE UNIQUE INDEX `menu_cost_snapshots_index_43` ON `menu_cost_snapshots` (`menu_day_id`, `kitchen_id`, `approval_round_no`);

CREATE UNIQUE INDEX `menu_cost_snapshot_lines_index_44` ON `menu_cost_snapshot_lines` (`snapshot_id`, `dish_id`, `ingredient_id`);

CREATE UNIQUE INDEX `cost_recalculations_index_45` ON `cost_recalculations` (`snapshot_id`, `event_key`);

CREATE INDEX `cost_alerts_index_46` ON `cost_alerts` (`menu_day_id`, `status`);

CREATE UNIQUE INDEX `cost_alert_kitchens_index_47` ON `cost_alert_kitchens` (`alert_id`, `kitchen_id`);

CREATE UNIQUE INDEX `cost_estimate_servings_index_48` ON `cost_estimate_servings` (`estimate_id`, `dish_id`);

CREATE UNIQUE INDEX `cost_estimate_components_index_49` ON `cost_estimate_components` (`estimate_line_id`, `dish_id`);

CREATE UNIQUE INDEX `cost_estimate_allowances_index_50` ON `cost_estimate_allowances` (`estimate_id`, `allowance_id`);

CREATE INDEX `service_points_index_51` ON `service_points` (`customer_id`);

CREATE INDEX `service_points_index_52` ON `service_points` (`kitchen_id`);

CREATE UNIQUE INDEX `service_schedules_index_53` ON `service_schedules` (`service_point_id`, `shift`, `weekday`);

CREATE UNIQUE INDEX `customer_quotas_index_54` ON `customer_quotas` (`customer_id`, `effective_from`);

CREATE INDEX `eaters_index_55` ON `eaters` (`customer_id`, `status`);

CREATE UNIQUE INDEX `meal_selections_index_56` ON `meal_selections` (`eater_id`, `service_date`, `shift`);

CREATE INDEX `meal_selections_index_57` ON `meal_selections` (`service_point_id`, `service_date`, `shift`, `dish_id`);

CREATE UNIQUE INDEX `orders_index_58` ON `orders` (`service_point_id`, `service_date`, `shift`);

CREATE INDEX `orders_index_59` ON `orders` (`service_date`, `status`);

CREATE UNIQUE INDEX `order_dish_lines_index_60` ON `order_dish_lines` (`order_id`, `dish_id`);

CREATE INDEX `customer_price_terms_index_61` ON `customer_price_terms` (`customer_id`, `meal_type_id`, `effective_from`);

CREATE UNIQUE INDEX `order_pricing_snapshots_index_62` ON `order_pricing_snapshots` (`order_id`, `order_version`);

CREATE UNIQUE INDEX `order_discount_records_index_63` ON `order_discount_records` (`order_id`, `proposal_key`);

CREATE INDEX `order_discount_records_index_64` ON `order_discount_records` (`order_id`, `status`);

CREATE UNIQUE INDEX `order_discount_events_index_65` ON `order_discount_events` (`discount_id`, `event_key`);

CREATE UNIQUE INDEX `nutrient_value_revisions_index_66` ON `nutrient_value_revisions` (`ingredient_id`, `version`);

CREATE UNIQUE INDEX `nutrition_calculations_index_67` ON `nutrition_calculations` (`created_by`, `request_route`, `request_key`);

CREATE INDEX `nutrition_calculations_index_68` ON `nutrition_calculations` (`menu_id`, `created_at`);

CREATE UNIQUE INDEX `agent_run_contexts_index_69` ON `agent_run_contexts` (`actor_id`, `request_route`, `request_key`);

CREATE UNIQUE INDEX `agent_tool_events_index_70` ON `agent_tool_events` (`run_id`, `seq`);

ALTER TABLE `kitchens` COMMENT = 'Cơ sở (bếp): Hoàng Đạo Thành, Phúc Diễn';

ALTER TABLE `users` COMMENT = 'Tài khoản — 4 loại định danh (SRS nền tảng mục 2.3)';

ALTER TABLE `login_logs` COMMENT = 'Thời gian lưu: điểm mở N-03 (đề xuất 1 năm)';

ALTER TABLE `delegations` COMMENT = 'Uỷ quyền duyệt khi vắng (FR-AUTH-RBAC-003). Phụ thuộc điểm mở O-06';

ALTER TABLE `audit_logs` COMMENT = 'Bất biến (BR-AUD-002): tài khoản ứng dụng chỉ có INSERT, SELECT. Phân vùng theo tháng. Thời gian lưu: điểm mở N-03';

ALTER TABLE `agent_runs` COMMENT = 'Nhật ký lượt chạy agent (FEAT-023)';

ALTER TABLE `change_requests` COMMENT = 'Giá trị đề nghị cho bản ghi đang hiệu lực, chờ duyệt (FR-MENU-DISH-002, FR-MENU-RUL-006). Tối đa 1 đề nghị PENDING mỗi bản ghi — kiểm ở tầng ứng dụng';

ALTER TABLE `approvals` COMMENT = 'Mỗi dòng là một quyết định của một người duyệt; cho phép nhiều người duyệt (BR-MNU-008). Cột approved_by trên các bảng nghiệp vụ = người duyệt cuối, ghi cùng giao dịch';

ALTER TABLE `ingredient_seasons` COMMENT = 'Mùa vụ của rau (BR-MENU-018)';

ALTER TABLE `dish_conflicts` COMMENT = 'Cặp món kỵ nhau, ví dụ nem - nộm (BR-MENU-034). Danh sách: điểm mở H-4';

ALTER TABLE `recipes` COMMENT = 'Công thức ACTIVE không sửa; thay đổi tạo phiên bản mới';

ALTER TABLE `meal_types` COMMENT = 'Loại suất do dinh dưỡng viên tự tạo (D-20)';

ALTER TABLE `menus` COMMENT = 'Duy nhất theo (meal_type_id, customer_id, week_start) trong các bản không huỷ — kiểm ở tầng ứng dụng';

ALTER TABLE `ingredient_prices` COMMENT = 'Giá nhập do nội bộ nhập (D-13). Không sửa đè: giá mới là dòng mới';

ALTER TABLE `cost_estimates` COMMENT = 'BR-EST-004: bất biến sau khi lưu; snapshot và các dòng con ghi trong cùng giao dịch.';

ALTER TABLE `cost_estimate_lines` COMMENT = 'FR-COST-EST-004: một dòng nguyên liệu/ngày/cơ sở; định lượng mỗi suất và số suất nằm ở cost_estimate_components. Nguyên liệu ngoài cost vẫn có lượng mua, amount_vnd = 0.';

ALTER TABLE `cost_sheets` COMMENT = 'FR-COST-DISH-006/007: nội dung chụp bất biến từ khi gửi; quyết định duyệt dùng approvals.entity = cost_sheets. Bị trả lại thì lập bản mới.';

ALTER TABLE `cost_sheet_lines` COMMENT = 'Bảng phân rã bất biến, BR-CALC-007. Công thức phải khớp cost_sheets.recipe_id; nguyên liệu ngoài cost có giá null, line_cost_vnd = 0.';

ALTER TABLE `cost_allowances` COMMENT = 'FR-COST-MEAL-004: mỗi thay đổi tạo bản đề nghị mới; duyệt qua approvals.entity = cost_allowances. Khoản riêng loại suất ưu tiên khoản chung cùng tên (BR-CALC-008).';

ALTER TABLE `menu_cost_snapshots` COMMENT = 'FR-COST-MEAL-006: INSERT cùng giao dịch chuyển menus sang APPROVED ở người duyệt cuối. Không UPDATE/DELETE nội dung, không ghi đè qua vòng duyệt.';

ALTER TABLE `menu_cost_snapshot_lines` COMMENT = 'Lưu cả món chính không được chọn bởi DAT_NHAT để giải thích đầy đủ. Tổng cost dòng không phải cost suất; áp cách gộp món chính từ inputs_snapshot.';

ALTER TABLE `cost_recalculations` COMMENT = 'FR-COST-ALR-001: kết quả mới lưu riêng bất biến; inputs_snapshot gồm dòng giá/công thức đã dùng, không cập nhật bản duyệt.';

ALTER TABLE `cost_alerts` COMMENT = 'FR-COST-ALR-002/003: một cảnh báo đầu mục/ngày; chi tiết nhiều cơ sở. Thông báo dùng notifications.entity = cost_alerts, entity_id = id.';

ALTER TABLE `cost_alert_kitchens` COMMENT = 'Hai cơ sở cùng vượt chỉ tạo một cảnh báo ngày với hai dòng; lấy cost cũ/mới từ FK, không chép số có thể lệch nhau.';

ALTER TABLE `cost_estimate_servings` COMMENT = 'Lưu số suất từng món chính, BR-EST-001. Tổng lượt chọn / main_pick = số suất ngày; dữ liệu sau lưu bất biến.';

ALTER TABLE `cost_estimate_components` COMMENT = 'Phân rã dòng nguyên liệu về từng món và phiên bản công thức; không làm tròn mua từng món.';

ALTER TABLE `cost_estimate_allowances` COMMENT = 'Khoản khoán tách khỏi dòng nguyên liệu; không tính trùng khoản chung và riêng cùng tên.';

ALTER TABLE `eater_health_profiles` COMMENT = 'Chỉ chính người ăn đọc được. Xoá cứng khi người ăn yêu cầu (NFR-PRIV-001) — ngoại lệ duy nhất của quy tắc không xoá cứng';

ALTER TABLE `customer_quotas` COMMENT = 'Định mức suất chung của công ty (D-21)';

ALTER TABLE `customer_qr_codes` COMMENT = 'Mã QR công ty dùng để xác minh người ăn (D-19)';

ALTER TABLE `eaters` COMMENT = 'Cách định danh người ăn qua QR: chốt ở SRS R6';

ALTER TABLE `meal_selections` COMMENT = 'Bảng chịu tải cao nhất. Phân vùng theo tháng của service_date';

ALTER TABLE `selection_counters` COMMENT = 'Bộ đếm theo món, cập nhật cùng giao dịch với meal_selections';

ALTER TABLE `orders` COMMENT = 'Một dòng mỗi điểm - ngày - ca; đặt, giao, nhận, tính tiền theo SUẤT';

ALTER TABLE `order_dish_lines` COMMENT = 'Phân rã theo MÓN cho kế hoạch sản xuất. Tổng 3 cột của mọi dòng = orders.total_servings';

ALTER TABLE `users` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `user_roles` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `user_roles` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `sessions` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `login_logs` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `delegations` ADD FOREIGN KEY (`from_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `delegations` ADD FOREIGN KEY (`to_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `audit_logs` ADD FOREIGN KEY (`actor_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `audit_logs` ADD FOREIGN KEY (`on_behalf_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `parameters` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `notifications` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `agent_runs` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `change_requests` ADD FOREIGN KEY (`requested_by`) REFERENCES `users` (`id`);

ALTER TABLE `approvals` ADD FOREIGN KEY (`approver_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `approvals` ADD FOREIGN KEY (`delegation_id`) REFERENCES `delegations` (`id`);

ALTER TABLE `ingredients` ADD FOREIGN KEY (`group_id`) REFERENCES `ingredient_groups` (`id`);

ALTER TABLE `ingredient_seasons` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `dishes` ADD FOREIGN KEY (`main_group_id`) REFERENCES `ingredient_groups` (`id`);

ALTER TABLE `dishes` ADD FOREIGN KEY (`cooking_method_id`) REFERENCES `cooking_methods` (`id`);

ALTER TABLE `dishes` ADD FOREIGN KEY (`base_dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `dishes` ADD FOREIGN KEY (`image_file_id`) REFERENCES `files` (`id`);

ALTER TABLE `dishes` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `dish_allergens` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `dish_allergens` ADD FOREIGN KEY (`allergen_id`) REFERENCES `allergens` (`id`);

ALTER TABLE `dish_conflicts` ADD FOREIGN KEY (`dish_a_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `dish_conflicts` ADD FOREIGN KEY (`dish_b_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `recipes` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `recipes` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `recipe_items` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `recipe_items` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `dish_prices` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `dish_prices` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `menus` ADD FOREIGN KEY (`meal_type_id`) REFERENCES `meal_types` (`id`);

ALTER TABLE `menus` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `menus` ADD FOREIGN KEY (`agent_run_id`) REFERENCES `agent_runs` (`id`);

ALTER TABLE `menus` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `menu_days` ADD FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`);

ALTER TABLE `menu_days` ADD FOREIGN KEY (`default_dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `menu_day_items` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `menu_day_items` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `menu_day_items` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `menu_rule_results` ADD FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`);

ALTER TABLE `menu_rule_results` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `menu_rule_results` ADD FOREIGN KEY (`rule_code`) REFERENCES `menu_rules` (`code`);

ALTER TABLE `ingredient_prices` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `ingredient_prices` ADD FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

ALTER TABLE `ingredient_prices` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `ingredient_prices` ADD FOREIGN KEY (`pricing_verified_by`) REFERENCES `users` (`id`);

ALTER TABLE `ingredient_prices` ADD FOREIGN KEY (`source_file_id`) REFERENCES `files` (`id`);

ALTER TABLE `cost_estimates` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `cost_estimates` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `cost_estimates` ADD FOREIGN KEY (`computed_by`) REFERENCES `users` (`id`);

ALTER TABLE `cost_estimate_lines` ADD FOREIGN KEY (`estimate_id`) REFERENCES `cost_estimates` (`id`);

ALTER TABLE `cost_estimate_lines` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `cost_estimate_lines` ADD FOREIGN KEY (`ingredient_price_id`) REFERENCES `ingredient_prices` (`id`);

ALTER TABLE `cost_estimate_lines` ADD FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

ALTER TABLE `cost_sheets` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `cost_sheets` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `cost_sheets` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `cost_sheets` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `cost_sheets` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `cost_sheet_lines` ADD FOREIGN KEY (`sheet_id`) REFERENCES `cost_sheets` (`id`);

ALTER TABLE `cost_sheet_lines` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `cost_sheet_lines` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `cost_sheet_lines` ADD FOREIGN KEY (`ingredient_price_id`) REFERENCES `ingredient_prices` (`id`);

ALTER TABLE `cost_sheet_lines` ADD FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

ALTER TABLE `cost_allowances` ADD FOREIGN KEY (`meal_type_id`) REFERENCES `meal_types` (`id`);

ALTER TABLE `cost_allowances` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `cost_allowances` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `menu_cost_snapshots` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `menu_cost_snapshots` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `menu_cost_snapshots` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`snapshot_id`) REFERENCES `menu_cost_snapshots` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`ingredient_price_id`) REFERENCES `ingredient_prices` (`id`);

ALTER TABLE `menu_cost_snapshot_lines` ADD FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`);

ALTER TABLE `cost_recalculations` ADD FOREIGN KEY (`snapshot_id`) REFERENCES `menu_cost_snapshots` (`id`);

ALTER TABLE `cost_alerts` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `cost_alerts` ADD FOREIGN KEY (`closed_by`) REFERENCES `users` (`id`);

ALTER TABLE `cost_alert_kitchens` ADD FOREIGN KEY (`alert_id`) REFERENCES `cost_alerts` (`id`);

ALTER TABLE `cost_alert_kitchens` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `cost_alert_kitchens` ADD FOREIGN KEY (`snapshot_id`) REFERENCES `menu_cost_snapshots` (`id`);

ALTER TABLE `cost_alert_kitchens` ADD FOREIGN KEY (`latest_recalculation_id`) REFERENCES `cost_recalculations` (`id`);

ALTER TABLE `cost_estimate_servings` ADD FOREIGN KEY (`estimate_id`) REFERENCES `cost_estimates` (`id`);

ALTER TABLE `cost_estimate_servings` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `cost_estimate_components` ADD FOREIGN KEY (`estimate_line_id`) REFERENCES `cost_estimate_lines` (`id`);

ALTER TABLE `cost_estimate_components` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `cost_estimate_components` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `cost_estimate_allowances` ADD FOREIGN KEY (`estimate_id`) REFERENCES `cost_estimates` (`id`);

ALTER TABLE `cost_estimate_allowances` ADD FOREIGN KEY (`allowance_id`) REFERENCES `cost_allowances` (`id`);

ALTER TABLE `nutrient_values` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `eater_health_profiles` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `service_points` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `service_points` ADD FOREIGN KEY (`kitchen_id`) REFERENCES `kitchens` (`id`);

ALTER TABLE `service_schedules` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `customer_quotas` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `customer_quotas` ADD FOREIGN KEY (`meal_type_id`) REFERENCES `meal_types` (`id`);

ALTER TABLE `customer_quotas` ADD FOREIGN KEY (`approved_by`) REFERENCES `users` (`id`);

ALTER TABLE `customer_qr_codes` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `customer_qr_codes` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `eaters` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `eaters` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `eaters` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `meal_selections` ADD FOREIGN KEY (`eater_id`) REFERENCES `eaters` (`id`);

ALTER TABLE `meal_selections` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `meal_selections` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `meal_selections` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `selection_counters` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `selection_counters` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `selection_counters` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`service_point_id`) REFERENCES `service_points` (`id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`meal_type_id`) REFERENCES `meal_types` (`id`);

ALTER TABLE `orders` ADD FOREIGN KEY (`menu_day_id`) REFERENCES `menu_days` (`id`);

ALTER TABLE `order_dish_lines` ADD FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

ALTER TABLE `order_dish_lines` ADD FOREIGN KEY (`dish_id`) REFERENCES `dishes` (`id`);

ALTER TABLE `customer_price_terms` ADD FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

ALTER TABLE `customer_price_terms` ADD FOREIGN KEY (`meal_type_id`) REFERENCES `meal_types` (`id`);

ALTER TABLE `customer_price_terms` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `customer_price_terms` ADD FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

ALTER TABLE `order_pricing_snapshots` ADD FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

ALTER TABLE `order_pricing_snapshots` ADD FOREIGN KEY (`price_term_id`) REFERENCES `customer_price_terms` (`id`);

ALTER TABLE `order_pricing_snapshots` ADD FOREIGN KEY (`captured_by`) REFERENCES `users` (`id`);

ALTER TABLE `order_discount_records` ADD FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

ALTER TABLE `order_discount_records` ADD FOREIGN KEY (`pricing_snapshot_id`) REFERENCES `order_pricing_snapshots` (`id`);

ALTER TABLE `order_discount_records` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `order_discount_records` ADD FOREIGN KEY (`updated_by`) REFERENCES `users` (`id`);

ALTER TABLE `order_discount_events` ADD FOREIGN KEY (`discount_id`) REFERENCES `order_discount_records` (`id`);

ALTER TABLE `order_discount_events` ADD FOREIGN KEY (`actor_id`) REFERENCES `users` (`id`);

ALTER TABLE `nutrient_value_revisions` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `ingredients` (`id`);

ALTER TABLE `nutrient_value_revisions` ADD FOREIGN KEY (`changed_by`) REFERENCES `users` (`id`);

ALTER TABLE `nutrition_calculations` ADD FOREIGN KEY (`recipe_id`) REFERENCES `recipes` (`id`);

ALTER TABLE `nutrition_calculations` ADD FOREIGN KEY (`menu_id`) REFERENCES `menus` (`id`);

ALTER TABLE `nutrition_calculations` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `agent_run_contexts` ADD FOREIGN KEY (`run_id`) REFERENCES `agent_runs` (`id`);

ALTER TABLE `agent_run_contexts` ADD FOREIGN KEY (`parent_run_id`) REFERENCES `agent_runs` (`id`);

ALTER TABLE `agent_run_contexts` ADD FOREIGN KEY (`actor_id`) REFERENCES `users` (`id`);

ALTER TABLE `agent_run_contexts` ADD FOREIGN KEY (`base_menu_id`) REFERENCES `menus` (`id`);

ALTER TABLE `agent_run_contexts` ADD FOREIGN KEY (`applied_menu_id`) REFERENCES `menus` (`id`);

ALTER TABLE `agent_tool_events` ADD FOREIGN KEY (`run_id`) REFERENCES `agent_runs` (`id`);
