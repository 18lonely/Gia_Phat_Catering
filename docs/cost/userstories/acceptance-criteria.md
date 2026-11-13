# Tiêu chí nghiệm thu Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft để BA/QA/Tech lead review.

Nguồn: [SRS Cost](../srs/spec.md), [16 use case](../srs/usecase-diagram.md), [API đề xuất](../api/api-spec.md), [user flow](../ui/user-flow.md).

Mỗi nhóm là Gherkin Given/When/Then, gồm thành công, lỗi và biên/quyền. Dữ liệu số là fixture giả định; VAT8% không phải quyết định của Gia Phát. Ca BLOCKED cần chốt oracle trước khi chạy; không chấm PASS chỉ vì hệ thống từ chối mọi thao tác. Một scenario có nhiều fixture phải chạy từng fixture và ghi từng kết quả.

<a id="us-cost-001"></a>

## US-COST-001: Danh mục nhà cung cấp

### AC-COST-001-01: Tạo, sửa và lọc NCC

Truy vết: FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003; BR-PRC-001. Gate: không có.

```gherkin
Scenario: AC-COST-001-01 Tạo, sửa và lọc NCC
  Given KT có quyền ghi; chưa có NCC An Bình
  When tạo An Bình loại REGULAR; sửa điện thoại; lọc tên An Bình, loại REGULAR và ACTIVE
  Then có đúng một NCC ACTIVE với điện thoại mới, lịch sử ghi người thao tác và nội dung thay đổi
```

### AC-COST-001-02: Tên trùng sau chuẩn hóa

Truy vết: FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003; BR-PRC-001, BR-CAT-001, ERR-COST-409-01. Gate: không có.

```gherkin
Scenario: AC-COST-001-02 Tên trùng sau chuẩn hóa
  Given đã có NCC An Bình chưa huỷ
  When tạo NCC có tên "  AN   BÌNH  "
  Then HTTP 409 ERR-COST-409-01; không thêm NCC
```

### AC-COST-001-03: Ngừng không xóa giá cũ

Truy vết: FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003; BR-PRC-007, ERR-COST-422-02. Gate: FLOW-COST-Q03.

```gherkin
Scenario: AC-COST-001-03 Ngừng không xóa giá cũ
  Given NCC An Bình có giá tham chiếu 120000 ngày 10/11/2026
  When ngừng NCC với lý do "Không tiếp tục mua hàng"; tính giá tại 10/11; thử nhập giá mới
  Then giá lịch sử vẫn dùng; giá mới bị từ chối; cảnh báo tham chiếu đang dùng được ghi nhận theo thiết kế Q03
```

<a id="us-cost-002"></a>

## US-COST-002: Nhập giá nguyên liệu

### AC-COST-002-01: Giá đầu tiên

Truy vết: FR-COST-PRC-001; BR-PRC-002, BR-PRC-005. Gate: không có.

```gherkin
Scenario: AC-COST-002-01 Giá đầu tiên
  Given nguyên liệu I1 và NCC S1 ACTIVE; chưa có giá; ngày hệ thống 11/11/2026
  When nhập I1/S1/A giá 120000 ngày 11/11
  Then tạo một dòng giá, tự đánh dấu tham chiếu, ghi audit; không có bước duyệt giá thứ hai trong thiết kế hiện tại
```

### AC-COST-002-02: Giá không hợp lệ

Truy vết: FR-COST-PRC-001; BR-PRC-002, ERR-COST-422-01. Gate: không có.

```gherkin
Scenario: AC-COST-002-02 Giá không hợp lệ
  Given I1/S1 ACTIVE
  When lần lượt nhập giá 0, -1, 1.5; mỗi lần dùng khóa yêu cầu mới
  Then mỗi lần HTTP 422 ERR-COST-422-01; không tạo dòng
```

### AC-COST-002-03: Biên ngày và khóa trùng

Truy vết: FR-COST-PRC-001; BR-PRC-003, BR-PRC-005, ERR-COST-422-02, ERR-COST-409-02. Gate: E3-Q13.

```gherkin
Scenario: AC-COST-002-03 Biên ngày và khóa trùng
  Given hôm nay 11/11/2026; hồi tố cấu hình 7 ngày
  When nhập từng bản độc lập tại 04/11, 11/12 rồi tại 03/11, 12/12; gửi lại tuple I1/S1/A/ngày đã tồn tại bằng khóa mới
  Then hai ngày biên hợp lệ; hai ngày ngoài biên trả ERR-COST-422-02; tuple trùng trả ERR-COST-409-02
```

### AC-COST-002-04: Tham chiếu không tồn tại

Truy vết: FR-COST-PRC-001; ERR-COST-404-01. Gate: không có.

```gherkin
Scenario: AC-COST-002-04 Tham chiếu không tồn tại
  Given không có nguyên liệu I999
  When nhập giá cho I999 hoặc NCC không tồn tại
  Then HTTP 404 ERR-COST-404-01; không tạo giá
```

### AC-COST-002-05: Schema và trường do server quản lý

Truy vết: FR-COST-PRC-001; ERR-COST-400-01. Gate: review API.

```gherkin
Scenario: AC-COST-002-05 Schema và trường do server quản lý
  Given KT có token hợp lệ; chưa có giá tuple định tạo
  When gửi JSON thiếu priceVnd, enum sai, thêm createdBy hoặc totalCost client tự đặt
  Then 400 ERR-COST-400-01 theo hợp đồng đề xuất, details.path chỉ field sai; không ghi giá
```

### AC-COST-002-06: NCC inactive có hai mã lỗi trong SRS

Truy vết: FR-COST-PRC-001; ERR-COST-404-01, ERR-COST-422-02. Gate: QA-COST-Q01: BA/Tech lead thống nhất mã.

```gherkin
Scenario: AC-COST-002-06 NCC inactive có hai mã lỗi trong SRS
  Given S1 tồn tại nhưng INACTIVE; I1 ACTIVE
  When nhập giá cho S1
  Then không ghi giá; oracle mã lỗi BLOCKED vì ma trận404-01 nói tham chiếu không còn dùng,422-02 lại nói NCC ngừng; cần thống nhất trước nghiệm thu hợp đồng
```

<a id="us-cost-003"></a>

## US-COST-003: Chọn và tra giá tham chiếu

### AC-COST-003-01: Ưu tiên giá cơ sở

Truy vết: FR-COST-PRC-002, FR-COST-PRC-003; BR-PRC-006, BR-COST-004. Gate: không có.

```gherkin
Scenario: AC-COST-003-01 Ưu tiên giá cơ sở
  Given I1 có giá chung 100000 ngày 10/11 và giá A 120000 ngày 01/11; không có giá B
  When tra I1 tại 11/11 cho A và B
  Then A nhận 120000 dù giá chung mới hơn; B nhận 100000 kèm NCC/ngày giá
```

### AC-COST-003-02: Không dùng giá tương lai

Truy vết: FR-COST-PRC-002, FR-COST-PRC-003; BR-PRC-006, ERR-COST-404-02. Gate: không có.

```gherkin
Scenario: AC-COST-003-02 Không dùng giá tương lai
  Given I2 chỉ có giá hiệu lực 16/11
  When tra I2 ngày 11/11
  Then HTTP 404 ERR-COST-404-02; không dùng giá tương lai
```

### AC-COST-003-03: Chuyển cờ trong cùng nhóm tương lai

Truy vết: FR-COST-PRC-002, FR-COST-PRC-003; BR-PRC-005. Gate: E3-Q4; E3-Q14.

```gherkin
Scenario: AC-COST-003-03 Chuyển cờ trong cùng nhóm tương lai
  Given hai giá I1/A/16-11 thuộc hai NCC; chỉ giá thứ nhất tham chiếu
  When chọn giá thứ hai làm tham chiếu; tra I1/A/16-11
  Then chỉ giá thứ hai còn cờ trong nhóm; giá nhóm ngày/cơ sở khác giữ nguyên; đổi cờ giá đã hiệu lực chờ quyết định riêng
```

