---
id: DOC-E7-USER-GUIDE
title: Hướng dẫn vận hành E7
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e7]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E7: Giao nhận và doanh thu

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Bếp trưởng, đại diện khách, kế toán doanh thu, Giám đốc. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-DLV-001: Lập phiếu giao nhận

[Use case gốc](usecases/UC-DLV-001.md)

1. Bếp trưởng chọn đơn hàng tại UI-E7-01; hệ thống hiển thị khách, điểm, ngày/ca và số chốt từ nguồn được phép đọc.
2. Bếp trưởng chỉ rõ orderId, orderRevisionRef và planRevisionRef, nhập số giao thực tế và bằng chứng giao.
3. Hệ thống đối chiếu đơn hàng với điểm/khách/cơ sở từ nguồn tin cậy, kiểm quyền lập phiếu và tình trạng các gate nguồn.
4. Hệ thống kiểm số giao nguyên không âm và các revision tham chiếu còn phù hợp, không tự chuyển sang bản nguồn mới.
5. Hệ thống ghi phiếu, bằng chứng và dấu vết người/thời điểm; giữ số chốt và số giao thành hai giá trị riêng.
6. Hệ thống trả phiếu chờ khách xác nhận cùng nguồn tham chiếu để bếp trưởng đối chiếu.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Số giao âm, không nguyên hoặc sai tham chiếu: hệ thống trả ERR-DLV-422-01 và yêu cầu sửa đầu vào; chưa tạo phiếu.
- 4b. Revision đơn hàng đã thay: hệ thống trả ERR-E7-409-01, yêu cầu tải lại để đối chiếu; không chuyển nguồn hoặc ghi đè.
- 3a. Phiên hết hạn: hệ thống trả ERR-E7-401-01, yêu cầu đăng nhập lại; chưa ghi phiếu, không tự gửi lại lệnh.
- 3b. Thiếu quyền hoặc ngoài phạm vi: hệ thống trả ERR-E7-403-01 hoặc ERR-E7-404-01 tương ứng; không trả dữ liệu ngoài phạm vi và không tạo phiếu.
- 3c. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; phiếu chưa được tạo, không điền số thiếu bằng 0.
- 5a. Mất phản hồi khi lưu: hệ thống hiển thị kết quả chưa rõ; bếp trưởng đối chiếu phiếu/nguồn trước lệnh mới. Trạng thái lưu chưa xác định, replay vẫn BLOCKED E7-Q08.

### UC-DLV-002: Xác nhận số nhận qua link

[Use case gốc](usecases/UC-DLV-002.md)

1. Đại diện khách truy cập link; hệ thống kiểm điều kiện xác minh và phạm vi phiếu trước khi hiển thị UI-E7-02.
2. Hệ thống hiển thị nguồn phiếu, số giao và version; việc xem phiếu chưa ghi số nhận.
3. Đại diện khách nhập số suất nhận thực, cung cấp bằng chứng xác nhận và gửi deliveryId cùng version đang xem.
4. Hệ thống kiểm quyền xác nhận hiện tại, số nhận và version của phiếu theo hợp đồng API.
5. Hệ thống lưu số nhận, bằng chứng, người xác nhận và thời điểm, giữ riêng số giao và số chốt.
6. Hệ thống trả xác nhận đã ghi cùng trạng thái nhận hoặc chênh lệch để đại diện khách kiểm tra.

Khi gặp nhánh rẽ hoặc lỗi:

- 1a. Link bị thu hồi hoặc không đủ quyền: hệ thống trả ERR-E7-403-01; số nhận chưa được ghi và không lộ secret link.
- 1b. Phiên không hợp lệ hoặc phiếu ngoài phạm vi: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-404-01 tương ứng; không hiển thị dữ liệu phiếu và không ghi xác nhận.
- 1c. Cơ chế xác minh/nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 và mã gate; xác nhận vẫn bị chặn.
- 3a. Khách không gửi xác nhận: hệ thống giữ chờ, đánh dấu nhánh xử lý BLOCKED Q-13; không lấy số giao/chốt làm số nhận và không tự đặt thời hạn.
- 5a. Mất phản hồi sau khi gửi: hệ thống báo chưa rõ kết quả; đại diện khách đối chiếu xác nhận/version trước lệnh mới. Chưa kết luận đã lưu hay chưa, replay E7-Q08 vẫn BLOCKED.

