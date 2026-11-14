---
id: DOC-NEN-TANG-TEST-SYSTEM-CASES
title: Ca hệ thống E1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, system, e1]
author: BA
last_updated: 2026-11-16
---
# Ca hệ thống E1: Nền tảng

Draft · 16/11/2026 · Thiết kế kiểm thử, chưa chạy.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo 8 ca xuyên nhiều FR theo khuôn chung các epic. Không thay ca trong test-cases |

Ca hệ thống đi qua nhiều FR liên tiếp hoặc nhiều phân hệ. Chúng **trùng mục tiêu một phần** với ca NFR, BR, ERR trong [test case E1](test-cases.md), nên không cộng vào số mục tiêu độc lập. Dữ liệu dùng [fixture giả lập](fixtures/README.md); ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Kết quả mong đợi | Trạng thái | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-CORE-SYS-01 | FR-AUTH-ACC-001 đến 003, FR-AUTH-LGN-001, FR-SYS-AUD-001 | Tài khoản quản trị giả lập; cơ sở A, B | Tạo tài khoản bếp trưởng cơ sở A, đăng nhập lần đầu, đổi mật khẩu, đổi cơ sở sang B, khóa tài khoản | Mỗi bước có audit đủ actor, trước sau, lý do; phiên cũ bị thu hồi khi khóa; đổi cơ sở có hiệu lực ở yêu cầu kế tiếp | BLOCKED N-01, N-02 | | |
| TC-CORE-SYS-02 | FR-AUTH-RBAC-001; NFR-SEC-001 | Hai quản lý cơ sở A, B; dữ liệu MENU, COST giả lập của cả hai cơ sở | Quản lý A gọi mọi route đọc của E1 đến E3 với ID thuộc cơ sở B | 404 ngoài phạm vi, không lộ tên, số liệu hay tồn tại bản ghi của B; đây là tiêu chí R1 | NOT RUN | | |
| TC-CORE-SYS-03 | FR-AUTH-RBAC-003, FR-SYS-PRM-002; BR-SEC-008 | Giám đốc ủy quyền duyệt cho người B trong 3 ngày | B duyệt một đề nghị tham số do chính B lập; B duyệt đề nghị của người khác; hết hạn ủy quyền rồi duyệt lại | Tự duyệt bị chặn; duyệt hợp lệ ghi `delegation_id`; sau hạn bị 403 | BLOCKED O-06 | | |
| TC-CORE-SYS-04 | FR-AUTH-SVC-001; BR-SEC-009/010 | Tài khoản `svc-agent-noi-bo`, `svc-agent-dinh-duong-vien`; người dùng có và không có quyền cost | Agent gọi công cụ thay hai người dùng khác nhau | Quyền hữu hiệu là giao của hai bên; agent khách không đọc được bảng cost ở mức CSDL | NOT RUN | | |
| TC-CORE-SYS-05 | FR-SYS-AUD-003/004; NFR-REL-001 | Một thực thể MENU đang dùng | Hủy bản ghi không lý do, có lý do; thử xóa cứng qua API | Thiếu lý do bị 422; hủy là đổi trạng thái có audit; không có đường xóa cứng | NOT RUN | | |
| TC-CORE-SYS-06 | FR-SYS-NTF-001/002, FR-SYS-JOB-001 | Tác vụ nền giả lập thất bại 2 lần | Chạy tác vụ, để lỗi, chạy lại thủ công | Thông báo tạo một lần cho mỗi sự cố, không trùng; chạy lại có audit | BLOCKED E1-Q04 | | |
| TC-CORE-SYS-07 | NFR-PERF-001/002, NFR-CAP-001 | Môi trường tải; profile 1000 người dùng đồng thời trên API mẫu | Chạy kịch bản đọc và ghi hỗn hợp 30 phút | p95 đọc ≤ 300 ms, ghi ≤ 800 ms; 0 lỗi phân quyền do tải | BLOCKED O-04 (hạ tầng) | | |
| TC-CORE-SYS-08 | FR-SYS-FILE-001; NFR-SEC-004 | Tệp riêng của thực thể A | Người không có quyền với A xin link; người có quyền xin link rồi dùng sau hạn | Không có link khi không quyền; link hết hạn bị từ chối; không lộ `storage_key` | NOT RUN | | |

8 ca. 0 ca đã chạy, Actual và Evidence để trống. Không dùng kiểm wireframe thay cho kết quả sản phẩm.
