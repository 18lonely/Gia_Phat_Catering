---
id: DOC-E8-USECASES-UC-PUB-002-MD
title: "UC-PUB-002: Xem tin và bài viết"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-002: Xem tin và bài viết

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-BLOG-001 · FEAT-055 · P0 · US-PUB-002.

Level: Sea level. Actor chính: Khách vãng lai đọc tin Gia Phát. Bên quan tâm: người soạn cần bài chưa công bố không bị tìm thấy qua mặt tiền công khai.

Trigger: Khách tìm bài viết về Gia Phát qua mục tin tức hoặc đường dẫn bài đã biết.

Tiền điều kiện (nghiệp vụ): Khách truy cập danh sách hoặc có slug bài; không yêu cầu tài khoản.
Tiền điều kiện (gate còn mở): E8-Q01/08 về nguồn bài cũ và quyền xuất bản chưa chốt; không lấy bản chuyển nháp làm bài công khai.

Luồng chính:
1. Khách chọn bộ lọc và trang danh sách tại UI-PUB-02.
2. Hệ thống tìm các bài được phép công khai theo bộ lọc và quy ước phân trang được duyệt.
3. Hệ thống trả danh sách với tiêu đề và metadata công khai; bài chưa duyệt không có trong danh sách, sitemap hay kết quả tìm kiếm.
4. Khách chọn một bài; hệ thống tra slug và kiểm lại revision còn được phép đọc công khai.
5. Hệ thống trả tiêu đề, nội dung và media đúng revision của bài để khách đọc; không ghi trạng thái bài.

Hậu điều kiện thành công: Khách nhận danh sách/chi tiết bài công khai đúng nguồn; revision và trạng thái nghiệp vụ không đổi.
Bảo đảm tối thiểu: Không trả raw HTML chưa an toàn hoặc metadata nội bộ; GET không tạo lead hay xuất bản bài.

Extensions:
- 2a. Không có bài phù hợp: hệ thống trả danh sách rỗng; không tạo bài giả, dữ liệu giữ nguyên.
- 4a. Bài chưa duyệt, thu hồi hoặc không tồn tại: hệ thống trả ERR-PUB-404-01, không lộ bản nháp; khách có thể về danh sách.
- 2b. Nguồn/quyền công khai chưa đủ: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q01/08; không dùng policy mặc định.
- 4b. Revision thay đổi trong lúc đọc: hệ thống kiểm lại bản được phép; không dùng bản đã thu hồi để trả chi tiết.
- 5a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01 và thông báo an toàn; dữ liệu bài không đổi.

[API](../api/api-spec.md) API-PUB-002; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
