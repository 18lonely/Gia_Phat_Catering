---
id: DOC-AGENT-NOI-BO-REVIEW-HANDOFF
title: Bàn giao BA nháp E5
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [handoff, e5]
author: BA
last_updated: 2026-11-16
---
# Bàn giao BA nháp E5: Agent Nội bộ

Draft · 16/11/2026 · Thiết kế BA để review, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách bàn giao riêng cho E5 theo khuôn chung các epic; trước đây gộp trong bàn giao chung E1 đến E5 |

## Gói này gồm gì

E5 thuộc đợt Now, release R5 (MVP v1.0.0), phạm vi FEAT-021 đến FEAT-023. Bàn giao chung trước đây: [bàn giao bổ sung E1 đến E5](../../gia-phat/review/ba-completion-handoff.md). Tài liệu thêm: [Gói review E4 và E5 ngày 11/11/2026](../../gia-phat/review/mvp-e4-e5-handoff.md), [kiến trúc AI agent](../../nen-tang/srs/agent-architecture.md).

## Đọc theo thứ tự nào

1. [Epic](../epic-spec.md), [câu hỏi](questions.md), [phụ thuộc](dependencies.md).
2. [SRS](../srs/spec.md), [ERD và từ điển](../srs/erd.md), [kiến trúc AI agent](../../nen-tang/srs/agent-architecture.md).
3. [UC](../usecases/index.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [wireframe ASCII](../ui/wireframe-ascii.md).
4. [Story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [ca hệ thống](../test/system-cases.md), [RTM](../test/traceability.md), [nghiệm thu R5](../test/r5-acceptance.md).
5. [Preview](../preview.html) để xem toàn bộ kèm sơ đồ; [báo cáo kiểm](../validation/report.md) cho kết quả kiểm tài liệu.

## Số liệu chính (đếm tự động ngày 16/11/2026)

| Mục | Số |
| :--- | ---: |
| FR (mã duy nhất trong SRS) | 6 |
| Use case | 6 |
| Story | 6 |
| AC | 18 |
| Test case (mã duy nhất) | 32 |
| Endpoint trong catalog | 6 |
| Sơ đồ đã render | 5 |
| Màn hình | 3 màn ASCII, 1 trang wireframe HTML |

Đây là số đếm tài liệu, không phải chức năng đã chạy. Số backend, migration, UAT đã thực hiện đều là 0; schema giữ 65 bảng.

## Những điểm người review cần quyết định

- AIO-Q01 đến Q07: nhà cung cấp mô hình, hành vi khi CANH_BAO, bộ 20 yêu cầu thử, quyền đọc log, kiêng diễn đạt tự do, contract adapter, đo phản hồi đầu
- O-04: nhà cung cấp mô hình và hạ tầng
- Baseline thời gian dựng thực đơn trước MVP (BO-03)

Danh sách đầy đủ ở [câu hỏi](questions.md) và [sổ quyết định](../../gia-phat/review/decision-pack/decision-register.md). Không câu nào được tự chốt trong gói này.

## Giới hạn

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không phải VAT 0%; chiết khấu theo đơn là khoản riêng. CK-Q01 đến CK-Q10, DATA-COST-Q01 đến Q06, NFR-COST-002 giữ nguyên. FEAT-046, FEAT-047, FEAT-063 vẫn chỉ gate O-03.

## Việc tiếp theo

Chốt các điểm ở mục trên với người có thẩm quyền, có nguồn và ngày; sau đó sửa tài liệu bằng quy trình phân tích tác động (CR). Chuẩn bị dữ liệu thật cho [ca nghiệm thu R5](../test/r5-acceptance.md).
