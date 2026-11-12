---
id: DOC-E10-REVIEW-HANDOFF-MD
title: Bàn giao gói BA nháp E10 — 12/11/2026
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Bàn giao gói BA nháp E10 — 12/11/2026

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## Gói này gồm gì

Bốn feature P1 FEAT-070–073: hồ sơ 360°, vòng đời/nguy cơ rời theo lịch điểm, cơ hội/báo giá và hợp đồng/phụ lục giá. Tất cả có thiết kế có điều kiện; E10 không có feature chỉ gate. Luồng tích hợp, tiêu chí trùng, ngưỡng rủi ro và chính sách hiệu lực còn chờ quyết định.

## Đọc theo thứ tự nào

1. [Epic](../epic-spec.md), [SRS](../srs/spec.md), [câu hỏi](questions.md) và [phụ thuộc](dependencies.md).
2. [UC](../usecases/index.md), [backlog](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md).
3. [Trạng thái](../srs/states.md), [luồng](../ui/user-flow.md), [API](../api/api-spec.md), [mapping](../api/data-mapping.md), [từ điển](../srs/data-dictionary.md).
4. [Wireframe](../html-wireframe/crm-workbench.html), [preview](../preview.html), [RTM](../test/traceability.md), [khung R10](../test/r10-acceptance.md), [báo cáo kiểm](../validation/report.md).

## Số liệu chính

16 FR ↔ 16 UC ↔ 16 story; 48 AC ↔ 48 ca chức năng: 21 BLOCKED, 27 NOT RUN. 10 ca hệ thống có overlap: 5 BLOCKED, 5 NOT RUN; không cộng vào tỷ lệ nghiệm thu. 23 HTTP endpoint + 7 port logic; 9 màn trong một HTML; 4 sơ đồ trạng thái + 2 sơ đồ luồng, có SVG/HTML.

Độ phủ tài liệu mới **60/78 ≈ 76,9%**; ba feature FEAT-046/047/063 chỉ gate giữ riêng. Đây không là tiến độ phần mềm hoặc BA được duyệt. Schema 65 bảng giữ nguyên; cấu trúc mới chỉ đề xuất trong từ điển.

## Điểm cần người review quyết định

- E10-Q01: Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?
- E10-Q02: Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?
- E10-Q03: Ai lập, ai duyệt gộp/hoàn tác; có người thay và kiểm tách nhiệm vụ thế nào?
- E10-Q04: Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?
- E10-Q05: Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?
- E10-Q06: Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?
- E10-Q07: Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?
- E10-Q08: Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?
- E10-Q09: Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?
- E10-Q10: Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?
- E10-Q11: Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?
- E10-Q12: Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?
- E10-Q13: Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?
- E10-Q14: Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?
- E10-Q15: Biên lợi nhuận nội bộ trên báo giá dùng công thức, thành phần và nguồn phiên bản nào; ai được xem?

Cột trả lời trống. Khuyến nghị không thay quyết định; không hỏi lại sổ nguồn.

## Giới hạn và tiếp nối

E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04 đều giữ trạng thái chờ tại sổ nguồn. Không hỏi lại, tự trả lời hoặc quyết định thay.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.

Chưa backend, migration, gọi AI hoặc UAT. Không mở E11–E13 hay FEAT-084. Receipt website/E9 không là chấp thuận báo giá, duyệt MENU hoặc ký hợp đồng. Phản hồi trong hồ sơ chỉ là vùng đọc chưa có nguồn. Kiểm tài liệu/mock không chuyển ca sản phẩm thành đạt. Chỉ cập nhật theo phản hồi có nguồn; đồng bộ toàn chuỗi khi thay quyết định. PRD/roadmap không append vì E9 thực tế không append hai file đó; chỉ nối thêm OVERVIEW và dashboard sau kiểm.
