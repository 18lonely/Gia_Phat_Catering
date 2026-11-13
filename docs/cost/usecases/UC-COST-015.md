# UC-COST-015: Kiểm ngân sách cho Agent Dinh dưỡng viên

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** svc-agent-dinh-duong-vien.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Fish level.
- **Quyền:** Chỉ quyền gọi FR-COST-RUL-003; không có quyền đọc bảng Cost.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Tài khoản dịch vụ xác thực; có phiên trò chuyện để tính giới hạn; có loại suất, tuần và món theo ngày.
- **Kích hoạt:** Agent gửi một thực đơn cần kiểm ngân sách.
- **Hậu điều kiện thành công:** Agent chỉ có kết quả tổng hợp, không có số liệu hay lý do đủ để truy ngược theo ngày.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-RUL-003`.
- **Điểm chạm:** SVC-COST-01 (không phải màn hình), xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống kiểm định danh dịch vụ và giới hạn 30 lời gọi/phiên.
2. Hệ thống kiểm cấu trúc thực đơn và danh mục hợp lệ.
3. Dịch vụ nội bộ tính ngân sách mọi ngày/cơ sở; agent không truy vấn dữ liệu giá trực tiếp.
4. Hệ thống tổng hợp đúng một trạng thái cho cả thực đơn: DAT, KHONG_DAT hoặc KHONG_XAC_DINH.
5. Hệ thống trả trạng thái, không trả cost, %, ngưỡng, ngày/món vượt; log ứng dụng không ghi con số cost.

## Luồng nhánh và ngoại lệ

- **1a. Vượt giới hạn:** ERR-COST-429-01; agent hướng dẫn gửi thực đơn cho Gia Phát xem, không lặp gọi để dò ngưỡng.
- **2a. Nội dung không hợp lệ:** ERR-MENU-422-14; phản hồi không chứa dữ liệu cost.
- **3a. Thiếu dữ liệu giá:** Trả KHONG_XAC_DINH cho cả thực đơn; không tiết lộ nguyên liệu/ngày gây thiếu.
- **4a. Một ngày vượt và một ngày không tính được:** Thứ tự ưu tiên hai trạng thái chưa được SRS chốt: FLOW-COST-Q09. Không âm thầm chọn DAT; nhánh cần quyết định trước triển khai.
- **1b. Agent gọi API đọc giá/cost hoặc hết quyền:** ERR-AUTH-403-02; không chuyển sang tài khoản Agent Nội bộ. CANH_BAO không biến KHONG_DAT ngân sách thành DAT.

## Quy tắc và điểm mở

- Quy tắc: BR-SEC-010, BR-CALC-011.
- Điểm mở/giới hạn: E9 cần cân nhắc mức hữu ích so với hạn chế dò cost; FLOW-COST-Q09.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
