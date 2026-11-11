---
id: DOC-NEN-TANG-EPIC-SPEC
title: Đặc tả epic — E1 / R1
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Đặc tả epic — E1 / R1

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Mục tiêu và phạm vi

FEAT-001–005, nguồn [PRD](../gia-phat/01-prd.md) và [roadmap](../gia-phat/02-roadmap.md). Đăng nhập và quyền; tài khoản; audit; tham số; thông báo nội bộ. Tệp, job, health là nền kỹ thuật trong SRS. P1 MFA/ủy quyền/kênh ngoài giữ gated N-04/O-06/Q-14.

## Capability / release

| Bước | Kết quả | Gate |
| :--- | :--- | :--- |
| Đặc tả | SRS,API,dữ liệu,UC,UI,AC/test và câu hỏi review | Draft hiện tại, không phải baseline đã ký |
| Chuẩn bị triển khai | Chốt hợp đồng và các điểm chặn; đội ước lượng backlog | Có người quản trị, nguồn định danh N-01, người duyệt O-06 và hạ tầng O-04. |
| Kiểm thử / nghiệm thu | 5 nhóm vai trò nghiệp vụ theo roadmap đăng nhập đúng scope, không đọc chéo cơ sở;100% thay đổi có audit; đo tải theo NFR nền. Vai trò hệ thống/nhánh kế toán chi tiết theo SRS, không suy số nhóm= sốrole enum. | Backend,môi trường,dữ liệu thật và người duyệt; chưa có |

Ngày phát hành/Story Point chưa đặt (O-04). Không bổ sung tính năng mới để lấp mẫu tài liệu. [SRS](srs/spec.md), [backlog](userstories/backlog.md), [gap](gap-analysis.md), [preview](preview.html).
