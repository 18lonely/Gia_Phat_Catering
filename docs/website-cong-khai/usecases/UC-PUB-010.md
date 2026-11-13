---
id: DOC-E8-USECASES-UC-PUB-010-MD
title: "UC-PUB-010: Xem trước nội dung"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-010: Xem trước nội dung

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-PREV-001 · FEAT-059 · P0 · US-PUB-010.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH trong vai trò người soạn có quyền xem trước. Bên quan tâm: người review cần đúng bản nháp, khách không được đọc bản chưa công bố.

Trigger: Người soạn cần kiểm tra cách hiển thị của revision vừa chuẩn bị trước khi xin công bố.

Tiền điều kiện (nghiệp vụ): Có contentId và revision nháp; người xem có phiên và quyền xem trước nội dung.
Tiền điều kiện (gate còn mở): E8-Q08 chưa chốt vai trò/quy trình; không tự coi đường dẫn preview là quyền truy cập.

Luồng chính:
1. Người soạn chọn contentId và revision cần xem trước tại UI-PUB-06.
2. Hệ thống xác thực phiên, quyền xem trước và phạm vi nội dung của người yêu cầu.
3. Hệ thống đọc đúng revision được yêu cầu và đối chiếu trạng thái nguồn để nhận diện bản đã thay đổi.
4. Hệ thống render nội dung/media an toàn và gắn nhãn nháp/xem trước.
5. Hệ thống trả bản xem trước chỉ trong phạm vi được phép; không đưa preview vào public cache hoặc index.

Hậu điều kiện thành công: Người soạn xem đúng revision nháp; trạng thái xuất bản và dữ liệu nghiệp vụ không đổi.
Bảo đảm tối thiểu: GET không xuất bản; khách đoán URL không được đọc nháp, không thực thi script từ nội dung.

Extensions:
- 2a. Phiên thiếu/hết hạn hoặc thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; không render bản nháp cho người yêu cầu.
- 3a. Nội dung không có hoặc ngoài scope: hệ thống trả ERR-PUB-404-01; không tiết lộ nội dung nháp, dữ liệu giữ nguyên.
- 3b. Revision đã cũ: hệ thống cảnh báo bản thay đổi để người soạn kiểm lại; không tự ghi hay công bố bản mới.
- 2b. Policy chưa được chọn: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q08; không mở preview công khai để vượt gate.
- 4a. Dịch vụ không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có preview hợp lệ, revision không đổi.

[API](../api/api-spec.md) API-PUB-010; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
