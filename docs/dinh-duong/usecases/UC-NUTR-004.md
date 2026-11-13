# UC-NUTR-004: Tính dinh dưỡng tổ hợp suất

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Tính dinh dưỡng tổ hợp suất”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Calculation MEAL theo tổ hợp tường minh; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: menuId, menuVersion, serviceDate, selectedItemIds, clientRevision.
- Quy tắc: BR-NUTR-004; FR: FR-NUTR-CALC-002.

## Luồng chính

1. Người dùng mở UI-NUTR-03 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm món thuộc ngày và đủ số món theo meal_type; chỉ cộng món chọn và món cố định đúng một lần; không cộng tất cả lựa chọn chính, không lấy món đắt nhất của COST; gắn recipeId/version và nguồn vào kết quả.
4. Hệ thống trả Calculation MEAL theo tổ hợp tường minh; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
3a. suất cần 1 chính, người dùng chọn A và B: 422 ERR-NUTR-422-03; không tính tổng.
3b. đang xem menuVersion=2, một người sửa thành 3: 409 ERR-NUTR-409-01 hoặc 404 ERR-NUTR-404-01 tương ứng; không lộ dữ liệu ngoài quyền.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
