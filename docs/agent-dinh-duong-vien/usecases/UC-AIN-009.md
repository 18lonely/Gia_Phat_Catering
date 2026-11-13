---
id: DOC-E9-USECASES-UC-AIN-009-MD
title: "UC-AIN-009: Kiểm và giữ hạn mức lượt/ngân sách"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-009: Kiểm và giữ hạn mức lượt/ngân sách

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Fish level. Actor chính: Agent Dinh dưỡng viên, qua orchestrator yêu cầu admission; đây là vai trò hệ thống trong PRD, không phải khách tự cấp ngân sách. Giám đốc (PER-08) giám sát khi được cấp quyền.
Truy vết: FR-AIN-LIMT-001 / FEAT-064 / US-AIN-009.

Trigger: Một lượt hoặc bước tool/model sắp phát sinh chi phí cần được kiểm hạn mức trước khi chạy.

Tiền điều kiện (nghiệp vụ): Có principal/group đã xác minh từ server, requestKey, policyVersion và upper bound chi phí cưỡng chế được.
Tiền điều kiện (gate còn mở): E9-Q01, E9-Q07, E9-Q13 chưa chốt provider, nhóm/lượt/cap/đơn vị/ngày và giao dịch; O-03 không được mở qua admission.

Luồng chính:
1. Orchestrator gửi principal/group, policyVersion, requestKey và upper bound của bước cần nhận tới PORT-AIN-ADMISSION.
2. Admission kiểm policy hiện hành, đơn vị/ngày ngân sách, quyền chủ thể và upper bound có xác định/cưỡng chế được hay không.
3. Admission đối chiếu lượt còn lại và tổng spentConfirmed + outstandingReserved + upperBound với cap.
4. Khi đủ điều kiện, admission giữ chỗ nguyên tử cả lượt và ngân sách trước mọi phát sinh chi phí, gắn reservationRef với yêu cầu.
5. Orchestrator nhận ADMITTED và chỉ cho bước tiếp tục khi quyền cùng budget lease còn hiệu lực; mỗi bước có chi phí phải được kiểm lại điều kiện.
6. Hệ thống trả trạng thái an toàn cho UI-AIN-06 khi cần, giữ metadata phục vụ đối soát; không đưa chi tiết trần nội bộ cho khách.

Hậu điều kiện thành công: Lượt được nhận có reservation hợp lệ trước khi phát sinh chi phí; không vượt cap do các lượt đồng thời.
Bảo đảm tối thiểu: Unknown không bằng 0, timeout không có nghĩa provider không tính tiền; không chuyển sang quota AIO hay đổi identity để vượt trần.

Extensions:
- 3a. Hết lượt/chạm cap: admission trả QUOTA_BLOCKED/BUDGET_BLOCKED với ERR-AIN-429-01; không nhận lượt hoặc gọi provider.
- 2a. Không xác định upper bound hoặc còn usage chưa rõ: admission giữ UNKNOWN_BLOCKED và không giải phóng phần reserve chưa xác định; không phát sinh bước chi phí mới theo giả định 0.
- 2b. Policy/provider chưa sẵn sàng: hệ thống trả ERR-AIN-503-01 kèm gate; chưa có admission hợp lệ.
- 4a. Nhiều yêu cầu sát trần hoặc retry cùng yêu cầu: admission kiểm/giữ chỗ nguyên tử và trả kết quả yêu cầu gốc theo policy; không tính lượt hai lần hoặc overspend.
- 5a. Lease/quyền không còn hợp lệ: hệ thống chặn bước tiếp theo; reservation/usage đã có không bị tự xóa để giả còn ngân sách.

## Giao tiếp và kiểm

PORT-AIN-ADMISSION: PORT PORT-AIN-ADMISSION; UI-AIN-06. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