### UC-DLV-003: Lập biên bản chênh lệch

[Use case gốc](usecases/UC-DLV-003.md)

1. Dinh dưỡng viên chọn deliveryId tại UI-E7-03 và xem số giao, số nhận cùng bằng chứng nguồn.
2. Dinh dưỡng viên nhập mô tả sự việc, tham chiếu số giao/nhận và evidenceRef của hai phía.
3. Hệ thống kiểm phiên, quyền xử lý phiếu, phạm vi khách/cơ sở và khả năng sử dụng nguồn.
4. Hệ thống đối chiếu các số tham chiếu với phiếu; khi có đủ số nhận, hệ thống xác định phần chênh giao/nhận.
5. Hệ thống kiểm tác động tới kỳ khóa rồi ghi biên bản có version, bằng chứng và liên kết phiếu gốc.
6. Hệ thống trả biên bản để dinh dưỡng viên rà lại; biên bản chưa tự làm giảm tiền phải trả.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Thiếu bằng chứng nhận khi kết luận đã thống nhất: hệ thống trả ERR-DLV-422-02 và giữ nháp; thiếu số nhận thì chênh lệch vẫn chưa xác định.
- 5a. Thay đổi số ảnh hưởng kỳ đã khóa: hệ thống trả ERR-FIN-409-02, yêu cầu mở lại hợp lệ; số liệu kỳ và phiếu chưa bị sửa.
- 3a. Hết phiên hoặc thiếu quyền: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-403-01 tương ứng; không ghi biên bản mới.
- 3b. Phiếu ngoài scope: hệ thống trả ERR-E7-404-01; không lộ phiếu và không ghi thay đổi.
- 3c. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; không kết luận chênh lệch đã thống nhất.
- 5b. Mất phản hồi khi ghi: hệ thống báo kết quả chưa rõ; dinh dưỡng viên đối chiếu biên bản/version trước lệnh mới, không kết luận chưa lưu. Replay E7-Q08 BLOCKED.

### UC-DLV-004: Ghi thỏa thuận xử lý chênh lệch

[Use case gốc](usecases/UC-DLV-004.md)

1. Dinh dưỡng viên chọn discrepancyId tại UI-E7-03 và đối chiếu phần lệch với phiếu giao/nhận gốc.
2. Dinh dưỡng viên nhập phương án giao bù hoặc giảm trừ đã thỏa thuận, evidenceRef và version biên bản.
3. Hệ thống kiểm quyền, phạm vi, version biên bản và các gate áp dụng cho phương án.
4. Hệ thống đối chiếu bằng chứng hai phía và phần thiếu được xử lý, kiểm việc ghi nhận có đếm trùng với xử lý trước hay không.
5. Với giao bù, hệ thống gắn phiếu bù và số bù thực với phiếu gốc; với giảm trừ, hệ thống giữ dòng điều chỉnh riêng theo thỏa thuận có căn cứ.
6. Hệ thống lưu dấu vết và trả thỏa thuận cùng nguồn phục vụ xác định số tính tiền; không tự thay số chốt E6.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Chưa có bằng chứng thỏa thuận: hệ thống trả ERR-DLV-422-02; không áp giảm trừ, phải trả giữ nguyên.
- 4b. Phần thiếu đã giao bù nhưng lại được đề nghị giảm trừ: hệ thống hiển thị BLOCKED E7-Q02; không tự cộng hai cách, giữ xử lý đã có.
- 3a. Hết phiên/thiếu quyền: hệ thống trả ERR-E7-401-01/ERR-E7-403-01 tương ứng; không ghi thỏa thuận.
- 3b. Biên bản ngoài scope: hệ thống trả ERR-E7-404-01; không trả dữ liệu hoặc ghi thay đổi.
- 3c. Thiếu nguồn/policy cho phương án: hệ thống trả ERR-E7-503-01 kèm gate; phần xử lý chưa được áp dụng.
- 6a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; dinh dưỡng viên đối chiếu thỏa thuận/version trước lệnh mới. Chưa kết luận trạng thái lưu, replay E7-Q08 BLOCKED.

