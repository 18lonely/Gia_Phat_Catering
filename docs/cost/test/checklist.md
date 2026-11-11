# Checklist kiểm thử Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft để BA/QA/Tech lead review.

Nguồn: [SRS Cost](../srs/spec.md), [16 use case](../srs/usecase-diagram.md), [API đề xuất](../api/api-spec.md), [user flow](../ui/user-flow.md).

Checklist đã được tự rà truy vết với SRS, chưa có BA/QA ký duyệt. Test case chi tiết được soạn song song làm bản nháp review theo yêu cầu tiếp tục công việc; chưa coi bước review con người đã hoàn tất.

| Nhóm | Story | Nội dung cần review | Số ca | Trạng thái review |
| :--- | :--- | :--- | :---: | :--- |
| CHK-COST-001 | US-COST-001 | Tạo, sửa và lọc NCC; Tên trùng sau chuẩn hóa; Ngừng không xóa giá cũ | 3 | Chờ BA/QA |
| CHK-COST-002 | US-COST-002 | Giá đầu tiên; Giá không hợp lệ; Biên ngày và khóa trùng; Tham chiếu không tồn tại; Schema và trường do server quản lý; NCC inactive có hai mã lỗi trong SRS | 6 | Chờ BA/QA |
| CHK-COST-003 | US-COST-003 | Ưu tiên giá cơ sở; Không dùng giá tương lai; Chuyển cờ trong cùng nhóm tương lai | 3 | Chờ BA/QA |
| CHK-COST-004 | US-COST-004 | Bỏ qua dòng không đổi; Một dòng sai rollback; Mất phản hồi sau commit; Hiệu năng lưới200 dòng; Key cùng body khác và đang xử lý | 5 | Chờ BA/QA |
| CHK-COST-005 | US-COST-005 | Đọc đúng tên cột; Tệp lỗi không ghi; Giới hạn dòng và đọc số; Import đã kiểm bị đổi; Số dạng văn bản và trang tính | 5 | Chờ BA/QA |
| CHK-COST-006 | US-COST-006 | Hủy giá tương lai độc lập; Giá đã hiệu lực; Phạm vi lịch sử | 3 | Chờ BA/QA |
| CHK-COST-007 | US-COST-007 | Thiếu giá theo cơ sở; Chạy lại không nhân cảnh báo; Biên tuổi giá | 3 | Chờ BA/QA |
| CHK-COST-008 | US-COST-008 | Xác nhận rồi lưu; Hủy xác nhận; Đúng ngưỡng và giá đầu tiên; Token xác nhận stale | 4 | Chờ BA/QA |
| CHK-COST-009 | US-COST-009 | Gắn PDF hợp lệ; Sai nội dung và quá dung lượng; Thu hồi quyền và URL hết hạn | 3 | Chờ BA/QA |
| CHK-COST-010 | US-COST-010 | Tính chính xác theo đơn vị; Không trả tổng thiếu; Công thức theo ngày và quyền; Món không tồn tại; Hao hụt đúng một lần; Đối soát bộ kế toán; Decimal và không làm tròn trung gian; Tổng cost0 không chia cho0 | 8 | Chờ BA/QA |
| CHK-COST-011 | US-COST-011 | So sánh cùng ngày; Một bản thiếu giá; Cost gốc bằng0 | 3 | Chờ BA/QA |
| CHK-COST-012 | US-COST-012 | Chụp bản pending; Sai loại món; Thiếu một giá | 3 | Chờ BA/QA |
| CHK-COST-013 | US-COST-013 | Duyệt bởi người khác; Không tự duyệt hoặc thiếu lý do; Hiệu lực và cơ sở; Hai quyết định cạnh tranh | 4 | Chờ BA/QA |
| CHK-COST-014 | US-COST-014 | Gợi ý không tự ghi; Thiếu giá không phân nhóm; Biên phân nhóm | 3 | Chờ BA/QA |
| CHK-COST-015 | US-COST-015 | Ngày đủ món; VAT thiếu hoặc mẫu số0; Làm tròn rồi so ngưỡng; Ba phương pháp món chính; Ngày chưa đủ món và phản hồi cũ; Hiệu năng tính thực đơn | 6 | Chờ BA/QA |
| CHK-COST-016 | US-COST-016 | Ưu tiên riêng thay chung; Khoản sai không nhận; Số0 và người đề nghị; Khoản trùng khi duyệt | 4 | Chờ BA/QA |
| CHK-COST-017 | US-COST-017 | Mọi cơ sở đều đạt; Một cơ sở vượt; Cảnh báo không bỏ qua dữ liệu thiếu | 3 | Chờ BA/QA |
| CHK-COST-018 | US-COST-018 | Chụp từng ngày/cơ sở; Giá đổi trong lúc chờ; Bất biến và rollback | 3 | Chờ BA/QA |
| CHK-COST-019 | US-COST-019 | Duyệt thay đổi SYS; Tự duyệt bị cấm; Hiệu lực tương lai | 3 | Chờ BA/QA |
| CHK-COST-020 | US-COST-020 | Đăng ký đúng quy tắc; Không lộ tiền trong lỗi; Quyền thay đổi và agent nội bộ; Hồi quy quy tắc đã thuộc MENU | 4 | Chờ BA/QA |
| CHK-COST-021 | US-COST-021 | Chỉ một trạng thái; Thực đơn lỗi; Quota lời gọi31; Thiếu giá và trạng thái hỗn hợp; Không rò dữ liệu toàn API; Quyền DB agent khách; Log budget không chứa số | 7 | Chờ BA/QA |
| CHK-COST-022 | US-COST-022 | Gộp nguyên liệu và đủ cột; Số suất sai; Làm tròn lên lượng mua; K lớn hơn1 | 4 | Chờ BA/QA |
| CHK-COST-023 | US-COST-023 | Tuần đủ dữ liệu; Một ngày thiếu giá; Retry tuần và phiên bản | 3 | Chờ BA/QA |
| CHK-COST-024 | US-COST-024 | Lập lại không sửa cũ; Bếp không xem cơ sở khác; Không có cột tiền ẩn | 3 | Chờ BA/QA |
| CHK-COST-025 | US-COST-025 | Bản đủ giá; Quyền bị thu hồi trước tải; Bản chỉ lượng không giấu tiền trong tệp | 3 | Chờ BA/QA |
| CHK-COST-026 | US-COST-026 | Tính lại đúng tập; Không tính lại ngày đã qua; Không trùng cảnh báo | 3 | Chờ BA/QA |
| CHK-COST-027 | US-COST-027 | Đóng tay có audit; Lý do ngắn hoặc thiếu quyền; Đóng theo sự kiện nghiệp vụ | 3 | Chờ BA/QA |
| CHK-COST-028 | US-COST-028 | Mô phỏng không ghi; Giá giả định sai; Phạm vi và thiếu giá khác | 3 | Chờ BA/QA |

