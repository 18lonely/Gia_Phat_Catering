---
id: DOC-NEN-TANG-API-DATA-MAPPING
title: Mapping dữ liệu E1, API, schema và màn hình
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [data-mapping, api, e1]
author: BA
last_updated: 2026-11-16
---
# Mapping dữ liệu E1: Nền tảng

Draft · 16/11/2026 · Thiết kế BA để review, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo mapping 3 tầng API, bảng DBML, màn hình theo khuôn chung các epic. Không đổi API hay schema |

Nguồn: [catalog API](endpoint-catalog.json), [API spec](api-spec.md), [DBML 65 bảng](../../nen-tang/srs/schema.dbml), [ERD nền](../../nen-tang/srs/erd.md). Tên bảng và cột đã đối chiếu với DBML. Không migration, không thêm bảng.

## 1. Endpoint, bảng nguồn, màn hình

| API | Method và route | FR | Bảng DBML đọc hoặc ghi | Màn hình |
| :--- | :--- | :--- | :--- | :--- |
| API-CORE-001 | `POST /v1/auth/sessions` | FR-AUTH-LGN-001 | sessions, users, login_logs | UI-CORE-01 |
| API-CORE-002 | `POST /v1/auth/session-refreshes` | FR-AUTH-LGN-002 | sessions | UI-CORE-01 |
| API-CORE-003 | `POST /v1/auth/session-revocations` | FR-AUTH-LGN-003 | sessions | UI-CORE-01 |
| API-CORE-004 | `POST /v1/auth/mfa-verifications` | FR-AUTH-LGN-004 | sessions, users (MFA chờ N-04, E1-Q03) | UI-CORE-01 |
| API-CORE-005 | `PUT /v1/auth/me/password` | FR-AUTH-PWD-001 | users.password_hash, sessions | UI-CORE-01, 02 |
| API-CORE-006 | `POST /v1/auth/users/{id}/password-resets` | FR-AUTH-PWD-002 | users.temp_password_expires_at, audit_logs | UI-CORE-02 |
| API-CORE-007 | `POST /v1/auth/users` | FR-AUTH-ACC-001 | users, user_roles, audit_logs | UI-CORE-02 |
| API-CORE-008 | `PATCH /v1/auth/users/{id}/status` | FR-AUTH-ACC-002 | users.status, users.locked_until, audit_logs | UI-CORE-02 |
| API-CORE-009 | `PUT /v1/auth/users/{id}/roles` | FR-AUTH-ACC-003 | user_roles (role_code, kitchen_id), audit_logs | UI-CORE-02 |
| API-CORE-010 | `GET /v1/auth/login-logs` | FR-AUTH-ACC-004 | login_logs | UI-CORE-03 |
| API-CORE-011 | `GET /v1/auth/permission-matrix` | FR-AUTH-RBAC-002 | user_roles; ma trận quyền trong SRS, không có bảng riêng | UI-CORE-02 |
| API-CORE-012 | `POST /v1/auth/delegations` | FR-AUTH-RBAC-003 | delegations, audit_logs | UI-CORE-02 |
| API-CORE-013 | `GET /v1/auth/me` | FR-AUTH-RBAC-001 | users, user_roles, delegations | UI-CORE-01, 02 |
| API-CORE-014 | `GET /v1/auth/users` | FR-AUTH-ACC-001 | users, user_roles, audit_logs | UI-CORE-02 |
| API-CORE-015 | `GET /v1/sys/audit-logs` | FR-SYS-AUD-002 | audit_logs | UI-CORE-03 |
| API-CORE-016 | `GET /v1/sys/parameters` | FR-SYS-PRM-001 | parameters | UI-CORE-04 |
| API-CORE-017 | `POST /v1/sys/parameter-changes` | FR-SYS-PRM-001 | change_requests, parameters | UI-CORE-04 |
| API-CORE-018 | `POST /v1/sys/parameter-changes/{id}/decisions` | FR-SYS-PRM-002 | approvals, parameters, audit_logs | UI-CORE-04 |
| API-CORE-019 | `GET /v1/sys/notifications` | FR-SYS-NTF-002 | notifications | UI-CORE-05 |
| API-CORE-020 | `PATCH /v1/sys/notifications/{id}` | FR-SYS-NTF-002 | notifications | UI-CORE-05 |
| API-CORE-021 | `POST /v1/sys/files` | FR-SYS-FILE-001 | files | UI-CORE-06 |
| API-CORE-022 | `POST /v1/sys/files/{id}/access-links` | FR-SYS-FILE-001 | files (link tạm, không lưu bảng) | UI-CORE-06 |
| API-CORE-023 | `GET /v1/sys/jobs` | FR-SYS-JOB-001 | Chưa có bảng job trong DBML | UI-CORE-06 |
| API-CORE-024 | `POST /v1/sys/jobs/{id}/retries` | FR-SYS-JOB-001 | Chưa có bảng job trong DBML | UI-CORE-06 |
| API-CORE-025 | `GET /v1/health` | FR-SYS-HLT-001 | Không đọc bảng nghiệp vụ | Không có màn |

