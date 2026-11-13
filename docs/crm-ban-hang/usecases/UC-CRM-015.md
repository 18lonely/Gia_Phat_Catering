---
id: DOC-E10-USECASES-UC-CRM-015-MD
title: "UC-CRM-015: Lập phụ lục thay đổi giá"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-015: Lập phụ lục thay đổi giá

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-073. Cấp độ: Sea level (mục tiêu người dùng).

Tác nhân chính: Dinh dưỡng viên kiêm chăm sóc khách hàng. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần đổi giá có lịch sử và tránh tính lại kỳ đã đối soát; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-SALE-AMND-001 ↔ UC-CRM-015 ↔ US-CRM-015; API-CRM-015; UI-CRM-09.

## Kích hoạt

Dinh dưỡng viên kiêm chăm sóc khách hàng cần lập phụ lục thay đổi giá để đổi giá có lịch sử và tránh tính lại kỳ đã đối soát, từ màn UI-CRM-09 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: contractRef, baseVersion, predecessorPriceRefs, giá đề nghị, from/to, reason, evidenceRef.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q10/11/12; E6-CG-04/05/07; E7-Q05. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-09 hoặc gọi API-CRM-015, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp contractRef, baseVersion, predecessorPriceRefs, giá đề nghị, from/to, reason, evidenceRef; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Lưu phụ lục DRAFT và quan hệ bản trước/bản sau, giữ nội dung giá cũ bất biến. Khi được duyệt phải kiểm cùng quy tắc ACTV và không chồng lấn; sửa hồi tố và tác động đơn đã khóa chờ Q12, không tự mở kỳ.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Phụ lục nháp và diff lịch sử; không sửa giá hoặc snapshot order cũ.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Phụ lục nháp và diff lịch sử; không sửa giá hoặc snapshot order cũ. Có bằng chứng nguồn và dấu vết thay đổi có thể đối soát theo requestId.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q10/11/12; E6-CG-04/05/07; E7-Q05; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. người dùng đòi sửa trực tiếp bản giá đã dùng cho order: khi gửi phụ lục kèm lệnh ghi đè lịch sử, hệ thống ERR-CRM-422-01; không sửa snapshot và không tự mở kỳ khóa E7. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. gửi lại cùng khóa và cùng nội dung phụ lục: khi lưu lại sau mất phản hồi, hệ thống trả cùng phụ lục, không tạo hai chuỗi thay thế.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-015: POST /v1/crm/contracts/{id}/amendments. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
