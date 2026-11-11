# Bàn giao E6 — phần độc lập với policy mở

11/11/2026 · Draft BA; không backend/migration/E7–E13. Mốc bổ sung của [handoff trước](handoff.md), giữ nguyên bản cũ. [Preview](../preview.html) · [Báo cáo kiểm/file thay đổi](../validation/independent-report.md).

Đã sửa SRS/UC/sequence còn hứa plan v1 ngay khi khóa; kết quả khóa là revision/outbox, plan có thể pending. [Mapping](../api/data-mapping.md) phân biệt summary/selection/order version và order/plan revision, replay trước kiểm stale đối với receipt đã commit, mất phản hồi và gap tra requestId. [Lifecycle](../srs/lock-plan-review.md) có actor, nguồn, guard, lỗi, dữ liệu, tiêu chí kiểm cho thiếu nguồn/ngoại lệ/completeness/publish/ack/start. [Dependency](dependencies.md) làm rõ tạo account không đồng nghĩa cấp quyền E6 và customer master chưa có contract.

[12ca INV](../test/invariant-cases.md) có truy vết tới AC gốc; tất cả NOT RUN, không tăng57AC. [Fixture/checklist/profile1000CCU](../test/fixtures/README.md) hoàn toàn synthetic; chưa chạy tải hoặc pilot2khách/2tuần. Tổng99mô tả ca có overlap, không phải99mục tiêu độc lập. Bộ57ca vẫn29NOT RUN/28BLOCKED;8DR giữ BLOCKED;0test backend.

## Chặn và phần tiếp theo

E6-EVID-001/002 giữ nguyên; không hỏi lại hoặc chọn phạm vi một/nhiều khách, C→S, xử lý vượt T.0/8finding đã xác nhận đóng;17/19capability có thiết kế điều kiện,2gate O-03;40/78feature toàn sản phẩm có thiết kế nháp. Persistence, identity, nguồn lịch hiệu lực, quyền ngoại lệ/publish/ack/start và quy đổi vẫn cần review/decision, không freeze schema/API.

Tiếp tục độc lập: rà alias tên cột trong ERD so từ điển; phân rã ChangeInput.deltaByDish khi có nhiều recipe/portion mà không tự đổi catalog; rà test/UI gốc còn assumption về publish/completeness; chuẩn bị bảng tiêu chí evidence cho adapter/receipt/manifest. Khi có quyết định mới thì cập nhật chuỗi FR→UC→API/data/UI→AC/test, giữ mẫu số và trạng thái tách biệt. Không chạy script sinh build/extend/api/finalize, không mở CRM E10.
