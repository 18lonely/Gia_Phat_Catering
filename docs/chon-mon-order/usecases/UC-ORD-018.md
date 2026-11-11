---
id: DOC-E6-USECASES-UC-ORD-018
title: UC-ORD-018 — Giữ cổng gợi ý cá nhân
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-018 — Giữ cổng gợi ý cá nhân

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-018 / Fish — kiểm cổng.
- **Truy vết:** FEAT-047 / P1; FR-NUTR-REC-001; US-E6-018; GATE-047; UI-ORD-12.
- **Actor chính:** Người ăn có tài khoản xem trạng thái tính năng trên UI-ORD-12; không có actor thu hồ sơ hoặc chạy thuật toán trong phạm vi gate hiện hành.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** người ăn mở gợi ý.
- **Tiền điều kiện:** O-03 chưa được phê duyệt mở tính năng; GATE-046/GATE-047 là mã truy vết, không HTTP endpoint.
- **Bảo đảm tối thiểu:** Không thu thập/lưu hồ sơ sức khỏe hoặc consent ngầm; không suy bệnh từ lịch sử; không tạo recommendation/selection/order từ gate.
- **Hậu điều kiện thành công:** tính năng chưa mở; chọn món thủ công vẫn có theo quyền.

## Luồng chính

1. Người ăn mở mục tương ứng trên UI-ORD-12; hiển thị trạng thái chưa mở, không tải hồ sơ sức khỏe.
2. Không yêu cầu profile, consentVersion hoặc dữ liệu sức khỏe; không gọi API sức khỏe/gợi ý vì catalog chưa có endpoint.
3. Giữ gate O-03; các yêu cầu consent, xóa/lưu vết và thuật toán chỉ là nội dung thiết kế tương lai chờ ORD-Q15/O-03.
4. Hiển thị chưa mở tính năng; người dùng có thể về luồng chọn món thủ công theo quyền sẵn có.
5. Kết thúc ở trạng thái gate; không request ghi, receipt, commit hoặc retry mutation; không trả gợi ý giả.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given không có consent/hồ sơ hợp lệ; When yêu cầu suy bệnh từ lịch sử chọn; Then không suy diễn và không tự tạo hồ sơ.
- **3a — biên/đồng thời:** Given gợi ý tương lai được duyệt; When review hành vi áp dụng; Then phải có lựa chọn tường minh; không tự ghi selection hoặc đổi order.
- **3b — không đủ quyền truy cập UI:** dùng kiểm phiên/quyền nền nếu áp dụng; không tạo mã lỗi HTTP cho endpoint sức khỏe chưa tồn tại.
- **4a — không tải được UI:** có thể mở lại trang; không có lệnh sức khỏe để replay hoặc dùng Idempotency-Key.
- **4b — gate thay đổi trong tương lai:** chỉ thiết kế luồng mới sau evidence phê duyệt; không tự mở schema/contract trong phiên này.
- **4c — phụ thuộc chưa sẵn sàng:** giữ trạng thái chưa mở; không fallback sang thu profile/consent hoặc suy diễn bệnh.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: không thêm dữ liệu hồ sơ/gợi ý. Bộ ba AC: AC-E6-018-1, AC-E6-018-2, AC-E6-018-3; test: TC-E6-018-1, TC-E6-018-2, TC-E6-018-3. Gate O-03 giữ CHỜ XÁC NHẬN.


## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-14 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
