# UC-AIO-004: Áp dụng phương án thành bản nháp

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU, COST và model provider.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Áp dụng phương án thành bản nháp”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: 201 Menu DRAFT hoặc replay 200 cùng menu/version; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: runId, candidateRevision, baseVersion nếu sửa, idempotency key.
- Quy tắc: BR-AIO-004; FR: FR-AIO-APLY-001.

## Luồng chính

1. Người dùng mở UI-AIO-02 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm lại quyền, trạng thái nguồn DRAFT/CHECKED, version, danh mục, quy tắc và cost hiện hành. Nếu nguồn khác evidence: 409 yêu cầu chạy lại. Cùng giao dịch ghi toàn tuần DRAFT, source=AGENT_INTERNAL, agent_run_id, audit và applied_menu_id; không gửi duyệt/công bố.
4. Hệ thống trả 201 Menu DRAFT hoặc replay 200 cùng menu/version; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-AIO-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-AIO-403-01; id ngoài scope → ERR-AIO-404-01.
3a. run VALID nhưng giá hoặc menuVersion đã đổi; hoặc menu PENDING: 409 ERR-AIO-409-01; không ghi một phần tuần; cần chạy lại/đi quy trình MENU.
3b. server đã commit áp dụng nhưng client mất phản hồi: chỉ một menu/version được áp dụng; trả kết quả đã ghi theo quyền hiện tại; không nhân đôi audit thay đổi.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
