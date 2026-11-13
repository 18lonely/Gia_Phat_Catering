---
id: DOC-E8-REVIEW-QUESTIONS-MD
title: Sổ câu hỏi mở E8
version: 0.1.1
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-13
---
# Sổ câu hỏi mở E8

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-05; E8-Q13; XC-08; E8-Q05, E9-Q11 |


Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

Tất cả **CHỜ TRẢ LỜI**. Trả lời và nguồn/người/ngày để trống. Phương án chỉ tham khảo, chưa được chọn; không hỏi lại trong phiên.

| Mã | Câu hỏi | Phương án tham khảo / đánh đổi | Nhánh BLOCKED | Trả lời | Nguồn / người / ngày |
| :--- | :--- | :--- | :--- | :--- | :--- |
| E8-Q01 | DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ? | Xuất inventory có mã bài/URL/status/hash; hoặc crawl đối chiếu bản export, không thay export bằng URL đoán | Mapping thật, mẫu số 100% URL, R8 |  |  |
| E8-Q02 | Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback? | Giữ đường dẫn có thể bảo toàn; 301 tới nội dung tương đương. Bài xóa cần quyết định riêng; 404/410 không tự tính đạt R8 | Kích hoạt redirect, bài xóa/trùng, cutover |  |  |
| E8-Q03 | Giá suất nào được công khai; ai duyệt, thời hạn hiệu lực và cách ghi VAT/giá tham khảo ra sao? | Bản giá công khai riêng được duyệt hoặc tham chiếu giá được cho phép; không lấy price_cap hay giá hợp đồng làm mặc định | Giá FEAT-056, projection giá và hiệu lực |  |  |
| E8-Q04 | Nguồn E2/E4 ở trạng thái nào đủ điều kiện hiển thị định lượng, 4 chỉ số và dị ứng; làm gì khi stale/thu hồi/thiếu? | Tham chiếu menu PUBLISHED, recipe ACTIVE đúng ngày và calculation có provenance; thêm phê duyệt công khai khi cần. NUTR chưa có trạng thái duyệt riêng | Public snapshot/refresh, R4, độ đầy đủ dữ liệu FEAT-056 |  |  |
| E8-Q05 | FEAT-057 sinh mẫu từ thư viện, thuật toán hay cách khác; có phải qua máy kiểm E2; giới hạn loại suất/số suất/kiêng kỵ/ngày/lượt là gì? | Lọc mẫu được duyệt hoặc dựng qua bộ kiểm không lưu E2; chưa chọn. Không nới quy tắc cứng hoặc triển khai Agent E9 | Generation, kiểm quy tắc và giới hạn chính thức |  |  |
| E8-Q06 | Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào? | Kho lead E8 riêng rồi chuyển khi E10 có contract; hoặc đầu nhận hiện hữu được duyệt. Không tự dùng customers/eaters làm lead | Ghi lead thật, retention/xóa, hợp đồng E10 |  |  |
| E8-Q07 | Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao? | Rate limit nền + kiểm trường; bổ sung giải pháp sau review. Thông báo riêng trạng thái lưu lead, không coi gửi thông báo là lưu thành công | Provider chống spam, recipient, notification/retry |  |  |
| E8-Q08 | Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào? | Tách quyền soạn và công bố, có thể thêm duyệt độc lập; hoặc workflow ít bước được xác nhận. Không tự gán PER-05 toàn quyền | Quyền runtime, bước duyệt, CMS/publication |  |  |
| E8-Q09 | Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào? | Tái dùng files nền với metadata public riêng; chỉ loại ảnh trong tập nền, không tự mở SVG; lịch/cỡ chờ xác nhận | Media pipeline, layout/lịch và quyền public asset |  |  |
| E8-Q10 | BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo? | So phiên tự nhiên theo cùng công cụ/định nghĩa và kỳ so sánh tương đương; lưu bằng chứng baseline trước cutover | Đo BO-09, kết luận G-Next; baseline=0/thiếu chưa tính tỷ lệ |  |  |
| E8-Q11 | Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04? | Xác nhận quyền, diễn tập chuyển và rollback rồi mới chọn cửa sổ; không tự chọn nhà cung cấp hoặc ngày | R8 start/cutover; đưa 054/055/059 lên Now |  |  |
| E8-Q12 | Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì? | Kế thừa nền khi tương thích; E4 dùng cursor/envelope khác nên adapter cần review, không tự freeze TTL/retry | Wire contract, cache/CDN, tải và fault tolerance |  |  |
| E8-Q13 | Nguồn nào giữ bản chủ của một lead/proposal qua E8, E9, E10; khóa liên kết và bằng chứng đồng ý nào được giữ khi bàn giao hoặc nhận lại? | Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. | BLOCKED xác nhận liên kết bản chủ và chống nhận trùng xuyên ba epic. XC-05; DEC-200. Đối chiếu khóa nguồn và receipt trong delta; giữ từng vòng đời, chưa gộp bảng. |  |  |

> Chờ E8-Q05, E9-Q11: XC-08. Phần phụ thuộc BLOCKED; giữ nguyên các nhánh chưa có quyết định. Căn cứ: [XC-08](../../gia-phat/review/decision-pack/cross-epic-consistency.md) và câu nguồn được dẫn; không coi đề xuất là xác nhận.

Chỉ đồng bộ khi có nguồn quyết định và phạm vi áp dụng, không tự đóng từ kiểm tài liệu. [Phụ thuộc](dependencies.md). E6/E7 giữ nguyên chờ trả lời tại sổ gốc, không tạo câu hỏi thay thế.
