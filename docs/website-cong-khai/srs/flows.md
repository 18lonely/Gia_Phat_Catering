---
id: DOC-E8-SRS-FLOWS
title: Sơ đồ tuần tự E8
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, website, lead, publication]
depends_on: [DOC-E8-SRS-SPEC-MD, DOC-E8-API-API-SPEC-MD, DOC-E8-SRS-STATES-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E8: Website công khai

Draft · 16/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 4 sơ đồ tuần tự theo API-PUB và BR-PUB hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Route lấy từ [API E8](../api/api-spec.md); trạng thái lấy từ [states](states.md). CMS, cache, CDN và nơi lưu lead chưa chọn nên được vẽ là thành phần logic. Bước có gate ghi nhãn BLOCKED.

## 1. Soạn, xem trước và công bố nội dung (FEAT-059)

```mermaid
sequenceDiagram
  autonumber
  actor S as Người soạn
  actor P as Người công bố
  participant API as API E8 admin
  participant DB as Kho nội dung
  participant C as Cache công khai

  S->>API: POST /v1/admin/public/contents (nháp mới)
  API->>DB: Ghi revision Draft và audit
  S->>API: PUT /v1/admin/public/contents/{id} (version)
  alt Version cũ
    API-->>S: 409, không ghi đè
  else Đúng version
    API->>API: Làm sạch body, kiểm slug và mediaRefs
    API->>DB: Ghi revision nháp mới, giữ bản công khai cũ
  end
  S->>API: GET .../{id}/preview
  API-->>S: Bản xem trước có nhãn nháp, không vào cache công khai
  P->>API: POST .../{id}/publication (revision, action, lý do)
  alt Policy duyệt chưa chọn (E8-Q08)
    API-->>P: Lỗi policy kèm mã gate, giữ trạng thái
  else Đủ quyền và đúng revision
    API->>DB: Đặt publicRevisionRef hoặc thu hồi, audit
    API->>C: Làm mới hoặc gỡ bản cũ (cơ chế chờ E8-Q12)
    API-->>P: 200 Published hoặc Withdrawn
  end
```

## 2. Xem thực đơn mẫu và dựng thử (FEAT-056, FEAT-057)

```mermaid
sequenceDiagram
  autonumber
  actor K as Khách truy cập
  participant W as Website
  participant API as API E8 public
  participant PJ as Projection công khai
  participant RC as Bộ kiểm E2

  K->>W: Mở trang thực đơn mẫu
  W->>API: GET /v1/public/menu-samples/{id}
  API->>PJ: Đọc projection theo allowlist (BR-PUB-001)
  alt Thiếu giá được phép, định lượng hoặc 4 chỉ số
    PJ-->>API: Nguồn chưa đủ (E8-Q03/04)
    API-->>W: Không hiện như bản đủ, ghi rõ thiếu
  else Đủ nguồn
    PJ-->>API: Giá, định lượng, kcal, đạm, béo, bột đường, dị ứng
    API-->>W: 200 kèm nhãn ước tính từ định lượng sống
  end

  K->>W: Chọn loại suất, số suất, nguyên liệu kiêng
  W->>API: POST /v1/public/menu-trials
  API->>API: Kiểm đầu vào, chặn dữ liệu sức khỏe (BR-PUB-005)
  alt Cách sinh mẫu chưa chọn (E8-Q05)
    API-->>W: BLOCKED kèm mã, không tạo kết quả giả
  else Policy đã duyệt
    API->>RC: Kiểm quy tắc cứng, không lưu thực đơn
    RC-->>API: Đạt hoặc không có phương án
    API-->>W: trialRef và kết quả mẫu chưa áp dụng
  end
```

## 3. Gửi form tư vấn và bàn giao lead (FEAT-058)

```mermaid
sequenceDiagram
  autonumber
  actor K as Khách truy cập
  participant API as API E8 public
  participant LD as Kho lead E8
  participant PT as PORT-PUB-LEAD-HANDOFF
  participant CRM as E10 CRM
  actor L as Người xử lý lead

  K->>API: POST /v1/public/leads (liên hệ, consent, nguồn, trialRef)
  alt Thiếu trường hoặc chưa đồng ý
    API-->>K: 422, không ghi lead
  else Hợp lệ
    API->>LD: Ghi lead bền vững kèm nguồn và consentVersion
    LD-->>API: Commit
    API-->>K: receiptRef, chưa đồng nghĩa CRM đã nhận
  end
  Note over K,API: Mất phản hồi: trạng thái Uncertain, đối soát trước khi gửi lại

  LD->>PT: Bàn giao lead
  alt E10 chưa có contract (E8-Q06/07)
    PT-->>LD: HandoffBlocked
  else Contract đã duyệt
    PT->>CRM: Gửi lead cùng identity bàn giao
    CRM-->>PT: receiptRef
    PT-->>LD: Acknowledged
  end
  L->>API: GET /v1/admin/public/lead-handoffs/{id}
  API-->>L: Trạng thái chờ, lỗi hoặc đã có receipt
```

## 4. Chuẩn bị và phục vụ URL cũ (FEAT-055)

```mermaid
sequenceDiagram
  autonumber
  actor Q as Người quản trị nội dung
  participant API as API E8 admin
  participant MP as Bảng mapping
  actor K as Khách hoặc bot tìm kiếm
  participant W as Handler website

  Q->>API: POST /v1/admin/public/url-maps (inventoryRef, KEEP hoặc REDIRECT)
  API->>MP: Đối chiếu DL-08, phát hiện trùng, đích nháp, vòng lặp
  alt Chưa có inventory DL-08 (E8-Q01)
    API-->>Q: Danh sách chặn, không báo đủ 100%
  else Có inventory
    API->>MP: Lưu mapping Proposed hoặc Blocked
  end
  Note over Q,MP: Verified sang Active cần duyệt cutover (E8-Q02, E8-Q11)

  K->>W: GET URL WordPress cũ
  W->>MP: Tra mapping Active
  alt KEEP
    W-->>K: 200 nội dung công khai đúng revision
  else REDIRECT
    W-->>K: 301 Location đích công khai đã duyệt
  else Không có mapping
    W-->>K: 404, không tự tính đạt R8
  end
```

Thứ tự ghi, chống gửi lặp cho khách ẩn danh và cơ chế làm mới cache là đề xuất; wire contract còn BLOCKED E8-Q12. Chưa có bằng chứng chạy.