<a id="us-cost-004"></a>

## US-COST-004: Nhập lưới nguyên tử

### AC-COST-004-01: Bỏ qua dòng không đổi

Truy vết: FR-COST-PRC-004; FR/use case của story. Gate: không có.

```gherkin
Scenario: AC-COST-004-01 Bỏ qua dòng không đổi
  Given lưới có hai nguyên liệu; I1=100000, I2=20000
  When lọc nhóm/bảo quản/đang dùng; đổi I1 thành 110000, giữ I2; lưu ngày hợp lệ
  Then tạo đúng một giá I1; I2 không thêm lịch sử
```

### AC-COST-004-02: Một dòng sai rollback

Truy vết: FR-COST-PRC-004; BR-PRC-002, ERR-COST-422-01. Gate: không có.

```gherkin
Scenario: AC-COST-004-02 Một dòng sai rollback
  Given lô có I1 giá 110000 và I2 giá 0
  When lưu lô; kiểm số giá trước/sau
  Then báo ERR-COST-422-01 gắn dòng I2; không tạo giá I1 hoặc I2
```

### AC-COST-004-03: Mất phản hồi sau commit

Truy vết: FR-COST-PRC-004; FR/use case của story. Gate: FLOW-COST-Q02.

```gherkin
Scenario: AC-COST-004-03 Mất phản hồi sau commit
  Given lô hợp lệ và key K; gateway làm mất phản hồi sau commit
  When đối soát K rồi retry cùng key/body trong 24 giờ
  Then trả kết quả đã lưu; số dòng không tăng lần hai; không tạo key mới chỉ vì timeout
```

### AC-COST-004-04: Hiệu năng lưới200 dòng

Truy vết: FR-COST-PRC-004; NFR-COST-003. Gate: môi trường backend.

```gherkin
Scenario: AC-COST-004-04 Hiệu năng lưới200 dòng
  Given 200 tuple giá mới hợp lệ, không cần xác nhận biến động; ghi cấu hình môi trường
  When gửi một lô200 dòng, đo từ gửi đến nhận xác nhận commit; đếm giá/audit
  Then <=3giây và đủ200 dòng; thời gian và tính nguyên tử cùng đạt
```

### AC-COST-004-05: Key cùng body khác và đang xử lý

Truy vết: FR-COST-PRC-004; ERR-COST-409-04, ERR-COST-409-05. Gate: FLOW-COST-Q02.

```gherkin
Scenario: AC-COST-004-05 Key cùng body khác và đang xử lý
  Given request K đã commit; request L được giữ ở trạng thái xử lý trong test
  When gửi K với giá khác; gửi đồng thời cùng L
  Then K trả ERR-COST-409-04 không ghi; L trả ERR-COST-409-05 kèm Retry-After; đối soát sau hoàn tất chỉ một kết quả
```

<a id="us-cost-005"></a>

## US-COST-005: Nhập XLSX giá

### AC-COST-005-01: Đọc đúng tên cột

Truy vết: FR-COST-PRC-005; BR-CAT-023. Gate: không có.

```gherkin
Scenario: AC-COST-005-01 Đọc đúng tên cột
  Given mẫu giá XLSX không mật khẩu, hai dòng hợp lệ; đổi thứ tự cột, thêm cột Ghi chú lạ, dòng trắng
  When kiểm tệp; xác nhận nhập
  Then kiểm không ghi; bỏ dòng trắng và cảnh báo cột lạ; xác nhận mới tạo hai dòng
```

### AC-COST-005-02: Tệp lỗi không ghi

Truy vết: FR-COST-PRC-005; BR-CAT-023, ERR-MENU-422-20. Gate: không có.

```gherkin
Scenario: AC-COST-005-02 Tệp lỗi không ghi
  Given tệp thiếu cột bắt buộc hoặc giá dòng 2 bằng 0
  When kiểm và thử xác nhận tệp chưa đạt
  Then ERR-MENU-422-20, lỗi có dòng/cột; không tạo giá
```

### AC-COST-005-03: Giới hạn dòng và đọc số

Truy vết: FR-COST-PRC-005; BR-CAT-023, ERR-MENU-422-20. Gate: không có.

```gherkin
Scenario: AC-COST-005-03 Giới hạn dòng và đọc số
  Given hai tệp mẫu có 2000 và 2001 dòng hợp lệ; số văn bản "120000"; tệp phụ có "120,000"
  When kiểm từng tệp; không xác nhận nhập
  Then 2000 dòng được kiểm; 2001 trả ERR-MENU-422-20; số nguyên văn bản được đọc; "120,000" là thập phân 120, không được hiểu là 120000
```

### AC-COST-005-04: Import đã kiểm bị đổi

Truy vết: FR-COST-PRC-005; ERR-COST-409-07. Gate: review API.

```gherkin
Scenario: AC-COST-005-04 Import đã kiểm bị đổi
  Given đã kiểm tệp và có token; thay bytes tệp hoặc dùng token hết hạn
  When commit token cũ với tệp mới
  Then ERR-COST-409-07; không nhập một dòng nào; phải kiểm lại
```

### AC-COST-005-05: Số dạng văn bản và trang tính

Truy vết: FR-COST-PRC-005; BR-CAT-023. Gate: không có.

```gherkin
Scenario: AC-COST-005-05 Số dạng văn bản và trang tính
  Given mẫu đúng trang; giá văn bản120000.0 và120000,0; trang khác có dữ liệu; file khác đặt mật khẩu
  When kiểm từng tệp không commit
  Then hai dạng số bằng120000 được đọc; bỏ trang khác kèm cảnh báo; tệp mật khẩu bị từ chối không ghi
```

<a id="us-cost-006"></a>

## US-COST-006: Lịch sử và hủy giá tương lai

### AC-COST-006-01: Hủy giá tương lai độc lập

Truy vết: FR-COST-PRC-006, FR-COST-PRC-007; BR-PRC-004, BR-AUD-001. Gate: không có.

```gherkin
Scenario: AC-COST-006-01 Hủy giá tương lai độc lập
  Given giá I1/A/16-11 là dòng duy nhất của ngày; hôm nay 11/11
  When xem lịch sử rồi hủy với lý do từ 10 ký tự
  Then dòng được đánh dấu hủy, giữ audit, không còn được chọn khi tra giá; các dòng cũ giữ nguyên
```

### AC-COST-006-02: Giá đã hiệu lực

Truy vết: FR-COST-PRC-006, FR-COST-PRC-007; BR-PRC-004, ERR-COST-409-03. Gate: không có.

```gherkin
Scenario: AC-COST-006-02 Giá đã hiệu lực
  Given giá ngày 10/11 và ngày 11/11; hôm nay 11/11
  When thử sửa hoặc hủy từng giá
  Then HTTP 409 ERR-COST-409-03; dữ liệu và cờ tham chiếu không bị đổi ngầm
```

### AC-COST-006-03: Phạm vi lịch sử

Truy vết: FR-COST-PRC-006, FR-COST-PRC-007; ERR-SYS-404-01. Gate: không có.

```gherkin
Scenario: AC-COST-006-03 Phạm vi lịch sử
  Given QL chỉ thuộc A; tồn tại giá riêng B
  When gọi trực tiếp chi tiết giá B bằng ID và lọc lịch sử B
  Then ERR-SYS-404-01 cho tài nguyên ngoài phạm vi; không lộ giá B
```

<a id="us-cost-007"></a>

## US-COST-007: Theo dõi giá thiếu và giá cũ

### AC-COST-007-01: Thiếu giá theo cơ sở

