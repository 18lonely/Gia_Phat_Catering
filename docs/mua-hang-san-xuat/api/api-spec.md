---
id: DOC-E11-API-API-SPEC-MD
title: Hợp đồng API đề xuất E11
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Hợp đồng API đề xuất E11

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## Phạm vi và quy ước

15 HTTP endpoint nháp và 4 port ranh giới; không API đang chạy. Mọi request xác thực theo E1; permission và scope kiểm server; ngoài scope 404, thiếu quyền 403. GET không ghi/tạo job/công nợ. Không webhook, không tích hợp NCC ngoài hệ thống.

Header đề xuất: Authorization theo E1, correlation/request id; lệnh ghi dùng version và khóa chống lặp. Cách truyền, thời hạn receipt, retry, envelope và giới hạn mảng chờ E11-Q13/E1-Q01; không đóng chúng bằng mẫu REST. Client không gửi actor được tin cậy, cost chuẩn hóa hoặc trạng thái duyệt có hiệu lực. Giá/ảnh dùng private,no-store; log không có ảnh/giá ngoài quyền.

Thành công dự kiến: GET 200; tạo nháp POST 201; kết quả kiểm POST 200. Lỗi 401/403/404 từ E1; 422 dữ liệu hoặc policy chưa đủ; 409 version; 503 nguồn lỗi. Outcome BLOCKED là dữ liệu readiness của GET hoặc lỗi lệnh không thể thực hiện, không tự đổi trạng thái nghiệp vụ.

Ví dụ envelope chỉ để review theo E1, chưa freeze E1-Q01:

```json
{"success":true,"data":{"status":"BLOCKED","gateRefs":["E11-Q02"]},"meta":null,"timestamp":"2026-11-12T03:00:00Z"}
```

Ví dụ lỗi: code ERR-PUR-409-11, message “Nguồn đã thay đổi”, details chỉ trường an toàn, requestId để đối soát; không stack hoặc giá.

## Catalog

| API | HTTP | FR | Màn |
| :--- | :--- | :--- | :--- |
| API-PUR-001 | POST /v1/purchasing/demands | FR-PUR-DEM-001 | UI-PUR-01 |
| API-PUR-002 | POST /v1/purchasing/purchase-orders | FR-PUR-POD-001 | UI-PUR-02 |
| API-PUR-003 | GET /v1/purchasing/purchase-orders/{id}/readiness | FR-PUR-POG-001 | UI-PUR-02 |
| API-PUR-004 | GET /v1/purchasing/lot-eligibility | FR-PUR-LOT-001 | UI-PUR-03 |
| API-PUR-005 | POST /v1/purchasing/goods-receipts | FR-PUR-RCV-001 | UI-PUR-03 |
| API-PUR-006 | POST /v1/purchasing/goods-receipts/{id}/evidence | FR-PUR-DOC-001 | UI-PUR-04 |
| API-PUR-007 | GET /v1/purchasing/supplier-balances | FR-PUR-APV-001 | UI-PUR-05 |
| API-PUR-008 | POST /v1/purchasing/purchase-comparisons | FR-COST-BUY-001 | UI-PUR-06 |
| API-PUR-009 | GET /v1/purchasing/purchase-comparisons/{id}/lines | FR-COST-BEX-001 | UI-PUR-06 |
| API-PUR-010 | POST /v1/purchasing/production-shifts | FR-PLAN-SHF-001 | UI-PUR-07 |
| API-PUR-011 | POST /v1/purchasing/pre-delivery-checks | FR-PLAN-QCG-001 | UI-PUR-08 |
| API-PUR-012 | POST /v1/purchasing/retained-samples | FR-PLAN-SMP-001 | UI-PUR-08 |
| API-PUR-013 | POST /v1/purchasing/substitution-candidates | FR-MENU-SUB-001 | UI-PUR-09 |
| API-PUR-014 | POST /v1/purchasing/substitution-checks | FR-MENU-SCK-001 | UI-PUR-09 |
| API-PUR-015 | GET /v1/purchasing/substitution-candidates/{id}/readiness | FR-MENU-SGT-001 | UI-PUR-09 |

