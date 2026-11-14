---
id: DOC-DINH-DUONG-REVIEW-DEPENDENCIES
title: Phụ thuộc E4 Dinh dưỡng
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [dependencies, e4]
author: BA
last_updated: 2026-11-16
---
# Phụ thuộc E4: Dinh dưỡng

Draft · 16/11/2026 · Gom từ roadmap, [gói review E4/E5](../../gia-phat/review/mvp-e4-e5-handoff.md) và các epic dùng E4; không thêm quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic: E4 chờ gì, epic nào dùng E4 |

## 1. E4 đang chờ gì

| Cần có | Loại | Nguồn | Chặn |
| :--- | :--- | :--- | :--- |
| R2: nguyên liệu, công thức có định lượng | Kỹ thuật | [E2](../../thuc-don-dinh-luong/srs/spec.md) | Toàn epic |
| Nguồn dữ liệu thành phần có ấn bản, trang (BRD DP-03) | Dữ liệu | [BRD mục 10](../../gia-phat/06-brd.md) | FR-NUTR-REF-001/002 |
| Ấn bản bảng thành phần, ý nghĩa định lượng sống, tổ hợp suất mẫu, làm tròn và dung sai "khớp" 5 suất (NUTR-Q01 đến Q04) | Quyết định | [Câu hỏi E4](questions.md) | FR-NUTR-CALC-001/002; nghiệm thu R4 |
| 5 suất tính tay độc lập (DATA-NUTR-Q01) | Dữ liệu | Câu hỏi E4 | Nghiệm thu R4 |
| O-02: một hay nhiều cỡ định lượng | Quyết định | [BRD mục 11](../../gia-phat/06-brd.md) | Tính dinh dưỡng theo cỡ |

R3 (Cost) và R4 không phụ thuộc nhau; có thể làm song song.

## 2. Epic nào dùng E4

| Epic dùng | Dùng gì của E4 | Ghi chú |
| :--- | :--- | :--- |
| E5 Agent Nội bộ | Bốn chỉ số của phương án | Agent không tự tính dinh dưỡng |
| E6 Chọn món | Thông tin dinh dưỡng món đã công bố (FR-NUTR-DSP-001) | Nhãn "ước tính từ định lượng sống" |
| E8 Website | Bốn chỉ số cho thực đơn mẫu | E8-Q04 chờ |
| E9 Agent Dinh dưỡng viên | SafeNutrition cho candidate chưa lưu | Adapter candidate chưa lưu chờ E9-Q11/12 |
| E12 Phản hồi | Mục tiêu nhóm, snapshot cho nhật ký bữa đã ăn | Không thu dữ liệu sức khỏe |

FEAT-046, FEAT-047 (hồ sơ và gợi ý cá nhân) vẫn chỉ gate O-03; E4 không nhận hồ sơ sức khỏe.
