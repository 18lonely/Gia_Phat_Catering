---
id: DOC-E7-REVIEW-HANDOFF-MD
title: Bàn giao BA nháp E7
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Bàn giao BA nháp E7

## Gói này gồm gì

E7 mô tả giao nhận theo suất, xử lý chênh lệch, tính doanh thu, đối soát, thu tiền, khóa/mở lại kỳ và chuẩn bị xuất MISA. Đây là thiết kế có điều kiện để review, chưa được phê duyệt hoặc triển khai. Mốc mở gói là 12/11/2026; thông tin “E8–E13 chưa mở” thuộc bối cảnh bàn giao ban đầu, không phải kết luận về các phiên sau.

## Đọc theo thứ tự nào

1. Đọc [Epic](../epic-spec.md), [Questions](questions.md) và [Dependencies](dependencies.md) để biết phạm vi và phần đang chặn.
2. Đọc [SRS](../srs/spec.md) rồi [UC](../usecases/index.md) để theo luồng từ giao hàng đến xuất file.
3. Đối chiếu [API](../api/api-spec.md), [Mapping](../api/data-mapping.md) và [UI](../ui/screens.md) để hiểu đầu vào, nguồn số liệu và quyền.
4. Đọc [Story](../userstories/backlog.md), [AC](../userstories/acceptance-criteria.md), [Test](../test/test-cases.md) và [RTM](../test/traceability.md) để kiểm độ phủ; xem [Preview](../preview.html) và [Kiểm](../validation/report.md) cho bằng chứng kiểm tài liệu lịch sử.

## Số liệu chính

- 5/5 feature E7 có thiết kế nháp có điều kiện; 13 FR tương ứng 13 UC và 13 story.
- 39 AC tương ứng 39 ca chức năng, cùng 39 mục tiêu; 8 ca hệ thống có overlap, không cộng thành số mục tiêu độc lập.
- Gói có 18 endpoint đề xuất, 8 màn và 4 sơ đồ flow/state. Những con số này là inventory tài liệu, không phải số chức năng đã chạy.
- Tại mốc mở E7, độ phủ toàn dự án là 45/78 feature ≈ 57,7%; 2 feature E6 chỉ gate được ghi riêng. Đây là số lịch sử, không phải tỷ lệ BA được duyệt hay tiến độ phần mềm.
- E6 còn 14/14 CG OPEN; schema 65 bảng không đổi. Số backend, migration và UAT đã thực hiện trong gói đều là 0.

## Những điểm người review cần quyết định

Các mục sau vẫn chờ trả lời, không có lựa chọn nào được tự chốt trong phiên chỉnh diễn đạt.

- Q-13: Cách xử lý khách không xác nhận, khoảng chờ và người quyết định số tính tiền.
- E7-Q01: Người được xác nhận nhận hàng và cơ chế xác minh, hiệu lực, thu hồi/cấp lại link.
- E7-Q02: Quyền thống nhất chênh lệch, giao nhiều lần, giao bù, nhận thừa và giảm trừ.
- E7-Q03: Căn cứ số tính tiền và cách quy đổi giảm trừ ra suất hoặc tiền.
- E7-Q04: Cơ sở doanh thu trước/sau VAT, làm tròn và chuẩn khớp biên bản.
- E7-Q05: Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa và vòng mở lại/tái đối soát/tái xuất.
- E7-Q06: Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền.
- E7-Q07: Sản phẩm/phiên bản MISA, mẫu nhập, mapping và bằng chứng nhập thành công.
- E7-Q08: Hợp đồng kỹ thuật, chống ghi trùng, lưu giữ, quyền, audit và profile tải/xuất.

## Giới hạn

Thiết kế E7 sử dụng nguồn E6 có điều kiện, không giải quyết thay producer. CG01/08/05/06 vẫn chờ; không hỏi lại hay tự điền. MISA chưa có mapping cột và chưa thử nhập; dữ liệu minh họa là synthetic. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002, O-02/O-03/O-04 và E6-EVID-001/002 giữ nguyên. Cost gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn không phải VAT 0%; CK là khoản riêng theo đơn, không giảm tiền khách phải trả.

## Việc tiếp theo

Review các điểm mở và bằng chứng nguồn theo sổ câu hỏi; chỉ đồng bộ tài liệu khi có evidence mới hoặc sai lệch cụ thể. Không tự trả lời Q-13, không chạy generator E6 hay sửa snapshot lịch sử. Phiên chỉnh diễn đạt không mở thêm phạm vi triển khai.
