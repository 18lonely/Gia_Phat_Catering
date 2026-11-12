---
id: DOC-E7-USECASES-UC-DLV-003-MD
title: UC-DLV-003 — Lập biên bản chênh lệch
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-DLV-003 — Lập biên bản chênh lệch

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-DLV-DIFF-001 · FEAT-050 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-03.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH được cấp quyền xử lý giao nhận. Bên quan tâm: khách và bếp cần giữ bằng chứng hai phía; kế toán cần căn cứ xử lý phần lệch.

Trigger: Dinh dưỡng viên nhận phản ánh số suất nhận khác số giao trên phiếu.

Tiền điều kiện — nghiệp vụ: Có phiếu giao để tham chiếu; người lập có quyền tại khách/cơ sở liên quan.
Tiền điều kiện — gate còn mở: E7-Q02 và E6-CG-08 chặn phần chưa có quyền/quy trình và nguồn được xác nhận.

Luồng chính:
1. Dinh dưỡng viên chọn deliveryId tại UI-E7-03 và xem số giao, số nhận cùng bằng chứng nguồn.
2. Dinh dưỡng viên nhập mô tả sự việc, tham chiếu số giao/nhận và evidenceRef của hai phía.
3. Hệ thống kiểm phiên, quyền xử lý phiếu, phạm vi khách/cơ sở và khả năng sử dụng nguồn.
4. Hệ thống đối chiếu các số tham chiếu với phiếu; khi có đủ số nhận, hệ thống xác định phần chênh giao/nhận.
5. Hệ thống kiểm tác động tới kỳ khóa rồi ghi biên bản có version, bằng chứng và liên kết phiếu gốc.
6. Hệ thống trả biên bản để dinh dưỡng viên rà lại; biên bản chưa tự làm giảm tiền phải trả.

Hậu điều kiện thành công: Biên bản lưu chênh lệch có căn cứ và truy được phiếu nguồn; chưa tự chọn phương án xử lý.
Bảo đảm tối thiểu: Hệ thống giữ riêng bằng chứng hai phía, không điền số nhận thiếu bằng 0; không ghi một phần hay sửa E6/kỳ khóa.

Extensions:
- 4a. Thiếu bằng chứng nhận khi kết luận đã thống nhất: hệ thống trả ERR-DLV-422-02 và giữ nháp; thiếu số nhận thì chênh lệch vẫn chưa xác định.
- 5a. Thay đổi số ảnh hưởng kỳ đã khóa: hệ thống trả ERR-FIN-409-02, yêu cầu mở lại hợp lệ; số liệu kỳ và phiếu chưa bị sửa.
- 3a. Hết phiên hoặc thiếu quyền: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-403-01 tương ứng; không ghi biên bản mới.
- 3b. Phiếu ngoài scope: hệ thống trả ERR-E7-404-01; không lộ phiếu và không ghi thay đổi.
- 3c. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; không kết luận chênh lệch đã thống nhất.
- 5b. Mất phản hồi khi ghi: hệ thống báo kết quả chưa rõ; dinh dưỡng viên đối chiếu biên bản/version trước lệnh mới, không kết luận chưa lưu. Replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-003-1, AC-E7-003-2, AC-E7-003-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
