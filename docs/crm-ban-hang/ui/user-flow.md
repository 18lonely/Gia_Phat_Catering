---
id: DOC-E10-UI-USER-FLOW-MD
title: Luồng người dùng E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Luồng người dùng E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Gộp trùng và hoàn tác

```mermaid
flowchart TD
 A[UI01 xem hồ sơ] --> B{Tiêu chí trùng Q02 đã duyệt?}
 B -->|Chưa| X[UI03 BLOCKED không quét tự động]
 B -->|Đã duyệt| C[UI03 rà cặp và bằng chứng]
 C --> D[Lập đề nghị và diff từng trường]
 D --> E{Người duyệt và phiên bản hợp lệ?}
 E -->|Không| F[Chặn hoặc tải lại diff]
 E -->|Có| G{Master và tham chiếu đủ điều kiện?}
 G -->|Chưa| X
 G -->|Có| H[Ghi gộp nguyên tử và ảnh trước]
 H --> I[Yêu cầu hoàn tác có lý do]
 I --> J{Có liên kết mới hoặc xung đột?}
 J -->|Có| K[Chờ phương án Q04 được duyệt]
 J -->|Không| L[Người thật duyệt hoàn tác]
 K --> L
 L --> M[Ghi bù giữ audit và snapshot]
```

Luồng thành công chỉ sau Q02/03/04 và CG08. Lỗi: thiếu quyền, version cũ, mất phản hồi, thiếu ảnh trước. Biên: hai đề nghị cùng khách, gộp vòng A→B→A, order mới giữa xem và duyệt; phải khóa/xác minh tập tham chiếu, không gộp hoặc hoàn tác một phần. Chưa có chính sách xử lý liên kết mới thì dừng.

## Báo giá đến hợp đồng

```mermaid
flowchart TD
 A[UI02 tiếp nhận hoặc UI01 chọn khách] --> B[UI05 cơ hội]
 B --> C[UI06 tạo revision báo giá]
 C --> D{MENU và giá có nguồn hợp lệ?}
 D -->|Không| X[Giữ nháp hoặc BLOCKED]
 D -->|Có| E[Gắn thực đơn đúng revision]
 E --> F[Người thật duyệt đúng hash]
 F --> G[UI07 projection dành cho khách]
 G --> H{Có bằng chứng chấp thuận đúng bản?}
 H -->|Không| C
 H -->|Có| I[UI08 lập hợp đồng nháp]
 I --> J{Ký và quyền duyệt đã đủ?}
 J -->|Không| X
 J -->|Có| K{Giá từ đến không chồng?}
 K -->|Không| L[UI09 rà xung đột khoảng giá]
 L --> I
 K -->|Có| M[Kích hoạt có nguồn và audit]
 M --> N[UI09 phụ lục mới giữ lịch sử]
 N --> J
```

Thay món hoặc giá sau phát hành tạo revision mới; không tự giữ bằng chứng chấp thuận cũ cho nội dung mới. Hợp đồng nháp chưa cấp quyền order. Chuyển nguồn giá sang E6/Cost vẫn BLOCKED theo dependency, không viết ngược snapshot. Không gửi báo giá thật từ mock.

## Trạng thái giao diện chung

Bình thường: có dữ liệu nguồn và nhãn synthetic trong mock. Đang tải: chưa hiện số cũ như số mới. Rỗng: không có bản ghi trong phạm vi. Thiếu nguồn: nhóm dữ liệu có null và gate. Lỗi: thông báo an toàn và requestId. Mất mạng: không báo lưu thành công; giữ khóa để đối soát sau khi nối lại. Không quyền: không hiển thị dữ liệu hạn chế. Xung đột: tải lại diff trước quyết định.
