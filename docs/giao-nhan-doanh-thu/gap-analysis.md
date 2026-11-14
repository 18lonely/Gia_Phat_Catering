---
id: DOC-E7-GAP-ANALYSIS
title: Rà khoảng trống E7
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [gap-analysis, giao-nhan, doanh-thu]
depends_on: [DOC-E7-SRS-SPEC-MD, DOC-E7-SRS-STATES-MD, DOC-E7-SRS-DATA-DICTIONARY-MD, DOC-E7-API-API-SPEC-MD, DOC-E7-REVIEW-QUESTIONS-MD]
author: BA
last_updated: 2026-11-16
---
# Rà khoảng trống E7: Giao nhận, doanh thu và đối soát

Draft · 16/11/2026 · Rà tài liệu, chưa phê duyệt, chưa triển khai.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-16 | BA | Khởi tạo: rà 13 FR, 13 UC, 18 API, 3 state, delta dữ liệu, 8 màn hình |

## 1. Phạm vi rà

- **Tài liệu đối chiếu:** [SRS](srs/spec.md), [states](srs/states.md), [delta dữ liệu](srs/data-dictionary.md), [ERD](srs/erd.md), [sơ đồ use case](srs/usecase-diagram.md), [sơ đồ tuần tự](srs/flows.md), [API](api/api-spec.md), [màn hình](ui/screens.md), [câu hỏi](review/questions.md), [phụ thuộc](review/dependencies.md).
- **Cách rà:** tìm luồng ngoại lệ, chuyển trạng thái, dữ liệu và vai trò chưa có FR, UC hoặc API đi kèm.
- **Không làm:** không trả lời câu hỏi mở, không thêm FR hoặc API, không đổi trạng thái ca test. Phương án ở cột cuối là đề xuất chờ người có thẩm quyền chọn.

## 2. Phát hiện

| Mã | Phân loại | Vị trí | Mô tả khoảng trống | Mức | Hướng xử lý đề xuất |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `GAP-E7-01` | Luồng ngoại lệ | FR-DLV-ACK-001; state phiếu | Khách không xác nhận thì phiếu nằm mãi ở WAITING_CONFIRMATION; chưa có hạn chờ, nhắc hay chuyển trạng thái | High | Giữ BLOCKED đến khi Q-13 được trả lời; sau đó thêm transition và ca test |
| `GAP-E7-02` | Trạng thái | State phiếu giao | Phiếu cho đơn 0 suất, đơn bị hủy, giao nhiều lần, nhận thừa chưa có transition (states.md tự ghi nhận) | High | Gom vào E7-Q02; cần nguồn E6 về hủy và zero (CG03) trước |
| `GAP-E7-03` | Thiếu chức năng | FEAT-049 | Không có FR, UC hay API để sửa hoặc hủy phiếu giao đã gửi, hay sửa xác nhận đã ghi; từ điển chỉ ghi "sửa xác nhận cần policy" | High | Đề xuất câu hỏi mới vào gói quyết định: ai được sửa, trong bao lâu, giữ lịch sử thế nào |
| `GAP-E7-04` | Thiếu chức năng | FEAT-052; FR-FIN-RCPT-001 | Không có luồng sửa, hủy hoặc hoàn chứng từ thu tiền | Medium | Đã nằm trong E7-Q06; giữ BLOCKED, không thêm API trước khi có trả lời |
| `GAP-E7-05` | Thiếu chức năng | FEAT-053; state yêu cầu mở lại | Sau khi kỳ mở lại và khóa lại, chưa có UC tái xuất MISA; states chỉ ghi "không tự tái xuất" | Medium | Gom vào E7-Q05 và E7-Q07; bổ sung UC sau khi có mẫu nhập |
| `GAP-E7-06` | Vai trò | UI-E7-05; FR-FIN-AGRE-001 | Màn hình cho phép khách đọc kỳ thuộc scope, nhưng không có FR hay UC cho khách xem kỳ đối soát, và kênh khách gửi bằng chứng thống nhất chưa mô tả | Medium | Đề xuất câu hỏi mới: khách xem và thống nhất kỳ trên hệ thống hay ngoài hệ thống |
| `GAP-E7-07` | Thông báo | FR-DLV-ACK-001; FR-FIN-RREQ-001 | Không có FR thông báo cho khách khi phiếu chờ xác nhận, hay cho Giám đốc khi có yêu cầu mở lại kỳ | Medium | Kiểm xem kênh thông báo nền E1 có dùng được không; nếu không, đề xuất câu hỏi mới |
| `GAP-E7-08` | Dữ liệu | Từ điển; ERD | `e7_reconciliation_lines` chỉ được nhắc chung với periods, chưa liệt kê cột (số tiền dòng, trạng thái đủ/thiếu, lý do chặn) | Medium | Bổ sung cột ở từ điển khi E7-Q05 và E7-Q08 có trả lời |
| `GAP-E7-09` | Quy tắc | BR-E7-009; NFR-E7-002 | "Kỳ LOCKED chặn cả phiếu, doanh thu, chứng từ" nhưng phiếu giao không có liên kết trực tiếp tới kỳ; chưa mô tả cách tìm kỳ bị ảnh hưởng khi ghi phiếu | Medium | Tech lead đề xuất cách tra (theo khách và ngày phục vụ) trong review kỹ thuật E7-Q08 |
| `GAP-E7-10` | Kiểm thử | test/ | E7 chưa có ca nghiệm thu mức release `r7-acceptance.md` như E9 đến E13 | Low | Bổ sung khi có dữ liệu pilot 2 khách một tháng (NFR-E7-003) |
| `GAP-E7-11` | Dữ liệu thật | NFR-E7-003 | Chưa có biên bản đối soát thật hay mẫu MISA để làm oracle "khớp biên bản" | High | Giữ BLOCKED E7-Q04, E7-Q07; không dùng synthetic thay bằng chứng |

## 3. Đã đóng trong phiên này

| Khoảng trống cũ | Cách đóng |
| :--- | :--- |
| Thiếu sơ đồ use case | Thêm [srs/usecase-diagram.md](srs/usecase-diagram.md) |
| Thiếu sơ đồ tuần tự | Thêm [srs/flows.md](srs/flows.md) |
| Thiếu ERD | Thêm [srs/erd.md](srs/erd.md), chỉ vẽ lại delta đã có |

## 4. Giữ nguyên

Mọi câu hỏi Q-13, E7-Q01 đến E7-Q08 giữ CHỜ TRẢ LỜI, cột trả lời trống. E6-CG-01/05/06/08 vẫn OPEN. Ba câu đề xuất mới ở GAP-E7-03, 06, 07 chưa có mã; cần đưa vào gói quyết định ở lần rà kế tiếp. Không có backend, migration hay UAT.
