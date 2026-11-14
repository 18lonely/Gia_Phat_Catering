---
id: DOC-E7-TEST-R7-ACCEPTANCE
title: Ca nghiệm thu R7
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r7, e7]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R7 · v1.2.0: Giao nhận và doanh thu (E7)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R7: R6 xong; chốt quy tắc khi khách không xác nhận (Q-13). Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R7-01 | Doanh thu một tháng do hệ thống tính khớp biên bản đối soát của 2 công ty chạy thử | Biên bản thật 2 khách một tháng | TC-E7-SYS-04 | BLOCKED E7-Q04, dữ liệu thật |  |  |
| R7-02 | File xuất nhập được vào MISA | Mẫu nhập MISA có phiên bản | TC-E7-SYS-04 | BLOCKED E7-Q07 |  |  |
| R7-03 | Kỳ đã khóa không sửa được nếu Giám đốc chưa duyệt mở lại | Kỳ khóa giả lập | Test case FR-FIN-LOCK, RREQ, RDEC | NOT RUN |  |  |

R7 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
