---
id: DOC-THUC-DON-DINH-LUONG-API-API-SPEC
title: Hợp đồng API MENU E2
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Hợp đồng API MENU E2

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Quy ước và quyền

SRS MENU là nguồn nghiệp vụ, hợp đồng này không sửa rule/priority. Prefix `/v1/menu`; kiểu Id:string số nguyên dương, Date:YYYY-MM-DD, money:integer đồng, quantity:decimal string. List dùng page/pageSize/total theo E1; GET không body. Authorization Bearer, X-Request-Id; tạo mới có Idempotency-Key; sửa/transition có version và lý do theo SRS. Từ chối field lạ, sai kiểu; 401/403/404/409/422/500 theo AUTH/SYS/MENU. Payload lỗi dùng `{code,message,details,requestId}`. Cùng key/body replay theo quyền hiện tại, khác body409 đề xuất E1-Q02; tạo sửa import/audit nguyên tử.

Quyền theo ma trận SRS MENU: DINH_DUONG_VIEN soạn/tạo, người có quyền duyệt tách người tạo/sửa cuối; vai trò chỉ xem chỉ thấy PUBLISHED. Endpoint công cụ agent cũng kiểm giao quyền và scope. Quyền cost.cost.read là điều kiện độc lập khi serialize số Cost; không có quyền thì cả message/detail/evidence không chứa giá nhập, cost%, số tiền.

## Kiểu request/response theo nhóm

| Nhóm | Input typed (ngoài path id) | Output |
| :--- | :--- | :--- |
| ING | name:string1..160,groupId:Id,purchaseUnit/useUnit:string,conversionFactor:Decimal>0,lossPct:Decimal0..100,hasBoneShell:boolean,supplyStable:boolean; update version:int>=1; seasons:[{fromMonth:1..12,toMonth:1..12}]; tên chuẩn hóa unique | Ingredient id + fields + status/version; List Ingredient |
| DISH | name,role:MAIN/SIDE/VEG/SOUP,mainIngredientGroupId,cookingMethodId,baseDishId?,healthy:boolean,sour:boolean,hasSauce:boolean,dry:boolean,complexity enum theo SRS,transportSuitability enum theo SRS,suitableForMassKitchen:boolean,costGroup enum theo SRS,isSpecial:boolean,allergenIds:Id[]; version/reason nếu sửa | Dish với trạng thái DRAFT/PENDING/ACTIVE/INACTIVE; không tự duyệt |
| RCP | dishId,portionCode:STD (O-02 chưa chốt),effectiveFrom:Date,items:[{ingredientId,isMain,qtyMin,qtyMax,qtyStd:Decimal,unit}]; >=1 dòng và >=1 chính,0<min<=std<=max; unit khớp nguyên liệu; compare leftId/rightId | Recipe versionNo/version,status,effectiveFrom,items; Compare thêm/bớt/đổi |
| PRC | dishId,portionCode,priceVnd:integer>0,effectiveFrom; giá gồmVAT; không nhập VAT0 từ cờ hóa đơn | DishPrice PENDING/APPROVED/RETURNED theo trạng thái được xác nhận ở SRS/ERD; RETURNED cần review MENU-API-Q02 nếu schema chưa khớp |
| MTY | name,priceCeilingVnd:int>0,mainOptions:int>0,mainSelections:int>0<=mainOptions,sideCount:int>=0,hasVeg/hasSoup/public:boolean,version nếu sửa | MealType DRAFT/ACTIVE/INACTIVE |
| MNU | mealTypeId,weekStart:Date thứHai,serviceDates:Date[] trong tuần; items mutation:{version,slot,operation:ADD/REPLACE/REMOVE,dishId?,oldDishId?}; defaultDish:{dishId,version}; copy:{targetWeek,reason}; tất cả kiểm trạng thái nguồn | Menu,MenuDay,items:{dishId,recipeId,slot}; defaultDishId; version; rule summary |
| RUL | saved check:{version}; unsaved:{mealTypeId,weekStart,days:[{serviceDate,defaultDishId,items:[{dishId,recipeId,slot}]}],kitchenIds,clientRevision}; reason:{version,reason>=10 chars}; rule-change:{ruleId,version,patch,reason} | RuleCheck {inputHash,clientRevision,ruleSetVersion,score,hardViolation,results:[{ruleId,pass,severity,penalty,message,detail}]} |
| APV | {version,decision?:APPROVE/RETURN,reason?}; lý do theo thao tác, không client supplied status/ruleScore/approvedBy | Menu với trạng thái mới; requestId; số Cost chỉ khi có quyền |
| IMP | type:INGREDIENT/DISH/RECIPE/PRICE; validate multipart XLSX tối đa2000 dòng, size10MB đề xuất cùng E1; import:{validationId,fileHash,sourceVersions}; không nhận file chưa validate | Validation {id,fileHash,valid,rows,errors:[{row,column,code,message}]}; Import {id,createdCount,status} |

