# UC-AIO-005 — Tra cứu nhật ký agent

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: GIAM_DOC; hệ thống hỗ trợ: AUTH/SYS, MENU, COST và model provider.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Tra cứu nhật ký agent”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: RunLog phân trang, ToolEvent[], usage; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: runId hoặc cursor, khoảng ngày, userId, status.
- Quy tắc: BR-AIO-005; FR: FR-AIO-LOG-001.

## Luồng chính

1. Người dùng mở UI-AIO-03 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Chỉ đọc theo quyền log và cơ sở; lưu model/promptVersion, input/output tokens, chi phí ước tính/thực ghi nhận, outcome, tool event requestId và thời gian. Chi phí chưa biết là null + UNKNOWN, không phải 0; lọc token/bí mật và nội dung ngoài quyền.
4. Hệ thống trả RunLog phân trang, ToolEvent[], usage; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-AIO-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-AIO-403-01; id ngoài scope → ERR-AIO-404-01.
3a. tài khoản không có aio.logs.read: 403 ERR-AIO-403-01; không trả prompt, cost hoặc token usage.
3b. provider timeout trước khi gửi usage: cost_vnd=null; usageStatus=UNKNOWN; không báo chi phí 0; giữ dấu vết lỗi đã lọc.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
