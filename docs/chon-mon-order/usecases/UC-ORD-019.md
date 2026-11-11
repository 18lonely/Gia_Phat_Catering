---
id: DOC-E6-USECASES-UC-ORD-019
title: UC-ORD-019 — Đọc kế hoạch sản xuất phiên bản
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-019 — Đọc kế hoạch sản xuất phiên bản

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-019 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-048 / P0; FR-PLAN-MEAL-001; US-E6-019; API-ORD-020, API-ORD-025; UI-ORD-13.
- **Actor chính:** Bếp trưởng/quản lý cơ sở có quyền đọc scope bếp. Worker tạo plan là producer độc lập từ event revision bền vững, không do GET kích hoạt.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Bếp yêu cầu danh sách hoặc chi tiết một revision kế hoạch trên UI-ORD-13 qua GET API-ORD-020/025.
- **Tiền điều kiện:** Phiên bếp và scope hợp lệ. Để đọc chi tiết thành công, plan/revision phải tồn tại và được phép xem theo contract; lock order không bảo đảm plan đã tạo. Current/visibility và quy đổi ORD-Q10/14 còn mở.
- **Bảo đảm tối thiểu:** GET không thay đổi dữ liệu nghiệp vụ, không lộ dữ liệu ngoài scope; lỗi/timeout không thành kết quả rỗng hoặc số0 giả. Log truy cập an toàn không là biên nhận ghi nghiệp vụ.
- **Hậu điều kiện thành công:** Bếp nhận bản kế hoạch được phép xem với plan revision và nguồn order revisions; không tạo/tăng revision, không publish/ack/start-production. Ví dụ synthetic hai nguồn MAIN A=60+40 cho tổng100 chỉ khi producer đã tạo đúng snapshot.

## Luồng chính

1. Actor mở UI-ORD-13; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Bếp gửi kitchenId/date/shift cho danh sách hoặc planId/revisionNo cho chi tiết theo API; không gửi orderRevisionId để yêu cầu tổng hợp.
3. Authorize scope bếp và revision thuộc plan; đọc snapshot producer đã tạo. Nguồn/manifest thiếu phải thể hiện theo thiết kế hiện có, không tự coi COMPLETE; current/visibility còn E6-CG-06.
4. Trả snapshot và các source revisions được phép đọc. Ví dụ synthetic MAIN A=100 từ60+40 là kiểm dữ liệu producer đã chuẩn bị, không phép cộng làm phát sinh plan trong GET; role/unit còn ORD-Q10.
5. UI hiển thị dữ liệu đọc và revision; không thông báo đã ghi/đã nhận kế hoạch thay cho ack, không chuyển IN_PRODUCTION. Không cần receipt hoặc commit nghiệp vụ cho GET.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given bếp K1 yêu cầu kế hoạch K2; When GET theo id K2; Then 404 ERR-ORD-404-01; không lộ tổng K2.
- **3a — producer riêng/biên liên thông:** nguồn synthetic rev1→rev2 tăng A5 được worker xử lý trước GET kế tiếp; producer không cộng hai revision cùng order, plan cũ bất biến. Nhánh này kiểm producer+read, không lệnh tạo kế hoạch từ bếp.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi GET:** có thể đọc lại với kiểm quyền/scope hiện tại; không cần Idempotency-Key hoặc đối soát receipt ghi; không tự chốt retry limits.
- **4b — nguồn/version đổi:** đọc lại theo contract query hiện có, hiển thị phiên bản nguồn của kết quả; không suy stale-write409 cho GET. Visibility/current/freshness còn gap, không tự chọn policy.
- **4c — phụ thuộc gián đoạn:** ERR-ORD-503-01 theo ma trận lỗi; không giả dữ liệu cũ là hiện hành hoặc thiếu dữ liệu là0. requestId chỉ là correlation, không chứng minh commit.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: production_plan_revisions,order_revisions (delta). Bộ ba AC: AC-E6-019-1, AC-E6-019-2, AC-E6-019-3; test: TC-E6-019-1, TC-E6-019-2, TC-E6-019-3. Gate ORD-Q10 giữ CHỜ XÁC NHẬN.

## Nhánh consistency bổ sung

Áp dụng [mapping token/replay](../api/data-mapping.md) và [guard/lifecycle](../srs/lock-plan-review.md). GET mất phản hồi chỉ đọc lại; producer đối soát event nguồn riêng; không coi requestId là endpoint tra cứu đã có. Lock thành công có thể chưa có plan; đọc plan không ack hoặc start-production. Policy còn mở giữ BLOCKED.

## Ranh giới thao tác đọc

API-ORD-020, API-ORD-025 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-06, E6-CG-07 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
