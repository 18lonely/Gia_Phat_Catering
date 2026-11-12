---
id: DOC-E10-USECASES-UC-CRM-011-MD
title: UC-CRM-011 — Đính kèm thực đơn có phiên bản vào báo giá
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-011 — Đính kèm thực đơn có phiên bản vào báo giá

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-072. Cấp độ: Sea level — mục tiêu người dùng.

Tác nhân chính: Dinh dưỡng viên kiêm chăm sóc khách hàng. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần gửi đúng thực đơn đã tư vấn và truy lại được khi thương lượng; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-SALE-MENU-001 ↔ UC-CRM-011 ↔ US-CRM-011; API-CRM-011; UI-CRM-06.

## Kích hoạt

Dinh dưỡng viên kiêm chăm sóc khách hàng cần đính kèm thực đơn có phiên bản vào báo giá để gửi đúng thực đơn đã tư vấn và truy lại được khi thương lượng, từ màn UI-CRM-06 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: quoteRevision, menuRef, menuRevision, sourceHash, phạm vi dùng cho khách.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q09; E9-Q06/12; O-02; NUTR-Q01–04; E8-Q04. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-06 hoặc gọi API-CRM-011, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp quoteRevision, menuRef, menuRevision, sourceHash, phạm vi dùng cho khách; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm quyền và nguồn MENU được phép theo Q09; chụp projection khách gắn đúng revision báo giá; thực đơn E9 chỉ là đề xuất cần người thật xử lý, không coi receipt là MENU được duyệt.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Tệp/nội dung thực đơn được phép và provenance; không tự sửa MENU hoặc dùng bản hiện hành động.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Tệp/nội dung thực đơn được phép và provenance; không tự sửa MENU hoặc dùng bản hiện hành động. Có bằng chứng nguồn và dấu vết thay đổi có thể đối soát theo requestId.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q09; E9-Q06/12; O-02; NUTR-Q01–04; E8-Q04; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. nguồn thực đơn bị thu hồi hoặc chỉ có nháp E9 chưa duyệt: khi đính kèm để phát hành báo giá, hệ thống ERR-CRM-422-01 hoặc BLOCKED theo nguồn; không tự công bố MENU. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. MENU có bản mới sau khi báo giá đã phát hành: khi mở lại báo giá cũ, hệ thống giữ đúng bản đính kèm cũ và cảnh báo nguồn; muốn thay phải tạo revision mới.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-011: POST /v1/crm/quotes/{id}/menu-attachments. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
