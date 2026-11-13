# UC-COST-010: Kiểm cổng duyệt và chụp cost đã duyệt

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Quy trình duyệt MENU; Dinh dưỡng viên và người duyệt theo quyền MENU.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Fish level.
- **Quyền:** Quyền gửi/duyệt MENU; dữ liệu cost lọc theo cost.cost.read.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Thực đơn đã lưu, đủ điều kiện MENU; người gửi/người duyệt theo O-06 và BR-SEC-008.
- **Kích hoạt:** Gửi duyệt thực đơn hoặc người duyệt cuối hoàn tất duyệt.
- **Hậu điều kiện thành công:** Gửi duyệt hoặc hoàn tất duyệt đúng trạng thái MENU; snapshot chỉ có khi APPROVED và tách theo cơ sở/vòng.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-MEAL-005`, `FR-COST-MEAL-006`.
- **Điểm chạm:** SCR-MENU-10, SCR-MENU-12, SCR-COST-12, xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Ở lệnh gửi duyệt, MENU gọi bộ kiểm Cost cho mọi ngày và cơ sở thuộc thực đơn.
2. Cost chạy UC-COST-009 và kiểm bảng tính hợp lệ cho món đặc thù.
3. Nếu đủ dữ liệu và đáp ứng chế độ kiểm, hệ thống trả kết quả cho MENU để tiếp tục PENDING; chưa ghi snapshot APPROVED.
4. Người duyệt xử lý theo luồng MENU; hệ thống lưu các lượt duyệt riêng biệt.
5. Khi thực đơn chuyển APPROVED ở người duyệt cuối, hệ thống ghi snapshot cost từng ngày/cơ sở/vòng duyệt, giá/định lượng/tham số đã dùng cùng giao dịch chuyển trạng thái.
6. Hệ thống hiển thị kết quả duyệt; các thay đổi giá sau đó đi UC-COST-014, không sửa bản chụp.

## Luồng nhánh và ngoại lệ

- **2a. Thiếu đầu vào:** Thiếu giá: ERR-COST-422-03; VAT: ERR-COST-422-05; thiếu bảng tính đặc thù hợp lệ: ERR-COST-422-04. Không chuyển PENDING, kể cả ở CANH_BAO.
- **2b. Vượt ngưỡng:** CHAN: ERR-COST-422-07 và giữ trạng thái trước gửi; CANH_BAO: cảnh báo rồi tiếp tục bước 3, không coi là ngoại lệ được duyệt. Lỗi trả cho người thiếu quyền không chứa số cost.
- **4a. Người duyệt trả lại:** Theo MENU; chưa ghi snapshot cho vòng chưa APPROVED. Bản chụp vòng duyệt cũ vẫn giữ.
- **5a. Ghi snapshot thất bại:** Rollback chuyển APPROVED và bản chụp cùng giao dịch; lỗi hạ tầng theo ERR-SYS-503-01/ERR-SYS-500-01, không hiển thị đã duyệt.
- **5b. Giá/tham số đổi giữa gửi và duyệt:** Chính sách kiểm lại, dùng giá ngày nào và cách xử lý khi vượt mới chờ FLOW-COST-Q06. Không giả định kết quả lúc gửi vẫn hợp lệ; nhánh này chưa đủ điều kiện nghiệm thu.
- **2c. Xin ngoại lệ vượt ngưỡng:** FR-COST-MEAL-007 chưa triển khai, chờ E3-Q9; không thiết kế nút bỏ qua trong CHAN.

## Quy tắc và điểm mở

- Quy tắc: BR-CALC-007, BR-CALC-009, BR-CALC-010, BR-SEC-008.
- Điểm mở/giới hạn: E3-Q9, E3-Q16, O-06, FLOW-COST-Q06; luồng ngoại lệ không được tính là đã có.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
