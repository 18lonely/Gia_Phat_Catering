---
id: DOC-COST-TEST-SYSTEM-CASES
title: Ca hệ thống E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, system, e3]
author: BA
last_updated: 2026-11-16
---
# Ca hệ thống E3: Cost

Draft · 16/11/2026 · Thiết kế kiểm thử, chưa chạy.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo 8 ca xuyên nhiều FR theo khuôn chung các epic. Không thay 108 cặp AC, test hay 12 ca kế toán |

Ca hệ thống đi qua nhiều FR liên tiếp hoặc nhiều phân hệ. Chúng **trùng mục tiêu một phần** với [test case](test-cases.md), [ca kế toán](../accounting/acceptance.md) và [kịch bản](scenario-catalog.json), nên không cộng vào số mục tiêu độc lập. Dữ liệu dùng [fixture 10 món, 10 ngày giả định](fixtures/README.md); ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Kết quả mong đợi | Trạng thái | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-COST-SYS-01 | FR-COST-PRC, MEAL, ALR | Thực đơn đã duyệt ở CANH_BAO, cost % dưới ngưỡng | Nhập giá mới làm cost vượt ngưỡng; chờ tính lại | Tác vụ tính lại tạo đúng một cảnh báo cho ngày, chi tiết theo cơ sở; snapshot lúc duyệt giữ nguyên | NOT RUN | | |
| TC-COST-SYS-02 | NFR-COST-002 | Bảng tính tay 10 món, 10 ngày của kế toán (chưa có) | Tính cost món và cost % ngày, so với bảng tay | Cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm | BLOCKED DATA-COST-Q01 đến Q06 | | |
| TC-COST-SYS-03 | FR-COST-PRC-004; NFR-COST-003 | Lưới 200 dòng, một dòng giá 0 | Lưu lưới; sửa dòng lỗi; lưu lại | Lần đầu không lưu dòng nào; lần sau lưu đủ 200 dòng trong ≤ 3 giây | NOT RUN | | |
| TC-COST-SYS-04 | FR-COST-RUL-003; NFR-COST-005, 006, 007 | Tài khoản `svc-agent-dinh-duong-vien` | Gọi kiểm ngân sách; thử SELECT trực tiếp bảng giá; đọc log | Chỉ nhận đạt hoặc không đạt; SELECT bị từ chối ở CSDL; log không có cost | NOT RUN | | |
| TC-COST-SYS-05 | FR-COST-MEAL-005, 008; BR-SEC-008 | Đề nghị đổi chế độ kiểm sang CHAN | Người đề nghị tự duyệt; Giám đốc duyệt với ngày hiệu lực tương lai | Tự duyệt bị chặn; chế độ hiện tại không đổi trước ngày hiệu lực | NOT RUN | | |
| TC-COST-SYS-06 | FR-COST-EST; FLOW-COST-Q07 | Tuần 6 ngày, một ngày thiếu giá | Lập dự toán cả tuần | Theo hiện trạng: báo lỗi theo ngày; rollback cả tuần hay lưu ngày hợp lệ chờ quyết định | BLOCKED FLOW-COST-Q07 | | |
| TC-COST-SYS-07 | Kế toán VAT; CK | Giá báo chưa VAT, cờ không yêu cầu hóa đơn; chiết khấu 5% theo đơn | Tính giá cost và số phải trả nhà cung cấp | Giá cost gồm VAT; cờ hóa đơn không làm VAT thành 0; chiết khấu không giảm số phải trả | BLOCKED CK-Q01 (cơ sở tính chiết khấu) | | |
| TC-COST-SYS-08 | NFR-COST-004 | 50 thực đơn hiệu lực, 100 giá đổi cùng lúc | Chạy tính lại hàng loạt | Hoàn tất ≤ 5 phút; không cảnh báo trùng | BLOCKED O-04 (môi trường) | | |

8 ca. 0 ca đã chạy, Actual và Evidence để trống.
