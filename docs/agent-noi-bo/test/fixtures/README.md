---
id: DOC-AGENT-NOI-BO-TEST-FIXTURES-README
title: Fixture giả lập E5
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [test, fixture, e5]
author: BA
last_updated: 2026-11-16
---
# Fixture giả lập E5: Agent Nội bộ

Draft · 16/11/2026 · Dữ liệu giả lập, không gọi mô hình AI.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo bộ yêu cầu và kịch bản cost giả lập theo khuôn chung các epic |

[synthetic.json](synthetic.json) gồm 4 yêu cầu mẫu (dựng tuần, kiêng mơ hồ, chỉnh một món, câu chèn lệnh) và 2 kịch bản cost (vượt ngưỡng ở CANH_BAO, thiếu VAT). Danh mục món dùng lại [fixture E2](../../../thuc-don-dinh-luong/test/fixtures/README.md).

- Kết quả mong đợi theo SRS hiện tại; hành vi khi CANH_BAO chờ AIO-Q02, cách hiểu kiêng diễn đạt tự do chờ AIO-Q05.
- Không phải bộ 20 yêu cầu nghiệm thu R5 (AIO-Q03). Không có mô hình nên không có output thật.
- Không phải seed runtime, không dùng làm bằng chứng nghiệm thu.
