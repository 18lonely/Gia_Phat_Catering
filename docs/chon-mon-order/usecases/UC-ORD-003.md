---
id: DOC-E6-USECASES-UC-ORD-003
title: "UC-ORD-003: Mở phiên QR giới hạn"
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-003: Mở phiên QR giới hạn

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-003 / Sea (mục tiêu nghiệp vụ).
- **Truy vết:** FEAT-032 / P0; FR-AUTH-QSES-001; US-E6-003; API-ORD-009; UI-ORD-02.
- **Actor chính:** Người ăn qua QR. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** mở phiên guest ngày 2026-11-16 tại điểm A1.
- **Tiền điều kiện:** QR A ACTIVE, policy định danh đã chốt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q01; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần.

## Luồng chính

1. Actor mở UI-ORD-02; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: qrToken,serviceDate,định danh phiên.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Phiên giới hạn một công ty/ngày/phạm vi; chống chọn trùng phụ thuộc định danh thật, không chỉ cookie/IP. Chưa chốt ORD-Q01 thì không tuyên bố giải quyết duplicate người.
4. Hệ thống thực hiện mở phiên guest ngày 2026-11-16 tại điểm A1; kết quả theo điều kiện review: phiên trả scope A/A1/ngày và expiresAt; không có quyền chọn tuần.
5. Hệ thống trả phiên có scope và expiry; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a. Đầu vào/quyền nghiệp vụ:** Given phiên guest thuộc A1 ngày 16; When gọi ngày 17 hoặc điểm B1; Then 404 ERR-ORD-404-01; không trả thực đơn ngoài scope.
- **3a. Biên/đồng thời:** Given phiên đã hết hạn; When gửi lựa chọn; Then 401 ERR-ORD-401-01; không tăng bộ đếm.
- **3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b. Xung đột:** xử lý mã lỗi theo route/identity policy; không bắt người dùng cung cấp version mà RegistrationInput/QrSessionInput không có. Không tự tạo/link danh tính khác để vượt xung đột.
- **4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: customer_qr_codes,eaters; delta qr_sessions. Bộ ba AC: AC-E6-003-1, AC-E6-003-2, AC-E6-003-3; test: TC-E6-003-1, TC-E6-003-2, TC-E6-003-3. Gate ORD-Q01 giữ CHỜ XÁC NHẬN.


## Kết quả rà UC ngày 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-01 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
