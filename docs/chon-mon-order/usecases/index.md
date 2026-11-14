---
id: DOC-E6-USECASES-INDEX
title: Danh mục use case E6
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [usecase, index, e6]
author: BA
last_updated: 2026-11-16
---
# Danh mục use case E6: Chọn món và order

Draft · 16/11/2026 · Chỉ mục, chưa phê duyệt nghiệp vụ, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: liệt kê 19 UC hiện có. Không thêm hay sửa UC |

Chỉ mục lấy tên và tác nhân từ từng file UC. Cột FR lấy từ [sơ đồ use case và ma trận truy vết](../srs/usecase-diagram.md); khi có khác biệt, file UC và ma trận là căn cứ.

| UC | Tên | Tác nhân chính | FR |
| :--- | :--- | :--- | :--- |
| [UC-ORD-001](UC-ORD-001.md) | Cấp quyền người đặt tổng | Nhân viên Gia Phát được cấp quyền quản trị khách/phạm vi tương ứng | `FR-AUTH-EXT-001` |
| [UC-ORD-002](UC-ORD-002.md) | Đăng ký qua QR công ty | Người ăn | `FR-AUTH-QREG-001` |
| [UC-ORD-003](UC-ORD-003.md) | Mở phiên QR giới hạn | Người ăn qua QR | `FR-AUTH-QSES-001` |
| [UC-ORD-004](UC-ORD-004.md) | Quản lý QR và danh sách người ăn | Người đặt tổng | `FR-AUTH-QRM-001` |
| [UC-ORD-005](UC-ORD-005.md) | Quản lý dữ liệu phục vụ | Dinh dưỡng viên | `FR-CUS-SVC-001` |
| [UC-ORD-006](UC-ORD-006.md) | Đặt định mức công ty | Người đặt tổng | `FR-ORD-QTA-001` |
| [UC-ORD-007](UC-ORD-007.md) | Chọn và đổi một món chính | Người ăn | `FR-ORD-SEL-001` |
| [UC-ORD-008](UC-ORD-008.md) | Gửi lựa chọn cả tuần | Người ăn có tài khoản | `FR-ORD-WEEK-001` |
| [UC-ORD-009](UC-ORD-009.md) | Chốt tổng suất và phân bổ | Người đặt tổng | `FR-ORD-SUB-001` |
| [UC-ORD-010](UC-ORD-010.md) | Gán món mặc định khi khóa | Scheduler/service principal có quyền scope gọi PORT-LOCK | `FR-ORD-DEF-001` |
| [UC-ORD-011](UC-ORD-011.md) | Khóa tại hạn và phát hành nguồn kế hoạch | Scheduler/service principal có quyền scope gọi PORT-LOCK | `FR-ORD-LOCK-001` |
| [UC-ORD-012](UC-ORD-012.md) | Đề nghị và duyệt thay đổi sau khóa | Người đặt tổng/nội bộ có quyền tạo đề nghị | `FR-ORD-CHG-001` |
| [UC-ORD-013](UC-ORD-013.md) | Điều phối nhập hộ | Dinh dưỡng viên | `FR-ORD-PXY-001` |
| [UC-ORD-014](UC-ORD-014.md) | Nhắc người chưa chọn | Scheduler khởi tạo lịch nhắc | `FR-ORD-REM-001` |
| [UC-ORD-015](UC-ORD-015.md) | Đổi chế độ chọn món | Người đặt tổng | `FR-ORD-MODE-001` |
| [UC-ORD-016](UC-ORD-016.md) | Xem thông tin món công bố | Người ăn | `FR-NUTR-DSP-001` |
| [UC-ORD-017](UC-ORD-017.md) | Giữ cổng hồ sơ sức khỏe | Người ăn có tài khoản xem trạng thái tính năng trên UI-ORD-12 | `FR-NUTR-PROF-001` |
| [UC-ORD-018](UC-ORD-018.md) | Giữ cổng gợi ý cá nhân | Người ăn có tài khoản xem trạng thái tính năng trên UI-ORD-12 | `FR-NUTR-REC-001` |
| [UC-ORD-019](UC-ORD-019.md) | Đọc kế hoạch sản xuất phiên bản | Bếp trưởng/quản lý cơ sở có quyền đọc scope bếp | `FR-PLAN-MEAL-001` |

Tổng 19 UC. Số liệu đo tài liệu, không đo phần mềm hay nghiệp vụ đã duyệt.
