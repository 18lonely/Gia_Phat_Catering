---
id: DOC-E7-USECASES-UC-FIN-006-MD
title: UC-FIN-006 — Tra cứu doanh thu và nguồn
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-006 — Tra cứu doanh thu và nguồn

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-VIEW-001 · FEAT-051 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-04.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: kế toán cần xem tổng cùng mức đầy đủ của nguồn, khách cần dữ liệu đúng phạm vi.

Trigger: Kế toán cần rà doanh thu của một khách trong khoảng ngày trước khi chuẩn bị đối soát.

Tiền điều kiện — nghiệp vụ: Kế toán có phiên và quyền đọc doanh thu; khoảng tra cứu có thể chưa có bản tính nào.
Tiền điều kiện — gate còn mở: E7-Q04/08 và E6-CG-08 còn chặn cách tổng hợp, bộ lọc và nguồn/scope; không coi hợp đồng đã freeze.

Luồng chính:
1. Kế toán nhập customerId, fromDate, toDate và trạng thái cần lọc tại UI-E7-04.
2. Hệ thống kiểm phiên, quyền đọc và phạm vi khách từ nguồn tin cậy.
3. Hệ thống đọc các bản tính đã có phù hợp bộ lọc, lấy nguồn số tính tiền và giá chụp của từng dòng.
4. Hệ thống tách dòng đủ căn cứ khỏi dòng chưa xác định; không cộng dòng thiếu như giá trị 0 vào tổng hoàn tất.
5. Hệ thống trả danh sách, nguồn và tổng có nhãn đủ/thiếu để kế toán đối chiếu; thao tác đọc không tạo bản tính.

Hậu điều kiện thành công: Kế toán nhận đúng tập dữ liệu được phép đọc và biết tổng còn thiếu căn cứ nào.
Bảo đảm tối thiểu: GET không ghi bản tính, không sửa E6 hoặc kỳ khóa và không trả tên khách/tổng ngoài scope.

Extensions:
- 2a. Khách ngoài scope: hệ thống trả ERR-E7-404-01; không lộ tên hay tổng, dữ liệu doanh thu giữ nguyên.
- 3a. Khoảng ngày không có dữ liệu: hệ thống trả danh sách rỗng; không tạo calculation và không biến thiếu dữ liệu thành doanh thu hoàn tất.
- 2b. Hết phiên hoặc thiếu quyền: hệ thống trả ERR-E7-401-01 hoặc ERR-E7-403-01 tương ứng; không trả danh sách và không thay dữ liệu.
- 3b. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; dữ liệu không bị thay đổi.
- 5a. Không nhận được phản hồi tra cứu: giao diện chưa có kết quả để đối chiếu; GET không phát sinh lệnh ghi hay replay nghiệp vụ. Quy ước kỹ thuật E7-Q08 vẫn BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-006-1, AC-E7-006-2, AC-E7-006-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
