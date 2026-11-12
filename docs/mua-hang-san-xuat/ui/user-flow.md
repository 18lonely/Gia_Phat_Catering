---
id: DOC-E11-UI-USER-FLOW-MD
title: Luồng người dùng E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Luồng người dùng E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Mua hàng đến đối chiếu

```mermaid
flowchart TD
 A[01 Nhu cầu và nguồn E6 E3] --> B{Đủ nguồn đã duyệt?}
 B -->|Không| X[BLOCKED và mã câu hỏi]
 B -->|Có| C[02 Đơn mua nháp]
 C --> D[03 Nhận hàng nháp và phạm vi lô]
 D --> E[04 Ảnh chứng từ]
 E --> F[05 Công nợ có căn cứ]
 F --> G[06 Đối chiếu ngày và cơ sở]
 G --> H{Đủ phân bổ và mẫu số?}
 H -->|Không| X
 H -->|Có| I[Hiện chênh điểm phần trăm]
```

Mũi tên là điều hướng review, không tự chuyển hiệu lực hoặc thay chính sách duyệt/ghi nhận. Nhánh mất mạng giữ nháp hiển thị và trạng thái chưa rõ; không retry ghi tự động.

## Bếp và món thay

```mermaid
flowchart TD
 A[07 Phân ca nháp] --> B[08 Kiểm trước giao và mẫu lưu]
 B --> C{Đủ chính sách và nguồn?}
 C -->|Không| D[BLOCKED E11 Q10 Q11 và E6]
 C -->|Có| E[Bàn giao E7 sau hợp đồng được duyệt]
 A --> F[09 Chọn món thay cùng vai trò]
 F --> G[Kiểm lại dị ứng quy tắc E2 cost E3]
 G --> H{Đúng nguồn và đủ kết quả?}
 H -->|Không| I[Giữ ứng viên nháp và lý do]
 H -->|Có| J[Cổng duyệt MENU hiện hành]
 J --> K[Ảnh hưởng E6 E7 còn chờ Q12]
```

## Trạng thái giao diện chung

Normal: dữ liệu synthetic có nhãn. Loading: ẩn số cũ; Empty: không có dữ liệu, không hiện tổng 0 giả; Missing: chỉ rõ nguồn/câu hỏi; Error: lỗi có thể phục hồi; Offline: không gửi; Denied: không hiện dữ liệu; Conflict: tải lại version trước thao tác. Mỗi màn có bộ chọn trạng thái để review. Không có thao tác nghiệp vụ thật. [Màn hình](screens.md).
