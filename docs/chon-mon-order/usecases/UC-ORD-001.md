---
id: DOC-E6-USECASES-UC-ORD-001
title: "UC-ORD-001: Cấp quyền người đặt tổng"
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-001: Cấp quyền người đặt tổng

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-001 / Sea (mục tiêu nghiệp vụ).
- **Truy vết:** FEAT-030 / P0; FR-AUTH-EXT-001; US-E6-001; API-ORD-006, API-ORD-007; UI-ORD-01.
- **Actor chính:** Nhân viên Gia Phát được cấp quyền quản trị khách/phạm vi tương ứng; không phải mọi nhân viên Gia Phát. AUTH kiểm quyền cấp vai trò.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** cấp vai trò người đặt tổng cho user U ở A.
- **Tiền điều kiện:** nhân viên được cấp quyền quản trị khách A và hợp đồng hợp lệ. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q01; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** Grant được ghi cho phạm vi A trong yêu cầu synthetic này, có audit người cấp/phạm vi; không cấp quyền nội bộ. Không kết luận tài khoản chỉ được thuộc một công ty; ORD-Q11/E6-EVID-002 còn mở.

## Luồng chính

1. Actor mở UI-ORD-01; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,userId,role,reason.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ cấp trong công ty có quyền; quyền người đặt tổng theo company/service point. Không kế thừa quyền nội bộ; log cấp/thu hồi và kiểm scope mỗi request.
4. Hệ thống thực hiện cấp vai trò người đặt tổng cho user U ở A; kết quả theo điều kiện review: grant chỉ cấp phạm vi A của yêu cầu; audit ghi người cấp và phạm vi; không kết luận scope một/nhiều công ty.
5. Hệ thống trả tài khoản công ty; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a. Đầu vào/quyền nghiệp vụ:** Given U là người đặt tổng A; When U cấp quyền nội bộ cho mình; Then 403 ERR-ORD-403-01; không thay user_roles.
- **3a. Biên/đồng thời:** Given quản trị chỉ được giao A; When gửi customerId B; Then 404 ERR-ORD-404-01; không tiết lộ B.
- **3b. Quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a. Mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b. Version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c. Phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: users,user_roles,customers. Bộ ba AC: AC-E6-001-1, AC-E6-001-2, AC-E6-001-3; test: TC-E6-001-1, TC-E6-001-2, TC-E6-001-3. Gate ORD-Q01 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-007 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC ngày 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-01, E6-CG-02, E6-CG-08 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
