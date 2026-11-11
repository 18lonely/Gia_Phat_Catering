# Test cases — NUTR

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Bộ ca được thiết kế, **0 ca backend đã chạy**. NOT RUN: chưa có backend/môi trường; BLOCKED: còn thiếu quyết định hoặc dữ liệu ngoài việc thiếu môi trường. Actual/evidence hiện “—”. Khi chạy ghi build, môi trường, tài khoản, fixture/version, requestId, thời gian, actual, defect/retest.

| TC | Story / AC | FR / BR | Tiền điều kiện / dữ liệu | Bước chạy | Expected | Trạng thái / blocker | Actual / evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-NUTR-001 | US-NUTR-001 / AC-NUTR-001 | FR-NUTR-REF-001 / BR-NUTR-001 | bảng thử nguyên liệu I1 chưa có, nguồn ghi rõ GIẢ ĐỊNH, kcal=100; đạm=10; béo=2; carb=15; ediblePct=80; unit=g | 1. Seed fixture vào môi trường test; 2. PUT đủ trường với version=0; 3. Đối chiếu response, bảng/audit và UI theo expected | 201; version=1; 1 revision và audit; số liệu giữ đúng, không đổi công thức món | NOT RUN | — |
| TC-NUTR-002 | US-NUTR-001 / AC-NUTR-002 | FR-NUTR-REF-001 / BR-NUTR-001 | I1 có version=1 | 1. Seed fixture vào môi trường test; 2. PUT energyKcal=-1 hoặc proteinG=null hoặc thiếu sourceLocator; 3. Đối chiếu response, bảng/audit và UI theo expected | 422; ERR-NUTR-422-01; không ghi bất kỳ bảng nào | NOT RUN | — |
| TC-NUTR-003 | US-NUTR-001 / AC-NUTR-003 | FR-NUTR-REF-001 / BR-NUTR-001 | hai người cùng đọc I1 version=1; người thứ nhất đã ghi version=2 | 1. Seed fixture vào môi trường test; 2. người thứ hai PUT version=1; 3. Đối chiếu response, bảng/audit và UI theo expected | 409 ERR-NUTR-409-01; giá trị version=2 không bị ghi đè | NOT RUN | — |
| TC-NUTR-004 | US-NUTR-002 / AC-NUTR-004 | FR-NUTR-REF-002 / BR-NUTR-002 | hai công thức thử dùng chung I1 và I2 đều đủ dữ liệu | 1. Seed fixture vào môi trường test; 2. POST recipeIds của hai công thức; 3. Đối chiếu response, bảng/audit và UI theo expected | 200; complete=2,total=2; không đếm lặp I1 | NOT RUN | — |
| TC-NUTR-005 | US-NUTR-002 / AC-NUTR-005 | FR-NUTR-REF-002 / BR-NUTR-002 | I2 chưa có bảng thành phần | 1. Seed fixture vào môi trường test; 2. kiểm độ phủ hai công thức có I2; 3. Đối chiếu response, bảng/audit và UI theo expected | 200; complete=1,total=2; missing ghi I2 và cả hai recipeId; không thay null bằng 0 | NOT RUN | — |
| TC-NUTR-006 | US-NUTR-002 / AC-NUTR-006 | FR-NUTR-REF-002 / BR-NUTR-002 | I1 có cả bốn chỉ số bằng 0 và nguồn đầy đủ | 1. Seed fixture vào môi trường test; 2. kiểm I1 rồi gửi lại khi thiếu đăng nhập; 3. Đối chiếu response, bảng/audit và UI theo expected | lần đầu complete=1; lần sau 401 ERR-NUTR-401-01; không trả dữ liệu | NOT RUN | — |
| TC-NUTR-007 | US-NUTR-003 / AC-NUTR-007 | FR-NUTR-CALC-001 / BR-NUTR-003 | fixture I1: qty=50g, edible=80%, kcal=100/P10/F2/C15 trên 100g; chỉ một dòng | 1. Seed fixture vào môi trường test; 2. tính món với công thức ACTIVE; 3. Đối chiếu response, bảng/audit và UI theo expected | totals=40.00 kcal,4.00g đạm,0.80g béo,6.00g carb; có nhãn ước tính từ định lượng sống | BLOCKED: NUTR-Q02 | — |
| TC-NUTR-008 | US-NUTR-003 / AC-NUTR-008 | FR-NUTR-CALC-001 / BR-NUTR-003 | công thức dùng 1 quả nhưng gramsPerUnit thiếu | 1. Seed fixture vào môi trường test; 2. tính món; 3. Đối chiếu response, bảng/audit và UI theo expected | 422 ERR-NUTR-422-02; totals=null; chỉ rõ nguyên liệu thiếu quy đổi, không trả tổng một phần | NOT RUN | — |
| TC-NUTR-009 | US-NUTR-003 / AC-NUTR-009 | FR-NUTR-CALC-001 / BR-NUTR-003 | qty=1 quả; gramsPerUnit=50; edible=80%; cùng thành phần I1 | 1. Seed fixture vào môi trường test; 2. tính rồi đổi COST_AP_HAO_HUT và tính lại; 3. Đối chiếu response, bảng/audit và UI theo expected | hai kết quả bằng nhau:40.00/4.00/0.80/6.00; không nhân hao hụt Cost | BLOCKED: NUTR-Q02 | — |
| TC-NUTR-010 | US-NUTR-004 / AC-NUTR-010 | FR-NUTR-CALC-002 / BR-NUTR-004 | suất thử yêu cầu 1 chính; chính A=40/4/0.8/6, B=80/8/1.6/12; phụ cố định=10/1/0.2/1.5 | 1. Seed fixture vào môi trường test; 2. chọn A và phụ rồi tính; 3. Đối chiếu response, bảng/audit và UI theo expected | 50.00 kcal,5.00g đạm,1.00g béo,7.50g carb; không cộng B; lưu danh sách món đã chọn | BLOCKED: NUTR-Q03 | — |
| TC-NUTR-011 | US-NUTR-004 / AC-NUTR-011 | FR-NUTR-CALC-002 / BR-NUTR-004 | suất cần 1 chính, người dùng chọn A và B | 1. Seed fixture vào môi trường test; 2. POST tổ hợp có 2 chính hoặc trùng itemId; 3. Đối chiếu response, bảng/audit và UI theo expected | 422 ERR-NUTR-422-03; không tính tổng | NOT RUN | — |
| TC-NUTR-012 | US-NUTR-004 / AC-NUTR-012 | FR-NUTR-CALC-002 / BR-NUTR-004 | đang xem menuVersion=2, một người sửa thành 3 | 1. Seed fixture vào môi trường test; 2. POST menuVersion=2 hoặc itemId thuộc cơ sở không có quyền; 3. Đối chiếu response, bảng/audit và UI theo expected | 409 ERR-NUTR-409-01 hoặc 404 ERR-NUTR-404-01 tương ứng; không lộ dữ liệu ngoài quyền | NOT RUN | — |
| TC-NUTR-013 | US-NUTR-005 / AC-NUTR-013 | FR-NUTR-SNAP-001 / BR-NUTR-005 | calculation C1 ghi I1 version=1; I1 đổi thành version=2 | 1. Seed fixture vào môi trường test; 2. GET C1; 3. Đối chiếu response, bảng/audit và UI theo expected | 200; giữ totals/source version=1; isStale=true; đề nghị tính lại | NOT RUN | — |
| TC-NUTR-014 | US-NUTR-005 / AC-NUTR-014 | FR-NUTR-SNAP-001 / BR-NUTR-005 | người dùng không có quyền cơ sở của C1 | 1. Seed fixture vào môi trường test; 2. GET C1; 3. Đối chiếu response, bảng/audit và UI theo expected | 404 ERR-NUTR-404-01; không trả totals hoặc nguồn | NOT RUN | — |
| TC-NUTR-015 | US-NUTR-005 / AC-NUTR-015 | FR-NUTR-SNAP-001 / BR-NUTR-005 | C1 và C2 là hai lần tính, clientRevision 1 và 2 | 1. Seed fixture vào môi trường test; 2. phản hồi C1 tới sau C2; 3. Đối chiếu response, bảng/audit và UI theo expected | UI giữ C2; lịch sử vẫn xem C1; cả hai có nhãn ước tính từ định lượng sống | NOT RUN | — |

