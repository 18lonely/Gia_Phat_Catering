---
id: DOC-E13-SRS-SPEC-MD
title: Đặc tả E13 — EXP
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e13, exp, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Đặc tả E13 — EXP

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu FEAT-088; giữ các quyết định còn chờ |

## 1. Giới thiệu

FEAT-088 P2 phục vụ PER-07/PER-08. Thuật ngữ: kỳ là phạm vi ngày được duyệt, không mặc định tháng; pool là nhóm chi phí chung chưa gán khách; run là snapshot lần báo cáo; chưa phân bổ là phần có nguồn nhưng chưa có căn cứ gán, khác dữ liệu thiếu. [Epic](../epic-spec.md) và [nguồn/phụ thuộc](../review/dependencies.md).

## 2. Tổng quan và quyền

E13 là consumer dữ liệu, không thay hệ thống nguồn. Môi trường dự kiến web nội bộ theo E1. PER-07 được đề xuất nhập nháp và đọc cơ sở được cấp; PER-08 duyệt phương pháp, đọc theo quyền. Chi tiết lương chỉ hai persona này và phải có quyền trường/scope cụ thể. PER-06, PER-05, khách và dịch vụ không tự có quyền E13. Chưa cấp người thay Giám đốc vì O-06.

## 3. Yêu cầu chức năng

