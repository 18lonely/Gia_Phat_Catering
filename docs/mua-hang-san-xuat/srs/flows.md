---
id: DOC-E11-SRS-FLOWS
title: Sơ đồ tuần tự E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, mua-hang, san-xuat, e11]
depends_on: [DOC-E11-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E11: Mua hàng và sản xuất

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 4 sơ đồ tuần tự theo API-PUR và BR-PUR hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Route lấy từ [API E11](../api/api-spec.md); trạng thái lấy từ [states](states.md). Bước có gate ghi nhãn BLOCKED; sơ đồ không mô tả cách E6 phát hành kế hoạch (CG06).

## 1. Nhu cầu, đơn mua và nhận hàng (FEAT-074, FEAT-075)

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán PER-07
  actor QL as Quản lý cơ sở
  participant API as API E11
  participant E6 as Kế hoạch E6
  participant E3 as Dự toán, NCC, giá E3
  participant DB as CSDL E11

  KT->>API: POST /v1/purchasing/demands (planRef, planRevision, estimateRef)
  API->>E6: Đọc đúng plan revision
  API->>E3: Đọc dự toán
  alt Kế hoạch chưa đủ điều kiện (CG06)
    API-->>KT: BLOCKED, không tính nhu cầu
  else Đủ nguồn
    API->>DB: Ghi nhu cầu theo nguyên liệu, netBuyQty để trống (E11-Q01)
    API-->>KT: 201 nhu cầu và nguồn thiếu
  end
  KT->>API: POST /v1/purchasing/purchase-orders (demandRef, supplierId, lines)
  API->>E3: Kiểm NCC trong danh mục, PriceInput có nguồn
  API->>DB: Đơn DRAFT, tổng tiền chỉ khi giá xác định
  KT->>API: GET .../purchase-orders/{id}/readiness
  API-->>KT: Điều kiện còn thiếu, BLOCKED E11-Q02 về người duyệt
  QL->>API: POST /v1/purchasing/goods-receipts (receivedQty, acceptedQty từng dòng)
  API->>API: Kiểm acceptedQty không lớn hơn receivedQty, không âm
  API->>DB: Phiếu DRAFT, giữ lượng đặt, nhận, chấp nhận riêng
  QL->>API: GET /v1/purchasing/lot-eligibility (ingredientId, storageType)
  API-->>QL: FROZEN hoặc DRY thuộc phạm vi lô, quy tắc lô chờ E11-Q03
  QL->>API: POST .../goods-receipts/{id}/evidence (fileRef)
  API->>DB: Liên kết ảnh, không xác nhận giá
```

## 2. Đối chiếu dự toán và thực mua (FEAT-076)

```mermaid
sequenceDiagram
  autonumber
  actor KT as Kế toán PER-07
  actor GD as Giám đốc PER-08
  participant API as API E11
  participant E3 as Dự toán E3
  participant DB as CSDL E11

  KT->>API: POST /v1/purchasing/purchase-comparisons (estimateRef, allocationRefs, ngày, cơ sở)
  API->>E3: Đọc dự toán cùng ngày và cơ sở
  API->>DB: Đọc thực mua đã phân bổ
  alt Cách gán thực mua theo ngày chưa chọn (E11-Q07)
    API-->>KT: BLOCKED, không trả tỷ lệ
  else Định nghĩa BO-02 chưa duyệt (E11-Q08)
    API->>DB: Lưu tiền dự toán và thực mua riêng, deltaPp để trống
    API-->>KT: Chưa xác định đạt hay không
  else Đủ điều kiện
    API->>DB: Lưu estimatedPct, actualPct, deltaPp
    API-->>KT: Kết quả so sánh có nguồn
  end
  GD->>API: GET .../purchase-comparisons/{id}/lines
  API-->>GD: Dòng dự toán, dòng nhận, giá gồm VAT, không tự phân rã giá và lượng
```

## 3. Phân ca, kiểm tra trước giao và mẫu lưu (FEAT-077)

```mermaid
sequenceDiagram
  autonumber
  actor BT as Bếp trưởng
  actor QL as Quản lý cơ sở
  participant API as API E11
  participant DB as CSDL E11

  BT->>API: POST /v1/purchasing/production-shifts (planRef, assignments)
  API->>DB: Phân ca DRAFT, không đánh dấu E6 đã bắt đầu sản xuất
  BT->>API: POST /v1/purchasing/pre-delivery-checks (checklistRef, results)
  alt Chưa có checklist được duyệt (E11-Q10)
    API-->>BT: BLOCKED
  else Còn mục chưa kiểm hoặc lỗi
    API->>DB: Ghi kết quả, chưa đủ căn cứ giao
  else Đủ mục
    API->>DB: Ghi phiếu QC
  end
  QL->>API: POST /v1/purchasing/retained-samples (mealRef, sampleCode, evidenceRef)
  API->>DB: Ghi sổ mẫu, hạn lưu và hủy chờ E11-Q11
```

## 4. Thay món do thiếu hàng (FEAT-078)

```mermaid
sequenceDiagram
  autonumber
  actor DD as Dinh dưỡng viên
  participant API as API E11
  participant E2 as Dị ứng, quy tắc E2
  participant E3 as Cost E3
  participant DB as CSDL E11

  DD->>API: POST /v1/purchasing/substitution-candidates (menuRef, originalDishId, replacementDishId)
  API->>API: Kiểm món thay cùng vai trò
  API->>DB: Ứng viên DRAFT, không sửa thực đơn đã công bố
  DD->>API: POST /v1/purchasing/substitution-checks (candidateRef, candidateVersion)
  API->>E2: Kiểm dị ứng và quy tắc trên đúng phiên bản
  API->>E3: Kiểm cost trên đúng phiên bản
  API->>DB: Lưu ba kết quả, thiếu một thì BLOCKED
  DD->>API: GET .../substitution-candidates/{id}/readiness
  alt Thiếu kết quả hoặc CHAN vượt cost
    API-->>DD: Chặn chuyển duyệt MENU
  else CANH_BAO hoặc đạt
    API-->>DD: Đủ điều kiện chuyển cổng MENU, giữ cảnh báo
  end
  Note over DD,DB: Tác động tới kế hoạch đã chốt và thông báo người liên quan chờ E11-Q12
```

Chống trùng, receipt, xử lý đồng thời là đề xuất; còn BLOCKED E11-Q13. Chưa có bằng chứng chạy.
