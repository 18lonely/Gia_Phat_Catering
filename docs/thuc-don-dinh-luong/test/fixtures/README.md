---
id: DOC-THUC-DON-TEST-FIXTURES-README
title: Fixture giả lập E2
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, fixture, e2]
author: BA
last_updated: 2026-11-16
---
# Fixture giả lập E2: Thực đơn và định lượng

Draft · 16/11/2026 · Dữ liệu giả lập, không phải món hay công thức của Gia Phát.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo bộ nguyên liệu, món, công thức, loại suất giả lập theo khuôn chung các epic |

[synthetic.json](synthetic.json) gồm 3 nguyên liệu (một có xương với hao hụt 20%), 3 món (hai món chính, một rau), một công thức chuẩn cho mỗi món và một loại suất 40.000 đ cho chọn 1 trong 3 món chính.

- Quy đổi kg sang g là 1000; định lượng tối thiểu, chuẩn, tối đa chỉ để thử kiểm khoảng.
- Ví dụ quy tắc "hai món chính cùng chiên" chỉ minh họa; quy tắc nào là cứng, mềm và con số chờ DL-01. 86 ca trong [ca quy tắc](../rule-test-cases.md) vẫn BLOCKED.
- Không phải 30 món của DL-03 đến DL-05. Không phải seed runtime, không dùng làm bằng chứng nghiệm thu R2.
