---
id: DOC-E11-USER-GUIDE
title: Hướng dẫn vận hành E11
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e11]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E11: Mua hàng và sản xuất

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Kế toán, quản lý cơ sở, bếp trưởng, dinh dưỡng viên. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-PUR-001: Lập nhu cầu nguyên liệu

[Use case gốc](usecases/UC-PUR-001.md)

1. Actor mở UI-PUR-01, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: planRef, planRevision, estimateRef, serviceDate, kitchenId.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đối chiếu đúng bản kế hoạch và dự toán; cộng theo nguyên liệu và đơn vị quy đổi đã có căn cứ; hiển thị nguồn thiếu, không tự trừ tồn hoặc áp hao hụt lần hai.
5. Hệ thống trả: Nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Thiếu hệ số g/kg: Chặn tổng hợp khác đơn vị; không coi hệ số là 1 (ERR-PUR-422-11).
- Bước 4. Kế hoạch đổi revision khi đang xem: Đánh dấu nguồn cũ; không dùng số cũ làm nhu cầu hiện hành.
- Bước 4. thiếu policy/nguồn tại E6 CG06, ORD-Q10/14; E11-Q01: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-002: Lập đơn mua nháp

[Use case gốc](usecases/UC-PUR-002.md)

1. Actor mở UI-PUR-02, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: demandRef, supplierId, lines, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Người lập chọn NCC từ danh mục E3, không có tự chọn; nhập lượng/đơn vị và PriceInput có nguồn; tổng tiền chỉ khi giá đã xác định.
5. Hệ thống trả: Đơn DRAFT, nguồn nhu cầu và giá được giữ.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Số lượng âm hoặc thiếu NCC: Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập (ERR-PUR-422-12).
- Bước 4. Giá UNKNOWN hoặc chưa rõ VAT phải trả: Giữ chưa xác định, không coi giá hoặc VAT bằng 0.
- Bước 4. thiếu policy/nguồn tại E11-Q01/02/13/14: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-003: Kiểm cổng phát hành đơn mua

[Use case gốc](usecases/UC-PUR-003.md)

1. Actor mở UI-PUR-02, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: purchaseOrderRef, version.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đọc tình trạng nguồn, quyết định duyệt và policy; thiếu E11-Q02 thì trả BLOCKED. Không mô tả người duyệt hay thuật toán hạn mức.
5. Hệ thống trả: Danh sách điều kiện thiếu, không phát hành.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Client tự gắn APPROVED: Không công nhận trạng thái do client tự khai (ERR-PUR-422-13).
- Bước 4. Tải lại cổng nhiều lần: GET không tạo quyết định, không gửi đơn cho NCC.
- Bước 4. thiếu policy/nguồn tại E11-Q02; O-06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-004: Kiểm phạm vi quản lý lô

[Use case gốc](usecases/UC-PUR-004.md)

1. Actor mở UI-PUR-03, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: ingredientId, storageType, receiptRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đọc phân loại E2; chỉ FROZEN hoặc DRY thuộc phạm vi lô; quy tắc mã/hạn/xuất còn chờ.
5. Hệ thống trả: Kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Hàng tươi được gửi yêu cầu quản lý lô: Không tạo lô cho hàng tươi (ERR-PUR-422-14).
- Bước 4. Thiếu loại bảo quản: Không suy là hàng khô; hiển thị chưa xác định.
- Bước 4. thiếu policy/nguồn tại E11-Q03: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-005: Ghi phiếu nhận hàng nháp

[Use case gốc](usecases/UC-PUR-005.md)

1. Actor mở UI-PUR-03, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Giữ lượng đặt, thực nhận và chấp nhận riêng theo dòng; ghi chứng cứ chênh; không tự hoàn tất đơn hay tăng công nợ chính thức.
5. Hệ thống trả: Phiếu DRAFT có phiên bản và chênh lệch hiển thị.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Chấp nhận 9 kg khi chỉ nhận 8 kg: Chặn dữ liệu mâu thuẫn, không ghi phiếu (ERR-PUR-422-15).
- Bước 4. Hai lần nhận cùng đơn: Giữ tham chiếu từng lần; chưa tự quyết hoàn tất khi policy chưa có.
- Bước 4. thiếu policy/nguồn tại E11-Q04/13: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-006: Gắn ảnh chứng từ vào phiếu

[Use case gốc](usecases/UC-PUR-006.md)

1. Actor mở UI-PUR-04, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: receiptRef, fileRef, version.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Kiểm quyền tệp E1 và cùng phạm vi phiếu; giữ nguồn ảnh và người gắn; mở ảnh không phải xác nhận giá hoặc nhận hàng.
5. Hệ thống trả: Liên kết ảnh nội bộ; trạng thái chứng từ riêng.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. File của cơ sở ngoài scope: Không lộ nội dung/URL tệp, không gắn chéo (ERR-PUR-422-16).
- Bước 4. Liên kết ảnh hết hạn 15 phút theo E1: Kiểm quyền để cấp lại liên kết; không công khai ảnh lâu dài.
- Bước 4. thiếu policy/nguồn tại E11-Q05/13; E1-Q01: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-007: Xem công nợ nhà cung cấp

