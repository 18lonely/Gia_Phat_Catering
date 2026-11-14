---
id: DOC-DINH-DUONG-TEST-R4-ACCEPTANCE
title: Ca nghiệm thu R4
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r4, e4]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R4 · v0.4.0: Dinh dưỡng (E4)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R4: R2 xong; có nguồn dữ liệu (BRD DP-03). Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R4-01 | 100% nguyên liệu của 30 món có đủ 4 chỉ số | Mapping 30 món, ấn bản bảng thành phần | TC-NUTR-SYS-02 | BLOCKED NUTR-Q01, DATA-NUTR-Q01 |  |  |
| R4-02 | Dinh dưỡng 5 suất mẫu do hệ thống tính khớp số dinh dưỡng viên tính tay | 5 suất tính tay độc lập; chuẩn khớp | TC-NUTR-SYS-03 | BLOCKED NUTR-Q04, DATA-NUTR-Q01 |  |  |
| R4-03 | Giao diện ghi nhãn "ước tính từ định lượng sống" | Màn hình E4 | TC-NUTR-SYS-06 | NOT RUN |  |  |

R4 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
