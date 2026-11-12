---
id: DOC-E8-USECASES-UC-PUB-004-MD
title: UC-PUB-004 — Phục vụ URL cũ
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-004 — Phục vụ URL cũ

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-URLR-001 · FEAT-055 · P0 · US-PUB-004.

Level: Sea level. Actor chính: Khách vãng lai đi theo URL bài viết cũ. Bên quan tâm: Gia Phát cần giữ khả năng truy cập bài sau chuyển đổi.

Trigger: Khách bấm một liên kết WordPress cũ từ kết quả tìm kiếm hoặc dấu trang.

Tiền điều kiện — nghiệp vụ: URL được gửi tới website; luồng thành công cần mapping đã duyệt và đích công khai hợp lệ.
Tiền điều kiện — gate còn mở: E8-Q01/02 chưa chốt inventory, mapping và cách xử lý URL ngoại lệ. UI-PUB-07 là màn quản trị mapping để review, không phải màn khách phải chọn.

Luồng chính:
1. Trình duyệt khách gửi yêu cầu đọc URL cũ tới website.
2. Hệ thống đối chiếu nguyên URL với inventory và mapping đã được duyệt, không kích hoạt mapping từ yêu cầu GET.
3. Hệ thống kiểm đích còn công khai và mapping không tạo vòng lặp hay chuyển hướng tới URL tùy ý.
4. Với KEEP, handler website trả HTTP 200 cùng nội dung đúng; với REDIRECT, handler trả HTTP 301 và Location đã được duyệt tại URL khách truy cập.
5. Trình duyệt hiển thị nội dung hoặc theo Location tới trang đích; hệ thống chỉ phục vụ dữ liệu công khai.

Hậu điều kiện thành công: URL cũ dẫn tới đúng nội dung theo mapping; không thay revision, lead hoặc trạng thái mapping.
Bảo đảm tối thiểu: Không dùng phản hồi API logic thay bằng chứng HTTP 200/301 của website; không lộ nháp và không tạo open redirect.

Extensions:
- 2a. URL ngoài inventory hoặc bài xóa chưa có quyết định: hệ thống không giả thành bài cũ đã map; nhánh chưa đủ căn cứ giữ BLOCKED E8-Q01/02, mapping không đổi.
- 3a. Vòng lặp hoặc đích nháp: hệ thống chặn mapping với ERR-PUB-422-03; không phát Location sai và không công khai đích nháp.
- 2b. Policy/nguồn chưa đủ: hệ thống trả ERR-PUB-422-02; không tự chọn KEEP hay REDIRECT.
- 3b. Đích thay revision/thu hồi: hệ thống kiểm lại quyền công khai, không dùng đích cũ đã mất hiệu lực; mapping không được tự sửa qua GET.
- 4a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01 với thông báo an toàn; không giả chuyển hướng thành công, dữ liệu giữ nguyên.

[API](../api/api-spec.md) API-PUB-004; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
