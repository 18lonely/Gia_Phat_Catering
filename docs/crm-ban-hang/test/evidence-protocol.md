---
id: DOC-E10-TEST-EVIDENCE-PROTOCOL-MD
title: Quy trình bằng chứng kiểm E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Quy trình bằng chứng kiểm E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

Mỗi lần chạy tương lai phải ghi caseId, batchId, người chạy/duyệt, môi trường/build, thời gian, datasetHash, decisionRefs và oracleRef. Chưa chạy thì Actual/Evidence trống. Sau có quyết định chỉ chuyển BLOCKED → NOT RUN có nguồn; chỉ sau chạy thật và bằng chứng mới được kết luận kết quả.

| Nhóm | Bằng chứng cần | Cách đối chiếu |
| :--- | :--- | :--- |
| Gộp/hoàn tác | before/after hashes, link-map, người duyệt, versions, requestId, commit timeline | Không mất tham chiếu; audit gốc còn nguyên; giao dịch mới không bị chuyển ngầm. |
| Giá/phụ lục | customer/mealType, khoảng hiệu lực, termVersion, evidence ký, order snapshot hash | Tối đa một khoảng khớp theo biên đã duyệt; hash snapshot lịch sử không đổi. |
| Projection | Server response, tệp/metadata, DOM, cache/error và quyền server | Canary synthetic không vượt biên; screenshot không đủ chứng minh server lọc. |
| Tín hiệu rời | scheduleVersion/ngoại lệ, observation window, nguồn order/giao nhận, evaluationRef | Đối chiếu từng kỳ đủ điều kiện; thiếu dữ liệu không bằng 0; policy version phải được duyệt. |
| R10 | Manifest nguồn độc lập và danh sách ngoại lệ theo ngày chốt | Đối chiếu từng dòng, không xóa khách/hợp đồng khó để tăng tỷ lệ. |

Báo cáo công khai phải che thông tin liên hệ, cost/margin và văn bản hợp đồng nhạy cảm; evidence gốc trong kho có quyền được duyệt. validation chỉ lưu bằng chứng kiểm tài liệu và mock synthetic, không thay bằng chứng sản phẩm. E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04 đều giữ trạng thái chờ tại sổ nguồn. Không hỏi lại, tự trả lời hoặc quyết định thay.
