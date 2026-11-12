---
id: DOC-E11-EPIC-SPEC-MD
title: E11 — Mua hàng và sản xuất
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# E11 — Mua hàng và sản xuất

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Mục tiêu và phạm vi

Nguồn: [PRD](../gia-phat/01-prd.md), [R11 và G-Next](../gia-phat/02-roadmap.md). Đúng 5 feature P1, 5 thiết kế nháp có điều kiện, 0 feature chỉ gate. Không mở E12/E13; FEAT-082/083 không có đặc tả.

| Feature | Module | Năng lực | Kết quả nháp |
| :--- | :--- | :--- | :--- |
| FEAT-074 | PUR / M5 | Nhu cầu, đơn mua, phạm vi lô | Nhu cầu gộp, đơn nháp, cổng duyệt chờ |
| FEAT-075 | PUR / M5 | Nhận hàng, ảnh, công nợ NCC | Phiếu nháp và truy nguồn; kỳ/số dư có điều kiện |
| FEAT-076 | COST / COST-07 | Đối chiếu theo ngày/cơ sở | So tiền và provenance; đo BO-02 chờ căn cứ |
| FEAT-077 | PLAN / M6 | Phân ca, QC, sổ mẫu | Nháp vận hành, chưa quyết cổng giao |
| FEAT-078 | MENU / MENU-08 | Thay món thiếu hàng | Cùng vai trò; kiểm lại và giữ cổng MENU |

## Người dùng và giá trị

PER-05 dinh dưỡng viên chọn món thay thế; PER-06 quản lý cơ sở/bếp trưởng ghi nhận và tổ chức bếp; PER-07 kế toán lập mua, nhận chứng từ, xem công nợ; PER-08 Giám đốc xem chênh lệch. Vai trò xem không tự là người duyệt.

## Thứ tự release có điều kiện

1. Review E11 và các quyết định liên quan; không đặt ngày/người triển khai/story point.
2. R3 và R6 phải xong theo R11; mở tài liệu không chứng minh G-Next đạt.
3. Sau nguồn/quyền được duyệt, chuẩn bị dữ liệu thật và chạy [nghiệm thu R11](test/r11-acceptance.md).

Đích R11: chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm theo ngày và cơ sở (BO-02); 100% bữa có mẫu lưu trên hệ thống. Công thức đo và mẫu hợp lệ còn chờ.

## Rủi ro và giới hạn

Thiếu phân bổ mua theo ngày, chính sách tồn/lô, quyền duyệt và mẫu lưu có thể đổi thiết kế. Mọi quyền là đề xuất theo vai trò × cơ sở; chưa tự cấp quyền hoặc chọn người duyệt. Các thao tác có nguồn/policy chưa chốt chỉ mô tả điểm chặn và phần độc lập, không triển khai tiếp producer. Không backend, migration, mô hình AI, commit hoặc xóa file.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02/R11 dùng ≤ 3 điểm phần trăm, không phải sai số tính toán. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chặn O-03, không thu dữ liệu sức khỏe.

[Phụ thuộc](review/dependencies.md) · [Câu hỏi](review/questions.md) · [SRS](srs/spec.md)