Mọi lệnh ghi số liệu còn ghi `audit_logs` theo FR-SYS-AUD-001; bảng này không lặp lại cho từng dòng.

## 2. Trường chính

| Trường API | Cột DBML | Màn hình | Chuyển đổi / lưu ý |
| :--- | :--- | :--- | :--- |
| username | users.username | UI-CORE-01, 02 | Hình thức đăng nhập (điện thoại, email, tên) chờ N-01 |
| password | users.password_hash | UI-CORE-01 | Chỉ nhận vào, không bao giờ trả ra; băm phía server |
| userId | users.id | UI-CORE-02 | BIGINT, truyền qua API dạng chuỗi |
| status | users.status, users.locked_until, users.failed_attempts | UI-CORE-02 | Khóa tạm sau nhiều lần sai theo SRS |
| roles[].roleCode, roles[].kitchenId | user_roles.role_code, user_roles.kitchen_id | UI-CORE-02 | Phạm vi cơ sở lấy từ server, không tin client |
| delegation | delegations (from_user_id, to_user_id, permission_code, valid_from, valid_to, reason) | UI-CORE-02 | Người thay khi vắng chờ O-06 |
| session | sessions (refresh_token_hash, expires_at, revoked_at, replaced_by_id) | UI-CORE-01 | Refresh token chỉ lưu dạng băm |
| loginLog | login_logs (occurred_at, username, result, ip, user_agent) | UI-CORE-03 | Thời gian lưu chờ N-03 |
| audit | audit_logs (actor_user_id, on_behalf_user_id, entity, entity_id, action, changes, reason, request_id) | UI-CORE-03 | Bất biến; ai đọc audit nhạy cảm chờ E1-Q05 |
| parameter | parameters (code, scope_type, scope_id, value, effective_from, status) | UI-CORE-04 | Đổi qua change_requests và approvals |
| notification | notifications (type, severity, title, body, entity, entity_id, status, seen_at, done_at) | UI-CORE-05 | Mở lại RESOLVED chờ E1-Q04 |
| file | files (storage_key, original_name, mime_type, size_bytes, is_public) | UI-CORE-06 | storage_key không ra client |
| job | Chưa có bảng | UI-CORE-06 | Cần bảng job khi chọn thư viện hàng đợi (đề xuất apalis) |

## 3. Quy ước chung

- ID nội bộ là BIGINT; API truyền dạng chuỗi để không mất độ chính xác.
- Tiền là số nguyên VND hoặc decimal truyền dạng chuỗi; không dùng float. Giá trị thiếu để trống, không mặc định 0.
- Phạm vi cơ sở và quyền lấy từ phiên ở server, không tin giá trị client gửi lên.
- Envelope lỗi, phân trang và idempotency chưa thống nhất giữa các epic (E1-Q01, E1-Q02).