Truy vết: FR-COST-PRC-008, FR-COST-PRC-009; BR-PRC-006. Gate: không có.

```gherkin
Scenario: AC-COST-007-01 Thiếu giá theo cơ sở
  Given I1 dùng ở hai công thức ACTIVE; chỉ có giá riêng A
  When tra danh sách thiếu giá B và A
  Then B có I1, số món ảnh hưởng 2; A không liệt kê I1; không lấy giá riêng A cho B
```

### AC-COST-007-02: Chạy lại không nhân cảnh báo

Truy vết: FR-COST-PRC-008, FR-COST-PRC-009; BR-PRC-008, BR-COST-005. Gate: FLOW-COST-Q03.

```gherkin
Scenario: AC-COST-007-02 Chạy lại không nhân cảnh báo
  Given I1 tươi có giá 8 ngày tuổi; ngưỡng 7
  When chạy worker giá cũ hai lần cùng ngày
  Then một cảnh báo đang mở cho I1 gửi KT; lần hai không tạo cảnh báo mở thứ hai
```

### AC-COST-007-03: Biên tuổi giá

Truy vết: FR-COST-PRC-008, FR-COST-PRC-009; BR-PRC-008, BR-COST-005. Gate: DL-01.

```gherkin
Scenario: AC-COST-007-03 Biên tuổi giá
  Given tươi có giá 7/8 ngày tuổi; khô và đông lạnh có giá 30/31 ngày tuổi; cấu hình 7/30
  When chạy kiểm tuổi giá
  Then 7 và 30 chưa cảnh báo; 8 và 31 cảnh báo; nguyên liệu ngoài công thức ACTIVE không bị đưa vào tập kiểm
```

<a id="us-cost-008"></a>

## US-COST-008: Xác nhận biến động giá

### AC-COST-008-01: Xác nhận rồi lưu

Truy vết: FR-COST-PRC-010; BR-PRC-009. Gate: không có.

```gherkin
Scenario: AC-COST-008-01 Xác nhận rồi lưu
  Given giá trước 100000; ngưỡng lệch 30%
  When nhập 131000; xác nhận cảnh báo
  Then trước xác nhận chưa có dòng mới; sau xác nhận tạo đúng một dòng
```

### AC-COST-008-02: Hủy xác nhận

Truy vết: FR-COST-PRC-010; BR-PRC-009. Gate: không có.

```gherkin
Scenario: AC-COST-008-02 Hủy xác nhận
  Given giá trước 100000
  When nhập 69000; chọn hủy cảnh báo
  Then không tạo dòng giá; có thể sửa dữ liệu nhập
```

### AC-COST-008-03: Đúng ngưỡng và giá đầu tiên

Truy vết: FR-COST-PRC-010; BR-PRC-009. Gate: không có.

```gherkin
Scenario: AC-COST-008-03 Đúng ngưỡng và giá đầu tiên
  Given giá trước 100000; ngưỡng 30%; I2 chưa có giá
  When thử giá 130000, 70000 ở các fixture độc lập; nhập giá đầu I2
  Then đúng 30% không hỏi vì quy tắc là vượt 30%; I2 không có cơ sở so sánh nên không hỏi
```

### AC-COST-008-04: Token xác nhận stale

Truy vết: FR-COST-PRC-010; ERR-COST-409-06. Gate: review API.

```gherkin
Scenario: AC-COST-008-04 Token xác nhận stale
  Given giá nền100000, đã cấp token cho giá131000; sau đó giá nền thay hoặc token hết hạn
  When xác nhận giá131000 bằng token cũ
  Then ERR-COST-409-06; không ghi, yêu cầu kiểm lại dựa trên giá nền mới
```

<a id="us-cost-009"></a>

## US-COST-009: Chứng từ giá

### AC-COST-009-01: Gắn PDF hợp lệ

Truy vết: FR-COST-PRC-011; FR/use case của story. Gate: không có.

```gherkin
Scenario: AC-COST-009-01 Gắn PDF hợp lệ
  Given KT có quyền và PDF thật 1 MB
  When upload rồi gắn vào giá hoặc một lô; mở bằng quyền hợp lệ
  Then truy lại cùng chứng từ; URL nội bộ có chữ ký hết hạn 15 phút
```

### AC-COST-009-02: Sai nội dung và quá dung lượng

Truy vết: FR-COST-PRC-011; ERR-SYS-415-01, ERR-SYS-413-01. Gate: không có.

```gherkin
Scenario: AC-COST-009-02 Sai nội dung và quá dung lượng
  Given tệp executable đổi đuôi .pdf; PDF lớn hơn 10 MB
  When upload từng tệp
  Then tệp giả trả ERR-SYS-415-01; tệp quá cỡ trả ERR-SYS-413-01; không tạo liên kết chứng từ
```

### AC-COST-009-03: Thu hồi quyền và URL hết hạn

Truy vết: FR-COST-PRC-011; FR/use case của story. Gate: không có.

```gherkin
Scenario: AC-COST-009-03 Thu hồi quyền và URL hết hạn
  Given chứng từ giá thuộc B; QL thuộc A; URL đã hết hạn
  When thử tải bằng QL A; thử tải URL hết hạn
  Then không trả bytes chứng từ; không rò qua URL tải hoặc thông báo lỗi
```

<a id="us-cost-010"></a>

## US-COST-010: Cost món và bảng phân rã

### AC-COST-010-01: Tính chính xác theo đơn vị

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; BR-CALC-001, BR-CALC-002, BR-CALC-006. Gate: không có.

```gherkin
Scenario: AC-COST-010-01 Tính chính xác theo đơn vị
  Given thịt 70g giá 120000/kg hệ số1000; trứng 3 quả giá800; hao hụt KHONG; cả hai tính cost
  When tính món và mở picker tại cùng ngày/cơ sở
  Then cost 10800; dòng thịt 8400, trứng 2400; có NCC/ngày giá/đơn vị/tỷ trọng; picker cùng ngày khớp 10800
```

### AC-COST-010-02: Không trả tổng thiếu

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; BR-CALC-002, BR-CALC-003, ERR-COST-422-03. Gate: không có.

```gherkin
Scenario: AC-COST-010-02 Không trả tổng thiếu
  Given thịt cần tính cost nhưng không có giá; trứng vẫn có giá; nước không tính cost và không có giá
  When tính món
  Then ERR-COST-422-03 liệt kê thịt, không liệt kê nước; không trả 2400 như cost toàn món
```

### AC-COST-010-03: Công thức theo ngày và quyền

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; BR-CALC-001, BR-CAT-014. Gate: không có.

```gherkin
Scenario: AC-COST-010-03 Công thức theo ngày và quyền
  Given R1 hiệu lực10/11 thịt70g; R2 hiệu lực16/11 thịt80g; giá120000; có thêm công thức đã gắn vào MENU PENDING
  When tính món tại15/11,16/11; kiểm MENU PENDING; gọi picker bằng người thiếu cost.cost.read
  Then chọn R1 rồi R2 theo ngày; MENU PENDING giữ công thức gắn; picker của người thiếu quyền không có trường tiền
```

### AC-COST-010-04: Món không tồn tại

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; ERR-MENU-404-01. Gate: không có.

```gherkin
Scenario: AC-COST-010-04 Món không tồn tại
  Given không có mã món M999
  When tính M999
  Then ERR-MENU-404-01; không trả kết quả số
```

### AC-COST-010-05: Hao hụt đúng một lần

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; BR-EST-002. Gate: E3-Q2.

```gherkin
Scenario: AC-COST-010-05 Hao hụt đúng một lần
  Given thịt70g, giá120000/kg, hao hụt20%, chế độ CO
  When tính cost một suất; lập dự toán10 suất chỉ có món này không khoản khoán
  Then cost thịt10500; lượng mua0.88kg sau làm tròn lên từ0.875; thành tiền105600; không chia hao hụt lần hai
```

