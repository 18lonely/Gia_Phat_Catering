---
id: DOC-E6-USECASES-UC-ORD-016
title: UC-ORD-016 — Xem thông tin món công bố
version: 0.2.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-ORD-016 — Xem thông tin món công bố

**Draft để review · cập nhật 12/11/2026 · Chưa duyệt nghiệp vụ, chưa triển khai backend/UAT.**

Mọi tên, mã, ngày phục vụ và con số trong ví dụ dưới đây là **synthetic**, không phải dữ liệu vận hành thật.

| Phiên bản | Ngày | Thay đổi |
| :--- | :--- | :--- |
| 0.2.0 | 2026-11-11 | Bổ sung chi tiết E6, giữ gate và mã gốc |
| 0.2.1 | 2026-11-12 | Phân biệt đọc, ghi, worker và gate theo catalog; giữ policy mở |

- **ID / mức:** UC-ORD-016 / Sea — mục tiêu nghiệp vụ.
- **Truy vết:** FEAT-045 / P0; FR-NUTR-DSP-001; US-E6-016; API-ORD-001; UI-ORD-06.
- **Actor chính:** Người ăn. Hỗ trợ: AUTH/SYS kiểm quyền và audit theo thao tác; nguồn/port chỉ tham gia khi được nêu trong luồng.
- **Bên quan tâm:** người ăn cần giữ đúng lựa chọn; người đặt tổng cần số suất giải thích được; bếp cần nguồn phiên bản; BA cần không che điểm mở.
- **Trigger:** người ăn mở chi tiết.
- **Tiền điều kiện:** Người ăn có phiên/quyền scope và menu công bố hợp lệ; nguồn dinh dưỡng có thể đủ hoặc thiếu. Nhánh đủ nguồn cho kết quả chính, nhánh thiếu theo 2a; provenance/freshness NUTR-Q03 còn mở.
- **Bảo đảm tối thiểu:** GET không thay đổi dữ liệu nghiệp vụ, không lộ dữ liệu ngoài scope; lỗi/timeout không thành kết quả rỗng hoặc số0 giả. Log truy cập an toàn không là biên nhận ghi nghiệp vụ.
- **Hậu điều kiện thành công:** hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính.

## Luồng chính

1. Actor mở UI-ORD-06; hệ thống tải dữ liệu và version trong phạm vi được cấp.
2. Actor cung cấp: published menu/day/dish.
3. Hệ thống kiểm kiểu, quyền, trạng thái nguồn và các điều kiện: Chỉ dữ liệu công bố: định lượng,4 chỉ số có nhãn ước tính,dị ứng và phạm vi tổ hợp; thiếu dữ liệu ghi chưa có, không điền0. DTO allowlist không có Cost/giá nhập/note nội bộ.
4. Hệ thống thực hiện người ăn mở chi tiết; kết quả theo điều kiện review: hiện định lượng sống, kcal/đạm/béo/bột đường, dị ứng và nhãn ước tính.
5. Hệ thống trả DTO món an toàn đã lọc; đây là GET, không tạo selection/Calculation hoặc biên nhận ghi. Ghi log truy cập an toàn theo nền nếu cần.

## Nhánh rẽ và ngoại lệ

- **2a — đầu vào/quyền nghiệp vụ:** Given thiếu dữ liệu dinh dưỡng một nguyên liệu; When mở tổ hợp; Then totals=null và lý do thiếu; không hiển thị 0 như kết quả thật.
- **3a — biên/đồng thời:** Given client dò field cost và id khách khác; When gọi available-meals; Then DTO chỉ allowlist; ngoài scope 404; lỗi không lộ cost/giá nhập.
- **3b — quyền bị thu hồi:** ERR-ORD-401-01/403-01/404-01 theo [ma trận lỗi](../srs/operational-rules.md); không tiếp tục bằng dữ liệu cache.
- **4a — mất phản hồi GET:** có thể đọc lại với kiểm quyền/scope hiện tại; không cần Idempotency-Key hoặc đối soát receipt ghi; không tự chốt retry limits.
- **4b — nguồn/version đổi:** đọc lại theo contract query hiện có, hiển thị phiên bản nguồn của kết quả; không suy stale-write409 cho GET. Visibility/current/freshness còn gap, không tự chọn policy.
- **4c — phụ thuộc gián đoạn:** ERR-ORD-503-01 theo ma trận lỗi; không giả dữ liệu cũ là hiện hành hoặc thiếu dữ liệu là0. requestId chỉ là correlation, không chứng minh commit.

## Quy tắc, dữ liệu và kiểm thử

[BR và nhánh vận hành](../srs/operational-rules.md), [SRS capability](../srs/spec.md), [API](../api/api-spec.md), [data dictionary](../srs/data-dictionary.md).
Dữ liệu: menu_day_items,recipes,dish_allergens,nutrition_calculations. Bộ ba AC: AC-E6-016-1, AC-E6-016-2, AC-E6-016-3; test: TC-E6-016-1, TC-E6-016-2, TC-E6-016-3. Gate NUTR-Q03 giữ CHỜ XÁC NHẬN.

## Mapping dữ liệu thiếu

Theo [adapter review](../api/adapter-contract-review.md), totals=null là nghĩa nghiệp vụ: bốn trường dinh dưỡng SafeDish đều null khi nguồn tính không đủ; missing chỉ chứa nhãn an toàn, không raw ingredientId/breakdown. Không biến timeout thành thiếu dữ liệu đã xác định; sourceVersion/kind/stale còn gap chưa freeze.

## Ranh giới thao tác đọc

API-ORD-001 là GET: actor có quyền yêu cầu query/path theo catalog, kiểm lại quyền/scope mỗi lần. Kết quả là dữ liệu đọc, không tạo receipt, commit nghiệp vụ hoặc tăng version; không dùng Idempotency-Key. Mất phản hồi có thể đọc lại, không tự chốt số lần/giãn cách retry. Nguồn đổi được trình bày theo version/nguồn trả về; không mặc định lỗi stale-write 409 chỉ vì đọc lại. Timeout không được giả thành danh sách rỗng hoặc dữ liệu đã đủ.

## Kết quả rà UC — 12/11/2026

Đối chiếu [ma trận rà 19 UC](../review/uc-operation-review.md). Gap liên quan: E6-CG-09, E6-CG-10 tại [sổ gap chung](../review/contract-gap-register.md); DOCUMENT_CLARIFIED, chưa đóng gap. Mã FR/US/AC/TC và trạng thái test giữ nguyên.