## Kiểm lỗi hợp đồng bổ sung

| TC | Mã lỗi | Dữ liệu / thao tác | Expected | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| TC-NUTR-ERR-01 | ERR-NUTR-400-01 | Gọi endpoint thuộc điều kiện “JSON/kiểu/field lạ không hợp lệ”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 400, error.code đúng; thông báo “Yêu cầu chưa đúng định dạng.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-02 | ERR-NUTR-401-01 | Gọi endpoint thuộc điều kiện “Phiên không hợp lệ”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 401, error.code đúng; thông báo “Vui lòng đăng nhập lại.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-03 | ERR-NUTR-403-01 | Gọi endpoint thuộc điều kiện “Thiếu quyền thao tác”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 403, error.code đúng; thông báo “Bạn không có quyền thực hiện.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-04 | ERR-NUTR-404-01 | Gọi endpoint thuộc điều kiện “Không tồn tại hoặc ngoài scope”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 404, error.code đúng; thông báo “Không tìm thấy dữ liệu.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-05 | ERR-NUTR-409-01 | Gọi endpoint thuộc điều kiện “Version hoặc trạng thái nguồn đã đổi”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 409, error.code đúng; thông báo “Dữ liệu đã thay đổi.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-06 | ERR-NUTR-422-01 | Gọi endpoint thuộc điều kiện “Số âm/null, nguồn thiếu hoặc số vượt precision”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 422, error.code đúng; thông báo “Thành phần dinh dưỡng chưa hợp lệ.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-07 | ERR-NUTR-422-02 | Gọi endpoint thuộc điều kiện “Thiếu thành phần/quy đổi/recipe hiệu lực”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 422, error.code đúng; thông báo “Chưa đủ dữ liệu để tính.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-08 | ERR-NUTR-422-03 | Gọi endpoint thuộc điều kiện “Tổ hợp suất sai cấu trúc/trùng món”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 422, error.code đúng; thông báo “Tổ hợp món chưa hợp lệ.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |
| TC-NUTR-ERR-09 | ERR-NUTR-500-01 | Gọi endpoint thuộc điều kiện “Lỗi giao dịch nội bộ”; stub lỗi giao dịch/queue với 5xx; giữ requestId | HTTP 500, error.code đúng; thông báo “Chưa thể hoàn tất.”; không dữ liệu ngoài scope, không ghi một phần; kiểm response và DB/audit | NOT RUN |

