---
id: DOC-E7-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria E7 (Given / When / Then)
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria E7 (Given / When / Then)

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

## US-DLV-001 / FR-DLV-NOTE-001

### AC-E7-001-1: Thành công có điều kiện

```gherkin
Given số chốt synthetic 100, số giao 98, nguồn được xác nhận hợp lệ theo giả định
When lập phiếu giao 98
Then giữ số chốt 100 và giao 98; không sửa order
```

Trạng thái kiểm: BLOCKED. Gate happy path: E6-CG-05/06/08; E7-Q02.

### AC-E7-001-2: Lỗi nghiệp vụ

```gherkin
Given số giao -1
When lưu phiếu
Then ERR-DLV-422-01; không tạo phiếu
```

Trạng thái kiểm: NOT RUN. Gate happy path: E6-CG-05/06/08; E7-Q02.

### AC-E7-001-3: Biên / an toàn

```gherkin
Given order revision nguồn đã thay
When lưu phiếu tham chiếu bản cũ
Then ERR-E7-409-01; không tự chuyển revision
```

Trạng thái kiểm: NOT RUN. Gate happy path: E6-CG-05/06/08; E7-Q02.

## US-DLV-002 / FR-DLV-ACK-001

### AC-E7-002-1: Thành công có điều kiện

```gherkin
Given phiếu synthetic giao 98 và quyền link được xác minh theo policy giả định hợp lệ
When nhập nhận 98 và xác nhận
Then lưu số nhận 98, actor/thời điểm và version
```

Trạng thái kiểm: BLOCKED. Gate happy path: E6-CG-01/08; E7-Q01; Q-13.

### AC-E7-002-2: Lỗi nghiệp vụ

```gherkin
Given link bị thu hồi hoặc không đủ scope
When xác nhận nhận
Then ERR-E7-403-01; không ghi số nhận
```

Trạng thái kiểm: NOT RUN. Gate happy path: E6-CG-01/08; E7-Q01; Q-13.

### AC-E7-002-3: Biên / an toàn

```gherkin
Given khách không trả lời
When đến thời điểm chờ xử lý
Then BLOCKED Q-13; không tự lấy số giao/chốt làm số nhận
```

Trạng thái kiểm: BLOCKED. Gate happy path: E6-CG-01/08; E7-Q01; Q-13.

## US-DLV-003 / FR-DLV-DIFF-001

### AC-E7-003-1: Thành công có điều kiện

```gherkin
Given phiếu synthetic giao 100 nhận 98 có bằng chứng
When lập biên bản
Then ghi chênh 2, chưa tự giảm tiền
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q02; E6-CG-08.

### AC-E7-003-2: Lỗi nghiệp vụ

```gherkin
Given thiếu bằng chứng nhận
When kết luận chênh lệch đã thống nhất
Then ERR-DLV-422-02; giữ nháp
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q02; E6-CG-08.

### AC-E7-003-3: Biên / an toàn

```gherkin
Given phiếu thuộc kỳ khóa
When sửa số làm thay đổi kỳ
Then ERR-FIN-409-02; cần mở lại hợp lệ
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q02; E6-CG-08.

## US-DLV-004 / FR-DLV-RES-001

### AC-E7-004-1: Thành công có điều kiện

```gherkin
Given thiếu synthetic 2 suất, thỏa thuận bù 2 và phiếu bù được xác nhận
When ghi xử lý
Then giữ phiếu gốc, liên kết bù, không đếm hai lần
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q02/03; CK-Q07–09 khi liên quan CK.

### AC-E7-004-2: Lỗi nghiệp vụ

```gherkin
Given chưa có thỏa thuận
When áp giảm trừ
Then ERR-DLV-422-02; không đổi phải trả
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q02/03; CK-Q07–09 khi liên quan CK.

### AC-E7-004-3: Biên / an toàn

```gherkin
Given phần thiếu đã giao bù
When thêm giảm trừ cùng phần thiếu
Then BLOCKED E7-Q02; không tự cộng hai cách
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q02/03; CK-Q07–09 khi liên quan CK.

