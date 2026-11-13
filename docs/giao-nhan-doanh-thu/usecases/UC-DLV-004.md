---
id: DOC-E7-USECASES-UC-DLV-004-MD
title: "UC-DLV-004: Ghi thỏa thuận xử lý chênh lệch"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-DLV-004: Ghi thỏa thuận xử lý chênh lệch

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-DLV-RES-001 · FEAT-050 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-03.

Level: Sea level. Actor chính: Dinh dưỡng viên kiêm CSKH được cấp quyền vận hành giao nhận. Bên quan tâm: khách cần thực hiện đúng thỏa thuận; kế toán cần tách giao bù, giảm trừ và chiết khấu.

Trigger: Khách và Gia Phát có thỏa thuận xử lý phần chênh lệch đã ghi trên biên bản.

Tiền điều kiện (nghiệp vụ): Biên bản chênh lệch và phiếu gốc tồn tại; người ghi có quyền xử lý, có bằng chứng thỏa thuận hai phía.
Tiền điều kiện (gate còn mở): E7-Q02/03; CK-Q07–09 khi liên quan CK. Luồng có điều kiện, chưa chọn cách duyệt hay quy đổi giảm trừ.

Luồng chính:
1. Dinh dưỡng viên chọn discrepancyId tại UI-E7-03 và đối chiếu phần lệch với phiếu giao/nhận gốc.
2. Dinh dưỡng viên nhập phương án giao bù hoặc giảm trừ đã thỏa thuận, evidenceRef và version biên bản.
3. Hệ thống kiểm quyền, phạm vi, version biên bản và các gate áp dụng cho phương án.
4. Hệ thống đối chiếu bằng chứng hai phía và phần thiếu được xử lý, kiểm việc ghi nhận có đếm trùng với xử lý trước hay không.
5. Với giao bù, hệ thống gắn phiếu bù và số bù thực với phiếu gốc; với giảm trừ, hệ thống giữ dòng điều chỉnh riêng theo thỏa thuận có căn cứ.
6. Hệ thống lưu dấu vết và trả thỏa thuận cùng nguồn phục vụ xác định số tính tiền; không tự thay số chốt E6.

Hậu điều kiện thành công: Thỏa thuận truy được biên bản, phiếu gốc và bằng chứng; giao bù và giảm trừ không bị cộng hai lần cho cùng phần thiếu.
Bảo đảm tối thiểu: Không có thỏa thuận hợp lệ thì tiền phải trả chưa đổi; giảm trừ chênh lệch không được coi là CK. Lỗi không ghi một phần hoặc sửa kỳ khóa.

Extensions:
- 4a. Chưa có bằng chứng thỏa thuận: hệ thống trả ERR-DLV-422-02; không áp giảm trừ, phải trả giữ nguyên.
- 4b. Phần thiếu đã giao bù nhưng lại được đề nghị giảm trừ: hệ thống hiển thị BLOCKED E7-Q02; không tự cộng hai cách, giữ xử lý đã có.
- 3a. Hết phiên/thiếu quyền: hệ thống trả ERR-E7-401-01/ERR-E7-403-01 tương ứng; không ghi thỏa thuận.
- 3b. Biên bản ngoài scope: hệ thống trả ERR-E7-404-01; không trả dữ liệu hoặc ghi thay đổi.
- 3c. Thiếu nguồn/policy cho phương án: hệ thống trả ERR-E7-503-01 kèm gate; phần xử lý chưa được áp dụng.
- 6a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; dinh dưỡng viên đối chiếu thỏa thuận/version trước lệnh mới. Chưa kết luận trạng thái lưu, replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-004-1, AC-E7-004-2, AC-E7-004-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
