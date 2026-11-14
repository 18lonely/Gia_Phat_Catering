---
id: DOC-COST-USECASES-INDEX
title: Danh mục use case E3
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [usecase, index, e3]
author: BA
last_updated: 2026-11-16
---
# Danh mục use case E3: Cost

Draft · 16/11/2026 · Chỉ mục, chưa phê duyệt nghiệp vụ, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: liệt kê 16 UC hiện có. Không thêm hay sửa UC |

Chỉ mục lấy tên và tác nhân từ từng file UC. Cột FR lấy từ [sơ đồ use case và ma trận truy vết](../srs/usecase-diagram.md); khi có khác biệt, file UC và ma trận là căn cứ.

| UC | Tên | Tác nhân chính | FR |
| :--- | :--- | :--- | :--- |
| [UC-COST-001](UC-COST-001.md) | Quản lý nhà cung cấp | Kế toán mua hàng | `FR-COST-SUP-001` |
| [UC-COST-002](UC-COST-002.md) | Nhập và quản lý giá tham chiếu | Kế toán mua hàng | `FR-COST-PRC-001` |
| [UC-COST-003](UC-COST-003.md) | Nhập đồng thời nhiều giá trên lưới | Kế toán mua hàng | `FR-COST-PRC-004` |
| [UC-COST-004](UC-COST-004.md) | Nhập giá từ bảng tính | Kế toán mua hàng | `FR-COST-PRC-005` |
| [UC-COST-005](UC-COST-005.md) | Theo dõi lịch sử, giá thiếu và giá cũ | Kế toán mua hàng; bộ lập lịch (nhánh tự động) | `FR-COST-PRC-006` |
| [UC-COST-006](UC-COST-006.md) | Xem và so sánh cost món | Người nội bộ có quyền đọc cost; Agent Nội bộ theo quyền người dùng | `FR-COST-DISH-001` |
| [UC-COST-007](UC-COST-007.md) | Lập và duyệt bảng tính món đặc thù | Dinh dưỡng viên (lập); Giám đốc (duyệt) | `FR-COST-DISH-006` |
| [UC-COST-008](UC-COST-008.md) | Đề nghị và duyệt khoản khoán | Kế toán mua hàng (đề nghị); Giám đốc (duyệt) | `FR-COST-MEAL-004` |
| [UC-COST-009](UC-COST-009.md) | Kiểm cost và phân rã ngân sách thực đơn | Dinh dưỡng viên; người nội bộ được xem thực đơn | `FR-COST-MEAL-001` |
| [UC-COST-010](UC-COST-010.md) | Kiểm cổng duyệt và chụp cost đã duyệt | Quy trình duyệt MENU; Dinh dưỡng viên và người duyệt theo quyền MENU | `FR-COST-MEAL-005` |
| [UC-COST-011](UC-COST-011.md) | Đề nghị và duyệt chế độ kiểm cost | Người có quyền quản lý tham số; Giám đốc duyệt | `FR-COST-MEAL-008` |
| [UC-COST-012](UC-COST-012.md) | Lập và lập lại bảng dự toán | Dinh dưỡng viên hoặc kế toán mua hàng | `FR-COST-EST-001` |
| [UC-COST-013](UC-COST-013.md) | Xem lịch sử và xuất bảng dự toán | Người nội bộ có quyền; Bếp trưởng chỉ xem lượng cơ sở mình | `FR-COST-EST-004` |
| [UC-COST-014](UC-COST-014.md) | Tính lại và xử lý cảnh báo vượt cost | Tác vụ nền (khởi tạo); Dinh dưỡng viên/Giám đốc/Kế toán mua hàng (xử lý) | `FR-COST-ALR-001` |
| [UC-COST-015](UC-COST-015.md) | Kiểm ngân sách cho Agent Dinh dưỡng viên | svc-agent-dinh-duong-vien | `FR-COST-RUL-003` |
| [UC-COST-016](UC-COST-016.md) | Xem trước tác động của giá giả định | Người nội bộ được phép xem cost, vai trò cụ thể chờ chốt | `FR-COST-ALR-005` |

Tổng 16 UC. Số liệu đo tài liệu, không đo phần mềm hay nghiệp vụ đã duyệt.