## US-FIN-005 / FR-FIN-REV-001

### AC-E7-005-1: Thành công có điều kiện

```gherkin
Given synthetic số tính tiền 100 có căn cứ, giá chụp 40000 gồm VAT thử 8%, CK riêng 200000
When tính doanh thu
Then phải trả 4000000, CK 200000 riêng, trước VAT 4000000/1.08 trước làm tròn; không phải trả 3800000
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q03/04; Q-13; E6-CG-04/05/07.

### AC-E7-005-2: Lỗi nghiệp vụ

```gherkin
Given context giá UNKNOWN hoặc số tính tiền không có căn cứ
When tính chính thức
Then ERR-FIN-422-01; chưa xác định, không điền 0
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q03/04; Q-13; E6-CG-04/05/07.

### AC-E7-005-3: Biên / an toàn

```gherkin
Given giá hiện tại đổi 42000 sau order
When tính lại cùng snapshot
Then vẫn dùng giá chụp 40000
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q03/04; Q-13; E6-CG-04/05/07.

## US-FIN-006 / FR-FIN-VIEW-001

### AC-E7-006-1: Thành công có điều kiện

```gherkin
Given hai bản tính synthetic hợp lệ trong scope
When lọc khách/ngày
Then trả đúng tập và nguồn số tính tiền/giá chụp
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q04/08; E6-CG-08.

### AC-E7-006-2: Lỗi nghiệp vụ

```gherkin
Given khách ngoài scope
When tra cứu
Then ERR-E7-404-01; không lộ tên hoặc tổng
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q04/08; E6-CG-08.

### AC-E7-006-3: Biên / an toàn

```gherkin
Given khoảng ngày không có dữ liệu
When tra cứu
Then trả danh sách rỗng, không tạo calculation qua GET
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q04/08; E6-CG-08.

## US-FIN-007 / FR-FIN-REC-001

### AC-E7-007-1: Thành công có điều kiện

```gherkin
Given synthetic tập doanh thu tháng có nguồn hợp lệ
When lập kỳ
Then kỳ nháp giữ tập nguồn và tổng, chưa tự thống nhất
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; Q-13; E6-CG-08.

### AC-E7-007-2: Lỗi nghiệp vụ

```gherkin
Given fromDate sau toDate
When lập kỳ
Then ERR-FIN-422-02; không tạo kỳ
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; Q-13; E6-CG-08.

### AC-E7-007-3: Biên / an toàn

```gherkin
Given có phiếu chưa được khách xác nhận
When chuẩn bị chốt kỳ
Then BLOCKED Q-13; dòng chờ không bị bỏ qua
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; Q-13; E6-CG-08.

## US-FIN-008 / FR-FIN-AGRE-001

### AC-E7-008-1: Thành công có điều kiện

```gherkin
Given kỳ synthetic đủ nguồn và biên bản khách khớp revision
When ghi thống nhất
Then lưu evidence/revision; số đã thu không đổi
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; Q-13; E6-CG-01/08.

### AC-E7-008-2: Lỗi nghiệp vụ

```gherkin
Given tổng biên bản khác tổng kỳ
When ghi thống nhất
Then ERR-FIN-422-02; giữ chưa thống nhất
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; Q-13; E6-CG-01/08.

### AC-E7-008-3: Biên / an toàn

```gherkin
Given nguồn kỳ thay khi khách đang xác nhận
When ghi theo bản cũ
Then ERR-E7-409-01; không áp bằng chứng cũ cho bản mới
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; Q-13; E6-CG-01/08.

## US-FIN-009 / FR-FIN-RCPT-001

### AC-E7-009-1: Thành công có điều kiện

```gherkin
Given kỳ mở synthetic phải trả 4000000, chứng từ thu 1000000 hợp lệ
When ghi thu 1000000
Then đã thu 1000000, còn 3000000; phải trả gốc không đổi
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q06; E7-Q05 về thu sau khóa.

### AC-E7-009-2: Lỗi nghiệp vụ

```gherkin
Given tiền thu -1
When ghi thu
Then ERR-FIN-422-03; không tạo khoản thu
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q06; E7-Q05 về thu sau khóa.

