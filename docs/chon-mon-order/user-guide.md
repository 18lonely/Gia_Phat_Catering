---
id: DOC-E6-USER-GUIDE
title: Hướng dẫn vận hành E6
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e6]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E6: Chọn món và order

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Người ăn, người đặt tổng, dinh dưỡng viên, bếp. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-ORD-001: Cấp quyền người đặt tổng

[Use case gốc](usecases/UC-ORD-001.md)

1. Actor mở UI-ORD-01; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,userId,role,reason.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ cấp trong công ty có quyền; quyền người đặt tổng theo company/service point. Không kế thừa quyền nội bộ; log cấp/thu hồi và kiểm scope mỗi request.
4. Hệ thống thực hiện cấp vai trò người đặt tổng cho user U ở A; kết quả theo điều kiện review: grant chỉ cấp phạm vi A của yêu cầu; audit ghi người cấp và phạm vi; không kết luận scope một/nhiều công ty.
5. Hệ thống trả tài khoản công ty; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given U là người đặt tổng A; When U cấp quyền nội bộ cho mình; Then 403 ERR-ORD-403-01; không thay user_roles.
- 3a. Biên/đồng thời:** Given quản trị chỉ được giao A; When gửi customerId B; Then 404 ERR-ORD-404-01; không tiết lộ B.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-002: Đăng ký qua QR công ty

[Use case gốc](usecases/UC-ORD-002.md)

1. Actor mở UI-ORD-02; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: qrToken,thông tin định danh được chốt.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: QR xác minh công ty theo D-19, không tự chứng minh duy nhất một người. Chỉ tạo/link eater sau kiểm QR ACTIVE và chính sách định danh ORD-Q01; không suy QR công khai là quyền đọc toàn công ty.
4. Hệ thống thực hiện xác minh và đăng ký với identity hợp lệ; kết quả theo điều kiện review: liên kết eater với tài khoản và A; không cấp quyền người đặt tổng.
5. Hệ thống trả user/eater đã liên kết; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given QR đã ROTATED; When đăng ký bằng token cũ; Then 401 ERR-ORD-401-01; không tạo eater.
- 3a. Biên/đồng thời:** Given identity đã có trên thiết bị khác; When đăng ký lần nữa; Then kết quả theo ORD-Q01; không tuyên bố cookie ngăn trùng người.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Xung đột:** xử lý mã lỗi theo route/identity policy; không bắt người dùng cung cấp version mà RegistrationInput/QrSessionInput không có. Không tự tạo/link danh tính khác để vượt xung đột.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-003: Mở phiên QR giới hạn

[Use case gốc](usecases/UC-ORD-003.md)

1. Actor mở UI-ORD-02; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: qrToken,serviceDate,định danh phiên.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Phiên giới hạn một công ty/ngày/phạm vi; chống chọn trùng phụ thuộc định danh thật, không chỉ cookie/IP. Chưa chốt ORD-Q01 thì không tuyên bố giải quyết duplicate người.
4. Hệ thống thực hiện mở phiên guest ngày 2026-11-16 tại điểm A1; kết quả theo điều kiện review: phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần.
5. Hệ thống trả phiên có scope và expiry; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given phiên guest thuộc A1 ngày 16; When gọi ngày 17 hoặc điểm B1; Then 404 ERR-ORD-404-01; không trả thực đơn ngoài scope.
- 3a. Biên/đồng thời:** Given phiên đã hết hạn; When gửi lựa chọn; Then 401 ERR-ORD-401-01; không tăng bộ đếm.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Xung đột:** xử lý mã lỗi theo route/identity policy; không bắt người dùng cung cấp version mà RegistrationInput/QrSessionInput không có. Không tự tạo/link danh tính khác để vượt xung đột.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-004: Quản lý QR và danh sách người ăn

[Use case gốc](usecases/UC-ORD-004.md)

