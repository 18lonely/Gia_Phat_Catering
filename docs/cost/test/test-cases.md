# Test case Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft để BA/QA/Tech lead review.

Nguồn: [SRS Cost](../srs/spec.md), [16 use case](../srs/usecase-diagram.md), [API đề xuất](../api/api-spec.md), [user flow](../ui/user-flow.md).

## Chuẩn bị và cách ghi kết quả

Chỉ chạy trên môi trường test có MENU/SYS/COST và dữ liệu cô lập. Reset fixture trước mỗi ca/biến thể; không dùng dữ liệu thật. Đặt ngày máy chủ test 11/11/2026 theo Asia/Ho_Chi_Minh cho ca giá; mô phỏng mốc hiệu lực khi ca yêu cầu. Tạo KT/DD/GD/QT/QL A/bếp A và hai service account đúng quyền SRS; tài khoản kiêm quyền chỉ dùng kiểm phân tách tạo/duyệt.

Mỗi ca: (1) chuẩn bị tiền điều kiện/fixture; (2) thực hiện các hành động theo thứ tự trong ô bước; (3) kiểm phản hồi, dữ liệu trước/sau, audit và quyền; (4) ghi actual, PASS/FAIL/BLOCKED, requestId, build, môi trường và bằng chứng. Các bước ghi database dùng quyền QA phù hợp ở môi trường test. Không sửa dữ liệu production. Ngày/tiền trong bảng là số mẫu, không phải cấu hình mặc định đã chốt.

Tất cả Actual và Evidence đang để “Chưa chạy”. NOT RUN nghĩa có expected theo thiết kế nhưng chưa chạy trên backend; BLOCKED nghĩa cần quyết định hoặc đầu vào/môi trường bổ sung. Không có test chức năng nào được báo PASS từ việc kiểm cấu trúc Markdown.

## US-COST-001: Danh mục nhà cung cấp

Ưu tiên P0; UC-COST-001; API: API-COST-001, API-COST-002, API-COST-003; FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003.

### TC-COST-001-01: Tạo, sửa và lọc NCC

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-001 / AC-COST-001-01 |
| Loại / nguồn | Functional; BR-PRC-001 |
| Tiền điều kiện và dữ liệu | KT có quyền ghi; chưa có NCC An Bình |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tạo An Bình loại REGULAR; sửa điện thoại; lọc tên An Bình, loại REGULAR và ACTIVE. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có đúng một NCC ACTIVE với điện thoại mới, lịch sử ghi người thao tác và nội dung thay đổi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-001-02: Tên trùng sau chuẩn hóa

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-001 / AC-COST-001-02 |
| Loại / nguồn | Functional; BR-PRC-001, BR-CAT-001, ERR-COST-409-01 |
| Tiền điều kiện và dữ liệu | đã có NCC An Bình chưa huỷ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tạo NCC có tên "  AN   BÌNH  ". 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | HTTP 409 ERR-COST-409-01; không thêm NCC |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-001-03: Ngừng không xóa giá cũ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-001 / AC-COST-001-03 |
| Loại / nguồn | Functional; BR-PRC-007, ERR-COST-422-02 |
| Tiền điều kiện và dữ liệu | NCC An Bình có giá tham chiếu 120000 ngày 10/11/2026 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. ngừng NCC với lý do "Không tiếp tục mua hàng"; tính giá tại 10/11; thử nhập giá mới. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | giá lịch sử vẫn dùng; giá mới bị từ chối; cảnh báo tham chiếu đang dùng được ghi nhận theo thiết kế Q03 |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q03) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-002: Nhập giá nguyên liệu

Ưu tiên P0; UC-COST-002; API: API-COST-005, API-COST-037; FR-COST-PRC-001.

### TC-COST-002-01: Giá đầu tiên

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-01 |
| Loại / nguồn | Functional; BR-PRC-002, BR-PRC-005 |
| Tiền điều kiện và dữ liệu | nguyên liệu I1 và NCC S1 ACTIVE; chưa có giá; ngày hệ thống 11/11/2026 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập I1/S1/A giá 120000 ngày 11/11. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tạo một dòng giá, tự đánh dấu tham chiếu, ghi audit; không có bước duyệt giá thứ hai trong thiết kế hiện tại |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-002-02: Giá không hợp lệ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-02 |
| Loại / nguồn | Functional; BR-PRC-002, ERR-COST-422-01 |
| Tiền điều kiện và dữ liệu | I1/S1 ACTIVE |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lần lượt nhập giá 0, -1, 1.5; mỗi lần dùng khóa yêu cầu mới. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | mỗi lần HTTP 422 ERR-COST-422-01; không tạo dòng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-002-03: Biên ngày và khóa trùng

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-03 |
| Loại / nguồn | Boundary; BR-PRC-003, BR-PRC-005, ERR-COST-422-02, ERR-COST-409-02 |
| Tiền điều kiện và dữ liệu | hôm nay 11/11/2026; hồi tố cấu hình 7 ngày |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập từng bản độc lập tại 04/11, 11/12 rồi tại 03/11, 12/12; gửi lại tuple I1/S1/A/ngày đã tồn tại bằng khóa mới. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | hai ngày biên hợp lệ; hai ngày ngoài biên trả ERR-COST-422-02; tuple trùng trả ERR-COST-409-02 |
| Trạng thái | BLOCKED (chờ E3-Q13) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-002-04: Tham chiếu không tồn tại

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-04 |
| Loại / nguồn | Functional; ERR-COST-404-01 |
| Tiền điều kiện và dữ liệu | không có nguyên liệu I999 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập giá cho I999 hoặc NCC không tồn tại. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | HTTP 404 ERR-COST-404-01; không tạo giá |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-002-05: Schema và trường do server quản lý

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-05 |
| Loại / nguồn | Contract; ERR-COST-400-01 |
| Tiền điều kiện và dữ liệu | KT có token hợp lệ; chưa có giá tuple định tạo |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi JSON thiếu priceVnd, enum sai, thêm createdBy hoặc totalCost client tự đặt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | 400 ERR-COST-400-01 theo hợp đồng đề xuất, details.path chỉ field sai; không ghi giá |
| Trạng thái | BLOCKED (review API) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-002-06: NCC inactive có hai mã lỗi trong SRS

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-002 / AC-COST-002-06 |
| Loại / nguồn | Contract; ERR-COST-404-01, ERR-COST-422-02 |
| Tiền điều kiện và dữ liệu | S1 tồn tại nhưng INACTIVE; I1 ACTIVE |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập giá cho S1. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không ghi giá; oracle mã lỗi BLOCKED vì ma trận404-01 nói tham chiếu không còn dùng,422-02 lại nói NCC ngừng; cần thống nhất trước nghiệm thu hợp đồng |
| Trạng thái | BLOCKED (QA-COST-Q01: BA/Tech lead thống nhất mã) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-003: Chọn và tra giá tham chiếu

Ưu tiên P0; UC-COST-002; API: API-COST-008, API-COST-010; FR-COST-PRC-002, FR-COST-PRC-003.

