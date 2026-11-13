# Backlog MVP (NUTR)

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Tất cả P0 theo feature MVP. Story point để **chưa ước lượng** vì O-04/đội chưa chốt; không giả số đã cam kết. INVEST: giá trị và AC cụ thể; còn phụ thuộc được nêu, chưa coi Sprint-ready khi câu hỏi liên quan mở.

| Story | Nội dung | FR / Feature | Phụ thuộc | UC / UI / API / Bảng |
| :--- | :--- | :--- | :--- | :--- |
| US-NUTR-001 | Là một DINH_DUONG_VIEN, tôi muốn quản lý bảng thành phần để tra được nguồn và sửa số liệu có lịch sử. | FR-NUTR-REF-001; FEAT-019 | R2, DL-07 | [UC-NUTR-001](../usecases/UC-NUTR-001.md); UI-NUTR-01; API-NUTR-001; nutrient_values, nutrient_value_revisions |
| US-NUTR-002 | Là một DINH_DUONG_VIEN, tôi muốn kiểm độ phủ nguyên liệu để biết dữ liệu còn thiếu trước khi tính dinh dưỡng. | FR-NUTR-REF-002; FEAT-019 | R2, DL-07 | [UC-NUTR-002](../usecases/UC-NUTR-002.md); UI-NUTR-01; API-NUTR-002; recipes, recipe_items, nutrient_values |
| US-NUTR-003 | Là một DINH_DUONG_VIEN, tôi muốn tính dinh dưỡng món để xem bốn chỉ số và cách tính từ công thức sống. | FR-NUTR-CALC-001; FEAT-020 | R2, DL-07 | [UC-NUTR-003](../usecases/UC-NUTR-003.md); UI-NUTR-02; API-NUTR-003; recipes, recipe_items, nutrient_values, nutrition_calculations |
| US-NUTR-004 | Là một DINH_DUONG_VIEN, tôi muốn tính dinh dưỡng tổ hợp suất để biết dinh dưỡng của đúng tổ hợp món đã chọn. | FR-NUTR-CALC-002; FEAT-020 | R2, DL-07 | [UC-NUTR-004](../usecases/UC-NUTR-004.md); UI-NUTR-03; API-NUTR-004; menus, menu_days, menu_day_items, nutrition_calculations |
| US-NUTR-005 | Là một DINH_DUONG_VIEN, tôi muốn xem kết quả và nguồn lịch sử để giải thích được số đã xem khi nguồn thay đổi. | FR-NUTR-SNAP-001; FEAT-020 | R2, DL-07 | [UC-NUTR-005](../usecases/UC-NUTR-005.md); UI-NUTR-02; API-NUTR-005; nutrition_calculations, nutrient_value_revisions |
