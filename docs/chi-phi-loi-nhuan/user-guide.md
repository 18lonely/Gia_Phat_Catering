---
id: DOC-E13-USER-GUIDE
title: Hướng dẫn vận hành E13
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e13]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E13: Chi phí và lợi nhuận

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Kế toán, Giám đốc. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-EXP-001: Quản lý và khóa kỳ chi phí

[Use case gốc](usecases/UC-EXP-001.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn periodRef, kitchenRef, fromDate, toDate, version, lockDecisionRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm scope, nguồn và quyết định khóa; kỳ mở cho nhập nháp. Chỉ khóa khi chính sách và quyền đã được duyệt; giữ snapshot bất biến.
5. Hệ thống trả Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: kỳ đã LOCKED; khi gửi sửa trực tiếp kỳ thì ERR-EXP-409-01; không đổi byte dữ liệu gốc.
- 4d. Biên**: hai thao tác cùng version cũ; khi gửi khóa đồng thời với ghi chi phí thì chỉ một version hợp lệ; thao tác còn lại ERR-EXP-409-02.

### UC-EXP-002: Ghi chi phí theo cơ sở và loại

[Use case gốc](usecases/UC-EXP-002.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn periodRef, kitchenRef, typeVersionRef, amount, evidenceRef, sourceKey, customerRef?.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm kỳ mở, căn cứ khoản tiền và loại. Khoản trực tiếp phải có khách và căn cứ gán trực tiếp; khoản chung giữ pool riêng. Không nhận lại cost E3/E11 như khoản mới.
5. Hệ thống trả Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: dòng chi phí thiếu chứng từ hoặc loại; khi gửi lưu thì ERR-EXP-422-01 và chỉ ra trường thiếu; không ghi dòng.
- 4d. Biên**: sourceKey đã nằm trong cost E3/E11 của cùng kỳ; khi nhập lại khoản đó thì ERR-EXP-409-03; không cộng hai lần.

### UC-EXP-003: Ghi giờ công thực tế theo ca

[Use case gốc](usecases/UC-EXP-003.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn personRef, kitchenRef, shiftRevisionRef, workDate, hours, attendanceEvidenceRef, version.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Đối chiếu người/cơ sở với tham chiếu E11; phân ca là dự kiến, không sinh giờ thực tế. Lưu giờ nháp cùng bằng chứng; nguồn chấm công và xác nhận chính thức còn chờ.
5. Hệ thống trả Bảng DRAFT; giờ thực tế và ca dự kiến tách riêng; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: chỉ có phân ca E11, không có giờ thực tế; khi yêu cầu xác nhận chấm công thì ERR-EXP-422-02; không suy đã làm đủ giờ.
- 4d. Biên**: một người có hai dòng cùng nguồn ca; khi gửi lại dòng chấm công thì không cộng đôi giờ; conflict hoặc receipt theo contract được duyệt.

### UC-EXP-004: Tham chiếu chi phí nhân công

[Use case gốc](usecases/UC-EXP-004.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn attendanceVersionRef, rateVersionRef hoặc payrollAmountRef, evidenceRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Chỉ dùng nguồn đơn giá/tiền công và giờ đã xác nhận. Hai cách là lựa chọn phải duyệt, không cộng cả hai. Thiếu giá giữ null; không tính bảo hiểm, thuế TNCN, phụ cấp hoặc lương thực lĩnh.
5. Hệ thống trả Chi phí nhân công có nguồn hoặc BLOCKED; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: có giờ công nhưng chưa có đơn giá hay nguồn tiền công; khi yêu cầu tính chi phí thì ERR-EXP-422-02; amount null, không mặc định 0.
- 4d. Biên**: đơn giá nguồn thay phiên bản sau kỳ khóa; khi đọc báo cáo cũ thì giữ phiên bản đã chụp; thay đổi chỉ qua điều chỉnh.

### UC-EXP-005: Soạn phiên bản phương pháp phân bổ

[Use case gốc](usecases/UC-EXP-005.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn methodRef?, baseVersion?, scope, proposedBasis, effectiveRange, sourceDefinitionRefs, rationale.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Lưu phương án nháp, các driver và căn cứ đề xuất dưới dạng dữ liệu có phiên bản. Không mặc định phương pháp nào; không thực thi biểu thức tùy ý. Nội dung thuật toán chỉ đặc tả sau E13-Q05.
5. Hệ thống trả Phiên bản DRAFT; không có hiệu lực phân bổ; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: bản phương pháp đã APPROVED; khi sửa nội dung trên cùng version thì ERR-EXP-409-01; cần phiên bản mới.
- 4d. Biên**: chưa chọn phương pháp nào; khi mở form mới thì không có driver mặc định, không tính tỷ trọng hoặc lợi nhuận.

### UC-EXP-006: Ghi duyệt phương pháp của Giám đốc

[Use case gốc](usecases/UC-EXP-006.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn methodVersionRef, expectedVersion, expectedHash, decision, evidenceRef, reason.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm quyền Giám đốc, khác người tạo/sửa cuối theo E1; kiểm đủ nội dung và bằng chứng. Quyết định gắn hash và hiệu lực cụ thể. Không suy ủy quyền từ chức danh; O-06 còn mở.
5. Hệ thống trả Quyết định APPROVED hoặc RETURNED; version không đổi nội dung; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: người duyệt cũng là người lập/sửa cuối; khi gửi chấp thuận thì ERR-EXP-403-01; không có quyết định hiệu lực.
- 4d. Biên**: hash nội dung thay đổi từ lúc mở màn duyệt; khi gửi duyệt hash cũ thì ERR-EXP-409-02; yêu cầu đọc lại, không duyệt nhầm bản.

### UC-EXP-007: Kiểm cổng và lập lần phân bổ

[Use case gốc](usecases/UC-EXP-007.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn periodSnapshotRef, methodVersionRef, sourceManifestRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm phương pháp được duyệt đúng scope/hiệu lực và bộ nguồn đầy đủ. Chưa có phương pháp: BLOCKED, chỉ hiển thị chi phí trực tiếp, không tạo kết quả giả. Khi đủ quyết định mới triển khai engine theo hợp đồng được duyệt.
5. Hệ thống trả Lần chạy BLOCKED hoặc bản phân bổ có methodVersion; phần chưa phân bổ riêng; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: không có phương pháp APPROVED; khi yêu cầu lợi nhuận theo khách thì ERR-EXP-422-03 và BLOCKED; chỉ xem chi phí trực tiếp.
- 4d. Biên**: driver thiếu hoặc tổng driver bằng 0; khi yêu cầu phân bổ thì không chia 0, không dồn cho khách bất kỳ; giữ khoản chưa phân bổ và lý do.

### UC-EXP-008: Tra cứu lợi nhuận theo khách

[Use case gốc](usecases/UC-EXP-008.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn runRef, customerRef, kitchenRef, periodRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Đọc snapshot có nguồn E7 đã đối soát và cost E3/E11; không tính lại từ suất giao hay giá hiện hành E10. Thiếu bất kỳ căn cứ công thức/nguồn/phương pháp thì lợi nhuận null; báo cáo chỉ phần trực tiếp được phép.
5. Hệ thống trả Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: doanh thu chưa đối soát hoặc không có căn cứ thành phần lợi nhuận; khi mở báo cáo khách thì ERR-EXP-422-02; BLOCKED, không gọi chênh thu trừ nguyên liệu là lợi nhuận.
- 4d. Biên**: khách có nguồn ở hai cơ sở; khi lọc theo từng cơ sở rồi tổng khách thì không trộn khóa; không cộng nguồn trùng; chỉ tổng khi từng phần đủ căn cứ.

### UC-EXP-009: Đối chiếu lợi nhuận với từng cơ sở

[Use case gốc](usecases/UC-EXP-009.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn runRef, facilityResultRef, resultDefinitionVersionRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Ghép cùng cơ sở/kỳ, cùng bộ thành phần và revision. Tách kết quả các khách, phần chưa phân bổ, chênh so số chuẩn độc lập. Không cộng khách thiếu như 0; không tự cho phép sai số.
5. Hệ thống trả Bảng đối chiếu có residual/unallocated/delta; chưa khớp không nghiệm thu; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: cơ sở 200, tổng khách 250, chưa phân bổ có tác động -50; khi mở đối chiếu thì hiện cầu nối 250 - 50 = 200, nhưng R13 vẫn chưa đạt vì khách chưa phân bổ hết.
- 4d. Biên**: cơ sở 200, tổng khách 250, phần chưa phân bổ -40; khi mở đối chiếu thì delta -10 hiện rõ; không giấu 10 vào khách cuối, không dùng dung sai Cost.

### UC-EXP-010: Lập điều chỉnh sau khóa có phê duyệt

[Use case gốc](usecases/UC-EXP-010.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn originalEntryRef, lockedSnapshotRef, adjustmentAmount, reason, evidenceRef, approvalRef.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Giữ nguyên bản gốc. Đề nghị điều chỉnh là dòng riêng, lý do và người duyệt bắt buộc trước ghi nhận. Người duyệt/quy tắc kỳ đích chờ Q10; không tự chọn hoặc mở khóa E7.
5. Hệ thống trả Đề nghị PENDING; chỉ POSTED khi có quyết định hợp lệ; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: đề nghị không có lý do hoặc người duyệt hợp lệ; khi yêu cầu ghi nhận điều chỉnh thì ERR-EXP-422-04; kỳ và số liệu gốc không đổi.
- 4d. Biên**: đề nghị đã được ghi nhận; khi gửi lại cùng khóa nghiệp vụ thì không ghi bút toán lần hai; trả receipt hoặc conflict theo contract đã duyệt.

### UC-EXP-011: Bảo vệ lương và đầu ra nội bộ

[Use case gốc](usecases/UC-EXP-011.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn runRef, actorScope, purpose, projection.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Kiểm quyền hiện tại ở server và truy cập nguồn; chỉ PER-07/PER-08 có quyền chi tiết lương theo scope. Báo cáo theo khách nội bộ chỉ tổng hợp nhân công, không người/giờ/đơn giá. Tài liệu gửi khách tuyệt đối không có lợi nhuận/biên lợi nhuận/cost/lương.
5. Hệ thống trả Projection nội bộ cho phép hoặc từ chối; không có đường gửi khách E13; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: người ngoài PER-07/PER-08 hoặc phiên phía khách; khi truy cập chi tiết công/lương/lợi nhuận hoặc xuất thì ERR-EXP-403-01; không lộ qua payload, lỗi, log, cache, file hoặc metadata.
- 4d. Biên**: người vừa bị thu hồi quyền nhưng có runRef đã biết; khi đọc lại hoặc yêu cầu bản xuất thì từ chối theo quyền hiện tại; không dùng cache quyền cũ.

### UC-EXP-012: Kiểm nguồn và truy nguyên lần báo cáo

[Use case gốc](usecases/UC-EXP-012.md)

1. Người dùng chọn cơ sở/kỳ và mở dữ liệu cần xử lý.
2. Người dùng cung cấp hoặc chọn runRef, sourceManifestRef, expectedVersions.
3. Hệ thống kiểm phiên, scope, version và điều kiện nguồn; hiển thị các nguồn thiếu trước khi tiếp tục.
4. Hệ thống thực hiện: Hiện nguồn E3/E7/E10/E11, định nghĩa chỉ số, thời điểm chụp, phạm vi, phiên bản và thiếu nguồn. Nguồn đổi tạo lần mới; không hồi tố sửa lần cũ. Đầu nối E12 chỉ ranh giới đọc, chưa triển khai adapter.
5. Hệ thống trả Manifest, danh sách BLOCKED và liên kết nội bộ theo quyền; thao tác ghi có audit và tham chiếu quyết định, thao tác đọc giữ nguồn.
6. Người dùng xem kết quả và nguồn, không coi nhãn nháp là nghiệm thu.

Khi gặp nhánh rẽ hoặc lỗi:

- 3a. Chưa xác thực → ERR-EXP-401-01; ngoài quyền → ERR-EXP-403-01; kết thúc, không gửi dữ liệu nhạy cảm.
- 3b. Thiếu nguồn/quyết định → ERR-EXP-422-02, riêng thiếu phương pháp → ERR-EXP-422-03; giữ BLOCKED, không chuyển null thành 0. Người dùng chỉ xem phần độc lập được phép.
- 3c. Không tìm thấy tham chiếu trong scope → ERR-EXP-404-01; không tiết lộ dữ liệu ngoài quyền.
- 4a. Nguồn hoặc version thay đổi → ERR-EXP-409-02; đọc lại, không tự retry ghi.
- 4b. Nguồn tạm lỗi → ERR-EXP-503-01; giữ lịch sử, không ghi thành công giả.
- 4c. Đặc thù**: thiếu một nguồn trong manifest cần thiết; khi yêu cầu đánh dấu đủ dữ liệu thì ERR-EXP-422-02; nguồn thiếu không có giá trị 0 thay thế.
- 4d. Biên**: nguồn E7 có revision mới sau lần chạy; khi đọc lần chạy cũ và đề nghị làm mới thì bản cũ bất biến; lần mới phải kiểm lại gate và có id khác.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-EXP-401-01 | Phiên làm việc không hợp lệ. | Đăng nhập lại. |
| ERR-EXP-403-01 | Bạn không có quyền thực hiện. | Liên hệ đầu mối cấp quyền, không hiển thị giá trị bị cấm. |
| ERR-EXP-404-01 | Không tìm thấy dữ liệu. | Kiểm tra tham chiếu; không tiết lộ sự tồn tại ngoài scope. |
| ERR-EXP-409-01 | Bản này không thể ghi đè. | Lập điều chỉnh hoặc phiên bản mới. |
| ERR-EXP-409-02 | Dữ liệu đã thay đổi. | Đọc lại và review lại. |
| ERR-EXP-409-03 | Khoản này đã có trong nguồn. | Đối chiếu nguồn, không nhập lại. |
| ERR-EXP-422-01 | Chưa đủ thông tin ghi chi phí. | Bổ sung trường được chỉ rõ. |
| ERR-EXP-422-02 | Chưa đủ căn cứ để tính. | Xem danh sách điều kiện còn thiếu. |
| ERR-EXP-422-03 | Lợi nhuận theo khách đang BLOCKED. | Chỉ xem chi phí trực tiếp; chờ quyết định Giám đốc. |
| ERR-EXP-422-04 | Chưa thể ghi nhận điều chỉnh. | Bổ sung lý do và quyết định hợp lệ. |
| ERR-EXP-503-01 | Tạm thời chưa đọc được nguồn. | Giữ lần cũ, thử đọc lại theo quy trình; không thay bằng 0. |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
