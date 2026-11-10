# Tiêu chí Chấp nhận (Acceptance Criteria — Gherkin BDD) — Epic E2 · Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `28-acceptance-criteria.md` · BA-Kit v1.0 |
| Phiên bản | 0.1.0 |
| Trạng thái | Draft |
| Ngày | 2026-11-10 |
| Tài liệu liên quan | [Backlog](backlog.md) · [SRS epic](../srs/spec.md) · [User-flow](../ui/user-flow.md) · [Bảng quy tắc](../../gia-phat/brainstorms/quy-tac-thuc-don.md) |

### Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-10 | BA | Khởi tạo cho 53 story của backlog v0.1.0 |

## Quy ước

- Mã kịch bản: `AC-MENU-{số story}-{số thứ tự}`, ghi ở dòng thẻ ngay trên `Scenario`.
- Mỗi story có tối thiểu 3 kịch bản theo `rules/08`: `@happy` thuận lợi · `@error` lỗi nghiệp vụ · `@edge` biên.
- Thẻ `@blocked(mã)` = kịch bản viết theo cách đang xử lý tạm; phải rà lại khi điểm mở đó có câu trả lời.
- Người dùng trong kịch bản: **DDV** = tài khoản vai trò Dinh dưỡng viên · **ND1**, **ND2** = hai tài khoản có quyền duyệt · **BT** = tài khoản vai trò Bếp trưởng (chỉ xem).
- Tên món, định lượng, giá trong kịch bản là **dữ liệu kiểm thử minh họa**, không phải số liệu của Gia Phát.
- "Hôm nay" = ngày chạy kiểm thử; "D+n" = n ngày sau hôm nay.
- Mọi kịch bản tạo, sửa, huỷ, duyệt đều ngầm có kết quả "có bản ghi nhật ký thay đổi" (`FR-SYS-AUD-001`); không lặp lại ở từng kịch bản.

---

# Lát R2.1 — Danh mục

## US-MENU-01 — Tạo và sửa nguyên liệu

```gherkin
Feature: Tạo và sửa nguyên liệu

  @AC-MENU-01-1 @happy
  Scenario: Tạo nguyên liệu tính theo gram
    Given DDV đang ở màn hình danh sách nguyên liệu
    And đã có nhóm nguyên liệu "Lợn"
    When DDV tạo nguyên liệu "Thịt lợn nạc vai", nhóm "Lợn", đơn vị mua "kg", đơn vị dùng "g", hệ số quy đổi 1000, loại bảo quản "Tươi"
    Then nguyên liệu được lưu ở trạng thái "ACTIVE" và có mã do hệ thống cấp
    And nguyên liệu xuất hiện trong danh sách chọn khi lập công thức

  @AC-MENU-01-2 @happy
  Scenario: Tạo nguyên liệu không tính theo gram
    When DDV tạo nguyên liệu "Đậu phụ", đơn vị mua "bìa", đơn vị dùng "bìa", hệ số quy đổi 1
    Then nguyên liệu được lưu với đơn vị dùng "bìa"

  @AC-MENU-01-3 @error
  Scenario: Tên trùng nguyên liệu đã có
    Given đã có nguyên liệu "Thịt lợn nạc vai"
    When DDV tạo nguyên liệu tên "thịt lợn nạc vai " (khác hoa thường, thừa dấu cách)
    Then hệ thống không tạo nguyên liệu
    And trả lỗi "ERR-MENU-409-01"

  @AC-MENU-01-4 @error
  Scenario: Hệ số quy đổi sai với cặp kg – g
    When DDV tạo nguyên liệu với đơn vị mua "kg", đơn vị dùng "g", hệ số quy đổi 100
    Then hệ thống không tạo nguyên liệu
    And trả lỗi "ERR-MENU-422-01" tại ô hệ số quy đổi

  @AC-MENU-01-5 @error
  Scenario: Nguyên liệu có xương nhưng thiếu tỷ lệ hao hụt
    When DDV tạo nguyên liệu "Sườn lợn", tích "có xương hoặc vỏ" và để trống tỷ lệ hao hụt
    Then hệ thống không tạo nguyên liệu
    And trả lỗi "ERR-MENU-422-02"

  @AC-MENU-01-6 @edge
  Scenario: Không sửa được đơn vị của nguyên liệu đang nằm trong công thức hiệu lực
    Given nguyên liệu "Cá trắm" nằm trong 2 công thức ở trạng thái "ACTIVE"
    When DDV sửa đơn vị dùng của "Cá trắm" từ "g" sang "kg"
    Then hệ thống không lưu thay đổi
    And trả lỗi "ERR-MENU-409-02" nêu số công thức là 2

  @AC-MENU-01-7 @edge
  Scenario: Hai người sửa cùng một nguyên liệu
    Given DDV và một tài khoản khác cùng mở nguyên liệu "Cà chua" ở phiên bản 3
    And tài khoản kia đã lưu thay đổi trước
    When DDV lưu thay đổi của mình
    Then hệ thống không ghi đè và trả lỗi "ERR-SYS-409-02"
```

## US-MENU-02 — Ngừng dùng nguyên liệu

```gherkin
Feature: Ngừng dùng nguyên liệu

  @AC-MENU-02-1 @happy
  Scenario: Ngừng dùng nguyên liệu không còn công thức nào dùng
    Given nguyên liệu "Bột nêm cũ" không nằm trong công thức "ACTIVE" nào
    When DDV chọn "Ngừng dùng" và nhập lý do "Đã đổi sang loại khác"
    Then nguyên liệu chuyển trạng thái "INACTIVE"
    And không còn xuất hiện trong danh sách chọn khi lập công thức mới

  @AC-MENU-02-2 @error
  Scenario: Ngừng dùng nguyên liệu đang nằm trong công thức hiệu lực
    Given nguyên liệu "Cá trắm" nằm trong công thức "ACTIVE" của món "Cá kho" và "Cá rán"
    When DDV chọn "Ngừng dùng" cho "Cá trắm"
    Then nguyên liệu giữ trạng thái "ACTIVE"
    And hệ thống trả lỗi "ERR-SYS-409-01" kèm danh sách 2 công thức

  @AC-MENU-02-3 @edge
  Scenario: Nguyên liệu chỉ còn trong công thức đã thay thế
    Given nguyên liệu "Đường thắng" chỉ nằm trong công thức ở trạng thái "SUPERSEDED"
    When DDV chọn "Ngừng dùng" và nhập lý do hợp lệ
    Then nguyên liệu chuyển trạng thái "INACTIVE"
    And công thức "SUPERSEDED" vẫn hiển thị được tên nguyên liệu này
```

## US-MENU-03 — Tìm và lọc nguyên liệu

```gherkin
Feature: Tìm và lọc nguyên liệu

  @AC-MENU-03-1 @happy
  Scenario: Lọc theo nhóm và trạng thái
    Given có 45 nguyên liệu, trong đó 6 nguyên liệu nhóm "Cá" ở trạng thái "ACTIVE"
    When BT lọc nhóm "Cá" và trạng thái "ACTIVE"
    Then danh sách hiện đúng 6 nguyên liệu

  @AC-MENU-03-2 @edge
  Scenario: Phân trang
    Given có 45 nguyên liệu
    When BT mở danh sách không lọc
    Then trang đầu hiện 20 nguyên liệu và tổng số ghi 45

  @AC-MENU-03-3 @edge
  Scenario: Bộ lọc không ra kết quả
    When BT tìm theo tên "xyz không tồn tại"
    Then danh sách hiện thông báo "Không có nguyên liệu khớp bộ lọc" và nút "Xoá lọc"

  @AC-MENU-03-4 @error
  Scenario: Vai trò chỉ xem không có nút sửa
    When BT mở danh sách nguyên liệu
    Then không có nút "Thêm nguyên liệu"
    And gọi trực tiếp lệnh tạo nguyên liệu trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-04 — Quản lý nhóm nguyên liệu

```gherkin
Feature: Quản lý nhóm nguyên liệu chính

  @AC-MENU-04-1 @happy @blocked(H-3)
  Scenario: Tạo nhóm kèm nguồn đạm
    When DDV tạo nhóm "Ếch" với nguồn đạm "Thịt"
    Then nhóm xuất hiện trong danh sách chọn của nguyên liệu và của món

  @AC-MENU-04-2 @error
  Scenario: Tên nhóm trùng
    Given đã có nhóm "Cá"
    When DDV tạo nhóm "cá"
    Then hệ thống trả lỗi "ERR-MENU-409-01"

  @AC-MENU-04-3 @edge
  Scenario: Không huỷ được nhóm đang được dùng
    Given nhóm "Cá" có 6 nguyên liệu và 5 món
    When DDV huỷ nhóm "Cá"
    Then nhóm không bị huỷ và hệ thống trả lỗi "ERR-SYS-409-01"
```

## US-MENU-05 — Khai mùa vụ

```gherkin
Feature: Khai mùa vụ của rau

  @AC-MENU-05-1 @happy
  Scenario: Khai một khoảng mùa
    When DDV khai mùa vụ của "Rau muống" từ tháng 4 đến tháng 9
    Then nguyên liệu "Rau muống" có 1 khoảng mùa "4–9"

  @AC-MENU-05-2 @error
  Scenario: Tháng ngoài khoảng 1–12
    When DDV khai mùa vụ từ tháng 0 đến tháng 13
    Then hệ thống trả lỗi "ERR-MENU-422-03"

  @AC-MENU-05-3 @edge
  Scenario: Mùa vụ vắt qua cuối năm
    When DDV khai mùa vụ của "Cải thảo" từ tháng 10 đến tháng 2
    Then khoảng mùa được lưu
    And tháng 12 và tháng 1 được coi là trong mùa, tháng 6 là ngoài mùa
```

## US-MENU-06 — Quản lý phương pháp chế biến

```gherkin
Feature: Quản lý phương pháp chế biến

  @AC-MENU-06-1 @happy @blocked(H-1,H-8)
  Scenario: Tạo phương pháp có cờ ít dầu mỡ
    When DDV tạo phương pháp "Hấp", không tích "là chiên/rán", tích "ít dầu mỡ"
    Then phương pháp "Hấp" chọn được cho món
    And món dùng phương pháp "Hấp" gắn được cờ Healthy

  @AC-MENU-06-2 @error
  Scenario: Tên phương pháp trùng
    Given đã có phương pháp "Kho"
    When DDV tạo phương pháp "kho"
    Then hệ thống trả lỗi "ERR-MENU-409-01"

  @AC-MENU-06-3 @edge
  Scenario: Bỏ cờ ít dầu mỡ khi đang có món Healthy dùng phương pháp đó
    Given món "Cá hấp" ở trạng thái "ACTIVE", có cờ Healthy, dùng phương pháp "Hấp"
    When DDV bỏ cờ "ít dầu mỡ" của phương pháp "Hấp"
    Then hệ thống không lưu và trả lỗi "ERR-SYS-409-01" kèm danh sách món Healthy đang dùng
