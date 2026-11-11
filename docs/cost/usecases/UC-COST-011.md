# UC-COST-011: Đề nghị và duyệt chế độ kiểm cost

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Người có quyền quản lý tham số; Giám đốc duyệt.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** Quyền quản lý/duyệt tham số theo SRS nền tảng; không suy ra từ cost.price.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có tài khoản được cấp quyền tham số; người duyệt khác người đề nghị.
- **Kích hoạt:** Người quản lý tham số mở COST_CHE_DO_KIEM.
- **Hậu điều kiện thành công:** Chế độ mới có phê duyệt/ngày hiệu lực hoặc bị từ chối; giữ lịch sử tham số.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-MEAL-008`.
- **Điểm chạm:** SCR-COST-13 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống hiện giá trị có hiệu lực, ngày hiệu lực và các đề nghị đang chờ.
2. Người đề nghị chọn CANH_BAO hoặc CHAN, ngày hiệu lực và lý do.
3. Hệ thống kiểm dữ liệu và tạo đề nghị PENDING theo FR-SYS-PRM-001.
4. Giám đốc xem đề nghị và duyệt theo FR-SYS-PRM-002; hệ thống kiểm không tự duyệt.
5. Hệ thống ghi phiên bản tham số được duyệt; chỉ áp dụng khi đến ngày hiệu lực.
6. Các lần kiểm dùng tham số hiệu lực theo ngày nghiệp vụ, snapshot cũ không thay đổi.

## Luồng nhánh và ngoại lệ

- **3a. Sai giá trị hoặc ngày quá khứ:** ERR-SYS-422-02; giữ tham số cũ, sửa đề nghị.
- **3b. Thiếu lý do:** ERR-SYS-422-01; quay lại bước 2.
- **4a. Tự duyệt:** ERR-SYS-403-01; cần người khác có thẩm quyền.
- **4b. Từ chối:** Đề nghị REJECTED; giá trị cũ tiếp tục dùng, không tự chuyển sang CHAN.
- **6a. Mặc định và điểm mở:** CANH_BAO chỉ là mặc định đề xuất; không dùng luồng này để tự quyết VAT hay hợp thức hoá ngoại lệ E3-Q9.

## Quy tắc và điểm mở

- Quy tắc: BR-SYS-001, BR-SYS-002, BR-SEC-008, BR-CALC-010.
- Điểm mở/giới hạn: O-06; người được đề nghị tham số theo ma trận nền tảng, không tạo vai trò mới.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
