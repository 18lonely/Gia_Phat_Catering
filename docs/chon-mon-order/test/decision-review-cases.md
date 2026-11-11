---
id: DOC-E6-DECISION-REVIEW-CASES
title: Ca review quyết định E6
version: 0.1.0
phase: Review
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Ca review quyết định E6

Dữ liệu **synthetic**. Expected là đề xuất trong [DR-01–04](../review/decision-review.md), chưa quyết định nghiệp vụ. Tất cả Actual/Evidence chưa có; không test backend đã chạy. Không nhập tên/mã người thật để minh họa.

| TC / truy vết | Given | When | Then đề xuất | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-DR-01 / RV01; FEAT-031/032/036; UC002/003/007; API008/009/002 | Membership M được công ty xác nhận, đã chọn A qua account | M xác minh trên guest thiết bị khác rồi đổi B | Cùng một lựa chọn nghiệp vụ, A giảm1/B tăng1; không tạo suất thứ2 | BLOCKED ORD-Q01/11 |
| TC-E6-DR-02 / RV01; FR-AUTH-QSES-001 | Người X biết mã nhân viên M nhưng không có bằng chứng sở hữu | Gửi QR công ty và mã M | Không cấp phiên ghi thay M chỉ dựa mã; không tiết lộ thông tin M | BLOCKED ORD-Q01 |
| TC-E6-DR-03 / RV02; FEAT-036/042; UC007/013; API002/004 | T=100,S=60,C=10; M có allocation chọn hộ | M tự chọn B trước hạn | S=61,C=9,D=30; chuyển nguồn/món nguyên tử, giữ actor nhập hộ trong lịch sử | BLOCKED ORD-Q06 |
| TC-E6-DR-04 / RV03; FEAT-036/038; UC007/009; API002/004 | Đã gửi T=70,S=60,C=10 | Người mới gửi chọn | Theo phương án khuyến nghị: từ chối vượt T, giữ S/C/T; không tự tăng tổng | BLOCKED ORD-Q06/13 |
| TC-E6-DR-05 / RV04; FR-ORD-SUB-001; API003/004 | Summary token10; người khác đổi lựa chọn nên token11 | Gửi tổng với summaryVersion10 | 409, không ghi tổng dựa snapshot cũ; tải summary11 và xác nhận lại | BLOCKED thiết kế summary token/môi trường |
| TC-E6-DR-06 / RV06; FEAT-040/048; UC011/019; API020/025 | Scope có2điểm theo lịch; A khóa, B NEEDS_ATTENTION | Bếp đọc plan từ A | Nêu thiếu B; không hiển thị đầy đủ hoặc coi B=0 | BLOCKED ORD-Q07/13/14 |
| TC-E6-DR-07 / RV05; FEAT-048; UC019 | Plan2 đã publish, bếp mới nhận Plan1 | Xem trạng thái phát hành/nhận/sản xuất | Plan2 chưa được xác nhận nhận; publish không tự chuyển IN_PRODUCTION | BLOCKED ORD-Q14 |
| TC-E6-DR-08 / RV08; FEAT-040; UC011; PORT-LOCK | Qua hạn, lock thiếu default; có bản menu mới | Người không có quyền xử lý ngoại lệ retry với nguồn mới | Không dùng retry kỹ thuật để vượt quyền; cần quyết định/nguồn/version hợp lệ | BLOCKED ORD-Q07/12 |
