---
id: DOC-E12-UI-SCREENS-MD
title: Màn hình và quyền E12
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Màn hình và quyền E12

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

| Màn | Tên | FR | Persona / quyền đề xuất | Thành phần chính |
| :--- | :--- | :--- | :--- | :--- |
| UI-FBR-01 | Đánh giá bữa ăn | FR-FB-RATE-001 | PER-02, PER-03, PER-04, PER-05 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Đánh giá có receipt và trạng thái tiếp nhận |
| UI-FBR-02 | Khiếu nại | FR-FB-CASE-001 | PER-02, PER-03, PER-04, PER-05 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Hồ sơ tiếp nhận cùng lịch sử; xử lý chính thức chờ chính sách |
| UI-FBR-03 | Phân tích lựa chọn món | FR-FB-SELR-001 | PER-05 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Số lựa chọn có nguồn khi đủ căn cứ; tỷ lệ chưa xác định |
| UI-FBR-04 | Đề xuất cải tiến thực đơn | FR-FB-PROP-001 | PER-05 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Đề xuất nháp cùng căn cứ và điều kiện kiểm lại |
| UI-FBR-05 | Dashboard bốn vai trò | FR-RPT-ROLE-001 | PER-05, PER-06, PER-07, PER-08 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Bốn góc nhìn có nguồn, trạng thái thiếu và quyền riêng |
| UI-FBR-06 | Nguồn cost % | FR-RPT-CPCT-001 | PER-05, PER-06, PER-07, PER-08 theo quyền riêng | Nguồn, ngày, trạng thái thiếu, form có nhãn; Cost % ngày có nguồn E3; ô theo khách chưa xác định khi thiếu công thức |
| UI-FBR-07 | Rà soát giá và kiểm phương án | FR-AIO-PRRV-001, FR-AIO-RCHK-001 | PER-05, PER-08 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Đề xuất nháp chờ người thật duyệt, hoặc thiếu nguồn; Bảng kiểm có nguồn; dù đủ kiểm vẫn chỉ nháp chờ người thật |
| UI-FBR-08 | Dự toán, nhu cầu và giá lệch | FR-AIO-ESTR-001, FR-AIO-DEMR-001, FR-AIO-PDEV-001 | PER-07 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Nháp diễn giải dự toán chờ người thật rà; Nháp diễn giải nhu cầu với thiếu nguồn rõ ràng; Nháp giải thích; cảnh báo chính thức chưa xác định |
| UI-FBR-09 | Hỗ trợ CRM | FR-AIO-CRMS-001, FR-AIO-CRMQ-001 | PER-05, PER-08 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Nháp tóm tắt và danh sách việc cần người thật rà; Nháp báo giá có nguồn và nhãn chưa phát hành |
| UI-FBR-10 | Hỏi đáp số liệu | FR-AIO-DQA-001 | PER-07, PER-08 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Câu trả lời nháp chờ người thật rà, kèm số nguồn hoặc không đủ dữ liệu |
| UI-FBR-11 | Mục tiêu dinh dưỡng nhóm | FR-NUTR-GRPT-001, FR-NUTR-GRPC-001 | PER-05 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Mục tiêu nhóm nháp có nguồn hoặc danh sách thiếu; So sánh có phiên bản hoặc chưa xác định |
| UI-FBR-12 | Nhật ký bữa đã ăn | FR-NUTR-DCON-001, FR-NUTR-DREC-001, FR-NUTR-DVIW-001, FR-NUTR-DDEL-001 | PER-03 | Nguồn, ngày, trạng thái thiếu, form có nhãn; Đồng ý có phiên bản hoặc nhật ký chưa bật; Bản ghi bữa đã ăn có nguồn hoặc chặn thiếu bằng chứng; Danh sách bữa và dinh dưỡng suất; không phải lượng hấp thu thực; Receipt yêu cầu xóa; trạng thái có bằng chứng, đồng ý bị rút |

Quyền đề xuất phải kiểm trên server; vai trò chỉ là góc nhìn. Dashboard PER-05/06/07/08 dùng chỉ số có nguồn và quyền riêng theo [catalog chỉ số](../api/data-mapping.md). Không tự cấp cost cho PER-06 hoặc mọi Giám đốc. Nhập liệu wireframe chỉ là synthetic; nút review mở dialog và không gửi mạng.
