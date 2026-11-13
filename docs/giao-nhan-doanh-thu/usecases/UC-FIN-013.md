---
id: DOC-E7-USECASES-UC-FIN-013-MD
title: "UC-FIN-013: Chuẩn bị và yêu cầu xuất MISA"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-013: Chuẩn bị và yêu cầu xuất MISA

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-MISA-001 · FEAT-053 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-08.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: kế toán cần file đúng mẫu nhập MISA và truy được kỳ nguồn.

Trigger: Kế toán cần chuyển số liệu kỳ đối soát sang MISA theo mẫu nhập đã được xác nhận.

Tiền điều kiện (nghiệp vụ): Có kỳ/revision để xuất và quyền xuất của kế toán; mẫu nhập cùng mapping phải được xác nhận trước khi có file.
Tiền điều kiện (gate còn mở): E7-Q07/08 về mẫu, mapping và hợp đồng xuất; E7-Q05 về kỳ được phép xuất. Hiện chưa có căn cứ tạo cột hoặc thử nhập thực tế.

Luồng chính:
1. Kế toán chọn periodId và revision tại UI-E7-08 để rà nguồn kỳ.
2. Kế toán tham chiếu templateRef của mẫu nhập và mapping được duyệt, gửi yêu cầu xuất.
3. Hệ thống kiểm phiên, quyền xuất, phạm vi và điều kiện kỳ được phép xuất theo policy.
4. Hệ thống kiểm revision nguồn, mẫu nhập và mapping; không tự suy định dạng file, tài khoản hay mã thuế.
5. Khi đủ điều kiện, hệ thống ghi yêu cầu xuất cùng nguồn, trạng thái và dấu vết; chỉ tạo file theo mapping đã duyệt.
6. Hệ thống trả trạng thái/lỗi và fileRef khi thực sự có file để kế toán theo dõi; có file chưa chứng minh nhập MISA thành công.

Hậu điều kiện thành công: Yêu cầu xuất truy được revision và mẫu nhập; file chỉ tồn tại khi đủ căn cứ, không làm tăng số đã thu.
Bảo đảm tối thiểu: Thiếu mẫu không tạo file giả; không sửa E6, snapshot kỳ hay bytes file cũ. Lỗi không được báo thành công một phần.

Extensions:
- 4a. Chưa có mẫu/mapping chính thức: hệ thống trả ERR-FIN-422-04, chặn xuất; không có file hoặc cột tự tạo.
- 6a. Kỳ đã mở lại sau lần xuất trước: hệ thống hiển thị revision cũ và yêu cầu rà lại; file cũ giữ nguyên bytes, không coi là bản hiện hành.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; không tạo yêu cầu xuất hợp lệ.
- 3b. Thiếu nguồn/policy: hệ thống trả ERR-E7-503-01 kèm gate; xuất vẫn bị chặn.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả; kế toán tra yêu cầu xuất/version trước lệnh mới. Chưa xác định đã tạo hay chưa; replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-013-1, AC-E7-013-2, AC-E7-013-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
