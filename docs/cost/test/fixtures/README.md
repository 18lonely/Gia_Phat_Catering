# Bộ số liệu đối soát giả định

Phiên bản 0.1.0 · 11/11/2026 · Draft; O-01 được xác nhận một phần trong phiên, các chi tiết còn lại chờ review.

**Không phải dữ liệu Gia Phát, chưa có kế toán xác nhận.** 10 món minh họa công thức định lượng × đơn giá, chuyển đơn vị và hao hụt; 10 ngày dùng cost món chính đầu vào độc lập để kiểm cách gộp, VAT và làm tròn. Đây không phải 10 thực đơn hoàn chỉnh hay seed database, không kiểm chọn giá theo ngày, chọn công thức, duyệt, RBAC hoặc engine production.

JSON lưu số tiền/định lượng dạng chuỗi decimal; expected được nhập tường minh để so với phép tính. [Script kiểm](../../validation/check-reconciliation.py) dùng Decimal và chỉ kiểm công thức mẫu. Thay bằng dữ liệu thật phải giữ bản nguồn, ghi VAT/cơ sở/ngày/giá và người xác nhận; không sửa file này thành bằng chứng NFR-COST-002 đã đạt.

| Món mẫu | Tên | Cost chính xác kỳ vọng (đ) |
| :--- | :--- | ---: |
| MOCK-DISH-01 | Thịt và trứng mẫu | 10800 |
| MOCK-DISH-02 | Thịt đơn mẫu | 8400 |
| MOCK-DISH-03 | Thịt hao hụt20% mẫu | 10500 |
| MOCK-DISH-04 | Nước không tính cost mẫu | 8400 |
| MOCK-DISH-05 | Phần lẻ ba dòng mẫu | 1.2 |
| MOCK-DISH-06 | Không có thành phần tính cost | 0 |
| MOCK-DISH-07 | Định lượng80g mẫu | 9600 |
| MOCK-DISH-08 | Giá cơ sở B mẫu | 8820 |
| MOCK-DISH-09 | Trứng mẫu | 2400 |
| MOCK-DISH-10 | Hải sản hao hụt20% mẫu | 12500 |

| Ngày mẫu | Cơ sở | Cách tính | Cost suất (đ) | VAT% | Cost% sau làm tròn | Kết quả |
| :--- | :--- | :--- | ---: | ---: | ---: | :--- |
| 2026-11-16 | A | DAT_NHAT | 18800 | 8 | 50.76 | DAT |
| 2026-11-17 | A | DAT_NHAT | 21000 | 8 | 56.70 | KHONG_DAT |
| 2026-11-18 | A | DAT_NHAT | 20000 | 0 | 50.00 | DAT |
| 2026-11-19 | A | DAT_NHAT | 52004 | 0 | 52.00 | DAT |
| 2026-11-20 | A | DAT_NHAT | 52005 | 0 | 52.01 | KHONG_DAT |
| 2026-11-21 | A | DAT_NHAT | 32000 | 0 | 40.00 | DAT |
| 2026-11-22 | A | BINH_QUAN | 28000 | 0 | 35.00 | DAT |
| 2026-11-23 | A | MAC_DINH | 24000 | 0 | 30.00 | DAT |
| 2026-11-24 | A | DAT_NHAT | 0 | 8 | 0.00 | DAT |
| 2026-11-25 | B | DAT_NHAT | 21000 | 8 | 56.70 | KHONG_DAT |

Ngưỡng52% trong fixture; dữ liệu K=2 chỉ kiểm công thức BR-CALC-004, không quyết định mở dự toán K>1 đang chờ E3-Q15. Cost0 không kiểm cách hiển thị tỷ trọng đang chờ Q04. Bộ thực tế cho NFR-COST-002 vẫn chưa có.
