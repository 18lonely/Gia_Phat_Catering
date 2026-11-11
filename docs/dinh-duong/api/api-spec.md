# Hợp đồng API — Dinh dưỡng MVP

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

## Quy ước chung

Hợp đồng đề xuất v0.1, chưa có server chạy. Prefix `/v1` kế thừa Cost. HTTPS; phiên Bearer từ AUTH, không đưa token vào log; nếu triển khai cookie phải có CSRF theo nền tảng. `Content-Type: application/json`; `X-Request-Id` để truy vết; id là chuỗi số nguyên dương để không mất precision bigint; ngày `YYYY-MM-DD` theo Asia/Ho_Chi_Minh, thời điểm UTC ISO 8601.

Response chuẩn: `{success:true,data:...,error:null,meta:{requestId},timestamp}`; lỗi `{success:false,data:null,error:{code,message,fields:[{field,reason}]},meta:{requestId},timestamp}`. Số decimal biểu diễn bằng chuỗi dấu chấm, không dấu phân cách nghìn; totals không có NaN/Infinity. Từ chối field ngoài schema. Response list có `items,nextCursor`; limit mặc định 20, tối đa 100 **đề xuất**; cursor opaque gắn filter/scope; không tin cursor để bỏ kiểm quyền. Sort ổn định theo id; log sort created_at/id giảm dần. 400 sai JSON/kiểu; 401 mất phiên; 403 thiếu quyền; 404 id ngoài scope/không tồn tại; 409 xung đột; 422 dữ liệu nghiệp vụ; 500 lỗi giao dịch; chi tiết mã ở SRS.

Mỗi POST ghi bền vững cần `Idempotency-Key` (chuỗi 16–128 ký tự **đề xuất**) scope=(user,route,key), hash body chuẩn hóa. Cùng body trả resource gốc theo quyền hiện tại; body khác 409; request đang xử lý trả 409 kèm Retry-After và resourceId nếu đã có. Đề xuất giữ key tối thiểu 24h, cần Tech lead review; hết hạn không chứng minh chưa ghi. Sổ key phải nằm trong kho bền vững/giao dịch cùng resource, không chỉ Redis TTL. Thiết kế dưới đây có cột request_key/request_hash và unique trong bảng đích; việc dọn key chưa được cho phép. PUT dùng version lạc quan; replay PUT sau mất phản hồi phải GET giá trị/version và revision để đối soát. Không tự retry lệnh bằng key mới khi chưa rõ kết quả.

Không có webhook công khai. Endpoint chỉ đọc hoặc kiểm độ phủ không gọi provider và không thay trạng thái MENU. Tất cả dữ liệu ví dụ dưới đây là **GIẢ ĐỊNH để review**, không phải dữ liệu thực tế Gia Phát.

## Kiểu dữ liệu

| Kiểu | Trường và ràng buộc |
| :--- | :--- |
| NutrientInput | version:int≥0 (0 khi tạo); energyKcal:decimal(7,2)≥0; proteinG/fatG/carbG:decimal(6,2)≥0; ediblePct:decimal(5,2) trong [0,100]; gramsPerUnit:decimal(8,2)>0 bắt buộc nếu use_unit≠g, null nếu g; source:string1..120; sourceEdition:string1..120; sourceLocator:string1..120; reason:string10..500. Tất cả bắt buộc trừ gramsPerUnit theo điều kiện; không default ediblePct ở API |
| NutrientValue | NutrientInput không reason + ingredientId, updatedAt, updatedBy, revisionId; revision chứa reason; 4 chỉ số luôn có đơn vị trên 100g phần ăn được |
| CoverageInput | recipeIds:Id[1..200] không trùng; giới hạn 200 là đề xuất, không giới hạn nghiệp vụ 30 món |
| Coverage | total:int; complete:int; missing:[{ingredientId,recipeIds,fields}]; recipeVersions:[{recipeId,version}]; không có totals dinh dưỡng |
| DishInput | recipeId:Id; serviceDate:Date; clientRevision:int≥1 |
| MealInput | menuId:Id; menuVersion:int≥1; serviceDate:Date; selectedItemIds:Id[] đầy đủ món chính và cố định của tổ hợp, không trùng; clientRevision:int≥1; số lượng món đối chiếu meal_types và ngày, không nhận quantity tự do |
| Totals | energyKcal,proteinG,fatG,carbG:decimal string ≥0; đơn vị kcal/g; tổng lưu decimal(24,8), hiển thị 2 chữ số đề xuất NUTR-Q04 |
| Calculation | id,kind:DISH/MEAL,recipeId? hoặc menuId/menuVersion?,serviceDate,selectedItemIds?,clientRevision,totals,displayTotals,label,sourceVersions,breakdown,calculatedAt,isStale:boolean; label cố định “ước tính từ định lượng sống” |
| breakdown[] | recipeId,ingredientId,qtyStd,unit,gramsPerUnit,ediblePct,edibleGrams,nutrientRevisionId,valuesPer100g,contribution; đủ dữ liệu tái tính độc lập |
| sourceVersions | recipeIds/versions; nutrientRevisionIds; unit conversion values; menuVersion nếu có; calculationMethodVersion='NUTR-0.1'; roundingPolicy='PROPOSED_HALF_UP_2' |

