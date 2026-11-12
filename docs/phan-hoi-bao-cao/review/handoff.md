---
id: DOC-E12-REVIEW-HANDOFF-MD
title: Bàn giao gói BA nháp E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Bàn giao gói BA nháp E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; không đóng câu hỏi nguồn |

## Phạm vi và cách đọc

Chỉ FEAT-079–087, 7 P1 và 2 P2. 9/9 feature có thiết kế nháp có điều kiện; 0 feature E12 chỉ gate. [Epic](../epic-spec.md) → [SRS](../srs/spec.md) → [câu hỏi](questions.md)/[phụ thuộc](dependencies.md) → [UC](../usecases/index.md), [story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [API](../api/api-spec.md), [RTM](../test/traceability.md), [preview](../preview.html), [wireframe](../html-wireframe/feedback-report-workbench.html), [báo cáo kiểm](../validation/report.md).

## Số liệu và giới hạn

20 FR / 20 UC / 20 story; 60 AC và 60 ca chức năng (23 BLOCKED, 37 NOT RUN). 12 ca hệ thống và 8 ca lỗi có overlap (5 BLOCKED, 15 NOT RUN); 3 dòng R12 BLOCKED. Actual/Evidence trống. 20 endpoint đề xuất, 7 port chỉ đọc, 12 màn, 5 state và 2 flow. 18 câu E12-Q01–18 để trống trả lời.

Thiết kế tài liệu nháp **(65 + 9) / 78 = 74/78 ≈ 94,9 %**. Ba feature FEAT-046/047/063 chỉ gate O-03 không cộng tử số. Không phải BA được duyệt hoặc tiến độ phần mềm. E13/FEAT-088 chưa mở. R6/R7/R10/R11/G-Next chưa có bằng chứng đạt.

Tỷ lệ món chỉ từ lựa chọn thật E6, mẫu số chưa chọn. Cost % dùng định nghĩa E3, tổng theo khách chờ Q08. Bốn feature AI chỉ công cụ đọc theo giao quyền ở tool/DB và nháp chờ người thật, không tự ghi nghiệp vụ. FEAT-084 chỉ đọc E10. FEAT-086 cấp nhóm, không ngưỡng tự đặt. FEAT-087 chỉ bữa đã ăn và giá trị suất, tự nguyện/có đồng ý/xóa được; không sức khỏe hoặc gợi ý cá nhân, không dùng FEAT-046/047.

Cost gồm VAT phải trả NCC; cờ hóa đơn riêng không là VAT 0 %; CK %/tiền suất riêng theo đơn, không giảm phải trả NCC hoặc tự trừ tiền khách. NFR-COST-002 ≤ 1 đ và ≤ 0,01 điểm phần trăm; BO-02 ≤ 3 điểm phần trăm là mục tiêu R11. O-02/O-03 và mọi câu nguồn giữ nguyên.

## Giới hạn kiểm bảo toàn cần bàn giao

Ba checker cấu trúc/render/UI đạt; hash-check còn 4 sai lệch so baseline ở OVERVIEW, dashboard, gia-phat/review/next-session-prompt.md và progress-assessment.md. Sai lệch được quan sát trước append E12; phiên chưa có lệnh ghi các file này khi phát hiện, chưa biết tác nhân. Không khôi phục hoặc ghi lại baseline. Hai tổng quan chỉ được append sau khi chụp hash bản hiện tại, prefix đó giữ nguyên. Xem [báo cáo](../validation/report.md) và [bằng chứng trước append](../validation/pre-append-drift.json). Không tuyên bố đã đạt điều kiện 0 file cũ thay đổi.

## Prompt tiếp nối cho phiên sau

Bạn là BA tại D:\BA. Chỉ làm tài liệu E12 trong docs/phan-hoi-bao-cao/. Đọc review/handoff.md, validation/report.md, review/questions.md và review/dependencies.md trước. Không mở E13. Chỉ bổ sung phần có quyết định được cung cấp kèm nguồn; câu chưa trả lời giữ trống, nhánh phụ thuộc BLOCKED; không hỏi lại hoặc đặc tả tiếp producer đang chờ. Không backend/migration/gọi mô hình AI/system prompt/chọn provider hoặc model/commit/xóa file. Không chạy lại author-e12.cjs, complete-e12.cjs, refine-e12.cjs hoặc append-e12-status.cjs để tránh ghi lại chỉnh sửa review; sửa trực tiếp artifact cần đổi. Giữ baseline E12 và toàn bộ nguồn E1–E11, PRD, roadmap, schema 65 bảng; chỉ append OVERVIEW/dashboard nếu được yêu cầu. Giữ E3 Cost/VAT/CK, NFR-COST-002 và O-02/O-03. Đối chiếu 4 sai lệch trong pre-append-drift.json riêng; không tự khôi phục ngoài phạm vi hoặc ghi đè baseline để bỏ lỗi. Chạy check-e12.cjs, render-e12.cjs, check-ui-e12.cjs, hash-check-e12.cjs sau lần sửa cuối, xem ảnh desktop/mobile rồi cập nhật report và files-created.json. Không dùng kiểm mock thay ca sản phẩm.
