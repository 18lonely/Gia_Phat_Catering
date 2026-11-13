---
id: DOC-E6-USECASES-UC-ORD-004
title: "UC-ORD-004: Quản lý QR và danh sách người ăn"
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-004: Quản lý QR và danh sách người ăn

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-004 / Sea (mục tiêu nghiệp vụ).
- **Truy vết:** FEAT-033 / P0; FR-AUTH-QRM-001; US-E6-004; API-ORD-010, API-ORD-011, API-ORD-012; UI-ORD-03.
- **Actor chính:** Người đặt tổng. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Người đặt tổng xem danh sách (GET 010), yêu cầu quay vòng QR (POST 011) hoặc gỡ người ăn (PATCH 012); đây là ba thao tác riêng.
- **Tiền điều kiện:** người đặt tổng A có QR ACTIVE version hiện tại. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q02; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** GET trả danh sách trong scope, không đổi dữ liệu. Quay vòng trả token mới một lần, token cũ ROTATED; gỡ trả trạng thái REMOVED và giữ lịch sử. Tác động phiên/lựa chọn chưa khóa vẫn chờ ORD-Q02.

## Luồng chính

1. Actor mở UI-ORD-03; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Nếu chỉ xem, gọi API-ORD-010 và kết thúc bằng danh sách scoped. Nếu quay vòng, dùng QrRotationInput/API-ORD-011; nếu gỡ, dùng EaterStatusInput/API-ORD-012. Không dùng chung payload action cho cả ba route.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Đổi QR vô hiệu token cũ; gỡ người ăn không xóa lịch sử order/lựa chọn. Tác động phiên đang mở/lựa chọn trước chốt chờ ORD-Q02; quyền chỉ công ty mình.
4. Quay vòng hợp lệ: token cũ ROTATED, secret mới chỉ cấp lần đầu. Gỡ hợp lệ: trạng thái REMOVED, giữ lịch sử; tác động phiên/lựa chọn còn chờ ORD-Q02. GET không thực hiện hai thay đổi này.
5. Hệ thống trả QR/người ăn trạng thái mới; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a. Đầu vào/quyền nghiệp vụ:** Given danh sách thuộc khách B; When người đặt tổng A đọc danh sách; Then 404 ERR-ORD-404-01; không lộ tên người ăn B.
- **3a. Biên/đồng thời:** Given eater đã có order khóa; When gỡ eater; Then giữ lịch sử; tác động phiên/lựa chọn chưa khóa BLOCKED ORD-Q02.
- **3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: customer_qr_codes,eaters. Bộ ba AC: AC-E6-004-1, AC-E6-004-2, AC-E6-004-3; test: TC-E6-004-1, TC-E6-004-2, TC-E6-004-3. Gate ORD-Q02 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-010 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC ngày 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-01 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
