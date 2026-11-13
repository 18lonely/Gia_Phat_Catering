# UC-NUTR-005: Xem kết quả và nguồn lịch sử

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Xem kết quả và nguồn lịch sử”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: Calculation, sourceVersions, isStale, label; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: calculationId; quyền hiện tại.
- Quy tắc: BR-NUTR-005; FR: FR-NUTR-SNAP-001.

## Luồng chính

1. Người dùng mở UI-NUTR-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kết quả tính thành công lưu bất biến inputs_snapshot và totals; GET trả bản cũ cùng isStale nếu nguồn hiện tại khác. Tính lại tạo id mới; không thay lịch sử hay biến bản tính thành bản duyệt thực đơn.
4. Hệ thống trả Calculation, sourceVersions, isStale, label; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-NUTR-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-NUTR-403-01; id ngoài scope → ERR-NUTR-404-01.
3a. người dùng không có quyền cơ sở của C1: 404 ERR-NUTR-404-01; không trả totals hoặc nguồn.
3b. C1 và C2 là hai lần tính, clientRevision 1 và 2: UI giữ C2; lịch sử vẫn xem C1; cả hai có nhãn ước tính từ định lượng sống.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
