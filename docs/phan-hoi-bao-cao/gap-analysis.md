---
id: DOC-E12-GAP-ANALYSIS
title: Rà khoảng trống E12
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, phan-hoi, bao-cao, e12]
depends_on: [DOC-E12-SRS-SPEC-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E12: Phản hồi và báo cáo

Nháp có điều kiện · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 20 FR, 20 UC, 20 API, 5 state, từ điển, 12 màn hình; đối chiếu kiến trúc AI agent 14/11/2026 |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [từ điển](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [kiến trúc AI agent](../nen-tang/srs/agent-architecture.md).
- **Cách rà:** đối chiếu chuyển trạng thái với API; tìm dữ liệu chỉ có đường ghi mà không có đường đọc hoặc ngược lại; so quy ước API với các epic khác.
- **Không làm:** không trả lời E12-Q01 đến E12-Q18, không thêm FR hoặc API.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E12-01` | Thiếu chức năng | FEAT-079; state khiếu nại | Khiếu nại dừng ở POLICY_PENDING; không có FR phân công, xử lý, phản hồi người gửi, đóng hay mở lại | High | Đã nằm trong E12-Q03; bổ sung FR sau khi có quy trình |
| `GAP-E12-02` | Thiếu API đọc | API-FBR-001, 002 | Đánh giá và khiếu nại chỉ có POST; không có GET danh sách hay chi tiết cho nhân viên, cũng không cho người gửi xem lại khiếu nại của mình | Medium | Gom vào E12-Q02/07 (ai được xem); bổ sung API đọc sau khi có quyền |
| `GAP-E12-03` | Thiếu API | State đề xuất AI; API-FBR-007 đến 014 | DRAFT_REVIEW sang REVIEWED cần "người thật ghi nhận review", nhưng không có API ghi nhận review, cũng không có GET đề xuất | Medium | Gom vào E12-Q09; quyết định review ghi ở E12 hay ở phân hệ đích (MENU, CRM, PUR) |
| `GAP-E12-04` | Thiếu chức năng | FEAT-086; state mục tiêu nhóm | Mục tiêu nhóm dừng ở REVIEW_PENDING "chờ chính sách kích hoạt"; không có FR duyệt và kích hoạt | Medium | Đã nằm trong E12-Q14 |
| `GAP-E12-05` | Trạng thái | FEAT-087 | Bốn FR nhật ký (đồng ý, ghi, xem, xóa) nhưng không có state diagram cho consent và yêu cầu xóa; rút đồng ý ảnh hưởng bữa đã ghi thế nào chưa vẽ | Medium | Vẽ state sau khi E12-Q15, E12-Q16 có trả lời |
| `GAP-E12-06` | Nhất quán | API E12 | Route E12 dùng tiền tố `/api/v1/e12/...` theo số epic; các epic khác dùng `/v1/<phân hệ>/...` (ví dụ `/v1/crm`, `/v1/purchasing`) | Medium | Đưa vào E12-Q18; đề xuất thống nhất theo phân hệ trước khi freeze |
| `GAP-E12-07` | Liên epic | FR-AIO-DEMR-001; FR-AIO-PDEV-001 | Diễn giải nhu cầu và giá lệch phụ thuộc E11 chưa có tồn kho (GAP-E11-04) và ngưỡng giá lệch (E12-Q10); kiến trúc agent mục 4.2 giả định có công cụ "đọc tồn" | Medium | Giữ BLOCKED; xử lý cùng GAP-E11-04 |
| `GAP-E12-08` | Thông báo | FEAT-082 | "Rà soát khi giá đổi" do người dùng tự kích hoạt; chưa có FR báo cho DDV khi E3 có sự kiện giá đổi ảnh hưởng thực đơn | Low | Đề xuất câu hỏi mới về kích hoạt tự động và người nhận |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại từ điển đã có |

## 4. Giữ nguyên

E12-Q01 đến E12-Q18 giữ CHỜ TRẢ LỜI. FEAT-087 không thu hay suy luận sức khỏe; FEAT-046/047/063 giữ gate O-03. Câu đề xuất mới ở GAP-E12-08 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không backend, không gọi mô hình AI.
