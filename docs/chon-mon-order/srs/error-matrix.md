---
id: DOC-E6-SRS-ERROR-MATRIX
title: Ma trận lỗi E6
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [error-matrix, e6]
author: BA
last_updated: 2026-11-16
---
# Ma trận lỗi E6: Chọn món và order

Draft · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Chuyển nguyên văn 4 dòng mã lỗi từ [SRS E6](spec.md) sang file riêng theo khuôn chung các epic. Không đổi mã hay nội dung |

Ghi chú về lỗi và quy tắc liên quan vẫn nằm trong [SRS E6](spec.md).

| Mã | HTTP / trigger | Thông báo / xử lý |
| :--- | :--- | :--- |
| ERR-ORD-409-01 | 409 version/deadline snapshot đã đổi | “Dữ liệu đã thay đổi hoặc đã khóa. Tải lại trước khi chọn.” Không ghi selection/counter một phần |
| ERR-ORD-422-01 | 422 tổ hợp/món/định mức không hợp lệ | “Lựa chọn không thuộc thực đơn hoặc vượt định mức.” Chọn lại |
| ERR-ORD-422-02 | 422 T<S+C | “Tổng suất nhỏ hơn số đã phân bổ.” Người đặt tổng giải quyết, không xóa tự động |
| ERR-ORD-422-03 | 422 thiếu total/default/định mức tại lúc khóa | “Chưa đủ dữ liệu để khóa.” Chuyển xử lý vận hành theo ORD-Q07 |
