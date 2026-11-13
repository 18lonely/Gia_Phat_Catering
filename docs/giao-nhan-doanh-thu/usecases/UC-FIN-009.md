---
id: DOC-E7-USECASES-UC-FIN-009-MD
title: "UC-FIN-009: Ghi nhận thu tiền"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-009: Ghi nhận thu tiền

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-RCPT-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-06.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: khách cần khoản thanh toán được ghi đúng kỳ; kế toán cần đối chiếu chứng từ và số còn phải thu.

Trigger: Kế toán nhận chứng từ khách thanh toán cho kỳ đối soát.

Tiền điều kiện (nghiệp vụ): Có kỳ và chứng từ thu thuộc khách; kế toán có quyền ghi khoản thu.
Tiền điều kiện (gate còn mở): E7-Q06 về thu một phần/thừa, phân bổ và sửa/hủy; E7-Q05 về thu sau khóa. Chưa mở các nhánh thanh toán nâng cao.

Luồng chính:
1. Kế toán chọn periodId tại UI-E7-06, đối chiếu khách, phải trả và các khoản đã thu.
2. Kế toán nhập số tiền, ngày nhận, chứng từ và version kỳ đang xem.
3. Hệ thống kiểm phiên, quyền trên khách/kỳ, version và điều kiện kỳ được ghi thu.
4. Hệ thống kiểm tiền dương, chứng từ đúng khách/kỳ và việc chứng từ đã được ghi nhận hay chưa.
5. Hệ thống ghi khoản thu cùng dấu vết, giữ tiền phải trả gốc riêng với tổng đã thu và số còn phải thu.
6. Hệ thống trả khoản thu để kế toán đối chiếu chứng từ; không suy khoản thu từ việc kỳ thống nhất hoặc đã xuất MISA.

Hậu điều kiện thành công: Khoản thu truy được chứng từ và kỳ; số đã thu/còn phải thu phản ánh khoản hợp lệ, phải trả gốc không đổi.
Bảo đảm tối thiểu: Lỗi không tạo khoản thu một phần, không ghi trùng chứng từ hay sửa E6/kỳ khóa. Mất phản hồi chưa chứng minh thu chưa được lưu.

Extensions:
- 4a. Tiền không dương hoặc chứng từ sai/trùng: hệ thống trả ERR-FIN-422-03 và yêu cầu đối chiếu; không tạo thêm khoản thu.
- 3a. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; tiền đã thu không đổi.
- 3b. Policy thu hoặc nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; chưa ghi khoản thu theo nhánh bị chặn.
- 5a. Mất phản hồi lệnh thu: hệ thống hiển thị chưa rõ kết quả; kế toán đối chiếu chứng từ và khoản thu trước thao tác mới. Trạng thái lưu chưa xác định, replay BLOCKED E7-Q08.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-009-1, AC-E7-009-2, AC-E7-009-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
