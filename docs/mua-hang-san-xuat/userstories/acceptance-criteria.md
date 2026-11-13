---
id: DOC-E11-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## US-PUR-001: Lập nhu cầu nguyên liệu

FR-PUR-DEM-001; BR-PUR-001; gate E6 CG06, ORD-Q10/14; E11-Q01.

### AC-PUR-001-1: Thành công có điều kiện

```gherkin
Scenario: Lập nhu cầu nguyên liệu (trường hợp 1)
  Given Nguồn có 100 suất × 70 g, hệ số 1000 g/kg đã xác nhận
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập nhu cầu nguyên liệu
  Then Nhu cầu gộp 7000 g = 7 kg; lượng mua ròng chưa xác định
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-001-2: Lỗi nghiệp vụ

```gherkin
Scenario: Lập nhu cầu nguyên liệu (trường hợp 2)
  Given Thiếu hệ số g/kg
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập nhu cầu nguyên liệu
  Then Chặn tổng hợp khác đơn vị; không coi hệ số là 1
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-001-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Lập nhu cầu nguyên liệu (trường hợp 3)
  Given Kế hoạch đổi revision khi đang xem
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập nhu cầu nguyên liệu
  Then Đánh dấu nguồn cũ; không dùng số cũ làm nhu cầu hiện hành
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-002: Lập đơn mua nháp

FR-PUR-POD-001; BR-PUR-002; gate E11-Q01/02/13/14.

### AC-PUR-002-1: Thành công có điều kiện

```gherkin
Scenario: Lập đơn mua nháp (trường hợp 1)
  Given NCC synthetic do người lập chọn, lượng 2 kg; giá cuối 108000 đ/kg
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập đơn mua nháp
  Then Nháp có tiền hàng 216000 đ khi căn cứ giá đủ; chưa phát hành
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-002-2: Lỗi nghiệp vụ

```gherkin
Scenario: Lập đơn mua nháp (trường hợp 2)
  Given Số lượng âm hoặc thiếu NCC
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập đơn mua nháp
  Then Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-002-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Lập đơn mua nháp (trường hợp 3)
  Given Giá UNKNOWN hoặc chưa rõ VAT phải trả
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập đơn mua nháp
  Then Giữ chưa xác định, không coi giá hoặc VAT bằng 0
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-003: Kiểm cổng phát hành đơn mua

FR-PUR-POG-001; BR-PUR-003; gate E11-Q02; O-06.

### AC-PUR-003-1: Thành công có điều kiện

```gherkin
Scenario: Kiểm cổng phát hành đơn mua (trường hợp 1)
  Given Đơn nháp chưa có chính sách duyệt
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng phát hành đơn mua
  Then Trả BLOCKED kèm E11-Q02; đơn giữ DRAFT
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-003-2: Lỗi nghiệp vụ

```gherkin
Scenario: Kiểm cổng phát hành đơn mua (trường hợp 2)
  Given Client tự gắn APPROVED
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng phát hành đơn mua
  Then Không công nhận trạng thái do client tự khai
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-003-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Kiểm cổng phát hành đơn mua (trường hợp 3)
  Given Tải lại cổng nhiều lần
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng phát hành đơn mua
  Then GET không tạo quyết định, không gửi đơn cho NCC
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-004: Kiểm phạm vi quản lý lô

FR-PUR-LOT-001; BR-PUR-004; gate E11-Q03.

### AC-PUR-004-1: Thành công có điều kiện

```gherkin
Scenario: Kiểm phạm vi quản lý lô (trường hợp 1)
  Given Nguyên liệu thuộc FROZEN hoặc DRY
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm phạm vi quản lý lô
  Then Hiển thị thuộc phạm vi lô; chi tiết lô còn chờ
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-004-2: Lỗi nghiệp vụ

```gherkin
Scenario: Kiểm phạm vi quản lý lô (trường hợp 2)
  Given Hàng tươi được gửi yêu cầu quản lý lô
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm phạm vi quản lý lô
  Then Không tạo lô cho hàng tươi
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-004-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Kiểm phạm vi quản lý lô (trường hợp 3)
  Given Thiếu loại bảo quản
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm phạm vi quản lý lô
  Then Không suy là hàng khô; hiển thị chưa xác định
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-005: Ghi phiếu nhận hàng nháp

