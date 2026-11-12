---
id: DOC-E7-USECASES-UC-FIN-008-MD
title: UC-FIN-008 — Ghi nhận thống nhất đối soát
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-008 — Ghi nhận thống nhất đối soát

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-AGRE-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-05.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Actor hỗ trợ: Người đặt tổng kiêm đại diện khách xác nhận đối soát. Bên quan tâm: hai phía cần thống nhất cùng một bản số liệu.

Trigger: Kế toán nhận bằng chứng khách thống nhất biên bản của kỳ đối soát.

Tiền điều kiện — nghiệp vụ: Có kỳ để đối soát và bằng chứng khách gắn với tập nguồn/revision; kế toán có quyền ghi nhận.
Tiền điều kiện — gate còn mở: E7-Q05, Q-13 và E6-CG-01/08 chưa chốt điều kiện thống nhất, xác minh khách và nguồn.

Luồng chính:
1. Kế toán chọn periodId tại UI-E7-05; hệ thống hiển thị tổng, version và các nguồn của kỳ.
2. Kế toán cung cấp agreementEvidenceRef và version tương ứng với biên bản khách đã xác nhận.
3. Hệ thống kiểm phiên/quyền trên kỳ và điều kiện xác minh đại diện khách, đối chiếu version đang gửi với nguồn kỳ.
4. Hệ thống đối chiếu tổng biên bản, revision và các dòng chênh lệch còn chưa thống nhất.
5. Khi đủ điều kiện, hệ thống lưu bằng chứng cùng revision, ghi trạng thái kỳ thống nhất và dấu vết thao tác.
6. Hệ thống trả kỳ thống nhất tại UI-E7-05; số đã thu vẫn giữ nguyên.

Hậu điều kiện thành công: Kỳ được ghi nhận thống nhất với bằng chứng đúng bản nguồn; không phát sinh khoản thu.
Bảo đảm tối thiểu: Không dùng bằng chứng của revision cũ cho bản mới; lỗi không ghi một phần và không sửa E6/kỳ khóa.

Extensions:
- 4a. Tổng biên bản khác tổng kỳ hoặc còn chênh chưa thống nhất: hệ thống trả ERR-FIN-422-02; kỳ giữ chưa thống nhất.
- 3a. Nguồn kỳ đã thay khi khách xác nhận: hệ thống trả ERR-E7-409-01 và yêu cầu đối chiếu lại; bằng chứng cũ không áp cho bản mới.
- 3b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; trạng thái kỳ không đổi.
- 3c. Chưa đủ nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; chưa ghi thống nhất.
- 5a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; kế toán đối chiếu kỳ và bằng chứng trước lệnh mới. Chưa xác định đã lưu hay chưa, replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-008-1, AC-E7-008-2, AC-E7-008-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