### TC-COST-003-01: Ưu tiên giá cơ sở

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-003 / AC-COST-003-01 |
| Loại / nguồn | Functional; BR-PRC-006, BR-COST-004 |
| Tiền điều kiện và dữ liệu | I1 có giá chung 100000 ngày 10/11 và giá A 120000 ngày 01/11; không có giá B |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tra I1 tại 11/11 cho A và B. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | A nhận 120000 dù giá chung mới hơn; B nhận 100000 kèm NCC/ngày giá |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-003-02: Không dùng giá tương lai

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-003 / AC-COST-003-02 |
| Loại / nguồn | Functional; BR-PRC-006, ERR-COST-404-02 |
| Tiền điều kiện và dữ liệu | I2 chỉ có giá hiệu lực 16/11 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tra I2 ngày 11/11. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | HTTP 404 ERR-COST-404-02; không dùng giá tương lai |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-003-03: Chuyển cờ trong cùng nhóm tương lai

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-003 / AC-COST-003-03 |
| Loại / nguồn | Boundary; BR-PRC-005 |
| Tiền điều kiện và dữ liệu | hai giá I1/A/16-11 thuộc hai NCC; chỉ giá thứ nhất tham chiếu |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chọn giá thứ hai làm tham chiếu; tra I1/A/16-11. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chỉ giá thứ hai còn cờ trong nhóm; giá nhóm ngày/cơ sở khác giữ nguyên; đổi cờ giá đã hiệu lực chờ quyết định riêng |
| Trạng thái | BLOCKED (chờ E3-Q4); E3-Q14 |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-004: Nhập lưới nguyên tử

Ưu tiên P0; UC-COST-003; API: API-COST-006, API-COST-037; FR-COST-PRC-004.

### TC-COST-004-01: Bỏ qua dòng không đổi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-004 / AC-COST-004-01 |
| Loại / nguồn | Functional; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | lưới có hai nguyên liệu; I1=100000, I2=20000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lọc nhóm/bảo quản/đang dùng; đổi I1 thành 110000, giữ I2; lưu ngày hợp lệ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tạo đúng một giá I1; I2 không thêm lịch sử |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-004-02: Một dòng sai rollback

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-004 / AC-COST-004-02 |
| Loại / nguồn | Functional; BR-PRC-002, ERR-COST-422-01 |
| Tiền điều kiện và dữ liệu | lô có I1 giá 110000 và I2 giá 0 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lưu lô; kiểm số giá trước/sau. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | báo ERR-COST-422-01 gắn dòng I2; không tạo giá I1 hoặc I2 |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-004-03: Mất phản hồi sau commit

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-004 / AC-COST-004-03 |
| Loại / nguồn | Integration; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | lô hợp lệ và key K; gateway làm mất phản hồi sau commit |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đối soát K rồi retry cùng key/body trong 24 giờ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | trả kết quả đã lưu; số dòng không tăng lần hai; không tạo key mới chỉ vì timeout |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-004-04: Hiệu năng lưới200 dòng

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-004 / AC-COST-004-04 |
| Loại / nguồn | Performance; NFR-COST-003 |
| Tiền điều kiện và dữ liệu | 200 tuple giá mới hợp lệ, không cần xác nhận biến động; ghi cấu hình môi trường |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi một lô200 dòng, đo từ gửi đến nhận xác nhận commit; đếm giá/audit. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | <=3giây và đủ200 dòng; thời gian và tính nguyên tử cùng đạt |
| Trạng thái | BLOCKED (môi trường backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-004-05: Key cùng body khác và đang xử lý

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-004 / AC-COST-004-05 |
| Loại / nguồn | Contract; ERR-COST-409-04, ERR-COST-409-05 |
| Tiền điều kiện và dữ liệu | request K đã commit; request L được giữ ở trạng thái xử lý trong test |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi K với giá khác; gửi đồng thời cùng L. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | K trả ERR-COST-409-04 không ghi; L trả ERR-COST-409-05 kèm Retry-After; đối soát sau hoàn tất chỉ một kết quả |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-005: Nhập XLSX giá

Ưu tiên P0; UC-COST-004; API: API-COST-012, API-COST-013, API-COST-014; FR-COST-PRC-005.

### TC-COST-005-01: Đọc đúng tên cột

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-005 / AC-COST-005-01 |
| Loại / nguồn | Functional; BR-CAT-023 |
| Tiền điều kiện và dữ liệu | mẫu giá XLSX không mật khẩu, hai dòng hợp lệ; đổi thứ tự cột, thêm cột Ghi chú lạ, dòng trắng |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm tệp; xác nhận nhập. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | kiểm không ghi; bỏ dòng trắng và cảnh báo cột lạ; xác nhận mới tạo hai dòng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-005-02: Tệp lỗi không ghi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-005 / AC-COST-005-02 |
| Loại / nguồn | Functional; BR-CAT-023, ERR-MENU-422-20 |
| Tiền điều kiện và dữ liệu | tệp thiếu cột bắt buộc hoặc giá dòng 2 bằng 0 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm và thử xác nhận tệp chưa đạt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-MENU-422-20, lỗi có dòng/cột; không tạo giá |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-005-03: Giới hạn dòng và đọc số

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-005 / AC-COST-005-03 |
| Loại / nguồn | Boundary; BR-CAT-023, ERR-MENU-422-20 |
| Tiền điều kiện và dữ liệu | hai tệp mẫu có 2000 và 2001 dòng hợp lệ; số văn bản "120000"; tệp phụ có "120,000" |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm từng tệp; không xác nhận nhập. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | 2000 dòng được kiểm; 2001 trả ERR-MENU-422-20; số nguyên văn bản được đọc; "120,000" là thập phân 120, không được hiểu là 120000 |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-005-04: Import đã kiểm bị đổi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-005 / AC-COST-005-04 |
| Loại / nguồn | Contract; ERR-COST-409-07 |
| Tiền điều kiện và dữ liệu | đã kiểm tệp và có token; thay bytes tệp hoặc dùng token hết hạn |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. commit token cũ với tệp mới. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-409-07; không nhập một dòng nào; phải kiểm lại |
| Trạng thái | BLOCKED (review API) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-005-05: Số dạng văn bản và trang tính

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-005 / AC-COST-005-05 |
| Loại / nguồn | Boundary; BR-CAT-023 |
| Tiền điều kiện và dữ liệu | mẫu đúng trang; giá văn bản120000.0 và120000,0; trang khác có dữ liệu; file khác đặt mật khẩu |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm từng tệp không commit. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | hai dạng số bằng120000 được đọc; bỏ trang khác kèm cảnh báo; tệp mật khẩu bị từ chối không ghi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-006: Lịch sử và hủy giá tương lai

Ưu tiên P0; UC-COST-002,005; API: API-COST-004, API-COST-009; FR-COST-PRC-006, FR-COST-PRC-007.

### TC-COST-006-01: Hủy giá tương lai độc lập

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-006 / AC-COST-006-01 |
| Loại / nguồn | Functional; BR-PRC-004, BR-AUD-001 |
| Tiền điều kiện và dữ liệu | giá I1/A/16-11 là dòng duy nhất của ngày; hôm nay 11/11 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xem lịch sử rồi hủy với lý do từ 10 ký tự. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | dòng được đánh dấu hủy, giữ audit, không còn được chọn khi tra giá; các dòng cũ giữ nguyên |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-006-02: Giá đã hiệu lực

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-006 / AC-COST-006-02 |
| Loại / nguồn | Functional; BR-PRC-004, ERR-COST-409-03 |
| Tiền điều kiện và dữ liệu | giá ngày 10/11 và ngày 11/11; hôm nay 11/11 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. thử sửa hoặc hủy từng giá. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | HTTP 409 ERR-COST-409-03; dữ liệu và cờ tham chiếu không bị đổi ngầm |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-006-03: Phạm vi lịch sử

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-006 / AC-COST-006-03 |
| Loại / nguồn | Security; ERR-SYS-404-01 |
| Tiền điều kiện và dữ liệu | QL chỉ thuộc A; tồn tại giá riêng B |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi trực tiếp chi tiết giá B bằng ID và lọc lịch sử B. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-SYS-404-01 cho tài nguyên ngoài phạm vi; không lộ giá B |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-007: Theo dõi giá thiếu và giá cũ

Ưu tiên P0; UC-COST-005; API: API-COST-011; FR-COST-PRC-008, FR-COST-PRC-009.

### TC-COST-007-01: Thiếu giá theo cơ sở

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-007 / AC-COST-007-01 |
| Loại / nguồn | Functional; BR-PRC-006 |
| Tiền điều kiện và dữ liệu | I1 dùng ở hai công thức ACTIVE; chỉ có giá riêng A |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tra danh sách thiếu giá B và A. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | B có I1, số món ảnh hưởng 2; A không liệt kê I1; không lấy giá riêng A cho B |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-007-02: Chạy lại không nhân cảnh báo

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-007 / AC-COST-007-02 |
| Loại / nguồn | Functional; BR-PRC-008, BR-COST-005 |
| Tiền điều kiện và dữ liệu | I1 tươi có giá 8 ngày tuổi; ngưỡng 7 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chạy worker giá cũ hai lần cùng ngày. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | một cảnh báo đang mở cho I1 gửi KT; lần hai không tạo cảnh báo mở thứ hai |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q03) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-007-03: Biên tuổi giá

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-007 / AC-COST-007-03 |
| Loại / nguồn | Boundary; BR-PRC-008, BR-COST-005 |
| Tiền điều kiện và dữ liệu | tươi có giá 7/8 ngày tuổi; khô và đông lạnh có giá 30/31 ngày tuổi; cấu hình 7/30 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chạy kiểm tuổi giá. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | 7 và 30 chưa cảnh báo; 8 và 31 cảnh báo; nguyên liệu ngoài công thức ACTIVE không bị đưa vào tập kiểm |
| Trạng thái | BLOCKED (chờ DL-01) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-008: Xác nhận biến động giá

