---
id: DOC-NEN-TANG-REVIEW-HANDOFF
title: Bàn giao BA nháp E1
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [handoff, e1]
author: BA
last_updated: 2026-11-16
---
# Bàn giao BA nháp E1: Nền tảng

Draft · 16/11/2026 · Thiết kế BA để review, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách bàn giao riêng cho E1 theo khuôn chung các epic; trước đây gộp trong bàn giao chung E1 đến E5 |

## Gói này gồm gì

E1 thuộc đợt Now, release R1, phạm vi FEAT-001 đến FEAT-005. Bàn giao chung trước đây: [bàn giao bổ sung E1 đến E5](../../gia-phat/review/ba-completion-handoff.md). Tài liệu thêm: [Kiến trúc hệ thống](../srs/architecture.md), [kiến trúc AI agent](../srs/agent-architecture.md), [CR-CORE-2026-001](../cr/CR-CORE-2026-001.md) (backend Rust/Axum).

## Đọc theo thứ tự nào

1. [Epic](../epic-spec.md), [câu hỏi](questions.md), [phụ thuộc](dependencies.md).
2. [SRS](../srs/spec.md) phần NFR toàn hệ thống, phân quyền, nhật ký; [ERD](../srs/erd.md), [DBML 65 bảng](../srs/schema.dbml).
3. [UC](../usecases/index.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [màn hình](../ui/screens.md).
4. [Story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [ca hệ thống](../test/system-cases.md), [RTM](../test/traceability.md), [nghiệm thu R1](../test/r1-acceptance.md).
5. [Preview](../preview.html) để xem toàn bộ kèm sơ đồ; [báo cáo kiểm](../validation/report.md) cho kết quả kiểm tài liệu.

## Số liệu chính (đếm tự động ngày 16/11/2026)

| Mục | Số |
| :--- | ---: |
| FR (mã duy nhất trong SRS) | 26 |
| Use case | 26 |
| Story | 26 |
| AC | 78 |
| Test case (mã duy nhất) | 140 |
| Endpoint trong catalog | 25 |
| Sơ đồ đã render | 16 |
| Màn hình | 6 màn HTML |

Đây là số đếm tài liệu, không phải chức năng đã chạy. Số backend, migration, UAT đã thực hiện đều là 0; schema giữ 65 bảng.

## Những điểm người review cần quyết định

- N-01 đến N-04: cách đăng nhập, người giữ quyền quản trị, thời gian lưu nhật ký, bắt buộc 2 bước
- E1-Q01 đến E1-Q06: envelope lỗi, phân trang, idempotency, MFA, thông báo, quyền đọc audit, đo phản hồi đầu
- O-04 hạ tầng, O-06 người duyệt

Danh sách đầy đủ ở [câu hỏi](questions.md) và [sổ quyết định](../../gia-phat/review/decision-pack/decision-register.md). Không câu nào được tự chốt trong gói này.

## Giới hạn

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không phải VAT 0%; chiết khấu theo đơn là khoản riêng. CK-Q01 đến CK-Q10, DATA-COST-Q01 đến Q06, NFR-COST-002 giữ nguyên. FEAT-046, FEAT-047, FEAT-063 vẫn chỉ gate O-03.

## Việc tiếp theo

Chốt các điểm ở mục trên với người có thẩm quyền, có nguồn và ngày; sau đó sửa tài liệu bằng quy trình phân tích tác động (CR). Chuẩn bị dữ liệu thật cho [ca nghiệm thu R1](../test/r1-acceptance.md).
