---
id: DOC-NEN-TANG-TEST-R1-ACCEPTANCE
title: Ca nghiệm thu R1
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, acceptance, r1, e1]
author: BA
last_updated: 2026-11-16
---
# Ca nghiệm thu R1 · v0.1.0: Nền tảng (E1)

Draft · 16/11/2026 · Chưa chạy, chưa nghiệm thu.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn ca nghiệm thu R9 đến R13; tiêu chí lấy nguyên từ roadmap |

Tiêu chí nghiệm thu lấy nguyên văn ý từ [roadmap](../../gia-phat/02-roadmap.md), không thêm hay nới. Điều kiện bắt đầu R1: O-04 có câu trả lời về hạ tầng; O-06 có người duyệt. Ghi bằng chứng theo [protocol](evidence-protocol.md).

| Mã | Tiêu chí roadmap | Dữ liệu hoặc điều kiện cần | Ca liên quan | Trạng thái | Kết quả | Bằng chứng |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| R1-01 | 5 vai trò nội bộ đăng nhập được | Fixture tài khoản; hình thức đăng nhập N-01 | TC-CORE-SYS-01; test case FR-AUTH-LGN | BLOCKED N-01 |  |  |
| R1-02 | Quản lý cơ sở A không đọc được dữ liệu cơ sở B | Dữ liệu hai cơ sở | TC-CORE-SYS-02 | NOT RUN |  |  |
| R1-03 | 100% thao tác sửa số liệu có bản ghi nhật ký | Danh sách mọi route ghi của E1 đến E3 | TC-CORE-SYS-01, 05 | NOT RUN |  |  |
| R1-04 | Kiểm thử tải 1000 người dùng đồng thời, p95 ≤ 300 ms đọc, ≤ 800 ms ghi trên API mẫu | Môi trường tải, profile được duyệt | TC-CORE-SYS-07 | BLOCKED O-04 |  |  |

R1 chỉ đạt khi mọi dòng có kết quả đạt kèm bằng chứng trên sản phẩm thật. Ca chức năng và ca hệ thống đạt không tự làm dòng nghiệm thu đạt. Dữ liệu giả lập không thay dữ liệu thật mà tiêu chí yêu cầu.
