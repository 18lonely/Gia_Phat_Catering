---
id: DOC-E8-USECASES-UC-PUB-005-MD
title: "UC-PUB-005: Xem thực đơn mẫu có giá"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-005: Xem thực đơn mẫu có giá

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-MENU-001 · FEAT-056 · P0 · US-PUB-005.

Level: Sea level. Actor chính: Khách vãng lai tìm hiểu suất ăn tập thể. Bên quan tâm: khách cần giá và thông tin món có căn cứ; Gia Phát cần bảo vệ giá nội bộ.

Trigger: Khách xem một thực đơn tuần mẫu để cân nhắc dịch vụ suất ăn.

Tiền điều kiện (nghiệp vụ): Có publicSampleId và ngày hiển thị cần tra cứu; khách không cần tài khoản.
Tiền điều kiện (gate còn mở): E8-Q03/04 về giá được phép công khai và nguồn thực đơn/dinh dưỡng chưa chốt; luồng đủ dữ liệu chỉ có điều kiện.

Luồng chính:
1. Khách chọn mẫu tại UI-PUB-03; hệ thống nhận publicSampleId và ngày hiển thị.
2. Hệ thống tra projection công khai và kiểm quyền hiển thị giá suất theo nguồn được cho phép.
3. Hệ thống đối chiếu menu, recipe và nutrition revision cùng ngày nguồn, kiểm phần thiếu hoặc hết hiệu lực.
4. Hệ thống lấy định lượng theo suất, năng lượng kcal, đạm/béo/bột đường theo g và dị ứng; không lấy price_cap hoặc giá hợp đồng làm giá public.
5. Hệ thống trả tuần mẫu, giá và dữ liệu đủ căn cứ với nhãn “ước tính từ định lượng sống”, kèm nguồn để khách đọc.

Hậu điều kiện thành công: Khách xem mẫu đủ giá được phép, định lượng, 4 chỉ số có đơn vị và dị ứng; không tạo order hoặc sửa nguồn.
Bảo đảm tối thiểu: Thiếu số liệu không thành 0; danh sách dị ứng rỗng chưa chứng minh không dị ứng. Không trả cost, giá nhập hoặc dữ liệu khách nội bộ.

Extensions:
- 2a. Mẫu không tồn tại hoặc không công khai: hệ thống trả ERR-PUB-404-01; không lộ bản nháp, dữ liệu không đổi.
- 3a. Giá chưa được phép, nguồn stale/missing hoặc thiếu policy: hệ thống trả ERR-PUB-422-02 và giữ BLOCKED E8-Q03/04 cho phần phụ thuộc; không báo trang mẫu đã đầy đủ.
- 3b. Revision đổi trong lúc đọc: hệ thống kiểm lại nguồn; không ghép các revision lệch nhau để giả kết quả đủ.
- 5a. Nguồn không khả dụng: hệ thống trả ERR-PUB-503-01; chưa có kết quả mẫu hợp lệ, không ghi dữ liệu nghiệp vụ.

[API](../api/api-spec.md) API-PUB-005; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