FR-PUR-RCV-001; BR-PUR-005; gate E11-Q04/13.

### AC-PUR-005-1: Thành công có điều kiện

```gherkin
Scenario: Ghi phiếu nhận hàng nháp (trường hợp 1)
  Given Đặt 10 kg, nhận 8 kg; người nhận khai chấp nhận 7 kg
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi phiếu nhận hàng nháp
  Then Hiện riêng 10/8/7 kg; 1 kg chưa chấp nhận, 2 kg chưa nhận; chưa tự trả hàng
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-005-2: Lỗi nghiệp vụ

```gherkin
Scenario: Ghi phiếu nhận hàng nháp (trường hợp 2)
  Given Chấp nhận 9 kg khi chỉ nhận 8 kg
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi phiếu nhận hàng nháp
  Then Chặn dữ liệu mâu thuẫn, không ghi phiếu
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-005-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Ghi phiếu nhận hàng nháp (trường hợp 3)
  Given Hai lần nhận cùng đơn
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi phiếu nhận hàng nháp
  Then Giữ tham chiếu từng lần; chưa tự quyết hoàn tất khi policy chưa có
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-006: Gắn ảnh chứng từ vào phiếu

FR-PUR-DOC-001; BR-PUR-006; gate E11-Q05/13; E1-Q01.

### AC-PUR-006-1: Thành công có điều kiện

```gherkin
Scenario: Gắn ảnh chứng từ vào phiếu (trường hợp 1)
  Given Ảnh synthetic thuộc phiếu/cơ sở và MIME hợp lệ theo E1
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện gắn ảnh chứng từ vào phiếu
  Then Gắn được tham chiếu ảnh; không chuyển phiếu sang đã nhận chính thức
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-006-2: Lỗi nghiệp vụ

```gherkin
Scenario: Gắn ảnh chứng từ vào phiếu (trường hợp 2)
  Given File của cơ sở ngoài scope
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện gắn ảnh chứng từ vào phiếu
  Then Không lộ nội dung/URL tệp, không gắn chéo
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-006-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Gắn ảnh chứng từ vào phiếu (trường hợp 3)
  Given Liên kết ảnh hết hạn 15 phút theo E1
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện gắn ảnh chứng từ vào phiếu
  Then Kiểm quyền để cấp lại liên kết; không công khai ảnh lâu dài
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-007: Xem công nợ nhà cung cấp

FR-PUR-APV-001; BR-PUR-007; gate E11-Q06/04.

### AC-PUR-007-1: Thành công có điều kiện

```gherkin
Scenario: Xem công nợ nhà cung cấp (trường hợp 1)
  Given Có 216000 đ nghĩa vụ và 100000 đ thanh toán có căn cứ, đầu kỳ 0 đã xác nhận
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện xem công nợ nhà cung cấp
  Then Dư 116000 đ theo fixture đã đủ căn cứ; không giảm bởi CK khách
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-007-2: Lỗi nghiệp vụ

```gherkin
Scenario: Xem công nợ nhà cung cấp (trường hợp 2)
  Given Thiếu số dư đầu kỳ
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện xem công nợ nhà cung cấp
  Then Không báo tổng công nợ hoàn chỉnh
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-007-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Xem công nợ nhà cung cấp (trường hợp 3)
  Given Đơn có CK khách 5 %
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện xem công nợ nhà cung cấp
  Then Không trừ 5 % khỏi phải trả NCC; không tự giảm số khách phải trả
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-008: Đối chiếu dự toán và thực mua

FR-COST-BUY-001; BR-PUR-008; gate E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04.

### AC-PUR-008-1: Thành công có điều kiện

```gherkin
Scenario: Đối chiếu dự toán và thực mua (trường hợp 1)
  Given Fixture minh họa có tỷ lệ cùng mẫu số đã được xác nhận: 50 % và 53 %
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện đối chiếu dự toán và thực mua
  Then Chênh hiển thị 3 điểm phần trăm; không gọi tăng tương đối 6 % là tiêu chí R11
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-008-2: Lỗi nghiệp vụ

```gherkin
Scenario: Đối chiếu dự toán và thực mua (trường hợp 2)
  Given Thực mua của cơ sở khác hoặc ngày chưa phân bổ
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện đối chiếu dự toán và thực mua
  Then Không ghép với dự toán để kết luận đạt
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-008-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Đối chiếu dự toán và thực mua (trường hợp 3)
  Given Mẫu số bằng 0 hoặc chưa biết
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện đối chiếu dự toán và thực mua
  Then Tỷ lệ và chênh null; kết luận chưa xác định
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-009: Giải thích nguồn chênh lệch

