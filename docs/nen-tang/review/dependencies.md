---
id: DOC-NEN-TANG-REVIEW-DEPENDENCIES
title: Phụ thuộc E1 Nền tảng
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [dependencies, e1]
author: BA
last_updated: 2026-11-16
---
# Phụ thuộc E1: Nền tảng

Draft · 16/11/2026 · Gom từ roadmap, SRS và các epic dùng E1; không thêm quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic: E1 chờ gì, epic nào dùng E1 |

## 1. E1 đang chờ gì

| Cần có | Loại | Nguồn | Chặn |
| :--- | :--- | :--- | :--- |
| Hạ tầng, đội phát triển, nhà cung cấp (O-04) | Quyết định | [BRD mục 11](../../gia-phat/06-brd.md) | Bắt đầu R1 theo [roadmap](../../gia-phat/02-roadmap.md) |
| Người duyệt và người thay khi vắng (O-06) | Quyết định | BRD mục 11 | Bắt đầu R1; FR-AUTH-RBAC-003 |
| Cách đăng nhập, người giữ quyền quản trị, thời gian lưu nhật ký, bắt buộc 2 bước (N-01 đến N-04) | Quyết định | [SRS E1](../srs/spec.md) | FR-AUTH-LGN, FR-AUTH-ACC, FR-SYS-AUD |
| Envelope lỗi, phân trang, idempotency, MFA, thông báo, quyền đọc audit, cách đo NFR-PERF-003 (E1-Q01 đến E1-Q06) | Quyết định kỹ thuật | [Câu hỏi E1](questions.md) | Freeze hợp đồng API cho mọi epic |
| Công nghệ backend Rust/Axum (D-22) | Đã chốt 14/11/2026 | [CR-CORE-2026-001](../cr/CR-CORE-2026-001.md) | Không chặn; tên thư viện vẫn là đề xuất |

E1 không chờ dữ liệu của epic nào khác.

## 2. Epic nào dùng E1

| Epic dùng | Dùng gì của E1 | Ghi chú |
| :--- | :--- | :--- |
| E2 đến E13 | Đăng nhập, RBAC và phạm vi cơ sở (FR-AUTH-RBAC-001), nhật ký (FR-SYS-AUD-001 đến 004), lý do bắt buộc | Mọi API ghi số liệu cần audit |
| E2, E3, E9 | Tham số và duyệt tham số (FR-SYS-PRM-001/002) | Ví dụ `COST_CHE_DO_KIEM`, hạn mức AI |
| E2, E3, E7, E13 | Đề nghị thay đổi và lượt duyệt (`change_requests`, `approvals`), người duyệt khác người lập (BR-SEC-008) | E7 mở lại kỳ, E13 duyệt phương pháp |
| E5, E9 | Tài khoản dịch vụ cho agent (FR-AUTH-SVC-001), giao quyền (BR-SEC-009/010) | Hai tài khoản tách biệt |
| E6 | Mở rộng AUTH cho người đặt tổng và người ăn qua QR (FR-AUTH-EXT, QREG, QSES) | Thiết kế ở E6, dùng nền E1 |
| E6, E7, E11, E12 | Thông báo (FR-SYS-NTF-001 đến 003), tệp (FR-SYS-FILE-001), tác vụ nền (FR-SYS-JOB-001) | Kênh ngoài chờ Q-14 |

Vì mọi epic dùng E1, các câu E1-Q01 đến E1-Q06 nên được chốt trước khi freeze API của bất kỳ epic nào.
