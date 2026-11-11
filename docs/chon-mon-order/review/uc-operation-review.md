# Rà actor và ranh giới thao tác 19 UC E6

12/11/2026 · DOCUMENT_CLARIFIED, chỉ BA. Tiếp nối [DTO handoff](dto-handoff.md); đây là ma trận đối chiếu UC, không sổ gap mới. Trạng thái gap chỉ tại [sổ chung](contract-gap-register.md). Không có backend/UAT hoặc evidence phê duyệt policy mới.

## Phân loại và căn cứ

19/19 UC đã rà: 12 UC có lệnh ghi HTTP (8 có nhánh đọc, 4 chủ yếu ghi), 3 UC worker/port (010/011 cùng PORT-LOCK), 2 UC đọc, 2 UC gate-only. Theo dõi vận hành là nhánh đọc của 011/014, không job mới. Giữ 26 HTTP endpoint và 2 port; không thêm API tra receipt, retry job, publish, ack hoặc start-production.

[SRS](../srs/spec.md) xác định FR; [catalog](../api/endpoint-catalog.json), [API](../api/api-spec.md) và [route review](../api/route-validation-review.md) xác định phương thức/DTO. [Lifecycle](../srs/lock-plan-review.md) và [mapping](../api/data-mapping.md) xác định ranh giới transaction/producer. Các nhãn NEEDS_ATTENTION/completeness và persistence vẫn là thiết kế có điều kiện, không trạng thái backend đã triển khai.

Mỗi dòng dưới giữ FEAT/FR/US tại [RTM](../test/traceability.md); AC/TC viết `nnn-1/2/3` nghĩa ba mã AC-E6-nnn-1…3 và TC-E6-nnn-1…3 hiện có trong [57 AC](../userstories/acceptance-criteria.md) / [57 ca](../test/review-test-cases.md). Không đổi mã hoặc status để phản ánh sửa tài liệu.