### AC-COST-010-06: Đối soát bộ kế toán

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; NFR-COST-002. Gate: O-01; dữ liệu kế toán.

```gherkin
Scenario: AC-COST-010-06 Đối soát bộ kế toán
  Given kế toán cung cấp10 món và10 ngày đã ký xác nhận; cấu hình VAT/phương pháp ghi kèm
  When tính lặp từng bộ bằng decimal, so bảng tay và lần tính trước
  Then sai lệch cost món<=1đ, cost%<=0.01 điểm phần trăm; lặp cùng đầu vào có cùng kết quả; lưu bảng actual/expected
```

### AC-COST-010-07: Decimal và không làm tròn trung gian

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; NFR-COST-008, BR-CALC-006. Gate: không có.

```gherkin
Scenario: AC-COST-010-07 Decimal và không làm tròn trung gian
  Given fixture0.1+0.2 đơn vị dùng; giá1đ/đơn vị; fixture có ba dòng cost0.4đ
  When rà kiểu dữ liệu engine và tính hai fixture
  Then tổng chính xác0.3; tổng ba dòng1.2 hiển thị1đ, không làm tròn từng dòng thành0; không dùng float cho tiền/định lượng
```

### AC-COST-010-08: Tổng cost0 không chia cho0

Truy vết: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; BR-CALC-002. Gate: FLOW-COST-Q04.

```gherkin
Scenario: AC-COST-010-08 Tổng cost0 không chia cho0
  Given mọi nguyên liệu món có cờ không tính cost
  When tính món và xem tỷ trọng từng dòng
  Then tổng cost0; cách biểu diễn tỷ trọng chờ Q04; không NaN/Infinity và không suy ra giá nhập0
```

<a id="us-cost-011"></a>

## US-COST-011: So sánh công thức

### AC-COST-011-01: So sánh cùng ngày

Truy vết: FR-COST-DISH-005; FR/use case của story. Gate: không có.

```gherkin
Scenario: AC-COST-011-01 So sánh cùng ngày
  Given R1 cost10000, R2 cost11000 tại cùng D/A
  When so sánh R1 và R2
  Then chênh1000 và10%; không ghi giá hay tự duyệt công thức
```

### AC-COST-011-02: Một bản thiếu giá

Truy vết: FR-COST-DISH-005; ERR-COST-422-03. Gate: không có.

```gherkin
Scenario: AC-COST-011-02 Một bản thiếu giá
  Given R2 có nguyên liệu chưa có giá
  When so sánh R1/R2
  Then ERR-COST-422-03; không suy diễn R2 bằng0 và không trả delta sai
```

### AC-COST-011-03: Cost gốc bằng0

Truy vết: FR-COST-DISH-005; FR/use case của story. Gate: FLOW-COST-Q04.

```gherkin
Scenario: AC-COST-011-03 Cost gốc bằng0
  Given R1 có mọi nguyên liệu không tính cost; R2 cost1000
  When so sánh hai bản
  Then delta tiền1000; cách hiển thị delta% phải theo quyết định Q04; không trả Infinity/NaN
```

<a id="us-cost-012"></a>

## US-COST-012: Lập bảng món đặc thù

### AC-COST-012-01: Chụp bản pending

Truy vết: FR-COST-DISH-006; BR-CALC-010. Gate: không có.

```gherkin
Scenario: AC-COST-012-01 Chụp bản pending
  Given món đặc thù M1 đủ giá tại A/D
  When lập bảng có ghi chú và gửi
  Then bảng PENDING giữ công thức, giá, cơ sở, ngày tính và người lập; thay giá sau đó không sửa nội dung chụp
```

### AC-COST-012-02: Sai loại món

Truy vết: FR-COST-DISH-006; ERR-COST-422-04. Gate: không có.

```gherkin
Scenario: AC-COST-012-02 Sai loại món
  Given M2 không có cờ đặc thù
  When lập bảng đặc thù cho M2
  Then ERR-COST-422-04; không tạo bảng
```

### AC-COST-012-03: Thiếu một giá

Truy vết: FR-COST-DISH-006; BR-CALC-003, ERR-COST-422-03. Gate: không có.

```gherkin
Scenario: AC-COST-012-03 Thiếu một giá
  Given M1 đặc thù thiếu giá thịt
  When gửi bảng M1
  Then ERR-COST-422-03, danh sách thiếu; không tạo bản chụp thiếu rồi coi là đủ
```

<a id="us-cost-013"></a>

## US-COST-013: Duyệt bảng món đặc thù

### AC-COST-013-01: Duyệt bởi người khác

Truy vết: FR-COST-DISH-007; BR-SEC-008, BR-CALC-010. Gate: không có.

```gherkin
Scenario: AC-COST-013-01 Duyệt bởi người khác
  Given bảng PENDING do DD1 tạo/sửa; GD1 khác DD1
  When GD1 duyệt
  Then APPROVED, có audit quyết định; dữ liệu chụp không bị tính lại
```

### AC-COST-013-02: Không tự duyệt hoặc thiếu lý do

Truy vết: FR-COST-DISH-007; BR-SEC-008, ERR-SYS-403-01, ERR-SYS-422-01. Gate: không có.

```gherkin
Scenario: AC-COST-013-02 Không tự duyệt hoặc thiếu lý do
  Given người có quyền duyệt đồng thời là người tạo hoặc người sửa cuối của bảng; bảng khác do người khác tạo
  When tự duyệt bảng đầu; trả lại bảng thứ hai với lý do9 ký tự rồi10 ký tự
  Then tự duyệt trả ERR-SYS-403-01; lý do9 trả ERR-SYS-422-01; lý do10 cho trả lại, giữ bản chụp
```

### AC-COST-013-03: Hiệu lực và cơ sở

Truy vết: FR-COST-DISH-007; BR-CALC-007, BR-COST-007. Gate: E3-Q16.

```gherkin
Scenario: AC-COST-013-03 Hiệu lực và cơ sở
  Given bảng M1 được duyệt ở A; ngày lập và ngày tính khác nhau; thời hạn cấu hình90
  When kiểm điều kiện M1 ở mốc89/90/91 ngày và cơ sở B
  Then ghi nhận kết quả theo bộ lọc được chốt ở E3-Q16 trước khi chạy; không tự coi bảng A dùng được ở B
```

### AC-COST-013-04: Hai quyết định cạnh tranh

Truy vết: FR-COST-DISH-007; ERR-SYS-409-02, ERR-COST-409-07. Gate: review API và concurrency token.

```gherkin
Scenario: AC-COST-013-04 Hai quyết định cạnh tranh
  Given cùng bảng PENDING v1; hai người có quyền duyệt khác người tạo/sửa
  When người1 duyệt v1; người2 gửi trả lại v1 với khóa mới
  Then chỉ một quyết định được commit; version cũ ERR-SYS-409-02; nếu tải version mới nhưng trạng thái đã duyệt thì ERR-COST-409-07; không ghi đè quyết định trước
```

<a id="us-cost-014"></a>

## US-COST-014: Gợi ý nhóm cost

### AC-COST-014-01: Gợi ý không tự ghi

Truy vết: FR-COST-DISH-008; FR/use case của story. Gate: E3-Q7.

```gherkin
Scenario: AC-COST-014-01 Gợi ý không tự ghi
  Given ngưỡng phân nhóm đã được duyệt trong fixture và món đủ giá
  When yêu cầu gợi ý
  Then trả nhóm theo ngưỡng; nhóm đang lưu không đổi cho tới thao tác quyết định của người dùng
```

### AC-COST-014-02: Thiếu giá không phân nhóm

Truy vết: FR-COST-DISH-008; BR-CALC-003. Gate: E3-Q7.

