---
id: DOC-E8-USERSTORIES-ACCEPTANCE-CRITERIA-MD
title: Acceptance criteria Given / When / Then
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Acceptance criteria Given / When / Then

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Làm rõ AC-PUB-003-H (cùng AC, không tăng số lượng): Given bản xuất synthetic có sourceId/body/media/ngày gốc và policy chuyển đã duyệt; When chuẩn bị chuyển bài và mapping; Then có nháp với provenance và đối chiếu nội dung, giữ ngày gốc, không nhân đôi sourceId khi chạy lại, không tự công bố. AC-PUB-003-E bao gồm media thiếu/bài trùng hoặc đã xóa chưa quyết định → ngoại lệ BLOCKED. Evidence runtime ở TC-PUB-S05.

| AC | FR | Given / When / Then |
| :--- | :--- | :--- |
| AC-PUB-001-H | FR-PUB-PAGE-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Xem trang giới thiệu; Then Nội dung xuất bản khớp revision và điều hướng đúng |
| AC-PUB-001-E | FR-PUB-PAGE-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Xem trang giới thiệu; Then Slug nháp/thu hồi trả 404, không lộ bản nháp |
| AC-PUB-001-B | FR-PUB-PAGE-001 | Given chưa có quyết định E8-Q08; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q08; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-002-H | FR-PUB-BLOG-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Xem tin và bài viết; Then Bài synthetic đã xuất bản hiện đúng tiêu đề/nội dung |
| AC-PUB-002-E | FR-PUB-BLOG-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Xem tin và bài viết; Then Bài chưa duyệt không có trong list, sitemap hoặc tìm kiếm |
| AC-PUB-002-B | FR-PUB-BLOG-001 | Given chưa có quyết định E8-Q01/08; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q01/08; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-003-H | FR-PUB-URLM-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Chuẩn bị mapping WordPress; Then Inventory synthetic đầy đủ có từng URL, kết quả rà và provenance |
| AC-PUB-003-E | FR-PUB-URLM-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Chuẩn bị mapping WordPress; Then Thiếu DL-08 hoặc bài đã xóa chưa có quyết định giữ BLOCKED, không tự chuyển về trang chủ |
| AC-PUB-003-B | FR-PUB-URLM-001 | Given chưa có quyết định E8-Q01/02; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q01/02; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-004-H | FR-PUB-URLR-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Phục vụ URL cũ; Then URL synthetic đã map trả đúng trang hoặc 301 tới đích đúng |
| AC-PUB-004-E | FR-PUB-URLR-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Phục vụ URL cũ; Then Mapping vòng lặp/đích nháp không được kích hoạt; URL ngoài inventory không giả thành bài cũ |
| AC-PUB-004-B | FR-PUB-URLR-001 | Given chưa có quyết định E8-Q01/02; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q01/02; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-005-H | FR-PUB-MENU-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Xem thực đơn mẫu có giá; Then Nguồn hợp lệ trả đủ giá được phép, định lượng theo suất, 4 chỉ số có đơn vị, dị ứng |
| AC-PUB-005-E | FR-PUB-MENU-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Xem thực đơn mẫu có giá; Then Giá chưa được phép hoặc nguồn stale/missing chặn phần phụ thuộc; thiếu không thành 0 hay không dị ứng |
| AC-PUB-005-B | FR-PUB-MENU-001 | Given chưa có quyết định E8-Q03/04; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q03/04; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-006-H | FR-PUB-TRY-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Dựng thử thực đơn tuần; Then Khi policy có căn cứ, kết quả tuần mẫu đúng đầu vào và mang nhãn mẫu, chưa đặt hàng |
| AC-PUB-006-E | FR-PUB-TRY-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Dựng thử thực đơn tuần; Then Số âm/lẻ bị từ chối; tổ hợp vô nghiệm không nới quy tắc cứng; chưa chốt engine trả BLOCKED |
| AC-PUB-006-B | FR-PUB-TRY-001 | Given chưa có quyết định E8-Q05/04; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q05/04; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-007-H | FR-PUB-LEAD-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Gửi form tư vấn; Then Với policy đã duyệt, form hợp lệ tạo một bản ghi kèm source và trialRef hợp lệ nếu có |
| AC-PUB-007-E | FR-PUB-LEAD-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Gửi form tư vấn; Then Không consent thì không ghi; mất phản hồi không gửi lại bằng định danh mới; chưa chọn nơi lưu thì BLOCKED |
| AC-PUB-007-B | FR-PUB-LEAD-001 | Given chưa có quyết định E8-Q06/07; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q06/07; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-008-H | FR-PUB-RELY-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Theo dõi điểm nối lead; Then Bản ghi đã lưu nhưng chưa receipt hiển thị chờ E10; giữ source/trialRef |
| AC-PUB-008-E | FR-PUB-RELY-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Theo dõi điểm nối lead; Then CRM không khả dụng không mất lead và không báo đã đồng bộ; GET không gửi thông báo hay bàn giao |
| AC-PUB-008-B | FR-PUB-RELY-001 | Given chưa có quyết định E8-Q06/07/11; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q06/07/11; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-009-H | FR-PUB-EDIT-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Soạn và sửa nội dung; Then Bản nháp hợp lệ lưu revision, bản công khai cũ giữ nguyên |
| AC-PUB-009-E | FR-PUB-EDIT-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Soạn và sửa nội dung; Then Version cũ trả 409; HTML có script không được thực thi hoặc phát tán |
| AC-PUB-009-B | FR-PUB-EDIT-001 | Given chưa có quyết định E8-Q08/09; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q08/09; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-010-H | FR-PUB-PREV-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Xem trước nội dung; Then Người có quyền xem đúng bản nháp với nhãn xem trước |
| AC-PUB-010-E | FR-PUB-PREV-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Xem trước nội dung; Then Khách đoán URL không đọc được nháp; stale revision có cảnh báo |
| AC-PUB-010-B | FR-PUB-PREV-001 | Given chưa có quyết định E8-Q08; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q08; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-011-H | FR-PUB-PUBL-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Yêu cầu công bố hoặc thu hồi; Then Khi policy được duyệt, thao tác hợp lệ công bố đúng revision, thu hồi chặn truy cập |
| AC-PUB-011-E | FR-PUB-PUBL-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Yêu cầu công bố hoặc thu hồi; Then Thiếu quyền/duyệt hoặc bản đã đổi không công bố; không tự coi người soạn có quyền duyệt |
| AC-PUB-011-B | FR-PUB-PUBL-001 | Given chưa có quyết định E8-Q08/09/02; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q08/09/02; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |
| AC-PUB-012-H | FR-PUB-MEDI-001 | Given nguồn hợp lệ và policy liên quan đã được xác nhận; When Quản lý ảnh và banner; Then Ảnh synthetic hợp lệ có alt và gắn revision nội dung, chưa tự công khai |
| AC-PUB-012-E | FR-PUB-MEDI-001 | Given đầu vào hoặc quyền không hợp lệ như tình huống dưới; When Quản lý ảnh và banner; Then File private/không an toàn không vào public; ảnh đang dùng không bị gỡ âm thầm |
| AC-PUB-012-B | FR-PUB-MEDI-001 | Given chưa có quyết định E8-Q09/08; When thực hiện nhánh phụ thuộc; Then Giữ BLOCKED E8-Q09/08; không ghi/công bố hoặc bịa dữ liệu phụ thuộc |

