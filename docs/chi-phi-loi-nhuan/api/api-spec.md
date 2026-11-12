---
id: DOC-E13-API-API-SPEC-MD
title: Đề xuất hợp đồng API EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Đề xuất hợp đồng API EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## 1. Trạng thái hợp đồng

Chỉ thiết kế tài liệu. 18 endpoint đề xuất, 5 port logic; không triển khai hoặc gọi API. Freeze, envelope, receipt, giới hạn, phân trang, TTL và cơ chế retry chờ E13-Q12/E1-Q01–05. Không webhook, callback hay tích hợp chấm công/kế toán được chọn. Không endpoint gửi khách hoặc xóa cứng.

## 2. Xác thực, ghi và lỗi

Mọi request cần phiên E1; kiểm quyền hành động, cơ sở, khách và trường trước đọc dữ liệu. Authorization theo chuẩn nền chờ freeze; Content-Type application/json cho body; requestId để truy vết. POST có khóa chống lặp theo contract được duyệt, không đặt tên header/TTL thành chuẩn mới. expectedVersion và expectedHash bắt buộc khi tác động bản hiện có. Kiểm lại trong cùng giao dịch với audit, không ghi nửa chừng. Timeout chưa biết kết quả phải đối soát receipt, không gửi lại mù.

GET dùng path/query theo request bên dưới, không GET body. POST tạo nháp trả 201; thao tác chuyển trạng thái trả 200 khi thật sự hoàn tất. Lần kiểm trả BLOCKED là trạng thái nghiệp vụ, không báo thành công tính toán; lệnh yêu cầu tính thiếu điều kiện trả 422 và mã EXP. Envelope minh họa theo ba-kit, chưa freeze:

```json
{"success":false,"data":null,"error":{"code":"ERR-EXP-422-03","message":"Lợi nhuận theo khách đang BLOCKED."},"meta":{"requestId":"synthetic-request"},"timestamp":"2026-11-12T00:00:00Z"}
```

Đọc run bị chặn có thể trả 200 với status BLOCKED, methodVersionRef null, profit null, blockedReasons và directCosts đúng quyền; tuyệt đối không success=true cho hành động phân bổ chưa thực hiện. Mọi trường tiền dùng decimal string và currency; null + reason khác 0. Lỗi chung 401/403/404/503 theo [ma trận](../srs/error-matrix.md), 409 cho bất biến/version/trùng, 422 cho thiếu điều kiện. Log chỉ mã/tham chiếu, không lương hoặc giá trị bị cấm.

## 3. Danh mục và payload

### API-EXP-001 — POST /v1/expense-periods

- FR: FR-EXP-PER-001; màn UI-EXP-01.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: periodRef, kitchenRef, fromDate, toDate, version, lockDecisionRef.
- Response data: Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q02. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-002 — POST /v1/expense-entries

- FR: FR-EXP-COST-001; màn UI-EXP-02.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: periodRef, kitchenRef, typeVersionRef, amount, evidenceRef, sourceKey, customerRef?.
- Response data: Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q01. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-003 — POST /v1/attendance-sheets

- FR: FR-EXP-TIME-001; màn UI-EXP-03.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: personRef, kitchenRef, shiftRevisionRef, workDate, hours, attendanceEvidenceRef, version.
- Response data: Bảng DRAFT; giờ thực tế và ca dự kiến tách riêng; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q03; E11-Q09. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-004 — POST /v1/labor-cost-references

- FR: FR-EXP-LAB-001; màn UI-EXP-03.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: attendanceVersionRef, rateVersionRef hoặc payrollAmountRef, evidenceRef.
- Response data: Chi phí nhân công có nguồn hoặc BLOCKED; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q03/04. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-005 — POST /v1/allocation-method-versions

- FR: FR-EXP-METH-001; màn UI-EXP-04.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: methodRef?, baseVersion?, scope, proposedBasis, effectiveRange, sourceDefinitionRefs, rationale.
- Response data: Phiên bản DRAFT; không có hiệu lực phân bổ; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05/09. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-006 — POST /v1/allocation-method-versions/{id}/decisions

- FR: FR-EXP-APRV-001; màn UI-EXP-04.
- Quyền: PER-08 + quyền hành động + scope cơ sở.
- Request JSON body: methodVersionRef, expectedVersion, expectedHash, decision, evidenceRef, reason.
- Response data: Quyết định APPROVED hoặc RETURNED; version không đổi nội dung; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05; O-06. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-007 — POST /v1/allocation-runs

- FR: FR-EXP-ALLOC-001; màn UI-EXP-05.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: periodSnapshotRef, methodVersionRef, sourceManifestRef.
- Response data: Lần chạy BLOCKED hoặc bản phân bổ có methodVersion; phần chưa phân bổ riêng; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05/06/09/12. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-008 — GET /v1/profit-runs/{id}/customers

