---
id: DOC-E8-UI-SCREENS-MD
title: Màn hình và quyền E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Màn hình và quyền E8

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

| Màn | Nội dung | FR | Quyền / gate |
| :--- | :--- | :--- | :--- |
| UI-PUB-01 | Giới thiệu, dịch vụ, dự án, đối tác | PAGE | Public published |
| UI-PUB-02 | Blog danh sách và chi tiết | BLOG | Public published |
| UI-PUB-03 | Thực đơn mẫu và giá | MENU | Projection public E8-Q03/04 |
| UI-PUB-04 | Dựng thử tuần | TRY | Public, policy E8-Q05 |
| UI-PUB-05 | Form tư vấn / tiếp nhận | LEAD | Public, consent E8-Q06 |
| UI-PUB-06 | Danh sách, soạn, xem trước, công bố | EDIT/PREV/PUBL | Auth; quyền E8-Q08 |
| UI-PUB-07 | Inventory/mapping URL cũ | URLM/URLR | Auth mapping; khách chỉ kết quả URL |
| UI-PUB-08 | Tiếp nhận và điểm nối lead | RELY | Auth; contact tối thiểu E8-Q06 |
| UI-PUB-09 | Ảnh và banner | MEDI | Auth E8-Q09 |

[Wireframe](../html-wireframe/public-workbench.html):9 màn, desktop/mobile, dữ liệu synthetic. Chuyển màn là công cụ review, không giả khách có quyền admin. Modal xem trước và nút kiểm mô phỏng local, không gọi API/lưu dữ liệu thật. Bản mẫu có giá40.000 đ, số dinh dưỡng giả định và dị ứng synthetic để rà bố cục, không phê duyệt public. Loading/empty/error thay nội dung chính, không giữ dữ liệu như đã tải. [User flow](user-flow.md).
