---
id: DOC-E10-SRS-ERD
title: ERD E10, kế thừa và delta đề xuất
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [erd, crm, e10, delta]
depends_on: [DOC-E10-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# ERD E10: kế thừa và delta đề xuất

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: vẽ quan hệ cho nguồn hiện hữu và cấu trúc đề xuất trong từ điển dữ liệu E10. Không thêm thực thể hay trường |

Sơ đồ chỉ vẽ lại [từ điển dữ liệu E10](data-dictionary.md) và câu "Quan hệ" ở cuối từ điển. **Schema chung giữ 65 bảng**; không DDL, không migration. Khóa và độ dài vật lý chờ E10-Q13. Không có quan hệ tới hồ sơ sức khỏe.

## 1. Sơ đồ

```mermaid
erDiagram
  customers ||--o{ service_points : "có điểm"
  service_points ||--o{ service_schedules : "lịch"
  customers ||--o{ customer_price_terms : "giá"
  customer_price_terms |o--o{ order_pricing_snapshots : "price_term_id"

  customers ||--o{ crm_contact_drafts : "liên hệ nháp"
  crm_intakes |o--o{ sale_opportunities : "nguồn cơ hội"
  customers |o--o{ sale_opportunities : "cơ hội"
  customers ||--o{ crm_merge_reviews : "rà trùng"
  crm_merge_reviews |o--o| crm_merge_reviews : "reversalOf"
  customers ||--o{ crm_lifecycle_events : "vòng đời"
  sale_opportunities ||--o{ sale_quote_revisions : "báo giá"
  sale_quote_revisions ||--o| sale_quote_publications : "bản cho khách"
  sale_quote_revisions |o--o{ sale_contracts : "từ báo giá"
  customers ||--o{ sale_contracts : "hợp đồng"
  sale_contracts ||--o{ sale_contract_amendments : "phụ lục"
  sale_contracts ||--o{ sale_contract_price_links : "dòng giá"
  sale_contract_amendments |o--o{ sale_contract_price_links : "dòng giá"
  sale_contract_price_links }o--|| customer_price_terms : "priceTermRef"

  customer_price_terms {
    bigint id PK
    bigint customer_id FK
    bigint meal_type_id FK
    decimal quoted_unit_price
    date effective_from
    date effective_to
    string sale_price_basis
    decimal vat_rate_pct
    boolean invoice_requested
    string status
    int version
  }
  crm_contact_drafts {
    id id PK
    ref customerRef FK
    string displayName
    string contactRole
    json channels
    ref sourceEvidenceRef
    int version
  }
  crm_intakes {
    id id PK
    string sourceSystem
    string sourceRef
    string sourceRevision
    hash sourceHash
    ref safeMenuRef
    ref contactRef
    ref consentRef
    ref receiptRef
  }
  crm_merge_reviews {
    id id PK
    ref leftRef FK
    ref rightRef FK
    json versions
    json fieldChoices
    json beforeImage
    json linkMap
    ref decisionRef
    ref reversalOf
  }
  crm_lifecycle_events {
    ref customerRef FK
    enum previousState
    enum nextState
    ref evidenceRef
    json scheduleRefs
    ref evaluationRef
    enum completeness
  }
  sale_opportunities {
    id id PK
    ref customerOrIntakeRef
    ref ownerRef
    enum stage
    ref evidenceRef
    int version
  }
  sale_quote_revisions {
    ref quoteRef PK
    int revisionNo PK
    int version
    int baseRevision
    json lines
    json terms
    json attachments
    hash contentHash
  }
  sale_quote_publications {
    ref quoteRef FK
    int revisionNo FK
    json publishedProjection
  }
  sale_contracts {
    id id PK
    ref customerRef FK
    ref quoteRevisionRef FK
    ref legacyEvidenceRef
    ref signatureEvidenceRef
    enum status
    int version
  }
  sale_contract_amendments {
    id id PK
    ref contractRef FK
    ref predecessorRef
    enum status
    int version
  }
  sale_contract_price_links {
    ref contractRef FK
    ref amendmentRef FK
    ref priceTermRef FK
    ref predecessorTermRef
    date effectiveFrom
    date effectiveTo
    ref approvalRef
  }
```

`customers`, `service_points`, `service_schedules`, `customer_price_terms`, `order_pricing_snapshots` là bảng có sẵn trong [DBML tổng](../../nen-tang/srs/schema.dbml). Từ điển gộp "merge_reviews/events", "lifecycle_events/risk_evaluations", "quote_revisions/publications", "contracts/amendments" thành từng dòng; sơ đồ tách bảng theo tên nhưng trường chỉ lấy từ dòng gộp tương ứng. `crm_risk_evaluations` và `sale_opportunity_events` chưa có trường riêng nên không vẽ.

## 2. Ràng buộc cần review

| Nhóm | Ràng buộc | Căn cứ / gate |
| :--- | :--- | :--- |
| Liên hệ | Chỉ nháp; không đồng bộ master khách khi CG08 còn mở | BR-CRM-001; E10-Q01 |
| Tiếp nhận | Unique (sourceSystem, sourceRef, sourceRevision); khác hash cùng khóa là xung đột; không lưu raw chat | BR-CRM-011; E10-Q16 |
| Gộp | Không xóa khách gốc; ảnh trước có scope; quyết định và hoàn tác bất biến | BR-CRM-003/004; E10-Q03/04 |
| Vòng đời | Không suy rời từ ngày không có order; thiếu dữ liệu không thành 0 | BR-CRM-005; E10-Q05/06 |
| Báo giá | Unique (quoteRef, revisionNo); revision đã phát hành bất biến; projection khách không có cost | BR-CRM-006/007; E10-Q08 |
| Giá hợp đồng | Không chồng khoảng ACTIVE trên (customer, mealType), kể cả giao dịch đồng thời; ngày kết thúc trống chưa tự là vô hạn | BR-CRM-008; E10-Q11 |
| Phụ lục | Giữ giá cũ bất biến; không viết lại `order_pricing_snapshots` | BR-CRM-009; E10-Q12 |
