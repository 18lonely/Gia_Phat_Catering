---
id: DOC-E11-TEST-TRACEABILITY-MD
title: "RTM E11: FR đến màn hình"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# RTM E11: FR đến màn hình

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

Mỗi FR có UC, story, 3 AC và 3 ca; API là thiết kế có điều kiện. Truy vết không chứng minh nghiệp vụ được duyệt.

| Feature | FR | UC | Story | AC | Test | API | Màn | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-074 | FR-PUR-DEM-001 | [UC-PUR-001](../usecases/UC-PUR-001.md) | US-PUR-001 | AC-PUR-001-1, AC-PUR-001-2, AC-PUR-001-3 | TC-PUR-001-1, TC-PUR-001-2, TC-PUR-001-3 | API-PUR-001 | UI-PUR-01 | E6 CG06, ORD-Q10/14; E11-Q01 |
| FEAT-074 | FR-PUR-POD-001 | [UC-PUR-002](../usecases/UC-PUR-002.md) | US-PUR-002 | AC-PUR-002-1, AC-PUR-002-2, AC-PUR-002-3 | TC-PUR-002-1, TC-PUR-002-2, TC-PUR-002-3 | API-PUR-002 | UI-PUR-02 | E11-Q01/02/13/14 |
| FEAT-074 | FR-PUR-POG-001 | [UC-PUR-003](../usecases/UC-PUR-003.md) | US-PUR-003 | AC-PUR-003-1, AC-PUR-003-2, AC-PUR-003-3 | TC-PUR-003-1, TC-PUR-003-2, TC-PUR-003-3 | API-PUR-003 | UI-PUR-02 | E11-Q02; O-06 |
| FEAT-074 | FR-PUR-LOT-001 | [UC-PUR-004](../usecases/UC-PUR-004.md) | US-PUR-004 | AC-PUR-004-1, AC-PUR-004-2, AC-PUR-004-3 | TC-PUR-004-1, TC-PUR-004-2, TC-PUR-004-3 | API-PUR-004 | UI-PUR-03 | E11-Q03 |
| FEAT-075 | FR-PUR-RCV-001 | [UC-PUR-005](../usecases/UC-PUR-005.md) | US-PUR-005 | AC-PUR-005-1, AC-PUR-005-2, AC-PUR-005-3 | TC-PUR-005-1, TC-PUR-005-2, TC-PUR-005-3 | API-PUR-005 | UI-PUR-03 | E11-Q04/13 |
| FEAT-075 | FR-PUR-DOC-001 | [UC-PUR-006](../usecases/UC-PUR-006.md) | US-PUR-006 | AC-PUR-006-1, AC-PUR-006-2, AC-PUR-006-3 | TC-PUR-006-1, TC-PUR-006-2, TC-PUR-006-3 | API-PUR-006 | UI-PUR-04 | E11-Q05/13; E1-Q01 |
| FEAT-075 | FR-PUR-APV-001 | [UC-PUR-007](../usecases/UC-PUR-007.md) | US-PUR-007 | AC-PUR-007-1, AC-PUR-007-2, AC-PUR-007-3 | TC-PUR-007-1, TC-PUR-007-2, TC-PUR-007-3 | API-PUR-007 | UI-PUR-05 | E11-Q06/04 |
| FEAT-076 | FR-COST-BUY-001 | [UC-PUR-008](../usecases/UC-PUR-008.md) | US-PUR-008 | AC-PUR-008-1, AC-PUR-008-2, AC-PUR-008-3 | TC-PUR-008-1, TC-PUR-008-2, TC-PUR-008-3 | API-PUR-008 | UI-PUR-06 | E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04 |
| FEAT-076 | FR-COST-BEX-001 | [UC-PUR-009](../usecases/UC-PUR-009.md) | US-PUR-009 | AC-PUR-009-1, AC-PUR-009-2, AC-PUR-009-3 | TC-PUR-009-1, TC-PUR-009-2, TC-PUR-009-3 | API-PUR-009 | UI-PUR-06 | E11-Q07/08/14 |
| FEAT-077 | FR-PLAN-SHF-001 | [UC-PUR-010](../usecases/UC-PUR-010.md) | US-PUR-010 | AC-PUR-010-1, AC-PUR-010-2, AC-PUR-010-3 | TC-PUR-010-1, TC-PUR-010-2, TC-PUR-010-3 | API-PUR-010 | UI-PUR-07 | E11-Q09; E6 CG06 |
| FEAT-077 | FR-PLAN-QCG-001 | [UC-PUR-011](../usecases/UC-PUR-011.md) | US-PUR-011 | AC-PUR-011-1, AC-PUR-011-2, AC-PUR-011-3 | TC-PUR-011-1, TC-PUR-011-2, TC-PUR-011-3 | API-PUR-011 | UI-PUR-08 | E11-Q10; E7-Q02; E6 CG06 |
| FEAT-077 | FR-PLAN-SMP-001 | [UC-PUR-012](../usecases/UC-PUR-012.md) | US-PUR-012 | AC-PUR-012-1, AC-PUR-012-2, AC-PUR-012-3 | TC-PUR-012-1, TC-PUR-012-2, TC-PUR-012-3 | API-PUR-012 | UI-PUR-08 | E11-Q11; E6 CG06 |
| FEAT-078 | FR-MENU-SUB-001 | [UC-PUR-013](../usecases/UC-PUR-013.md) | US-PUR-013 | AC-PUR-013-1, AC-PUR-013-2, AC-PUR-013-3 | TC-PUR-013-1, TC-PUR-013-2, TC-PUR-013-3 | API-PUR-013 | UI-PUR-09 | E11-Q12/15; O-02 |
| FEAT-078 | FR-MENU-SCK-001 | [UC-PUR-014](../usecases/UC-PUR-014.md) | US-PUR-014 | AC-PUR-014-1, AC-PUR-014-2, AC-PUR-014-3 | TC-PUR-014-1, TC-PUR-014-2, TC-PUR-014-3 | API-PUR-014 | UI-PUR-09 | DL-01; E11-Q15; O-01/O-02; CK/DATA-COST |
| FEAT-078 | FR-MENU-SGT-001 | [UC-PUR-015](../usecases/UC-PUR-015.md) | US-PUR-015 | AC-PUR-015-1, AC-PUR-015-2, AC-PUR-015-3 | TC-PUR-015-1, TC-PUR-015-2, TC-PUR-015-3 | API-PUR-015 | UI-PUR-09 | E11-Q12/13; DL-01; E6 CG05/06/07 |


[Ca hệ thống](system-cases.md) phủ NFR-PUR-001–005, NFR-COST-002 và ERR-PUR-409-11/503-11/422-99. Các lỗi FR và BR có ca riêng trong [test-cases](test-cases.md).
