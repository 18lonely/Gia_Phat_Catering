# Backlog kế toán mở rộng

Phiên bản0.1.0 ·11/11/2026 · Draft, phụ thuộc CR-COST-2026-001.

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | 6 story,18 AC/test bổ sung thiết kế; không gộp vào45 FR Cost gốc |

Ưu tiên P0 là đề xuất bên trong extension khi được đưa vào release, không tự thêm vào R3. SP là sơ bộ3/story, đội dev phải ước lượng lại. FR-ACC-001–006 là mã yêu cầu thiết kế mới, chưa nâng thành yêu cầu baseline đã được chủ sở hữu duyệt. Các quyền mới chưa cấp; story không sẵn sàng triển khai production trước gate. [Hợp đồng](../api/accounting-contract.md), [mô hình](../../nen-tang/srs/erd.md), [wireframe](../html-wireframe/accounting-workbench.html), [CK câu hỏi](../accounting/business-rules.md).

## US-ACC-001: Chuẩn hóa giá mua

Là một kế toán mua hàng, tôi muốn nhập giá báo theo cách ghi VAT để cost dùng đúng số phải trả.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-001 / P0 / 3 |
| API | API-COST-005/006/007/012/013/014; API-ACC-001 |
| Dữ liệu | ingredient_prices |
| Màn | SCR-ACC-01 |
| Gate | Rounding giá mua; policy migration |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-001 |

## US-ACC-002: Context giá và hóa đơn

Là một kế toán được cấp quyền, tôi muốn xem điều kiện giá chụp theo đơn để không nhầm yêu cầu hóa đơn với thuế suất.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-002 / P0 / 3 |
| API | API-ACC-002 |
| Dữ liệu | order_pricing_snapshots |
| Màn | SCR-ACC-02 |
| Gate | Sale context và quyền mới |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-002 |

## US-ACC-003: Tính thử khoản riêng

Là một kế toán được cấp quyền, tôi muốn xem chiết khấu riêng trước khi ghi để kiểm số mà không thay tiền đơn.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-003 / P0 / 3 |
| API | API-ACC-003 |
| Dữ liệu | Không ghi; đọc order_pricing_snapshots |
| Màn | SCR-ACC-03 |
| Gate | CK-Q01/02/03/04/10 |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-003 |

## US-ACC-004: Lưu bản nháp khoản riêng

Là một kế toán được cấp quyền, tôi muốn lưu điều kiện chiết khấu theo đơn để review và truy lại điều kiện.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-004 / P0 / 3 |
| API | API-ACC-004/005/006 |
| Dữ liệu | order_discount_records; order_discount_events |
| Màn | SCR-ACC-03/04 |
| Gate | CK-Q04; chưa duyệt/chi trả |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-004 |

## US-ACC-005: Thỏa thuận giá nháp

Là một kế toán được cấp quyền, tôi muốn ghi cách báo giá và yêu cầu hóa đơn khách để chuẩn bị dữ liệu hợp đồng có nguồn.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-005 / P0 / 3 |
| API | API-ACC-007/008 |
| Dữ liệu | customer_price_terms |
| Màn | SCR-ACC-02 |
| Gate | Quyền terms và activation sales policy |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-005 |

## US-ACC-006: Đơn đổi cần rà lại

Là một kế toán được cấp quyền, tôi muốn biết khoản riêng chịu ảnh hưởng khi đơn đổi để không dùng nhầm số lượng cũ để chi trả.

| Trường | Nội dung |
| :--- | :--- |
| FR / ưu tiên / SP sơ bộ | FR-ACC-006 / P0 / 3 |
| API | Sự kiện nội bộ order.changed |
| Dữ liệu | order_discount_records; order_discount_events; order_pricing_snapshots |
| Màn | SCR-ACC-04 |
| Gate | CK-Q07/08/09; chỉ cơ chế đánh dấu review |
| AC/test | [AC và test](../accounting/design-tests.md), nhóm US-ACC-006 |