FR-COST-BEX-001; BR-PUR-009; gate E11-Q07/08/14.

### AC-PUR-009-1: Thành công có điều kiện

```gherkin
Scenario: Giải thích nguồn chênh lệch (trường hợp 1)
  Given Hai dòng cùng nguyên liệu và đơn vị có nguồn được phép đọc
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện giải thích nguồn chênh lệch
  Then Hiện lượng và giá hai phía, liên kết chứng từ; không ghi đè dự toán
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-009-2: Lỗi nghiệp vụ

```gherkin
Scenario: Giải thích nguồn chênh lệch (trường hợp 2)
  Given Người không có cost.cost.read yêu cầu tiền
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện giải thích nguồn chênh lệch
  Then Không trả tiền hoặc cost trong body/lỗi/log hiển thị
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-009-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Giải thích nguồn chênh lệch (trường hợp 3)
  Given Giá E3 mới có hiệu lực sau bản dự toán
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện giải thích nguồn chênh lệch
  Then Giữ giá snapshot dự toán; giá mới không sửa lịch sử
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-010: Lập phân ca nháp

FR-PLAN-SHF-001; BR-PUR-010; gate E11-Q09; E6 CG06.

### AC-PUR-010-1: Thành công có điều kiện

```gherkin
Scenario: Lập phân ca nháp (trường hợp 1)
  Given Ca synthetic, phân công công việc cho mã nhân sự giả thuộc scope
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập phân ca nháp
  Then Giữ bản nháp; trạng thái bắt đầu sản xuất E6 không đổi
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-010-2: Lỗi nghiệp vụ

```gherkin
Scenario: Lập phân ca nháp (trường hợp 2)
  Given Nhân sự ngoài cơ sở được phép
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập phân ca nháp
  Then Từ chối gắn vào ca
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-010-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Lập phân ca nháp (trường hợp 3)
  Given Plan revision thay đổi
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập phân ca nháp
  Then Đánh dấu cần rà soát phân công; không tự kế thừa xác nhận bản cũ
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-011: Ghi kiểm tra trước giao

FR-PLAN-QCG-001; BR-PUR-011; gate E11-Q10; E7-Q02; E6 CG06.

### AC-PUR-011-1: Thành công có điều kiện

```gherkin
Scenario: Ghi kiểm tra trước giao (trường hợp 1)
  Given Checklist mẫu có mục kiểm hộp chưa kiểm
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi kiểm tra trước giao
  Then Hiện chưa đủ căn cứ giao; không tự chuyển E7 sang giao thành công
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-011-2: Lỗi nghiệp vụ

```gherkin
Scenario: Ghi kiểm tra trước giao (trường hợp 2)
  Given Client bỏ mục không đạt khỏi yêu cầu
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi kiểm tra trước giao
  Then Không kết luận đủ dựa trên tập mục thiếu
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-011-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Ghi kiểm tra trước giao (trường hợp 3)
  Given Tất cả mục mẫu được đánh đạt nhưng policy chưa duyệt
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi kiểm tra trước giao
  Then Vẫn BLOCKED E11-Q10; không phát sinh phiếu giao
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-012: Ghi sổ mẫu lưu theo bữa

FR-PLAN-SMP-001; BR-PUR-012; gate E11-Q11; E6 CG06.

### AC-PUR-012-1: Thành công có điều kiện

