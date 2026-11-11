# UC-COST-014: Tính lại và xử lý cảnh báo vượt cost

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Tác vụ nền (khởi tạo); Dinh dưỡng viên/Giám đốc/Kế toán mua hàng (xử lý).
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** Worker theo tài khoản dịch vụ; người xử lý có cost.alert.read.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có giá tham chiếu mới/đến hiệu lực; thực đơn APPROVED hoặc PUBLISHED có dùng nguyên liệu bị ảnh hưởng.
- **Kích hoạt:** Sự kiện giá tham chiếu hoặc người dùng mở danh sách cảnh báo.
- **Hậu điều kiện thành công:** Có kết quả tính lại độc lập và vòng đời cảnh báo có truy vết; bản duyệt ban đầu không đổi.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-ALR-001`, `FR-COST-ALR-002`, `FR-COST-ALR-003`.
- **Điểm chạm:** SCR-COST-16, SCR-COST-17 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Tác vụ lấy các ngày phục vụ từ hôm nay trở đi thuộc các thực đơn bị ảnh hưởng, theo cơ sở và vòng duyệt hiện hành.
2. Hệ thống tính lại và lưu cost_recalculations riêng; không cập nhật snapshot lúc duyệt.
3. Khi ngày chuyển từ đạt sang vượt, hệ thống mở/cập nhật một cảnh báo/ngày, có chi tiết các cơ sở và nguyên liệu/giá gây thay đổi.
4. Hệ thống gửi thông báo nội bộ cho Dinh dưỡng viên và Giám đốc; mục tiêu hoàn tất tính lại ≤5 phút theo NFR-COST-004.
5. Người có cost.alert.read mở cảnh báo, xem cost lúc duyệt và hiện tại, cơ sở bị ảnh hưởng.
6. Người có quyền MENU thu hồi/sửa thực đơn theo MENU, hoặc người xử lý đóng tay kèm lý do; hệ thống ghi trạng thái và audit.

## Luồng nhánh và ngoại lệ

- **2a. Retry hoặc kết quả trả đảo thứ tự:** Dùng khoá sự kiện theo ERD chống trùng; không để tác vụ cũ ghi đè liên kết kết quả mới.
- **2b. Không tính được:** Lưu KHONG_XAC_DINH và dữ liệu thiếu; không gán 0 hoặc tự đóng cảnh báo đang mở. Mã vận hành lỗi kỹ thuật theo nền tảng; cách thông báo thiếu dữ liệu cần API/worker đặc tả.
- **3a. Đã có cảnh báo mở hoặc cả hai cơ sở cùng vượt:** Cập nhật cùng đầu mục ngày và chi tiết cơ sở; không nhân đôi cảnh báo.
- **3b. Bản duyệt ban đầu đã vượt do CANH_BAO:** Không tự coi là chuyển từ đạt sang vượt; điều kiện phát cảnh báo tiếp theo chờ FLOW-COST-Q08.
- **6a. Giá phục hồi:** Đóng tự động chỉ khi tất cả cơ sở liên quan tính được và đạt. Giữ lịch sử snapshot/tính lại.
- **6b. Đóng tay thiếu lý do:** ERR-SYS-422-01; giữ OPEN. Đóng cảnh báo không thay đổi kết quả ngân sách và không cấp quyền chuyển bếp.
- **6c. Yêu cầu chặn chuyển bếp:** FR-COST-ALR-004 chờ E3-Q10, chưa hiện thực R3; không thêm bước này vào luồng thành công.

## Quy tắc và điểm mở

- Quy tắc: BR-COST-011, BR-CALC-010, BR-AUD-001.
- Điểm mở/giới hạn: E3-Q10, FLOW-COST-Q08; không gửi con số cost qua cổng khách.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
