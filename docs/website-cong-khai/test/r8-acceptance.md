---
id: DOC-E8-TEST-R8-ACCEPTANCE
title: Ca nghiệm thu R8
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r8, e8]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R8 · v1.3.0: Website công khai (E8)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R8: R4 xong; DL-08 xong; có quyền quản trị tên miền. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R8-01 | 100% URL bài viết cũ trả về đúng trang hoặc 301 | Inventory WordPress DL-08 | TC-PUB-S05 | BLOCKED E8-Q01 |  |  |
| R8-02 | 100% lead từ form có bản ghi kèm nguồn | Nơi lưu lead được duyệt | TC-PUB-S03 | BLOCKED E8-Q06 |  |  |
| R8-03 | Trang thực đơn mẫu hiện đủ giá, định lượng, 4 chỉ số, dị ứng | Giá công khai được duyệt, nguồn E2, E4 | TC-PUB-S11 | BLOCKED E8-Q03, E8-Q04 |  |  |

R8 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
