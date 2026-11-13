---
id: DOC-GIA-PHAT-PROGRESS-STATUS-2026-11-12
title: Rà tiến độ tài liệu BA Gia Phát ngày 12/11/2026
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [progress, review, e1-e13]
depends_on: [DOC-PRD-GIA-PHAT]
author: BA
last_updated: 2026-11-12
---
# Rà tiến độ tài liệu BA Gia Phát ngày 12/11/2026

Nháp · Chỉ đo hồ sơ tài liệu, không đo phần mềm. Nguồn số liệu: [OVERVIEW](../../OVERVIEW.md), [dashboard](../../project-dashboard.md), handoff và báo cáo kiểm của từng epic, [PRD](../01-prd.md), [roadmap](../02-roadmap.md). Không sửa file nào trong số này.

## 1. Kết luận nhanh

| Chỉ số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| Tổng feature theo PRD | 78 | FEAT-001 → FEAT-088 |
| Feature có thiết kế tài liệu nháp | **60 / 78 ≈ 76,9 %** | E1–E5: 23 · E6: 17 · E7: 5 · E8: 6 · E9: 5 · E10: 4 |
| Feature chỉ đặc tả cổng chặn (gate-only) | 3 | FEAT-046, FEAT-047, FEAT-063: chờ O-03, không tính vào độ phủ |
| Feature chưa mở tài liệu | **15** | E11: FEAT-074–078 (5) · E12: FEAT-079–087 (9) · E13: FEAT-088 (1) |
| Feature được stakeholder phê duyệt | 0 | Toàn bộ là nháp có điều kiện |
| Ca kiểm thử sản phẩm đã chạy | 0 | Mọi ca NOT RUN hoặc BLOCKED |
| Backend / migration / UAT | 0 | Schema chung vẫn 65 bảng, chưa migration |
| Câu hỏi / điểm mở đang chờ | ~118 | Liệt kê ở mục 4; 0 câu được đóng bằng quyết định ký |

Nói ngắn: **giai đoạn đặc tả + thiết kế + thiết kế test đã phủ khoảng 3/4 sản phẩm; giai đoạn phê duyệt chưa bắt đầu.** Phần còn lại gồm 3 epic cuối (15 feature, nhóm R11–R13 của roadmap, đều P1/P2) và toàn bộ việc chốt câu hỏi với người có thẩm quyền.

## 2. Tiến độ theo epic

Ký hiệu: ✔ có tài liệu nháp · ◐ có một phần / có điều kiện · ✘ chưa có.

| Epic | Feature | FR · UC · story | AC / ca chức năng | API đề xuất | Màn wireframe | Đặc tả | Thiết kế | Test design | Duyệt | Chạy test |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| E1 Nền tảng | 5 | 26 · 26 · 26 | 78 | 25 HTTP + port nội bộ | 6 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E2 Thực đơn định lượng | 8 | 55 · 13 · 53 | 86 ca rule (BLOCKED) | 60 | 3 | ✔ | ✔ | ◐ (RCP-007 chờ O-02) | ✘ | ✘ |
| E3 Cost + kế toán | 5 | 45 (+6 kế toán) · 16 · 28 (+6) | 108 (+18 thiết kế, +12 nghiệp vụ) | 37 + 8 kế toán | 18 + 4 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E4 Dinh dưỡng | 2 | 5 · 5 · 5 | 28 ca thiết kế | 7 | 3 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E5 Agent nội bộ | 3 | 6 · 6 · 6 | 32 ca thiết kế | 6 | 3 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E6 Chọn món / order | 17 + 2 gate | 19 UC / story | 57 AC; 99 mô tả ca có overlap | 26 HTTP + 2 port | 13 | ✔ | ◐ (14/14 CG OPEN) | ✔ | ✘ | ✘ |
| E7 Giao nhận / doanh thu | 5 | 13 · 13 · 13 | 39 + 8 hệ thống | 18 | 8 | ✔ | ◐ (MISA chưa mapping) | ✔ | ✘ | ✘ |
| E8 Website công khai | 6 | 12 · 12 · 12 | 36 + 12 hệ thống | 16 HTTP + 1 port | 9 | ✔ | ◐ | ✔ | ✘ | ✘ |
| E9 Agent dinh dưỡng viên | 5 + 1 gate | 13 · 13 · 13 | 39 + 13 hệ thống | 11 HTTP + 4 port | 7 | ✔ | ◐ | ✔ | ✘ | ✘ |
| E10 CRM bán hàng | 4 | 16 · 16 · 16 | 48 + 10 hệ thống | 23 HTTP + 7 port | 9 | ✔ | ◐ | ✔ | ✘ | ✘ |
| E11 Mua hàng & sản xuất | 5 | Chưa có | Chưa có | Chưa có | Chưa có | ✘ | ✘ | ✘ | ✘ | ✘ |
| E12 Phản hồi & báo cáo | 9 | Chưa có | Chưa có | Chưa có | Chưa có | ✘ | ✘ | ✘ | ✘ | ✘ |
| E13 Chi phí & lợi nhuận | 1 | Chưa có | Chưa có | Chưa có | Chưa có | ✘ | ✘ | ✘ | ✘ | ✘ |

