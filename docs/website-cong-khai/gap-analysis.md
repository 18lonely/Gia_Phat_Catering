---
id: DOC-E8-GAP-ANALYSIS
title: Rà khoảng trống E8
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, website]
depends_on: [DOC-E8-SRS-SPEC-MD, DOC-E8-SRS-STATES-MD, DOC-E8-SRS-DATA-DICTIONARY-MD, DOC-E8-API-API-SPEC-MD, DOC-E8-REVIEW-QUESTIONS-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E8: Website công khai

Draft · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 12 FR, 12 UC, 16 API, 3 state, delta dữ liệu, 9 màn hình |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [delta dữ liệu](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md).
- **Cách rà:** tìm dữ liệu được đọc nhưng không có luồng tạo, trạng thái không có API chuyển, và yêu cầu pháp lý hoặc vận hành chưa có FR.
- **Không làm:** không trả lời E8-Q01 đến E8-Q13, không thêm FR hoặc API, không chọn CMS hay nhà cung cấp.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E8-01` | Thiếu chức năng | FEAT-056; `pub_sample_projections`, `pub_price_permissions` | Khách đọc thực đơn mẫu, nhưng không có FR, UC hay API để chọn tuần nào thành mẫu công khai, nhập và duyệt giá công khai, hoặc thu hồi mẫu. FR-PUB-EDIT chỉ phủ trang, bài, banner | High | Đề xuất câu hỏi mới: ai chọn và duyệt mẫu công khai; sau khi có E8-Q03/04 thì bổ sung FR quản trị mẫu |
| `GAP-E8-02` | Pháp lý / riêng tư | FEAT-058; NFR-PUB-006 | Không có luồng cho khách yêu cầu xem, sửa hoặc xóa thông tin đã gửi qua form; chỉ có "thời hạn lưu, xóa chờ E8-Q06" | High | Gom vào E8-Q06; cần người phụ trách pháp lý xác nhận nghĩa vụ trước khi viết FR |
| `GAP-E8-03` | Quy tắc chéo | State nội dung và state URL | Thu hồi một bài đang là đích của mapping Active sẽ làm 301 trỏ tới trang không công khai; chưa có quy tắc chặn hoặc cảnh báo khi thu hồi | High | Đề xuất bổ sung BR khi trả lời E8-Q02: kiểm mapping trước khi thu hồi |
| `GAP-E8-04` | Thiếu API | State URL; API-PUB-003 | State có Verified, Active, Disabled (rollback), nhưng chỉ có POST tạo mapping; không có endpoint kích hoạt cutover hay rollback | Medium | Bổ sung API sau khi E8-Q02, E8-Q11 chốt người duyệt cutover |
| `GAP-E8-05` | Thiếu chức năng | State lead; FR-PUB-RELY-001 | HandoffBlocked và RetryReview có trong state, nhưng FR-PUB-RELY chỉ đọc; không có thao tác cho người xử lý gửi lại hay đánh dấu xử lý tay | Medium | Gom vào E8-Q07; không thêm thao tác ghi trước khi có contract E10 |
| `GAP-E8-06` | SEO | FEAT-055; NFR-PUB-008 | DTO có `canonicalPath` nhưng chưa có FR cho sitemap, robots, thẻ meta; BO-09 (giữ 90% lưu lượng organic) phụ thuộc các mục này | Medium | Đề xuất bổ sung FR kỹ thuật SEO khi chọn CMS (E8-Q08, E8-Q11) |
| `GAP-E8-07` | Pháp lý / đo lường | NFR-PUB-006, 008 | Đo BO-09 cần công cụ analytics; chưa có yêu cầu về banner đồng ý cookie hay cách thu thập không định danh | Medium | Gom vào E8-Q10 cùng câu hỏi pháp lý ở GAP-E8-02 |
| `GAP-E8-08` | Dữ liệu | `pub_url_mappings`, `pub_lead_handoffs` | Hai bảng chưa có khóa chính rõ ràng trong từ điển; ERD chưa đánh dấu PK | Low | Bổ sung khi review kỹ thuật E8-Q12 |
| `GAP-E8-09` | Kiểm thử | test/ | Chưa có ca nghiệm thu mức release `r8-acceptance.md` như E9 đến E13 | Low | Bổ sung khi có inventory DL-08 thật để đo 100% URL |
| `GAP-E8-10` | Dữ liệu thật | NFR-PUB-003; R8 | Chưa có inventory WordPress và baseline lưu lượng; mọi kiểm URL hiện chỉ trên synthetic | High | Giữ BLOCKED E8-Q01, E8-Q10; không dùng synthetic thay bằng chứng |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại delta đã có |

## 4. Giữ nguyên

E8-Q01 đến E8-Q13 giữ CHỜ TRẢ LỜI, cột trả lời trống. Các câu đề xuất mới ở GAP-E8-01 và GAP-E8-02 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không backend, migration hay UAT.
