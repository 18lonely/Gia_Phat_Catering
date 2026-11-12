---
id: DOC-E11-REVIEW-DEPENDENCIES-MD
title: Phụ thuộc E11 và ranh giới chưa chốt
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Phụ thuộc E11 và ranh giới chưa chốt

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

| Nguồn | Điểm nối | Giới hạn |
| :--- | :--- | :--- |
| E2 | Định lượng sống, đơn vị/quy đổi, loại bảo quản, vai trò món, chất gây dị ứng và quy tắc; cổng duyệt MENU | Nhu cầu không áp hao hụt lần hai; thay món cùng vai trò và luôn kiểm lại. DL-01/O-02 giữ chặn; không giải quyết cỡ định lượng |
| E3 | Dự toán có phiên bản, PriceInput, cost gồm VAT; NFR-COST-002 | Giữ bản dự toán; nhận hàng chưa tự cập nhật giá. CK-Q01–10, DATA-COST-Q01–06, O-01 và các câu E3 giữ mở |
| E6 | Kế hoạch theo cơ sở/ngày/ca/món và revision | CG01–14, ORD-Q01–15, E6-EVID-001/002 giữ nguyên. Không thiết kế build/publish/ack/start hay sửa order thay E6; chỉ báo thiếu nguồn |
| E7 | Điểm nối kiểm trước giao, số giao/nhận và căn cứ doanh thu | Q-13/E7-Q01–08 chưa chốt; QC không là nhận hàng của khách, công nợ NCC không là phải thu khách; không tự lấy doanh thu làm mẫu số BO-02 |
| E1 | Quyền theo cơ sở, audit, files, approvals; DBML 65 bảng | E1-Q01–05/O-06 giữ mở; file MIME JPG/PNG/WEBP/PDF ≤ 10 MB, signed link 15 phút theo nguồn; chính sách ảnh E11-Q05 chưa chọn |

Nguồn đọc: [E2](../../thuc-don-dinh-luong/srs/spec.md), [E3](../../cost/srs/spec.md), [kế toán](../../cost/accounting/business-rules.md), [PriceInput](../../cost/api/api-spec.md), [E6](../../chon-mon-order/srs/spec.md), [CG](../../chon-mon-order/review/contract-gap-register.md), [E7](../../giao-nhan-doanh-thu/srs/spec.md), [E1](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml).

Giữ chờ toàn bộ E8-Q01–12; E9-Q01–14; E10-Q01–15; O-01–O-06; CK-Q01–10; DATA-COST-Q01–06; AIO-Q01–06; NUTR-Q01–04; DL-01; E1-Q01–05. Các câu E8–E10 không là lý do mở producer mới trong E11. Không đặc tả FEAT-082/083, không mở E12/E13.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02/R11 dùng ≤ 3 điểm phần trăm, không phải sai số tính toán. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chặn O-03, không thu dữ liệu sức khỏe.
