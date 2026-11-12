---
id: DOC-E9-USECASES-UC-AIN-004-MD
title: UC-AIN-004 — Giải thích thực đơn
version: 0.2.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# UC-AIN-004 — Giải thích thực đơn

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

Level: Sea level. Actor chính: Khách vãng lai (PER-01) hoặc người đặt tổng (PER-02). Bên quan tâm: khách cần hiểu phương án dựa trên số liệu hệ thống, không nhận số tự suy đoán.
Truy vết: FR-AIN-EXPL-001 / FEAT-061 / US-AIN-004.

Trigger: Khi xem candidate đã kiểm, khách hỏi về món, định lượng, bảng kiểm công khai hoặc dinh dưỡng của phương án.

Tiền điều kiện — nghiệp vụ: Có candidateRef/revision thuộc phiên và chủ đề giải thích nằm trong allowlist đã duyệt.
Tiền điều kiện — gate còn mở: E9-Q04, E9-Q05, E9-Q12 chưa chốt giá public, phản hồi nhánh kinh tế và nguồn; O-03 vẫn đóng đối với sức khỏe.

Luồng chính:
1. Khách chọn mục cần giải thích tại UI-AIN-02, gửi candidateRef/revision và topic được phép.
2. Hệ thống kiểm quyền sở hữu, revision và evidence của candidate, chặn chủ đề ngoài phạm vi trước khi diễn giải.
3. Hệ thống lấy projection món/định lượng/bảng kiểm public cùng 4 chỉ số từ E4 và provenance tương ứng.
4. Hệ thống chỉ diễn giải các giá trị đã được cung cấp, gắn đơn vị, nguồn và nhãn “ước tính từ định lượng sống”.
5. Hệ thống lọc lời giải thích trước khi trả cho khách; không nêu nguyên nhân cost hoặc đưa giá suất chưa có nguồn được duyệt.

Hậu điều kiện thành công: Lời giải thích bám đúng revision và dữ liệu có nguồn; không tạo hay thay đổi thực đơn chính thức.
Bảo đảm tối thiểu: Model không tự tính cost/định lượng/dinh dưỡng; dữ liệu thiếu khác 0 và dị ứng chưa biết khác không dị ứng.

Extensions:
- 3a. Dinh dưỡng thiếu/stale: hệ thống ghi chưa đủ/cũ và giữ tổng thiếu là null; không bịa số hoặc báo kết quả đầy đủ.
- 2a. Khách yêu cầu suy giá nhập từ giá suất/định lượng: hệ thống từ chối an toàn ERR-AIN-403-01; không gọi tool cấm, không tạo phép suy ngược.
- 2b. Candidate ngoài scope hoặc revision đã đổi: hệ thống trả ERR-AIN-404-01/ERR-AIN-409-01 tương ứng; chưa có giải thích mới hợp lệ.
- 3b. Nguồn/policy chưa sẵn sàng: hệ thống trả ERR-AIN-503-01 kèm gate; không giả kết quả hoặc tự hiển thị giá.

## Giao tiếp và kiểm

API-AIN-004: POST /v1/nutrition-agent/requests/{id}/explanations; UI-AIN-02. [AC](../userstories/acceptance-criteria.md), [test](../test/test-cases.md), [lỗi](../srs/error-matrix.md). Model không trực tiếp gọi control port/quản trị/gửi nháp. Điểm chưa quyết định giữ BLOCKED, không mở rộng producer E6/E8.
