# UC-COST-006: Xem và so sánh cost món

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Người nội bộ có quyền đọc cost; Agent Nội bộ theo quyền người dùng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.cost.read; giá chi tiết kiểm thêm cost.price.read.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Món/công thức truy cập được; có cỡ định lượng, ngày tính và cơ sở. Không yêu cầu đủ giá làm tiền điều kiện vì thiếu giá là nhánh cần xử lý.
- **Kích hoạt:** Mở cost món từ danh mục, hộp chọn món hoặc màn duyệt công thức.
- **Hậu điều kiện thành công:** Người dùng thấy kết quả tính hợp lệ hoặc nguyên nhân chưa tính được; không đổi công thức/giá.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-DISH-001`, `FR-COST-DISH-002`, `FR-COST-DISH-003`, `FR-COST-DISH-004`, `FR-COST-DISH-005`, `FR-COST-DISH-008`.
- **Điểm chạm:** SCR-COST-08 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Người dùng chọn món, cỡ, ngày và cơ sở; hệ thống kiểm quyền/phạm vi.
2. Hệ thống lấy công thức hiệu lực và giá tham chiếu cho các nguyên liệu tính vào cost.
3. Hệ thống tính cost và tỷ trọng dòng theo SRS 3.3.1, áp hao hụt đúng một lần nếu cấu hình CO.
4. Hệ thống hiện tổng, định lượng, đơn vị, giá đơn vị dùng, thành tiền, tỷ trọng, NCC và ngày hiệu lực theo quyền.
5. Người dùng đổi ngày/cơ sở để tính lại; kết quả tra cứu không lưu thành bản chụp.

## Luồng nhánh và ngoại lệ

- **2a. Thiếu giá:** ERR-COST-422-03 kèm danh sách thiếu theo quyền; không trả tổng cost không đầy đủ. Món không tồn tại trả ERR-MENU-404-01.
- **1a. Danh mục hoặc hộp chọn món:** Hiển thị cost theo hôm nay hoặc ngày phục vụ của ô; thiếu giá có nhãn; người không có cost.cost.read không nhận trường cost.
- **2b. So sánh hai công thức (P1):** Tính phiên bản hiệu lực và phiên bản đề nghị tại cùng ngày/cơ sở; hiện chênh đồng và %. Nếu một bên thiếu giá thì không suy ra chênh lệch. Mẫu số bằng 0: cách trình bày tỷ lệ chưa chốt, FLOW-COST-Q04.
- **4a. Gợi ý nhóm cost (P1):** Chỉ gợi ý khi ngưỡng nhóm đã chốt; người dùng tự quyết, không tự lưu cost_tier. Chờ E3-Q7 thì hiện chưa cấu hình, vẫn cho xem cost.
- **3a. Cost món bằng 0:** Không chia 0 khi tính tỷ trọng; cách thể hiện tỷ trọng chờ FLOW-COST-Q04, không bịa tỷ lệ.

## Quy tắc và điểm mở

- Quy tắc: BR-CALC-001, BR-CALC-002, BR-CALC-003, BR-CALC-006, BR-SEC-009.
- Điểm mở/giới hạn: O-01, E3-Q2, E3-Q7, FLOW-COST-Q04.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
