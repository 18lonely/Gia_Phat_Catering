---
id: DOC-THUC-DON-TEST-R2-ACCEPTANCE
title: Ca nghiệm thu R2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r2, e2]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R2 · v0.2.0: Thực đơn và định lượng (E2)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R2: R1 xong; DL-01 xong; O-02 có câu trả lời. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R2-01 | Đủ 30 món có đủ 12 thuộc tính và công thức đã duyệt | DL-03 đến DL-05 | TC-MENU-SYS-01 | BLOCKED DL-03 đến DL-05 |  |  |
| R2-02 | Mỗi quy tắc được duyệt ở DL-01 có ít nhất 1 ca đạt và 1 ca vi phạm | Danh sách quy tắc DL-01 | 86 ca trong rule-test-cases | BLOCKED DL-01 |  |  |
| R2-03 | Thực đơn vi phạm quy tắc cứng không gửi duyệt được | Danh sách quy tắc cứng | TC-MENU-SYS-01 | BLOCKED DL-01 |  |  |
| R2-04 | Công thức không tự duyệt được bởi người tạo | Hai tài khoản dinh dưỡng viên và người duyệt | TC-MENU-SYS-03 | NOT RUN |  |  |

R2 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
