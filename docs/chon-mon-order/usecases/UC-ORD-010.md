---
id: DOC-E6-USECASES-UC-ORD-010
title: UC-ORD-010 — Gán món mặc định khi khóa
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-010 — Gán món mặc định khi khóa

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-010 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-039 / P0; FR-ORD-DEF-001; US-E6-010; PORT-LOCK; UI-ORD-09.
- **Actor chính:** Scheduler/service principal có quyền scope gọi PORT-LOCK; worker kế hoạch xử lý outbox riêng. Vận hành chỉ theo dõi UI-ORD-09, không đóng vai scheduler mở UI.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Sự kiện đến hạn theo clock server và cấu hình deadline có version; scheduler gọi PORT-LOCK với eventKey. UC-ORD-010 là bước gán default trong cùng lần khóa UC-ORD-011, không job ghi thứ hai.
- **Tiền điều kiện:** synthetic T=100,S=60,C=10; default A hợp lệ. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào ORD-Q06, ORD-Q07; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** D=30 cho A; MAIN tổng 100; không tạo 30 eater giả.

## Luồng chính

1. Scheduler nhận sự kiện đến hạn, resolve servicePointId/serviceDate/shift và deadlineVersion; không mở UI-ORD-09.
2. Service gọi PORT-LOCK(servicePointId,serviceDate,shift,deadlineVersion,eventKey); menu/default/quota/counter là nguồn server kiểm lại, không payload do vận hành tùy nhập.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: D-14: gán phần còn lại về default MAIN hợp lệ; không tạo người ăn giả cho suất chưa có định danh. Tổng số từ người đặt tổng, không dùng số người đăng ký làm total. Thiếu total/default thì trạng thái cần xử lý theo ORD-Q07.
4. Hệ thống thực hiện scheduler khóa; kết quả theo điều kiện review: D=30 cho A; MAIN tổng 100; không tạo 30 eater giả.
5. PORT-LOCK trả orderRevisionId/outboxId sau commit hoặc NEEDS_ATTENTION khi thiếu nguồn; không trả plan giả đã sẵn sàng. Gán default nằm trong giao dịch khóa, không commit riêng. Vận hành xem kết quả; API-ORD-020 chỉ đọc plan đã được worker tạo.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given default không thuộc MAIN ngày công bố; When scheduler khóa; Then 422 ERR-ORD-422-03; không phát hành kế hoạch.
- **3a — biên/đồng thời:** Given chưa có total; có 100 người đăng ký; When scheduler khóa; Then total vẫn chưa xác định; không tự coi T=100; xử lý ORD-Q07.
- **3b — service không đủ quyền:** dừng xử lý scope; không mượn phiên người dùng/cache để khóa. Mã ERR là lý do tham chiếu miền; port nội bộ không có HTTP status trực tiếp.
- **4a — mất kết quả job:** đối soát operation/source hash và eventKey theo mapping; retry cùng sự kiện không tạo revision/outbox đôi. eventKey không phải header Idempotency-Key HTTP; không tự thêm API tra job.
- **4b — nguồn/version đổi:** dừng khóa trên baseline cũ, ghi outcome để xử lý theo lifecycle; không tự lấy nguồn mới rồi dùng eventKey cũ. Remediation/override vẫn chờ ORD-Q07/12/O-06.
- **4c — phụ thuộc gián đoạn:** chưa biết commit thì đối soát như 4a; chưa đủ nguồn thì không LOCKED giả. Retry worker plan tách retry lock; không mở lại order đã khóa.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: order_revisions,order_revision_lines (delta). Bộ ba AC: AC-E6-010-1, AC-E6-010-2, AC-E6-010-3; test: TC-E6-010-1, TC-E6-010-2, TC-E6-010-3. Gate ORD-Q06, ORD-Q07 giữ CHỜ XÁC NHẬN.

## Nhánh consistency bổ sung

Áp dụng [mapping token/replay](../api/data-mapping.md) và [guard/lifecycle](../srs/lock-plan-review.md). Mất kết quả PORT-LOCK đối soát eventKey và source hash; không coi requestId là endpoint tra cứu đã có. Lock thành công có thể chưa có plan; đọc plan không ack hoặc start-production. Policy còn mở giữ BLOCKED.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-03, E6-CG-04, E6-CG-05 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
