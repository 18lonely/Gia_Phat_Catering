---
id: DOC-E10-USER-GUIDE
title: Hướng dẫn vận hành E10
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e10]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E10: Khách hàng và bán hàng

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Dinh dưỡng viên kiêm chăm sóc khách hàng, người duyệt. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-CRM-001: Xem hồ sơ khách hàng 360°

[Use case gốc](usecases/UC-CRM-001.md)

1. Tác nhân mở UI-CRM-01 hoặc gọi API-CRM-001, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerId, kỳ xem và phạm vi cơ sở; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đọc từng nhóm liên hệ, điểm, hợp đồng, order, doanh thu, phản hồi theo nguồn và quyền; giữ nguồn, thời điểm và độ đầy đủ riêng từng nhóm.
5. Hệ thống đọc dữ liệu đã có, đối chiếu phiên bản và mức đầy đủ; không chạy tác vụ ghi hoặc đánh giá mới bên dưới GET.
6. Hệ thống trả Hồ sơ có các nhóm dữ liệu và trạng thái ĐỦ / THIẾU / CHƯA CÓ NGUỒN; không cộng phần chưa xác định thành 0.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E6-CG-01/08; E7-Q03/04/08; E10-Q01; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. nguồn doanh thu hoặc phản hồi chưa có: khi mở hồ sơ A, hệ thống nhóm tương ứng ghi CHƯA CÓ NGUỒN; giá trị null, không 0; không mở chức năng phản hồi E12. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. người dùng chỉ có phạm vi khách A: khi đổi mã hồ sơ sang khách B, hệ thống trả ERR-CRM-404-01; không lộ liên hệ hoặc tổng tiền của B.
- 5a. Nguồn đọc không khả dụng trả phần thiếu có nhãn hoặc ERR-CRM-503-01 nếu không xác định được phạm vi; không lưu kết quả giả.

### UC-CRM-002: Ghi nháp thông tin liên hệ CRM

[Use case gốc](usecases/UC-CRM-002.md)

1. Tác nhân mở UI-CRM-01 hoặc gọi API-CRM-002, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, tên liên hệ, vai trò liên hệ, phương thức liên hệ, nguồn xác minh; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm quyền và dữ liệu tối thiểu theo chính sách được duyệt; lưu bản nháp liên hệ gắn khách tham chiếu, không tạo khách chủ hoặc tài khoản đặt món.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Bản nháp liên hệ có version và audit; khách chủ và điểm phục vụ không đổi.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q01; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. yêu cầu chứa role quản trị hoặc customerId ngoài phạm vi: khi gửi nháp liên hệ, hệ thống từ chối trường lạ hoặc phạm vi; không cấp quyền đặt món. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. quyết định thời gian lưu và xử lý xóa chưa có: khi yêu cầu lưu hoặc xóa thông tin liên hệ thật, hệ thống giữ BLOCKED E10-Q01; không dùng thời gian lưu audit làm thời gian lưu liên hệ.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-003: Tiếp nhận đề xuất từ website và E9

[Use case gốc](usecases/UC-CRM-003.md)

1. Tác nhân mở UI-CRM-02 hoặc gọi API-CRM-003, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp sourceSystem, sourceRef, sourceRevision, sourceHash, contactRef, consentRef, safeMenuRef nếu có; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm giao tiếp đầu nhận đã được duyệt, chống trùng theo nguồn và revision; chỉ lưu nội dung được phép; cấp receipt sau ghi bền vững; nhân viên phân loại sau tiếp nhận.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Phiếu tiếp nhận và receipt của E10, chưa phải khách chủ hoặc hợp đồng; không trả dữ liệu nội bộ về E8/E9.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E8-Q06/07/12; E9-Q06/10/13; E10-Q13; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. đầu nhận hoặc consent chưa được duyệt: khi nhận đề xuất thật, hệ thống trả ERR-CRM-503-01; không báo đã vào CRM và không tự tạo customers. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. phiếu đã lưu nhưng mất phản hồi: khi nhận lại cùng nguồn, revision và nội dung, hệ thống trả receipt cũ theo quyền hiện tại; khác hash cùng định danh trả ERR-CRM-409-02.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-004: Lập đề nghị rà khách nghi trùng

[Use case gốc](usecases/UC-CRM-004.md)

