---
id: DOC-E11-SRS-SPEC-MD
title: "SRS E11: Mua hàng và sản xuất"
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [e11, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# SRS E11: Mua hàng và sản xuất

Nháp có điều kiện · Chưa phê duyệt · 12/11/2026.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở tài liệu E11; giữ câu hỏi chưa có câu trả lời |

## 1. Giới thiệu

Mục đích: đặc tả nháp đúng FEAT-074–078 theo [epic](../epic-spec.md), chuẩn IEEE 830. NCC là nhà cung cấp; QC là kiểm tra trước giao; revision là bản nguồn bất biến, version là token kiểm thay đổi. Đơn mua, phiếu nhận, chứng từ, nghĩa vụ trả và thanh toán là các sự kiện riêng.

## 2. Tổng quan

Web nội bộ desktop/mobile, dữ liệu theo cơ sở. Mọi quyền là đề xuất theo vai trò × cơ sở; chưa tự cấp quyền hoặc chọn người duyệt. Các thao tác có nguồn/policy chưa chốt chỉ mô tả điểm chặn và phần độc lập, không triển khai tiếp producer. Không backend, migration, mô hình AI, commit hoặc xóa file. [Phân quyền và màn](../ui/screens.md); [nguồn và gate](../review/dependencies.md).

## 3.1 Yêu cầu chức năng

| FR / Feature | Tên / Actor | Ưu tiên | Input | Xử lý | Output | BR / ERR | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-PUR-DEM-001 / FEAT-074 | Lập nhu cầu nguyên liệu: Kế toán (PER-07) | P1 | planRef, planRevision, estimateRef, serviceDate, kitchenId | Đối chiếu đúng bản kế hoạch và dự toán; cộng theo nguyên liệu và đơn vị quy đổi đã có căn cứ; hiển thị nguồn thiếu, không tự trừ tồn hoặc áp hao hụt lần hai. | Nhu cầu gộp theo ngày/cơ sở, tách lượng mua ròng chưa xác định | BR-PUR-001 / ERR-PUR-422-11 | E6 CG06, ORD-Q10/14; E11-Q01 |
| FR-PUR-POD-001 / FEAT-074 | Lập đơn mua nháp: Kế toán (PER-07) | P1 | demandRef, supplierId, lines, reason | Người lập chọn NCC từ danh mục E3, không có tự chọn; nhập lượng/đơn vị và PriceInput có nguồn; tổng tiền chỉ khi giá đã xác định. | Đơn DRAFT, nguồn nhu cầu và giá được giữ | BR-PUR-002 / ERR-PUR-422-12 | E11-Q01/02/13/14 |
| FR-PUR-POG-001 / FEAT-074 | Kiểm cổng phát hành đơn mua: Kế toán (PER-07) | P1 | purchaseOrderRef, version | Đọc tình trạng nguồn, quyết định duyệt và policy; thiếu E11-Q02 thì trả BLOCKED. Không mô tả người duyệt hay thuật toán hạn mức. | Danh sách điều kiện thiếu, không phát hành | BR-PUR-003 / ERR-PUR-422-13 | E11-Q02; O-06 |
| FR-PUR-LOT-001 / FEAT-074 | Kiểm phạm vi quản lý lô: Quản lý cơ sở (PER-06) | P1 | ingredientId, storageType, receiptRef | Đọc phân loại E2; chỉ FROZEN hoặc DRY thuộc phạm vi lô; quy tắc mã/hạn/xuất còn chờ. | Kết quả thuộc/không thuộc phạm vi; chưa tạo lô thật | BR-PUR-004 / ERR-PUR-422-14 | E11-Q03 |
| FR-PUR-RCV-001 / FEAT-075 | Ghi phiếu nhận hàng nháp: Quản lý cơ sở (PER-06) | P1 | purchaseOrderRef, lines.receivedQty, lines.acceptedQty, receivedAt, reason | Giữ lượng đặt, thực nhận và chấp nhận riêng theo dòng; ghi chứng cứ chênh; không tự hoàn tất đơn hay tăng công nợ chính thức. | Phiếu DRAFT có phiên bản và chênh lệch hiển thị | BR-PUR-005 / ERR-PUR-422-15 | E11-Q04/13 |
| FR-PUR-DOC-001 / FEAT-075 | Gắn ảnh chứng từ vào phiếu: Quản lý cơ sở (PER-06) | P1 | receiptRef, fileRef, version | Kiểm quyền tệp E1 và cùng phạm vi phiếu; giữ nguồn ảnh và người gắn; mở ảnh không phải xác nhận giá hoặc nhận hàng. | Liên kết ảnh nội bộ; trạng thái chứng từ riêng | BR-PUR-006 / ERR-PUR-422-16 | E11-Q05/13; E1-Q01 |
| FR-PUR-APV-001 / FEAT-075 | Xem công nợ nhà cung cấp: Kế toán (PER-07) | P1 | supplierId, kitchenId, fromDate, toDate | Đọc số dư và nguồn được xác nhận; thiếu đầu kỳ/ghi nhận/thanh toán thì trả chưa xác định, không biến phiếu nhận thành đã trả. | Bảng nghĩa vụ, thanh toán, điều chỉnh riêng và nguồn thiếu | BR-PUR-007 / ERR-PUR-422-17 | E11-Q06/04 |
| FR-COST-BUY-001 / FEAT-076 | Đối chiếu dự toán và thực mua: Kế toán (PER-07) | P1 | estimateRef, purchaseAllocationRefs, date, kitchenId, measurementBasisRef | Giữ tiền dự toán và thực mua riêng; chỉ so tỷ lệ khi cùng scope, đủ nguồn và có định nghĩa BO-02 được duyệt; thiếu thì không trả đạt. | Hai số tiền, hai tỷ lệ, chênh điểm phần trăm hoặc null có lý do | BR-PUR-008 / ERR-PUR-422-18 | E11-Q07/08; O-01; DATA-COST-Q01–06; E7-Q03/04 |
| FR-COST-BEX-001 / FEAT-076 | Giải thích nguồn chênh lệch: Giám đốc/Kế toán (PER-08/07) | P1 | comparisonRef, ingredientId | Truy về dòng dự toán, dòng nhận/mua và giá gồm VAT; hiển thị lượng/giá/đơn vị và nguồn. Không tự phân rã tác động giá/lượng nếu chưa chốt phương pháp. | Chi tiết đối chiếu có provenance, giới hạn và thiếu nguồn | BR-PUR-009 / ERR-PUR-403-11 | E11-Q07/08/14 |
| FR-PLAN-SHF-001 / FEAT-077 | Lập phân ca nháp: Bếp trưởng (PER-06) | P1 | kitchenId, serviceDate, shiftRef, assignments, planRef | Ghi phân công dự kiến gắn đúng nguồn; không xác nhận đã bắt đầu sản xuất E6, không tự chốt đủ người hoặc giờ ca. | Phân ca DRAFT và các điều kiện còn thiếu | BR-PUR-010 / ERR-PUR-422-20 | E11-Q09; E6 CG06 |
| FR-PLAN-QCG-001 / FEAT-077 | Ghi kiểm tra trước giao: Bếp trưởng (PER-06) | P1 | shiftRef, checklistRef, results, reason | Ghi kết quả theo mục đã được duyệt; thiếu checklist hoặc còn mục chưa kiểm thì chưa đủ căn cứ giao. QC không ghi số khách nhận hoặc doanh thu. | Phiếu QC nháp và cổng chưa sẵn sàng | BR-PUR-011 / ERR-PUR-422-21 | E11-Q10; E7-Q02; E6 CG06 |
| FR-PLAN-SMP-001 / FEAT-077 | Ghi sổ mẫu lưu theo bữa: Quản lý cơ sở (PER-06) | P1 | mealRef, kitchenId, sampleCode, recordedAt, recordedBy, evidenceRef | Ghi mẫu và liên kết bữa; phân biệt đã có bản ghi với mẫu hợp lệ theo policy; không tự đặt hạn lưu hay hủy. | Sổ mẫu nháp, danh sách bữa thiếu mẫu | BR-PUR-012 / ERR-PUR-422-22 | E11-Q11; E6 CG06 |
| FR-MENU-SUB-001 / FEAT-078 | Lập ứng viên món thay thế: Dinh dưỡng viên (PER-05) | P1 | menuRef, menuVersion, originalDishId, replacementDishId, reason | Người dùng chọn món cùng vai trò từ danh mục được phép; ghi thiếu hàng và nguồn; tạo ứng viên DRAFT, không thay thực đơn công bố. | Ứng viên nháp có món cũ/mới và vai trò | BR-PUR-013 / ERR-PUR-422-23 | E11-Q12/15; O-02 |
| FR-MENU-SCK-001 / FEAT-078 | Kiểm lại ứng viên thay món: Dinh dưỡng viên (PER-05) | P1 | candidateRef, candidateVersion, menuSourceRef | Mỗi lần thay đều yêu cầu kiểm lại dị ứng, quy tắc E2 và cost E3 trên cùng phiên bản; chỉ hiển thị kết quả có provenance; không dùng lại kết quả món cũ. | Bộ kết quả hoặc trạng thái BLOCKED kèm nguồn thiếu | BR-PUR-014 / ERR-PUR-422-24 | DL-01; E11-Q15; O-01/O-02; CK/DATA-COST |
| FR-MENU-SGT-001 / FEAT-078 | Kiểm cổng chuyển duyệt MENU: Dinh dưỡng viên (PER-05) | P1 | candidateRef, candidateVersion, checkRefs | Kiểm đủ kết quả đúng nguồn và cổng MENU hiện hành. CHAN chặn vượt cost; CANH_BAO giữ cảnh báo và vẫn qua MENU; thiếu đầu vào luôn chặn. Không ghi duyệt/công bố hoặc cập nhật E6. | Readiness và lý do chặn; việc chuyển thật chờ adapter nguồn | BR-PUR-015 / ERR-PUR-422-25 | E11-Q12/13; DL-01; E6 CG05/06/07 |

## 3.2 Quy tắc nghiệp vụ

Mỗi dòng dưới là ràng buộc của FR tương ứng, không tự chốt chính sách ở cột Gate. Không ngoại lệ ngầm.

| BR | KHI | THÌ | Ngoại lệ |
| :--- | :--- | :--- | :--- |
| BR-PUR-001 | Thực hiện lập nhu cầu nguyên liệu | Đối chiếu đúng bản kế hoạch và dự toán; cộng theo nguyên liệu và đơn vị quy đổi đã có căn cứ; hiển thị nguồn thiếu, không tự trừ tồn hoặc áp hao hụt lần hai. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-002 | Thực hiện lập đơn mua nháp | Người lập chọn NCC từ danh mục E3, không có tự chọn; nhập lượng/đơn vị và PriceInput có nguồn; tổng tiền chỉ khi giá đã xác định. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-003 | Thực hiện kiểm cổng phát hành đơn mua | Đọc tình trạng nguồn, quyết định duyệt và policy; thiếu E11-Q02 thì trả BLOCKED. Không mô tả người duyệt hay thuật toán hạn mức. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-004 | Thực hiện kiểm phạm vi quản lý lô | Đọc phân loại E2; chỉ FROZEN hoặc DRY thuộc phạm vi lô; quy tắc mã/hạn/xuất còn chờ. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-005 | Thực hiện ghi phiếu nhận hàng nháp | Giữ lượng đặt, thực nhận và chấp nhận riêng theo dòng; ghi chứng cứ chênh; không tự hoàn tất đơn hay tăng công nợ chính thức. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-006 | Thực hiện gắn ảnh chứng từ vào phiếu | Kiểm quyền tệp E1 và cùng phạm vi phiếu; giữ nguồn ảnh và người gắn; mở ảnh không phải xác nhận giá hoặc nhận hàng. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-007 | Thực hiện xem công nợ nhà cung cấp | Đọc số dư và nguồn được xác nhận; thiếu đầu kỳ/ghi nhận/thanh toán thì trả chưa xác định, không biến phiếu nhận thành đã trả. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-008 | Thực hiện đối chiếu dự toán và thực mua | Giữ tiền dự toán và thực mua riêng; chỉ so tỷ lệ khi cùng scope, đủ nguồn và có định nghĩa BO-02 được duyệt; thiếu thì không trả đạt. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-009 | Thực hiện giải thích nguồn chênh lệch | Truy về dòng dự toán, dòng nhận/mua và giá gồm VAT; hiển thị lượng/giá/đơn vị và nguồn. Không tự phân rã tác động giá/lượng nếu chưa chốt phương pháp. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-010 | Thực hiện lập phân ca nháp | Ghi phân công dự kiến gắn đúng nguồn; không xác nhận đã bắt đầu sản xuất E6, không tự chốt đủ người hoặc giờ ca. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-011 | Thực hiện ghi kiểm tra trước giao | Ghi kết quả theo mục đã được duyệt; thiếu checklist hoặc còn mục chưa kiểm thì chưa đủ căn cứ giao. QC không ghi số khách nhận hoặc doanh thu. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-012 | Thực hiện ghi sổ mẫu lưu theo bữa | Ghi mẫu và liên kết bữa; phân biệt đã có bản ghi với mẫu hợp lệ theo policy; không tự đặt hạn lưu hay hủy. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-013 | Thực hiện lập ứng viên món thay thế | Người dùng chọn món cùng vai trò từ danh mục được phép; ghi thiếu hàng và nguồn; tạo ứng viên DRAFT, không thay thực đơn công bố. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-014 | Thực hiện kiểm lại ứng viên thay món | Mỗi lần thay đều yêu cầu kiểm lại dị ứng, quy tắc E2 và cost E3 trên cùng phiên bản; chỉ hiển thị kết quả có provenance; không dùng lại kết quả món cũ. | Không; thiếu nguồn/policy thì BLOCKED |
| BR-PUR-015 | Thực hiện kiểm cổng chuyển duyệt menu | Kiểm đủ kết quả đúng nguồn và cổng MENU hiện hành. CHAN chặn vượt cost; CANH_BAO giữ cảnh báo và vẫn qua MENU; thiếu đầu vào luôn chặn. Không ghi duyệt/công bố hoặc cập nhật E6. | Không; thiếu nguồn/policy thì BLOCKED |

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả nhà cung cấp và không tự khấu trừ số khách phải trả. NFR-COST-002: cost món lệch ≤ 1 đ; cost % ngày lệch ≤ 0,01 điểm phần trăm. BO-02/R11 dùng ≤ 3 điểm phần trăm, không phải sai số tính toán. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chặn O-03, không thu dữ liệu sức khỏe.

## 3.3 Giao diện ngoài

[API](../api/api-spec.md), [mapping](../api/data-mapping.md), [từ điển dữ liệu đề xuất](data-dictionary.md). E2/E3/E6/E7 chỉ là ranh giới phụ thuộc chưa cố định; không tạo route nguồn hoặc thay DTO nguồn.

## 3.4 Phi chức năng

| NFR | Chỉ tiêu và phương pháp | Gate |
| :--- | :--- | :--- |
| NFR-PUR-001 | 0 truy cập ngoài cơ sở; 0 lộ tiền/giá/ảnh qua response, lỗi hoặc log cho người thiếu quyền; thử từng route với scope A/B | E11-Q13; quyền E1 |
| NFR-PUR-002 | 100% sửa số liệu có actor, thời điểm, trước/sau, lý do; không ghi trùng khi retry; thử fault/concurrency | E11-Q13; không chọn cơ chế persistence |
| NFR-PUR-003 | Kế thừa nền p95 đọc ≤ 300 ms, ghi ≤ 800 ms tại 1000 người đồng thời; profile E11 chưa duyệt | E11-Q13; không lấy 1000 TPS từ mẫu |
| NFR-PUR-004 | Wireframe tại 1440 / 390 / 360 px không tràn ngang trang; mọi trường có nhãn | Chỉ mock, không thay kiểm sản phẩm |
| NFR-PUR-005 | Đối chiếu cost dùng NFR-COST-002: 10 món lệch ≤ 1 đ, 10 ngày lệch ≤ 0,01 điểm phần trăm | DATA-COST-Q01–06; không thay bằng 1 % |

## 3.5 Lỗi

[Ma trận lỗi](error-matrix.md). Mất quyền/nguồn hoặc version xung đột không được báo thành công một phần. GET chỉ đọc, không tính ghi ẩn hoặc phát hành.

## 4. Phụ lục

[Trạng thái](states.md) · [Luồng](../ui/user-flow.md) · [RTM](../test/traceability.md). Schema chung giữ 65 bảng; mọi dữ liệu mới chỉ là delta đề xuất.
