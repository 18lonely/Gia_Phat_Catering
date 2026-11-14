---
id: DOC-COST-REVIEW-DEPENDENCIES
title: Phụ thuộc E3 Cost
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [dependencies, e3]
author: BA
last_updated: 2026-11-16
---
# Phụ thuộc E3: Cost

Draft · 16/11/2026 · Gom từ [epic E3 mục 2.5](../epic-spec.md), roadmap và các epic dùng E3; không thêm quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic: E3 chờ gì, epic nào dùng E3 |

## 1. E3 đang chờ gì

| Cần có | Loại | Nguồn | Chặn |
| :--- | :--- | :--- | :--- |
| R2: nguyên liệu, công thức, thực đơn, bộ kiểm quy tắc, chỗ móc gửi duyệt | Kỹ thuật | [E2](../../thuc-don-dinh-luong/srs/spec.md) | Toàn epic |
| DL-02: kế toán xác nhận VAT và thành phần cost (O-01, đã xác nhận một phần) | Nghiệp vụ | [Quy tắc kế toán](../accounting/business-rules.md) | Cost % ngày |
| DL-06: bảng giá nhập hiện hành theo nhà cung cấp | Dữ liệu | [Roadmap](../../gia-phat/02-roadmap.md) | Nghiệm thu giá nhập |
| DL-01: con số của 8 quy tắc cost | Nghiệp vụ | [Quy tắc thực đơn](../../gia-phat/brainstorms/quy-tac-thuc-don.md) | Kiểm cost thực đơn |
| Bảng tính cost tay 10 món, 10 ngày (DATA-COST-Q01 đến Q06) | Dữ liệu | [Phiếu dữ liệu kế toán](accountant-input.md) | Nghiệm thu NFR-COST-002, R3 |
| E3-Q, FLOW-COST-Q, QA-COST-Q, CK-Q | Quyết định | [Câu hỏi E3](questions.md) | Theo từng FR, 46 ca BLOCKED |

## 2. Epic nào dùng E3

| Epic dùng | Dùng gì của E3 | Ghi chú |
| :--- | :--- | :--- |
| E2 Thực đơn | Kiểm cost ở cổng gửi duyệt (CHAN, CANH_BAO), cost % ngày theo cơ sở | Qua hook, không đổi cổng MENU |
| E5 Agent Nội bộ | Kiểm cost phương án, đọc cost theo quyền người dùng | Không trả VALID khi vượt cost (AIO-Q02) |
| E9 Agent Dinh dưỡng viên | Kiểm ngân sách cho agent khách (FR-COST-RUL-003) | Mâu thuẫn với E9 ghi ở GAP-E9-10 |
| E6, E7 | Giá chụp theo order, VAT, chiết khấu riêng | Chiết khấu không giảm phải trả nhà cung cấp |
| E10 CRM | Cost nội bộ cho báo giá (PORT-CRM-COST) | Không ra bản cho khách |
| E11 Mua hàng | Danh mục NCC, PriceInput, dự toán | Đối chiếu dự toán và thực mua |
| E12, E13 | Cost % ngày, cost nguyên liệu | Không định nghĩa lại cost |

Xác nhận kế toán giữ nguyên: cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không phải VAT 0%; chiết khấu % hoặc tiền mỗi suất là khoản riêng theo đơn.
