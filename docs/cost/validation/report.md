# Kiểm tra đợt đồng bộ Cost

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: kiểm tra thiết kế/wireframe đạt, chưa nghiệm thu sản phẩm.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Ghi kết quả kiểm tra sau đồng bộ 9 mục của SRS Cost 4.3 |

## Kết quả

| Kiểm tra | Kết quả |
| :--- | :--- |
| Parse DBML, xuất DDL MySQL bằng `@dbml/core` 12.0.0 | Đạt; 57 bảng, không lỗi parser; chưa thực thi DDL |
| Miền Cost | 15 bảng, gồm 11 bảng mới; mỗi bảng có từ điển dữ liệu ở ERD 5.4 |
| Bỏ cost đơn ở `menu_days` | Đạt; thay bằng snapshot ngày/cơ sở/vòng duyệt |
| 6 tham số mới trong SRS nền tảng | Đạt, mỗi mã xuất hiện đúng một dòng danh mục; BR-SYS-002 dùng cờ cần duyệt |
| Liên kết tương đối trong ERD, SRS nền tảng, SRS Cost và epic Cost | Đạt |
| Wireframe trên Chrome headless, desktop 1440×1080 | Có 6 ô cost; có trạng thái đạt/vượt; đổi cơ sở đổi số; đổi món cập nhật; chưa đủ món không kết luận đạt |
| Chế độ cảnh báo/chặn | Vượt ngân sách là SOFT/0 điểm ở CANH_BAO, HARD ở CHAN; các lỗi nghiệp vụ khác vẫn giữ nguyên |
| Quyền xem cost | Không hiển thị % ở dòng cost khi chuyển quyền mô phỏng; bảng kiểm cost không đưa số nhạy cảm vào detail |
| Thiếu giá/VAT | Hiện đúng trạng thái, bộ kiểm trả lỗi HARD |
| Mobile 390×844 | Một ngày được hiển thị; chuyển tab đúng ngày; không tràn ngang viewport |
| Trạng thái rỗng và JavaScript | Hiển thị chưa xếp món; không có lỗi JavaScript |
| Xem ảnh chụp desktop/mobile | Đã kiểm tra bố cục; sửa grid min-width gây tràn ngang trên mobile |

## Cách chạy lại

[Script kiểm tra](check.cjs) dùng Node.js, `@dbml/core` và `playwright`, Chrome cài sẵn. Cài thư viện vào thư mục kiểm tra riêng; không cần thêm dependency vào dự án sản phẩm:

```powershell
$costCheckDir = Join-Path $env:TEMP 'gia-phat-cost-validation'
npm.cmd install --prefix $costCheckDir --no-audit --no-fund @dbml/core@12.0.0 playwright
node D:/BA/docs/cost/validation/check.cjs $costCheckDir
```

Ảnh chụp được lưu tại thư mục kiểm tra tạm. Script kiểm tra thiết kế và tương tác wireframe; không thay thế test nghiệp vụ Cost của sản phẩm.

## Giới hạn còn lại

- DBML không tự thực thi các CHECK, unique có điều kiện, generated key, khoá giao dịch và quy tắc liên bảng mô tả ở ERD 5.4. Chưa có migration production.
- Wireframe dùng số cost giả lập độc lập với giá bán và VAT mẫu 8%; không có dữ liệu thật, engine tính cost, API hay phân quyền phía server. Bộ chuyển quyền chỉ minh hoạ hiển thị.
- Còn các quyết định nghiệp vụ mở, bao gồm E3-Q14 (cờ giá tham chiếu đã hiệu lực), E3-Q15 (số suất khi chọn nhiều món chính), E3-Q16 (hiệu lực/cơ sở của bảng tính đặc thù).
- Hoàn thành 9/9 mục đồng bộ tài liệu không có nghĩa toàn epic Cost hoặc MVP đã hoàn thành.
