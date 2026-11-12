# Bảng phụ thuộc E9

Draft · 12/11/2026 · Tất cả SRS/API producer dưới đây là **nháp/chưa duyệt**, không contract freeze. Trạng thái thiết kế của bản ghi không chứng minh dữ liệu thật sẵn sàng.

| E9 lấy gì | Nguồn cụ thể | Trạng thái nguồn | Câu hỏi / nhánh BLOCKED |
| :--- | :--- | :--- | :--- |
| Danh mục/công thức/định lượng, ngày phục vụ | [E2 SRS](../../thuc-don-dinh-luong/srs/spec.md), dishes/recipes/recipe_items/meal_types | Nháp; ACTIVE/hiệu lực là yêu cầu, DL-03–05 chưa evidence | O-02, E2-Q3; E9-Q03/12 |
| Máy quy tắc cứng sau mọi lần chỉnh | E2 FR-MENU-RUL-002 kiểm chưa lưu; FR-MENU-RUL-003 | Nháp; DL-01 chưa duyệt, không tự đóng43 quy tắc | E9-Q11/12/13, DL-01; không nới quy tắc |
| 4 chỉ số có nguồn, nhãn ước tính | [E4 SRS](../../dinh-duong/srs/spec.md), [API](../../dinh-duong/api/api-spec.md), nutrition_calculations | Nháp; nguồn/dung sai/cách tính chưa chốt, R4 chưa nghiệm thu | NUTR-Q01–04/DATA-NUTR-Q01; E9-Q12; adapter candidate chưa lưu |
| Mẫu orchestration/kiểm/apply và log | [E5 SRS](../../agent-noi-bo/srs/spec.md), [API](../../agent-noi-bo/api/api-spec.md), [câu hỏi](../../agent-noi-bo/review/questions.md) | Nháp; R5 chưa xong; AIO là tiền thân, không contract reuse | AIO-Q01–06 đều còn mở; E9-Q01/03/05/09/10/11/13; không dùng applyDraft/quyền cost của AIO |
| Xác minh người dùng/quyền khách | [E6 SRS](../../chon-mon-order/srs/spec.md), [sổ CG](../../chon-mon-order/review/contract-gap-register.md) | Nháp; R6 chưa xong;14/14 CG OPEN | CG01/08/05/06 chờ; E9-Q02 tham chiếu không hỏi lại/sửa producer |
| Gợi ý FEAT-047 | E6 FR-NUTR-PROF-001/REC-001; FEAT-046/047 | Gate-only O-03; không contract hồ sơ/gợi ý | FEAT-063 chỉ gate; E9-Q14; không đọc eater_health_profiles |
| Website entry, trial và nguồn public | [E8 SRS](../../website-cong-khai/srs/spec.md), [câu hỏi](../../website-cong-khai/review/questions.md) | Nháp; R8 chưa xong; FEAT-057 engine chưa chọn | E8-Q03/04/05/06/12; E9-Q02/04/06/11/12/13; không sửa E8 |
| Auth/service/audit/tham số/schema | [E1 SRS](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml) | Nháp65 bảng; BR-SEC-009/010 và quyền DB là ràng buộc nền | E9-Q02/07/08/10/13; guest audit và group scope còn delta |
| Cổng kinh tế nội bộ và nguyên tắc VAT/CK | [E3 business rules](../../cost/accounting/business-rules.md), [SRS](../../cost/srs/spec.md) | Nguyên tắc kế toán đã xác nhận; thiết kế/đầu vào chưa freeze | E9-Q05/AIO-Q02; không tự đổi CHAN/CANH_BAO, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 |
| Điểm nhận đề xuất | E8-Q06 và PORT-AIN-HANDOFF | Chưa chọn nơi lưu/nhận; CRM E10 chưa mở | E9-Q06; chỉ port tối thiểu, không đặc tả CRM |
| Điều kiện release và nghiệm thu | [Roadmap R9/G-Next](../../gia-phat/02-roadmap.md) | R5/R6/R8 chưa evidence xong; nghiệm thu chưa chạy | O-04; E9-Q09/13; không đánh dấu release/gate đạt |

E6 CG01/08/05/06, E7 Q-13/E7-Q01–08 và E8-Q01–12 tiếp tục CHỜ TRẢ LỜI; không hỏi lại, tự điền hoặc đặc tả thêm phần phụ thuộc. E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04 và AIO-Q01–06 không đóng. E10–E13 chưa mở.
