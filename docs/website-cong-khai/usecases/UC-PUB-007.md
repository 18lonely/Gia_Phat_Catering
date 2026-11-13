---
id: DOC-E8-USECASES-UC-PUB-007-MD
title: "UC-PUB-007: Gửi form tư vấn"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-007: Gửi form tư vấn

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-LEAD-001 · FEAT-058 · P0 · US-PUB-007.

Level: Sea level. Actor chính: Khách vãng lai cần tư vấn suất ăn. Bên quan tâm: Gia Phát cần yêu cầu có nguồn và consent; khách cần biết yêu cầu đã được tiếp nhận hay chưa.

Trigger: Sau khi tìm hiểu dịch vụ hoặc xem mẫu thử, khách gửi nhu cầu để Gia Phát liên hệ tư vấn.

Tiền điều kiện (nghiệp vụ): Có form và nội dung consent để khách đọc; trialRef chỉ có khi khách thực sự đã dựng mẫu.
Tiền điều kiện (gate còn mở): E8-Q06/07 chưa chốt trường bắt buộc, nơi lưu, consent, chống spam và thông báo. Không giả nơi nhận CRM đã sẵn sàng.

Luồng chính:
1. Khách nhập thông tin liên hệ tối thiểu tại UI-PUB-05, đọc nội dung consent và thể hiện đồng ý theo bản được duyệt.
2. Hệ thống nhận thông tin, consent/version, nguồn và trialRef nếu có; kiểm trường bắt buộc và dữ liệu được phép.
3. Hệ thống đối chiếu provenance nguồn, tính hợp lệ của trialRef và điều kiện lưu/chống spam đã được phê duyệt.
4. Hệ thống lưu bền vững yêu cầu tư vấn kèm nguồn, consent và tham chiếu mẫu hợp lệ; không dùng customers/eaters làm nơi lưu mặc định.
5. Chỉ sau khi xác định bản ghi đã lưu, hệ thống trả mã tiếp nhận an toàn cho khách; không báo CRM đã nhận thay cho receipt bàn giao.

Hậu điều kiện thành công: Yêu cầu tư vấn có bản ghi bền vững và nguồn; khách nhận mã tiếp nhận, trạng thái CRM được phân biệt.
Bảo đảm tối thiểu: Không có consent thì không ghi lead; không lưu hồ sơ sức khỏe, không bịa trialRef hoặc lộ thông tin liên hệ trong URL/log.

Extensions:
- 2a. Thiếu consent hoặc trường bắt buộc: hệ thống trả ERR-PUB-422-01 và chỉ rõ trường cần sửa; chưa tạo lead.
- 3a. Chưa chọn nơi lưu/policy: hệ thống trả ERR-PUB-422-02 và BLOCKED E8-Q06/07; không giả đã tiếp nhận.
- 3b. Vượt giới hạn chống spam đã duyệt: hệ thống trả ERR-PUB-429-01; không tự retry tạo yêu cầu mới.
- 4a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống trả thông báo chưa xác nhận hoàn tất theo ERR-PUB-500-01 và giữ mã yêu cầu để đối soát; trạng thái lưu chưa rõ, không gửi lại bằng định danh mới.
- 5a. Thông báo hoặc bên nhận CRM lỗi sau khi lưu: hệ thống giữ bản ghi/nguồn đã có; không dùng lỗi thông báo để phủ nhận việc lưu hoặc báo đã bàn giao.

[API](../api/api-spec.md) API-PUB-007; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
