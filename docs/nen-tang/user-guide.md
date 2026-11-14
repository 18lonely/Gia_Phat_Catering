---
id: DOC-NEN-TANG-USER-GUIDE
title: Hướng dẫn vận hành E1
version: 0.1.0
phase: Handoff
domain: Gia Phát
tags: [user-guide, e1]
author: BA
last_updated: 2026-11-16
---
# Hướng dẫn vận hành E1: Nền tảng

Phiên bản 0.1.0 · 16/11/2026 · Hướng dẫn theo thiết kế, chưa phải phần mềm triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo từ use case và ma trận lỗi hiện có theo khuôn /userguide; không thêm quy trình mới |

Người dùng chính: Quản trị hệ thống và mọi nhân viên nội bộ. Các bước dưới đây lấy nguyên văn từ luồng chính và nhánh rẽ của từng use case; khi use case đổi, hướng dẫn phải đổi theo. Bước nào còn chờ quyết định ghi trong [câu hỏi mở](review/questions.md) thì chưa vận hành được. Màn hình minh họa xem [wireframe](html-wireframe/) (dữ liệu giả lập).

## 1. Ai làm gì

Xem cột tác nhân trong [danh mục use case](usecases/index.md). Quyền cụ thể do quản trị cấp theo vai trò; vai trò không tự có quyền chỉ vì tên gọi.

## 2. Thao tác theo use case

### UC-CORE-001: Đăng nhập nội bộ

