---
id: DOC-E6-REVIEW-HANDOFF
title: Bàn giao E6 để review
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Bàn giao E6 để review

11/11/2026 · **Draft đã tự kiểm cấu trúc/hiển thị; chưa ký baseline nghiệp vụ, chưa backend/migration/UAT.**

## Điểm vào review

[Preview](../preview.html) · [Wireframe](../html-wireframe/order-workbench.html) · [Phạm vi](scope-assessment.md) · [RTM](../test/traceability.md) · [Báo cáo kiểm tra](../validation/report.md).

Giữ FEAT-030–048:14P0/5P1; 17 capability có thiết kế có điều kiện và2 capability chỉ gate O-03. Có19UC,57AC,26HTTP endpoint đề xuất,2port,13màn và8sơ đồ. Không coi số lượng này là19 tính năng được duyệt. Bộ test gồm10ca gốc giữ nguyên,57ca theoAC và12ca hệ thống; có trùng mục tiêu,0test backend đã chạy.

## File chính và thay đổi

| Nhóm | File / nội dung |
| :--- | :--- |
| Phạm vi/SRS | [epic](../epic-spec.md), [SRS](../srs/spec.md), [quy tắc vận hành](../srs/operational-rules.md), [scope assessment](scope-assessment.md) |
| UC/flow/state | [19 UC và sơ đồ](../srs/usecase-diagram.md), [user flow](../ui/user-flow.md), [sequence](../srs/flows.md), [state](../srs/states.md) |
| Data/API | [data dictionary](../srs/data-dictionary.md), [ERD gốc](../srs/erd.md), [API contract](../api/api-spec.md), [catalog](../api/endpoint-catalog.json) |
| UI/backlog | [13 màn](../html-wireframe/order-workbench.html), [screen catalog](../ui/screen-catalog.md), [backlog](../userstories/backlog.md), [57AC](../userstories/acceptance-criteria.md) |
| QA | [57ca mới](../test/review-test-cases.md), [12ca hệ thống](../test/system-test-cases.md), [10ca gốc](../test/test-cases.md), [checklist](../test/checklist.md), [RTM](../test/traceability.md) |
| Câu hỏi/phụ thuộc | [ORD-Q01–15](questions.md), [dependencies](dependencies.md), [gap](../gap-analysis.md) |
| Đồng bộ | OVERVIEW, project-dashboard, PRD, roadmap, kế hoạch, sổ phạm vi; SRS E1–E5, ERD nền và handoff/report gói trước có liên kết tiếp nối |

[Danh sách file thêm/sửa](../validation/change-manifest.md) được tính từ hash trước phiên. Workspace không có Git; không tuyên bố commit hoặc diff Git. Script build/extend/finalize là công cụ soạn một lần, **không chạy lại mù** vì có phần append; sửa Markdown nguồn rồi chỉ chạy checker/renderer.

## Điểm chặn

- ORD-Q01–10 **không được đóng**. Bổ sung ORD-Q11–15: scope khách/điểm/guest audit; thu hồi MENU/deadline; hủy/chuyển điểm/zero order; bếp nhận version; consent khi mở O-03.
- Tuần atomic/partial, C bổ sung/thay thế, T<S+C, default/lock thiếu đầu vào, sửa sau khóa và phân rã món phụ còn policy chờ. Các phương án ghi trong tài liệu/wireframe là đề xuất synthetic.
- FEAT-046/047 vẫn BLOCKED O-03: không write API/health form/thuật toán. FR-MENU-RCP-007 vẫn BLOCKED O-02.
- Schema giữ65bảng, DBML không đổi. Delta revision/QR/session/outbox/mode chưa merge/duyệt/migration; users loại SERVICE có sẵn, guest audit và scope nhiều điểm còn thiếu thiết kế được duyệt.
- NFR/pilot/G-Now chưa evidence. Chưa dữ liệu kế toán thật10món/10ngày; giữ DATA-COST-Q01–06 và CK-Q01–10.

Cost gồmVAT phải trảNCC; không hóa đơn không nghĩaVAT0%; chiết khấu% hoặc tiền/suất là khoản riêng theođơn, không tự giảm tiền khách phải trả. NFR-COST-002: cost món≤1đ, cost% ngày≤0,01 điểm phần trăm. Không thay quy tắc này khi duyệt E6.

## Công việc phiên tiếp theo

1. Review quyết định theo thứ tự identity/scope → S/C/T và deadline/default → quota/menu thay đổi → change approval/plan → tuần/mode/nhắc. Ghi người/ngày/nguồn/ví dụ vào từng ORD-Q trước đóng.
2. Tech lead chốt contract/envelope, binding tài khoản khách, idempotency/audit/outbox và schema delta so với65bảng; BA cập nhật đầy đủ chuỗi RTM theo quyết định.
3. QA review expected synthetic, chuẩn bị profile1000CCU và dữ liệu pilot2khách/2tuần; chuyển BLOCKED→NOT RUN khi đủ đầu vào, không chuyển PASS vì tài liệu đã có.
4. Chỉ sau review E6 mới xem xét mở rộng E7–E13; chưa triển khai backend trong phạm vi công việc này.

## Review quyết định tiếp nối ngày 11/11/2026

[DR-01–04](decision-review.md) · [Findings](decision-findings.md) · [Báo cáo](../validation/decision-review-report.md). E6-EVID-001 xác nhận có danh sách/người quản lý; ORD-Q01 chỉ xác nhận một phần đầu vào, cơ chế chưa chốt. Tiếp theo lấy quyết định về credential/scope, C→S/S vượt T, ngoại lệ sau hạn và completeness/ack/start-production; chưa freeze schema/API hoặc mở E7–E13.

## Cập nhật phản hồi E6-EVID-002

Ngày11/11/2026, người dùng yêu cầu giữ mở cả phạm vi người đặt tổng (ORD-Q11), chuyển chọn hộ→tự chọn và xử lý S+C vượt T (ORD-Q06). Đã ghi vào sổ câu hỏi và bảng DR. Không áp phương án mặc định; test phụ thuộc vẫn BLOCKED, schema/API chưa freeze. Không có thay đổi backend hoặc quy tắc nghiệp vụ được duyệt.
