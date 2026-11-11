# UC-COST-002: Nhập và quản lý giá tham chiếu

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Kế toán mua hàng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.price.read; cost.price.write.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Nguyên liệu và nhà cung cấp còn dùng; ngày nghiệp vụ theo giờ Việt Nam.
- **Kích hoạt:** Kế toán chọn Nhập giá từ bảng giá hoặc nguyên liệu thiếu giá.
- **Hậu điều kiện thành công:** Dòng giá mới và lịch sử/audit tồn tại; việc tính lại không sửa snapshot đã duyệt.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-PRC-001`, `FR-COST-PRC-002`, `FR-COST-PRC-003`, `FR-COST-PRC-007`, `FR-COST-PRC-010`, `FR-COST-PRC-011`.
- **Điểm chạm:** SCR-COST-03, SCR-COST-04 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống hiển thị nguyên liệu, đơn vị mua và giá tham chiếu trước đó tại phạm vi được chọn.
2. Kế toán chọn nhà cung cấp, cơ sở hoặc cả hai, giá nguyên đồng, ngày hiệu lực; chọn tham chiếu và chứng từ nếu có.
3. Hệ thống kiểm giá, ngày, nguồn tham chiếu, trùng khoá và nhà cung cấp còn ACTIVE.
4. Nếu chênh lệch vượt ngưỡng cấu hình, hệ thống đưa giá cũ/mới và tỷ lệ; kế toán xác nhận tiếp tục.
5. Hệ thống ghi giá mới, lựa chọn tham chiếu hợp lệ, liên kết chứng từ và audit trong một giao dịch; không sửa tiền của dòng cũ.
6. Hệ thống trả dòng đã lưu. Khi tra giá ngày D: chọn giá riêng cơ sở mới nhất không sau D; chỉ khi không có giá riêng mới dùng giá chung.
7. Nếu giá tham chiếu có hiệu lực, hệ thống phát sự kiện tính lại; giá tương lai được xử lý khi đến ngày hiệu lực.

## Luồng nhánh và ngoại lệ

- **3a. Giá hoặc ngày không hợp lệ:** Giá ≤ 0/không nguyên: ERR-COST-422-01; ngày quá khoảng hồi tố hoặc tương lai, NCC ngừng: ERR-COST-422-02; tham chiếu không tồn tại/ngừng: ERR-COST-404-01. Quay lại bước 2.
- **3b. Trùng giá:** ERR-COST-409-02; không tạo dòng, mở lịch sử để đối chiếu; phạm vi cả hai cơ sở cũng phải chống trùng.
- **4a. Không có giá trước hoặc lệch trong ngưỡng:** Bỏ qua xác nhận bất thường; bước 5. Nếu người dùng từ chối xác nhận thì không ghi giá.
- **2a. Chứng từ sai:** ERR-SYS-413-01 nếu >10 MB; ERR-SYS-415-01 nếu không phải ảnh/PDF hỗ trợ. Chọn lại hoặc bỏ tệp tuỳ chọn. Tệp bảng tính nhập giá thuộc UC-COST-004.
- **6a. Không có giá tại ngày/phạm vi:** Trả ERR-COST-404-02, không lấy giá tương lai hoặc giá của cơ sở khác.
- **2b. Đổi tham chiếu của giá chưa hiệu lực:** Chọn dòng mới trong cùng nguyên liệu/phạm vi/ngày; giao dịch bỏ cờ cũ và đặt cờ mới, giữ một tham chiếu. Giá đã hiệu lực: nhánh chưa chốt E3-Q14, không tự mở quyền thay hồi tố.
- **2c. Huỷ giá tương lai:** Nhập lý do và xác nhận; chỉ huỷ khi ngày hiệu lực > hôm nay. Giá đã hiệu lực trả ERR-COST-409-03. Nếu đây là giá tham chiếu và còn báo giá khác cùng ngày: cách chọn giá thay thế chờ FLOW-COST-Q01, không âm thầm chọn NCC.

## Quy tắc và điểm mở

- Quy tắc: BR-PRC-002, BR-PRC-003, BR-PRC-004, BR-PRC-005, BR-PRC-006, BR-PRC-009.
- Điểm mở/giới hạn: E3-Q4, E3-Q6, E3-Q13, E3-Q14; FLOW-COST-Q01. Chưa có bước duyệt giá nhập.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
