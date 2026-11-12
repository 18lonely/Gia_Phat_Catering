---
id: DOC-E12-REVIEW-DEPENDENCIES-MD
title: Điểm nối E12 và các gói nguồn
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Điểm nối E12 và các gói nguồn

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; không đóng câu hỏi nguồn |

| Gói | Nguồn chỉ đọc | Dữ liệu / trách nhiệm nguồn | E12 sử dụng / ranh giới | Điều kiện chưa đạt |
| :--- | :--- | :--- | :--- | :--- |
| E2 | [SRS MENU](../../thuc-don-dinh-luong/srs/spec.md) | Catalog, công thức hiệu lực, vai trò món, nhãn dị ứng, kiểm thuần FR-MENU-RUL-002, cổng duyệt MENU | FEAT-080/082/086; E12 không sửa menu | DL-01/O-02; FR-MENU-RCP-007 vẫn chặn; không mở nhiều cỡ |
| E3 | [SRS Cost](../../cost/srs/spec.md); [kế toán](../../cost/accounting/business-rules.md) | Cost % mục 3.3.2, dự toán mục 3.3.4, giá VAT, provenance và quyền cost | FEAT-081/082/083; chỉ đọc số hệ thống | O-01, CK-Q01–10, DATA-COST-Q01–06; NFR-COST-002 giữ |
| E4 | [SRS NUTR](../../dinh-duong/srs/spec.md); [câu hỏi](../../dinh-duong/review/questions.md) | Bốn chỉ số của tổ hợp suất, snapshot/nguồn, nhãn ước tính từ định lượng sống | FEAT-086/087; không tự tính ngưỡng/giá trị | NUTR-Q01–04; không dùng dung sai Cost làm dung sai dinh dưỡng |
| E5 | [SRS AIO](../../agent-noi-bo/srs/spec.md); [câu hỏi](../../agent-noi-bo/review/questions.md) | Giao quyền người dùng–dịch vụ, tool allowlist chỉ đọc, nhật ký và provenance | FEAT-082–085; không dùng apply của E5 | AIO-Q01–06; đặc biệt CANH_BAO, quyền log và adapter chưa đóng |
| E6 | [SRS order](../../chon-mon-order/srs/spec.md); [CG](../../chon-mon-order/review/contract-gap-register.md) | Lựa chọn thật, scope người ăn, nguồn menu/suất và revision có căn cứ | FEAT-079/080/083/087; không suy lựa chọn từ sản xuất hay đã ăn từ chọn | CG01–14, ORD-Q01–15, E6-EVID-001/002; không đặc tả tiếp producer |
| E7 | [SRS giao nhận/doanh thu](../../giao-nhan-doanh-thu/srs/spec.md) | Số tính tiền, giá snapshot, doanh thu/đối soát có evidence | FEAT-081/085; giao/nhận khác đã ăn của cá nhân | Q-13, E7-Q01–08; không lấy số giao làm doanh thu |
| E9 | [SRS AIN](../../agent-dinh-duong-vien/srs/spec.md); [câu hỏi](../../agent-dinh-duong-vien/review/questions.md) | Ranh giới agent khách, projection và gate FEAT-063 | Không chia sẻ quyền/cache AIO với AIN; không mở gợi ý cá nhân | E9-Q01–14; O-03/FEAT-046/047/063 giữ gate |
| E10 | [SRS CRM](../../crm-ban-hang/srs/spec.md); [epic](../../crm-ban-hang/epic-spec.md); [câu hỏi](../../crm-ban-hang/review/questions.md) | Projection đọc khách, lịch, báo giá có phiên bản; ghi chú FEAT-084 là biên của E12 | FEAT-084 chỉ đọc, nhắc việc/báo giá là nội dung nháp | E10-Q01–15; không sửa đặc tả E10 hay tạo task/quote |
| E11 | [SRS mua hàng](../../mua-hang-san-xuat/srs/spec.md); [câu hỏi](../../mua-hang-san-xuat/review/questions.md) | Nhu cầu gộp, đối chiếu thực mua và bằng chứng nguồn | FEAT-081/083; không tạo đơn mua, trừ tồn hoặc phân bổ | E11-Q01–15; BO-02 không là ngưỡng giá lệch |

Nền tảng: [SRS](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md), [schema](../../nen-tang/srs/schema.dbml); E1 giữ identity/scope/audit, BR-SEC-008/009/010 và NFR-PRIV-001/002. Schema giữ 65 bảng. E1-Q01–05 không đóng.

R12 cần R6, R7, R10, R11 xong; G-Next vẫn cần bằng chứng BO-05/06/09. Chưa có bằng chứng đạt; mở tài liệu không miễn các điều kiện này. Giữ toàn bộ E8-Q01–12, O-01–O-06, DL-01 và câu nguồn trên, không hỏi lại hoặc chọn thay.

FEAT-087 độc lập với O-03 vì không đọc eater_health_profiles, không nhận bệnh lý/chỉ số cơ thể, không suy luận và không gợi ý; chỉ sự kiện bữa đã ăn cùng snapshot suất. Chính sách identity/consent/retention/bằng chứng còn BLOCKED, nhưng không làm feature này chỉ gate. Bất kỳ mở rộng FEAT-046/047 là gate-only O-03, ngoài thiết kế hiện tại.
