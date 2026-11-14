---
id: DOC-E10-SRS-FLOWS
title: Sơ đồ tuần tự E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, crm, e10]
depends_on: [DOC-E10-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E10: Khách hàng và bán hàng

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 4 sơ đồ tuần tự theo API-CRM, port và BR-CRM hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Route và port lấy từ [API E10](../api/api-spec.md); trạng thái lấy từ [states](states.md). Bước có gate ghi nhãn BLOCKED.

## 1. Tiếp nhận lead và đề xuất (FEAT-070)

```mermaid
sequenceDiagram
  autonumber
  participant SRC as E8 website / E9 agent
  participant API as API CRM
  participant DB as CSDL CRM
  actor CS as DDV kiêm CSKH

  SRC->>API: POST /v1/crm/intakes (sourceSystem, sourceRef, sourceRevision, sourceHash)
  API->>API: Kiểm dịch vụ gọi được cấp quyền
  alt Giao tiếp đầu nhận chưa duyệt (E8-Q06, E9-Q06, E10-Q16)
    API-->>SRC: 503 mã gate, không ghi
  else Đã có intake cùng khóa nguồn
    alt Cùng hash
      API-->>SRC: Trả receipt cũ
    else Khác hash
      API-->>SRC: 409 xung đột
    end
  else Mới
    API->>DB: Ghi intake, chỉ nội dung được phép, audit
    DB-->>API: Commit
    API-->>SRC: receiptRef (không là duyệt thực đơn)
  end
  CS->>API: GET /v1/crm/intakes/{id}
  API-->>CS: Intake, nguồn, trạng thái chờ người thật
```

## 2. Rà trùng, gộp và hoàn tác (FEAT-070)

```mermaid
sequenceDiagram
  autonumber
  actor CS as DDV kiêm CSKH
  participant API as API CRM
  participant DB as CSDL CRM
  actor DG as Người duyệt gộp

  CS->>API: POST /v1/crm/duplicate-reviews (cặp khách, bằng chứng, versions)
  Note over CS,API: Tiêu chí phát hiện tự động chưa duyệt (E10-Q02), chỉ đề nghị thủ công
  API->>DB: Ghi đề nghị rà trùng
  DG->>API: POST .../duplicate-reviews/{id}/decisions (baseVersions, chọn trường)
  API->>API: Kiểm người duyệt khác người lập và sửa cuối
  alt Version cũ hoặc tự duyệt
    API-->>DG: 409 hoặc 403
  else Quyền sở hữu mã khách chưa chốt (CG08)
    API-->>DG: 503 mã gate, không gộp
  else Đủ điều kiện
    API->>DB: Lưu ảnh trước gộp, ánh xạ, sự kiện gộp, audit
    API-->>DG: 200 mergeRef
  end
  DG->>API: POST /v1/crm/merges/{id}/reversals (lý do, bằng chứng)
  API->>DB: Đọc ảnh trước và liên kết phát sinh sau gộp
  alt Cách xử lý liên kết mới chưa chọn (E10-Q04)
    API-->>DG: BLOCKED
  else Đã có quy tắc
    API->>DB: Ghi sự kiện bù, không xóa audit hay snapshot tài chính
  end
```

## 3. Báo giá từ nháp đến bản cho khách (FEAT-072)

```mermaid
sequenceDiagram
  autonumber
  actor CS as DDV kiêm CSKH
  participant API as API CRM
  participant CO as PORT-CRM-COST
  participant MN as PORT-CRM-MENU
  participant DB as CSDL CRM
  actor DQ as Người duyệt báo giá

  CS->>API: POST /v1/crm/quote-revisions (opportunityRef, dòng loại suất, điều kiện)
  API->>CO: Đọc cost nội bộ cho người có quyền riêng
  CO-->>API: Cost, margin (công thức chờ E10-Q15)
  API->>DB: Tạo báo giá và revision đầu, hash nội dung
  CS->>API: POST /v1/crm/quotes/{id}/menu-attachments (menuRef, menuRevision)
  API->>MN: Kiểm nguồn MENU được phép (E10-Q09)
  API->>DB: Chụp projection thực đơn vào đúng revision
  DQ->>API: POST /v1/crm/quotes/{id}/publications (quoteRevision, expectedHash)
  alt Hash khác hoặc người duyệt không hợp lệ
    API-->>DQ: 409 hoặc 403
  else Đủ điều kiện
    API->>API: Tạo projection allowlist, loại cost, margin, giá nhập
    API->>DB: Lưu bản phát hành bất biến, revision ISSUED
    API-->>DQ: 201 publicationRef
  end
```

## 4. Hợp đồng, kích hoạt giá và tra giá (FEAT-073)

```mermaid
sequenceDiagram
  autonumber
  actor CS as DDV kiêm CSKH
  participant API as API CRM
  participant DB as CSDL CRM
  actor DH as Người duyệt hợp đồng
  participant ORD as Dịch vụ order E6

  CS->>API: POST /v1/crm/contracts (quoteRevision, acceptanceEvidenceRef)
  API->>API: Kiểm bằng chứng chấp thuận đúng revision, không lấy lượt xem làm chấp thuận
  API->>DB: Hợp đồng DRAFT tham chiếu báo giá bất biến
  DH->>API: POST /v1/crm/contracts/{id}/activations (priceLines, effectiveFrom, effectiveTo)
  alt Quy ước biên ngày chưa duyệt (E10-Q11)
    API-->>DH: BLOCKED, không kích hoạt
  else Có khoảng ACTIVE chồng trên cùng khách và loại suất
    API-->>DH: 409, không ghi
  else Hợp lệ
    API->>DB: Khóa dòng customer + mealType, ghi customer_price_terms ACTIVE và liên kết
    API-->>DH: 200 ACTIVE hoặc SCHEDULED
  end
  CS->>API: POST /v1/crm/contracts/{id}/amendments (giá mới, from, to)
  API->>DB: Phụ lục DRAFT, giữ giá cũ bất biến
  Note over CS,DB: Phụ lục được duyệt bằng cùng quy tắc kích hoạt, không hồi tố snapshot order (BR-CRM-009)
  ORD->>API: GET /v1/crm/price-resolutions (customerRef, mealTypeRef, serviceDate)
  API-->>ORD: priceTermRef, contract hoặc amendmentRef, version, căn cứ VAT
```

Chống trùng, receipt và giao dịch đồng thời là đề xuất; hợp đồng kỹ thuật còn BLOCKED E10-Q13. Chưa có bằng chứng chạy.