Thiếu dữ liệu trả 422 với `error.fields` và `error.missing[]`, `data:null`; UI biểu diễn totals=null. Không tạo Calculation thành công cho dữ liệu thiếu. GET kết quả cũ có isStale tính từ version hiện hành; nếu nguồn đã ngừng thì vẫn giữ dữ liệu lịch sử trong phạm vi quyền.

## Danh mục

| ID | Method/path | Quyền | Request | Thành công | Truy vết |
| :--- | :--- | :--- | :--- | :--- | :--- |
| API-NUTR-001 | PUT /v1/nutrition/ingredients/{id} | nutr.write | NutrientInput | 201 tạo /200 sửa; NutrientValue; nguyên tử current+revision+audit | FR-NUTR-REF-001; UI-NUTR-01 |
| API-NUTR-002 | POST /v1/nutrition/coverage-checks | nutr.read | CoverageInput; không cần key, không ghi | 200 Coverage kể cả còn missing | FR-NUTR-REF-002; UI-NUTR-01 |
| API-NUTR-003 | POST /v1/nutrition/dish-calculations | nutr.calculate, MENU read | DishInput + key | 201 Calculation; replay 200 cùng id | FR-NUTR-CALC-001; UI-NUTR-02 |
| API-NUTR-004 | POST /v1/nutrition/meal-calculations | nutr.calculate, MENU read đúng scope | MealInput + key | 201 Calculation; replay 200; tổ hợp sai 422-03 | FR-NUTR-CALC-002; UI-NUTR-03 |
| API-NUTR-005 | GET /v1/nutrition/calculations/{id} | nutr.read và scope nguồn | Không body | 200 Calculation; ngoài scope 404 | FR-NUTR-SNAP-001; UI-NUTR-02/03 |
| API-NUTR-006 | GET /v1/nutrition/ingredients | nutr.read | ingredientIds?:CSV Id, search?:string≤120, cursor?,limit? | 200 List NutrientValue; chưa nhập trả item ingredientId với value=null; không giả 0 | FR-NUTR-REF-001/002; UI-NUTR-01 |
| API-NUTR-007 | GET /v1/nutrition/ingredients/{id}/revisions | nutr.read | cursor?,limit? | 200 List revisionId/version/valueSnapshot/reason/changedBy/changedAt | FR-NUTR-REF-001, FR-NUTR-SNAP-001; UI-NUTR-01/02 |

Mã lỗi dùng prefix ERR-NUTR: PUT: 422-01/409-01; tính món: 422-02; tính suất: 422-02/03,409-01; tất cả áp lỗi chung theo trigger SRS. Idempotency collision/in-flight ở POST dùng 409-01 với reason `KEY_BODY_MISMATCH`/`IN_PROGRESS` (không mượn mã AIO). 500 không trả kết quả một phần. PUT version=0 nhưng bản ghi đã có trả409, không upsert mù.

## Ví dụ tính món

```json
{"recipeId":"101","serviceDate":"2026-11-16","clientRevision":1}
```

Với fixture I1 ở AC-NUTR-007, data thành công có dạng:

```json
{"id":"901","kind":"DISH","recipeId":"101","serviceDate":"2026-11-16","clientRevision":1,"totals":{"energyKcal":"40.00000000","proteinG":"4.00000000","fatG":"0.80000000","carbG":"6.00000000"},"displayTotals":{"energyKcal":"40.00","proteinG":"4.00","fatG":"0.80","carbG":"6.00"},"label":"ước tính từ định lượng sống","isStale":false}
```

Ví dụ rút gọn bỏ provenance/breakdown để đọc; response thực theo kiểu Calculation phải có đủ hai trường đó và calculatedAt. Không dùng ví dụ rút gọn làm schema bỏ trường. Khi cần đối soát dùng snapshot chưa làm tròn, không cộng displayTotals.

## Gate review

[NUTR-Q01–04 và DATA-NUTR-Q01](../review/questions.md) còn mở. Không upload/import Excel mới trong hợp đồng MVP này; DL-07 được nhập tay theo từng nguyên liệu. Nếu cần nhập hàng loạt phải bổ sung CR và validation dòng, không suy từ import MENU.
