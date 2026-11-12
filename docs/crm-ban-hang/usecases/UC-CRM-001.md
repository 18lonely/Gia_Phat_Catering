---
id: DOC-E10-USECASES-UC-CRM-001-MD
title: UC-CRM-001 — Xem hồ sơ khách hàng 360°
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-001 — Xem hồ sơ khách hàng 360°

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-070. Cấp độ: Sea level — mục tiêu người dùng.

Tác nhân chính: Dinh dưỡng viên kiêm chăm sóc khách hàng. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần đối chiếu lịch sử khách mà không nhập lại doanh thu; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-CUS-VIEW-001 ↔ UC-CRM-001 ↔ US-CRM-001; API-CRM-001; UI-CRM-01.

## Kích hoạt

Dinh dưỡng viên kiêm chăm sóc khách hàng cần xem hồ sơ khách hàng 360° để đối chiếu lịch sử khách mà không nhập lại doanh thu, từ màn UI-CRM-01 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: customerId, kỳ xem và phạm vi cơ sở.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E6-CG-01/08; E7-Q03/04/08; E10-Q01. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-01 hoặc gọi API-CRM-001, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerId, kỳ xem và phạm vi cơ sở; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Đọc từng nhóm liên hệ, điểm, hợp đồng, order, doanh thu, phản hồi theo nguồn và quyền; giữ nguồn, thời điểm và độ đầy đủ riêng từng nhóm.
5. Hệ thống đọc dữ liệu đã có, đối chiếu phiên bản và mức đầy đủ; không chạy tác vụ ghi hoặc đánh giá mới bên dưới GET.
6. Hệ thống trả Hồ sơ có các nhóm dữ liệu và trạng thái ĐỦ / THIẾU / CHƯA CÓ NGUỒN; không cộng phần chưa xác định thành 0.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Hồ sơ có các nhóm dữ liệu và trạng thái ĐỦ / THIẾU / CHƯA CÓ NGUỒN; không cộng phần chưa xác định thành 0. Dữ liệu nguồn và trạng thái nghiệp vụ không bị thay đổi bởi thao tác xem.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E6-CG-01/08; E7-Q03/04/08; E10-Q01; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. nguồn doanh thu hoặc phản hồi chưa có: khi mở hồ sơ A, hệ thống nhóm tương ứng ghi CHƯA CÓ NGUỒN; giá trị null, không 0; không mở chức năng phản hồi E12. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. người dùng chỉ có phạm vi khách A: khi đổi mã hồ sơ sang khách B, hệ thống trả ERR-CRM-404-01; không lộ liên hệ hoặc tổng tiền của B.
- 5a. Nguồn đọc không khả dụng trả phần thiếu có nhãn hoặc ERR-CRM-503-01 nếu không xác định được phạm vi; không lưu kết quả giả.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-001: GET /v1/crm/customers/{id}/overview. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