Các bộ ca hệ thống/invariant có overlap với ca chức năng nên không cộng dồn thành tỷ lệ nghiệm thu. Số liệu E6–E10 lấy từ handoff/báo cáo kiểm của từng gói; E1–E5 lấy từ [dashboard](../../project-dashboard.md).

### Hồ sơ cấp sản phẩm

Kế hoạch tổng thể, PRD, roadmap, URD, BRD và brainstorm phạm vi đều có bản nháp. Mỗi epic E1–E10 có epic spec, SRS, use case, user story, AC, API, data mapping, user flow, wireframe HTML, checklist/test case, RTM, preview HTML và báo cáo kiểm. E3 có thêm quy tắc kế toán, CR, hướng dẫn sử dụng.

## 3. Chất lượng kiểm tài liệu

- Mỗi gói E7–E10 có checker cấu trúc/truy vết/liên kết riêng, renderer sơ đồ và kiểm UI mock ở 1440 / 390 / 360 px; báo cáo cuối của E10 ghi 0 lỗi cấu trúc, 6/6 sơ đồ render, 256 kiểm UI mock 0 lỗi.
- Bảo toàn SHA256: 761 file cũ giữ nguyên ở phiên E10; OVERVIEW và dashboard chỉ append.
- Hạn chế đã biết: lỗi “số dính chữ” (ví dụ `65bảng`, `40/78feature`) còn trong OVERVIEW, dashboard và report lịch sử E6–E9 vì các file này bị khóa sửa; `scripts/render_diagrams.py` mà skill preview nhắc tới không tồn tại; không có `AGENTS.md`.
- Kiểm mock đạt **không** phải test sản phẩm; chưa audit WCAG hay kiểm thiết bị thật.

## 4. Điểm mở đang chặn

| Nhóm | Câu hỏi | Ảnh hưởng chính |
| :--- | :--- | :--- |
| Gốc PRD | O-01 → O-06 | O-02 chặn FR-MENU-RCP-007; O-03 chặn FEAT-046/047/063; O-04 chặn đưa feature lên Now |
| E1 | E1-Q01–05 | Chuẩn API, idempotency, MFA, thông báo, quyền quản trị |
| E2 | DL-01 | Toàn bộ 86 ca rule BLOCKED |
| E3 Cost | CK-Q01–10, DATA-COST-Q01–06, E3-Q14–16 | Thiếu dữ liệu kế toán 10 món / 10 ngày; chi tiết chiết khấu |
| E4 / E5 | NUTR-Q01–04, AIO-Q01–06 | Nguồn công thức dinh dưỡng, điều kiện agent trả nháp đạt |
| E6 | CG01–14, ORD-Q01–15, E6-EVID-001/002 | Ưu tiên duyệt CG01/08/05/06 rồi CG12 |
| E7 | Q-13, E7-Q01–08 | Nhánh phụ thuộc E6 và xuất MISA |
| E8 | E8-Q01–12 | Generation, giá công khai, lead, CMS, cutover |
| E9 | E9-Q01–14 | Identity/consent, nguồn công khai, ngân sách AI |
| E10 | E10-Q01–15 | Tiêu chí trùng, ngưỡng nguy cơ rời, duyệt báo giá/hợp đồng |

Các nguyên tắc đã được người dùng xác nhận và phải giữ: cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %; chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm số phải trả nhà cung cấp; NFR-COST-002 (cost món lệch ≤ 1 đ, cost % ngày lệch ≤ 0,01 điểm phần trăm).

## 5. Nhận định và khuyến nghị

1. **Rủi ro lớn nhất là nợ quyết định, không phải thiếu tài liệu.** ~118 câu mở, 0 câu đóng; mỗi epic mới tiếp tục xây trên nguồn nháp chưa freeze (E11 phụ thuộc Cost E3, MENU E2, kế hoạch E6). Càng mở thêm epic, chi phí sửa khi stakeholder trả lời càng lớn.
2. **E11 là bước tiếp theo tự nhiên** (theo thứ tự roadmap R11, 5 feature P1, liên quan trực tiếp BO-02 về chênh lệch cost thực mua ≤ 3 điểm %).
3. **Song song nên tổ chức một buổi chốt câu hỏi** với Giám đốc / kế toán / bếp trưởng, theo thứ tự: O-03, O-04, DL-01, CK-Q01–10 + dữ liệu 10 món / 10 ngày, E6 CG01/08/05/06. Đây là điều kiện để chuyển cột “Duyệt” từ ✘ sang ✔ cho MVP E1–E5.
4. E12 (9 feature, gồm dashboard và 4 tính năng AI) nên mở sau E11 vì phụ thuộc R6, R7, R10, R11; E13 cần Giám đốc duyệt nguyên tắc phân bổ chi phí trước.

