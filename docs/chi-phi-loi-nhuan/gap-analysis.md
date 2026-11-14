---
id: DOC-E13-GAP-ANALYSIS
title: Rà khoảng trống E13
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, chi-phi, loi-nhuan, e13]
depends_on: [DOC-E13-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E13: Chi phí và lợi nhuận

Nháp có điều kiện · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 12 FR, 12 UC, 18 API, 5 state, từ điển, 8 màn hình |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [từ điển](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md).
- **Cách rà:** đối chiếu chuyển trạng thái với API; tìm dữ liệu tham chiếu (danh mục, đơn giá, nhân sự) chưa có nơi tạo.
- **Không làm:** không trả lời E13-Q01 đến E13-Q14, không chọn phương pháp phân bổ.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E13-01` | Dữ liệu chủ | FR-EXP-COST-001; `type_version_ref` | Từ điển nói danh mục loại chi phí có phiên bản, hiệu lực, quyết định, nhưng không có FR, API hay bảng để tạo và duyệt danh mục | High | Đã nằm trong E13-Q01; bổ sung FR quản lý danh mục khi có danh sách loại |
| `GAP-E13-02` | Thiếu API | State bảng chấm công | SUBMITTED sang CONFIRMED hoặc RETURNED không có API; chỉ có tạo và trình | Medium | Gom vào E13-Q03 (ai xác nhận giờ) |
| `GAP-E13-03` | Dữ liệu chủ | FR-EXP-LAB-001; `rate_version_ref` | Đơn giá nhân công có phiên bản được tham chiếu nhưng không có FR nhập hay duyệt đơn giá | Medium | Đã nằm trong E13-Q04 |
| `GAP-E13-04` | Liên epic | `attendance_sheets.person_ref` | Người chấm công không mặc định là `users`; E11 phân ca cũng dùng "mã nhân sự" mà chưa có nguồn (GAP-E11-08) | Medium | Xử lý chung với GAP-E11-08 |
| `GAP-E13-05` | Thiếu API | FR-EXP-COST-001 | Không có API sửa hay hủy khoản chi phí khi kỳ còn OPEN; chỉ có tạo mới | Medium | Đề xuất bổ sung khi review kỹ thuật E13-Q12 |
| `GAP-E13-06` | Trạng thái | State phương pháp | APPROVED là trạng thái cuối; chưa có cách thay thế hay ngừng một phương pháp, và chồng hiệu lực giữa hai bản chưa xử lý | Medium | Gom vào E13-Q05 |
| `GAP-E13-07` | Thiếu chức năng | E13-Q12 | Câu hỏi nhắc "export nội bộ" nhưng không có FR xuất báo cáo lợi nhuận | Low | Bổ sung FR khi E13-Q12 có trả lời |
| `GAP-E13-08` | Liên epic | E13-Q13; E12 dashboard | Chỉ số lợi nhuận và biên lợi nhuận chuyển sang dashboard E12 chưa có định nghĩa chung | Low | Đã nằm trong E13-Q13 |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại từ điển đã có |

## 4. Giữ nguyên

E13-Q01 đến E13-Q14 giữ CHỜ TRẢ LỜI. Chưa chọn phương pháp phân bổ; lợi nhuận theo khách BLOCKED khi chưa có bản duyệt. Không backend, migration hay UAT.
