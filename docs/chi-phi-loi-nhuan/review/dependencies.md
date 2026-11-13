---
id: DOC-E13-REVIEW-DEPENDENCIES-MD
title: Điểm nối và phụ thuộc E13
version: 0.1.1
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Điểm nối và phụ thuộc E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-01; ACC-CONF-02; XC-03; E7-Q03, E7-Q04, E13-Q12; XC-10; E13-Q08, CK-Q05, CK-Q09 |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

| Gói | Nguồn chỉ đọc | Điểm nối | Điều kiện / giới hạn |
| :--- | :--- | :--- | :--- |
| E3 | [SRS Cost](../../cost/srs/spec.md), [kế toán](../../cost/accounting/business-rules.md), [decision register](../../cost/review/decision-register.md) | Snapshot cost, dự toán, giá gồm VAT, khoản khoán | Không định nghĩa lại cost hoặc dùng dự toán như thực mua; O-01/CK/DATA-COST còn mở. |
| E7 | [SRS](../../giao-nhan-doanh-thu/srs/spec.md), [câu hỏi](../../giao-nhan-doanh-thu/review/questions.md) | Doanh thu đã đối soát, scope khách/kỳ và revision | Q-13/E7-Q03/04/05/08 chưa đóng; không tự tính thu hoặc mở lại kỳ. |
| E10 | [SRS](../../crm-ban-hang/srs/spec.md), [câu hỏi](../../crm-ban-hang/review/questions.md) | Khách/điểm/hợp đồng/giá và nguồn lịch sử | Không dùng giá hiện hành tính lại E7; E10-Q15 chưa có công thức margin; projection gửi khách không có cost/margin. |
| E11 | [SRS](../../mua-hang-san-xuat/srs/spec.md), [câu hỏi](../../mua-hang-san-xuat/review/questions.md) | Thực mua, nguồn công nợ, phân ca FR-PLAN-SHF-001 | E11-Q07 phân bổ thực mua, Q09 phân ca, Q13 contract còn mở; phân ca khác chấm công, không suy đã trả từ công nợ. |
| E12 | [SRS](../../phan-hoi-bao-cao/srs/spec.md), [câu hỏi](../../phan-hoi-bao-cao/review/questions.md) | Ranh giới chỉ số tổng hợp kèm definitionVersion/methodVersion/status/scope | E12-Q06/07/08/18 còn mở; không thay cost % bằng lợi nhuận; không mở công cụ AI. |

> Chờ E7-Q03, E7-Q04, E13-Q12: XC-03. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-03](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

## Nền và điều kiện release

[Nền SRS](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml): quyền vai trò × cơ sở, tách tạo/duyệt BR-SEC-008, audit, snapshot. 65 bảng giữ nguyên; đề xuất EXP chỉ trong từ điển. XC-01: ERD đã làm rõ theo ACC-CONF-02 tại [nghiệp vụ kế toán](../../cost/accounting/business-rules.md); cost gồm VAT phải trả. O-01 về thành phần cost khác và VAT bán ra vẫn mở.

R7/R11 và Giám đốc duyệt phương pháp: chưa có bằng chứng. Chỉ duyệt tài liệu sau này cũng không tự chứng minh R13 đạt. O-06 chưa có người thay; không tự chỉ định.

Giữ nguyên các câu đang chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp phần producer phụ thuộc các câu này.

> Chờ E13-Q08, CK-Q05, CK-Q09: XC-10. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-10](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn; không giảm số phải trả nhà cung cấp, không tự khấu trừ số khách phải trả. Chưa quyết định khoản chiết khấu đi vào lợi nhuận thế nào. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-01 (cost ≤ 52 % doanh thu) và BO-02 (≤ 3 điểm phần trăm) là mục tiêu kinh doanh, không là dung sai đối chiếu E13. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03.