### UC-FIN-005: Tính doanh thu từ số tính tiền

[Use case gốc](usecases/UC-FIN-005.md)

1. Kế toán chọn đơn tại UI-E7-04 và tham chiếu orderRevisionRef, pricingSnapshotId.
2. Kế toán cung cấp billableServings và basisEvidenceRef, không mặc định số giao hoặc số nhận là số tính tiền.
3. Hệ thống kiểm phiên, quyền trên khách và nguồn giá/số tính tiền, đối chiếu snapshot với đúng order/version.
4. Hệ thống kiểm context VAT, căn cứ số tính tiền và các gate trước khi xác định các khoản tiền.
5. Hệ thống tính phải trả từ số tính tiền nhân giá chụp, trình bày riêng VAT/doanh thu chưa VAT và CK theo đơn; CK không giảm phải trả.
6. Hệ thống lưu bản tính nháp kèm nguồn, dấu vết và trả kết quả để kế toán kiểm tra tại UI-E7-04.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Context giá UNKNOWN hoặc số tính tiền không có căn cứ: hệ thống trả ERR-FIN-422-01; bản tính chưa được coi là xác định, không điền 0.
- 3a. Giá hiện tại đã đổi sau order: hệ thống tiếp tục dùng giá chụp của order; giá sống không thay snapshot. Ví dụ synthetic giá sống 42000, giá chụp 40000 thì bản tính vẫn dùng 40000.
- 3b. Hết phiên, thiếu quyền hoặc ngoài scope: hệ thống trả ERR-E7-401-01, ERR-E7-403-01 hoặc ERR-E7-404-01 tương ứng; không tạo bản tính hay lộ nguồn ngoài phạm vi.
- 3c. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; chưa xác định doanh thu.
- 6a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; kế toán đối chiếu bản tính/version trước lệnh mới. Chưa xác định đã lưu hay chưa; replay E7-Q08 BLOCKED.

### UC-FIN-006: Tra cứu doanh thu và nguồn

[Use case gốc](usecases/UC-FIN-006.md)

1. Kế toán nhập customerId, fromDate, toDate và trạng thái cần lọc tại UI-E7-04.
2. Hệ thống kiểm phiên, quyền đọc và phạm vi khách từ nguồn tin cậy.
3. Hệ thống đọc các bản tính đã có phù hợp bộ lọc, lấy nguồn số tính tiền và giá chụp của từng dòng.
4. Hệ thống tách dòng đủ căn cứ khỏi dòng chưa xác định; không cộng dòng thiếu như giá trị 0 vào tổng hoàn tất.
5. Hệ thống trả danh sách, nguồn và tổng có nhãn đủ/thiếu để kế toán đối chiếu; thao tác đọc không tạo bản tính.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Khách ngoài scope: hệ thống trả ERR-E7-404-01; không lộ tên hay tổng, dữ liệu doanh thu giữ nguyên.
- 3a. Khoảng ngày không có dữ liệu: hệ thống trả danh sách rỗng; không tạo calculation và không biến thiếu dữ liệu thành doanh thu hoàn tất.
- 2b. Hết phiên hoặc thiếu quyền: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-403-01 tương ứng; không trả danh sách và không thay dữ liệu.
- 3b. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; dữ liệu không bị thay đổi.
- 5a. Không nhận được phản hồi tra cứu: giao diện chưa có kết quả để đối chiếu; GET không phát sinh lệnh ghi hay replay nghiệp vụ. Quy ước kỹ thuật E7-Q08 vẫn BLOCKED.

### UC-FIN-007: Lập kỳ đối soát

[Use case gốc](usecases/UC-FIN-007.md)

