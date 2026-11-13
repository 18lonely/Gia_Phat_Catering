---
id: DOC-E7-SRS-SPEC-MD
title: "SRS E7: Giao nhận, doanh thu và đối soát"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# SRS E7: Giao nhận, doanh thu và đối soát

Draft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.

## 1. Giới thiệu

[PRD](../../gia-phat/01-prd.md) · [Epic](../epic-spec.md) · [Nền tảng](../../nen-tang/srs/spec.md) · [Kế toán](../../cost/accounting/business-rules.md).

Phiếu ghi sự kiện giao/nhận theo suất. Kỳ đối soát là tập dữ liệu một khách/khoảng ngày. Revision là bản nguồn; version là token thay đổi, không tráo hai khái niệm.

## 2. Tổng quan

Bếp/vận hành ghi giao, đại diện khách xác nhận, kế toán đối soát/thu tiền, Giám đốc duyệt mở lại. [Quyền/UI](../ui/screens.md) là đề xuất, không tự cấp quyền chỉ vì role đã có. Web desktop/mobile; phiên này HTML offline. [Phụ thuộc](../review/dependencies.md) chặn E6/auth/link; [câu hỏi](../review/questions.md) chặn Q-13, căn cứ tiền, mẫu MISA. CG01/08/05/06 chỉ là cổng đầu vào, không đặc tả cách producer vượt cổng.

## 3.1 FR: tất cả P0 theo PRD

