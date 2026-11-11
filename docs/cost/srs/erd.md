---
id: DOC-COST-SRS-ERD
title: Mô hình dữ liệu miền Cost — chỉ mục hiện hành
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Mô hình dữ liệu miền Cost — chỉ mục hiện hành

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Không tạo lại mô hình đã có. [ERD tổng mục5](../../nen-tang/srs/erd.md) và [DBML](../../nen-tang/srs/schema.dbml) là nguồn từ điển/cấu trúc. Miền Cost gồm15 bảng nền và4 bảng mở rộng kế toán; số65 là tổng toàn schema tại lần kiểm E4/E5, không phải65 bảng Cost.

| Nhóm | Bảng / invariant |
| :--- | :--- |
| Giá và cấu hình | suppliers,ingredient_prices,cost_allowances; giá nguyên liệu gồmVAT phải trả NCC |
| Bảng tính đặc thù | cost_sheets,cost_sheet_lines; lifecycle và hiệu lực theo SRS |
| Snapshot và tính lại | menu_cost_snapshots,menu_cost_snapshot_lines,cost_recalculations; bất biến theo vòng duyệt; event retry không ghi đè |
| Cảnh báo | cost_alerts,cost_alert_kitchens; một cảnh báo có chi tiết nhiều cơ sở |
| Dự toán | cost_estimates,cost_estimate_lines,cost_estimate_servings,cost_estimate_components,cost_estimate_allowances; snapshot số suất và phân rã |
| Kế toán mở rộng | customer_price_terms,order_pricing_snapshots,order_discount_records,order_discount_events; chiết khấu khoản riêng, không trừ phải trả |

Từ điển chi tiết và ràng buộc không lặp ở đây; [hợp đồng kế toán](../api/accounting-contract.md), [điểm CK](../accounting/business-rules.md). Chưa chạy migration hoặc có dữ liệu10 món/10 ngày thật.
