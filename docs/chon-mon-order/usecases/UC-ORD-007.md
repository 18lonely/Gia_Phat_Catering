---
id: DOC-E6-USECASES-UC-ORD-007
title: UC-ORD-007 — Chọn và đổi một món chính
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-007 — Chọn và đổi một món chính

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-007 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-036 / P0; FR-ORD-SEL-001; US-E6-007; API-ORD-001, API-ORD-002, API-ORD-017; UI-ORD-06.
- **Actor chính:** Người ăn. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Người ăn xác nhận chọn hoặc đổi món; replay chỉ là nhánh phục hồi của cùng mutation, không phải thao tác bắt buộc trong luồng thành công.
- **Tiền điều kiện:** eater E chọn A version 1 trước hạn, giá tổ hợp B hợp lệ. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q01, ORD-Q04; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** version 2; A giảm 1, B tăng 1 đúng một lần.

## Luồng chính

1. Actor mở UI-ORD-06; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: menuDayId,dishId,servicePointId,date,shift,version,key.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ menu PUBLISHED, món MAIN thuộc ngày, recipe/giá hiệu lực và tổ hợp trong định mức. Identity từ phiên; unique eater+date+shift; trước deadline server; sửa counter giảm món cũ/tăng món mới cùng transaction.
4. API-ORD-002 ghi selection và counter nguyên tử theo guard. Ví dụ synthetic đổi A version1 sang B tạo version2, A giảm1/B tăng1; replay cùng key/body không ghi lần hai.
5. Hệ thống trả selection/version và tổng đúng; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given định mức synthetic 40000đ, tổ hợp 40001đ; When gửi chọn tổ hợp; Then 422 ERR-ORD-422-01; lựa chọn/counter không đổi.
- **3a — biên/đồng thời:** Given định mức synthetic 40000đ, tổ hợp đúng 40000đ và đủ cơ cấu; When gửi chọn trước hạn với version hiện tại; Then được nhận; không yêu cầu người ăn bù tiền.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: meal_selections,selection_counters,menu_days. Bộ ba AC: AC-E6-007-1, AC-E6-007-2, AC-E6-007-3; test: TC-E6-007-1, TC-E6-007-2, TC-E6-007-3. Gate ORD-Q01, ORD-Q04 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-001, API-ORD-017 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-03, E6-CG-04 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
