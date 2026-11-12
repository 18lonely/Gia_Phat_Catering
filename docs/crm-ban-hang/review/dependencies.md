---
id: DOC-E10-REVIEW-DEPENDENCIES-MD
title: Phụ thuộc E10 — chỉ nhận/đọc nguồn có điều kiện
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Phụ thuộc E10 — chỉ nhận/đọc nguồn có điều kiện

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

Tất cả API/SRS nguồn dưới là **nháp**, không hợp đồng đã cố định. Các đề xuất consumer E10 không trả lời thay câu hỏi producer. Nhánh tích hợp thực tế dưới đây đều BLOCKED cho tới khi có quyết định nguồn và review adapter; chỉ mô tả tập thông tin cần nhận, không chọn cơ chế chưa được duyệt.

| Điểm nối / chiều | Nguồn | E10 sử dụng | Câu hỏi chặn / giới hạn |
| :--- | :--- | :--- | :--- |
| PORT-PUB-LEAD-HANDOFF → E10 | [E8 API](../../website-cong-khai/api/api-spec.md), [câu hỏi](../../website-cong-khai/review/questions.md) | FR-CUS-LEAD-001; phiếu tiếp nhận và nguồn/trial an toàn | E8-Q06/07/12; E10-Q13. Không chọn nơi lưu tạm, trường liên hệ hoặc consent thay E8. |
| PORT-AIN-HANDOFF → E10 | [E9 dependencies](../../agent-dinh-duong-vien/review/dependencies.md), [API](../../agent-dinh-duong-vien/api/api-spec.md) | FR-CUS-LEAD-001; proposalRef/revision/hash, receipt riêng | E9-Q06/10/12/13. Không mặc định E10 là đầu nhận đã được duyệt; receipt không là MENU được duyệt. |
| Khách/điểm/lịch và order → hồ sơ | [E6 mapping](../../chon-mon-order/api/data-mapping.md), [sổ CG](../../chon-mon-order/review/contract-gap-register.md), [API](../../chon-mon-order/api/api-spec.md) | FR-CUS-VIEW-001/LIFE-001/RISK-001; tham chiếu lịch, order, số suất có nguồn | CG01/02/03/04/05/06/07/08/09/11; ORD-Q01–15, E6-EVID-001/002. Không xây master hoặc quyết định khóa/plan. |
| Giao/nhận/doanh thu → hồ sơ | [E7 API](../../giao-nhan-doanh-thu/api/api-spec.md), [câu hỏi](../../giao-nhan-doanh-thu/review/questions.md) | FR-CUS-VIEW-001/RISK-001; số giao, số nhận, số tính tiền tách riêng | Q-13; E7-Q01–08, đặc biệt Q02/03/04/05/08. Không tự quyết số tính tiền hoặc VAT/làm tròn. |
| MENU → báo giá | [MENU API](../../thuc-don-dinh-luong/api/api-spec.md), [SRS](../../thuc-don-dinh-luong/srs/spec.md) | FR-SALE-MENU-001; menu/recipe revision và projection được phép | O-02, DL-01, E8-Q04, E9-Q12; NUTR-Q01–04 khi kèm dinh dưỡng. Không lấy price_cap làm giá bán. |
| Cost → nội bộ báo giá | [Cost SRS](../../cost/srs/spec.md), [kế toán](../../cost/accounting/business-rules.md), [contract](../../cost/api/accounting-contract.md) | FR-SALE-QUOT-001; cost và trạng thái nguồn theo quyền nội bộ | O-01; CK-Q01–10; DATA-COST-Q01–06; E10-Q15. Không tự định nghĩa margin hoặc tính lại cost. |
| Giá E10 → E6/Cost | customer_price_terms và order_pricing_snapshots trong [schema](../../nen-tang/srs/schema.dbml) | FR-SALE-PRIC-001; đề xuất nguồn giá có hiệu lực, chưa chụp order | E10-Q11/12/13; CG04/05/07/08/11; CK. Trách nhiệm chụp của producer giữ nguyên; không ghi ngược snapshot. |
| Quyền/audit/envelope → E10 | [E1 API](../../nen-tang/api/api-spec.md), [SRS](../../nen-tang/srs/spec.md) | Mọi FR; kiểm quyền và audit bất biến | E1-Q01/02; O-06; E10-Q03/08/10/13; không lấy vai trò Giám đốc làm quyết định người duyệt. |
| Phản hồi / hỗ trợ CRM tương lai | PRD FEAT-079 và FEAT-084 thuộc E12 | Chỉ ô chưa có nguồn ở hồ sơ, không endpoint hay luồng AI | E12 chưa mở; không thu phản hồi, tóm tắt AI, nhắc việc hoặc nháp báo giá bằng AI. |
| Điều kiện release | [R10/G-Next](../../gia-phat/02-roadmap.md) | Mẫu số và bằng chứng R10 | E10-Q14; O-04; E8-Q10; BO-05/06/09 chưa có bằng chứng cổng đạt. |

E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04 đều giữ trạng thái chờ tại sổ nguồn. Không hỏi lại, tự trả lời hoặc quyết định thay.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.

Không mở rộng các điểm O-03/O-05, không đưa dữ liệu sức khỏe vào hồ sơ CRM. Các thông tin chưa có contract trả trạng thái thiếu/gate, không tạo dữ liệu giả để lấp chỗ trống.
