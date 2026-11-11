---
id: DOC-E6-USECASES-UC-ORD-008
title: UC-ORD-008 — Gửi lựa chọn cả tuần
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-008 — Gửi lựa chọn cả tuần

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-008 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-037 / P1; FR-ORD-WEEK-001; US-E6-008; API-ORD-018; UI-ORD-07.
- **Actor chính:** Người ăn có tài khoản. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** gửi lựa chọn tuần kèm version từng ngày.
- **Tiền điều kiện:** tài khoản có 5 ngày công bố còn mở, ORD-Q05 đã chốt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q05; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** không xóa lịch sử, không cấp thêm quyền, không lộ dữ liệu ngoài scope; không báo thành công cả tuần khi có ngày lỗi. Atomic toàn tuần hay partial theo ngày chờ ORD-Q05, không lấy template rollback chung để chốt policy.
- **Hậu điều kiện thành công:** trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt.

## Luồng chính

1. Actor mở UI-ORD-07; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: selections[],perDayVersion,key.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ ngày có thực đơn công bố và còn mở; QR guest không dùng. Atomic cả tuần hay kết quả từng ngày chờ ORD-Q05; không báo cả tuần thành công nếu một ngày lỗi.
4. Hệ thống thực hiện gửi lựa chọn tuần kèm version từng ngày; kết quả theo điều kiện review: trả biên nhận nêu từng ngày và kết quả toàn yêu cầu theo policy đã duyệt.
5. Hệ thống trả kết quả từng ngày có trạng thái; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given guest QR chỉ có phạm vi ngày; When gửi lựa chọn tuần; Then 403 ERR-ORD-403-01; không ghi ngày nào.
- **3a — biên/đồng thời:** Given 4 ngày hợp lệ và 1 ngày đã khóa; When gửi tuần; Then không báo thành công toàn tuần; atomic rollback hoặc partial receipt chờ ORD-Q05.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: meal_selections; delta weekly submission receipt. Bộ ba AC: AC-E6-008-1, AC-E6-008-2, AC-E6-008-3; test: TC-E6-008-1, TC-E6-008-2, TC-E6-008-3. Gate ORD-Q05 giữ CHỜ XÁC NHẬN.


## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-12 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
