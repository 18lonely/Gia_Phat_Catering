---
id: DOC-E12-USER-GUIDE
title: Hướng dẫn vận hành E12
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e12]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E12: Phản hồi và báo cáo

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Người ăn, dinh dưỡng viên, kế toán, Giám đốc. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-FBR-001: Gửi đánh giá bữa ăn

[Use case gốc](usecases/UC-FBR-001.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp mealRef, ratingScaleRef, ratingValue, sourceScope.
4. Hệ thống thực hiện: Kiểm quyền phản hồi đúng bữa; chỉ nhận giá trị theo thang đã được duyệt; ghi nguồn và người gửi theo chính sách định danh, không lấy số chọn làm bằng chứng đã ăn.
5. Hệ thống trình bày đánh giá có receipt và trạng thái tiếp nhận, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Giá trị ngoài thang đã duyệt → Từ chối giá trị, không ghi đánh giá; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Gửi lại cùng yêu cầu sau mất phản hồi → Chỉ một đánh giá theo receipt; chính sách số lần đánh giá vẫn chờ Q02. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-002: Tiếp nhận và theo dõi khiếu nại

[Use case gốc](usecases/UC-FBR-002.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp mealRef, complaintCategoryRef, nội dung về bữa, caseVersion.
4. Hệ thống thực hiện: Giữ khiếu nại riêng với điểm đánh giá; chỉ người có quyền xem hồ sơ trong scope. Ghi diễn biến, không tự đóng theo thời gian hoặc tự giảm tiền đơn. SLA và người xử lý chưa chọn.
5. Hệ thống trình bày hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Yêu cầu đóng hồ sơ khi thiếu chính sách xử lý → Giữ hồ sơ chưa kết thúc; báo thiếu chính sách; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Khách gửi nội dung trùng nhưng chưa có receipt xác định → Không tự gộp hoặc xóa; nêu cần rà trùng theo Q02. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-003: Xem tỷ lệ được chọn theo món

[Use case gốc](usecases/UC-FBR-003.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp ngày, khách, điểm, ca, dishRef, selectionSourceRef.
4. Hệ thống thực hiện: Chỉ lấy lựa chọn thật của người ăn từ E6; phân biệt tự chọn với gán mặc định, nhập tổng và sản xuất. Chưa có mẫu số hoặc provenance đủ thì tỷ lệ null, không tự chọn trong ba mẫu số.
5. Hệ thống trình bày số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Nguồn chỉ có số suất sản xuất → Không tính hoặc suy tỷ lệ được chọn; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Mẫu số thiếu hoặc bằng 0 → Trả null cùng lý do; không trả 0 % hoặc chia cho 0. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-004: Lập đề xuất cải tiến thực đơn từ phản hồi

[Use case gốc](usecases/UC-FBR-004.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp dishMetricRefs, feedbackRefs, menuRef, revision, ghi chú đề xuất.
4. Hệ thống thực hiện: Người dùng đọc dữ liệu có nguồn, tự chọn món cần rà; thiếu mẫu số không xếp hạng tỷ lệ. Lưu đề xuất nháp riêng, không tự đổi MENU; thay món hoặc định lượng phải qua E2, dị ứng và E3.
5. Hệ thống trình bày đề xuất nháp cùng căn cứ và điều kiện kiểm lại, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Không có tỷ lệ nhưng yêu cầu xếp hạng món ít được chọn → Không xếp hạng; ghi thiếu mẫu số; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Nguồn phản hồi thay đổi sau khi lập nháp → Đánh dấu cần rà lại, không dùng bằng chứng cũ để chuyển duyệt. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-005: Xem dashboard theo bốn vai trò

[Use case gốc](usecases/UC-FBR-005.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp roleView, dateRange, customerRef, kitchenRef.
4. Hệ thống thực hiện: Server lấy scope và giao quyền thực; từng ô có metricDefinitionRef, sourceRefs, asOf, completeness. Danh mục chỉ số từng vai trò là đề xuất chờ duyệt. Không trả tổng hoàn tất nếu thiếu nguồn.
5. Hệ thống trình bày bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Đổi roleView thành giám đốc khi không có quyền → Từ chối; roleView không cấp thêm quyền; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Một nguồn lỗi trong nhiều chỉ số → Ô lỗi hiện thiếu nguồn, ô độc lập vẫn có nguồn; không cộng thiếu như 0. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-006: Đọc cost % ngày và theo khách

[Use case gốc](usecases/UC-FBR-006.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp date, customerRef, kitchenRef, costResultRef.
4. Hệ thống thực hiện: Đọc cost % đã tính ở E3, giữ đúng loại chỉ số, mẫu số và phiên bản. Cost % thực đơn khác cost % dự toán; không bình quân tỷ lệ. Tổng theo khách chờ phương pháp ghép/phân bổ được duyệt, không thay bằng lợi nhuận E13.
5. Hệ thống trình bày cost % ngày có nguồn e3; ô theo khách chưa xác định khi thiếu công thức, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Không có cost.cost.read → Loại số cost khỏi API, UI, lỗi, log và cache; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Khách có nhiều loại suất hoặc ngày không doanh thu → Không bình quân tỷ lệ hay dùng số giao làm mẫu số; giữ chưa xác định. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-007: Yêu cầu rà soát thực đơn khi giá đổi

[Use case gốc](usecases/UC-FBR-007.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp priceChangeRef, menuRef, menuRevision, scope.
4. Hệ thống thực hiện: Chỉ đọc sự kiện giá E3 và thực đơn được phép; diễn giải ảnh hưởng và đề xuất đổi món hoặc định lượng có nguồn. Không ghi giá, công thức hay thực đơn. Không tự tính tiền.
5. Hệ thống trình bày đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Sự kiện giá không có VAT phải trả xác định → Không đưa số cost hay phương án đạt; báo thiếu nguồn; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Giá hoặc menu đổi trong lúc rà → Kết quả gắn revision cũ và cần rà lại; không tự áp dụng. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-008: Kiểm lại đề xuất đổi món hoặc định lượng

[Use case gốc](usecases/UC-FBR-008.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp candidateRef, candidateRevision, menuSourceRef.
4. Hệ thống thực hiện: Biên tin cậy gọi kiểm thuần E2 FR-MENU-RUL-002, kiểm dị ứng trên nhãn và ràng buộc thực đơn được phép, cost E3 cho cùng hash; không gọi apply của E5. Giữ AIO-Q02 về CANH_BAO.
5. Hệ thống trình bày bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Một lần thay định lượng không chạy lại kiểm dị ứng/E2/E3 → Chặn nhãn sẵn sàng review; nêu kiểm còn thiếu; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Nguồn kiểm khác hash ứng viên → Từ chối ghép kết quả; yêu cầu kiểm lại cùng revision. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-009: Diễn giải dự toán có nguồn

[Use case gốc](usecases/UC-FBR-009.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp estimateRef, estimateRevision, date, kitchenRef.
4. Hệ thống thực hiện: Chỉ đọc dự toán E3 trong scope; giữ lượng mua, đơn vị, giá gồm VAT, khoản khoán và tổng từ hệ thống; AI chỉ giải thích, không tạo con số.
5. Hệ thống trình bày nháp diễn giải dự toán chờ người thật rà, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Dòng dự toán thiếu nguồn giá → Không bịa giá hoặc tổng hoàn tất; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Hao hụt đã nằm trong lượng E3 → Giữ lượng nguồn; không áp hao hụt thêm lần nữa. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-010: Diễn giải nhu cầu nguyên liệu

[Use case gốc](usecases/UC-FBR-010.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp demandRef, planRevisionRef, estimateRef.
4. Hệ thống thực hiện: Đọc nhu cầu E11 và revision nguồn; phân biệt nhu cầu gộp với mua ròng. Chưa chốt trừ tồn/dự phòng thì không đề xuất lượng mua ròng; không tạo đơn mua hoặc chọn NCC.
5. Hệ thống trình bày nháp diễn giải nhu cầu với thiếu nguồn rõ ràng, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Chỉ có kế hoạch thiếu revision hoặc nguồn chưa đủ → Giữ BLOCKED_DATA, không kết luận đủ để mua; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Yêu cầu trừ tồn khi chính sách chưa chốt → Không trừ; giữ nhu cầu gộp và tham chiếu E11-Q01. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-011: Giải thích cảnh báo giá lệch

[Use case gốc](usecases/UC-FBR-011.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp comparisonRef, priceSourceRefs, alertPolicyRef.
4. Hệ thống thực hiện: Đọc so sánh E3/E11 cùng đơn vị, VAT, thời điểm và scope. Ngưỡng giá lệch chờ E12-Q10; không mượn BO-02 hoặc sai số NFR làm ngưỡng giá.
5. Hệ thống trình bày nháp giải thích; cảnh báo chính thức chưa xác định, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Không có ngưỡng cảnh báo được duyệt → Không gán cảnh báo đạt/vượt; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Hai giá khác đơn vị hoặc cách ghi VAT → Không so trực tiếp; chờ nguồn quy đổi E3. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-012: Tóm tắt khách và đề xuất nhắc việc

[Use case gốc](usecases/UC-FBR-012.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp customerRef, timeRange, CRM sourceRefs.
4. Hệ thống thực hiện: Chỉ đọc projection CRM E10 theo quyền người hỏi. Tóm tắt phải dẫn bản ghi; thiếu lịch không suy khách rời. Nhắc việc là nội dung đề xuất, không tạo task, không gửi thông báo hoặc đổi hồ sơ.
5. Hệ thống trình bày nháp tóm tắt và danh sách việc cần người thật rà, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Văn bản CRM yêu cầu đọc khách ngoài scope → Coi là dữ liệu, chặn tại công cụ/DB trước lấy dữ liệu; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Nguồn phản hồi mới chưa sẵn sàng → Ghi thiếu nguồn; không bịa khiếu nại hoặc nguy cơ rời. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-013: Soạn nội dung báo giá nháp để review

[Use case gốc](usecases/UC-FBR-013.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp customerRef, quoteRevisionRef, menuRef, nguồn giá được phép.
4. Hệ thống thực hiện: Chỉ dùng trường E10 cho phép đọc; chưa có giá thì không bịa. Đầu ra là nội dung đề xuất, không tạo quote E10, không phát hành/gửi hoặc cam kết giá. Cost/biên lợi nhuận cần quyền riêng; bản dự kiến cho khách không chứa các trường này.
5. Hệ thống trình bày nháp báo giá có nguồn và nhãn chưa phát hành, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Yêu cầu gửi báo giá hoặc sửa giá hợp đồng → Từ chối hành động ghi/gửi; chỉ trả nháp; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Báo giá nguồn đã có revision mới → Ghi cũ nguồn và yêu cầu review; không thay snapshot cũ. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-014: Hỏi đáp số liệu theo quyền

[Use case gốc](usecases/UC-FBR-014.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp câu hỏi về chỉ số, dateRange, customerRef, metricDefinitionRef.
4. Hệ thống thực hiện: Chỉ công cụ đọc allowlist, giao quyền người dùng–dịch vụ tại API/tool/DB. Không SQL hay URL tùy ý; không tự tính số từ văn bản. Lọc cả trường lồng nhau, lỗi, log và cache; không lộ cost/biên lợi nhuận qua suy ngược.
5. Hệ thống trình bày câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Câu hỏi yêu cầu cập nhật doanh thu hoặc dò cost ngoài quyền → Không có công cụ ghi; từ chối dữ liệu cấm trước khi đưa vào bộ diễn giải; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Quyền bị thu hồi giữa hai lần gọi công cụ → Lần gọi sau và kết quả cuối bị chặn; không dùng cache quyền cũ. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-015: Lập mục tiêu dinh dưỡng nhóm

[Use case gốc](usecases/UC-FBR-015.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp groupRef phi y tế, mục tiêu có sourceRef, effectiveRange, version.
4. Hệ thống thực hiện: Chỉ mục tiêu cấp nhóm người ăn; không danh sách bệnh lý, hồ sơ cá nhân hoặc suy nhóm từ sức khỏe. Nguồn chỉ số/công thức/ngưỡng chờ NUTR-Q01–04; chưa có thì chỉ nháp thiếu căn cứ, không kích hoạt.
5. Hệ thống trình bày mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Yêu cầu đặt mục tiêu cho một người theo bệnh lý → Từ chối ngoài phạm vi; không lưu hồ sơ; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Hai mục tiêu trùng khoảng nhóm khi chưa có policy ưu tiên → Không tự chọn mục tiêu mới nhất; giữ xung đột chờ Q14. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-016: Kiểm thực đơn theo mục tiêu nhóm

[Use case gốc](usecases/UC-FBR-016.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp groupTargetRef, targetVersion, menuRevision, nutritionCalculationRefs.
4. Hệ thống thực hiện: Đọc bản tính E4 cho tổ hợp suất có nguồn và mục tiêu được duyệt; thiếu công thức/ngưỡng thì chưa đánh giá. Không tự đặt mức kcal hoặc đổi kết quả thành cổng công bố MENU.
5. Hệ thống trình bày so sánh có phiên bản hoặc chưa xác định, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Không có nguồn/ngưỡng đã duyệt → Không kết luận đạt dinh dưỡng; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Một thành phần suất thiếu giá trị dinh dưỡng → Giữ totals=null theo E4; không so tổng một phần như đầy đủ. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-017: Đồng ý dùng nhật ký bữa đã ăn

[Use case gốc](usecases/UC-FBR-017.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp consentPolicyRef, explicitAgreement.
4. Hệ thống thực hiện: Tự nguyện, không chọn sẵn; nội dung chỉ bữa đã ăn và giá trị của suất. Không gọi FEAT-046/047; từ chối không ảnh hưởng chọn món. Chủ thể lấy từ phiên server; chi tiết identity E6 chưa chốt thì chặn nhận thật.
5. Hệ thống trình bày đồng ý có phiên bản hoặc nhật ký chưa bật, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Không đánh dấu đồng ý mà gửi yêu cầu bật → Không bật, không ghi bữa hoặc dinh dưỡng cá nhân; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Rút đồng ý sau khi đã có bữa → Dừng ghi thêm; cho yêu cầu xóa riêng, không mở hồ sơ sức khỏe. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-018: Ghi bữa đã ăn vào nhật ký

[Use case gốc](usecases/UC-FBR-018.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp consentRef, consumedMealRef, consumedAt, mealNutritionSnapshotRef.
4. Hệ thống thực hiện: Chỉ nhận bữa đã ăn theo bằng chứng/chính sách E12-Q17; lựa chọn/order/giao nhận không tự chứng minh cá nhân đã ăn. Lưu liên kết tổ hợp và 4 giá trị E4, nhãn ước tính; không trường text sức khỏe, không suy lượng hấp thu.
5. Hệ thống trình bày bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Chỉ có lựa chọn cho ngày mai → Không ghi thành bữa đã ăn; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Bữa đã ăn nhưng snapshot thiếu một chỉ số → Không bịa số; hiển thị thiếu nguồn, không coi đủ dinh dưỡng. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-019: Xem nhật ký dinh dưỡng của mình

[Use case gốc](usecases/UC-FBR-019.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp dateRange; subject từ phiên.
4. Hệ thống thực hiện: Chỉ đọc bữa đã ghi của chủ thể, snapshot lịch sử và nhãn ước tính từ định lượng sống. Không khuyến nghị cá nhân, không chấm sức khỏe, không so mục tiêu nhóm như mục tiêu cá nhân.
5. Hệ thống trình bày danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Sửa subjectRef sang người khác → Không trả bữa hoặc tiết lộ tồn tại của nhật ký khác; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Nguồn dinh dưỡng đổi sau ngày ăn → Giữ snapshot lịch sử và nhãn nguồn cũ, không viết lại. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

### UC-FBR-020: Yêu cầu xóa nhật ký và rút đồng ý

[Use case gốc](usecases/UC-FBR-020.md)

1. Người dùng mở màn hình và chọn nguồn/phạm vi cần làm việc.
2. Hệ thống kiểm quyền hiện tại trên hành động, chủ thể và từng nguồn trước đọc; không lấy roleView hoặc scope client làm quyền.
3. Người dùng cung cấp consentRef, diaryScope, explicitDeleteConfirmation.
4. Hệ thống thực hiện: Xác thực chủ thể, cho xóa dữ liệu của mình theo nền ≤ 72 giờ; không xóa giao dịch nguồn E6/E7. Cơ chế bản sao/retention chờ Q16; receipt chỉ xác nhận nhận yêu cầu, không báo đã xóa khi chưa có evidence.
5. Hệ thống trình bày receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút, nguồn và các điểm còn chờ.
6. Người dùng rà kết quả; với đề xuất AI, người thật quyết định ở quy trình nghiệp vụ nguồn riêng, E12 không tự áp dụng.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. hết phiên → ERR-FBR-401-01; đăng nhập rồi bắt đầu lại.
- 2b. thiếu quyền hành động → ERR-FBR-403-01; tham chiếu ngoài scope → ERR-FBR-404-01. Dừng trước lấy dữ liệu.
- 3a. sai kiểu hoặc field ngoài danh sách → ERR-FBR-400-01; trả lỗi trường an toàn, không ghi.
- 4a. Yêu cầu xóa nhật ký của người khác → Từ chối trước khi ghi yêu cầu; ERR-FBR-422-01 khi yêu cầu hành động không đủ điều kiện. GET hợp lệ có số chưa có trả availability/missingReason riêng.
- 4b. Gửi lặp khi yêu cầu xóa đang xử lý → Trả cùng receipt theo quyền hiện tại, không tuyên bố hoàn tất sớm. Revision xung đột trả ERR-FBR-409-01, không tự ghi đè.
- 4c. nguồn gián đoạn → ERR-FBR-503-01, không thay số thiếu bằng 0.
- 5a. lỗi nội bộ/receipt → ERR-FBR-500-01; đối soát requestId, không tự coi lần gửi mất phản hồi là chưa ghi.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-FBR-400-01 | Yêu cầu chưa đúng định dạng. | Sửa trường được chỉ ra |
| ERR-FBR-401-01 | Vui lòng đăng nhập lại. | Đăng nhập |
| ERR-FBR-403-01 | Bạn không có quyền thực hiện thao tác này. | Kiểm quyền đã được cấp |
| ERR-FBR-404-01 | Không tìm thấy dữ liệu được phép xem. | Chọn lại nguồn |
| ERR-FBR-409-01 | Nguồn đã thay đổi. Vui lòng rà lại. | Tải lại, không ghi đè |
| ERR-FBR-422-01 | Chưa đủ căn cứ để thực hiện. | Xem mã câu hỏi hoặc nguồn thiếu |
| ERR-FBR-500-01 | Chưa thể hoàn tất yêu cầu. | Đối soát bằng requestId, không coi đã thành công |
| ERR-FBR-503-01 | Nguồn dữ liệu đang gián đoạn. | Giữ trạng thái chưa xác định |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
