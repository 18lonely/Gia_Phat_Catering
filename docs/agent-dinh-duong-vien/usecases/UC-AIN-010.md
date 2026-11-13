---
id: DOC-E9-USECASES-UC-AIN-010-MD
title: "UC-AIN-010: Xem và đề nghị đổi hạn mức"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-010: Xem và đề nghị đổi hạn mức

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Giám đốc (PER-08) có quyền quản trị hạn mức được cấp. Bên quan tâm: người dùng cần áp đúng policy, Gia Phát cần kiểm soát thay đổi ngân sách.
Truy vết: FR-AIN-CONF-001 / FEAT-064 / US-AIN-010.

Trigger: Giám đốc cần điều chỉnh hạn mức của một nhóm sau khi rà chính sách sử dụng và ngân sách AI.

Tiền điều kiện (nghiệp vụ): Có phiên/quyền quản trị, group và policyVersion để đối chiếu; các giá trị đề nghị có căn cứ, không dùng số mặc định.
Tiền điều kiện (gate còn mở): E9-Q07, E9-Q08, E9-Q13 chưa chốt hạn mức, quyền/duyệt/hiệu lực và contract. O-03 không mở qua cấu hình hạn mức.

Luồng chính:
1. Giám đốc xem nhóm và policyVersion tại UI-AIN-05, cùng đơn vị và thời gian áp dụng được phép đọc.
2. Giám đốc đề nghị giới hạn lượt, cửa sổ đếm, cap ngày, đơn vị/múi giờ, hiệu lực và lý do thay đổi.
3. Hệ thống kiểm quyền server, version hiện tại và các giá trị theo policy đã được duyệt.
4. Hệ thống đối chiếu đề nghị với spent/reserved hiện có, không hồi tố xóa chi phí hoặc reservation.
5. Nếu policy yêu cầu duyệt, hệ thống tạo đề nghị và tách người tạo/sửa cuối khỏi người duyệt theo E1; nếu không, áp dụng theo workflow đã được xác nhận.
6. Hệ thống lưu audit trước/sau/lý do/version và trả cấu hình hoặc đề nghị cùng trạng thái hiệu lực.

Hậu điều kiện thành công: Thay đổi có dấu vết và chỉ hiệu lực theo workflow được duyệt; không tự chọn số lượt/cap.
Bảo đảm tối thiểu: Persona Giám đốc không tự là quyền runtime; chưa có cơ chế duyệt thì không kích hoạt, không sửa debt lịch sử.

Extensions:
- 3a. Thiếu quyền: hệ thống trả ERR-AIN-403-01; cấu hình/quota chưa đổi.
- 3b. Chưa quyết định policy/duyệt: hệ thống trả ERR-AIN-503-01 và giữ BLOCKED E9-Q07/E9-Q08/E9-Q13; không kích hoạt cấu hình.
- 3c. Version cũ: hệ thống trả ERR-AIN-409-01 để tải lại; không ghi đè policy mới.
- 4a. Cap đề nghị thấp hơn spent + reserved: khi thay đổi có hiệu lực hợp lệ, hệ thống chặn admission mới và báo quản trị; không hủy debt, giả hoàn tiền hoặc sửa quá khứ.
- 6a. Lỗi ghi/audit hoặc mất phản hồi: hệ thống báo ERR-AIN-500-01, yêu cầu đối soát; chưa xác định thay đổi đã lưu, không báo tăng quota thành công.

## Giao tiếp và kiểm

API-AIN-010: PUT /v1/nutrition-agent/admin/limits/{group}; UI-AIN-05. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
