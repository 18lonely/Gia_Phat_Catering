# Wireframe Cost — hướng dẫn review

Phiên bản 0.1.0 · 11/11/2026 · Draft.

Mở [cost-workbench.html](cost-workbench.html) bằng trình duyệt. Chọn vai trò, cơ sở và trạng thái ở thanh trên; dùng menu 01–18 để chuyển màn. Mỗi màn tương ứng SCR-COST-01–18 trong [user flow](../ui/user-flow.md). Có thể mở thẳng bằng `#screen-14`, ví dụ màn lập dự toán.

## Các luồng có thể thử

- Kế toán: tạo NCC, nhập giá và xác nhận biến động lớn, nhập lưới, xem kiểm tra nhập mẫu, đề nghị khoản khoán, lập dự toán.
- Dinh dưỡng viên: lập bảng tính đặc thù; chuyển Giám đốc để duyệt hoặc trả lại có lý do.
- Quản trị tham số: đề nghị chế độ kiểm; chuyển Giám đốc duyệt. Ngày tương lai chưa đổi chế độ hiện tại.
- Bếp trưởng: chỉ xem số lượng dự toán của cơ sở đã chọn; bản xem trước xuất cũng không có tiền.
- Quản lý cơ sở: kiểm phạm vi cơ sở ở dự toán và bảng tính.
- Trạng thái: tải, rỗng, lỗi, mất mạng. Mất mạng chặn ghi trong mẫu.

## Giới hạn

Toàn bộ tên, giá, công thức, VAT, kết quả tính và người dùng đều giả lập. Dữ liệu nằm trong bộ nhớ, tải lại trang sẽ mất. Bộ chọn vai trò phục vụ review, không phải cơ chế bảo mật. Giá nguyên liệu trong bảng phân rã chỉ minh họa một phần chi phí; dòng chi phí khác giúp đối soát với tổng mẫu, không thay engine cost.

Nhập XLSX chỉ mô phỏng các kịch bản hợp lệ/lỗi; không phân tích file thật. Xuất XLSX/PDF chỉ xem trước, không tạo tệp. Chứng từ chỉ kiểm tên file/kích thước trên trình duyệt, không upload. Không gọi API, không có máy chủ, retry/idempotency hay lưu trữ thực. Chế độ tương lai không có bộ lập lịch.

Q01/Q03/Q05/Q06/Q07/Q09/Q10 và các điểm mở SRS vẫn cần review. Nhánh tuần và các thao tác thiếu quyết định được khóa/ghi chú; mô phỏng P2 không thay đổi giá thật.

[Hợp đồng API](../api/api-spec.md) · [Báo cáo kiểm tra](../validation/api-wireframe-report.md).

Bổ sung11/11/2026: mẫu18 màn chưa thể hiện giá báo/giá cost gồm VAT, context hóa đơn khách hoặc khoản chiết khấu theo đơn. Đọc [CR kế toán](../cr/CR-COST-2026-001.md) trước khi dùng mẫu làm yêu cầu triển khai.

## Bổ sung4 màn kế toán

[accounting-workbench.html](accounting-workbench.html) gồm SCR-ACC-01 chuẩn hóa giá,02 context/thỏa thuận nháp,03 khoản riêng,04 lịch sử và đơn đổi. Kết nối từ18 màn Cost. Bộ chọn quyền chỉ minh họa, chưa cấp quyền thật. Mẫu hỗ trợ gross/fixed; NET chưa chốt làm tròn nên hiển thị chưa xác định. Không thay thế import XLSX, activation hợp đồng, duyệt hay thanh toán. [Backlog](../userstories/accounting-backlog.md) và [API](../api/accounting-contract.md) là nguồn phạm vi.