1. Actor mở UI-ORD-03; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Nếu chỉ xem, gọi API-ORD-010 và kết thúc bằng danh sách scoped. Nếu quay vòng, dùng QrRotationInput/API-ORD-011; nếu gỡ, dùng EaterStatusInput/API-ORD-012. Không dùng chung payload action cho cả ba route.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Đổi QR vô hiệu token cũ; gỡ người ăn không xóa lịch sử order/lựa chọn. Tác động phiên đang mở/lựa chọn trước chốt chờ ORD-Q02; quyền chỉ công ty mình.
4. Quay vòng hợp lệ: token cũ ROTATED, secret mới chỉ cấp lần đầu. Gỡ hợp lệ: trạng thái REMOVED, giữ lịch sử; tác động phiên/lựa chọn còn chờ ORD-Q02. GET không thực hiện hai thay đổi này.
5. Hệ thống trả QR/người ăn trạng thái mới; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given danh sách thuộc khách B; When người đặt tổng A đọc danh sách; Then 404 ERR-ORD-404-01; không lộ tên người ăn B.
- 3a. Biên/đồng thời:** Given eater đã có order khóa; When gỡ eater; Then giữ lịch sử; tác động phiên/lựa chọn chưa khóa BLOCKED ORD-Q02.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-005: Quản lý dữ liệu phục vụ

[Use case gốc](usecases/UC-ORD-005.md)

1. Actor mở UI-ORD-04; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Đọc API-ORD-013; tạo điểm bằng API-ORD-026/ServiceInput version=0 hoặc sửa điểm hiện hữu bằng API-ORD-014/version hiện tại. Customer/kitchen đã tồn tại; không upsert qua PUT hoặc tạo customer master ở đây.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Điểm thuộc đúng khách; lịch theo ngày trong tuần/ca; cơ sở phục vụ xác định. Không tự mở CRM360/hợp đồng Later; thay đổi không sửa snapshot đã khóa.
4. Hệ thống thực hiện lưu điểm A1, bếp K1 và lịch thứ Hai ca LUNCH; kết quả theo điều kiện review: điểm thuộc A, lịch duy nhất theo điểm/ca/thứ, version tăng.
5. Hệ thống trả dữ liệu phục vụ có version; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given A1 thuộc A; When lưu lịch với customer B; Then 422 ERR-ORD-422-04; không tạo quan hệ chéo khách.
- 3a. Biên/đồng thời:** Given order cũ khóa ở K1; When đề xuất đổi bếp sang K2; Then snapshot cũ giữ K1; hiệu lực tương lai chờ ORD-Q03.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-006: Đặt định mức công ty

[Use case gốc](usecases/UC-ORD-006.md)

1. Actor mở UI-ORD-05; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,mealTypeId,effectiveFrom,version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Định mức chung theo D-21, giá và cơ cấu có hiệu lực; không người ăn tự trả chênh. Ai duyệt/thời điểm áp dụng khi đang chọn chờ ORD-Q04; thiếu định mức chặn chọn.
4. Hệ thống thực hiện người đặt tổng lưu định mức chung; kết quả theo điều kiện review: version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người.
5. Hệ thống trả quota version; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given chưa có định mức hiệu lực; When người ăn chọn món; Then 422 ERR-ORD-422-01; không ghi lựa chọn.
- 3a. Biên/đồng thời:** Given đã có lựa chọn theo quota v1; When lưu quota v2 giữa ngày; Then không âm thầm tính lại v1; xử lý theo ORD-Q04.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-007: Chọn và đổi một món chính

[Use case gốc](usecases/UC-ORD-007.md)

1. Actor mở UI-ORD-06; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: menuDayId,dishId,servicePointId,date,shift,version,key.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ menu PUBLISHED, món MAIN thuộc ngày, recipe/giá hiệu lực và tổ hợp trong định mức. Identity từ phiên; unique eater+date+shift; trước deadline server; sửa counter giảm món cũ/tăng món mới cùng transaction.
4. API-ORD-002 ghi selection và counter nguyên tử theo guard. Ví dụ synthetic đổi A version1 sang B tạo version2, A giảm1/B tăng1; replay cùng key/body không ghi lần hai.
5. Hệ thống trả selection/version và tổng đúng; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given định mức synthetic 40000đ, tổ hợp 40001đ; When gửi chọn tổ hợp; Then 422 ERR-ORD-422-01; lựa chọn/counter không đổi.
- 3a. Biên/đồng thời:** Given định mức synthetic 40000đ, tổ hợp đúng 40000đ và đủ cơ cấu; When gửi chọn trước hạn với version hiện tại; Then được nhận; không yêu cầu người ăn bù tiền.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-008: Gửi lựa chọn cả tuần

[Use case gốc](usecases/UC-ORD-008.md)

