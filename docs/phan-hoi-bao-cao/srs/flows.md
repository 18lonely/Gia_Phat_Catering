---
id: DOC-E12-SRS-FLOWS
title: Sơ đồ tuần tự E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, phan-hoi, bao-cao, e12]
depends_on: [DOC-E12-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E12: Phản hồi và báo cáo

Nháp có điều kiện · 16/11/2026 · Chưa phê duyệt, chưa triển khai, không gọi mô hình AI.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 4 sơ đồ tuần tự theo API-FBR và quy tắc E12 hiện có. Không thêm endpoint, mã lỗi hay quy tắc |

Route lấy từ [API E12](../api/api-spec.md); trạng thái lấy từ [states](states.md). Cách chạy Agent Nội bộ tham chiếu [kiến trúc AI agent](../../nen-tang/srs/agent-architecture.md) ở mức đề xuất.

## 1. Đánh giá và khiếu nại (FEAT-079)

```mermaid
sequenceDiagram
  autonumber
  actor NA as Người ăn / người đặt tổng
  participant API as API E12
  participant E6 as Bữa ăn E6
  participant DB as CSDL E12

  NA->>API: POST /api/v1/e12/feedback/ratings (mealRef, ratingScaleRef, ratingValue)
  API->>E6: Kiểm bữa thuộc phạm vi người gửi
  alt Thang chưa duyệt hoặc cách xác minh QR chưa chốt (E12-Q01/02)
    API-->>NA: BLOCKED, không ghi
  else Hợp lệ
    API->>DB: Ghi đánh giá kèm nguồn, receipt
    API-->>NA: 201 receiptRef
  end
  NA->>API: POST /api/v1/e12/feedback/cases (mealRef, danh mục, nội dung về bữa)
  API->>DB: Ghi khiếu nại riêng với điểm đánh giá
  API-->>NA: 201, trạng thái RECEIVED
  Note over API,DB: Xử lý, phân công, SLA, đóng: POLICY_PENDING chờ E12-Q03
```

## 2. Dashboard và cost % (FEAT-081)

```mermaid
sequenceDiagram
  autonumber
  actor U as PER-05/06/07/08
  participant API as API E12
  participant AUTH as Quyền nền E1
  participant E3 as Cost E3
  participant SRC as Nguồn E6 E7 E10 E11

  U->>API: GET /api/v1/e12/reports/role-dashboards (roleView, dateRange)
  API->>AUTH: Lấy scope và quyền thật từ server
  API->>SRC: Đọc từng chỉ số theo metricDefinitionRef
  alt Danh mục chỉ số chưa chọn (E12-Q06)
    API-->>U: Ô BLOCKED kèm lý do
  else Có định nghĩa
    API-->>U: Giá trị, nguồn, asOf, completeness từng ô
  end
  U->>API: GET /api/v1/e12/reports/cost-percentages (date, customerRef)
  API->>AUTH: Kiểm quyền xem cost riêng (E12-Q07)
  API->>E3: Đọc cost % ngày đã tính, không tính lại
  alt Cost % theo khách
    API-->>U: BLOCKED E12-Q08 (mẫu số, phân bổ chưa chọn)
  else Cost % ngày
    API-->>U: Giá trị đúng loại chỉ số và phiên bản E3
  end
```

## 3. Trợ lý nội bộ: rà soát khi giá đổi (FEAT-082)

```mermaid
sequenceDiagram
  autonumber
  actor DD as DDV hoặc Giám đốc
  participant API as API E12
  participant AIO as Agent Nội bộ
  participant TL as Công cụ chỉ đọc
  participant E2 as Bộ kiểm E2
  participant DB as CSDL E12

  DD->>API: POST /api/v1/e12/assistant/price-review-proposals (priceChangeRef, menuRef)
  API->>AIO: Lượt chạy với quyền giao của người dùng
  AIO->>TL: Đọc sự kiện giá E3, thực đơn được phép
  TL-->>AIO: Dữ liệu trong scope
  AIO-->>API: Đề xuất đổi món hoặc định lượng (nháp)
  API->>DB: Lưu đề xuất REQUESTED hoặc DRAFT_REVIEW
  DD->>API: POST /api/v1/e12/assistant/menu-proposal-checks (candidateRef, revision)
  API->>E2: FR-MENU-RUL-002 không lưu, kiểm dị ứng, kiểm cost
  alt Thiếu nguồn
    API->>DB: BLOCKED_DATA
  else Đủ bảng kiểm
    API->>DB: DRAFT_REVIEW kèm kết quả kiểm
  end
  API-->>DD: Đề xuất chờ người thật, không ghi MENU
  Note over DD,DB: Nguồn hoặc quyền đổi sau đó: đề xuất STALE
```

## 4. Nhật ký bữa đã ăn (FEAT-087, P2)

```mermaid
sequenceDiagram
  autonumber
  actor NA as Người ăn PER-03
  participant API as API E12
  participant E4 as Dinh dưỡng E4
  participant DB as Kho nhật ký E12

  NA->>API: POST /api/v1/e12/nutrition/diary-consents (explicitAgreement)
  alt Nội dung đồng ý chưa duyệt (E12-Q15)
    API-->>NA: BLOCKED
  else Đã duyệt
    API->>DB: Ghi consent, không chọn sẵn
  end
  NA->>API: POST /api/v1/e12/nutrition/diary-meals (consumedMealRef, consumedAt)
  alt Chưa có bằng chứng đã ăn (E12-Q17)
    API-->>NA: BLOCKED, không suy từ lựa chọn hay giao nhận
  else Có bằng chứng
    API->>E4: Lấy snapshot 4 chỉ số của suất
    API->>DB: Ghi bữa đã ăn và snapshot
  end
  NA->>API: GET /api/v1/e12/nutrition/diary-meals (dateRange)
  API-->>NA: Bữa đã ghi, nhãn ước tính, không khuyến nghị cá nhân
  NA->>API: POST /api/v1/e12/nutrition/diary-deletion-requests
  API->>DB: Ghi yêu cầu xóa, không xóa giao dịch nguồn E6 E7
  API-->>NA: receiptRef, hoàn tất chỉ khi có bằng chứng xóa (E12-Q16)
```

Envelope, idempotency, receipt và refresh cache là đề xuất; còn BLOCKED E12-Q18. Chưa có bằng chứng chạy.