[Use case gốc](usecases/UC-CORE-001.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận tên đăng nhập, mật khẩu.
3. Xác thực nhân viên bằng tên đăng nhập và mật khẩu. Kiểm tra tài khoản đang hoạt động, chưa bị khoá. Ghi nhật ký đăng nhập cả khi thành công lẫn thất bại. Dạng tên đăng nhập: [N-01]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. sai mật khẩu lần5 → 423 ERR-AUTH-423-01; khóa15 phút; log thất bại.
- 3b. gửi11 lần/phút từ cùng IP → 429 ERR-AUTH-429-01; không xác thực vượt giới hạn.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-002: Làm mới phiên

[Use case gốc](usecases/UC-CORE-002.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận refresh token.
3. Đổi refresh token còn hạn lấy access token mới; refresh token cũ bị vô hiệu ngay (xoay vòng). Dùng lại refresh token đã vô hiệu → thu hồi mọi phiên của tài khoản.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. dùng lại R1 sau khi xoay thành R2 → 401 ERR-AUTH-401-02; thu hồi các phiên trong≤60 giây.
- 3b. hai request đồng thời dùng R1 → chỉ một refresh thành công; lần reuse kích hoạt thu hồi; client không gửi refresh song song.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-003: Đăng xuất

[Use case gốc](usecases/UC-CORE-003.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Thu hồi phiên hiện tại; tuỳ chọn thu hồi mọi phiên của mình.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. dùng lại access token của phiên vừa logout sau thời hạn thu hồi → 401 ERR-AUTH-401-02; không đọc nghiệp vụ.
- 3b. chọn allSessions=true → cảS1/S2 bị thu hồi, logout lại không tạo tác dụng phụ.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-004: Xác thực 2 bước

[Use case gốc](usecases/UC-CORE-004.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã 6 số.
3. Vai trò `GIAM_DOC`, `KT_DOANH_THU`, `QUAN_TRI` nhập thêm mã 6 số từ ứng dụng xác thực. Có làm hay không: [N-04]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. nhập mã6 số sai → 401 ERR-AUTH-401-03; không cấp phiên đầy đủ.
- 3b. mã đúng nhưng đã dùng trong bước xác thực trước → không cho replay; cách đăng ký/recovery chờ E1-Q03.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-005: Đổi mật khẩu

[Use case gốc](usecases/UC-CORE-005.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mật khẩu cũ, mật khẩu mới.
3. Người dùng đổi mật khẩu của mình; phải nhập đúng mật khẩu hiện tại. Sau khi đổi, mọi phiên khác bị thu hồi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. đặt mật khẩu9 ký tự hoặc thuộc3 mật khẩu gần nhất → 422 ERR-AUTH-422-01; mật khẩu không đổi.
- 3b. đổi thành công từS1 rồi gọi bằngS2 → S1 giữ, S2 thu hồi≤60 giây; không ghi mật khẩu/token vào audit.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-006: Cấp lại mật khẩu

[Use case gốc](usecases/UC-CORE-006.md)

1. Actor mở UI-CORE-01 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, lý do.
3. QUAN_TRI` cấp mật khẩu tạm cho một tài khoản. Mật khẩu tạm hết hạn sau 24 giờ và buộc đổi ở lần đăng nhập đầu.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. reset userId không tồn tại → 404 ERR-AUTH-404-01; không trả mật khẩu.
- 3b. dùng mật khẩu tạm sau24 giờ → không đăng nhập; mật khẩu tạm chỉ hiển thị một lần, retry không trả lại secret.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-007: Tạo tài khoản nội bộ

[Use case gốc](usecases/UC-CORE-007.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận họ tên, tên đăng nhập, vai trò, cơ sở.
3. QUAN_TRI` tạo tài khoản, gán ít nhất 1 vai trò; vai trò `QL_CO_SO`, `BEP_TRUONG` bắt buộc gán ít nhất 1 cơ sở.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. bỏ kitchenIds hoặc roles rỗng → 422 ERR-AUTH-422-02; không tạo user/role một phần.
- 3b. hai request tạo cùng tên đăng nhập → một tài khoản được tạo; request còn lại409 ERR-AUTH-409-01.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-008: Khoá / mở khoá tài khoản

[Use case gốc](usecases/UC-CORE-008.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, lý do.
3. Khoá làm tài khoản không đăng nhập được và thu hồi mọi phiên trong ≤ 60 giây.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. bỏ lý do hoặc nhập9 ký tự → 422 ERR-SYS-422-01; trạng thái không đổi.
- 3b. khóa rồi thử API ở giây60 → mọi phiên bị thu hồi; mở khóa không hồi sinh phiên cũ.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-009: Sửa vai trò và cơ sở

[Use case gốc](usecases/UC-CORE-009.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã tài khoản, vai trò, cơ sở, lý do.
3. Thay đổi có hiệu lực ở yêu cầu kế tiếp của người dùng, không cần đăng nhập lại.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. gửi version cũ → 409 ERR-SYS-409-02; không ghi đè.
- 3b. U1 gọi API K1 ngay yêu cầu kế tiếp → 404 ERR-SYS-404-01; quyền mới có hiệu lực, không cần đăng nhập lại.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-010: Xem nhật ký đăng nhập

[Use case gốc](usecases/UC-CORE-010.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận bộ lọc.
3. Lọc theo tài khoản, khoảng ngày, kết quả. Mỗi dòng: thời điểm, kết quả, địa chỉ IP, thiết bị.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. pageSize=101 → 422 ERR-SYS-422-03; không tự cắt về100.
- 3b. trang lớn hơn trang cuối → items rỗng,total đúng; không có mật khẩu/token trong log.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-011: Kiểm quyền mỗi yêu cầu

[Use case gốc](usecases/UC-CORE-011.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận token, tài nguyên.
3. Mỗi API khai báo quyền cần có. Hệ thống kiểm (1) tài khoản có quyền đó qua vai trò, (2) bản ghi được yêu cầu nằm trong phạm vi dữ liệu của tài khoản. Thiếu (1) → 403. Thiếu (2) → 404, để không lộ sự tồn tại của bản ghi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. U1 đọc id thuộcK2 → 404 ERR-SYS-404-01; không lộ tồn tại.
- 3b. U1 có hai vai trò, bỏ quyền ở một vai trò còn vai trò khác cấp → hợp quyền vai trò được áp dụng cùng phạm vi; không tự mở scopeK2.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-012: Xem ma trận vai trò – quyền

[Use case gốc](usecases/UC-CORE-012.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Hiển thị vai trò nào có quyền nào. Bản đầu chỉ đọc; thay đổi ma trận qua bản phát hành.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. thử PATCH ma trận vai trò → không có endpoint ghi; 405 hoặc không route; không sửa dữ liệu.
- 3b. vai trò QUAN_TRI mở Cost không được cấp → không suy QUAN_TRI có toàn quyền nghiệp vụ;403 ERR-AUTH-403-02.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-013: Uỷ quyền duyệt khi vắng

[Use case gốc](usecases/UC-CORE-013.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận người được uỷ, quyền, từ ngày, đến ngày.
3. Người có quyền duyệt chỉ định người thay trong một khoảng ngày. Người thay nhận đúng các quyền duyệt được uỷ, hết hạn tự thu hồi. Phụ thuộc [O-06]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. ủy quyền chính mình hoặc ngày kết thúc trước ngày bắt đầu → 422 ERR-AUTH-422-03.
- 3b. U2 là người sửa cuối bản ghi được đề nghị duyệt → 403 ERR-SYS-403-01; ủy quyền không phá tách người tạo/sửa và duyệt.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-014: Tài khoản dịch vụ cho agent

[Use case gốc](usecases/UC-CORE-014.md)

1. Actor mở UI-CORE-02 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Hai tài khoản tách biệt: `svc-agent-noi-bo`, `svc-agent-dinh-duong-vien`. Mỗi tài khoản có danh sách quyền gắn cứng, không đăng nhập qua giao diện.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. agent phía khách gọi cost hoặc SELECT bảng Cost bằng service DB account → 403 ở API và denied DB; không trả số trong lỗi.
- 3b. quyền user bị thu hồi giữa hai tool call → tool thứ hai từ chối; giao quyền service/user tính mỗi lần, không đăng nhập UI.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-015: Ghi nhật ký thay đổi

[Use case gốc](usecases/UC-CORE-015.md)

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận: (tự động).
3. Mọi lệnh tạo, sửa, huỷ, duyệt trên bảng nghiệp vụ sinh 1 bản ghi nhật ký trong cùng giao dịch cơ sở dữ liệu: ai, lúc nào, thực thể, mã bản ghi, hành động, giá trị cũ → mới của từng trường đổi, lý do, mã yêu cầu. Nếu thao tác do agent thực hiện: ghi cả tài khoản dịch vụ và người dùng đang dùng agent.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. gây lỗi ghi audit sau bước update → rollback cả update; không thay đổi nghiệp vụ không audit.
- 3b. gửi retry cùng idempotency key → chỉ một thay đổi và một audit nghiệp vụ; ghi đủ before/after và on_behalf.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-016: Tra cứu nhật ký

[Use case gốc](usecases/UC-CORE-016.md)

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận bộ lọc.
3. Lọc theo thực thể, mã bản ghi, người, khoảng ngày, hành động. Xem lịch sử của một bản ghi theo thứ tự thời gian.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. truy vấn history entityK2 → 404 ERR-SYS-404-01 hoặc list rỗng theo scope; không lộ dữ liệu.
- 3b. hai bản ghi cùng timestamp → thứ tự ổn định timestamp,id; kiểm trang tiếp không mất/lặp dòng.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-017: Bắt buộc lý do

[Use case gốc](usecases/UC-CORE-017.md)

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận lý do.
3. Thao tác thuộc danh sách ở `BR-AUD-001` bị từ chối nếu thiếu lý do từ 10 ký tự.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. reason chỉ có9 ký tự sau trim → 422 ERR-SYS-422-01; không ghi.
- 3b. reason đủ10 ký tự có chuỗi HTML → lưu chuỗi văn bản; UI escape; không chạy script.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-018: Huỷ thay cho xoá

[Use case gốc](usecases/UC-CORE-018.md)

1. Actor mở UI-CORE-03 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã bản ghi, lý do.
3. Không có API xoá cứng bản ghi nghiệp vụ. Huỷ đặt cờ, giữ dữ liệu, bản ghi huỷ không xuất hiện ở danh sách mặc định.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. hủy nguyên liệu được công thức hiệu lực tham chiếu → 409 ERR-SYS-409-01; không hủy.
- 3b. sau hủy tìm list mặc định và history → list không có; history giữ dữ liệu/cờ hủy; không SQL DELETE nghiệp vụ.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-019: Quản lý tham số

[Use case gốc](usecases/UC-CORE-019.md)

1. Actor mở UI-CORE-04 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã, giá trị, phạm vi, ngày hiệu lực, lý do.
3. Mỗi tham số có: mã, kiểu, giá trị, phạm vi áp dụng (toàn hệ thống / cơ sở / công ty khách / điểm phục vụ), ngày hiệu lực từ. Giá trị dùng cho một ngày nghiệp vụ là giá trị có hiệu lực tại ngày đó ở phạm vi hẹp nhất. Danh mục khởi tạo ở Phụ lục 4.3.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. effectiveFrom=D-1 hoặc value sai kiểu → 422 ERR-SYS-422-02; không sửa giá quá khứ.
- 3b. tra ngàyD vàD+1 có tham số toàn hệ thống vàK1 → D dùng bản cũ; D+1 dùng phạm vi hẹp nhất đã được duyệt; thiếu VAT vẫn null.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-020: Duyệt thay đổi tham số

[Use case gốc](usecases/UC-CORE-020.md)

1. Actor mở UI-CORE-04 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã đề nghị, quyết định, lý do.
3. Tham số gắn cờ "cần duyệt" chỉ có hiệu lực sau khi người có quyền duyệt chấp thuận; người đề nghị không tự duyệt.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. A hoặc người sửa cuối tự duyệt → 403 ERR-SYS-403-01; giữ trạng thái chờ.
- 3b. B duyệt rồi truy giá trị ngày trước hiệu lực → chỉ có hiệu lực từ ngày đã khai; audit bất biến.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-021: Tạo thông báo trong hệ thống

[Use case gốc](usecases/UC-CORE-021.md)

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận sự kiện.
3. Module nghiệp vụ phát sự kiện; SYS tạo thông báo cho người nhận theo vai trò và phạm vi. Mỗi thông báo: loại, tiêu đề, nội dung, liên kết tới bản ghi, mức độ.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. payload tham chiếuK2 mà người nhận chỉ cóK1 → không tạo/hiển thị dữ liệuK2; không để link bypass scope.
- 3b. worker nhận lạiE1 → đề xuất một thông báo/người/event; cách lưu unique chờ E1-Q04.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-022: Trạng thái thông báo

[Use case gốc](usecases/UC-CORE-022.md)

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận mã thông báo, trạng thái.
3. 3 trạng thái: mới, đã xem, đã xử lý. Danh sách lọc theo trạng thái; hiện số thông báo mới trên thanh điều hướng.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. U2 sửa trạng thái thông báoU1 → 404 ERR-SYS-404-01.
- 3b. U1 đánh dấu SEEN rồi RESOLVED và retry → đếm NEW giảm một; không tạo thông báo mới; hồi trạng thái chờ E1-Q04.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-023: Gửi qua kênh ngoài

[Use case gốc](usecases/UC-CORE-023.md)

1. Actor mở UI-CORE-05 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận người nhận, mẫu, dữ liệu.
3. Giao diện gửi chung cho mọi kênh; gửi qua hàng đợi, thử lại tối đa 3 lần, lưu kết quả từng lần gửi. Kênh cụ thể: [Q-14]
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. provider lỗi cả3 lần → trạng thái failed; ERR-SYS-502-01 ở job; không tự gửi lần4.
- 3b. retry sau provider đã nhận nhưng callback mất → cần provider messageId/idempotency; nếu chưa đối soát không phát lặp mù.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-024: Tải tệp lên

[Use case gốc](usecases/UC-CORE-024.md)

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; nhận tệp, thực thể gắn kèm.
3. Nhận JPG, PNG, WEBP, PDF; tối đa 10 MB mỗi tệp. Kiểm tra loại tệp theo nội dung, không theo đuôi tên. Tệp nội bộ chỉ truy cập qua liên kết có chữ ký, hết hạn sau 15 phút.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. đổi đuôi exe thành png hoặc tệp lớn hơn10MB → 415 ERR-SYS-415-01 hoặc413 ERR-SYS-413-01.
- 3b. mở signed URL sau15 phút hoặc actor khác entity → URL hết hạn/không được cấp; không công khai object storage.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-025: Tác vụ nền

[Use case gốc](usecases/UC-CORE-025.md)

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Hàng đợi có: thử lại với khoảng cách tăng dần, tối đa 5 lần; hàng đợi lỗi cho tác vụ hỏng hẳn; khoá chống chạy trùng cho tác vụ định giờ. `QUAN_TRI` xem được trạng thái và chạy lại tác vụ lỗi.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. worker lỗi đủ5 lần → chuyển hàng đợi lỗi; log từng lần; không retry vô hạn.
- 3b. hai worker claim cùng job định giờ → chỉ một hiệu ứng nghiệp vụ; admin replay không nhân đôi effect đã commit.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

### UC-CORE-026: Kiểm tra sức khoẻ

[Use case gốc](usecases/UC-CORE-026.md)

1. Actor mở UI-CORE-06 hoặc module gọi port được cấp quyền.
2. Hệ thống kiểm phiên, quyền và scope; không cần dữ liệu đầu vào.
3. Điểm kiểm tra `/v1/health` trả trạng thái API, MySQL, Redis, hàng đợi; dùng cho cân bằng tải và giám sát.
4. Trả kết quả, requestId và trạng thái; UI không báo thành công khi mất response.

Khi gặp nhánh rẽ hoặc lỗi:

- 2a. Thiếu quyền403 ERR-AUTH-403-02, ngoài scope404 ERR-SYS-404-01; dừng trước ghi.
- 3a. ngắt MySQL → 503 ERR-SYS-503-01; readiness không đạt.
- 3b. gọi health từ Internet không có quyền nội bộ → chỉ minimal status; không lộ DSN/secret/topology chi tiết.
- 4a. Offline/timeout: giữ input không chứa password; đối soát resource/version/key trước retry. Với port không có UI, lỗi về module gọi và rollback tương ứng.

## 3. Tra cứu sự cố

| Mã | Thông báo | Hướng xử lý |
| :--- | :--- | :--- |
| `ERR-AUTH-401-01` | "Tên đăng nhập hoặc mật khẩu không đúng." | Nhập lại; không cho biết trường nào sai |
| `ERR-AUTH-401-02` | "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." | Chuyển về màn hình đăng nhập |
| `ERR-AUTH-401-03` | "Mã xác thực không đúng hoặc đã hết hạn." | Nhập mã mới |
| `ERR-AUTH-403-01` | "Tài khoản đang bị khoá. Vui lòng liên hệ quản trị hệ thống." | Liên hệ quản trị |
| `ERR-AUTH-403-02` | "Bạn không có quyền thực hiện thao tác này." | Quay lại; liên hệ quản trị nếu cần quyền |
| `ERR-AUTH-404-01` | "Không tìm thấy tài khoản." | Kiểm tra lại mã tài khoản |
| `ERR-AUTH-409-01` | "Tên đăng nhập đã được dùng." | Chọn tên khác |
| `ERR-AUTH-422-01` | "Mật khẩu cần ít nhất 10 ký tự, có chữ và số, không trùng 3 mật khẩu gần nhất." | Nhập mật khẩu khác |
| `ERR-AUTH-422-02` | "Vai trò này cần gán ít nhất một cơ sở." | Chọn cơ sở |
| `ERR-AUTH-422-03` | "Thông tin uỷ quyền không hợp lệ." | Sửa người nhận hoặc khoảng ngày |
| `ERR-AUTH-423-01` | "Tài khoản tạm khoá 15 phút do nhập sai nhiều lần." | Đợi hoặc liên hệ quản trị |
| `ERR-AUTH-429-01` | "Bạn thao tác quá nhanh. Vui lòng thử lại sau 1 phút." | Đợi rồi thử lại |
| `ERR-SYS-403-01` | "Bạn không thể duyệt nội dung do chính mình tạo hoặc sửa." | Chuyển cho người duyệt khác |
| `ERR-SYS-404-01` | "Không tìm thấy dữ liệu." | Quay lại danh sách |
| `ERR-SYS-409-01` | "Không thể huỷ vì dữ liệu đang được sử dụng." | Xem danh sách nơi đang dùng |
| `ERR-SYS-409-02` | "Dữ liệu vừa được người khác cập nhật. Vui lòng tải lại." | Tải lại rồi sửa |
| `ERR-SYS-413-01` | "Tệp vượt quá 10 MB." | Chọn tệp nhỏ hơn |
| `ERR-SYS-415-01` | "Chỉ nhận tệp JPG, PNG, WEBP, PDF." | Chọn tệp đúng loại |
| `ERR-SYS-422-01` | "Vui lòng nhập lý do (ít nhất 10 ký tự)." | Nhập lý do |
| `ERR-SYS-422-02` | "Giá trị tham số không hợp lệ." | Sửa giá trị |
| `ERR-SYS-422-03` | "Tham số phân trang không hợp lệ." | Giao diện không tạo ra lỗi này; lập trình viên sửa lời gọi |
| `ERR-SYS-500-01` | "Có lỗi xảy ra. Vui lòng thử lại; nếu vẫn lỗi, gửi mã {requestId} cho quản trị." | Thử lại; báo quản trị |
| `ERR-SYS-502-01` | (không hiện cho người dùng cuối; hiện trong trang tác vụ nền) | Quản trị chạy lại |
| `ERR-SYS-503-01` | "Hệ thống đang bận. Vui lòng thử lại sau ít phút." | Thử lại; giám sát tự cảnh báo |

Nguồn: [ma trận lỗi](srs/error-matrix.md).

Mất phản hồi sau khi gửi: chưa biết đã lưu hay chưa. Tải lại và đối chiếu trước khi gửi lệnh mới, không tạo bản ghi lần hai.

## 4. Giới hạn

Chưa có backend, chưa có UAT. Hướng dẫn chỉ dùng để review quy trình và chuẩn bị đào tạo; không dùng làm tài liệu vận hành chính thức trước khi phần mềm được nghiệm thu.
