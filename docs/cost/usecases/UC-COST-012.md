# UC-COST-012: Lập và lập lại bảng dự toán

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Dinh dưỡng viên hoặc kế toán mua hàng.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.estimate.write; cost.estimate.read.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có thực đơn đã lưu (trạng thái bất kỳ), ngày/cơ sở; trước R6 nhập số suất dự kiến bằng tay.
- **Kích hoạt:** Người dùng chọn Lập dự toán ngày hoặc tuần.
- **Hậu điều kiện thành công:** Mỗi ngày lưu thành công có bản bất biến và lịch sử; kết quả gộp tuần có truy vết về đúng các phiên bản ngày.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-EST-001`, `FR-COST-EST-002`, `FR-COST-EST-003`, `FR-COST-EST-004`, `FR-COST-EST-006`.
- **Điểm chạm:** SCR-COST-14, SCR-COST-15 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Người dùng chọn thực đơn, ngày/tuần và một cơ sở; hệ thống tải món/công thức liên quan.
2. Người dùng nhập số suất từng món chính; hệ thống tính tổng lượt chọn/main_pick và số suất món phụ, rau, canh.
3. Hệ thống kiểm số nguyên không âm, tổng >0; tra giá và tham số, tính lượng mua/chi phí theo SRS 3.3.4.
4. Hệ thống gộp nguyên liệu theo ngày/cơ sở, giữ phân rã theo món, áp hao hụt một lần, làm tròn lượng mua sau gộp.
5. Hệ thống lưu bản dự toán mới có version_no, số suất theo món, dòng nguyên liệu, khoản khoán và đầu vào chụp trong cùng giao dịch cho một ngày.
6. Hệ thống hiện đủ cột dự toán, tổng chi phí, doanh thu chưa VAT; phân biệt cost % theo số suất với cost % theo cách kiểm thực đơn.
7. Nếu lập tuần, hệ thống trình bày các ngày và bảng gộp tuần theo đúng batch/cơ sở, giữ giá từng ngày.

## Luồng nhánh và ngoại lệ

- **3a. Số suất không hợp lệ:** ERR-COST-422-08; không lưu bản ngày. Trường hợp main_pick>1 mà tổng không chia hết: chờ E3-Q15, mô hình đề xuất không nhận phân số suất.
- **3b. Thiếu giá/VAT:** ERR-COST-422-03 hoặc ERR-COST-422-05; không ghi tổng bị thiếu. Nguyên liệu ngoài cost vẫn giữ lượng, không tự lấy giá 0 cho nguyên liệu trong cost.
- **5a. Lập lại:** Tạo version_no mới, giữ nguyên bản cũ. Khi hai người lập cùng lúc, cấp số dưới giao dịch theo ERD; không ghi đè.
- **7a. Một ngày trong tuần lỗi:** Chưa chốt lưu toàn tuần nguyên tử hay cho lưu từng ngày hợp lệ: FLOW-COST-Q07. Hiển thị ngày lỗi; không báo cả tuần đã xong hoặc tự chọn hành vi lưu một phần.
- **6a. Cost % dự toán khác màn soạn:** Giải thích hai phương pháp tính, không sửa số để làm chúng bằng nhau; số suất nhập tay vẫn là dự kiến.

## Quy tắc và điểm mở

- Quy tắc: BR-EST-001, BR-EST-002, BR-EST-003, BR-EST-004, BR-CALC-010.
- Điểm mở/giới hạn: E3-Q8, E3-Q15, O-01, FLOW-COST-Q07.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