```gherkin
Scenario: AC-COST-014-02 Thiếu giá không phân nhóm
  Given món có nguyên liệu thiếu giá
  When yêu cầu gợi ý
  Then không đưa nhóm thấp do coi giá thiếu là0; trả chưa tính được
```

### AC-COST-014-03: Biên phân nhóm

Truy vết: FR-COST-DISH-008; FR/use case của story. Gate: E3-Q7.

```gherkin
Scenario: AC-COST-014-03 Biên phân nhóm
  Given có quyết định E3-Q7 về ngưỡng và dấu so sánh
  When thử cost dưới, đúng, trên ngưỡng một đồng
  Then nhóm khớp quyết định được duyệt; chưa điền ngưỡng tự đặt vào production
```

<a id="us-cost-015"></a>

## US-COST-015: Cost ngày trên thực đơn

### AC-COST-015-01: Ngày đủ món

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; BR-CALC-005, BR-CALC-006, BR-COST-002, BR-COST-003. Gate: O-01; E2-Q1.

```gherkin
Scenario: AC-COST-015-01 Ngày đủ món
  Given fixture giá suất40000 VAT8%, phần chính10800, phụ/rau/canh6500, khoán1500; ngưỡng52
  When tính cost ngày và mở phân rã
  Then cost18800; doanh thu chưa VAT=40000/1.08, cost50.76%, đạt; dư hiển thị459đ; có từng phần và cách tính
```

### AC-COST-015-02: VAT thiếu hoặc mẫu số0

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; BR-CALC-005, ERR-COST-422-05. Gate: không có.

```gherkin
Scenario: AC-COST-015-02 VAT thiếu hoặc mẫu số0
  Given fixture không đặt VAT; fixture khác giá suất0
  When tính từng ngày
  Then ERR-COST-422-05; không mặc định VAT0 hay trả cost%0
```

### AC-COST-015-03: Làm tròn rồi so ngưỡng

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; BR-CALC-006, BR-COST-001. Gate: không có.

```gherkin
Scenario: AC-COST-015-03 Làm tròn rồi so ngưỡng
  Given fixture VAT0, giá suất100000, ngưỡng52; cost52004 và52005 ở hai lần độc lập
  When tính cost% và kiểm ngưỡng
  Then 52.004% làm tròn52.00 đạt;52.005% làm tròn52.01 vượt; trung gian không làm tròn
```

### AC-COST-015-04: Ba phương pháp món chính

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; BR-CALC-004. Gate: E3-Q1; E3-Q12.

```gherkin
Scenario: AC-COST-015-04 Ba phương pháp món chính
  Given các món chính gồm Healthy có cost8000,10000,12000; K=2; món mặc định10000
  When tính từng cấu hình DAT_NHAT, BINH_QUAN, MAC_DINH
  Then phần chính lần lượt24000,20000,20000; không bỏ Healthy khỏi trung bình
```

### AC-COST-015-05: Ngày chưa đủ món và phản hồi cũ

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; FR/use case của story. Gate: FLOW-COST-Q02.

```gherkin
Scenario: AC-COST-015-05 Ngày chưa đủ món và phản hồi cũ
  Given ngày mới có món chính; hai lượt sửa có revision1 và2
  When tính phần có; trả phản hồi revision1 sau revision2
  Then hiện chưa đủ món, không gắn nhãn đạt cho ngày hoàn chỉnh; không ghi đè kết quả revision2 bằng revision1
```

### AC-COST-015-06: Hiệu năng tính thực đơn

Truy vết: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; NFR-COST-001. Gate: môi trường backend.

```gherkin
Scenario: AC-COST-015-06 Hiệu năng tính thực đơn
  Given fixture6 ngày x7 món, đủ giá; ghi môi trường, cơ sở, cache và cấu hình
  When chạy50 lần đo API cost và bộ kiểm đầy đủ, lưu từng mẫu; p95 theo thứ tự mẫu thứ48
  Then p95 Cost<=1s; tổng bộ kiểm theo NFR-MENU-001<=2s; không tính thời gian render wireframe
```

<a id="us-cost-016"></a>

## US-COST-016: Khoản khoán

### AC-COST-016-01: Ưu tiên riêng thay chung

Truy vết: FR-COST-MEAL-004; BR-CALC-008, BR-SEC-008. Gate: không có.

```gherkin
Scenario: AC-COST-016-01 Ưu tiên riêng thay chung
  Given khoản Gia vị chung1000 đã duyệt; đề nghị riêng suất40K1500 ngày16/11
  When người khác duyệt đề nghị; tính ngày15/11 và16/11 cho suất40K
  Then ngày15 dùng1000; ngày16 dùng1500 thay vì2500; không áp PENDING
```

### AC-COST-016-02: Khoản sai không nhận

Truy vết: FR-COST-MEAL-004; BR-CALC-008, ERR-COST-422-06. Gate: không có.

```gherkin
Scenario: AC-COST-016-02 Khoản sai không nhận
  Given KT có quyền
  When gửi khoản -1,1.5 hoặc thiếu ngày hiệu lực
  Then mỗi đầu vào trả ERR-COST-422-06; không tạo đề nghị
```

### AC-COST-016-03: Số0 và người đề nghị

Truy vết: FR-COST-MEAL-004; BR-CALC-008, BR-SEC-008, ERR-SYS-403-01. Gate: không có.

```gherkin
Scenario: AC-COST-016-03 Số0 và người đề nghị
  Given khoản giá0 ngày hợp lệ lý do đủ; người tạo có cả quyền duyệt trong fixture
  When gửi đề nghị0 rồi tự duyệt
  Then đề nghị0 hợp lệ, tự duyệt ERR-SYS-403-01; giá0 của khoản không bị nhầm với giá nguyên liệu
```

### AC-COST-016-04: Khoản trùng khi duyệt

Truy vết: FR-COST-MEAL-004; ERR-COST-409-08. Gate: review API.

```gherkin
Scenario: AC-COST-016-04 Khoản trùng khi duyệt
  Given đã có Gia vị/ALL/16-11 APPROVED; có đề nghị khác cùng tuple sau chuẩn hóa tên
  When duyệt đề nghị thứ hai
  Then ERR-COST-409-08; không tạo hai khoản cùng tên/phạm vi/ngày hiệu lực
```

<a id="us-cost-017"></a>

## US-COST-017: Cổng gửi duyệt

### AC-COST-017-01: Mọi cơ sở đều đạt

Truy vết: FR-COST-MEAL-005; BR-CALC-009. Gate: không có.

```gherkin
Scenario: AC-COST-017-01 Mọi cơ sở đều đạt
  Given thực đơn đủ món, đủ giá/VAT, bảng đặc thù còn hiệu lực; A/B cùng dưới ngưỡng
  When gửi duyệt ở chế độ CHAN
  Then Cost cho qua; MENU tiếp tục các điều kiện khác, không tự coi toàn bộ MENU đã được duyệt
```

### AC-COST-017-02: Một cơ sở vượt

Truy vết: FR-COST-MEAL-005; BR-CALC-009, BR-COST-001, ERR-COST-422-07. Gate: không có.

```gherkin
Scenario: AC-COST-017-02 Một cơ sở vượt
  Given A cost50%, B cost54%, ngưỡng52; CHAN
  When gửi duyệt thực đơn chung A/B và thử bỏ B khỏi request
  Then ERR-COST-422-07; không PENDING; server vẫn kiểm đủ cơ sở và trả chi tiết theo quyền
```

### AC-COST-017-03: Cảnh báo không bỏ qua dữ liệu thiếu

Truy vết: FR-COST-MEAL-005; BR-CALC-003, BR-CALC-007, ERR-COST-422-03, ERR-COST-422-04, ERR-COST-422-05. Gate: không có.

