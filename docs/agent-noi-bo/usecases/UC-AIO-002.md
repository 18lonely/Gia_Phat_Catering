# UC-AIO-002 — Kiểm phương án bằng hệ thống

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU, COST và model provider.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Kiểm phương án bằng hệ thống”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Run outcome VALID/NO_SOLUTION/BLOCKED_DATA, bảng kiểm và evidence; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: candidate với recipeId, ngày, cơ sở; revision và phiên bản tham số.
- Quy tắc: BR-AIO-002; FR: FR-AIO-CHK-001.

## Luồng chính

1. Người dùng mở UI-AIO-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Gọi FR-MENU-RUL-002 và API-COST-025 cho cùng hash phương án; hệ thống tính số, mô hình chỉ diễn giải. Chỉ VALID khi không vi phạm cứng, đủ đầu vào, không vượt ngưỡng từng ngày/cơ sở và không chứa món ngoài danh mục; giữ cảnh báo mềm, không tự viết lý do thay người duyệt.
4. Hệ thống trả Run outcome VALID/NO_SOLUTION/BLOCKED_DATA, bảng kiểm và evidence; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-AIO-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-AIO-403-01; id ngoài scope → ERR-AIO-404-01.
3a. một nguyên liệu thiếu VAT hoặc giá hiệu lực: DONE/BLOCKED_DATA; không có candidate áp dụng; chỉ rõ dependency COST và nguyên nhân; không tự gán VAT 0.
3b. quy tắc cứng đạt nhưng cost vượt ở 1 cơ sở với chế độ CANH_BAO: DONE/NO_SOLUTION; không nhãn VALID; không thay chế độ hay ngưỡng Cost.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
