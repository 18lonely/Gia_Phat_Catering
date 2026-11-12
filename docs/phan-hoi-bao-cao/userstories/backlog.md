---
id: DOC-E12-USERSTORIES-BACKLOG-MD
title: Backlog E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Backlog E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

Chưa sẵn sàng cam kết Sprint: còn gate ở từng dòng. INVEST: giá trị và mục tiêu tách theo UC; có 3 AC/story; E và I chưa xác nhận do contract/nguồn chưa đủ. Không gán story point, người phụ trách hoặc ngày triển khai.

| Story | Feature / FR | User story | Ưu tiên | AC | Phụ thuộc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| US-FBR-001 | FEAT-079 / FR-FB-RATE-001 | Là PER-02, PER-03, PER-04, PER-05, tôi muốn gửi đánh giá bữa ăn để nhận đánh giá có receipt và trạng thái tiếp nhận và biết căn cứ còn thiếu. | P1 | AC-FBR-001-1, AC-FBR-001-2, AC-FBR-001-3 | E12-Q01/02; E6 CG01/08 |
| US-FBR-002 | FEAT-079 / FR-FB-CASE-001 | Là PER-02, PER-03, PER-04, PER-05, tôi muốn tiếp nhận và theo dõi khiếu nại để nhận hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách và biết căn cứ còn thiếu. | P1 | AC-FBR-002-1, AC-FBR-002-2, AC-FBR-002-3 | E12-Q02/03; E6 CG01/08; E7-Q02 |
| US-FBR-003 | FEAT-080 / FR-FB-SELR-001 | Là PER-05, tôi muốn xem tỷ lệ được chọn theo món để nhận số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định và biết căn cứ còn thiếu. | P1 | AC-FBR-003-1, AC-FBR-003-2, AC-FBR-003-3 | E12-Q04; E6 CG01–14, ORD-Q01–15, E6-EVID-001/002 |
| US-FBR-004 | FEAT-080 / FR-FB-PROP-001 | Là PER-05, tôi muốn lập đề xuất cải tiến thực đơn từ phản hồi để nhận đề xuất nháp cùng căn cứ và điều kiện kiểm lại và biết căn cứ còn thiếu. | P1 | AC-FBR-004-1, AC-FBR-004-2, AC-FBR-004-3 | E12-Q04/05; DL-01; O-02 |
| US-FBR-005 | FEAT-081 / FR-RPT-ROLE-001 | Là PER-05, PER-06, PER-07, PER-08, tôi muốn xem dashboard theo bốn vai trò để nhận bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng và biết căn cứ còn thiếu. | P1 | AC-FBR-005-1, AC-FBR-005-2, AC-FBR-005-3 | E12-Q06/07/08; E7-Q03/04; E10-Q07; E11-Q07/08 |
| US-FBR-006 | FEAT-081 / FR-RPT-CPCT-001 | Là PER-05, PER-06, PER-07, PER-08 theo quyền riêng, tôi muốn đọc cost % ngày và theo khách để nhận cost % ngày có nguồn e3; ô theo khách chưa xác định khi thiếu công thức và biết căn cứ còn thiếu. | P1 | AC-FBR-006-1, AC-FBR-006-2, AC-FBR-006-3 | E12-Q07/08; O-01; DATA-COST-Q01–06; E11-Q07/08 |
| US-FBR-007 | FEAT-082 / FR-AIO-PRRV-001 | Là PER-05, PER-08, tôi muốn yêu cầu rà soát thực đơn khi giá đổi để nhận đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn và biết căn cứ còn thiếu. | P1 | AC-FBR-007-1, AC-FBR-007-2, AC-FBR-007-3 | AIO-Q01–06; E12-Q09; O-01/O-02 |
| US-FBR-008 | FEAT-082 / FR-AIO-RCHK-001 | Là PER-05, PER-08, tôi muốn kiểm lại đề xuất đổi món hoặc định lượng để nhận bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật và biết căn cứ còn thiếu. | P1 | AC-FBR-008-1, AC-FBR-008-2, AC-FBR-008-3 | AIO-Q02/05/06; DL-01; E11-Q15; E12-Q09 |
| US-FBR-009 | FEAT-083 / FR-AIO-ESTR-001 | Là PER-07, tôi muốn diễn giải dự toán có nguồn để nhận nháp diễn giải dự toán chờ người thật rà và biết căn cứ còn thiếu. | P1 | AC-FBR-009-1, AC-FBR-009-2, AC-FBR-009-3 | AIO-Q01–06; E12-Q09; DATA-COST-Q01–06 |
| US-FBR-010 | FEAT-083 / FR-AIO-DEMR-001 | Là PER-07, tôi muốn diễn giải nhu cầu nguyên liệu để nhận nháp diễn giải nhu cầu với thiếu nguồn rõ ràng và biết căn cứ còn thiếu. | P1 | AC-FBR-010-1, AC-FBR-010-2, AC-FBR-010-3 | E11-Q01/03/13; E6 CG06; AIO-Q01–06 |
| US-FBR-011 | FEAT-083 / FR-AIO-PDEV-001 | Là PER-07, tôi muốn giải thích cảnh báo giá lệch để nhận nháp giải thích; cảnh báo chính thức chưa xác định và biết căn cứ còn thiếu. | P1 | AC-FBR-011-1, AC-FBR-011-2, AC-FBR-011-3 | E12-Q10; E11-Q07/08/14; AIO-Q01–06 |
| US-FBR-012 | FEAT-084 / FR-AIO-CRMS-001 | Là PER-05, PER-08, tôi muốn tóm tắt khách và đề xuất nhắc việc để nhận nháp tóm tắt và danh sách việc cần người thật rà và biết căn cứ còn thiếu. | P1 | AC-FBR-012-1, AC-FBR-012-2, AC-FBR-012-3 | E10-Q01/05/06/13; AIO-Q01–06; E12-Q11 |
| US-FBR-013 | FEAT-084 / FR-AIO-CRMQ-001 | Là PER-05, PER-08, tôi muốn soạn nội dung báo giá nháp để review để nhận nháp báo giá có nguồn và nhãn chưa phát hành và biết căn cứ còn thiếu. | P1 | AC-FBR-013-1, AC-FBR-013-2, AC-FBR-013-3 | E10-Q08/09/13/15; AIO-Q01–06; E12-Q11 |
| US-FBR-014 | FEAT-085 / FR-AIO-DQA-001 | Là PER-07, PER-08, tôi muốn hỏi đáp số liệu theo quyền để nhận câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu và biết căn cứ còn thiếu. | P2 | AC-FBR-014-1, AC-FBR-014-2, AC-FBR-014-3 | AIO-Q01–06; E12-Q06/07/08/12; E10-Q15 |
| US-FBR-015 | FEAT-086 / FR-NUTR-GRPT-001 | Là PER-05, tôi muốn lập mục tiêu dinh dưỡng nhóm để nhận mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu và biết căn cứ còn thiếu. | P1 | AC-FBR-015-1, AC-FBR-015-2, AC-FBR-015-3 | NUTR-Q01–04; E12-Q13/14 |
| US-FBR-016 | FEAT-086 / FR-NUTR-GRPC-001 | Là PER-05, tôi muốn kiểm thực đơn theo mục tiêu nhóm để nhận so sánh có phiên bản hoặc chưa xác định và biết căn cứ còn thiếu. | P1 | AC-FBR-016-1, AC-FBR-016-2, AC-FBR-016-3 | NUTR-Q01–04; E12-Q13/14; DL-01 |
| US-FBR-017 | FEAT-087 / FR-NUTR-DCON-001 | Là PER-03, tôi muốn đồng ý dùng nhật ký bữa đã ăn để nhận đồng ý có phiên bản hoặc nhật ký chưa bật và biết căn cứ còn thiếu. | P2 | AC-FBR-017-1, AC-FBR-017-2, AC-FBR-017-3 | E12-Q15/16; E6 CG01/08; E1 NFR-PRIV-001 |
| US-FBR-018 | FEAT-087 / FR-NUTR-DREC-001 | Là PER-03, tôi muốn ghi bữa đã ăn vào nhật ký để nhận bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng và biết căn cứ còn thiếu. | P2 | AC-FBR-018-1, AC-FBR-018-2, AC-FBR-018-3 | E12-Q15/17; NUTR-Q01–04; E6 CG01/08/10 |
| US-FBR-019 | FEAT-087 / FR-NUTR-DVIW-001 | Là PER-03, tôi muốn xem nhật ký dinh dưỡng của mình để nhận danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực và biết căn cứ còn thiếu. | P2 | AC-FBR-019-1, AC-FBR-019-2, AC-FBR-019-3 | E12-Q15/16; E6 CG01/08; NUTR-Q03/04 |
| US-FBR-020 | FEAT-087 / FR-NUTR-DDEL-001 | Là PER-03, tôi muốn yêu cầu xóa nhật ký và rút đồng ý để nhận receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút và biết căn cứ còn thiếu. | P2 | AC-FBR-020-1, AC-FBR-020-2, AC-FBR-020-3 | E12-Q15/16; E1 NFR-PRIV-001 |

