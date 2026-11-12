# Từ điển và delta E9

Draft · 12/11/2026 · [Mapping chi tiết](../api/data-mapping.md) là danh mục nguồn→API→UI; [DTO](../api/api-spec.md) là hình dạng đề xuất, không contract đã freeze.

| Thuật ngữ | Ý nghĩa / bất biến |
| :--- | :--- |
| candidateRevision/hash | Phiên bản và hash nội dung thực đơn canonical; chỉnh bất kỳ món/ngày làm mất hiệu lực evidence cũ |
| sourceVersions | Các phiên bản món/công thức/quy tắc/nguồn dinh dưỡng; không bí mật hoặc costInputVersions cho khách |
| CHECKED | Nháp đạt quy tắc cứng theo evidence; không phải Gia Phát duyệt hoặc đã công bố |
| proposalReceipt | Bằng chứng ghi bền vững đề xuất; không là chứng cứ CRM/đơn hàng/duyệt |
| admission reservation | Giữ ngân sách AI trước phát sinh chi phí; chỉ hệ thống tin cậy quản lý |
| UNKNOWN usage | Chưa biết chi phí; không bằng0, không tự hoàn ngân sách |
| groupRef | Nhóm người dùng theo policy được duyệt; không suy từ role client/địa chỉ IP |
| public projection | Tập trường cho phép, lọc trước model và trước UI; không entity/JSON nguyên bảng |

ID, ngày, decimal và nullability theo DTO; field chưa có nguồn giữ BLOCKED, không điền số synthetic vào nguồn thật. Không sửa DBML65 bảng; không tạo bản sao schema giả vờ đã tích hợp delta.
