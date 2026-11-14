---
id: DOC-THUC-DON-REVIEW-DEPENDENCIES
title: Phụ thuộc E2 Thực đơn và định lượng
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [dependencies, e2]
author: BA
last_updated: 2026-11-16
---
# Phụ thuộc E2: Thực đơn và định lượng

Draft · 16/11/2026 · Gom từ [epic E2 mục 2.4](../epic-spec.md), roadmap và các epic dùng E2; không thêm quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic: E2 chờ gì, epic nào dùng E2 |

## 1. E2 đang chờ gì

| Cần có | Loại | Nguồn | Chặn |
| :--- | :--- | :--- | :--- |
| R1: tài khoản, phân quyền, nhật ký, tham số, thông báo | Kỹ thuật | [E1](../../nen-tang/srs/spec.md) | Toàn epic |
| DL-01: người soạn docx duyệt 43 quy tắc, trả lời H-1 đến H-9 | Nghiệp vụ | [Quy tắc thực đơn](../../gia-phat/brainstorms/quy-tac-thuc-don.md) | Số liệu bộ kiểm quy tắc; 86 ca quy tắc BLOCKED |
| DL-03 đến DL-05: danh sách nguyên liệu, 30 món, công thức, giá bán | Dữ liệu | [Roadmap](../../gia-phat/02-roadmap.md) | Nghiệm thu R2 |
| O-02: một hay nhiều cỡ định lượng | Quyết định | [BRD mục 11](../../gia-phat/06-brd.md) | FR-MENU-RCP-007 |
| O-06: ai duyệt | Quyết định | BRD mục 11 | Duyệt món, công thức, thực đơn, giá |
| E2-Q1 đến E2-Q11, MENU-API-Q01 đến Q03 | Quyết định | [Câu hỏi E2](questions.md) | Theo từng FR |

## 2. Epic nào dùng E2

| Epic dùng | Dùng gì của E2 | Ghi chú |
| :--- | :--- | :--- |
| E3 Cost | Nguyên liệu, công thức, loại suất, thực đơn; chỗ móc kiểm cost vào cổng gửi duyệt MENU | Cost không tự đổi cổng MENU |
| E4 Dinh dưỡng | Nguyên liệu và định lượng công thức | Ý nghĩa định lượng sống chờ NUTR-Q |
| E5 Agent Nội bộ | Bộ kiểm quy tắc không lưu (FR-MENU-RUL-002), áp dụng phương án thành bản nháp | Agent không tự công bố |
| E6 Chọn món | Thực đơn đã công bố, món và vai trò món | Người ăn chỉ thấy bản công bố |
| E8 Website | Projection công khai của thực đơn mẫu | E8-Q04 chờ |
| E9 Agent Dinh dưỡng viên | Danh mục món đã duyệt, bộ kiểm quy tắc | Chỉ projection không có cost |
| E11 Mua hàng | Loại bảo quản nguyên liệu, vai trò món cho thay món, cổng MENU | Thay món phải qua cổng MENU |
| E10, E12 | Thực đơn có phiên bản cho báo giá; dữ liệu món cho phân tích lựa chọn | Chỉ đọc |
