# Backlog MVP (AIO)

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Tất cả P0 theo feature MVP. Story point để **chưa ước lượng** vì O-04/đội chưa chốt; không giả số đã cam kết. INVEST: giá trị và AC cụ thể; còn phụ thuộc được nêu, chưa coi Sprint-ready khi câu hỏi liên quan mở.

| Story | Nội dung | FR / Feature | Phụ thuộc | UC / UI / API / Bảng |
| :--- | :--- | :--- | :--- | :--- |
| US-AIO-001 | Là một DINH_DUONG_VIEN, tôi muốn yêu cầu dựng thực đơn tuần để có phương án nháp theo loại suất, tuần và kiêng kỵ. | FR-AIO-GEN-001; FEAT-021 | R1/R2/R3, O-04 | [UC-AIO-001](../usecases/UC-AIO-001.md); UI-AIO-01; API-AIO-001; agent_runs, agent_run_contexts |
| US-AIO-002 | Là một DINH_DUONG_VIEN, tôi muốn kiểm phương án bằng hệ thống để chỉ nhận nháp đạt có bằng chứng quy tắc và cost. | FR-AIO-CHK-001; FEAT-021 | R1/R2/R3, O-04 | [UC-AIO-002](../usecases/UC-AIO-002.md); UI-AIO-02; API-AIO-002; agent_run_contexts, agent_tool_events |
| US-AIO-003 | Là một DINH_DUONG_VIEN, tôi muốn chỉnh thực đơn bằng lời để xem rõ món đổi và kiểm lại toàn tuần. | FR-AIO-EDIT-001; FEAT-022 | R1/R2/R3, O-04 | [UC-AIO-003](../usecases/UC-AIO-003.md); UI-AIO-02; API-AIO-003; agent_runs, agent_run_contexts |
| US-AIO-004 | Là một DINH_DUONG_VIEN, tôi muốn áp dụng phương án thành bản nháp để chủ động nhận thay đổi đã kiểm trước khi duyệt. | FR-AIO-APLY-001; FEAT-022 | R1/R2/R3, O-04 | [UC-AIO-004](../usecases/UC-AIO-004.md); UI-AIO-02; API-AIO-004; menus, menu_days, menu_day_items, agent_run_contexts, audit_logs |
| US-AIO-005 | Là một GIAM_DOC, tôi muốn tra cứu nhật ký agent để kiểm được ai yêu cầu, công cụ, kết quả và chi phí. | FR-AIO-LOG-001; FEAT-023 | R1/R2/R3, O-04 | [UC-AIO-005](../usecases/UC-AIO-005.md); UI-AIO-03; API-AIO-005; agent_runs, agent_run_contexts, agent_tool_events |
| US-AIO-006 | Là một DINH_DUONG_VIEN, tôi muốn theo dõi và kết thúc lượt chạy lỗi để biết chạy lỗi hay hết hạn mà không tạo nháp trùng. | FR-AIO-OPS-001; FEAT-023 | R1/R2/R3, O-04 | [UC-AIO-006](../usecases/UC-AIO-006.md); UI-AIO-03; API-AIO-006; agent_runs, agent_tool_events, agent_run_contexts |
