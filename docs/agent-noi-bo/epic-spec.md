---
id: DOC-AGENT-NOI-BO-EPIC-SPEC
title: Đặc tả epic (E5 / R5)
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Đặc tả epic (E5 / R5)

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Mục tiêu và phạm vi

FEAT-021–023, nguồn [PRD](../gia-phat/01-prd.md) và [roadmap](../gia-phat/02-roadmap.md). P0 dựng tuần, chỉnh bằng lời, nhật ký. Chỉ bản nháp; MENU/COST tính và kiểm. Agent khách/CRM/mua hàng/hỏi đáp Later ngoài phạm vi.

## Capability / release

| Bước | Kết quả | Gate |
| :--- | :--- | :--- |
| Đặc tả | SRS,API,dữ liệu,UC,UI,AC/test và câu hỏi review | Draft hiện tại, không phải baseline đã ký |
| Chuẩn bị triển khai | Chốt hợp đồng và các điểm chặn; đội ước lượng backlog | R2/R3, DL-01, O-04, AIO-Q01–06. R4 không tự thêm thành cổng generation, nhưng thuộc G-Now. |
| Kiểm thử / nghiệm thu | 20 yêu cầu khả thi cho ra100% nháp không vi phạm cứng/không vượt cost,0 món ngoài ACTIVE,≤60giây mỗi tuần;100% run có log; giảm≥50% thời gian so baseline trước MVP. | Backend,môi trường,dữ liệu thật và người duyệt; chưa có |

Ngày phát hành/Story Point chưa đặt (O-04). Không bổ sung tính năng mới để lấp mẫu tài liệu. [SRS](srs/spec.md), [backlog](userstories/backlog.md), [gap](gap-analysis.md), [preview](preview.html).