## API-PUR-001 — Lập nhu cầu nguyên liệu

- Request logic: planRef, planRevision, estimateRef, serviceDate, kitchenId. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Đối chiếu đúng bản kế hoạch và dự toán; cộng theo nguyên liệu và đơn vị quy đổi đã có căn cứ; hiển thị nguồn thiếu, không tự trừ tồn hoặc áp hao hụt lần hai.
- Response allowlist: Nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định; chỉ trường thuộc demand, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-11 — Chặn tổng hợp khác đơn vị; không coi hệ số là 1. Lỗi chung và version như mục trên.
- Quyền: Kế toán (PER-07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E6 CG06, ORD-Q10/14; E11-Q01. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Nguồn có 100 suất × 70 g, hệ số 1000 g/kg đã xác nhận → Nhu cầu gộp 7000 g = 7 kg; lượng mua ròng chưa xác định.
- Truy vết: FR-PUR-DEM-001; UC-PUR-001; US-PUR-001; UI-PUR-01.

## API-PUR-002 — Lập đơn mua nháp

- Request logic: demandRef, supplierId, lines, reason. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Người lập chọn NCC từ danh mục E3, không có tự chọn; nhập lượng/đơn vị và PriceInput có nguồn; tổng tiền chỉ khi giá đã xác định.
- Response allowlist: Đơn DRAFT, nguồn nhu cầu và giá được giữ; chỉ trường thuộc purchaseOrder, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-12 — Từ chối lưu nháp không hợp lệ; giữ dữ liệu nhập. Lỗi chung và version như mục trên.
- Quyền: Kế toán (PER-07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q01/02/13/14. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: NCC synthetic do người lập chọn, lượng 2 kg; giá cuối 108000 đ/kg → Nháp có tiền hàng 216000 đ khi căn cứ giá đủ; chưa phát hành.
- Truy vết: FR-PUR-POD-001; UC-PUR-002; US-PUR-002; UI-PUR-02.

## API-PUR-003 — Kiểm cổng phát hành đơn mua

- Request logic: purchaseOrderRef, version. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Đọc tình trạng nguồn, quyết định duyệt và policy; thiếu E11-Q02 thì trả BLOCKED. Không mô tả người duyệt hay thuật toán hạn mức.
- Response allowlist: Danh sách điều kiện thiếu, không phát hành; chỉ trường thuộc purchaseOrder, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-13 — Không công nhận trạng thái do client tự khai. Lỗi chung và version như mục trên.
- Quyền: Kế toán (PER-07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q02; O-06. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Đơn nháp chưa có chính sách duyệt → Trả BLOCKED kèm E11-Q02; đơn giữ DRAFT.
- Truy vết: FR-PUR-POG-001; UC-PUR-003; US-PUR-003; UI-PUR-02.

## API-PUR-004 — Kiểm phạm vi quản lý lô

- Request logic: ingredientId, storageType, receiptRef. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Đọc phân loại E2; chỉ FROZEN hoặc DRY thuộc phạm vi lô; quy tắc mã/hạn/xuất còn chờ.
- Response allowlist: Kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật; chỉ trường thuộc lotScope, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-14 — Không tạo lô cho hàng tươi. Lỗi chung và version như mục trên.
- Quyền: Quản lý cơ sở (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q03. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Nguyên liệu thuộc FROZEN hoặc DRY → Hiển thị thuộc phạm vi lô; chi tiết lô còn chờ.
- Truy vết: FR-PUR-LOT-001; UC-PUR-004; US-PUR-004; UI-PUR-03.

## API-PUR-005 — Ghi phiếu nhận hàng nháp

- Request logic: purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Giữ lượng đặt, thực nhận và chấp nhận riêng theo dòng; ghi chứng cứ chênh; không tự hoàn tất đơn hay tăng công nợ chính thức.
- Response allowlist: Phiếu DRAFT có phiên bản và chênh lệch hiển thị; chỉ trường thuộc goodsReceipt, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-15 — Chặn dữ liệu mâu thuẫn, không ghi phiếu. Lỗi chung và version như mục trên.
- Quyền: Quản lý cơ sở (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q04/13. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Đặt 10 kg, nhận 8 kg; người nhận khai chấp nhận 7 kg → Hiện riêng 10/8/7 kg; 1 kg chưa chấp nhận, 2 kg chưa nhận; chưa tự trả hàng.
- Truy vết: FR-PUR-RCV-001; UC-PUR-005; US-PUR-005; UI-PUR-03.

## API-PUR-006 — Gắn ảnh chứng từ vào phiếu

- Request logic: receiptRef, fileRef, version. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Kiểm quyền tệp E1 và cùng phạm vi phiếu; giữ nguồn ảnh và người gắn; mở ảnh không phải xác nhận giá hoặc nhận hàng.
- Response allowlist: Liên kết ảnh nội bộ; trạng thái chứng từ riêng; chỉ trường thuộc receiptEvidence, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-16 — Không lộ nội dung/URL tệp, không gắn chéo. Lỗi chung và version như mục trên.
- Quyền: Quản lý cơ sở (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q05/13; E1-Q01. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Ảnh synthetic thuộc phiếu/cơ sở và MIME hợp lệ theo E1 → Gắn được tham chiếu ảnh; không chuyển phiếu sang đã nhận chính thức.
- Truy vết: FR-PUR-DOC-001; UC-PUR-006; US-PUR-006; UI-PUR-04.

## API-PUR-007 — Xem công nợ nhà cung cấp

- Request logic: supplierId, kitchenId, fromDate, toDate. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Đọc số dư và nguồn được xác nhận; thiếu đầu kỳ/ghi nhận/thanh toán thì trả chưa xác định, không biến phiếu nhận thành đã trả.
- Response allowlist: Bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu; chỉ trường thuộc supplierBalance, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-17 — Không báo tổng công nợ hoàn chỉnh. Lỗi chung và version như mục trên.
- Quyền: Kế toán (PER-07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q06/04. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Có 216000 đ nghĩa vụ và 100000 đ thanh toán có căn cứ, đầu kỳ 0 đã xác nhận → Dư 116000 đ theo fixture đã đủ căn cứ; không giảm bởi CK khách.
- Truy vết: FR-PUR-APV-001; UC-PUR-007; US-PUR-007; UI-PUR-05.

## API-PUR-008 — Đối chiếu dự toán và thực mua

- Request logic: estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Giữ tiền dự toán và thực mua riêng; chỉ so tỷ lệ khi cùng scope, đủ nguồn và có định nghĩa BO-02 được duyệt; thiếu thì không trả đạt.
- Response allowlist: Hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do; chỉ trường thuộc comparison, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-18 — Không ghép với dự toán để kết luận đạt. Lỗi chung và version như mục trên.
- Quyền: Kế toán (PER-07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Fixture minh họa có tỷ lệ cùng mẫu số đã được xác nhận: 50 % và 53 % → Chênh hiển thị 3 điểm phần trăm; không gọi tăng tương đối 6 % là tiêu chí R11.
- Truy vết: FR-COST-BUY-001; UC-PUR-008; US-PUR-008; UI-PUR-06.

## API-PUR-009 — Giải thích nguồn chênh lệch

- Request logic: comparisonRef, ingredientId. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Truy về dòng dự toán, dòng nhận/mua và giá gồm VAT; hiển thị lượng/giá/đơn vị và nguồn. Không tự phân rã tác động giá/lượng nếu chưa chốt phương pháp.
- Response allowlist: Chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn; chỉ trường thuộc comparisonLine, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-403-11 — Không trả tiền hoặc cost trong body/lỗi/log hiển thị. Lỗi chung và version như mục trên.
- Quyền: Giám đốc/Kế toán (PER-08/07) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q07/08/14. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Hai dòng cùng nguyên liệu và đơn vị có nguồn được phép đọc → Hiện lượng và giá hai phía, liên kết chứng từ; không ghi đè dự toán.
- Truy vết: FR-COST-BEX-001; UC-PUR-009; US-PUR-009; UI-PUR-06.

## API-PUR-010 — Lập phân ca nháp

- Request logic: kitchenId, serviceDate, shiftRef, assignments, planRef. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Ghi phân công dự kiến gắn đúng nguồn; không xác nhận đã bắt đầu sản xuất E6, không tự chốt đủ người hoặc giờ ca.
- Response allowlist: Phân ca DRAFT và các điều kiện còn thiếu; chỉ trường thuộc productionShift, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-20 — Từ chối gắn vào ca. Lỗi chung và version như mục trên.
- Quyền: Bếp trưởng (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q09; E6 CG06. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Ca synthetic, phân công công việc cho mã nhân sự giả thuộc scope → Giữ bản nháp; trạng thái bắt đầu sản xuất E6 không đổi.
- Truy vết: FR-PLAN-SHF-001; UC-PUR-010; US-PUR-010; UI-PUR-07.

## API-PUR-011 — Ghi kiểm tra trước giao

- Request logic: shiftRef, checklistRef, results, reason. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Ghi kết quả theo mục đã được duyệt; thiếu checklist hoặc còn mục chưa kiểm thì chưa đủ căn cứ giao. QC không ghi số khách nhận hoặc doanh thu.
- Response allowlist: Phiếu QC nháp và cổng chưa sẵn sàng; chỉ trường thuộc qualityCheck, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-21 — Không kết luận đủ dựa trên tập mục thiếu. Lỗi chung và version như mục trên.
- Quyền: Bếp trưởng (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q10; E7-Q02; E6 CG06. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Checklist mẫu có mục kiểm hộp chưa kiểm → Hiện chưa đủ căn cứ giao; không tự chuyển E7 sang giao thành công.
- Truy vết: FR-PLAN-QCG-001; UC-PUR-011; US-PUR-011; UI-PUR-08.

## API-PUR-012 — Ghi sổ mẫu lưu theo bữa

- Request logic: mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Ghi mẫu và liên kết bữa; phân biệt đã có bản ghi với mẫu hợp lệ theo policy; không tự đặt hạn lưu hay hủy.
- Response allowlist: Sổ mẫu nháp, danh sách bữa thiếu mẫu; chỉ trường thuộc retainedSample, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-22 — Chặn bản ghi không truy được nguồn. Lỗi chung và version như mục trên.
- Quyền: Quản lý cơ sở (PER-06) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q11; E6 CG06. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Tập bữa synthetic đã xác nhận có 10 bữa, 9 bữa có bản ghi mẫu → Độ phủ bản ghi 90 %, liệt kê 1 bữa thiếu; chưa đạt mục tiêu 100 % R11.
- Truy vết: FR-PLAN-SMP-001; UC-PUR-012; US-PUR-012; UI-PUR-08.

## API-PUR-013 — Lập ứng viên món thay thế

- Request logic: menuRef, menuVersion, originalDishId, replacementDishId, reason. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Người dùng chọn món cùng vai trò từ danh mục được phép; ghi thiếu hàng và nguồn; tạo ứng viên DRAFT, không thay thực đơn công bố.
- Response allowlist: Ứng viên nháp có món cũ/mới và vai trò; chỉ trường thuộc substitution, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-23 — Chặn khác vai trò, không tạo thay thế hợp lệ. Lỗi chung và version như mục trên.
- Quyền: Dinh dưỡng viên (PER-05) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q12/15; O-02. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Đổi một món MAIN sang món MAIN đang được phép dùng → Tạo ứng viên DRAFT; thực đơn công bố không đổi.
- Truy vết: FR-MENU-SUB-001; UC-PUR-013; US-PUR-013; UI-PUR-09.

## API-PUR-014 — Kiểm lại ứng viên thay món

- Request logic: candidateRef, candidateVersion, menuSourceRef. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Mỗi lần thay đều yêu cầu kiểm lại dị ứng, quy tắc E2 và cost E3 trên cùng phiên bản; chỉ hiển thị kết quả có provenance; không dùng lại kết quả món cũ.
- Response allowlist: Bộ kết quả hoặc trạng thái BLOCKED kèm nguồn thiếu; chỉ trường thuộc substitutionCheck, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-24 — BLOCKED; không trả đạt dù quy tắc khác đạt. Lỗi chung và version như mục trên.
- Quyền: Dinh dưỡng viên (PER-05) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: DL-01; E11-Q15; O-01/O-02; CK/DATA-COST. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Ứng viên có đủ nhãn dị ứng, rule và giá trong fixture đã duyệt → Có đủ ba kết quả đúng candidateVersion; vẫn chưa được công bố.
- Truy vết: FR-MENU-SCK-001; UC-PUR-014; US-PUR-014; UI-PUR-09.

## API-PUR-015 — Kiểm cổng chuyển duyệt MENU

- Request logic: candidateRef, candidateVersion, checkRefs. Kiểu/nullability theo [từ điển](../srs/data-dictionary.md); wire shape chưa cố định ở phần thiếu nguồn.
- Xử lý: Kiểm đủ kết quả đúng nguồn và cổng MENU hiện hành. CHAN chặn vượt cost; CANH_BAO giữ cảnh báo và vẫn qua MENU; thiếu đầu vào luôn chặn. Không ghi duyệt/công bố hoặc cập nhật E6.
- Response allowlist: Readiness và lý do chặn; việc chuyển thật chờ adapter nguồn; chỉ trường thuộc substitution, không trả nguyên upstream body.
- Lỗi nghiệp vụ: ERR-PUR-422-25 — Không được chuyển như đã đạt; giữ ứng viên. Lỗi chung và version như mục trên.
- Quyền: Dinh dưỡng viên (PER-05) chỉ là vai trò đề xuất; mỗi request kiểm action + kitchen scope.
- Gate: E11-Q12/13; DL-01; E6 CG05/06/07. Phần chưa rõ giữ BLOCKED, không cung cấp thuật toán nguồn.
- Ví dụ synthetic: Kết quả dị ứng, rule, cost đúng phiên bản; MENU vẫn chưa duyệt → Hiện cần qua cổng MENU; không tự công bố hoặc sửa kế hoạch.
- Truy vết: FR-MENU-SGT-001; UC-PUR-015; US-PUR-015; UI-PUR-09.

## Port phụ thuộc

| Port | Ranh giới | Giới hạn |
| :--- | :--- | :--- |
| PORT-PUR-PLAN | E6 → nhu cầu/phân ca | Chỉ tham chiếu bản nguồn; CG06 còn chờ, không thiết kế build/publish/ack/start |
| PORT-PUR-PRICE | Nhận hàng → E3 PriceInput | Q14; không tự cập nhật giá tham chiếu hoặc ghi đè giá hiệu lực |
| PORT-PUR-MENU | Ứng viên → E2 quy tắc/dị ứng và E3 cost | Cùng candidate/version; luôn kiểm lại; chuyển duyệt theo MENU, không tự công bố |
| PORT-PUR-DLV | QC/mẫu → E7 | Q10/E7-Q02; không tạo số nhận/doanh thu hoặc chốt xử lý Q-13 |


PriceInput giữ ingredientId, supplierId, kitchenId, quotedUnitPrice, priceBasis, căn cứ VAT và pricingEvidence theo E3. Không nhận priceVnd như số client được tin cậy. Chưa rõ phần lẻ thì BLOCKED normalization, không tự làm tròn. [Catalog máy đọc](endpoint-catalog.json).