```

## US-MENU-07 — Tạo món nháp

```gherkin
Feature: Tạo món ở trạng thái nháp

  @AC-MENU-07-1 @happy
  Scenario: Tạo món chính đủ thuộc tính
    When DDV tạo món "Cá sốt cà chua": vai trò "Món chính", nhóm "Cá", phương pháp "Sốt", kết cấu "Có nước sốt", vị chua "Có", nhóm cost "Cao", chất gây dị ứng "Cá"
    Then món được lưu ở trạng thái "DRAFT" và có mã do hệ thống cấp
    And món chưa chọn được khi xếp thực đơn

  @AC-MENU-07-2 @error
  Scenario: Tên món trùng
    Given đã có món "Cá kho"
    When DDV tạo món tên "Cá kho"
    Then hệ thống trả lỗi "ERR-MENU-409-01" kèm liên kết tới món đã có

  @AC-MENU-07-3 @error
  Scenario: Gắn Healthy với phương pháp không ít dầu mỡ
    Given phương pháp "Chiên" không có cờ ít dầu mỡ
    When DDV tạo món phương pháp "Chiên" và tích Healthy
    Then hệ thống trả lỗi "ERR-MENU-422-04" nêu phương pháp hiện tại là "Chiên"

  @AC-MENU-07-4 @error
  Scenario: Món gốc khác vai trò
    Given món "Canh chua" có vai trò "Canh"
    When DDV tạo món vai trò "Món chính" và chọn món gốc là "Canh chua"
    Then hệ thống trả lỗi "ERR-MENU-422-05"

  @AC-MENU-07-5 @edge
  Scenario: Món gốc chỉ một cấp
    Given món "Thịt kho tàu" có món gốc là "Thịt kho trứng cút"
    When DDV tạo món mới và chọn món gốc là "Thịt kho tàu"
    Then hệ thống trả lỗi "ERR-MENU-422-05"

  @AC-MENU-07-6 @edge
  Scenario: Mỗi thuộc tính có chú giải
    When DDV mở form tạo món
    Then mỗi trong 12 thuộc tính ảnh hưởng quy tắc hiển thị một dòng định nghĩa và ít nhất 1 ví dụ
```

## US-MENU-08 — Khai cặp món kỵ nhau

```gherkin
Feature: Khai cặp món không xếp cùng ngày

  @AC-MENU-08-1 @happy @blocked(H-4)
  Scenario: Khai một cặp kỵ
    When DDV khai cặp "Nem rán" – "Nộm" với ghi chú "cùng kiểu chế biến"
    Then cặp được lưu
    And bộ kiểm quy tắc báo vi phạm "BR-MENU-034" khi hai món cùng một ngày

  @AC-MENU-08-2 @error
  Scenario: Hai món của cặp giống nhau
    When DDV khai cặp "Nem rán" – "Nem rán"
    Then hệ thống trả lỗi "ERR-MENU-422-07"

  @AC-MENU-08-3 @edge
  Scenario: Cặp đã có theo thứ tự ngược
    Given đã có cặp "Nem rán" – "Nộm"
    When DDV khai cặp "Nộm" – "Nem rán"
    Then hệ thống trả lỗi "ERR-MENU-409-01"
```

## US-MENU-09 — Tìm và lọc món

```gherkin
Feature: Tìm và lọc món

  @AC-MENU-09-1 @happy
  Scenario: Lọc theo vai trò và Healthy
    Given có 16 món chính "ACTIVE", trong đó 4 món có cờ Healthy
    When DDV lọc vai trò "Món chính", Healthy "Có", trạng thái "ACTIVE"
    Then danh sách hiện đúng 4 món

  @AC-MENU-09-2 @edge
  Scenario: Món có đề nghị thay đổi đang chờ duyệt
    Given món "Sườn sốt chua ngọt" có 1 đề nghị thay đổi ở trạng thái "PENDING"
    When DDV mở danh sách món
    Then dòng "Sườn sốt chua ngọt" hiện nhãn "chờ duyệt thay đổi" và trạng thái vẫn là "ACTIVE"

  @AC-MENU-09-3 @error
  Scenario: Vai trò chỉ xem không thấy giá bán
    When BT mở chi tiết một món
    Then không có nút sửa và không có thẻ "Giá bán"
```

## US-MENU-10 — Gửi duyệt món

```gherkin
Feature: Gửi duyệt món nháp

  @AC-MENU-10-1 @happy
  Scenario: Gửi duyệt món đã có công thức chờ duyệt
    Given món "Cá hấp" ở trạng thái "DRAFT" và có 1 công thức ở trạng thái "PENDING"
    When DDV gửi duyệt món "Cá hấp"
    Then món chuyển trạng thái "PENDING"
    And mỗi tài khoản có quyền "menu.catalog.approve" nhận 1 thông báo dẫn tới món

  @AC-MENU-10-2 @error
  Scenario: Gửi duyệt món chưa có công thức
    Given món "Gà rán" ở trạng thái "DRAFT" và chưa có công thức nào
    When DDV gửi duyệt món "Gà rán"
    Then món giữ trạng thái "DRAFT"
    And hệ thống trả lỗi "ERR-MENU-422-06"

  @AC-MENU-10-3 @edge
  Scenario: Gửi duyệt nhiều món, một món không đạt
    Given DDV chọn 3 món nháp, trong đó "Gà rán" chưa có công thức
    When DDV gửi duyệt cả 3 món
    Then 2 món chuyển "PENDING", "Gà rán" giữ "DRAFT"
    And kết quả báo "2 thành công, 1 lỗi" kèm lý do của "Gà rán"

  @AC-MENU-10-4 @edge
  Scenario: Món có công thức chỉ ở trạng thái nháp
    Given món "Bò xào" có 1 công thức ở trạng thái "DRAFT"
    When DDV gửi duyệt món "Bò xào"
    Then hệ thống trả lỗi "ERR-MENU-422-06"
```

## US-MENU-11 — Duyệt hoặc trả lại món

```gherkin
Feature: Duyệt hoặc trả lại món

  @AC-MENU-11-1 @happy @blocked(O-06)
  Scenario: Duyệt món có công thức đang hiệu lực
    Given món "Cá hấp" ở trạng thái "PENDING", do DDV tạo, có công thức "ACTIVE"
    When ND1 duyệt món "Cá hấp"
    Then món chuyển trạng thái "ACTIVE" và chọn được khi xếp thực đơn
    And DDV nhận thông báo kết quả

  @AC-MENU-11-2 @happy
  Scenario: Duyệt món và công thức đầu tiên trong cùng một lần
    Given món "Gà rán" và công thức v1 của nó cùng ở trạng thái "PENDING"
    When ND1 chọn cả món và công thức rồi duyệt một lần
    Then công thức chuyển "ACTIVE" trước, sau đó món chuyển "ACTIVE"

  @AC-MENU-11-3 @error
  Scenario: Người sửa cuối tự duyệt
    Given món "Tôm luộc" ở trạng thái "PENDING" và ND1 là người sửa cuối
    When ND1 duyệt món "Tôm luộc"
    Then món giữ trạng thái "PENDING"
    And hệ thống trả lỗi "ERR-SYS-403-01"

  @AC-MENU-11-4 @error
  Scenario: Duyệt món khi công thức chưa được duyệt
    Given món "Gà rán" ở trạng thái "PENDING" và chỉ có công thức ở trạng thái "PENDING"
    When ND1 duyệt riêng món "Gà rán"
    Then hệ thống trả lỗi "ERR-MENU-422-06"

  @AC-MENU-11-5 @error
  Scenario: Trả lại không có lý do
    When ND1 chọn "Trả lại" món "Cá hấp" và để trống lý do
    Then món giữ trạng thái "PENDING" và hệ thống trả lỗi "ERR-SYS-422-01"

  @AC-MENU-11-6 @edge
  Scenario: Trả lại có lý do
    When ND1 trả lại món "Cá hấp" với lý do "Thuộc tính kết cấu chưa đúng"
    Then món về trạng thái "DRAFT"
    And DDV nhận thông báo kèm nguyên văn lý do
```

## US-MENU-12 — Tải mẫu và kiểm tệp nhập

```gherkin
Feature: Kiểm tệp bảng tính trước khi nhập

  @AC-MENU-12-1 @happy
  Scenario: Tệp nguyên liệu không có lỗi
    Given DDV đã tải mẫu "nguyên liệu" và điền 120 dòng hợp lệ
    When DDV tải tệp lên và chọn "Kiểm tra"
    Then hệ thống báo "120 dòng hợp lệ, 0 lỗi" và bật nút "Nhập"
    And chưa có nguyên liệu nào được tạo

  @AC-MENU-12-2 @error
  Scenario: Tệp có dòng lỗi
    Given tệp món có dòng 14 gắn Healthy với phương pháp "Chiên" và dòng 27 trùng tên món đã có
    When DDV chọn "Kiểm tra"
    Then hệ thống trả lỗi "ERR-MENU-422-20" kèm danh sách: dòng 14 – cột Healthy – "ERR-MENU-422-04"; dòng 27 – cột Tên – "ERR-MENU-409-01"
    And nút "Nhập" bị khoá

  @AC-MENU-12-3 @error
  Scenario: Tệp sai mẫu
    When DDV tải lên tệp thiếu cột "Đơn vị dùng"
    Then hệ thống trả lỗi "ERR-MENU-422-20" nêu cột bị thiếu

  @AC-MENU-12-4 @edge
  Scenario: Tệp đúng 2.000 dòng và 2.001 dòng
    When DDV kiểm tệp 2.000 dòng dữ liệu
    Then tệp được kiểm
    When DDV kiểm tệp 2.001 dòng dữ liệu
    Then hệ thống trả lỗi "ERR-MENU-422-20" nêu giới hạn 2.000 dòng

  @AC-MENU-12-5 @edge
  Scenario: Hai dòng trong tệp trùng tên nhau
    Given tệp món có dòng 5 và dòng 9 cùng tên "Cá kho riềng"
    When DDV chọn "Kiểm tra"
    Then cả dòng 5 và dòng 9 đều bị đánh dấu lỗi

  @AC-MENU-12-6 @edge
  Scenario: Việc kiểm kéo dài hơn 5 giây
    Given tệp 2.000 dòng cần hơn 5 giây để kiểm
    When DDV chọn "Kiểm tra" rồi rời trang
    Then việc kiểm tiếp tục chạy nền
    And DDV nhận thông báo khi kiểm xong, mở lại được kết quả
```

## US-MENU-13 — Nhập tệp đã kiểm sạch

```gherkin
Feature: Nhập dữ liệu từ tệp đã kiểm

  @AC-MENU-13-1 @happy @blocked(E2-Q10)
  Scenario: Nhập 40 món
    Given tệp món 40 dòng đã qua kiểm tra không lỗi
    When DDV chọn "Nhập"
    Then 40 món được tạo ở trạng thái "DRAFT"
    And hệ thống báo "40 món đã tạo" kèm liên kết tới danh sách món vừa nhập

  @AC-MENU-13-2 @happy
  Scenario: Nhập nguyên liệu
    Given tệp nguyên liệu 120 dòng đã qua kiểm tra không lỗi
    When DDV chọn "Nhập"
    Then 120 nguyên liệu được tạo ở trạng thái "ACTIVE"

  @AC-MENU-13-3 @error
  Scenario: Dữ liệu hệ thống thay đổi giữa lúc kiểm và lúc nhập
    Given tệp món đã qua kiểm tra không lỗi
    And sau đó một tài khoản khác tạo món trùng tên với dòng 8 của tệp
    When DDV chọn "Nhập"
    Then không có món nào được tạo
    And hệ thống trả lỗi "ERR-MENU-422-20" và yêu cầu kiểm lại

  @AC-MENU-13-4 @edge
  Scenario: Món nhập vào không tự hiệu lực
    Given DDV vừa nhập 40 món
    When DDV mở hộp chọn món của một thực đơn
    Then không món nào trong 40 món xuất hiện
