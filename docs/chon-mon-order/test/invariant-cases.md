# Ca invariant E6 độc lập với lựa chọn policy

11/11/2026 ·12ca bổ sung, tất cả **NOT RUN**, Actual/Evidence: chưa có. Đây là oracle thiết kế review, không khẳng định đã có backend hoặc policy được phê duyệt. Môi trường chưa có; NOT RUN nghĩa chưa thực thi, khác BLOCKED vì chưa chọn expected nghiệp vụ. Không đổi trạng thái8ca DR hoặc57ca theo AC.

Fixture: [synthetic](fixtures/README.md). Mapping: [API/data/UI](../api/data-mapping.md), [lifecycle](../srs/lock-plan-review.md). Các ID INV là ca bổ sung tham chiếu AC gốc, không sinh thêm AC vào mẫu số57. Có overlap với SYS/DR; không cộng thành mục tiêu độc lập.

| TC | Finding → FR → UC | API/port → data → UI | AC tham chiếu | Given / When | Then | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-E6-INV-01 | E6-RV-04 → FR-ORD-SUB-001 → [UC-ORD-009](../usecases/UC-ORD-009.md) | API-ORD-003/004 → summary token → UI-ORD-08/11 | AC-E6-009-3 | summary41/order8; gửi token40 | 409-01; không đổi order/counter/token | NOT RUN |
| TC-E6-INV-02 | E6-RV-04 → FR-ORD-SEL-001 → [UC-ORD-007](../usecases/UC-ORD-007.md) | API-ORD-002 → selection/counter/summary → UI-ORD-06 | AC-E6-007-3 | Đổi món với version hợp lệ trước hạn, không C/T conflict | Counter giảm/tăng nguyên tử; summary đổi dù order version giữ nguyên | NOT RUN |
| TC-E6-INV-03 | E6-RV-04 → FR-ORD-SUB-001 → [UC-ORD-009](../usecases/UC-ORD-009.md) | API-ORD-004 → receipt → UI-ORD-08 | AC-E6-009-3 | Mất response sau commit; retry cùng key/body và token đầu vào cũ | Trả receipt cũ theo quyền hiện tại; không đánh stale như thao tác mới | NOT RUN |
| TC-E6-INV-04 | E6-RV-01 → FR-AUTH-EXT-001 → [UC-ORD-001](../usecases/UC-ORD-001.md) | API-ORD-006 → grant/receipt → UI-ORD-01 | AC-E6-001-2 | Grant đã commit; thu hồi quyền actor rồi replay cùng key | Không lộ resource ngoài quyền hiện tại; không tạo grant mới | NOT RUN |
| TC-E6-INV-05 | E6-RV-08 → FR-ORD-LOCK-001 → [UC-ORD-011](../usecases/UC-ORD-011.md) | PORT-LOCK → counter/lock outcome → UI-ORD-09 | AC-E6-011-3 | Dùng counterMismatch trước khóa | Không LOCKED/snapshot thành công giả; ghi lỗi vận hành | NOT RUN |
| TC-E6-INV-06 | E6-RV-05 → FR-ORD-LOCK-001 → [UC-ORD-011](../usecases/UC-ORD-011.md) | PORT-LOCK → revision/outbox → UI-ORD-09 | AC-E6-011-3 | Commit order rồi worker plan lỗi | Order vẫn LOCKED; plan chưa READY; retry không revision đôi | NOT RUN |
| TC-E6-INV-07 | E6-RV-06 → FR-PLAN-MEAL-001 → [UC-ORD-019](../usecases/UC-ORD-019.md) | API-ORD-020/025 → manifest → UI-ORD-13 | AC-E6-019-1 | Fixture E có3điểm; I có2, M có1 | Không trình bày đủ nguồn bằng2/2 hoặc tự publish | NOT RUN |
| TC-E6-INV-08 | E6-RV-07 → FR-PLAN-MEAL-001 → [UC-ORD-019](../usecases/UC-ORD-019.md) | API-ORD-020/025 → source revision → UI-ORD-13 | AC-E6-019-3 | A2+B1=100; thay A3=65 rồi replay A2 | Tổng105; chỉ A3+B1; bản cũ100 bất biến | NOT RUN |
| TC-E6-INV-09 | E6-RV-05 → FR-PLAN-MEAL-001 → [UC-ORD-019](../usecases/UC-ORD-019.md) | API-ORD-025 → ack/start separation → UI-ORD-13 | AC-E6-019-1 | Đọc bản đã publish khi chưa có sự kiện ack/start | GET không ghi ack hoặc chuyển IN_PRODUCTION | NOT RUN |
| TC-E6-INV-10 | E6-RV-08 → FR-ORD-DEF-001 → [UC-ORD-010](../usecases/UC-ORD-010.md) | PORT-LOCK → missing source → UI-ORD-09 | AC-E6-010-2 | total=null hoặc default thiếu; chạy lock | Không tự dùng0/danh sách làmT hoặc món đầu làm default | NOT RUN |
| TC-E6-INV-11 | E6-RV-07 → FR-PLAN-MEAL-001 → [UC-ORD-019](../usecases/UC-ORD-019.md) | API-ORD-025 → line identity → UI-ORD-13 | AC-E6-019-3 | Hai dòng cùng dish nhưng recipe/portion/unit khác | Không gộp lượng khác định lượng/đơn vị; quy đổi chưa xác định giữ gap | NOT RUN |
| TC-E6-INV-12 | E6-RV-01 → FR-AUTH-EXT-001 → [UC-ORD-001](../usecases/UC-ORD-001.md) | API-ORD-006 → account/grant → UI-ORD-01 | AC-E6-001-3 | Account có sẵn; grant thất bại, retry cùng key | Không cấp quyền rộng/xóa account để bù; không grant đôi | NOT RUN |

## Ca còn chặn không được thay bằng invariant

DR01–02 identity; DR03 C→S; DR04 vượt T; DR05 persistence token; DR06 định nghĩa nguồn; DR07 publish/ack/start; DR08 remediation sau hạn vẫn giữ BLOCKED. RV07 về quy đổi phần ăn tiếp tục mở dù không có ca DR riêng. INV chỉ kiểm tính toàn vẹn dưới tiền điều kiện nêu rõ, không xác nhận8finding đã đóng. SYS-01 tải và SYS-12 pilot vẫn BLOCKED.

## Evidence và phạm vi mở rộng review

[Bộ evidence](evidence-protocol.md) bổ sung điều kiện đối soát cho12ca hiện có, không thêm ca. INV-11 cần xem cả role/unit và cặp giảm/tăng khi recipe đổi; ambiguous deltaByDish vẫn chưa có write contract được duyệt. RV links dùng mã chuẩn E6-RV-01–08; sửa tên mã không đóng finding.
