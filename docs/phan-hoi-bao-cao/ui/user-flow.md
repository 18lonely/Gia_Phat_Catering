---
id: DOC-E12-UI-USER-FLOW-MD
title: Luồng người dùng E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Luồng người dùng E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## Phản hồi và báo cáo

```mermaid
flowchart TD
 A[Chọn vai trò và phạm vi] --> B{Có quyền hiện tại?}
 B -->|Không| C[Từ chối an toàn]
 B -->|Có| D[Đánh giá hoặc xem dashboard]
 D --> E{Đủ nguồn và định nghĩa?}
 E -->|Không| F[Hiện thiếu nguồn - không thay bằng 0]
 E -->|Có| G[Xem số và nguồn]
 G --> H[Đề xuất nháp chờ người thật]
```

## Nhật ký độc lập với hồ sơ sức khỏe

```mermaid
flowchart TD
 A[Người ăn có tài khoản] --> B{Đồng ý tự nguyện?}
 B -->|Không| C[Không ghi nhật ký - vẫn chọn món]
 B -->|Có| D{Có căn cứ bữa đã ăn?}
 D -->|Không| E[Chờ căn cứ Q17]
 D -->|Có| F[Ghi bữa và snapshot dinh dưỡng suất]
 F --> G[Xem của mình]
 G --> H[Rút đồng ý và yêu cầu xóa]
 H --> I[Receipt - chờ bằng chứng hoàn tất]
```

Mọi màn hỗ trợ Normal/Loading/Empty/Missing/Error/Offline/Denied/Conflict. Loading không hiện số cũ như mới; Empty không kết luận không có nhu cầu; Offline không gửi ngầm; Conflict yêu cầu rà revision. Bốn màn AI chỉ nháp, không có nút áp dụng nghiệp vụ. Nhật ký không có form bệnh lý hoặc gợi ý. [Danh mục màn](screens.md).