```

---

# Lát R2.2 — Công thức, giá bán, loại suất

## US-MENU-14 — Lập công thức nháp

```gherkin
Feature: Lập công thức nháp

  @AC-MENU-14-1 @happy @blocked(O-02,E2-Q5)
  Scenario: Lập công thức có nguyên liệu chính và phụ
    Given món "Thịt kho trứng cút" có nhóm nguyên liệu chính "Lợn"
    When DDV lập công thức hiệu lực từ D+7 với: "Thịt lợn nạc vai" (chính) 65 – 70 – 70 g; "Trứng cút" (không chính) 3 – 3 – 3 quả
    Then công thức được lưu ở trạng thái "DRAFT" với số phiên bản 1
    And đơn vị của từng dòng tự lấy theo đơn vị dùng của nguyên liệu

  @AC-MENU-14-2 @error
  Scenario: Không có nguyên liệu chính
    When DDV lưu công thức mà không dòng nào được đánh dấu nguyên liệu chính
    Then hệ thống trả lỗi "ERR-MENU-422-08"

  @AC-MENU-14-3 @error
  Scenario: Lặp nguyên liệu
    When DDV lưu công thức có 2 dòng cùng nguyên liệu "Cà chua"
    Then hệ thống trả lỗi "ERR-MENU-422-08"

  @AC-MENU-14-4 @error
  Scenario: Chuẩn nhỏ hơn tối thiểu
    When DDV lưu công thức có dòng "Cá trắm" tối thiểu 130, chuẩn 120, tối đa 140
    Then hệ thống trả lỗi "ERR-MENU-422-09" chỉ rõ dòng sai

  @AC-MENU-14-5 @error
  Scenario: Nguyên liệu chính không thuộc nhóm của món
    Given món "Cá sốt cà chua" có nhóm nguyên liệu chính "Cá"
    When DDV lưu công thức chỉ có "Cà chua" (nhóm "Rau") là nguyên liệu chính
    Then hệ thống trả lỗi "ERR-MENU-422-10" nêu nhóm cần có là "Cá"

  @AC-MENU-14-6 @edge
  Scenario: Ba giá trị định lượng bằng nhau
    When DDV lưu dòng "Trứng cút" tối thiểu 3, chuẩn 3, tối đa 3
    Then dòng được chấp nhận

  @AC-MENU-14-7 @edge
  Scenario: Rau và canh không bắt buộc khớp nhóm
    Given món "Canh chua" có vai trò "Canh" và nhóm nguyên liệu chính "Rau"
    When DDV lưu công thức có nguyên liệu chính duy nhất là "Cá trắm"
    Then công thức được lưu, không báo "ERR-MENU-422-10"
```

## US-MENU-15 — Tạo nguyên liệu trong lúc soạn công thức

```gherkin
Feature: Tạo nguyên liệu còn thiếu khi đang soạn công thức

  @AC-MENU-15-1 @happy
  Scenario: Tạo nguyên liệu và giữ các dòng đã nhập
    Given DDV đang soạn công thức và đã nhập 3 dòng chưa lưu
    When DDV mở ngăn "Nguyên liệu mới", tạo "Cá rô phi" hợp lệ và lưu
    Then "Cá rô phi" xuất hiện trong công thức đang soạn
    And 3 dòng đã nhập giữ nguyên nguyên liệu và định lượng

  @AC-MENU-15-2 @error
  Scenario: Nguyên liệu mới trùng tên
    Given đã có nguyên liệu "Cá trắm"
    When DDV tạo "Cá trắm" trong ngăn "Nguyên liệu mới"
    Then ngăn không đóng và hiện lỗi "ERR-MENU-409-01"
    And các dòng công thức đã nhập giữ nguyên

  @AC-MENU-15-3 @edge
  Scenario: Đóng ngăn mà không lưu
    Given DDV đã nhập 3 dòng công thức chưa lưu và mở ngăn "Nguyên liệu mới"
    When DDV chọn "Huỷ"
    Then không có nguyên liệu nào được tạo và 3 dòng giữ nguyên
```

## US-MENU-16 — Duyệt hoặc trả lại công thức

```gherkin
Feature: Duyệt hoặc trả lại công thức

  @AC-MENU-16-1 @happy @blocked(O-06)
  Scenario: Duyệt công thức đầu tiên có ngày hiệu lực đã đến
    Given công thức v1 của "Gà rán" ở trạng thái "PENDING", do DDV tạo, hiệu lực từ hôm nay
    When ND1 duyệt công thức
    Then công thức chuyển trạng thái "ACTIVE"

  @AC-MENU-16-2 @happy
  Scenario: Duyệt phiên bản mới có ngày hiệu lực trong tương lai
    Given "Thịt kho trứng cút" có công thức v1 "ACTIVE" và v2 "PENDING" hiệu lực từ D+10
    When ND1 duyệt v2
    Then v1 và v2 cùng ở trạng thái "ACTIVE"
    And công thức hiệu lực cho ngày D+9 là v1, cho ngày D+10 là v2
    And vào ngày D+10 v1 chuyển trạng thái "SUPERSEDED"

  @AC-MENU-16-3 @error
  Scenario: Người tạo tự duyệt
    Given công thức v1 của "Gà rán" do ND1 tạo, ở trạng thái "PENDING"
    When ND1 duyệt công thức
    Then hệ thống trả lỗi "ERR-SYS-403-01" và công thức giữ trạng thái "PENDING"

  @AC-MENU-16-4 @error
  Scenario: Sửa công thức đã gửi duyệt
    Given công thức v1 của "Gà rán" ở trạng thái "PENDING"
    When DDV sửa định lượng của một dòng
    Then hệ thống trả lỗi "ERR-MENU-409-03"

  @AC-MENU-16-5 @edge
  Scenario: Trả lại công thức
    When ND1 trả lại công thức v1 của "Gà rán" với lý do "Định lượng gà thấp hơn bảng chuẩn"
    Then công thức về trạng thái "DRAFT" và DDV sửa được
    And DDV nhận thông báo kèm lý do
```

## US-MENU-17 — Tạo phiên bản công thức mới

```gherkin
Feature: Tạo phiên bản mới từ công thức đang hiệu lực

  @AC-MENU-17-1 @happy
  Scenario: Tạo v3 từ v2
    Given "Cá sốt cà chua" có công thức v2 ở trạng thái "ACTIVE" với 4 dòng
    When DDV chọn "Tạo phiên bản mới", nhập lý do "Giá cá tăng" và ngày hiệu lực D+14
    Then công thức v3 được tạo ở trạng thái "DRAFT" với 4 dòng giống v2
    And v2 vẫn ở trạng thái "ACTIVE"

  @AC-MENU-17-2 @error
  Scenario: Thiếu lý do
    When DDV chọn "Tạo phiên bản mới" và nhập lý do "ngắn"
    Then hệ thống trả lỗi "ERR-SYS-422-01" và không tạo phiên bản

  @AC-MENU-17-3 @edge
  Scenario: Thực đơn đã gắn phiên bản cũ không đổi
    Given thực đơn tuần sau ở trạng thái "PUBLISHED" đã gắn công thức v2 của "Cá sốt cà chua"
    When v3 được duyệt với ngày hiệu lực nằm trong tuần sau
    Then thực đơn đó vẫn gắn v2

  @AC-MENU-17-4 @edge
  Scenario: Đang có một bản nháp
    Given "Cá sốt cà chua" đã có công thức v3 ở trạng thái "DRAFT"
    When DDV mở công thức v2
    Then không có nút "Tạo phiên bản mới"
```

## US-MENU-18 — Lấy đúng công thức hiệu lực theo ngày

```gherkin
Feature: Công thức hiệu lực theo ngày phục vụ

  @AC-MENU-18-1 @happy
  Scenario: Có một công thức hiệu lực
    Given "Cá kho" có công thức v1 "ACTIVE" hiệu lực từ 01/10
    When hệ thống lấy công thức của "Cá kho" cho ngày 20/11
    Then kết quả là v1

  @AC-MENU-18-2 @edge
  Scenario: Hai phiên bản, ngày phục vụ đúng ngày chuyển tiếp
    Given "Thịt kho trứng cút" có v1 hiệu lực từ 01/08 và v2 hiệu lực từ 23/11, cùng "ACTIVE"
    When hệ thống lấy công thức cho ngày 22/11 và ngày 23/11
    Then kết quả lần lượt là v1 và v2

  @AC-MENU-18-3 @error
  Scenario: Chưa có công thức hiệu lực cho ngày đó
    Given "Gà rán" chỉ có công thức v1 "ACTIVE" hiệu lực từ 16/11
    When hệ thống lấy công thức của "Gà rán" cho ngày 15/11
    Then hệ thống trả lỗi "ERR-MENU-404-01" nêu tên món "Gà rán" và ngày 15/11
```

## US-MENU-19 — So sánh hai phiên bản công thức

```gherkin
Feature: So sánh phiên bản công thức

  @AC-MENU-19-1 @happy
  Scenario: Hiện dòng đổi, thêm, bỏ
    Given v1 có "Thịt lợn" chuẩn 70 g, "Trứng cút" 3 quả, "Đường thắng" 5 g
    And v2 có "Thịt lợn" chuẩn 65 g, "Trứng cút" 3 quả, "Hành khô" 3 g
    When ND1 mở so sánh v1 với v2
    Then "Thịt lợn" được đánh dấu "đổi định lượng", "Hành khô" là "thêm", "Đường thắng" là "bỏ", "Trứng cút" là "không đổi"

  @AC-MENU-19-2 @edge
  Scenario: Hai phiên bản giống hệt nhau
    When ND1 so sánh hai phiên bản có cùng các dòng và định lượng
    Then màn hình ghi "Không có khác biệt"

  @AC-MENU-19-3 @error
  Scenario: Công thức đầu tiên không có gì để so sánh
    Given "Gà rán" chỉ có công thức v1
    When ND1 mở chi tiết duyệt công thức v1
    Then màn hình hiện bảng định lượng, không hiện phần so sánh
```

## US-MENU-20 — Đặt giá bán

```gherkin
Feature: Đặt giá bán cho món

  @AC-MENU-20-1 @happy @blocked(E2-Q1)
  Scenario: Đặt giá đầu tiên
    Given món "Cá hấp" chưa có giá bán
    When DDV đặt giá 22000 đồng, hiệu lực từ D+1
    Then giá được lưu ở trạng thái "PENDING"
    And tài khoản có quyền "menu.price.approve" nhận thông báo

  @AC-MENU-20-2 @error
  Scenario: Giá không phải bội số của 100 đồng
    When DDV đặt giá 22050 đồng
    Then hệ thống trả lỗi "ERR-MENU-422-11"

  @AC-MENU-20-3 @error
  Scenario: Ngày hiệu lực là hôm nay
    When DDV đặt giá 22000 đồng, hiệu lực từ hôm nay
    Then hệ thống trả lỗi "ERR-MENU-422-11"

  @AC-MENU-20-4 @error
  Scenario: Trùng ngày hiệu lực
    Given món "Bò xào" đã có giá hiệu lực từ 01/12
    When DDV đặt giá khác cũng hiệu lực từ 01/12
    Then hệ thống trả lỗi "ERR-MENU-409-04"

  @AC-MENU-20-5 @edge
  Scenario: Giá bằng 0
    When DDV đặt giá 0 đồng, hiệu lực từ D+1
    Then giá được lưu ở trạng thái "PENDING"
```

## US-MENU-21 — Duyệt giá bán và lấy giá hiệu lực

```gherkin
Feature: Duyệt giá bán

  @AC-MENU-21-1 @happy @blocked(O-06,E2-Q7)
  Scenario: Duyệt giá
    Given giá 26000 đồng của "Bò xào" hiệu lực từ 01/12, do DDV tạo, ở trạng thái "PENDING"
    When ND1 duyệt giá
    Then giá chuyển trạng thái "APPROVED"
    And giá hiệu lực của "Bò xào" cho ngày 30/11 là giá cũ, cho ngày 01/12 là 26000 đồng

  @AC-MENU-21-2 @error
  Scenario: Món chưa có giá hiệu lực
    Given "Cá hấp" chỉ có giá "APPROVED" hiệu lực từ 01/12
    When hệ thống lấy giá của "Cá hấp" cho ngày 25/11
    Then hệ thống trả lỗi "ERR-MENU-404-02"

  @AC-MENU-21-3 @error
  Scenario: Giá chờ duyệt không được dùng
    Given "Cá hấp" có giá 22000 đồng hiệu lực từ D+1 ở trạng thái "PENDING"
    When hệ thống lấy giá của "Cá hấp" cho ngày D+2
    Then hệ thống trả lỗi "ERR-MENU-404-02"

  @AC-MENU-21-4 @edge
  Scenario: Giá đã hiệu lực không sửa, không huỷ được
    Given giá 24000 đồng của "Bò xào" ở trạng thái "APPROVED", hiệu lực từ ngày đã qua
    When DDV sửa hoặc huỷ giá này
    Then giá không đổi và hệ thống trả lỗi "ERR-MENU-409-10"

  @AC-MENU-21-5 @edge
  Scenario: Trả lại giá
    When ND1 trả lại giá 26000 đồng với lý do "Tăng quá nhanh so với tháng trước"
    Then giá chuyển trạng thái "REJECTED" và không bao giờ được dùng
