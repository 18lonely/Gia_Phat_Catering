# UC-MENU-008: Kiểm quy tắc thực đơn

Phiên bản 0.1.0 · 2026-11-10 · Draft · [Sơ đồ use case](../srs/usecase-diagram.md) · [SRS](../srs/spec.md)

- **Tác nhân chính**: Hệ thống — được gọi từ `UC-MENU-007`, `UC-MENU-009`, và từ agent ở R5, R9.
- **Phạm vi**: Module MENU — dịch vụ kiểm quy tắc.
- **Cấp độ**: Fish level (chức năng con).
- **Các bên liên quan & kỳ vọng**:
  - Dinh dưỡng viên: biết chính xác quy tắc nào vi phạm, ở ngày nào, món nào.
  - Người duyệt: tin được rằng thực đơn gửi lên đã qua cùng một bộ kiểm.
  - Agent: dùng đúng bộ kiểm mà người dùng thấy, không có bộ kiểm riêng.
- **Tiền điều kiện**: thực đơn tồn tại (đã lưu) hoặc nội dung thực đơn được gửi kèm lời gọi (chưa lưu).
- **Hậu điều kiện thành công**: có kết quả đạt / không đạt cho từng quy tắc đang bật, điểm quy tắc, và cờ "còn vi phạm cứng". Với thực đơn đã lưu, kết quả cũ được thay bằng kết quả mới.
- **Đảm bảo tối thiểu**: cùng đầu vào và cùng danh mục quy tắc luôn cho cùng kết quả (`NFR-MENU-005`). Thực đơn từ `PENDING` trở đi không bị ghi đè kết quả.
- **Kích hoạt**: một món trong thực đơn nháp thay đổi; hoặc Dinh dưỡng viên gửi duyệt; hoặc agent yêu cầu kiểm một phương án.

## Luồng sự kiện chính

1. Hệ thống nạp thực đơn: loại suất, các ngày phục vụ, món ở từng ô kèm thuộc tính hiện hành của món.
2. Hệ thống nạp danh mục quy tắc đang bật cùng tham số.
3. Hệ thống nạp các ngày phục vụ liền trước tuần đó của cùng loại suất, nếu quy tắc cần.
4. Với mỗi ngày, hệ thống chạy các quy tắc cấp ngày.
5. Hệ thống chạy các quy tắc cấp tuần trên toàn thực đơn.
6. Với mỗi quy tắc không đạt, hệ thống ghi: mã, tên, loại, ngày liên quan, món liên quan, giá trị đo được, giới hạn.
7. Hệ thống tính điểm: 100 trừ tổng điểm phạt của các quy tắc mềm không đạt, sàn là 0. Quy tắc cấp ngày không đạt ở nhiều ngày bị trừ mỗi ngày một lần.
8. Hệ thống đặt cờ "còn vi phạm cứng" nếu có ít nhất một quy tắc cứng không đạt.
9. Hệ thống ghi kết quả (nếu thực đơn đã lưu) và trả về cho nơi gọi.

## Các luồng nhánh & ngoại lệ

- **1a. Ngày chưa đủ món**: các quy tắc về cơ cấu (`BR-MENU-001`, `002`, `004`, `005`) báo không đạt; các quy tắc khác chỉ xét món đã có. Use case tiếp tục.
- **1b. Lời gọi cho thực đơn chưa lưu chứa món không tồn tại, không `ACTIVE`, hoặc sai vai trò**: hệ thống báo `ERR-MENU-422-14`; kết thúc.
- **1c. Món không có giá bán hiệu lực tại ngày phục vụ** (cần cho `BR-COST-012`): quy tắc đó báo không đạt kèm `ERR-MENU-404-02`. Use case tiếp tục.
- **3a. Không có thực đơn tuần trước**: quy tắc xét ngày liền trước chỉ tính trong tuần hiện tại.
- **9a. Lần kiểm này làm một quy tắc mềm mức nặng chuyển từ không đạt sang đạt**: hệ thống xoá lý do chấp nhận đã ghi cho quy tắc đó.
- **9b. Thực đơn ở trạng thái `PENDING`, `APPROVED`, `PUBLISHED` hoặc `WITHDRAWN`**: hệ thống trả kết quả đã có lúc gửi duyệt, không chạy lại ([E2-Q11]).

## Quy tắc nghiệp vụ liên quan

Cách tính từng quy tắc: SRS mục 3.3.2. Trong R2 chạy 31 quy tắc `BR-MENU` và `BR-COST-012`; `BR-COST-008` → `010` kiểm khi lưu công thức và nguyên liệu, không chạy ở đây. Các quy tắc cost cần giá nhập đăng ký thêm ở R3.

## Yêu cầu đặc biệt

- p95 ≤ 2 giây cho thực đơn 6 ngày, mỗi ngày ≤ 10 món (`NFR-MENU-001`).
- 20 lời gọi đồng thời cho thực đơn chưa lưu với p95 ≤ 2 giây (`NFR-MENU-002`).

## Điểm mở

- Loại cứng/mềm, điểm phạt, giá trị tham số từng quy tắc: chờ DL-01.
- Bước 3 có áp dụng hay không: [E2-Q2].
- `BR-MENU-051` chưa có định nghĩa: [H-5].
