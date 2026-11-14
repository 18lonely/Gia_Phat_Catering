---
id: DOC-E12-SRS-USECASE-DIAGRAM
title: Sơ đồ use case E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [usecase-diagram, phan-hoi, bao-cao, e12]
depends_on: [DOC-E12-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ use case E12: Phản hồi và báo cáo

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa triển khai, không gọi mô hình AI.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: sơ đồ actor và ma trận FR, UC, màn hình, API cho 20 UC hiện có. Không thêm FR hoặc UC |

File này chỉ vẽ lại phạm vi trong [SRS E12](spec.md), [danh mục UC](../usecases/index.md) và [màn hình](../ui/screens.md). Bốn feature AI (FEAT-082 đến FEAT-085) chạy qua Agent Nội bộ với quyền của người dùng; đầu ra chỉ là đề xuất nháp chờ người thật.

## 1. Tác nhân

| Tác nhân | Persona | Ghi chú |
| :--- | :--- | :--- |
| Người đặt tổng | PER-02 | Đánh giá, khiếu nại |
| Người ăn có tài khoản | PER-03 | Đánh giá, khiếu nại, nhật ký bữa đã ăn (P2) |
| Người ăn qua QR | PER-04 | Đánh giá, khiếu nại; cách xác minh chờ E12-Q02 |
| Dinh dưỡng viên kiêm CSKH | PER-05 | Phân tích lựa chọn, đề xuất cải tiến, dashboard, mục tiêu nhóm, hỗ trợ CRM |
| Bếp trưởng / Quản lý cơ sở | PER-06 | Dashboard theo vai trò |
| Kế toán | PER-07 | Dashboard, cost %, diễn giải dự toán, nhu cầu, giá lệch, hỏi đáp số liệu |
| Giám đốc | PER-08 | Dashboard, cost %, rà soát giá, hỗ trợ CRM, hỏi đáp số liệu |
| Agent Nội bộ (AIO) | Hệ thống | Công cụ chỉ đọc theo giao quyền người dùng và `svc-agent-noi-bo` |
| Nguồn E2, E3, E4, E6, E10, E11 | Hệ thống | Lựa chọn thật, cost %, dinh dưỡng, CRM, nhu cầu mua |

## 2. Sơ đồ

```mermaid
flowchart LR
  NA["Người ăn PER-03/04"]
  DT["Người đặt tổng PER-02"]
  DD["DDV kiêm CSKH PER-05"]
  BT["Bếp / QL cơ sở PER-06"]
  KT["Kế toán PER-07"]
  GD["Giám đốc PER-08"]
  AIO[("Agent Nội bộ")]
  SRC[("E2 E3 E4 E6 E10 E11")]

  subgraph FB["Phản hồi (FB)"]
    U1(["UC-FBR-001 Gửi đánh giá"])
    U2(["UC-FBR-002 Khiếu nại"])
    U3(["UC-FBR-003 Tỷ lệ chọn theo món"])
    U4(["UC-FBR-004 Đề xuất cải tiến thực đơn"])
  end
  subgraph RPT["Báo cáo (RPT)"]
    U5(["UC-FBR-005 Dashboard 4 vai trò"])
    U6(["UC-FBR-006 Cost % ngày, theo khách"])
  end
  subgraph AI["Trợ lý nội bộ (AIO)"]
    U7(["UC-FBR-007 Rà soát khi giá đổi"])
    U8(["UC-FBR-008 Kiểm lại đề xuất"])
    U9(["UC-FBR-009 Diễn giải dự toán"])
    U10(["UC-FBR-010 Diễn giải nhu cầu"])
    U11(["UC-FBR-011 Giải thích giá lệch"])
    U12(["UC-FBR-012 Tóm tắt khách, nhắc việc"])
    U13(["UC-FBR-013 Nội dung báo giá nháp"])
    U14(["UC-FBR-014 Hỏi đáp số liệu P2"])
  end
  subgraph NUTR["Dinh dưỡng (NUTR)"]
    U15(["UC-FBR-015 Mục tiêu nhóm"])
    U16(["UC-FBR-016 Kiểm theo mục tiêu nhóm"])
    U17(["UC-FBR-017 Đồng ý nhật ký P2"])
    U18(["UC-FBR-018 Ghi bữa đã ăn P2"])
    U19(["UC-FBR-019 Xem nhật ký P2"])
    U20(["UC-FBR-020 Xóa nhật ký P2"])
  end

  NA --> U1
  NA --> U2
  DT --> U1
  DT --> U2
  DD --> U1
  DD --> U2
  DD --> U3
  DD --> U4
  DD --> U5
  DD --> U6
  BT --> U5
  BT --> U6
  KT --> U5
  KT --> U6
  GD --> U5
  GD --> U6
  DD --> U7
  GD --> U7
  DD --> U8
  GD --> U8
  KT --> U9
  KT --> U10
  KT --> U11
  DD --> U12
  GD --> U12
  DD --> U13
  GD --> U13
  KT --> U14
  GD --> U14
  DD --> U15
  DD --> U16
  NA --> U17
  NA --> U18
  NA --> U19
  NA --> U20
  U7 -. "dùng" .-> AIO
  U9 -. "dùng" .-> AIO
  U12 -. "dùng" .-> AIO
  U14 -. "dùng" .-> AIO
  SRC -. "nguồn đọc" .-> U3
  SRC -. "nguồn đọc" .-> U6
  U7 -. "phương án" .-> U8
  U3 -. "số liệu" .-> U4
  U15 -. "mục tiêu" .-> U16
  U17 -. "consent" .-> U18
```

Nhật ký bữa đã ăn (FEAT-087) chỉ ghi bữa và giá trị dinh dưỡng của suất; không thu, suy luận hay lưu sức khỏe, không dùng FEAT-046/047. Người ăn PER-04 dùng nhật ký hay không còn chờ E12-Q15, E12-Q17 nên sơ đồ gộp chung nhóm "Người ăn".

## 3. Ma trận FR, UC, màn hình, API

| UC | FR | Feature | Tác nhân chính | Màn hình | API | Gate chính |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [UC-FBR-001](../usecases/UC-FBR-001.md) | FR-FB-RATE-001 | FEAT-079 | PER-02/03/04/05 | UI-FBR-01 | API-FBR-001 | E12-Q01/02 |
| [UC-FBR-002](../usecases/UC-FBR-002.md) | FR-FB-CASE-001 | FEAT-079 | PER-02/03/04/05 | UI-FBR-02 | API-FBR-002 | E12-Q02/03 |
| [UC-FBR-003](../usecases/UC-FBR-003.md) | FR-FB-SELR-001 | FEAT-080 | PER-05 | UI-FBR-03 | API-FBR-003 | E12-Q04 |
| [UC-FBR-004](../usecases/UC-FBR-004.md) | FR-FB-PROP-001 | FEAT-080 | PER-05 | UI-FBR-04 | API-FBR-004 | E12-Q05 |
| [UC-FBR-005](../usecases/UC-FBR-005.md) | FR-RPT-ROLE-001 | FEAT-081 | PER-05/06/07/08 | UI-FBR-05 | API-FBR-005 | E12-Q06/07 |
| [UC-FBR-006](../usecases/UC-FBR-006.md) | FR-RPT-CPCT-001 | FEAT-081 | PER-05/06/07/08 | UI-FBR-06 | API-FBR-006 | E12-Q07/08 |
| [UC-FBR-007](../usecases/UC-FBR-007.md) | FR-AIO-PRRV-001 | FEAT-082 | PER-05/08 | UI-FBR-07 | API-FBR-007 | E12-Q09 |
| [UC-FBR-008](../usecases/UC-FBR-008.md) | FR-AIO-RCHK-001 | FEAT-082 | PER-05/08 | UI-FBR-07 | API-FBR-008 | E12-Q09 |
| [UC-FBR-009](../usecases/UC-FBR-009.md) | FR-AIO-ESTR-001 | FEAT-083 | PER-07 | UI-FBR-08 | API-FBR-009 | E12-Q09 |
| [UC-FBR-010](../usecases/UC-FBR-010.md) | FR-AIO-DEMR-001 | FEAT-083 | PER-07 | UI-FBR-08 | API-FBR-010 | E12-Q09; E11-Q01 |
| [UC-FBR-011](../usecases/UC-FBR-011.md) | FR-AIO-PDEV-001 | FEAT-083 | PER-07 | UI-FBR-08 | API-FBR-011 | E12-Q10 |
| [UC-FBR-012](../usecases/UC-FBR-012.md) | FR-AIO-CRMS-001 | FEAT-084 | PER-05/08 | UI-FBR-09 | API-FBR-012 | E12-Q11 |
| [UC-FBR-013](../usecases/UC-FBR-013.md) | FR-AIO-CRMQ-001 | FEAT-084 | PER-05/08 | UI-FBR-09 | API-FBR-013 | E12-Q11 |
| [UC-FBR-014](../usecases/UC-FBR-014.md) | FR-AIO-DQA-001 | FEAT-085 (P2) | PER-07/08 | UI-FBR-10 | API-FBR-014 | E12-Q12 |
| [UC-FBR-015](../usecases/UC-FBR-015.md) | FR-NUTR-GRPT-001 | FEAT-086 | PER-05 | UI-FBR-11 | API-FBR-015 | E12-Q13/14; NUTR-Q01 đến Q04 |
| [UC-FBR-016](../usecases/UC-FBR-016.md) | FR-NUTR-GRPC-001 | FEAT-086 | PER-05 | UI-FBR-11 | API-FBR-016 | E12-Q13/14 |
| [UC-FBR-017](../usecases/UC-FBR-017.md) | FR-NUTR-DCON-001 | FEAT-087 (P2) | PER-03 | UI-FBR-12 | API-FBR-017 | E12-Q15 |
| [UC-FBR-018](../usecases/UC-FBR-018.md) | FR-NUTR-DREC-001 | FEAT-087 (P2) | PER-03 | UI-FBR-12 | API-FBR-018 | E12-Q17 |
| [UC-FBR-019](../usecases/UC-FBR-019.md) | FR-NUTR-DVIW-001 | FEAT-087 (P2) | PER-03 | UI-FBR-12 | API-FBR-019 | E12-Q15 |
| [UC-FBR-020](../usecases/UC-FBR-020.md) | FR-NUTR-DDEL-001 | FEAT-087 (P2) | PER-03 | UI-FBR-12 | API-FBR-020 | E12-Q16 |

20/20 FR có đúng một UC; 9/9 feature FEAT-079 đến FEAT-087 có ít nhất một UC. Số liệu đo tài liệu, không đo phần mềm.
