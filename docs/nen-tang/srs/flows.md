---
id: DOC-NEN-TANG-SRS-FLOWS
title: Luồng tuần tự — Nền tảng
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Luồng tuần tự — Nền tảng

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Đổi tham số có duyệt

```mermaid
sequenceDiagram
  autonumber
  actor U as QUAN_TRI
  participant S as SYS
  participant V as Giám đốc
  participant DB as Kho dữ liệu
  U->>S: propose(code,value,scope,effectiveFrom,reason)
  S->>S: kiểm kiểu, scope, ngày và reason
  S->>DB: lưu PENDING + audit
  S->>V: quyết định với version
  V-->>S: Kết quả cùng phiên bản nguồn
  alt khác người tạo và người sửa cuối
    S->>DB: ghi APPROVED + audit trong giao dịch
    DB-->>S: Commit thành công
    S-->>U: Kết quả và requestId
  else Không đủ điều kiện
    S-->>U: 403 ERR-SYS-403-01 / 409 ERR-SYS-409-02, không ghi một phần
  end
```

Mất phản hồi sau commit: tra resource/version hoặc replay cùng key theo quyền hiện tại, không tạo mới mù. Hủy thao tác trước xác nhận không gọi lệnh ghi; sau commit phải dùng lifecycle nghiệp vụ, không dùng nút quay lại để rollback. Lỗi DB/audit rollback cả giao dịch. Thiết kế chưa có transaction/backend thực thi.

[SRS](spec.md) · [API](../api/api-spec.md) · [Trạng thái](states.md).
