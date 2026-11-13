---
id: DOC-CHON-MON-ORDER-EPIC-SPEC
title: "E6: Chọn món và Order: gói BA để review"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# E6: Chọn món và Order: gói BA để review

**Draft: thiết kế BA để review; chưa duyệt nghiệp vụ, chưa triển khai phần mềm.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung theo kế hoạch; giữ điểm mở và xác nhận đã có |

## Phạm vi

R6, FEAT-030–048 theo PRD:19 tính năng, gồm14 P0 và5 P1. Gói v0.2 có đầy đủ nhóm tài liệu review: UC, flow/state/data, API, wireframe, backlog/AC/test, RTM và preview; còn các gate chưa được phê duyệt. Các FR dưới đây là mức capability cần phân rã thêm khi chốt câu hỏi; không coi số19FR là đủ test toàn sản phẩm.

Đối tượng: người đặt tổng, người ăn có tài khoản/QR, dinh dưỡng viên nhập hộ, bếp trưởng/quản lý cơ sở, scheduler. E6 không ghi nhận doanh thu/xử lý giao nhận/MISA (E7), không mở CRM đầy đủ (E10).

## Phụ thuộc và nghiệm thu

E1–E5 đủ điều kiện G-Now trước release R6. Có thể soạn tài liệu trước khi phần mềm vượt G-Now. Mục tiêu roadmap:1000 người chọn trong10 phút trước hạn chốt,0 lựa chọn mất/trùng; phần chưa chọn về mặc định; chặn vượt định mức; chạy thử2 công ty trong2 tuần. Chưa có môi trường/dữ liệu thật để kiểm.

FEAT-046/047 gated O-03; không tự thêm thông tin bệnh lý. Q-14 kênh nhắc,Q-16 hạn/ngưỡng đổi,O-06 người duyệt còn mở. Ngày/ước lượng chờ O-04.

[SRS review](srs/spec.md) · [Câu hỏi](review/questions.md) · [Dữ liệu](srs/erd.md) · [Luồng](srs/flows.md) · [Backlog](userstories/backlog.md) · [Ca trọng yếu](test/test-cases.md).

## Bổ sung v0.2.0

[Preview](preview.html) · [Scope assessment](review/scope-assessment.md) · [Bàn giao](review/handoff.md) · [Báo cáo kiểm tra](validation/report.md). 19UC,57AC,26HTTP endpoint,2port,13màn wireframe; 2 feature O-03 chỉ có gate. Giữ10ca gốc, bổ sung57ca theoAC và12ca hệ thống; không có kết quả kiểm thử backend.