1. Actor mở UI-ORD-07; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: selections[],perDayVersion,key.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ ngày có thực đơn công bố và còn mở; QR guest không dùng. Atomic cả tuần hay kết quả từng ngày chờ ORD-Q05; không báo cả tuần thành công nếu một ngày lỗi.
4. Hệ thống thực hiện gửi lựa chọn tuần kèm version từng ngày; kết quả theo điều kiện review: trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt.
5. Hệ thống trả kết quả từng ngày có trạng thái; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given guest QR chỉ có phạm vi ngày; When gửi lựa chọn tuần; Then 403 ERR-ORD-403-01; không ghi ngày nào.
- 3a. Biên/đồng thời:** Given 4 ngày hợp lệ và 1 ngày đã khóa; When gửi tuần; Then không báo thành công toàn tuần; atomic rollback hoặc partial receipt chờ ORD-Q05.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-009: Chốt tổng suất và phân bổ

[Use case gốc](usecases/UC-ORD-009.md)

1. Actor mở UI-ORD-08; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Đọc Summary qua API-ORD-003; gửi SubmissionInput qua API-ORD-004 với version của order và summaryVersion riêng. Nhập hộ phải có source/evidenceRef/reason theo quyền; tên field theo API, không lấy token Summary làm orders.version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Tách số tự chọn và số nhập thêm cho người chưa chọn. Đề xuất T>=S+C, dư T-S-C gán mặc định lúc khóa; T<S+C trả xung đột cần xử lý tường minh, không xóa lựa chọn cá nhân tự động.
4. Hệ thống thực hiện gửi tổng; kết quả theo điều kiện review: SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa.
5. Hệ thống trả order SUBMITTED và breakdown; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given synthetic S=60,C=10,T=65; When gửi tổng; Then đề xuất 422 ERR-ORD-422-02; không xóa 5 lựa chọn; chờ ORD-Q06.
- 3a. Biên/đồng thời:** Given synthetic S=60,C=10,T=70; When gửi tổng rồi khóa đủ điều kiện; Then D=0; không tạo dòng default ảo.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-010: Gán món mặc định khi khóa

[Use case gốc](usecases/UC-ORD-010.md)

1. Scheduler nhận sự kiện đến hạn, resolve servicePointId/serviceDate/shift và deadlineVersion; không mở UI-ORD-09.
2. Service gọi PORT-LOCK(servicePointId,serviceDate,shift,deadlineVersion,eventKey); menu/default/quota/counter là nguồn server kiểm lại, không payload do vận hành tùy nhập.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: D-14: gán phần còn lại về default MAIN hợp lệ; không tạo người ăn giả cho suất chưa có định danh. Tổng số từ người đặt tổng, không dùng số người đăng ký làm total. Thiếu total/default thì trạng thái cần xử lý theo ORD-Q07.
4. Hệ thống thực hiện scheduler khóa; kết quả theo điều kiện review: D=30 cho A; MAIN tổng 100; không tạo 30 eater giả.
5. PORT-LOCK trả orderRevisionId/outboxId sau commit hoặc NEEDS_ATTENTION khi thiếu nguồn; không trả plan giả đã sẵn sàng. Gán default nằm trong giao dịch khóa, không commit riêng. Vận hành xem kết quả; API-ORD-020 chỉ đọc plan đã được worker tạo.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given default không thuộc MAIN ngày công bố; When scheduler khóa; Then 422 ERR-ORD-422-03; không phát hành kế hoạch.
- 3a. Biên/đồng thời:** Given chưa có total; có 100 người đăng ký; When scheduler khóa; Then total vẫn chưa xác định; không tự coi T=100; xử lý ORD-Q07.
- 3b. Service không đủ quyền:** dừng xử lý scope; không mượn phiên người dùng/cache để khóa. Mã ERR là lý do tham chiếu miền; port nội bộ không có HTTP status trực tiếp.
- 4a. Mất kết quả job:** đối soát operation/source hash và eventKey theo mapping; retry cùng sự kiện không tạo revision/outbox đôi. eventKey không phải header Idempotency-Key HTTP; không tự thêm API tra job.
- 4b. Nguồn/version đổi:** dừng khóa trên baseline cũ, ghi outcome để xử lý theo lifecycle; không tự lấy nguồn mới rồi dùng eventKey cũ. Remediation/override vẫn chờ ORD-Q07/12/O-06.
- 4c. Phụ thuộc gián đoạn:** chưa biết commit thì đối soát như 4a; chưa đủ nguồn thì không LOCKED giả. Retry worker plan tách retry lock; không mở lại order đã khóa.

