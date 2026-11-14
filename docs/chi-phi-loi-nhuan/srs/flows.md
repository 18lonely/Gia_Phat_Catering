---
id: DOC-E13-SRS-FLOWS
title: Sơ đồ tuần tự E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, chi-phi, loi-nhuan, e13]
depends_on: [DOC-E13-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E13: Chi phí và lợi nhuận

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 3 sơ đồ tuần tự theo API-EXP và quy tắc E13 hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Route lấy từ [API E13](../api/api-spec.md); trạng thái lấy từ [states](states.md). Bước có gate ghi nhãn BLOCKED.

## 1. Kỳ chi phí, ghi chi phí và chấm công

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán PER-07
  participant API as API E13
  participant E11 as Phân ca E11
  participant DB as CSDL E13

  KT->>API: POST /v1/expense-periods (kitchenRef, fromDate, toDate)
  API->>DB: Kỳ OPEN
  KT->>API: POST /v1/expense-entries (typeVersionRef, amount, evidenceRef, sourceKey, customerRef)
  alt Danh mục loại chi phí chưa chọn (E13-Q01)
    API-->>KT: BLOCKED
  else Kỳ đã khóa
    API-->>KT: 409, chỉ được lập điều chỉnh
  else Khoản trực tiếp thiếu khách hoặc trùng sourceKey với E3, E11
    API-->>KT: 422 hoặc 409
  else Hợp lệ
    API->>DB: Ghi khoản chi phí và audit
  end
  KT->>API: POST /v1/attendance-sheets (personRef, shiftRevisionRef, workDate, hours)
  API->>E11: Đối chiếu người, cơ sở với phân ca
  Note over API,E11: Phân ca là dự kiến, không sinh giờ thực tế
  API->>DB: Bảng công DRAFT, giờ thiếu để trống
  KT->>API: POST .../attendance-sheets/{id}/submissions
  API->>DB: SUBMITTED, chờ xác nhận (nguồn xác nhận chờ E13-Q03)
  KT->>API: POST /v1/expense-periods/{id}/locks
  alt Lịch khóa, người khóa chưa chốt (E13-Q02)
    API-->>KT: BLOCKED
  else Đủ điều kiện
    API->>DB: Kỳ LOCKED, chụp snapshot
  end
```

## 2. Phương pháp phân bổ và lần báo cáo lợi nhuận

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán PER-07
  actor GD as Giám đốc PER-08
  participant API as API E13
  participant SRC as Nguồn E3 E7 E10 E11
  participant DB as CSDL E13

  KT->>API: POST /v1/allocation-method-versions (scope, proposedBasis, effectiveRange)
  API->>DB: Phương pháp DRAFT, dữ liệu mô tả, không chọn sẵn cách phân bổ
  KT->>API: POST .../allocation-method-versions/{id}/submissions
  API->>DB: SUBMITTED
  GD->>API: POST .../allocation-method-versions/{id}/decisions (expectedVersion, expectedHash)
  alt Giám đốc là người tạo hoặc sửa cuối, hoặc hash khác
    API-->>GD: 403 hoặc 409
  else Trả lại
    API->>DB: RETURNED
  else Duyệt
    API->>DB: APPROVED, bất biến
  end
  KT->>API: POST /v1/allocation-runs (periodSnapshotRef, methodVersionRef, sourceManifestRef)
  API->>SRC: Kiểm bộ nguồn đủ và đúng phiên bản
  alt Chưa có phương pháp duyệt hoặc thiếu nguồn
    API->>DB: Lần chạy BLOCKED kèm lý do, chỉ hiện chi phí trực tiếp
  else Đủ
    API->>DB: Lần chạy READY, kết quả theo khách và phần chưa phân bổ
  end
  GD->>API: GET /v1/profit-runs/{id}/reconciliation
  API-->>GD: Từng cơ sở: tổng khách, phần chưa phân bổ, chênh so số chuẩn
  Note over GD,API: Còn phần chưa phân bổ thì chưa đủ R13, không giấu phần dư vào khách nào
```

## 3. Điều chỉnh sau khóa và đầu ra nội bộ

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán PER-07
  actor ND as Người duyệt điều chỉnh
  participant API as API E13
  participant DB as CSDL E13

  KT->>API: POST /v1/expense-adjustments (originalEntryRef, lockedSnapshotRef, số điều chỉnh, lý do)
  API->>DB: Điều chỉnh PENDING, giữ bản gốc bất biến
  ND->>API: POST /v1/expense-adjustments/{id}/decisions
  alt Người duyệt và kỳ đích chưa chốt (E13-Q10)
    API-->>ND: BLOCKED
  else Từ chối
    API->>DB: REJECTED
  else Duyệt
    API->>DB: POSTED, dòng riêng có lý do và người duyệt
  end
  KT->>API: GET /v1/profit-runs/{id}/internal-projection
  API->>API: Kiểm quyền chi tiết lương theo scope (E13-Q11)
  API-->>KT: Projection nội bộ, báo cáo cho khách chỉ số tổng hợp
```

Chống trùng, receipt và export nội bộ là đề xuất; còn BLOCKED E13-Q12. Chưa có bằng chứng chạy.