```gherkin
Scenario: AC-COST-017-03 Cảnh báo không bỏ qua dữ liệu thiếu
  Given CANH_BAO; lần1 đủ giá cost54%; lần2 thiếu giá; lần3 đặc thù thiếu bảng; lần4 thiếu VAT
  When gửi duyệt từng fixture
  Then lần1 Cost chỉ cảnh báo; lần2/3/4 vẫn chặn với ERR-COST-422-03/04/05 tương ứng; không có nút ngoại lệ CHAN
```

<a id="us-cost-018"></a>

## US-COST-018: Snapshot lúc duyệt

### AC-COST-018-01: Chụp từng ngày/cơ sở

Truy vết: FR-COST-MEAL-006; BR-CALC-010. Gate: FLOW-COST-Q02.

```gherkin
Scenario: AC-COST-018-01 Chụp từng ngày/cơ sở
  Given MENU PENDING đủ điều kiện, không có thay đổi đầu vào từ lần kiểm; 6 ngày,2 cơ sở
  When duyệt thành APPROVED
  Then có12 snapshot cho vòng duyệt, chứa giá/nguồn/ngày/params; ghi APPROVED và snapshot cùng giao dịch đề xuất
```

### AC-COST-018-02: Giá đổi trong lúc chờ

Truy vết: FR-COST-MEAL-006; BR-CALC-010. Gate: FLOW-COST-Q06.

```gherkin
Scenario: AC-COST-018-02 Giá đổi trong lúc chờ
  Given MENU PENDING đã kiểm bằng giá cũ; giá mới có hiệu lực trước khi duyệt
  When duyệt thực đơn
  Then chưa xác định oracle số liệu chụp đến khi Q06 chốt chính sách kiểm lại; ca phải BLOCKED, không mặc nhiên chụp kết quả cũ hoặc mới
```

### AC-COST-018-03: Bất biến và rollback

Truy vết: FR-COST-MEAL-006; BR-CALC-010. Gate: FLOW-COST-Q02.

```gherkin
Scenario: AC-COST-018-03 Bất biến và rollback
  Given đã có snapshot vòng1; fixture khác cố ý gây lỗi khi lưu snapshot trước commit
  When đổi giá/công thức/params rồi đọc vòng1; thử duyệt fixture lỗi
  Then vòng1 không đổi; giao dịch lỗi không để APPROVED thiếu snapshot; retry đối soát không tạo trùng vòng
```

<a id="us-cost-019"></a>

## US-COST-019: Chế độ kiểm Cost

### AC-COST-019-01: Duyệt thay đổi SYS

Truy vết: FR-COST-MEAL-008; BR-SYS-002, BR-SEC-008. Gate: không có.

```gherkin
Scenario: AC-COST-019-01 Duyệt thay đổi SYS
  Given CANH_BAO hiện hành; QT đề nghị CHAN hiệu lực hôm nay
  When GD khác người tạo duyệt
  Then trước duyệt vẫn CANH_BAO; sau duyệt CHAN áp dụng từ ngày hiệu lực
```

### AC-COST-019-02: Tự duyệt bị cấm

Truy vết: FR-COST-MEAL-008; BR-SEC-008, ERR-SYS-403-01. Gate: không có.

```gherkin
Scenario: AC-COST-019-02 Tự duyệt bị cấm
  Given người đề nghị cũng có quyền duyệt
  When tự duyệt đề nghị hoặc người sửa cuối duyệt
  Then ERR-SYS-403-01; tham số không thay
```

### AC-COST-019-03: Hiệu lực tương lai

Truy vết: FR-COST-MEAL-008; BR-SYS-002, BR-CALC-010. Gate: không có.

```gherkin
Scenario: AC-COST-019-03 Hiệu lực tương lai
  Given CHAN đã duyệt hiệu lực16/11, hiện11/11
  When kiểm ngày trước và đúng thời điểm có hiệu lực theo SYS
  Then trước hiệu lực giữ chế độ cũ; tới hiệu lực áp CHAN; bản chụp quá khứ không đổi
```

<a id="us-cost-020"></a>

## US-COST-020: Bộ kiểm và ẩn con số

### AC-COST-020-01: Đăng ký đúng quy tắc

Truy vết: FR-COST-RUL-001, FR-COST-RUL-002; BR-COST-001, BR-COST-005, BR-COST-006, BR-COST-007. Gate: DL-01; E3-Q7.

```gherkin
Scenario: AC-COST-020-01 Đăng ký đúng quy tắc
  Given fixture có ngày vượt, giá cũ, cặp chính/phụ cost cao, đặc thù thiếu bảng
  When chạy bộ kiểm tích hợp MENU
  Then có kết quả BR-COST-001/005/006/007 theo loại cấu hình; không đăng ký002/003/004 thành lỗi kiểm độc lập
```

### AC-COST-020-02: Không lộ tiền trong lỗi

Truy vết: FR-COST-RUL-001, FR-COST-RUL-002; ERR-COST-422-07. Gate: không có.

```gherkin
Scenario: AC-COST-020-02 Không lộ tiền trong lỗi
  Given tài khoản có quyền kiểm MENU nhưng thiếu cost.cost.read
  When kiểm ngày vượt và gửi duyệt ở CHAN; đọc JSON/network và UI
  Then chỉ nhãn đạt/không đạt; ERR-COST-422-07 được rút gọn, không cost%, tiền, breakdown trong details
```

### AC-COST-020-03: Quyền thay đổi và agent nội bộ

Truy vết: FR-COST-RUL-001, FR-COST-RUL-002; BR-SEC-009. Gate: không có.

```gherkin
Scenario: AC-COST-020-03 Quyền thay đổi và agent nội bộ
  Given agent nội bộ thay QL A; quyền cost bị thu hồi giữa hai yêu cầu
  When gọi cost B rồi lặp yêu cầu A sau thu hồi
  Then không trả dữ liệu B; quyền hiệu lực là giao quyền dịch vụ/người; yêu cầu kế tiếp không replay dữ liệu đã mất quyền
```

### AC-COST-020-04: Hồi quy quy tắc đã thuộc MENU

Truy vết: FR-COST-RUL-001, FR-COST-RUL-002; BR-COST-008, BR-COST-009, BR-COST-010, BR-COST-012. Gate: E2-Q5.

```gherkin
Scenario: AC-COST-020-04 Hồi quy quy tắc đã thuộc MENU
  Given fixture chuẩn min70/max80g; phụ tối đa50g; nguyên liệu có xương chưa khai hao hụt; định mức40000
  When lưu công thức chính69g và81g, phụ51g; lưu nguyên liệu thiếu hao hụt; chọn món tổng40001
  Then MENU chặn theo BR-COST-008/009/010/012; Cost không thay thế kiểm này; ngưỡng min/max/phụ là fixture chờ E2-Q5
```

<a id="us-cost-021"></a>

## US-COST-021: Ngân sách cho agent phía khách

### AC-COST-021-01: Chỉ một trạng thái

Truy vết: FR-COST-RUL-003; BR-CALC-011, BR-SEC-010. Gate: không có.

```gherkin
Scenario: AC-COST-021-01 Chỉ một trạng thái
  Given phiên còn quota; thực đơn hợp lệ mọi ngày đều đạt
  When gọi budget-check
  Then chỉ result DAT; không ngày vượt, ngưỡng, cost, giá, snapshot trong body hoặc log
```

### AC-COST-021-02: Thực đơn lỗi

Truy vết: FR-COST-RUL-003; ERR-MENU-422-14. Gate: không có.

```gherkin
Scenario: AC-COST-021-02 Thực đơn lỗi
  Given payload chứa món INACTIVE hoặc lặp món trong ngày
  When gọi budget-check
  Then ERR-MENU-422-14; không trả dữ liệu tiền trong lỗi
```

