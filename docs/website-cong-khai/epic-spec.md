---
id: DOC-E8-EPIC-SPEC-MD
title: "E8: Website công khai"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# E8: Website công khai

Draft · 12/11/2026 · Thiết kế có điều kiện, chưa phê duyệt; 0 backend/migration/UAT.

## Mục tiêu và phạm vi

Thay WordPress, cung cấp thực đơn mẫu có giá và tiếp nhận lead có nguồn. Căn cứ [PRD](../gia-phat/01-prd.md), [roadmap](../gia-phat/02-roadmap.md), D-10 trong [kế hoạch](../gia-phat/00-ke-hoach-tong-the.md). Chỉ mở E8 theo người dùng 12/11/2026. E9–E13 chưa mở; PUB-05 chat agent thuộc E9, không thêm thành feature thứ bảy.

| Feature | Mã cũ | Tên | Ưu tiên | Capability |
| :--- | :--- | :--- | :--- | :--- |
| FEAT-054 | PUB-01 | Trang giới thiệu, dịch vụ, dự án, đối tác | P0 | Nội dung công khai và điều hướng; không bịa tên thật |
| FEAT-055 | PUB-02 | Tin tức / blog và chuyển bài cũ | P0 | Danh sách/chi tiết bài; kiểm inventory và mapping URL giữ nguyên hoặc 301 |
| FEAT-056 | PUB-03 | Thực đơn mẫu có giá | P0 | Giá suất được phép công khai; định lượng, 4 chỉ số, dị ứng theo nguồn |
| FEAT-057 | PUB-04 | Công cụ dựng thực đơn thử | P1 | Chọn loại suất, số suất, kiêng kỵ → tuần mẫu; không Agent E9 |
| FEAT-058 | PUB-06 | Form tư vấn → lead | P0 | Ghi nhận nguồn và thực đơn đã dựng; điểm nối CRM chờ E10 |
| FEAT-059 | PUB-07 | Quản trị nội dung | P0 | Soạn/xem trước/xuất bản theo quyền được duyệt; ảnh/banner |

6/6 feature có thiết kế nháp có điều kiện; 0 feature E8 chỉ gate. FEAT-057 có input/output, nhánh vô nghiệm và bảo vệ dữ liệu; thuật toán/engine vẫn BLOCKED, không chỉ là dòng gate. Không coi capability có thiết kế là đã duyệt.

Ngoài phạm vi: backend, migration/chuyển dữ liệu thật, sửa schema65 bảng, CRM E10, Agent E9, order/thanh toán, hồ sơ sức khỏe, tư vấn y khoa; lựa chọn CMS/hosting/analytics/chống spam; ngày triển khai/story point/tên người phụ trách.

## R8 nguyên văn

| Release | Tên đợt phát hành | Mục tiêu chính | Danh sách Feature ID | Cỡ | Điều kiện bắt đầu | Ngày dự kiến | Tiêu chí nghiệm thu |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `R8` · v1.3.0 | Website công khai (E8) | Thay WordPress, có thực đơn mẫu kèm giá, lead vào CRM | `FEAT-054` → `FEAT-059` | L | R4 xong (cần dinh dưỡng để hiển thị); DL-08 xong; có quyền quản trị tên miền | Chờ O-04 | 100% URL bài viết cũ trả về đúng trang hoặc 301; 100% lead từ form có bản ghi kèm nguồn; trang thực đơn mẫu hiện đủ giá, định lượng, 4 chỉ số, dị ứng |

R4 xong, DL-08 xong và có quyền quản trị tên miền là điều kiện bắt đầu release, chưa có bằng chứng đạt. Soạn nháp theo yêu cầu không xác nhận đã qua các cổng. DL-08 cần trước SRS R8: gói này chưa freeze và phần mapping thật BLOCKED.

R7 và R8 không phụ thuộc nhau. FEAT-054/055/059 không cần dữ liệu thực đơn theo roadmap; chỉ có thể kéo lên Now khi có quyết định O-04, phiên này không tự quyết. Cổng G-Now vẫn là điều kiện đợt Next theo roadmap; việc mở tài liệu E8 không miễn cổng.

**Cổng G-Next** (điều kiện để mở đợt Later): ≥ 90% order của các công ty đã chuyển lên hệ thống ghi nhận qua cổng (BO-06); ≥ 70% suất có lựa chọn của người ăn trước hạn chốt (BO-05); số phiên truy cập tự nhiên sau 60 ngày ≥ 90% mức trước chuyển đổi (BO-09).

## Kế hoạch và nghiệm thu

Thứ tự tài liệu: nội dung/URL → projection mẫu và form → review dữ liệu/quyền → kiểm tích hợp khi có môi trường. Đây không phải lịch release. [Câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md), [RTM](test/traceability.md). BO-09 cần baseline và cùng định nghĩa phiên trước/sau, chờ E8-Q10. Chưa được đánh dấu R8/G-Next đạt.

E6 CG01/08/05/06 và E7 Q-13/E7-Q01–08 CHỜ TRẢ LỜI; không hỏi lại, không đặc tả tiếp phần phụ thuộc.14/14 CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. Cost/VAT/CK, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 và O-02/O-03/O-04 không đổi.
