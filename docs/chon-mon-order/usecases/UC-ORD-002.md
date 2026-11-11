---
id: DOC-E6-USECASES-UC-ORD-002
title: UC-ORD-002 — Đăng ký qua QR công ty
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-002 — Đăng ký qua QR công ty

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-002 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-031 / P0; FR-AUTH-QREG-001; US-E6-002; API-ORD-008; UI-ORD-02.
- **Actor chính:** Người ăn. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** xác minh và đăng ký với identity hợp lệ.
- **Tiền điều kiện:** QR A ACTIVE và identity policy đã được duyệt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q01; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** liên kết eater với tài khoản và A; không cấp quyền người đặt tổng.

## Luồng chính

1. Actor mở UI-ORD-02; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: qrToken,thông tin định danh được chốt.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: QR xác minh công ty theo D-19, không tự chứng minh duy nhất một người. Chỉ tạo/link eater sau kiểm QR ACTIVE và chính sách định danh ORD-Q01; không suy QR công khai là quyền đọc toàn công ty.
4. Hệ thống thực hiện xác minh và đăng ký với identity hợp lệ; kết quả theo điều kiện review: liên kết eater với tài khoản và A; không cấp quyền người đặt tổng.
5. Hệ thống trả user/eater đã liên kết; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given QR đã ROTATED; When đăng ký bằng token cũ; Then 401 ERR-ORD-401-01; không tạo eater.
- **3a — biên/đồng thời:** Given identity đã có trên thiết bị khác; When đăng ký lần nữa; Then kết quả theo ORD-Q01; không tuyên bố cookie ngăn trùng người.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — xung đột:** xử lý mã lỗi theo route/identity policy; không bắt người dùng cung cấp version mà RegistrationInput/QrSessionInput không có. Không tự tạo/link danh tính khác để vượt xung đột.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: customer_qr_codes,eaters,users. Bộ ba AC: AC-E6-002-1, AC-E6-002-2, AC-E6-002-3; test: TC-E6-002-1, TC-E6-002-2, TC-E6-002-3. Gate ORD-Q01 giữ CHỜ XÁC NHẬN.


## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-01 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
