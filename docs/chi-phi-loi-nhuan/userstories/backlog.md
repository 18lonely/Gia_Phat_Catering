---
id: DOC-E13-USERSTORIES-BACKLOG-MD
title: Backlog FEAT-088
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Backlog FEAT-088

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

| Story | FR / UC | User story | Ưu tiên | Story point | AC | Phụ thuộc |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| US-EXP-001 | FR-EXP-PER-001 / UC-EXP-001 | Là một PER-07, tôi muốn quản lý và khóa kỳ chi phí để kỳ open hoặc locked; danh sách điều kiện thiếu. | P2 |  | AC-EXP-001-1, AC-EXP-001-2, AC-EXP-001-3 | E13-Q02 |
| US-EXP-002 | FR-EXP-COST-001 / UC-EXP-002 | Là một PER-07, tôi muốn ghi chi phí theo cơ sở và loại để dòng chi phí draft có nguồn; chưa hạch toán chính thức. | P2 |  | AC-EXP-002-1, AC-EXP-002-2, AC-EXP-002-3 | E13-Q01 |
| US-EXP-003 | FR-EXP-TIME-001 / UC-EXP-003 | Là một PER-07, tôi muốn ghi giờ công thực tế theo ca để bảng draft; giờ thực tế và ca dự kiến tách riêng. | P2 |  | AC-EXP-003-1, AC-EXP-003-2, AC-EXP-003-3 | E13-Q03; E11-Q09 |
| US-EXP-004 | FR-EXP-LAB-001 / UC-EXP-004 | Là một PER-07, tôi muốn tham chiếu chi phí nhân công để chi phí nhân công có nguồn hoặc blocked. | P2 |  | AC-EXP-004-1, AC-EXP-004-2, AC-EXP-004-3 | E13-Q03/04 |
| US-EXP-005 | FR-EXP-METH-001 / UC-EXP-005 | Là một PER-07, tôi muốn soạn phiên bản phương pháp phân bổ để phiên bản draft; không có hiệu lực phân bổ. | P2 |  | AC-EXP-005-1, AC-EXP-005-2, AC-EXP-005-3 | E13-Q05/09 |
| US-EXP-006 | FR-EXP-APRV-001 / UC-EXP-006 | Là một PER-08, tôi muốn ghi duyệt phương pháp của giám đốc để quyết định approved hoặc returned; version không đổi nội dung. | P2 |  | AC-EXP-006-1, AC-EXP-006-2, AC-EXP-006-3 | E13-Q05; O-06 |
| US-EXP-007 | FR-EXP-ALLOC-001 / UC-EXP-007 | Là một PER-07, tôi muốn kiểm cổng và lập lần phân bổ để lần chạy blocked hoặc bản phân bổ có methodversion; phần chưa phân bổ riêng. | P2 |  | AC-EXP-007-1, AC-EXP-007-2, AC-EXP-007-3 | E13-Q05/06/09/12 |
| US-EXP-008 | FR-EXP-PROF-001 / UC-EXP-008 | Là một PER-07/PER-08, tôi muốn tra cứu lợi nhuận theo khách để báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định. | P2 |  | AC-EXP-008-1, AC-EXP-008-2, AC-EXP-008-3 | E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15 |
| US-EXP-009 | FR-EXP-RECON-001 / UC-EXP-009 | Là một PER-08, tôi muốn đối chiếu lợi nhuận với từng cơ sở để bảng đối chiếu có residual/unallocated/delta; chưa khớp không nghiệm thu. | P2 |  | AC-EXP-009-1, AC-EXP-009-2, AC-EXP-009-3 | E13-Q06/08/09/14 |
| US-EXP-010 | FR-EXP-ADJ-001 / UC-EXP-010 | Là một PER-07, tôi muốn lập điều chỉnh sau khóa có phê duyệt để đề nghị pending; chỉ posted khi có quyết định hợp lệ. | P2 |  | AC-EXP-010-1, AC-EXP-010-2, AC-EXP-010-3 | E13-Q10; O-06 |
| US-EXP-011 | FR-EXP-SAFE-001 / UC-EXP-011 | Là một PER-07/PER-08, tôi muốn bảo vệ lương và đầu ra nội bộ để projection nội bộ cho phép hoặc từ chối; không có đường gửi khách e13. | P2 |  | AC-EXP-011-1, AC-EXP-011-2, AC-EXP-011-3 | E13-Q11/12; E12-Q07 |
| US-EXP-012 | FR-EXP-SRC-001 / UC-EXP-012 | Là một PER-07/PER-08, tôi muốn kiểm nguồn và truy nguyên lần báo cáo để manifest, danh sách blocked và liên kết nội bộ theo quyền. | P2 |  | AC-EXP-012-1, AC-EXP-012-2, AC-EXP-012-3 | E13-Q12/13 |

INVEST: mỗi story có giá trị và ba AC; ranh giới có thể thương lượng. Độc lập triển khai, khả năng ước lượng và kích thước sprint **chưa xác nhận** do gate nguồn. Chưa sẵn sàng đưa vào sprint; không gán story point, tên phụ trách hoặc ngày triển khai.