### UC-ORD-011: Khóa tại hạn và phát hành nguồn kế hoạch

[Use case gốc](usecases/UC-ORD-011.md)

1. Scheduler nhận sự kiện đến hạn, resolve servicePointId/serviceDate/shift và deadlineVersion; không mở UI-ORD-09.
2. Service gọi PORT-LOCK(servicePointId,serviceDate,shift,deadlineVersion,eventKey); menu/default/quota/counter là nguồn server kiểm lại, không payload do vận hành tùy nhập.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Dùng clock server; khóa cạnh tranh với selection/submission; snapshot order/line, audit và outbox nguyên tử; worker tạo kế hoạch riêng. Retry event không tạo v2. Ngưỡng15:00 D-1 là giả định Q-16 chưa duyệt.
4. Hệ thống thực hiện scheduler khóa scope điểm/ngày/ca; kết quả theo điều kiện review: order LOCKED; một revision và một outbox event bền vững.
5. PORT-LOCK trả orderRevisionId/outboxId sau commit hoặc NEEDS_ATTENTION khi thiếu nguồn; không trả plan giả đã sẵn sàng. Gán default nằm trong giao dịch khóa, không commit riêng. Vận hành xem kết quả; API-ORD-020 chỉ đọc plan đã được worker tạo.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given clock server đúng bằng deadline; When người ăn gửi PUT; Then đề xuất 409 ERR-ORD-409-01; không ghi; biên deadline chờ ORD-Q07.
- 3a. Biên/đồng thời:** Given lock event đã xử lý, worker mất phản hồi; When retry cùng eventKey; Then trả revision cũ; không tăng plan revision lần hai.
- 3b. Service không đủ quyền:** dừng xử lý scope; không mượn phiên người dùng/cache để khóa. Mã ERR là lý do tham chiếu miền; port nội bộ không có HTTP status trực tiếp.
- 4a. Mất kết quả job:** đối soát operation/source hash và eventKey theo mapping; retry cùng sự kiện không tạo revision/outbox đôi. eventKey không phải header Idempotency-Key HTTP; không tự thêm API tra job.
- 4b. Nguồn/version đổi:** dừng khóa trên baseline cũ, ghi outcome để xử lý theo lifecycle; không tự lấy nguồn mới rồi dùng eventKey cũ. Remediation/override vẫn chờ ORD-Q07/12/O-06.
- 4c. Phụ thuộc gián đoạn:** chưa biết commit thì đối soát như 4a; chưa đủ nguồn thì không LOCKED giả. Retry worker plan tách retry lock; không mở lại order đã khóa.

### UC-ORD-012: Đề nghị và duyệt thay đổi sau khóa

[Use case gốc](usecases/UC-ORD-012.md)

1. Actor mở UI-ORD-10; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Người đề nghị gửi ChangeInput/API-ORD-005 theo baseline xác định; người duyệt đọc danh sách bằng API-ORD-021, rồi gửi DecisionInput/API-ORD-022 với version đề nghị và baseOrderRevisionId.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Không sửa trực tiếp snapshot khóa. Đề nghị có delta +/-; đánh giá ngưỡng theo Q-16; duyệt khác người tạo/sửa cuối; nếu được duyệt tạo version mới và thông báo bếp. Không tự sửa số đã giao/đối soát của E7.
4. Kiểm separation và baseline lúc quyết định. APPROVED tạo revision/outbox theo thiết kế nguyên tử; REJECTED không đổi order revision. Worker phát sinh kế hoạch riêng; response duyệt chưa chứng minh bếp đã nhận.
5. Hệ thống trả change request và revision nếu duyệt; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given đề nghị PENDING do U tạo; When U tự duyệt; Then 403 ERR-ORD-403-01; order vẫn rev1.
- 3a. Biên/đồng thời:** Given đề nghị dựa rev1 nhưng hiện hành rev2; When duyệt đề nghị cũ; Then 409 ERR-ORD-409-01; không áp delta lên sai baseline.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-013: Điều phối nhập hộ

[Use case gốc](usecases/UC-ORD-013.md)

