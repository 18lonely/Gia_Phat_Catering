---
id: DOC-E10-USECASES-UC-CRM-009-MD
title: UC-CRM-009 — Quản lý cơ hội và phễu bán hàng
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-009 — Quản lý cơ hội và phễu bán hàng

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-072. Cấp độ: Sea level — mục tiêu người dùng.

Tác nhân chính: Dinh dưỡng viên kiêm chăm sóc khách hàng. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần theo dõi tiến trình tư vấn tới hợp đồng có bằng chứng; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-SALE-OPP-001 ↔ UC-CRM-009 ↔ US-CRM-009; API-CRM-009; UI-CRM-05.

## Kích hoạt

Dinh dưỡng viên kiêm chăm sóc khách hàng cần quản lý cơ hội và phễu bán hàng để theo dõi tiến trình tư vấn tới hợp đồng có bằng chứng, từ màn UI-CRM-05 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: opportunityRef nếu đã có, customerOrIntakeRef, stage đề nghị, ownerRef, evidenceRef, version.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q07/08; E6-CG-08. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-05 hoặc gọi API-CRM-009, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp opportunityRef nếu đã có, customerOrIntakeRef, stage đề nghị, ownerRef, evidenceRef, version; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Tạo cơ hội nháp hoặc ghi sự kiện chuyển giai đoạn sau kiểm policy; giữ chủ cơ hội, lịch sử, nguồn thắng/thua; đếm theo cơ hội duy nhất và cùng kỳ/cohort, không coi mọi lead là cơ hội đã đủ điều kiện.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Cơ hội và lịch sử giai đoạn; bảng phễu nêu định nghĩa mẫu số, thiếu thì chưa tính tỷ lệ.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Cơ hội và lịch sử giai đoạn; bảng phễu nêu định nghĩa mẫu số, thiếu thì chưa tính tỷ lệ. Có bằng chứng nguồn và dấu vết thay đổi có thể đối soát theo requestId.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q07/08; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. chỉ có báo giá đã gửi, chưa có bằng chứng thắng: khi đề nghị ghi WON, hệ thống ERR-CRM-422-01; không tự suy thắng từ việc gửi báo giá. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. mẫu số cơ hội của kỳ bằng 0: khi xem tỷ lệ chuyển đổi, hệ thống hiện chưa có cơ sở tính, tỷ lệ null; không chia 0 hoặc hiển thị 100%.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-009: POST /v1/crm/opportunity-events. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
