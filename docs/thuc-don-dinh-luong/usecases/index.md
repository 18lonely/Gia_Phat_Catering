---
id: DOC-THUC-DON-USECASES-INDEX
title: Danh mục use case E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [usecase, index, e2]
author: BA
last_updated: 2026-11-16
---
# Danh mục use case E2: Thực đơn và định lượng

Draft · 16/11/2026 · Chỉ mục, chưa phê duyệt nghiệp vụ, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: liệt kê 13 UC hiện có. Không thêm hay sửa UC |

Chỉ mục lấy tên và tác nhân từ từng file UC. Cột FR lấy từ [sơ đồ use case và ma trận truy vết](../srs/usecase-diagram.md); khi có khác biệt, file UC và ma trận là căn cứ.

| UC | Tên | Tác nhân chính | FR |
| :--- | :--- | :--- | :--- |
| [UC-MENU-001](UC-MENU-001.md) | Quản lý nguyên liệu | Dinh dưỡng viên | `FR-MENU-ING-001` → `006` |
| [UC-MENU-002](UC-MENU-002.md) | Tạo món và gửi duyệt | Dinh dưỡng viên | `FR-MENU-DISH-001`, `003`, `007`, `008` |
| [UC-MENU-003](UC-MENU-003.md) | Sửa thuộc tính món đang dùng | Dinh dưỡng viên | `FR-MENU-DISH-002`, `005` |
| [UC-MENU-004](UC-MENU-004.md) | Lập công thức và phiên bản mới | Dinh dưỡng viên | `FR-MENU-RCP-001` → `006` |
| [UC-MENU-005](UC-MENU-005.md) | Đặt giá bán món | Dinh dưỡng viên | `FR-MENU-PRC-001` → `004` |
| [UC-MENU-006](UC-MENU-006.md) | Tạo loại suất | Dinh dưỡng viên | `FR-MENU-MTY-001` → `004` |
| [UC-MENU-007](UC-MENU-007.md) | Dựng thực đơn tuần | Dinh dưỡng viên | `FR-MENU-MNU-001` → `009` |
| [UC-MENU-008](UC-MENU-008.md) | Kiểm quy tắc thực đơn | Hệ thống, được gọi từ `UC-MENU-007`, `UC-MENU-009`, và từ agent ở R5, R9 | `FR-MENU-RUL-001` → `004` |
| [UC-MENU-009](UC-MENU-009.md) | Gửi duyệt thực đơn | Dinh dưỡng viên | `FR-MENU-APV-001`, `006` |
| [UC-MENU-010](UC-MENU-010.md) | Duyệt nội dung chờ duyệt | Người duyệt (vai trò `GIAM_DOC` hoặc người được uỷ quyền) | `FR-MENU-DISH-004`, `RCP-003`, `PRC-002`, `APV-002`, `RUL-006`, `007` |
| [UC-MENU-011](UC-MENU-011.md) | Công bố và thu hồi thực đơn | Dinh dưỡng viên | `FR-MENU-APV-003` → `005` |
| [UC-MENU-012](UC-MENU-012.md) | Nhập dữ liệu từ bảng tính | Dinh dưỡng viên | `FR-MENU-IMP-001` → `003` |
| [UC-MENU-013](UC-MENU-013.md) | Sửa danh mục quy tắc | Dinh dưỡng viên | `FR-MENU-RUL-005`, `006` |

Tổng 13 UC. Số liệu đo tài liệu, không đo phần mềm hay nghiệp vụ đã duyệt.