| FR / Feature | Chức năng / Actor | Ưu tiên | Input | Xử lý | Output | BR / Lỗi | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-EXP-PER-001 / FEAT-088 | Quản lý và khóa kỳ chi phí — PER-07 | P2 | periodRef, kitchenRef, fromDate, toDate, version, lockDecisionRef | Kiểm scope, nguồn và quyết định khóa; kỳ mở cho nhập nháp. Chỉ khóa khi chính sách và quyền đã được duyệt; giữ snapshot bất biến. | Kỳ OPEN hoặc LOCKED; danh sách điều kiện thiếu | BR-EXP-001; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q02 |
| FR-EXP-COST-001 / FEAT-088 | Ghi chi phí theo cơ sở và loại — PER-07 | P2 | periodRef, kitchenRef, typeVersionRef, amount, evidenceRef, sourceKey, customerRef? | Kiểm kỳ mở, căn cứ khoản tiền và loại. Khoản trực tiếp phải có khách và căn cứ gán trực tiếp; khoản chung giữ pool riêng. Không nhận lại cost E3/E11 như khoản mới. | Dòng chi phí DRAFT có nguồn; chưa hạch toán chính thức | BR-EXP-002; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q01 |
| FR-EXP-TIME-001 / FEAT-088 | Ghi giờ công thực tế theo ca — PER-07 | P2 | personRef, kitchenRef, shiftRevisionRef, workDate, hours, attendanceEvidenceRef, version | Đối chiếu người/cơ sở với tham chiếu E11; phân ca là dự kiến, không sinh giờ thực tế. Lưu giờ nháp cùng bằng chứng; nguồn chấm công và xác nhận chính thức còn chờ. | Bảng DRAFT; giờ thực tế và ca dự kiến tách riêng | BR-EXP-003; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q03; E11-Q09 |
| FR-EXP-LAB-001 / FEAT-088 | Tham chiếu chi phí nhân công — PER-07 | P2 | attendanceVersionRef, rateVersionRef hoặc payrollAmountRef, evidenceRef | Chỉ dùng nguồn đơn giá/tiền công và giờ đã xác nhận. Hai cách là lựa chọn phải duyệt, không cộng cả hai. Thiếu giá giữ null; không tính bảo hiểm, thuế TNCN, phụ cấp hoặc lương thực lĩnh. | Chi phí nhân công có nguồn hoặc BLOCKED | BR-EXP-004; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q03/04 |
| FR-EXP-METH-001 / FEAT-088 | Soạn phiên bản phương pháp phân bổ — PER-07 | P2 | methodRef?, baseVersion?, scope, proposedBasis, effectiveRange, sourceDefinitionRefs, rationale | Lưu phương án nháp, các driver và căn cứ đề xuất dưới dạng dữ liệu có phiên bản. Không mặc định phương pháp nào; không thực thi biểu thức tùy ý. Nội dung thuật toán chỉ đặc tả sau E13-Q05. | Phiên bản DRAFT; không có hiệu lực phân bổ | BR-EXP-005; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q05/09 |
| FR-EXP-APRV-001 / FEAT-088 | Ghi duyệt phương pháp của Giám đốc — PER-08 | P2 | methodVersionRef, expectedVersion, expectedHash, decision, evidenceRef, reason | Kiểm quyền Giám đốc, khác người tạo/sửa cuối theo E1; kiểm đủ nội dung và bằng chứng. Quyết định gắn hash và hiệu lực cụ thể. Không suy ủy quyền từ chức danh; O-06 còn mở. | Quyết định APPROVED hoặc RETURNED; version không đổi nội dung | BR-EXP-006; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q05; O-06 |
| FR-EXP-ALLOC-001 / FEAT-088 | Kiểm cổng và lập lần phân bổ — PER-07 | P2 | periodSnapshotRef, methodVersionRef, sourceManifestRef | Kiểm phương pháp được duyệt đúng scope/hiệu lực và bộ nguồn đầy đủ. Chưa có phương pháp: BLOCKED, chỉ hiển thị chi phí trực tiếp, không tạo kết quả giả. Khi đủ quyết định mới triển khai engine theo hợp đồng được duyệt. | Lần chạy BLOCKED hoặc bản phân bổ có methodVersion; phần chưa phân bổ riêng | BR-EXP-007; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q05/06/09/12 |
| FR-EXP-PROF-001 / FEAT-088 | Tra cứu lợi nhuận theo khách — PER-07/PER-08 | P2 | runRef, customerRef, kitchenRef, periodRef | Đọc snapshot có nguồn E7 đã đối soát và cost E3/E11; không tính lại từ suất giao hay giá hiện hành E10. Thiếu bất kỳ căn cứ công thức/nguồn/phương pháp thì lợi nhuận null; báo cáo chỉ phần trực tiếp được phép. | Báo cáo nội bộ có nguồn, version và trạng thái; margin chưa xác định | BR-EXP-008; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q05/07/08/13; E7-Q03/04/05; E10-Q15 |
| FR-EXP-RECON-001 / FEAT-088 | Đối chiếu lợi nhuận với từng cơ sở — PER-08 | P2 | runRef, facilityResultRef, resultDefinitionVersionRef | Ghép cùng cơ sở/kỳ, cùng bộ thành phần và revision. Tách kết quả các khách, phần chưa phân bổ, chênh so số chuẩn độc lập. Không cộng khách thiếu như 0; không tự cho phép sai số. | Bảng đối chiếu có residual/unallocated/delta; chưa khớp không nghiệm thu | BR-EXP-009; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q06/08/09/14 |
| FR-EXP-ADJ-001 / FEAT-088 | Lập điều chỉnh sau khóa có phê duyệt — PER-07 | P2 | originalEntryRef, lockedSnapshotRef, adjustmentAmount, reason, evidenceRef, approvalRef | Giữ nguyên bản gốc. Đề nghị điều chỉnh là dòng riêng, lý do và người duyệt bắt buộc trước ghi nhận. Người duyệt/quy tắc kỳ đích chờ Q10; không tự chọn hoặc mở khóa E7. | Đề nghị PENDING; chỉ POSTED khi có quyết định hợp lệ | BR-EXP-010; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q10; O-06 |
| FR-EXP-SAFE-001 / FEAT-088 | Bảo vệ lương và đầu ra nội bộ — PER-07/PER-08 | P2 | runRef, actorScope, purpose, projection | Kiểm quyền hiện tại ở server và truy cập nguồn; chỉ PER-07/PER-08 có quyền chi tiết lương theo scope. Báo cáo theo khách nội bộ chỉ tổng hợp nhân công, không người/giờ/đơn giá. Tài liệu gửi khách tuyệt đối không có lợi nhuận/biên lợi nhuận/cost/lương. | Projection nội bộ cho phép hoặc từ chối; không có đường gửi khách E13 | BR-EXP-011; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q11/12; E12-Q07 |
| FR-EXP-SRC-001 / FEAT-088 | Kiểm nguồn và truy nguyên lần báo cáo — PER-07/PER-08 | P2 | runRef, sourceManifestRef, expectedVersions | Hiện nguồn E3/E7/E10/E11, định nghĩa chỉ số, thời điểm chụp, phạm vi, phiên bản và thiếu nguồn. Nguồn đổi tạo lần mới; không hồi tố sửa lần cũ. Đầu nối E12 chỉ ranh giới đọc, chưa triển khai adapter. | Manifest, danh sách BLOCKED và liên kết nội bộ theo quyền | BR-EXP-012; ERR-EXP-403-01, ERR-EXP-422-02; xem ma trận lỗi | E13-Q12/13 |

