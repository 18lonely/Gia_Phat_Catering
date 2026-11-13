---
id: DOC-NEN-TANG-REVIEW-QUESTIONS
title: Câu hỏi thiết kế nền tảng
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# Câu hỏi thiết kế nền tảng

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-12; E1-Q06 |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Giữ N-01–04, O-04, O-06, Q-14, Q-18 tại SRS. Các câu mới đều CHỜ XÁC NHẬN, chưa có người/ngày phê duyệt.

| Mã | Câu hỏi | Vai trò | Tác động / hướng đề xuất | Trả lời |
| :--- | :--- | :--- | :--- | :--- |
| E1-Q01 | Thống nhất envelope lỗi và page/cursor giữa E1 và E3/E4/E5 thế nào? | Tech lead, BA | E1/E2 giữ chuẩn SRS page; các extension cursor/envelope ghi ngoại lệ đề xuất, chưa coi API toàn hệ thống đã nhất quán |  |
| E1-Q02 | Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không? | Tech lead | Không replay mật khẩu tạm; backend store/transaction chưa có |  |
| E1-Q03 | MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể? | Giám đốc, Tech lead | P1 gated; không tự triển khai chỉ dựa ô nhập6 số |  |
| E1-Q04 | Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu? | BA, Tech lead | Đề xuất NEW→SEEN→RESOLVED; bảng notifications hiện chưa có version/event key; cần delta trước backend |  |
| E1-Q05 | Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào? | Giám đốc | Chưa thêm quyền nghiệp vụ cho QUAN_TRI; cần quyết định trước vận hành |  |
| E1-Q06 | NFR-PERF-003 đo ký tự nội dung đầu hay phản hồi tiến trình đầu; mốc bắt đầu, kết thúc và cách đo với polling là gì? | chưa rõ | BLOCKED kết luận đạt phép đo phản hồi đầu E1/E5. XC-12; DEC-198. Nguồn đề xuất phản hồi tiến trình đầu; chưa chọn thay NFR gốc. |  |

NFR-PERF-003 nói ký tự đầu≤5 giây nhưng E5 dùng polling2 giây: đề xuất coi đây là phản hồi tiến trình đầu tiên, không phải token AI đầu tiên; cần xác nhận cùng AIO-Q01, không tự đổi NFR gốc.

> Chờ E1-Q06 — XC-12. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-12](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.
