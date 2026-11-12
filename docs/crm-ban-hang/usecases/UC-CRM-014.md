---
id: DOC-E10-USECASES-UC-CRM-014-MD
title: UC-CRM-014 — Kích hoạt hợp đồng và giá theo loại suất
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-014 — Kích hoạt hợp đồng và giá theo loại suất

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-073. Cấp độ: Sea level — mục tiêu người dùng.

Tác nhân chính: Người duyệt hợp đồng được chỉ định. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần áp một giá có căn cứ cho từng loại suất và thời gian; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-SALE-ACTV-001 ↔ UC-CRM-014 ↔ US-CRM-014; API-CRM-014; UI-CRM-08.

## Kích hoạt

Người duyệt hợp đồng được chỉ định cần kích hoạt hợp đồng và giá theo loại suất để áp một giá có căn cứ cho từng loại suất và thời gian, từ màn UI-CRM-08 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: contractVersion, amendmentRef/amendmentVersion nếu kích hoạt phụ lục, signatureEvidenceRef, priceLines theo mealTypeRef, effectiveFrom, effectiveTo, salePriceBasis, vatRatePct.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q10/11/12; O-01; CK-Q01–10; E6-CG-08. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-08 hoặc gọi API-CRM-014, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp contractVersion, amendmentRef/amendmentVersion nếu kích hoạt phụ lục, signatureEvidenceRef, priceLines theo mealTypeRef, effectiveFrom, effectiveTo, salePriceBasis, vatRatePct; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Kiểm bằng chứng, quyền duyệt và hiệu lực; phụ lục phải thuộc hợp đồng trong path và đúng version. Kiểm không chồng khoảng giá ACTIVE theo customer + mealType như nguồn hiện có; kiểm nguyên tử khi cạnh tranh. Chưa chốt quy ước biên ngày không kích hoạt.
5. Hệ thống đối chiếu lại version và quyền tại thời điểm ghi; lưu nghiệp vụ, audit và receipt cùng một giao dịch. Nếu chưa thể bảo đảm thì không báo hoàn tất.
6. Hệ thống trả Hợp đồng và bộ giá hiệu lực nhất quán, audit và nguồn phụ lục; không ghi giá ngược vào order đã chụp.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Hợp đồng và bộ giá hiệu lực nhất quán, audit và nguồn phụ lục; không ghi giá ngược vào order đã chụp. Có bằng chứng nguồn và dấu vết thay đổi có thể đối soát theo requestId.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q10/11/12; O-01; CK-Q01–10; E6-CG-08; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. hai bộ giá cùng khách và loại suất có phần giao nhau: khi kích hoạt bộ thứ hai, hệ thống ERR-CRM-409-03; không ACTIVE một phần và không chọn giá theo bản ghi mới nhất. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. hai bộ giá liền kề đúng ngày kết thúc/bắt đầu: khi kiểm tra hiệu lực tại ranh giới, hệ thống kết quả theo quy ước biên đã duyệt E10-Q11; trước quyết định thì BLOCKED.
- 5a. Version cũ trả ERR-CRM-409-01; tác nhân tải lại và rà diff. Cùng khóa khác nội dung trả ERR-CRM-409-02, không tạo bản mới. Lỗi ghi/audit trả ERR-CRM-500-01; đối soát bằng khóa cũ trước thử lại.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-014: POST /v1/crm/contracts/{id}/activations. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