1. Actor mở UI-ORD-11; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Đọc Summary qua API-ORD-003; gửi SubmissionInput qua API-ORD-004 với version của order và summaryVersion riêng. Nhập hộ phải có source/evidenceRef/reason theo quyền; tên field theo API, không lấy token Summary làm orders.version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Ghi nguồn ZALO/PHONE theo quyền, người nhập thay và bằng chứng; không gửi Zalo. Áp cùng version/deadline/định mức; không tự ghi đè lựa chọn cá nhân.
4. Hệ thống thực hiện nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason; kết quả theo điều kiện review: order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân.
5. Hệ thống trả order có nguồn nhập hộ; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given người ăn tự chọn có phiên hợp lệ; When gửi source ZALO để giả vai DDV; Then 403 ERR-ORD-403-01; không ghi order.
- 3a. Biên/đồng thời:** Given người đặt tổng và DDV cùng đọc version 1; When cả hai gửi tổng; Then một commit version 2; bên sau 409; không ghi đè mù.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-014: Nhắc người chưa chọn

[Use case gốc](usecases/UC-ORD-014.md)

1. Scheduler nhận sự kiện nhắc theo lịch, không mở UI; truyền scope,scheduledAt,eventId vào PORT-REM.
2. Worker kiểm cấu hình kênh, quyền scope và eligibility hiện tại trước gửi; giữ eventId để dedupe.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ người đủ điều kiện chưa chọn; lọc scope/dedupe; kênh ngoài Q-14 chưa chốt. Không tự gửi SMS/Zalo/email khi chưa có cấu hình và quyền.
4. Hệ thống thực hiện scheduler lập nhắc trước hạn; kết quả theo điều kiện review: chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi.
5. Ghi/trả ReminderRun theo outcome thực tế; việc gửi phụ thuộc kênh/policy đã duyệt. Vận hành đọc API-ORD-023; GET không enqueue/retry hoặc gửi thông báo.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given Q-14 chưa chốt hoặc thiếu cấu hình kênh; When job nhắc chạy; Then BLOCKED_CONFIGURATION; không gọi SMS/Zalo/email.
- 3a. Biên/đồng thời:** Given event nhắc đã thành công; When worker nhận lại eventId; Then không gửi lần hai; đối soát kết quả không tạo thông báo trùng.
- 3b. Quyền/eligibility đổi:** worker kiểm lại trước gửi và không gửi người ngoài phạm vi; người vận hành đọc lịch sử cũng phải qua kiểm quyền HTTP riêng.
- 4a. Mất phản hồi worker/provider:** đối soát eventId/kết quả gửi trước retry để tránh trùng; không tự đổi eventId hoặc coi GET reminder-runs là lệnh gửi lại. Retry/retention còn Q-14/E1-Q04.
- 4b. Nguồn người nhận đổi:** kiểm lại eligibility trước gửi; không dùng template stale-write409 hoặc yêu cầu người dùng gửi version cho PORT-REM.
- 4c. Thiếu cấu hình/phụ thuộc gián đoạn:** phân biệt BLOCKED_CONFIGURATION với kết quả gửi chưa xác định; không tự báo SENT hoặc giả rollback provider. HTTP503 chỉ áp dụng route HTTP theo ma trận lỗi.

### UC-ORD-015: Đổi chế độ chọn món

[Use case gốc](usecases/UC-ORD-015.md)

1. Actor mở UI-ORD-05; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,enabled,effectiveFrom,version,reason.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Khi tắt người đặt tổng nhập cho công ty. Đã có lựa chọn xử lý thế nào/hiệu lực giữa ngày chờ ORD-Q09; không âm thầm xóa lịch sử.
4. Hệ thống thực hiện người đặt tổng tắt chọn món; kết quả theo điều kiện review: người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền.
5. Hệ thống trả mode version; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given khách đã tắt chọn từ đầu ngày; When người ăn PUT trực tiếp; Then 409 ERR-ORD-409-01; không thay số suất.
- 3a. Biên/đồng thời:** Given đã có 60 lựa chọn; When đề nghị tắt giữa ngày; Then giữ 60 lựa chọn và lịch sử; tác động chờ ORD-Q09.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- 4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- 4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

### UC-ORD-016: Xem thông tin món công bố

[Use case gốc](usecases/UC-ORD-016.md)

