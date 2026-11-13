---
id: DOC-THUC-DON-DINH-LUONG-SRS-FLOWS
title: "Luồng tuần tự: Thực đơn và định lượng"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Luồng tuần tự: Thực đơn và định lượng

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Gửi duyệt thực đơn

```mermaid
sequenceDiagram
  autonumber
  actor U as Dinh dưỡng viên
  participant S as MENU
  participant V as COST validator
  participant DB as Kho dữ liệu
  U->>S: submit(menuId,version)
  S->>S: đọc snapshot menu và quy tắc
  S->>DB: kiểm rule toàn tuần
  S->>V: kiểm cost cùng input/version
  V-->>S: Kết quả cùng phiên bản nguồn
  alt không hard violation và đủ cost, vượt chỉ chặn CHAN
    S->>DB: ghi PENDING và bằng chứng trong giao dịch
    DB-->>S: Commit thành công
    S-->>U: Kết quả và requestId
  else Không đủ điều kiện
    S-->>U: 422 thiếu đầu vào / hard violation,409 stale, không ghi một phần
  end
```

Mất phản hồi sau commit: tra resource/version hoặc replay cùng key theo quyền hiện tại, không tạo mới mù. Hủy thao tác trước xác nhận không gọi lệnh ghi; sau commit phải dùng lifecycle nghiệp vụ, không dùng nút quay lại để rollback. Lỗi DB/audit rollback cả giao dịch. Thiết kế chưa có transaction/backend thực thi.

[SRS](spec.md) · [API](../api/api-spec.md) · [Trạng thái](states.md).
