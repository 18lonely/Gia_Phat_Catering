---
id: DOC-E7-USECASES-UC-FIN-012-MD
title: "UC-FIN-012: Duyệt hoặc từ chối mở lại kỳ"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-012: Duyệt hoặc từ chối mở lại kỳ

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-RDEC-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-07.

Level: Sea level. Actor chính: Giám đốc. Bên quan tâm: kế toán cần quyết định để xử lý sai lệch; khách cần giữ bản đối soát khóa và dấu vết thay đổi.

Trigger: Giám đốc nhận đề nghị mở lại kỳ có lý do và bằng chứng từ kế toán.

Tiền điều kiện (nghiệp vụ): Có yêu cầu mở lại chờ quyết định và kỳ khóa; Giám đốc khác người lập/sửa cuối theo BR-SEC-008.
Tiền điều kiện (gate còn mở): E7-Q05 về vòng mở lại; O-06 không tự cấp người thay. Luồng không xác nhận các policy này đã được duyệt.

Luồng chính:
1. Giám đốc xem yêu cầu tại UI-E7-07, gồm lý do, nội dung sửa, bằng chứng và người lập/sửa cuối.
2. Giám đốc chọn approve hoặc reject, nhập reason và gửi requestId, requestVersion, periodVersion.
3. Hệ thống kiểm phiên, vai trò Giám đốc, phạm vi kỳ và điều kiện không tự duyệt theo BR-SEC-008.
4. Hệ thống đối chiếu version yêu cầu/kỳ và trạng thái được phép quyết định theo gate.
5. Với quyết định approve hợp lệ, hệ thống lưu quyết định, chuyển kỳ sang REOPENED và giữ nguyên snapshot khóa cũ.
6. Hệ thống trả quyết định và trạng thái kỳ; việc sửa sau mở phải qua đối soát lại, chưa tự thống nhất số liệu mới.

Hậu điều kiện thành công: Quyết định được lưu; duyệt mở tạo trạng thái REOPENED, còn từ chối giữ LOCKED và snapshot cũ.
Bảo đảm tối thiểu: Không tự cấp quyền duyệt cho Admin/người thay; lỗi không ghi một phần hoặc sửa E6, không xóa snapshot khóa.

Extensions:
- 3a. Người quyết định là người lập/sửa cuối hoặc không phải Giám đốc: hệ thống trả ERR-E7-403-01; kỳ vẫn khóa, không ghi duyệt mở.
- 5a. Giám đốc chọn reject: hệ thống lưu quyết định từ chối và trả kỳ LOCKED; số liệu không đổi.
- 3b. Hết phiên hoặc ngoài scope: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-404-01 tương ứng; quyết định chưa được ghi.
- 4a. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; không tự mở kỳ.
- 5b. Mất phản hồi ghi quyết định: hệ thống báo kết quả chưa rõ; Giám đốc đối chiếu yêu cầu/kỳ trước lệnh mới. Không suy kỳ đã mở hoặc chưa mở; replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-012-1, AC-E7-012-2, AC-E7-012-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
