---
id: DOC-E11-GAP-ANALYSIS
title: Rà khoảng trống E11
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, mua-hang, san-xuat, e11]
depends_on: [DOC-E11-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E11: Mua hàng và sản xuất

Nháp có điều kiện · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 15 FR, 15 UC, 15 API, 5 state, từ điển, 9 màn hình |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [từ điển](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md).
- **Cách rà:** đối chiếu từng chuyển trạng thái với API có sẵn; tìm dữ liệu được đọc nhưng không có nơi ghi.
- **Không làm:** không trả lời E11-Q01 đến E11-Q15, không thêm FR hoặc API, không chọn người duyệt hay chính sách tồn kho.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E11-01` | Thiếu API | State đơn mua; FR-PUR-POG-001 | State có REVIEW_REQUIRED, ISSUED, CLOSED nhưng chỉ có POST tạo nháp và GET kiểm cổng; không có API gửi duyệt, duyệt, phát hành, hủy hay đóng đơn | High | Đã nằm trong E11-Q02; bổ sung API sau khi chọn người duyệt |
| `GAP-E11-02` | Thiếu API | State phiếu nhận | EVIDENCE_REQUIRED sang CONFIRMED, CLOSED không có API; phiếu chỉ tạo được ở DRAFT | Medium | Gom vào E11-Q04/05 |
| `GAP-E11-03` | Thiếu nguồn | FR-PUR-APV-001; `supplier_balance_views` | Công nợ là projection đọc gồm đầu kỳ, nghĩa vụ, thanh toán, điều chỉnh, nhưng không có FR nào ghi nghĩa vụ hay thanh toán NCC | High | Đã nằm trong E11-Q06; cần chốt sự kiện ghi nhận nợ và nơi ghi thanh toán (E11 hay kế toán ngoài hệ thống) |
| `GAP-E11-04` | Thiếu chức năng | E11-Q01; FR-PUR-LOT-001 | Câu hỏi nhắc "tồn khả dụng", và có phạm vi lô, nhưng không có FR nào ghi xuất kho, tồn kho hay kiểm kê; nhu cầu mua không thể trừ tồn nếu không có nguồn tồn | High | Đề xuất câu hỏi mới vào gói quyết định: E11 có quản lý tồn kho không, hay chỉ ghi nhận hàng. [Kiến trúc AI agent](../nen-tang/srs/agent-architecture.md) mục 4.2 cũng giả định có công cụ "đọc tồn" cho FEAT-083 |
| `GAP-E11-05` | Thiếu chức năng | FEAT-075 | Trả hàng NCC, hàng hỏng sau nhận không có FR (chỉ có trong câu hỏi E11-Q04) | Medium | Bổ sung FR khi E11-Q04 có trả lời |
| `GAP-E11-06` | Trạng thái | FR-PLAN-SMP-001 | Mẫu lưu và kiểm tra trước giao không có state diagram; hủy mẫu hết hạn không có FR | Medium | Gom vào E11-Q10/11; vẽ state sau khi có hạn lưu và quy trình hủy |
| `GAP-E11-07` | Liên epic | FR-MENU-SGT-001; state đề xuất món thay | Sau MENU_REVIEW, chưa mô tả cách E2 nhận ứng viên để duyệt và cách báo cho bếp và E6 khi kế hoạch đã chốt | Medium | Đã nằm trong E11-Q12; giữ BLOCKED |
| `GAP-E11-08` | Dữ liệu chủ | FR-PLAN-SHF-001; `production_shifts.assignments` | Phân ca dùng "mã nhân sự", nhưng schema 65 bảng không có bảng nhân sự bếp ngoài `users`; E13 chấm công cũng cần nguồn này | Medium | Đề xuất câu hỏi mới: nhân sự bếp là `users` hay danh mục riêng; đối chiếu với E13 |
| `GAP-E11-09` | Vai trò | SRS; màn hình | Bếp trưởng và Quản lý cơ sở cùng gắn PER-06, trong khi hệ thống có hai vai trò `BEP_TRUONG`, `QL_CO_SO`; chưa rõ thao tác nào cần vai trò nào | Low | Rà lại với E11-Q13 (danh sách quyền) |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại từ điển đã có |

## 4. Giữ nguyên

E11-Q01 đến E11-Q15 giữ CHỜ TRẢ LỜI; CG06 vẫn mở. Câu đề xuất mới ở GAP-E11-04 và GAP-E11-08 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không backend, migration hay UAT.
