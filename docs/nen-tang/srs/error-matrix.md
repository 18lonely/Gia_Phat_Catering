---
id: DOC-NEN-TANG-SRS-ERROR-MATRIX
title: Ma trận lỗi E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e1]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E1: Nền tảng

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 24 dòng mã lỗi từ [SRS E1](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E1](spec.md).

| Mã ERR | HTTP | Điều kiện phát sinh | Khoá bản địa hoá | Thông báo hiển thị | Mức | Hành động tiếp theo |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `ERR-AUTH-401-01` | 401 | Sai tên đăng nhập hoặc mật khẩu | `auth.invalid_credentials` | "Tên đăng nhập hoặc mật khẩu không đúng." | Medium | Nhập lại; không cho biết trường nào sai |
| `ERR-AUTH-401-02` | 401 | Phiên hết hạn, bị thu hồi, hoặc refresh token đã dùng | `auth.session_expired` | "Phiên làm việc đã hết hạn. Vui lòng đăng nhập lại." | Medium | Chuyển về màn hình đăng nhập |
| `ERR-AUTH-401-03` | 401 | Mã xác thực 2 bước sai hoặc hết hạn | `auth.otp_invalid` | "Mã xác thực không đúng hoặc đã hết hạn." | Medium | Nhập mã mới |
| `ERR-AUTH-403-01` | 403 | Tài khoản bị khoá bởi quản trị | `auth.account_locked` | "Tài khoản đang bị khoá. Vui lòng liên hệ quản trị hệ thống." | High | Liên hệ quản trị |
| `ERR-AUTH-403-02` | 403 | Thiếu quyền thực hiện thao tác | `auth.forbidden` | "Bạn không có quyền thực hiện thao tác này." | High | Quay lại; liên hệ quản trị nếu cần quyền |
| `ERR-AUTH-404-01` | 404 | Không tìm thấy tài khoản | `auth.account_not_found` | "Không tìm thấy tài khoản." | Medium | Kiểm tra lại mã tài khoản |
| `ERR-AUTH-409-01` | 409 | Tên đăng nhập đã tồn tại | `auth.username_taken` | "Tên đăng nhập đã được dùng." | Medium | Chọn tên khác |
| `ERR-AUTH-422-01` | 422 | Mật khẩu mới không đạt `BR-SEC-001` | `auth.password_weak` | "Mật khẩu cần ít nhất 10 ký tự, có chữ và số, không trùng 3 mật khẩu gần nhất." | Medium | Nhập mật khẩu khác |
| `ERR-AUTH-422-02` | 422 | Vai trò theo cơ sở nhưng chưa gán cơ sở, hoặc không có vai trò nào | `auth.role_scope_invalid` | "Vai trò này cần gán ít nhất một cơ sở." | Medium | Chọn cơ sở |
| `ERR-AUTH-422-03` | 422 | Uỷ quyền cho chính mình, hoặc khoảng ngày không hợp lệ | `auth.delegation_invalid` | "Thông tin uỷ quyền không hợp lệ." | Medium | Sửa người nhận hoặc khoảng ngày |
| `ERR-AUTH-423-01` | 423 | Khoá tạm do sai mật khẩu 5 lần | `auth.temp_locked` | "Tài khoản tạm khoá 15 phút do nhập sai nhiều lần." | High | Đợi hoặc liên hệ quản trị |
| `ERR-AUTH-429-01` | 429 | Vượt giới hạn tần suất đăng nhập | `auth.rate_limited` | "Bạn thao tác quá nhanh. Vui lòng thử lại sau 1 phút." | Low | Đợi rồi thử lại |
| `ERR-SYS-403-01` | 403 | Người đề nghị tự duyệt, hoặc người tạo tự duyệt | `sys.self_approval` | "Bạn không thể duyệt nội dung do chính mình tạo hoặc sửa." | High | Chuyển cho người duyệt khác |
| `ERR-SYS-404-01` | 404 | Bản ghi không tồn tại hoặc ngoài phạm vi dữ liệu | `sys.not_found` | "Không tìm thấy dữ liệu." | Medium | Quay lại danh sách |
| `ERR-SYS-409-01` | 409 | Huỷ bản ghi đang được bản ghi khác đang hiệu lực tham chiếu | `sys.in_use` | "Không thể huỷ vì dữ liệu đang được sử dụng." | Medium | Xem danh sách nơi đang dùng |
| `ERR-SYS-409-02` | 409 | Bản ghi đã bị người khác sửa (lệch phiên bản) | `sys.version_conflict` | "Dữ liệu vừa được người khác cập nhật. Vui lòng tải lại." | Medium | Tải lại rồi sửa |
| `ERR-SYS-413-01` | 413 | Tệp lớn hơn 10 MB | `sys.file_too_large` | "Tệp vượt quá 10 MB." | Medium | Chọn tệp nhỏ hơn |
| `ERR-SYS-415-01` | 415 | Loại tệp không được hỗ trợ | `sys.file_type` | "Chỉ nhận tệp JPG, PNG, WEBP, PDF." | Medium | Chọn tệp đúng loại |
| `ERR-SYS-422-01` | 422 | Thiếu lý do hoặc lý do dưới 10 ký tự | `sys.reason_required` | "Vui lòng nhập lý do (ít nhất 10 ký tự)." | Medium | Nhập lý do |
| `ERR-SYS-422-02` | 422 | Giá trị tham số sai kiểu, ngoài khoảng, hoặc ngày hiệu lực trong quá khứ | `sys.param_invalid` | "Giá trị tham số không hợp lệ." | Medium | Sửa giá trị |
| `ERR-SYS-422-03` | 422 | Tham số phân trang ngoài khoảng: `page` < 1, `pageSize` < 1 hoặc > 100, hoặc không phải số nguyên | `sys.pagination_invalid` | "Tham số phân trang không hợp lệ." | Low | Giao diện không tạo ra lỗi này; lập trình viên sửa lời gọi |
| `ERR-SYS-500-01` | 500 | Lỗi không lường trước | `sys.internal` | "Có lỗi xảy ra. Vui lòng thử lại; nếu vẫn lỗi, gửi mã {requestId} cho quản trị." | Critical | Thử lại; báo quản trị |
| `ERR-SYS-502-01` | 502 | Kênh thông báo ngoài không phản hồi sau 3 lần thử | `sys.notify_failed` | (không hiện cho người dùng cuối; hiện trong trang tác vụ nền) | Low | Quản trị chạy lại |
| `ERR-SYS-503-01` | 503 | MySQL hoặc Redis không sẵn sàng | `sys.unavailable` | "Hệ thống đang bận. Vui lòng thử lại sau ít phút." | Critical | Thử lại; giám sát tự cảnh báo |