1. Actor mở UI-ORD-06; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: published menu/day/dish.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ dữ liệu công bố: định lượng,4 chỉ số có nhãn ước tính,dị ứng và phạm vi tổ hợp; thiếu dữ liệu ghi chưa có, không điền0. DTO allowlist không có Cost/giá nhập/note nội bộ.
4. Hệ thống thực hiện người ăn mở chi tiết; kết quả theo điều kiện review: hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính.
5. Hệ thống trả DTO món an toàn đã lọc; đây là GET, không tạo selection/Calculation hoặc biên nhận ghi. Ghi log truy cập an toàn theo nền nếu cần.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given thiếu dữ liệu dinh dưỡng một nguyên liệu; When mở tổ hợp; Then totals=null và lý do thiếu; không hiển thị 0 như kết quả thật.
- 3a. Biên/đồng thời:** Given client dò field cost và id khách khác; When gọi available-meals; Then DTO chỉ allowlist; ngoài scope 404; lỗi không lộ cost/giá nhập.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi GET:** có thể đọc lại với kiểm quyền/scope hiện tại; không cần Idempotency-Key hoặc đối soát receipt ghi; không tự chốt retry limits.
- 4b. Nguồn/version đổi:** đọc lại theo contract query hiện có, hiển thị phiên bản nguồn của kết quả; không suy stale-write409 cho GET. Visibility/current/freshness còn gap, không tự chọn policy.
- 4c. Phụ thuộc gián đoạn:** ERR-ORD-503-01 theo ma trận lỗi; không giả dữ liệu cũ là hiện hành hoặc thiếu dữ liệu là0. requestId chỉ là correlation, không chứng minh commit.

### UC-ORD-017: Giữ cổng hồ sơ sức khỏe

[Use case gốc](usecases/UC-ORD-017.md)

1. Người ăn mở mục tương ứng trên UI-ORD-12; hiển thị trạng thái chưa mở, không tải hồ sơ sức khỏe.
2. Không yêu cầu profile, consentVersion hoặc dữ liệu sức khỏe; không gọi API sức khỏe/gợi ý vì catalog chưa có endpoint.
3. Giữ gate O-03; các yêu cầu consent, xóa/lưu vết và thuật toán chỉ là nội dung thiết kế tương lai chờ ORD-Q15/O-03.
4. Hiển thị chưa mở tính năng; người dùng có thể về luồng chọn món thủ công theo quyền sẵn có.
5. Kết thúc ở trạng thái gate; không request ghi, receipt, commit hoặc retry mutation; không trả gợi ý giả.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given client cố gửi bệnh lý khi gate đóng; When gọi đường ghi chưa công bố; Then không ghi dữ liệu; không tạo consent ngầm; contract chưa mở.
- 3a. Biên/đồng thời:** Given người dùng không đồng ý hoặc rút đồng ý trong thiết kế tương lai; When review hồ sơ; Then chưa được thu thập; tiêu chí xóa/lưu vết cần O-03 và ORD-Q15.
- 3b. Không đủ quyền truy cập UI:** dùng kiểm phiên/quyền nền nếu áp dụng; không tạo mã lỗi HTTP cho endpoint sức khỏe chưa tồn tại.
- 4a. Không tải được UI:** có thể mở lại trang; không có lệnh sức khỏe để replay hoặc dùng Idempotency-Key.
- 4b. Gate thay đổi trong tương lai:** chỉ thiết kế luồng mới sau evidence phê duyệt; không tự mở schema/contract trong phiên này.
- 4c. Phụ thuộc chưa sẵn sàng:** giữ trạng thái chưa mở; không fallback sang thu profile/consent hoặc suy diễn bệnh.

### UC-ORD-018: Giữ cổng gợi ý cá nhân

[Use case gốc](usecases/UC-ORD-018.md)

