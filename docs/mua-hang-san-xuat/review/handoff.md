---
id: DOC-E11-REVIEW-HANDOFF-MD
title: Bàn giao gói BA nháp E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Bàn giao gói BA nháp E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Phạm vi và cách đọc

Đúng FEAT-074–078, đều P1: 5/5 feature có thiết kế nháp có điều kiện; 0 feature E11 chỉ gate. Đọc [epic](../epic-spec.md), [SRS](../srs/spec.md), [câu hỏi](questions.md), [phụ thuộc](dependencies.md), rồi [UC](../usecases/index.md), [backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [wireframe](../html-wireframe/purchase-workbench.html), [RTM](../test/traceability.md), [R11](../test/r11-acceptance.md) và [báo cáo](../validation/report.md).

## Số liệu và giới hạn

15 FR / 15 UC / 15 story; 45 AC và 45 ca chức năng (13 BLOCKED, 32 NOT RUN). 10 ca hệ thống có overlap (5 BLOCKED, 5 NOT RUN); 15 HTTP endpoint + 4 port ranh giới; 9 màn; 5 state + 2 flow. 15 câu E11-Q01–15 để trống trả lời.

Độ phủ thiết kế tài liệu nháp **(60 + 5) / 78 = 65/78 ≈ 83,3 %**. Ba feature chỉ gate FEAT-046/047/063 ghi riêng, không cộng vào tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. Schema 65 bảng giữ nguyên.

E2 cấp định lượng/vai trò/dị ứng/rule và cổng duyệt; E3 cấp giá VAT/dự toán; E6 cấp kế hoạch nhưng CG06 còn chờ; E7 giữ giao nhận/doanh thu. Nhu cầu chưa có trừ tồn; lô chỉ đông lạnh/khô; kỳ công nợ, hạn mẫu và chính sách duyệt chưa chọn. R11/G-Next chưa nghiệm thu.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02/R11 dùng ≤ 3 điểm phần trăm, không phải sai số tính toán. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chặn O-03, không thu dữ liệu sức khỏe.

## Prompt tiếp nối cho phiên sau

Bạn là BA tại D:\BA. Chỉ làm tài liệu E11 trong docs/mua-hang-san-xuat/. Đọc handoff, validation/report.md, questions.md và dependencies.md trước. Chỉ bổ sung phần đã có câu trả lời được cung cấp với nguồn rõ; phần còn thiếu giữ BLOCKED, cột Trả lời trống. Không mở E12/E13, không đặc tả FEAT-082/083, không backend/migration/AI/commit/xóa file. Giữ baseline E11 và mọi kết quả lịch sử E6–E10. Giữ nguyên Cost/VAT/CK/NFR-COST-002 và mọi gate nguồn. Không sửa ngoài gói trừ append OVERVIEW/dashboard nếu được yêu cầu. Sau sửa chạy check-e11.cjs, render-e11.cjs, check-ui-e11.cjs, hash-check-e11.cjs; xem ảnh desktop/mobile, cập nhật manifest và báo cáo đúng bằng chứng. Không dùng mock làm ca sản phẩm đạt.
