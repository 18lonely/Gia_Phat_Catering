---
id: DOC-E10-USECASES-UC-CRM-002-MD
title: UC-CRM-002 — Ghi nháp thông tin liên hệ CRM
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-002 — Ghi nháp thông tin liên hệ CRM

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-070. Cấp độ: Sea level — mục tiêu người dùng.

Tác nhân chính: Dinh dưỡng viên kiêm chăm sóc khách hàng. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần lưu đầu mối có nguồn xác minh; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-CUS-CONT-001 ↔ UC-CRM-002 ↔ US-CRM-002; API-CRM-002; UI-CRM-01.

## Kích hoạt

Dinh dưỡng viên kiêm chăm sóc khách hàng cần ghi nháp thông tin liên hệ crm để lưu đầu mối có nguồn xác minh, từ màn UI-CRM-01 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: customerRef, tên liên hệ, vai trò liên hệ, phương thức liên hệ, nguồn xác minh.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q01; E6-CG-08. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-01 hoặc gọi API-CRM-002, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, tên liên hệ, vai trò liên hệ, phương thức liên hệ, nguồn xác minh; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm quyền và dữ liệu tối thiểu theo chính sách được duyệt; lưu bản nháp liên hệ gắn khách tham chiếu, không tạo khách chủ hoặc tài khoản đặt món.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Bản nháp liên hệ có version và audit; khách chủ và điểm phục vụ không đổi.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Bản nháp liên hệ có version và audit; khách chủ và điểm phục vụ không đổi. Có bằng chứng nguồn và dấu vết thay đổi có thể đối soát theo requestId.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q01; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. yêu cầu chứa role quản trị hoặc customerId ngoài phạm vi: khi gửi nháp liên hệ, hệ thống từ chối trường lạ hoặc phạm vi; không cấp quyền đặt món. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. quyết định thời gian lưu và xử lý xóa chưa có: khi yêu cầu lưu hoặc xóa thông tin liên hệ thật, hệ thống giữ BLOCKED E10-Q01; không dùng thời gian lưu audit làm thời gian lưu liên hệ.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-002: POST /v1/crm/customer-contact-drafts. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
