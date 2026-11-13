---
id: DOC-E13-EPIC-SPEC-MD
title: "E13: Chi phí và lợi nhuận"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# E13: Chi phí và lợi nhuận

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## 1. Mục tiêu và phạm vi

Đúng một feature FEAT-088, EXP / M10, P2, PER-07 (Kế toán), PER-08 (Giám đốc). Đây là epic cuối theo [PRD](../gia-phat/01-prd.md). Mục tiêu R13: báo cáo lợi nhuận theo khách đối chiếu được với kết quả kinh doanh từng cơ sở.

Bốn năng lực đều P2: ghi chi phí cơ sở theo kỳ/loại; chấm công và tham chiếu chi phí nhân công; quản lý phiên bản phương pháp được duyệt; báo cáo và đối chiếu có truy nguyên. Không thêm feature PRD.

## 2. Điều kiện phát hành

[Roadmap R13](../gia-phat/02-roadmap.md) cần R7, R11 xong và Giám đốc duyệt nguyên tắc phân bổ. Chưa có bằng chứng cho cả ba. Thứ tự dự kiến: review nguồn và câu hỏi → duyệt nguyên tắc/phạm vi → chốt contract và kiểm dữ liệu → kiểm R13. Không gán ngày triển khai, người cụ thể hoặc effort. Mở tài liệu không miễn gate.

Không chọn phương pháp phân bổ. Chưa có bản duyệt thì báo cáo khách BLOCKED, chỉ xem chi phí trực tiếp; bản báo cáo luôn giữ methodVersionRef kể cả null kèm lý do khi bị chặn.

## 3. Ngoài phạm vi

Không tính lương, bảo hiểm, thuế TNCN, thanh toán lương, thay thế kế toán/MISA, định nghĩa lại cost hoặc doanh thu, AI, backend, migration. Không tự mở khóa E7 hoặc sửa producer E3/E7/E10/E11/E12.

## 4. Rủi ro và đo kết quả

Rủi ro chính: đếm trùng nguyên liệu/khoản khoán; trộn dự toán với thực mua; lấy phân ca làm chấm công; lộ lương; phần chưa phân bổ bị giấu. Chỉ nghiệm thu khi cùng kỳ/cơ sở/định nghĩa, phần chưa phân bổ bằng 0 và tổng lợi nhuận khách khớp số chuẩn cơ sở. Bộ chứng cứ thực chưa có.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn; không giảm số phải trả nhà cung cấp, không tự khấu trừ số khách phải trả. Chưa quyết định khoản chiết khấu đi vào lợi nhuận thế nào. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-01 (cost ≤ 52 % doanh thu) và BO-02 (≤ 3 điểm phần trăm) là mục tiêu kinh doanh, không là dung sai đối chiếu E13. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03.

[Đặc tả](srs/spec.md) · [Câu hỏi](review/questions.md) · [Điểm nối](review/dependencies.md).
