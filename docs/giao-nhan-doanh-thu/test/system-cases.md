---
id: DOC-E7-TEST-SYSTEM-CASES-MD
title: Ca hệ thống, rule và NFR E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ca hệ thống, rule và NFR E7

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

| Mã | Truy vết | Tiền điều kiện | Bước chạy | Expected | Status | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-E7-SYS-01 | NFR-E7-001 / BR-E7-001 | 2 khách/cơ sở synthetic, từng role và phiên hết hạn | Gọi tất cả18 route với đúng/sai scope, thiếu role, hết phiên; kiểm body/log | 401 ERR-E7-401-01,403 ERR-E7-403-01,404 ERR-E7-404-01; không lộ dữ liệu/secret | BLOCKED E7-Q01/08 |  |  |
| TC-E7-SYS-02 | BR-E7-006/007 | Giá inclusive synthetic 40000, VAT thử8%, invoice true/false; CK riêng200000 | Giữ nguồn, đổi cờ hóa đơn trong bộ dữ liệu thử độc lập; tính/đọc | Phải trả không đổi chỉ vì invoice=false; CK không giảm phải trả; missing VAT không0 | NOT RUN |  |  |
| TC-E7-SYS-03 | BR-E7-003/008 / NFR-E7-002 | Chứng từ thu synthetic và fault trước/sau commit | Gửi đồng thời/lặp chứng từ; ngắt phản hồi; tra dữ liệu/audit trước lệnh mới | Không cộng hai lần, không success một phần; ERR-FIN-422-03 khi chứng từ trùng; replay oracle chi tiết chờ Q08 | BLOCKED E7-Q06/08 |  |  |
| TC-E7-SYS-04 | NFR-E7-003 / BR-E7-011 | Tháng biên bản thật 2 khách và mẫu MISA có version (chưa có) | Đối chiếu từng dòng/tổng, xuất và thử nhập MISA, lưu evidence | Khớp theo chuẩn được duyệt; MISA nhận file; synthetic không đủ nghiệm thu | BLOCKED E7-Q04/07 và dữ liệu thật |  |  |
| TC-E7-SYS-05 | BR-E7-002/010 | Nguồn E6 thiếu/không sẵn sàng hoặc gate chưa chốt | Thử NOTE/REV/REC; kiểm không ghi và hiển thị reason | ERR-E7-503-01 + mã gate; không lấy0 hoặc tự quyết CG05/06 | NOT RUN |  |  |
| TC-E7-SYS-06 | NFR-E7-004 | Profile E7 synthetic 1000CCU sau khi được duyệt | Đo p95 đọc/ghi, error và duplication, tách job xuất | Đọc≤300ms/ghi≤800ms theo nền; chưa có target xuất file mới | BLOCKED E7-Q08/môi trường |  |  |
| TC-E7-SYS-07 | NFR-E7-005 | HTML mới synthetic, viewport390/1440 | Mở8 màn, thử validation, trạng thái loading/empty/error/offline và reopen; chụp/xem ảnh | Không tràn toàn trang; label/focus/nhãn BLOCKED rõ; chỉ chứng minh mock | NOT RUN (kết quả mock riêng validation/ui-result.json) |  |  |
| TC-E7-SYS-08 | BR-E7-003/010 | Fault server có requestId synthetic | Mô phỏng lỗi nội bộ sau gửi và kiểm UI/log | ERR-E7-500-01 không lộ upstream body; UNKNOWN, không auto-submit | BLOCKED E7-Q08 |  |  |

8 ca bổ sung có overlap với39 ca AC, không cộng thành47 mục tiêu độc lập. 0 test backend. SYS07 có thể kiểm mock riêng, không đổi thành PASS sản phẩm.
