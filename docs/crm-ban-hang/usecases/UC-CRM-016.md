---
id: DOC-E10-USECASES-UC-CRM-016-MD
title: UC-CRM-016 — Tra giá hợp đồng cho thời điểm phục vụ
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# UC-CRM-016 — Tra giá hợp đồng cho thời điểm phục vụ

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Phạm vi và tác nhân

Phạm vi: E10, FEAT-073. Cấp độ: Fish level — giao tiếp hệ thống phục vụ mục tiêu người dùng.

Tác nhân chính: Dịch vụ order được cấp quyền; kế toán tra cứu. Tác nhân hỗ trợ: dịch vụ xác thực/audit E1; chủ dữ liệu nguồn trong bảng phụ thuộc. Bên quan tâm: nhân viên cần đặt đơn dùng đúng điều khoản giá mà vẫn giữ trách nhiệm nguồn; khách cần dữ liệu đúng phạm vi; kế toán cần lịch sử giá và giao dịch không bị thay đổi ngoài thẩm quyền.

Truy vết: FR-SALE-PRIC-001 ↔ UC-CRM-016 ↔ US-CRM-016; API-CRM-016; UI-CRM-09.

## Kích hoạt

Dịch vụ order được cấp quyền; kế toán tra cứu cần tra giá hợp đồng cho thời điểm phục vụ để đặt đơn dùng đúng điều khoản giá mà vẫn giữ trách nhiệm nguồn, từ màn UI-CRM-09 hoặc giao tiếp dịch vụ tương ứng.

## Tiền điều kiện

- Có phiên hoặc danh tính dịch vụ được cấp quyền đúng khách/cơ sở. Tham chiếu nguồn có thể đối soát và không lấy quyền từ body.
- Đầu vào nghiệp vụ: customerRef, mealTypeRef, serviceDate, sourceScope đã xác minh.
- Luồng thành công chỉ áp dụng sau khi quyết định cần thiết được duyệt: E10-Q11/12/13; E6-CG-04/05/07/08/11; CK-Q01–10. Hiện các nhánh này BLOCKED; mô tả điều kiện không có nghĩa đã được trả lời.

## Luồng chính

1. Tác nhân mở UI-CRM-09 hoặc gọi API-CRM-016, chọn đối tượng và rà nguồn hiện hành.
2. Tác nhân cung cấp customerRef, mealTypeRef, serviceDate, sourceScope đã xác minh; hệ thống kiểm định dạng và trường được phép.
3. Hệ thống xác minh actor, phạm vi đối tượng và các gate trước khi xử lý nội dung.
4. Hệ thống thực hiện nghiệp vụ: Chỉ đọc bộ giá đã có hiệu lực theo quy ước được duyệt; trả priceTermRef, contract/amendmentRef, version, căn cứ VAT. Không tự chụp giá vào order; adapter E6/Cost phải được duyệt riêng.
5. Hệ thống đọc dữ liệu đã có, đối chiếu phiên bản và mức đầy đủ; không chạy tác vụ ghi hoặc đánh giá mới bên dưới GET.
6. Hệ thống trả Một kết quả có nguồn hoặc UNRESOLVED; không dùng giá hiện tại thay snapshot lịch sử.
7. Tác nhân rà kết quả, mã nguồn và trạng thái; chỉ tiếp tục bước kế tiếp khi đủ căn cứ, không suy thành đã nghiệm thu.

## Hậu điều kiện thành công

Một kết quả có nguồn hoặc UNRESOLVED; không dùng giá hiện tại thay snapshot lịch sử. Dữ liệu nguồn và trạng thái nghiệp vụ không bị thay đổi bởi thao tác xem.

## Bảo đảm tối thiểu

Không lộ dữ liệu ngoài quyền; không mất bản cũ, không sửa snapshot tài chính, không tự đóng câu hỏi. Lỗi trước commit không tạo kết quả một phần; mất phản hồi giữ trạng thái chưa rõ phía người gọi cho tới đối soát.

## Nhánh thay thế và ngoại lệ

- 2a. Sai kiểu hoặc trường ngoài danh mục: ERR-CRM-400-01; giữ dữ liệu hiện có, chỉ rõ tên trường an toàn để tác nhân sửa và quay lại bước 2.
- 3a. Thiếu/hết phiên: ERR-CRM-401-01; yêu cầu xác thực lại. Thiếu quyền hành động: ERR-CRM-403-01. Tài nguyên ngoài phạm vi: ERR-CRM-404-01 đồng nhất với không tồn tại, không tiết lộ mã khách khác.
- 3b. Gate hoặc nguồn bắt buộc chưa sẵn sàng: ERR-CRM-503-01; giữ BLOCKED với E10-Q11/12/13; E6-CG-04/05/07/08/11; CK-Q01–10; không tự chọn phương án thay thế. Với hồ sơ tổng hợp, chỉ nhóm dữ liệu thiếu bị đánh dấu, không dựng tổng giả.
- 4a. không có hoặc có hơn một giá khớp, VAT cần thiết chưa rõ: khi tra giá, hệ thống UNRESOLVED hoặc ERR-CRM-409-03; không lấy giá 0 hoặc tự chọn giá mới nhất. Tác nhân xử lý theo nguồn quyết định, không vượt gate.
- 4b. đơn lịch sử đã có pricingSnapshot và sau đó có phụ lục mới: khi xem hồ sơ đơn cũ, hệ thống vẫn dùng snapshot đúng order/version từ E6/Cost; không thay bằng kết quả tra giá hiện tại.
- 5a. Nguồn đọc không khả dụng trả phần thiếu có nhãn hoặc ERR-CRM-503-01 nếu không xác định được phạm vi; không lưu kết quả giả.

## Quy tắc và giao tiếp

BR-CRM-001/002/011/012; các quy tắc miền tương ứng tại [SRS](../srs/spec.md). API-CRM-016: GET /v1/crm/price-resolutions. [AC](../userstories/acceptance-criteria.md) · [Ca kiểm](../test/test-cases.md) · [Lỗi](../srs/error-matrix.md).
