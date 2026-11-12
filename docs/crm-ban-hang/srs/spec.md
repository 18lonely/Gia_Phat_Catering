---
id: DOC-E10-SRS-SPEC-MD
title: SRS E10 — Khách hàng và bán hàng
version: 0.1.0
phase: Specification
domain: Gia Phát
tags: [crm, e10, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# SRS E10 — Khách hàng và bán hàng

Nháp có điều kiện · Chưa phê duyệt, chưa cố định hợp đồng giao tiếp.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở riêng tài liệu E10; giữ mọi quyết định chưa có căn cứ ở trạng thái chờ |

## 1. Giới thiệu

Đặc tả hành vi nháp cho [4 feature](../epic-spec.md). Phân hệ CUS và SALE theo PRD, UC và story dùng CRM để theo dõi chung. FR là yêu cầu chức năng; UC là tình huống sử dụng; AC là tiêu chí chấp nhận; RTM là ma trận truy vết.

## 2. Tổng quan và vai trò

PER-05 là dinh dưỡng viên kiêm chăm sóc khách hàng, PER-07 là kế toán, PER-08 là Giám đốc. Vai trò không tự cấp quyền. Người duyệt gộp/giá/hợp đồng phải được chỉ định; O-06 chưa đóng. Khách chỉ xem bản phát hành thuộc phạm vi của mình sau khi cơ chế truy cập được duyệt. Nền web trên máy tính/điện thoại; không giao tiếp phần cứng.

Nguồn là nháp theo [bảng phụ thuộc](../review/dependencies.md), không cố định hợp đồng nguồn. Chỉ thiết kế miền E10; không đặc tả tiếp cơ chế identity/master/khóa/plan đang chờ ở E6.

## 3.1. Yêu cầu chức năng

| FR / feature | Tên / actor / ưu tiên | Đầu vào | Xử lý | Đầu ra | Phụ thuộc |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR-CUS-VIEW-001 / FEAT-070 | Xem hồ sơ khách hàng 360°; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | customerId, kỳ xem và phạm vi cơ sở | Đọc từng nhóm liên hệ, điểm, hợp đồng, order, doanh thu, phản hồi theo nguồn và quyền; giữ nguồn, thời điểm và độ đầy đủ riêng từng nhóm | Hồ sơ có các nhóm dữ liệu và trạng thái ĐỦ / THIẾU / CHƯA CÓ NGUỒN; không cộng phần chưa xác định thành 0 | E6-CG-01/08; E7-Q03/04/08; E10-Q01 |
| FR-CUS-CONT-001 / FEAT-070 | Ghi nháp thông tin liên hệ CRM; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | customerRef, tên liên hệ, vai trò liên hệ, phương thức liên hệ, nguồn xác minh | Kiểm quyền và dữ liệu tối thiểu theo chính sách được duyệt; lưu bản nháp liên hệ gắn khách tham chiếu, không tạo khách chủ hoặc tài khoản đặt món | Bản nháp liên hệ có version và audit; khách chủ và điểm phục vụ không đổi | E10-Q01; E6-CG-08 |
| FR-CUS-LEAD-001 / FEAT-070 | Tiếp nhận đề xuất từ website và E9; Dịch vụ tiếp nhận được cấp quyền; nhân viên chăm sóc khách theo dõi; P1 | sourceSystem, sourceRef, sourceRevision, sourceHash, contactRef, consentRef, safeMenuRef nếu có | Kiểm giao tiếp đầu nhận đã được duyệt, chống trùng theo nguồn và revision; chỉ lưu nội dung được phép; cấp receipt sau ghi bền vững; nhân viên phân loại sau tiếp nhận | Phiếu tiếp nhận và receipt của E10, chưa phải khách chủ hoặc hợp đồng; không trả dữ liệu nội bộ về E8/E9 | E8-Q06/07/12; E9-Q06/10/13; E10-Q13 |
| FR-CUS-DUP-001 / FEAT-070 | Lập đề nghị rà khách nghi trùng; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | cặp customerRef, bằng chứng nghi trùng, nguồn và version của hai hồ sơ | Chỉ áp tiêu chí phát hiện sau quyết định E10-Q02; hiện chỉ thiết kế khung danh sách và bằng chứng. Nhân viên mở cặp để đối chiếu, đề nghị giữ hồ sơ nào và từng trường; không tự gộp | Đề nghị chờ duyệt với bản so sánh, nguồn và tập tham chiếu chịu tác động | E10-Q02/03; E6-CG-08 |
| FR-CUS-MRG-001 / FEAT-070 | Duyệt đề nghị gộp khách; Người duyệt gộp được chỉ định; P1 | reviewId, baseVersions, quyết định, lựa chọn trường và lý do | Người thật xem diff và tác động; kiểm quyền, tách người lập/sửa cuối với người duyệt theo đề xuất; chỉ thực hiện khi quyền sở hữu mã và cơ chế tham chiếu đã được duyệt; lưu ánh xạ và ảnh trước gộp nguyên tử | Quyết định, nhật ký gộp, liên kết truy nguyên; không xóa hồ sơ gốc hoặc sửa snapshot tài chính | E10-Q03/04; E6-CG-08; O-06 |
| FR-CUS-UNDO-001 / FEAT-070 | Hoàn tác một lần gộp khách; Người duyệt hoàn tác được chỉ định; P1 | mergeRef, versions hiện tại, lý do, bằng chứng và phân tích liên kết phát sinh sau gộp | Đọc ảnh trước gộp và diff hiện tại; lập phương án hoàn tác có người duyệt. Phải xử lý tham chiếu phát sinh theo quyết định Q04; ghi bù có liên kết tới lần gộp, không xóa audit hoặc tái tính giao dịch quá khứ | Bản hoàn tác có audit hoặc danh sách xung đột cần xử lý; hồ sơ lịch sử vẫn truy nguyên | E10-Q03/04; E6-CG-08 |
| FR-CUS-LIFE-001 / FEAT-071 | Xem và đề nghị đổi vòng đời khách; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | customerRef, trạng thái hiện tại, trạng thái đề nghị, evidenceRef, reason, version | Đối chiếu ma trận chuyển đã duyệt với bằng chứng lịch phục vụ từng điểm; giữ sự kiện và actor; không suy khách rời từ một ngày không có order; tín hiệu rủi ro khác quyết định chuyển vòng đời | Sự kiện vòng đời có căn cứ và lịch sử; nhánh không đủ căn cứ giữ trạng thái cũ | E10-Q05/06; E6-CG-05/06/08 |
| FR-CUS-RISK-001 / FEAT-071 | Rà tín hiệu nguy cơ rời theo lịch điểm; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | customerRef, khoảng quan sát, lịch điểm có phiên bản, sự kiện phục vụ có nguồn | Đọc kết quả đánh giá đã có với nguồn và mức đầy đủ; chỉ đánh giá các kỳ phục vụ dự kiến, loại ngày nghỉ đã xác nhận theo policy. Không tự đặt số ngày, trọng số, ngưỡng hoặc suy thiếu dữ liệu là không phát sinh | Tín hiệu có lý do, lịch/nguồn, hoặc CHƯA ĐỦ DỮ LIỆU; GET không chạy tác vụ đánh giá | E10-Q06; E6-CG-03/05/06/08; E7-Q02/03; Q-13 |
| FR-SALE-OPP-001 / FEAT-072 | Quản lý cơ hội và phễu bán hàng; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | opportunityRef nếu đã có, customerOrIntakeRef, stage đề nghị, ownerRef, evidenceRef, version | Tạo cơ hội nháp hoặc ghi sự kiện chuyển giai đoạn sau kiểm policy; giữ chủ cơ hội, lịch sử, nguồn thắng/thua; đếm theo cơ hội duy nhất và cùng kỳ/cohort, không coi mọi lead là cơ hội đã đủ điều kiện | Cơ hội và lịch sử giai đoạn; bảng phễu nêu định nghĩa mẫu số, thiếu thì chưa tính tỷ lệ | E10-Q07/08; E6-CG-08 |
| FR-SALE-QUOT-001 / FEAT-072 | Soạn phiên bản báo giá; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | quoteRef và baseRevision chỉ khi sửa báo giá đã có; opportunityRef, dòng loại suất/giá, điều kiện, hiệu lực đề nghị | Lần đầu không có quoteRef/baseRevision thì tạo báo giá và revision đầu cùng giao dịch; lần sửa bắt buộc cả hai, tạo revision mới từ bản gốc, giữ diff và liên hệ cơ hội; không sửa bản đã phát hành. Giá, VAT và điều kiện phải có căn cứ; phần tính margin chỉ nội bộ và không tự chọn công thức | Phiên bản nháp mới; bản phát hành cũ bất biến, trạng thái duyệt không tự sao chép | E10-Q08/15; O-01; CK-Q01–10 |
| FR-SALE-MENU-001 / FEAT-072 | Đính kèm thực đơn có phiên bản vào báo giá; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | quoteRevision, menuRef, menuRevision, sourceHash, phạm vi dùng cho khách | Kiểm quyền và nguồn MENU được phép theo Q09; chụp projection khách gắn đúng revision báo giá; thực đơn E9 chỉ là đề xuất cần người thật xử lý, không coi receipt là MENU được duyệt | Tệp/nội dung thực đơn được phép và provenance; không tự sửa MENU hoặc dùng bản hiện hành động | E10-Q09; E9-Q06/12; O-02; NUTR-Q01–04; E8-Q04 |
| FR-SALE-SAFE-001 / FEAT-072 | Duyệt và tạo bản báo giá dành cho khách; Người duyệt báo giá được chỉ định; nhân viên chăm sóc khách; P1 | quoteRevision, expectedHash, quyết định duyệt, evidenceRef, recipientScope | Kiểm người duyệt, hiệu lực và nguồn; tạo projection allowlist riêng tại server rồi lưu bản phát hành. Cost và margin chỉ người nội bộ có quyền riêng đọc; không nhúng rồi ẩn CSS. Phiên này không gửi thư/tin nhắn cho khách | Bản phát hành có hash và revision chỉ gồm trường khách được phép; lỗi không lộ cost | E10-Q08/09/13; O-06 |
| FR-SALE-CONT-001 / FEAT-073 | Lập hợp đồng từ báo giá được chấp thuận; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | customerRef, quoteRevision, acceptanceEvidenceRef, draftTerms, fileRefs | Đối chiếu bằng chứng khách chấp thuận đúng revision và quyền lập; tạo hợp đồng DRAFT tham chiếu báo giá bất biến. Không lấy việc xem/tải báo giá làm chấp thuận hoặc chữ ký; nhập hợp đồng hiện hữu theo nguồn riêng sau Q10 | Hợp đồng nháp có nguồn và các dòng giá đề nghị; chưa hiệu lực, không tạo order | E10-Q08/10/11; E6-CG-08 |
| FR-SALE-ACTV-001 / FEAT-073 | Kích hoạt hợp đồng và giá theo loại suất; Người duyệt hợp đồng được chỉ định; P1 | contractVersion, amendmentRef/amendmentVersion nếu kích hoạt phụ lục, signatureEvidenceRef, priceLines theo mealTypeRef, effectiveFrom, effectiveTo, salePriceBasis, vatRatePct | Kiểm bằng chứng, quyền duyệt và hiệu lực; phụ lục phải thuộc hợp đồng trong path và đúng version. Kiểm không chồng khoảng giá ACTIVE theo customer + mealType như nguồn hiện có; kiểm nguyên tử khi cạnh tranh. Chưa chốt quy ước biên ngày không kích hoạt | Hợp đồng và bộ giá hiệu lực nhất quán, audit và nguồn phụ lục; không ghi giá ngược vào order đã chụp | E10-Q10/11/12; O-01; CK-Q01–10; E6-CG-08 |
| FR-SALE-AMND-001 / FEAT-073 | Lập phụ lục thay đổi giá; Dinh dưỡng viên kiêm chăm sóc khách hàng; P1 | contractRef, baseVersion, predecessorPriceRefs, giá đề nghị, from/to, reason, evidenceRef | Lưu phụ lục DRAFT và quan hệ bản trước/bản sau, giữ nội dung giá cũ bất biến. Khi được duyệt phải kiểm cùng quy tắc ACTV và không chồng lấn; sửa hồi tố và tác động đơn đã khóa chờ Q12, không tự mở kỳ | Phụ lục nháp và diff lịch sử; không sửa giá hoặc snapshot order cũ | E10-Q10/11/12; E6-CG-04/05/07; E7-Q05 |
| FR-SALE-PRIC-001 / FEAT-073 | Tra giá hợp đồng cho thời điểm phục vụ; Dịch vụ order được cấp quyền; kế toán tra cứu; P1 | customerRef, mealTypeRef, serviceDate, sourceScope đã xác minh | Chỉ đọc bộ giá đã có hiệu lực theo quy ước được duyệt; trả priceTermRef, contract/amendmentRef, version, căn cứ VAT. Không tự chụp giá vào order; adapter E6/Cost phải được duyệt riêng | Một kết quả có nguồn hoặc UNRESOLVED; không dùng giá hiện tại thay snapshot lịch sử | E10-Q11/12/13; E6-CG-04/05/07/08/11; CK-Q01–10 |

Mọi FR chịu BR-CRM-001/002/011/012 và lỗi chung 400/401/403/404/409/422/500/503 trong [ma trận lỗi](error-matrix.md). Gộp/hoàn tác thêm BR-CRM-003/004; vòng đời thêm 005; báo giá thêm 006/007/010; hợp đồng thêm 008/009/010.

## 3.2. Quy tắc nghiệp vụ

| Mã | Phạm vi | Khi / thì / ngoại lệ |
| :--- | :--- | :--- |
| BR-CRM-001 | Phạm vi và quyền | KHI đọc/ghi THÌ kiểm actor và quyền trên khách/cơ sở từ server; không tin scope client; không ngoại lệ do biết ID. Không có ngoại lệ ngầm. |
| BR-CRM-002 | Nguồn và thiếu dữ liệu | KHI nguồn thiếu/cũ THÌ ghi trạng thái cùng provenance, null không bằng 0; không dùng số giao tự tính doanh thu. Không có ngoại lệ ngầm. |
| BR-CRM-003 | Gộp có duyệt | KHI nghi trùng THÌ chỉ lập đề nghị; tiêu chí chưa duyệt thì không chạy phát hiện. Gộp có người thật duyệt và ảnh trước, không xóa khách gốc. Không có ngoại lệ ngầm. |
| BR-CRM-004 | Hoàn tác | KHI hoàn tác THÌ ghi sự kiện bù có người duyệt và kiểm tham chiếu mới; không xóa audit hoặc sửa snapshot tài chính. Không có ngoại lệ ngầm. |
| BR-CRM-005 | Lịch phục vụ | KHI đánh giá nguy cơ rời THÌ dùng kỳ phục vụ dự kiến của từng điểm và ngoại lệ đã duyệt; không order ngoài lịch không là bằng chứng rời. Không có ngoại lệ ngầm. |
| BR-CRM-006 | Phiên bản | KHI sửa báo giá đã phát hành THÌ tạo revision nháp mới; giữ bản cũ, nguồn và bằng chứng khách đã nhận. Không có ngoại lệ ngầm. |
| BR-CRM-007 | Projection khách | KHI xuất báo giá cho khách THÌ chỉ allowlist ở server; không cost, giá nhập, margin, tỷ lệ cost hoặc nội dung nội bộ trong JSON/HTML/tệp/lỗi/log/cache. Không có ngoại lệ ngầm. |
| BR-CRM-008 | Giá hiệu lực | KHI kích hoạt giá THÌ không chồng khoảng ACTIVE trên customer + mealType; kiểm cả giao dịch đồng thời. Quy ước biên ngày chưa duyệt thì chặn kích hoạt. Không có ngoại lệ ngầm. |
| BR-CRM-009 | Phụ lục | KHI đổi giá THÌ giữ lịch sử phụ lục và nguồn bản trước; không hồi tố snapshot order hoặc tự mở kỳ E7. Không có ngoại lệ ngầm. |
| BR-CRM-010 | Kế toán | Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ không yêu cầu hóa đơn là cờ riêng, không đồng nghĩa VAT 0%. CK% và tiền suất riêng theo đơn là khoản riêng, không làm giảm số phải trả nhà cung cấp; không tự khấu trừ vào tiền khách phải trả. Không thay CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002. Không có ngoại lệ ngầm. |
| BR-CRM-011 | Receipt và cạnh tranh | KHI ghi THÌ lưu nghiệp vụ/audit/receipt nguyên tử; cùng khóa và nội dung trả bản cũ theo quyền hiện tại, khác nội dung báo xung đột; mất phản hồi không là chưa ghi. Không có ngoại lệ ngầm. |
| BR-CRM-012 | Gate | KHI chưa có quyết định bắt buộc THÌ nhánh giữ BLOCKED; receipt lead không là duyệt thực đơn hoặc ký hợp đồng. Không miễn G-Next. Không có ngoại lệ ngầm. |

## 3.3. Giao diện ngoài

[API](../api/api-spec.md), [mapping](../api/data-mapping.md), [màn hình](../ui/screens.md). Nội bộ xem cost và margin phải có quyền riêng. Khách, website và AIN không được nhận các trường này, kể cả người hỏi có quyền nội bộ ở kênh khác. Không có thao tác gửi thư/tin nhắn thật trong tài liệu/mock.

## 3.4. Yêu cầu phi chức năng

| Mã | Tiêu chí | Kiểm / gate |
| :--- | :--- | :--- |
| NFR-CRM-001 | 0 trường cost/margin/giá nhập lọt projection khách, lỗi hoặc cache; kiểm phạm vi từng request | TC-CRM-S001; S002; S003 |
| NFR-CRM-002 | 100% thay đổi/gộp/hoàn tác có actor, thời điểm, trước/sau, lý do, requestId; audit bất biến | TC-CRM-S004 |
| NFR-CRM-003 | 0 khoảng giá chồng ACTIVE; 0 snapshot lịch sử bị viết lại khi đổi phụ lục | TC-CRM-S005; S006 |
| NFR-CRM-004 | Kế thừa nền 1000 người đồng thời; p95 đọc ≤ 300 ms, ghi ≤ 800 ms, không đồng nhất người đồng thời với giao dịch/giây | TC-CRM-S008 BLOCKED E10-Q13/O-04 về profile và dữ liệu tải |
| NFR-CRM-005 | 1440, 390, 360 px không tràn toàn trang; có nhãn và focus bàn phím; mục tiêu WCAG 2.1 AA theo nền | TC-CRM-S009; kiểm mock riêng không thay kiểm sản phẩm |
| NFR-CRM-006 | Dữ liệu liên hệ tối thiểu, không secret trong log; xóa/lưu theo policy được duyệt; TLS theo nền | TC-CRM-S010 BLOCKED E10-Q01; không tự đặt retention |

## 4. Phụ lục

[Từ điển](data-dictionary.md) · [Trạng thái](states.md) · [UC](../usecases/index.md) · [RTM](../test/traceability.md). E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04 đều giữ trạng thái chờ tại sổ nguồn. Không hỏi lại, tự trả lời hoặc quyết định thay.