| FR / Feature | Tên / actor | Input logic | Xử lý | Output | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR-DLV-NOTE-001 / FEAT-049 | Lập phiếu giao nhận: Bếp trưởng / quản lý cơ sở | orderId, orderRevisionRef, planRevisionRef, số giao, bằng chứng giao | Đối chiếu scope và nguồn; giữ số chốt/số giao riêng, ghi phiếu và provenance, không sửa order E6 | Phiếu chờ khách xác nhận | E6-CG-05/06/08; E7-Q02 |
| FR-DLV-ACK-001 / FEAT-049 | Xác nhận số nhận qua link: Đại diện khách được xác minh | deliveryId, số nhận, version, bằng chứng xác nhận | Chỉ ghi khi người nhận được xác minh đúng scope theo policy đã duyệt; mở link không là xác nhận; giữ số nhận thực và dấu vết | Xác nhận nhận hoặc chênh lệch | E6-CG-01/08; E7-Q01; Q-13 |
| FR-DLV-DIFF-001 / FEAT-050 | Lập biên bản chênh lệch: Dinh dưỡng viên / vận hành được cấp quyền | deliveryId, số giao/nhận tham chiếu, mô tả, evidenceRef | Giữ bằng chứng hai phía; so sánh số giao/nhận; thiếu số nhận thì chưa xác định chênh, không điền 0 | Biên bản có version, liên kết phiếu | E7-Q02; E6-CG-08 |
| FR-DLV-RES-001 / FEAT-050 | Ghi thỏa thuận xử lý chênh lệch: Vận hành được cấp quyền | discrepancyId, phương án giao bù/giảm trừ, evidenceRef, version | Ghi thỏa thuận hai phía; giao bù gắn phiếu gốc và số bù thực; giảm trừ giữ dòng điều chỉnh riêng; không tự cộng cả hai cách cho một phần thiếu | Thỏa thuận và nguồn số tính tiền | E7-Q02/03; CK-Q07–09 khi liên quan CK |
| FR-FIN-REV-001 / FEAT-051 | Tính doanh thu từ số tính tiền: Kế toán doanh thu | orderRevisionRef, pricingSnapshotId, billableServings, basisEvidenceRef | Kiểm căn cứ số tính tiền và giá chụp đúng order/version; tính số tính tiền × giá chụp; tách phải trả, VAT/doanh thu chưa VAT và CK riêng; thiếu context thì chưa xác định | Bản tính nháp có provenance | E7-Q03/04; Q-13; E6-CG-04/05/07 |
| FR-FIN-VIEW-001 / FEAT-051 | Tra cứu doanh thu và nguồn: Kế toán doanh thu | customerId, fromDate, toDate, trạng thái | Đọc bản tính có sẵn theo scope; tách dòng đủ/thiếu; không cộng dòng chưa xác định như 0 vào tổng hoàn tất | Danh sách, nguồn và tổng có nhãn đủ/thiếu | E7-Q04/08; E6-CG-08 |
| FR-FIN-REC-001 / FEAT-052 | Lập kỳ đối soát: Kế toán doanh thu | customerId, fromDate, toDate, revenueRefs | Chụp tập nguồn/version; liệt kê dòng thiếu/tranh chấp, không bỏ dòng lỗi để báo đủ | Kỳ nháp và danh sách chặn | E7-Q05; Q-13; E6-CG-08 |
| FR-FIN-AGRE-001 / FEAT-052 | Ghi nhận thống nhất đối soát: Kế toán và đại diện khách | periodId, version, agreementEvidenceRef | Đối chiếu tổng và nguồn đúng revision với bằng chứng khách; còn chênh lệch chưa thống nhất; không tự ghi thu | Kỳ thống nhất có bằng chứng | E7-Q05; Q-13; E6-CG-01/08 |
| FR-FIN-RCPT-001 / FEAT-052 | Ghi nhận thu tiền: Kế toán doanh thu | periodId, số tiền, ngày nhận, chứng từ, version | Kiểm tiền dương, đúng khách/kỳ và chứng từ; ghi khoản thu có dấu vết; không suy đã thu từ thống nhất hoặc xuất MISA | Khoản thu và còn phải thu riêng | E7-Q06; E7-Q05 về thu sau khóa |
| FR-FIN-LOCK-001 / FEAT-052 | Khóa kỳ đối soát: Kế toán doanh thu | periodId, version, nguồn quyết định | Kiểm đủ nguồn/điều kiện khóa đã được duyệt; giữ snapshot bất biến; chặn mọi đường ghi ảnh hưởng kỳ | Kỳ LOCKED và audit | E7-Q05; Q-13 |
| FR-FIN-RREQ-001 / FEAT-052 | Đề nghị mở lại kỳ: Kế toán doanh thu | periodId, version, lý do, nội dung sửa, evidenceRef | Kỳ phải khóa; lý do ≥10 ký tự theo nền; tạo yêu cầu, không mở khóa | Yêu cầu chờ Giám đốc, kỳ vẫn khóa | E7-Q05; O-06 về ủy quyền giữ mở |
| FR-FIN-RDEC-001 / FEAT-052 | Duyệt hoặc từ chối mở lại kỳ: Giám đốc | requestId, requestVersion, periodVersion, approve/reject, reason | Kiểm Giám đốc khác người lập/sửa cuối theo BR-SEC-008; đúng version mới mở; từ chối giữ khóa; giữ snapshot cũ, sửa sau mở phải đối soát lại | Quyết định; kỳ REOPENED hoặc LOCKED | E7-Q05; O-06 không tự cấp người thay |
| FR-FIN-MISA-001 / FEAT-053 | Chuẩn bị và yêu cầu xuất MISA: Kế toán doanh thu | periodId, revision, templateRef đã xác nhận | Kiểm quyền/nguồn kỳ và mẫu nhập/mapping được duyệt; ghi yêu cầu xuất có nguồn/trạng thái/lỗi; thiếu mẫu thì chặn, không tự tạo cột | Yêu cầu xuất; file chỉ sau mapping được duyệt | E7-Q07/08; E7-Q05 về kỳ được phép xuất |

BR-E7-001/002/003/010 áp mọi FR. ACK/DIFF/RES thêm004; REV/VIEW/REC/AGRE thêm005/006/007; RCPT thêm008; LOCK/RREQ/RDEC thêm009; MISA thêm011. [Lỗi](error-matrix.md) và [RTM](../test/traceability.md).

## 3.2 Business rules

