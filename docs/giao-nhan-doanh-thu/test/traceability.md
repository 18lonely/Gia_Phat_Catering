---
id: DOC-E7-TEST-TRACEABILITY-MD
title: RTM E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# RTM E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| Feature | FR | UC | Story | AC | API | UI | Test | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-049 | FR-DLV-NOTE-001 | [UC-DLV-001](../usecases/UC-DLV-001.md) | US-DLV-001 | AC-E7-001-1, AC-E7-001-2, AC-E7-001-3 | API-E7-001 | UI-E7-01 | TC-E7-001-1, TC-E7-001-2, TC-E7-001-3 | E6-CG-05/06/08; E7-Q02 |
| FEAT-049 | FR-DLV-ACK-001 | [UC-DLV-002](../usecases/UC-DLV-002.md) | US-DLV-002 | AC-E7-002-1, AC-E7-002-2, AC-E7-002-3 | API-E7-002 | UI-E7-02 | TC-E7-002-1, TC-E7-002-2, TC-E7-002-3 | E6-CG-01/08; E7-Q01; Q-13 |
| FEAT-050 | FR-DLV-DIFF-001 | [UC-DLV-003](../usecases/UC-DLV-003.md) | US-DLV-003 | AC-E7-003-1, AC-E7-003-2, AC-E7-003-3 | API-E7-003 | UI-E7-03 | TC-E7-003-1, TC-E7-003-2, TC-E7-003-3 | E7-Q02; E6-CG-08 |
| FEAT-050 | FR-DLV-RES-001 | [UC-DLV-004](../usecases/UC-DLV-004.md) | US-DLV-004 | AC-E7-004-1, AC-E7-004-2, AC-E7-004-3 | API-E7-004 | UI-E7-03 | TC-E7-004-1, TC-E7-004-2, TC-E7-004-3 | E7-Q02/03; CK-Q07–09 khi liên quan CK |
| FEAT-051 | FR-FIN-REV-001 | [UC-FIN-005](../usecases/UC-FIN-005.md) | US-FIN-005 | AC-E7-005-1, AC-E7-005-2, AC-E7-005-3 | API-E7-005 | UI-E7-04 | TC-E7-005-1, TC-E7-005-2, TC-E7-005-3 | E7-Q03/04; Q-13; E6-CG-04/05/07 |
| FEAT-051 | FR-FIN-VIEW-001 | [UC-FIN-006](../usecases/UC-FIN-006.md) | US-FIN-006 | AC-E7-006-1, AC-E7-006-2, AC-E7-006-3 | API-E7-006 | UI-E7-04 | TC-E7-006-1, TC-E7-006-2, TC-E7-006-3 | E7-Q04/08; E6-CG-08 |
| FEAT-052 | FR-FIN-REC-001 | [UC-FIN-007](../usecases/UC-FIN-007.md) | US-FIN-007 | AC-E7-007-1, AC-E7-007-2, AC-E7-007-3 | API-E7-007 | UI-E7-05 | TC-E7-007-1, TC-E7-007-2, TC-E7-007-3 | E7-Q05; Q-13; E6-CG-08 |
| FEAT-052 | FR-FIN-AGRE-001 | [UC-FIN-008](../usecases/UC-FIN-008.md) | US-FIN-008 | AC-E7-008-1, AC-E7-008-2, AC-E7-008-3 | API-E7-008 | UI-E7-05 | TC-E7-008-1, TC-E7-008-2, TC-E7-008-3 | E7-Q05; Q-13; E6-CG-01/08 |
| FEAT-052 | FR-FIN-RCPT-001 | [UC-FIN-009](../usecases/UC-FIN-009.md) | US-FIN-009 | AC-E7-009-1, AC-E7-009-2, AC-E7-009-3 | API-E7-009 | UI-E7-06 | TC-E7-009-1, TC-E7-009-2, TC-E7-009-3 | E7-Q06; E7-Q05 về thu sau khóa |
| FEAT-052 | FR-FIN-LOCK-001 | [UC-FIN-010](../usecases/UC-FIN-010.md) | US-FIN-010 | AC-E7-010-1, AC-E7-010-2, AC-E7-010-3 | API-E7-010 | UI-E7-05 | TC-E7-010-1, TC-E7-010-2, TC-E7-010-3 | E7-Q05; Q-13 |
| FEAT-052 | FR-FIN-RREQ-001 | [UC-FIN-011](../usecases/UC-FIN-011.md) | US-FIN-011 | AC-E7-011-1, AC-E7-011-2, AC-E7-011-3 | API-E7-011 | UI-E7-07 | TC-E7-011-1, TC-E7-011-2, TC-E7-011-3 | E7-Q05; O-06 về ủy quyền giữ mở |
| FEAT-052 | FR-FIN-RDEC-001 | [UC-FIN-012](../usecases/UC-FIN-012.md) | US-FIN-012 | AC-E7-012-1, AC-E7-012-2, AC-E7-012-3 | API-E7-012 | UI-E7-07 | TC-E7-012-1, TC-E7-012-2, TC-E7-012-3 | E7-Q05; O-06 không tự cấp người thay |
| FEAT-053 | FR-FIN-MISA-001 | [UC-FIN-013](../usecases/UC-FIN-013.md) | US-FIN-013 | AC-E7-013-1, AC-E7-013-2, AC-E7-013-3 | API-E7-013 | UI-E7-08 | TC-E7-013-1, TC-E7-013-2, TC-E7-013-3 | E7-Q07/08; E7-Q05 về kỳ được phép xuất |

13/13 FR có luồng có UC/story/3 AC/API/UI/test; 5/5 feature có thiết kế nháp có điều kiện; 0 feature E7 chỉ gate. FEAT-053 có preflight/yêu cầu xuất nhưng file mapping BLOCKED E7-Q07. Hai feature E6 FEAT-046/047 chỉ gate O-03 tính riêng. Độ phủ nháp (23 E1–E5 +17 E6 +5 E7)/78 =45/78≈57,7%; không phải BA duyệt hay tiến độ phần mềm.


## Endpoint đọc bổ sung

| API | FR / UC / story | UI | Test đọc và quyền |
| :--- | :--- | :--- | :--- |
| API-E7-014 | FR-DLV-NOTE-001 / UC-DLV-001 / US-DLV-001 | UI-E7-01 | TC-E7-001-1 (đọc sau ghi); TC-E7-SYS-01 |
| API-E7-015 | FR-DLV-ACK-001 / UC-DLV-002 / US-DLV-002 | UI-E7-02 | TC-E7-002-1/2 (đọc phiếu không xác nhận); TC-E7-SYS-01 |
| API-E7-016 | FR-DLV-DIFF-001 / UC-DLV-003 / US-DLV-003 | UI-E7-03 | TC-E7-003-1 (đọc lại biên bản); TC-E7-SYS-01 |
| API-E7-017 | FR-FIN-REC-001 / UC-FIN-007 / US-FIN-007 | UI-E7-05 | TC-E7-007-1 (đọc tập nguồn); TC-E7-SYS-01 |
| API-E7-018 | FR-FIN-MISA-001 / UC-FIN-013 / US-FIN-013 | UI-E7-08 | TC-E7-013-3 (đọc bản xuất cũ); TC-E7-SYS-01 |

Các bước producer+read cùng mã ca, không cộng ca mới; GET không tạo phiếu/bản tính/file. Read authorization và lỗi chung được kiểm theo SYS01, dữ liệu thiếu SYS05.