[Use case gốc](usecases/UC-PUR-007.md)

1. Actor mở UI-PUR-05, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: supplierId, kitchenId, fromDate, toDate.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Đọc số dư và nguồn được xác nhận; thiếu đầu kỳ/ghi nhận/thanh toán thì trả chưa xác định, không biến phiếu nhận thành đã trả.
5. Hệ thống trả: Bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Thiếu số dư đầu kỳ: Không báo tổng công nợ hoàn chỉnh (ERR-PUR-422-17).
- Bước 4. Đơn có CK khách 5 %: Không trừ 5 % khỏi phải trả NCC; không tự giảm số khách phải trả.
- Bước 4. thiếu policy/nguồn tại E11-Q06/04: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-008: Đối chiếu dự toán và thực mua

[Use case gốc](usecases/UC-PUR-008.md)

1. Actor mở UI-PUR-06, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Giữ tiền dự toán và thực mua riêng; chỉ so tỷ lệ khi cùng scope, đủ nguồn và có định nghĩa BO-02 được duyệt; thiếu thì không trả đạt.
5. Hệ thống trả: Hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Thực mua của cơ sở khác hoặc ngày chưa phân bổ: Không ghép với dự toán để kết luận đạt (ERR-PUR-422-18).
- Bước 4. Mẫu số bằng 0 hoặc chưa biết: Tỷ lệ và chênh null; kết luận chưa xác định.
- Bước 4. thiếu policy/nguồn tại E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-009: Giải thích nguồn chênh lệch

[Use case gốc](usecases/UC-PUR-009.md)

1. Actor mở UI-PUR-06, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: comparisonRef, ingredientId.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Truy về dòng dự toán, dòng nhận/mua và giá gồm VAT; hiển thị lượng/giá/đơn vị và nguồn. Không tự phân rã tác động giá/lượng nếu chưa chốt phương pháp.
5. Hệ thống trả: Chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Người không có cost.cost.read yêu cầu tiền: Không trả tiền hoặc cost trong body/lỗi/log hiển thị (ERR-PUR-403-11).
- Bước 4. Giá E3 mới có hiệu lực sau bản dự toán: Giữ giá snapshot dự toán; giá mới không sửa lịch sử.
- Bước 4. thiếu policy/nguồn tại E11-Q07/08/14: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-010: Lập phân ca nháp

[Use case gốc](usecases/UC-PUR-010.md)

1. Actor mở UI-PUR-07, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: kitchenId, serviceDate, shiftRef, assignments, planRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi phân công dự kiến gắn đúng nguồn; không xác nhận đã bắt đầu sản xuất E6, không tự chốt đủ người hoặc giờ ca.
5. Hệ thống trả: Phân ca DRAFT và các điều kiện còn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Nhân sự ngoài cơ sở được phép: Từ chối gắn vào ca (ERR-PUR-422-20).
- Bước 4. Plan revision thay đổi: Đánh dấu cần rà soát phân công; không tự kế thừa xác nhận bản cũ.
- Bước 4. thiếu policy/nguồn tại E11-Q09; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-011: Ghi kiểm tra trước giao

[Use case gốc](usecases/UC-PUR-011.md)

1. Actor mở UI-PUR-08, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: shiftRef, checklistRef, results, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi kết quả theo mục đã được duyệt; thiếu checklist hoặc còn mục chưa kiểm thì chưa đủ căn cứ giao. QC không ghi số khách nhận hoặc doanh thu.
5. Hệ thống trả: Phiếu QC nháp và cổng chưa sẵn sàng.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Client bỏ mục không đạt khỏi yêu cầu: Không kết luận đủ dựa trên tập mục thiếu (ERR-PUR-422-21).
- Bước 4. Tất cả mục mẫu được đánh đạt nhưng policy chưa duyệt: Vẫn BLOCKED E11-Q10; không phát sinh phiếu giao.
- Bước 4. thiếu policy/nguồn tại E11-Q10; E7-Q02; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-012: Ghi sổ mẫu lưu theo bữa

[Use case gốc](usecases/UC-PUR-012.md)

1. Actor mở UI-PUR-08, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Ghi mẫu và liên kết bữa; phân biệt đã có bản ghi với mẫu hợp lệ theo policy; không tự đặt hạn lưu hay hủy.
5. Hệ thống trả: Sổ mẫu nháp, danh sách bữa thiếu mẫu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Thiếu mã bữa hoặc cơ sở: Chặn bản ghi không truy được nguồn (ERR-PUR-422-22).
- Bước 4. Hai mẫu cùng bữa và 1 bữa khác chưa có mẫu: Đếm bữa phân biệt, không lấy số mẫu chia số bữa để báo đủ.
- Bước 4. thiếu policy/nguồn tại E11-Q11; E6 CG06: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-013: Lập ứng viên món thay thế

