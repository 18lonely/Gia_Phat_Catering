---
id: DOC-E8-TEST-TRACEABILITY-MD
title: RTM feature → FR → UC → story → API → UI → test
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# RTM feature → FR → UC → story → API → UI → test

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-05; E8-Q13 |


Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

| Feature | FR | UC | Story | AC | API | UI | Test | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-054 | FR-PUB-PAGE-001 | [UC-PUB-001](../usecases/UC-PUB-001.md) | US-PUB-001 | AC-PUB-001-H/E/B | API-PUB-001 | UI-PUB-01 | TC-PUB-001-H/E/B | E8-Q08 |
| FEAT-055 | FR-PUB-BLOG-001 | [UC-PUB-002](../usecases/UC-PUB-002.md) | US-PUB-002 | AC-PUB-002-H/E/B | API-PUB-002 | UI-PUB-02 | TC-PUB-002-H/E/B | E8-Q01/08 |
| FEAT-055 | FR-PUB-URLM-001 | [UC-PUB-003](../usecases/UC-PUB-003.md) | US-PUB-003 | AC-PUB-003-H/E/B | API-PUB-003 | UI-PUB-07 | TC-PUB-003-H/E/B | E8-Q01/02 |
| FEAT-055 | FR-PUB-URLR-001 | [UC-PUB-004](../usecases/UC-PUB-004.md) | US-PUB-004 | AC-PUB-004-H/E/B | API-PUB-004 | UI-PUB-07 | TC-PUB-004-H/E/B | E8-Q01/02 |
| FEAT-056 | FR-PUB-MENU-001 | [UC-PUB-005](../usecases/UC-PUB-005.md) | US-PUB-005 | AC-PUB-005-H/E/B | API-PUB-005 | UI-PUB-03 | TC-PUB-005-H/E/B | E8-Q03/04 |
| FEAT-057 | FR-PUB-TRY-001 | [UC-PUB-006](../usecases/UC-PUB-006.md) | US-PUB-006 | AC-PUB-006-H/E/B | API-PUB-006 | UI-PUB-04 | TC-PUB-006-H/E/B | E8-Q05/04 |
| FEAT-058 | FR-PUB-LEAD-001 | [UC-PUB-007](../usecases/UC-PUB-007.md) | US-PUB-007 | AC-PUB-007-H/E/B | API-PUB-007 | UI-PUB-05 | TC-PUB-007-H/E/B | E8-Q06/07 |
| FEAT-058 | FR-PUB-RELY-001 | [UC-PUB-008](../usecases/UC-PUB-008.md) | US-PUB-008 | AC-PUB-008-H/E/B | API-PUB-008 | UI-PUB-08 | TC-PUB-008-H/E/B | E8-Q06/07/11 |
| FEAT-059 | FR-PUB-EDIT-001 | [UC-PUB-009](../usecases/UC-PUB-009.md) | US-PUB-009 | AC-PUB-009-H/E/B | API-PUB-009 | UI-PUB-06 | TC-PUB-009-H/E/B | E8-Q08/09 |
| FEAT-059 | FR-PUB-PREV-001 | [UC-PUB-010](../usecases/UC-PUB-010.md) | US-PUB-010 | AC-PUB-010-H/E/B | API-PUB-010 | UI-PUB-06 | TC-PUB-010-H/E/B | E8-Q08 |
| FEAT-059 | FR-PUB-PUBL-001 | [UC-PUB-011](../usecases/UC-PUB-011.md) | US-PUB-011 | AC-PUB-011-H/E/B | API-PUB-011 | UI-PUB-06 | TC-PUB-011-H/E/B | E8-Q08/09/02 |
| FEAT-059 | FR-PUB-MEDI-001 | [UC-PUB-012](../usecases/UC-PUB-012.md) | US-PUB-012 | AC-PUB-012-H/E/B | API-PUB-012 | UI-PUB-09 | TC-PUB-012-H/E/B | E8-Q09/08 |

Phủ12/12 FR có luồng;6/6 feature có thiết kế nháp có điều kiện,0 E8 gate-only;36 AC/ca không phải36 mục tiêu nghiệm thu độc lập. BR/NFR và test hệ thống xem [system-cases](system-cases.md). API phụ trợ cùng FR trong catalog.

FR-PUB-URLM-001 / UC-PUB-003 / US-PUB-003 còn truy vết API-PUB-016, UI-PUB-06 và TC-PUB-S05 cho chuyển nội dung bài thành nháp, đối chiếu sourceId/body/media/ngày gốc; API-PUB-003/UI-PUB-07 cho mapping URL. Nhánh import/CMS BLOCKED E8-Q01/02/08/09; không tự công bố sau chuyển.

## Bổ sung gate (XC-05)

> Chờ E8-Q13: XC-05. BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. Nguồn: [sổ câu hỏi](../review/questions.md).

Ca liên quan: TC-PUB-007-H. Các ca chứng minh chính sách hoặc tích hợp thật phụ thuộc câu này giữ BLOCKED. Ca kiểm invariant bằng dữ liệu giả vẫn NOT RUN, không chứng minh chính sách được duyệt.

| Câu hỏi bổ sung | Ca phụ thuộc | Trạng thái | Căn cứ |
| :--- | :--- | :--- | :--- |
| E8-Q13 | TC-PUB-007-H, TC-PUB-008-H | BLOCKED (giữ từ trước; bổ sung gate) | XC-05; [sổ câu hỏi](../review/questions.md) |
