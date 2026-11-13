---
id: DOC-DINH-DUONG-SRS-USECASE-DIAGRAM
title: "Sơ đồ use case: Dinh dưỡng"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Sơ đồ use case: Dinh dưỡng

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Sơ đồ tổng quan chia nhóm để đọc; bảng dưới nối từng UC. Include/extend chỉ dùng khi có quan hệ nghiệp vụ, không coi mọi UC tự bao gồm nhau.

```mermaid
flowchart LR
  U[Người vận hành theo quyền]
  G[Giám đốc hoặc quản trị]
  subgraph SYS[Phạm vi Dinh dưỡng]
    A([Nhập và yêu cầu])
    B([Kiểm và xử lý])
    C([Xem kết quả và lịch sử])
  end
  U --> A
  U --> B
  U --> C
  G --> C
```

| UC | Tên / tài liệu |
| :--- | :--- |
| UC-NUTR-001 | [UC-NUTR-001: Quản lý bảng thành phần](../usecases/UC-NUTR-001.md) |
| UC-NUTR-002 | [UC-NUTR-002: Kiểm độ phủ nguyên liệu](../usecases/UC-NUTR-002.md) |
| UC-NUTR-003 | [UC-NUTR-003: Tính dinh dưỡng món](../usecases/UC-NUTR-003.md) |
| UC-NUTR-004 | [UC-NUTR-004: Tính dinh dưỡng tổ hợp suất](../usecases/UC-NUTR-004.md) |
| UC-NUTR-005 | [UC-NUTR-005: Xem kết quả và nguồn lịch sử](../usecases/UC-NUTR-005.md) |
