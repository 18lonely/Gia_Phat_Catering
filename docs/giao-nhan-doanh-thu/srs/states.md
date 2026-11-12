---
id: DOC-E7-SRS-STATES-MD
title: State diagram E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# State diagram E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

## Phiếu giao nhận

Tên trạng thái là delta E7, không đổi orders enum. Nguồn hợp lệ BLOCKED CG05/06/08; xác nhận BLOCKED CG01/E7-Q01. Không đặc tả cách vượt cổng.

```mermaid
stateDiagram-v2
 [*] --> DRAFT
 DRAFT --> WAITING_CONFIRMATION: ghi giao - nguồn hợp lệ có điều kiện
 WAITING_CONFIRMATION --> CONFIRMED: nhận đúng số và đủ quyền
 WAITING_CONFIRMATION --> DISPUTED: xác nhận có chênh lệch
 WAITING_CONFIRMATION --> WAITING_CONFIRMATION: không trả lời - BLOCKED Q13
 DISPUTED --> RESOLUTION_PENDING: lập biên bản
 RESOLUTION_PENDING --> RESOLVED: thỏa thuận và evidence - Q02
```

CONFIRMED không tự xác định số tính tiền/đã thu/đối soát. Phiếu bù liên kết, không sửa gốc. Zero/hủy/nhận thừa/giao nhiều lần chưa transition tự động.

## Kỳ đối soát

```mermaid
stateDiagram-v2
 [*] --> DRAFT
 DRAFT --> RECONCILING: lập tập nguồn
 RECONCILING --> RECONCILING: thiếu hoặc tranh chấp - BLOCKED
 RECONCILING --> AGREED: đủ nguồn và evidence đúng revision
 AGREED --> LOCKED: điều kiện khóa được duyệt - Q05
 LOCKED --> REOPENED: Giám đốc duyệt đúng version
 REOPENED --> RECONCILING: sửa có audit và đối soát lại
```

Thu tiền là chiều dữ liệu riêng; AGREED/LOCKED không suy PAID. Chưa chọn có phải thu đủ trước khóa. LOCKED chặn cả phiếu/doanh thu/chứng từ/import.

## Yêu cầu mở lại

```mermaid
stateDiagram-v2
 [*] --> REQUESTED: kỳ khóa và lý do hợp lệ
 REQUESTED --> APPROVED: Giám đốc khác lập và sửa cuối
 REQUESTED --> REJECTED: từ chối
 REQUESTED --> REQUESTED: chưa duyệt - kỳ vẫn khóa
 APPROVED --> [*]: kỳ REOPENED - giữ snapshot cũ
 REJECTED --> [*]: kỳ vẫn LOCKED
```

Kiểm version tại ghi; quyết định cũ không mở kỳ mới. O-06 không tự cấp người thay. File đã xuất giữ revision cũ/cần rà lại, không sửa bytes hoặc auto tái xuất. [Q05/07/08](../review/questions.md).
