---
id: DOC-E6-USECASES-UC-ORD-006
title: "UC-ORD-006: Đặt định mức công ty"
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-006: Đặt định mức công ty

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-006 / Sea (mục tiêu nghiệp vụ).
- **Truy vết:** FEAT-035 / P0; FR-ORD-QTA-001; US-E6-006; API-ORD-015, API-ORD-016; UI-ORD-05.
- **Actor chính:** Người đặt tổng. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** người đặt tổng lưu định mức chung.
- **Tiền điều kiện:** loại suất đã duyệt và policy hiệu lực đã xác nhận. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q04; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người.

## Luồng chính

1. Actor mở UI-ORD-05; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,mealTypeId,effectiveFrom,version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Định mức chung theo D-21, giá và cơ cấu có hiệu lực; không người ăn tự trả chênh. Ai duyệt/thời điểm áp dụng khi đang chọn chờ ORD-Q04; thiếu định mức chặn chọn.
4. Hệ thống thực hiện người đặt tổng lưu định mức chung; kết quả theo điều kiện review: version định mức mới tham chiếu loại suất, giá và cơ cấu; không tạo giá riêng theo người.
5. Hệ thống trả quota version; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a. Đầu vào/quyền nghiệp vụ:** Given chưa có định mức hiệu lực; When người ăn chọn món; Then 422 ERR-ORD-422-01; không ghi lựa chọn.
- **3a. Biên/đồng thời:** Given đã có lựa chọn theo quota v1; When lưu quota v2 giữa ngày; Then không âm thầm tính lại v1; xử lý theo ORD-Q04.
- **3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: customer_quotas,meal_types,dish_prices. Bộ ba AC: AC-E6-006-1, AC-E6-006-2, AC-E6-006-3; test: TC-E6-006-1, TC-E6-006-2, TC-E6-006-3. Gate ORD-Q04 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-015 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC ngày 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-11 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
