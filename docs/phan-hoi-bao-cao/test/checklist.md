---
id: DOC-E12-TEST-CHECKLIST-MD
title: Checklist kiểm thử E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Checklist kiểm thử E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; không đóng câu hỏi nguồn |

Chưa có review phê duyệt BA/QA; vẫn soạn ca nháp theo yêu cầu phiên. Không dùng kiểm HTML thay test sản phẩm.

| Nhóm | Phạm vi | Ca liên quan |
| :--- | :--- | :--- |
| Chức năng | Mọi FR: nhánh có điều kiện, lỗi nghiệp vụ và biên | TC-FBR-001-1 đến TC-FBR-020-3 |
| Quyền / bảo mật | Scope, chủ thể, trường cost, công cụ chỉ đọc, thu hồi quyền, injection | TC-FBR-S001, S002, S003 |
| Dữ liệu / nguồn | Không suy chọn từ sản xuất; không bình quân cost; VAT/CK; thiếu khác 0 | TC-FBR-S004, S005, S006 |
| Riêng tư | Không sức khỏe, consent, xóa, không gợi ý cá nhân | TC-FBR-S007, S008 |
| Phiên bản / độ bền | Hash validator, race, retry, receipt, không tự áp dụng | TC-FBR-S009, S010 |
| Hiệu năng / giao diện | Tải kế thừa nền, bố cục và nhãn | TC-FBR-S011, S012 |
| Lỗi | Mọi ERR-FBR có ca lỗi riêng | TC-FBR-E001 đến E008 |
| Nghiệm thu R12 | Bốn dashboard từ dữ liệu thật, tỷ lệ chọn từ lựa chọn thật; gate nguồn | r12-acceptance.md |

