---
id: DOC-E10-GAP-ANALYSIS
title: Rà khoảng trống E10
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, crm, e10]
depends_on: [DOC-E10-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E10: Khách hàng và bán hàng

Nháp có điều kiện · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 16 FR, 16 UC, 23 API, 7 port, 4 state, từ điển, 9 màn hình |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [từ điển](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md).
- **Cách rà:** tìm trạng thái không có API chuyển, dữ liệu cần cho R10 chưa có luồng nhập, và chỗ nối liên epic chỉ đi một chiều.
- **Không làm:** không trả lời E10-Q01 đến E10-Q16, không thêm FR hoặc API, không chỉ định người duyệt.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E10-01` | Thiếu chức năng | State hợp đồng; FEAT-073 | State có ACTIVE sang TERMINATED, nhưng không có FR, UC hay API chấm dứt hợp đồng; cũng chưa rõ giá ACTIVE xử lý thế nào khi chấm dứt | High | Đã nằm trong E10-Q10; bổ sung FR sau khi có trả lời |
| `GAP-E10-02` | Luồng dữ liệu | FR-SALE-OPP-001; state vòng đời | Cơ hội thắng từ một intake chưa có khách: E10 không được tạo khách chủ (CG08), nên chưa có đường từ WON sang hồ sơ khách và hợp đồng | High | Gom vào CG08 và E10-Q05; cần quyết định ai tạo khách chủ |
| `GAP-E10-03` | Dữ liệu thật | R10; E10-Q14 | Từ điển có `legacyEvidenceRef` cho hợp đồng hiện hữu, nhưng không có FR hay UC nhập danh sách khách và hợp đồng đang hiệu lực; R10 cần dữ liệu này | High | Gom vào E10-Q10 và E10-Q14; quyết định nhập tay hay nhập file |
| `GAP-E10-04` | Thiếu chức năng | State báo giá ISSUED | Chuyển sang ACCEPTED cần bằng chứng khách chấp thuận, nhưng không có kênh cho khách xem và chấp thuận bản báo giá; SRS nói khách chỉ xem sau khi cơ chế truy cập được duyệt | Medium | Gom vào E10-Q08; quyết định khách chấp thuận trong hệ thống hay ngoài hệ thống |
| `GAP-E10-05` | Tự động hóa | State báo giá ISSUED sang EXPIRED; state hợp đồng SCHEDULED sang ACTIVE | Hai chuyển trạng thái phụ thuộc thời gian nhưng không có FR hay tác vụ định kỳ nào thực hiện | Medium | Đề xuất bổ sung FR tác vụ hệ thống sau khi E10-Q08, E10-Q11 có trả lời |
| `GAP-E10-06` | Liên epic | FR-CUS-LEAD-001; state đề xuất E9 | E9 có trạng thái HUMAN_REVIEW, DECLINED, REVIEWED_PROPOSAL chờ người thật xử lý, nhưng E10 chỉ nhận một chiều; không có port trả kết quả xử lý về E9 hay E8 | Medium | Gom vào E10-Q16 (XC-05); quyết định bản chủ của lead và kênh trả trạng thái |
| `GAP-E10-07` | Thiếu nguồn | FR-CUS-RISK-001 | FR chỉ "đọc kết quả đánh giá đã có"; không có FR hay tác vụ nào tạo `risk_evaluations` | Medium | Gom vào E10-Q06; bổ sung FR tác vụ đánh giá khi có ngưỡng và cửa sổ |
| `GAP-E10-08` | Cảnh báo | FEAT-071, FEAT-073 | Không có FR nhắc hợp đồng sắp hết hạn, báo giá sắp hết hiệu lực hay khách chuyển AT_RISK | Low | Đề xuất câu hỏi mới về kênh và người nhận nhắc việc |
| `GAP-E10-09` | Dữ liệu | Từ điển | `crm_risk_evaluations` và `sale_opportunity_events` được nhắc tên nhưng chưa liệt kê trường | Low | Bổ sung khi E10-Q06, E10-Q07 có trả lời |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại từ điển đã có |

## 4. Giữ nguyên

E10-Q01 đến E10-Q16 giữ CHỜ TRẢ LỜI. CG08 và O-06 vẫn mở. Câu đề xuất mới ở GAP-E10-08 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không backend, migration hay UAT.
