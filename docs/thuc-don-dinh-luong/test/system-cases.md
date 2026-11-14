---
id: DOC-THUC-DON-TEST-SYSTEM-CASES
title: Ca hệ thống E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, system, e2]
author: BA
last_updated: 2026-11-16
---
# Ca hệ thống E2: Thực đơn và định lượng

Draft · 16/11/2026 · Thiết kế kiểm thử, chưa chạy.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo 8 ca xuyên nhiều FR theo khuôn chung các epic. Không thay ca trong test-cases hay rule-test-cases |

Ca hệ thống đi qua nhiều FR liên tiếp hoặc nhiều phân hệ. Chúng **trùng mục tiêu một phần** với [test case](test-cases.md) và [ca quy tắc](rule-test-cases.md), nên không cộng vào số mục tiêu độc lập. Dữ liệu dùng [fixture giả lập](fixtures/README.md); ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Kết quả mong đợi | Trạng thái | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-MENU-SYS-01 | FR-MENU-ING, DISH, RCP, MNU, RUL, APV | Bộ fixture 3 nguyên liệu, 2 món | Tạo nguyên liệu, món, công thức; gửi duyệt và duyệt; dựng thực đơn 1 tuần; kiểm quy tắc; gửi duyệt; duyệt; công bố | Mọi bước đúng trạng thái; thực đơn chỉ công bố sau duyệt; audit đủ | BLOCKED DL-01 (số liệu quy tắc) | | |
| TC-MENU-SYS-02 | FR-MENU-APV-001; hook Cost | Thực đơn đạt quy tắc cứng; tham số `COST_CHE_DO_KIEM` = CHAN rồi CANH_BAO | Gửi duyệt khi cost vượt ngưỡng ở từng chế độ; thiếu giá một nguyên liệu | CHAN chặn gửi duyệt; CANH_BAO cho gửi kèm cảnh báo; thiếu đầu vào luôn chặn | NOT RUN | | |
| TC-MENU-SYS-03 | FR-MENU-RCP-003/004; BR-SEC-008 | Công thức do dinh dưỡng viên A lập | A tự duyệt; B duyệt; tạo phiên bản mới có hiệu lực tương lai | Tự duyệt bị chặn (tiêu chí R2); thực đơn ngày cũ vẫn dùng phiên bản cũ | NOT RUN | | |
| TC-MENU-SYS-04 | FR-MENU-RUL-006; E2-Q11 | Thực đơn ở DRAFT và một thực đơn PENDING | Đổi điểm phạt một quy tắc mềm qua đề nghị đã duyệt; kiểm lại cả hai | DRAFT kiểm theo quy tắc mới; PENDING giữ kết quả lúc gửi (theo hiện trạng, chờ E2-Q11) | BLOCKED E2-Q11 | | |
| TC-MENU-SYS-05 | FR-MENU-RUL-002; NFR-MENU-002, 005 | Danh mục quy tắc cố định | 20 lần gọi đồng thời kiểm không lưu với cùng phương án | Cùng kết quả cả 20 lần; p95 ≤ 2 giây; không ghi `menu_rule_results` | NOT RUN | | |
| TC-MENU-SYS-06 | FR-MENU-IMP-001 đến 003; NFR-MENU-003 | Tệp 2.000 dòng, có 5 dòng lỗi | Kiểm tệp, xem lỗi, nhập | Báo đúng 5 dòng lỗi; nhập chỉ tạo mới; tệp lớn chạy qua tác vụ nền | BLOCKED MENU-API-Q03 | | |
| TC-MENU-SYS-07 | FR-MENU-APV-004/005 | Thực đơn đã công bố và E6 đã có lựa chọn của người ăn (giả lập) | Thu hồi, sửa, mở lại | Thu hồi có lý do và audit; tác động lên lựa chọn đã có được báo, không xóa im lặng; thu hồi cả tuần hay từng ngày chờ E2-Q8 | BLOCKED E2-Q8 | | |
| TC-MENU-SYS-08 | FR-MENU-RCP-007; O-02 | Món có 2 cỡ định lượng | Lập công thức cho từng cỡ | Chưa chạy được vì chưa chốt một hay nhiều cỡ | BLOCKED O-02 | | |

8 ca. 0 ca đã chạy, Actual và Evidence để trống.
