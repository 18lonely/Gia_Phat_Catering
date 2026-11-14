---
id: DOC-E9-SRS-FLOWS
title: Sơ đồ tuần tự E9
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [sequence, ai-agent, ain]
depends_on: [DOC-E9-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Sơ đồ tuần tự E9: Agent Dinh dưỡng viên

Draft · 16/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt, chưa triển khai, không gọi mô hình AI.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: 3 sơ đồ tuần tự theo API-AIN, 4 port và BR-AIN hiện có. Không thêm endpoint, công cụ hay quy tắc |

Route, công cụ và port lấy từ [API và allowlist E9](../api/api-spec.md); trạng thái lấy từ [states](states.md). Cách chạy agent (hàng đợi, MCP công khai) tham chiếu [kiến trúc AI agent](../../nen-tang/srs/agent-architecture.md) ở mức đề xuất. Nhà cung cấp mô hình chưa chọn (E9-Q01).

## 1. Yêu cầu thực đơn, admission và kiểm E2 (FEAT-060, FEAT-064, FEAT-065)

```mermaid
sequenceDiagram
  autonumber
  actor KH as Khách PER-01/02
  participant API as API AIN
  participant SF as PORT-AIN-SAFETY
  participant AD as PORT-AIN-ADMISSION
  participant OR as Orchestrator AIN
  participant TG as PORT-AIN-TOOL-GUARD
  participant LLM as Mô hình (chưa chọn)
  participant E2 as Projection E2 / E4

  KH->>API: POST /v1/nutrition-agent/requests (sessionRef, loại suất, số suất, kiêng)
  API->>SF: Kiểm ranh giới sức khỏe ở đầu vào
  alt Có nội dung bệnh lý, điều trị
    SF-->>API: Ngoài phạm vi, không lưu raw (BR-AIN-010)
    API-->>KH: Trạng thái ngoài phạm vi, lời nhắc chờ E9-Q09
  else Hợp lệ
    API->>AD: requestKey, group, upperBound
    alt Hết lượt, vượt trần hoặc không xác định upper bound
      AD-->>API: QUOTA_BLOCKED, BUDGET_BLOCKED hoặc UNKNOWN_BLOCKED
      API-->>KH: Tạm chặn, không hiện số trần
    else Giữ chỗ nguyên tử thành công
      AD-->>API: reservationRef
      API-->>KH: 202 runRef
      OR->>LLM: Ngữ cảnh đã lọc
      LLM->>TG: Gọi ain.catalog.read
      TG->>E2: Đọc projection món đã duyệt
      E2-->>LLM: Món, định lượng được phép, dị ứng
      LLM-->>OR: Candidate nháp
      OR->>TG: ain.menu.validateDraft (candidateRef, hash)
      TG->>E2: FR-MENU-RUL-002 không lưu
      alt Vi phạm cứng hoặc validator lỗi
        E2-->>OR: Không đạt, chỉ mã quy tắc công khai
        OR->>OR: Run INVALID hoặc FAILED, không trả VALID
      else Đạt
        E2-->>OR: SafeCheck cùng hash
        OR->>OR: Run CHECKED
      end
      OR->>AD: Quyết toán usage theo eventId
    end
  end
  KH->>API: GET /v1/nutrition-agent/requests/{id}
  API-->>KH: SafeRun, SafeCandidate, SafeNutrition (không cost)
```

## 2. Chỉnh thực đơn và kiểm lại (FEAT-061)

```mermaid
sequenceDiagram
  autonumber
  actor KH as Khách
  participant API as API AIN
  participant AD as PORT-AIN-ADMISSION
  participant OR as Orchestrator AIN
  participant E2 as Bộ kiểm E2

  KH->>API: POST .../requests/{id}/revisions (baseRevision, chỉ dẫn)
  API->>API: Kiểm baseRevision còn mới nhất
  alt Revision cũ
    API-->>KH: 409, không ghi đè
  else Đúng revision
    API->>AD: Giữ chỗ lượt mới
    AD-->>API: reservationRef
    OR->>OR: Tạo revision mới kèm diff, hash mới
    OR->>E2: Kiểm lại toàn tuần, không tái dùng kết quả cũ
    E2-->>OR: SafeCheck cho hash mới
    OR-->>API: CHECKED hoặc INVALID
    API-->>KH: Revision mới và kết quả kiểm
  end
  Note over KH,E2: Nguồn món hoặc quy tắc đổi sau khi kiểm: candidate STALE, phải kiểm lại
```

## 3. Gửi đề xuất về Gia Phát (FEAT-062)

```mermaid
sequenceDiagram
  autonumber
  actor KH as Khách
  participant API as API AIN
  participant DB as Kho đề xuất AIN
  participant HO as PORT-AIN-HANDOFF
  participant RCV as Đầu nhận (chưa chọn)
  actor NV as Người thật Gia Phát

  KH->>API: POST /v1/nutrition-agent/proposals (candidateRef, revision, consent, xác nhận)
  API->>API: Kiểm quyền sở hữu, candidate CHECKED, consent
  alt Nơi nhận hoặc consent chưa chốt (E9-Q06/10)
    API-->>KH: BLOCKED, không ghi
  else Đủ điều kiện
    API->>DB: Ghi proposal và nguồn bền vững
    DB-->>API: Commit
    API-->>KH: ProposalReceipt (chỉ là tiếp nhận)
    DB->>HO: Bàn giao
    HO->>RCV: proposalRef, candidate, contact được duyệt
    alt Lỗi chuyển
      RCV-->>HO: Lỗi
      HO-->>DB: HANDOFF_ERROR, retry cùng identity
    else Có receipt
      RCV-->>HO: receiptRef
      HO-->>DB: RECEIVED
      NV->>RCV: Xem và quyết định
    end
  end
  KH->>API: GET /v1/nutrition-agent/proposals/{id}
  API-->>KH: Trạng thái có bằng chứng, không cam kết SLA
```

Mô hình không gọi được PORT-AIN-HANDOFF; đề xuất không tạo thực đơn, đơn hàng hay báo giá (BR-AIN-004). Idempotency, TTL, deadline và giao dịch quota còn BLOCKED E9-Q13; chưa có bằng chứng chạy.
