---
id: DOC-AGENT-NOI-BO-API-DATA-MAPPING
title: Mapping dữ liệu E5, API, schema và màn hình
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-mapping, api, e5]
author: BA
last_updated: 2026-11-16
---
# Mapping dữ liệu E5: Agent Nội bộ

Draft · 16/11/2026 · Thiết kế BA để review, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo mapping 3 tầng API, bảng DBML, màn hình theo khuôn chung các epic. Không đổi API hay schema |

Nguồn: [catalog API](endpoint-catalog.json), [API spec](api-spec.md), [DBML 65 bảng](../../nen-tang/srs/schema.dbml), [ERD nền](../../nen-tang/srs/erd.md). Tên bảng và cột đã đối chiếu với DBML. Không migration, không thêm bảng.

## 1. Endpoint, bảng nguồn, màn hình

| API | Method và route | FR | Bảng DBML đọc hoặc ghi | Màn hình |
| :--- | :--- | :--- | :--- | :--- |
| API-AIO-001 | `POST /v1/internal-agent/runs` | FR-AIO-GEN-001 | agent_runs, agent_run_contexts | UI-AIO-01 |
| API-AIO-002 | `GET /v1/internal-agent/runs/{id}` | FR-AIO-CHK-001 | agent_runs, agent_run_contexts | UI-AIO-02 |
| API-AIO-003 | `POST /v1/internal-agent/revisions` | FR-AIO-EDIT-001 | agent_run_contexts (candidate_revision, candidate_hash) | UI-AIO-02 |
| API-AIO-004 | `POST /v1/internal-agent/runs/{id}/applications` | FR-AIO-APLY-001 | agent_run_contexts (applied_*), menus, menu_days, menu_day_items | UI-AIO-02 |
| API-AIO-005 | `GET /v1/internal-agent/run-logs` | FR-AIO-LOG-001 | agent_runs, agent_tool_events | UI-AIO-03 |
| API-AIO-006 | `GET /v1/internal-agent/runs/{id}/events` | FR-AIO-OPS-001 | agent_tool_events | UI-AIO-03 |

Mọi lệnh ghi số liệu còn ghi `audit_logs` theo FR-SYS-AUD-001; bảng này không lặp lại cho từng dòng.

## 2. Trường chính

| Trường API | Cột DBML | Màn hình | Chuyển đổi / lưu ý |
| :--- | :--- | :--- | :--- |
| runId, status | agent_runs (id, status), agent_code = NOI_BO | UI-AIO-01, 02 | DONE không đồng nghĩa phương án đạt |
| requestText | agent_runs.request_text | UI-AIO-01 | Ai được xem chờ AIO-Q04 |
| usage | agent_runs (input_tokens, output_tokens, cost_vnd), agent_run_contexts.usage_status | UI-AIO-03 | Đơn vị và nhà cung cấp chờ AIO-Q01 |
| baseMenuId, baseVersion | agent_run_contexts (base_menu_id, base_version) | UI-AIO-02 | Kiểm lại version khi áp dụng |
| candidateRevision, candidateHash, candidate | agent_run_contexts (candidate_revision, candidate_hash, candidate_snapshot) | UI-AIO-02 | Mỗi lần chỉnh tạo revision và hash mới |
| evidence | agent_run_contexts.evidence_snapshot | UI-AIO-02 | Kết quả kiểm MENU, COST cùng hash |
| outcome, questions | agent_run_contexts (outcome, questions) | UI-AIO-02 | NEEDS_INPUT, NO_SOLUTION, BLOCKED_DATA không có nháp để áp dụng |
| modelCode, promptVersion, deadlineAt | agent_run_contexts (model_code, prompt_version, deadline_at) | UI-AIO-03 | Chưa chọn mô hình (O-04) |
| application | agent_run_contexts (applied_menu_id, applied_menu_version, application_key, application_hash, applied_at) | UI-AIO-02 | Áp dụng chỉ tạo menus DRAFT, nguyên tử |
| toolEvents | agent_tool_events (seq, tool_name, status, request_id, argument_hash, result_hash, safe_summary) | UI-AIO-03 | Chỉ metadata đã lọc |

## 3. Quy ước chung

- ID nội bộ là BIGINT; API truyền dạng chuỗi để không mất độ chính xác.
- Tiền là số nguyên VND hoặc decimal truyền dạng chuỗi; không dùng float. Giá trị thiếu để trống, không mặc định 0.
- Phạm vi cơ sở và quyền lấy từ phiên ở server, không tin giá trị client gửi lên.
- Envelope lỗi, phân trang và idempotency chưa thống nhất giữa các epic (E1-Q01, E1-Q02).