1. Tác nhân mở UI-CRM-03 hoặc gọi API-CRM-004, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp cặp customerRef, bằng chứng nghi trùng, nguồn và version của hai hồ sơ; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Chỉ áp tiêu chí phát hiện sau quyết định E10-Q02; hiện chỉ thiết kế khung danh sách và bằng chứng. Nhân viên mở cặp để đối chiếu, đề nghị giữ hồ sơ nào và từng trường; không tự gộp.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Đề nghị chờ duyệt với bản so sánh, nguồn và tập tham chiếu chịu tác động.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q02/03; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. chưa chốt tiêu chí phát hiện trùng: khi yêu cầu quét tự động, hệ thống BLOCKED E10-Q02; không tự chọn số điện thoại, tên hoặc mã số thuế làm khóa gộp. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. hai khách khác nhau dùng chung một đầu mối: khi đánh giá cặp theo tiêu chí chính thức, hệ thống kết quả theo bộ tiêu chí được duyệt; không có quy tắc mặc định coi chung đầu mối là trùng.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-005: Duyệt đề nghị gộp khách

[Use case gốc](usecases/UC-CRM-005.md)

1. Tác nhân mở UI-CRM-03 hoặc gọi API-CRM-005, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp reviewId, baseVersions, quyết định, lựa chọn trường và lý do; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Người thật xem diff và tác động; kiểm quyền, tách người lập/sửa cuối với người duyệt theo đề xuất; chỉ thực hiện khi quyền sở hữu mã và cơ chế tham chiếu đã được duyệt; lưu ánh xạ và ảnh trước gộp nguyên tử.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Quyết định, nhật ký gộp, liên kết truy nguyên; không xóa hồ sơ gốc hoặc sửa snapshot tài chính.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q03/04; E6-CG-08; O-06; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. người lập đề nghị tự duyệt hoặc chưa có quyền duyệt: khi gửi quyết định gộp, hệ thống ERR-CRM-403-01 hoặc ERR-CRM-503-01; không thay ánh xạ khách. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. một hồ sơ đổi version sau khi người duyệt mở diff: khi xác nhận gộp bằng version cũ, hệ thống ERR-CRM-409-01; tải lại diff, không ghi đè thay đổi mới.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-006: Hoàn tác một lần gộp khách

[Use case gốc](usecases/UC-CRM-006.md)

1. Tác nhân mở UI-CRM-03 hoặc gọi API-CRM-006, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp mergeRef, versions hiện tại, lý do, bằng chứng và phân tích liên kết phát sinh sau gộp; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đọc ảnh trước gộp và diff hiện tại; lập phương án hoàn tác có người duyệt. Phải xử lý tham chiếu phát sinh theo quyết định Q04; ghi bù có liên kết tới lần gộp, không xóa audit hoặc tái tính giao dịch quá khứ.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Bản hoàn tác có audit hoặc danh sách xung đột cần xử lý; hồ sơ lịch sử vẫn truy nguyên.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q03/04; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. thiếu ảnh trước gộp hoặc có tham chiếu mới chưa có phương án: khi yêu cầu hoàn tác, hệ thống ERR-CRM-422-01 hoặc BLOCKED E10-Q04; không khôi phục một phần. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. đã phát sinh order và hợp đồng mới sau gộp: khi lập phương án hoàn tác, hệ thống phân bổ theo quyết định được duyệt; không tự chuyển toàn bộ giao dịch mới về một khách.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-007: Xem và đề nghị đổi vòng đời khách

[Use case gốc](usecases/UC-CRM-007.md)

1. Tác nhân mở UI-CRM-04 hoặc gọi API-CRM-007, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, trạng thái hiện tại, trạng thái đề nghị, evidenceRef, reason, version; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đối chiếu ma trận chuyển đã duyệt với bằng chứng lịch phục vụ từng điểm; giữ sự kiện và actor; không suy khách rời từ một ngày không có order; tín hiệu rủi ro khác quyết định chuyển vòng đời.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Sự kiện vòng đời có căn cứ và lịch sử; nhánh không đủ căn cứ giữ trạng thái cũ.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q05/06; E6-CG-05/06/08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. không có order vào ngày không nằm trong lịch phục vụ: khi xem vòng đời khách, hệ thống không tự chuyển CHURNED hoặc AT_RISK chỉ từ sự vắng mặt đó. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. khách có nhiều điểm với lịch phục vụ khác nhau: khi tổng hợp vòng đời khách, hệ thống áp đúng quy tắc tổng hợp đã được duyệt; chưa có quy tắc thì BLOCKED E10-Q05.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-008: Rà tín hiệu nguy cơ rời theo lịch điểm