### AC-COST-021-03: Quota lời gọi31

Truy vết: FR-COST-RUL-003; ERR-COST-429-01. Gate: không có.

```gherkin
Scenario: AC-COST-021-03 Quota lời gọi31
  Given một phiên đã có29 lời gọi; payload hợp lệ
  When gọi lần30 rồi31, thử đổi key yêu cầu trong cùng phiên
  Then lần30 xử lý; lần31 ERR-COST-429-01, không có con số; key mới không reset quota
```

### AC-COST-021-04: Thiếu giá và trạng thái hỗn hợp

Truy vết: FR-COST-RUL-003; BR-CALC-011. Gate: FLOW-COST-Q09.

```gherkin
Scenario: AC-COST-021-04 Thiếu giá và trạng thái hỗn hợp
  Given fixture1 tất cả xác định và một ngày vượt; fixture2 thiếu giá nhưng không có ngày vượt; fixture3 vừa vượt vừa thiếu
  When gọi từng fixture
  Then fixture1 KHONG_DAT; fixture2 KHONG_XAC_DINH; fixture3 BLOCKED chờ ưu tiên Q09, không tự chốt
```

### AC-COST-021-05: Không rò dữ liệu toàn API

Truy vết: FR-COST-RUL-003; NFR-COST-005. Gate: E3-Q11.

```gherkin
Scenario: AC-COST-021-05 Không rò dữ liệu toàn API
  Given bốn tài khoản: bếp A, người nội bộ không quyền giá/cost, svc khách, QL A truy B; danh mục MENU/COST
  When gọi success/error/list/detail/export/replay với từng tài khoản; kiểm JSON, file và cache
  Then không con số hoặc trường giá/cost ngoài quyền trong mọi đường phản hồi; ghi endpoint x actor x outcome
```

### AC-COST-021-06: Quyền DB agent khách

Truy vết: FR-COST-RUL-003; NFR-COST-006, BR-SEC-010. Gate: môi trường backend.

```gherkin
Scenario: AC-COST-021-06 Quyền DB agent khách
  Given tài khoản DB thật dùng cho agent khách; danh mục15 bảng Cost từ DBML
  When kiểm grants rồi SELECT từng bảng Cost gồm bảng snapshot/allowance/alert mới; kiểm service không dùng tài khoản quyền cao để lách
  Then mọi SELECT trực tiếp bị từ chối; không chỉ kiểm4 bảng cũ
```

### AC-COST-021-07: Log budget không chứa số

Truy vết: FR-COST-RUL-003; NFR-COST-007, BR-SEC-010. Gate: môi trường backend.

```gherkin
Scenario: AC-COST-021-07 Log budget không chứa số
  Given budget trả DAT,KHONG_DAT,KHONG_XAC_DINH và các lỗi; fixture cost có giá trị nhận dạng
  When gọi các nhánh; kiểm log ứng dụng, exception, trace của budget-check
  Then không cost/giá/cost% trong log hoặc payload debug; vẫn có requestId cho đối soát
```

<a id="us-cost-022"></a>

## US-COST-022: Dự toán ngày

### AC-COST-022-01: Gộp nguyên liệu và đủ cột

Truy vết: FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004; BR-EST-001, BR-EST-002, BR-EST-003. Gate: không có.

```gherkin
Scenario: AC-COST-022-01 Gộp nguyên liệu và đủ cột
  Given K=1,10 suất; công thức mỗi suất thịt70g trứng3 quả; giá120000/kg và800/quả; khoán1500; VAT0,giá suất40000
  When lập dự toán ngày
  Then thịt0.70kg=84000, trứng30quả=24000, khoán15000; tổng123000, doanh thu400000,cost30.75%; đủ phân rã món/giá/NCC/ngày/công thức
```

### AC-COST-022-02: Số suất sai

Truy vết: FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004; BR-EST-001, ERR-COST-422-08. Gate: không có.

```gherkin
Scenario: AC-COST-022-02 Số suất sai
  Given thực đơn đủ giá
  When lập từng fixture số suất -1,1.5 hoặc tất cả0
  Then ERR-COST-422-08; không lưu bản dự toán
```

### AC-COST-022-03: Làm tròn lên lượng mua

Truy vết: FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004; BR-EST-002. Gate: không có.

```gherkin
Scenario: AC-COST-022-03 Làm tròn lên lượng mua
  Given K=1; nguyên liệu tổng1001g, hệ số1000, giá100000/kg; không hao hụt/khoán
  When lập dự toán
  Then lượng1.01kg, thành tiền101000; không làm tròn gần nhất thành1.00kg
```

### AC-COST-022-04: K lớn hơn1

Truy vết: FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004; BR-EST-001. Gate: E3-Q15.

```gherkin
Scenario: AC-COST-022-04 K lớn hơn1
  Given K=2; số lượt chọn món chính50 và30, fixture khác50 và31
  When lập dự toán với chính sách Q15 được duyệt
  Then theo đề xuất chia K: N=40 cho fixture1; fixture2 không chia hết cần xử lý theo quyết định; ca BLOCKED trước khi Q15 chốt
```

<a id="us-cost-023"></a>

## US-COST-023: Dự toán tuần

### AC-COST-023-01: Tuần đủ dữ liệu

Truy vết: FR-COST-EST-003; BR-EST-003. Gate: FLOW-COST-Q07.

```gherkin
Scenario: AC-COST-023-01 Tuần đủ dữ liệu
  Given hai ngày cùng nguyên liệu I1; ngày1 dùng1kg,ngày2 dùng2kg; giá100000 và110000/kg; không khoán
  When lập tuần theo hợp đồng Q07 đã duyệt
  Then có bản ngày; bảng tuần I1 tổng3kg, tiền320000; truy được giá/ngày từng phần, không nhân3kg với một giá duy nhất
```

### AC-COST-023-02: Một ngày thiếu giá

Truy vết: FR-COST-EST-003; BR-CALC-003, ERR-COST-422-03. Gate: FLOW-COST-Q07.

```gherkin
Scenario: AC-COST-023-02 Một ngày thiếu giá
  Given tuần có ngày2 thiếu giá, còn lại hợp lệ
  When lập tuần
  Then báo lỗi ngày2; atomicity và số bản được phép ghi phải theo Q07; chưa chạy với oracle tự đặt
```

### AC-COST-023-03: Retry tuần và phiên bản

Truy vết: FR-COST-EST-003; BR-EST-004. Gate: FLOW-COST-Q02; FLOW-COST-Q07.

```gherkin
Scenario: AC-COST-023-03 Retry tuần và phiên bản
  Given đã commit một batch nhưng mất phản hồi; giữ key cũ
  When đối soát rồi retry cùng key trong24h
  Then không tạo thêm bản ngày hoặc batch; kết quả theo semantics Q07 được duyệt
```

<a id="us-cost-024"></a>

## US-COST-024: Lịch sử và bản chỉ lượng

### AC-COST-024-01: Lập lại không sửa cũ

Truy vết: FR-COST-EST-005, FR-COST-EST-006; BR-EST-004, BR-CALC-010. Gate: không có.

```gherkin
Scenario: AC-COST-024-01 Lập lại không sửa cũ
  Given dự toán v1 giá100000; KT cập nhật giá110000
  When KT lập lại cùng ngày/cơ sở; đọc cả hai bản bằng quyền đầy đủ
  Then v2 có người/thời điểm mới, v1 giữ giá100000; không sửa số suất hoặc dữ liệu chụp v1
```

### AC-COST-024-02: Bếp không xem cơ sở khác

Truy vết: FR-COST-EST-005, FR-COST-EST-006; ERR-SYS-404-01. Gate: E3-Q11.

