---
id: DOC-E7-TEST-CHECKLIST-MD
title: Checklist kiểm E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Checklist kiểm E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| Checklist | Mục kiểm | Rule/NFR | Ca thiết kế |
| :--- | :--- | :--- | :--- |
| CHK-E7-01 | Số chốt/giao/nhận/tính tiền tách; missing khác0; revision đúng | BR-E7-002/004/005 | TC-E7-001-1/3, TC-E7-002-3, TC-E7-005-1/2/3 |
| CHK-E7-02 | Quyền/scope/link/không leak | BR-E7-001; NFR-E7-001 | TC-E7-002-2, TC-E7-006-2, TC-E7-SYS-01 |
| CHK-E7-03 | VAT/invoice/CK riêng | BR-E7-006/007 | TC-E7-005-1/2, TC-E7-SYS-02 |
| CHK-E7-04 | Giao bù/giảm trừ có thỏa thuận | BR-E7-004 | TC-E7-003-1/2, TC-E7-004-1/2/3 |
| CHK-E7-05 | Thu tiền/dup/mất phản hồi | BR-E7-003/008 | TC-E7-009-1/2/3, TC-E7-SYS-03 |
| CHK-E7-06 | Khóa/reopen qua mọi đường | BR-E7-009; NFR-E7-002 | TC-E7-010-1/2/3, TC-E7-011-1/2/3, TC-E7-012-1/2/3 |
| CHK-E7-07 | MISA và nghiệm thu tháng | BR-E7-011; NFR-E7-003 | TC-E7-013-1/2/3, TC-E7-SYS-04 |
| CHK-E7-08 | Gate/hạ tầng/error/không fake evidence | BR-E7-010; NFR-E7-004/005 | TC-E7-SYS-05/06/07/08 |

Rà checklist không là test sản phẩm PASS. Các rule/error còn chung được phủ tại [system cases](system-cases.md); các FR đã truy vết [RTM](traceability.md).


## Độ phủ error matrix

| Mã lỗi | Ca phủ |
| :--- | :--- |
| ERR-E7-401-01 / 403-01 / 404-01 | TC-E7-SYS-01; TC-E7-002-2/006-2/012-2 |
| ERR-E7-409-01 | TC-E7-001-3/008-3/010-3 |
| ERR-E7-503-01 | TC-E7-SYS-05 |
| ERR-E7-500-01 | TC-E7-SYS-08 |
| ERR-DLV-422-01 | TC-E7-001-2 |
| ERR-DLV-422-02 | TC-E7-003-2/004-2 |
| ERR-FIN-422-01 | TC-E7-005-2 |
| ERR-FIN-422-02 | TC-E7-007-2/008-2/010-2/011-2 |
| ERR-FIN-422-03 | TC-E7-009-2; TC-E7-SYS-03 |
| ERR-FIN-409-02 | TC-E7-003-3/011-3 |
| ERR-FIN-422-04 | TC-E7-013-2 |
