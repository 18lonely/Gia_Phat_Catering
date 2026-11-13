# UC-COST-008: Đề nghị và duyệt khoản khoán

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng (đề nghị); Giám đốc (duyệt).
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.allowance.write; cost.allowance.approve.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có người đề nghị và người duyệt độc lập; danh sách khoản thực tế chờ O-01.
- **Kích hoạt:** Kế toán chọn thêm khoản hoặc đề nghị thay đổi khoản hiện hành.
- **Hậu điều kiện thành công:** Có khoản được duyệt để tính tương lai hoặc quyết định trả lại; không tính đồng thời khoản chung và riêng cùng tên.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-MEAL-004`.
- **Điểm chạm:** SCR-COST-11, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Kế toán nhập tên, số tiền nguyên đồng/suất, loại suất hoặc mọi loại suất, ngày hiệu lực và lý do.
2. Hệ thống kiểm dữ liệu; lưu cost_allowances PENDING, không thay khoản đang hiệu lực.
3. Giám đốc mở đề nghị, so sánh giá trị/phạm vi và ngày hiệu lực.
4. Giám đốc duyệt; hệ thống kiểm tách người lập/duyệt rồi ghi APPROVED, approvals và audit.
5. Tại ngày tính, hệ thống lấy bản được duyệt có hiệu lực; khoản riêng loại suất thắng khoản chung cùng tên.
6. Các lần tính mới dùng khoản mới; snapshot/dự toán cũ giữ nguyên.

## Luồng nhánh và ngoại lệ

- **2a. Tiền âm/không nguyên hoặc thiếu ngày:** ERR-COST-422-06; giữ form, quay lại bước 1.
- **2b. Thiếu lý do:** ERR-SYS-422-01; nhập đủ lý do, không tạo đề nghị chưa hợp lệ.
- **4a. Tự duyệt:** ERR-SYS-403-01; không áp dụng khoản.
- **4b. Trả lại:** Ghi REJECTED và lý do; khoản cũ tiếp tục áp dụng. Lập đề nghị mới để sửa.
- **4c. Trùng tên chuẩn hoá/phạm vi/ngày với bản đã duyệt:** Không tạo hai khoản hiệu lực trùng; kiểm theo ERD 5.4. Mã lỗi chuyên biệt và cách chọn đề nghị chờ API, không mượn lỗi giá nhập.

## Quy tắc và điểm mở

- Quy tắc: BR-CALC-008, BR-CALC-010, BR-SEC-008, BR-AUD-001.
- Điểm mở/giới hạn: O-01; quy tắc đọc danh sách khoản khoán theo vai trò cần làm rõ trong API (FLOW-COST-Q05).

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
