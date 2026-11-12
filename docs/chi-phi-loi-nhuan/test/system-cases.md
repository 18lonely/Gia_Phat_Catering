---
id: DOC-E13-TEST-SYSTEM-CASES-MD
title: Ca hệ thống và lỗi dùng chung E13
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Ca hệ thống và lỗi dùng chung E13

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

Các ca có overlap với chức năng, không cộng thành tỷ lệ nghiệm thu. Mỗi ca chuẩn bị dữ liệu synthetic theo tiền điều kiện, đăng nhập actor/scope tương ứng rồi thực hiện bước mô tả.

| Test | FR / NFR | Tiền điều kiện / dữ liệu | Bước | Expected | Status | Gate | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-EXP-SYS-01 | FR-EXP-SAFE-001; NFR-EXP-001 | Người ngoài scope biết runRef | Gọi API đọc/nguồn và yêu cầu export qua phiên khác. Kiểm payload/lỗi/cache/file. | ERR-EXP-403-01; 0 trường lương/lợi nhuận lộ. | NOT RUN | Quy tắc quyền tối thiểu đã có |  |  |
| TC-EXP-SYS-02 | FR-EXP-SAFE-001; NFR-EXP-001 | Bản mẫu gửi khách của E10/E12 | Kiểm projection server, file, metadata, trường lồng nhau và thông báo lỗi. | Không có cost, lợi nhuận, biên lợi nhuận, người/giờ/đơn giá công; không chỉ ẩn CSS. | NOT RUN | Kiểm liên gói chỉ thiết kế, không sửa producer |  |  |
| TC-EXP-SYS-03 | FR-EXP-SRC-001; NFR-EXP-002 | E7 lỗi hoặc chưa đối soát | Cung cấp số suất giao hợp lệ rồi yêu cầu báo cáo. | ERR-EXP-422-02; không tự tính doanh thu từ giao. | NOT RUN | E7-Q03/04/05 giữ mở |  |  |
| TC-EXP-SYS-04 | FR-EXP-COST-001; BR-EXP-002 | Nguồn cost có VAT, cờ hóa đơn false, CK riêng | Đọc manifest và đối chiếu tiền nguồn; thử nhập lại khoản khoán. | Cost giữ VAT phải trả; không suy VAT 0 %; CK không giảm phải trả NCC/khách; ERR-EXP-409-03 nếu trùng nguồn. | BLOCKED | E13-Q01/08; CK/DATA-COST |  |  |
| TC-EXP-SYS-05 | FR-EXP-RECON-001; NFR-EXP-003 | Hai cơ sở cùng khách; một cơ sở thiếu nguồn | Đối chiếu từng cơ sở rồi yêu cầu tổng khách. | Không dùng cơ sở đủ bù cơ sở thiếu; tổng khách chưa hoàn tất. | BLOCKED | E13-Q07/08/14 |  |  |
| TC-EXP-SYS-06 | FR-EXP-PER-001; FR-EXP-ADJ-001; NFR-EXP-002 | Kỳ khóa và yêu cầu sửa/điều chỉnh đồng thời | Ghi nhận hash cũ, gửi sửa trực tiếp, tạo đề nghị thiếu lý do. | ERR-EXP-409-01 và ERR-EXP-422-04; bản cũ bất biến. | NOT RUN | Chưa có sản phẩm |  |  |
| TC-EXP-SYS-07 | FR-EXP-SRC-001; NFR-EXP-004 | Profile tải E13 được duyệt | Chạy tải đọc/ghi và báo cáo theo bộ nguồn đủ lớn; đo p95/5xx. | Đối chiếu nền 1000 người dùng, p95 đọc ≤ 300 ms, ghi ≤ 800 ms; run theo profile riêng. | BLOCKED | E13-Q12; chưa môi trường/profile |  |  |
| TC-EXP-SYS-08 | FR-EXP-SRC-001; NFR-EXP-002 | Timeout sau ghi nhận hoặc nguồn cập nhật giữa lượt | Đối soát receipt rồi yêu cầu lại cùng khóa; so version nguồn. | Không ghi lặp hoặc trộn revision; lần mới giữ manifest riêng. | BLOCKED | E13-Q12 |  |  |
| TC-EXP-SYS-09 | FR-EXP-TIME-001; FR-EXP-SAFE-001; NFR-EXP-006 | Audit thao tác công có dữ liệu lương | Xem log phổ thông và audit bảo vệ bằng vai trò ngoài quyền. | Log không chứa lương; audit có actor/thời điểm/ref/lý do, không lộ ngoài quyền. | NOT RUN | Retention chờ Q11 |  |  |
| TC-EXP-SYS-10 | FR-EXP-SRC-001 | Chưa xác thực | Gửi request đọc nguồn với điều kiện lỗi; so snapshot trước/sau. | ERR-EXP-401-01; Phiên làm việc không hợp lệ. Không thay số thiếu bằng 0. | NOT RUN | Contract mapping chờ Q12, nguyên tắc an toàn độc lập |  |  |
| TC-EXP-SYS-11 | FR-EXP-SRC-001 | Không tìm thấy tham chiếu trong phạm vi được phép | Gửi request đọc nguồn với điều kiện lỗi; so snapshot trước/sau. | ERR-EXP-404-01; Không tìm thấy dữ liệu. Không thay số thiếu bằng 0. | NOT RUN | Contract mapping chờ Q12, nguyên tắc an toàn độc lập |  |  |
| TC-EXP-SYS-12 | FR-EXP-SRC-001 | Nguồn không truy cập được | Gửi request đọc nguồn với điều kiện lỗi; so snapshot trước/sau. | ERR-EXP-503-01; Tạm thời chưa đọc được nguồn. Không thay số thiếu bằng 0. | NOT RUN | Contract mapping chờ Q12, nguyên tắc an toàn độc lập |  |  |
| TC-EXP-SYS-13 | FR-EXP-RECON-001; NFR-EXP-005 | Wireframe ở 1440 / 390 / 360 px | Mở cả tám màn, tab bàn phím, thử form/dialog và trạng thái thiếu/lỗi. | Không tràn ngang toàn trang, đọc được nhãn gate; mục tiêu WCAG AA cần audit riêng. | NOT RUN | Kiểm mock không thay ca sản phẩm |  |  |

