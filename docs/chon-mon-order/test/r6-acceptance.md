---
id: DOC-E6-TEST-R6-ACCEPTANCE
title: Ca nghiệm thu R6
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r6, e6]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R6 · v1.1.0: Chọn món và order (E6)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R6: Cổng G-Now đạt; chốt kênh thông báo (Q-14); O-03 có câu trả lời nếu làm FEAT-046, 047. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R6-01 | 1000 người dùng đồng thời chọn món trong 10 phút trước hạn chốt, 0 lựa chọn bị mất hoặc ghi trùng | Môi trường tải, profile | TC-E6-SYS-01, 02 | BLOCKED O-04, ORD-Q07 |  |  |
| R6-02 | Tại hạn chốt 100% suất chưa chọn được gán món mặc định | Quy tắc khóa và món mặc định | TC-E6-SYS-02, 12 | BLOCKED ORD-Q07, CG05 |  |  |
| R6-03 | Tổ hợp vượt định mức bị chặn | Định mức công ty | TC-E6-SYS-12; test case FR-ORD-QTA | BLOCKED ORD-Q (định mức) |  |  |
| R6-04 | Chạy thử với 2 công ty khách trong 2 tuần | Hai khách thật đồng ý chạy thử | TC-E6-SYS-12 | BLOCKED G-Now |  |  |

R6 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