[Use case gốc](usecases/UC-PUR-013.md)

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: menuRef, menuVersion, originalDishId, replacementDishId, reason.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Người dùng chọn món cùng vai trò từ danh mục được phép; ghi thiếu hàng và nguồn; tạo ứng viên DRAFT, không thay thực đơn công bố.
5. Hệ thống trả: Ứng viên nháp có món cũ/mới và vai trò.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Đổi món MAIN sang SOUP: Chặn khác vai trò, không tạo thay thế hợp lệ (ERR-PUR-422-23).
- Bước 4. Món có tên giống nhưng vai trò khác: So mã vai trò, không so chuỗi tên món.
- Bước 4. thiếu policy/nguồn tại E11-Q12/15; O-02: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-014: Kiểm lại ứng viên thay món

[Use case gốc](usecases/UC-PUR-014.md)

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: candidateRef, candidateVersion, menuSourceRef.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Mỗi lần thay đều yêu cầu kiểm lại dị ứng, quy tắc E2 và cost E3 trên cùng phiên bản; chỉ hiển thị kết quả có provenance; không dùng lại kết quả món cũ.
5. Hệ thống trả: Bộ kết quả hoặc trạng thái BLOCKED kèm nguồn thiếu.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Thiếu giá hoặc thiếu căn cứ dị ứng: BLOCKED; không trả đạt dù quy tắc khác đạt (ERR-PUR-422-24).
- Bước 4. Người dùng đổi ứng viên sau lần kiểm: Kết quả cũ không hợp lệ; chạy lại cả ba kiểm.
- Bước 4. thiếu policy/nguồn tại DL-01; E11-Q15; O-01/O-02; CK/DATA-COST: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

### UC-PUR-015: Kiểm cổng chuyển duyệt MENU

[Use case gốc](usecases/UC-PUR-015.md)

1. Actor mở UI-PUR-09, chọn cơ sở và nguồn thuộc quyền.
2. Hệ thống trả tên nguồn, revision và tình trạng đủ/thiếu, không tự chọn bản thay thế.
3. Actor cung cấp hoặc đối chiếu: candidateRef, candidateVersion, checkRefs.
4. Hệ thống kiểm dữ liệu và thực hiện phần độc lập: Kiểm đủ kết quả đúng nguồn và cổng MENU hiện hành. CHAN chặn vượt cost; CANH_BAO giữ cảnh báo và vẫn qua MENU; thiếu đầu vào luôn chặn. Không ghi duyệt/công bố hoặc cập nhật E6.
5. Hệ thống trả: Readiness và lý do chặn; việc chuyển thật chờ adapter nguồn.
6. Actor xem kết quả và lý do còn chặn; thao tác ghi có audit, thao tác đọc không thay trạng thái.

Khi gặp nhánh rẽ hoặc lỗi:

- Bước 2. thiếu quyền: dùng 403/404 theo E1; không hiện bản ghi ngoài scope.
- Bước 3. Quy tắc cứng vi phạm hoặc thiếu cost: Không được chuyển như đã đạt; giữ ứng viên (ERR-PUR-422-25).
- Bước 4. Nguồn thay đổi giữa kiểm và chuyển: Từ chối dùng kết quả cũ; yêu cầu kiểm lại, không bỏ qua MENU.
- Bước 4. thiếu policy/nguồn tại E11-Q12/13; DL-01; E6 CG05/06/07: trả BLOCKED kèm mã, dừng nhánh phụ thuộc; không tạo kết quả đạt giả.
- Bước 5. kết nối mất sau gửi: chưa xác định kết quả; không gửi lặp như thao tác mới trước đối soát. Cơ chế chờ E11-Q13.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-PUR-422-11 | Chặn tổng hợp khác đơn vị; không coi hệ số là 1 | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-12 | Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-13 | Không công nhận trạng thái do client tự khai | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-14 | Không tạo lô cho hàng tươi | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-15 | Chặn dữ liệu mâu thuẫn, không ghi phiếu | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-16 | Không lộ nội dung/URL tệp, không gắn chéo | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-17 | Không báo tổng công nợ hoàn chỉnh | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-18 | Không ghép với dự toán để kết luận đạt | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-403-11 | Không trả tiền hoặc cost trong body/lỗi/log hiển thị | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-20 | Từ chối gắn vào ca | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-21 | Không kết luận đủ dựa trên tập mục thiếu | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-22 | Chặn bản ghi không truy được nguồn | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-23 | Chặn khác vai trò, không tạo thay thế hợp lệ | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-24 | BLOCKED; không trả đạt dù quy tắc khác đạt | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |
| ERR-PUR-422-25 | Không được chuyển như đã đạt; giữ ứng viên | Giữ bản cũ; sửa nguồn hoặc quyền rồi thử lại |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