Ưu tiên P1; UC-COST-002; API: API-COST-005, API-COST-006, API-COST-007; FR-COST-PRC-010.

### TC-COST-008-01: Xác nhận rồi lưu

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-008 / AC-COST-008-01 |
| Loại / nguồn | Functional; BR-PRC-009 |
| Tiền điều kiện và dữ liệu | giá trước 100000; ngưỡng lệch 30% |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập 131000; xác nhận cảnh báo. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | trước xác nhận chưa có dòng mới; sau xác nhận tạo đúng một dòng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-008-02: Hủy xác nhận

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-008 / AC-COST-008-02 |
| Loại / nguồn | Functional; BR-PRC-009 |
| Tiền điều kiện và dữ liệu | giá trước 100000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. nhập 69000; chọn hủy cảnh báo. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không tạo dòng giá; có thể sửa dữ liệu nhập |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-008-03: Đúng ngưỡng và giá đầu tiên

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-008 / AC-COST-008-03 |
| Loại / nguồn | Boundary; BR-PRC-009 |
| Tiền điều kiện và dữ liệu | giá trước 100000; ngưỡng 30%; I2 chưa có giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. thử giá 130000, 70000 ở các fixture độc lập; nhập giá đầu I2. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | đúng 30% không hỏi vì quy tắc là vượt 30%; I2 không có cơ sở so sánh nên không hỏi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-008-04: Token xác nhận stale

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-008 / AC-COST-008-04 |
| Loại / nguồn | Contract; ERR-COST-409-06 |
| Tiền điều kiện và dữ liệu | giá nền100000, đã cấp token cho giá131000; sau đó giá nền thay hoặc token hết hạn |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xác nhận giá131000 bằng token cũ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-409-06; không ghi, yêu cầu kiểm lại dựa trên giá nền mới |
| Trạng thái | BLOCKED (review API) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-009: Chứng từ giá

Ưu tiên P1; UC-COST-002; API: API-COST-005, API-COST-006; FR-COST-PRC-011.

### TC-COST-009-01: Gắn PDF hợp lệ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-009 / AC-COST-009-01 |
| Loại / nguồn | Functional; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | KT có quyền và PDF thật 1 MB |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. upload rồi gắn vào giá hoặc một lô; mở bằng quyền hợp lệ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | truy lại cùng chứng từ; URL nội bộ có chữ ký hết hạn 15 phút |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-009-02: Sai nội dung và quá dung lượng

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-009 / AC-COST-009-02 |
| Loại / nguồn | Functional; ERR-SYS-415-01, ERR-SYS-413-01 |
| Tiền điều kiện và dữ liệu | tệp executable đổi đuôi .pdf; PDF lớn hơn 10 MB |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. upload từng tệp. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tệp giả trả ERR-SYS-415-01; tệp quá cỡ trả ERR-SYS-413-01; không tạo liên kết chứng từ |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-009-03: Thu hồi quyền và URL hết hạn

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-009 / AC-COST-009-03 |
| Loại / nguồn | Security; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | chứng từ giá thuộc B; QL thuộc A; URL đã hết hạn |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. thử tải bằng QL A; thử tải URL hết hạn. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không trả bytes chứng từ; không rò qua URL tải hoặc thông báo lỗi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-010: Cost món và bảng phân rã

Ưu tiên P0; UC-COST-006; API: API-COST-015; FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004.

