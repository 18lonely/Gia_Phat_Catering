---
id: DOC-THUC-DON-UI-SCREENS
title: Màn hình và quyền E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [ui, screens, e2]
author: BA
last_updated: 2026-11-16
---
# Màn hình và quyền E2: Thực đơn và định lượng

Draft · 16/11/2026 · Danh mục màn hình, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo danh mục theo khuôn chung các epic; nội dung lấy từ bảng màn hình trong user flow |

Danh mục gốc nằm trong [user flow E2](user-flow.md); khi có khác biệt, user flow là căn cứ. Không có mã SCR-MENU-11.

| Màn | Tên | Đường dẫn | Vai trò | UC | Thao tác chính |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SCR-MENU-01 | Danh sách nguyên liệu | `/menu/ingredients` | Tất cả vai trò nội bộ | UC-MENU-001 | Tìm, lọc, thêm, mở chi tiết |
| SCR-MENU-02 | Form nguyên liệu (ngăn trượt) | `/menu/ingredients/:id` | Dinh dưỡng viên | UC-MENU-001 | Tạo, sửa, ngừng dùng, khai mùa vụ |
| SCR-MENU-03 | Danh mục phụ | `/menu/settings` | Dinh dưỡng viên | UC-MENU-001, 002 | Nhóm nguyên liệu, phương pháp chế biến, chất gây dị ứng, cặp món kỵ |
| SCR-MENU-04 | Danh sách món | `/menu/dishes` | Tất cả vai trò nội bộ | UC-MENU-002, 003 | Tìm, lọc, thêm, gửi duyệt hàng loạt |
| SCR-MENU-05 | Chi tiết món | `/menu/dishes/:id` | Tất cả; sửa: Dinh dưỡng viên | UC-MENU-002, 003, 005 | Thuộc tính, công thức, giá bán, lịch sử |
| SCR-MENU-06 | Soạn công thức | `/menu/dishes/:id/recipes/:rid` | Dinh dưỡng viên | UC-MENU-004 | Thêm dòng nguyên liệu, định lượng, gửi duyệt, phiên bản mới |
| SCR-MENU-07 | So sánh phiên bản công thức | `/menu/dishes/:id/recipes/compare` | Dinh dưỡng viên, người duyệt | UC-MENU-004, 010 | Xem dòng thêm, bớt, đổi |
| SCR-MENU-08 | Loại suất | `/menu/meal-types` | Dinh dưỡng viên | UC-MENU-006 | Tạo, kích hoạt, ngừng |
| SCR-MENU-09 | Danh sách thực đơn | `/menu/menus` | Tất cả vai trò nội bộ | UC-MENU-007, 011 | Lọc, tạo, sao chép |
| SCR-MENU-10 | Soạn thực đơn tuần | `/menu/menus/:id/edit` | Dinh dưỡng viên | UC-MENU-007, 008, 009 | Lưới ngày và vị trí, bảng kiểm quy tắc, món mặc định, gửi duyệt |
| SCR-MENU-12 | Xem thực đơn | `/menu/menus/:id` | Tất cả vai trò nội bộ | UC-MENU-011 | Chỉ đọc; công bố, thu hồi, xuất PDF |
| SCR-MENU-13 | Chờ duyệt | `/approvals` | Người duyệt | UC-MENU-010 | Danh sách theo loại, duyệt hàng loạt |
| SCR-MENU-14 | Chi tiết duyệt | `/approvals/:type/:id` | Người duyệt | UC-MENU-010 | Duyệt, trả lại kèm lý do |
| SCR-MENU-15 | Danh mục quy tắc | `/menu/rules` | Dinh dưỡng viên, người duyệt | UC-MENU-013 | Xem, đề nghị sửa |
| SCR-MENU-16 | Nhập từ bảng tính | `/menu/import` | Dinh dưỡng viên | UC-MENU-012 | Tải mẫu, tải tệp, kiểm, nhập |

Người duyệt là `GIAM_DOC` hoặc người được ủy quyền; tách người duyệt món và người duyệt giá chờ E2-Q7. Phần cost trên SCR-MENU-10, 12 do E3 cung cấp qua SCR-COST-12.

Wireframe HTML: [soạn thực đơn tuần](../html-wireframe/soan-thuc-don-tuan.html), [chi tiết món](../html-wireframe/chi-tiet-mon.html), [chờ duyệt](../html-wireframe/cho-duyet.html); dữ liệu giả lập. [Mapping dữ liệu](../api/data-mapping.md).