```gherkin
Scenario: Ghi sổ mẫu lưu theo bữa (trường hợp 1)
  Given Tập bữa synthetic đã xác nhận có 10 bữa, 9 bữa có bản ghi mẫu
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi sổ mẫu lưu theo bữa
  Then Độ phủ bản ghi 90 %, liệt kê 1 bữa thiếu; chưa đạt mục tiêu 100 % R11
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-012-2: Lỗi nghiệp vụ

```gherkin
Scenario: Ghi sổ mẫu lưu theo bữa (trường hợp 2)
  Given Thiếu mã bữa hoặc cơ sở
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi sổ mẫu lưu theo bữa
  Then Chặn bản ghi không truy được nguồn
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-012-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Ghi sổ mẫu lưu theo bữa (trường hợp 3)
  Given Hai mẫu cùng bữa và 1 bữa khác chưa có mẫu
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện ghi sổ mẫu lưu theo bữa
  Then Đếm bữa phân biệt, không lấy số mẫu chia số bữa để báo đủ
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-013: Lập ứng viên món thay thế

FR-MENU-SUB-001; BR-PUR-013; gate E11-Q12/15; O-02.

### AC-PUR-013-1: Thành công có điều kiện

```gherkin
Scenario: Lập ứng viên món thay thế (trường hợp 1)
  Given Đổi một món MAIN sang món MAIN đang được phép dùng
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập ứng viên món thay thế
  Then Tạo ứng viên DRAFT; thực đơn công bố không đổi
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-013-2: Lỗi nghiệp vụ

```gherkin
Scenario: Lập ứng viên món thay thế (trường hợp 2)
  Given Đổi món MAIN sang SOUP
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập ứng viên món thay thế
  Then Chặn khác vai trò, không tạo thay thế hợp lệ
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-013-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Lập ứng viên món thay thế (trường hợp 3)
  Given Món có tên giống nhưng vai trò khác
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện lập ứng viên món thay thế
  Then So mã vai trò, không so chuỗi tên món
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-014: Kiểm lại ứng viên thay món

FR-MENU-SCK-001; BR-PUR-014; gate DL-01; E11-Q15; O-01/O-02; CK/DATA-COST.

### AC-PUR-014-1: Thành công có điều kiện

```gherkin
Scenario: Kiểm lại ứng viên thay món (trường hợp 1)
  Given Ứng viên có đủ nhãn dị ứng, rule và giá trong fixture đã duyệt
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm lại ứng viên thay món
  Then Có đủ ba kết quả đúng candidateVersion; vẫn chưa được công bố
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-014-2: Lỗi nghiệp vụ

```gherkin
Scenario: Kiểm lại ứng viên thay món (trường hợp 2)
  Given Thiếu giá hoặc thiếu căn cứ dị ứng
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm lại ứng viên thay món
  Then BLOCKED; không trả đạt dù quy tắc khác đạt
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-014-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Kiểm lại ứng viên thay món (trường hợp 3)
  Given Người dùng đổi ứng viên sau lần kiểm
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm lại ứng viên thay món
  Then Kết quả cũ không hợp lệ; chạy lại cả ba kiểm
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

## US-PUR-015: Kiểm cổng chuyển duyệt MENU

FR-MENU-SGT-001; BR-PUR-015; gate E11-Q12/13; DL-01; E6 CG05/06/07.

### AC-PUR-015-1: Thành công có điều kiện

```gherkin
Scenario: Kiểm cổng chuyển duyệt MENU (trường hợp 1)
  Given Kết quả dị ứng, rule, cost đúng phiên bản; MENU vẫn chưa duyệt
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng chuyển duyệt menu
  Then Hiện cần qua cổng MENU; không tự công bố hoặc sửa kế hoạch
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-015-2: Lỗi nghiệp vụ

```gherkin
Scenario: Kiểm cổng chuyển duyệt MENU (trường hợp 2)
  Given Quy tắc cứng vi phạm hoặc thiếu cost
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng chuyển duyệt menu
  Then Không được chuyển như đã đạt; giữ ứng viên
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

### AC-PUR-015-3: Biên hoặc thay đổi nguồn

```gherkin
Scenario: Kiểm cổng chuyển duyệt MENU (trường hợp 3)
  Given Nguồn thay đổi giữa kiểm và chuyển
  And Người thao tác có quyền trên cơ sở synthetic, trừ ca chủ ý kiểm thiếu quyền
  When Người thao tác thực hiện kiểm cổng chuyển duyệt menu
  Then Từ chối dùng kết quả cũ; yêu cầu kiểm lại, không bỏ qua MENU
  And Không sửa nguồn E2/E3/E6/E7 hoặc tự đóng câu hỏi mở
```

