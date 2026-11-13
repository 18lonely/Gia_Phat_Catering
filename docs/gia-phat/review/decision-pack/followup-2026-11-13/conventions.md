---
id: DOC-FOLLOWUP-CONVENTIONS
title: Quy ước mô tả tham chiếu, phiên bản và ranh giới contract
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [draft, followup]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Quy ước mô tả tham chiếu, phiên bản và ranh giới contract

Nháp · 13/11/2026 · Chưa có quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 13/11/2026 | BA | Rà XC-01–12 và DEC; giữ câu trả lời trống |

XC-04 — quy ước tài liệu đề xuất, không là contract đã duyệt. Phần kiểu truyền thực tế vẫn BLOCKED theo câu kỹ thuật từng epic.

| Khái niệm | Cách ghi thống nhất trong tài liệu | Căn cứ |
| :--- | :--- | :--- |
| Định danh | Tách kiểu lưu trữ nội bộ với kiểu truyền API; không suy số học từ mã định danh | [E10](../../../../crm-ban-hang/srs/data-dictionary.md), [E13](../../../../chi-phi-loi-nhuan/srs/data-dictionary.md) |
| Version khi sửa | Token so khớp bản hiện tại; kiểu lưu trữ Integer không đủ kết luận kiểu wire; consumer không tự tăng token opaque | [E11](../../../../mua-hang-san-xuat/srs/data-dictionary.md), [E12](../../../../phan-hoi-bao-cao/srs/data-dictionary.md) |
| Revision nguồn | Tham chiếu phiên bản bất biến của producer, khác version chống sửa đồng thời | [E12](../../../../phan-hoi-bao-cao/srs/data-dictionary.md) |
| Reference nguồn | Ghi producer, định danh và revision theo contract nguồn; thiếu mapping thì BLOCKED | [E11](../../../../mua-hang-san-xuat/srs/data-dictionary.md), [E13 manifest](../../../../chi-phi-loi-nhuan/srs/data-dictionary.md) |

Chưa chọn kiểu wire chung, tên field chung, precision, TTL hoặc endpoint. Câu tương đương đang mở: E7-Q08, E8-Q12, E9-Q13, E10-Q13, E11-Q13, E12-Q18, E13-Q12. Mỗi epic cần mapping producer → consumer trước khi freeze.

XC-08: giữ riêng endpoint và quyền hiện hữu; E8-Q05/E9-Q11 chưa trả lời nên không hợp nhất bộ dựng. XC-12: E1-Q06/AIO-Q07 hỏi cách đo; không đổi NFR. XC-09: giá nguồn có phần lẻ khác giá cost; không suy quy tắc làm tròn chung.