```

## US-MENU-22 — Lịch sử giá bán

```gherkin
Feature: Lịch sử giá bán của món

  @AC-MENU-22-1 @happy
  Scenario: Xem lịch sử
    Given "Cá sốt cà chua" có giá 21000 đồng từ 01/08 và 22000 đồng từ 01/10, cùng "APPROVED"
    When DDV mở thẻ "Giá bán"
    Then danh sách hiện 2 dòng, mới nhất ở trên, dòng 22000 đồng ghi "đang áp dụng"

  @AC-MENU-22-2 @edge
  Scenario: Món chưa có giá
    When DDV mở thẻ "Giá bán" của món chưa có giá
    Then màn hình ghi "Món chưa có giá bán"

  @AC-MENU-22-3 @error
  Scenario: Vai trò không có quyền xem giá
    When BT gọi trực tiếp lệnh xem lịch sử giá
    Then hệ thống trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-23 — Tạo loại suất

```gherkin
Feature: Tạo và kích hoạt loại suất

  @AC-MENU-23-1 @happy
  Scenario: Tạo loại suất 40.000 đồng
    When DDV tạo loại suất "Suất 40.000đ": ngưỡng giá 40000, 3 món chính đưa ra, chọn 1, 2 món phụ, có rau, có canh
    Then loại suất được lưu ở trạng thái "DRAFT"
    When DDV kích hoạt loại suất
    Then loại suất chuyển "ACTIVE" và chọn được khi tạo thực đơn

  @AC-MENU-23-2 @error
  Scenario: Số món chính được chọn lớn hơn số đưa ra
    When DDV tạo loại suất với 2 món chính đưa ra và chọn 3
    Then hệ thống trả lỗi "ERR-MENU-422-12"

  @AC-MENU-23-3 @edge
  Scenario: Số món phụ ở biên
    When DDV tạo loại suất với 0 món phụ
    Then loại suất được lưu
    When DDV tạo loại suất với 6 món phụ
    Then hệ thống trả lỗi "ERR-MENU-422-12"

  @AC-MENU-23-4 @edge
  Scenario: Loại suất nháp chưa dùng được
    Given loại suất "Suất 35.000đ" ở trạng thái "DRAFT"
    When DDV tạo thực đơn mới
    Then "Suất 35.000đ" không có trong danh sách chọn loại suất
```

## US-MENU-24 — Khoá cơ cấu loại suất

```gherkin
Feature: Khoá cơ cấu loại suất đã có thực đơn gửi duyệt

  @AC-MENU-24-1 @happy
  Scenario: Sửa cơ cấu khi chưa có thực đơn gửi duyệt
    Given "Suất 40.000đ" chỉ có thực đơn ở trạng thái "DRAFT"
    When DDV sửa số món phụ từ 2 thành 3
    Then thay đổi được lưu

  @AC-MENU-24-2 @error
  Scenario: Sửa cơ cấu khi đã có thực đơn chờ duyệt
    Given "Suất 40.000đ" có 1 thực đơn ở trạng thái "PENDING"
    When DDV sửa ngưỡng giá từ 40000 thành 42000
    Then hệ thống trả lỗi "ERR-MENU-409-05"

  @AC-MENU-24-3 @edge
  Scenario: Tên vẫn sửa được
    Given "Suất 40.000đ" có thực đơn ở trạng thái "PUBLISHED"
    When DDV đổi tên thành "Suất tiêu chuẩn 40.000đ"
    Then tên mới được lưu

  @AC-MENU-24-4 @edge
  Scenario: Ngừng loại suất không ảnh hưởng thực đơn đã công bố
    Given "Suất 40.000đ" có thực đơn tuần sau ở trạng thái "PUBLISHED"
    When DDV ngừng loại suất
    Then thực đơn tuần sau vẫn ở trạng thái "PUBLISHED"
    And không tạo được thực đơn mới cho loại suất này
```

## US-MENU-25 — Đánh dấu loại suất công khai

```gherkin
Feature: Đánh dấu loại suất công khai

  @AC-MENU-25-1 @happy
  Scenario: Bật cờ công khai
    When DDV bật cờ "công khai" cho "Suất 40.000đ"
    Then cờ được lưu và hiện trong danh sách loại suất

  @AC-MENU-25-2 @edge
  Scenario: Bật cờ khi loại suất đã có thực đơn công bố
    Given "Suất 40.000đ" có thực đơn "PUBLISHED"
    When DDV bật cờ "công khai"
    Then cờ được lưu (cờ này không thuộc cơ cấu bị khoá)

  @AC-MENU-25-3 @error
  Scenario: Vai trò chỉ xem không bật được
    When BT gọi trực tiếp lệnh bật cờ "công khai"
    Then hệ thống trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-26 — Đề nghị sửa thuộc tính món đang dùng

```gherkin
Feature: Đề nghị sửa thuộc tính món đang dùng

  @AC-MENU-26-1 @happy
  Scenario: Đề nghị đổi một thuộc tính ảnh hưởng quy tắc
    Given món "Sườn sốt chua ngọt" ở trạng thái "ACTIVE" với vị chua "Không"
    When DDV đổi vị chua thành "Có", nhập lý do "Gắn thiếu khi tạo món" và gửi đề nghị
    Then một đề nghị thay đổi được tạo ở trạng thái "PENDING" ghi "Vị chua: Không → Có"
    And món vẫn "ACTIVE" với vị chua "Không" và hiện nhãn "chờ duyệt thay đổi"

  @AC-MENU-26-2 @happy
  Scenario: Sửa trường không ảnh hưởng quy tắc
    When DDV sửa mô tả của món "Sườn sốt chua ngọt"
    Then mô tả mới được lưu ngay, không tạo đề nghị

  @AC-MENU-26-3 @error
  Scenario: Thiếu lý do
    When DDV đổi phương pháp chế biến của món "ACTIVE" và gửi đề nghị với lý do 5 ký tự
    Then hệ thống trả lỗi "ERR-SYS-422-01" và không tạo đề nghị

  @AC-MENU-26-4 @error
  Scenario: Giá trị đề nghị vi phạm ràng buộc
    Given món "Cá rán" ở trạng thái "ACTIVE" dùng phương pháp "Chiên"
    When DDV đề nghị bật cờ Healthy
    Then hệ thống trả lỗi "ERR-MENU-422-04" và không tạo đề nghị

  @AC-MENU-26-5 @edge
  Scenario: Món đã có đề nghị đang chờ
    Given món "Sườn sốt chua ngọt" có 1 đề nghị ở trạng thái "PENDING"
    When DDV mở món
    Then các ô thuộc tính bị khoá và có nút "Rút đề nghị"

  @AC-MENU-26-6 @edge
  Scenario: Rút đề nghị
    When DDV chọn "Rút đề nghị"
    Then đề nghị chuyển trạng thái "WITHDRAWN", món không đổi và sửa lại được
```

## US-MENU-27 — Duyệt đề nghị thay đổi

```gherkin
Feature: Duyệt hoặc trả lại đề nghị thay đổi

  @AC-MENU-27-1 @happy @blocked(O-06)
  Scenario: Duyệt đề nghị sửa món
    Given đề nghị "Vị chua: Không → Có" của món "Sườn sốt chua ngọt" ở trạng thái "PENDING", do DDV gửi
    When ND1 duyệt đề nghị
    Then món có vị chua "Có", đề nghị chuyển "APPROVED", nhãn "chờ duyệt thay đổi" biến mất
    And thực đơn "DRAFT" có món này được kiểm lại bằng giá trị mới ở lần kiểm kế tiếp

  @AC-MENU-27-2 @error
  Scenario: Người đề nghị tự duyệt
    Given đề nghị do ND1 gửi
    When ND1 duyệt đề nghị đó
    Then hệ thống trả lỗi "ERR-SYS-403-01"

  @AC-MENU-27-3 @edge
  Scenario: Đề nghị đã lỗi thời
    Given đề nghị ghi "Phương pháp: Rán → Chiên" cho món "Đậu rán"
    And sau khi đề nghị được gửi, phương pháp của "Đậu rán" đã bị đổi bằng đường khác
    When ND1 mở đề nghị
    Then đề nghị ở trạng thái "STALE", nút "Duyệt" và "Trả lại" bị tắt
    And người đề nghị nhận thông báo cần gửi lại

  @AC-MENU-27-4 @edge
  Scenario: Thực đơn đã gửi duyệt giữ kết quả cũ
    Given một thực đơn "PENDING" có món "Sườn sốt chua ngọt"
    When đề nghị đổi vị chua của món được duyệt
    Then kết quả kiểm quy tắc của thực đơn đó không đổi

  @AC-MENU-27-5 @edge
  Scenario: Trả lại đề nghị
    When ND1 trả lại đề nghị với lý do hợp lệ
    Then đề nghị chuyển "REJECTED" và món không đổi
```

## US-MENU-28 — Ngừng dùng món

```gherkin
Feature: Ngừng dùng món

  @AC-MENU-28-1 @happy
  Scenario: Ngừng dùng món không nằm trong thực đơn sắp phục vụ
    Given món "Mực xào" ở trạng thái "ACTIVE" và không nằm trong thực đơn "PUBLISHED" nào có ngày phục vụ từ hôm nay
    When DDV chọn "Ngừng dùng" với lý do hợp lệ
    Then món chuyển trạng thái "INACTIVE" và không còn trong hộp chọn món

  @AC-MENU-28-2 @error
  Scenario: Món nằm trong thực đơn đã công bố sắp phục vụ
    Given món "Cá sốt cà chua" nằm trong thực đơn "PUBLISHED" có ngày phục vụ D+3
    When DDV chọn "Ngừng dùng"
    Then món giữ trạng thái "ACTIVE"
    And hệ thống trả lỗi "ERR-SYS-409-01" kèm tên thực đơn

  @AC-MENU-28-3 @edge
  Scenario: Món chỉ nằm trong thực đơn đã phục vụ xong
    Given món "Mực xào" chỉ nằm trong thực đơn "PUBLISHED" có ngày phục vụ cuối là hôm qua
    When DDV chọn "Ngừng dùng" với lý do hợp lệ
    Then món chuyển trạng thái "INACTIVE"

  @AC-MENU-28-4 @edge
  Scenario: Món nằm trong thực đơn nháp
    Given món "Mực xào" nằm trong một thực đơn "DRAFT"
    When DDV ngừng dùng món
    Then món chuyển "INACTIVE"
    And lần gửi duyệt kế tiếp của thực đơn đó bị chặn bởi "ERR-MENU-422-17"
