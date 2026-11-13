# UC-COST-003: Nhập đồng thời nhiều giá trên lưới

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.price.read; cost.price.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Danh mục nguyên liệu còn dùng; có quyền ghi giá.
- **Kích hoạt:** Kế toán mở lưới giá và chọn phạm vi/cơ sở.
- **Hậu điều kiện thành công:** Toàn bộ thay đổi được lưu hoặc toàn bộ không được lưu; không có lô nhập nửa chừng.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-PRC-004`.
- **Điểm chạm:** SCR-COST-03, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống cho lọc nhóm, bảo quản và nguyên liệu đang dùng trong công thức ACTIVE.
2. Hệ thống tải giá tham chiếu hiện tại, đơn vị mua; kế toán nhập giá mới và ngày hiệu lực ở nhiều dòng.
3. Kế toán chọn Lưu; hệ thống bỏ qua dòng không đổi và kiểm từng dòng bằng quy tắc của UC-COST-002.
4. Hệ thống tập hợp các giá lệch bất thường để kế toán xác nhận trước ghi.
5. Hệ thống ghi toàn bộ dòng hợp lệ cùng audit trong một giao dịch hoặc không ghi dòng nào.
6. Hệ thống báo số dòng tạo mới, làm mới lưới; phát sự kiện giá theo UC-COST-014.

## Luồng nhánh và ngoại lệ

- **3a. Một dòng lỗi:** Trả lỗi theo dòng/ô: ERR-COST-422-01, ERR-COST-422-02, ERR-COST-409-02 hoặc ERR-COST-404-01. Không lưu dòng nào; giữ dữ liệu lưới để sửa.
- **3b. Không có dòng thay đổi:** Báo không có thay đổi; không tạo phiên bản giá mới.
- **4a. Không xác nhận giá lệch:** Không ghi cả lô; quay về lưới để sửa hoặc xác nhận lại.
- **5a. Giá bị nhập trùng trong lúc đang sửa:** Kiểm lại ở giao dịch ghi; trả ERR-COST-409-02 cho dòng liên quan, rollback cả lô. Mất phản hồi: đối soát lịch sử trước gửi lại theo quy ước chung.

## Quy tắc và điểm mở

- Quy tắc: BR-PRC-002, BR-PRC-005, BR-PRC-009.
- Điểm mở/giới hạn: Ngưỡng cảnh báo giá là đề xuất; không thay bằng bước phê duyệt.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
