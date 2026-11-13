---
id: DOC-COST-SRS-FLOWS
title: Luồng tuần tự (Cost)
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Luồng tuần tự (Cost)

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Tính cost và chụp khi duyệt

```mermaid
sequenceDiagram
  autonumber
  actor U as MENU
  participant S as COST
  participant V as Nguồn giá và tham số
  participant DB as Kho dữ liệu
  U->>S: calculate(menuRevision,kitchenIds,dates)
  S->>S: đọc giá gồmVAT phải trả và cấu hình hiệu lực
  S->>DB: tính theo công thức SRS, không chiết khấu khỏi phải trả
  S->>V: yêu cầu chụp vòng duyệt
  V-->>S: Kết quả cùng phiên bản nguồn
  alt đủ giá/VAT/bảng đặc thù, version nguồn còn đúng
    S->>DB: ghi snapshot của vòng duyệt, không sửa snapshot cũ
    DB-->>S: Commit thành công
    S-->>U: Kết quả và requestId
  else Không đủ điều kiện
    S-->>U: 422 thiếu giá/VAT,409 nguồn đổi, không ghi một phần
  end
```

Mất phản hồi sau commit: tra resource/version hoặc replay cùng key theo quyền hiện tại, không tạo mới mù. Hủy thao tác trước xác nhận không gọi lệnh ghi; sau commit phải dùng lifecycle nghiệp vụ, không dùng nút quay lại để rollback. Lỗi DB/audit rollback cả giao dịch. Thiết kế chưa có transaction/backend thực thi.

[SRS](spec.md) · [API](../api/api-spec.md) · [Trạng thái](states.md).
