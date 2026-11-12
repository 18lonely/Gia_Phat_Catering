---
id: DOC-E13-UI-USER-FLOW-MD
title: Luồng sử dụng EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Luồng sử dụng EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## Ghi nhận và báo cáo

```mermaid
flowchart TD
 A[Chọn cơ sở và kỳ] --> B{Có quyền hiện tại?}
 B -->|Không| X[Từ chối không lộ dữ liệu]
 B -->|Có| C[Chi phí trực tiếp và công có nguồn]
 C --> D[Kiểm manifest và phương pháp]
 D --> E{Đủ bản duyệt và nguồn?}
 E -->|Không| F[BLOCKED chỉ xem chi phí trực tiếp]
 E -->|Có| G[Tạo lần báo cáo mới]
 G --> H[Đối chiếu khách và cơ sở]
 H --> I{Hết phần chưa phân bổ và khớp tổng?}
 I -->|Không| J[Hiện riêng phần chưa phân bổ và chênh lệch]
 I -->|Có| K[Chuẩn bị bằng chứng R13]
```

## Sửa sau khóa

```mermaid
flowchart LR
 A[Kỳ đã khóa] --> B[Đề nghị bút toán riêng]
 B --> C{Đủ chính sách và duyệt?}
 C -->|Không| D[PENDING không đổi bản gốc]
 C -->|Có| E[Ghi điều chỉnh theo kỳ được duyệt]
 E --> F[Lần báo cáo mới giữ tham chiếu cũ]
```

| Trạng thái UI | Hành vi |
| :--- | :--- |
| Normal | Hiện dữ liệu synthetic và nhãn nguồn; dữ liệu thật vẫn có gate. |
| Loading | Đang đọc nguồn; không hiện số cũ thành số kỳ mới. |
| Empty | Chưa có bản ghi, không biểu diễn là chi phí 0. |
| Error | Thông báo an toàn và hướng xử lý, giữ phạm vi đã chọn. |
| Offline | Không xếp hàng ghi tiền tự động; dữ liệu chỉ minh họa. |
| Blocked | Hiện câu hỏi/nguồn thiếu; không bật hành động tính hoặc phát hành. |

[Màn hình](screens.md) · [Wireframe](../html-wireframe/profit-workbench.html).
