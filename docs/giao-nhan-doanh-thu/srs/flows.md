---
id: DOC-E7-SRS-FLOWS
title: Sơ đồ tuần tự E7
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, giao-nhan, doanh-thu, doi-soat]
depends_on: [DOC-E7-SRS-SPEC-MD, DOC-E7-API-API-SPEC-MD, DOC-E7-SRS-STATES-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E7: Giao nhận, doanh thu và đối soát

Draft · 16/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 3 sơ đồ tuần tự theo API-E7 và BR-E7 hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Các sơ đồ dùng đúng route trong [API E7](../api/api-spec.md) và mã lỗi trong [ma trận lỗi](error-matrix.md). Bước có gate được ghi nhãn BLOCKED; sơ đồ không mô tả cách producer E6 vượt cổng CG01/05/06/08.

## 1. Giao, xác nhận và chênh lệch (FEAT-049, FEAT-050)

```mermaid
sequenceDiagram
  autonumber
  actor BT as Bếp trưởng / QL cơ sở
  participant UI as Web E7
  participant API as API E7
  participant E6 as Nguồn E6
  participant DB as CSDL E7
  actor DK as Đại diện khách
  actor VH as Vận hành

  BT->>UI: Nhập số giao và bằng chứng
  UI->>API: POST /v1/deliveries (orderId, orderRevisionRef, planRevisionRef)
  API->>API: Kiểm quyền và scope cơ sở (BR-E7-001)
  API->>E6: Đọc order revision, plan revision
  alt Nguồn thiếu hoặc chưa đủ điều kiện (CG05/06/08)
    E6-->>API: Không có bản hợp lệ
    API-->>UI: 503 kèm mã gate, không tạo phiếu
  else Nguồn hợp lệ có điều kiện
    API->>DB: Ghi phiếu WAITING_CONFIRMATION, số chốt và số giao riêng, audit
    DB-->>API: Commit
    API-->>UI: 201 phiếu chờ xác nhận
  end

  DK->>UI: Mở link nhận hàng
  Note over DK,UI: Mở link không là xác nhận. Cơ chế xác minh BLOCKED E7-Q01, CG01
  DK->>API: POST /v1/deliveries/{id}/confirmations (số nhận, version)
  API->>DB: Kiểm version phiếu
  alt Version cũ
    API-->>DK: 409, không ghi
  else Số nhận bằng số giao
    API->>DB: Ghi xác nhận, phiếu CONFIRMED
  else Số nhận khác số giao
    API->>DB: Ghi xác nhận, phiếu DISPUTED
    VH->>API: POST /v1/delivery-discrepancies (evidenceRef)
    API->>DB: Ghi biên bản, phiếu RESOLUTION_PENDING
    VH->>API: POST /v1/delivery-discrepancies/{id}/resolutions
    Note over VH,API: Giao bù hoặc giảm trừ, không cộng cả hai cho một phần thiếu (BR-E7-004)
    API->>DB: Ghi thỏa thuận, phiếu RESOLVED
  end
  Note over DK,API: Khách không trả lời: phiếu giữ WAITING_CONFIRMATION, BLOCKED Q-13
```

## 2. Doanh thu, đối soát, thu tiền và khóa kỳ (FEAT-051, FEAT-052)

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán doanh thu
  participant API as API E7
  participant E6 as Giá chụp E6
  participant DB as CSDL E7
  actor DK as Đại diện khách

  KT->>API: POST /v1/revenue-calculations (orderRevisionRef, pricingSnapshotId, billableServings)
  API->>E6: Đọc pricing snapshot đúng order version
  alt Thiếu căn cứ số tính tiền hoặc context VAT
    API->>DB: Lưu bản tính trạng thái chưa xác định, không ghi 0
  else Đủ nguồn
    API->>DB: Lưu số tính tiền x giá chụp, tách phải trả, VAT, CK riêng (BR-E7-005/006/007)
  end
  API-->>KT: 201 bản tính có provenance

  KT->>API: POST /v1/reconciliation-periods (customerId, fromDate, toDate)
  API->>DB: Chụp tập nguồn và version, liệt kê dòng thiếu, tranh chấp
  API-->>KT: 201 kỳ RECONCILING kèm danh sách chặn
  DK-->>KT: Bằng chứng thống nhất (kênh chờ E7-Q05, Q-13)
  KT->>API: POST .../agreements (periodVersion, agreementEvidenceRef)
  API->>DB: Kỳ AGREED, không tự ghi đã thu
  KT->>API: POST .../receipts (số tiền, chứng từ, version)
  API->>DB: Ghi khoản thu riêng, chặn trùng chứng từ (BR-E7-008)
  KT->>API: POST .../locks (periodVersion)
  alt Điều kiện khóa chưa duyệt (E7-Q05)
    API-->>KT: 503 mã gate, kỳ giữ AGREED
  else Đủ điều kiện
    API->>DB: Kỳ LOCKED, snapshot bất biến, audit
    API-->>KT: 200
  end
```

## 3. Mở lại kỳ đã khóa và xuất MISA (FEAT-052, FEAT-053)

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán doanh thu
  participant API as API E7
  participant DB as CSDL E7
  actor GD as Giám đốc

  KT->>API: POST .../reopen-requests (lý do tối thiểu 10 ký tự)
  API->>DB: Ghi yêu cầu REQUESTED, kỳ vẫn LOCKED
  GD->>API: POST /v1/reopen-requests/{id}/decisions (requestVersion, periodVersion)
  API->>DB: Kiểm Giám đốc khác người lập và sửa cuối (BR-SEC-008)
  alt Cùng người hoặc version cũ
    API-->>GD: 403 hoặc 409, kỳ giữ LOCKED
  else Từ chối
    API->>DB: Yêu cầu REJECTED, kỳ giữ LOCKED
  else Duyệt
    API->>DB: Yêu cầu APPROVED, kỳ REOPENED, giữ snapshot cũ
    Note over KT,DB: Sửa sau mở lại phải đối soát lại và khóa lại
  end

  KT->>API: POST /v1/misa-exports (periodId, revision, templateRef)
  alt Chưa có mẫu nhập được xác nhận (E7-Q07)
    API->>DB: Ghi yêu cầu BLOCKED, không tạo file
    API-->>KT: Trạng thái BLOCKED kèm mã gate
  else Có mẫu và mapping được duyệt
    API->>DB: Ghi yêu cầu, fileRef, sourceFingerprint
    API-->>KT: Trạng thái và fileRef
  end
  Note over KT,API: fileRef không chứng minh nhập MISA thành công
```

Thứ tự ghi và chống trùng (idempotency, khóa dòng) là đề xuất; persistence, TTL và envelope còn BLOCKED E7-Q08. Đây là thiết kế, chưa có bằng chứng chạy race hay fault test.
