---
id: DOC-AGENT-NOI-BO-REVIEW-DEPENDENCIES
title: Phụ thuộc E5 Agent Nội bộ
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [dependencies, e5]
author: BA
last_updated: 2026-11-16
---
# Phụ thuộc E5: Agent Nội bộ

Draft · 16/11/2026 · Gom từ roadmap, [gói review E4/E5](../../gia-phat/review/mvp-e4-e5-handoff.md), [kiến trúc AI agent](../../nen-tang/srs/agent-architecture.md) và các epic dùng E5; không thêm quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo theo khuôn chung các epic: E5 chờ gì, epic nào dùng E5 |

## 1. E5 đang chờ gì

| Cần có | Loại | Nguồn | Chặn |
| :--- | :--- | :--- | :--- |
| R2: bộ kiểm quy tắc không lưu, áp dụng thành bản nháp | Kỹ thuật | [E2](../../thuc-don-dinh-luong/srs/spec.md) | FR-AIO-CHK-001, FR-AIO-APLY-001 |
| R3: kiểm cost phương án, đọc cost theo quyền | Kỹ thuật | [E3](../../cost/srs/spec.md) | FR-AIO-CHK-001 |
| Tài khoản dịch vụ `svc-agent-noi-bo`, giao quyền | Kỹ thuật | [E1](../../nen-tang/srs/spec.md) FR-AUTH-SVC-001 | Mọi lượt chạy |
| O-04: nhà cung cấp mô hình, hạ tầng | Quyết định | [BRD mục 11](../../gia-phat/06-brd.md) | Bắt đầu R5 |
| Hạn mức, hành vi khi CANH_BAO, quyền đọc log, tiêu chí nháp đạt, contract, đo phản hồi đầu (AIO-Q01 đến Q07) | Quyết định | [Câu hỏi E5](questions.md) | Theo từng FR |
| Baseline thời gian dựng thực đơn trước MVP và 20 yêu cầu thử | Dữ liệu | [Roadmap R5](../../gia-phat/02-roadmap.md) | Đo BO-03, nghiệm thu R5 |
| Dinh dưỡng E4 | Kỹ thuật, không bắt buộc | [E4](../../dinh-duong/srs/spec.md) | Chỉ hiển thị chỉ số; R5 không phụ thuộc cứng R4 |

## 2. Epic nào dùng E5

| Epic dùng | Dùng gì của E5 | Ghi chú |
| :--- | :--- | :--- |
| E12 Phản hồi và báo cáo | Runtime agent, công cụ chỉ đọc cho FEAT-082 đến FEAT-085 | Công cụ đọc kế hoạch, tồn, CRM, báo cáo được thêm ở R12 |
| E9 Agent Dinh dưỡng viên | Không dùng chung | Hai agent tách tài khoản, hàng đợi, công cụ, hạn mức (BR-AIN-006) |

E5 là bản MVP v1.0.0; cổng G-Now chỉ đạt khi dinh dưỡng viên dùng hệ thống thật 4 tuần liên tiếp.