1. Người ăn mở mục tương ứng trên UI-ORD-12; hiển thị trạng thái chưa mở, không tải hồ sơ sức khỏe.
2. Không yêu cầu profile, consentVersion hoặc dữ liệu sức khỏe; không gọi API sức khỏe/gợi ý vì catalog chưa có endpoint.
3. Giữ gate O-03; các yêu cầu consent, xóa/lưu vết và thuật toán chỉ là nội dung thiết kế tương lai chờ ORD-Q15/O-03.
4. Hiển thị chưa mở tính năng; người dùng có thể về luồng chọn món thủ công theo quyền sẵn có.
5. Kết thúc ở trạng thái gate; không request ghi, receipt, commit hoặc retry mutation; không trả gợi ý giả.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given không có consent/hồ sơ hợp lệ; When yêu cầu suy bệnh từ lịch sử chọn; Then không suy diễn và không tự tạo hồ sơ.
- 3a. Biên/đồng thời:** Given gợi ý tương lai được duyệt; When review hành vi áp dụng; Then phải có lựa chọn tường minh; không tự ghi selection hoặc đổi order.
- 3b. Không đủ quyền truy cập UI:** dùng kiểm phiên/quyền nền nếu áp dụng; không tạo mã lỗi HTTP cho endpoint sức khỏe chưa tồn tại.
- 4a. Không tải được UI:** có thể mở lại trang; không có lệnh sức khỏe để replay hoặc dùng Idempotency-Key.
- 4b. Gate thay đổi trong tương lai:** chỉ thiết kế luồng mới sau evidence phê duyệt; không tự mở schema/contract trong phiên này.
- 4c. Phụ thuộc chưa sẵn sàng:** giữ trạng thái chưa mở; không fallback sang thu profile/consent hoặc suy diễn bệnh.

### UC-ORD-019: Đọc kế hoạch sản xuất phiên bản

[Use case gốc](usecases/UC-ORD-019.md)

1. Actor mở UI-ORD-13; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Bếp gửi kitchenId/date/shift cho danh sách hoặc planId/revisionNo cho chi tiết theo API; không gửi orderRevisionId để yêu cầu tổng hợp.
3. Authorize scope bếp và revision thuộc plan; đọc snapshot producer đã tạo. Nguồn/manifest thiếu phải thể hiện theo thiết kế hiện có, không tự coi COMPLETE; current/visibility còn E6-CG-06.
4. Trả snapshot và các source revisions được phép đọc. Ví dụ synthetic MAIN A=100 từ60+40 là kiểm dữ liệu producer đã chuẩn bị, không phép cộng làm phát sinh plan trong GET; role/unit còn ORD-Q10.
5. UI hiển thị dữ liệu đọc và revision; không thông báo đã ghi/đã nhận kế hoạch thay cho ack, không chuyển IN_PRODUCTION. Không cần receipt hoặc commit nghiệp vụ cho GET.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Đầu vào/quyền nghiệp vụ:** Given bếp K1 yêu cầu kế hoạch K2; When GET theo id K2; Then 404 ERR-ORD-404-01; không lộ tổng K2.
- 3a. Producer riêng/biên liên thông:** nguồn synthetic rev1→rev2 tăng A5 được worker xử lý trước GET kế tiếp; producer không cộng hai revision cùng order, plan cũ bất biến. Nhánh này kiểm producer+read, không lệnh tạo kế hoạch từ bếp.
- 3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- 4a. Mất phản hồi GET:** có thể đọc lại với kiểm quyền/scope hiện tại; không cần Idempotency-Key hoặc đối soát receipt ghi; không tự chốt retry limits.
- 4b. Nguồn/version đổi:** đọc lại theo contract query hiện có, hiển thị phiên bản nguồn của kết quả; không suy stale-write409 cho GET. Visibility/current/freshness còn gap, không tự chọn policy.
- 4c. Phụ thuộc gián đoạn:** ERR-ORD-503-01 theo ma trận lỗi; không giả dữ liệu cũ là hiện hành hoặc thiếu dữ liệu là0. requestId chỉ là correlation, không chứng minh commit.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| ERR-ORD-409-01 | “Dữ liệu đã thay đổi hoặc đã khóa. Tải lại trước khi chọn.” Không ghi selection/counter một phần | Xem ma trận lỗi |
| ERR-ORD-422-01 | “Lựa chọn không thuộc thực đơn hoặc vượt định mức.” Chọn lại | Xem ma trận lỗi |
| ERR-ORD-422-02 | “Tổng suất nhỏ hơn số đã phân bổ.” Người đặt tổng giải quyết, không xóa tự động | Xem ma trận lỗi |
| ERR-ORD-422-03 | “Chưa đủ dữ liệu để khóa.” Chuyển xử lý vận hành theo ORD-Q07 | Xem ma trận lỗi |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
