# Từ điển và delta E9

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-04; E9-Q13 |


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

## Quy ước tài liệu liên epic — XC-04

[Quy ước tham chiếu và phiên bản](../../gia-phat/review/decision-pack/followup-2026-11-13/conventions.md) phân biệt kiểu lưu trữ, token khi sửa và revision nguồn. Đây là đề xuất cách mô tả, không thay contract.

> Chờ E9-Q13 — XC-04. Mapping tên/kiểu wire của từng producer và consumer còn BLOCKED; không ép token opaque thành số hoặc tự lấy bản mới nhất. Căn cứ chi tiết nằm trong quy ước được dẫn ở trên.
