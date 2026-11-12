---
id: DOC-E8-REVIEW-DEPENDENCIES-MD
title: Phụ thuộc dữ liệu và cổng E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Phụ thuộc dữ liệu và cổng E8

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Tất cả tài liệu producer dưới là **nháp/chưa duyệt**, không contract freeze; trạng thái bản ghi minh họa không chứng minh nguồn thật đã sẵn sàng.

| Dữ liệu / consumer | Nguồn cụ thể | Trạng thái nguồn / yêu cầu dự kiến | Điểm mở / nhánh BLOCKED |
| :--- | :--- | :--- | :--- |
| Món, định lượng FEAT-056/057 | [E2 SRS](../../thuc-don-dinh-luong/srs/spec.md), recipes/recipe_items/dishes | Nháp; ACTIVE và hiệu lực theo ngày trong thiết kế, chưa có chứng cứ dữ liệu | E8-Q04/05, O-02, DL-01/03/04/05 |
| Tuần mẫu | E2 FR-MENU-APV-003, menus/menu_day_items | Nháp; dịch vụ tra PUBLISHED; quyền công khai riêng chưa rõ | E8-Q04; không công khai menu theo khách |
| Kiểm quy tắc FEAT-057 | E2 FR-MENU-RUL-002 không lưu, menu_rules/results | Nháp; DL-01 chưa duyệt, không coi43 quy tắc đã freeze; cách gọi E8 chưa chọn | E8-Q05, DL-01 |
| Giá suất FEAT-056 | E2 meal_types/dish_prices; [E3 kế toán](../../cost/accounting/business-rules.md) | Nháp; ngưỡng/giá món khác giá suất public; nguyên tắc VAT/CK đã xác nhận nhưng giá thật chưa có | E8-Q03, O-02; CK/DATA-COST giữ nguyên |
| Gate cost nội bộ khi mẫu cần kiểm | [E3 SRS](../../cost/srs/spec.md), cổng MENU | Nháp, CHAN/CANH_BAO và missing input giữ nguyên; chỉ đọc kết luận an toàn nếu được phép, không số cost | E8-Q04/05; không tự đổi NFR-COST-002 |
| 4 chỉ số / nguồn | [E4 SRS](../../dinh-duong/srs/spec.md), [API](../../dinh-duong/api/api-spec.md), nutrition_calculations | Nháp, calculation bất biến có isStale; không có trạng thái duyệt; R4 chưa nghiệm thu | E8-Q04; NUTR-Q01–04/DATA-NUTR-Q01 |
| Dị ứng | E2 dish_allergens/allergens; E4 không thay nguồn dị ứng | Nháp; chưa có chứng cứ đủ/đã rà dị ứng | E8-Q04; không suy [] là không dị ứng |
| Auth/audit/files | [E1 SRS](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md) | Nháp; role PUB, audit anonymous, public asset cần review | E8-Q08/09/12 |
| Bài/URL cũ | DL-08 roadmap | Chưa được cung cấp; không có danh sách/URL thật | E8-Q01/02 |
| Hạ tầng/quyền tên miền | O-04, R8 | Chưa có evidence quyền/quyết định cutover | E8-Q11 |
| Lead → CRM | PORT-PUB-LEAD-HANDOFF, [API E8](../api/api-spec.md) | E10 chưa mở; contract chưa có, nơi lưu tạm chưa chọn | E8-Q06/07/12; không đặc tả CRM |
| BO-09 | G-Next, baseline organic | Chưa công cụ/mốc số liệu | E8-Q10 |

R7/R8 độc lập; không lấy E6/E7 làm dependency cứng mới. E6 CG01/08/05/06 và E7 Q-13/E7-Q01–08 giữ CHỜ TRẢ LỜI ở sổ gốc;14/14 CG OPEN. E9–E13 chưa mở. [Câu hỏi E8](questions.md) là sổ quyết định duy nhất E8.