### TC-COST-010-01: Tính chính xác theo đơn vị

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-01 |
| Loại / nguồn | Functional; BR-CALC-001, BR-CALC-002, BR-CALC-006 |
| Tiền điều kiện và dữ liệu | thịt 70g giá 120000/kg hệ số1000; trứng 3 quả giá800; hao hụt KHONG; cả hai tính cost |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính món và mở picker tại cùng ngày/cơ sở. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | cost 10800; dòng thịt 8400, trứng 2400; có NCC/ngày giá/đơn vị/tỷ trọng; picker cùng ngày khớp 10800 |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-02: Không trả tổng thiếu

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-02 |
| Loại / nguồn | Functional; BR-CALC-002, BR-CALC-003, ERR-COST-422-03 |
| Tiền điều kiện và dữ liệu | thịt cần tính cost nhưng không có giá; trứng vẫn có giá; nước không tính cost và không có giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính món. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-03 liệt kê thịt, không liệt kê nước; không trả 2400 như cost toàn món |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-03: Công thức theo ngày và quyền

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-03 |
| Loại / nguồn | Security; BR-CALC-001, BR-CAT-014 |
| Tiền điều kiện và dữ liệu | R1 hiệu lực10/11 thịt70g; R2 hiệu lực16/11 thịt80g; giá120000; có thêm công thức đã gắn vào MENU PENDING |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính món tại15/11,16/11; kiểm MENU PENDING; gọi picker bằng người thiếu cost.cost.read. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chọn R1 rồi R2 theo ngày; MENU PENDING giữ công thức gắn; picker của người thiếu quyền không có trường tiền |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-04: Món không tồn tại

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-04 |
| Loại / nguồn | Functional; ERR-MENU-404-01 |
| Tiền điều kiện và dữ liệu | không có mã món M999 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính M999. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-MENU-404-01; không trả kết quả số |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-05: Hao hụt đúng một lần

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-05 |
| Loại / nguồn | Boundary; BR-EST-002 |
| Tiền điều kiện và dữ liệu | thịt70g, giá120000/kg, hao hụt20%, chế độ CO |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính cost một suất; lập dự toán10 suất chỉ có món này không khoản khoán. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | cost thịt10500; lượng mua0.88kg sau làm tròn lên từ0.875; thành tiền105600; không chia hao hụt lần hai |
| Trạng thái | BLOCKED (chờ E3-Q2) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-06: Đối soát bộ kế toán

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-06 |
| Loại / nguồn | Accuracy; NFR-COST-002 |
| Tiền điều kiện và dữ liệu | kế toán cung cấp10 món và10 ngày đã ký xác nhận; cấu hình VAT/phương pháp ghi kèm |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính lặp từng bộ bằng decimal, so bảng tay và lần tính trước. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | sai lệch cost món<=1đ, cost%<=0.01 điểm phần trăm; lặp cùng đầu vào có cùng kết quả; lưu bảng actual/expected |
| Trạng thái | BLOCKED (chờ O-01); dữ liệu kế toán |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-07: Decimal và không làm tròn trung gian

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-07 |
| Loại / nguồn | Accuracy; NFR-COST-008, BR-CALC-006 |
| Tiền điều kiện và dữ liệu | fixture0.1+0.2 đơn vị dùng; giá1đ/đơn vị; fixture có ba dòng cost0.4đ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. rà kiểu dữ liệu engine và tính hai fixture. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tổng chính xác0.3; tổng ba dòng1.2 hiển thị1đ, không làm tròn từng dòng thành0; không dùng float cho tiền/định lượng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-010-08: Tổng cost0 không chia cho0

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-010 / AC-COST-010-08 |
| Loại / nguồn | Boundary; BR-CALC-002 |
| Tiền điều kiện và dữ liệu | mọi nguyên liệu món có cờ không tính cost |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính món và xem tỷ trọng từng dòng. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tổng cost0; cách biểu diễn tỷ trọng chờ Q04; không NaN/Infinity và không suy ra giá nhập0 |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q04) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-011: So sánh công thức

Ưu tiên P1; UC-COST-006; API: API-COST-016; FR-COST-DISH-005.

### TC-COST-011-01: So sánh cùng ngày

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-011 / AC-COST-011-01 |
| Loại / nguồn | Functional; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | R1 cost10000, R2 cost11000 tại cùng D/A |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. so sánh R1 và R2. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chênh1000 và10%; không ghi giá hay tự duyệt công thức |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-011-02: Một bản thiếu giá

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-011 / AC-COST-011-02 |
| Loại / nguồn | Functional; ERR-COST-422-03 |
| Tiền điều kiện và dữ liệu | R2 có nguyên liệu chưa có giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. so sánh R1/R2. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-03; không suy diễn R2 bằng0 và không trả delta sai |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-011-03: Cost gốc bằng0

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-011 / AC-COST-011-03 |
| Loại / nguồn | Boundary; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | R1 có mọi nguyên liệu không tính cost; R2 cost1000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. so sánh hai bản. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | delta tiền1000; cách hiển thị delta% phải theo quyết định Q04; không trả Infinity/NaN |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q04) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-012: Lập bảng món đặc thù

Ưu tiên P0; UC-COST-007; API: API-COST-018, API-COST-019, API-COST-020; FR-COST-DISH-006.

### TC-COST-012-01: Chụp bản pending

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-012 / AC-COST-012-01 |
| Loại / nguồn | Functional; BR-CALC-010 |
| Tiền điều kiện và dữ liệu | món đặc thù M1 đủ giá tại A/D |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập bảng có ghi chú và gửi. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | bảng PENDING giữ công thức, giá, cơ sở, ngày tính và người lập; thay giá sau đó không sửa nội dung chụp |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-012-02: Sai loại món

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-012 / AC-COST-012-02 |
| Loại / nguồn | Functional; ERR-COST-422-04 |
| Tiền điều kiện và dữ liệu | M2 không có cờ đặc thù |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập bảng đặc thù cho M2. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-04; không tạo bảng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-012-03: Thiếu một giá

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-012 / AC-COST-012-03 |
| Loại / nguồn | Functional; BR-CALC-003, ERR-COST-422-03 |
| Tiền điều kiện và dữ liệu | M1 đặc thù thiếu giá thịt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi bảng M1. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-03, danh sách thiếu; không tạo bản chụp thiếu rồi coi là đủ |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-013: Duyệt bảng món đặc thù

Ưu tiên P0; UC-COST-007; API: API-COST-018, API-COST-019, API-COST-021; FR-COST-DISH-007.

### TC-COST-013-01: Duyệt bởi người khác

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-013 / AC-COST-013-01 |
| Loại / nguồn | Functional; BR-SEC-008, BR-CALC-010 |
| Tiền điều kiện và dữ liệu | bảng PENDING do DD1 tạo/sửa; GD1 khác DD1 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. GD1 duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | APPROVED, có audit quyết định; dữ liệu chụp không bị tính lại |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-013-02: Không tự duyệt hoặc thiếu lý do

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-013 / AC-COST-013-02 |
| Loại / nguồn | Functional; BR-SEC-008, ERR-SYS-403-01, ERR-SYS-422-01 |
| Tiền điều kiện và dữ liệu | người có quyền duyệt đồng thời là người tạo hoặc người sửa cuối của bảng; bảng khác do người khác tạo |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tự duyệt bảng đầu; trả lại bảng thứ hai với lý do9 ký tự rồi10 ký tự. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | tự duyệt trả ERR-SYS-403-01; lý do9 trả ERR-SYS-422-01; lý do10 cho trả lại, giữ bản chụp |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-013-03: Hiệu lực và cơ sở

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-013 / AC-COST-013-03 |
| Loại / nguồn | Boundary; BR-CALC-007, BR-COST-007 |
| Tiền điều kiện và dữ liệu | bảng M1 được duyệt ở A; ngày lập và ngày tính khác nhau; thời hạn cấu hình90 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm điều kiện M1 ở mốc89/90/91 ngày và cơ sở B. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ghi nhận kết quả theo bộ lọc được chốt ở E3-Q16 trước khi chạy; không tự coi bảng A dùng được ở B |
| Trạng thái | BLOCKED (chờ E3-Q16) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-013-04: Hai quyết định cạnh tranh

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-013 / AC-COST-013-04 |
| Loại / nguồn | Contract; ERR-SYS-409-02, ERR-COST-409-07 |
| Tiền điều kiện và dữ liệu | cùng bảng PENDING v1; hai người có quyền duyệt khác người tạo/sửa |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. người1 duyệt v1; người2 gửi trả lại v1 với khóa mới. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chỉ một quyết định được commit; version cũ ERR-SYS-409-02; nếu tải version mới nhưng trạng thái đã duyệt thì ERR-COST-409-07; không ghi đè quyết định trước |
| Trạng thái | BLOCKED (review API và concurrency token) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-014: Gợi ý nhóm cost

Ưu tiên P1; UC-COST-006; API: API-COST-017; FR-COST-DISH-008.

