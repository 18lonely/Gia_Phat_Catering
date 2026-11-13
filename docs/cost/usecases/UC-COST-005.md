# UC-COST-005: Theo dõi lịch sử, giá thiếu và giá cũ

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng; bộ lập lịch (nhánh tự động).
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.price.read; ghi bổ sung cần cost.price.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có công thức ACTIVE để xác định nguyên liệu cần theo dõi; lịch chạy hàng ngày được cấu hình.
- **Kích hoạt:** Kế toán mở Theo dõi giá hoặc bộ lập lịch đến kỳ.
- **Hậu điều kiện thành công:** Người dùng xác định được nguồn giá và các món bị ảnh hưởng; cảnh báo tác vụ không bị nhân đôi.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-PRC-006`, `FR-COST-PRC-008`, `FR-COST-PRC-009`.
- **Điểm chạm:** SCR-COST-06, SCR-COST-07, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Người dùng chọn cơ sở và bộ lọc chưa có giá/giá cũ/lịch sử nguyên liệu.
2. Hệ thống tra giá tham chiếu hôm nay theo từng cơ sở và công thức ACTIVE.
3. Hệ thống liệt kê nguyên liệu thiếu giá cùng số món bị ảnh hưởng; giá cũ kèm ngày hiệu lực và tuổi giá.
4. Người dùng mở một nguyên liệu; hệ thống hiện lịch sử theo NCC/ngày/cơ sở, cờ tham chiếu và dòng áp dụng hôm nay.
5. Nếu có quyền ghi, người dùng mở UC-COST-002 hoặc UC-COST-003 để bổ sung giá rồi làm mới danh sách.

## Luồng nhánh và ngoại lệ

- **2a. Tác vụ hàng ngày:** Tính tuổi giá theo loại bảo quản; chỉ sinh một cảnh báo đang mở/nguyên liệu cho KT_MUA_HANG. Chi tiết cơ sở không làm tăng đầu mục trùng.
- **3a. Không có nguyên liệu bị ảnh hưởng:** Hiện danh sách rỗng có giải thích, không tạo cảnh báo giả.
- **2b. Không có giá riêng cơ sở:** Dùng giá chung nếu có; không có cả hai thì thiếu giá, không coi là giá cũ hoặc cost 0.
- **5a. Chỉ có quyền đọc:** Giữ chức năng xem; không cho ghi giá. Cơ chế tự đóng cảnh báo giá cũ sau cập nhật chưa có trong SRS: FLOW-COST-Q03.

## Quy tắc và điểm mở

- Quy tắc: BR-PRC-006, BR-PRC-008, BR-COST-005.
- Điểm mở/giới hạn: E3-Q5, FLOW-COST-Q03; thời điểm chạy hàng ngày chờ vận hành cấu hình.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
