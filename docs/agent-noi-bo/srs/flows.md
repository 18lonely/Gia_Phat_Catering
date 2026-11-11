---
id: DOC-AGENT-NOI-BO-SRS-FLOWS
title: Luồng tuần tự — Agent Nội bộ
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Luồng tuần tự — Agent Nội bộ

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Áp dụng nháp agent

```mermaid
sequenceDiagram
  autonumber
  actor U as Dinh dưỡng viên
  participant S as AIO
  participant V as MENU và COST
  participant DB as Kho dữ liệu
  U->>S: apply(runId,candidateRevision,baseVersion,key)
  S->>S: kiểm quyền và run VALID
  S->>DB: đọc candidate/hash và nguồn cũ
  S->>V: kiểm lại quy tắc/cost/phiên bản
  V-->>S: Kết quả cùng phiên bản nguồn
  alt quyền còn hiệu lực, nguồn còn đúng, MENU DRAFT/CHECKED
    S->>DB: ghi toàn tuần DRAFT + audit + marker applied nguyên tử
    DB-->>S: Commit thành công
    S-->>U: Kết quả và requestId
  else Không đủ điều kiện
    S-->>U: 409 ERR-AIO-409-01,422 chưaVALID, không ghi một phần
  end
```

Mất phản hồi sau commit: tra resource/version hoặc replay cùng key theo quyền hiện tại, không tạo mới mù. Hủy thao tác trước xác nhận không gọi lệnh ghi; sau commit phải dùng lifecycle nghiệp vụ, không dùng nút quay lại để rollback. Lỗi DB/audit rollback cả giao dịch. Thiết kế chưa có transaction/backend thực thi.

[SRS](spec.md) · [API](../api/api-spec.md) · [Trạng thái](states.md).
