---
id: DOC-E7-USERSTORIES-BACKLOG-MD
title: Backlog E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Backlog E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| Story | FR | UC | Story | Ưu tiên | Phụ thuộc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| US-DLV-001 | FR-DLV-NOTE-001 | UC-DLV-001 | Là Bếp trưởng / quản lý cơ sở, tôi muốn lập phiếu giao nhận để phiếu chờ khách xác nhận. | P0 | E6-CG-05/06/08; E7-Q02 |
| US-DLV-002 | FR-DLV-ACK-001 | UC-DLV-002 | Là Đại diện khách được xác minh, tôi muốn xác nhận số nhận qua link để xác nhận nhận hoặc chênh lệch. | P0 | E6-CG-01/08; E7-Q01; Q-13 |
| US-DLV-003 | FR-DLV-DIFF-001 | UC-DLV-003 | Là Dinh dưỡng viên / vận hành được cấp quyền, tôi muốn lập biên bản chênh lệch để biên bản có version, liên kết phiếu. | P0 | E7-Q02; E6-CG-08 |
| US-DLV-004 | FR-DLV-RES-001 | UC-DLV-004 | Là Vận hành được cấp quyền, tôi muốn ghi thỏa thuận xử lý chênh lệch để thỏa thuận và nguồn số tính tiền. | P0 | E7-Q02/03; CK-Q07–09 khi liên quan CK |
| US-FIN-005 | FR-FIN-REV-001 | UC-FIN-005 | Là Kế toán doanh thu, tôi muốn tính doanh thu từ số tính tiền để bản tính nháp có provenance. | P0 | E7-Q03/04; Q-13; E6-CG-04/05/07 |
| US-FIN-006 | FR-FIN-VIEW-001 | UC-FIN-006 | Là Kế toán doanh thu, tôi muốn tra cứu doanh thu và nguồn để danh sách, nguồn và tổng có nhãn đủ/thiếu. | P0 | E7-Q04/08; E6-CG-08 |
| US-FIN-007 | FR-FIN-REC-001 | UC-FIN-007 | Là Kế toán doanh thu, tôi muốn lập kỳ đối soát để kỳ nháp và danh sách chặn. | P0 | E7-Q05; Q-13; E6-CG-08 |
| US-FIN-008 | FR-FIN-AGRE-001 | UC-FIN-008 | Là Kế toán và đại diện khách, tôi muốn ghi nhận thống nhất đối soát để kỳ thống nhất có bằng chứng. | P0 | E7-Q05; Q-13; E6-CG-01/08 |
| US-FIN-009 | FR-FIN-RCPT-001 | UC-FIN-009 | Là Kế toán doanh thu, tôi muốn ghi nhận thu tiền để khoản thu và còn phải thu riêng. | P0 | E7-Q06; E7-Q05 về thu sau khóa |
| US-FIN-010 | FR-FIN-LOCK-001 | UC-FIN-010 | Là Kế toán doanh thu, tôi muốn khóa kỳ đối soát để kỳ locked và audit. | P0 | E7-Q05; Q-13 |
| US-FIN-011 | FR-FIN-RREQ-001 | UC-FIN-011 | Là Kế toán doanh thu, tôi muốn đề nghị mở lại kỳ để yêu cầu chờ giám đốc, kỳ vẫn khóa. | P0 | E7-Q05; O-06 về ủy quyền giữ mở |
| US-FIN-012 | FR-FIN-RDEC-001 | UC-FIN-012 | Là Giám đốc, tôi muốn duyệt hoặc từ chối mở lại kỳ để quyết định; kỳ reopened hoặc locked. | P0 | E7-Q05; O-06 không tự cấp người thay |
| US-FIN-013 | FR-FIN-MISA-001 | UC-FIN-013 | Là Kế toán doanh thu, tôi muốn chuẩn bị và yêu cầu xuất misa để yêu cầu xuất; file chỉ sau mapping được duyệt. | P0 | E7-Q07/08; E7-Q05 về kỳ được phép xuất |

13 story nháp, chưa sprint-ready: I/E/T của INVEST phụ thuộc policy/contract/dữ liệu/môi trường; N/V có mô tả, S cần refinement. Không gán story point/ngày/người phụ trách. [AC](acceptance-criteria.md) · [RTM](../test/traceability.md).
