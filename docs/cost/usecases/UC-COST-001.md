# UC-COST-001: Quản lý nhà cung cấp

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.supplier.read; cost.supplier.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Tài khoản nội bộ có quyền tương ứng; thao tác ghi chỉ dành cho kế toán mua hàng.
- **Kích hoạt:** Kế toán mở danh sách nhà cung cấp và chọn thêm mới.
- **Hậu điều kiện thành công:** Nhà cung cấp được tạo/sửa/ngừng đúng yêu cầu; giá lịch sử không thay đổi.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-SUP-001`, `FR-COST-SUP-002`, `FR-COST-SUP-003`.
- **Điểm chạm:** SCR-COST-01, SCR-COST-02 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống hiển thị danh sách, bộ lọc tên, loại và trạng thái.
2. Kế toán nhập tên, loại thường xuyên/tiểu thương, điện thoại và ghi chú rồi chọn Lưu.
3. Hệ thống chuẩn hoá tên và kiểm trùng theo BR-PRC-001.
4. Hệ thống cấp mã, tạo nhà cung cấp ACTIVE và ghi nhật ký trong cùng giao dịch.
5. Hệ thống mở chi tiết bản ghi vừa tạo; danh sách phản ánh kết quả.

## Luồng nhánh và ngoại lệ

- **3a. Tên trùng:** Trả ERR-COST-409-01; giữ dữ liệu nhập, quay lại bước 2.
- **2a. Sửa thông tin:** Mở bản ghi đã có, sửa rồi kiểm như bước 3; phiên bản cũ trả ERR-SYS-409-02, tải lại trước sửa tiếp.
- **2b. Ngừng nhà cung cấp:** Kế toán nhập lý do, xác nhận; chuyển INACTIVE, ghi audit. Giá cũ giữ nguyên và vẫn dùng được; nếu đang có giá tham chiếu thì sinh cảnh báo. Không huỷ giá để ngừng nhà cung cấp.
- **1a. Chỉ có quyền đọc hoặc không có kết quả lọc:** Cho xem/lọc, ẩn thao tác ghi; danh sách rỗng có hướng dẫn xoá bộ lọc. Gọi API ghi thiếu quyền trả ERR-AUTH-403-02.

## Quy tắc và điểm mở

- Quy tắc: BR-PRC-001, BR-PRC-007, BR-AUD-001.
- Điểm mở/giới hạn: Không bổ sung luồng mua hàng/công nợ R11.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
