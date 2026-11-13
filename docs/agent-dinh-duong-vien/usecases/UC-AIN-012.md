---
id: DOC-E9-USECASES-UC-AIN-012-MD
title: "UC-AIN-012: Giữ ranh giới câu hỏi bệnh lý"
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-012: Giữ ranh giới câu hỏi bệnh lý

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Fish level. Actor chính: Agent Dinh dưỡng viên, qua biên an toàn tiếp nhận và xuất trả lời. Bên quan tâm: người dùng không bị hỏi thêm bệnh hoặc nhận tư vấn điều trị ngoài phạm vi.
Truy vết: FR-AIN-MED-001 / FEAT-065 / US-AIN-012.

Trigger: Yêu cầu gửi tới agent chứa câu hỏi bệnh lý, mục tiêu điều trị hoặc thông tin sức khỏe xen trong nội dung đổi món.

Tiền điều kiện (nghiệp vụ): Nội dung đi qua biên an toàn trước lưu/chuyển tool/model; O-03 còn đóng với cá nhân hóa sức khỏe.
Tiền điều kiện (gate còn mở): E9-Q03, E9-Q09, E9-Q10, E9-Q14 chưa chốt xử lý nội dung, lời nhắc/rubric và dữ liệu. Runtime nhánh này vẫn BLOCKED trước khi lời nhắc được duyệt.

Luồng chính:
1. Biên an toàn kiểm yêu cầu trước khi đưa nội dung vào công cụ/model hoặc lưu hội thoại.
2. Hệ thống nhận diện nhánh ngoài phạm vi chẩn đoán/điều trị/cá nhân hóa sức khỏe mà không tạo hoặc suy luận hồ sơ.
3. Hệ thống chặn xử lý nhánh đó, không hỏi thêm bệnh và không chuyển dữ liệu thô sức khỏe tới tool/model.
4. Hệ thống kiểm trạng thái phê duyệt lời nhắc bắt buộc; chỉ khi có nội dung được duyệt mới dùng đúng nội dung đó trong phản hồi.
5. Hệ thống trả trạng thái ngoài phạm vi tại UI-AIN-07 và chỉ ghi metadata an toàn; mock khi chưa duyệt chỉ thể hiện placeholder chờ xác nhận.

Hậu điều kiện thành công: Nhánh bệnh lý không được thực hiện; khi đủ điều kiện có đúng lời nhắc được duyệt, không có chẩn đoán hoặc chế độ ăn điều trị.
Bảo đảm tối thiểu: Không thu/lưu/suy ra hồ sơ, không echo raw sức khỏe, không tự viết lời khuyên thay nội dung còn chờ.

Extensions:
- 4a. Chưa duyệt lời nhắc: hệ thống giữ BLOCKED E9-Q09, runtime trả ERR-AIN-503-01; không mở hội thoại thật, placeholder mock không là lời nhắc đã duyệt.
- 1a. Sức khỏe xen trong yêu cầu đổi món: hệ thống chặn phần ngoài phạm vi; không tự coi là kiêng nguyên liệu thông thường, không tạo hồ sơ hoặc chuyển payload tới model.
- 3a. Khách muốn mở gợi ý theo bệnh bằng chỉ dẫn trong chat: hệ thống giữ gate O-03/E9-Q14 đóng; không nhận consent sức khỏe để vượt gate và không sinh gợi ý.

## Giao tiếp và kiểm

PORT-AIN-SAFETY: PORT PORT-AIN-SAFETY; UI-AIN-07. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