1. Kế toán chọn khách, fromDate, toDate và revenueRefs tại UI-E7-05.
2. Hệ thống kiểm phiên, quyền theo khách và thứ tự ngày bắt đầu/kết thúc.
3. Hệ thống đọc tập doanh thu cùng version nguồn trong phạm vi được chọn, kiểm khả năng sử dụng nguồn theo gate.
4. Hệ thống lập danh sách dòng đủ, thiếu và tranh chấp; phiếu chờ khách xác nhận vẫn nằm trong tập cần rà.
5. Hệ thống chụp tập nguồn/version và tổng có căn cứ vào kỳ nháp, ghi dấu vết tạo kỳ.
6. Hệ thống trả kỳ nháp cùng danh sách chặn để kế toán chuẩn bị đối chiếu với khách.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. fromDate sau toDate: hệ thống trả ERR-FIN-422-02, yêu cầu sửa khoảng ngày; không tạo kỳ.
- 4a. Có phiếu chưa được khách xác nhận: hệ thống hiển thị BLOCKED Q-13 khi chuẩn bị chốt; dòng chờ được giữ, kỳ chưa được coi là đủ để chốt.
- 2b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không tạo kỳ hoặc lộ nguồn khách khác.
- 3a. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; không tạo kết quả đủ giả.
- 5a. Mất phản hồi tạo kỳ: hệ thống báo chưa rõ kết quả; kế toán đối chiếu kỳ/version trước lệnh mới. Trạng thái lưu chưa xác định, replay E7-Q08 BLOCKED.

### UC-FIN-008: Ghi nhận thống nhất đối soát

[Use case gốc](usecases/UC-FIN-008.md)

1. Kế toán chọn periodId tại UI-E7-05; hệ thống hiển thị tổng, version và các nguồn của kỳ.
2. Kế toán cung cấp agreementEvidenceRef và version tương ứng với biên bản khách đã xác nhận.
3. Hệ thống kiểm phiên/quyền trên kỳ và điều kiện xác minh đại diện khách, đối chiếu version đang gửi với nguồn kỳ.
4. Hệ thống đối chiếu tổng biên bản, revision và các dòng chênh lệch còn chưa thống nhất.
5. Khi đủ điều kiện, hệ thống lưu bằng chứng cùng revision, ghi trạng thái kỳ thống nhất và dấu vết thao tác.
6. Hệ thống trả kỳ thống nhất tại UI-E7-05; số đã thu vẫn giữ nguyên.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Tổng biên bản khác tổng kỳ hoặc còn chênh chưa thống nhất: hệ thống trả ERR-FIN-422-02; kỳ giữ chưa thống nhất.
- 3a. Nguồn kỳ đã thay khi khách xác nhận: hệ thống trả ERR-E7-409-01 và yêu cầu đối chiếu lại; bằng chứng cũ không áp cho bản mới.
- 3b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; trạng thái kỳ không đổi.
- 3c. Chưa đủ nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; chưa ghi thống nhất.
- 5a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; kế toán đối chiếu kỳ và bằng chứng trước lệnh mới. Chưa xác định đã lưu hay chưa, replay E7-Q08 BLOCKED.

### UC-FIN-009: Ghi nhận thu tiền

[Use case gốc](usecases/UC-FIN-009.md)

1. Kế toán chọn periodId tại UI-E7-06, đối chiếu khách, phải trả và các khoản đã thu.
2. Kế toán nhập số tiền, ngày nhận, chứng từ và version kỳ đang xem.
3. Hệ thống kiểm phiên, quyền trên khách/kỳ, version và điều kiện kỳ được ghi thu.
4. Hệ thống kiểm tiền dương, chứng từ đúng khách/kỳ và việc chứng từ đã được ghi nhận hay chưa.
5. Hệ thống ghi khoản thu cùng dấu vết, giữ tiền phải trả gốc riêng với tổng đã thu và số còn phải thu.
6. Hệ thống trả khoản thu để kế toán đối chiếu chứng từ; không suy khoản thu từ việc kỳ thống nhất hoặc đã xuất MISA.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Tiền không dương hoặc chứng từ sai/trùng: hệ thống trả ERR-FIN-422-03 và yêu cầu đối chiếu; không tạo thêm khoản thu.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; tiền đã thu không đổi.
- 3b. Policy thu hoặc nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; chưa ghi khoản thu theo nhánh bị chặn.
- 5a. Mất phản hồi lệnh thu: hệ thống hiển thị chưa rõ kết quả; kế toán đối chiếu chứng từ và khoản thu trước thao tác mới. Trạng thái lưu chưa xác định, replay BLOCKED E7-Q08.