## 4. Quy tắc nghiệp vụ

| BR | KHI | THÌ | Ngoại lệ |
| :--- | :--- | :--- | :--- |
| BR-EXP-001 | Quản lý và khóa kỳ chi phí | Kiểm scope, nguồn và quyết định khóa; kỳ mở cho nhập nháp. Chỉ khóa khi chính sách và quyền đã được duyệt; giữ snapshot bất biến. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-002 | Ghi chi phí theo cơ sở và loại | Kiểm kỳ mở, căn cứ khoản tiền và loại. Khoản trực tiếp phải có khách và căn cứ gán trực tiếp; khoản chung giữ pool riêng. Không nhận lại cost E3/E11 như khoản mới. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-003 | Ghi giờ công thực tế theo ca | Đối chiếu người/cơ sở với tham chiếu E11; phân ca là dự kiến, không sinh giờ thực tế. Lưu giờ nháp cùng bằng chứng; nguồn chấm công và xác nhận chính thức còn chờ. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-004 | Tham chiếu chi phí nhân công | Chỉ dùng nguồn đơn giá/tiền công và giờ đã xác nhận. Hai cách là lựa chọn phải duyệt, không cộng cả hai. Thiếu giá giữ null; không tính bảo hiểm, thuế TNCN, phụ cấp hoặc lương thực lĩnh. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-005 | Soạn phiên bản phương pháp phân bổ | Lưu phương án nháp, các driver và căn cứ đề xuất dưới dạng dữ liệu có phiên bản. Không mặc định phương pháp nào; không thực thi biểu thức tùy ý. Nội dung thuật toán chỉ đặc tả sau E13-Q05. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-006 | Ghi duyệt phương pháp của Giám đốc | Kiểm quyền Giám đốc, khác người tạo/sửa cuối theo E1; kiểm đủ nội dung và bằng chứng. Quyết định gắn hash và hiệu lực cụ thể. Không suy ủy quyền từ chức danh; O-06 còn mở. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-007 | Kiểm cổng và lập lần phân bổ | Kiểm phương pháp được duyệt đúng scope/hiệu lực và bộ nguồn đầy đủ. Chưa có phương pháp: BLOCKED, chỉ hiển thị chi phí trực tiếp, không tạo kết quả giả. Khi đủ quyết định mới triển khai engine theo hợp đồng được duyệt. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-008 | Tra cứu lợi nhuận theo khách | Đọc snapshot có nguồn E7 đã đối soát và cost E3/E11; không tính lại từ suất giao hay giá hiện hành E10. Thiếu bất kỳ căn cứ công thức/nguồn/phương pháp thì lợi nhuận null; báo cáo chỉ phần trực tiếp được phép. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-009 | Đối chiếu lợi nhuận với từng cơ sở | Ghép cùng cơ sở/kỳ, cùng bộ thành phần và revision. Tách kết quả các khách, phần chưa phân bổ, chênh so số chuẩn độc lập. Không cộng khách thiếu như 0; không tự cho phép sai số. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-010 | Lập điều chỉnh sau khóa có phê duyệt | Giữ nguyên bản gốc. Đề nghị điều chỉnh là dòng riêng, lý do và người duyệt bắt buộc trước ghi nhận. Người duyệt/quy tắc kỳ đích chờ Q10; không tự chọn hoặc mở khóa E7. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-011 | Bảo vệ lương và đầu ra nội bộ | Kiểm quyền hiện tại ở server và truy cập nguồn; chỉ PER-07/PER-08 có quyền chi tiết lương theo scope. Báo cáo theo khách nội bộ chỉ tổng hợp nhân công, không người/giờ/đơn giá. Tài liệu gửi khách tuyệt đối không có lợi nhuận/biên lợi nhuận/cost/lương. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |
| BR-EXP-012 | Kiểm nguồn và truy nguyên lần báo cáo | Hiện nguồn E3/E7/E10/E11, định nghĩa chỉ số, thời điểm chụp, phạm vi, phiên bản và thiếu nguồn. Nguồn đổi tạo lần mới; không hồi tố sửa lần cũ. Đầu nối E12 chỉ ranh giới đọc, chưa triển khai adapter. | Không bỏ qua gate; thiếu quyết định giữ BLOCKED |

## 5. Đối chiếu tổng và thành phần

Chưa chọn công thức lợi nhuận hoặc biên lợi nhuận thực tế. Các ký hiệu sau chỉ là bất biến bảo toàn của **cùng tập thành phần đã được duyệt**, không quyết định cách hạch toán CK, VAT hoặc giá vốn. Kết quả cơ sở B lấy số chuẩn độc lập có nguồn/định nghĩa, không lấy chính tổng khách làm số chuẩn.

