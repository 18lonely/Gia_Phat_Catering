---
id: DOC-DECISION-PACK-CONSISTENCY
title: Rà nhất quán liên epic
version: 0.1.1
phase: Review
domain: Gia Phát
tags: [decision-pack, draft, review]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Rà nhất quán liên epic

Nháp · 13/11/2026 · Chuẩn bị quyết định, chưa phê duyệt.

| Phiên bản | Ngày | Vai trò | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 13/11/2026 | BA | XC-01–12: trạng thái xử lý |
| 0.1.0 | 13/11/2026 | BA | Hợp nhất nguồn để review; giữ câu mở |

## Phạm vi và cách kiểm

Quét tự động [scan-cross-epic.cjs](validation/scan-cross-epic.cjs): mã FR/BR/NFR/ERR/UC tại hàng định nghĩa đầu cột hoặc heading UC trong SRS/usecase; bỏ bảng truy vết. Endpoint so method + path, path độc lập method, chuẩn hóa tên biến đường dẫn và so FR để tìm chức năng chung. Port được đọc riêng cùng catalog; không coi port là HTTP. Quét không suy rằng mã tham chiếu lại là khai báo trùng.

Kết quả: 1048 vị trí mã; 302 bản ghi endpoint/port; **0 ứng viên trùng tự động**. [Kết quả máy](validation/cross-epic-result.json). Đây là giới hạn tìm kiếm có cấu trúc; không chứng minh ngữ nghĩa hoàn toàn nhất quán.

Kiểm thủ công: đọc bảy từ điển E7–E13, mapping E9 được từ điển dẫn tới; đối chiếu tên với 65 bảng trong DBML; so các trường reference/version/giá và các producer/consumer có cùng chức năng. Đọc đoạn E3/E7 làm gốc và các câu hỏi/dependency E11–E13. Các phát hiện dưới ghi rõ vị trí, không sửa nguồn.

## Phát hiện

## XC-01 — O-01 về VAT đầu vào còn diễn đạt cũ trong ERD

Mức: **Cao**. ERD còn hỏi giá nhập có gồm VAT đầu vào; xác nhận kế toán E3 và dependency E13 đã nêu cost gồm VAT phải trả. Đây là phần có câu trả lời ngầm, cần xác nhận phạm vi O-01 còn mở; VAT bán ra và khoản khoán chưa được đóng.

Nguồn và dòng:

- [docs/nen-tang/srs/erd.md:580](../../../nen-tang/srs/erd.md#L580).
- [docs/cost/accounting/business-rules.md:18](../../../cost/accounting/business-rules.md#L18).
- [docs/chi-phi-loi-nhuan/review/dependencies.md:31](../../../chi-phi-loi-nhuan/review/dependencies.md#L31).

Đề xuất xử lý: Ở phiên có quyết định ký, đánh dấu phần VAT đầu vào đã có căn cứ và sửa diễn đạt cũ theo CR; giữ các nhánh O-01 chưa trả lời. Gốc ưu tiên: ACC-CONF-02 của E3.

Cần xác nhận: Kế toán, BA. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **ĐÃ SỬA** — loại A; Chỉ sửa VAT đầu vào theo ACC-CONF-02; giữ O-01 mở. Xem [kết quả XC-01](followup-2026-11-13/xc-resolution.md).

## XC-02 — Các mẫu số cost không được thay thế nhau

Mức: **Cao**. E3 định nghĩa cost suất trên doanh thu chưa VAT; E11 hỏi mẫu số BO-02; E12 hỏi tập ghép/trọng số theo khách; E13 hỏi thành phần kết quả kinh doanh. Các chỉ số có liên quan nhưng chưa có ánh xạ được duyệt. Không phát hiện căn cứ để coi chúng là cùng một tỷ lệ.

Nguồn và dòng:

- [docs/cost/srs/spec.md:64](../../../cost/srs/spec.md#L64).
- [docs/mua-hang-san-xuat/review/questions.md:32](../../../mua-hang-san-xuat/review/questions.md#L32).
- [docs/phan-hoi-bao-cao/review/questions.md:32](../../../phan-hoi-bao-cao/review/questions.md#L32).
- [docs/chi-phi-loi-nhuan/review/questions.md:32](../../../chi-phi-loi-nhuan/review/questions.md#L32).

Đề xuất xử lý: Lập bảng định nghĩa nguồn và bộ đối chiếu cùng phạm vi sau khi từng câu được ký. Dùng E3 làm gốc cost/VAT/chiết khấu, E7 làm gốc doanh thu. BO-01 ≤ 52 % và BO-02 ≤ 3 điểm phần trăm không phải dung sai NFR-COST-002.

Cần xác nhận: Kế toán, Giám đốc, chủ dashboard. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-02](followup-2026-11-13/xc-resolution.md).

## XC-03 — Doanh thu E13 phụ thuộc số tính tiền và VAT E7 còn mở

Mức: **Cao**. E13 yêu cầu doanh thu đã đối soát có revision; E7 chưa chốt số tính tiền, căn cứ VAT và dung sai đối chiếu. Bản snapshot đề xuất không chứng minh doanh thu chính thức đã đủ nguồn.

Nguồn và dòng:

- [docs/giao-nhan-doanh-thu/review/questions.md:21](../../../giao-nhan-doanh-thu/review/questions.md#L21).
- [docs/giao-nhan-doanh-thu/review/questions.md:22](../../../giao-nhan-doanh-thu/review/questions.md#L22).
- [docs/chi-phi-loi-nhuan/review/dependencies.md:24](../../../chi-phi-loi-nhuan/review/dependencies.md#L24).

Đề xuất xử lý: Giữ gate R13; sau quyết định E7 mới chuẩn hóa hợp đồng đọc doanh thu và evidence. Không suy số tính tiền từ số giao/nhận. Không mượn dung sai Cost cho R7/R13.

Cần xác nhận: Kế toán, Giám đốc. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-03](followup-2026-11-13/xc-resolution.md).

## XC-04 — Tên và kiểu version/định danh ở delta chưa thống nhất

Mức: **Trung bình**. E11 dùng Integer, E12 dùng opaque token, E13 dùng INTEGER và chọn BIGINT UNSIGNED đề xuất; E10 chưa chọn khóa vật lý mới. Đây là khác mức trừu tượng, chưa chứng minh mâu thuẫn runtime. Nếu consumer ép version thành số thì mất tính opaque.

Nguồn và dòng:

- [docs/mua-hang-san-xuat/srs/data-dictionary.md:34](../../../mua-hang-san-xuat/srs/data-dictionary.md#L34).
- [docs/phan-hoi-bao-cao/srs/data-dictionary.md:45](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L45).
- [docs/chi-phi-loi-nhuan/srs/data-dictionary.md:23](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L23).

Đề xuất xử lý: Tech lead xác nhận kiểu wire và mapping riêng từng nguồn; không đổi schema 65 bảng. Thống nhất quy ước reference/revision/version trước freeze.

Cần xác nhận: Tech lead, chủ dữ liệu E10–E13. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **ĐÃ SỬA** — loại B; Đã thống nhất cách mô tả; mapping wire vẫn BLOCKED theo câu contract E7–E13. Xem [kết quả XC-04](followup-2026-11-13/xc-resolution.md).

## XC-05 — Lead và proposal xuất hiện ở ba delta

Mức: **Trung bình**. Ba cấu trúc có contact/consent/source/receipt cùng chức năng tiếp nhận nhưng khác producer và vòng đời. Chưa có tên bảng vật lý trùng chính xác; vẫn có nguy cơ ghi nhiều bản cho một nguồn hoặc coi receipt là duyệt.

Nguồn và dòng:

- [docs/website-cong-khai/srs/data-dictionary.md:23](../../../website-cong-khai/srs/data-dictionary.md#L23).
- [docs/agent-dinh-duong-vien/api/data-mapping.md:29](../../../agent-dinh-duong-vien/api/data-mapping.md#L29).
- [docs/crm-ban-hang/srs/data-dictionary.md:44](../../../crm-ban-hang/srs/data-dictionary.md#L44).

Đề xuất xử lý: Xác nhận nguồn chủ, khóa bàn giao và phạm vi consent qua E8-Q06, E9-Q06/10, E10-Q13. Giữ các delta độc lập cho đến khi có quyết định; không tự gộp bảng.

Cần xác nhận: Kinh doanh, phụ trách dữ liệu, Tech lead. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-05](followup-2026-11-13/xc-resolution.md).

## XC-06 — Đồng ý nhật ký khác đồng ý sức khỏe; bữa đã ăn cần evidence riêng

Mức: **Cao**. Nguồn đã phân biệt FEAT-087 phi y tế với FEAT-046/047/063. Đây là câu trả lời ngầm về ranh giới, cần xác nhận; không trả lời consent/retention hoặc bằng chứng đã ăn. Chọn món, giao hàng và nhận hàng không chứng minh cá nhân đã ăn.

Nguồn và dòng:

- [docs/phan-hoi-bao-cao/review/questions.md:39](../../../phan-hoi-bao-cao/review/questions.md#L39).
- [docs/phan-hoi-bao-cao/review/questions.md:41](../../../phan-hoi-bao-cao/review/questions.md#L41).
- [docs/phan-hoi-bao-cao/review/dependencies.md:37](../../../phan-hoi-bao-cao/review/dependencies.md#L37).
- [docs/agent-dinh-duong-vien/review/questions.md:31](../../../agent-dinh-duong-vien/review/questions.md#L31).

Đề xuất xử lý: Giữ nhóm O-03 riêng; trình E12-Q15/16/17 theo chính sách nhật ký. Không mở thu thập sức khỏe, không suy đã ăn từ E6/E7.

Cần xác nhận: Giám đốc, phụ trách dữ liệu, Dinh dưỡng viên. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-06](followup-2026-11-13/xc-resolution.md).

## XC-07 — Người duyệt trong các epic mới vẫn chưa được O-06 chỉ định

Mức: **Trung bình**. Tách người lập/người sửa cuối khỏi người duyệt là nguyên tắc nền. Các epic mới đã mô tả approval nhưng người duyệt, hạn mức và người thay còn mở; không thể dùng tên persona để tự cấp quyền.

Nguồn và dòng:

- [docs/mua-hang-san-xuat/review/questions.md:26](../../../mua-hang-san-xuat/review/questions.md#L26).
- [docs/chi-phi-loi-nhuan/review/questions.md:34](../../../chi-phi-loi-nhuan/review/questions.md#L34).
- [docs/crm-ban-hang/review/questions.md:27](../../../crm-ban-hang/review/questions.md#L27).
- [docs/nen-tang/srs/spec.md:401](../../../nen-tang/srs/spec.md#L401).

Đề xuất xử lý: Trình ma trận theo nghiệp vụ trong nhóm O-06; ghi phạm vi từng chữ ký. Các vai trò chỉ tham gia review chưa được tính là người có quyền quyết định.

Cần xác nhận: Giám đốc, BA. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-07](followup-2026-11-13/xc-resolution.md).

## XC-08 — Hai chức năng dựng thực đơn public có khả năng dùng chung

Mức: **Trung bình**. Quét path/method không thấy trùng, nhưng FEAT-057 và FEAT-060 cùng dựng thực đơn public; E9-Q11 đã hỏi dùng chung hay tách bộ dựng/port kiểm. Khác URL không chứng minh khác chức năng.

Nguồn và dòng:

- [docs/website-cong-khai/review/questions.md:22](../../../website-cong-khai/review/questions.md#L22).
- [docs/agent-dinh-duong-vien/review/questions.md:28](../../../agent-dinh-duong-vien/review/questions.md#L28).
- [docs/website-cong-khai/api/endpoint-catalog.json:102](../../../website-cong-khai/api/endpoint-catalog.json#L102).
- [docs/agent-dinh-duong-vien/api/endpoint-catalog.json:29](../../../agent-dinh-duong-vien/api/endpoint-catalog.json#L29).

Đề xuất xử lý: Review quyết định dùng chung port kiểm hay bộ dựng riêng, giữ quyền và quota từng agent. Không tự hợp nhất endpoint hoặc dùng credential AIO cho AIN.

Cần xác nhận: Tech lead, Dinh dưỡng viên, chủ website. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-08](followup-2026-11-13/xc-resolution.md).

## XC-09 — Dữ liệu giá có phần lẻ và giá cost nguyên đồng còn gate

Mức: **Trung bình**. E10 giữ quoted_unit_price decimal(18,6), E11 có giá cost Integer money và phần lẻ chờ review, E13 chưa chọn precision/làm tròn/phần dư. Các trường khác nghĩa nên không kết luận trùng kiểu sai; cần mapping để tránh cắt phần lẻ khi truyền nguồn.

Nguồn và dòng:

- [docs/crm-ban-hang/srs/data-dictionary.md:30](../../../crm-ban-hang/srs/data-dictionary.md#L30).
- [docs/mua-hang-san-xuat/srs/data-dictionary.md:40](../../../mua-hang-san-xuat/srs/data-dictionary.md#L40).
- [docs/chi-phi-loi-nhuan/review/questions.md:33](../../../chi-phi-loi-nhuan/review/questions.md#L33).

Đề xuất xử lý: Chốt chuẩn hóa PriceInput và quy tắc làm tròn từng chỉ số theo nguồn. Giữ NFR-COST-002 ≤ 1 đ và ≤ 0,01 điểm phần trăm, không dùng làm quy tắc làm tròn mọi tiền.

Cần xác nhận: Kế toán, Tech lead. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-09](followup-2026-11-13/xc-resolution.md).

## XC-10 — Chiết khấu riêng chưa có chính sách đưa vào lợi nhuận

Mức: **Trung bình**. E3 giữ khoản chiết khấu riêng theo đơn; E13 hỏi cách ghi vào kết quả kinh doanh. Không có xung đột trực tiếp đã chứng minh, nhưng không thể tự trừ CK khỏi doanh thu hoặc phải trả NCC để tạo lợi nhuận.

Nguồn và dòng:

- [docs/cost/accounting/business-rules.md:95](../../../cost/accounting/business-rules.md#L95).
- [docs/cost/accounting/business-rules.md:99](../../../cost/accounting/business-rules.md#L99).
- [docs/chi-phi-loi-nhuan/review/dependencies.md:37](../../../chi-phi-loi-nhuan/review/dependencies.md#L37).

Đề xuất xử lý: Kế toán xác nhận kỳ ghi nhận, trạng thái xử lý và cách chống đếm đôi. Giữ nguyên phải trả NCC và không tự khấu trừ tiền khách.

Cần xác nhận: Kế toán, Giám đốc. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-10](followup-2026-11-13/xc-resolution.md).

## XC-11 — MISA chỉ có câu nguồn E7; không tạo quyết định xuất MISA cho E11/E13

Mức: **Thấp**. E7 hỏi mẫu nhập MISA; E13 chỉ hỏi export nội bộ; E11 phân biệt công nợ NCC với phải thu khách. Không thấy căn cứ trong sổ để gộp cả ba thành một quyết định MISA.

Nguồn và dòng:

- [docs/giao-nhan-doanh-thu/review/questions.md:25](../../../giao-nhan-doanh-thu/review/questions.md#L25).
- [docs/mua-hang-san-xuat/review/dependencies.md:26](../../../mua-hang-san-xuat/review/dependencies.md#L26).
- [docs/chi-phi-loi-nhuan/review/questions.md:36](../../../chi-phi-loi-nhuan/review/questions.md#L36).

Đề xuất xử lý: Giữ E7-Q07 riêng; BA hỏi lại phạm vi chỉ khi có nhu cầu xuất khác được xác nhận. Không tự đặt định dạng file, mapping hay nhà cung cấp.

Cần xác nhận: Kế toán, BA. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-11](followup-2026-11-13/xc-resolution.md).

## XC-12 — E1 và E5 diễn giải thời gian phản hồi đầu khác nhau

Mức: **Trung bình**. E1 ghi ký tự đầu trong 5 giây; ghi chú E1 nêu polling E5 và đề xuất hiểu là phản hồi tiến trình đầu, không phải token đầu. Đây mới là đề xuất, không tự sửa NFR gốc.

Nguồn và dòng:

- [docs/nen-tang/review/questions.md:28](../../../nen-tang/review/questions.md#L28).
- [docs/agent-noi-bo/review/questions.md:13](../../../agent-noi-bo/review/questions.md#L13).

Đề xuất xử lý: Tech lead và QA xác nhận cách đo sau khi O-04/AIO-Q01 có nguồn. Giữ giới hạn phản hồi và thời gian dựng thực đơn là hai chỉ số riêng.

Cần xác nhận: Tech lead, QA, Giám đốc. Cách kiểm: Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.

Trạng thái: **CHỜ QUYẾT ĐỊNH** — loại C; Không chọn phương án; câu tương đương hiện có được tái dùng, không tạo mã trùng. Xem [kết quả XC-12](followup-2026-11-13/xc-resolution.md).

## Danh mục delta ngoài schema

59 dòng thực thể/nhóm đề xuất được liệt kê dưới, kèm toàn bộ trường riêng từ nguồn. [Bản máy](validation/delta-inventory.json). Không có tên vật lý đề xuất giống hệt nhau giữa các epic trong danh mục này. Các trường cùng nghĩa khác tên/kiểu và chức năng chồng nhau xem XC-04, XC-05, XC-09. E7 tái dùng approvals/change_requests là nguồn nền, không phải bảng mới. Tên ghép có dấu “/” là nhóm logic chưa chốt số bảng.

### E7 — e7_delivery_notes

[Nguồn, dòng 18](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L18). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id ID; orderId ID; orderRevisionRef/planRevisionRef opaque; deliveredServings int; state; version int; evidenceRef | PK id; orderId→orders; số giao≥0; nguồn bắt buộc theo policy đã xác nhận; không dùng thiếu=0 | CG05/06/08; Q02

### E7 — e7_receipt_confirmations

[Nguồn, dòng 19](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L19). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; deliveryId; receivedServings int; actorRef; confirmedAt UTC; evidenceRef; version | Gắn phiếu/version; chưa có xác nhận thì chưa có số nhận, không default0. Sửa xác nhận cần policy, giữ lịch sử | CG01; Q01/02/13

### E7 — e7_discrepancies / resolutions

[Nguồn, dòng 20](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L20). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; deliveryId; description; evidenceRef; resolutionType; linkedSupplementRef; adjustmentBasis | Mỗi thỏa thuận gắn phần chênh và bằng chứng; không tự cả bù+giảm trừ. Chưa field tiền tự tính khi thiếu basis | Q02/03

### E7 — e7_revenue_snapshots

[Nguồn, dòng 21](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L21). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; orderId; orderRevisionRef; pricingSnapshotId; billableServings; basisEvidenceRef; grossAmountDue/revenueExVat decimal; contextStatus | Giữ nguồn bất biến; cùng order/version; kết quả chưa xác định nullable logic, không0. Số gốc snapshot không ghi đè | Q03/04/08

### E7 — e7_reconciliation_periods / lines

[Nguồn, dòng 22](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L22). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; customerId; fromDate/toDate; revision; state; sourceRefs; totals; completeness | Một tập nguồn có version; phạm vi/chồng kỳ và tái chụp cần duyệt; snapshot khóa bất biến | Q05

### E7 — e7_cash_receipts

[Nguồn, dòng 23](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L23). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; periodId; amount decimal; receivedDate; evidenceRef; version | Tiền dương, chứng từ/scope hợp lệ; uniqueness nghiệp vụ và allocation chưa freeze | Q06/08

### E7 — Reuse change_requests / approvals + liên kết kỳ

[Nguồn, dòng 24](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L24). Tái dùng nền: change_requests, approvals.

Trích trường và ràng buộc nguồn:

> entityRef; requestVersion; periodVersion; creator/lastEditor; reason; decision | Đề xuất dùng workflow nền, không tạo hai nguồn duyệt; Giám đốc khác người lập/sửa cuối; lý do≥10 ký tự; yêu cầu không mở khóa | Q05/08; O-06

### E7 — e7_export_runs

[Nguồn, dòng 25](../../../giao-nhan-doanh-thu/srs/data-dictionary.md#L25). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id; periodRef/revision; templateRef; status; errorSummary; fileRef; sourceFingerprint | FileRef chỉ có khi thật sự tạo; template chưa biết; giữ bytes/revision cũ khi kỳ mở lại | Q07/08

### E8 — pub_content_revisions

[Nguồn, dòng 18](../../../website-cong-khai/srs/data-dictionary.md#L18). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> contentRef, revision, type, title, slug, sanitizedBody, mediaRefs, status, publicRevisionRef | Public pointer chỉ revision được phép; revision cũ giữ nguồn, version chống ghi đè | E8-Q08

### E8 — pub_url_mappings

[Nguồn, dòng 19](../../../website-cong-khai/srs/data-dictionary.md#L19). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> inventoryRef, sourceURL, action, targetPath, revision, verification, activationEvidence | Một URL nguồn một quyết định trong revision, không vòng lặp; không coi bài xóa là miễn R8 | E8-Q01/02

### E8 — pub_sample_projections

[Nguồn, dòng 20](../../../website-cong-khai/srs/data-dictionary.md#L20). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> publicSampleRef, menuRef/version, recipeRefs, nutrientCalculationRef, publicPriceRef, eligibilityEvidence | Chỉ trường allowlist; pointer vào nguồn không công khai ID nội bộ | E8-Q03/04

### E8 — pub_price_permissions

[Nguồn, dòng 21](../../../website-cong-khai/srs/data-dictionary.md#L21). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> publicPriceRef, amount, displayBasis, approverEvidence, effectiveRange | Có thể thay bằng nguồn được xác nhận; không tự lấy ngưỡng giá | E8-Q03

### E8 — pub_trial_contexts

[Nguồn, dòng 22](../../../website-cong-khai/srs/data-dictionary.md#L22). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> trialRef, allowedInputs, publicResult, provenance | Không hồ sơ người ăn/health; có cần lưu và expiry chưa quyết | E8-Q05/12

### E8 — pub_lead_intake

[Nguồn, dòng 23](../../../website-cong-khai/srs/data-dictionary.md#L23). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> leadRef, minimalContact, source, consentVersion/evidence, trialRef?, receivedAt | Chỉ lưu khi policy đồng ý; nguồn đi cùng record, không dùng bảng khách thật | E8-Q06

### E8 — pub_lead_handoffs

[Nguồn, dòng 24](../../../website-cong-khai/srs/data-dictionary.md#L24). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> leadRef, handoffIdentity, state, receiptRef?, lastErrorCode | Chưa receipt không ACK; không enum/phễu CRM | E8-Q06/07

### E8 — pub_media_metadata

[Nguồn, dòng 25](../../../website-cong-khai/srs/data-dictionary.md#L25). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> fileRef, altText, rightsEvidenceRef, placements, revision | Chỉ file cho phép; ảnh/banner dùng revision nội dung | E8-Q09

### E9 — ain_sessions

[Nguồn, dòng 27](../../../agent-dinh-duong-vien/api/data-mapping.md#L27). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, principalRef, identityPolicyVersion, consentRef, state, createdAt, expiresAt | Identity/retention Q02/10; không raw sức khỏe; không tự tạo users guest

### E9 — ain_candidates

[Nguồn, dòng 28](../../../agent-dinh-duong-vien/api/data-mapping.md#L28). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, sessionRef, runRef, revision, parentRevision, canonicalHash, safeContent, evidenceRefs, sourceVersions, state | Unique(sessionRef,id,revision); evidence phải cùng hash; không official MENU

### E9 — ain_proposals

[Nguồn, dòng 29](../../../agent-dinh-duong-vien/api/data-mapping.md#L29). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, ownerRef, candidateRef/revision/hash, source, contactRef, consentRef, requestKey/bodyHash, state, receiptRef | ACK chỉ khi lưu bền vững; unique(owner,route,key); Q06/10/13; không lead CRM giả

### E9 — ain_limit_policies

[Nguồn, dòng 30](../../../agent-dinh-duong-vien/api/data-mapping.md#L30). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, groupRef, version, countPolicy, dailyCap, unit, timezone, effectiveAt, approvalRef | Giá trị chưa chọn; không ghi quá khứ; duyệt theo Q08 và E1

### E9 — ain_budget_reservations

[Nguồn, dòng 31](../../../agent-dinh-duong-vien/api/data-mapping.md#L31). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, principal/group, dayKey, policyRef, runRef, upperBound, state, requestKey | Admission atomic; không release UNKNOWN; Q07/13

### E9 — ain_usage_events

[Nguồn, dòng 32](../../../agent-dinh-duong-vien/api/data-mapping.md#L32). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, runRef, providerEventRef, dayKey, usageState, amount/unit, reservationRef, sourceHash | Unique event; không sửa mất lịch sử; confirmed/reserved reconciliation, unknown khác0

### E10 — crm_contact_drafts

[Nguồn, dòng 43](../../../crm-ban-hang/srs/data-dictionary.md#L43). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, customerRef, displayName, contactRole, channels, sourceEvidenceRef, version | Id PK; customer FK logic; string; object theo Q01; Id; int; required theo policy | Chỉ nháp liên hệ; không đồng bộ master khi CG08 mở.

### E10 — crm_intakes

[Nguồn, dòng 44](../../../crm-ban-hang/srs/data-dictionary.md#L44). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, sourceSystem, sourceRef, sourceRevision, sourceHash, safeMenuRef, contactRef, consentRef, receiptRef | Id PK; strings required; safeMenuRef nullable; consent/contact theo nguồn | Unique(sourceSystem,sourceRef,sourceRevision); khác hash cùng khóa là xung đột; không raw chat.

### E10 — crm_merge_reviews/events

[Nguồn, dòng 45](../../../crm-ban-hang/srs/data-dictionary.md#L45). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, leftRef, rightRef, versions, fieldChoices, beforeImage, linkMap, decisionRef, reversalOf | Id; hai FK khách; JSON có schema; decisionRef nullable khi nháp; reversalOf nullable | Không xóa nguồn; ảnh trước có scope và quyền; quyết định/hoàn tác bất biến.

### E10 — crm_lifecycle_events/risk_evaluations

[Nguồn, dòng 46](../../../crm-ban-hang/srs/data-dictionary.md#L46). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> customerRef, previousState, nextState, evidenceRef, scheduleRefs, evaluationRef, completeness | FK; enum theo states; Id[]; state | Lịch ngoại lệ và ngưỡng chưa có; không lấy thiếu dữ liệu thành zero.

### E10 — sale_opportunities/events

[Nguồn, dòng 47](../../../crm-ban-hang/srs/data-dictionary.md#L47). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, customerOrIntakeRef, ownerRef, stage, evidenceRef, version | Id PK; FK logic; stage theo Q07; evidence nullable ở nháp | Một cơ hội nhiều báo giá; lịch sử sự kiện không ghi đè.

### E10 — sale_quote_revisions/publications

[Nguồn, dòng 48](../../../crm-ban-hang/srs/data-dictionary.md#L48). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> quoteRef, revisionNo, version, baseRevision, lines, terms, attachments, contentHash, publishedProjection | Id; int; int; FK logic nullable; JSON có schema; hash; projection nullable trước phát hành | Unique(quoteRef,revisionNo); revision đã phát hành bất biến; cost tách riêng.

### E10 — sale_contracts/amendments

[Nguồn, dòng 49](../../../crm-ban-hang/srs/data-dictionary.md#L49). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> id, customerRef, quoteRevisionRef, legacyEvidenceRef, signatureEvidenceRef, predecessorRef, status, version | Id PK; FK; quote/legacy ít nhất một nguồn; signature nullable khi nháp; predecessor nullable cho bản đầu | Hợp đồng nhiều phụ lục; phụ lục nhiều dòng loại suất; liên kết nguồn không mất khi gộp.

### E10 — sale_contract_price_links / hiệu lực lịch sử

[Nguồn, dòng 50](../../../crm-ban-hang/srs/data-dictionary.md#L50). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> contractRef, amendmentRef, priceTermRef, predecessorTermRef, effectiveFrom, effectiveTo, approvalRef | FK logic; date/date nullable theo Q11; approval nullable trước duyệt | Đề xuất nối vào customer_price_terms; không tự tạo bảng giá cạnh tranh. Mọi thay khoảng có lịch sử và quyết định Q12.

### E11 — demand / purchase_demands

[Nguồn, dòng 51](../../../mua-hang-san-xuat/srs/data-dictionary.md#L51). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> planRef, estimateRef (Reference; không null khi tính); lines (Array); grossQty (Decimal); netBuyQty (Decimal nullable) | FR-PUR-DEM-001; Q01 và CG06; netBuyQty chưa tính

### E11 — purchaseOrder / purchase_orders

[Nguồn, dòng 52](../../../mua-hang-san-xuat/srs/data-dictionary.md#L52). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> supplierId (Id; bắt buộc khi lưu); demandRef (Reference); lines (Array không rỗng); approvalRef (Reference nullable) | FR-PUR-POD-001/POG; Q02; NCC do người lập chọn

### E11 — lotScope / stock_lots

[Nguồn, dòng 53](../../../mua-hang-san-xuat/srs/data-dictionary.md#L53). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> ingredientId (Id); storageType (Enum FROZEN/DRY); lotCode/expiry (chưa đặc tả theo Q03) | Chỉ ranh giới, không bắt buộc lô hàng tươi

### E11 — goodsReceipt / goods_receipts

[Nguồn, dòng 54](../../../mua-hang-san-xuat/srs/data-dictionary.md#L54). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> purchaseOrderRef (Reference); receivedQty, acceptedQty (Decimal; không âm; accepted ≤ received); receivedAt (Timestamp) | Q04; nhận nhiều lần không ghi đè lần cũ

### E11 — receiptEvidence / receipt_evidence

[Nguồn, dòng 55](../../../mua-hang-san-xuat/srs/data-dictionary.md#L55). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> receiptRef, fileRef (Reference; không null; unique logic cặp tham chiếu đề xuất) | Q05/Q13; liên kết không xác nhận giá

### E11 — supplierBalance / supplier_balance_views

[Nguồn, dòng 56](../../../mua-hang-san-xuat/srs/data-dictionary.md#L56). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> opening, obligations, payments, adjustments, closing (Decimal nullable); completeness (Enum) | Projection đọc; nguồn ghi nhận/kỳ Q06; không tạo sổ cái

### E11 — comparison / purchase_comparisons

[Nguồn, dòng 57](../../../mua-hang-san-xuat/srs/data-dictionary.md#L57). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> estimateRef, allocationRefs, measurementBasisRef (Reference); estimatedPct, actualPct, deltaPp (Decimal nullable) | Q07/08; ngày và cơ sở cùng phạm vi

### E11 — comparisonLine / purchase_comparison_lines

[Nguồn, dòng 58](../../../mua-hang-san-xuat/srs/data-dictionary.md#L58). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> ingredientId, estimateLineRef, receiptLineRef (Reference); quantity/unit/price hai phía | Không tự phân bổ hoặc sửa snapshot

### E11 — productionShift / production_shifts

[Nguồn, dòng 59](../../../mua-hang-san-xuat/srs/data-dictionary.md#L59). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> shiftRef, planRef (Reference); assignments (Array mã nhân sự/công việc) | Q09/CG06; không timestamp bắt đầu E6 tự sinh

### E11 — qualityCheck / pre_delivery_checks

[Nguồn, dòng 60](../../../mua-hang-san-xuat/srs/data-dictionary.md#L60). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> shiftRef, checklistRef (Reference); results (mục/kết quả/chứng cứ) | Q10; chưa định nghĩa checklist thực

### E11 — retainedSample / retained_samples

[Nguồn, dòng 61](../../../mua-hang-san-xuat/srs/data-dictionary.md#L61). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> mealRef (Reference); sampleCode (Text); evidenceRef (Reference nullable ở nháp) | Q11; chưa có hạn lưu/lượng mẫu/nhiệt độ

### E11 — substitution / substitution_candidates

[Nguồn, dòng 62](../../../mua-hang-san-xuat/srs/data-dictionary.md#L62). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> menuRef, menuVersion, originalDishId, replacementDishId, role (Reference/Enum); reason | Cùng vai trò; Q12; không ghi menu công bố

### E11 — substitutionCheck / substitution_checks

[Nguồn, dòng 63](../../../mua-hang-san-xuat/srs/data-dictionary.md#L63). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> candidateRef, candidateVersion; allergenResultRef, ruleResultRef, costResultRef (Reference nullable khi thiếu) | Ba kiểm đúng nguồn; thiếu một thì BLOCKED

### E12 — feedback_rating

[Nguồn, dòng 27](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L27). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Đề xuất mới; ERD có khung feedbacks nhưng DBML chưa có bảng FB | mealRef, scaleRef, value, actorRef, scopeRef, receiptRef

### E12 — feedback_case

[Nguồn, dòng 28](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L28). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Đề xuất mới | mealRef, categoryRef, nội dung về bữa, status, version, historyRefs

### E12 — dish_metric_projection

[Nguồn, dòng 29](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L29). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Projection đề xuất, không thêm bảng source E6 | dishRef, scopeRef, choiceSourceRefs, numerator, denominatorDefinitionRef, denominator, rate, completeness

### E12 — role_metric_projection

[Nguồn, dòng 30](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L30). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Projection đề xuất | metricDefinitionRef, value, unit, sourceRefs, asOf, completeness, missingReason

### E12 — review_proposal

[Nguồn, dòng 31](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L31). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Tài liệu nháp đề xuất; không ghi MENU/CRM/PUR | kind, sourceRefs, sourceRevision, diff, checkRefs, reviewState

### E12 — group_nutrition_target

[Nguồn, dòng 32](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L32). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Delta nhóm phi y tế đề xuất | groupRef, targets, sourceRef, version, effectiveRange, state

### E12 — diary_consent

[Nguồn, dòng 33](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L33). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Delta riêng, không dùng eater_health_profiles | subjectRef, policyRef, agreedAt, withdrawnAt

### E12 — diary_meal

[Nguồn, dòng 34](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L34). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Delta riêng, không liên kết hồ sơ sức khỏe | subjectRef, consumedMealRef, consumedAt, evidenceRef, nutritionSnapshotRef

### E12 — diary_deletion_request

[Nguồn, dòng 35](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L35). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> Delta quyền xóa đề xuất | subjectRef, scopeRef, receiptRef, state, completedEvidenceRef

### E13 — expense_periods

[Nguồn, dòng 25](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L25). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | kitchen ref | kitchen_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK kitchens | Scope cơ sở |
> | from date / to date | from_date / to_date | DATE | — | Không | — | Biên ngày chờ Q02 |
> | status | status | ENUM | — | Không | — | OPEN / LOCKED |
> | locked snapshot ref | locked_snapshot_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK đề xuất | Bắt buộc khi khóa |

### E13 — expense_entries

[Nguồn, dòng 34](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L34). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | period ref | period_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Kỳ mở |
> | type version ref | type_version_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Danh mục Q01 chưa chọn |
> | amount | amount | DECIMAL | Chờ Q09 | Không | — | Tiền có đơn vị và căn cứ; không float |
> | customer ref | customer_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK customers | Bắt buộc với trực tiếp; null với chung |
> | source key / evidence ref | source_key / evidence_ref | STRING | Chờ Q12 | Không | Unique scope | Chống trùng với E3/E11 |

### E13 — attendance_sheets

[Nguồn, dòng 44](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L44). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | person ref | person_ref | STRING | Chờ Q03 | Không | Tham chiếu nguồn | Không mặc định người lao động có tài khoản users |
> | shift revision ref | shift_revision_ref | STRING | Chờ E11 | Không | Nguồn E11 | Phân ca không chứng minh đã làm |
> | kitchen ref / work date | kitchen_ref / work_date | BIGINT UNSIGNED / DATE | 20 chữ số / — | Không | FK kitchens | Theo cơ sở/ca |
> | hours | hours | DECIMAL | Chờ Q03 | Có | — | Null khi thiếu; 0 chỉ khi có xác nhận 0 giờ |
> | evidence ref / status | evidence_ref / status | STRING / ENUM | Chờ Q03 | Không | — | DRAFT / SUBMITTED / CONFIRMED / RETURNED |

### E13 — labor_cost_refs

[Nguồn, dòng 54](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L54). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | attendance version ref | attendance_version_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Bản công xác nhận |
> | rate version ref / payroll amount ref | rate_version_ref / payroll_amount_ref | STRING | Chờ Q04 | Có | Nguồn lương | Một cách tính được duyệt; không cộng hai nguồn |
> | amount | amount | DECIMAL | Chờ Q09 | Có | — | Null nếu thiếu nguồn; dữ liệu nhạy cảm |

### E13 — allocation_method_versions

[Nguồn, dòng 62](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L62). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | method ref / revision | method_ref / revision | BIGINT UNSIGNED / INTEGER | 20 chữ số / — | Không | Unique cặp | Phiên bản bất biến sau duyệt |
> | proposed basis / driver definition refs | proposed_basis / driver_definition_refs | JSON | Chờ Q05 | Có | — | Dữ liệu mô tả; không có default hoặc code thực thi |
> | scope / effective range | scope / effective_range | JSON | Chờ Q05 | Không | — | Cơ sở/kỳ; không tự xử lý chồng hiệu lực |
> | status | status | ENUM | — | Không | — | DRAFT / SUBMITTED / APPROVED / RETURNED |
> | approver ref / approved at / approval evidence ref / content hash | approver_ref / approved_at / approval_evidence_ref / content_hash | BIGINT UNSIGNED / TIME / STRING | Chờ Q12 | Có | Tham chiếu duyệt | Bắt buộc đủ khi APPROVED; khác lập/sửa cuối |

### E13 — profit_runs

[Nguồn, dòng 72](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L72). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | period snapshot ref / source manifest ref | period_snapshot_ref / source_manifest_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Cùng phạm vi, nguồn có version |
> | method version ref | method_version_ref | BIGINT UNSIGNED | 20 chữ số | Có | FK đề xuất | Null chỉ khi BLOCKED vì chưa có duyệt |
> | status / blocked reasons | status / blocked_reasons | ENUM / JSON | — | Không | — | DRAFT / BLOCKED / READY / RECONCILED |
> | facility result ref / definition version ref | facility_result_ref / definition_version_ref | STRING | Chờ Q08 | Có | Nguồn chuẩn | Không dùng tổng khách tự tạo làm số chuẩn |
> | customer results / unallocated effect / reconciliation delta | customer_results / unallocated_effect / reconciliation_delta | JSON / DECIMAL | Chờ Q09 | Có | — | Null nếu BLOCKED; tách từng cơ sở/khách; không gộp thiếu nguồn |

### E13 — expense_adjustments

[Nguồn, dòng 82](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L82). Tên đề xuất chưa phải bảng được merge.

Trích trường và ràng buộc nguồn:

> | original entry ref / locked snapshot ref | original_entry_ref / locked_snapshot_ref | BIGINT UNSIGNED | 20 chữ số | Không | FK đề xuất | Giữ nguồn gốc bất biến |
> | adjustment amount / target period ref | adjustment_amount / target_period_ref | DECIMAL / BIGINT UNSIGNED | Chờ Q09/10 | Có | FK đề xuất | Dấu tăng/giảm; kỳ đích chưa chọn |
> | reason / evidence ref / approver ref | reason / evidence_ref / approver_ref | STRING / BIGINT UNSIGNED | Chờ Q10 | Có | — | Bắt buộc đủ trước POSTED |
> | status | status | ENUM | — | Không | — | PENDING / REJECTED / POSTED |

## Trường chung của các delta

Các trường dưới áp dụng cùng những trường riêng đã liệt kê; tên/kiểu vẫn là đề xuất nguồn.

### mua-hang-san-xuat

[Dòng 31](../../../mua-hang-san-xuat/srs/data-dictionary.md#L31):

> Mã | id | Id | Theo E1 | Không | PK đề xuất | Cấp bởi hệ thống; chưa chọn kiểu mới | Định danh

[Dòng 32](../../../mua-hang-san-xuat/srs/data-dictionary.md#L32):

> Cơ sở | kitchen_id | Id | Theo E1 | Không | FK logic kitchens | Scope từ quyền hiện tại | Không tin cơ sở client tự khai

[Dòng 33](../../../mua-hang-san-xuat/srs/data-dictionary.md#L33):

> Ngày phục vụ | service_date | Date | ISO date | Tùy thực thể | — | Không mặc định hôm nay | Tách ngày nhận và ngày phục vụ

[Dòng 34](../../../mua-hang-san-xuat/srs/data-dictionary.md#L34):

> Phiên bản | version | Integer | Chờ contract | Không | — | Token kiểm khi ghi | Không tráo revision nguồn

[Dòng 35](../../../mua-hang-san-xuat/srs/data-dictionary.md#L35):

> Nguồn | source_refs | Reference[] | Chờ contract | Không | FK logic | Giữ loại, id, revision nguồn | Thiếu thì BLOCKED

[Dòng 36](../../../mua-hang-san-xuat/srs/data-dictionary.md#L36):

> Lượng | quantity | Decimal string | Chờ độ chính xác | Có khi chưa biết | — | Kèm unit; không âm; null không là 0 | Không cộng kg với suất

[Dòng 37](../../../mua-hang-san-xuat/srs/data-dictionary.md#L37):

> Giá nguồn | quoted_unit_price | Decimal string | Theo PriceInput E3 | Có khi thiếu | — | Không dùng trực tiếp tính cost | Giá báo

[Dòng 38](../../../mua-hang-san-xuat/srs/data-dictionary.md#L38):

> Cơ sở giá | price_basis | Enum | Theo E3 | Có khi thiếu | — | INCLUSIVE / EXCLUSIVE / FINAL_CONFIRMED | Không dùng UNKNOWN như đã chuẩn hóa

[Dòng 39](../../../mua-hang-san-xuat/srs/data-dictionary.md#L39):

> VAT | vat_rate_pct / vat_unit_amount | Decimal string | Theo E3 | Theo basis | — | EXCLUSIVE cần đúng một căn cứ hợp lệ | Không tự mặc định 0

[Dòng 40](../../../mua-hang-san-xuat/srs/data-dictionary.md#L40):

> Giá cost | effective_cost_unit_price | Integer money | Theo E3 | Có khi chưa xác định | — | Server chuẩn hóa gồm VAT; phần lẻ chờ | Không nhận số tin cậy từ client

[Dòng 41](../../../mua-hang-san-xuat/srs/data-dictionary.md#L41):

> Nguồn giá | pricing_evidence | Text/reference | Theo E3 | Không khi xác định giá | — | Giữ chứng từ/xác nhận | Không suy từ cờ hóa đơn

[Dòng 42](../../../mua-hang-san-xuat/srs/data-dictionary.md#L42):

> Tệp | file_ref | Id | Theo E1 | Có ở bản nháp | FK logic files | Quyền theo chủ thể, không public URL | Ảnh chứng từ

[Dòng 43](../../../mua-hang-san-xuat/srs/data-dictionary.md#L43):

> Trạng thái | status | Enum | Theo states | Không | — | DRAFT khi tạo nháp | Không suy được duyệt

[Dòng 44](../../../mua-hang-san-xuat/srs/data-dictionary.md#L44):

> Người/thời điểm | actor_id / recorded_at | Id / Timestamp | Theo E1 | Không khi ghi | FK logic users | Do phiên/server xác định | Audit

[Dòng 45](../../../mua-hang-san-xuat/srs/data-dictionary.md#L45):

> Lý do | reason | Text | Theo E1 / chờ Q13 | Không khi sửa số | — | Không ghi đè lịch sử | Căn cứ thay đổi

### phan-hoi-bao-cao

[Dòng 41](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L41):

> Định danh | id | Opaque reference | Chờ contract | Không | PK đề xuất | Server cấp, không chọn UUID/bigint mới | Mã E12, không suy kiểu từ schema nguồn

[Dòng 42](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L42):

> Chủ thể | subject_ref | Reference | Theo E1/E6 | Không cho nhật ký | FK logic | Server lấy từ phiên, không tin client | Chỉ chủ nhật ký được xem

[Dòng 43](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L43):

> Phạm vi | scope_ref | Object/reference | Chờ Q18 | Không | FK logic | Khách/cơ sở/điểm; giao quyền hiện tại | Không chỉ lọc UI

[Dòng 44](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L44):

> Nguồn | source_refs | Array reference | Chờ Q18 | Không khi có số | FK logic | module, recordRef, revision, asOf, scope | Không đưa tham chiếu nhạy cảm ra ngoài quyền

[Dòng 45](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L45):

> Phiên bản | version | Opaque token | Chờ Q18 | Không khi sửa | — | So khớp, không mặc định lấy mới nhất | Khác revision bất biến của nguồn

[Dòng 46](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L46):

> Giá trị | value | Decimal hoặc null | Theo producer | Có | — | Null khi missing; không default 0 | Không float tiền; tỷ lệ theo producer

[Dòng 47](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L47):

> Mẫu số | denominator | Decimal hoặc null | Theo định nghĩa được duyệt | Có | — | Chưa chọn mẫu số tỷ lệ chọn; không default | 0 không chia; cần definitionRef

[Dòng 48](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L48):

> Bốn chỉ số suất | nutrition_snapshot_ref | Reference | Theo E4 | Có khi thiếu | FK logic | energy_kcal/protein_g/fat_g/carb_g từ E4 | Không lưu bệnh, cân nặng hoặc suy lượng hấp thu

[Dòng 49](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L49):

> Đồng ý | policy_ref | Reference | Chờ Q15 | Không khi bật | FK logic | Explicit, không chọn sẵn | Đồng ý nhật ký không là đồng ý hồ sơ sức khỏe

[Dòng 50](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L50):

> Bữa đã ăn | consumed_meal_ref | Reference | Chờ Q17 | Không khi ghi | FK logic | Căn cứ đã ăn riêng; order không chứng minh | Không tự ghi từ lựa chọn

[Dòng 51](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L51):

> Mục tiêu nhóm | targets | Object nguồn | NUTR-Q01–04 | Có khi nháp thiếu | — | Không số mặc định; nguồn và phiên bản bắt buộc khi dùng | Không có subjectRef cá nhân trong mục tiêu

[Dòng 52](../../../phan-hoi-bao-cao/srs/data-dictionary.md#L52):

> Kết quả xóa | completed_evidence_ref | Reference | Chờ Q16 | Có trước hoàn tất | FK logic | Chỉ có khi chứng minh xóa; không xóa nguồn E6/E7 | Không báo hoàn tất từ receipt

[Trường chung E13, dòng 23](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L23):

> Mọi thực thể đề xuất có id BIGINT UNSIGNED (20 chữ số tối đa, PK, không null), version INTEGER (không null), createdBy/createdAt và auditRef (không null); Khóa mới đề xuất kế thừa BIGINT UNSIGNED của nền; API truyền định danh dạng chuỗi để không mất chính xác. Trường liệt kê là enum logic, physical đề xuất VARCHAR(24) + CHECK theo nền, không phải MySQL ENUM. Thời điểm lưu UTC, ngày nghiệp vụ theo giờ Việt Nam; biên kỳ cụ thể vẫn chờ Q02. Độ dài trường chưa có căn cứ và lưu trữ chi tiết chờ Q12. Các trường lương không vào log thông thường. Không chọn precision hoặc retention từ ví dụ.

[Trường chung E13, dòng 91](../../../chi-phi-loi-nhuan/srs/data-dictionary.md#L91):

> Danh mục loại chi phí có version/effectiveRange/decisionRef đề xuất kèm Q01, chưa điền loại thực tế. Manifest nguồn tối thiểu gồm producer, sourceRef, revision/hash, kitchenRef, periodRange, customerRef nếu có, kind (dự toán/thực mua/doanh thu đối soát), completeness và capturedAt. Không dùng estimate thay actual.

## Ranh giới nguyên tắc

Cost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất riêng theo đơn, không giảm phải trả NCC và không tự khấu trừ phải trả khách. NFR-COST-002 giữ ≤ 1 đ cho cost món, ≤ 0,01 điểm phần trăm cho cost % ngày; BO-01/BO-02 là mục tiêu kinh doanh. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03, không thu dữ liệu sức khỏe.

## Cần BA làm rõ

Các phát hiện ghi “cần xác nhận” không đóng câu hỏi. Danh sách mọi mã thiếu vai trò/release nằm trong [báo cáo](validation/report.md). Chưa có contract nguồn freeze hoặc dữ liệu thực để xác nhận tương thích kiểu. Không suy thời hạn, hạn mức, phương pháp phân bổ, mẫu số hay người ký từ ví dụ.