| UC | Loại / actor / trigger | Contract đọc và ghi | Hậu điều kiện / điểm đã làm rõ | Đối chiếu AC/TC và gap gốc |
| :--- | :--- | :--- | :--- | :--- |
| [UC-ORD-001](../usecases/UC-ORD-001.md) | Ghi + đọc; nhân viên được quyền quản trị khách yêu cầu cấp grant | GET007; POST006 | Grant trong scope yêu cầu; ví dụ A không quyết định scope một/nhiều công ty | 001-1/2/3; CG01/02/08 |
| [UC-ORD-002](../usecases/UC-ORD-002.md) | Ghi; người ăn xác minh đăng ký | POST008 | Link sau proof; không yêu cầu version không có trong DTO; replay không cấp lại secret | 002-1/2/3; CG01 |
| [UC-ORD-003](../usecases/UC-ORD-003.md) | Ghi; người ăn qua QR mở phiên | POST009 | Phiên scoped/expiry; identity còn mở, không bắt version client | 003-1/2/3; CG01 |
| [UC-ORD-004](../usecases/UC-ORD-004.md) | Ghi + đọc; người đặt tổng xem/quay vòng/gỡ | GET010; POST011; PATCH012 | Tách list, rotate và REMOVED; GET không đổi token/status | 004-1/2/3; CG01 |
| [UC-ORD-005](../usecases/UC-ORD-005.md) | Ghi + đọc; DDV quản lý phục vụ | GET013; PUT014; POST026 | Tách tạo/sửa; không PUT upsert/customer master | 005-1/2/3; CG08 |
| [UC-ORD-006](../usecases/UC-ORD-006.md) | Ghi + đọc; người đặt tổng lưu định mức | GET015; POST016 | Quota response khác GET; hiệu lực/phê duyệt chưa chốt | 006-1/2/3; CG11 |
| [UC-ORD-007](../usecases/UC-ORD-007.md) | Ghi + đọc; người ăn xác nhận chọn/đổi | GET001/017; PUT002 | Counter nguyên tử theo thiết kế; replay là phục hồi, không bước bắt buộc happy path | 007-1/2/3; CG03/04 |
| [UC-ORD-008](../usecases/UC-ORD-008.md) | Ghi; người ăn tài khoản gửi tuần | POST018 | Receipt theo từng ngày/policy; không tự chọn atomic hay partial | 008-1/2/3; CG12 |
| [UC-ORD-009](../usecases/UC-ORD-009.md) | Ghi + đọc; người đặt tổng gửi tổng | GET003/019; POST004 | summaryVersion riêng order version; SUBMITTED không LOCKED | 009-1/2/3; CG03/04 |
| [UC-ORD-010](../usecases/UC-ORD-010.md) | Worker; scheduler đến hạn | PORT-LOCK | Gán default trong cùng giao dịch khóa 011, không job/commit thứ hai | 010-1/2/3; INV10; CG03/04/05 |
| [UC-ORD-011](../usecases/UC-ORD-011.md) | Worker + theo dõi; scheduler đến hạn, vận hành xem | PORT-LOCK; GET020 | Revision/outbox sau commit; plan có thể chưa có; service không mở UI | 011-1/2/3; INV05/06; CG04/05/06 |
| [UC-ORD-012](../usecases/UC-ORD-012.md) | Ghi + đọc; người đề nghị và người duyệt riêng | POST005; GET021; POST022 | Tạo đề nghị không tạo order revision; approve/reject khác nhau; response chưa chứng minh bếp nhận | 012-1/2/3; CG05/07 |
| [UC-ORD-013](../usecases/UC-ORD-013.md) | Ghi + đọc; DDV nhập hộ có evidence | GET003; POST004 | source/actor/bằng chứng; hai token riêng; không gửi Zalo | 013-1/2/3; CG03/04 |
| [UC-ORD-014](../usecases/UC-ORD-014.md) | Worker + theo dõi; lịch nhắc và vận hành xem | PORT-REM; GET023 | eventId/outcome; đọc không enqueue/gửi; không giả rollback được provider | 014-1/2/3; CG12 |
| [UC-ORD-015](../usecases/UC-ORD-015.md) | Ghi; người đặt tổng đổi mode | PUT024 | Không xóa lựa chọn; hiệu lực/version tạo mới còn mở | 015-1/2/3; CG12 |
| [UC-ORD-016](../usecases/UC-ORD-016.md) | Đọc; người ăn mở chi tiết | GET001 | DTO safe, thiếu nguồn khác timeout; không Calculation/receipt; đổi nguồn không tự là stale-write409 | 016-1/2/3; SYS09; CG09/10 |
| [UC-ORD-017](../usecases/UC-ORD-017.md) | Gate; người ăn mở hồ sơ | GATE-046, không HTTP | Chưa mở; không nhận profile/consent, không retry lệnh ghi | 017-1/2/3; CG14 |
| [UC-ORD-018](../usecases/UC-ORD-018.md) | Gate; người ăn mở gợi ý | GATE-047, không HTTP | Chưa mở; không suy bệnh/thu profile hoặc tạo gợi ý giả | 018-1/2/3; CG14 |
| [UC-ORD-019](../usecases/UC-ORD-019.md) | Đọc; bếp yêu cầu plan/revision | GET020/025 | Producer xử lý event trước, GET chỉ đọc; không build/publish/ack/start | 019-1/2/3; INV07/08/09/11; CG06/07 |

## Tác động và giới hạn

Sửa trực tiếp 19 UC, hai đầu vào gate sai trong SRS và hướng dẫn thực hiện test theo loại thao tác. API/AC/RTM/catalog giữ nguyên vì đã mô tả ranh giới cần dùng; các câu AC001 “chỉ có quyền A” được hiểu trong phạm vi yêu cầu, không suy scope toàn tài khoản. AC019-1/3 là producer+read: giữ ca liên thông, tách hai giai đoạn trong hướng dẫn thực hiện; không diễn giải GET thành command. Các ví dụ đều synthetic.

Không thay wireframe, schema, dữ liệu mẫu, 57 dòng ca hoặc 57 AC. 99 mô tả ca có overlap vẫn gồm 10+57+12+8+12; 57 ca là 29 NOT RUN/28 BLOCKED, 12 INV NOT RUN, 8 DR BLOCKED. Backend 0 ca. E6-EVID-001/002, scope/C→S/vượtT và Cost/O-02/O-03 giữ nguyên.

19/19 rà diễn đạt không tương đương 19/19 build-ready: 0/14 CG và 0/8 RV được xác nhận đóng. Các điều kiện đóng, owner vai trò và policy chỉ theo sổ gap chung. [Báo cáo kiểm và file thay đổi](../validation/uc-review-report.md).
