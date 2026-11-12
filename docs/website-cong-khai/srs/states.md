---
id: DOC-E8-SRS-STATES-MD
title: Trạng thái nội dung, URL và lead
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Trạng thái nội dung, URL và lead

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Tất cả state bên dưới là **đề xuất**, không tự chốt workflow E8-Q08 hay CRM E10. BLOCKED là kết quả preflight tài liệu, không bắt buộc enum DB.

## Nội dung / bài viết

```mermaid
stateDiagram-v2
 [*] --> Draft
 Draft --> Preview: xem trước có quyền
 Preview --> Draft: sửa revision
 Draft --> Review: nếu policy yêu cầu duyệt
 Review --> Draft: trả lại
 Review --> Ready: duyệt đúng revision
 Draft --> Ready: chỉ nếu policy không cần duyệt
 Ready --> Published: đủ quyền và gate E8-Q08
 Published --> Withdrawn: thu hồi có lý do và audit
 Published --> Draft: tạo revision mới - giữ bản public cũ
 Withdrawn --> Draft: sửa và đi lại gate
```
Draft→Ready và Review chưa chọn; không chạy đồng thời như hai cách lách duyệt. Preview là trạng thái tương tác, không lưu thành trạng thái nghiệp vụ. Public pointer độc lập revision nháp; thu hồi invalidates cache theo E8-Q12.

## Chuyển hướng URL cũ

```mermaid
stateDiagram-v2
 [*] --> Inventoried: có DL-08
 Inventoried --> Proposed: KEEP hoặc REDIRECT
 Proposed --> Blocked: trùng - xóa - thiếu đích - loop
 Blocked --> Proposed: có quyết định và sửa mapping
 Proposed --> Verified: kiểm inventory và đích
 Verified --> Active: duyệt cutover E8-Q02 và Q11
 Active --> Disabled: rollback có căn cứ
 Disabled --> Proposed: rà lại mapping
```
KEEP trả200 đúng bài, REDIRECT trả301; request GET không thay trạng thái. Verified không là đã cutover. R8 không tự miễn bài xóa khỏi mẫu số.

## Lead từ form

```mermaid
stateDiagram-v2
 [*] --> Input
 Input --> Invalid: sai trường hoặc chưa consent
 Invalid --> Input: sửa
 Input --> Pending: đủ policy và ghi bền vững
 Input --> Uncertain: mất phản hồi
 Uncertain --> Pending: đối soát tìm thấy record
 Uncertain --> Input: chỉ khi xác nhận chưa ghi
 Pending --> HandoffBlocked: E10 chưa có contract
 Pending --> Sent: đã gửi theo contract được duyệt
 Sent --> Acknowledged: receipt xác nhận
 Sent --> RetryReview: timeout hoặc lỗi
 RetryReview --> Sent: retry cùng identity theo policy
```
Input/Invalid/Uncertain là phía trình duyệt, không suy có record. Pending trở đi mới là lead đã lưu; Sent≠Acknowledged. Không định nghĩa các stage CRM. Notification có trạng thái độc lập, thất bại không xóa lead. E8-Q06/07/12 giữ chặn persistence/retry/retention.
