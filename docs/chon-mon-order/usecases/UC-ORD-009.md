---
id: DOC-E6-USECASES-UC-ORD-009
title: UC-ORD-009 — Chốt tổng suất và phân bổ
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-009 — Chốt tổng suất và phân bổ

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-009 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-038 / P0; FR-ORD-SUB-001; US-E6-009; API-ORD-003, API-ORD-004, API-ORD-019; UI-ORD-08.
- **Actor chính:** Người đặt tổng. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** gửi tổng.
- **Tiền điều kiện:** synthetic S=60,C=10,T=100 và ORD-Q06 đã duyệt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q06; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa.

## Luồng chính

1. Actor mở UI-ORD-08; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Đọc Summary qua API-ORD-003; gửi SubmissionInput qua API-ORD-004 với version của order và summaryVersion riêng. Nhập hộ phải có source/evidenceRef/reason theo quyền; tên field theo API, không lấy token Summary làm orders.version.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Tách số tự chọn và số nhập thêm cho người chưa chọn. Đề xuất T>=S+C, dư T-S-C gán mặc định lúc khóa; T<S+C trả xung đột cần xử lý tường minh, không xóa lựa chọn cá nhân tự động.
4. Hệ thống thực hiện gửi tổng; kết quả theo điều kiện review: SUBMITTED; còn 30 suất chưa phân bổ; chưa gán default trước khóa.
5. Hệ thống trả order SUBMITTED và breakdown; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given synthetic S=60,C=10,T=65; When gửi tổng; Then đề xuất 422 ERR-ORD-422-02; không xóa 5 lựa chọn; chờ ORD-Q06.
- **3a — biên/đồng thời:** Given synthetic S=60,C=10,T=70; When gửi tổng rồi khóa đủ điều kiện; Then D=0; không tạo dòng default ảo.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: orders,order_dish_lines,selection_counters. Bộ ba AC: AC-E6-009-1, AC-E6-009-2, AC-E6-009-3; test: TC-E6-009-1, TC-E6-009-2, TC-E6-009-3. Gate ORD-Q06 giữ CHỜ XÁC NHẬN.

## Nhánh consistency bổ sung

Áp dụng [mapping token/replay](../api/data-mapping.md) và [guard/lifecycle](../srs/lock-plan-review.md). Mất phản hồi đối soát cùng key/body; không coi requestId là endpoint tra cứu đã có. Lock thành công có thể chưa có plan; đọc plan không ack hoặc start-production. Policy còn mở giữ BLOCKED.

## Ranh giới thao tác đọc

API-ORD-003, API-ORD-019 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-03, E6-CG-04 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
