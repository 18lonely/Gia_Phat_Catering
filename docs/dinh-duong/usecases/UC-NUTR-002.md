# UC-NUTR-002 — Kiểm độ phủ nguyên liệu

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Kiểm độ phủ nguyên liệu”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Coverage: complete/total, missing[], recipeVersions; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: recipeIds của danh mục 30 món đã duyệt.
- Quy tắc: BR-NUTR-002; FR: FR-NUTR-REF-002.

## Luồng chính

1. Người dùng mở UI-NUTR-01 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Lấy tập nguyên liệu duy nhất từ đúng phiên bản công thức; đếm đủ 4 chỉ số, nguồn, đơn vị và tỷ lệ; chỉ số 0 hợp lệ khác null; trả thiếu theo nguyên liệu và món bị ảnh hưởng, không tự điền số.
4. Hệ thống trả Coverage: complete/total, missing[], recipeVersions; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
3a. I2 chưa có bảng thành phần: 200; complete=1,total=2; missing ghi I2 và cả hai recipeId; không thay null bằng 0.
3b. I1 có cả bốn chỉ số bằng 0 và nguồn đầy đủ: lần đầu complete=1; lần sau 401 ERR-NUTR-401-01; không trả dữ liệu.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
