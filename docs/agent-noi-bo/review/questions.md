# Sổ câu hỏi (AIO)

Phiên bản 0.1.1 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-12; AIO-Q07; XC-12; AIO-Q07, E1-Q06 |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Không có người/ngày ký thay stakeholder. Đề xuất kỹ thuật không đóng điểm mở nghiệp vụ.

| Mã | Câu hỏi | Vai trò cần trả lời | Tác động | Trạng thái | Trả lời |
| :--- | :--- | :--- | :--- | :--- | :--- |
| AIO-Q01 | Nhà cung cấp/model, ngân sách, concurrency, số lần thử, token tối đa và cách ghi chi phí/tỷ giá nào? | Giám đốc, Tech lead | O-04; không có mặc định ngân sách được duyệt | CHỜ XÁC NHẬN |  |
| AIO-Q02 | Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không? | Chủ sản phẩm, dinh dưỡng viên | FR-AIO-CHK-001; đề xuất NO_SOLUTION không cho áp dụng; không thay cổng MENU/Cost | CHỜ XÁC NHẬN |  |
| AIO-Q03 | 20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao? | Dinh dưỡng viên, QA | NFR-AIO-001/002; không tính từ chối/timeout là một thực đơn đạt | CHỜ XÁC NHẬN |  |
| AIO-Q04 | Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào? | Giám đốc, Tech lead | FR-AIO-LOG-001; mặc định thiết kế không có API xuất log | CHỜ XÁC NHẬN |  |
| AIO-Q05 | Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào? | Dinh dưỡng viên | FR-AIO-GEN-001/EDIT-001; chưa rõ phải hỏi lại, không tư vấn điều trị | CHỜ XÁC NHẬN |  |
| AIO-Q06 | Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout? | Tech lead, BA | FR-AIO-APLY-001; hợp đồng port đề xuất, chưa có endpoint MENU được triển khai | CHỜ XÁC NHẬN |  |
| AIO-Q07 | E5 phải cung cấp bằng chứng nào để đối chiếu phép đo phản hồi đầu NFR-PERF-003 với polling và thời gian dựng thực đơn? | chưa rõ | BLOCKED nghiệm thu phép đo phản hồi đầu; AIO-Q01 và E1-Q06 còn mở. XC-12; DEC-199. Đối chiếu đề xuất E1-Q06; giữ hai chỉ số riêng, chưa chọn cách đo. | CHỜ TRẢ LỜI |  |

> Chờ AIO-Q07, E1-Q06: XC-12. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-12](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Khi trả lời: ghi lựa chọn, ví dụ/ca biên, người xác nhận, ngày, nguồn và phiên bản tài liệu; cập nhật SRS/API/ERD/UI/AC/test rồi mới đóng. Ca BLOCKED chuyển NOT RUN khi đủ đầu vào, không tự chuyển PASS. Các ca kỹ thuật dùng fixture giả định có thể chuẩn bị độc lập.