[Use case gốc](usecases/UC-CRM-008.md)

1. Tác nhân mở UI-CRM-04 hoặc gọi API-CRM-008, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, khoảng quan sát, lịch điểm có phiên bản, sự kiện phục vụ có nguồn; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đọc kết quả đánh giá đã có với nguồn và mức đầy đủ; chỉ đánh giá các kỳ phục vụ dự kiến, loại ngày nghỉ đã xác nhận theo policy. Không tự đặt số ngày, trọng số, ngưỡng hoặc suy thiếu dữ liệu là không phát sinh.
5. Hệ thống đọc dữ liệu đã có, đối chiếu phiên bản và mức đầy đủ; không chạy tác vụ ghi hoặc đánh giá mới bên dưới GET.
6. Hệ thống trả Tín hiệu có lý do, lịch/nguồn, hoặc CHƯA ĐỦ DỮ LIỆU; GET không chạy tác vụ đánh giá.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q06; E6-CG-03/05/06/08; E7-Q02/03; Q-13; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. lịch thiếu hoặc dữ liệu giao nhận chưa xác nhận: khi xem tín hiệu, hệ thống hiện CHƯA ĐỦ DỮ LIỆU và nguyên nhân, không chấm rủi ro thấp hoặc cao giả. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. cùng dữ liệu được đọc lại hai lần: khi GET tín hiệu, hệ thống không sinh thêm cảnh báo, không đổi vòng đời, giữ cùng evaluationRef.
- 5a. Nguồn đọc không khả dụng trả phần thiếu có nhãn hoặc ERR-CRM-503-01 nếu không xác định được phạm vi; không lưu kết quả giả.

### UC-CRM-009: Quản lý cơ hội và phễu bán hàng

[Use case gốc](usecases/UC-CRM-009.md)

1. Tác nhân mở UI-CRM-05 hoặc gọi API-CRM-009, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp opportunityRef nếu đã có, customerOrIntakeRef, stage đề nghị, ownerRef, evidenceRef, version; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Tạo cơ hội nháp hoặc ghi sự kiện chuyển giai đoạn sau kiểm policy; giữ chủ cơ hội, lịch sử, nguồn thắng/thua; đếm theo cơ hội duy nhất và cùng kỳ/cohort, không coi mọi lead là cơ hội đã đủ điều kiện.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Cơ hội và lịch sử giai đoạn; bảng phễu nêu định nghĩa mẫu số, thiếu thì chưa tính tỷ lệ.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q07/08; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. chỉ có báo giá đã gửi, chưa có bằng chứng thắng: khi đề nghị ghi WON, hệ thống ERR-CRM-422-01; không tự suy thắng từ việc gửi báo giá. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. mẫu số cơ hội của kỳ bằng 0: khi xem tỷ lệ chuyển đổi, hệ thống hiện chưa có cơ sở tính, tỷ lệ null; không chia 0 hoặc hiển thị 100%.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-010: Soạn phiên bản báo giá

[Use case gốc](usecases/UC-CRM-010.md)

1. Tác nhân mở UI-CRM-06 hoặc gọi API-CRM-010, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp quoteRef và baseRevision chỉ khi sửa báo giá đã có; opportunityRef, dòng loại suất/giá, điều kiện, hiệu lực đề nghị; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Lần đầu không có quoteRef/baseRevision thì tạo báo giá và revision đầu cùng giao dịch; lần sửa bắt buộc cả hai, tạo revision mới từ bản gốc, giữ diff và liên hệ cơ hội; không sửa bản đã phát hành. Giá, VAT và điều kiện phải có căn cứ; phần tính margin chỉ nội bộ và không tự chọn công thức.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Phiên bản nháp mới; bản phát hành cũ bất biến, trạng thái duyệt không tự sao chép.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q08/15; O-01; CK-Q01–10; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. client gửi approvedBy, margin hoặc số tổng để ép kết quả: khi lưu báo giá, hệ thống từ chối trường ngoài hợp đồng; không tin tổng hay người duyệt client. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. hai người cùng sửa baseRevision: khi lưu bản thứ hai sau khi bản thứ nhất đã ghi, hệ thống ERR-CRM-409-01; không mất diff và không ghi đè revision.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-011: Đính kèm thực đơn có phiên bản vào báo giá

[Use case gốc](usecases/UC-CRM-011.md)

