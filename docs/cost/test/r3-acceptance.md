---
id: DOC-COST-TEST-R3-ACCEPTANCE
title: Ca nghiệm thu R3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r3, e3]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R3 · v0.3.0: Cost (E3)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R3: R2 xong; DL-02 xong. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R3-01 | 10 món lệch không quá 1 đ so với kế toán (NFR-COST-002) | Bảng tính tay 10 món của kế toán | TC-COST-SYS-02 | BLOCKED DATA-COST-Q01 đến Q06 |  |  |
| R3-02 | 10 ngày cost % lệch không quá 0,01 điểm phần trăm | Bảng tính tay 10 ngày của kế toán | TC-COST-SYS-02 | BLOCKED DATA-COST-Q01 đến Q06 |  |  |
| R3-03 | CHAN chặn gửi duyệt khi vượt, CANH_BAO cảnh báo, thiếu đầu vào vẫn chặn | Tham số chế độ kiểm | TC-MENU-SYS-02 | NOT RUN |  |  |
| R3-04 | Công bố qua cổng MENU | Luồng duyệt E2 | TC-MENU-SYS-01 | BLOCKED DL-01 |  |  |
| R3-05 | Dự toán đủ cột theo SRS FR-COST-EST-004 | Thực đơn đã duyệt và số suất | Test case FR-COST-EST | BLOCKED E3-Q8 (nguồn số suất) |  |  |

R3 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
