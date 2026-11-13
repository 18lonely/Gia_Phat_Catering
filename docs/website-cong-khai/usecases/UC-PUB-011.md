---
id: DOC-E8-USECASES-UC-PUB-011-MD
title: "UC-PUB-011: Yêu cầu công bố hoặc thu hồi"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-011: Yêu cầu công bố hoặc thu hồi

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-PUBL-001 · FEAT-059 · P0 · US-PUB-011.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH chỉ khi được cấp riêng quyền công bố/thu hồi. Bên quan tâm: khách cần đúng bản công khai; người duyệt cần quyết định có dấu vết. Việc gán quyền cho persona còn chờ xác nhận.

Trigger: Nội dung đã được chuẩn bị để công bố, hoặc Gia Phát cần ngừng cho khách truy cập một revision đang công khai.

Tiền điều kiện (nghiệp vụ): Có contentId, revision và lý do thao tác; người yêu cầu có quyền tương ứng theo policy được duyệt.
Tiền điều kiện (gate còn mở): E8-Q08/09/02 về duyệt, media và URL chưa chốt; không coi người soạn mặc nhiên có quyền duyệt/công bố.

Luồng chính:
1. Người có quyền chọn nội dung/revision tại UI-PUB-06 và rà bản muốn công bố hoặc thu hồi.
2. Người đó gửi contentId, revision, action và lý do thao tác.
3. Hệ thống kiểm phiên/quyền, policy duyệt và điều kiện độc lập người duyệt nếu workflow có duyệt.
4. Hệ thống kiểm revision, media và URL của nội dung đúng điều kiện công khai/thu hồi.
5. Khi đủ điều kiện, hệ thống ghi quyết định công bố hoặc thu hồi cùng audit, bảo đảm cache phản ánh quyết định.
6. Hệ thống trả revision công khai hoặc trạng thái thu hồi; bản đã thu hồi không tiếp tục được phục vụ công khai.

Hậu điều kiện thành công: Đúng revision được công bố/thu hồi và có dấu vết; trạng thái public phù hợp quyết định.
Bảo đảm tối thiểu: Không tự chọn workflow duyệt, TTL/purge hoặc cấp quyền; lỗi không báo thành công một phần, không phát tán nháp.

Extensions:
- 3a. Thiếu phiên/quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; trạng thái công bố giữ nguyên.
- 3b. Chưa có policy hoặc thiếu điều kiện duyệt: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q08/09/02; chưa công bố/thu hồi.
- 4a. Revision đã thay đổi: hệ thống trả ERR-PUB-409-01, yêu cầu rà lại; không áp quyết định cũ cho bản mới.
- 4b. Media/URL chưa đủ điều kiện: hệ thống trả ERR-PUB-422-02; không công bố nội dung không an toàn.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01, giữ requestId để đối soát; chưa xác định hoàn tất, không báo public đã đổi thành công.

[API](../api/api-spec.md) API-PUB-011; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
