---
id: DOC-GIA-PHAT-PROGRESS-STATUS-2026-11-13
title: Rà tiến độ tài liệu BA Gia Phát — 13/11/2026
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [progress, review, e1-e13, decision-pack]
depends_on: [DOC-PRD-GIA-PHAT, DOC-GIA-PHAT-PROGRESS-STATUS-2026-11-12]
author: BA
last_updated: 2026-11-13
---
# Rà tiến độ tài liệu BA Gia Phát — 13/11/2026

Nháp · Chỉ đo hồ sơ tài liệu, không đo phần mềm. Nguồn số liệu: [OVERVIEW](../../OVERVIEW.md) (mốc E11, E12, E13), handoff và báo cáo kiểm của từng gói, [PRD](../01-prd.md), [roadmap](../02-roadmap.md), lịch sử git. Bản trước: [12/11/2026](progress-status-2026-11-12.md) (giữ nguyên, không sửa). Không sửa file nào khác.

## 1. Kết luận nhanh

| Chỉ số | 12/11 | 13/11 | Ghi chú |
| :--- | :--- | :--- | :--- |
| Feature có thiết kế tài liệu nháp | 60 / 78 | **75 / 78 ≈ 96,2 %** | Thêm E11 (5), E12 (9), E13 (1) |
| Feature chỉ gate | 3 | 3 | FEAT-046, FEAT-047, FEAT-063 — chờ O-03 |
| Feature chưa mở tài liệu | 15 | **0** | Đã mở đủ 13 epic theo PRD |
| Feature được stakeholder phê duyệt | 0 | 0 | Toàn bộ là nháp có điều kiện |
| Ca kiểm thử sản phẩm đã chạy | 0 | 0 | Mọi ca NOT RUN hoặc BLOCKED |
| Backend / migration / UAT | 0 | 0 | Schema chung vẫn 65 bảng |
| Câu hỏi / gap mở | ~118 | **~169** | Thêm E11-Q 15, E12-Q 18, E13-Q 14; 0 câu đóng |

Nói ngắn: **giai đoạn viết tài liệu nháp đã xong (75/78, 3 còn lại là gate có chủ đích). Giai đoạn phê duyệt vẫn ở 0.** Không còn epic nào để mở. Nút thắt duy nhất bây giờ là chốt quyết định với stakeholder.

## 2. Tiến độ theo epic

Ký hiệu: ✔ có tài liệu nháp · ◐ có một phần / có điều kiện · ✘ chưa có.

| Epic | Feature | FR · UC · story | AC / ca chức năng | API đề xuất | Màn | Đặc tả | Thiết kế | Test design | Duyệt | Chạy test |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| E1 Nền tảng | 5 | 26 · 26 · 26 | 78 | 25 HTTP + port | 6 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E2 Thực đơn định lượng | 8 | 55 · 13 · 53 | 86 ca rule (BLOCKED) | 60 | 3 | ✔ | ✔ | ◐ | ✘ | ✘ |
| E3 Cost + kế toán | 5 | 45 (+6) · 16 · 28 (+6) | 108 (+30) | 37 + 8 | 22 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E4 Dinh dưỡng | 2 | 5 · 5 · 5 | 28 | 7 | 3 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E5 Agent nội bộ | 3 | 6 · 6 · 6 | 32 | 6 | 3 | ✔ | ✔ | ✔ | ✘ | ✘ |
| E6 Chọn món / order | 17 + 2 gate | 19 UC / story | 57 AC | 26 HTTP + 2 port | 13 | ✔ | ◐ (14 CG) | ✔ | ✘ | ✘ |
| E7 Giao nhận / doanh thu | 5 | 13 · 13 · 13 | 39 + 8 | 18 | 8 | ✔ | ◐ (MISA) | ✔ | ✘ | ✘ |
| E8 Website công khai | 6 | 12 · 12 · 12 | 36 + 12 | 16 + 1 port | 9 | ✔ | ◐ | ✔ | ✘ | ✘ |
| E9 Agent dinh dưỡng viên | 5 + 1 gate | 13 · 13 · 13 | 39 + 13 | 11 + 4 port | 7 | ✔ | ◐ | ✔ | ✘ | ✘ |
| E10 CRM bán hàng | 4 | 16 · 16 · 16 | 48 + 10 | 23 + 7 port | 9 | ✔ | ◐ | ✔ | ✘ | ✘ |
| **E11 Mua hàng & sản xuất** | 5 | 15 · 15 · 15 | 45 (13 BLOCKED) + 10 | 15 + 4 port | 9 | ✔ | ◐ | ✔ | ✘ | ✘ |
| **E12 Phản hồi & báo cáo** | 9 | 20 · 20 · 20 | 60 (23 BLOCKED) + 20 | 20 + 7 port | 12 | ✔ | ◐ | ✔ | ✘ | ✘ |
| **E13 Chi phí & lợi nhuận** | 1 | 12 · 12 · 12 | 36 (16 BLOCKED) + 13 | 18 + 5 port | 8 | ✔ | ◐ (chờ phương pháp phân bổ) | ✔ | ✘ | ✘ |

