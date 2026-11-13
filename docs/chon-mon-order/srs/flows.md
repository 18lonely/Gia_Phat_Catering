---
id: DOC-CHON-MON-ORDER-SRS-FLOWS
title: "Sequence E6: race chọn món và khóa"
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Sequence E6: race chọn món và khóa

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

```mermaid
sequenceDiagram
  autonumber
  actor E as Người ăn
  participant O as ORD
  participant DB as Giao dịch dữ liệu
  participant J as Scheduler
  E->>O: PUT lựa chọn,version,key
  O->>DB: Khóa scope điểm-ngày-ca,kiểm deadline/quyền
  alt Trước chốt và version đúng
    O->>DB: Ghi selection và counter cùng transaction
    DB-->>E: Commit + selection version
  else Đã khóa hoặc nguồn đổi
    O-->>E: 409 không ghi một phần
  end
  J->>DB: PORT-LOCK - UC010/011 cùng scope và một transaction
  alt T đủ và default hợp lệ
    J->>DB: Gán default và chụp order revision + lines + audit + outbox
    DB-->>J: Commit khóa - plan có thể chưa có
  else Thiếu tổng hoặc default
    J-->>O: Cần xử lý theo ORD-Q07
  end
```

Thứ tự commit được server xác định; retry PORT-LOCK cùng eventKey không khóa/tạo order revision lần hai. Worker xử lý outbox tạo plan riêng sau commit; lỗi xử lý event không mở khóa số đặt. Publish là bước riêng chờ ORD-Q14, không đồng nghĩa build plan. Đây là thiết kế, chưa có bằng chứng race test.

## Đổi sau khóa và phát hành delta

```mermaid
sequenceDiagram
  actor C as Người đề nghị
  participant O as ORD
  actor A as Người duyệt
  participant DB as Transaction
  participant W as Outbox worker
  participant P as Kế hoạch
  actor K as Bếp
  C->>O: Đề nghị baseRevision và delta
  O->>DB: Lưu PENDING cùng audit
  A->>O: Quyết định với version
  O->>DB: Kiểm khác người tạo và baseline
  alt Gate đã chốt và dữ liệu hợp lệ
    DB->>DB: Revision mới - approval - outbox
    DB-->>O: Commit
    W->>DB: Đọc event bền vững
    W->>P: Thay đóng góp order bằng revision mới
    P-->>W: Plan revision và delta
    K->>P: GET020/025 đọc plan hoặc revisions
    P-->>K: Dữ liệu được phép đọc - không build hoặc ack
  else Tự duyệt hoặc stale
    DB-->>O: 403 hoặc 409 - không sửa order
  end
```

Làm rõ 12/11/2026: service principal gọi port/event, không mở UI; vận hành GET kết quả không kích hoạt job. Hai sơ đồ giữ ranh giới producer+read theo UC011/019 và AC/TC019-1/3. GET không commit nghiệp vụ, tạo receipt, publish/ack/start-production hoặc retry bằng Idempotency-Key. Không thêm contract retry/retention; CG04/05/06/07 vẫn OPEN.
