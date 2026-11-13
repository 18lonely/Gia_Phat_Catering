# UC-COST-016: Xem trước tác động của giá giả định

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Người nội bộ được phép xem cost, vai trò cụ thể chờ chốt.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** Đề xuất cần cost.price.read và cost.cost.read; chưa được coi là quyền đã cấp.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** P2, chưa phải phạm vi bắt buộc của R3; cần chốt quyền trước triển khai.
- **Kích hoạt:** Người dùng chọn Xem trước tác động của giá.
- **Hậu điều kiện thành công:** Có kết quả giả định hoặc lý do chưa tính được; dữ liệu nghiệp vụ không thay đổi.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-ALR-005`.
- **Điểm chạm:** SCR-COST-18, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Người dùng chọn nguyên liệu, cơ sở và giá giả định.
2. Hệ thống kiểm đầu vào và phạm vi theo quyền đã được duyệt.
3. Hệ thống mô phỏng cost các ngày thực đơn liên quan bằng giá giả định, tách khỏi bảng giá thật.
4. Hệ thống trả danh sách ngày sẽ vượt ngưỡng theo quyền, gắn nhãn mô phỏng.
5. Người dùng đóng kết quả; không lưu giá, snapshot, dự toán hay cảnh báo nghiệp vụ.

## Luồng nhánh và ngoại lệ

- **2a. Giá không hợp lệ hoặc nguyên liệu không tồn tại:** ERR-COST-422-01 hoặc ERR-COST-404-01; sửa đầu vào.
- **3a. Thiếu giá khác:** Không khẳng định ngày đó đạt; hiển thị chưa tính được cho người có quyền. Phạm vi ngày/trạng thái cần mô phỏng chờ FLOW-COST-Q10.
- **4a. Không có ngày vượt:** Hiện không có ngày vượt trong phạm vi mô phỏng, không tuyên bố mọi thực đơn của hệ thống đều đạt.
- **5a. Muốn áp dụng giá:** Quay sang UC-COST-002 nhập và xác nhận độc lập; kết quả mô phỏng không có nút tự áp dụng chưa được SRS quy định.

## Quy tắc và điểm mở

- Quy tắc: BR-PRC-002, BR-CALC-003.
- Điểm mở/giới hạn: FLOW-COST-Q10: quyền, phạm vi ngày và trạng thái mô phỏng; giữ P2.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
