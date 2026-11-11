# UC-COST-013: Xem lịch sử và xuất bảng dự toán

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Người nội bộ có quyền; Bếp trưởng chỉ xem lượng cơ sở mình.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.estimate.read hoặc cost.estimate.qty; kiểm lại quyền khi xuất.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có bảng dự toán đã lưu thuộc phạm vi được xem.
- **Kích hoạt:** Người dùng mở lịch sử dự toán hoặc chọn xuất tệp.
- **Hậu điều kiện thành công:** Người dùng xem/xuất đúng phiên bản và đúng mức quyền; không thay đổi số liệu lịch sử.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-EST-004`, `FR-COST-EST-005`, `FR-COST-EST-006`, `FR-COST-EST-007`.
- **Điểm chạm:** SCR-COST-15 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Người dùng chọn ngày/cơ sở và phiên bản; hệ thống kiểm quyền và phạm vi.
2. Hệ thống tải bản chụp đã lưu, thời điểm/người lập và số suất theo món.
3. Người có quyền đọc đầy đủ thấy giá, chi phí và cost %; người chỉ có quyền số lượng nhận bảng không chứa các trường tiền/cost.
4. Người dùng chọn XLSX hoặc PDF (P1); hệ thống kiểm lại quyền rồi tạo tệp theo cùng mức dữ liệu được phép.
5. Người dùng nhận tệp của phiên bản đã chọn; xuất không tạo bản dự toán mới.

## Luồng nhánh và ngoại lệ

- **1a. Không tồn tại hoặc ngoài cơ sở:** ERR-SYS-404-01; không lộ tên hoặc giá bản ghi ngoài phạm vi.
- **3a. Chỉ có quyền số lượng:** Loại giá đơn vị, thành tiền, tổng chi phí, doanh thu và cost % khỏi payload/tệp; không chỉ ẩn cột. Vẫn xem nguyên liệu, định lượng, lượng mua, số suất.
- **4a. Quyền bị thu hồi trước khi tải:** ERR-AUTH-403-02 hoặc ERR-SYS-404-01 theo nguyên nhân; không trả tệp đã tạo dưới quyền cao hơn.
- **4b. Xuất thất bại:** Không báo tải xong; giữ phiên bản đang xem. ERR-SYS-500-01/ERR-SYS-503-01 cho lỗi tương ứng; cho thử xuất lại, không tính lại cost.

## Quy tắc và điểm mở

- Quy tắc: BR-EST-004, BR-CALC-010, BR-SEC-007, BR-SEC-010.
- Điểm mở/giới hạn: E3-Q11; quyền Bếp trưởng hiện là đề xuất chỉ lượng.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
