# User flow (AIO)

Phiên bản 0.1.0 · 2026-11-11 · **Draft: đề xuất thiết kế để review, chưa phê duyệt nghiệp vụ; chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo gói MVP từ PRD/roadmap và thiết kế hiện có |

```mermaid
flowchart TD
  A[Yêu cầu UI-AIO-01] --> B{Đủ quyền, input, quota?}
  B -- Không --> C[Báo lỗi, không gọi model]
  B -- Có --> D[QUEUED rồi RUNNING, log bền vững]
  D --> E{Hiểu rõ kiêng kỵ và yêu cầu?}
  E -- Không --> F[DONE NEEDS_INPUT]
  F --> A
  E -- Có --> G[Đề xuất candidate từ danh mục ACTIVE]
  G --> H[MENU kiểm quy tắc và COST kiểm số]
  H --> I{Đạt, đủ, không vượt?}
  I -- Không --> J{Còn lượt thử và thời gian?}
  J -- Có --> G
  J -- Không --> K[NO_SOLUTION hoặc BLOCKED_DATA hoặc TIMEOUT]
  I -- Có --> L[UI-AIO-02 xem nháp VALID và bảng kiểm]
  L --> M[Chỉnh bằng lời tạo run mới và diff]
  M --> E
  L --> N[Người dùng xác nhận áp dụng]
  N --> O{Quyền và nguồn còn đúng?}
  O -- Không --> P[409 hoặc từ chối quyền, không ghi]
  O -- Có --> Q[Ghi tuần DRAFT + audit nguyên tử]
  Q --> R[Người dùng đi tiếp FEAT-013 của MENU]
  K --> S[UI-AIO-03 nhật ký]
  Q --> S
```

## Trạng thái màn hình chung

| Trạng thái | Hiển thị / hành vi |
| :--- | :--- |
| Normal | Đủ nhãn, nguồn/version và quyền thao tác; nút quay lại không ghi dữ liệu |
| Loading | Khóa gửi trùng, giữ input; đối chiếu clientRevision hoặc runId trước nhận response |
| Empty | Nêu chưa có dữ liệu/lượt chạy; không thay bằng số 0 hoặc ví dụ thật |
| Error | Hiện mã/requestId và hướng xử lý SRS; 409 yêu cầu tải lại; không tự ghi đè |
| Offline | Dừng poll/tính/lưu; giữ nội dung nhập trong phiên, không báo thành công; trở lại mạng phải GET đối soát trước retry |
| Permission changed | Dừng gọi tiếp; bỏ dữ liệu hiển thị không còn quyền, server vẫn kiểm lại; không replay response cũ |

Truy vết màn và trường: [wireframe](wireframe-ascii.md); [API](../api/api-spec.md); [use case/story/test](../test/traceability.md). Không có test tương tác UI vì đây là wireframe ASCII.