Tên API camelCase ánh xạ cột snake_case trong DBML tổng. Tất cả trường SRS bắt buộc phải có; enum đầy đủ/độ dài vật lý lấy [từ điển MENU](../srs/erd.md), không thêm giá trị enum ngoài schema. Thông tin nguồn recipe/price luôn theo ngày phục vụ, không lấy ngày hiện tại của client.

## Danh mục

| ID | Method/path | FR / priority | Input | Output / hành vi | Lỗi nghiệp vụ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-MENU-001 | POST /v1/menu/ingredients | FR-MENU-ING-001 / P0 | tên, nhóm, đơn vị mua, đơn vị dùng, hệ số quy đổi, loại bảo quản, có xương/vỏ, tỷ lệ hao hụt, nguồn cung ổn định; kiểu nhómING | 201; Nguyên liệu. Tạo nguyên liệu ở trạng thái `ACTIVE`. Hệ thống cấp mã. | ERR-MENU-409-01`, `ERR-MENU-422-01`, `ERR-MENU-422-02 |
| API-MENU-002 | PATCH /v1/menu/ingredients/{id} | FR-MENU-ING-002 / P0 | như trên + `version; kiểu nhómING | 200; Nguyên liệu. Sửa mọi trường trừ mã. Sửa đơn vị dùng hoặc hệ số quy đổi bị chặn nếu nguyên liệu đang nằm trong công thức `ACTIVE`. | ERR-MENU-409-02`, `ERR-SYS-409-02 |
| API-MENU-003 | POST /v1/menu/ingredients/{id}/status-changes | FR-MENU-ING-003 / P0 | mã, lý do; kiểu nhómING | 201; Trạng thái mới. Chuyển `INACTIVE` hoặc huỷ. Bị chặn nếu đang nằm trong công thức `ACTIVE`; lỗi trả kèm danh sách công thức. | ERR-SYS-409-01 |
| API-MENU-004 | GET /v1/menu/ingredients | FR-MENU-ING-004 / P0 | bộ lọc; kiểu nhómING | 200; Danh sách. Lọc theo tên, nhóm, loại bảo quản, trạng thái; phân trang. | — |
| API-MENU-005 | GET /v1/menu/ingredient-groups | FR-MENU-ING-005 / P0 | tên, nguồn đạm; kiểu nhómING | 200; Nhóm. Tạo, sửa, huỷ nhóm; mỗi nhóm khai nguồn đạm (thịt, cá, trứng, thuỷ sản, đậu, không). Danh sách khởi tạo: [H-3] | ERR-MENU-409-01 |
| API-MENU-006 | POST /v1/menu/ingredient-groups | FR-MENU-ING-005 / P0 | tên, nguồn đạm; kiểu nhómING | 201; Nhóm. Tạo, sửa, huỷ nhóm; mỗi nhóm khai nguồn đạm (thịt, cá, trứng, thuỷ sản, đậu, không). Danh sách khởi tạo: [H-3] | ERR-MENU-409-01 |
| API-MENU-007 | PATCH /v1/menu/ingredient-groups/{id} | FR-MENU-ING-005 / P0 | tên, nguồn đạm; kiểu nhómING | 200; Nhóm. Tạo, sửa, huỷ nhóm; mỗi nhóm khai nguồn đạm (thịt, cá, trứng, thuỷ sản, đậu, không). Danh sách khởi tạo: [H-3] | ERR-MENU-409-01 |
| API-MENU-008 | PUT /v1/menu/ingredients/{id}/seasons | FR-MENU-ING-006 / P1 | mã nguyên liệu, tháng từ, tháng đến; kiểu nhómING | 200; Mùa vụ. Một nguyên liệu có 0 hoặc nhiều khoảng tháng trong mùa. | ERR-MENU-422-03 |
| API-MENU-009 | POST /v1/menu/dishes | FR-MENU-DISH-001 / P0 | tên, mô tả, 12 thuộc tính, chất gây dị ứng; kiểu nhómDISH | 201; Món `DRAFT. Tạo món ở trạng thái `DRAFT` với 12 thuộc tính: vai trò, nhóm nguyên liệu chính, phương pháp chế biến, món gốc, Healthy, vị chua, kết cấu, thanh nhẹ, cầu kỳ, chịu vận chuyển, phù hợp bếp lớn, nhóm cost, đặc thù. | ERR-MENU-409-01`, `ERR-MENU-422-04`, `ERR-MENU-422-05 |
| API-MENU-010 | PATCH /v1/menu/dishes/{id} | FR-MENU-DISH-002 / P0 | như trên + `version`, lý do; kiểu nhómDISH | 200; Món. DRAFT`: sửa tự do. `ACTIVE`: sửa thuộc tính ảnh hưởng quy tắc tạo một đề nghị thay đổi chờ duyệt (`change_requests`); món vẫn `ACTIVE` với giá trị cũ và hiện nhãn "chờ duyệt thay đổi" cho đến khi đề nghị được duyệt. Mỗi món tối đa 1 đề nghị đang chờ. | ERR-SYS-409-02`, `ERR-SYS-422-01 |
| API-MENU-011 | POST /v1/menu/dishes/{id}/submissions | FR-MENU-DISH-003 / P0 | mã món; kiểu nhómDISH | 201; Món `PENDING. DRAFT` → `PENDING`. Điều kiện: đủ thuộc tính bắt buộc và có ít nhất 1 công thức ở trạng thái `PENDING` hoặc `ACTIVE`. | ERR-MENU-422-06 |
| API-MENU-012 | POST /v1/menu/dishes/{id}/decisions | FR-MENU-DISH-004 / P0 | danh sách mã, quyết định, lý do; kiểu nhómDISH | 201; Trạng thái mới. Duyệt: `PENDING` → `ACTIVE`. Trả lại: → `DRAFT` kèm lý do. Duyệt được nhiều món một lần. | ERR-SYS-403-01`, `ERR-MENU-422-06 |
| API-MENU-013 | POST /v1/menu/dishes/{id}/deactivations | FR-MENU-DISH-005 / P0 | mã, lý do; kiểu nhómDISH | 201; Trạng thái mới. ACTIVE` → `INACTIVE`. Bị chặn nếu món nằm trong thực đơn `PUBLISHED` có ngày phục vụ từ hôm nay trở đi. Món nằm trong thực đơn `DRAFT`/`CHECKED` hoặc thực đơn đã phục vụ xong **không** bị chặn; thực đơn nháp chứa món đã ngừng sẽ bị chặn ở bước gửi duyệt (`ERR-MENU-422-17`). | ERR-SYS-409-01 |
| API-MENU-014 | GET /v1/menu/dishes | FR-MENU-DISH-006 / P0 | bộ lọc; kiểu nhómDISH | 200; Danh sách. Lọc theo tên, vai trò, nhóm nguyên liệu, phương pháp, Healthy, trạng thái; phân trang. | — |
| API-MENU-015 | GET /v1/menu/cooking-methods | FR-MENU-DISH-007 / P0 | tên, 2 cờ; kiểu nhómDISH | 200; Phương pháp. Mỗi phương pháp có 2 cờ: là chiên/rán; là ít dầu mỡ. Danh sách khởi tạo: [H-8]; phương pháp nào là ít dầu mỡ: [H-1]. Không bỏ được cờ ít dầu mỡ khi còn món Healthy đang dùng phương pháp đó. | ERR-MENU-409-01`, `ERR-SYS-409-01 |
| API-MENU-016 | POST /v1/menu/cooking-methods | FR-MENU-DISH-007 / P0 | tên, 2 cờ; kiểu nhómDISH | 201; Phương pháp. Mỗi phương pháp có 2 cờ: là chiên/rán; là ít dầu mỡ. Danh sách khởi tạo: [H-8]; phương pháp nào là ít dầu mỡ: [H-1]. Không bỏ được cờ ít dầu mỡ khi còn món Healthy đang dùng phương pháp đó. | ERR-MENU-409-01`, `ERR-SYS-409-01 |
| API-MENU-017 | PATCH /v1/menu/cooking-methods/{id} | FR-MENU-DISH-007 / P0 | tên, 2 cờ; kiểu nhómDISH | 200; Phương pháp. Mỗi phương pháp có 2 cờ: là chiên/rán; là ít dầu mỡ. Danh sách khởi tạo: [H-8]; phương pháp nào là ít dầu mỡ: [H-1]. Không bỏ được cờ ít dầu mỡ khi còn món Healthy đang dùng phương pháp đó. | ERR-MENU-409-01`, `ERR-SYS-409-01 |
| API-MENU-018 | GET /v1/menu/dish-conflicts | FR-MENU-DISH-008 / P0 | món A, món B, ghi chú; kiểu nhómDISH | 200; Cặp kỵ. Khai cặp 2 món không được xếp cùng ngày. Danh sách khởi tạo: [H-4] | ERR-MENU-409-01`, `ERR-MENU-422-07 |
| API-MENU-019 | POST /v1/menu/dish-conflicts | FR-MENU-DISH-008 / P0 | món A, món B, ghi chú; kiểu nhómDISH | 201; Cặp kỵ. Khai cặp 2 món không được xếp cùng ngày. Danh sách khởi tạo: [H-4] | ERR-MENU-409-01`, `ERR-MENU-422-07 |
| API-MENU-020 | POST /v1/menu/dishes/{id}/images | FR-MENU-DISH-009 / P1 | mã món, tệp; kiểu nhómDISH | 201; —. Gắn 1 ảnh cho món qua `FR-SYS-FILE-001`. | ERR-SYS-413-01`, `ERR-SYS-415-01 |
| API-MENU-021 | POST /v1/menu/recipes | FR-MENU-RCP-001 / P0 | mã món, cỡ định lượng (mặc định `STD`), ngày hiệu lực, các dòng; kiểu nhómRCP | 201; Công thức `DRAFT`, phiên bản kế tiếp. Tạo công thức `DRAFT` cho một món: ≥ 1 dòng nguyên liệu, ≥ 1 dòng đánh dấu nguyên liệu chính. Mỗi dòng: định lượng tối thiểu, tối đa, chuẩn; đơn vị tự lấy từ đơn vị dùng của nguyên liệu. | ERR-MENU-422-08`, `ERR-MENU-422-09`, `ERR-MENU-422-10`, `ERR-MENU-422-21 |
| API-MENU-022 | PATCH /v1/menu/recipes/{id} | FR-MENU-RCP-002 / P0 | như trên + `version; kiểu nhómRCP | 200; Công thức. Chỉ sửa được khi `DRAFT`. | ERR-MENU-409-03 |
| API-MENU-023 | POST /v1/menu/recipes/{id}/transitions | FR-MENU-RCP-003 / P0 | mã, quyết định, lý do; kiểu nhómRCP | 201; Trạng thái mới. DRAFT` → `PENDING` → `ACTIVE` hoặc về `DRAFT`. Khi duyệt: nếu ngày hiệu lực ≤ hôm nay thì phiên bản `ACTIVE` trước đó cùng món, cùng cỡ chuyển `SUPERSEDED`; nếu ngày hiệu lực ở tương lai thì cả hai cùng `ACTIVE` và tác vụ nền chuyển phiên bản cũ vào ngày hiệu lực. | ERR-SYS-403-01 |
| API-MENU-024 | POST /v1/menu/recipes/{id}/versions | FR-MENU-RCP-004 / P0 | mã công thức, ngày hiệu lực, lý do; kiểu nhómRCP | 201; Công thức `DRAFT. Sao chép một phiên bản `ACTIVE` thành `DRAFT` với số phiên bản kế tiếp. | — |
| API-MENU-025 | GET /v1/menu/effective-recipes | FR-MENU-RCP-005 / P0 | mã món, cỡ, ngày D; kiểu nhómRCP | 200; Công thức. Trả công thức `ACTIVE` của món và cỡ định lượng có ngày hiệu lực lớn nhất không vượt ngày D. | ERR-MENU-404-01 |
| API-MENU-026 | GET /v1/menu/recipe-comparisons | FR-MENU-RCP-006 / P1 | 2 mã công thức; kiểu nhómRCP | 200; Bảng khác biệt. Hiện từng dòng nguyên liệu thêm, bớt, đổi định lượng. | — |
| API-MENU-027 | POST /v1/menu/dish-prices | FR-MENU-PRC-001 / P0 | mã món, cỡ, giá, ngày hiệu lực; kiểu nhómPRC | 201; Giá `PENDING. Tạo giá `PENDING` cho một món và cỡ định lượng; giá đã gồm VAT [D-15]. | ERR-MENU-422-11`, `ERR-MENU-409-04 |
| API-MENU-028 | POST /v1/menu/dish-prices/{id}/decisions | FR-MENU-PRC-002 / P0 | mã, quyết định, lý do; kiểu nhómPRC | 201; Trạng thái mới. PENDING` → `APPROVED`. Giá `APPROVED` không sửa, không huỷ nếu ngày hiệu lực đã đến. | ERR-SYS-403-01`, `ERR-MENU-409-10 |
| API-MENU-029 | GET /v1/menu/effective-dish-prices | FR-MENU-PRC-003 / P0 | mã món, cỡ, ngày D; kiểu nhómPRC | 200; Giá. Trả giá `APPROVED` có ngày hiệu lực lớn nhất không vượt ngày D. | ERR-MENU-404-02 |
| API-MENU-030 | GET /v1/menu/dishes/{id}/price-history | FR-MENU-PRC-004 / P1 | mã món; kiểu nhómPRC | 200; Danh sách. Danh sách giá của một món theo thời gian. | — |
| API-MENU-031 | POST /v1/menu/meal-types | FR-MENU-MTY-001 / P0 | tên, ngưỡng giá (gồm VAT), số món chính đưa ra, số món chính được chọn, số món phụ, có rau, có canh; kiểu nhómMTY | 201; Loại suất. Tạo ở trạng thái `DRAFT`. | ERR-MENU-422-12 |
| API-MENU-032 | POST /v1/menu/meal-types/{id}/status-changes | FR-MENU-MTY-002 / P0 | mã, lý do; kiểu nhómMTY | 201; Trạng thái mới. DRAFT` → `ACTIVE` → `INACTIVE`. Ngừng không ảnh hưởng thực đơn đã công bố. | — |
| API-MENU-033 | PATCH /v1/menu/meal-types/{id} | FR-MENU-MTY-003 / P0 | như `001` + `version; kiểu nhómMTY | 200; Loại suất. Tên và cờ công khai: sửa bất kỳ lúc nào. Cơ cấu (ngưỡng giá, số món, rau, canh): chỉ sửa khi chưa có thực đơn nào từ `PENDING` trở đi. | ERR-MENU-409-05 |
| API-MENU-034 | PATCH /v1/menu/meal-types/{id}/visibility | FR-MENU-MTY-004 / P1 | mã, cờ; kiểu nhómMTY | 200; —. Loại suất công khai hiện trên website ở E8. | — |
| API-MENU-035 | POST /v1/menu/menus | FR-MENU-MNU-001 / P0 | loại suất, ngày thứ Hai của tuần, danh sách ngày phục vụ; kiểu nhómMNU | 201; Thực đơn `DRAFT` với các ngày trống. Tạo thực đơn `DRAFT` cho một loại suất `ACTIVE` và một tuần; chọn các ngày phục vụ trong tuần. Các ngày được phép: [E2-Q3] | ERR-MENU-409-06`, `ERR-MENU-422-13 |
| API-MENU-036 | PUT /v1/menu/menu-days/{id}/items | FR-MENU-MNU-002 / P0 | mã ngày, vị trí, mã món; kiểu nhómMNU | 200; Ngày đã cập nhật + kết quả kiểm. Thêm, đổi, bỏ món ở một vị trí của một ngày. Chỉ chọn được món `ACTIVE` có vai trò khớp vị trí. Hệ thống gắn công thức hiệu lực tại ngày phục vụ. Sau mỗi thay đổi, bộ kiểm chạy lại (`FR-MENU-RUL-001`). | ERR-MENU-422-14`, `ERR-MENU-404-01`, `ERR-MENU-409-07 |
| API-MENU-037 | PUT /v1/menu/menu-days/{id}/default-dish | FR-MENU-MNU-003 / P0 | mã ngày, mã món; kiểu nhómMNU | 200; —. Đặt một trong các món chính của ngày làm món mặc định. Bỏ món đang là mặc định khỏi ngày thì món mặc định bị xoá. | ERR-MENU-422-15 |
| API-MENU-038 | POST /v1/menu/menus/{id}/copies | FR-MENU-MNU-005 / P1 | mã thực đơn nguồn, tuần đích; kiểu nhómMNU | 201; Thực đơn `DRAFT. Tạo bản `DRAFT` cho tuần đích từ một thực đơn bất kỳ cùng loại suất. Món không còn `ACTIVE` bị bỏ trống và được liệt kê. Món mặc định của từng ngày được sao chép theo (trừ khi món đó bị bỏ trống). Mỗi ô gắn công thức hiệu lực tại ngày phục vụ mới. Bộ kiểm chạy ngay trên bản sao. | ERR-MENU-409-06 |
| API-MENU-039 | GET /v1/menu/dish-usage | FR-MENU-MNU-006 / P1 | loại suất, tuần; kiểu nhómMNU | 200; Bảng món × ngày. Khi chọn món, hiện mỗi món đã xuất hiện ngày nào trong 4 tuần gần nhất của cùng loại suất. Chỉ tính thực đơn ở trạng thái `PUBLISHED`; không tính thực đơn nháp, chờ duyệt, đã thu hồi, đã huỷ, và không tính loại suất khác. | — |
| API-MENU-040 | GET /v1/menu/menus | FR-MENU-MNU-007 / P0 | bộ lọc; kiểu nhómMNU | 200; Danh sách / chi tiết. Lọc theo loại suất, tuần, trạng thái. Vai trò không có quyền ghi chỉ thấy `PUBLISHED`. | — |
| API-MENU-041 | POST /v1/menu/menus/{id}/exports | FR-MENU-MNU-008 / P1 | mã thực đơn; kiểu nhómMNU | 202; Tệp PDF. Xuất thực đơn tuần ra PDF: ngày × vị trí × tên món, đánh dấu món mặc định; tiêu đề ghi loại suất và khoảng ngày. Tệp **không** chứa giá bán, giá nhập hay cost. Thực đơn chưa `PUBLISHED` có dòng "BẢN NHÁP — CHƯA CÔNG BỐ" trên mỗi trang. | — |
| API-MENU-042 | POST /v1/menu/menus/{id}/cancellations | FR-MENU-MNU-009 / P0 | mã, lý do; kiểu nhómMNU | 201; —. Huỷ thực đơn `DRAFT` hoặc `CHECKED`. | ERR-MENU-409-08 |
| API-MENU-043 | POST /v1/menu/menus/{id}/checks | FR-MENU-RUL-001 / P0 | mã thực đơn; kiểu nhómRUL | 200; Danh sách kết quả, điểm, cờ. Chạy mọi quy tắc đang áp dụng trên một thực đơn. Trả kết quả từng quy tắc, điểm quy tắc, và cờ "còn vi phạm cứng". Ghi kết quả vào `menu_rule_results`, thay kết quả cũ. Với quy tắc cost, chỉ người có `cost.cost.read` nhận cost % và số tiền; người thiếu quyền chỉ nhận đạt/không đạt. API phải loại bỏ số nhạy cảm cả trong detail và thông báo lỗi, không chỉ ẩn ở UI (`FR-COST-RUL-002`, `NFR-COST-005`). Cách tính từng quy tắc ở mục 3.3. | — |
| API-MENU-044 | POST /v1/menu/menu-validations | FR-MENU-RUL-002 / P0 | loại suất, tuần, các ngày và món; kiểu nhómRUL | 200; Như `001. Như `001` nhưng nhận nội dung thực đơn trong yêu cầu và không ghi gì. Dùng cho agent ở E5, E9 thử phương án. | ERR-MENU-422-14 |
| API-MENU-045 | GET /v1/menu/menus/{id}/rule-results | FR-MENU-RUL-003 / P0 | —; kiểu nhómRUL | 200; Ví dụ: "BR-MENU-012 · Thịt lợn ở món chính 3 ngày liền (T2, T3, T4) · giới hạn 2". Mỗi kết quả không đạt nêu: mã quy tắc, tên, loại, ngày liên quan, món liên quan, giá trị đo được, giới hạn. | — |
| API-MENU-046 | PUT /v1/menu/rule-results/{id}/acceptance-reasons | FR-MENU-RUL-004 / P0 | mã kết quả, lý do; kiểu nhómRUL | 200; —. Với quy tắc mềm–nặng không đạt, người dựng ghi lý do ≥ 10 ký tự. Lý do bị xoá nếu lần kiểm sau quy tắc đó đạt. | ERR-SYS-422-01 |
| API-MENU-047 | GET /v1/menu/menu-rules | FR-MENU-RUL-005 / P0 | —; kiểu nhómRUL | 200; Danh sách. Xem danh sách quy tắc: mã, tên, loại, điểm phạt, phạm vi ngày/tuần, tham số, đang bật. | — |
| API-MENU-048 | POST /v1/menu/menu-rule-changes | FR-MENU-RUL-006 / P0 | mã quy tắc, giá trị mới, lý do; kiểu nhómRUL | 200; Đề nghị chờ duyệt. Đề nghị bật/tắt, đổi loại, đổi điểm phạt, đổi tham số. Có hiệu lực sau khi duyệt. Thực đơn `DRAFT`, `CHECKED` được kiểm lại bằng quy tắc mới ở lần kiểm kế tiếp; thực đơn từ `PENDING` trở đi giữ kết quả lúc gửi duyệt ([E2-Q11]). | ERR-SYS-403-01`, `ERR-MENU-422-16 |
| API-MENU-049 | POST /v1/menu/menus/{id}/submissions | FR-MENU-APV-001 / P0 | mã thực đơn; kiểu nhómAPV | 200; Thực đơn `PENDING. DRAFT`/`CHECKED` → `PENDING`. Hệ thống chạy lại bộ kiểm ngay trước khi chuyển. Điều kiện ở `BR-MNU-005`. Thông báo cho người có quyền duyệt theo `BR-MNU-010`. | ERR-MENU-422-17`, `ERR-MENU-422-18`, `ERR-MENU-422-19 |
| API-MENU-050 | POST /v1/menu/menus/{id}/decisions | FR-MENU-APV-002 / P0 | mã, quyết định, lý do; kiểu nhómAPV | 200; Trạng thái mới. Duyệt: → `APPROVED`, đóng băng kết quả kiểm và công thức đã gắn. Trả lại: → `DRAFT` kèm lý do. Thông báo cho người tạo. | ERR-SYS-403-01 |
| API-MENU-051 | POST /v1/menu/menus/{id}/publications | FR-MENU-APV-003 / P0 | mã; kiểu nhómAPV | 200; Thực đơn `PUBLISHED. APPROVED` → `PUBLISHED`. Từ lúc này thực đơn xuất hiện ở dịch vụ tra cứu thực đơn đã công bố. | ERR-MENU-409-09 |
| API-MENU-052 | POST /v1/menu/menus/{id}/withdrawals | FR-MENU-APV-004 / P0 | mã, lý do; kiểu nhómAPV | 200; Thực đơn `WITHDRAWN. PUBLISHED` → `WITHDRAWN`, bắt buộc lý do. Phát sự kiện để E6 xử lý lựa chọn món đã có. | ERR-SYS-422-01 |
| API-MENU-053 | POST /v1/menu/menus/{id}/reopenings | FR-MENU-APV-005 / P0 | mã; kiểu nhómAPV | 200; Thực đơn `DRAFT. WITHDRAWN` → `DRAFT`; sau đó đi lại toàn bộ chu trình kiểm, duyệt, công bố. | — |
| API-MENU-054 | GET /v1/menu/import-templates/{type} | FR-MENU-IMP-001 / P0 | loại mẫu; kiểu nhómIMP | 200; Tệp `.xlsx. 4 mẫu `.xlsx`: nguyên liệu, món, công thức, giá bán. Mỗi mẫu có dòng tiêu đề, dòng ví dụ, và trang liệt kê giá trị hợp lệ của các cột liệt kê. | — |
| API-MENU-055 | POST /v1/menu/import-validations | FR-MENU-IMP-002 / P0 | loại, tệp; kiểu nhómIMP | 201; Số dòng hợp lệ, danh sách lỗi. Đọc tệp, kiểm từng dòng theo đúng quy tắc của FR tạo tương ứng, trả danh sách lỗi theo số dòng và cột. Không ghi gì. Tối đa 2.000 dòng mỗi tệp. | ERR-MENU-422-20`, `ERR-SYS-413-01`, `ERR-SYS-415-01 |
| API-MENU-056 | POST /v1/menu/imports | FR-MENU-IMP-003 / P0 | loại, tệp; kiểu nhómIMP | 201; Số bản ghi đã tạo. Chỉ chạy khi tệp không còn lỗi. Ghi toàn bộ trong một giao dịch: tất cả hoặc không gì cả. Món và công thức vào `DRAFT`; giá vào `PENDING`; nguyên liệu vào `ACTIVE`. | ERR-MENU-422-20 |
| API-MENU-057 | GET /v1/menu/menus/{id} | FR-MENU-MNU-007 | path id; không body | 200 chi tiết/version; scope hiện tại, lịch sử có nhãn trạng thái | ERR-SYS-404-01 |
| API-MENU-058 | GET /v1/menu/dishes/{id} | FR-MENU-DISH-006 | path id; không body | 200 chi tiết/version; scope hiện tại, lịch sử có nhãn trạng thái | ERR-SYS-404-01 |
| API-MENU-059 | GET /v1/menu/ingredients/{id} | FR-MENU-ING-004 | path id; không body | 200 chi tiết/version; scope hiện tại, lịch sử có nhãn trạng thái | ERR-SYS-404-01 |
| API-MENU-060 | GET /v1/menu/recipes/{id} | FR-MENU-RCP-005 | path id; không body | 200 chi tiết/version; scope hiện tại, lịch sử có nhãn trạng thái | ERR-SYS-404-01 |

