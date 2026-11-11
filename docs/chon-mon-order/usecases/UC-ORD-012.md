---
id: DOC-E6-USECASES-UC-ORD-012
title: UC-ORD-012 — Đề nghị và duyệt thay đổi sau khóa
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-012 — Đề nghị và duyệt thay đổi sau khóa

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-012 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-041 / P0; FR-ORD-CHG-001; US-E6-012; API-ORD-005, API-ORD-021, API-ORD-022; UI-ORD-10.
- **Actor chính:** Người đặt tổng/nội bộ có quyền tạo đề nghị; người duyệt được chỉ định khác người tạo/sửa cuối. Vai trò/ngưỡng cụ thể chờ O-06/Q-16/ORD-Q08; AUTH kiểm quyền từng thao tác.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** Người có quyền gửi đề nghị thay đổi; sau đó người duyệt thực hiện quyết định riêng khi đề nghị đủ điều kiện.
- **Tiền điều kiện:** order LOCKED rev1; ngưỡng và người duyệt đã chốt. Scope và trạng thái nguồn hợp lệ. Luồng chính có điều kiện vào Q-16, O-06, ORD-Q08; chưa xác nhận thì chỉ review, không bật production.
- **Bảo đảm tối thiểu:** lỗi không ghi một phần, không xóa lịch sử, không cấp thêm quyền; không lộ dữ liệu ngoài phạm vi.
- **Hậu điều kiện thành công:** Tạo đề nghị chỉ trả Change, chưa đổi order revision. APPROVED hợp lệ mới tạo revision/outbox, giữ bản cũ; REJECTED không tạo revision. Việc bếp nhận delta đúng revision cần evidence riêng, không suy từ response duyệt.

## Luồng chính

1. Actor mở UI-ORD-10; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Người đề nghị gửi ChangeInput/API-ORD-005 theo baseline xác định; người duyệt đọc danh sách bằng API-ORD-021, rồi gửi DecisionInput/API-ORD-022 với version đề nghị và baseOrderRevisionId.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Không sửa trực tiếp snapshot khóa. Đề nghị có delta +/-; đánh giá ngưỡng theo Q-16; duyệt khác người tạo/sửa cuối; nếu được duyệt tạo version mới và thông báo bếp. Không tự sửa số đã giao/đối soát của E7.
4. Kiểm separation và baseline lúc quyết định. APPROVED tạo revision/outbox theo thiết kế nguyên tử; REJECTED không đổi order revision. Worker phát sinh kế hoạch riêng; response duyệt chưa chứng minh bếp đã nhận.
5. Hệ thống trả change request và revision nếu duyệt; UI chỉ xác nhận kết quả ghi theo response DTO của mutation đã commit; không áp điều này cho GET. Audit theo transaction thiết kế; không tự thêm receipt endpoint.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given đề nghị PENDING do U tạo; When U tự duyệt; Then 403 ERR-ORD-403-01; order vẫn rev1.
- **3a — biên/đồng thời:** Given đề nghị dựa rev1 nhưng hiện hành rev2; When duyệt đề nghị cũ; Then 409 ERR-ORD-409-01; không áp delta lên sai baseline.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi mutation:** chưa xác định kết quả thì giữ cùng Idempotency-Key/body để replay theo contract và quyền hiện tại; đọc resource bằng GET đã có nếu đủ ID/quyền. Không tự tạo endpoint tra receipt hoặc suy requestId là bằng chứng commit. Secret QR không được phát lại trong replay.
- **4b — version hoặc trạng thái đổi khi ghi:** ERR-ORD-409-01 theo mutation tương ứng; tải lại nguồn hợp lệ, hiển thị khác biệt trước thao tác mới. Không ghi đè hoặc tự đặt version tạo mới ở nhánh chưa chốt.
- **4c — phụ thuộc gián đoạn khi ghi:** ERR-ORD-503-01; chưa xác định commit thì xử lý như 4a, không báo thất bại/thành công chắc chắn. requestId chỉ phục vụ correlation.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: order_change_requests,order_revisions,approvals (delta/existing). Bộ ba AC: AC-E6-012-1, AC-E6-012-2, AC-E6-012-3; test: TC-E6-012-1, TC-E6-012-2, TC-E6-012-3. Gate Q-16, O-06, ORD-Q08 giữ CHỜ XÁC NHẬN.

## Nhánh consistency bổ sung

Áp dụng [mapping token/replay](../api/data-mapping.md) và [guard/lifecycle](../srs/lock-plan-review.md). Mất phản hồi đối soát cùng key/body; không coi requestId là endpoint tra cứu đã có. Lock thành công có thể chưa có plan; đọc plan không ack hoặc start-production. Policy còn mở giữ BLOCKED.

## Nhánh baseline không xác định được dòng

Nếu dishId trong deltaByDish ánh xạ0hoặc nhiều dòng baseline, không chọn recipe hiện hành/dòng đầu và không tự phân bổ delta. Xử lý theo [ranh giới contract](../api/delta-contract-review.md); workflow thêm món hoặc chọn dòng cần thiết kế được review trước ghi. Approve chỉ dùng baseline đã xác định, kiểm lại version/quyền; không báo thành công khi chưa có commit. Không thêm API hoặc tự mở policy ORD-Q08/10.

## Ranh giới thao tác đọc

API-ORD-021 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-05, E6-CG-07 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