### TC-COST-014-01: Gợi ý không tự ghi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-014 / AC-COST-014-01 |
| Loại / nguồn | Functional; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | ngưỡng phân nhóm đã được duyệt trong fixture và món đủ giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. yêu cầu gợi ý. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | trả nhóm theo ngưỡng; nhóm đang lưu không đổi cho tới thao tác quyết định của người dùng |
| Trạng thái | BLOCKED (chờ E3-Q7) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-014-02: Thiếu giá không phân nhóm

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-014 / AC-COST-014-02 |
| Loại / nguồn | Functional; BR-CALC-003 |
| Tiền điều kiện và dữ liệu | món có nguyên liệu thiếu giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. yêu cầu gợi ý. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không đưa nhóm thấp do coi giá thiếu là0; trả chưa tính được |
| Trạng thái | BLOCKED (chờ E3-Q7) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-014-03: Biên phân nhóm

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-014 / AC-COST-014-03 |
| Loại / nguồn | Boundary; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | có quyết định E3-Q7 về ngưỡng và dấu so sánh |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. thử cost dưới, đúng, trên ngưỡng một đồng. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | nhóm khớp quyết định được duyệt; chưa điền ngưỡng tự đặt vào production |
| Trạng thái | BLOCKED (chờ E3-Q7) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-015: Cost ngày trên thực đơn

Ưu tiên P0; UC-COST-009; API: API-COST-025; FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003.

### TC-COST-015-01: Ngày đủ món

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-01 |
| Loại / nguồn | Functional; BR-CALC-005, BR-CALC-006, BR-COST-002, BR-COST-003 |
| Tiền điều kiện và dữ liệu | fixture giá suất40000 VAT8%, phần chính10800, phụ/rau/canh6500, khoán1500; ngưỡng52 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính cost ngày và mở phân rã. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | cost18800; doanh thu chưa VAT=40000/1.08, cost50.76%, đạt; dư hiển thị459đ; có từng phần và cách tính |
| Trạng thái | BLOCKED (chờ O-01); E2-Q1 |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-015-02: VAT thiếu hoặc mẫu số0

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-02 |
| Loại / nguồn | Functional; BR-CALC-005, ERR-COST-422-05 |
| Tiền điều kiện và dữ liệu | fixture không đặt VAT; fixture khác giá suất0 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính từng ngày. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-05; không mặc định VAT0 hay trả cost%0 |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-015-03: Làm tròn rồi so ngưỡng

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-03 |
| Loại / nguồn | Boundary; BR-CALC-006, BR-COST-001 |
| Tiền điều kiện và dữ liệu | fixture VAT0, giá suất100000, ngưỡng52; cost52004 và52005 ở hai lần độc lập |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính cost% và kiểm ngưỡng. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | 52.004% làm tròn52.00 đạt;52.005% làm tròn52.01 vượt; trung gian không làm tròn |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-015-04: Ba phương pháp món chính

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-04 |
| Loại / nguồn | Functional; BR-CALC-004 |
| Tiền điều kiện và dữ liệu | các món chính gồm Healthy có cost8000,10000,12000; K=2; món mặc định10000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính từng cấu hình DAT_NHAT, BINH_QUAN, MAC_DINH. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | phần chính lần lượt24000,20000,20000; không bỏ Healthy khỏi trung bình |
| Trạng thái | BLOCKED (chờ E3-Q1); E3-Q12 |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-015-05: Ngày chưa đủ món và phản hồi cũ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-05 |
| Loại / nguồn | Integration; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | ngày mới có món chính; hai lượt sửa có revision1 và2 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tính phần có; trả phản hồi revision1 sau revision2. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | hiện chưa đủ món, không gắn nhãn đạt cho ngày hoàn chỉnh; không ghi đè kết quả revision2 bằng revision1 |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-015-06: Hiệu năng tính thực đơn

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-015 / AC-COST-015-06 |
| Loại / nguồn | Performance; NFR-COST-001 |
| Tiền điều kiện và dữ liệu | fixture6 ngày x7 món, đủ giá; ghi môi trường, cơ sở, cache và cấu hình |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chạy50 lần đo API cost và bộ kiểm đầy đủ, lưu từng mẫu; p95 theo thứ tự mẫu thứ48. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | p95 Cost<=1s; tổng bộ kiểm theo NFR-MENU-001<=2s; không tính thời gian render wireframe |
| Trạng thái | BLOCKED (môi trường backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-016: Khoản khoán

Ưu tiên P0; UC-COST-008; API: API-COST-022, API-COST-023, API-COST-024; FR-COST-MEAL-004.

### TC-COST-016-01: Ưu tiên riêng thay chung

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-016 / AC-COST-016-01 |
| Loại / nguồn | Functional; BR-CALC-008, BR-SEC-008 |
| Tiền điều kiện và dữ liệu | khoản Gia vị chung1000 đã duyệt; đề nghị riêng suất40K1500 ngày16/11 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. người khác duyệt đề nghị; tính ngày15/11 và16/11 cho suất40K. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ngày15 dùng1000; ngày16 dùng1500 thay vì2500; không áp PENDING |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-016-02: Khoản sai không nhận

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-016 / AC-COST-016-02 |
| Loại / nguồn | Functional; BR-CALC-008, ERR-COST-422-06 |
| Tiền điều kiện và dữ liệu | KT có quyền |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi khoản -1,1.5 hoặc thiếu ngày hiệu lực. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | mỗi đầu vào trả ERR-COST-422-06; không tạo đề nghị |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-016-03: Số0 và người đề nghị

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-016 / AC-COST-016-03 |
| Loại / nguồn | Boundary; BR-CALC-008, BR-SEC-008, ERR-SYS-403-01 |
| Tiền điều kiện và dữ liệu | khoản giá0 ngày hợp lệ lý do đủ; người tạo có cả quyền duyệt trong fixture |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi đề nghị0 rồi tự duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | đề nghị0 hợp lệ, tự duyệt ERR-SYS-403-01; giá0 của khoản không bị nhầm với giá nguyên liệu |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-016-04: Khoản trùng khi duyệt

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-016 / AC-COST-016-04 |
| Loại / nguồn | Contract; ERR-COST-409-08 |
| Tiền điều kiện và dữ liệu | đã có Gia vị/ALL/16-11 APPROVED; có đề nghị khác cùng tuple sau chuẩn hóa tên |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. duyệt đề nghị thứ hai. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-409-08; không tạo hai khoản cùng tên/phạm vi/ngày hiệu lực |
| Trạng thái | BLOCKED (review API) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-017: Cổng gửi duyệt

Ưu tiên P0; UC-COST-010; API: hook nội bộ/SYS; FR-COST-MEAL-005.

### TC-COST-017-01: Mọi cơ sở đều đạt

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-017 / AC-COST-017-01 |
| Loại / nguồn | Functional; BR-CALC-009 |
| Tiền điều kiện và dữ liệu | thực đơn đủ món, đủ giá/VAT, bảng đặc thù còn hiệu lực; A/B cùng dưới ngưỡng |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi duyệt ở chế độ CHAN. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | Cost cho qua; MENU tiếp tục các điều kiện khác, không tự coi toàn bộ MENU đã được duyệt |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-017-02: Một cơ sở vượt

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-017 / AC-COST-017-02 |
| Loại / nguồn | Functional; BR-CALC-009, BR-COST-001, ERR-COST-422-07 |
| Tiền điều kiện và dữ liệu | A cost50%, B cost54%, ngưỡng52; CHAN |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi duyệt thực đơn chung A/B và thử bỏ B khỏi request. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-07; không PENDING; server vẫn kiểm đủ cơ sở và trả chi tiết theo quyền |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-017-03: Cảnh báo không bỏ qua dữ liệu thiếu

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-017 / AC-COST-017-03 |
| Loại / nguồn | Boundary; BR-CALC-003, BR-CALC-007, ERR-COST-422-03, ERR-COST-422-04, ERR-COST-422-05 |
| Tiền điều kiện và dữ liệu | CANH_BAO; lần1 đủ giá cost54%; lần2 thiếu giá; lần3 đặc thù thiếu bảng; lần4 thiếu VAT |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gửi duyệt từng fixture. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | lần1 Cost chỉ cảnh báo; lần2/3/4 vẫn chặn với ERR-COST-422-03/04/05 tương ứng; không có nút ngoại lệ CHAN |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-018: Snapshot lúc duyệt

Ưu tiên P0; UC-COST-010; API: API-COST-026; FR-COST-MEAL-006.

### TC-COST-018-01: Chụp từng ngày/cơ sở

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-018 / AC-COST-018-01 |
| Loại / nguồn | Functional; BR-CALC-010 |
| Tiền điều kiện và dữ liệu | MENU PENDING đủ điều kiện, không có thay đổi đầu vào từ lần kiểm; 6 ngày,2 cơ sở |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. duyệt thành APPROVED. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có12 snapshot cho vòng duyệt, chứa giá/nguồn/ngày/params; ghi APPROVED và snapshot cùng giao dịch đề xuất |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-018-02: Giá đổi trong lúc chờ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-018 / AC-COST-018-02 |
| Loại / nguồn | Functional; BR-CALC-010 |
| Tiền điều kiện và dữ liệu | MENU PENDING đã kiểm bằng giá cũ; giá mới có hiệu lực trước khi duyệt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. duyệt thực đơn. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chưa xác định oracle số liệu chụp đến khi Q06 chốt chính sách kiểm lại; ca phải BLOCKED, không mặc nhiên chụp kết quả cũ hoặc mới |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q06) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-018-03: Bất biến và rollback

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-018 / AC-COST-018-03 |
| Loại / nguồn | Integration; BR-CALC-010 |
| Tiền điều kiện và dữ liệu | đã có snapshot vòng1; fixture khác cố ý gây lỗi khi lưu snapshot trước commit |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đổi giá/công thức/params rồi đọc vòng1; thử duyệt fixture lỗi. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | vòng1 không đổi; giao dịch lỗi không để APPROVED thiếu snapshot; retry đối soát không tạo trùng vòng |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-019: Chế độ kiểm Cost

