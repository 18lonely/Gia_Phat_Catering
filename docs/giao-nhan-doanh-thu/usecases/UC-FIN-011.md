---
id: DOC-E7-USECASES-UC-FIN-011-MD
title: "UC-FIN-011: Đề nghị mở lại kỳ"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-011: Đề nghị mở lại kỳ

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-RREQ-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-07.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: Giám đốc cần biết lý do và nội dung sửa; khách cần bản khóa cũ không bị thay trước duyệt.

Trigger: Kế toán phát hiện nội dung cần sửa trong kỳ đối soát đã khóa.

Tiền điều kiện (nghiệp vụ): Kỳ đang LOCKED; kế toán có quyền lập đề nghị và bằng chứng cho nội dung cần sửa.
Tiền điều kiện (gate còn mở): E7-Q05 về mở lại/tái đối soát; O-06 về ủy quyền giữ mở, không tự cấp người duyệt thay.

Luồng chính:
1. Kế toán chọn periodId tại UI-E7-07 và xem snapshot khóa cùng version kỳ.
2. Kế toán nhập lý do, nội dung dự kiến sửa và evidenceRef, gửi kèm version.
3. Hệ thống kiểm phiên, quyền trên kỳ và trạng thái khóa hiện tại.
4. Hệ thống kiểm version, lý do ít nhất 10 ký tự và căn cứ đề nghị theo điều kiện được duyệt.
5. Hệ thống ghi yêu cầu chờ Giám đốc cùng dấu vết, không chuyển kỳ sang mở.
6. Hệ thống trả yêu cầu và trạng thái kỳ vẫn khóa để kế toán theo dõi quyết định.

Hậu điều kiện thành công: Yêu cầu mở lại đang chờ Giám đốc; số liệu và snapshot kỳ chưa thay đổi.
Bảo đảm tối thiểu: Tạo yêu cầu không cấp quyền sửa kỳ; lỗi không lưu yêu cầu một phần và không sửa E6.

Extensions:
- 4a. Lý do dưới 10 ký tự hoặc điều kiện kỳ không hợp lệ: hệ thống trả ERR-FIN-422-02; không lưu đề nghị.
- 6a. Kế toán sửa doanh thu khi đề nghị còn chờ: hệ thống trả ERR-FIN-409-02; kỳ và số liệu vẫn khóa.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không ghi đề nghị mới.
- 4b. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; kỳ không được mở.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả lập đề nghị; kế toán tra yêu cầu/version trước lệnh mới. Kỳ không được coi là đã mở, replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-011-1, AC-E7-011-2, AC-E7-011-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