| Mã | KHI → THÌ; ngoại lệ | Căn cứ / trạng thái |
| :--- | :--- | :--- |
| BR-E7-001 | KHI đọc/ghi THÌ kiểm quyền/scope hiện tại; không ngoại lệ bằng link công khai | Nền FR-AUTH-RBAC-001; CG01/08 và E7-Q01 |
| BR-E7-002 | KHI dùng E6 THÌ giữ order revision/order version/plan revision riêng; thiếu không =0, không tự lấy bản mới | Mapping E6; CG04/05/06/07/08 |
| BR-E7-003 | KHI ghi THÌ kiểm version, audit actor/time/trước-sau; lỗi không thành công một phần; GET không ghi | Đề xuất; persistence E7-Q08 |
| BR-E7-004 | KHI nhận khác giao/chốt THÌ giữ từng số và thỏa thuận bù/giảm trừ; không tự xử lý im lặng | FEAT-049/050; Q-13/E7-Q02 |
| BR-E7-005 | KHI tính doanh thu THÌ số tính tiền có căn cứ × giá chụp order; không lấy giá sống hoặc dòng món | FEAT-051; E7-Q03 |
| BR-E7-006 | KHI xử lý VAT THÌ invoiceRequested riêng, thiếu context chưa xác định; cost nguyên liệu gồm VAT phải trả NCC | Kế toán; E7-Q04 còn mở |
| BR-E7-007 | KHI có CK % hoặc tiền/suất THÌ khoản riêng theo đơn, không giảm phải trả hoặc suy đã chi; giảm trừ chênh không là CK | Kế toán đã xác nhận; CK-Q01–10 giữ |
| BR-E7-008 | KHI ghi thu THÌ tiền dương, chứng từ đúng khách/kỳ, không ghi trùng; AGREED/export không là PAID | FEAT-052; E7-Q06/08 |
| BR-E7-009 | KHI kỳ khóa THÌ không sửa trước Giám đốc duyệt mở; chờ/từ chối vẫn khóa; duyệt khác lập/sửa cuối; lý do ≥10 ký tự | R7; BR-SEC-008/BR-AUD-001 nền; O-06 giữ mở |
| BR-E7-010 | KHI thiếu nguồn/policy THÌ ghi BLOCKED kèm mã, không dùng synthetic thay evidence thật | Chỉ dẫn 12/11/2026 |
| BR-E7-011 | KHI xuất MISA THÌ dùng mẫu được xác nhận/giữ revision nguồn; thiếu mẫu không tự tạo cột | FEAT-053/R7; E7-Q07 |

## 3.3 Giao diện ngoài

[API](../api/api-spec.md), [mapping](../api/data-mapping.md), [wireframe](../html-wireframe/revenue-workbench.html). MISA là file theo mẫu, không thêm webhook/connector.

## 3.4 NFR

| Mã | Chỉ tiêu / phương pháp | Giới hạn |
| :--- | :--- | :--- |
| NFR-E7-001 | 0 truy cập chéo khách/cơ sở hoặc lộ cost/secret link qua response/log hiển thị; thử từng route/role/scope | Link BLOCKED E7-Q01/CG01 |
| NFR-E7-002 | 0 sửa kỳ LOCKED trước Giám đốc duyệt; 100% sửa số có audit; thử mọi đường ghi/race/fault | R1/R7; chưa runtime |
| NFR-E7-003 | Doanh thu một tháng khớp biên bản 2 khách; file nhập được MISA | R7; dữ liệu/mẫu/rounding chưa có; không mượn dung sai Cost |
| NFR-E7-004 | Kế thừa nền p95 đọc ≤300ms, ghi ≤800ms tại profile 1000 người đồng thời | Profile E7/xuất E7-Q08; không tự dùng 1000TPS template |
| NFR-E7-005 | 390px/1440px không tràn ngang toàn trang; label/focus và lỗi/BLOCKED đọc được | Chỉ kiểm HTML mới; chưa audit accessibility đầy đủ |

## 3.5 Lỗi và phụ lục

[Error matrix](error-matrix.md) · [States](states.md) · [Delta](data-dictionary.md) · [Flow](../ui/user-flow.md) · [RTM](../test/traceability.md).

Không sửa O-02/O-03/O-04 hoặc E6-EVID-001/002; không hỏi lại scope/C→S/S+C vượt T.