Ưu tiên P0; UC-COST-011; API: hook nội bộ/SYS; FR-COST-MEAL-008.

### TC-COST-019-01: Duyệt thay đổi SYS

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-019 / AC-COST-019-01 |
| Loại / nguồn | Functional; BR-SYS-002, BR-SEC-008 |
| Tiền điều kiện và dữ liệu | CANH_BAO hiện hành; QT đề nghị CHAN hiệu lực hôm nay |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. GD khác người tạo duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | trước duyệt vẫn CANH_BAO; sau duyệt CHAN áp dụng từ ngày hiệu lực |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-019-02: Tự duyệt bị cấm

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-019 / AC-COST-019-02 |
| Loại / nguồn | Functional; BR-SEC-008, ERR-SYS-403-01 |
| Tiền điều kiện và dữ liệu | người đề nghị cũng có quyền duyệt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tự duyệt đề nghị hoặc người sửa cuối duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-SYS-403-01; tham số không thay |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-019-03: Hiệu lực tương lai

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-019 / AC-COST-019-03 |
| Loại / nguồn | Boundary; BR-SYS-002, BR-CALC-010 |
| Tiền điều kiện và dữ liệu | CHAN đã duyệt hiệu lực16/11, hiện11/11 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm ngày trước và đúng thời điểm có hiệu lực theo SYS. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | trước hiệu lực giữ chế độ cũ; tới hiệu lực áp CHAN; bản chụp quá khứ không đổi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-020: Bộ kiểm và ẩn con số

Ưu tiên P0; UC-COST-009; API: API-COST-025; FR-COST-RUL-001, FR-COST-RUL-002.

### TC-COST-020-01: Đăng ký đúng quy tắc

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-020 / AC-COST-020-01 |
| Loại / nguồn | Functional; BR-COST-001, BR-COST-005, BR-COST-006, BR-COST-007 |
| Tiền điều kiện và dữ liệu | fixture có ngày vượt, giá cũ, cặp chính/phụ cost cao, đặc thù thiếu bảng |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chạy bộ kiểm tích hợp MENU. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có kết quả BR-COST-001/005/006/007 theo loại cấu hình; không đăng ký002/003/004 thành lỗi kiểm độc lập |
| Trạng thái | BLOCKED (chờ DL-01); E3-Q7 |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-020-02: Không lộ tiền trong lỗi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-020 / AC-COST-020-02 |
| Loại / nguồn | Security; ERR-COST-422-07 |
| Tiền điều kiện và dữ liệu | tài khoản có quyền kiểm MENU nhưng thiếu cost.cost.read |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm ngày vượt và gửi duyệt ở CHAN; đọc JSON/network và UI. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chỉ nhãn đạt/không đạt; ERR-COST-422-07 được rút gọn, không cost%, tiền, breakdown trong details |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-020-03: Quyền thay đổi và agent nội bộ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-020 / AC-COST-020-03 |
| Loại / nguồn | Security; BR-SEC-009 |
| Tiền điều kiện và dữ liệu | agent nội bộ thay QL A; quyền cost bị thu hồi giữa hai yêu cầu |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi cost B rồi lặp yêu cầu A sau thu hồi. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không trả dữ liệu B; quyền hiệu lực là giao quyền dịch vụ/người; yêu cầu kế tiếp không replay dữ liệu đã mất quyền |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-020-04: Hồi quy quy tắc đã thuộc MENU

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-020 / AC-COST-020-04 |
| Loại / nguồn | Integration; BR-COST-008, BR-COST-009, BR-COST-010, BR-COST-012 |
| Tiền điều kiện và dữ liệu | fixture chuẩn min70/max80g; phụ tối đa50g; nguyên liệu có xương chưa khai hao hụt; định mức40000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lưu công thức chính69g và81g, phụ51g; lưu nguyên liệu thiếu hao hụt; chọn món tổng40001. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | MENU chặn theo BR-COST-008/009/010/012; Cost không thay thế kiểm này; ngưỡng min/max/phụ là fixture chờ E2-Q5 |
| Trạng thái | BLOCKED (chờ E2-Q5) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-021: Ngân sách cho agent phía khách

Ưu tiên P0; UC-COST-015; API: API-COST-036; FR-COST-RUL-003.

