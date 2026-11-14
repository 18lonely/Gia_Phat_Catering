---
id: DOC-COST-UI-SCREENS
title: Màn hình và quyền E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [ui, screens, e3]
author: BA
last_updated: 2026-11-16
---
# Màn hình và quyền E3: Cost

Draft · 16/11/2026 · Danh mục màn hình, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo danh mục 18 màn Cost và 4 màn kế toán theo khuôn chung các epic; nội dung lấy từ user flow và README wireframe |

Danh mục gốc nằm trong [user flow Cost](user-flow.md); khi có khác biệt, user flow là căn cứ.

## 1. Màn Cost

| Màn | Tên | Đi từ | Đi tới | UC |
| :--- | :--- | :--- | :--- | :--- |
| SCR-COST-01 | Danh sách NCC | Điều hướng Cost | 02, 03 | UC-COST-001 |
| SCR-COST-02 | Form, chi tiết NCC | 01 | 01, 03 | UC-COST-001 |
| SCR-COST-03 | Bảng giá, lưới giá theo cơ sở | Điều hướng, 06 | 04, 05, 07 | UC-COST-002, 003 |
| SCR-COST-04 | Nhập giá, đổi tham chiếu, hủy giá tương lai | 03, 06, 07 | 03, 07 | UC-COST-002 |
| SCR-COST-05 | Tải mẫu, kiểm XLSX, xác nhận nhập | 03 | Báo cáo lỗi hoặc 03 | UC-COST-004 |
| SCR-COST-06 | Nguyên liệu thiếu giá, giá cũ | Điều hướng, thông báo | 07, 04 | UC-COST-005 |
| SCR-COST-07 | Lịch sử giá nguyên liệu | 03, 06 | 04, 03 | UC-COST-002, 005 |
| SCR-COST-08 | Phân rã cost món, so sánh công thức | Danh sách món, duyệt công thức | 09, MENU | UC-COST-006 |
| SCR-COST-09 | Lập, chi tiết bảng tính đặc thù | 08, 10 | 10 | UC-COST-007 |
| SCR-COST-10 | Bảng tính chờ duyệt | Điều hướng | 09; duyệt hoặc trả lại | UC-COST-007 |
| SCR-COST-11 | Khoản khoán: danh sách, đề nghị, duyệt | Điều hướng | Chi tiết, lịch sử | UC-COST-008 |
| SCR-COST-12 | Phân rã cost ngày, cơ sở và snapshot | SCR-MENU-10, SCR-MENU-12, 17 | Thực đơn hoặc cảnh báo | UC-COST-009, 010 |
| SCR-COST-13 | Tham số Cost trong SYS | Quản lý tham số | Đề nghị và duyệt | UC-COST-011 |
| SCR-COST-14 | Nhập số suất lập dự toán | Thực đơn, lịch sử dự toán | 15 hoặc lỗi theo ngày | UC-COST-012 |
| SCR-COST-15 | Bản dự toán, lịch sử, xuất | 14, điều hướng | Phiên bản khác, tải tệp | UC-COST-012, 013 |
| SCR-COST-16 | Danh sách cảnh báo vượt cost | Thông báo, điều hướng | 17 | UC-COST-014 |
| SCR-COST-17 | Chi tiết cảnh báo theo cơ sở | 16 | 12, MENU, 16 | UC-COST-014 |
| SCR-COST-18 | Mô phỏng giá (P2) | 04 | Đóng, nhập giá qua 04 | UC-COST-016 |

## 2. Màn kế toán mở rộng

| Màn | Tên | Ghi chú |
| :--- | :--- | :--- |
| SCR-ACC-01 | Chuẩn hóa giá | Giá báo, giá cost gồm VAT |
| SCR-ACC-02 | Context hóa đơn, thỏa thuận nháp | Cờ không yêu cầu hóa đơn là cờ riêng |
| SCR-ACC-03 | Khoản riêng (chiết khấu theo đơn) | Không giảm số phải trả nhà cung cấp |
| SCR-ACC-04 | Lịch sử và đơn đổi | CK-Q07 đến CK-Q09 chờ |

## 3. Quyền xem

- Bếp trưởng chỉ xem số lượng dự toán của cơ sở mình, không thấy tiền (E3-Q11).
- Ai đọc khoản khoán chờ FLOW-COST-Q05; vai trò dùng mô phỏng giá chờ FLOW-COST-Q10.
- Đổi chế độ kiểm sang CHAN cần Giám đốc duyệt.
- Cost không ra cổng khách hay Agent Dinh dưỡng viên (BR-SEC-010).

Wireframe: [18 màn Cost](../html-wireframe/cost-workbench.html), [4 màn kế toán](../html-wireframe/accounting-workbench.html), [hướng dẫn review](../html-wireframe/README.md); dữ liệu giả lập. [Mapping dữ liệu](../api/data-mapping.md).
