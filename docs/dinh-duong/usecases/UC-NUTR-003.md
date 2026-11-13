# UC-NUTR-003: Tính dinh dưỡng món

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Tính dinh dưỡng món”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Calculation DISH, 4 totals, breakdown, provenance, label; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: recipeId ACTIVE, serviceDate, clientRevision.
- Quy tắc: BR-NUTR-003; FR: FR-NUTR-CALC-001.

## Luồng chính

1. Người dùng mở UI-NUTR-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Theo từng dòng qty_std × hệ số gram × edible_pct/100 × chỉ số/100; cộng Decimal chưa làm tròn; không áp COST_AP_HAO_HUT, không suy năng lượng bằng 4-4-9; trả phân rã và nguồn. Recipe phải có hiệu lực ngày phục vụ.
4. Hệ thống trả Calculation DISH, 4 totals, breakdown, provenance, label; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
3a. công thức dùng 1 quả nhưng gramsPerUnit thiếu: 422 ERR-NUTR-422-02; totals=null; chỉ rõ nguyên liệu thiếu quy đổi, không trả tổng một phần.
3b. qty=1 quả; gramsPerUnit=50; edible=80%; cùng thành phần I1: hai kết quả bằng nhau:40.00/4.00/0.80/6.00; không nhân hao hụt Cost.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