```

## US-MENU-29 — Ảnh món

```gherkin
Feature: Gắn ảnh cho món

  @AC-MENU-29-1 @happy
  Scenario: Tải ảnh hợp lệ
    When DDV tải ảnh JPG 2 MB cho món "Cá hấp"
    Then ảnh được lưu và hiển thị ở chi tiết món

  @AC-MENU-29-2 @error
  Scenario: Sai định dạng
    When DDV tải tệp GIF cho món
    Then hệ thống trả lỗi "ERR-SYS-415-01"

  @AC-MENU-29-3 @edge
  Scenario: Kích thước ở biên
    When DDV tải ảnh PNG đúng 10 MB
    Then ảnh được lưu
    When DDV tải ảnh PNG lớn hơn 10 MB
    Then hệ thống trả lỗi "ERR-SYS-413-01"

  @AC-MENU-29-4 @edge
  Scenario: Tệp đổi đuôi
    When DDV tải tệp PDF đã đổi tên thành ".jpg"
    Then hệ thống trả lỗi "ERR-SYS-415-01" (kiểm theo nội dung tệp)
```

## US-MENU-30 — Nhập công thức và giá bán từ bảng tính

```gherkin
Feature: Nhập công thức và giá bán từ bảng tính

  @AC-MENU-30-1 @happy @blocked(O-02)
  Scenario: Nhập công thức cho 30 món
    Given 30 món và các nguyên liệu liên quan đã có trong hệ thống
    And tệp công thức 95 dòng đã qua kiểm tra không lỗi
    When DDV chọn "Nhập"
    Then 30 công thức v1 được tạo ở trạng thái "DRAFT" với tổng 95 dòng nguyên liệu

  @AC-MENU-30-2 @happy
  Scenario: Nhập giá bán
    Given tệp giá bán 30 dòng đã qua kiểm tra không lỗi
    When DDV chọn "Nhập"
    Then 30 giá được tạo ở trạng thái "PENDING"

  @AC-MENU-30-3 @error
  Scenario: Công thức tham chiếu món chưa có
    Given tệp công thức có dòng 12 ghi món "Vịt quay" chưa có trong hệ thống
    When DDV chọn "Kiểm tra"
    Then dòng 12 bị báo lỗi "không tìm thấy món" và nút "Nhập" bị khoá

  @AC-MENU-30-4 @error
  Scenario: Công thức trong tệp vi phạm khoảng định lượng
    Given tệp công thức có dòng 20 với tối thiểu 70, chuẩn 65
    When DDV chọn "Kiểm tra"
    Then dòng 20 bị báo lỗi "ERR-MENU-422-09"

  @AC-MENU-30-5 @edge
  Scenario: Món trong tệp thiếu nguyên liệu chính
    Given các dòng của món "Cá kho" trong tệp không có dòng nào đánh dấu nguyên liệu chính
    When DDV chọn "Kiểm tra"
    Then mọi dòng của "Cá kho" bị báo lỗi "ERR-MENU-422-08"
```

---

# Lát R2.3 — Thực đơn và bộ kiểm quy tắc

Dữ liệu nền dùng chung cho lát này: loại suất "Suất 40.000đ" (3 món chính đưa ra, 2 món phụ, có rau, có canh, ngưỡng giá 40.000 đồng) ở trạng thái "ACTIVE"; mọi món nêu tên đều "ACTIVE", có công thức và giá hiệu lực, trừ khi kịch bản nói khác.

## US-MENU-31 — Tạo thực đơn tuần

```gherkin
Feature: Tạo thực đơn nháp cho một loại suất và một tuần

  @AC-MENU-31-1 @happy @blocked(E2-Q3,E2-Q4)
  Scenario: Tạo thực đơn 6 ngày
    When DDV tạo thực đơn cho "Suất 40.000đ", tuần bắt đầu thứ Hai 16/11/2026, các ngày phục vụ T2 đến T7
    Then thực đơn được tạo ở trạng thái "DRAFT" với 6 ngày
    And mỗi ngày có 3 ô món chính, 2 ô món phụ, 1 ô rau, 1 ô canh, tất cả trống

  @AC-MENU-31-2 @error
  Scenario: Ngày bắt đầu không phải thứ Hai
    When DDV tạo thực đơn với tuần bắt đầu thứ Ba 17/11/2026
    Then hệ thống trả lỗi "ERR-MENU-422-13"

  @AC-MENU-31-3 @error
  Scenario: Đã có thực đơn cho loại suất và tuần đó
    Given đã có thực đơn "DRAFT" của "Suất 40.000đ" cho tuần 16/11/2026
    When DDV tạo thực đơn thứ hai cho cùng loại suất và tuần
    Then hệ thống trả lỗi "ERR-MENU-409-06" và mở thực đơn đã có

  @AC-MENU-31-4 @edge
  Scenario: Tuần có ngày nghỉ
    When DDV tạo thực đơn chỉ chọn T2, T3, T5, T6
    Then thực đơn có đúng 4 ngày

  @AC-MENU-31-5 @edge
  Scenario: Tạo lại sau khi thực đơn cũ đã huỷ
    Given thực đơn của "Suất 40.000đ" tuần 16/11/2026 đã bị huỷ
    When DDV tạo thực đơn mới cho cùng loại suất và tuần
    Then thực đơn mới được tạo
```

## US-MENU-32 — Xếp món vào ô

```gherkin
Feature: Xếp, đổi, bỏ món ở từng ô

  @AC-MENU-32-1 @happy
  Scenario: Xếp một món chính
    Given thực đơn "DRAFT" có ô "Món chính 1" của T2 đang trống
    When DDV chọn món "Thịt kho trứng cút" cho ô đó
    Then ô hiện "Thịt kho trứng cút"
    And ô được gắn phiên bản công thức hiệu lực tại ngày T2
    And bộ kiểm quy tắc chạy lại

  @AC-MENU-32-2 @error
  Scenario: Hộp chọn chỉ có món đúng vai trò
    When DDV mở hộp chọn món cho ô "Rau"
    Then danh sách chỉ gồm món có vai trò "Rau" ở trạng thái "ACTIVE"
    And gọi trực tiếp lệnh xếp món chính vào ô "Rau" trả lỗi "ERR-MENU-422-14"

  @AC-MENU-32-3 @error
  Scenario: Món không có công thức hiệu lực ngày phục vụ
    Given "Gà rán" có công thức hiệu lực từ 18/11
    When DDV xếp "Gà rán" vào ngày 16/11
    Then món không được xếp và hệ thống trả lỗi "ERR-MENU-404-01" kèm liên kết tới thẻ Công thức của món

  @AC-MENU-32-4 @error
  Scenario: Món không có giá bán hiệu lực ngày phục vụ
    Given "Cá hấp" có giá hiệu lực từ 01/12
    When DDV xếp "Cá hấp" vào ngày 16/11
    Then món không được xếp và hệ thống trả lỗi "ERR-MENU-404-02"

  @AC-MENU-32-5 @edge
  Scenario: Một món một lần mỗi ngày
    Given "Đậu rán" đã ở ô "Món phụ 1" của T2
    When DDV mở hộp chọn món cho ô "Món phụ 2" của T2
    Then "Đậu rán" hiện mờ với nhãn "đã có trong ngày" và không chọn được

  @AC-MENU-32-6 @edge
  Scenario: Món bị ngừng dùng trong lúc hộp chọn đang mở
    Given DDV đang mở hộp chọn món và "Mực xào" còn trong danh sách
    And một tài khoản khác ngừng dùng "Mực xào"
    When DDV chọn "Mực xào"
    Then hệ thống trả lỗi "ERR-MENU-422-14" và làm mới danh sách

  @AC-MENU-32-7 @edge
  Scenario: Sửa thực đơn không còn ở trạng thái soạn
    Given thực đơn ở trạng thái "PENDING"
    When DDV gọi lệnh đổi món ở một ô
    Then hệ thống trả lỗi "ERR-MENU-409-07"
```

## US-MENU-33 — Chọn món mặc định

```gherkin
Feature: Chọn món mặc định cho từng ngày

  @AC-MENU-33-1 @happy
  Scenario: Chọn món mặc định
    Given T2 có 3 món chính "Thịt kho trứng cút", "Cá kho", "Gà luộc"
    When DDV chọn "Thịt kho trứng cút" làm món mặc định của T2
    Then ô đó hiện nhãn "MẶC ĐỊNH"

  @AC-MENU-33-2 @error
  Scenario: Chọn món phụ làm mặc định
    When DDV gọi lệnh đặt "Đậu rán" (món phụ của T2) làm món mặc định
    Then hệ thống trả lỗi "ERR-MENU-422-15"

  @AC-MENU-33-3 @edge
  Scenario: Bỏ món đang là mặc định
    Given "Thịt kho trứng cút" là món mặc định của T2 và thực đơn ở trạng thái "CHECKED"
    When DDV bỏ "Thịt kho trứng cút" khỏi T2
    Then T2 không còn món mặc định
    And thực đơn về trạng thái "DRAFT"

  @AC-MENU-33-4 @edge
  Scenario: Đổi món mặc định
    Given "Thịt kho trứng cút" là món mặc định của T2
    When DDV chọn "Cá kho" làm món mặc định của T2
    Then chỉ "Cá kho" có nhãn "MẶC ĐỊNH"
```

## US-MENU-34 — Xem danh sách và chi tiết thực đơn

```gherkin
Feature: Xem thực đơn

  @AC-MENU-34-1 @happy
  Scenario: Dinh dưỡng viên thấy mọi trạng thái
    Given có 2 thực đơn "PUBLISHED", 1 "PENDING", 1 "DRAFT"
    When DDV mở danh sách thực đơn
    Then danh sách hiện 4 thực đơn kèm trạng thái và điểm quy tắc

  @AC-MENU-34-2 @happy
  Scenario: Vai trò chỉ xem chỉ thấy thực đơn đã công bố
    When BT mở danh sách thực đơn
    Then danh sách hiện 2 thực đơn "PUBLISHED"

  @AC-MENU-34-3 @error
  Scenario: Mở thực đơn chưa công bố bằng đường dẫn trực tiếp
    When BT mở đường dẫn của thực đơn "DRAFT"
    Then hệ thống trả lỗi "ERR-SYS-404-01"

  @AC-MENU-34-4 @edge
  Scenario: Chưa có thực đơn nào
    Given chưa có thực đơn nào
    When DDV mở danh sách thực đơn
    Then màn hình ghi "Chưa có thực đơn" và có nút "Tạo thực đơn"
```

## US-MENU-35 — Huỷ thực đơn nháp

```gherkin
Feature: Huỷ thực đơn nháp

  @AC-MENU-35-1 @happy
  Scenario: Huỷ thực đơn nháp
    Given thực đơn ở trạng thái "DRAFT"
    When DDV chọn "Huỷ thực đơn" và nhập lý do "Dựng thử, không dùng"
    Then thực đơn bị huỷ và không còn trong danh sách mặc định

  @AC-MENU-35-2 @error
  Scenario: Huỷ thực đơn đã gửi duyệt
    Given thực đơn ở trạng thái "PENDING"
    When DDV gọi lệnh huỷ thực đơn
    Then hệ thống trả lỗi "ERR-MENU-409-08"

  @AC-MENU-35-3 @edge
  Scenario: Huỷ thực đơn đã kiểm
    Given thực đơn ở trạng thái "CHECKED"
    When DDV huỷ với lý do hợp lệ
    Then thực đơn bị huỷ

  @AC-MENU-35-4 @error
  Scenario: Thiếu lý do
    When DDV chọn "Huỷ thực đơn" và để trống lý do
    Then hệ thống trả lỗi "ERR-SYS-422-01"
