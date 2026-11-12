---
id: DOC-E8-USECASES-UC-PUB-003-MD
title: UC-PUB-003 — Chuẩn bị mapping WordPress
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-003 — Chuẩn bị mapping WordPress

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-URLM-001 · FEAT-055 · P0 · US-PUB-003.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH trong vai trò quản trị nội dung, chỉ khi được cấp quyền. Bên quan tâm: khách cần đường dẫn cũ còn tới đúng bài; Gia Phát cần bảo toàn nội dung nguồn.

Trigger: Gia Phát nhận bản xuất WordPress và cần đối chiếu bài/URL trước chuyển website.

Tiền điều kiện — nghiệp vụ: Có inventoryRef và bản xuất bài/media có provenance để rà; người thực hiện có quyền soạn và chuẩn bị mapping.
Tiền điều kiện — gate còn mở: E8-Q01/02 chặn inventory và tiêu chí KEEP/REDIRECT; E8-Q01/08/09 chặn cách chuyển nội dung/CMS/media. Không chọn importer hoặc cutover trong UC.

Luồng chính:
1. Người quản trị nạp thông tin inventory tại UI-PUB-07 và đối chiếu từng sourceId, URL nguồn, title/body/media/ngày công bố gốc trong DL-08.
2. Người quản trị chuẩn bị nội dung nháp theo quyền soạn; hệ thống làm sạch HTML, giữ provenance và ngày gốc riêng ngày chuyển.
3. Hệ thống kiểm sourceId đã có để không nhân đôi bài khi chuẩn bị lại; người quản trị đối chiếu nội dung, ảnh và liên kết với bản nguồn.
4. Người quản trị khai báo URL nguồn, target, KEEP/REDIRECT và revision; giữ ánh xạ sourceId tới contentRef/revision và targetPath.
5. Hệ thống kiểm quyền, revision, URL trùng, đích công khai và vòng lặp; liệt kê ngoại lệ theo từng URL, không bỏ khỏi mẫu số.
6. Hệ thống lưu bảng mapping nháp, kết quả đối chiếu và dấu vết; trả danh sách chặn để người quản trị rà.
7. Người quản trị kiểm lại nháp; nội dung chỉ công bố qua UC-PUB-011 khi đủ điều kiện, mapping chưa tự kích hoạt.

Hậu điều kiện thành công: Bảng mapping nháp có nguồn từng URL và kết quả đối chiếu nội dung; chưa có thay đổi website công khai.
Bảo đảm tối thiểu: Không báo đạt đủ URL khi thiếu inventory; không tự chuyển bài xóa về trang chủ hoặc công bố nháp sau chuyển.

Extensions:
- 1a. Thiếu DL-08: hệ thống báo ERR-PUB-422-02 và BLOCKED E8-Q01/02; chưa có căn cứ tính độ phủ URL.
- 3a. Media thiếu, bài trùng hoặc đã xóa chưa có quyết định: hệ thống ghi ngoại lệ BLOCKED; giữ dòng trong inventory, không nhân đôi hoặc tự chọn đích.
- 5a. Mapping vòng lặp, trùng nguồn hoặc đích không công khai: hệ thống trả ERR-PUB-422-03; không kích hoạt mapping sai.
- 5b. Revision đã đổi: hệ thống trả ERR-PUB-409-01, yêu cầu tải lại đối chiếu; không ghi đè bản mới.
- 5c. Hết phiên/thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01; chưa lưu thay đổi mapping.
- 6a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01, giữ requestId để đối soát; chưa xác định đã ghi hay chưa, không báo hoàn tất.

[API](../api/api-spec.md) API-PUB-003; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