### UC-FIN-010: Khóa kỳ đối soát

[Use case gốc](usecases/UC-FIN-010.md)

1. Kế toán chọn periodId tại UI-E7-05 và rà tổng, tập nguồn cùng trạng thái thống nhất.
2. Kế toán gửi yêu cầu khóa với version kỳ và nguồn quyết định.
3. Hệ thống kiểm phiên, quyền, phạm vi kỳ và version hiện tại so với lệnh khóa.
4. Hệ thống kiểm nguồn đã đủ và các điều kiện khóa theo policy được duyệt; không bỏ qua dòng chưa xác định.
5. Hệ thống chuyển kỳ sang LOCKED, giữ snapshot và ghi audit của thao tác khóa.
6. Hệ thống trả trạng thái LOCKED; mọi đường ghi ảnh hưởng số liệu kỳ bị chặn cho đến khi có duyệt mở lại hợp lệ.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Còn nguồn chưa xác định hoặc điều kiện khóa không đạt: hệ thống trả ERR-FIN-422-02; kỳ chưa chuyển sang LOCKED.
- 3a. Hai lệnh khóa cùng version: một lệnh chuyển trạng thái; hệ thống trả ERR-E7-409-01 cho lệnh còn lại, không ghi đè snapshot.
- 3b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; kỳ giữ trạng thái trước lệnh.
- 4b. Policy/nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; không tự coi đủ điều kiện khóa.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả; kế toán tra trạng thái/version kỳ trước lệnh mới. Chưa xác định đã khóa hay chưa, replay E7-Q08 BLOCKED.

### UC-FIN-011: Đề nghị mở lại kỳ

[Use case gốc](usecases/UC-FIN-011.md)

1. Kế toán chọn periodId tại UI-E7-07 và xem snapshot khóa cùng version kỳ.
2. Kế toán nhập lý do, nội dung dự kiến sửa và evidenceRef, gửi kèm version.
3. Hệ thống kiểm phiên, quyền trên kỳ và trạng thái khóa hiện tại.
4. Hệ thống kiểm version, lý do ít nhất 10 ký tự và căn cứ đề nghị theo điều kiện được duyệt.
5. Hệ thống ghi yêu cầu chờ Giám đốc cùng dấu vết, không chuyển kỳ sang mở.
6. Hệ thống trả yêu cầu và trạng thái kỳ vẫn khóa để kế toán theo dõi quyết định.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Lý do dưới 10 ký tự hoặc điều kiện kỳ không hợp lệ: hệ thống trả ERR-FIN-422-02; không lưu đề nghị.
- 6a. Kế toán sửa doanh thu khi đề nghị còn chờ: hệ thống trả ERR-FIN-409-02; kỳ và số liệu vẫn khóa.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không ghi đề nghị mới.
- 4b. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; kỳ không được mở.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả lập đề nghị; kế toán tra yêu cầu/version trước lệnh mới. Kỳ không được coi là đã mở, replay E7-Q08 BLOCKED.

### UC-FIN-012: Duyệt hoặc từ chối mở lại kỳ

[Use case gốc](usecases/UC-FIN-012.md)

