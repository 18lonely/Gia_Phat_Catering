---
id: DOC-E8-SRS-ERD
title: ERD E8, kế thừa và delta đề xuất
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [erd, website, delta]
depends_on: [DOC-E8-SRS-DATA-DICTIONARY-MD]
author: BA
last_updated: 2026-11-16
---
# ERD E8: kế thừa và delta đề xuất

Draft · 16/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: vẽ quan hệ cho 8 thực thể delta trong từ điển dữ liệu E8. Không thêm thực thể hay trường |

Sơ đồ chỉ vẽ lại [delta dữ liệu E8](data-dictionary.md). **Schema chung giữ 65 bảng**; không chọn CMS, không DDL, không migration. Kiểu dữ liệu, độ dài, index, transaction và retention chờ E8-Q06, E8-Q08, E8-Q12. Không có bảng sức khỏe.

## 1. Sơ đồ

```mermaid
erDiagram
  pub_content_revisions }o--o{ pub_media_metadata : "mediaRefs"
  pub_media_metadata }o--|| files : "fileRef"
  pub_url_mappings }o--o| pub_content_revisions : "targetPath"
  pub_sample_projections }o--|| menus : "menuRef"
  pub_sample_projections }o--o{ recipes : "recipeRefs"
  pub_sample_projections }o--o| pub_price_permissions : "publicPriceRef"
  pub_trial_contexts |o--o{ pub_lead_intake : "trialRef"
  pub_lead_intake ||--o{ pub_lead_handoffs : "bàn giao"

  pub_content_revisions {
    ref contentRef PK
    int revision PK
    enum type
    string title
    string slug
    text sanitizedBody
    json mediaRefs
    enum status
    ref publicRevisionRef
  }
  pub_url_mappings {
    ref inventoryRef
    string sourceURL
    enum action
    string targetPath
    int revision
    enum verification
    ref activationEvidence
  }
  pub_sample_projections {
    ref publicSampleRef PK
    ref menuRef
    json recipeRefs
    ref nutrientCalculationRef
    ref publicPriceRef
    ref eligibilityEvidence
  }
  pub_price_permissions {
    ref publicPriceRef PK
    decimal amount
    enum displayBasis
    ref approverEvidence
    range effectiveRange
  }
  pub_trial_contexts {
    ref trialRef PK
    json allowedInputs
    json publicResult
    ref provenance
  }
  pub_lead_intake {
    ref leadRef PK
    json minimalContact
    string source
    ref consentVersion
    ref trialRef
    utc receivedAt
  }
  pub_lead_handoffs {
    ref leadRef FK
    ref handoffIdentity
    enum state
    ref receiptRef
    string lastErrorCode
  }
  pub_media_metadata {
    ref fileRef FK
    string altText
    ref rightsEvidenceRef
    json placements
    int revision
  }
```

`files`, `menus`, `recipes` là bảng có sẵn trong [DBML tổng](../../nen-tang/srs/schema.dbml); `nutrientCalculationRef` trỏ tới delta E4 nên không vẽ thành bảng. Các bảng tiền tố `pub_` là delta. Khóa chính ghi PK là gợi ý theo trường tham chiếu trong từ điển, chưa phải quyết định thiết kế.

## 2. Ràng buộc cần review

| Nhóm | Ràng buộc | Căn cứ / gate |
| :--- | :--- | :--- |
| Nội dung | Con trỏ công khai chỉ trỏ revision được phép; sửa tạo revision mới, giữ bản công khai cũ; version chống ghi đè | BR-PUB-008/009; E8-Q08 |
| URL cũ | Một URL nguồn một quyết định trong mỗi revision mapping; không vòng lặp; đích phải công khai | BR-PUB-004; E8-Q01/02 |
| Thực đơn mẫu | Chỉ trường allowlist; ID nội bộ E2, E4 không ra client; thiếu chỉ số không thành 0 | BR-PUB-001/003; E8-Q04 |
| Giá công khai | Không lấy `price_cap` hay giá hợp đồng làm giá công khai | BR-PUB-002; E8-Q03 |
| Dựng thử | Không lưu hồ sơ người ăn hay dữ liệu sức khỏe; có lưu kết quả và thời hạn hay không chưa quyết | BR-PUB-005; E8-Q05/12 |
| Lead | Chỉ ghi khi có consent đúng phiên bản; không dùng `customers`, `eaters` làm lead; chưa receipt thì chưa là đã vào CRM | BR-PUB-006/007; E8-Q06/07/13 |
| Ảnh | Chỉ file được phép công khai; không lộ `storage_key` | E8-Q09 |