Ca hệ thống có overlap với ca chức năng nên không cộng thành tỷ lệ nghiệm thu.

## 3. Chất lượng kiểm của ba gói mới

| Gói | Cấu trúc / truy vết | Sơ đồ | UI mock | Bảo toàn hash |
| :--- | :--- | :--- | :--- | :--- |
| E11 | 0 lỗi | 7/7 | 283 kiểm, 0 lỗi | 871/873 giữ hash, 2 file append — đạt |
| E12 | 0 lỗi | 7/7 | 378 kiểm, 0 lỗi | 941/945 — **4 sai lệch ghi nhận** |
| E13 | 0 lỗi | 7/7 | 327 kiểm, 0 lỗi | 1068/1070, 2 file append — đạt |

**Giải thích 4 sai lệch hash của E12 (phát hiện khi rà ngày 13/11):** baseline E12 chụp lúc 15:10:45 ngày 12/11. Commit `71e2a4c` lúc 15:14:00 (“gỡ link tới phiên rà soát uc-refresh-2026-11-12 đã xoá”) xóa đúng 2 dòng ở mỗi file `OVERVIEW.md`, `project-dashboard.md`, `gia-phat/review/next-session-prompt.md`, `gia-phat/review/progress-assessment.md` — trùng khớp 4 file và thời điểm ghi ~15:13:53 trong báo cáo E12. Đây là thao tác dọn link có chủ đích của người dùng, không phải lỗi phiên E12. Bằng chứng: `git show 71e2a4c`. Báo cáo E12 không sửa; ghi nhận ở đây và trong gói quyết định.

Hạn chế còn lại (không đổi từ 12/11): lỗi “số dính chữ” trong OVERVIEW/dashboard và report lịch sử E6–E9; không có `AGENTS.md`; `scripts/render_diagrams.py` không tồn tại; kiểm mock không phải test sản phẩm.

## 4. Điểm mở đang chặn — khoảng 169 mục

| Nhóm | Mã | Số | Người cần trả lời (theo nguồn) |
| :--- | :--- | ---: | :--- |
| Gốc PRD | O-01 → O-06 | 6 | Kế toán, Dinh dưỡng viên, Giám đốc |
| E1 | E1-Q01–05 | 5 | Tech lead, Giám đốc |
| E2 | DL-01 | 1 | Dinh dưỡng viên / bếp trưởng |
| E3 | CK-Q01–10, DATA-COST-Q01–06, E3-Q14–16 | 19 | Kế toán |
| E4 / E5 | NUTR-Q01–04, AIO-Q01–06 | 10 | Dinh dưỡng viên, Giám đốc |
| E6 | CG01–14, ORD-Q01–15, E6-EVID-001/002 | 31 | Phụ trách khách, Tech lead |
| E7 | Q-13, E7-Q01–08 | 9 | Kế toán, điều phối |
| E8 | E8-Q01–12 | 12 | Marketing, Giám đốc |
| E9 | E9-Q01–14 | 14 | Dinh dưỡng viên, Giám đốc |
| E10 | E10-Q01–15 | 15 | Kinh doanh |
| E11 | E11-Q01–15 | 15 | Mua hàng, bếp trưởng, kế toán |
| E12 | E12-Q01–18 | 18 | Giám đốc, kế toán, dinh dưỡng viên |
| E13 | E13-Q01–14 | 14 | Giám đốc, kế toán |

Nhiều câu trùng ý giữa các epic (ví dụ: người duyệt ngoại lệ O-06 ↔ E11-Q02 ↔ E13; định nghĩa cost % ↔ E12-Q08 ↔ CK-Q; identity khách E6-CG01 ↔ E9 ↔ E12). Gộp lại có thể giảm đáng kể số quyết định thật phải ký.

Các nguyên tắc đã xác nhận và phải giữ: cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %; chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm số phải trả nhà cung cấp; NFR-COST-002 (≤ 1 đ, ≤ 0,01 điểm phần trăm).

## 5. Nhận định và khuyến nghị

1. **Dừng viết thêm đặc tả.** Mở thêm tài liệu trên nguồn chưa freeze chỉ làm tăng chi phí sửa. 96,2 % là trần thực tế cho tới khi O-03 được trả lời.
2. **Việc tiếp theo là “gói quyết định” (decision pack):** gộp ~169 câu thành một sổ duy nhất, khử trùng, xếp theo người quyết định và theo mức chặn release (MVP R1–R5 trước), kèm chương trình họp.
3. **Thứ tự chốt đề xuất:** O-03, O-04, O-06 → DL-01, O-01/O-02 → CK-Q01–10 + dữ liệu 10 món / 10 ngày → E6 CG01/08/05/06 → phương pháp phân bổ E13. Năm nhóm đầu đủ để chuyển cột “Duyệt” sang ✔ cho MVP E1–E5.
4. Song song có thể rà nhất quán liên epic (mã, thực thể đề xuất ngoài schema 65 bảng ở E11–E13, endpoint trùng chức năng) — nằm trong cùng prompt.
