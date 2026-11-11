# UC-NUTR-001 — Quản lý bảng thành phần

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Quản lý bảng thành phần”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: NutrientValue với version mới; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: ingredientId, 4 chỉ số/100 g phần ăn được, ediblePct, gramsPerUnit, sourceEdition, sourceLocator, version, lý do.
- Quy tắc: BR-NUTR-001; FR: FR-NUTR-REF-001.

## Luồng chính

1. Người dùng mở UI-NUTR-01 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm kiểu và miền giá trị; bắt buộc nguồn D-17 có ấn bản và trang/mã thực phẩm; ghi giá trị hiện hành, bản lịch sử và audit trong một giao dịch; không ngầm dùng mặc định 100 khi chưa được người nhập xác nhận.
4. Hệ thống trả NutrientValue với version mới; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
3a. I1 có version=1: 422; ERR-NUTR-422-01; không ghi bất kỳ bảng nào.
3b. hai người cùng đọc I1 version=1; người thứ nhất đã ghi version=2: 409 ERR-NUTR-409-01; giá trị version=2 không bị ghi đè.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