```

## US-MENU-36 — Kiểm quy tắc cấp ngày

Các kịch bản dưới đây kiểm **khung** của bộ kiểm bằng hai quy tắc mà docx nêu rõ con số (3 món chính; nem – nộm). Bộ kịch bản cho từng quy tắc còn lại — mỗi quy tắc 1 ca đạt và 1 ca vi phạm — viết sau khi DL-01 duyệt con số.

```gherkin
Feature: Kiểm quy tắc cấp ngày sau mỗi thay đổi

  @AC-MENU-36-1 @happy
  Scenario: Ngày không vi phạm
    Given T2 có đủ 3 món chính khác nhóm nguyên liệu trong đó đúng 1 món Healthy, 2 món phụ, rau, canh
    When bộ kiểm chạy
    Then không có kết quả "không đạt" nào của quy tắc cấp ngày cho T2

  @AC-MENU-36-2 @error
  Scenario: Vi phạm quy tắc cứng về cặp kỵ
    Given cặp "Nem rán" – "Nộm" đã được khai là kỵ nhau
    When DDV xếp "Nem rán" và "Nộm" vào hai ô món phụ của T4
    Then bảng kiểm có 1 kết quả không đạt mã "BR-MENU-034", loại bắt buộc
    And kết quả ghi ngày "T4" và hai món "Nem rán", "Nộm"

  @AC-MENU-36-3 @edge
  Scenario: Chi tiết vi phạm nêu giá trị đo và giới hạn
    Given T7 mới có 1 món chính
    When bộ kiểm chạy
    Then kết quả "BR-MENU-001" của T7 ghi "có 1/3 món chính"

  @AC-MENU-36-4 @edge
  Scenario: Ngày hoàn toàn trống không sinh vi phạm
    Given T7 chưa có món nào
    When bộ kiểm chạy
    Then không có kết quả nào cho T7

  @AC-MENU-36-5 @edge
  Scenario: Kết quả xác định
    Given một thực đơn cố định và danh mục quy tắc không đổi
    When bộ kiểm chạy 100 lần
    Then 100 lần cho cùng danh sách kết quả và cùng điểm

  @AC-MENU-36-6 @edge
  Scenario: Thời gian phản hồi
    Given thực đơn 6 ngày, mỗi ngày 7 món
    When bộ kiểm chạy 50 lần
    Then p95 thời gian phản hồi không vượt 2 giây

  @AC-MENU-36-7 @edge
  Scenario: Quy tắc bị tắt không chạy
    Given quy tắc "BR-MENU-034" đã được tắt trong danh mục
    When DDV xếp "Nem rán" và "Nộm" cùng ngày
    Then bảng kiểm không có kết quả nào của "BR-MENU-034"
```

## US-MENU-37 — Kiểm quy tắc cấp tuần

Con số trong kịch bản (2 ngày liền, 1 lần mỗi tuần) là giá trị đề xuất của bảng quy tắc, dùng làm ví dụ; thay bằng giá trị được duyệt ở DL-01.

```gherkin
Feature: Kiểm quy tắc xét trên cả tuần

  @AC-MENU-37-1 @happy @blocked(DL-01)
  Scenario: Tuần không vi phạm
    Given không nhóm nguyên liệu nào có mặt ở món chính quá 2 ngày phục vụ liên tiếp
    And không món chính nào xuất hiện quá 1 lần trong tuần
    When bộ kiểm chạy
    Then không có kết quả không đạt của "BR-MENU-012" và "BR-MENU-013"

  @AC-MENU-37-2 @error @blocked(DL-01,H-2)
  Scenario: Một nhóm nguyên liệu 3 ngày liền
    Given T2, T3, T4 đều có một món chính thuộc nhóm "Lợn"
    When bộ kiểm chạy
    Then có 1 kết quả không đạt "BR-MENU-012" ghi "Lợn" và các ngày "T2, T3, T4"

  @AC-MENU-37-3 @edge
  Scenario: Ngày nghỉ làm ngắt chuỗi liên tiếp
    Given thực đơn chỉ phục vụ T2, T3, T5, T6 và nhóm "Lợn" có ở T2, T3, T5
    When bộ kiểm chạy
    Then chuỗi liên tiếp được tính theo ngày phục vụ: T2, T3, T5 là 3 ngày phục vụ liền nhau
    And có 1 kết quả không đạt "BR-MENU-012"

  @AC-MENU-37-4 @edge
  Scenario: Biến thể đổi tên được đếm theo món gốc
    Given "Thịt kho tàu" có món gốc là "Thịt kho trứng cút"
    And T2 có "Thịt kho trứng cút", T5 có "Thịt kho tàu"
    When bộ kiểm chạy
    Then có 1 kết quả không đạt "BR-MENU-013" ghi 2 lần xuất hiện ở T2 và T5

  @AC-MENU-37-5 @edge @blocked(E2-Q2)
  Scenario: Không có thực đơn tuần trước
    Given loại suất chưa có thực đơn cho tuần liền trước
    When bộ kiểm chạy
    Then quy tắc tuần chỉ xét các ngày của tuần hiện tại
    And bảng kiểm ghi chú "không có dữ liệu tuần trước"
```

Kịch bản AC-MENU-37-3 giả định ngày nghỉ **không** ngắt chuỗi (chỉ đếm ngày phục vụ). Đây là cách hiểu của SRS mục 3.3.2; cần người soạn docx xác nhận cùng [H-2].

## US-MENU-38 — Điểm quy tắc và trạng thái "đã kiểm"

```gherkin
Feature: Điểm quy tắc và chuyển trạng thái đã kiểm

  @AC-MENU-38-1 @happy
  Scenario: Thực đơn đủ điều kiện chuyển "đã kiểm"
    Given mọi ô của mọi ngày đã có món và mọi ngày có món mặc định
    And không có kết quả không đạt nào của quy tắc bắt buộc
    When bộ kiểm chạy
    Then thực đơn chuyển trạng thái "CHECKED" và nút "Gửi duyệt" bật

  @AC-MENU-38-2 @happy @blocked(DL-01)
  Scenario: Tính điểm
    Given thực đơn có 2 cảnh báo điểm phạt 3 và 1 cảnh báo điểm phạt 2
    When bộ kiểm chạy
    Then điểm quy tắc là 92

  @AC-MENU-38-3 @edge
  Scenario: Quy tắc cấp ngày vi phạm ở nhiều ngày
    Given một quy tắc cấp ngày điểm phạt 3 không đạt ở T2, T4 và T6
    When bộ kiểm chạy
    Then điểm bị trừ 9

  @AC-MENU-38-4 @edge
  Scenario: Điểm không âm
    Given tổng điểm phạt của các cảnh báo là 120
    When bộ kiểm chạy
    Then điểm quy tắc là 0

  @AC-MENU-38-5 @error
  Scenario: Vi phạm bắt buộc không trừ điểm nhưng chặn trạng thái
    Given thực đơn đủ món, đủ món mặc định, có 1 vi phạm bắt buộc và không có cảnh báo
    When bộ kiểm chạy
    Then điểm quy tắc là 100
    And thực đơn giữ trạng thái "DRAFT" và nút "Gửi duyệt" tắt

  @AC-MENU-38-6 @edge
  Scenario: Thực đơn đã kiểm rơi về nháp
    Given thực đơn ở trạng thái "CHECKED"
    When DDV đổi một món làm phát sinh vi phạm bắt buộc
    Then thực đơn về trạng thái "DRAFT"
```

## US-MENU-39 — Kiểm ngưỡng giá suất

Toàn bộ story viết theo phương án đang đề xuất; nếu [E2-Q1] được trả lời khác, viết lại.

```gherkin
Feature: Kiểm tổng giá bán của mỗi tổ hợp suất so với ngưỡng

  @AC-MENU-39-1 @happy @blocked(E2-Q1)
  Scenario: Mọi tổ hợp trong ngưỡng
    Given T2 có món phụ 5000 và 4000, rau 3000, canh 2500 (tổng 14500)
    And 3 món chính giá 22000, 22000, 23000
    When bộ kiểm chạy
    Then không có kết quả không đạt "BR-COST-012" cho T2

  @AC-MENU-39-2 @error @blocked(E2-Q1)
  Scenario: Một món chính làm suất vượt ngưỡng
    Given T4 có món phụ, rau, canh tổng 17000 và món chính "Bò xào" giá 24000
    When bộ kiểm chạy
    Then có 1 kết quả không đạt "BR-COST-012" cho T4
    And kết quả ghi "Bò xào", tổng 41000 và phần vượt 1000

  @AC-MENU-39-3 @edge @blocked(E2-Q1)
  Scenario: Tổng đúng bằng ngưỡng
    Given T3 có món phụ, rau, canh tổng 16000 và một món chính giá 24000
    When bộ kiểm chạy
    Then không có kết quả không đạt "BR-COST-012" cho món chính đó

  @AC-MENU-39-4 @edge
  Scenario: Dùng giá hiệu lực tại ngày phục vụ
    Given "Bò xào" có giá 24000 đến hết 30/11 và 26000 từ 01/12
    When bộ kiểm chạy cho ngày 30/11 và ngày 01/12
    Then tổng giá được tính bằng 24000 cho ngày 30/11 và 26000 cho ngày 01/12
```

## US-MENU-40 — Lý do chấp nhận cho cảnh báo mức nặng

```gherkin
Feature: Ghi lý do chấp nhận cảnh báo mức nặng

  @AC-MENU-40-1 @happy
  Scenario: Ghi lý do
    Given thực đơn có 1 cảnh báo điểm phạt 3
    When DDV ghi lý do "Khách yêu cầu có thịt lợn mỗi ngày đầu tuần"
    Then lý do được lưu kèm cảnh báo đó và hiển thị cho người duyệt

  @AC-MENU-40-2 @error
  Scenario: Lý do quá ngắn
    When DDV ghi lý do "ok" cho cảnh báo điểm phạt 3 rồi gửi duyệt
    Then hệ thống trả lỗi "ERR-MENU-422-19"

  @AC-MENU-40-3 @edge
  Scenario: Lý do tự xoá khi cảnh báo hết
    Given DDV đã ghi lý do cho cảnh báo "BR-MENU-030" của T4
    When DDV đổi món làm T4 chỉ còn 1 món vị chua
    Then cảnh báo biến mất và lý do đã ghi bị xoá
    And nếu cảnh báo đó xuất hiện lại sau này, ô lý do trống

  @AC-MENU-40-4 @edge
  Scenario: Cảnh báo mức vừa và nhẹ không cần lý do
    Given thực đơn chỉ có cảnh báo điểm phạt 2 và 1
    When DDV gửi duyệt
    Then việc gửi duyệt không bị chặn vì thiếu lý do
```

## US-MENU-41 — Kiểm thực đơn chưa lưu

```gherkin
Feature: Kiểm quy tắc cho thực đơn chưa lưu

  @AC-MENU-41-1 @happy
  Scenario: Kết quả giống thực đơn đã lưu
    Given một thực đơn đã lưu có kết quả kiểm K
    When tài khoản dịch vụ của agent gửi đúng nội dung thực đơn đó tới lệnh kiểm thực đơn chưa lưu
    Then kết quả trả về giống hệt K
    And không có bản ghi nào được tạo hoặc thay đổi

  @AC-MENU-41-2 @error
  Scenario: Nội dung chứa món không hợp lệ
    When agent gửi thực đơn có một món ở trạng thái "DRAFT"
    Then hệ thống trả lỗi "ERR-MENU-422-14" nêu món không hợp lệ

  @AC-MENU-41-3 @edge
  Scenario: Tải đồng thời
    When 20 lời gọi kiểm thực đơn chưa lưu được gửi đồng thời
    Then p95 thời gian phản hồi không vượt 2 giây và không lời gọi nào lỗi

  @AC-MENU-41-4 @error
  Scenario: Tài khoản không có quyền
    When BT gọi lệnh kiểm thực đơn chưa lưu
    Then hệ thống trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-42 — Xem danh mục quy tắc

