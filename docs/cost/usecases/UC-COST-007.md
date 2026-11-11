# UC-COST-007: Lập và duyệt bảng tính món đặc thù

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Dinh dưỡng viên (lập); Giám đốc (duyệt).
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.sheet.write; cost.sheet.approve; đọc theo cost.cost.read.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Món có cờ đặc thù; người lập và người duyệt là hai người khác nhau. Tính cost đủ giá trước khi chụp.
- **Kích hoạt:** Dinh dưỡng viên chọn Lập bảng tính trên chi tiết cost món.
- **Hậu điều kiện thành công:** Bảng tính có quyết định và người duyệt; dữ liệu tính đã chụp giữ nguyên, không đồng nghĩa thực đơn đã được duyệt.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-DISH-006`, `FR-COST-DISH-007`.
- **Điểm chạm:** SCR-COST-09, SCR-COST-10 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Dinh dưỡng viên chọn ngày, cơ sở, cỡ; hệ thống thực hiện UC-COST-006.
2. Dinh dưỡng viên kiểm bảng phân rã, nhập ghi chú và gửi duyệt.
3. Hệ thống lưu cost_sheets và các dòng chụp ở PENDING, ghi audit; nội dung chụp không đổi theo giá mới.
4. Giám đốc mở danh sách chờ duyệt, xem dữ liệu chụp, ngày và cơ sở tính.
5. Giám đốc chọn Duyệt; hệ thống kiểm quyền và không tự duyệt, ghi approvals cùng trạng thái APPROVED.
6. Hệ thống hiển thị quyết định; bảng tính được dùng kiểm điều kiện món đặc thù theo quy tắc hiệu lực đã được chốt.

## Luồng nhánh và ngoại lệ

- **1a. Không phải món đặc thù hoặc thiếu giá:** ERR-COST-422-04 hoặc ERR-COST-422-03; chưa tạo bản chụp, quay lại chọn món/giá.
- **5a. Tự duyệt:** ERR-SYS-403-01; giữ PENDING, chuyển người duyệt khác.
- **5b. Trả lại:** Giám đốc nhập lý do ít nhất 10 ký tự; thiếu trả ERR-SYS-422-01. Ghi REJECTED và quyết định; người lập tạo bản mới, không sửa nội dung bản đã gửi.
- **5c. Đã được xử lý trong phiên khác:** Không ghi quyết định trùng; tải lại trạng thái. Hợp đồng phiên bản/lệnh duyệt cần API cụ thể, FLOW-COST-Q02.
- **6a. Bảng cũ hoặc cơ sở khác:** Không tự suy ra hiệu lực dùng chéo cơ sở; E3-Q16 phải được chốt trước nghiệm thu nhánh dùng bảng tính.

## Quy tắc và điểm mở

- Quy tắc: BR-CALC-007, BR-SEC-008, BR-CALC-010.
- Điểm mở/giới hạn: O-06, E3-Q16; mặc định 90 ngày vẫn là đề xuất.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
