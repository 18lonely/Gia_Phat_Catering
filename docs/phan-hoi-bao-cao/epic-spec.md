---
id: DOC-E12-EPIC-SPEC-MD
title: "E12: Phản hồi và báo cáo"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e12, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# E12: Phản hồi và báo cáo

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E12; giữ nguyên câu hỏi chưa trả lời |

## 1. Mục tiêu và nguồn

Dữ liệu lựa chọn thật và đánh giá quay về cải tiến thực đơn. [PRD](../gia-phat/01-prd.md) và [roadmap](../gia-phat/02-roadmap.md) là nguồn phạm vi. BO-01/KR1.1 và BO-04/KR2.1 liên quan kiểm thực đơn; BO-02/KR1.2 là mục tiêu R11; BO-05/KR3.1 và BO-06/KR3.2 thuộc G-Next. Không lấy tỷ lệ chọn từng món thay tỷ lệ suất có lựa chọn của BO-05.

## 2. Capability

| Feature | Module | Nội dung | Ưu tiên | Persona | Mức thiết kế |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FEAT-079 | FB / M8 | Đánh giá bữa ăn, khiếu nại | P1 | PER-02 → 05 | Nháp có điều kiện |
| FEAT-080 | FB / M8 | Phân tích món và đề xuất thực đơn | P1 | PER-05 | Nháp có điều kiện |
| FEAT-081 | RPT | Dashboard theo vai trò | P1 | PER-05 → 08 | Nháp có điều kiện |
| FEAT-082 | AIO / AIO-02 | Rà soát thực đơn khi giá đổi | P1 | PER-05, PER-08 | Nháp có điều kiện |
| FEAT-083 | AIO / AIO-03, 04 | Dự toán, nhu cầu nguyên liệu, cảnh báo giá lệch | P1 | PER-07 | Nháp có điều kiện |
| FEAT-084 | AIO / AIO-05 | Hỗ trợ CRM | P1 | PER-05, PER-08 | Nháp có điều kiện |
| FEAT-085 | AIO / AIO-06 | Hỏi đáp số liệu | P2 | PER-07, PER-08 | Nháp có điều kiện |
| FEAT-086 | NUTR / NUTR-06 | Mục tiêu dinh dưỡng theo nhóm người ăn | P1 | PER-05 | Nháp có điều kiện |
| FEAT-087 | NUTR / NUTR-07 | Nhật ký dinh dưỡng cá nhân | P2 | PER-03 | Nháp có điều kiện |

PER-02: người đặt tổng; PER-03: người ăn có tài khoản; PER-04: người ăn qua QR; PER-05: dinh dưỡng viên kiêm CSKH; PER-06: quản lý cơ sở/bếp trưởng; PER-07: kế toán; PER-08: Giám đốc. Persona không tự cấp quyền.

## 3. Thứ tự release và điều kiện

Chỉ mở hồ sơ E12. R12 thuộc Later, cần R6/R7/R10/R11 xong và G-Next; chưa có bằng chứng. Chuẩn bị định nghĩa chỉ số và quyền → review nguồn/contract → chạy ca thật và đối chiếu → mới xét nghiệm thu R12. Không đặt ngày, người phụ trách, story point hoặc chi phí AI.

## 4. Ranh giới

Bốn feature AI chỉ dùng công cụ đọc theo quyền và trả đề xuất nháp chờ người thật duyệt; không tự ghi nghiệp vụ. FEAT-084 chỉ đọc E10, không mở lại hoặc sửa E10. FEAT-086 là mục tiêu nhóm phi y tế, ngưỡng/công thức chờ NUTR-Q01–04. FEAT-087 được thiết kế độc lập: chỉ bữa đã ăn và giá trị dinh dưỡng suất, tự nguyện/có đồng ý/xóa được; không thu, suy luận hoặc lưu sức khỏe, không gợi ý cá nhân. Bất kỳ mở rộng sang FEAT-046/047 chỉ gate O-03, chưa thiết kế nhánh đó.

Thiết kế tài liệu nháp **(65 + 9) / 78 = 74/78 ≈ 94,9 %**. E12 có 9 feature thiết kế nháp có điều kiện, 0 feature chỉ gate. Ba feature FEAT-046/047/063 chỉ gate O-03 ghi riêng, không cộng vào tử số. Không phải BA được duyệt hoặc tiến độ phần mềm. E13/FEAT-088 chưa mở; R6, R7, R10, R11 và G-Next chưa có bằng chứng đạt.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm số phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02 ≤ 3 điểm phần trăm là mục tiêu R11, không phải sai số tính toán. FR-MENU-RCP-007 chặn O-02; FEAT-046/047/063 chặn O-03.

[Phụ thuộc](review/dependencies.md) · [Câu hỏi](review/questions.md) · [SRS](srs/spec.md).
