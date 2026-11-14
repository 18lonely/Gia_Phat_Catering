---
id: DOC-AGENT-NOI-BO-TEST-R5-ACCEPTANCE
title: Ca nghiệm thu R5
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r5, e5]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R5 · v1.0.0: MVP: Agent Nội bộ dựng thực đơn (E5)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R5: R2, R3 xong; O-04 chọn xong nhà cung cấp mô hình. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R5-01 | Trên 20 yêu cầu thử, 100% thực đơn không vi phạm quy tắc cứng và không vượt ngưỡng cost | Bộ 20 yêu cầu được duyệt | TC-AIO-SYS-05 | BLOCKED AIO-Q03, O-04 |  |  |
| R5-02 | 0 món ngoài danh mục đã duyệt | Danh mục món đã duyệt | TC-AIO-SYS-05 | BLOCKED O-04 |  |  |
| R5-03 | Thực đơn tuần trả về trong ≤ 60 giây | Môi trường có mô hình | TC-AIO-SYS-05 | BLOCKED O-04 |  |  |
| R5-04 | 100% lượt chạy có nhật ký | Lượt chạy thành công và lỗi | TC-AIO-SYS-06 | NOT RUN |  |  |
| R5-05 | Thời gian dựng một thực đơn tuần giảm ≥ 50% so với trước MVP (BO-03) | Số đo trước MVP | Đo riêng, chưa có ca | BLOCKED AIO-Q03 (cách đo) |  |  |

R5 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
