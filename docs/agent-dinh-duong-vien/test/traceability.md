---
id: DOC-E9-TEST-TRACEABILITY-MD
title: RTM E9
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# RTM E9

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

| Feature | FR | UC | Story | AC | API / port | UI | Test |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-060 | FR-AIN-SESS-001 | UC-AIN-001 | US-AIN-001 | AC-AIN-001-01→03 | API-AIN-001 | UI-AIN-01 | TC-AIN-001-01→03 |
| FEAT-060 | FR-AIN-GEN-001 | UC-AIN-002 | US-AIN-002 | AC-AIN-002-01→03 | API-AIN-002 | UI-AIN-01 | TC-AIN-002-01→03 |
| FEAT-060 | FR-AIN-CHK-001 | UC-AIN-003 | US-AIN-003 | AC-AIN-003-01→03 | API-AIN-003 | UI-AIN-02 | TC-AIN-003-01→03 |
| FEAT-061 | FR-AIN-EXPL-001 | UC-AIN-004 | US-AIN-004 | AC-AIN-004-01→03 | API-AIN-004 | UI-AIN-02 | TC-AIN-004-01→03 |
| FEAT-061 | FR-AIN-EDIT-001 | UC-AIN-005 | US-AIN-005 | AC-AIN-005-01→03 | API-AIN-005 | UI-AIN-03 | TC-AIN-005-01→03 |
| FEAT-062 | FR-AIN-SEND-001 | UC-AIN-006 | US-AIN-006 | AC-AIN-006-01→03 | API-AIN-006 | UI-AIN-04 | TC-AIN-006-01→03 |
| FEAT-062 | FR-AIN-STAT-001 | UC-AIN-007 | US-AIN-007 | AC-AIN-007-01→03 | API-AIN-007 | UI-AIN-04 | TC-AIN-007-01→03 |
| FEAT-063 (gate-only) | FR-AIN-GATE-001 | UC-AIN-008 | US-AIN-008 | AC-AIN-008-01→03 | API-AIN-008 | UI-AIN-07 | TC-AIN-008-01→03 |
| FEAT-064 | FR-AIN-LIMT-001 | UC-AIN-009 | US-AIN-009 | AC-AIN-009-01→03 | PORT-AIN-ADMISSION | UI-AIN-06 | TC-AIN-009-01→03 |
| FEAT-064 | FR-AIN-CONF-001 | UC-AIN-010 | US-AIN-010 | AC-AIN-010-01→03 | API-AIN-010 | UI-AIN-05 | TC-AIN-010-01→03 |
| FEAT-065 | FR-AIN-SAFE-001 | UC-AIN-011 | US-AIN-011 | AC-AIN-011-01→03 | PORT-AIN-TOOL-GUARD | UI-AIN-07 | TC-AIN-011-01→03 |
| FEAT-065 | FR-AIN-MED-001 | UC-AIN-012 | US-AIN-012 | AC-AIN-012-01→03 | PORT-AIN-SAFETY | UI-AIN-07 | TC-AIN-012-01→03 |
| FEAT-064 | FR-AIN-LOG-001 | UC-AIN-013 | US-AIN-013 | AC-AIN-013-01→03 | API-AIN-013 | UI-AIN-05 | TC-AIN-013-01→03 |

FR-AIN-CONF-001 còn API-AIN-014 GET cấu hình. FR-AIN-SEND-001 còn PORT-AIN-HANDOFF cho điểm nhận tối thiểu. Tất cả mã UC/story/AC/test tương ứng trong [UC](../usecases/index.md), [backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [ca](test-cases.md), [catalog](../api/endpoint-catalog.json), [UI](../ui/screens.md). FEAT-063 dòng riêng chỉ gate an toàn, không đóng góp 5 feature có thiết kế. BR/NFR test chéo tại [ca hệ thống](system-cases.md); không cộng overlap thành mục tiêu nghiệm thu độc lập.
