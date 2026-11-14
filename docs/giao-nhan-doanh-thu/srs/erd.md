---
id: DOC-E7-SRS-ERD
title: ERD E7, kế thừa và delta đề xuất
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [erd, giao-nhan, doanh-thu, delta]
depends_on: [DOC-E7-SRS-DATA-DICTIONARY-MD]
author: BA
last_updated: 2026-11-16
---
# ERD E7: kế thừa và delta đề xuất

Draft · 16/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: vẽ quan hệ cho delta trong từ điển dữ liệu E7. Không thêm thực thể hay trường |

Sơ đồ chỉ vẽ lại [delta dữ liệu E7](data-dictionary.md) và quan hệ logic đã ghi ở đó. **Schema chung giữ 65 bảng**; không có DDL, migration hay bảng được merge. Kiểu dữ liệu, độ dài, unique, index, retention chưa chốt và vẫn BLOCKED E7-Q08. Tên trường viết theo tên logic trong từ điển.

## 1. Sơ đồ

```mermaid
erDiagram
  customers ||--o{ service_points : "có"
  customers ||--o{ orders : "đặt"
  orders ||--o{ order_pricing_snapshots : "giá chụp"
  customers ||--o{ e7_reconciliation_periods : "đối soát"

  orders ||--o{ e7_delivery_notes : "giao"
  e7_delivery_notes ||--o{ e7_receipt_confirmations : "xác nhận"
  e7_delivery_notes ||--o{ e7_discrepancies : "chênh lệch"
  e7_discrepancies ||--o{ e7_resolutions : "thỏa thuận"
  e7_resolutions }o--o| e7_delivery_notes : "phiếu bù"

  orders ||--o{ e7_revenue_snapshots : "doanh thu"
  order_pricing_snapshots ||--o{ e7_revenue_snapshots : "giá dùng"
  e7_reconciliation_periods ||--o{ e7_reconciliation_lines : "dòng"
  e7_reconciliation_lines }o--|| e7_revenue_snapshots : "nguồn"
  e7_reconciliation_periods ||--o{ e7_cash_receipts : "thu tiền"
  e7_reconciliation_periods ||--o{ change_requests : "mở lại"
  change_requests ||--o{ approvals : "quyết định"
  e7_reconciliation_periods ||--o{ e7_export_runs : "xuất MISA"

  e7_delivery_notes {
    id id PK
    id orderId FK
    opaque orderRevisionRef
    opaque planRevisionRef
    int deliveredServings
    enum state
    int version
    ref evidenceRef
  }
  e7_receipt_confirmations {
    id id PK
    id deliveryId FK
    int receivedServings
    ref actorRef
    utc confirmedAt
    ref evidenceRef
    int version
  }
  e7_discrepancies {
    id id PK
    id deliveryId FK
    text description
    ref evidenceRef
  }
  e7_resolutions {
    id id PK
    id discrepancyId FK
    enum resolutionType
    id linkedSupplementRef FK
    ref adjustmentBasis
  }
  e7_revenue_snapshots {
    id id PK
    id orderId FK
    opaque orderRevisionRef
    id pricingSnapshotId FK
    int billableServings
    ref basisEvidenceRef
    decimal grossAmountDue
    decimal revenueExVat
    enum contextStatus
  }
  e7_reconciliation_periods {
    id id PK
    id customerId FK
    date fromDate
    date toDate
    int revision
    enum state
    json sourceRefs
    json totals
    enum completeness
  }
  e7_reconciliation_lines {
    id id PK
    id periodId FK
    id revenueSnapshotId FK
  }
  e7_cash_receipts {
    id id PK
    id periodId FK
    decimal amount
    date receivedDate
    ref evidenceRef
    int version
  }
  e7_export_runs {
    id id PK
    id periodRef FK
    int revision
    ref templateRef
    enum status
    text errorSummary
    ref fileRef
    hash sourceFingerprint
  }
```

`customers`, `service_points`, `orders`, `order_pricing_snapshots`, `change_requests`, `approvals` là bảng có sẵn trong [DBML tổng](../../nen-tang/srs/schema.dbml); các bảng tiền tố `e7_` là delta. `e7_reconciliation_lines` được tách từ dòng "periods / lines" của từ điển; cột của bảng dòng chưa được liệt kê ở từ điển nên chỉ vẽ khóa.

## 2. Ràng buộc cần review

| Nhóm | Ràng buộc | Căn cứ / gate |
| :--- | :--- | :--- |
| Phiếu và xác nhận | Số giao, số nhận nguyên không âm; chưa xác nhận thì số nhận không có, không mặc định 0; sửa xác nhận giữ lịch sử | BR-E7-002/004; Q-13, E7-Q01/02 |
| Thỏa thuận | Một phần thiếu chỉ có một cách xử lý (giao bù hoặc giảm trừ); phiếu bù liên kết, không sửa phiếu gốc | BR-E7-004; E7-Q02/03 |
| Doanh thu | Giá lấy từ `order_pricing_snapshots` đúng (order_id, order_version); kết quả chưa xác định để trống logic, không ghi 0 | BR-E7-005/006; E7-Q03/04 |
| Kỳ đối soát | Kỳ LOCKED bất biến; chống chồng kỳ chưa chọn | BR-E7-009; E7-Q05 |
| Thu tiền | Tiền dương; cùng chứng từ không cộng hai lần; phân bổ nhiều kỳ chưa chọn | BR-E7-008; E7-Q06 |
| Mở lại | Dùng chung `change_requests` và `approvals` của nền, không tạo nguồn duyệt thứ hai | BR-E7-009; O-06 |
| Xuất MISA | fileRef chỉ có khi tạo file thật; giữ bytes cũ khi kỳ mở lại | BR-E7-011; E7-Q07 |
| Liên kết E6 | `orderRevisionRef`, `planRevisionRef` trỏ tới delta E6 chưa merge (`order_revisions`, `production_plan_revisions`), chưa coi là FK đã triển khai | E6-CG-04/05/06/07 |

E7 không ghi `orders.status` thành DELIVERED, CONFIRMED hay RECONCILED chỉ vì DBML có enum đó; tác động ngược về nguồn E6 chờ contract được duyệt ([phụ thuộc](../review/dependencies.md)).
