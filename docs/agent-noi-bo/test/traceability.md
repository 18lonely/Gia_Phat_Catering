# Ma trận truy vết — AIO

Phiên bản 0.1.1 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-12; AIO-Q07 |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Mỗi dòng là một kịch bản, không phải chứng nhận đủ kiểm thử mọi tổ hợp.

| Feature | FR | UC | Story | AC | TC | API | UI | Bảng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-021 | FR-AIO-GEN-001 | UC-AIO-001 | US-AIO-001 | AC-AIO-001 | TC-AIO-001 | API-AIO-001 | UI-AIO-01 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-021 | FR-AIO-GEN-001 | UC-AIO-001 | US-AIO-001 | AC-AIO-002 | TC-AIO-002 | API-AIO-001 | UI-AIO-01 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-021 | FR-AIO-GEN-001 | UC-AIO-001 | US-AIO-001 | AC-AIO-003 | TC-AIO-003 | API-AIO-001 | UI-AIO-01 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-021 | FR-AIO-CHK-001 | UC-AIO-002 | US-AIO-002 | AC-AIO-004 | TC-AIO-004 | API-AIO-002 | UI-AIO-02 | agent_run_contexts, agent_tool_events | NOT RUN |
| FEAT-021 | FR-AIO-CHK-001 | UC-AIO-002 | US-AIO-002 | AC-AIO-005 | TC-AIO-005 | API-AIO-002 | UI-AIO-02 | agent_run_contexts, agent_tool_events | NOT RUN |
| FEAT-021 | FR-AIO-CHK-001 | UC-AIO-002 | US-AIO-002 | AC-AIO-006 | TC-AIO-006 | API-AIO-002 | UI-AIO-02 | agent_run_contexts, agent_tool_events | BLOCKED: AIO-Q02 |
| FEAT-022 | FR-AIO-EDIT-001 | UC-AIO-003 | US-AIO-003 | AC-AIO-007 | TC-AIO-007 | API-AIO-003 | UI-AIO-02 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-022 | FR-AIO-EDIT-001 | UC-AIO-003 | US-AIO-003 | AC-AIO-008 | TC-AIO-008 | API-AIO-003 | UI-AIO-02 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-022 | FR-AIO-EDIT-001 | UC-AIO-003 | US-AIO-003 | AC-AIO-009 | TC-AIO-009 | API-AIO-003 | UI-AIO-02 | agent_runs, agent_run_contexts | NOT RUN |
| FEAT-022 | FR-AIO-APLY-001 | UC-AIO-004 | US-AIO-004 | AC-AIO-010 | TC-AIO-010 | API-AIO-004 | UI-AIO-02 | menus, menu_days, menu_day_items, agent_run_contexts, audit_logs | NOT RUN |
| FEAT-022 | FR-AIO-APLY-001 | UC-AIO-004 | US-AIO-004 | AC-AIO-011 | TC-AIO-011 | API-AIO-004 | UI-AIO-02 | menus, menu_days, menu_day_items, agent_run_contexts, audit_logs | NOT RUN |
| FEAT-022 | FR-AIO-APLY-001 | UC-AIO-004 | US-AIO-004 | AC-AIO-012 | TC-AIO-012 | API-AIO-004 | UI-AIO-02 | menus, menu_days, menu_day_items, agent_run_contexts, audit_logs | NOT RUN |
| FEAT-023 | FR-AIO-LOG-001 | UC-AIO-005 | US-AIO-005 | AC-AIO-013 | TC-AIO-013 | API-AIO-005 | UI-AIO-03 | agent_runs, agent_run_contexts, agent_tool_events | NOT RUN |
| FEAT-023 | FR-AIO-LOG-001 | UC-AIO-005 | US-AIO-005 | AC-AIO-014 | TC-AIO-014 | API-AIO-005 | UI-AIO-03 | agent_runs, agent_run_contexts, agent_tool_events | NOT RUN |
| FEAT-023 | FR-AIO-LOG-001 | UC-AIO-005 | US-AIO-005 | AC-AIO-015 | TC-AIO-015 | API-AIO-005 | UI-AIO-03 | agent_runs, agent_run_contexts, agent_tool_events | NOT RUN |
| FEAT-023 | FR-AIO-OPS-001 | UC-AIO-006 | US-AIO-006 | AC-AIO-016 | TC-AIO-016 | API-AIO-006 | UI-AIO-03 | agent_runs, agent_tool_events, agent_run_contexts | NOT RUN |
| FEAT-023 | FR-AIO-OPS-001 | UC-AIO-006 | US-AIO-006 | AC-AIO-017 | TC-AIO-017 | API-AIO-006 | UI-AIO-03 | agent_runs, agent_tool_events, agent_run_contexts | NOT RUN |
| FEAT-023 | FR-AIO-OPS-001 | UC-AIO-006 | US-AIO-006 | AC-AIO-018 | TC-AIO-018 | API-AIO-006 | UI-AIO-03 | agent_runs, agent_tool_events, agent_run_contexts | BLOCKED: AIO-Q01 |

## Bổ sung gate — XC-12

> Chờ AIO-Q07 — XC-12. BLOCKED nghiệm thu phép đo phản hồi đầu; AIO-Q01 và E1-Q06 còn mở. Nguồn: [sổ câu hỏi](../review/questions.md).

Phép đo/tích hợp này chưa có ca độc lập được xác nhận; cần truy vết sau quyết định. Các ca chứng minh chính sách hoặc tích hợp thật phụ thuộc câu này giữ BLOCKED. Ca kiểm invariant bằng dữ liệu giả vẫn NOT RUN, không chứng minh chính sách được duyệt.

| Câu hỏi bổ sung | Ca phụ thuộc | Trạng thái | Căn cứ |
| :--- | :--- | :--- | :--- |
| AIO-Q07 | TC-AIO-NFR-01 | BLOCKED (giữ từ trước; bổ sung gate) | XC-12; [sổ câu hỏi](../review/questions.md) |
