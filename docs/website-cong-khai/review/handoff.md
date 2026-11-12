---
id: DOC-E8-REVIEW-HANDOFF-MD
title: Bàn giao gói BA nháp E8
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Bàn giao gói BA nháp E8

## Gói này gồm gì

E8 gồm trang giới thiệu/dịch vụ/dự án/đối tác, blog và bảo toàn bài/URL WordPress, thực đơn mẫu có giá, dựng thử tuần, form tư vấn và quản trị nội dung/ảnh. Đây là thiết kế có điều kiện; public projection chỉ chứa trường được phép công khai, không phải dữ liệu nội bộ đưa ra rồi ẩn trên UI.

## Đọc theo thứ tự nào

1. Đọc [Epic](../epic-spec.md), [Câu hỏi](questions.md) và [Phụ thuộc](dependencies.md) để nắm phạm vi và nguồn còn thiếu.
2. Đọc [SRS](../srs/spec.md), sau đó theo [Preview](../preview.html) tới UC, API và UI của từng luồng.
3. Dùng [RTM](../test/traceability.md) để đối chiếu FR, story, AC và ca kiểm; [Kiểm](../validation/report.md) là kết quả kiểm tài liệu/mock tại mốc bàn giao cũ, không phải UAT.

## Số liệu chính

- 6/6 feature E8 có thiết kế nháp có điều kiện: 5 P0 và 1 P1; 0/6 feature chỉ gate.
- 12 FR tương ứng 12 UC và 12 story; 36 AC tương ứng 36 ca chức năng, gồm 12 BLOCKED và 24 NOT RUN.
- 12 ca hệ thống gồm 6 BLOCKED và 6 NOT RUN, có overlap với các mục tiêu chức năng; không cộng thành độ phủ nghiệm thu.
- 16 HTTP endpoint đề xuất và 1 port nối E10 tối thiểu; 9 màn HTML, 3 sơ đồ trạng thái và 2 sơ đồ luồng.
- Độ phủ tại mốc mở E8 là 51/78 feature ≈ 65,4% = 23 E1–E5 + 17 E6 + 5 E7 + 6 E8; 2 feature E6 chỉ gate O-03 ghi riêng. Đây là số lịch sử của thiết kế nháp, không phải BA được duyệt hoặc tiến độ phần mềm.
- 12/12 câu E8-Q01–12 còn chờ; 65 bảng không sửa; 0 backend, migration hoặc UAT trong gói.

## Những điểm người review cần quyết định

- E8-Q01: Nguồn inventory bài, URL, media WordPress và cách xác nhận đầy đủ DL-08.
- E8-Q02: Tiêu chí KEEP/301, xử lý bài trùng/xóa và duyệt mapping/rollback.
- E8-Q03: Giá suất được công khai, người duyệt, hiệu lực và cách ghi VAT/giá tham khảo.
- E8-Q04: Điều kiện nguồn E2/E4 đủ cho công khai và cách xử lý thiếu, stale hoặc thu hồi.
- E8-Q05: Cách dựng mẫu, bộ kiểm và giới hạn đầu vào/lượt sử dụng.
- E8-Q06: Nơi lưu lead, trường bắt buộc, consent, lưu/xóa và receipt bàn giao khi E10 chưa mở.
- E8-Q07: Chống spam, nơi nhận thông báo và cách xử lý gửi lặp/thất lạc.
- E8-Q08: CMS, quyền soạn/duyệt/công bố/thu hồi và có hay không bước duyệt.
- E8-Q09: Quyền ảnh/banner, loại/dung lượng, alt, vị trí/lịch và gỡ ảnh đang dùng.
- E8-Q10: Công cụ và baseline đo organic, kỳ so sánh sau 60 ngày cho BO-09.
- E8-Q11: Quyền domain/DNS, hạ tầng, cutover/rollback và quyết định O-04.
- E8-Q12: Envelope, phân trang, cache, chống gửi lặp, receipt, profile tải và thời hạn nháp.

## Giới hạn

R4, DL-08 và quyền domain chưa có bằng chứng hoàn tất. Giá/nguồn public, trial engine, nơi lưu lead và CMS chưa được chọn. Không thu dữ liệu sức khỏe, không gọi Agent E9 từ công cụ dựng thử. E10 chỉ có điểm nối tối thiểu, chưa có hồ sơ/phễu CRM. Mọi dữ liệu minh họa là synthetic.

E6/E7 giữ các nhánh đang chờ; 14 CG E6 OPEN. E6-EVID-001/002, CK/DATA-COST/NFR-COST-002 và O-02/O-03/O-04 còn hiệu lực. Không hỏi lại hay mở rộng producer; API/DTO/delta vẫn là nháp.

## Việc tiếp theo

Review các quyết định và bằng chứng nguồn; chỉ cập nhật đúng chuỗi truy vết khi có căn cứ mới hoặc sai lệch cụ thể, không tự chọn phương án. Không chạy lại author-e8.cjs. Trong phiên chỉnh diễn đạt dùng checker phiên thay check-e8.cjs vì checker cũ khóa hash E7 trước chỉnh sửa; render-e8.cjs chỉ dựng tài liệu. Wireframe không đổi nên không cần kiểm UI lại.