```gherkin
Scenario: AC-COST-024-02 Bếp không xem cơ sở khác
  Given bếp A chỉ có cost.estimate.qty; tồn tại dự toán B
  When đổi ID/path/query sang B
  Then ERR-SYS-404-01; không trả dòng của B
```

### AC-COST-024-03: Không có cột tiền ẩn

Truy vết: FR-COST-EST-005, FR-COST-EST-006; NFR-COST-005. Gate: E3-Q11.

```gherkin
Scenario: AC-COST-024-03 Không có cột tiền ẩn
  Given bếp A mở dự toán A
  When đọc raw JSON, DOM và đối soát mọi nested field
  Then có số lượng/đơn vị/phân rã; không giá/thành tiền/tổng/cost%/inputsSnapshot chứa tiền, kể cả trường ẩn
```

<a id="us-cost-025"></a>

## US-COST-025: Xuất dự toán

### AC-COST-025-01: Bản đủ giá

Truy vết: FR-COST-EST-007; BR-CALC-010. Gate: không có.

```gherkin
Scenario: AC-COST-025-01 Bản đủ giá
  Given KT có quyền estimate.read và bản v1
  When xuất XLSX và PDF
  Then hai tệp đúng v1, đủ dòng/tổng/đơn vị và metadata; số liệu khớp snapshot không tính lại theo giá mới
```

### AC-COST-025-02: Quyền bị thu hồi trước tải

Truy vết: FR-COST-EST-007; FR/use case của story. Gate: không có.

```gherkin
Scenario: AC-COST-025-02 Quyền bị thu hồi trước tải
  Given yêu cầu xuất hợp lệ đã được tạo; thu hồi quyền trước khi tải
  When tải tệp và retry URL cũ
  Then không tải được dữ liệu ngoài quyền; phản hồi lỗi không chứa tiền
```

### AC-COST-025-03: Bản chỉ lượng không giấu tiền trong tệp

Truy vết: FR-COST-EST-007; FR/use case của story. Gate: E3-Q11.

```gherkin
Scenario: AC-COST-025-03 Bản chỉ lượng không giấu tiền trong tệp
  Given bếp A có qty và dự toán A
  When xuất hai định dạng; giải nén XLSX kiểm sheets, hidden cells, sharedStrings, công thức; kiểm PDF text/metadata
  Then không có tiền/cost trong bất kỳ thành phần nào; chỉ lượng của A
```

<a id="us-cost-026"></a>

## US-COST-026: Tính lại và mở cảnh báo

### AC-COST-026-01: Tính lại đúng tập

Truy vết: FR-COST-ALR-001, FR-COST-ALR-002; BR-COST-011, BR-CALC-010, NFR-COST-004. Gate: không có.

```gherkin
Scenario: AC-COST-026-01 Tính lại đúng tập
  Given 100 giá đổi ảnh hưởng50 thực đơn APPROVED/PUBLISHED ngày phục vụ từ hôm nay; snapshot trước đạt
  When kích hoạt giá mới và đo đến khi lưu kết quả/cảnh báo
  Then hoàn tất<=5phút; snapshot giữ nguyên; kết quả mới tách riêng; ngày chuyển đạt sang vượt có cảnh báo cho DD/GD
```

### AC-COST-026-02: Không tính lại ngày đã qua

Truy vết: FR-COST-ALR-001, FR-COST-ALR-002; BR-COST-011. Gate: không có.

```gherkin
Scenario: AC-COST-026-02 Không tính lại ngày đã qua
  Given có ngày hôm qua đã duyệt và ngày tương lai DRAFT không thuộc tập worker
  When đổi giá liên quan
  Then không đưa hai bản đó vào tập tính lại FR-COST-ALR-001; không sửa snapshot của chúng
```

### AC-COST-026-03: Không trùng cảnh báo

Truy vết: FR-COST-ALR-001, FR-COST-ALR-002; BR-COST-011. Gate: FLOW-COST-Q08.

```gherkin
Scenario: AC-COST-026-03 Không trùng cảnh báo
  Given ngày chung A/B đã có cảnh báo OPEN; giá tiếp tục đổi ở hai cơ sở
  When phát lặp sự kiện giá và xử lý đồng thời
  Then một cảnh báo OPEN cho thực đơn/ngày, chi tiết A/B cập nhật; không tạo hai đầu mục; ngày vốn vượt lúc duyệt chờ Q08
```

<a id="us-cost-027"></a>

## US-COST-027: Xử lý cảnh báo

### AC-COST-027-01: Đóng tay có audit

Truy vết: FR-COST-ALR-003; BR-AUD-001. Gate: không có.

```gherkin
Scenario: AC-COST-027-01 Đóng tay có audit
  Given DD có cost.alert.read; cảnh báo OPEN và thực đơn vẫn vượt
  When xem danh sách; đóng với lý do "Đã trao đổi để xử lý"
  Then CLOSED; audit người/thời điểm/lý do; không biến kết quả vượt thành đạt hoặc sửa snapshot
```

### AC-COST-027-02: Lý do ngắn hoặc thiếu quyền

Truy vết: FR-COST-ALR-003; BR-AUD-001, ERR-SYS-422-01, ERR-AUTH-403-02. Gate: không có.

```gherkin
Scenario: AC-COST-027-02 Lý do ngắn hoặc thiếu quyền
  Given cảnh báo OPEN; KT doanh thu không có alert.read; DD có quyền
  When KT doanh thu thử đóng; DD đóng với9 ký tự
  Then thiếu quyền ERR-AUTH-403-02; lý do ngắn ERR-SYS-422-01; giữ OPEN
```

### AC-COST-027-03: Đóng theo sự kiện nghiệp vụ

Truy vết: FR-COST-ALR-003; BR-AUD-001. Gate: không có.

```gherkin
Scenario: AC-COST-027-03 Đóng theo sự kiện nghiệp vụ
  Given hai fixture cảnh báo OPEN: giá đổi lại về đạt; thực đơn được thu hồi và sửa
  When xử lý từng sự kiện
  Then cảnh báo tương ứng đóng; ghi nguồn xử lý và giữ lịch sử giá/snapshot
```

<a id="us-cost-028"></a>

## US-COST-028: Mô phỏng giá

### AC-COST-028-01: Mô phỏng không ghi

Truy vết: FR-COST-ALR-005; FR/use case của story. Gate: FLOW-COST-Q10.

```gherkin
Scenario: AC-COST-028-01 Mô phỏng không ghi
  Given quyền/phạm vi Q10 đã chốt; giá thật100000; giả định130000
  When chạy mô phỏng rồi so số bản ghi giá/snapshot/estimate/alert trước sau
  Then có danh sách ngày vượt trong phạm vi; các bảng nghiệp vụ không đổi; nhãn mô phỏng
```

### AC-COST-028-02: Giá giả định sai

Truy vết: FR-COST-ALR-005; BR-PRC-002, ERR-COST-422-01. Gate: FLOW-COST-Q10.

```gherkin
Scenario: AC-COST-028-02 Giá giả định sai
  Given nguyên liệu hợp lệ
  When mô phỏng giá0 hoặc-1
  Then ERR-COST-422-01, không chạy ghi nghiệp vụ
```

### AC-COST-028-03: Phạm vi và thiếu giá khác

Truy vết: FR-COST-ALR-005; BR-CALC-003. Gate: FLOW-COST-Q10.

```gherkin
Scenario: AC-COST-028-03 Phạm vi và thiếu giá khác
  Given chỉ được mô phỏng A; một ngày A thiếu giá nguyên liệu khác; có thực đơn B
  When mô phỏng A rồi cố yêu cầu B
  Then ngày thiếu được ghi chưa tính được; không khẳng định đạt; không trả dữ liệu B
```


## Lịch sử sửa đổi

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo bản nháp truy vết, giữ điểm mở và trạng thái chưa chạy |
