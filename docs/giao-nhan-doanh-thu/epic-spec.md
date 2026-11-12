---
id: DOC-E7-EPIC-SPEC-MD
title: E7 — Giao nhận & doanh thu
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# E7 — Giao nhận & doanh thu

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

## Mục tiêu và phạm vi

Khép vòng từ order đến đối soát theo [PRD](../gia-phat/01-prd.md) và [roadmap](../gia-phat/02-roadmap.md). Chỉ dẫn người dùng 12/11/2026 mở tài liệu E7 thay lệnh cũ không mở E7–E13 **chỉ đối với E7**. E8–E13 chưa mở. E6 dừng chờ CG01/08/05/06, không đặc tả tiếp producer hoặc giả contract freeze.

| Feature | Tên | P0 theo PRD | P1 |
| :--- | :--- | :--- | :--- |
| FEAT-049 | Giao hàng và xác nhận nhận | Theo suất; xác nhận bằng link | Không có trong PRD; không tự thêm |
| FEAT-050 | Biên bản chênh lệch | Giao bù, giảm trừ theo thoả thuận | Không có trong PRD; không tự thêm |
| FEAT-051 | Doanh thu ghi nhận | Số tính tiền × giá chụp tại thời điểm order | Không có trong PRD; không tự thêm |
| FEAT-052 | Đối soát, thu tiền, khoá kỳ | Mở lại kỳ cần Giám đốc duyệt | Không có trong PRD; không tự thêm |
| FEAT-053 | Xuất file MISA | Theo mẫu nhập của MISA | Không có trong PRD; không tự thêm |

Trong phạm vi: 13 FR cho phiếu theo suất, link xác nhận, biên bản/thỏa thuận chênh lệch, số tính tiền × giá chụp, đối soát/thu tiền/khóa/mở lại, chuẩn bị xuất theo mẫu MISA.

Ngoài phạm vi: backend, migration, SQL, sửa DBML65 bảng; CRM/E8–E13; điều phối xe/kho/lợi nhuận, phát hành hóa đơn, tích hợp trực tiếp MISA; tự chi trả/bù trừ CK. Không lấy dòng món làm số suất.

## R7 nguyên văn từ roadmap

| Release | Tên đợt phát hành | Mục tiêu chính | Danh sách Feature ID | Cỡ | Điều kiện bắt đầu | Ngày dự kiến | Tiêu chí nghiệm thu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

| `R7` · v1.2.0 | Giao nhận & doanh thu (E7) | Khép vòng từ order đến đối soát | `FEAT-049` → `FEAT-053` | L | R6 xong; chốt quy tắc khi khách không xác nhận (Q-13) | Chờ O-04 | Doanh thu một tháng do hệ thống tính khớp biên bản đối soát với khách của 2 công ty chạy thử; file xuất nhập được vào MISA; kỳ đã khoá không sửa được nếu Giám đốc chưa duyệt mở lại |

**Cổng G-Next** (điều kiện để mở đợt Later): ≥ 90% order của các công ty đã chuyển lên hệ thống ghi nhận qua cổng (BO-06); ≥ 70% suất có lựa chọn của người ăn trước hạn chốt (BO-05); số phiên truy cập tự nhiên sau 60 ngày ≥ 90% mức trước chuyển đổi (BO-09).

R6 xong và chốt Q-13 là điều kiện release, chưa đạt chỉ vì mở hồ sơ nháp. G-Next là cổng Later, không là quyền mở E8–E13 phiên này. Không gán ngày triển khai/effort/người phụ trách.

## Tiêu chí bàn giao hồ sơ nháp

Mỗi feature có FR/UC/story/AC/API/UI/test và gate tại chỗ. [RTM](test/traceability.md) · [Phụ thuộc](review/dependencies.md) · [Câu hỏi](review/questions.md) · [Kiểm](validation/report.md).

5/5 feature có thiết kế có điều kiện, 0 feature E7 chỉ gate. FEAT-053 có preflight/provenance/luồng xuất nhưng **chưa mapping cột file**. Đây không phải BA được duyệt hoặc phần mềm hoàn thành.
