---
id: DOC-DINH-DUONG-REVIEW-HANDOFF
title: Bàn giao BA nháp E4
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [handoff, e4]
author: BA
last_updated: 2026-11-16
---
# Bàn giao BA nháp E4: Dinh dưỡng

Draft · 16/11/2026 · Thiết kế BA để review, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách bàn giao riêng cho E4 theo khuôn chung các epic; trước đây gộp trong bàn giao chung E1 đến E5 |

## Gói này gồm gì

E4 thuộc đợt Now, release R4, phạm vi FEAT-019, FEAT-020. Bàn giao chung trước đây: [bàn giao bổ sung E1 đến E5](../../gia-phat/review/ba-completion-handoff.md). Tài liệu thêm: [Gói review E4 và E5 ngày 11/11/2026](../../gia-phat/review/mvp-e4-e5-handoff.md).

## Đọc theo thứ tự nào

1. [Epic](../epic-spec.md), [câu hỏi](questions.md), [phụ thuộc](dependencies.md).
2. [SRS](../srs/spec.md), [ERD và từ điển](../srs/erd.md).
3. [UC](../usecases/index.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [wireframe ASCII](../ui/wireframe-ascii.md).
4. [Story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [ca hệ thống](../test/system-cases.md), [RTM](../test/traceability.md), [nghiệm thu R4](../test/r4-acceptance.md).
5. [Preview](../preview.html) để xem toàn bộ kèm sơ đồ; [báo cáo kiểm](../validation/report.md) cho kết quả kiểm tài liệu.

## Số liệu chính (đếm tự động ngày 16/11/2026)

| Mục | Số |
| :--- | ---: |
| FR (mã duy nhất trong SRS) | 5 |
| Use case | 5 |
| Story | 5 |
| AC | 15 |
| Test case (mã duy nhất) | 28 |
| Endpoint trong catalog | 7 |
| Sơ đồ đã render | 5 |
| Màn hình | 3 màn ASCII, 1 trang wireframe HTML |

Đây là số đếm tài liệu, không phải chức năng đã chạy. Số backend, migration, UAT đã thực hiện đều là 0; schema giữ 65 bảng.

## Những điểm người review cần quyết định

- NUTR-Q01 đến Q04: ấn bản bảng thành phần, ý nghĩa định lượng sống, suất mẫu, làm tròn và dung sai
- DATA-NUTR-Q01: mapping 30 món và 5 suất tính tay
- BRD DP-03: nguồn dữ liệu dinh dưỡng

Danh sách đầy đủ ở [câu hỏi](questions.md) và [sổ quyết định](../../gia-phat/review/decision-pack/decision-register.md). Không câu nào được tự chốt trong gói này.

## Giới hạn

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không phải VAT 0%; chiết khấu theo đơn là khoản riêng. CK-Q01 đến CK-Q10, DATA-COST-Q01 đến Q06, NFR-COST-002 giữ nguyên. FEAT-046, FEAT-047, FEAT-063 vẫn chỉ gate O-03.

## Việc tiếp theo

Chốt các điểm ở mục trên với người có thẩm quyền, có nguồn và ngày; sau đó sửa tài liệu bằng quy trình phân tích tác động (CR). Chuẩn bị dữ liệu thật cho [ca nghiệm thu R4](../test/r4-acceptance.md).