```gherkin
Feature: Xem danh mục quy tắc

  @AC-MENU-42-1 @happy @blocked(DL-01)
  Scenario: Xem danh mục
    When DDV mở danh mục quy tắc
    Then mỗi quy tắc hiện mã, tên, câu gốc trong file quy chuẩn, loại, điểm phạt, phạm vi ngày hoặc tuần, tham số, trạng thái bật/tắt

  @AC-MENU-42-2 @edge
  Scenario: Quy tắc có đề nghị đang chờ duyệt
    Given quy tắc "BR-MENU-012" có 1 đề nghị thay đổi "PENDING"
    When DDV mở danh mục quy tắc
    Then dòng "BR-MENU-012" hiện nhãn "chờ duyệt thay đổi", giá trị hiển thị là giá trị đang áp dụng

  @AC-MENU-42-3 @error
  Scenario: Vai trò chỉ xem không sửa được
    When BT mở danh mục quy tắc
    Then không có nút "Sửa"
    And gọi trực tiếp lệnh đề nghị sửa quy tắc trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-43 — Đề nghị sửa quy tắc

```gherkin
Feature: Đề nghị sửa danh mục quy tắc

  @AC-MENU-43-1 @happy @blocked(E2-Q11)
  Scenario: Đề nghị đổi tham số
    Given "BR-MENU-012" đang có tham số số ngày liên tiếp tối đa là 2
    When DDV đề nghị đổi thành 3 với lý do "Thịt lợn dùng nhiều nhất, giới hạn 2 gây cảnh báo ở mọi thực đơn"
    Then một đề nghị "PENDING" được tạo ghi "2 → 3"
    And bộ kiểm vẫn dùng giá trị 2

  @AC-MENU-43-2 @happy
  Scenario: Đề nghị được duyệt
    Given đề nghị "2 → 3" của "BR-MENU-012" ở trạng thái "PENDING", do DDV gửi
    When ND1 duyệt đề nghị
    Then tham số của "BR-MENU-012" là 3
    And thực đơn "DRAFT" được kiểm bằng giá trị 3 ở lần kiểm kế tiếp

  @AC-MENU-43-3 @error
  Scenario: Điểm phạt ngoài khoảng
    When DDV đề nghị đặt điểm phạt 5 cho một quy tắc mềm
    Then hệ thống trả lỗi "ERR-MENU-422-16"

  @AC-MENU-43-4 @error
  Scenario: Thiếu lý do
    When DDV đề nghị tắt một quy tắc mà không nhập lý do
    Then hệ thống trả lỗi "ERR-SYS-422-01"

  @AC-MENU-43-5 @edge
  Scenario: Quy tắc mới chặt hơn làm thực đơn đã kiểm rơi về nháp
    Given một thực đơn "CHECKED" đạt khi quy tắc "BR-MENU-010" đang tắt
    When đề nghị bật "BR-MENU-010" được duyệt và thực đơn được kiểm lại
    And thực đơn có 2 món chính cùng nhóm nguyên liệu trong một ngày
    Then thực đơn về trạng thái "DRAFT" và hiện nhãn "cần kiểm lại" trong danh sách

  @AC-MENU-43-6 @edge @blocked(E2-Q11)
  Scenario: Thực đơn đã gửi duyệt giữ kết quả cũ
    Given một thực đơn "PENDING" có kết quả kiểm K
    When một đề nghị sửa quy tắc được duyệt
    Then kết quả kiểm của thực đơn đó vẫn là K
```

---

# Lát R2.4 — Duyệt, công bố và phần P1

## US-MENU-44 — Gửi duyệt thực đơn

```gherkin
Feature: Gửi duyệt thực đơn

  @AC-MENU-44-1 @happy @blocked(E2-Q6)
  Scenario: Gửi duyệt thực đơn đã kiểm
    Given thực đơn ở trạng thái "CHECKED" với điểm 91
    When DDV chọn "Gửi duyệt"
    Then bộ kiểm chạy lại ngay trước khi chuyển trạng thái
    And thực đơn chuyển "PENDING", hiện "chờ duyệt 0/1" và ở chế độ chỉ đọc
    And mỗi tài khoản có quyền "menu.menu.approve" nhận 1 thông báo

  @AC-MENU-44-2 @error
  Scenario: Còn ô trống và thiếu món mặc định
    Given T7 còn 6 ô trống và T6, T7 chưa có món mặc định
    When DDV chọn "Gửi duyệt"
    Then hệ thống trả lỗi "ERR-MENU-422-17" liệt kê các ô trống và các ngày thiếu món mặc định
    And thực đơn giữ trạng thái "DRAFT"

  @AC-MENU-44-3 @error
  Scenario: Còn vi phạm bắt buộc
    Given thực đơn đủ món nhưng có 1 vi phạm "BR-MENU-034"
    When DDV chọn "Gửi duyệt"
    Then hệ thống trả lỗi "ERR-MENU-422-18" nêu số vi phạm là 1

  @AC-MENU-44-4 @error
  Scenario: Cảnh báo mức nặng chưa có lý do
    Given thực đơn có 2 cảnh báo điểm phạt 3, mới ghi lý do cho 1
    When DDV chọn "Gửi duyệt"
    Then hệ thống trả lỗi "ERR-MENU-422-19" nêu còn 1 cảnh báo thiếu lý do

  @AC-MENU-44-5 @edge
  Scenario: Món bị ngừng dùng sau khi thực đơn đã kiểm
    Given thực đơn "CHECKED" có món "Mực xào"
    And "Mực xào" vừa bị ngừng dùng
    When DDV chọn "Gửi duyệt"
    Then hệ thống trả lỗi "ERR-MENU-422-17" nêu món "Mực xào" không còn dùng được

  @AC-MENU-44-6 @edge
  Scenario: Điểm dưới ngưỡng cần hai người duyệt
    Given tham số "QUY_TAC_DIEM_TOI_THIEU" là 80 và thực đơn có điểm 74
    When DDV gửi duyệt thành công
    Then thực đơn hiện "chờ duyệt 0/2"

  @AC-MENU-44-7 @edge
  Scenario: Bộ kiểm đăng ký thêm báo không đạt
    Given một bộ kiểm khác đã đăng ký vào bước gửi duyệt và trả kết quả không đạt
    When DDV chọn "Gửi duyệt"
    Then thực đơn giữ trạng thái cũ và hiện thông báo của bộ kiểm đó
```

## US-MENU-45 — Duyệt hoặc trả lại thực đơn

```gherkin
Feature: Duyệt hoặc trả lại thực đơn

  @AC-MENU-45-1 @happy @blocked(O-06)
  Scenario: Duyệt thực đơn cần một người duyệt
    Given thực đơn "PENDING" do DDV tạo, cần 1 người duyệt
    When ND1 duyệt
    Then thực đơn chuyển "APPROVED"
    And kết quả kiểm quy tắc và phiên bản công thức đã gắn bị đóng băng
    And DDV nhận thông báo

  @AC-MENU-45-2 @happy
  Scenario: Màn hình duyệt hiện đủ thông tin
    When ND1 mở thực đơn chờ duyệt
    Then màn hình hiện lưới món theo ngày, món mặc định, điểm quy tắc
    And mỗi cảnh báo điểm phạt 3 hiện kèm lý do chấp nhận của người dựng

  @AC-MENU-45-3 @error
  Scenario: Người tạo tự duyệt
    Given thực đơn "PENDING" do ND1 tạo
    When ND1 duyệt
    Then hệ thống trả lỗi "ERR-SYS-403-01"

  @AC-MENU-45-4 @error
  Scenario: Trả lại thiếu lý do
    When ND1 chọn "Trả lại" và để trống lý do
    Then hệ thống trả lỗi "ERR-SYS-422-01" và thực đơn giữ "PENDING"

  @AC-MENU-45-5 @edge
  Scenario: Trả lại có lý do
    When ND1 trả lại với lý do "Thứ Tư có 3 món chiên, đề nghị đổi"
    Then thực đơn về "DRAFT", DDV sửa được và nhận thông báo kèm lý do
    And lần gửi duyệt sau bắt đầu vòng duyệt mới từ 0

  @AC-MENU-45-6 @edge
  Scenario: Công thức đổi sau khi thực đơn đã duyệt
    Given thực đơn "APPROVED" gắn công thức v1 của "Thịt kho trứng cút"
    When công thức v2 của món đó được duyệt và có hiệu lực trong tuần của thực đơn
    Then thực đơn vẫn gắn v1
```

## US-MENU-46 — Trang chờ duyệt

```gherkin
Feature: Trang tổng hợp nội dung chờ duyệt

  @AC-MENU-46-1 @happy @blocked(O-06,E2-Q7)
  Scenario: Xem theo loại
    Given có 3 món, 2 công thức, 2 giá bán, 3 đề nghị thay đổi, 2 thực đơn đang chờ duyệt
    When ND1 mở trang "Chờ duyệt"
    Then trang hiện 12 mục nhóm theo 5 loại, mỗi bộ lọc loại kèm số đếm đúng

  @AC-MENU-46-2 @happy
  Scenario: Duyệt hàng loạt
    Given ND1 tích chọn 3 món, trong đó 1 món ND1 là người sửa cuối
    When ND1 chọn "Duyệt mục đã chọn"
    Then 2 món chuyển "ACTIVE", 1 món giữ "PENDING"
    And kết quả báo "2 thành công, 1 lỗi" kèm "ERR-SYS-403-01" cho món bị lỗi

  @AC-MENU-46-3 @edge
  Scenario: Không có gì chờ duyệt
    Given không có mục nào chờ ND1 duyệt
    When ND1 mở trang "Chờ duyệt"
    Then trang ghi "Không có nội dung chờ duyệt"

  @AC-MENU-46-4 @edge
  Scenario: Mục đã được người khác xử lý
    Given ND1 và ND2 cùng mở một giá bán chờ duyệt
    And ND2 đã duyệt trước
    When ND1 chọn "Duyệt"
    Then hệ thống trả lỗi "ERR-SYS-409-02" và tải lại trạng thái hiện tại

  @AC-MENU-46-5 @error
  Scenario: Tài khoản không có quyền duyệt
    When DDV mở đường dẫn trang "Chờ duyệt"
    Then hệ thống trả lỗi "ERR-AUTH-403-02"

  @AC-MENU-46-6 @edge
  Scenario: Duyệt bằng quyền được uỷ đã hết hạn
    Given ND2 được ND1 uỷ quyền duyệt thực đơn đến hết hôm qua
    When ND2 duyệt một thực đơn
    Then hệ thống trả lỗi "ERR-AUTH-403-02"
```

## US-MENU-47 — Thông báo duyệt

```gherkin
Feature: Thông báo khi có nội dung chờ duyệt và khi có kết quả

  @AC-MENU-47-1 @happy
  Scenario: Người duyệt nhận thông báo
    When DDV gửi duyệt một thực đơn
    Then mỗi tài khoản có quyền duyệt thực đơn có 1 thông báo trạng thái "mới"
    And bấm thông báo mở thẳng màn hình chi tiết duyệt của thực đơn đó

  @AC-MENU-47-2 @happy
  Scenario: Người tạo nhận kết quả trả lại
    When ND1 trả lại thực đơn với lý do "Thứ Tư có 3 món chiên"
    Then DDV có 1 thông báo chứa nguyên văn lý do, bấm vào mở thực đơn ở chế độ sửa

  @AC-MENU-47-3 @edge
  Scenario: Gửi duyệt nhiều món một lần
    When DDV gửi duyệt 10 món trong một lần
    Then mỗi người duyệt nhận 1 thông báo gộp ghi "10 món chờ duyệt", không phải 10 thông báo

  @AC-MENU-47-4 @error
  Scenario: Người gửi không tự nhận thông báo chờ duyệt
    Given ND1 vừa có quyền tạo vừa có quyền duyệt
    When ND1 gửi duyệt một món do mình tạo
    Then ND1 không nhận thông báo chờ duyệt cho món đó