Đặt P là tổng kết quả khách đã tính đầy đủ; U là tác động có dấu của phần chưa phân bổ; D = B − (P + U). Chi phí chưa phân bổ 50 đ có tác động U = −50 đ. Hiển thị cả tiền chi phí chưa phân bổ dương và tác động âm để tránh hiểu nhầm. Báo cáo có thể giải thích B = P + U khi D = 0, nhưng **R13 chưa đạt nếu U còn khác 0**. Muốn hoàn tất đối chiếu theo khách phải U = 0, D = 0 và P = B, không còn nguồn thiếu. Không tự đặt dung sai/làm tròn; Q09 còn mở. Không lấy chênh lệch do thiếu dữ liệu làm “chưa phân bổ”.

Fixture synthetic, không là phương pháp: B = 200 đ, P = 250 đ, chi phí chưa phân bổ = 50 đ, U = −50 đ, D = 0. Nhãn: đối chiếu cầu nối khớp, phân bổ chưa hoàn tất. Nếu chi phí chưa phân bổ chỉ 40 đ thì D = −10 đ; hiện riêng, không dồn vào khách cuối. Không có bản duyệt phương pháp thì chỉ hiện chi phí trực tiếp; không hiển thị cả P, B như lợi nhuận sẵn dùng trong báo cáo khách.

Doanh thu luôn từ snapshot E7 đã đối soát, không số giao × giá hiện hành. Cost nguyên liệu dùng E3/E11 đúng loại dự toán/thực mua và provenance; không cộng cả hai, không nhân cost món dự toán thành giá vốn thực. Khoản chung cấp công ty ở pool riêng chờ Q06, không tự đưa xuống cơ sở. Khách nhiều cơ sở đối chiếu từng khóa kitchenRef + periodRef trước khi tổng khách.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” là cờ riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn; không giảm số phải trả nhà cung cấp, không tự khấu trừ số khách phải trả. Chưa quyết định khoản chiết khấu đi vào lợi nhuận thế nào. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-01 (cost ≤ 52 % doanh thu) và BO-02 (≤ 3 điểm phần trăm) là mục tiêu kinh doanh, không là dung sai đối chiếu E13. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03.

## 6. Phi chức năng

| NFR | Tiêu chí | Đánh giá |
| :--- | :--- | :--- |
| NFR-EXP-001 | 0 lần lộ chi tiết lương ngoài PER-07/PER-08 có scope; 0 trường lợi nhuận/biên lợi nhuận trên tài liệu gửi khách, kể cả payload/lỗi/cache/export. | Ca bảo mật ở hệ thống thật; mock không chứng minh. |
| NFR-EXP-002 | 100 % lần báo cáo giữ manifest nguồn, trạng thái, định nghĩa và methodVersion; 0 lần ghi đè snapshot khóa. | Đối chiếu audit trước/sau; thiếu nguồn BLOCKED. |
| NFR-EXP-003 | D = 0 trên số gốc và U = 0 trước hoàn tất R13; không tự dung sai. | Công thức thành phần/làm tròn chờ E13-Q08/09. |
| NFR-EXP-004 | Kế thừa nền 1000 người dùng đồng thời, p95 đọc ≤ 300 ms, ghi ≤ 800 ms; báo cáo theo lô cần profile riêng. | Tải E13 BLOCKED chờ Q12, không tự chọn SLA cho run. |
| NFR-EXP-005 | UI không tràn ngang toàn trang ở 1440 / 390 / 360 px; mục tiêu WCAG 2.1 AA theo nền. | Kiểm mock và rà ảnh; chưa audit WCAG đầy đủ. |
| NFR-EXP-006 | 100 % thay đổi tiền/duyệt/điều chỉnh có actor, thời điểm, tham chiếu và lý do; log phổ thông không chứa lương. | Audit chi tiết bảo vệ cùng quyền trường, retention chờ Q11. |

## 7. Giao diện và phụ lục

[API](../api/api-spec.md) · [Dữ liệu đề xuất](data-dictionary.md) · [Lỗi](error-matrix.md) · [Trạng thái](states.md) · [Màn](../ui/screens.md) · [RTM](../test/traceability.md). Tất cả hợp đồng là đề xuất, không contract freeze.

Giữ nguyên các câu đang chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp phần producer phụ thuộc các câu này.
