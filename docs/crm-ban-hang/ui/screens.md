---
id: DOC-E10-UI-SCREENS-MD
title: 9 màn hình review E10
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# 9 màn hình review E10

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

| Màn | Tên | Nhóm FR | Nội dung |
| :--- | :--- | :--- | :--- |
| UI-CRM-01 | Hồ sơ khách hàng 360° | VIEW/CONT | Liên hệ, điểm, hợp đồng, order, doanh thu, phản hồi; nguồn và trạng thái từng nhóm |
| UI-CRM-02 | Tiếp nhận yêu cầu tư vấn | LEAD | Nguồn website/E9, nháp thực đơn, receipt và chờ người thật |
| UI-CRM-03 | Rà trùng, duyệt gộp và hoàn tác | DUP/MRG/UNDO | Diff từng trường, bằng chứng, người duyệt, ảnh trước và liên kết mới |
| UI-CRM-04 | Vòng đời và nguy cơ rời | LIFE/RISK | Lịch theo điểm, ngày nghỉ, bằng chứng và chưa đủ dữ liệu |
| UI-CRM-05 | Cơ hội và phễu | OPP | Chủ cơ hội, giai đoạn đề xuất, lịch sử và mẫu số |
| UI-CRM-06 | Báo giá nội bộ có phiên bản | QUOT/MENU | Giá theo loại suất, điều kiện, thực đơn, cost/margin chỉ nội bộ có quyền |
| UI-CRM-07 | Bản báo giá dành cho khách | SAFE | Projection riêng, giá bán/điều kiện/thực đơn được duyệt, không cost/margin |
| UI-CRM-08 | Hợp đồng | CONT/ACTV | Bằng chứng chấp thuận/ký, trạng thái, giá theo loại suất, hiệu lực |
| UI-CRM-09 | Phụ lục và tra giá | AMND/PRIC | Lịch sử trước/sau, từ–đến, xung đột khoảng và nguồn giá theo ngày |

[Wireframe](../html-wireframe/crm-workbench.html) là một HTML đen trắng, không mạng hoặc lưu dữ liệu. Có điều hướng, lựa chọn trạng thái và mở hộp review; không giả gửi/gộp/kích hoạt thành công. Người review xem cả bình thường, tải, rỗng, thiếu nguồn, lỗi, mất mạng, không quyền, xung đột. Màn khách dùng mẫu dữ liệu riêng; kiểm mock không chứng minh API bảo vệ projection.
