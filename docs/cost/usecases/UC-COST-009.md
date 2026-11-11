# UC-COST-009: Kiểm cost và phân rã ngân sách thực đơn

Phiên bản: 0.1.0 · Ngày: 11/11/2026 · Trạng thái: Draft, chờ review nghiệp vụ.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ SRS Cost v0.1.1 và ERD v0.3.0 |

- **Tác nhân chính/hỗ trợ:** Dinh dưỡng viên; người nội bộ được xem thực đơn.
- **Phạm vi:** Nền tảng Gia Phát, phân hệ Cost; các bước MENU/SYS được gọi qua phân hệ tương ứng.
- **Cấp độ:** Sea level.
- **Quyền:** cost.cost.read để xem con số; quyền MENU để xem/sửa thực đơn.
- **Bên liên quan và kỳ vọng:** tác nhân cần hoàn thành mục tiêu trên; kế toán cần truy vết nguồn giá; người duyệt cần số liệu nhất quán; người ngoài phạm vi không được nhận dữ liệu cost.
- **Tiền điều kiện:** Có thực đơn đã lưu hoặc nội dung nháp, loại suất và các ngày phục vụ; phạm vi cơ sở được xác định.
- **Kích hoạt:** Người dùng mở thực đơn hoặc thêm/đổi/bỏ món.
- **Hậu điều kiện thành công:** Có kết quả ngân sách đúng phiên bản nội dung và phạm vi; chưa tạo snapshot duyệt.
- **Đảm bảo tối thiểu:** không sửa dữ liệu lịch sử đã chụp; lỗi trước commit không ghi một phần; không trả dữ liệu vượt quyền. Với lệnh ghi mất phản hồi, đối soát thay vì khẳng định chưa lưu.
- **Truy vết FR:** `FR-COST-MEAL-001`, `FR-COST-MEAL-002`, `FR-COST-MEAL-003`, `FR-COST-RUL-001`, `FR-COST-RUL-002`.
- **Điểm chạm:** SCR-MENU-10, SCR-COST-12 — xem [user flow](../ui/user-flow.md).

## Luồng sự kiện chính

1. Hệ thống nhận phiên bản nội dung hiện tại và xác định ngày/cơ sở cần kiểm.
2. Hệ thống tính cost từng món theo UC-COST-006; chọn cách gộp món chính, khoản khoán, VAT và ngưỡng hiệu lực.
3. Hệ thống tính cost suất và cost % theo SRS 3.3.2; so ngưỡng bằng % đã làm tròn hai số.
4. Hệ thống trả bảng kiểm gồm BR-COST-001, BR-COST-005, BR-COST-006, BR-COST-007 cùng các quy tắc MENU, lọc dữ liệu theo quyền.
5. Mỗi cột ngày hiện kết quả theo cơ sở; người có quyền mở phân rã món chính/phụ/rau/canh/khoản khoán, doanh thu và phần dư/vượt.
6. Khi đổi món, hệ thống chạy lại và chỉ hiển thị kết quả ứng với nội dung mới nhất.

## Luồng nhánh và ngoại lệ

- **2a. Thiếu giá/VAT:** ERR-COST-422-03 hoặc ERR-COST-422-05; hiện nguyên nhân, không hiện cost 0 hay kết luận đạt. Bổ sung dữ liệu rồi tính lại.
- **2b. Ngày chưa đủ món:** Hiện cost phần có thể tính được kèm chưa đủ món; không kết luận đạt toàn ngày. Nếu phần đã có thiếu giá thì ưu tiên báo thiếu dữ liệu.
- **4a. Không có cost.cost.read:** Bảng kiểm chỉ đạt/không đạt; API loại số tiền, cost %, ngưỡng và chi tiết có thể lộ cost. Dịch vụ agent riêng theo UC-COST-015.
- **4b. Một cơ sở vượt, một cơ sở đạt:** Ngày không đạt ngân sách; chỉ chặn gửi duyệt ở CHAN. Thiếu giá chung/riêng ở một cơ sở thì không xác định, không bỏ qua cơ sở đó.
- **6a. Hai lần kiểm trả về đảo thứ tự:** Không dùng kết quả cũ cho nội dung mới; correlation/version là đề xuất kỹ thuật chờ API. Mất mạng: giữ nháp trên màn hình, không giả lập đạt để gửi duyệt.

## Quy tắc và điểm mở

- Quy tắc: BR-CALC-004, BR-CALC-005, BR-CALC-006, BR-CALC-009, BR-COST-001, BR-COST-007.
- Điểm mở/giới hạn: O-01, E3-Q1, E3-Q2, E3-Q3, E3-Q7, E3-Q12, E2-Q1, DL-01.

## Quy ước dùng chung

Áp dụng [quy ước lỗi/quyền và mất phản hồi](../ui/user-flow.md#quy-uoc-dung-chung). Thiếu quyền trả ERR-AUTH-403-02; ngoài phạm vi trả ERR-SYS-404-01. Lỗi nghiệp vụ trước commit không ghi thay đổi; mất phản hồi sau gửi là **chưa biết đã lưu hay chưa**, phải đối soát trước gửi lại. Các lựa chọn đánh dấu đề xuất/điểm mở không được xem là quyết định đã duyệt.

Nguồn: [SRS Cost](../srs/spec.md) · [Sơ đồ và ma trận truy vết](../srs/usecase-diagram.md) · [ERD](../../nen-tang/srs/erd.md).
