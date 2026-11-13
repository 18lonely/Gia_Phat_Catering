---
id: DOC-E8-USECASES-UC-PUB-001-MD
title: "UC-PUB-001: Xem trang giới thiệu"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-001: Xem trang giới thiệu

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-PAGE-001 · FEAT-054 · P0 · US-PUB-001.

Level: Sea level. Actor chính: Khách vãng lai tìm hiểu dịch vụ Gia Phát. Bên quan tâm: Gia Phát cần chỉ đưa nội dung được phép ra công khai.

Trigger: Khách tìm hiểu năng lực Gia Phát và truy cập trang giới thiệu, dịch vụ, dự án hoặc đối tác theo đường dẫn trang.

Tiền điều kiện (nghiệp vụ): Có slug cần tra cứu; khách không cần tài khoản để đọc nội dung công khai.
Tiền điều kiện (gate còn mở): E8-Q08 chưa chốt quyền/quy trình xuất bản; không coi mọi revision đã có là được công khai.

Luồng chính:
1. Khách truy cập slug trang thuộc UI-PUB-01.
2. Hệ thống tra trang tương ứng và xác định revision được phép xuất bản.
3. Hệ thống lấy nội dung, media và metadata thuộc tập trường công khai, loại dữ liệu quản trị/nội bộ khỏi phản hồi.
4. Hệ thống trả nội dung đúng revision cùng liên kết tới dịch vụ, dự án và đối tác được công khai.
5. Khách đọc trang và chọn liên kết liên quan; hệ thống tiếp tục phục vụ theo quyền công khai của trang đích.

Hậu điều kiện thành công: Khách xem đúng nội dung xuất bản và điều hướng tới trang liên quan; dữ liệu nghiệp vụ không đổi.
Bảo đảm tối thiểu: GET không công bố revision hay tạo lead; không tiết lộ bản nháp, cost hoặc dữ liệu khách nội bộ.

Extensions:
- 2a. Slug không có nội dung công khai, thuộc bản nháp hoặc đã thu hồi: hệ thống trả ERR-PUB-404-01 và hướng về danh sách; không lộ sự tồn tại bản nháp, dữ liệu giữ nguyên.
- 2b. Chưa có policy cho nhánh xuất bản: hệ thống báo chưa đủ điều kiện ERR-PUB-422-02, giữ BLOCKED E8-Q08; không tự công bố.
- 3a. Nguồn không khả dụng: hệ thống trả ERR-PUB-503-01 với thông báo an toàn; không giả trang đã tải và không thay dữ liệu.
- 4a. Revision nguồn thay đổi trước lúc trả trang: hệ thống kiểm lại bản được phép công khai; không phát tán revision cũ đã bị thu hồi.

[API](../api/api-spec.md) API-PUB-001; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
