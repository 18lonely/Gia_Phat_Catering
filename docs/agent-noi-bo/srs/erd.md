# ERD và từ điển dữ liệu (AIO)

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

Nguồn vật lý duy nhất: [schema tổng DBML v0.5.0](../../nen-tang/srs/schema.dbml). Thiết kế bổ sung, chưa migration. Không tạo bảng thứ hai thay nutrient_values hoặc agent_runs. DBML không tự thực thi mọi CHECK trong tài liệu này.

```mermaid
erDiagram
  users ||--o{ agent_runs : requests
  agent_runs ||--o| agent_run_contexts : internal_context
  agent_runs ||--o{ agent_tool_events : trace
  agent_runs o|--o{ agent_run_contexts : revision_parent
  menus o|--o{ agent_run_contexts : base_menu
  menus o|--o{ agent_run_contexts : applied_menu
  agent_runs o|--o{ menus : latest_agent_application
```

Từ điển dữ liệu (bảng kế thừa, bảng mới, ràng buộc giao dịch) đã chuyển nguyên văn sang [data-dictionary.md](data-dictionary.md) ngày 16/11/2026.
