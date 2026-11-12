---
id: DOC-E13-REVIEW-HANDOFF-MD
title: Bàn giao gói BA nháp E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Bàn giao gói BA nháp E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## Phạm vi và đường đọc

FEAT-088 P2 có thiết kế nháp có điều kiện, 0 feature E13 chỉ gate. [Epic](../epic-spec.md) → [SRS](../srs/spec.md) → [câu hỏi](questions.md) / [phụ thuộc](dependencies.md) → [UC](../usecases/index.md), [backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [RTM](../test/traceability.md), [API](../api/api-spec.md), [preview](../preview.html), [wireframe](../html-wireframe/profit-workbench.html), [báo cáo kiểm](../validation/report.md).

## Số liệu và giới hạn

12 FR / 12 UC / 12 story; 36 AC và 36 ca chức năng (16 BLOCKED, 20 NOT RUN); 13 ca hệ thống có overlap, 4 dòng R13 BLOCKED; 18 endpoint đề xuất, 5 port ranh giới; 8 màn, 5 state và 2 flow. 14 câu E13-Q01–14 trả lời trống. Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (74 + 1) / 78 = 75/78 ≈ 96,2 %**. FEAT-046/047/063 chỉ gate O-03 ghi riêng. Không phải BA được duyệt hoặc tiến độ phần mềm. Đây là epic cuối theo PRD; bước tiếp theo là review/chốt câu hỏi với stakeholder, không mở thêm epic hoặc coi release đã đạt.

Chưa có phương pháp duyệt: lợi nhuận khách BLOCKED, chỉ xem trực tiếp. Cầu nối tổng có phần chưa phân bổ chưa đủ R13. Bản khóa bất biến, sửa bằng bút toán có lý do và duyệt. Lương chỉ PER-07/PER-08 theo quyền; báo cáo khách nội bộ chỉ tổng hợp, không gửi lợi nhuận/biên lợi nhuận ra khách.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn; không giảm số phải trả nhà cung cấp, không tự khấu trừ số khách phải trả. Chưa quyết định khoản chiết khấu đi vào lợi nhuận thế nào. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-01 (cost ≤ 52 % doanh thu) và BO-02 (≤ 3 điểm phần trăm) là mục tiêu kinh doanh, không là dung sai đối chiếu E13. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03.

Giữ nguyên các câu đang chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp phần producer phụ thuộc các câu này.

## Prompt tiếp nối cho phiên sau

Bạn là BA tại D:\BA, chỉ làm tài liệu. Đọc docs/chi-phi-loi-nhuan/review/handoff.md, validation/report.md, review/questions.md và review/dependencies.md trước. E13 là epic cuối, chuyển sang review/chốt câu hỏi với stakeholder trên bằng chứng được cung cấp. Không tự trả lời hoặc đóng câu hỏi, không chọn phương pháp phân bổ, công thức margin, người phụ trách, ngày triển khai hoặc story point. Chỉ cập nhật phần có quyết định kèm nguồn và phân tích tác động; phần chưa có vẫn BLOCKED. Không backend/migration/gọi mô hình AI/commit/xóa file. Không chạy lại author-e13.cjs hoặc complete-e13.cjs vì có thể ghi đè chỉnh sửa review. Giữ baseline và toàn bộ nguồn E1–E12, PRD, roadmap, schema 65 bảng; không sửa ngoài gói nếu chưa có yêu cầu riêng. Chạy bốn checker E13, xem ảnh desktop/mobile, cập nhật manifest/report; không dùng kiểm mock thay ca sản phẩm. Mọi thay đổi OVERVIEW/dashboard chỉ append nếu được yêu cầu.
