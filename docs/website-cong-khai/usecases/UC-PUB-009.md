---
id: DOC-E8-USECASES-UC-PUB-009-MD
title: "UC-PUB-009: Soạn và sửa nội dung"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-009: Soạn và sửa nội dung

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-EDIT-001 · FEAT-059 · P0 · US-PUB-009.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH trong vai trò người soạn được cấp quyền. Bên quan tâm: khách cần bản công khai ổn định; người soạn cần giữ bản sửa để review.

Trigger: Người soạn có nội dung trang, bài viết hoặc banner cần bổ sung/chỉnh sửa trước khi công bố.

Tiền điều kiện (nghiệp vụ): Người soạn có phiên và quyền soạn; khi sửa phải có content và version đang làm việc.
Tiền điều kiện (gate còn mở): E8-Q08/09 về CMS, quyền và media chưa chốt; persona không tự cấp quyền runtime.

Luồng chính:
1. Người soạn chọn nội dung tại UI-PUB-06, xem revision/version đang sửa hoặc bắt đầu nháp mới.
2. Người soạn nhập loại trang/bài/banner, title, body, slug và mediaRefs; gửi version khi cập nhật bản đã có.
3. Hệ thống kiểm phiên/quyền thao tác, slug, trường được phép và version; không nhận cờ công khai qua lệnh sửa.
4. Hệ thống kiểm nội dung HTML và media theo chính sách an toàn, không để script được thực thi/phát tán.
5. Hệ thống ghi revision nháp và audit, trả bản nháp/version mới; revision đang công khai giữ nguyên.

Hậu điều kiện thành công: Nội dung sửa nằm trong revision nháp có dấu vết; chưa thay trang công khai.
Bảo đảm tối thiểu: Không dùng quyền soạn thay quyền công bố; không ghi thành công một phần khi lỗi và không lộ dữ liệu nội bộ qua nội dung.

Extensions:
- 3a. Version cũ: hệ thống trả ERR-PUB-409-01, yêu cầu tải lại để đối chiếu; không ghi đè bản mới.
- 3b. Hết phiên/thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01; nháp chưa được ghi.
- 4a. HTML có script hoặc media chưa an toàn: hệ thống ngăn thực thi/phát tán và yêu cầu rà nội dung; bản công khai giữ nguyên, chưa báo nháp hợp lệ.
- 3c. Policy quyền/media chưa đủ: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q08/09; không tự chọn CMS hay quyền.
- 5a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-PUB-500-01 và requestId để đối soát; kết quả lưu chưa rõ, không gửi lệnh mới để ghi đè.

[API](../api/api-spec.md) API-PUB-009; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
