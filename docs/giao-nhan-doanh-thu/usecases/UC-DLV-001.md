---
id: DOC-E7-USECASES-UC-DLV-001-MD
title: "UC-DLV-001: Lập phiếu giao nhận"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-DLV-001: Lập phiếu giao nhận

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

FR: FR-DLV-NOTE-001 · FEAT-049 · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · UI-E7-01.

Level: Sea level. Actor chính: Bếp trưởng hoặc quản lý cơ sở phụ trách giao hàng. Bên quan tâm: người nhận cần đối chiếu số giao; kế toán cần nguồn phiếu để đối soát.

Trigger: Bếp trưởng ghi nhận số suất thực giao của chuyến hàng theo kế hoạch sản xuất.

Tiền điều kiện (nghiệp vụ): Người lập có phiên và quyền tại cơ sở; đơn hàng và bản kế hoạch nguồn tồn tại.
Tiền điều kiện (gate còn mở): E6-CG-05/06/08 và E7-Q02 chưa có quyết định/evidence cho luồng thành công; chỉ mô tả xử lý khi đầu vào được xác nhận hợp lệ.

Luồng chính:
1. Bếp trưởng chọn đơn hàng tại UI-E7-01; hệ thống hiển thị khách, điểm, ngày/ca và số chốt từ nguồn được phép đọc.
2. Bếp trưởng chỉ rõ orderId, orderRevisionRef và planRevisionRef, nhập số giao thực tế và bằng chứng giao.
3. Hệ thống đối chiếu đơn hàng với điểm/khách/cơ sở từ nguồn tin cậy, kiểm quyền lập phiếu và tình trạng các gate nguồn.
4. Hệ thống kiểm số giao nguyên không âm và các revision tham chiếu còn phù hợp, không tự chuyển sang bản nguồn mới.
5. Hệ thống ghi phiếu, bằng chứng và dấu vết người/thời điểm; giữ số chốt và số giao thành hai giá trị riêng.
6. Hệ thống trả phiếu chờ khách xác nhận cùng nguồn tham chiếu để bếp trưởng đối chiếu.

Hậu điều kiện thành công: Phiếu giao tồn tại và chờ khách xác nhận; order E6 giữ nguyên số chốt.
Bảo đảm tối thiểu: Lỗi trước khi ghi không tạo phiếu một phần; không sửa E6 hoặc số liệu kỳ khóa. Mất phản hồi không chứng minh phiếu chưa được lưu.

Extensions:
- 4a. Số giao âm, không nguyên hoặc sai tham chiếu: hệ thống trả ERR-DLV-422-01 và yêu cầu sửa đầu vào; chưa tạo phiếu.
- 4b. Revision đơn hàng đã thay: hệ thống trả ERR-E7-409-01, yêu cầu tải lại để đối chiếu; không chuyển nguồn hoặc ghi đè.
- 3a. Phiên hết hạn: hệ thống trả ERR-E7-401-01, yêu cầu đăng nhập lại; chưa ghi phiếu, không tự gửi lại lệnh.
- 3b. Thiếu quyền hoặc ngoài phạm vi: hệ thống trả ERR-E7-403-01 hoặc ERR-E7-404-01 tương ứng; không trả dữ liệu ngoài phạm vi và không tạo phiếu.
- 3c. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-E7-503-01 kèm gate; phiếu chưa được tạo, không điền số thiếu bằng 0.
- 5a. Mất phản hồi khi lưu: hệ thống hiển thị kết quả chưa rõ; bếp trưởng đối chiếu phiếu/nguồn trước lệnh mới. Trạng thái lưu chưa xác định, replay vẫn BLOCKED E7-Q08.

BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): AC-E7-001-1, AC-E7-001-2, AC-E7-001-3. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.