### AC-E7-009-3: Biên / an toàn

```gherkin
Given mất phản hồi lệnh thu
When định gửi thao tác mới
Then hiện chưa rõ kết quả, đối chiếu chứng từ; replay BLOCKED E7-Q08
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q06; E7-Q05 về thu sau khóa.

## US-FIN-010 / FR-FIN-LOCK-001

### AC-E7-010-1: Thành công có điều kiện

```gherkin
Given kỳ synthetic đã thống nhất và đủ điều kiện khóa giả định được duyệt
When khóa kỳ
Then snapshot giữ nguyên, mọi sửa số bị chặn
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; Q-13.

### AC-E7-010-2: Lỗi nghiệp vụ

```gherkin
Given còn nguồn chưa xác định
When khóa kỳ
Then ERR-FIN-422-02; không khóa
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; Q-13.

### AC-E7-010-3: Biên / an toàn

```gherkin
Given hai lệnh khóa cùng version
When ghi cạnh tranh
Then một chuyển trạng thái; lệnh còn lại ERR-E7-409-01
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; Q-13.

## US-FIN-011 / FR-FIN-RREQ-001

### AC-E7-011-1: Thành công có điều kiện

```gherkin
Given kỳ synthetic khóa, lý do hợp lệ và bằng chứng
When gửi đề nghị
Then yêu cầu chờ; số liệu kỳ vẫn khóa
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; O-06 về ủy quyền giữ mở.

### AC-E7-011-2: Lỗi nghiệp vụ

```gherkin
Given lý do dưới 10 ký tự
When gửi đề nghị
Then ERR-FIN-422-02; không lưu
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; O-06 về ủy quyền giữ mở.

### AC-E7-011-3: Biên / an toàn

```gherkin
Given đề nghị chưa duyệt
When sửa doanh thu kỳ
Then ERR-FIN-409-02; chờ không là mở
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; O-06 về ủy quyền giữ mở.

## US-FIN-012 / FR-FIN-RDEC-001

### AC-E7-012-1: Thành công có điều kiện

```gherkin
Given Giám đốc synthetic khác người lập/sửa cuối, yêu cầu hợp lệ
When duyệt đúng version
Then kỳ REOPENED, snapshot khóa cũ còn nguyên
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q05; O-06 không tự cấp người thay.

### AC-E7-012-2: Lỗi nghiệp vụ

```gherkin
Given người duyệt là người lập hoặc không phải Giám đốc
When duyệt
Then ERR-E7-403-01; kỳ vẫn khóa
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; O-06 không tự cấp người thay.

### AC-E7-012-3: Biên / an toàn

```gherkin
Given Giám đốc chọn từ chối
When ghi quyết định
Then yêu cầu từ chối, kỳ LOCKED, số liệu không đổi
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q05; O-06 không tự cấp người thay.

## US-FIN-013 / FR-FIN-MISA-001

### AC-E7-013-1: Thành công có điều kiện

```gherkin
Given kỳ synthetic hợp lệ, mẫu nhập/mapping MISA đã duyệt trong môi trường thử
When xuất và thử nhập MISA
Then file được nhận; lưu evidence nhập, không ghi đã thu
```

Trạng thái kiểm: BLOCKED. Gate happy path: E7-Q07/08; E7-Q05 về kỳ được phép xuất.

### AC-E7-013-2: Lỗi nghiệp vụ

```gherkin
Given chưa có mẫu chính thức
When yêu cầu xuất
Then ERR-FIN-422-04; không file/cột giả
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q07/08; E7-Q05 về kỳ được phép xuất.

### AC-E7-013-3: Biên / an toàn

```gherkin
Given kỳ đã mở lại sau xuất
When xem file cũ
Then hiện revision cũ và cần rà lại, không sửa bytes cũ hoặc coi hiện hành
```

Trạng thái kiểm: NOT RUN. Gate happy path: E7-Q07/08; E7-Q05 về kỳ được phép xuất.