## Review xuyên suốt

- Chức năng và dữ liệu: 24 BR định nghĩa trong Cost, các quy tắc Cost/MENU/SYS phụ thuộc, lỗi nghiệp vụ, ranh giới ngày/số tiền/quota.
- Bảo mật: role × cơ sở × endpoint, success/error/export/replay, không giấu tiền bằng CSS; quyền người tạo và người sửa cuối khi duyệt.
- Giao diện: trạng thái loading/empty/error/offline, giữ bản sửa khi lỗi, không hiển thị phản hồi revision cũ. Wireframe chỉ là bằng chứng thiết kế; mobile/keyboard của app thật cần QA bổ sung sau khi có UI.
- Hiệu năng/chính xác: cả 8 NFR Cost có ca; cần môi trường thật và bộ đối soát 10 món/10 ngày của kế toán.
- Kỹ thuật API: idempotency/hash, xung đột phiên bản, xác nhận stale, import token stale và outbox cần test tích hợp sau Tech lead duyệt. Đây là phần bổ sung bên dưới, không thay14 lỗi SRS.
- Hoãn: FR-COST-MEAL-007 và FR-COST-ALR-004 chưa có test thực thi thành công; không tính vào độ phủ đã viết ca.

Người review cần điền: tên/ngày, quyết định chấp nhận hoặc yêu cầu sửa, điểm mở liên quan; trạng thái mặc định Chờ review.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo bản nháp truy vết, giữ điểm mở và trạng thái chưa chạy |