```

## US-MENU-48 — Công bố thực đơn

```gherkin
Feature: Công bố thực đơn đã duyệt

  @AC-MENU-48-1 @happy @blocked(E2-Q9)
  Scenario: Công bố
    Given thực đơn "APPROVED" có ngày phục vụ đầu tiên là D+5
    When DDV chọn "Công bố"
    Then thực đơn chuyển "PUBLISHED"
    And BT thấy thực đơn trong danh sách
    And tài khoản vai trò quản lý cơ sở và bếp trưởng nhận thông báo

  @AC-MENU-48-2 @error
  Scenario: Ngày phục vụ đầu tiên là hôm nay
    Given thực đơn "APPROVED" có ngày phục vụ đầu tiên là hôm nay
    When DDV chọn "Công bố"
    Then hệ thống trả lỗi "ERR-MENU-409-09" và thực đơn giữ "APPROVED"

  @AC-MENU-48-3 @edge
  Scenario: Ngày phục vụ đầu tiên là ngày mai
    Given thực đơn "APPROVED" có ngày phục vụ đầu tiên là D+1
    When DDV chọn "Công bố"
    Then thực đơn chuyển "PUBLISHED"

  @AC-MENU-48-4 @edge
  Scenario: Thực đơn chưa duyệt không có nút công bố
    Given thực đơn ở trạng thái "PENDING"
    When DDV mở thực đơn
    Then không có nút "Công bố"
```

## US-MENU-49 — Thu hồi và sửa lại

```gherkin
Feature: Thu hồi thực đơn đã công bố và sửa lại

  @AC-MENU-49-1 @happy @blocked(E2-Q8)
  Scenario: Thu hồi rồi sửa
    Given thực đơn ở trạng thái "PUBLISHED"
    When DDV chọn "Thu hồi" với lý do "Nhà cung cấp báo hết cá trắm cả tuần"
    Then thực đơn chuyển "WITHDRAWN" và BT không còn thấy trong danh sách
    When DDV chọn "Sửa"
    Then thực đơn về "DRAFT" và sửa được

  @AC-MENU-49-2 @error
  Scenario: Thu hồi thiếu lý do
    When DDV chọn "Thu hồi" với lý do 4 ký tự
    Then hệ thống trả lỗi "ERR-SYS-422-01" và thực đơn giữ "PUBLISHED"

  @AC-MENU-49-3 @edge
  Scenario: Sửa lại phải qua đủ chu trình
    Given thực đơn vừa về "DRAFT" sau thu hồi
    When DDV đổi 1 món
    Then thực đơn phải được kiểm, gửi duyệt, duyệt rồi mới công bố lại được

  @AC-MENU-49-4 @edge
  Scenario: Kết quả kiểm tính lại theo giá trị hiện hành
    Given sau khi thực đơn được công bố, thuộc tính vị chua của một món trong thực đơn đã đổi thành "Có"
    When DDV thu hồi, chọn "Sửa" và bộ kiểm chạy
    Then kết quả kiểm dùng thuộc tính mới của món đó

  @AC-MENU-49-5 @edge
  Scenario: Thu hồi phát sự kiện cho phân hệ khác
    When DDV thu hồi thực đơn
    Then hệ thống phát sự kiện "thực đơn bị thu hồi" mang mã thực đơn và lý do
```

## US-MENU-50 — Hai người duyệt khi điểm thấp

Toàn bộ story phụ thuộc [O-06]: không thực hiện được nếu Gia Phát chỉ có một người duyệt.

```gherkin
Feature: Thực đơn điểm thấp cần hai người duyệt

  @AC-MENU-50-1 @happy @blocked(O-06)
  Scenario: Hai người duyệt lần lượt
    Given thực đơn "PENDING" có điểm 74, cần 2 người duyệt
    When ND1 duyệt
    Then thực đơn vẫn "PENDING" và hiện "đã duyệt 1/2"
    When ND2 duyệt
    Then thực đơn chuyển "APPROVED"

  @AC-MENU-50-2 @error @blocked(O-06)
  Scenario: Một người duyệt hai lần
    Given ND1 đã duyệt thực đơn cần 2 người duyệt
    When ND1 duyệt lần nữa
    Then hệ thống trả lỗi "ERR-SYS-403-01" và thực đơn vẫn "đã duyệt 1/2"

  @AC-MENU-50-3 @edge
  Scenario: Điểm đúng bằng ngưỡng
    Given tham số "QUY_TAC_DIEM_TOI_THIEU" là 80 và thực đơn có điểm 80
    When DDV gửi duyệt
    Then thực đơn cần 1 người duyệt

  @AC-MENU-50-4 @edge @blocked(O-06)
  Scenario: Người thứ hai trả lại
    Given ND1 đã duyệt thực đơn cần 2 người duyệt
    When ND2 trả lại với lý do hợp lệ
    Then thực đơn về "DRAFT" và quyết định duyệt của ND1 không còn hiệu lực cho vòng sau
```

## US-MENU-51 — Sao chép thực đơn

```gherkin
Feature: Sao chép thực đơn từ tuần khác

  @AC-MENU-51-1 @happy
  Scenario: Sao chép sang tuần mới
    Given thực đơn tuần 09/11 của "Suất 40.000đ" có đủ 42 ô
    When DDV sao chép sang tuần 23/11
    Then thực đơn mới ở trạng thái "DRAFT" với 42 ô giống nguồn
    And mỗi ô gắn công thức hiệu lực tại ngày phục vụ mới
    And món mặc định của từng ngày được sao chép

  @AC-MENU-51-2 @error
  Scenario: Tuần đích đã có thực đơn
    Given tuần 23/11 đã có thực đơn của "Suất 40.000đ"
    When DDV sao chép sang tuần 23/11
    Then hệ thống trả lỗi "ERR-MENU-409-06"

  @AC-MENU-51-3 @edge
  Scenario: Thực đơn nguồn có món đã ngừng dùng
    Given thực đơn nguồn có "Mực xào" ở T3 và "Mực xào" đã "INACTIVE"
    When DDV sao chép
    Then ô tương ứng của T3 để trống
    And màn hình liệt kê "Mực xào" trong danh sách món bị bỏ

  @AC-MENU-51-4 @edge
  Scenario: Thực đơn sao chép được kiểm ngay
    When DDV sao chép một thực đơn
    Then bộ kiểm chạy trên bản sao và bảng kiểm hiện kết quả theo quy tắc hiện hành
```

## US-MENU-52 — Lịch sử món đã dùng

```gherkin
Feature: Lịch sử món 4 tuần gần nhất khi chọn món

  @AC-MENU-52-1 @happy
  Scenario: Hiện ngày đã dùng
    Given "Cá kho" đã xuất hiện ở T4 11/11 trong thực đơn "PUBLISHED" của "Suất 40.000đ"
    When DDV mở hộp chọn món chính cho tuần 16/11 của "Suất 40.000đ"
    Then dòng "Cá kho" ghi "đã dùng: T4 11/11"

  @AC-MENU-52-2 @edge
  Scenario: Món chưa dùng trong 4 tuần
    When DDV mở hộp chọn món
    Then món không xuất hiện trong 4 tuần trước ghi "chưa dùng 4 tuần gần nhất"

  @AC-MENU-52-3 @edge
  Scenario: Không tính loại suất khác
    Given "Cá kho" chỉ xuất hiện trong thực đơn của "Suất 35.000đ"
    When DDV mở hộp chọn món cho "Suất 40.000đ"
    Then dòng "Cá kho" ghi "chưa dùng 4 tuần gần nhất"

  @AC-MENU-52-4 @error
  Scenario: Không tính thực đơn nháp và đã huỷ
    Given "Cá kho" chỉ xuất hiện trong một thực đơn "DRAFT" của tuần trước
    When DDV mở hộp chọn món
    Then dòng "Cá kho" ghi "chưa dùng 4 tuần gần nhất"
```

## US-MENU-53 — Xuất PDF

```gherkin
Feature: Xuất thực đơn tuần ra PDF

  @AC-MENU-53-1 @happy
  Scenario: Xuất thực đơn đã công bố
    Given thực đơn "PUBLISHED" 6 ngày
    When DDV chọn "Xuất PDF"
    Then tệp PDF có lưới 6 cột ngày × 7 dòng vị trí với tên món, đánh dấu món mặc định
    And tiêu đề ghi tên loại suất và khoảng ngày của tuần

  @AC-MENU-53-2 @edge
  Scenario: Xuất thực đơn chưa công bố
    Given thực đơn ở trạng thái "DRAFT"
    When DDV chọn "Xuất PDF"
    Then mỗi trang của tệp có dòng "BẢN NHÁP — CHƯA CÔNG BỐ"

  @AC-MENU-53-3 @error
  Scenario: Vai trò chỉ xem xuất thực đơn chưa công bố
    When BT gọi lệnh xuất PDF của thực đơn "DRAFT"
    Then hệ thống trả lỗi "ERR-SYS-404-01"

  @AC-MENU-53-4 @edge
  Scenario: Tệp không chứa giá và cost
    When DDV xuất PDF một thực đơn
    Then tệp không có giá bán, giá nhập hay cost
```

---

## Phát sinh khi viết tiêu chí nghiệm thu

Các điểm dưới đây chưa có trong SRS v0.1.0; kịch bản tương ứng viết theo cách xử lý ghi ở cột giữa. **Cả 10 điểm đã được đưa vào SRS v0.2.0 (mục 4.4)** ngày 10/11/2026; cách xử lý vẫn là đề xuất của BA, chưa có người nghiệp vụ duyệt.

| # | Điểm phát sinh | Kịch bản đang viết theo | Kịch bản |
| :--- | :--- | :--- | :--- |
| 1 | Bỏ cờ "ít dầu mỡ" của phương pháp chế biến khi đang có món Healthy dùng phương pháp đó | Chặn, trả `ERR-SYS-409-01` kèm danh sách món | AC-MENU-06-3 |
| 2 | Sửa hoặc huỷ giá đã hiệu lực: SRS có quy tắc `BR-CAT-016` nhưng chưa có mã lỗi riêng | Chặn, trả `ERR-MENU-409-10` (mã thêm ở SRS v0.2.0) | AC-MENU-21-4 |
| 3 | Ngừng dùng món đang nằm trong thực đơn **nháp** | Cho ngừng; thực đơn nháp bị chặn ở lần gửi duyệt | AC-MENU-28-4 |
| 4 | Ngày nghỉ có ngắt chuỗi "ngày liên tiếp" không | Không ngắt: đếm theo ngày phục vụ | AC-MENU-37-3 |
| 5 | Gửi duyệt nhiều mục một lần sinh mấy thông báo | Một thông báo gộp cho mỗi người duyệt | AC-MENU-47-3 |
| 6 | Người vừa có quyền tạo vừa có quyền duyệt có nhận thông báo cho nội dung của chính mình không | Không | AC-MENU-47-4 |
| 7 | Lịch sử món 4 tuần tính những thực đơn nào | Chỉ thực đơn đã công bố, cùng loại suất | AC-MENU-52-3, 52-4 |
| 8 | PDF thực đơn có chứa giá bán không | Không | AC-MENU-53-4 |
| 9 | Món mặc định có được sao chép cùng thực đơn không | Có | AC-MENU-51-1 |
| 10 | Người thứ hai trả lại thì quyết định của người thứ nhất ra sao | Mất hiệu lực; vòng sau duyệt lại từ đầu | AC-MENU-50-4 |

## Phần còn thiếu

| Nội dung | Chờ |
| :--- | :--- |
| Bộ kịch bản cho từng quy tắc thực đơn (mỗi quy tắc 1 ca đạt, 1 ca vi phạm; khoảng 60–70 kịch bản) | DL-01 |
| Kịch bản cho `US-MENU-39` theo phương án cuối cùng | [E2-Q1] |
| Kịch bản cho nhiều cỡ định lượng | [O-02] |
| Rà lại mọi kịch bản có thẻ `@blocked` | Điểm mở tương ứng |
