---
id: DOC-DINH-DUONG-TEST-FIXTURES-README
title: Fixture giả lập E4
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, fixture, e4]
author: BA
last_updated: 2026-11-16
---
# Fixture giả lập E4: Dinh dưỡng

Draft · 16/11/2026 · Dữ liệu giả lập, không phải dữ liệu Gia Phát.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Tách số liệu giả định đang ghi trong TC-NUTR-001 đến 007 ra file riêng theo khuôn chung các epic |

[synthetic.json](synthetic.json) dùng lại đúng số đã ghi trong [test case E4](../test-cases.md): nguyên liệu I1 có 100 kcal, 10 g đạm, 2 g béo, 15 g bột đường trên 100 g phần ăn được, tỷ lệ ăn được 80%; công thức R1 dùng 50 g I1.

- Nếu định lượng 50 g là gram sống còn phần bỏ đi: phần ăn được 40 g, ra 40 kcal.
- Nếu 50 g đã là phần ăn được: ra 50 kcal.

Hai biến thể được giữ song song vì NUTR-Q02 chưa trả lời. Công thức R2 có I2 chưa có số liệu, dùng cho ca thiếu dữ liệu: tổng để trống, không ghi 0. Làm tròn chờ NUTR-Q04.

Không phải seed runtime, không phải 30 món hay 5 suất tính tay của R4 (DATA-NUTR-Q01). Không dùng file này làm bằng chứng nghiệm thu.
