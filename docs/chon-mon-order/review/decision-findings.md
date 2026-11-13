---
id: DOC-E6-DECISION-FINDINGS
title: Phát hiện qua review quyết định E6
version: 0.1.0
phase: Review
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Phát hiện qua review quyết định E6

Đây là review thiết kế, không phải lỗi phát hiện bằng test backend. [Bảng quyết định](decision-review.md) cung cấp phương án và ví dụ synthetic.

| Mã / mức | Bằng chứng hiện tại | Rủi ro / xử lý | Trạng thái |
| :--- | :--- | :--- | :--- |
| E6-RV-01 / High | QR dùng chung; eaters.user_id nullable; identityProof chưa đặc tả | Account và guest có thể thành2người; đề xuất cùng membership dựa danh sách được xác nhận | CHỜ ORD-Q01/11; đã có E6-EVID-001 |
| E6-RV-02 / High | SubmissionInput.coordinatorLines chỉ dishId/qty, không người | Không nhận ra người đã chọn hộ quay lại tự chọn; cần allocation theo người hoặc workflow rà gộp | CHỜ ORD-Q06 |
| E6-RV-03 / High | Guard T>=S+C có ở gửi tổng/khóa; PUT chọn chưa nêu S tăng sau gửi | Order hợp lệ lúc gửi có thể quá tổng trước khóa; DR-02 so sánh chặn tăng S với yêu cầu chốt lại T | CHỜ ORD-Q06/13 |
| E6-RV-04 / High | Summary trả version nhưng request gọi summaryVersion; persistence token chưa mô tả | Làm rõ mapping và phạm vi token; thêm mô tả kỹ thuật đề xuất, không giả orders.version đủ | ĐÃ LÀM RÕ TÀI LIỆU; persistence còn chờ |
| E6-RV-05 / High | states.md trước review dùng “Phát hành kế hoạch” làm trigger IN_PRODUCTION, trong khi phần cuối chờ ORD-Q14 | Phân biệt publish/ack/start; sửa trigger thành sự kiện vận hành chờ chốt, không mở API start | ĐÃ SỬA MÂU THUẪN TÀI LIỆU; ORD-Q14 vẫn mở |
| E6-RV-06 / High | PlanSummary chỉ sourceOrderCount; không liệt kê nguồn còn thiếu | Có thể báo đủ bếp khi còn điểm chưa khóa; DR-04 yêu cầu định nghĩa tập nguồn dự kiến | CHỜ ORD-Q07/13/14 |
| E6-RV-07 / Medium | Delta ERD gốc unique(revision,dish), data dictionary dùng recipe/portion | Chốt tài liệu delta theo khóa có recipe/portion để không gộp định lượng; không đổi DBML | ĐÃ ĐỒNG BỘ ĐỀ XUẤT; ORD-Q10/O-02 vẫn mở |
| E6-RV-08 / Medium | Wireframe thiếu default rồi bấm lại lock tạo thành công; hướng dẫn chưa chỉ rõ đã giả định quyền xử lý sau hạn | Ghi rõ đây là giả lập remediation đã được phép, không phải quyền gia hạn được duyệt | ĐÃ GHI GIỚI HẠN DEMO; ORD-Q07 vẫn mở |

## Bộ ca review bổ sung

[decision-review-cases.md](../test/decision-review-cases.md) chứa8ca, tách khỏi57ca hiện có để không thay mẫu số kiểm trước. Các ca đều BLOCKED bởi quyết định tương ứng hoặc chưa có môi trường; Actual/Evidence chưa có. Không gán PASS cho phát hiện được sửa bằng văn bản.

## Kết quả đối với schema/API

Chưa đủ điều kiện freeze. Identity binding, coordinator allocation, summary concurrency token, plan completeness/ack và phục hồi sau hạn cần quyết định trước DDL/hợp đồng cuối. Giữ26endpoint/2port và65bảng; không thêm endpoint ngầm hoặc migration. Một khách có danh sách người ăn không tự chứng minh đã có đủ mã định danh/đồng bộ nghỉ việc/đổi điểm.

## Rà tiếp phần độc lập ngày 11/11/2026

RV01: bổ sung dependency provisioning, chưa chốt identity/scope. RV02/03: giữ nguyên policy mở, không chọn expected. RV04: mapping và thứ tự replay được làm rõ, persistence chưa duyệt. RV05: sửa thêm SRS/UC hứa plan v1 ngay sau lock, tách PENDING; quyền publish/ack/start vẫn mở. RV06: có mô hình E/I/M/X để review, nguồn kỳ vọng/policy publish chưa chốt. RV07: chỉ ra gap role/unit khi so delta, chưa duyệt quy đổi/DDL. RV08: bổ sung phân biệt retry và sửa nguồn sau hạn, quyền remediation chưa chốt. **0/8 finding được xác nhận đóng**.

[Mapping](../api/data-mapping.md) · [Lifecycle](../srs/lock-plan-review.md) · [12ca invariant](../test/invariant-cases.md). Đây là bổ sung kiểm thiết kế, không thay8ca DR đang BLOCKED.

## Review contract tiếp nối ngày 11/11/2026

RV04/05/07 được bổ sung [delta contract](../api/delta-contract-review.md) và [evidence protocol](../test/evidence-protocol.md): sửa alias tài liệu; payload ambiguous, role/unit, READY và persistence còn gap.0/8finding đóng;12INV sửa mã tham chiếu chuẩn, trạng thái giữ nguyên.
