---
id: DOC-DINH-DUONG-TEST-SYSTEM-CASES
title: Ca hệ thống E4
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, system, e4]
author: BA
last_updated: 2026-11-16
---
# Ca hệ thống E4: Dinh dưỡng

Draft · 16/11/2026 · Thiết kế kiểm thử, chưa chạy.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo 6 ca xuyên nhiều FR theo khuôn chung các epic. Không thay 28 ca trong test-cases |

Ca hệ thống **trùng mục tiêu một phần** với [test case E4](test-cases.md), nên không cộng vào số mục tiêu độc lập. Dữ liệu dùng [fixture giả lập](fixtures/README.md); ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Kết quả mong đợi | Trạng thái | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-NUTR-SYS-01 | FR-NUTR-REF-001, CALC-001, SNAP-001 | Món có 2 nguyên liệu đủ 4 chỉ số | Tính dinh dưỡng món; sửa giá trị một nguyên liệu; tính lại; mở kết quả cũ | Kết quả cũ giữ snapshot và revision cũ; kết quả mới dùng revision mới | NOT RUN | | |
| TC-NUTR-SYS-02 | FR-NUTR-REF-002; NFR-NUTR-001 | 30 món, một nguyên liệu thiếu chất béo | Kiểm độ phủ | Báo đúng nguyên liệu và món bị ảnh hưởng; không tính tổng như đủ | BLOCKED DATA-NUTR-Q01 | | |
| TC-NUTR-SYS-03 | FR-NUTR-CALC-002; NFR-NUTR-001 | 5 suất mẫu và số dinh dưỡng viên tính tay (chưa có) | Tính tổ hợp suất, so với số tay | Khớp theo chuẩn được duyệt ở NUTR-Q04 | BLOCKED NUTR-Q04, DATA-NUTR-Q01 | | |
| TC-NUTR-SYS-04 | FR-NUTR-CALC-002; NUTR-Q | Loại suất cho chọn 1 trong 3 món chính | Tính dinh dưỡng suất | Không cộng cả 3 món chính vào một suất | BLOCKED NUTR-Q03 | | |
| TC-NUTR-SYS-05 | NFR-NUTR-003 | Hai cơ sở; người dùng chỉ có quyền cơ sở A | Đọc kết quả tính của thực đơn khách riêng cơ sở B | 404, không lộ dữ liệu | NOT RUN | | |
| TC-NUTR-SYS-06 | NFR-NUTR-004 | Kết quả thiếu một chỉ số | Mở mọi nơi hiển thị tổng (E4, và E6, E8 khi có) | Có nhãn "ước tính từ định lượng sống", đơn vị, trạng thái thiếu | NOT RUN | | |

6 ca. 0 ca đã chạy, Actual và Evidence để trống.