1. Tác nhân mở UI-CRM-06 hoặc gọi API-CRM-011, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp quoteRevision, menuRef, menuRevision, sourceHash, phạm vi dùng cho khách; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm quyền và nguồn MENU được phép theo Q09; chụp projection khách gắn đúng revision báo giá; thực đơn E9 chỉ là đề xuất cần người thật xử lý, không coi receipt là MENU được duyệt.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Tệp/nội dung thực đơn được phép và provenance; không tự sửa MENU hoặc dùng bản hiện hành động.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q09; E9-Q06/12; O-02; NUTR-Q01–04; E8-Q04; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. nguồn thực đơn bị thu hồi hoặc chỉ có nháp E9 chưa duyệt: khi đính kèm để phát hành báo giá, hệ thống ERR-CRM-422-01 hoặc BLOCKED theo nguồn; không tự công bố MENU. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. MENU có bản mới sau khi báo giá đã phát hành: khi mở lại báo giá cũ, hệ thống giữ đúng bản đính kèm cũ và cảnh báo nguồn; muốn thay phải tạo revision mới.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-012: Duyệt và tạo bản báo giá dành cho khách

[Use case gốc](usecases/UC-CRM-012.md)

1. Tác nhân mở UI-CRM-07 hoặc gọi API-CRM-012, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp quoteRevision, expectedHash, quyết định duyệt, evidenceRef, recipientScope; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm người duyệt, hiệu lực và nguồn; tạo projection allowlist riêng tại server rồi lưu bản phát hành. Cost và margin chỉ người nội bộ có quyền riêng đọc; không nhúng rồi ẩn CSS. Phiên này không gửi thư/tin nhắn cho khách.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Bản phát hành có hash và revision chỉ gồm trường khách được phép; lỗi không lộ cost.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q08/09/13; O-06; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. dữ liệu lồng nhau hoặc lỗi chứa purchasePrice, costAmount hoặc margin: khi tạo projection khách, hệ thống loại theo allowlist trước lưu/xuất, không có trường nhạy cảm trong JSON, HTML, metadata, lỗi hoặc cache. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. khách B hoặc tài khoản AIN truy bản dành cho A: khi đọc bản phát hành, hệ thống ERR-CRM-404-01 hoặc ERR-CRM-403-01; không trả bản nội bộ và không nâng quyền dịch vụ.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-013: Lập hợp đồng từ báo giá được chấp thuận

[Use case gốc](usecases/UC-CRM-013.md)

1. Tác nhân mở UI-CRM-08 hoặc gọi API-CRM-013, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, quoteRevision, acceptanceEvidenceRef, draftTerms, fileRefs; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đối chiếu bằng chứng khách chấp thuận đúng revision và quyền lập; tạo hợp đồng DRAFT tham chiếu báo giá bất biến. Không lấy việc xem/tải báo giá làm chấp thuận hoặc chữ ký; nhập hợp đồng hiện hữu theo nguồn riêng sau Q10.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Hợp đồng nháp có nguồn và các dòng giá đề nghị; chưa hiệu lực, không tạo order.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q08/10/11; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. bằng chứng thuộc revision cũ nhưng yêu cầu lấy giá revision mới: khi lập hợp đồng, hệ thống ERR-CRM-409-01; yêu cầu đối chiếu lại, không đổi giá khách đã nhận. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. chỉ có lượt mở báo giá, không có bằng chứng chấp thuận: khi lập hợp đồng theo luồng báo giá đã chấp thuận, hệ thống ERR-CRM-422-01; không coi lượt xem là ký hoặc chấp thuận.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-014: Kích hoạt hợp đồng và giá theo loại suất

[Use case gốc](usecases/UC-CRM-014.md)

1. Tác nhân mở UI-CRM-08 hoặc gọi API-CRM-014, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp contractVersion, amendmentRef/amendmentVersion nếu kích hoạt phụ lục, signatureEvidenceRef, priceLines theo mealTypeRef, effectiveFrom, effectiveTo, salePriceBasis, vatRatePct; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm bằng chứng, quyền duyệt và hiệu lực; phụ lục phải thuộc hợp đồng trong path và đúng version. Kiểm không chồng khoảng giá ACTIVE theo customer + mealType như nguồn hiện có; kiểm nguyên tử khi cạnh tranh. Chưa chốt quy ước biên ngày không kích hoạt.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Hợp đồng và bộ giá hiệu lực nhất quán, audit và nguồn phụ lục; không ghi giá ngược vào order đã chụp.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q10/11/12; O-01; CK-Q01–10; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. hai bộ giá cùng khách và loại suất có phần giao nhau: khi kích hoạt bộ thứ hai, hệ thống ERR-CRM-409-03; không ACTIVE một phần và không chọn giá theo bản ghi mới nhất. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. hai bộ giá liền kề đúng ngày kết thúc/bắt đầu: khi kiểm tra hiệu lực tại ranh giới, hệ thống kết quả theo quy ước biên đã duyệt E10-Q11; trước quyết định thì BLOCKED.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-015: Lập phụ lục thay đổi giá

