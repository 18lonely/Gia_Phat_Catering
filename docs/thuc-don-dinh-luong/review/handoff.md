---
id: DOC-THUC-DON-REVIEW-HANDOFF
title: Bàn giao BA nháp E2
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [handoff, e2]
author: BA
last_updated: 2026-11-16
---
# Bàn giao BA nháp E2: Thực đơn và định lượng

Draft · 16/11/2026 · Thiết kế BA để review, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách bàn giao riêng cho E2 theo khuôn chung các epic; trước đây gộp trong bàn giao chung E1 đến E5 |

## Gói này gồm gì

E2 thuộc đợt Now, release R2, phạm vi FEAT-006 đến FEAT-013. Bàn giao chung trước đây: [bàn giao bổ sung E1 đến E5](../../gia-phat/review/ba-completion-handoff.md). Tài liệu thêm: [Ca quy tắc](../test/rule-test-cases.md), [truy vết API](../api/api-traceability.md).

## Đọc theo thứ tự nào

1. [Epic](../epic-spec.md), [câu hỏi](questions.md), [phụ thuộc](dependencies.md).
2. [SRS](../srs/spec.md), [quy tắc thực đơn](../../gia-phat/brainstorms/quy-tac-thuc-don.md).
3. [UC](../usecases/index.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [màn hình](../ui/screens.md).
4. [Story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [ca quy tắc](../test/rule-test-cases.md), [ca hệ thống](../test/system-cases.md), [RTM](../test/traceability.md), [nghiệm thu R2](../test/r2-acceptance.md).
5. [Preview](../preview.html) để xem toàn bộ kèm sơ đồ; [báo cáo kiểm](../validation/report.md) cho kết quả kiểm tài liệu.

## Số liệu chính (đếm tự động ngày 16/11/2026)

| Mục | Số |
| :--- | ---: |
| FR (mã duy nhất trong SRS) | 55 |
| Use case | 13 |
| Story | 53 |
| AC | 239 |
| Test case (mã duy nhất) | 335 |
| Endpoint trong catalog | 60 |
| Sơ đồ đã render | 11 |
| Màn hình | 3 trang wireframe HTML, 15 màn trong user flow |

Đây là số đếm tài liệu, không phải chức năng đã chạy. Số backend, migration, UAT đã thực hiện đều là 0; schema giữ 65 bảng.

## Những điểm người review cần quyết định

- DL-01: 43 quy tắc thực đơn chờ duyệt; 86 ca quy tắc BLOCKED
- O-02: một hay nhiều cỡ định lượng, chặn FR-MENU-RCP-007
- E2-Q1 đến E2-Q11, MENU-API-Q01 đến Q03 (ba câu API chưa có trong sổ quyết định)

Danh sách đầy đủ ở [câu hỏi](questions.md) và [sổ quyết định](../../gia-phat/review/decision-pack/decision-register.md). Không câu nào được tự chốt trong gói này.

## Giới hạn

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không phải VAT 0%; chiết khấu theo đơn là khoản riêng. CK-Q01 đến CK-Q10, DATA-COST-Q01 đến Q06, NFR-COST-002 giữ nguyên. FEAT-046, FEAT-047, FEAT-063 vẫn chỉ gate O-03.

## Việc tiếp theo

Chốt các điểm ở mục trên với người có thẩm quyền, có nguồn và ngày; sau đó sửa tài liệu bằng quy trình phân tích tác động (CR). Chuẩn bị dữ liệu thật cho [ca nghiệm thu R2](../test/r2-acceptance.md).
