---
id: DOC-GP-SCOPE-001
title: Sổ phạm vi sản phẩm Gia Phát
version: 0.1.0
phase: Discovery
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Sổ phạm vi sản phẩm và quyết định kế thừa

Draft · Tổng hợp từ tài liệu đã có, không phải buổi phỏng vấn hay quyết định mới.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung đầu ra bước1 của kế hoạch; tách quyết định kế thừa và điểm mở |

## Phạm vi hiện hành

Nguồn ưu tiên: xác nhận trực tiếp của người dùng → PRD/roadmap và SRS đã cập nhật → kế hoạch khung lịch sử. Khi nguồn chưa thống nhất, ghi câu hỏi, không tự chọn quyết định nghiệp vụ.

| Đợt | Phạm vi | Trạng thái tài liệu |
| :--- | :--- | :--- |
| Now | E1–E5,23 tính năng nội bộ | SRS nháp và gói BA để review; chưa triển khai/UAT |
| Next | E6–E9,36 tính năng | E6 có gói BA review v0.2 còn gate; E7–E9 chưa có SRS riêng |
| Later | E10–E13,19 tính năng | Phạm vi PRD/roadmap; chưa SRS riêng |

## Quyết định đã có nguồn — không hỏi lại như chưa từng chốt

| Chủ đề | Nguồn | Nội dung giữ nguyên |
| :--- | :--- | :--- |
| Giá công khai | D-10 | Khách vãng lai thấy giá suất |
| Người không chọn | D-14 | Dùng món mặc định; tổng suất do người đặt tổng chốt; chưa suy cách xử lý T nhỏ hơn số đã chọn |
| Giá40.000đ | D-15 | Đã gồmVAT; không suy thuế suất cụ thể |
| Dinh dưỡng | D-17 | Bảng thành phần thực phẩm Việt Nam,4 chỉ số, nhãn ước tính từ định lượng sống; ấn bản/mapping/dung sai còn mở |
| Giá món và loại suất | D-18/D-20 | Nội bộ đặt giá món; DDV tạo loại suất với giá/cơ cấu; không danh sách giá cố định tự suy |
| QR công ty | D-19 | Cơ chế xác minh người ăn; chưa giải quyết đầy đủ định danh guest và chống chọn trùng |
| Định mức công ty | D-21 | Công ty đặt định mức chung; người ăn chọn trong mức, không tự trả chênh |
| VAT/chiết khấu | [Quy tắc kế toán](../../cost/accounting/business-rules.md) | Cost gồmVAT phải trảNCC; cờ hóa đơn riêng; chiết khấu khoản riêng theođơn, không tự giảm phải trả |

Nguồn các D: [kế hoạch tổng thể mục1](../00-ke-hoach-tong-the.md). Các Q trong lịch sử đã được D giải quyết không được coi là câu hỏi mới chỉ vì còn xuất hiện trong phần lịch sử.

## Điểm chưa chốt và nơi quản lý

| Nhóm | Nguồn trạng thái hiện hành |
| :--- | :--- |
| Phạm vi/đội/người duyệt | O-01–06 tại [PRD](../01-prd.md); một phần O-01 đã rõ theo xác nhận kế toán, chưa đóng toàn bộ |
| Quy tắc thực đơn | DL-01,H-1–H-9 và E2-Q tại [bảng quy tắc](quy-tac-thuc-don.md), [SRS MENU](../../thuc-don-dinh-luong/srs/spec.md) |
| Nền tảng/API chung | N-01–04 và [E1-Q01–05](../../nen-tang/review/questions.md) |
| Cost/kế toán | [Sổ review](../../cost/review/decision-register.md), CK-Q01–10, DATA-COST-Q01–06; chưa có10món/10ngày thật |
| Dinh dưỡng/Agent nội bộ | [NUTR-Q và dữ liệu](../../dinh-duong/review/questions.md), [AIO-Q01–06](../../agent-noi-bo/review/questions.md) |
| Chọn món/order | [ORD-Q01–15](../../chon-mon-order/review/questions.md), Q-14/Q-16/O-03/O-06 |

Chưa có chữ ký/chấp thuận baseline sản phẩm. Mỗi quyết định mới cần người xác nhận,ngày,nguồn và ví dụ tác động; không lấy tài liệu được sinh ra làm bằng chứng quyết định.
