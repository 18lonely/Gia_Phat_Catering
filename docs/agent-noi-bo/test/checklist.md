---
id: DOC-AGENT-NOI-BO-TEST-CHECKLIST
title: Checklist — Agent Nội bộ
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Checklist — Agent Nội bộ

**Draft — thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

Mỗi mục dưới là checklist thiết kế, chưa có dấu PASS phần mềm. QA/BA chưa ký duyệt. [Test case](test-cases.md) và [RTM](traceability.md) là nguồn ca cụ thể.

| Nhóm | Nội dung cần kiểm | Bằng chứng khi chạy |
| :--- | :--- | :--- |
| Chức năng | Happy/negative/boundary của từng story; trạng thái trước/sau; hủy trước ghi | Response và dữ liệu/audit sau thao tác |
| Dữ liệu | 0 khác null, ngày hiệu lực, version cũ, dữ liệu nguồn đổi | Input snapshot và kết quả độc lập |
| Quyền | Gọi API trực tiếp ngoài scope; thu hồi quyền giữa tác vụ; lọc trường nhạy cảm | Log đã lọc và response không rò dữ liệu |
| Cạnh tranh | Hai lệnh cùng version/key; mất phản hồi sau commit; retry | Chỉ một hiệu ứng nghiệp vụ; audit nhất quán |
| Phụ thuộc | DB/queue/provider lỗi; timeout; không lấy số giả thay nguồn thiếu | Kết quả lỗi và trạng thái cuối truy vết được |
| UI | Offline/loading/empty/error; bàn phím;360/390/1440px; XSS text | Ảnh và log trình duyệt, phân biệt wireframe và sản phẩm |
| NFR | Tải, độ chính xác, audit và latency theo SRS | Build,môi trường,profile,actual; không chỉ ảnh giao diện |