### TC-COST-021-01: Chỉ một trạng thái

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-01 |
| Loại / nguồn | Functional; BR-CALC-011, BR-SEC-010 |
| Tiền điều kiện và dữ liệu | phiên còn quota; thực đơn hợp lệ mọi ngày đều đạt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi budget-check. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | chỉ result DAT; không ngày vượt, ngưỡng, cost, giá, snapshot trong body hoặc log |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-02: Thực đơn lỗi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-02 |
| Loại / nguồn | Functional; ERR-MENU-422-14 |
| Tiền điều kiện và dữ liệu | payload chứa món INACTIVE hoặc lặp món trong ngày |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi budget-check. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-MENU-422-14; không trả dữ liệu tiền trong lỗi |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-03: Quota lời gọi31

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-03 |
| Loại / nguồn | Boundary; ERR-COST-429-01 |
| Tiền điều kiện và dữ liệu | một phiên đã có29 lời gọi; payload hợp lệ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi lần30 rồi31, thử đổi key yêu cầu trong cùng phiên. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | lần30 xử lý; lần31 ERR-COST-429-01, không có con số; key mới không reset quota |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-04: Thiếu giá và trạng thái hỗn hợp

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-04 |
| Loại / nguồn | Functional; BR-CALC-011 |
| Tiền điều kiện và dữ liệu | fixture1 tất cả xác định và một ngày vượt; fixture2 thiếu giá nhưng không có ngày vượt; fixture3 vừa vượt vừa thiếu |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi từng fixture. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | fixture1 KHONG_DAT; fixture2 KHONG_XAC_DINH; fixture3 BLOCKED chờ ưu tiên Q09, không tự chốt |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q09) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-05: Không rò dữ liệu toàn API

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-05 |
| Loại / nguồn | Security; NFR-COST-005 |
| Tiền điều kiện và dữ liệu | bốn tài khoản: bếp A, người nội bộ không quyền giá/cost, svc khách, QL A truy B; danh mục MENU/COST |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi success/error/list/detail/export/replay với từng tài khoản; kiểm JSON, file và cache. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không con số hoặc trường giá/cost ngoài quyền trong mọi đường phản hồi; ghi endpoint x actor x outcome |
| Trạng thái | BLOCKED (chờ E3-Q11) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-06: Quyền DB agent khách

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-06 |
| Loại / nguồn | Security; NFR-COST-006, BR-SEC-010 |
| Tiền điều kiện và dữ liệu | tài khoản DB thật dùng cho agent khách; danh mục15 bảng Cost từ DBML |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kiểm grants rồi SELECT từng bảng Cost gồm bảng snapshot/allowance/alert mới; kiểm service không dùng tài khoản quyền cao để lách. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | mọi SELECT trực tiếp bị từ chối; không chỉ kiểm4 bảng cũ |
| Trạng thái | BLOCKED (môi trường backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-021-07: Log budget không chứa số

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-021 / AC-COST-021-07 |
| Loại / nguồn | Security; NFR-COST-007, BR-SEC-010 |
| Tiền điều kiện và dữ liệu | budget trả DAT,KHONG_DAT,KHONG_XAC_DINH và các lỗi; fixture cost có giá trị nhận dạng |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. gọi các nhánh; kiểm log ứng dụng, exception, trace của budget-check. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không cost/giá/cost% trong log hoặc payload debug; vẫn có requestId cho đối soát |
| Trạng thái | BLOCKED (môi trường backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-022: Dự toán ngày

Ưu tiên P0; UC-COST-012; API: API-COST-027, API-COST-030; FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004.

### TC-COST-022-01: Gộp nguyên liệu và đủ cột

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-022 / AC-COST-022-01 |
| Loại / nguồn | Functional; BR-EST-001, BR-EST-002, BR-EST-003 |
| Tiền điều kiện và dữ liệu | K=1,10 suất; công thức mỗi suất thịt70g trứng3 quả; giá120000/kg và800/quả; khoán1500; VAT0,giá suất40000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập dự toán ngày. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | thịt0.70kg=84000, trứng30quả=24000, khoán15000; tổng123000, doanh thu400000,cost30.75%; đủ phân rã món/giá/NCC/ngày/công thức |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-022-02: Số suất sai

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-022 / AC-COST-022-02 |
| Loại / nguồn | Functional; BR-EST-001, ERR-COST-422-08 |
| Tiền điều kiện và dữ liệu | thực đơn đủ giá |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập từng fixture số suất -1,1.5 hoặc tất cả0. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-08; không lưu bản dự toán |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-022-03: Làm tròn lên lượng mua

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-022 / AC-COST-022-03 |
| Loại / nguồn | Boundary; BR-EST-002 |
| Tiền điều kiện và dữ liệu | K=1; nguyên liệu tổng1001g, hệ số1000, giá100000/kg; không hao hụt/khoán |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập dự toán. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | lượng1.01kg, thành tiền101000; không làm tròn gần nhất thành1.00kg |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-022-04: K lớn hơn1

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-022 / AC-COST-022-04 |
| Loại / nguồn | Functional; BR-EST-001 |
| Tiền điều kiện và dữ liệu | K=2; số lượt chọn món chính50 và30, fixture khác50 và31 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập dự toán với chính sách Q15 được duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | theo đề xuất chia K: N=40 cho fixture1; fixture2 không chia hết cần xử lý theo quyết định; ca BLOCKED trước khi Q15 chốt |
| Trạng thái | BLOCKED (chờ E3-Q15) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-023: Dự toán tuần

Ưu tiên P0; UC-COST-012; API: API-COST-028; FR-COST-EST-003.

### TC-COST-023-01: Tuần đủ dữ liệu

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-023 / AC-COST-023-01 |
| Loại / nguồn | Functional; BR-EST-003 |
| Tiền điều kiện và dữ liệu | hai ngày cùng nguyên liệu I1; ngày1 dùng1kg,ngày2 dùng2kg; giá100000 và110000/kg; không khoán |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập tuần theo hợp đồng Q07 đã duyệt. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có bản ngày; bảng tuần I1 tổng3kg, tiền320000; truy được giá/ngày từng phần, không nhân3kg với một giá duy nhất |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q07) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-023-02: Một ngày thiếu giá

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-023 / AC-COST-023-02 |
| Loại / nguồn | Functional; BR-CALC-003, ERR-COST-422-03 |
| Tiền điều kiện và dữ liệu | tuần có ngày2 thiếu giá, còn lại hợp lệ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. lập tuần. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | báo lỗi ngày2; atomicity và số bản được phép ghi phải theo Q07; chưa chạy với oracle tự đặt |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q07) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-023-03: Retry tuần và phiên bản

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-023 / AC-COST-023-03 |
| Loại / nguồn | Integration; BR-EST-004 |
| Tiền điều kiện và dữ liệu | đã commit một batch nhưng mất phản hồi; giữ key cũ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đối soát rồi retry cùng key trong24h. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không tạo thêm bản ngày hoặc batch; kết quả theo semantics Q07 được duyệt |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q02); FLOW-COST-Q07 |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-024: Lịch sử và bản chỉ lượng

Ưu tiên P0; UC-COST-013; API: API-COST-027, API-COST-029, API-COST-030, API-COST-037; FR-COST-EST-005, FR-COST-EST-006.

### TC-COST-024-01: Lập lại không sửa cũ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-024 / AC-COST-024-01 |
| Loại / nguồn | Functional; BR-EST-004, BR-CALC-010 |
| Tiền điều kiện và dữ liệu | dự toán v1 giá100000; KT cập nhật giá110000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. KT lập lại cùng ngày/cơ sở; đọc cả hai bản bằng quyền đầy đủ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | v2 có người/thời điểm mới, v1 giữ giá100000; không sửa số suất hoặc dữ liệu chụp v1 |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-024-02: Bếp không xem cơ sở khác

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-024 / AC-COST-024-02 |
| Loại / nguồn | Security; ERR-SYS-404-01 |
| Tiền điều kiện và dữ liệu | bếp A chỉ có cost.estimate.qty; tồn tại dự toán B |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đổi ID/path/query sang B. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-SYS-404-01; không trả dòng của B |
| Trạng thái | BLOCKED (chờ E3-Q11) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-024-03: Không có cột tiền ẩn

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-024 / AC-COST-024-03 |
| Loại / nguồn | Security; NFR-COST-005 |
| Tiền điều kiện và dữ liệu | bếp A mở dự toán A |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đọc raw JSON, DOM và đối soát mọi nested field. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có số lượng/đơn vị/phân rã; không giá/thành tiền/tổng/cost%/inputsSnapshot chứa tiền, kể cả trường ẩn |
| Trạng thái | BLOCKED (chờ E3-Q11) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-025: Xuất dự toán

