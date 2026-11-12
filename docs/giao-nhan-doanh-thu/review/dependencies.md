---
id: DOC-E7-REVIEW-DEPENDENCIES-MD
title: Phụ thuộc E6 → E7 và cổng nguồn
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Phụ thuộc E6 → E7 và cổng nguồn

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

Mỗi dòng là **giả định có điều kiện** rằng producer cung cấp nguồn được xác nhận hợp lệ về sau. Trước đó tích hợp BLOCKED. Không freeze E6, không tạo route E6 hoặc tự quyết CG đang chờ.

| Dữ liệu cần | Nguồn / đường đọc hiện có | CG liên quan | E7 sử dụng và giới hạn |
| :--- | :--- | :--- | :--- |
| Số suất chốt | FR-ORD-SUB-001/LOCK-001; orders.total_servings; API-ORD-019 OrderRevision | CG03/04/05/11 | NOTE/REV giữ số chốt riêng; không lấy Summary live thay bản khóa hoặc tính lại T/S/C; hủy/zero chưa chốt |
| Order revision | API-ORD-019; revisionId/revisionNo/orderVersion; delta order_revisions chưa merge | CG04/05/07/11 | Đúng revision và pricing snapshot.order_version; revisionNo khác version; thiếu nguồn BLOCKED |
| Plan revision | API-ORD-020/025; planId/revisionNo/sources; delta production_plan_revisions | CG06/07/11 | Truy nguồn bếp; GET/READY không là publish/ack/start; bản đủ điều kiện giao chưa chốt → BLOCKED CG06, không thiết kế cách chọn bản |
| Điểm phục vụ | API-ORD-013; service_points.customer_id/kitchen_id; service_schedules | CG08/05/06 | Điểm thuộc khách/cơ sở và lịch phải có căn cứ; không tự tạo master/thay lịch |
| Khách | customers; users.customer_id; cổng customer/account E6 chưa có master API đầy đủ | CG01/02/08 | Binding/read contract BLOCKED; không lấy users.customer_id quyết scope một/nhiều khách |
| Giá chụp | order_pricing_snapshots unique(order_id,order_version); context_status/inputs_snapshot; orders.unit_price_vnd | CG04/05/07/11; CK | Dùng đúng snapshot; không tạo thay producer; servings snapshot không tự là billableServings |
| Quyền/envelope | FR-AUTH-RBAC-001 nền; adapter E6 | CG01/08/09/11 | Authorize E7 riêng; không chốt default/null/envelope E6 |

Nguồn: [SRS E6](../../chon-mon-order/srs/spec.md), [API](../../chon-mon-order/api/api-spec.md), [mapping](../../chon-mon-order/api/data-mapping.md), [lifecycle](../../chon-mon-order/srs/lock-plan-review.md), [dependencies](../../chon-mon-order/review/dependencies.md), [sổ CG](../../chon-mon-order/review/contract-gap-register.md).

Phần độc lập: giữ số giao/nhận riêng, đọc provenance, bảo vệ kỳ khóa, tách CK trên đầu vào giả định hợp lệ. Không đặc tả lại thời điểm khóa E6, điều kiện phát hành plan, identity hay owner master. E7 không ghi orders.status thành DELIVERED/CONFIRMED chỉ vì DBML có enum; tác động nguồn phải chờ contract được duyệt.

R6/Q-13 là gate R7; G-Next nguyên roadmap chưa có evidence đạt. MISA chỉ theo mẫu nhập PRD, chưa mapping cột. VAT cost phải trả NCC; invoice flag riêng; CK không giảm phải trả; không đóng CK/DATA-COST. Synthetic không thay pilot 2 khách/tháng đối soát thật.
