---
id: DOC-E6-USECASES-UC-ORD-013
title: UC-ORD-013 — Điều phối nhập hộ
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-013 — Điều phối nhập hộ

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-013 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-042 / P0; FR-ORD-PXY-001; US-E6-013; API-ORD-003, API-ORD-004; UI-ORD-11.
- **Actor chính:** Dinh dưỡng viên. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason.
- **Tiền điều kiện:** DDV được giao A có chứng cứ synthetic điện thoại. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q06; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân.

## Luồng chính

1. Actor mở UI-ORD-11; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Đọc Summary qua API-ORD-003; gửi SubmissionInput qua API-ORD-004 với version của order và summaryVersion riêng. Nhập hộ phải có source/evidenceRef/reason theo quyền; tên field theo API, không lấy token Summary làm orders.version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Ghi nguồn ZALO/PHONE theo quyền, người nhập thay và bằng chứng; không gửi Zalo. Áp cùng version/deadline/định mức; không tự ghi đè lựa chọn cá nhân.
4. Hệ thống thực hiện nhập hộ total, coordinatorLines,source PHONE,evidenceRef,reason; kết quả theo điều kiện review: order ghi người thao tác, nguồn và bằng chứng; giữ lựa chọn cá nhân.
5. Hệ thống trả order có nguồn nhập hộ; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given người ăn tự chọn có phiên hợp lệ; When gửi source ZALO để giả vai DDV; Then 403 ERR-ORD-403-01; không ghi order.
- **3a — biên/đồng thời:** Given người đặt tổng và DDV cùng đọc version 1; When cả hai gửi tổng; Then một commit version 2; bên sau 409; không ghi đè mù.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: orders,order_dish_lines,files,audit_logs. Bộ ba AC: AC-E6-013-1, AC-E6-013-2, AC-E6-013-3; test: TC-E6-013-1, TC-E6-013-2, TC-E6-013-3. Gate ORD-Q06 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-003 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-03, E6-CG-04 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
