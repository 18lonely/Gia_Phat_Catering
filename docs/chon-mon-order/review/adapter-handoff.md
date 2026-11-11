# Bàn giao E6 — adapter và validation route

11/11/2026 · BA draft. Tiếp nối [contract handoff](contract-handoff.md), giữ snapshot cũ. [Báo cáo kiểm/file thay đổi](../validation/adapter-report.md) · [Preview](../preview.html).

Đã đối chiếu E1/MENU/NUTR với E6: sửa mô tả success envelope chưa thống nhất; [adapter review](../api/adapter-contract-review.md) có allowlist/provenance và mapping lỗi có điều kiện. UC016 được sửa nhánh GET: không tạo Calculation/receipt ghi và không dùng retry key cho đọc. [Ma trận26route](../api/route-validation-review.md) ghi input,scope/guard,lỗi và gap. [6oracle synthetic](../test/fixtures/adapter-synthetic.json) phục vụ review, không thêm ca thực thi.

## Tiến độ và giới hạn

26/26route có dòng review validation;0/26route được kiểm thực thi trong phiên.40/78feature thiết kế nháp,17/19capability E6 có điều kiện,19/19RTM;0/8RV đóng.99mô tả ca overlap không đổi;57ca theoAC29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED;0backend/UAT/tải/pilot.26HTTP/2port,13màn,65bảng giữ nguyên. E6-EVID-001/002 và ba quyết định mở không đổi; chưa backend/migration/E7–E13.

## Còn chặn

E1-Q01 envelope; NUTR provenance/kind/stale và fallback; refresh/cache/calculation preparation và quyền service; request limits/nullability/range errors; customer/identity; các policy order/plan, O-02/O-03 và Cost giữ nguyên. Đọc tài liệu/kiểm fixture không đủ phê duyệt wire contract.

## Việc tiếp theo

Lập danh sách gap hợp đồng còn mở có owner vai trò, căn cứ, artifact bị ảnh hưởng và điều kiện đóng, tránh tiếp tục thêm lớp tài liệu trùng. Rà request/response nullability cụ thể và ma trận field required/optional cho các DTO còn thiếu; tách sửa chắc chắn khỏi đề xuất cần review. Không tự chọn defaults/limits, scope/C→S/vượtT; không hỏi lại ba câu. Chỉ đổi trạng thái khi có evidence mới. Nếu cần cập nhật mock thì kiểm UI và xem ảnh theo hướng dẫn.
