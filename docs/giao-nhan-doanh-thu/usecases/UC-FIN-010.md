---
id: DOC-E7-USECASES-UC-FIN-010-MD
title: "UC-FIN-010: Khóa kỳ đối soát"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-FIN-010: Khóa kỳ đối soát

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-FIN-LOCK-001 · FEAT-052 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-05.

Level: Sea level. Actor chính: Kế toán phụ trách doanh thu. Bên quan tâm: khách và kế toán cần bảo toàn bản đối soát đã thống nhất.

Trigger: Kế toán hoàn tất đối chiếu kỳ và yêu cầu khóa bản số liệu đủ điều kiện.

Tiền điều kiện (nghiệp vụ): Có kỳ đã thống nhất và nguồn quyết định khóa; kế toán có quyền khóa kỳ.
Tiền điều kiện (gate còn mở): E7-Q05 và Q-13 chưa chốt điều kiện khóa, xử lý phiếu khách im lặng; luồng thành công chưa có evidence thực tế.

Luồng chính:
1. Kế toán chọn periodId tại UI-E7-05 và rà tổng, tập nguồn cùng trạng thái thống nhất.
2. Kế toán gửi yêu cầu khóa với version kỳ và nguồn quyết định.
3. Hệ thống kiểm phiên, quyền, phạm vi kỳ và version hiện tại so với lệnh khóa.
4. Hệ thống kiểm nguồn đã đủ và các điều kiện khóa theo policy được duyệt; không bỏ qua dòng chưa xác định.
5. Hệ thống chuyển kỳ sang LOCKED, giữ snapshot và ghi audit của thao tác khóa.
6. Hệ thống trả trạng thái LOCKED; mọi đường ghi ảnh hưởng số liệu kỳ bị chặn cho đến khi có duyệt mở lại hợp lệ.

Hậu điều kiện thành công: Kỳ LOCKED có audit và snapshot bất biến; không chỉ khóa nút trên giao diện.
Bảo đảm tối thiểu: Thiếu điều kiện thì không khóa; lỗi không ghi trạng thái một phần hoặc sửa nguồn E6.

Extensions:
- 4a. Còn nguồn chưa xác định hoặc điều kiện khóa không đạt: hệ thống trả ERR-FIN-422-02; kỳ chưa chuyển sang LOCKED.
- 3a. Hai lệnh khóa cùng version: một lệnh chuyển trạng thái; hệ thống trả ERR-E7-409-01 cho lệnh còn lại, không ghi đè snapshot.
- 3b. Hết phiên/thiếu quyền/ngoài scope: hệ thống trả ERR-E7-401-01/ERR-E7-403-01/ERR-E7-404-01 tương ứng; kỳ giữ trạng thái trước lệnh.
- 4b. Policy/nguồn chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; không tự coi đủ điều kiện khóa.
- 5a. Mất phản hồi: hệ thống báo chưa rõ kết quả; kế toán tra trạng thái/version kỳ trước lệnh mới. Chưa xác định đã khóa hay chưa, replay E7-Q08 BLOCKED.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-010-1, AC-E7-010-2, AC-E7-010-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
