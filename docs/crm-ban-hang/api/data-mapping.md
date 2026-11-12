---
id: DOC-E10-API-DATA-MAPPING-MD
title: Mapping API — dữ liệu — màn hình E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Mapping API — dữ liệu — màn hình E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

Đây là ánh xạ logic đề xuất, không ánh xạ vật lý đã triển khai. Trường chưa có nguồn ghi đề xuất ở [từ điển](../srs/data-dictionary.md), không sửa schema.

| API field / port | Nguồn dữ liệu / trạng thái | Màn / nhãn | Chuyển đổi và gate |
| :--- | :--- | :--- | :--- |
| customerRef, displayName, lifecycleStatus | customers.id/name/lifecycle_status/version | UI-CRM-01 / Khách hàng | ID chuỗi; quyền và master CG08; không tạo khách từ lead. |
| contacts, contactDraft | Đề xuất crm_contact_drafts; không users | UI-CRM-01 / Liên hệ | Trường/retention Q01; nháp khác dữ liệu master. |
| pointRefs, scheduleRefs | service_points, service_schedules; ngoại lệ còn thiếu | UI-CRM-04 / Lịch điểm | Ngày/ca có nguồn; Q05/06, CG05/06/08; không đo nguy cơ theo ngày lịch. |
| orders.items / PORT-CRM-ORDERS | orders; delta order_revisions nháp của E6 | UI-CRM-01 / Order và số suất | Giữ total_servings và revision/orderVersion riêng; không dùng số này thay số tính tiền. |
| revenue / PORT-CRM-REVENUE | E7 revenue calculation nháp; API-E7-006 | UI-CRM-01 / Doanh thu | Tổng cùng kỳ và trạng thái nguồn; null khác 0; Q-13/E7-Q03/04/08. |
| feedback.state | Chưa có nguồn được duyệt; E12 chưa mở | UI-CRM-01 / Phản hồi | Chỉ CHƯA CÓ NGUỒN; không dựng collection/endpoint E12. |
| intake.sourceRef/revision/hash/receiptRef | E8 lead / E9 proposal qua hai port gốc; đề xuất crm_intakes | UI-CRM-02 / Tiếp nhận | Giữ nguồn và hai loại receipt; E8-Q06/E9-Q06 chưa trả lời. |
| duplicateReview / merge / reversal | Đề xuất crm_merge_reviews/events; customers chỉ tham chiếu | UI-CRM-03 / Diff, quyết định, hoàn tác | Không chuẩn hóa tên/điện thoại thành tiêu chí mặc định; Q02/03/04. |
| riskSignal / lifecycleEvent | Đề xuất evaluation/event + lịch và nguồn order/giao nhận | UI-CRM-04 / Nguy cơ và vòng đời | Không auto-score; thiếu lịch/nguồn là UNKNOWN; Q05/06. |
| opportunity.stage / funnel | Đề xuất sale_opportunities/events | UI-CRM-05 / Phễu | Stage và cohort Q07; denominator 0 trả null, không tỷ lệ giả. |
| quote.lines.quotedPrice / salePriceBasis / vatRatePct | Đề xuất revision báo giá, tham chiếu customer_price_terms nếu phù hợp | UI-CRM-06 / Giá bán và căn cứ | Decimal string; không meal_types.price_cap_vnd; O-01/CK và Q08. |
| internalEconomics / PORT-CRM-COST | Nguồn Cost nháp theo menu/cơ sở/ngày | UI-CRM-06 / Nội bộ có quyền | Không tự tính cost/margin; Q15; không ánh xạ sang UI-CRM-07. |
| menuAttachment / PORT-CRM-MENU | menus/menu_days/menu_day_items; dishes/recipes; nguồn dinh dưỡng nếu đủ | UI-CRM-06/07 / Thực đơn đính kèm | Chụp revision/hash; lọc theo Q09; nháp E9 không tự là MENU. |
| customerQuoteProjection | Đề xuất sale_quote_publications | UI-CRM-07 / Bản khách | Allowlist, không cost/margin/note nội bộ; giữ giá bán được duyệt, không số minh họa thành thật. |
| contract / amendment / priceLinks | Đề xuất hợp đồng/phụ lục + customer_price_terms hiện có | UI-CRM-08/09 / Giá hiệu lực | Khoảng giá không chồng theo customer + mealType; Q10/11/12; không tự mở rộng theo điểm/ca. |
| priceResolution / PORT-CRM-PRICING | customer_price_terms; link hợp đồng/phụ lục đề xuất | UI-CRM-09 / Tra giá theo ngày | Trả nguồn/version, không ghi order_pricing_snapshots; consumer CG04/05/07/08/11. |
| audit / requestId / version | audit_logs và version nguồn; action mapping còn Q13 | Mọi màn có hành động | Actor server; lý do theo nền; không raw PII/cost trong log đọc rộng. |

Không mặc định giá trị chưa xác định thành 0, không chuyển đồng thành nghìn đồng hoặc ép decimal sang float. Ngày hiệu lực không lấy từ đồng hồ client. Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.
