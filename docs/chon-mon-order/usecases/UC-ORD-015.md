---
id: DOC-E6-USECASES-UC-ORD-015
title: UC-ORD-015 — Đổi chế độ chọn món
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-015 — Đổi chế độ chọn món

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-015 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-044 / P1; FR-ORD-MODE-001; US-E6-015; API-ORD-024; UI-ORD-05.
- **Actor chính:** Người đặt tổng. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** người đặt tổng tắt chọn món.
- **Tiền điều kiện:** khách chưa có lựa chọn và policy ngày hiệu lực đã duyệt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q09; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền.

## Luồng chính

1. Actor mở UI-ORD-05; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: customerId,enabled,effectiveFrom,version,reason.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Khi tắt người đặt tổng nhập cho công ty. Đã có lựa chọn xử lý thế nào/hiệu lực giữa ngày chờ ORD-Q09; không âm thầm xóa lịch sử.
4. Hệ thống thực hiện người đặt tổng tắt chọn món; kết quả theo điều kiện review: người ăn không ghi mới; người đặt tổng dùng luồng tổng/nhập thay theo quyền.
5. Hệ thống trả mode version; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given khách đã tắt chọn từ đầu ngày; When người ăn PUT trực tiếp; Then 409 ERR-ORD-409-01; không thay số suất.
- **3a — biên/đồng thời:** Given đã có 60 lựa chọn; When đề nghị tắt giữa ngày; Then giữ 60 lựa chọn và lịch sử; tác động chờ ORD-Q09.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: customers; delta choice_mode_versions. Bộ ba AC: AC-E6-015-1, AC-E6-015-2, AC-E6-015-3; test: TC-E6-015-1, TC-E6-015-2, TC-E6-015-3. Gate ORD-Q09 giữ CHỜ XÁC NHẬN.


## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-12 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
