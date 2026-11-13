---
id: DOC-E8-USECASES-UC-PUB-008-MD
title: "UC-PUB-008: Theo dõi điểm nối lead"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-PUB-008: Theo dõi điểm nối lead

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

FR: FR-PUB-RELY-001 · FEAT-058 · P0 · US-PUB-008.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH khi được cấp quyền xử lý lead. Bên quan tâm: khách cần yêu cầu không thất lạc; Gia Phát cần phân biệt đã lưu và đã bàn giao.

Trigger: CSKH rà một yêu cầu tư vấn để biết nơi nhận đã xác nhận bàn giao hay còn chờ.

Tiền điều kiện (nghiệp vụ): Có leadRef của bản ghi được tiếp nhận; người tra cứu có phiên và quyền đọc lead.
Tiền điều kiện (gate còn mở): E8-Q06/07/11 chưa chốt nơi nhận, thông báo và vận hành; không tự cấp quyền cho vai trò CSKH hoặc mở CRM E10.

Luồng chính:
1. CSKH chọn leadRef tại UI-PUB-08 để tra tình trạng bàn giao.
2. Hệ thống kiểm phiên, quyền đọc lead và phạm vi bản ghi.
3. Hệ thống đọc trạng thái bàn giao đã có cùng source/trialRef và receiptRef nếu bên nhận đã phản hồi.
4. Hệ thống phân biệt bản ghi đã lưu nhưng chưa receipt với trạng thái có receipt; lỗi bên nhận được hiển thị riêng.
5. Hệ thống trả tình trạng chờ bàn giao, lỗi hoặc đã có receipt để CSKH theo dõi; GET không gửi thông báo hay thực hiện bàn giao.

Hậu điều kiện thành công: CSKH biết tình trạng có căn cứ; bản ghi và nguồn lead giữ nguyên.
Bảo đảm tối thiểu: Không biến đã lưu thành đã vào CRM, không mở hồ sơ/phễu E10 và không làm mất lead vì bên nhận không khả dụng.

Extensions:
- 2a. Phiên hết hạn hoặc thiếu quyền: hệ thống trả ERR-PUB-401-01/ERR-PUB-403-01 tương ứng; không trả thông tin lead, dữ liệu không đổi.
- 2b. Lead không tồn tại hoặc ngoài scope: hệ thống trả ERR-PUB-404-01; không lộ thông tin liên hệ.
- 3a. Chưa có receipt hoặc CRM không khả dụng: hệ thống hiển thị chờ E10/lỗi theo trạng thái đã lưu; lead và source/trialRef còn nguyên, không báo đã đồng bộ.
- 3b. Policy phụ thuộc chưa đủ: hệ thống hiển thị BLOCKED E8-Q06/07/11 với ERR-PUB-422-02 cho nhánh chưa thể xử lý; không tự bàn giao.
- 5a. Không đọc được dịch vụ: hệ thống trả ERR-PUB-503-01 và requestId an toàn; dữ liệu lead không bị sửa.

[API](../api/api-spec.md) API-PUB-008; [AC](../userstories/acceptance-criteria.md); [test](../test/test-cases.md).