1. Giám đốc xem yêu cầu tại UI-E7-07, gồm lý do, nội dung sửa, bằng chứng và người lập/sửa cuối.
2. Giám đốc chọn approve hoặc reject, nhập reason và gửi requestId, requestVersion, periodVersion.
3. Hệ thống kiểm phiên, vai trò Giám đốc, phạm vi kỳ và điều kiện không tự duyệt theo BR-SEC-008.
4. Hệ thống đối chiếu version yêu cầu/kỳ và trạng thái được phép quyết định theo gate.
5. Với quyết định approve hợp lệ, hệ thống lưu quyết định, chuyển kỳ sang REOPENED và giữ nguyên snapshot khóa cũ.
6. Hệ thống trả quyết định và trạng thái kỳ; việc sửa sau mở phải qua đối soát lại, chưa tự thống nhất số liệu mới.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Người quyết định là người lập/sửa cuối hoặc không phải Giám đốc: hệ thống trả ERR-E7-403-01; kỳ vẫn khóa, không ghi duyệt mở.
- 5a. Giám đốc chọn reject: hệ thống lưu quyết định từ chối và trả kỳ LOCKED; số liệu không đổi.
- 3b. Hết phiên hoặc ngoài scope: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-404-01 tương ứng; quyết định chưa được ghi.
- 4a. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; không tự mở kỳ.
- 5b. Mất phản hồi ghi quyết định: hệ thống báo kết quả chưa rõ; Giám đốc đối chiếu yêu cầu/kỳ trước lệnh mới. Không suy kỳ đã mở hoặc chưa mở; replay E7-Q08 BLOCKED.

### UC-FIN-013: Chuẩn bị và yêu cầu xuất MISA

[Use case gốc](usecases/UC-FIN-013.md)

1. Kế toán chọn periodId và revision tại UI-E7-08 để rà nguồn kỳ.
2. Kế toán tham chiếu templateRef của mẫu nhập và mapping được duyệt, gửi yêu cầu xuất.
3. Hệ thống kiểm phiên, quyền xuất, phạm vi và điều kiện kỳ được phép xuất theo policy.
4. Hệ thống kiểm revision nguồn, mẫu nhập và mapping; không tự suy định dạng file, tài khoản hay mã thuế.
5. Khi đủ điều kiện, hệ thống ghi yêu cầu xuất cùng nguồn, trạng thái và dấu vết; chỉ tạo file theo mapping đã duyệt.
6. Hệ thống trả trạng thái/lỗi và fileRef khi thực sự có file để kế toán theo dõi; có file chưa chứng minh nhập MISA thành công.

Khi gặp nhánh rẽ hoặc lỗi:

- 4a. Chưa có mẫu/mapping chính thức: hệ thống trả ERR-FIN-422-04, chặn xuất; không có file hoặc cột tự tạo.
- 6a. Kỳ đã mở lại sau lần xuất trước: hệ thống hiển thị revision cũ và yêu cầu rà lại; file cũ giữ nguyên bytes, không coi là bản hiện hành.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không tạo yêu cầu xuất hợp lệ.
- 3b. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; xuất vẫn bị chặn.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả; kế toán tra yêu cầu xuất/version trước lệnh mới. Chưa xác định đã tạo hay chưa; replay E7-Q08 BLOCKED.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-E7-401-01 | Phiên hết hạn. Đăng nhập lại. | Đăng nhập, không tự gửi lại lệnh |
| ERR-E7-403-01 | Không đủ quyền xác nhận thao tác. | Kiểm quyền, không hiện secret |
| ERR-E7-404-01 | Không tìm thấy dữ liệu. | Kiểm phạm vi |
| ERR-E7-409-01 | Dữ liệu đã đổi. Tải lại và đối chiếu. | Không tự ghi đè |
| ERR-E7-503-01 | Chưa đủ điều kiện xử lý. | Hiện gate, không điền 0 |
| ERR-DLV-422-01 | Kiểm tra số suất và phiếu nguồn. | Sửa dữ liệu |
| ERR-DLV-422-02 | Chưa đủ bằng chứng để thống nhất. | Giữ nháp |
| ERR-FIN-422-01 | Chưa xác định được doanh thu. | Kiểm nguồn |
| ERR-FIN-422-02 | Kiểm tra điều kiện đối soát và lý do. | Rà dòng chặn |
| ERR-FIN-422-03 | Kiểm tra số tiền và chứng từ thu. | Đối chiếu trước gửi lại |
| ERR-FIN-409-02 | Kỳ đã khóa. Cần Giám đốc duyệt mở lại. | Lập yêu cầu |
| ERR-FIN-422-04 | Chưa có mẫu nhập MISA được xác nhận. | Không xuất file giả |
| ERR-E7-500-01 | Chưa xác định kết quả. Đối chiếu trước thử lại. | Tra requestId, không ghi lặp |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
