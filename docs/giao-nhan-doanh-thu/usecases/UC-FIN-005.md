---
id: DOC-E7-USECASES-UC-FIN-005-MD
title: UC-FIN-005 — Tính doanh thu từ số tính tiền
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-005 — Tính doanh thu từ số tính tiền

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-REV-001 · FEAT-051 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-04.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: khách cần số phải trả đúng căn cứ; kế toán cần truy giá và thuế của đơn.

Trigger: Kế toán có căn cứ số suất tính tiền của đơn giao và cần lập bản tính doanh thu để đối soát.

Tiền điều kiện — nghiệp vụ: Có order revision, giá chụp và bằng chứng số tính tiền; kế toán có quyền tại khách tương ứng.
Tiền điều kiện — gate còn mở: E7-Q03/04, Q-13, E6-CG-04/05/07 chưa chốt căn cứ/nguồn và cách xử lý thuế, làm tròn. Luồng thành công chỉ có điều kiện.

Luồng chính:
1. Kế toán chọn đơn tại UI-E7-04 và tham chiếu orderRevisionRef, pricingSnapshotId.
2. Kế toán cung cấp billableServings và basisEvidenceRef, không mặc định số giao hoặc số nhận là số tính tiền.
3. Hệ thống kiểm phiên, quyền trên khách và nguồn giá/số tính tiền, đối chiếu snapshot với đúng order/version.
4. Hệ thống kiểm context VAT, căn cứ số tính tiền và các gate trước khi xác định các khoản tiền.
5. Hệ thống tính phải trả từ số tính tiền nhân giá chụp, trình bày riêng VAT/doanh thu chưa VAT và CK theo đơn; CK không giảm phải trả.
6. Hệ thống lưu bản tính nháp kèm nguồn, dấu vết và trả kết quả để kế toán kiểm tra tại UI-E7-04.

Hậu điều kiện thành công: Bản tính nháp truy được căn cứ số tính tiền và giá chụp; các khoản phải trả, VAT và CK được phân biệt.
Bảo đảm tối thiểu: Thiếu căn cứ thì doanh thu chưa xác định, không bằng 0. Cờ không yêu cầu hóa đơn không là VAT 0%; cost gồm VAT phải trả nhà cung cấp. Lỗi không ghi một phần, không sửa E6 hoặc kỳ khóa.

Extensions:
- 4a. Context giá UNKNOWN hoặc số tính tiền không có căn cứ: hệ thống trả ERR-FIN-422-01; bản tính chưa được coi là xác định, không điền 0.
- 3a. Giá hiện tại đã đổi sau order: hệ thống tiếp tục dùng giá chụp của order; giá sống không thay snapshot. Ví dụ synthetic giá sống 42000, giá chụp 40000 thì bản tính vẫn dùng 40000.
- 3b. Hết phiên, thiếu quyền hoặc ngoài scope: hệ thống trả ERR-E7-401-01, ERR-E7-403-01 hoặc ERR-E7-404-01 tương ứng; không tạo bản tính hay lộ nguồn ngoài phạm vi.
- 3c. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; chưa xác định doanh thu.
- 6a. Mất phản hồi ghi: hệ thống báo chưa rõ kết quả; kế toán đối chiếu bản tính/version trước lệnh mới. Chưa xác định đã lưu hay chưa; replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-005-1, AC-E7-005-2, AC-E7-005-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
