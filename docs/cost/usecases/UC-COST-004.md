# UC-COST-004: Nhập giá từ bảng tính

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.price.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Được phép nhập giá; dùng khung nhập MENU, không dùng upload chứng từ để đọc XLSX.
- **Kích hoạt:** Kế toán chọn Nhập bảng tính từ bảng giá.
- **Hậu điều kiện thành công:** Có kết quả nhập có thể đối chiếu với giá thực lưu; giá cũ không bị ghi đè.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-PRC-005`.
- **Điểm chạm:** SCR-COST-05, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống cung cấp mẫu nhập giá và hướng dẫn cột theo FR-MENU-IMP-001.
2. Kế toán chọn tệp XLSX; hệ thống đọc và kiểm theo khung FR-MENU-IMP-002, BR-CAT-023.
3. Hệ thống hiển thị dữ liệu xem trước và lỗi từng dòng/ô; kiểm nguyên liệu, NCC, phạm vi, giá, ngày, trùng và tham chiếu.
4. Khi dữ liệu hợp lệ, kế toán xác nhận nhập theo khung FR-MENU-IMP-003; các giá lệch bất thường cần xác nhận như UC-COST-002.
5. Hệ thống ghi toàn bộ trong một giao dịch (tất cả hoặc không gì cả) và trả số dòng đã tạo cùng thông tin truy vết nhập. Chỉ kế thừa cơ chế nhập E2; không kế thừa trạng thái PENDING của giá bán, vì giá nhập Cost không có bước duyệt.
6. Kế toán về bảng giá để xem các dòng vừa nhập.

## Luồng nhánh và ngoại lệ

- **2a. Tệp sai hoặc dữ liệu không hợp lệ:** ERR-MENU-422-20; hiện báo cáo dòng/ô, không thông báo thành công. Sửa file và kiểm lại.
- **3a. Giá trùng/nguồn đã ngừng:** Đưa lỗi miền Cost vào báo cáo nhập, không tự sửa ngày hoặc chọn NCC khác. Kiểm lại trạng thái trước commit.
- **4a. Người dùng huỷ:** Không ghi giá. Bản xem trước không phải giá có hiệu lực.
- **5a. Mất phản hồi khi nhập:** Không tự chạy lại lô; tải kết quả/lịch sử trước xác nhận gửi lại. Hợp đồng chống gửi trùng cần đặc tả ở API, FLOW-COST-Q02.

## Quy tắc và điểm mở

- Quy tắc: BR-CAT-023, BR-PRC-002, BR-PRC-003, BR-PRC-004, BR-PRC-005.
- Điểm mở/giới hạn: Kế thừa giới hạn tối đa 2.000 dòng/tệp và cơ chế giao dịch của khung E2; không tự đặt giới hạn XLSX mới. FLOW-COST-Q02.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