## Kiểm NFR / nghiệm thu release

| TC | NFR | Bước / dữ liệu | Expected | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| TC-NUTR-NFR-01 | NFR-NUTR-001 | Chuẩn bị 30 món và 5 suất tính tay có nguồn; tính qua API; ghi chênh lệch bốn chỉ số | độ phủ 100%; đối soát theo dung sai được duyệt | BLOCKED: DATA-NUTR-Q01, NUTR-Q04 |
| TC-NUTR-NFR-02 | NFR-NUTR-002 | Chạy đọc/ghi/tính với 1000 người, đo p95 và tỷ lệ lỗi theo profile QA duyệt | mục tiêu SRS NFR-NUTR-002; báo cáo tính riêng, không trộn latency | BLOCKED: profile tải và môi trường |
| TC-NUTR-NFR-03 | NFR-NUTR-003 | Gọi trực tiếp id cơ sở khác; ngắt DB sau ghi current trước revision/audit | không lộ dữ liệu; rollback toàn bộ | NOT RUN |
| TC-NUTR-NFR-04 | NFR-NUTR-004 | Mở mọi màn ở 390/1440px, tab bàn phím; tạo kết quả thiếu và cũ | nhãn ước tính, đơn vị, trạng thái đầy đủ; focus thao tác được | NOT RUN |
