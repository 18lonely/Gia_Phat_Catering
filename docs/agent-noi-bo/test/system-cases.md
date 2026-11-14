---
id: DOC-AGENT-NOI-BO-TEST-SYSTEM-CASES
title: Ca hệ thống E5
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, system, e5]
author: BA
last_updated: 2026-11-16
---
# Ca hệ thống E5: Agent Nội bộ

Draft · 16/11/2026 · Thiết kế kiểm thử, chưa chạy, không gọi mô hình AI.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo 7 ca xuyên nhiều FR và phân hệ theo khuôn chung các epic. Không thay 32 ca trong test-cases |

Ca hệ thống **trùng mục tiêu một phần** với [test case E5](test-cases.md), nên không cộng vào số mục tiêu độc lập. Dữ liệu dùng [fixture giả lập](fixtures/README.md); ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Kết quả mong đợi | Trạng thái | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-AIO-SYS-01 | FR-AIO-GEN, CHK, APLY; E2 FR-MENU-APV-001 | Danh mục món đã duyệt giả lập | Yêu cầu dựng tuần; xem kết quả kiểm; áp dụng thành bản nháp; gửi duyệt MENU | Bản nháp MENU tạo đúng một lần; gửi duyệt đi qua cổng MENU và Cost như thực đơn tay | BLOCKED O-04 (mô hình) | | |
| TC-AIO-SYS-02 | FR-AIO-CHK-001; AIO-Q02 | Phương án đạt quy tắc cứng, cost vượt ngưỡng; chế độ CANH_BAO | Chạy kiểm | Không trả VALID | BLOCKED AIO-Q02 | | |
| TC-AIO-SYS-03 | FR-AIO-APLY-001 | Phương án đã kiểm; người khác sửa thực đơn gốc trong lúc đó | Áp dụng | 409 vì version gốc đổi; không ghi dở dang | NOT RUN | | |
| TC-AIO-SYS-04 | FR-AIO-EDIT-001 | Phương án đã kiểm | Chỉnh bằng lời; áp dụng revision cũ | Revision mới có hash mới và phải kiểm lại; áp dụng revision cũ bị từ chối | NOT RUN | | |
| TC-AIO-SYS-05 | NFR-AIO-001 | Bộ 20 yêu cầu thử được duyệt (chưa có) | Chạy 20 yêu cầu | 100% đạt quy tắc cứng, không vượt cost; 0 món ngoài danh mục; mỗi tuần ≤ 60 giây | BLOCKED AIO-Q03, O-04 | | |
| TC-AIO-SYS-06 | NFR-AIO-003; FR-AIO-OPS-001 | Lượt chạy bị ngắt giữa chừng (timeout giả lập) | Theo dõi và kết thúc lượt lỗi; mở nhật ký | Có log bền vững; không có nháp để áp dụng; trạng thái kết thúc rõ | NOT RUN | | |
| TC-AIO-SYS-07 | NFR-AIO-004; BR-SEC-009 | Người dùng quản lý cơ sở A, không có quyền cost | Yêu cầu agent đọc cost và dữ liệu cơ sở B, kèm câu chèn lệnh | Không vượt giao quyền; không lộ cost hay dữ liệu cơ sở B; không lộ secret | NOT RUN | | |

7 ca. 0 ca đã chạy, Actual và Evidence để trống.
