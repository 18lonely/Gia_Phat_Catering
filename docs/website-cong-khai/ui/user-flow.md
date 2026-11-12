---
id: DOC-E8-UI-USER-FLOW-MD
title: Luồng khách truy cập và quản trị
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Luồng khách truy cập và quản trị

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

## Khách: happy / error / edge

```mermaid
flowchart TD
 A[URL trang hoặc URL cũ] --> B{Mapping và nội dung hợp lệ}
 B -->|Có| C[Xem trang hoặc301 đúng đích]
 B -->|Không| D[Không tìm thấy hoặc giữ chặn mapping]
 C --> E[Xem mẫu có giá và nguồn]
 E --> F{Đủ quyền public và dữ liệu}
 F -->|Không| G[Chưa sẵn sàng - không giả số0]
 F -->|Có| H[Dựng thử hoặc mở form]
 H --> I{Input và policy đủ}
 I -->|Không| J[Sửa input hoặc BLOCKED]
 I -->|Có| K[Mẫu tuần - chưa đặt hàng]
 K --> L[Form consent và source]
 L --> M{Ghi bền vững được xác nhận}
 M -->|Có| N[Biên nhận - chờ điểm nối CRM]
 M -->|Timeout| O[Chưa rõ kết quả - đối soát]
 M -->|Thiếu consent| P[Không lưu lead]
```
Biên: URL đã xóa/trùng chờ E8-Q02; không có mẫu phù hợp thì báo vô nghiệm, không nới hard rule; nguồn thay đổi/stale không tính từ ảnh chụp cũ như hiện hành; truy cập trực tiếp draft không trả nội dung; form không có trial vẫn cần source, không bịa trial. Reload không phát sinh lead.

## Người quản trị: happy / error / edge

```mermaid
flowchart TD
 A[Đăng nhập AUTH] --> B{Có quyền thao tác}
 B -->|Không| C[Từ chối]
 B -->|Có| D[Soạn revision và chọn ảnh]
 D --> E{Input file version hợp lệ}
 E -->|Không| F[Sửa lỗi hoặc tải lại]
 E -->|Có| G[Lưu nháp và audit]
 G --> H[Xem trước riêng tư]
 H --> I{Policy duyệt và quyền công bố đủ}
 I -->|Chưa| J[BLOCKED E8-Q08]
 I -->|Đủ| K[Công bố revision đúng]
 K --> L[Kiểm trang và cache]
 L --> M[Thu hồi có lý do nếu cần]
 A --> N[Đối chiếu DL-08 và URL]
 N --> O{Trùng xóa loop thiếu đích}
 O -->|Có| P[Giữ chặn - hỏi tại sổE8]
 O -->|Không| Q[Kiểm đủ rồi chờ duyệt cutover]
 A --> R[Theo dõi lead đã lưu]
 R --> S[Chưa receipt - chờE10]
```
Biên: hai người sửa cùng revision →409, không overwrite; thay ảnh đang công khai cần revision, không phá bài cũ; nút publish không tự cấp quyền; thu hồi phải loại bản cache/sitemap. Mất phiên giữ nội dung local nếu policy cho phép E8-Q12, không lưu PII mặc định ở browser.