Ưu tiên P1; UC-COST-013; API: API-COST-031; FR-COST-EST-007.

### TC-COST-025-01: Bản đủ giá

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-025 / AC-COST-025-01 |
| Loại / nguồn | Functional; BR-CALC-010 |
| Tiền điều kiện và dữ liệu | KT có quyền estimate.read và bản v1 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xuất XLSX và PDF. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | hai tệp đúng v1, đủ dòng/tổng/đơn vị và metadata; số liệu khớp snapshot không tính lại theo giá mới |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-025-02: Quyền bị thu hồi trước tải

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-025 / AC-COST-025-02 |
| Loại / nguồn | Security; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | yêu cầu xuất hợp lệ đã được tạo; thu hồi quyền trước khi tải |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. tải tệp và retry URL cũ. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không tải được dữ liệu ngoài quyền; phản hồi lỗi không chứa tiền |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-025-03: Bản chỉ lượng không giấu tiền trong tệp

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-025 / AC-COST-025-03 |
| Loại / nguồn | Security; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | bếp A có qty và dự toán A |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xuất hai định dạng; giải nén XLSX kiểm sheets, hidden cells, sharedStrings, công thức; kiểm PDF text/metadata. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không có tiền/cost trong bất kỳ thành phần nào; chỉ lượng của A |
| Trạng thái | BLOCKED (chờ E3-Q11) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-026: Tính lại và mở cảnh báo

Ưu tiên P1; UC-COST-014; API: API-COST-032, API-COST-033; FR-COST-ALR-001, FR-COST-ALR-002.

### TC-COST-026-01: Tính lại đúng tập

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-026 / AC-COST-026-01 |
| Loại / nguồn | Functional; BR-COST-011, BR-CALC-010, NFR-COST-004 |
| Tiền điều kiện và dữ liệu | 100 giá đổi ảnh hưởng50 thực đơn APPROVED/PUBLISHED ngày phục vụ từ hôm nay; snapshot trước đạt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. kích hoạt giá mới và đo đến khi lưu kết quả/cảnh báo. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | hoàn tất<=5phút; snapshot giữ nguyên; kết quả mới tách riêng; ngày chuyển đạt sang vượt có cảnh báo cho DD/GD |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-026-02: Không tính lại ngày đã qua

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-026 / AC-COST-026-02 |
| Loại / nguồn | Functional; BR-COST-011 |
| Tiền điều kiện và dữ liệu | có ngày hôm qua đã duyệt và ngày tương lai DRAFT không thuộc tập worker |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. đổi giá liên quan. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | không đưa hai bản đó vào tập tính lại FR-COST-ALR-001; không sửa snapshot của chúng |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-026-03: Không trùng cảnh báo

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-026 / AC-COST-026-03 |
| Loại / nguồn | Integration; BR-COST-011 |
| Tiền điều kiện và dữ liệu | ngày chung A/B đã có cảnh báo OPEN; giá tiếp tục đổi ở hai cơ sở |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. phát lặp sự kiện giá và xử lý đồng thời. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | một cảnh báo OPEN cho thực đơn/ngày, chi tiết A/B cập nhật; không tạo hai đầu mục; ngày vốn vượt lúc duyệt chờ Q08 |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q08) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-027: Xử lý cảnh báo

Ưu tiên P1; UC-COST-014; API: API-COST-032, API-COST-033, API-COST-034; FR-COST-ALR-003.

### TC-COST-027-01: Đóng tay có audit

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-027 / AC-COST-027-01 |
| Loại / nguồn | Functional; BR-AUD-001 |
| Tiền điều kiện và dữ liệu | DD có cost.alert.read; cảnh báo OPEN và thực đơn vẫn vượt |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xem danh sách; đóng với lý do "Đã trao đổi để xử lý". 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | CLOSED; audit người/thời điểm/lý do; không biến kết quả vượt thành đạt hoặc sửa snapshot |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-027-02: Lý do ngắn hoặc thiếu quyền

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-027 / AC-COST-027-02 |
| Loại / nguồn | Functional; BR-AUD-001, ERR-SYS-422-01, ERR-AUTH-403-02 |
| Tiền điều kiện và dữ liệu | cảnh báo OPEN; KT doanh thu không có alert.read; DD có quyền |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. KT doanh thu thử đóng; DD đóng với9 ký tự. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | thiếu quyền ERR-AUTH-403-02; lý do ngắn ERR-SYS-422-01; giữ OPEN |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-027-03: Đóng theo sự kiện nghiệp vụ

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-027 / AC-COST-027-03 |
| Loại / nguồn | Integration; BR-AUD-001 |
| Tiền điều kiện và dữ liệu | hai fixture cảnh báo OPEN: giá đổi lại về đạt; thực đơn được thu hồi và sửa |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. xử lý từng sự kiện. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | cảnh báo tương ứng đóng; ghi nguồn xử lý và giữ lịch sử giá/snapshot |
| Trạng thái | NOT RUN (chưa có backend) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

## US-COST-028: Mô phỏng giá

Ưu tiên P2; UC-COST-016; API: API-COST-035; FR-COST-ALR-005.

### TC-COST-028-01: Mô phỏng không ghi

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-028 / AC-COST-028-01 |
| Loại / nguồn | Functional; FR/use case nêu trên |
| Tiền điều kiện và dữ liệu | quyền/phạm vi Q10 đã chốt; giá thật100000; giả định130000 |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. chạy mô phỏng rồi so số bản ghi giá/snapshot/estimate/alert trước sau. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | có danh sách ngày vượt trong phạm vi; các bảng nghiệp vụ không đổi; nhãn mô phỏng |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q10) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-028-02: Giá giả định sai

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-028 / AC-COST-028-02 |
| Loại / nguồn | Functional; BR-PRC-002, ERR-COST-422-01 |
| Tiền điều kiện và dữ liệu | nguyên liệu hợp lệ |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. mô phỏng giá0 hoặc-1. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ERR-COST-422-01, không chạy ghi nghiệp vụ |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q10) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |

### TC-COST-028-03: Phạm vi và thiếu giá khác

| Trường | Nội dung |
| :--- | :--- |
| Story / AC | US-COST-028 / AC-COST-028-03 |
| Loại / nguồn | Security; BR-CALC-003 |
| Tiền điều kiện và dữ liệu | chỉ được mô phỏng A; một ngày A thiếu giá nguyên liệu khác; có thực đơn B |
| Bước thực hiện | 1. Chuẩn bị fixture trên. 2. mô phỏng A rồi cố yêu cầu B. 3. Đối chiếu kết quả và dữ liệu/audit. |
| Kết quả mong đợi | ngày thiếu được ghi chưa tính được; không khẳng định đạt; không trả dữ liệu B |
| Trạng thái | BLOCKED (chờ FLOW-COST-Q10) |
| Actual / Evidence / Defect | Chưa chạy / Chưa có / Chưa có |


## Lịch sử sửa đổi

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo bản nháp truy vết, giữ điểm mở và trạng thái chưa chạy |
