# Kiểm tra API và wireframe Cost

Ngày: 11/11/2026 · API/wireframe v0.1.0 · Trạng thái: kiểm tra bản nháp đạt, chưa nghiệm thu nghiệp vụ.

## Phạm vi và kết quả

| Hạng mục | Kết quả |
| :--- | :--- |
| API | 37 endpoint có method/path không trùng, 42 kiểu dữ liệu mô tả; chưa phải OpenAPI machine schema |
| Truy vết | Tập FR trong catalog khớp 45 FR của SRS qua endpoint, hook nội bộ hoặc 2 FR hoãn |
| Màn hình | Render 18/18; không có lỗi JavaScript trong lần kiểm |
| Mobile | 18/18 màn tại 390 px không tràn ngang toàn trang; bảng dài cuộn trong khung |
| Tương tác | Tạo NCC; mất mạng không ghi; giá biến động cần xác nhận trước khi lưu; nhập mẫu lỗi/hợp lệ |
| Duyệt | DD lập bảng, GD duyệt; đề nghị chế độ tương lai được duyệt nhưng chưa đổi chế độ hiện tại |
| Dự toán | Thiếu giá không lưu; bản mới tăng phiên bản và giữ nguyên bản cũ |
| Phân quyền mô phỏng | QL không thấy bảng tính cơ sở khác; bếp chỉ thấy dự toán cơ sở của mình và không thấy tiền cả trong bản xem trước xuất |
| Trạng thái | Loading, empty, error render được; offline chặn ghi |

Đã xem ảnh desktop 1440 px và mobile 390 px: chữ đọc được, form và bảng nằm trong khung. Đã sửa lọc cơ sở ở chi tiết bảng tính, trạng thái menu hiện tại và đối soát tổng dòng chi phí mẫu.

## Chạy lại

Script: [check-api-wireframe.cjs](check-api-wireframe.cjs). Cần Node.js, Playwright và Chrome; truyền thư mục chứa `node_modules/playwright` làm đối số:

```powershell
node docs/cost/validation/check-api-wireframe.cjs "$env:TEMP/gia-phat-cost-validation"
```

Ảnh: [desktop](cost-desktop.png), [mobile](cost-mobile.png). Catalog: [endpoint-catalog.json](../api/endpoint-catalog.json).

## Giới hạn và phần còn lại

Đây là kiểm tra tài liệu và tương tác dữ liệu giả. Chưa kiểm API thật, database, độ chính xác engine, an toàn backend, import/export thật hay hiệu năng. Kiểm quyền DOM trong mẫu không chứng minh bảo mật production. Chưa kiểm mọi tổ hợp vai trò/trạng thái hoặc mọi nhánh lỗi nghiệp vụ.

Hợp đồng đề xuất làm rõ idempotency 24h kế thừa SYS, đối soát khi mất phản hồi, phiên bản cạnh tranh và worker nội bộ. Một số mã lỗi kỹ thuật, token phiên bản, kho idempotency/outbox cần Tech lead review và thiết kế migration; không được coi đã có trong DBML.

Tiếp theo: backlog/user story và AC truy vết FR/UC/API/màn, checklist/test case nghiệp vụ; chốt các điểm mở SRS và user flow với chủ sở hữu. Giữ trạng thái Draft đến khi review nghiệp vụ hoàn tất.