## Port, feature gated và luồng nhiều bước

- FR-MENU-MNU-004 là bước kiểm giá trong checks/validations, không endpoint riêng. FR-MENU-APV-006 gọi COST API-COST-025 cùng input/version trước chuyển trạng thái; CHAN chặn vượt, CANH_BAO cảnh báo, thiếu đầu vào vẫn chặn. Không thay NFR-COST-002.
- FR-MENU-RUL-007 là guard P1 người duyệt thứhai tại submissions/decisions; chưa tự cấp vai trò/thẩm quyền ngoài O-06. FR-MENU-RCP-007 chưa xếp phạm vi, không có endpoint độc lập: giữ STD, chờ O-02.
- `recipes/{id}/transitions` nhận action SUBMIT/APPROVE/RETURN,version,reason; SUBMIT đòi DRAFT,APPROVE/RETURN đòi PENDING và quyền khác người tạo/sửa; tất cả nguyên tử và audit.
- `dish-conflicts` GET/POST quản lý cặp unordered(A,B), không self; bỏ cặp qua đề nghị thay đổi với version/reason, chưa hard-delete. Chốt route deactivate trước backend tại MENU-API-Q01.
- `menu-rule-changes` chỉ tạo đề nghị qua change_requests/approvals của nền tảng; không tự ghi rule có hiệu lực trước duyệt. Port applyApprovedChange phải được Tech lead chốt cùng E1 trước xây.
- Import XLSX tách khỏi FILE-001 (không nhận XLSX). Validate không ghi nghiệp vụ; import đối chiếu hash/version, mọi dòng cùng transaction; nguồn đổi thì409, hết hạn validation cần validate lại. Không reuse kết quả validate cho file khác.
- Xuất PDF MNU-008 là job có polling qua SYS jobs hoặc URL kết quả theo quyền; tài liệu chưa công bố có watermark mỗi trang; không chứa giá bán/giá nhập/cost. Đây là contract, chưa tạo file PDF/backend.

