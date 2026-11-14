---
id: DOC-NEN-TANG-UI-SCREENS
title: Màn hình và quyền E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [ui, screens, e1]
author: BA
last_updated: 2026-11-16
---
# Màn hình và quyền E1: Nền tảng

Draft · 16/11/2026 · Danh mục màn hình, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo danh mục 6 màn theo khuôn chung các epic, lấy từ wireframe và user flow hiện có |

| Màn | Tên | Nội dung | FR | API | Vai trò / gate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| UI-CORE-01 | Đăng nhập | Đăng nhập, xác thực 2 bước, đổi mật khẩu, đăng xuất | FR-AUTH-LGN-001 đến 004, FR-AUTH-PWD-001 | API-CORE-001 đến 005, 013 | Mọi nhân viên nội bộ; cách đăng nhập chờ N-01, MFA chờ N-04 |
| UI-CORE-02 | Tài khoản và quyền | Tạo tài khoản, khóa, gán vai trò và cơ sở, ủy quyền khi vắng, ma trận quyền | FR-AUTH-ACC-001 đến 003, FR-AUTH-PWD-002, FR-AUTH-RBAC-002/003 | API-CORE-006 đến 009, 011, 012, 014 | Quản trị; người giữ quyền quản trị chờ N-02 |
| UI-CORE-03 | Nhật ký | Nhật ký thay đổi chỉ đọc, nhật ký đăng nhập | FR-SYS-AUD-002, FR-AUTH-ACC-004 | API-CORE-010, 015 | Vai trò đọc audit nhạy cảm chờ E1-Q05 |
| UI-CORE-04 | Tham số | Xem tham số, đề nghị đổi, duyệt | FR-SYS-PRM-001/002 | API-CORE-016 đến 018 | Người đề nghị khác người duyệt (BR-SEC-008) |
| UI-CORE-05 | Thông báo | Danh sách, đánh dấu đã xem, đã xử lý | FR-SYS-NTF-001/002 | API-CORE-019, 020 | Người nhận; kênh ngoài chờ Q-14 |
| UI-CORE-06 | Tệp và tác vụ nền | Tải tệp, link truy cập tạm, theo dõi và chạy lại tác vụ | FR-SYS-FILE-001, FR-SYS-JOB-001 | API-CORE-021 đến 024 | Quản trị và người có quyền với thực thể chứa tệp |

FR không có màn riêng: FR-AUTH-RBAC-001 (kiểm quyền mỗi yêu cầu), FR-AUTH-SVC-001 (tài khoản dịch vụ), FR-SYS-AUD-001/003/004 (ghi nhật ký, bắt buộc lý do, hủy thay xóa), FR-SYS-NTF-003 (gửi kênh ngoài), FR-SYS-HLT-001 (kiểm tra sức khỏe). Chúng chạy bên dưới mọi màn.

[Wireframe HTML 6 màn](../html-wireframe/foundation-workbench.html) dùng dữ liệu giả lập, không gọi backend. [User flow](user-flow.md) · [Mapping dữ liệu](../api/data-mapping.md).
