---
id: DOC-E11-UI-SCREENS-MD
title: Danh mục màn và quyền E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Danh mục màn và quyền E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

| Màn | Tên | Actor đề xuất | FR | Trường / hành động |
| :--- | :--- | :--- | :--- | :--- |
| UI-PUR-01 | Nhu cầu nguyên liệu | Kế toán (PER-07) | FR-PUR-DEM-001 | planRef, planRevision, estimateRef, serviceDate, kitchenId |
| UI-PUR-02 | Đơn mua nháp | Kế toán (PER-07) | FR-PUR-POD-001, FR-PUR-POG-001 | demandRef, supplierId, lines, reason; purchaseOrderRef, version |
| UI-PUR-03 | Nhận hàng và phạm vi lô | Quản lý cơ sở (PER-06) | FR-PUR-LOT-001, FR-PUR-RCV-001 | ingredientId, storageType, receiptRef; purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason |
| UI-PUR-04 | Ảnh chứng từ | Quản lý cơ sở (PER-06) | FR-PUR-DOC-001 | receiptRef, fileRef, version |
| UI-PUR-05 | Công nợ nhà cung cấp | Kế toán (PER-07) | FR-PUR-APV-001 | supplierId, kitchenId, fromDate, toDate |
| UI-PUR-06 | Dự toán so với thực mua | Kế toán (PER-07); Giám đốc/Kế toán (PER-08/07) | FR-COST-BUY-001, FR-COST-BEX-001 | estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef; comparisonRef, ingredientId |
| UI-PUR-07 | Phân ca sản xuất | Bếp trưởng (PER-06) | FR-PLAN-SHF-001 | kitchenId, serviceDate, shiftRef, assignments, planRef |
| UI-PUR-08 | Kiểm trước giao và mẫu lưu | Bếp trưởng (PER-06); Quản lý cơ sở (PER-06) | FR-PLAN-QCG-001, FR-PLAN-SMP-001 | shiftRef, checklistRef, results, reason; mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef |
| UI-PUR-09 | Món thay thế | Dinh dưỡng viên (PER-05) | FR-MENU-SUB-001, FR-MENU-SCK-001, FR-MENU-SGT-001 | menuRef, menuVersion, originalDishId, replacementDishId, reason; candidateRef, candidateVersion, menuSourceRef; candidateRef, candidateVersion, checkRefs |

Mỗi màn có loading, empty, missing, error, offline, denied, conflict. Người thiếu quyền giá chỉ xem lượng; danh sách công nợ/đối chiếu chỉ cho quyền tài chính thích hợp. E1 kiểm mỗi request, không tin nút ẩn. File riêng theo quyền chủ thể. Quyền cụ thể chờ E11-Q13; không tự gán quyền duyệt cho PER-08. [Wireframe](../html-wireframe/purchase-workbench.html).