- FR: FR-EXP-PROF-001; màn UI-EXP-06.
- Quyền: PER-07/PER-08 + quyền hành động + scope cơ sở.
- Request query/path: runRef, customerRef, kitchenRef, periodRef.
- Response data: Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-009 — GET /v1/profit-runs/{id}/reconciliation

- FR: FR-EXP-RECON-001; màn UI-EXP-07.
- Quyền: PER-08 + quyền hành động + scope cơ sở.
- Request query/path: runRef, facilityResultRef, resultDefinitionVersionRef.
- Response data: Bảng đối chiếu có residual/unallocated/delta; chưa khớp không nghiệm thu; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q06/08/09/14. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-010 — POST /v1/expense-adjustments

- FR: FR-EXP-ADJ-001; màn UI-EXP-08.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: originalEntryRef, lockedSnapshotRef, adjustmentAmount, reason, evidenceRef, approvalRef.
- Response data: Đề nghị PENDING; chỉ POSTED khi có quyết định hợp lệ; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q10; O-06. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-011 — GET /v1/profit-runs/{id}/internal-projection

- FR: FR-EXP-SAFE-001; màn UI-EXP-06.
- Quyền: PER-07/PER-08 + quyền hành động + scope cơ sở.
- Request query/path: runRef, actorScope, purpose, projection.
- Response data: Projection nội bộ cho phép hoặc từ chối; không có đường gửi khách E13; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q11/12; E12-Q07. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-012 — GET /v1/profit-runs/{id}/sources

- FR: FR-EXP-SRC-001; màn UI-EXP-05.
- Quyền: PER-07/PER-08 + quyền hành động + scope cơ sở.
- Request query/path: runRef, sourceManifestRef, expectedVersions.
- Response data: Manifest, danh sách BLOCKED và liên kết nội bộ theo quyền; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q12/13. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-013 — POST /v1/expense-periods/{id}/locks

- FR: FR-EXP-PER-001; màn UI-EXP-01.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: periodRef, expectedVersion, lockDecisionRef.
- Response data: Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q02. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-014 — POST /v1/attendance-sheets/{id}/submissions

- FR: FR-EXP-TIME-001; màn UI-EXP-03.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: sheetRef, expectedVersion, evidenceRef.
- Response data: Bảng SUBMITTED giữ revision và bằng chứng; chưa tự xác nhận giờ công; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q03; E11-Q09. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-015 — POST /v1/allocation-method-versions/{id}/submissions

- FR: FR-EXP-METH-001; màn UI-EXP-04.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: methodVersionRef, expectedVersion, expectedHash.
- Response data: Phiên bản SUBMITTED chờ Giám đốc; chưa có hiệu lực phân bổ; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05/09. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-016 — POST /v1/expense-adjustments/{id}/decisions

- FR: FR-EXP-ADJ-001; màn UI-EXP-08.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request JSON body: adjustmentRef, expectedVersion, decision, reason, approvalEvidenceRef.
- Response data: Quyết định REJECTED hoặc POSTED theo chính sách đã duyệt; bản gốc bất biến; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q10; O-06. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-017 — POST /v1/profit-runs

- FR: FR-EXP-PROF-001; màn UI-EXP-06.
- Quyền: PER-07/PER-08 + quyền hành động + scope cơ sở.
- Request JSON body: allocationRunRef, sourceManifestRef, definitionVersionRef.
- Response data: Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

### API-EXP-018 — GET /v1/expense-periods/{id}/direct-costs

- FR: FR-EXP-COST-001; màn UI-EXP-02.
- Quyền: PER-07 + quyền hành động + scope cơ sở.
- Request query/path: periodRef, kitchenRef, customerRef?.
- Response data: Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức; thêm id, version, status, sourceRefs theo đối tượng.
- Điều kiện: E13-Q01. Không tự triển khai nhánh chưa chốt.
- Lỗi: ERR-EXP-401-01, ERR-EXP-403-01, ERR-EXP-404-01, ERR-EXP-409-01, ERR-EXP-409-02, ERR-EXP-409-03, ERR-EXP-422-01, ERR-EXP-422-02, ERR-EXP-422-03, ERR-EXP-422-04, ERR-EXP-503-01; dùng đúng trigger, không trả đồng loạt.

## 4. Duyệt và projection

API-EXP-006 chỉ PER-08 khác lập/sửa cuối; API-EXP-016 người duyệt chờ Q10, deny khi chưa cấu hình. API-EXP-008/011 không có personRef/hours/rate trong output theo khách. Chi tiết lương chỉ trả ở tài nguyên công cho PER-07/PER-08 được cấp quyền trường. Tham số purpose=customer không được dùng để xuất E13; từ chối, không dựa vào ẩn CSS. Mọi đường export tương lai phải kiểm lại quyền và allowlist; định dạng chưa chọn.

[Mapping](data-mapping.md) · [Catalog máy đọc](endpoint-catalog.json) · [RTM](../test/traceability.md).
