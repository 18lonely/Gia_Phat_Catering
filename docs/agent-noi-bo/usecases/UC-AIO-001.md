# UC-AIO-001 — Yêu cầu dựng thực đơn tuần

Phiên bản 0.1.0 · 2026-11-11 · **Draft — đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

- Mức: Sea level. Tác nhân chính: DINH_DUONG_VIEN; hệ thống hỗ trợ: AUTH/SYS, MENU, COST và model provider.
- Bên quan tâm: dinh dưỡng viên cần kết quả truy nguồn; Giám đốc cần audit và đúng phạm vi.
- Trigger: người dùng chọn “Yêu cầu dựng thực đơn tuần”.
- Tiền điều kiện: phiên hợp lệ, quyền được cấp, dữ liệu theo input có thể đọc trong phạm vi.
- Đảm bảo thành công: 202 Run QUEUED; sau đó RUNNING rồi DONE/REJECTED/FAILED; không vượt quyền hoặc tự công bố.
- Đảm bảo tối thiểu: lỗi không để lại dữ liệu nghiệp vụ một phần; log kỹ thuật chỉ chứa thông tin được phép.
- Input: mealTypeId, weekStart, kitchenIds, exclusions{ingredientIds,dishIds}, requestText, idempotency key.
- Quy tắc: BR-AIO-001; FR: FR-AIO-GEN-001.

## Luồng chính

1. Người dùng mở UI-AIO-01 và nhập/chọn đầu vào.
2. Hệ thống xác thực quyền, kiểm scope, kiểu dữ liệu và version.
3. Hệ thống xử lý: Kiểm quyền giao giữa người dùng và dịch vụ; tuần bắt đầu thứ Hai; chỉ dùng danh mục ACTIVE và công thức hiệu lực. Đăng ký run bền vững trước gọi mô hình; ngữ nghĩa chưa rõ chuyển NEEDS_INPUT, không đoán kiêng kỵ.
4. Hệ thống trả 202 Run QUEUED; sau đó RUNNING rồi DONE/REJECTED/FAILED; UI chỉ nhận đúng clientRevision/runId đang xem.
5. Người dùng xem kết quả, nguồn/trạng thái; quay lại sửa đầu vào hoặc chuyển bước tiếp theo trong user flow.

## Nhánh và ngoại lệ

2a. Mất phiên → ERR-AIO-401-01; yêu cầu đăng nhập lại, không tự phát lại lệnh ghi.
2b. Không có quyền → ERR-AIO-403-01; id ngoài scope → ERR-AIO-404-01.
3a. yêu cầu không xác định cá nào phải kiêng: run DONE/outcome=NEEDS_INPUT; câu hỏi và structuredInput thiếu, không có candidate để áp dụng.
3b. K1 đã tạo run R1: cùng body trả R1 không chạy lần hai; body khác 409 ERR-AIO-409-02.
4a. Mất mạng/phản hồi: giữ dữ liệu nhập; thao tác ghi phải đối soát version/run/key trước khi thử lại; không báo thành công nếu chưa xác định kết quả.

Kiểm chi tiết: [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [API](../api/api-spec.md).
