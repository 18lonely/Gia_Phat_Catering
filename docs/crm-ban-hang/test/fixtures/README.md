---
id: DOC-E10-TEST-FIXTURES-README-MD
title: Fixture synthetic E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Fixture synthetic E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

[synthetic.json](synthetic.json) chứa hai khách giả định, hai khoảng giá chồng rõ ở phần bên trong, projection khách minh họa và 48 scenario có oracle. Không có tiêu chí trùng, ngưỡng rủi ro hoặc công thức margin được tự chọn: các giá trị này là null.

Reset fixture riêng từng ca trong môi trường sản phẩm tương lai; không lấy trạng thái ca trước làm tiền điều kiện ca sau. Giá 40.000 đồng chỉ synthetic cho bố cục, không quyết định VAT hoặc giá hợp đồng thật. Đây không phải bộ khách/hợp đồng R10 được duyệt. Không seed, migration hoặc gọi API trong phiên BA.
