---
id: DOC-E9-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria Given / When / Then
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria Given / When / Then

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

| AC | FR | Given | When | Then |
| :--- | :--- | :--- | :--- | :--- |
| AC-AIN-001-01 | FR-AIN-SESS-001 | policy/consent đã duyệt và identity hợp lệ | mở phiên | có sessionRef đúng chủ thể, không cấp quyền cost |
| AC-AIN-001-02 | FR-AIN-SESS-001 | chưa chốt loại người dùng hoặc consent | mở phiên | từ chối, không gọi AI, không lưu hội thoại |
| AC-AIN-001-03 | FR-AIN-SESS-001 | phiên người khác hoặc đã thu hồi | đọc lại phiên | 404 hoặc 401 an toàn, không phục hồi dữ liệu ngoài quyền |
| AC-AIN-002-01 | FR-AIN-GEN-001 | nguồn đã duyệt, đủ hạn mức và yêu cầu khả thi | gửi yêu cầu | run bền vững; candidate phải qua CHK trước trình bày |
| AC-AIN-002-02 | FR-AIN-GEN-001 | số suất âm/lẻ hoặc kiêng kỵ không rõ | gửi | 400/422 hoặc NEEDS_INPUT, không tự đoán |
| AC-AIN-002-03 | FR-AIN-GEN-001 | gửi lặp cùng key/body sau mất mạng | gửi lại | trả cùng run, không reserve/tính lượt lần hai |
| AC-AIN-003-01 | FR-AIN-CHK-001 | candidate đúng nguồn và máy E2 không vi phạm cứng | hoàn tất kiểm rồi GET | hiện nháp đã kiểm, bảng kiểm an toàn và version |
| AC-AIN-003-02 | FR-AIN-CHK-001 | máy kiểm lỗi hoặc vi phạm cứng | đọc kết quả | không trả VALID; không cho gửi nháp đó |
| AC-AIN-003-03 | FR-AIN-CHK-001 | nguồn/ruleVersion đổi sau kiểm | xem hoặc gửi | đánh dấu stale và yêu cầu kiểm lại, không dùng evidence cũ |
| AC-AIN-004-01 | FR-AIN-EXPL-001 | candidate đã kiểm và đủ nguồn E4 | yêu cầu giải thích | 4 chỉ số có đơn vị/nguồn và nhãn ước tính từ định lượng sống |
| AC-AIN-004-02 | FR-AIN-EXPL-001 | nguồn dinh dưỡng thiếu hoặc stale | hỏi dinh dưỡng | ghi chưa đủ/cũ, không bịa số hoặc thay null bằng 0 |
| AC-AIN-004-03 | FR-AIN-EXPL-001 | hỏi suy giá nhập từ giá suất và định lượng | yêu cầu giải thích | không suy ngược, không gọi tool cấm; trả từ chối an toàn |
| AC-AIN-005-01 | FR-AIN-EDIT-001 | revision hiện hành và đổi món hợp lệ | chỉnh một ngày | chạy E2 toàn tuần; chỉ bản mới đạt mới được ghi đã kiểm |
| AC-AIN-005-02 | FR-AIN-EDIT-001 | đổi tạo vi phạm cứng | chỉnh | bản mới bị chặn; không trình bày hợp lệ, bản cũ chỉ lịch sử |
| AC-AIN-005-03 | FR-AIN-EDIT-001 | hai tab sửa cùng baseRevision | gửi hai chỉnh sửa | một revision tiến; lệnh cũ 409, không ghi đè |
| AC-AIN-006-01 | FR-AIN-SEND-001 | đầu nhận được duyệt, consent đủ, nháp đạt kiểm mới | xác nhận gửi | receipt bền vững và CHỜ XEM XÉT; không menus/order/báo giá |
| AC-AIN-006-02 | FR-AIN-SEND-001 | chưa chọn nơi lưu/đầu nhận | gửi | 503/policy closed, không báo thành công hoặc vào CRM |
| AC-AIN-006-03 | FR-AIN-SEND-001 | đã lưu nhưng mất phản hồi/nhận trùng | gửi lại cùng key | cùng proposal/receipt; không tạo lead hoặc đề xuất trùng |
| AC-AIN-007-01 | FR-AIN-STAT-001 | proposal đã tiếp nhận bền vững thuộc chủ thể | xem | hiện chờ người thật xem xét, không coi đã áp dụng |
| AC-AIN-007-02 | FR-AIN-STAT-001 | proposal ngoài quyền | xem | 404 đồng nhất không lộ tồn tại |
| AC-AIN-007-03 | FR-AIN-STAT-001 | chưa receipt bàn giao hoặc trạng thái đến muộn | xem | không tự chuyển đã bàn giao/đã duyệt |
| AC-AIN-008-01 | FR-AIN-GATE-001 | gate O-03 đóng | xem khả dụng | CLOSED, không có biểu mẫu hồ sơ |
| AC-AIN-008-02 | FR-AIN-GATE-001 | client cố gửi trường bệnh lý/hồ sơ | gọi đường không được hỗ trợ | từ chối, không chuyển payload tới model hoặc lưu hồ sơ |
| AC-AIN-008-03 | FR-AIN-GATE-001 | client tự khai gate đã mở | yêu cầu gợi ý | server giữ CLOSED; không quyền client đổi gate |
| AC-AIN-009-01 | FR-AIN-LIMT-001 | policy được duyệt và remaining đủ upper bound | nhận lượt | reserve nguyên tử trước bất kỳ phát sinh chi phí nào |
| AC-AIN-009-02 | FR-AIN-LIMT-001 | hết lượt/chạm trần hoặc không xác định được upper bound | nhận lượt | chặn không gọi provider; không fallback sang quota AIO |
| AC-AIN-009-03 | FR-AIN-LIMT-001 | nhiều lượt đồng thời sát trần, retry hoặc timeout usage unknown | nhận/đối soát | không overspend; giữ reserve khi chưa rõ usage; không hoàn bằng 0 |
| AC-AIN-010-01 | FR-AIN-CONF-001 | quyền và policy thay đổi đã duyệt | đề nghị đổi hạn mức | audit trước/sau/lý do/version; hiệu lực đúng workflow |
| AC-AIN-010-02 | FR-AIN-CONF-001 | thiếu quyền hoặc chưa quyết định cơ chế duyệt | đổi | 403 hoặc policy closed; không tăng quota |
| AC-AIN-010-03 | FR-AIN-CONF-001 | giảm cap thấp hơn spent+reserved hoặc version cũ | đổi | không hủy debt/ghi quá khứ; chặn admission mới, conflict 409 khi version cũ |
| AC-AIN-011-01 | FR-AIN-SAFE-001 | agent chỉ có quyền AIN và projection sạch | gọi catalog được phép | chỉ trường allowlist; credential không SELECT bảng cấm |
| AC-AIN-011-02 | FR-AIN-SAFE-001 | prompt chèn lệnh, tool alias/SQL/URL hoặc request cost gián tiếp | gọi tool | 403/deny trước truy cập, không chạy công cụ cấm |
| AC-AIN-011-03 | FR-AIN-SAFE-001 | cost nằm trong nested error/log/giải thích/cache hoặc chuỗi suy giá suất | trả kết quả | không lộ bất kỳ giá trị/ratio/chiết khấu; chặn cả kênh phụ |
| AC-AIN-012-01 | FR-AIN-MED-001 | nội dung nhắc và rubric đã duyệt | câu hỏi về bệnh lý | có đúng lời nhắc được duyệt và không chẩn đoán/điều trị |
| AC-AIN-012-02 | FR-AIN-MED-001 | chưa duyệt nội dung lời nhắc | cố mở hội thoại thật | BLOCKED; mock chỉ ghi nội dung chờ xác nhận |
| AC-AIN-012-03 | FR-AIN-MED-001 | nội dung sức khỏe xen trong yêu cầu đổi món | tiếp nhận | không lưu/suy ra hồ sơ, không tự coi là kiêng nguyên liệu thông thường |
| AC-AIN-013-01 | FR-AIN-LOG-001 | usage confirmed có nguồn và quyền xem | đối soát ngày | tổng AI đúng ledger/đơn vị và policyVersion, không cost nguyên liệu |
| AC-AIN-013-02 | FR-AIN-LOG-001 | usage missing/provider lỗi | xem báo cáo | UNKNOWN cùng reservation, không báo còn đủ tiền giả |
| AC-AIN-013-03 | FR-AIN-LOG-001 | sự kiện trùng/đến muộn qua ranh giới ngày | đối soát | một lần theo eventId; gắn ngày theo policy được duyệt; không reset debt |
