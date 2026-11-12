---
id: DOC-E8-TEST-SYSTEM-CASES-MD
title: Ca bảo mật, NFR và bất biến
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Ca bảo mật, NFR và bất biến

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

| TC | BR/NFR | Given / When (chuẩn bị và thao tác) | Then / oracle | Status | Actual | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TC-PUB-S01 | BR-PUB-001/002; NFR-PUB-001 | Gắn sentinel synthetic vào cost, giá nhập, costPct, allowances, discounts và object lồng nhau; gọi tất cả public route/HTML/meta/JSON-LD/cache/error | Không sentinel nội bộ ở bất cứ output nào; chỉ giá suất được phép. Kiểm cả raw bytes và UI. | NOT RUN |  |  |
| TC-PUB-S02 | BR-PUB-001/008/009; NFR-PUB-001 | Khách gọi admin/preview/private media, đoán ID, dùng cache sau phiên admin | 401/403/404 an toàn; không nháp/PII/storage_key; không shared cache riêng tư | NOT RUN |  |  |
| TC-PUB-S03 | BR-PUB-006/007; NFR-PUB-002 | Fault trước/sau commit lead; gửi lại cùng identity; CRM down; notification fail | Không báo thành công trước commit; source nguyên vẹn; không duplicate khi retry; không ACK trước receipt | BLOCKED E8-Q06/07/12 |  |  |
| TC-PUB-S04 | BR-PUB-008/009; NFR-PUB-002 | Hai người sửa cùng version; fault audit/publish; thu hồi khi cache còn bản cũ | 409 stale; không publish sai revision, không thành công thiếu audit; không phục vụ nội dung thu hồi | BLOCKED E8-Q08/12 |  |  |
| TC-PUB-S05 | BR-PUB-004; NFR-PUB-003 | Đối chiếu toàn inventory DL-08: giữ,301,trùng,xóa,slash/query,loop,đích private | Mỗi URL có evidence200 đúng bài hoặc301 đúng đích; missing/ngoại lệ chưa duyệt không coi đạt100% | BLOCKED E8-Q01/02/11 |  |  |
| TC-PUB-S06 | NFR-PUB-004 | Chạy1000CCU theo profile public đã duyệt, cold/hot cache, nguồn down | p95 đọc≤300ms/ghi≤800ms; công bố tỷ lệ lỗi/profile; chưa có runtime không ghi PASS | BLOCKED E8-Q11/12 |  |  |
| TC-PUB-S07 | NFR-PUB-005 | Mở9 màn ở360/390/1440px; tab/focus/labels; trạng thái empty/error/modal | Không tràn toàn trang, đọc được nội dung, modal đóng bằng bàn phím; mock result riêng | NOT RUN |  |  |
| TC-PUB-S08 | BR-PUB-005/006; NFR-PUB-006 | Gửi form thiếu consent, có trường healthProfile, raw referrer có email; xem log/analytics và thử lead ngoài quyền | Không ghi thiếu consent/health; không PII trong URL/log/analytics; không đọc chéo lead; retention chờ policy | NOT RUN |  |  |
| TC-PUB-S09 | BR-PUB-009; NFR-PUB-007 | Chèn script/event handler trong bài, ảnh SVG/script, tên file/path độc hại, CSRF khi dùng cookie | Không thực thi, không phát tán payload/secret; từ chối file ngoài ảnh đã duyệt | NOT RUN |  |  |
| TC-PUB-S10 | BR-PUB-011; NFR-PUB-008 | Chốt baseline và bộ lọc; lấy số organic sau60 ngày cùng định nghĩa; thử baseline thiếu/0 | Tỷ lệ after/before≥90% mới đạt; thiếu/0 giữ chưa xác định, không suy từ số URL | BLOCKED E8-Q10 |  |  |
| TC-PUB-S11 | BR-PUB-003/005 | Dữ liệu thiếu1 chỉ số;0 hợp lệ; allergy=[] chưa rà; stale recipe; trial vô nghiệm | Không hiển thị đủ giả, không kết luận không dị ứng, không nới hard rule hoặc đổi nguồn ngầm | BLOCKED E8-Q04/05 |  |  |
| TC-PUB-S12 | BR-PUB-012 | Đối chiếu E8 projection và nguồn kế toán; thử invoiceRequested=false, discount có giá trị | Không suy VAT0; không giảm giá công khai từ CK; không thay invariant E3; không đưa cost ra public | NOT RUN |  |  |

TC-PUB-S05 cũng kiểm chuyển nội dung: so sourceId/title/body/media/ngày gốc và internal links với bản xuất; chạy lại không nhân đôi bài, source hash thay đổi phải được rà lại; bài nhập vẫn nháp và public không đọc được. Thiếu media/nội dung hoặc sourceId trùng phải hiện ngoại lệ, không bỏ khỏi inventory để báo100%. Liên kết FR-PUB-URLM-001, UC-PUB-003, US-PUB-003, API-PUB-003/016, UI-PUB-06/07; BLOCKED E8-Q01/02/08/09.

12 ca bổ sung có overlap36 ca AC; không cộng thành48 mục tiêu độc lập. Các ca là thiết kế, chưa chạy backend.
