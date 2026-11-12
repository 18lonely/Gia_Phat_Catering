---
id: DOC-E8-USECASES-UC-PUB-012-MD
title: UC-PUB-012 — Quản lý ảnh và banner
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-012 — Quản lý ảnh và banner

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-MEDI-001 · FEAT-059 · P0 · US-PUB-012.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH trong vai trò quản trị nội dung được cấp quyền media. Bên quan tâm: khách cần ảnh an toàn; Gia Phát cần quyền sử dụng ảnh và biết nơi đang dùng.

Trigger: Người quản trị chuẩn bị ảnh/banner cho nội dung hoặc cần thay/gỡ ảnh đã gắn vào trang.

Tiền điều kiện — nghiệp vụ: Có fileRef, thông tin quyền sử dụng và nội dung/vị trí liên quan; người thao tác có phiên và quyền quản lý media.
Tiền điều kiện — gate còn mở: E8-Q09/08 chưa chốt loại/dung lượng ảnh, vị trí/lịch và quyền public asset; không tự mở loại ảnh mới.

Luồng chính:
1. Người quản trị chọn ảnh/banner tại UI-PUB-09 và cung cấp fileRef.
2. Người quản trị nhập altText, vị trí banner, quyền sử dụng và version khi cập nhật.
3. Hệ thống kiểm quyền thao tác, version, loại file an toàn và quyền đưa ảnh ra công khai.
4. Hệ thống đọc các vị trí/revision đang sử dụng ảnh để người quản trị rà tác động trước thay/gỡ.
5. Khi đủ điều kiện, hệ thống lưu media metadata nháp gắn với nội dung và audit, trả danh sách vị trí sử dụng; không tự công khai ảnh.

Hậu điều kiện thành công: Metadata ảnh có alt và liên kết nội dung, đủ nguồn quyền sử dụng để review; công khai vẫn theo workflow nội dung.
Bảo đảm tối thiểu: Không lộ storage_key/file riêng; ảnh đang dùng không bị gỡ âm thầm, không ghi một phần khi lỗi.

Extensions:
- 3a. File không thuộc loại ảnh an toàn được phép: hệ thống trả ERR-PUB-415-01; chưa ghi media hợp lệ hoặc đưa ảnh lên public.
- 3b. File private/thiếu quyền công khai hoặc policy: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q09/08; file không trở thành public.
- 4a. Ảnh đang được sử dụng: hệ thống hiển thị các vị trí để rà; khi chưa đủ quyết định gỡ/thay, liên kết đang dùng giữ nguyên.
- 3c. Phiên hết hạn/thiếu quyền hoặc version đã đổi: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01/ERR-PUB-409-01 tương ứng; không ghi đè metadata.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01 và mã yêu cầu để đối soát; trạng thái lưu chưa rõ, không báo hoàn tất.

[API](../api/api-spec.md) API-PUB-012; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