## Ví dụ kiểm nháp và ownership Agent

`POST /v1/menu/menu-validations` với `{mealTypeId:"10",weekStart:"2026-11-16",days:[...],kitchenIds:["1"],clientRevision:2}` →200 RuleCheck. Đây là dạng minh họa, days phải theo typed schema đầy đủ, không gửi dấu `...`.

Port `menu.validate` của E5 ánh xạ endpoint này, inputHash do server tính. Port `menu.applyDraft` vẫn là giao dịch phối hợp nội bộ, không cho model tự gọi HTTP để tạo/duyệt/công bố. POST checks chạy thành công có thể trả hardViolation=true: không nhầm HTTP200 với thực đơn đạt. UI nhận response chỉ khi đúng version/clientRevision.

## Câu hỏi hợp đồng — CHỜ XÁC NHẬN

| Mã | Nội dung | Người review |
| :--- | :--- | :--- |
| MENU-API-Q01 | Route thay đổi/hủy cặp kỵ và quyết định menu-rule-change dùng service chung hay API riêng; lifecycle/error chi tiết? | Tech lead, BA |
| MENU-API-Q02 | Giá bị trả lại có trạng thái RETURNED hay hủy đề nghị; đồng bộ trạng thái DBML trước migration? | BA, Tech lead |
| MENU-API-Q03 | TTL/size XLSX, nơi lưu validation hash/version, idempotency/output job export? | Tech lead |

Các điểm E2-Q*, DL-01, O-02/O-06 không được đóng bởi việc có API catalog. [RTM API](api-traceability.md).
