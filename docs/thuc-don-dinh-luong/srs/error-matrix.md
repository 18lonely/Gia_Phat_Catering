---
id: DOC-THUC-DON-SRS-ERROR-MATRIX
title: Ma trận lỗi E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e2]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E2: Thực đơn và định lượng

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 33 dòng mã lỗi từ [SRS E2](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E2](spec.md).

| Mã ERR | HTTP | Điều kiện phát sinh | Khoá bản địa hoá | Thông báo hiển thị | Mức | Hành động tiếp theo |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `ERR-MENU-404-01` | 404 | Món không có công thức hiệu lực tại ngày phục vụ | `menu.recipe_not_effective` | "Món {tên} chưa có công thức hiệu lực cho ngày {ngày}." | High | Tạo hoặc duyệt công thức |
| `ERR-MENU-404-02` | 404 | Món không có giá bán hiệu lực tại ngày phục vụ | `menu.price_not_effective` | "Món {tên} chưa có giá bán hiệu lực cho ngày {ngày}." | High | Đặt và duyệt giá bán |
| `ERR-MENU-409-01` | 409 | Trùng tên (`BR-CAT-001`) hoặc trùng cặp kỵ | `menu.duplicate_name` | "Tên này đã tồn tại." | Medium | Đổi tên hoặc dùng bản ghi có sẵn |
| `ERR-MENU-409-02` | 409 | Sửa đơn vị/hệ số của nguyên liệu đang trong công thức hiệu lực | `menu.ingredient_unit_locked` | "Không sửa được đơn vị vì nguyên liệu đang dùng trong {n} công thức." | Medium | Tạo nguyên liệu mới |
| `ERR-MENU-409-03` | 409 | Sửa công thức không ở trạng thái nháp | `menu.recipe_immutable` | "Công thức đã gửi duyệt không sửa được. Hãy tạo phiên bản mới." | Medium | Tạo phiên bản mới |
| `ERR-MENU-409-04` | 409 | Đã có giá cho cùng món, cỡ, ngày hiệu lực | `menu.price_exists` | "Đã có giá bán cho ngày hiệu lực này." | Medium | Chọn ngày khác |
| `ERR-MENU-409-05` | 409 | Sửa cơ cấu loại suất đã có thực đơn gửi duyệt | `menu.meal_type_locked` | "Loại suất đã có thực đơn nên không sửa được cơ cấu. Hãy tạo loại suất mới." | Medium | Tạo loại suất mới |
| `ERR-MENU-409-06` | 409 | Đã có thực đơn cho loại suất và tuần này | `menu.menu_exists` | "Tuần này đã có thực đơn cho loại suất đã chọn." | Medium | Mở thực đơn đã có |
| `ERR-MENU-409-07` | 409 | Sửa nội dung thực đơn không ở `DRAFT`/`CHECKED` | `menu.menu_not_editable` | "Thực đơn đang ở trạng thái {trạng thái} nên không sửa được." | Medium | Thu hồi hoặc chờ kết quả duyệt |
| `ERR-MENU-409-08` | 409 | Huỷ thực đơn đã gửi duyệt trở đi | `menu.menu_not_cancellable` | "Chỉ huỷ được thực đơn nháp." | Medium | Thu hồi nếu đã công bố |
| `ERR-MENU-409-09` | 409 | Công bố thực đơn có ngày phục vụ đầu tiên không sau hôm nay | `menu.publish_too_late` | "Thực đơn có ngày phục vụ đã qua hoặc là hôm nay nên không công bố được." | High | Bỏ các ngày đã qua, gửi duyệt lại |
| `ERR-MENU-409-10` | 409 | Sửa hoặc huỷ giá bán `APPROVED` có ngày hiệu lực đã đến (`BR-CAT-016`) | `menu.price_immutable` | "Giá đã hiệu lực không sửa hoặc huỷ được. Hãy đặt giá mới với ngày hiệu lực từ ngày mai." | Medium | Đặt giá mới |
| `ERR-MENU-422-01` | 422 | Hệ số quy đổi ≤ 0 hoặc sai với cặp kg–g | `menu.conversion_invalid` | "Hệ số quy đổi không hợp lệ." | Medium | Sửa hệ số |
| `ERR-MENU-422-02` | 422 | Thiếu tỷ lệ hao hụt cho nguyên liệu có xương/vỏ | `menu.waste_required` | "Nguyên liệu có xương hoặc vỏ cần khai tỷ lệ hao hụt." | Medium | Nhập tỷ lệ |
| `ERR-MENU-422-03` | 422 | Tháng mùa vụ ngoài 1–12 | `menu.season_invalid` | "Tháng phải từ 1 đến 12." | Medium | Sửa tháng |
| `ERR-MENU-422-04` | 422 | Gắn Healthy cho món có phương pháp không ít dầu mỡ | `menu.healthy_method` | "Món Healthy phải dùng phương pháp chế biến ít dầu mỡ." | Medium | Đổi phương pháp hoặc bỏ cờ |
| `ERR-MENU-422-05` | 422 | Món gốc sai (`BR-CAT-007`) | `menu.base_dish_invalid` | "Món gốc phải cùng vai trò và không phải là biến thể của món khác." | Medium | Chọn món gốc khác |
| `ERR-MENU-422-06` | 422 | Gửi duyệt hoặc duyệt món chưa có công thức | `menu.dish_no_recipe` | "Món cần có công thức trước khi duyệt." | High | Tạo công thức |
| `ERR-MENU-422-07` | 422 | Cặp kỵ gồm 2 món giống nhau | `menu.conflict_same_dish` | "Hai món của cặp phải khác nhau." | Medium | Chọn lại |
| `ERR-MENU-422-08` | 422 | Công thức sai cấu trúc (`BR-CAT-010`) | `menu.recipe_structure` | "Công thức cần ít nhất một nguyên liệu chính và không lặp nguyên liệu." | Medium | Sửa các dòng |
| `ERR-MENU-422-09` | 422 | Khoảng định lượng sai (`BR-CAT-011`) | `menu.qty_range` | "Định lượng phải thoả: tối thiểu ≤ chuẩn ≤ tối đa." | Medium | Sửa định lượng |
| `ERR-MENU-422-10` | 422 | Nguyên liệu chính không thuộc nhóm của món (`BR-CAT-012`) | `menu.main_group_mismatch` | "Công thức cần có nguyên liệu chính thuộc nhóm {nhóm} của món." | Medium | Sửa công thức hoặc nhóm của món |
| `ERR-MENU-422-11` | 422 | Giá bán sai (`BR-CAT-015`) hoặc ngày hiệu lực không sau hôm nay | `menu.price_invalid` | "Giá bán phải là bội số của 100 đồng và có hiệu lực từ ngày mai trở đi." | Medium | Sửa giá hoặc ngày |
| `ERR-MENU-422-12` | 422 | Cấu hình loại suất sai (`BR-CAT-017`) | `menu.meal_type_invalid` | "Cấu hình loại suất không hợp lệ." | Medium | Sửa cấu hình |
| `ERR-MENU-422-13` | 422 | Ngày bắt đầu tuần không phải thứ Hai, hoặc không chọn ngày phục vụ nào | `menu.week_invalid` | "Tuần phải bắt đầu từ thứ Hai và có ít nhất một ngày phục vụ." | Medium | Chọn lại |
| `ERR-MENU-422-14` | 422 | Xếp món không hoạt động, sai vai trò, vượt số ô, hoặc lặp trong ngày | `menu.slot_invalid` | "Không xếp được món {tên} vào vị trí này." | Medium | Chọn món khác |
| `ERR-MENU-422-15` | 422 | Món mặc định không phải món chính của ngày | `menu.default_invalid` | "Món mặc định phải là một món chính của ngày." | Medium | Chọn lại |
| `ERR-MENU-422-16` | 422 | Sửa quy tắc sai (`BR-MNU-007`) | `menu.rule_invalid` | "Giá trị quy tắc không hợp lệ." | Medium | Sửa giá trị |
| `ERR-MENU-422-17` | 422 | Gửi duyệt khi còn ô trống, thiếu món mặc định, hoặc có món không còn hoạt động | `menu.menu_incomplete` | "Thực đơn chưa đủ: {danh sách}." | High | Bổ sung |
| `ERR-MENU-422-18` | 422 | Gửi duyệt khi còn quy tắc cứng không đạt | `menu.hard_rule_failed` | "Thực đơn còn {n} vi phạm quy tắc bắt buộc." | High | Sửa thực đơn |
| `ERR-MENU-422-19` | 422 | Gửi duyệt khi vi phạm mềm–nặng chưa có lý do | `menu.waiver_required` | "Cần ghi lý do cho {n} cảnh báo mức nặng." | Medium | Ghi lý do |
| `ERR-MENU-422-20` | 422 | Tệp nhập còn dòng lỗi, sai mẫu, hoặc vượt 2.000 dòng | `menu.import_invalid` | "Tệp còn {n} lỗi. Xem danh sách lỗi theo dòng." | Medium | Sửa tệp, nhập lại |
| `ERR-MENU-422-21` | 422 | Ngày hiệu lực của công thức ở quá khứ, hoặc không sau ngày hiệu lực của phiên bản `ACTIVE`/`PENDING` khác cùng món và cỡ (`BR-CAT-022`) | `menu.recipe_effective_date` | "Ngày hiệu lực phải từ hôm nay và sau ngày hiệu lực của phiên bản hiện có ({ngày})." | Medium | Chọn ngày muộn hơn |
