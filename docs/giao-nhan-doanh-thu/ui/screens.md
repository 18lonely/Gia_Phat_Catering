---
id: DOC-E7-UI-SCREENS-MD
title: Màn hình và quyền E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Màn hình và quyền E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| UI | Màn hình | Dữ liệu | FR | Vai trò / gate |
| :--- | :--- | :--- | :--- | :--- |
| UI-E7-01 | Phiếu giao | Khách/điểm/ngày/ca, số chốt/giao, order/plan revision, evidence | FR-DLV-NOTE-001 | BEP_TRUONG/QL_CO_SO theo cơ sở, CG05/06/08 |
| UI-E7-02 | Xác nhận nhận | Số giao/nhận, nguồn phiếu, trạng thái link | FR-DLV-ACK-001 | Đại diện khách đủ quyền; CG01/E7-Q01 chưa chọn cơ chế |
| UI-E7-03 | Chênh lệch | Giao/nhận, bằng chứng, thỏa thuận bù/giảm trừ | FR-DLV-DIFF-001, FR-DLV-RES-001 | PER-05, chi tiết E7-Q02 |
| UI-E7-04 | Doanh thu | Số tính tiền, giá chụp, VAT/phải trả/CK riêng, dòng thiếu | FR-FIN-REV-001, FR-FIN-VIEW-001 | KT_DOANH_THU; khách không đọc CK nội bộ/cost |
| UI-E7-05 | Kỳ đối soát | Khoảng ngày/tập nguồn/version/biên bản/tổng/khóa | FR-FIN-REC-001, FR-FIN-AGRE-001, FR-FIN-LOCK-001 | KT_DOANH_THU; khách chỉ kỳ thuộc scope |
| UI-E7-06 | Thu tiền | Chứng từ/tiền nhận/đã thu/còn thu | FR-FIN-RCPT-001 | KT_DOANH_THU; đa kỳ/sửa hủy chưa mở |
| UI-E7-07 | Mở lại kỳ | Lý do/người lập-sửa cuối/quyết định/trạng thái | FR-FIN-RREQ-001, FR-FIN-RDEC-001 | KT_DOANH_THU lập; GIAM_DOC khác người lập/sửa cuối duyệt |
| UI-E7-08 | MISA | Kỳ/revision/mẫu nhập/trạng thái kiểm/yêu cầu xuất | FR-FIN-MISA-001 | KT_DOANH_THU; thiếu mẫu không tải file |

Quyền chi tiết E7-Q08 chưa cấp bằng tài liệu; server kiểm theo FR-AUTH-RBAC-001: ngoài scope404/thiếu quyền403. [Wireframe](../html-wireframe/revenue-workbench.html) có 8 màn synthetic, không backend.
