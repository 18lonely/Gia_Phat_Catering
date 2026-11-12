---
id: DOC-E10-TEST-R10-ACCEPTANCE-MD
title: Khung nghiệm thu R10 và cổng G-Next
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Khung nghiệm thu R10 và cổng G-Next

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Tiêu chí nguyên phạm vi roadmap

R10: **100% khách đang phục vụ có hồ sơ; 100% hợp đồng hiệu lực có phụ lục giá trong hệ thống**. G-Next phải đạt trước mở phát hành Later: ≥ 90% order qua cổng của công ty đã chuyển, ≥ 70% suất có lựa chọn trước hạn, truy cập tự nhiên sau 60 ngày ≥ 90% mức trước chuyển đổi. Mở tài liệu E10 không xác nhận cổng đạt.

| Bộ | Mẫu số / tử số | Oracle và bằng chứng | Status |
| :--- | :--- | :--- | :--- |
| R10-CUSTOMERS | Mẫu số: toàn bộ khách đang phục vụ từ manifest độc lập tại ngày chốt Q14. Tử số: khách có hồ sơ CRM truy được đúng nguồn. | Đối chiếu từng khách và lý do thiếu; người có thẩm quyền xác nhận đầy đủ. Không lấy customers đã nhập làm mẫu số. | BLOCKED E10-Q14; CG08 |
| R10-CONTRACTS | Mẫu số: toàn bộ hợp đồng hiệu lực từ kho/văn bản đã được duyệt tại ngày chốt. Tử số: hợp đồng có phụ lục giá trong hệ thống theo yêu cầu R10. | Đối chiếu đúng khách, loại suất, bằng chứng ký, phụ lục, khoảng hiệu lực không chồng, lịch sử và nguồn giá. Chưa có phụ lục không tự miễn tiêu chí. | BLOCKED E10-Q10/11/12/14 |
| G-Next | Ba chỉ số BO-06/05/09 từ nguồn được duyệt | Bằng chứng kỳ đo, baseline và người xác nhận; không dùng tỷ lệ tài liệu 60/78. | BLOCKED; nguồn E6/E8 và O-04 còn mở |

Mẫu số 0 hoặc chưa xác nhận: không kết luận 100%, ghi chưa đủ căn cứ. Mỗi ngoại lệ vẫn nằm trong manifest; không loại khỏi mẫu số để tăng tỷ lệ. 48 ca chức năng và 10 ca hệ thống không thay hai phép đối chiếu toàn bộ R10. Bộ synthetic chỉ minh họa, không thể chứng minh 100% khách/hợp đồng thật.

Chưa có môi trường, build, dữ liệu thực tế hoặc chữ ký phê duyệt; chưa chạy nghiệm thu. [Evidence](evidence-protocol.md).
