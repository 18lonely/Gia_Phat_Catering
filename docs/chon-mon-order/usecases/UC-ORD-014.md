---
id: DOC-E6-USECASES-UC-ORD-014
title: UC-ORD-014 — Nhắc người chưa chọn
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-014 — Nhắc người chưa chọn

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-014 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-043 / P1; FR-ORD-REM-001; US-E6-014; PORT-REM, API-ORD-023; UI-ORD-09.
- **Actor chính:** Scheduler khởi tạo lịch nhắc; service/worker có scope thực hiện PORT-REM. Người vận hành có quyền chỉ đọc ReminderRun trên UI-ORD-09 qua API-ORD-023.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Sự kiện nhắc tới scheduledAt theo cấu hình được duyệt; việc vận hành mở trang lịch sử không kích hoạt nhắc.
- **Tiền điều kiện:** kênh đã được duyệt, người nhận có định danh và còn đủ điều kiện. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào Q-14; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** Không gửi ngoài scope/khi kênh chưa được duyệt; không gửi trùng sự kiện đã thành công. Khi kết quả gửi chưa rõ phải đối soát, không giả rollback được thông báo đã gửi.
- **Hậu điều kiện thành công:** chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi.

## Luồng chính

1. Scheduler nhận sự kiện nhắc theo lịch, không mở UI; truyền scope,scheduledAt,eventId vào PORT-REM.
2. Worker kiểm cấu hình kênh, quyền scope và eligibility hiện tại trước gửi; giữ eventId để dedupe.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ người đủ điều kiện chưa chọn; lọc scope/dedupe; kênh ngoài Q-14 chưa chốt. Không tự gửi SMS/Zalo/email khi chưa có cấu hình và quyền.
4. Hệ thống thực hiện scheduler lập nhắc trước hạn; kết quả theo điều kiện review: chỉ nhắc người chưa chọn đúng scope; có eventId/kết quả gửi.
5. Ghi/trả ReminderRun theo outcome thực tế; việc gửi phụ thuộc kênh/policy đã duyệt. Vận hành đọc API-ORD-023; GET không enqueue/retry hoặc gửi thông báo.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given Q-14 chưa chốt hoặc thiếu cấu hình kênh; When job nhắc chạy; Then BLOCKED_CONFIGURATION; không gọi SMS/Zalo/email.
- **3a — biên/đồng thời:** Given event nhắc đã thành công; When worker nhận lại eventId; Then không gửi lần hai; đối soát kết quả không tạo thông báo trùng.
- **3b — quyền/eligibility đổi:** worker kiểm lại trước gửi và không gửi người ngoài phạm vi; người vận hành đọc lịch sử cũng phải qua kiểm quyền HTTP riêng.
- **4a — mất phản hồi worker/provider:** đối soát eventId/kết quả gửi trước retry để tránh trùng; không tự đổi eventId hoặc coi GET reminder-runs là lệnh gửi lại. Retry/retention còn Q-14/E1-Q04.
- **4b — nguồn người nhận đổi:** kiểm lại eligibility trước gửi; không dùng template stale-write409 hoặc yêu cầu người dùng gửi version cho PORT-REM.
- **4c — thiếu cấu hình/phụ thuộc gián đoạn:** phân biệt BLOCKED_CONFIGURATION với kết quả gửi chưa xác định; không tự báo SENT hoặc giả rollback provider. HTTP503 chỉ áp dụng route HTTP theo ma trận lỗi.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: notifications; delta outbox/dedupe. Bộ ba AC: AC-E6-014-1, AC-E6-014-2, AC-E6-014-3; test: TC-E6-014-1, TC-E6-014-2, TC-E6-014-3. Gate Q-14 giữ CHỜ XÁC NHẬN.


## Ranh giới thao tác đọc

API-ORD-023 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-12 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
