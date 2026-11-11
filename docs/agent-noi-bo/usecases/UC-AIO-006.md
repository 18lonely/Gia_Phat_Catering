# UC-AIO-006 — Theo dõi và kết thúc lượt chạy lỗi

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU, COST và model provider.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Theo dõi và kết thúc lượt chạy lỗi”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Run FAILED/outcome TIMEOUT hoặc DEPENDENCY_ERROR; reject 429 khi hết quota; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: runId; deadline, quota và worker event.
- Quy tắc: BR-AIO-006; FR: FR-AIO-OPS-001.

## Luồng chính

1. Người dùng mở UI-AIO-03 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Tổng thời gian tính từ nhận yêu cầu gồm hàng đợi; deadline tối đa 60 giây theo roadmap. Lỗi provider/validator kết thúc FAILED; timeout không nhận kết quả đến muộn. Hạn mức riêng agent nội bộ do O-04/AIO-Q01 xác nhận; không dùng API-COST-036 dành cho agent khách.
4. Hệ thống trả Run FAILED/outcome TIMEOUT hoặc DEPENDENCY_ERROR; reject 429 khi hết quota; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-AIO-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-AIO-403-01; id ngoài scope → ERR-AIO-404-01.
3a. worker chưa xong ở deadline 60 giây; kết quả tới giây 65: FAILED/TIMEOUT; candidate không áp dụng được; ghi late_result_ignored không mở lại run.
3b. quota cấu hình đã cạn hoặc provider không truy cập được: 429 ERR-AIO-429-01 không gọi provider; tình huống còn quota thì FAILED/DEPENDENCY_ERROR có log.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