[Use case gốc](usecases/UC-CRM-015.md)

1. Tác nhân mở UI-CRM-09 hoặc gọi API-CRM-015, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp contractRef, baseVersion, predecessorPriceRefs, giá đề nghị, from/to, reason, evidenceRef; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Lưu phụ lục DRAFT và quan hệ bản trước/bản sau, giữ nội dung giá cũ bất biến. Khi được duyệt phải kiểm cùng quy tắc ACTV và không chồng lấn; sửa hồi tố và tác động đơn đã khóa chờ Q12, không tự mở kỳ.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Phụ lục nháp và diff lịch sử; không sửa giá hoặc snapshot order cũ.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q10/11/12; E6-CG-04/05/07; E7-Q05; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. người dùng đòi sửa trực tiếp bản giá đã dùng cho order: khi gửi phụ lục kèm lệnh ghi đè lịch sử, hệ thống ERR-CRM-422-01; không sửa snapshot và không tự mở kỳ khóa E7. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. gửi lại cùng khóa và cùng nội dung phụ lục: khi lưu lại sau mất phản hồi, hệ thống trả cùng phụ lục, không tạo hai chuỗi thay thế.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

### UC-CRM-016: Tra giá hợp đồng cho thời điểm phục vụ

[Use case gốc](usecases/UC-CRM-016.md)

1. Tác nhân mở UI-CRM-09 hoặc gọi API-CRM-016, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, mealTypeRef, serviceDate, sourceScope đã xác minh; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Chỉ đọc bộ giá đã có hiệu lực theo quy ước được duyệt; trả priceTermRef, contract/amendmentRef, version, căn cứ VAT. Không tự chụp giá vào order; adapter E6/Cost phải được duyệt riêng.
5. Hệ thống đọc dữ liệu đã có, đối chiếu phiên bản và mức đầy đủ; không chạy tác vụ ghi hoặc đánh giá mới bên dưới GET.
6. Hệ thống trả Một kết quả có nguồn hoặc UNRESOLVED; không dùng giá hiện tại thay snapshot lịch sử.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q11/12/13; E6-CG-04/05/07/08/11; CK-Q01–10; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. không có hoặc có hơn một giá khớp, VAT cần thiết chưa rõ: khi tra giá, hệ thống UNRESOLVED hoặc ERR-CRM-409-03; không lấy giá 0 hoặc tự chọn giá mới nhất. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. đơn lịch sử đã có pricingSnapshot và sau đó có phụ lục mới: khi xem hồ sơ đơn cũ, hệ thống vẫn dùng snapshot đúng order/version từ E6/Cost; không thay bằng kết quả tra giá hiện tại.
- 5a. Nguồn đọc không khả dụng trả phần thiếu có nhãn hoặc ERR-CRM-503-01 nếu không xác định được phạm vi; không lưu kết quả giả.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-CRM-400-01 | crm.400.01 | Sửa trường được chỉ ra |
| ERR-CRM-401-01 | crm.401.01 | Xác thực lại |
| ERR-CRM-403-01 | crm.403.01 | Liên hệ người quản lý quyền |
| ERR-CRM-404-01 | crm.404.01 | Kiểm lại tham chiếu thuộc quyền |
| ERR-CRM-409-01 | crm.409.01 | Tải bản mới và đối chiếu |
| ERR-CRM-409-02 | crm.409.02 | Đối soát bản gốc |
| ERR-CRM-409-03 | crm.409.03 | Rà các khoảng của cùng khách và loại suất |
| ERR-CRM-422-01 | crm.422.01 | Bổ sung nguồn hoặc sửa đề nghị |
| ERR-CRM-500-01 | crm.500.01 | Giữ khóa cũ để đối soát |
| ERR-CRM-503-01 | crm.503.01 | Theo dõi gate; không thử vượt quyền |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
