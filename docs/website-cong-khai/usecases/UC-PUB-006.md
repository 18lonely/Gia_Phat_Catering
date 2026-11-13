---
id: DOC-E8-USECASES-UC-PUB-006-MD
title: "UC-PUB-006: Dựng thử thực đơn tuần"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-006: Dựng thử thực đơn tuần

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-TRY-001 · FEAT-057 · P1 · US-PUB-006.

Level: Sea level. Actor chính: Khách vãng lai khảo sát thực đơn tập thể. Bên quan tâm: khách cần mẫu phù hợp nhu cầu; Gia Phát cần phân biệt mẫu thử với đơn hàng.

Trigger: Khách muốn thử một tuần ăn theo loại suất, số suất và nguyên liệu cần kiêng trước khi liên hệ tư vấn.

Tiền điều kiện (nghiệp vụ): Có danh mục loại suất/kiêng nguyên liệu được phép công khai; không sử dụng hồ sơ sức khỏe cá nhân.
Tiền điều kiện (gate còn mở): E8-Q05/04 chưa chốt cách dựng, giới hạn và nguồn; không tự chọn engine hoặc gọi Agent E9.

Luồng chính:
1. Khách chọn loại suất công khai, nhập số suất và lựa chọn kiêng nguyên liệu tại UI-PUB-04.
2. Hệ thống kiểm số suất nguyên dương và đầu vào thuộc tập được phép; không nhận trường bệnh lý/người ăn.
3. Hệ thống kiểm policy dựng thử và nguồn được duyệt trước khi yêu cầu bộ dựng xử lý nhu cầu.
4. Khi đủ điều kiện, bộ dựng trả phương án tuần mẫu theo đầu vào; hệ thống kiểm kết quả theo policy đã có căn cứ, không nới quy tắc cứng.
5. Hệ thống lọc kết quả thành nội dung công khai và trả mẫu có nhãn chưa áp dụng để khách xem.

Hậu điều kiện thành công: Khách nhận tuần mẫu theo đầu vào; mẫu chưa phải đơn đặt hàng, báo giá cam kết hay thực đơn công bố.
Bảo đảm tối thiểu: Không ghi menus/order, không gọi Agent E9, không thu dữ liệu sức khỏe hoặc trả breakdown cost. Quy định lưu/hiệu lực mẫu chưa được tự chọn.

Extensions:
- 2a. Số suất âm, bằng 0 hoặc không nguyên: hệ thống trả ERR-PUB-422-01, yêu cầu sửa; chưa yêu cầu dựng mẫu.
- 3a. Chưa chốt engine/policy hoặc nguồn: hệ thống trả ERR-PUB-422-02, giữ BLOCKED E8-Q05/04; không dựng kết quả giả.
- 4a. Không tìm được phương án: hệ thống trả trạng thái không có phương án; quy tắc cứng giữ nguyên, không tạo order.
- 4b. Dịch vụ dựng không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có mẫu hợp lệ, không báo hoàn tất.
- 5a. Nguồn đổi trước khi trả mẫu: hệ thống kiểm lại revision/nguồn; không trả mẫu phụ thuộc nguồn chưa được phép.

[API](../api/api-spec.md) API-PUB-006; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
