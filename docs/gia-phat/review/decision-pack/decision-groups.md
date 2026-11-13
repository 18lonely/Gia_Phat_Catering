---
id: DOC-DECISION-PACK-GROUPS
title: Nhóm quyết định và phương án nguồn
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [decision-pack, draft, review]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-13
---
# Nhóm quyết định và phương án nguồn

Nháp · 13/11/2026 · Chuẩn bị quyết định, chưa phê duyệt.

| Phiên bản | Ngày | Vai trò | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 13/11/2026 | BA | Hợp nhất nguồn để review; giữ câu mở |

Nhóm chỉ gom phần quyết định chung. Câu nhiều nhánh vẫn phải được ký theo phạm vi từng mã; đồng ý một phần không đóng cả nhóm. Mỗi mục có câu tổng hợp, mã nguồn, vai trò và release. Phương án và tác động dưới đây trích nguồn, không tự bổ sung đánh đổi. Nếu nguồn không tách tác động từng phương án, ghi “chưa rõ”; không suy diễn.

Không gộp cost % E3, mẫu số BO-02 E11, cost % theo khách E12 và lợi nhuận E13 thành một công thức. Không gộp consent nhật ký FEAT-087 với consent sức khỏe O-03. MISA là câu E7-Q07; E11 và E13 không có câu riêng về MISA để gộp.

<a id="dec-01"></a>

## DEC-01 — Phạm vi sức khỏe và điều kiện mở gợi ý cá nhân

Cần quyết định: Phạm vi sức khỏe và điều kiện mở gợi ý cá nhân?

Mã nguồn: O-03, ORD-Q15, E9-Q14. Người quyết định: Giám đốc; Chủ sản phẩm, phụ trách dữ liệu; chưa rõ. Release: R6, R9. [Buổi 1](meeting-agenda.md#buoi-1).

### O-03

[Nguồn, dòng 252](../../01-prd.md#L252). Nội dung đầy đủ:

> Gợi ý cá nhân có xét bệnh lý không

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### ORD-Q15

[Nguồn, dòng 41](../../../chon-mon-order/review/questions.md#L41). Nội dung đầy đủ:

> Nếu mở O-03: consent/version, rút đồng ý, thời hạn xóa/lưu log, phạm vi bệnh lý và tiêu chí gợi ý cụ thể?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E9-Q14

[Nguồn, dòng 31](../../../agent-dinh-duong-vien/review/questions.md#L31). Nội dung đầy đủ:

> Mở FEAT-063 cần phê duyệt nào sau O-03/FEAT-046/047; PER-04 không tài khoản có được dùng không?

Phương án khuyến nghị đã có:

> Giữ gate đóng; sau quyết định mới review phạm vi persona, consent/quyền và contract FEAT-047; không xây nhánh gợi ý trước

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Toàn bộ gợi ý cá nhân/đọc hồ sơ/thu hoặc suy luận sức khỏe

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-02"></a>

## DEC-02 — Nguồn lực, hạ tầng và cấu hình ngân sách AI

Cần quyết định: Nguồn lực, hạ tầng và cấu hình ngân sách AI?

Mã nguồn: O-04, AIO-Q01, E9-Q01. Người quyết định: Giám đốc; Giám đốc, Tech lead; chưa rõ. Release: R1, R5, R9. [Buổi 1](meeting-agenda.md#buoi-1).

### O-04

[Nguồn, dòng 253](../../01-prd.md#L253). Nội dung đầy đủ:

> Đội phát triển, hạ tầng, nhà cung cấp AI, ngân sách

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### AIO-Q01

[Nguồn, dòng 13](../../../agent-noi-bo/review/questions.md#L13). Nội dung đầy đủ:

> Nhà cung cấp/model, ngân sách, concurrency, số lần thử, token tối đa và cách ghi chi phí/tỷ giá nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> O-04; không có mặc định ngân sách được duyệt

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E9-Q01

[Nguồn, dòng 18](../../../agent-dinh-duong-vien/review/questions.md#L18). Nội dung đầy đủ:

> O-04: nhà cung cấp mô hình, hạ tầng, vùng/nơi xử lý dữ liệu và đường chuyển dữ liệu nào được duyệt?

Phương án khuyến nghị đã có:

> So sánh phương án tự quản lý hoặc dịch vụ sau đánh giá dữ liệu; chưa chọn provider/model

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Toàn bộ gọi AI thật, cấu hình chi phí, release R9

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-03"></a>

## DEC-03 — Người duyệt ngoại lệ và cơ chế thay thế

Cần quyết định: Người duyệt ngoại lệ và cơ chế thay thế?

Mã nguồn: O-06, E11-Q02, E13-Q10, E10-Q03, CK-Q04. Người quyết định: Giám đốc; chưa rõ; Giám đốc và chủ dữ liệu khách; Giám đốc, kế toán. Release: R1, R11, R13, R10, R3. [Buổi 1](meeting-agenda.md#buoi-1).

### O-06

[Nguồn, dòng 255](../../01-prd.md#L255). Nội dung đầy đủ:

> Ai duyệt ngoại lệ và ai thay khi vắng

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E11-Q02

[Nguồn, dòng 26](../../../mua-hang-san-xuat/review/questions.md#L26). Nội dung đầy đủ:

> Ai lập, duyệt, phát hành đơn mua; xử lý sửa/hủy và người thay thế thế nào?

Phương án khuyến nghị đã có:

> Dùng tách tạo/duyệt của E1; chưa gán vai trò duyệt hoặc hạn mức.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Đơn mua chỉ nháp; phát hành và sửa đơn đã duyệt BLOCKED; O-06 giữ mở.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E13-Q10

[Nguồn, dòng 34](../../../chi-phi-loi-nhuan/review/questions.md#L34). Nội dung đầy đủ:

> Ai duyệt điều chỉnh sau khóa, ghi vào kỳ nào và bằng chứng nào bắt buộc?

Phương án khuyến nghị đã có:

> Bút toán riêng gắn bản gốc, lý do và người duyệt khác người lập/sửa cuối; không mở khóa tại E13.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Ghi nhận điều chỉnh chính thức; O-06; FR-EXP-ADJ-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E10-Q03

[Nguồn, dòng 27](../../../crm-ban-hang/review/questions.md#L27). Nội dung đầy đủ:

> Ai lập, ai duyệt gộp/hoàn tác; có người thay và kiểm tách nhiệm vụ thế nào?

Phương án khuyến nghị đã có:

> Người duyệt khác người lập/sửa cuối; quyền gộp và hoàn tác riêng.

Phương án khác đã có:

> Hội đồng review từng đợt dữ liệu trước khi giao quyền vận hành.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-DUP-001 / UC-CRM-004; FR-CUS-MRG-001 / UC-CRM-005; FR-CUS-UNDO-001 / UC-CRM-006

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### CK-Q04

[Nguồn, dòng 94](../../../cost/accounting/business-rules.md#L94). Nội dung đầy đủ:

> Ai được lập/sửa khoản chiết khấu? Ai được duyệt; có phân cấp theo số tiền hoặc tỷ lệ không? Người lập có được tự duyệt không, ai thay khi người duyệt vắng?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-04"></a>

## DEC-04 — Cỡ định lượng của một món

Cần quyết định: Cỡ định lượng của một món?

Mã nguồn: O-02, H-9. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### O-02

[Nguồn, dòng 251](../../01-prd.md#L251). Nội dung đầy đủ:

> Một món một định lượng hay nhiều cỡ định lượng

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### H-9

[Nguồn, dòng 128](../../brainstorms/quy-tac-thuc-don.md#L128). Nội dung đầy đủ:

> Bảng định lượng hiện chỉ có 23 dòng cho mức 40k. Khi dinh dưỡng viên tạo loại suất giá khác, định lượng giữ nguyên theo món (giá suất khác nhau do số món khác nhau), hay cùng một món có nhiều cỡ định lượng với giá khác nhau?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-05"></a>

## DEC-05 — Thành phần cost và VAT bán ra còn thiếu

Cần quyết định: Thành phần cost và VAT bán ra còn thiếu?

Mã nguồn: O-01, H-6, H-7. Người quyết định: Kế toán. Release: R3, R2. [Buổi 3](meeting-agenda.md#buoi-3).

### O-01

[Nguồn, dòng 250](../../01-prd.md#L250). Nội dung đầy đủ:

> Cost gồm những khoản nào; thuế suất VAT

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### H-6

[Nguồn, dòng 125](../../brainstorms/quy-tac-thuc-don.md#L125). Nội dung đầy đủ:

> Suất ăn đang xuất hoá đơn với thuế suất VAT bao nhiêu? (Cần kế toán trả lời.)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### H-7

[Nguồn, dòng 126](../../brainstorms/quy-tac-thuc-don.md#L126). Nội dung đầy đủ:

> Hiện tại khi tính 52%, kế toán/bếp đang cộng những khoản nào? Gạo, gia vị, dầu ăn, tráng miệng có tính không?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-06"></a>

## DEC-06 — Chuẩn envelope giữa các phân hệ

Cần quyết định: Chuẩn envelope giữa các phân hệ?

Mã nguồn: E1-Q01, E6-CG-09. Người quyết định: Tech lead, BA; Tech lead/API owner, BA. Release: R1, R6. [Buổi 1](meeting-agenda.md#buoi-1).

### E1-Q01

[Nguồn, dòng 22](../../../nen-tang/review/questions.md#L22). Nội dung đầy đủ:

> Thống nhất envelope lỗi và page/cursor giữa E1 và E3/E4/E5 thế nào?

Phương án khuyến nghị đã có:

> E1/E2 giữ chuẩn SRS page; các extension cursor/envelope ghi ngoại lệ đề xuất, chưa coi API toàn hệ thống đã nhất quán

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E6-CG-09

[Nguồn, dòng 15](../../../chon-mon-order/review/contract-gap-register.md#L15). Nội dung đầy đủ:

> Envelope/pagination/error mapping; E1-Q01

Phương án khuyến nghị đã có:

> Đề xuất E6 dùng success envelope theo E1: success/data/meta/timestamp; data list chỉ items, page/pageSize/total đặt ở meta, tránh lặp metadata. Error giữ code/message/details/requestId như E1/E6 đang mô tả. Adapter chuyển từ từng nguồn, không trả nguyên upstream body.

Phương án khác đã có:

> Giữ DTO trực tiếp của E6: ít thay đổi hơn nhưng client phải xử lý nhiều envelope. Thống nhất E6 theo E1 tác động toàn bộ consumer/test nháp E6, nên chỉ triển khai sau review version.

Tác động / phần chặn được nguồn mô tả:

> API owner review ví dụ success/list/error và mapping từng miền, chọn version/chuyển đổi. Chưa sửa 26route hoặc DTO hiện hành; không áp template skill thay E1-Q01.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-07"></a>

## DEC-07 — Xác minh người ăn và binding danh tính

Cần quyết định: Xác minh người ăn và binding danh tính?

Mã nguồn: ORD-Q01, E6-CG-01. Người quyết định: Gia Phát, BA; BA, phụ trách khách, Tech lead/Auth. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q01

[Nguồn, dòng 20](../../../chon-mon-order/review/questions.md#L20). Nội dung đầy đủ:

> Định danh duy nhất người ăn có tài khoản/QR bằng gì; xử lý nhiều thiết bị/QR chia sẻ và account trùng ra sao?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E6-CG-01

[Nguồn, dòng 7](../../../chon-mon-order/review/contract-gap-register.md#L7). Nội dung đầy đủ:

> Identity/binding/credential/guest audit; RV01, ORD-Q01/02/11; EVID001 chỉ xác nhận danh sách

Phương án khuyến nghị đã có:

> Dùng một định danh thành viên nội bộ ổn định gắn danh sách đã được quản lý xác nhận; account và guest nếu được hỗ trợ cùng tham chiếu thành viên đó. Quản lý xác nhận đúng người trước khi cấp liên kết/mã kích hoạt dùng một lần; QR tại điểm chỉ dẫn vào luồng, không tự chứng minh danh tính. Khôi phục/thu hồi phải kiểm lại người nhận và lưu audit. Không dùng mã nhân viên công khai làm mật khẩu.

Phương án khác đã có:

> OTP qua số điện thoại đã xác minh: thuận tiện khôi phục nhưng cần chất lượng dữ liệu số điện thoại và dịch vụ gửi.

Tác động / phần chặn được nguồn mô tả:

> Một người đổi điện thoại vẫn nối về cùng thành viên, không tự sinh người ăn mới; không gộp hai người chỉ vì trùng tên. Ưu điểm: tận dụng danh sách hiện có, chưa đòi số điện thoại cho tất cả. Đánh đổi: quản lý phải bàn giao mã riêng đúng người; không có kênh bàn giao an toàn thì chưa kích hoạt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-08"></a>

## DEC-08 — Scope người đặt tổng một hoặc nhiều khách

Cần quyết định: Scope người đặt tổng một hoặc nhiều khách?

Mã nguồn: ORD-Q11, E6-CG-02. Người quyết định: Gia Phát, Tech lead; Chủ sản phẩm, BA, Tech lead. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q11

[Nguồn, dòng 37](../../../chon-mon-order/review/questions.md#L37). Nội dung đầy đủ:

> Người đặt tổng có thể quản lý nhiều khách/điểm không; role customer scope và audit QR guest/service lưu thế nào khi user_roles/sessions/audit_logs hiện yêu cầu user?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E6-CG-02

[Nguồn, dòng 8](../../../chon-mon-order/review/contract-gap-register.md#L8). Nội dung đầy đủ:

> Scope người đặt tổng một/nhiều công ty; ORD-Q11, EVID002

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-09"></a>

## DEC-09 — Nguồn định lượng sống, phần ăn được và hao hụt

Cần quyết định: Nguồn định lượng sống, phần ăn được và hao hụt?

Mã nguồn: E3-Q2, NUTR-Q02. Người quyết định: Người soạn docx, bếp trưởng; Dinh dưỡng viên, bếp trưởng. Release: R3, R4. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q2

[Nguồn, dòng 13](../../../cost/review/decision-register.md#L13). Nội dung đầy đủ:

> Định lượng sống đã gồm xương, vỏ chưa

Phương án khuyến nghị đã có:

> Xác nhận định lượng sống là trước hay sau loại xương/vỏ; chỉ áp hao hụt một lần.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Áp hai lần sẽ tăng lượng mua sai; tắt hao hụt khi định lượng đã bao gồm phần bỏ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### NUTR-Q02

[Nguồn, dòng 14](../../../dinh-duong/review/questions.md#L14). Nội dung đầy đủ:

> qty_std là gram sống còn xương/vỏ hay gram phần ăn được? Xác nhận edible_pct và quy đổi theo từng nguyên liệu để không trừ hai lần.

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-NUTR-CALC-001; công thức khung kế thừa ERD, chưa nghiệm thu dữ liệu

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-10"></a>

## DEC-10 — Chính sách hạn chốt và xử lý nguồn sau hạn

Cần quyết định: Chính sách hạn chốt và xử lý nguồn sau hạn?

Mã nguồn: Q-16, ORD-Q08, E6-CG-05. Người quyết định: chưa rõ; Giám đốc, bếp trưởng; Vận hành, người duyệt được chỉ định, BA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### Q-16

[Nguồn, dòng 423](../../00-ke-hoach-tong-the.md#L423). Nội dung đầy đủ:

> Hạn chốt ca trưa 15:00 ngày D-1 và ngưỡng đổi sau chốt (5% / 10 suất / trước 06:00) có đúng thực tế không? Ngưỡng là "nhỏ hơn trong hai" hay "lớn hơn trong hai"?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### ORD-Q08

[Nguồn, dòng 27](../../../chon-mon-order/review/questions.md#L27). Nội dung đầy đủ:

> Ngưỡng đổi sau chốt, vai trò duyệt, delta âm và khi bếp đã sản xuất xử lý thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E6-CG-05

[Nguồn, dòng 11](../../../chon-mon-order/review/contract-gap-register.md#L11). Nội dung đầy đủ:

> Hạn, thiếu nguồn, remediation, quyền/ngưỡng đổi; RV08, ORD-Q07/08/12, Q-16/O-06

Phương án khuyến nghị đã có:

> Đề xuất lệnh chọn/chốt chỉ hợp lệ khi thời điểm kiểm hạn trong transaction theo đồng hồ server nhỏ hơn deadline hiệu lực; đúng deadline thuộc sau hạn. Thiếu nguồn/counter lệch thì giữ trạng thái cũ và NEEDS_ATTENTION. Vận hành lập yêu cầu xử lý nguồn; người duyệt được chỉ định, khác người tạo/sửa cuối, quyết định ngoại lệ. Retry kỹ thuật không gia hạn.

Phương án khác đã có:

> Xét thời điểm nhận request có bằng chứng đáng tin: thân thiện hơn với độ trễ nhưng cần contract queue/clock và xử lý request tồn đọng.

Tác động / phần chặn được nguồn mô tả:

> Hạn 15:00 chỉ là ví dụ: request tới trước nhưng tới bước kiểm hạn lúc 15:00 không được coi hợp lệ chỉ nhờ giờ gửi. Chọn quy tắc rõ để kiểm race; đánh đổi: người dùng sát hạn có thể bị từ chối dù đã bấm trước hạn. Không dùng ví dụ làm giờ mặc định.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-11"></a>

## DEC-11 — Phát hành, xác nhận revision và bắt đầu sản xuất

Cần quyết định: Phát hành, xác nhận revision và bắt đầu sản xuất?

Mã nguồn: ORD-Q14, E6-CG-06. Người quyết định: Bếp trưởng, vận hành; Bếp, vận hành, BA, Tech lead. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q14

[Nguồn, dòng 40](../../../chon-mon-order/review/questions.md#L40). Nội dung đầy đủ:

> Bếp phải xác nhận nhận phiên bản kế hoạch mới không; ai phát hành/cho IN_PRODUCTION và xử lý bản in cũ?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E6-CG-06

[Nguồn, dòng 12](../../../chon-mon-order/review/contract-gap-register.md#L12). Nội dung đầy đủ:

> Expected source/completeness, publish/ack/start; RV05/06, ORD-Q03/13/14

Phương án khuyến nghị đã có:

> Worker tạo bản kế hoạch để kiểm tra; chỉ cho phát hành khi tập nguồn kỳ vọng có căn cứ, không còn nguồn thiếu và các revision được kiểm lại. Bản thiếu/UNKNOWN chỉ phục vụ xử lý, không coi đủ để sản xuất. Đề xuất vận hành được cấp quyền phát hành, bếp trưởng theo scope xác nhận đúng revision, rồi ghi bắt đầu sản xuất bằng thao tác riêng. Bản mới cần xác nhận riêng; ack cũ không áp cho bản mới.

Phương án khác đã có:

> Cho phát hành một phần với quyết định ngoại lệ, nhãn thiếu và người chịu trách nhiệm: linh hoạt nhưng tăng rủi ro thiếu suất, cần chính sách riêng.

Tác động / phần chặn được nguồn mô tả:

> A+B+C là nguồn kỳ vọng nhưng mới có A+B: không gọi 2/2 là đủ. Bản 6 không kế thừa xác nhận bản 5. Giảm nguy cơ bếp dùng thiếu nguồn/bản cũ; đánh đổi: một nguồn chậm có thể giữ cả lần phát hành.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-12"></a>

## DEC-12 — Giá công khai cho website và agent khách

Cần quyết định: Giá công khai cho website và agent khách?

Mã nguồn: E8-Q03, E9-Q04. Người quyết định: chưa rõ. Release: R8, R9. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q03

[Nguồn, dòng 20](../../../website-cong-khai/review/questions.md#L20). Nội dung đầy đủ:

> Giá suất nào được công khai; ai duyệt, thời hạn hiệu lực và cách ghi VAT/giá tham khảo ra sao?

Phương án khuyến nghị đã có:

> Bản giá công khai riêng được duyệt hoặc tham chiếu giá được cho phép; không lấy price_cap hay giá hợp đồng làm mặc định

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Giá FEAT-056, projection giá và hiệu lực

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E9-Q04

[Nguồn, dòng 21](../../../agent-dinh-duong-vien/review/questions.md#L21). Nội dung đầy đủ:

> Có hiển thị giá suất cho khách không, nguồn/hiệu lực/nhãn giá nào được duyệt?

Phương án khuyến nghị đã có:

> Projection giá public riêng hoặc không hiển thị cho đến khi có nguồn; không dùng price_cap làm giá bán

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Hiển thị giá suất; không cam kết giá

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-13"></a>

## DEC-13 — Dựng thực đơn public và tái dùng bộ kiểm

Cần quyết định: Dựng thực đơn public và tái dùng bộ kiểm?

Mã nguồn: E8-Q05, E9-Q11. Người quyết định: chưa rõ. Release: R8, R9. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q05

[Nguồn, dòng 22](../../../website-cong-khai/review/questions.md#L22). Nội dung đầy đủ:

> FEAT-057 sinh mẫu từ thư viện, thuật toán hay cách khác; có phải qua máy kiểm E2; giới hạn loại suất/số suất/kiêng kỵ/ngày/lượt là gì?

Phương án khuyến nghị đã có:

> Lọc mẫu được duyệt hoặc dựng qua bộ kiểm không lưu E2; chưa chọn. Không nới quy tắc cứng hoặc triển khai Agent E9

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Generation, kiểm quy tắc và giới hạn chính thức

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E9-Q11

[Nguồn, dòng 28](../../../agent-dinh-duong-vien/review/questions.md#L28). Nội dung đầy đủ:

> FEAT-057 E8 và FEAT-060 E9 dùng chung bộ dựng hay tách; contract kiểm nguồn/quy tắc và quyền public thế nào?

Phương án khuyến nghị đã có:

> Có thể dùng chung port kiểm thuần, hoặc bộ dựng riêng; không dùng lại credential/quota AIO

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chốt adapter/bộ dựng và reuse; không sửa FEAT-057

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-14"></a>

## DEC-14 — Lợi nhuận báo giá và công thức kết quả kinh doanh

Cần quyết định: Lợi nhuận báo giá và công thức kết quả kinh doanh?

Mã nguồn: E10-Q15, E13-Q08. Người quyết định: Kế toán và Giám đốc; chưa rõ. Release: R10, R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E10-Q15

[Nguồn, dòng 39](../../../crm-ban-hang/review/questions.md#L39). Nội dung đầy đủ:

> Biên lợi nhuận nội bộ trên báo giá dùng công thức, thành phần và nguồn phiên bản nào; ai được xem?

Phương án khuyến nghị đã có:

> Giữ giá trị chưa xác định tới khi công thức/nguồn được duyệt; quyền riêng với báo giá.

Phương án khác đã có:

> Chỉ hiển thị cost có nguồn theo quyền và bỏ chỉ số biên lợi nhuận cho tới khi được duyệt.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-QUOT-001 / UC-CRM-010

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E13-Q08

[Nguồn, dòng 32](../../../chi-phi-loi-nhuan/review/questions.md#L32). Nội dung đầy đủ:

> Kết quả kinh doanh cơ sở gồm khoản nào, nguồn chuẩn nào, ghi nhận điều chỉnh và CK ra sao?

Phương án khuyến nghị đã có:

> Cần manifest thành phần và định nghĩa có phiên bản; không suy lợi nhuận bằng doanh thu trừ riêng cost nguyên liệu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kết quả chính thức, công thức lợi nhuận; O-01, CK-Q01–10, E10-Q15; FR-EXP-RECON-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-15"></a>

## DEC-15 — Nguồn công khai, độ đầy đủ và tính mới

Cần quyết định: Nguồn công khai, độ đầy đủ và tính mới?

Mã nguồn: E8-Q04, E9-Q12. Người quyết định: chưa rõ. Release: R8, R9. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q04

[Nguồn, dòng 21](../../../website-cong-khai/review/questions.md#L21). Nội dung đầy đủ:

> Nguồn E2/E4 ở trạng thái nào đủ điều kiện hiển thị định lượng, 4 chỉ số và dị ứng; làm gì khi stale/thu hồi/thiếu?

Phương án khuyến nghị đã có:

> Tham chiếu menu PUBLISHED, recipe ACTIVE đúng ngày và calculation có provenance; thêm phê duyệt công khai khi cần. NUTR chưa có trạng thái duyệt riêng

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Public snapshot/refresh, R4, độ đầy đủ dữ liệu FEAT-056

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

### E9-Q12

[Nguồn, dòng 29](../../../agent-dinh-duong-vien/review/questions.md#L29). Nội dung đầy đủ:

> Nguồn nào đủ điều kiện public; stale/thu hồi/thiếu dinh dưỡng/dị ứng xử lý ra sao; tuần/ngày phục vụ và nhiều cỡ?

Phương án khuyến nghị đã có:

> Projection có phiên bản nguồn, không coi thiếu là 0 hoặc không dị ứng; refresh phải kiểm lại

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kết quả thật, nhãn đầy đủ, mapping ngày/cỡ

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-16"></a>

## DEC-16 — Trường học, bệnh viện, tiệc cỗ có trong bản đầu không

Cần quyết định: Trường học, bệnh viện, tiệc cỗ có trong bản đầu không?

Mã nguồn: O-05. Người quyết định: Giám đốc. Release: R6. [Buổi 1](meeting-agenda.md#buoi-1).

### O-05

[Nguồn, dòng 254](../../01-prd.md#L254). Nội dung đầy đủ:

> Trường học, bệnh viện, tiệc cỗ có trong bản đầu không

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-17"></a>

## DEC-17 — Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không?

Cần quyết định: Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không?

Mã nguồn: E1-Q02. Người quyết định: Tech lead. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### E1-Q02

[Nguồn, dòng 23](../../../nen-tang/review/questions.md#L23). Nội dung đầy đủ:

> Scope/store/retention idempotency, mã lỗi key reuse và secret một lần được duyệt theo hợp đồng này không?

Phương án khuyến nghị đã có:

> Không replay mật khẩu tạm; backend store/transaction chưa có

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-18"></a>

## DEC-18 — MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể?

Cần quyết định: MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể?

Mã nguồn: E1-Q03. Người quyết định: Giám đốc, Tech lead. Release: chưa rõ. [Buổi 1](meeting-agenda.md#buoi-1).

### E1-Q03

[Nguồn, dòng 24](../../../nen-tang/review/questions.md#L24). Nội dung đầy đủ:

> MFA nếu N-04 bật: enrollment, reset thiết bị, recovery và chống replay cụ thể?

Phương án khuyến nghị đã có:

> P1 gated; không tự triển khai chỉ dựa ô nhập6 số

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-19"></a>

## DEC-19 — Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu?

Cần quyết định: Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu?

Mã nguồn: E1-Q04. Người quyết định: BA, Tech lead. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### E1-Q04

[Nguồn, dòng 25](../../../nen-tang/review/questions.md#L25). Nội dung đầy đủ:

> Thông báo có mở lại RESOLVED không; dedupe event và version lưu ở đâu?

Phương án khuyến nghị đã có:

> Đề xuất NEW→SEEN→RESOLVED; bảng notifications hiện chưa có version/event key; cần delta trước backend

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-20"></a>

## DEC-20 — Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào?

Cần quyết định: Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào?

Mã nguồn: E1-Q05. Người quyết định: Giám đốc. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### E1-Q05

[Nguồn, dòng 26](../../../nen-tang/review/questions.md#L26). Nội dung đầy đủ:

> Vai trò nào được đọc audit nhạy cảm, log toàn hệ thống; tự khóa/xóa QUAN_TRI cuối cùng xử lý thế nào?

Phương án khuyến nghị đã có:

> Chưa thêm quyền nghiệp vụ cho QUAN_TRI; cần quyết định trước vận hành

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-21"></a>

## DEC-21 — Nhân viên đăng nhập bằng số điện thoại, email, hay tên do quản trị đặt? (Bếp trưởng có thể không có email công việc.)

Cần quyết định: Nhân viên đăng nhập bằng số điện thoại, email, hay tên do quản trị đặt? (Bếp trưởng có thể không có email công việc.)?

Mã nguồn: N-01. Người quyết định: Giám đốc. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### N-01

[Nguồn, dòng 403](../../../nen-tang/srs/spec.md#L403). Nội dung đầy đủ:

> Nhân viên đăng nhập bằng số điện thoại, email, hay tên do quản trị đặt? (Bếp trưởng có thể không có email công việc.)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-22"></a>

## DEC-22 — Ai giữ vai trò quản trị hệ thống: người của Gia Phát hay đội phát triển?

Cần quyết định: Ai giữ vai trò quản trị hệ thống: người của Gia Phát hay đội phát triển?

Mã nguồn: N-02. Người quyết định: Giám đốc. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### N-02

[Nguồn, dòng 404](../../../nen-tang/srs/spec.md#L404). Nội dung đầy đủ:

> Ai giữ vai trò quản trị hệ thống: người của Gia Phát hay đội phát triển?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-23"></a>

## DEC-23 — Thời gian lưu nhật ký thay đổi (đề xuất 5 năm) và nhật ký đăng nhập (đề xuất 1 năm)

Cần quyết định: Thời gian lưu nhật ký thay đổi (đề xuất 5 năm) và nhật ký đăng nhập (đề xuất 1 năm)?

Mã nguồn: N-03. Người quyết định: Giám đốc, kế toán. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### N-03

[Nguồn, dòng 405](../../../nen-tang/srs/spec.md#L405). Nội dung đầy đủ:

> Thời gian lưu nhật ký thay đổi (đề xuất 5 năm) và nhật ký đăng nhập (đề xuất 1 năm)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-24"></a>

## DEC-24 — Có bắt buộc xác thực 2 bước cho Giám đốc, kế toán doanh thu, quản trị không?

Cần quyết định: Có bắt buộc xác thực 2 bước cho Giám đốc, kế toán doanh thu, quản trị không?

Mã nguồn: N-04. Người quyết định: Giám đốc. Release: chưa rõ. [Buổi 1](meeting-agenda.md#buoi-1).

### N-04

[Nguồn, dòng 406](../../../nen-tang/srs/spec.md#L406). Nội dung đầy đủ:

> Có bắt buộc xác thực 2 bước cho Giám đốc, kế toán doanh thu, quản trị không?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-25"></a>

## DEC-25 — Kênh thông báo ngoài (Zalo OA, SMS, email)

Cần quyết định: Kênh thông báo ngoài (Zalo OA, SMS, email)?

Mã nguồn: Q-14. Người quyết định: Giám đốc. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### Q-14

[Nguồn, dòng 407](../../../nen-tang/srs/spec.md#L407). Nội dung đầy đủ:

> Kênh thông báo ngoài (Zalo OA, SMS, email)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-26"></a>

## DEC-26 — Số người ăn, số công ty, số điểm giao mỗi ngày

Cần quyết định: Số người ăn, số công ty, số điểm giao mỗi ngày?

Mã nguồn: Q-18. Người quyết định: Giám đốc. Release: R1. [Buổi 1](meeting-agenda.md#buoi-1).

### Q-18

[Nguồn, dòng 408](../../../nen-tang/srs/spec.md#L408). Nội dung đầy đủ:

> Số người ăn, số công ty, số điểm giao mỗi ngày

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-27"></a>

## DEC-27 — Duyệt 43 quy tắc

Cần quyết định: Duyệt 43 quy tắc?

Mã nguồn: DL-01. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### DL-01

[Nguồn, dòng 440](../../../thuc-don-dinh-luong/srs/spec.md#L440). Nội dung đầy đủ:

> Duyệt 43 quy tắc

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-28"></a>

## DEC-28 — Cách kiểm ngưỡng giá suất

Cần quyết định: Cách kiểm ngưỡng giá suất?

Mã nguồn: E2-Q1. Người quyết định: Dinh dưỡng viên, Giám đốc. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q1

[Nguồn, dòng 444](../../../thuc-don-dinh-luong/srs/spec.md#L444). Nội dung đầy đủ:

> Cách kiểm ngưỡng giá suất

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-29"></a>

## DEC-29 — Quy tắc tuần có xét tuần trước không

Cần quyết định: Quy tắc tuần có xét tuần trước không?

Mã nguồn: E2-Q2. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q2

[Nguồn, dòng 445](../../../thuc-don-dinh-luong/srs/spec.md#L445). Nội dung đầy đủ:

> Quy tắc tuần có xét tuần trước không

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-30"></a>

## DEC-30 — Tuần phục vụ gồm những ngày nào

Cần quyết định: Tuần phục vụ gồm những ngày nào?

Mã nguồn: E2-Q3. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q3

[Nguồn, dòng 446](../../../thuc-don-dinh-luong/srs/spec.md#L446). Nội dung đầy đủ:

> Tuần phục vụ gồm những ngày nào

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-31"></a>

## DEC-31 — Thực đơn chung hay riêng theo khách

Cần quyết định: Thực đơn chung hay riêng theo khách?

Mã nguồn: E2-Q4. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q4

[Nguồn, dòng 447](../../../thuc-don-dinh-luong/srs/spec.md#L447). Nội dung đầy đủ:

> Thực đơn chung hay riêng theo khách

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-32"></a>

## DEC-32 — Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)

Cần quyết định: Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)?

Mã nguồn: E2-Q6. Người quyết định: Dinh dưỡng viên, người duyệt. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q6

[Nguồn, dòng 448](../../../thuc-don-dinh-luong/srs/spec.md#L448). Nội dung đầy đủ:

> Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-33"></a>

## DEC-33 — Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?

Cần quyết định: Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?

Mã nguồn: E2-Q7. Người quyết định: Giám đốc. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q7

[Nguồn, dòng 449](../../../thuc-don-dinh-luong/srs/spec.md#L449). Nội dung đầy đủ:

> Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-34"></a>

## DEC-34 — Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?

Cần quyết định: Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?

Mã nguồn: E2-Q8. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q8

[Nguồn, dòng 450](../../../thuc-don-dinh-luong/srs/spec.md#L450). Nội dung đầy đủ:

> Có cần thu hồi và sửa từng ngày của thực đơn đã công bố, thay vì cả tuần?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-35"></a>

## DEC-35 — Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)

Cần quyết định: Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)?

Mã nguồn: E2-Q9. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q9

[Nguồn, dòng 451](../../../thuc-don-dinh-luong/srs/spec.md#L451). Nội dung đầy đủ:

> Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-36"></a>

## DEC-36 — Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)

Cần quyết định: Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)?

Mã nguồn: E2-Q10. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q10

[Nguồn, dòng 452](../../../thuc-don-dinh-luong/srs/spec.md#L452). Nội dung đầy đủ:

> Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-37"></a>

## DEC-37 — Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)

Cần quyết định: Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)?

Mã nguồn: E2-Q11. Người quyết định: Người duyệt. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q11

[Nguồn, dòng 453](../../../thuc-don-dinh-luong/srs/spec.md#L453). Nội dung đầy đủ:

> Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt)

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-38"></a>

## DEC-38 — Khoảng định lượng và chất độn dùng chuẩn từng món hay bảng theo nguyên liệu/kiểu món; lưu ở đâu?

Cần quyết định: Khoảng định lượng và chất độn dùng chuẩn từng món hay bảng theo nguyên liệu/kiểu món; lưu ở đâu?

Mã nguồn: E2-Q5. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### E2-Q5

[Nguồn, dòng 454](../../../thuc-don-dinh-luong/srs/spec.md#L454). Nội dung đầy đủ:

> Khoảng định lượng chuẩn và mức chất độn cho phép lưu ở đâu: theo từng món (chính là qty_min–qty_max của công thức, khi đó BR-COST-008 tự thoả), hay có một bảng chuẩn theo loại nguyên liệu và kiểu món như bảng trong docx để mọi công thức phải nằm trong đó?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-39"></a>

## DEC-39 — Món Healthy chỉ được luộc, hay hấp / áp chảo ít dầu / nướng cũng được tính?

Cần quyết định: Món Healthy chỉ được luộc, hay hấp / áp chảo ít dầu / nướng cũng được tính?

Mã nguồn: H-1. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-1

[Nguồn, dòng 120](../../brainstorms/quy-tac-thuc-don.md#L120). Nội dung đầy đủ:

> Món Healthy chỉ được luộc, hay hấp / áp chảo ít dầu / nướng cũng được tính?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-40"></a>

## DEC-40 — "Nhiều ngày liên tiếp" là mấy ngày? Thịt lợn có được nới hơn các nhóm khác không (vì dùng nhiều nhất)?

Cần quyết định: "Nhiều ngày liên tiếp" là mấy ngày? Thịt lợn có được nới hơn các nhóm khác không (vì dùng nhiều nhất)?

Mã nguồn: H-2. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-2

[Nguồn, dòng 121](../../brainstorms/quy-tac-thuc-don.md#L121). Nội dung đầy đủ:

> "Nhiều ngày liên tiếp" là mấy ngày? Thịt lợn có được nới hơn các nhóm khác không (vì dùng nhiều nhất)?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-41"></a>

## DEC-41 — Duyệt danh sách nhóm nguyên liệu chính nào để so trùng; sườn tách riêng hay gộp vào lợn?

Cần quyết định: Duyệt danh sách nhóm nguyên liệu chính nào để so trùng; sườn tách riêng hay gộp vào lợn?

Mã nguồn: H-3. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-3

[Nguồn, dòng 122](../../brainstorms/quy-tac-thuc-don.md#L122). Nội dung đầy đủ:

> Danh sách nhóm nguyên liệu chính để máy so trùng — đề xuất: lợn, gà, bò, ếch, tôm, cá, sườn, trứng, đậu phụ, giò/chả, khác. Sườn tính riêng hay gộp vào lợn?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-42"></a>

## DEC-42 — Ngoài "nem – nộm" còn những cặp món nào không được xếp cùng ngày?

Cần quyết định: Ngoài "nem – nộm" còn những cặp món nào không được xếp cùng ngày?

Mã nguồn: H-4. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-4

[Nguồn, dòng 123](../../brainstorms/quy-tac-thuc-don.md#L123). Nội dung đầy đủ:

> Ngoài "nem – nộm" còn những cặp món nào không được xếp cùng ngày?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-43"></a>

## DEC-43 — Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào?

Cần quyết định: Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào?

Mã nguồn: H-5. Người quyết định: Dinh dưỡng viên. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-5

[Nguồn, dòng 124](../../brainstorms/quy-tac-thuc-don.md#L124). Nội dung đầy đủ:

> Có đặt mức năng lượng/đạm tối thiểu cho một suất không? Nếu có thì bao nhiêu, theo nhóm người ăn nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-44"></a>

## DEC-44 — Danh sách phương pháp chế biến — đề xuất: luộc, hấp, kho, rang, xào, sốt, chiên/rán, áp chảo, nướng, nộm/trộn, cuốn. Thiếu hoặc thừa gì?

Cần quyết định: Danh sách phương pháp chế biến — đề xuất: luộc, hấp, kho, rang, xào, sốt, chiên/rán, áp chảo, nướng, nộm/trộn, cuốn. Thiếu hoặc thừa gì?

Mã nguồn: H-8. Người quyết định: Người soạn docx. Release: R2. [Buổi 2](meeting-agenda.md#buoi-2).

### H-8

[Nguồn, dòng 127](../../brainstorms/quy-tac-thuc-don.md#L127). Nội dung đầy đủ:

> Danh sách phương pháp chế biến — đề xuất: luộc, hấp, kho, rang, xào, sốt, chiên/rán, áp chảo, nướng, nộm/trộn, cuốn. Thiếu hoặc thừa gì?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-45"></a>

## DEC-45 — Cost phần món chính

Cần quyết định: Cost phần món chính?

Mã nguồn: E3-Q1. Người quyết định: Giám đốc, kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q1

[Nguồn, dòng 12](../../../cost/review/decision-register.md#L12). Nội dung đầy đủ:

> Cost phần món chính

Phương án khuyến nghị đã có:

> Cân nhắc DAT_NHAT giai đoạn đầu; so với BINH_QUAN/MAC_DINH trên10 ngày thực tế trước khi chọn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> DAT_NHAT thận trọng nhưng có thể cao hơn cơ cấu chọn thực tế.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-46"></a>

## DEC-46 — Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào

Cần quyết định: Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào?

Mã nguồn: E3-Q3. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q3

[Nguồn, dòng 14](../../../cost/review/decision-register.md#L14). Nội dung đầy đủ:

> Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-47"></a>

## DEC-47 — Giá nào là giá tham chiếu

Cần quyết định: Giá nào là giá tham chiếu?

Mã nguồn: E3-Q4. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q4

[Nguồn, dòng 15](../../../cost/review/decision-register.md#L15). Nội dung đầy đủ:

> Giá nào là giá tham chiếu

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-48"></a>

## DEC-48 — Tần suất cập nhật giá thực tế

Cần quyết định: Tần suất cập nhật giá thực tế?

Mã nguồn: E3-Q5. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q5

[Nguồn, dòng 16](../../../cost/review/decision-register.md#L16). Nội dung đầy đủ:

> Tần suất cập nhật giá thực tế

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-49"></a>

## DEC-49 — Giá nhập có cần duyệt

Cần quyết định: Giá nhập có cần duyệt?

Mã nguồn: E3-Q6. Người quyết định: Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q6

[Nguồn, dòng 17](../../../cost/review/decision-register.md#L17). Nội dung đầy đủ:

> Giá nhập có cần duyệt

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-50"></a>

## DEC-50 — Định nghĩa cost cao / thấp

Cần quyết định: Định nghĩa cost cao / thấp?

Mã nguồn: E3-Q7. Người quyết định: Người soạn docx. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q7

[Nguồn, dòng 18](../../../cost/review/decision-register.md#L18). Nội dung đầy đủ:

> Định nghĩa cost cao / thấp

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-51"></a>

## DEC-51 — Nguồn số suất trước khi có order

Cần quyết định: Nguồn số suất trước khi có order?

Mã nguồn: E3-Q8. Người quyết định: Dinh dưỡng viên. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q8

[Nguồn, dòng 19](../../../cost/review/decision-register.md#L19). Nội dung đầy đủ:

> Nguồn số suất trước khi có order

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-52"></a>

## DEC-52 — Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ

Cần quyết định: Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ?

Mã nguồn: E3-Q9. Người quyết định: Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q9

[Nguồn, dòng 20](../../../cost/review/decision-register.md#L20). Nội dung đầy đủ:

> Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-53"></a>

## DEC-53 — Chặn chuyển bếp

Cần quyết định: Chặn chuyển bếp?

Mã nguồn: E3-Q10. Người quyết định: Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q10

[Nguồn, dòng 21](../../../cost/review/decision-register.md#L21). Nội dung đầy đủ:

> Chặn chuyển bếp

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-54"></a>

## DEC-54 — Bếp trưởng có xem giá và cost

Cần quyết định: Bếp trưởng có xem giá và cost?

Mã nguồn: E3-Q11. Người quyết định: Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q11

[Nguồn, dòng 22](../../../cost/review/decision-register.md#L22). Nội dung đầy đủ:

> Bếp trưởng có xem giá và cost

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-55"></a>

## DEC-55 — Khi tính BINH_QUAN hoặc DAT_NHAT, món chính Healthy (thường rẻ hơn) có được tính vào không

Cần quyết định: Khi tính BINH_QUAN hoặc DAT_NHAT, món chính Healthy (thường rẻ hơn) có được tính vào không?

Mã nguồn: E3-Q12. Người quyết định: Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q12

[Nguồn, dòng 25](../../../cost/review/decision-register.md#L25). Nội dung đầy đủ:

> Khi tính BINH_QUAN hoặc DAT_NHAT, món chính Healthy (thường rẻ hơn) có được tính vào không

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-56"></a>

## DEC-56 — Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không

Cần quyết định: Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không?

Mã nguồn: E3-Q13. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q13

[Nguồn, dòng 26](../../../cost/review/decision-register.md#L26). Nội dung đầy đủ:

> Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không

Phương án khuyến nghị đã có:

> Giữ phương án SRS làm ứng viên; chủ sở hữu xác nhận hoặc nêu phương án khác.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chưa có bằng chứng để tự quyết thay nghiệp vụ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-57"></a>

## DEC-57 — FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không?

Cần quyết định: FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không?

Mã nguồn: E3-Q14. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q14

[Nguồn, dòng 27](../../../cost/review/decision-register.md#L27). Nội dung đầy đủ:

> FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không?

Phương án khuyến nghị đã có:

> Giữ giá đã hiệu lực bất biến, chỉ đổi tham chiếu tương lai; nếu cần hồi tố phải thiết kế nghiệp vụ riêng.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Dễ kiểm toán nhưng kế toán không sửa cờ lịch sử trực tiếp.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-58"></a>

## DEC-58 — Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick

Cần quyết định: Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick?

Mã nguồn: E3-Q15. Người quyết định: Dinh dưỡng viên. Release: chưa rõ. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q15

[Nguồn, dòng 28](../../../cost/review/decision-register.md#L28). Nội dung đầy đủ:

> Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick

Phương án khuyến nghị đã có:

> R3 giới hạn K=1; chỉ mở K>1 khi xác nhận tổng lượt chọn chia hết K và cách xử lý phần dư.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Giảm rủi ro suy ra sai số suất; hạn chế loại suất nhiều món chính.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-59"></a>

## DEC-59 — Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá?

Cần quyết định: Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá?

Mã nguồn: E3-Q16. Người quyết định: Giám đốc, kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### E3-Q16

[Nguồn, dòng 29](../../../cost/review/decision-register.md#L29). Nội dung đầy đủ:

> Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá?

Phương án khuyến nghị đã có:

> Cân nhắc cùng món/cỡ/cơ sở, ngày lập đến ngày phục vụ <=N ngày; chốt riêng công thức đổi có làm hết hiệu lực không.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không tái dùng bảng khác cơ sở nếu chưa có quy tắc; tăng số bảng cần duyệt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-60"></a>

## DEC-60 — Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào?

Cần quyết định: Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào?

Mã nguồn: FLOW-COST-Q01. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q01

[Nguồn, dòng 30](../../../cost/review/decision-register.md#L30). Nội dung đầy đủ:

> Huỷ giá tham chiếu tương lai khi cùng ngày còn báo giá khác thì chọn giá thay thế thế nào?

Phương án khuyến nghị đã có:

> Yêu cầu chọn giá thay thế trong cùng giao dịch hủy, nếu còn báo giá khác cùng nhóm.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không tự chọn NCC; lỗi ở một bước rollback cả hai thay đổi.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-61"></a>

## DEC-61 — Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào?

Cần quyết định: Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào?

Mã nguồn: FLOW-COST-Q02. Người quyết định: Tech lead và BA. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q02

[Nguồn, dòng 31](../../../cost/review/decision-register.md#L31). Nội dung đầy đủ:

> Chống gửi trùng và đối soát khi mất phản hồi: request key/phiên bản/lịch sử trả ra thế nào?

Phương án khuyến nghị đã có:

> Review phương án API hiện có: key/hash theo actor/method/path, TTL24h, đối soát, commit nguyên tử.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Cần kho bền vững và migration; retry không được vượt quyền hiện tại.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-62"></a>

## DEC-62 — Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào?

Cần quyết định: Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào?

Mã nguồn: FLOW-COST-Q03. Người quyết định: BA, kế toán, Tech lead. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q03

[Nguồn, dòng 32](../../../cost/review/decision-register.md#L32). Nội dung đầy đủ:

> Cảnh báo giá cũ/nhà cung cấp ngừng được lưu, đóng và chống trùng thế nào?

Phương án khuyến nghị đã có:

> Tạo thiết kế cảnh báo nguyên liệu riêng, không dùng cost_alerts bắt buộc menu_day_id.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chốt khóa chống trùng theo nguyên liệu hay nguyên liệu/cơ sở trước thiết kế bảng.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-63"></a>

## DEC-63 — Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào?

Cần quyết định: Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào?

Mã nguồn: FLOW-COST-Q04. Người quyết định: Kế toán, UX/BA. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q04

[Nguồn, dòng 33](../../../cost/review/decision-register.md#L33). Nội dung đầy đủ:

> Cost món hoặc cost phiên bản cũ bằng 0 thì tỷ trọng/chênh lệch % hiện thế nào?

Phương án khuyến nghị đã có:

> Hiện dấu — và ghi Không áp dụng khi mẫu số0; giữ delta tiền nếu tính được.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không trả Infinity/NaN, không biến delta% thành0 gây hiểu nhầm.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-64"></a>

## DEC-64 — Ai được đọc danh sách/chi tiết khoản khoán?

Cần quyết định: Ai được đọc danh sách/chi tiết khoản khoán?

Mã nguồn: FLOW-COST-Q05. Người quyết định: Giám đốc, BA. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q05

[Nguồn, dòng 34](../../../cost/review/decision-register.md#L34). Nội dung đầy đủ:

> Ai được đọc danh sách/chi tiết khoản khoán?

Phương án khuyến nghị đã có:

> Xác nhận ma trận đọc danh mục quản trị riêng với quyền xem khoản trong phân rã cost.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Cần phân biệt số liệu người xem cost được biết với quyền xem đề nghị quản trị.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-65"></a>

## DEC-65 — Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào?

Cần quyết định: Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào?

Mã nguồn: FLOW-COST-Q06. Người quyết định: Giám đốc, kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q06

[Nguồn, dòng 35](../../../cost/review/decision-register.md#L35). Nội dung đầy đủ:

> Giá/tham số đổi trong thời gian PENDING: kiểm lại tại duyệt cuối hay chụp bộ giá lúc gửi? Nếu vượt mới thì trả lại thế nào?

Phương án khuyến nghị đã có:

> Cân nhắc kiểm lại tại duyệt cuối; nếu đủ điều kiện thì chụp bộ vừa kiểm cùng transaction.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Khi mới vượt ở CHAN cần trả lại hoặc giữ PENDING? phải chốt trạng thái; không tự chuyển.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-66"></a>

## DEC-66 — Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ?

Cần quyết định: Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ?

Mã nguồn: FLOW-COST-Q07. Người quyết định: Kế toán, dinh dưỡng viên. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q07

[Nguồn, dòng 36](../../../cost/review/decision-register.md#L36). Nội dung đầy đủ:

> Lập tuần có một ngày lỗi thì rollback cả tuần hay lưu ngày hợp lệ?

Phương án khuyến nghị đã có:

> Cân nhắc all-or-nothing cho cả batch tuần; trả lỗi theo ngày, không ghi ngày hợp lệ khi có lỗi.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Dễ đối soát/retry nhưng phải sửa mọi ngày lỗi trước khi có kết quả tuần.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-67"></a>

## DEC-67 — Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao?

Cần quyết định: Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao?

Mã nguồn: FLOW-COST-Q08. Người quyết định: Giám đốc, dinh dưỡng viên. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q08

[Nguồn, dòng 37](../../../cost/review/decision-register.md#L37). Nội dung đầy đủ:

> Thực đơn đã được duyệt vượt ngưỡng ở CANH_BAO: giá tăng tiếp hoặc phục hồi rồi vượt lại thì phát cảnh báo ra sao?

Phương án khuyến nghị đã có:

> Tách hai tình huống: vốn vượt khi duyệt và phục hồi rồi vượt lại; xác định có mở cảnh báo mới hay cập nhật lịch sử.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không dùng mức tăng tùy ý để phát thông báo; cần tránh lặp cảnh báo đang mở.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-68"></a>

## DEC-68 — Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không?

Cần quyết định: Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không?

Mã nguồn: FLOW-COST-Q09. Người quyết định: BA, chủ sản phẩm/AI lead. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q09

[Nguồn, dòng 38](../../../cost/review/decision-register.md#L38). Nội dung đầy đủ:

> Agent gặp đồng thời ngày vượt và ngày không tính được: ưu tiên trạng thái nào? VAT chưa cấu hình có cùng KHONG_XAC_DINH không?

Phương án khuyến nghị đã có:

> Cân nhắc KHONG_XAC_DINH ưu tiên khi bất kỳ ngày/cơ sở không tính được, kể cả thiếu VAT.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Tránh kết luận toàn bộ đã đánh giá, nhưng che mất một vi phạm đã chắc chắn; PO phải chọn.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-69"></a>

## DEC-69 — Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào?

Cần quyết định: Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào?

Mã nguồn: FLOW-COST-Q10. Người quyết định: Giám đốc, kế toán. Release: chưa rõ. [Buổi 3](meeting-agenda.md#buoi-3).

### FLOW-COST-Q10

[Nguồn, dòng 39](../../../cost/review/decision-register.md#L39). Nội dung đầy đủ:

> Mô phỏng giá P2 cho ai dùng, xét trạng thái và khoảng ngày nào?

Phương án khuyến nghị đã có:

> Giữ P2; chốt vai trò, phạm vi cơ sở, trạng thái thực đơn và cửa sổ ngày trước khi mở.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không tăng phạm vi R3 để hoàn tất một màn mẫu.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-70"></a>

## DEC-70 — NCC tồn tại INACTIVE trả 404-01 hay 422-02?

Cần quyết định: NCC tồn tại INACTIVE trả 404-01 hay 422-02?

Mã nguồn: QA-COST-Q01. Người quyết định: BA, Tech lead. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### QA-COST-Q01

[Nguồn, dòng 42](../../../cost/review/decision-register.md#L42). Nội dung đầy đủ:

> NCC tồn tại INACTIVE trả 404-01 hay 422-02?

Phương án khuyến nghị đã có:

> Cân nhắc422-02 khi NCC tồn tại nhưng INACTIVE;404-01 chỉ tham chiếu không tồn tại hoặc nguyên liệu không dùng.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Phải sửa câu chữ404-01 và đồng bộ các client; ngoài phạm vi vẫn dùng404 theo SYS.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-71"></a>

## DEC-71 — Chiết khấu % tính trên tiền suất đã gồm VAT hay chưa VAT? Cơ sở tính có bao gồm khoản phụ thu nào không?

Cần quyết định: Chiết khấu % tính trên tiền suất đã gồm VAT hay chưa VAT? Cơ sở tính có bao gồm khoản phụ thu nào không?

Mã nguồn: CK-Q01. Người quyết định: Kế toán, người phụ trách thỏa thuận khách. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q01

[Nguồn, dòng 91](../../../cost/accounting/business-rules.md#L91). Nội dung đầy đủ:

> Chiết khấu % tính trên tiền suất đã gồm VAT hay chưa VAT? Cơ sở tính có bao gồm khoản phụ thu nào không?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-72"></a>

## DEC-72 — Chiết khấu áp dụng mọi suất hay từng loại/dòng; số lượng căn cứ đặt, giao hay khách xác nhận?

Cần quyết định: Chiết khấu áp dụng mọi suất hay từng loại/dòng; số lượng căn cứ đặt, giao hay khách xác nhận?

Mã nguồn: CK-Q02. Người quyết định: Kế toán, vận hành, người phụ trách khách. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q02

[Nguồn, dòng 92](../../../cost/accounting/business-rules.md#L92). Nội dung đầy đủ:

> Khoản chiết khấu áp dụng cho mọi suất trong đơn hay chỉ một số loại suất/dòng? Số suất tính theo đặt hàng, giao thực tế hay số được khách xác nhận?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-73"></a>

## DEC-73 — Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào?

Cần quyết định: Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào?

Mã nguồn: CK-Q03. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q03

[Nguồn, dòng 93](../../../cost/accounting/business-rules.md#L93). Nội dung đầy đủ:

> Làm tròn tiền chiết khấu theo từng suất, từng dòng hay tổng đơn? Làm tròn tới đơn vị nào và theo cách nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-74"></a>

## DEC-74 — Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai?

Cần quyết định: Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai?

Mã nguồn: CK-Q05. Người quyết định: Kế toán, người phụ trách thỏa thuận khách. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q05

[Nguồn, dòng 95](../../../cost/accounting/business-rules.md#L95). Nội dung đầy đủ:

> Khoản riêng được chi tiền, chuyển khoản, bù trừ ở kỳ/đơn sau hay chỉ theo dõi? Người nhận/đối tượng được hưởng là ai?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-75"></a>

## DEC-75 — Xác nhận/xử lý chiết khấu lúc chốt, giao, thanh toán hay cuối kỳ; xử lý một phần và chứng từ thế nào?

Cần quyết định: Xác nhận/xử lý chiết khấu lúc chốt, giao, thanh toán hay cuối kỳ; xử lý một phần và chứng từ thế nào?

Mã nguồn: CK-Q06. Người quyết định: Kế toán. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q06

[Nguồn, dòng 96](../../../cost/accounting/business-rules.md#L96). Nội dung đầy đủ:

> Khoản chiết khấu được xác nhận và xử lý vào lúc nào: khi chốt đơn, giao xong, khách thanh toán hay cuối kỳ? Có xử lý một phần không; cần chứng từ gì để ghi đã xử lý?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-76"></a>

## DEC-76 — Đơn đổi suất/giá/loại khi chiết khấu chưa xử lý: tự tính lại, duyệt lại và giữ phiên bản cũ thế nào?

Cần quyết định: Đơn đổi suất/giá/loại khi chiết khấu chưa xử lý: tự tính lại, duyệt lại và giữ phiên bản cũ thế nào?

Mã nguồn: CK-Q07. Người quyết định: Kế toán, vận hành, người duyệt. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q07

[Nguồn, dòng 97](../../../cost/accounting/business-rules.md#L97). Nội dung đầy đủ:

> Nếu đơn đổi số suất, giá hoặc loại suất khi chiết khấu chưa duyệt/đã duyệt nhưng chưa xử lý, có tính lại tự động không? Có phải duyệt lại, và giữ phiên bản cũ thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-77"></a>

## DEC-77 — Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không?

Cần quyết định: Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không?

Mã nguồn: CK-Q08. Người quyết định: Kế toán, người duyệt. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q08

[Nguồn, dòng 98](../../../cost/accounting/business-rules.md#L98). Nội dung đầy đủ:

> Nếu đơn bị hủy toàn bộ hoặc một phần, khoản chiết khấu chưa xử lý được hủy/giảm thế nào? Ai xác nhận và có bắt buộc lý do không?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-78"></a>

## DEC-78 — Đơn đổi/hủy sau chi trả/bù trừ: thu hồi, bù kỳ sau hay điều chỉnh riêng; ai duyệt, chứng từ nào?

Cần quyết định: Đơn đổi/hủy sau chi trả/bù trừ: thu hồi, bù kỳ sau hay điều chỉnh riêng; ai duyệt, chứng từ nào?

Mã nguồn: CK-Q09. Người quyết định: Kế toán, Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q09

[Nguồn, dòng 99](../../../cost/accounting/business-rules.md#L99). Nội dung đầy đủ:

> Nếu chiết khấu đã chi trả/bù trừ rồi đơn mới đổi hoặc hủy, xử lý phần chênh lệch bằng thu hồi, bù kỳ sau hay khoản điều chỉnh riêng? Ai duyệt và cần chứng từ nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-79"></a>

## DEC-79 — Một đơn hưởng đồng thời chiết khấu %/tiền mỗi suất hoặc nhiều chương trình được không; cộng dồn, ưu tiên, trần thế nào?

Cần quyết định: Một đơn hưởng đồng thời chiết khấu %/tiền mỗi suất hoặc nhiều chương trình được không; cộng dồn, ưu tiên, trần thế nào?

Mã nguồn: CK-Q10. Người quyết định: Người phụ trách thỏa thuận khách, kế toán, Giám đốc. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### CK-Q10

[Nguồn, dòng 100](../../../cost/accounting/business-rules.md#L100). Nội dung đầy đủ:

> Một đơn có được hưởng đồng thời chiết khấu % và tiền/suất hoặc nhiều chương trình không? Nếu có, cộng dồn hay ưu tiên chương trình nào; có mức trần không?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-80"></a>

## DEC-80 — Ai phụ trách cung cấp và xác nhận 10 món/10 ngày thực tế? Khi nào có dữ liệu?

Cần quyết định: Ai phụ trách cung cấp và xác nhận 10 món/10 ngày thực tế? Khi nào có dữ liệu?

Mã nguồn: DATA-COST-Q01. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q01

[Nguồn, dòng 90](../../../cost/review/accountant-input.md#L90). Nội dung đầy đủ:

> Ai phụ trách cung cấp và xác nhận10 món/10 ngày thực tế? Khi nào có dữ liệu?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-81"></a>

## DEC-81 — File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào?

Cần quyết định: File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào?

Mã nguồn: DATA-COST-Q02. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q02

[Nguồn, dòng 91](../../../cost/review/accountant-input.md#L91). Nội dung đầy đủ:

> File/bảng nguồn ở đâu, thuộc cơ sở và ngày nào, phiên bản nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-82"></a>

## DEC-82 — Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào?

Cần quyết định: Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào?

Mã nguồn: DATA-COST-Q03. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q03

[Nguồn, dòng 92](../../../cost/review/accountant-input.md#L92). Nội dung đầy đủ:

> Mỗi món có công thức, đơn vị/quy đổi, giá báo/giá cuối cóVAT và nguồn giá nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-83"></a>

## DEC-83 — Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào?

Cần quyết định: Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào?

Mã nguồn: DATA-COST-Q04. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q04

[Nguồn, dòng 93](../../../cost/review/accountant-input.md#L93). Nội dung đầy đủ:

> Mỗi ngày dùng VAT bán ra, định mức, cách tính chính, hao hụt và khoản khoán nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-84"></a>

## DEC-84 — Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập?

Cần quyết định: Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập?

Mã nguồn: DATA-COST-Q05. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q05

[Nguồn, dòng 94](../../../cost/review/accountant-input.md#L94). Nội dung đầy đủ:

> Kết quả tính tay chưa/sau làm tròn là bao nhiêu, ai review độc lập?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-85"></a>

## DEC-85 — Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào?

Cần quyết định: Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào?

Mã nguồn: DATA-COST-Q06. Người quyết định: chưa rõ. Release: R3. [Buổi 3](meeting-agenda.md#buoi-3).

### DATA-COST-Q06

[Nguồn, dòng 95](../../../cost/review/accountant-input.md#L95). Nội dung đầy đủ:

> Nếu có chiết khấu, đơn gốc và khoản riêng được ghi thế nào; số phải trả và trạng thái xử lý có nguồn nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-86"></a>

## DEC-86 — Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu?

Cần quyết định: Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu?

Mã nguồn: NUTR-Q01. Người quyết định: Dinh dưỡng viên, Giám đốc. Release: R4. [Buổi 2](meeting-agenda.md#buoi-2).

### NUTR-Q01

[Nguồn, dòng 13](../../../dinh-duong/review/questions.md#L13). Nội dung đầy đủ:

> Ấn bản, trang/mã thực phẩm của Bảng thành phần thực phẩm Việt Nam nào được phép dùng; ai duyệt mapping và sửa số liệu?

Phương án khuyến nghị đã có:

> đề xuất, chưa có workflow duyệt riêng

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-019; nguồn D-17/DL-07; quyền ghi đề xuất, chưa có workflow duyệt riêng

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-87"></a>

## DEC-87 — Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi?

Cần quyết định: Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi?

Mã nguồn: NUTR-Q03. Người quyết định: Dinh dưỡng viên. Release: R4. [Buổi 2](meeting-agenda.md#buoi-2).

### NUTR-Q03

[Nguồn, dòng 15](../../../dinh-duong/review/questions.md#L15). Nội dung đầy đủ:

> Suất mẫu là tổ hợp chọn cụ thể hay món mặc định? Có gồm cơm/gia vị/đồ uống; ghi ở recipe/item nào để không bỏ sót hoặc đếm đôi?

Phương án khuyến nghị đã có:

> đề xuất tổ hợp tường minh, không sao chép cách chọn món đắt nhất Cost

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-NUTR-CALC-002; đề xuất tổ hợp tường minh, không sao chép cách chọn món đắt nhất Cost

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-88"></a>

## DEC-88 — Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.

Cần quyết định: Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.?

Mã nguồn: NUTR-Q04. Người quyết định: Dinh dưỡng viên, QA. Release: R4. [Buổi 2](meeting-agenda.md#buoi-2).

### NUTR-Q04

[Nguồn, dòng 16](../../../dinh-duong/review/questions.md#L16). Nội dung đầy đủ:

> Chốt cách làm tròn và dung sai khớp 5 suất tính tay theo R4; đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.

Phương án khuyến nghị đã có:

> đề xuất HALF_UP 2 chữ số ở tổng cuối, không dùng dung sai Cost.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> NFR-NUTR-001; chưa có ngưỡng nghiệm thu được duyệt

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-89"></a>

## DEC-89 — Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp.

Cần quyết định: Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp.?

Mã nguồn: DATA-NUTR-Q01. Người quyết định: Dinh dưỡng viên. Release: R4. [Buổi 2](meeting-agenda.md#buoi-2).

### DATA-NUTR-Q01

[Nguồn, dòng 17](../../../dinh-duong/review/questions.md#L17). Nội dung đầy đủ:

> Cung cấp mapping nguyên liệu của 30 món, ấn bản/nguồn và 5 suất tính tay độc lập, người lập/ngày/phương pháp.

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> DL-03/05/07, nghiệm thu R4; chưa có dữ liệu thật trong gói

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-90"></a>

## DEC-90 — Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không?

Cần quyết định: Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không?

Mã nguồn: AIO-Q02. Người quyết định: Chủ sản phẩm, dinh dưỡng viên. Release: R5. [Buổi 2](meeting-agenda.md#buoi-2).

### AIO-Q02

[Nguồn, dòng 14](../../../agent-noi-bo/review/questions.md#L14). Nội dung đầy đủ:

> Xác nhận R5 chỉ trả VALID nếu cost không vượt kể cả CANH_BAO; có cho người dùng xem phương án chưa đạt để sửa thủ công không?

Phương án khuyến nghị đã có:

> đề xuất NO_SOLUTION không cho áp dụng

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-CHK-001; đề xuất NO_SOLUTION không cho áp dụng; không thay cổng MENU/Cost

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-91"></a>

## DEC-91 — 20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao?

Cần quyết định: 20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao?

Mã nguồn: AIO-Q03. Người quyết định: Dinh dưỡng viên, QA. Release: R5. [Buổi 2](meeting-agenda.md#buoi-2).

### AIO-Q03

[Nguồn, dòng 15](../../../agent-noi-bo/review/questions.md#L15). Nội dung đầy đủ:

> 20 yêu cầu nghiệm thu gồm nhóm nào, dữ liệu khả thi nào, mẫu đo trước MVP và cách tính giảm 50% thời gian ra sao?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> NFR-AIO-001/002; không tính từ chối/timeout là một thực đơn đạt

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-92"></a>

## DEC-92 — Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào?

Cần quyết định: Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào?

Mã nguồn: AIO-Q04. Người quyết định: Giám đốc, Tech lead. Release: R5. [Buổi 2](meeting-agenda.md#buoi-2).

### AIO-Q04

[Nguồn, dòng 16](../../../agent-noi-bo/review/questions.md#L16). Nội dung đầy đủ:

> Ai xem prompt/tool arguments, lưu bao lâu, mức che dữ liệu và quyền xuất log thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-LOG-001; mặc định thiết kế không có API xuất log

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-93"></a>

## DEC-93 — Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào?

Cần quyết định: Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào?

Mã nguồn: AIO-Q05. Người quyết định: Dinh dưỡng viên. Release: R5. [Buổi 2](meeting-agenda.md#buoi-2).

### AIO-Q05

[Nguồn, dòng 17](../../../agent-noi-bo/review/questions.md#L17). Nội dung đầy đủ:

> Kiêng kỵ diễn đạt tự do được ánh xạ nguyên liệu/món tới mức nào; xử lý nguyên liệu phụ và ghi chú dị ứng chưa đủ thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-GEN-001/EDIT-001; chưa rõ phải hỏi lại, không tư vấn điều trị

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-94"></a>

## DEC-94 — Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout?

Cần quyết định: Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout?

Mã nguồn: AIO-Q06. Người quyết định: Tech lead, BA. Release: R5. [Buổi 2](meeting-agenda.md#buoi-2).

### AIO-Q06

[Nguồn, dòng 18](../../../agent-noi-bo/review/questions.md#L18). Nội dung đầy đủ:

> Chốt giao diện adapter MENU kiểm nháp/ghi nháp và giao dịch apply, nơi lưu idempotency/quota, xử lý khóa và rollout?

Phương án khuyến nghị đã có:

> đề xuất, chưa có endpoint MENU được triển khai

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-APLY-001; hợp đồng port đề xuất, chưa có endpoint MENU được triển khai

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-95"></a>

## DEC-95 — Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa?

Cần quyết định: Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa?

Mã nguồn: ORD-Q02. Người quyết định: Người đặt tổng, BA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q02

[Nguồn, dòng 21](../../../chon-mon-order/review/questions.md#L21). Nội dung đầy đủ:

> Đổi QR/gỡ người ăn có thu hồi phiên ngay và giữ hay hủy lựa chọn chưa khóa?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-96"></a>

## DEC-96 — Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order?

Cần quyết định: Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order?

Mã nguồn: ORD-Q03. Người quyết định: Vận hành. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q03

[Nguồn, dòng 22](../../../chon-mon-order/review/questions.md#L22). Nội dung đầy đủ:

> Một điểm phục vụ có đổi bếp/ca/lịch giữa kỳ; dữ liệu nào chụp lúc order?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-97"></a>

## DEC-97 — Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào?

Cần quyết định: Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào?

Mã nguồn: ORD-Q04. Người quyết định: Người phụ trách khách, DDV. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q04

[Nguồn, dòng 23](../../../chon-mon-order/review/questions.md#L23). Nội dung đầy đủ:

> Ai duyệt định mức; đổi định mức/menu/giá khi đã có lựa chọn xử lý thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-98"></a>

## DEC-98 — Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào?

Cần quyết định: Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào?

Mã nguồn: ORD-Q05. Người quyết định: Người đặt tổng, BA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q05

[Nguồn, dòng 24](../../../chon-mon-order/review/questions.md#L24). Nội dung đầy đủ:

> Chọn tuần atomic toàn tuần hay nhận từng ngày; UX trả lỗi từng ngày thế nào?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-99"></a>

## DEC-99 — T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món?

Cần quyết định: T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món?

Mã nguồn: ORD-Q06. Người quyết định: Người đặt tổng, DDV. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q06

[Nguồn, dòng 25](../../../chon-mon-order/review/questions.md#L25). Nội dung đầy đủ:

> T<S+C xử lý bằng tăng tổng hay điều chỉnh lựa chọn ai; C có phải nhập thêm hay tổng thay thế theo món?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-100"></a>

## DEC-100 — Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao?

Cần quyết định: Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao?

Mã nguồn: ORD-Q07. Người quyết định: Vận hành, Giám đốc. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q07

[Nguồn, dòng 26](../../../chon-mon-order/review/questions.md#L26). Nội dung đầy đủ:

> Đến hạn mà chưa có tổng/default hoặc job lỗi: ai xử lý, có gia hạn/khóa lại, báo bếp ra sao?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-101"></a>

## DEC-101 — Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi?

Cần quyết định: Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi?

Mã nguồn: ORD-Q09. Người quyết định: Người đặt tổng. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q09

[Nguồn, dòng 28](../../../chon-mon-order/review/questions.md#L28). Nội dung đầy đủ:

> Tắt chọn món có hiệu lực ngay hay từ ngày sau; xử lý các lựa chọn đã ghi?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-102"></a>

## DEC-102 — R6 luôn 1 MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao?

Cần quyết định: R6 luôn 1 MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao?

Mã nguồn: ORD-Q10. Người quyết định: DDV, bếp trưởng. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q10

[Nguồn, dòng 29](../../../chon-mon-order/review/questions.md#L29). Nội dung đầy đủ:

> R6 luôn1MAIN/suất hay hỗ trợ nhiềuMAIN; kế hoạch món phụ/rau/canh phân rã từ suất ra sao?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-103"></a>

## DEC-103 — MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn?

Cần quyết định: MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn?

Mã nguồn: ORD-Q12. Người quyết định: DDV, vận hành. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q12

[Nguồn, dòng 38](../../../chon-mon-order/review/questions.md#L38). Nội dung đầy đủ:

> MENU thu hồi/đổi bản khi có lựa chọn hoặc order khóa thì hủy/chọn lại/thay món thế nào; thứ tự override deadline khách/điểm/ca và biên đúng hạn?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-104"></a>

## DEC-104 — Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày?

Cần quyết định: Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày?

Mã nguồn: ORD-Q13. Người quyết định: Người đặt tổng, BA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### ORD-Q13

[Nguồn, dòng 39](../../../chon-mon-order/review/questions.md#L39). Nội dung đầy đủ:

> Người ăn có được hủy lựa chọn/đổi điểm cùng ca; T=0 có nghĩa hủy bữa không; giới hạn tối đa suất/ngày?

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-105"></a>

## DEC-105 — C có danh tính/gộp, C→S, vượtT, hủy/zero; RV02/03, ORD-Q06/13, EVID002

Cần quyết định: C có danh tính/gộp, C→S, vượtT, hủy/zero; RV02/03, ORD-Q06/13, EVID002?

Mã nguồn: E6-CG-03. Người quyết định: Chủ sản phẩm, vận hành, BA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-03

[Nguồn, dòng 9](../../../chon-mon-order/review/contract-gap-register.md#L9). Nội dung đầy đủ:

> C có danh tính/gộp, C→S, vượtT, hủy/zero; RV02/03, ORD-Q06/13, EVID002

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-106"></a>

## DEC-106 — Summary token, receipt, outbox transaction/retention; RV04, E1-Q02

Cần quyết định: Summary token, receipt, outbox transaction/retention; RV04, E1-Q02?

Mã nguồn: E6-CG-04. Người quyết định: Tech lead, BA, QA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-04

[Nguồn, dòng 10](../../../chon-mon-order/review/contract-gap-register.md#L10). Nội dung đầy đủ:

> Summary token, receipt, outbox transaction/retention; RV04, E1-Q02

Phương án khuyến nghị đã có:

> Giữ summary token theo scope; dữ liệu nghiệp vụ, revision, audit thành công, receipt và outbox cùng một transaction. UC010/011 dùng một PORT-LOCK và một lần khóa; eventKey khác HTTP key. Receipt đã commit được kiểm quyền hiện tại rồi replay, không ghi lại. Worker xử lý event sau commit, retry không tạo revision trùng.

Phương án khác đã có:

> Lưu receipt tách transaction dễ triển khai từng phần nhưng có khoảng mất dấu kết quả; không khuyến nghị. Khóa dòng hay CAS là lựa chọn kỹ thuật cần benchmark/review, chưa chọn bằng tài liệu BA.

Tác động / phần chặn được nguồn mô tả:

> Tech lead xác nhận storage/unique/lock/CAS, giữ và dọn receipt/outbox, recovery; QA thực thi fault trước/sau commit theo ca hiện có. Không tự đặt retention hoặc số retry; duyệt hướng không chứng minh atomic runtime.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-107"></a>

## DEC-107 — Delta line identity, unit/role/portion và món mới; RV07, ORD-Q04/08/10/12, O-02

Cần quyết định: Delta line identity, unit/role/portion và món mới; RV07, ORD-Q04/08/10/12, O-02?

Mã nguồn: E6-CG-07. Người quyết định: BA, dinh dưỡng viên, Tech lead. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-07

[Nguồn, dòng 13](../../../chon-mon-order/review/contract-gap-register.md#L13). Nội dung đầy đủ:

> Delta line identity, unit/role/portion và món mới; RV07, ORD-Q04/08/10/12, O-02

Phương án khuyến nghị đã có:

> Ưu tiên tham chiếu lineId bất biến của revision gốc khi sửa dòng đã tồn tại; so sánh snapshot theo dish+recipe+portion+role+unit. Thay recipe A bằng B biểu diễn giảm A và tăng B, dù tổng suất không đổi. Không cộng suất với gram.

Phương án khác đã có:

> Gửi khóa tổ hợp đầy đủ thay lineId: rõ nguồn nhưng payload dài và client phải giữ nhiều khóa. Chỉ dishId không đủ nếu có nhiều dòng cùng món.

Tác động / phần chặn được nguồn mô tả:

> Review lineId tồn tại trong phạm vi revision, tạo dòng mới, kiểu lượng và quy đổi; đồng bộ Change/OrderRevision/PlanRevision/API/data/AC sau khi chốt. Không quyết nhiều MAIN hoặc mở O-02.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-108"></a>

## DEC-108 — Customer master/account/service lifecycle; ORD-Q03/11

Cần quyết định: Customer master/account/service lifecycle; ORD-Q03/11?

Mã nguồn: E6-CG-08. Người quyết định: Nền tảng/Auth, BA, phụ trách khách. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-08

[Nguồn, dòng 14](../../../chon-mon-order/review/contract-gap-register.md#L14). Nội dung đầy đủ:

> Customer master/account/service lifecycle; ORD-Q03/11

Phương án khuyến nghị đã có:

> Nền tảng quản lý mã khách tối thiểu và vòng đời account; E6 tham chiếu khách đã tồn tại, tạo/cập nhật điểm phục vụ và grant tách biệt. Chỉ cho thao tác chọn/chốt khi có đủ nguồn và quyền theo từng thao tác. Tạo account thành công nhưng grant thất bại: giữ account chưa có quyền E6, xử lý lại bước grant sau khi kiểm quyền.

Phương án khác đã có:

> E6 tự giữ master khách tối thiểu: giảm phụ thuộc ban đầu nhưng thêm nghĩa vụ đồng bộ/chống trùng; không khuyến nghị trong phạm vi này.

Tác động / phần chặn được nguồn mô tả:

> Khách A đã có mã nhưng chưa có điểm: tạo điểm thuộc A; tạo điểm không tự tạo khách/account/grant. Tránh nhiều bản khách và tránh cấp quyền rộng để bù lỗi. Đánh đổi: onboarding phụ thuộc owner Nền tảng.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-109"></a>

## DEC-109 — NUTR provenance/kind/stale, refresh/cache/fallback; NUTR-Q03/04, ORD-Q04/12

Cần quyết định: NUTR provenance/kind/stale, refresh/cache/fallback; NUTR-Q03/04, ORD-Q04/12?

Mã nguồn: E6-CG-10. Người quyết định: Owner MENU/NUTR, BA, Tech lead. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-10

[Nguồn, dòng 16](../../../chon-mon-order/review/contract-gap-register.md#L16). Nội dung đầy đủ:

> NUTR provenance/kind/stale, refresh/cache/fallback; NUTR-Q03/04, ORD-Q04/12

Phương án khuyến nghị đã có:

> Calculation được principal service có quyền chuẩn bị trước bằng job/event khi nguồn thay đổi; GET chỉ đọc và đối chiếu provenance. Ưu tiên opaque source reference an toàn cho người ăn, provenance đầy đủ lưu nội bộ. Chưa có kết quả đúng nguồn thì không dùng kết quả cũ như hiện hành; thiếu dữ liệu đã xác định trả null/missing an toàn, lỗi phụ thuộc/thiếu cache cần outcome riêng, không giả bằng 0.

Phương án khác đã có:

> Tính đồng bộ lúc ghi/công bố nguồn: dễ gắn kết quả với phiên bản hơn nhưng tăng thời gian thao tác và phụ thuộc NUTR; không tính ghi ẩn dưới GET.

Tác động / phần chặn được nguồn mô tả:

> Owner MENU/NUTR review event/producer, DISH/MEAL, source reference, freshness, cache miss và projection. Chưa tự chọn thời gian cache, fallback hoặc mã lỗi mới; chưa mở profile/consent/thu sức khỏe.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-110"></a>

## DEC-110 — Required/optional/null, limits, enum/query, create-version chưa rõ

Cần quyết định: Required/optional/null, limits, enum/query, create-version chưa rõ?

Mã nguồn: E6-CG-11. Người quyết định: API owner, BA, QA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-11

[Nguồn, dòng 17](../../../chon-mon-order/review/contract-gap-register.md#L17). Nội dung đầy đủ:

> Required/optional/null, limits, enum/query, create-version chưa rõ

Phương án khuyến nghị đã có:

> Đề xuất required thiếu thì báo lỗi; optional cho phép vắng nhưng không tự cho phép null; unknown dùng null chỉ ở field được định nghĩa nullable. Không tự lấy hôm nay cho effectiveDate, không tự chọn scope hoặc chuyển unknown thành 0. Mỗi nhánh response có bảng field hiện diện riêng, ví dụ Registration pending không phát token hoặc bịa userId.

Phương án khác đã có:

> Dùng nhiều default ngầm: payload ngắn hơn nhưng có thể đổi nghĩa nghiệp vụ khi client bỏ field. Cho phép null mọi optional: dễ nhập hơn nhưng làm mất phân biệt chưa cung cấp và chủ động xóa.

Tác động / phần chặn được nguồn mô tả:

> API owner/QA quyết từng field còn gap, enum và giới hạn có căn cứ; chọn cụ thể omit/null cho từng nhánh và negative oracle. Đề xuất nguyên tắc không đóng 34DTO hoặc chốt toàn bộ limits/defaults/create-version.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-111"></a>

## DEC-111 — Tuần/mode/reminder policy; ORD-Q05/09, Q-14/E1-Q04

Cần quyết định: Tuần/mode/reminder policy; ORD-Q05/09, Q-14/E1-Q04?

Mã nguồn: E6-CG-12. Người quyết định: Chủ sản phẩm/vận hành, BA, Tech lead. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-12

[Nguồn, dòng 18](../../../chon-mon-order/review/contract-gap-register.md#L18). Nội dung đầy đủ:

> Tuần/mode/reminder policy; ORD-Q05/09, Q-14/E1-Q04

Phương án khuyến nghị đã có:

> Đề xuất chọn tuần nhận kết quả theo từng ngày: ngày hợp lệ được ghi, ngày lỗi trả lỗi riêng; không ghi một phần trong cùng ngày. Đề xuất thay đổi bật/tắt chọn món chỉ có hiệu lực từ ngày phục vụ tương lai được chọn rõ, giữ lịch sử và không tự xóa lựa chọn đã ghi. Nhắc trước mắt chỉ qua thông báo nội bộ cho người đủ điều kiện trong scope.

Phương án khác đã có:

> Tuần atomic toàn bộ; mode áp dụng ngay kèm xử lý lựa chọn cũ; gửi nhắc qua kênh bên ngoài. Mỗi phương án cần thêm quy tắc và evidence tương ứng.

Tác động / phần chặn được nguồn mô tả:

> 5 ngày, 1 ngày lỗi: hiển thị rõ 4 ngày đã ghi và 1 ngày chưa ghi. Giảm phải làm lại cả tuần nhưng UI phải báo kết quả từng ngày. Đề xuất tuần, mode, nhắc là ba lựa chọn có thể duyệt riêng.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-112"></a>

## DEC-112 — Wireframe chỉ mô phỏng một nguồn/version đồng bộ

Cần quyết định: Wireframe chỉ mô phỏng một nguồn/version đồng bộ?

Mã nguồn: E6-CG-13. Người quyết định: BA/UI, QA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-13

[Nguồn, dòng 19](../../../chon-mon-order/review/contract-gap-register.md#L19). Nội dung đầy đủ:

> Wireframe chỉ mô phỏng một nguồn/version đồng bộ

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-113"></a>

## DEC-113 — Gate sức khỏe và dữ liệu/QA môi trường chưa có

Cần quyết định: Gate sức khỏe và dữ liệu/QA môi trường chưa có?

Mã nguồn: E6-CG-14. Người quyết định: Chủ sản phẩm, phụ trách dữ liệu, QA. Release: R6. [Buổi 4](meeting-agenda.md#buoi-4).

### E6-CG-14

[Nguồn, dòng 20](../../../chon-mon-order/review/contract-gap-register.md#L20). Nội dung đầy đủ:

> Gate sức khỏe và dữ liệu/QA môi trường chưa có

Phương án khuyến nghị đã có:

Chưa có trong dòng nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

chưa rõ — nguồn chưa mô tả tác động theo từng phương án.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-114"></a>

## DEC-114 — Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?

Cần quyết định: Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?

Mã nguồn: Q-13. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### Q-13

[Nguồn, dòng 18](../../../giao-nhan-doanh-thu/review/questions.md#L18). Nội dung đầy đủ:

> Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?

Phương án khuyến nghị đã có:

> Giữ chờ và xử lý thủ công có bằng chứng; hoặc suy định theo thỏa thuận khách có thời hạn/thông báo/tranh chấp. Chưa chọn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> ACK im lặng; số tính tiền và thống nhất/khóa kỳ liên quan

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-115"></a>

## DEC-115 — Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?

Cần quyết định: Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?

Mã nguồn: E7-Q01. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q01

[Nguồn, dòng 19](../../../giao-nhan-doanh-thu/review/questions.md#L19). Nội dung đầy đủ:

> Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?

Phương án khuyến nghị đã có:

> Phiên có quyền hoặc token giới hạn scope cần review Auth; không lấy QR E6 làm quyền ký nhận.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Link; CG01/08 chờ, không đặc tả thêm producer E6

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-116"></a>

## DEC-116 — Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?

Cần quyết định: Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?

Mã nguồn: E7-Q02. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q02

[Nguồn, dòng 20](../../../giao-nhan-doanh-thu/review/questions.md#L20). Nội dung đầy đủ:

> Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?

Phương án khuyến nghị đã có:

> Giữ phiếu gốc + thỏa thuận/phiếu bù; cần chống đếm trùng và quyền.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> RES, tổng giao/nhận sau bù, tác động kỳ khóa

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-117"></a>

## DEC-117 — Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?

Cần quyết định: Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?

Mã nguồn: E7-Q03. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q03

[Nguồn, dòng 21](../../../giao-nhan-doanh-thu/review/questions.md#L21). Nội dung đầy đủ:

> Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?

Phương án khuyến nghị đã có:

> Căn cứ từng đơn có evidence; không mặc định số nhận/số chốt.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> REV; giảm trừ khác CK riêng

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-118"></a>

## DEC-118 — Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?

Cần quyết định: Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?

Mã nguồn: E7-Q04. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q04

[Nguồn, dòng 22](../../../giao-nhan-doanh-thu/review/questions.md#L22). Nội dung đầy đủ:

> Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?

Phương án khuyến nghị đã có:

> Hiện phải trả, VAT, doanh thu trước VAT riêng; không mượn dung sai Cost.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Tổng chính thức và R7

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-119"></a>

## DEC-119 — Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?

Cần quyết định: Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?

Mã nguồn: E7-Q05. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q05

[Nguồn, dòng 23](../../../giao-nhan-doanh-thu/review/questions.md#L23). Nội dung đầy đủ:

> Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?

Phương án khuyến nghị đã có:

> Snapshot từng vòng; chỉ Giám đốc duyệt mới mở. Điều kiện khác chưa chọn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> AGRE/LOCK và sửa sau REOPENED

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-120"></a>

## DEC-120 — Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?

Cần quyết định: Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?

Mã nguồn: E7-Q06. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q06

[Nguồn, dòng 24](../../../giao-nhan-doanh-thu/review/questions.md#L24). Nội dung đầy đủ:

> Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?

Phương án khuyến nghị đã có:

> Chứng từ/phân bổ riêng; không suy CK đã bù trừ.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Thanh toán nâng cao/chống trùng nghiệp vụ

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-121"></a>

## DEC-121 — Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?

Cần quyết định: Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?

Mã nguồn: E7-Q07. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q07

[Nguồn, dòng 25](../../../giao-nhan-doanh-thu/review/questions.md#L25). Nội dung đầy đủ:

> Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?

Phương án khuyến nghị đã có:

> Nhận mẫu có version và thử nhập môi trường được cấp; chưa giả CSV/XLSX, cột, mã thuế/tài khoản.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> File bytes/mapping cột/thử nhập MISA

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-122"></a>

## DEC-122 — Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?

Cần quyết định: Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?

Mã nguồn: E7-Q08. Người quyết định: chưa rõ. Release: R7. [Buổi 5](meeting-agenda.md#buoi-5).

### E7-Q08

[Nguồn, dòng 26](../../../giao-nhan-doanh-thu/review/questions.md#L26). Nội dung đầy đủ:

> Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?

Phương án khuyến nghị đã có:

> Kế thừa an toàn nền; review kỹ thuật, không đặt TTL/retry/limits tùy ý.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Wire contract/persistence/fault/load

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-123"></a>

## DEC-123 — DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ?

Cần quyết định: DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ?

Mã nguồn: E8-Q01. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q01

[Nguồn, dòng 18](../../../website-cong-khai/review/questions.md#L18). Nội dung đầy đủ:

> DL-08: danh sách bài viết, URL, media và trạng thái WordPress gốc ở đâu; ai xác nhận inventory đầy đủ?

Phương án khuyến nghị đã có:

> Xuất inventory có mã bài/URL/status/hash; hoặc crawl đối chiếu bản export, không thay export bằng URL đoán

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Mapping thật, mẫu số 100% URL, R8

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-124"></a>

## DEC-124 — Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback?

Cần quyết định: Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback?

Mã nguồn: E8-Q02. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q02

[Nguồn, dòng 19](../../../website-cong-khai/review/questions.md#L19). Nội dung đầy đủ:

> Giữ URL hay 301 theo tiêu chí nào; xử lý trùng/bài xóa, chữ hoa/dấu slash/query; ai duyệt mapping và rollback?

Phương án khuyến nghị đã có:

> Giữ đường dẫn có thể bảo toàn; 301 tới nội dung tương đương. Bài xóa cần quyết định riêng; 404/410 không tự tính đạt R8

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kích hoạt redirect, bài xóa/trùng, cutover

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-125"></a>

## DEC-125 — Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào?

Cần quyết định: Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào?

Mã nguồn: E8-Q06. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q06

[Nguồn, dòng 23](../../../website-cong-khai/review/questions.md#L23). Nội dung đầy đủ:

> Lead vào CRM khi E10 chưa mở: lưu tạm ở đâu, trường bắt buộc, consent/version, thời gian lưu/xóa và receipt bàn giao thế nào?

Phương án khuyến nghị đã có:

> Kho lead E8 riêng rồi chuyển khi E10 có contract; hoặc đầu nhận hiện hữu được duyệt. Không tự dùng customers/eaters làm lead

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Ghi lead thật, retention/xóa, hợp đồng E10

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-126"></a>

## DEC-126 — Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao?

Cần quyết định: Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao?

Mã nguồn: E8-Q07. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q07

[Nguồn, dòng 24](../../../website-cong-khai/review/questions.md#L24). Nội dung đầy đủ:

> Chống spam bằng cách nào; ai nhận thông báo qua kênh nào, xử lý lỗi/gửi lặp/thất lạc ra sao?

Phương án khuyến nghị đã có:

> Rate limit nền + kiểm trường; bổ sung giải pháp sau review. Thông báo riêng trạng thái lưu lead, không coi gửi thông báo là lưu thành công

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Provider chống spam, recipient, notification/retry

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-127"></a>

## DEC-127 — Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào?

Cần quyết định: Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào?

Mã nguồn: E8-Q08. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q08

[Nguồn, dòng 25](../../../website-cong-khai/review/questions.md#L25). Nội dung đầy đủ:

> Vai trò nào được soạn/duyệt/xuất bản/thu hồi; có bước duyệt không; chọn CMS nào?

Phương án khuyến nghị đã có:

> Tách quyền soạn và công bố, có thể thêm duyệt độc lập; hoặc workflow ít bước được xác nhận. Không tự gán PER-05 toàn quyền

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Quyền runtime, bước duyệt, CMS/publication

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-128"></a>

## DEC-128 — Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào?

Cần quyết định: Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào?

Mã nguồn: E8-Q09. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q09

[Nguồn, dòng 26](../../../website-cong-khai/review/questions.md#L26). Nội dung đầy đủ:

> Ảnh/banner: quyền sử dụng, loại/dung lượng, crop/alt, vị trí/lịch hiển thị, duyệt, gỡ ảnh đang dùng thế nào?

Phương án khuyến nghị đã có:

> Tái dùng files nền với metadata public riêng; chỉ loại ảnh trong tập nền, không tự mở SVG; lịch/cỡ chờ xác nhận

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Media pipeline, layout/lịch và quyền public asset

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-129"></a>

## DEC-129 — BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo?

Cần quyết định: BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo?

Mã nguồn: E8-Q10. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q10

[Nguồn, dòng 27](../../../website-cong-khai/review/questions.md#L27). Nội dung đầy đủ:

> BO-09 dùng công cụ nào; baseline tháng nào trước chuyển đổi, múi giờ/lọc bot/organic; cửa sổ sau 60 ngày và quyền truy cập số đo?

Phương án khuyến nghị đã có:

> So phiên tự nhiên theo cùng công cụ/định nghĩa và kỳ so sánh tương đương; lưu bằng chứng baseline trước cutover

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Đo BO-09, kết luận G-Next; baseline=0/thiếu chưa tính tỷ lệ

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-130"></a>

## DEC-130 — Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04?

Cần quyết định: Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04?

Mã nguồn: E8-Q11. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q11

[Nguồn, dòng 28](../../../website-cong-khai/review/questions.md#L28). Nội dung đầy đủ:

> Ai có quyền quản trị tên miền/DNS; hạ tầng, CMS/hosting, thời điểm chuyển đổi, rollback và người quyết định O-04?

Phương án khuyến nghị đã có:

> Xác nhận quyền, diễn tập chuyển và rollback rồi mới chọn cửa sổ; không tự chọn nhà cung cấp hoặc ngày

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> R8 start/cutover; đưa 054/055/059 lên Now

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-131"></a>

## DEC-131 — Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì?

Cần quyết định: Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì?

Mã nguồn: E8-Q12. Người quyết định: chưa rõ. Release: R8. [Buổi 7](meeting-agenda.md#buoi-7).

### E8-Q12

[Nguồn, dòng 29](../../../website-cong-khai/review/questions.md#L29). Nội dung đầy đủ:

> Chuẩn envelope/phân trang/cache invalidation, anonymous idempotency, receipt, profile tải và thời hạn draft E8 là gì?

Phương án khuyến nghị đã có:

> Kế thừa nền khi tương thích; E4 dùng cursor/envelope khác nên adapter cần review, không tự freeze TTL/retry

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Wire contract, cache/CDN, tải và fault tolerance

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-132"></a>

## DEC-132 — Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền?

Cần quyết định: Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền?

Mã nguồn: E9-Q02. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q02

[Nguồn, dòng 19](../../../agent-dinh-duong-vien/review/questions.md#L19). Nội dung đầy đủ:

> Ai dùng agent: khách vãng lai, khách có tài khoản hay cả hai; cách xác minh và gắn nhóm/quyền?

Phương án khuyến nghị đã có:

> Chỉ tài khoản hoặc thêm guest có xác minh; không lấy IP làm danh tính mặc định

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Mở phiên thật, quota theo người, audit guest

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-133"></a>

## DEC-133 — Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào?

Cần quyết định: Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào?

Mã nguồn: E9-Q03. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q03

[Nguồn, dòng 20](../../../agent-dinh-duong-vien/review/questions.md#L20). Nội dung đầy đủ:

> Khẩu vị/kiêng kỵ được nhận theo danh mục nào, giới hạn ra sao; xử lý nội dung tự do có thông tin sức khỏe thế nào?

Phương án khuyến nghị đã có:

> Danh mục sở thích/nguyên liệu đã duyệt; nội dung ngoài danh mục dừng làm rõ; không suy luận bệnh

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Nhận input thật, mapping kiêng kỵ; phạm vi sức khỏe vẫn đóng

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-134"></a>

## DEC-134 — Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không?

Cần quyết định: Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không?

Mã nguồn: E9-Q05. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q05

[Nguồn, dòng 22](../../../agent-dinh-duong-vien/review/questions.md#L22). Nội dung đầy đủ:

> Khi không đạt ngưỡng cost, AIN trả kết quả gì mà không lộ lý do cost; có cho xem phương án chưa đạt không?

Phương án khuyến nghị đã có:

> Thông báo chung không phân biệt nguyên nhân kinh tế hoặc chuyển người thật; chưa chọn; không truyền cost result cho model

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Nhánh vượt ngưỡng/CANH_BAO và kết quả công khai

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-135"></a>

## DEC-135 — FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào?

Cần quyết định: FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào?

Mã nguồn: E9-Q06. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q06

[Nguồn, dòng 23](../../../agent-dinh-duong-vien/review/questions.md#L23). Nội dung đầy đủ:

> FEAT-062 gửi nháp ở đâu khi CRM chưa mở; ai được nhận/duyệt, thời hạn xử lý, trạng thái khách thấy và receipt nào?

Phương án khuyến nghị đã có:

> Kho tiếp nhận riêng hoặc đầu nhận hiện hữu được duyệt; chỉ ACK khi ghi bền vững; tách receipt và duyệt

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Ghi nháp thật, chuyển giao, hiển thị kết quả xử lý; không mở E10

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-136"></a>

## DEC-136 — FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần?

Cần quyết định: FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần?

Mã nguồn: E9-Q07. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q07

[Nguồn, dòng 24](../../../agent-dinh-duong-vien/review/questions.md#L24). Nội dung đầy đủ:

> FEAT-064: nhóm người dùng, số lượt, định nghĩa một lượt/cửa sổ/reset, trần chi phí ngày, đơn vị đo/tỷ giá/múi giờ, hành vi chạm trần?

Phương án khuyến nghị đã có:

> Đếm lượt được nhận hoặc lượt hoàn tất theo policy được duyệt; reserve theo upper bound + đối soát; không có số mặc định

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Nhận lượt thật, quyết toán/hoàn lượt, trần/reset và retry

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-137"></a>

## DEC-137 — Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy?

Cần quyết định: Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy?

Mã nguồn: E9-Q08. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q08

[Nguồn, dòng 25](../../../agent-dinh-duong-vien/review/questions.md#L25). Nội dung đầy đủ:

> Ai được xem/sửa/duyệt hạn mức; thay đổi có cần duyệt và có hiệu lực khi nào, xử lý lượt đang chạy?

Phương án khuyến nghị đã có:

> PER-08 là persona quản trị nhưng quyền cụ thể phải cấp; nếu cần duyệt áp tách người tạo/sửa cuối

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kích hoạt cấu hình; không tự trao quyền vì là Giám đốc

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-138"></a>

## DEC-138 — Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì?

Cần quyết định: Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì?

Mã nguồn: E9-Q09. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q09

[Nguồn, dòng 26](../../../agent-dinh-duong-vien/review/questions.md#L26). Nội dung đầy đủ:

> Ai soạn và duyệt 30 yêu cầu thực đơn, 20 dò cost, 20 bệnh lý; oracle, lời nhắc bệnh lý bắt buộc, tiêu chí không chẩn đoán là gì?

Phương án khuyến nghị đã có:

> Duyệt manifest, dữ liệu khả thi và rubric độc lập trước chạy; từ chối/timeout không thay thực đơn đạt

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Nghiệm thu R9; nội dung lời nhắc chưa xác nhận

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-139"></a>

## DEC-139 — Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider?

Cần quyết định: Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider?

Mã nguồn: E9-Q10. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q10

[Nguồn, dòng 27](../../../agent-dinh-duong-vien/review/questions.md#L27). Nội dung đầy đủ:

> Lưu hội thoại bao lâu, ai xem, cơ chế đồng ý xử lý dữ liệu, xóa theo yêu cầu và xử lý bản sao/log/provider?

Phương án khuyến nghị đã có:

> Tối thiểu hóa; tách audit metadata khỏi nội dung; chốt quy trình xóa theo NFR-PRIV-001, không dùng retention log thay retention chat

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Lưu hội thoại thật, replay, xuất log, truyền dữ liệu provider

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-140"></a>

## DEC-140 — Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9?

Cần quyết định: Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9?

Mã nguồn: E9-Q13. Người quyết định: chưa rõ. Release: R9. [Buổi 8](meeting-agenda.md#buoi-8).

### E9-Q13

[Nguồn, dòng 30](../../../agent-dinh-duong-vien/review/questions.md#L30). Nội dung đầy đủ:

> Wire contract: idempotency, TTL, retry/deadline/concurrency, receipt đối soát, giao dịch quota/ledger và profile tải R9?

Phương án khuyến nghị đã có:

> Key bền vững gắn chủ thể/route/body; giữ reservation khi usage chưa rõ; profile theo nền chưa chọn số quota

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Freeze API/delta, fault tolerance và thử tải

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-141"></a>

## DEC-141 — Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?

Cần quyết định: Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?

Mã nguồn: E10-Q01. Người quyết định: Chủ nghiệp vụ chăm sóc khách và người phụ trách dữ liệu. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q01

[Nguồn, dòng 25](../../../crm-ban-hang/review/questions.md#L25). Nội dung đầy đủ:

> Những trường liên hệ CRM nào cần lưu, ai được xem/sửa, lưu bao lâu và xử lý xóa thế nào?

Phương án khuyến nghị đã có:

> Chỉ lưu trường phục vụ chăm sóc có nguồn; tách lịch sử nghiệp vụ và thông tin liên hệ.

Phương án khác đã có:

> Chỉ tham chiếu kho liên hệ đã được phê duyệt.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-VIEW-001 / UC-CRM-001; FR-CUS-CONT-001 / UC-CRM-002

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-142"></a>

## DEC-142 — Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?

Cần quyết định: Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?

Mã nguồn: E10-Q02. Người quyết định: Chủ dữ liệu khách và Giám đốc. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q02

[Nguồn, dòng 26](../../../crm-ban-hang/review/questions.md#L26). Nội dung đầy đủ:

> Tiêu chí phát hiện khách trùng, chuẩn hóa, mức tin cậy và bằng chứng nào được chấp nhận?

Phương án khuyến nghị đã có:

> Danh sách nghi trùng giải thích được, người thật rà từng cặp; tiêu chí cụ thể cần người quyết định cung cấp.

Phương án khác đã có:

> Chỉ tiếp nhận cặp nghi trùng do người dùng chỉ ra; chưa chạy phát hiện tự động.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-DUP-001 / UC-CRM-004

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-143"></a>

## DEC-143 — Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?

Cần quyết định: Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?

Mã nguồn: E10-Q04. Người quyết định: Chủ dữ liệu khách, kế toán và trưởng kỹ thuật. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q04

[Nguồn, dòng 28](../../../crm-ban-hang/review/questions.md#L28). Nội dung đầy đủ:

> Hoàn tác gộp xử lý liên kết mới, xung đột sửa hồ sơ và giao dịch phát sinh sau gộp thế nào?

Phương án khuyến nghị đã có:

> Ghi bù có diff, giữ snapshot tài chính; có xung đột thì chờ phương án được duyệt.

Phương án khác đã có:

> Chỉ cho hoàn tác tự phục vụ khi chưa có liên kết mới; trường hợp khác xử lý theo hồ sơ riêng.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-MRG-001 / UC-CRM-005; FR-CUS-UNDO-001 / UC-CRM-006

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-144"></a>

## DEC-144 — Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?

Cần quyết định: Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?

Mã nguồn: E10-Q05. Người quyết định: Chăm sóc khách và vận hành. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q05

[Nguồn, dòng 29](../../../crm-ban-hang/review/questions.md#L29). Nội dung đầy đủ:

> Bằng chứng và quyền chuyển từng trạng thái vòng đời, cách tổng hợp khách có nhiều điểm là gì?

Phương án khuyến nghị đã có:

> Giữ sự kiện có bằng chứng, tín hiệu riêng với trạng thái; người thật xác nhận chuyển quan trọng.

Phương án khác đã có:

> Tự chuyển một số trạng thái sau khi bộ quy tắc và nguồn được duyệt.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-LIFE-001 / UC-CRM-007

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-145"></a>

## DEC-145 — Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?

Cần quyết định: Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?

Mã nguồn: E10-Q06. Người quyết định: Chăm sóc khách và vận hành. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q06

[Nguồn, dòng 30](../../../crm-ban-hang/review/questions.md#L30). Nội dung đầy đủ:

> Cửa sổ quan sát, ngưỡng nguy cơ rời, lịch nghỉ/ngoại lệ và cách xử lý dữ liệu đến muộn được quyết định thế nào?

Phương án khuyến nghị đã có:

> Đếm kỳ phục vụ dự kiến đủ nguồn và giải thích từng tín hiệu; thiếu lịch thì chưa đánh giá.

Phương án khác đã có:

> Theo dõi thủ công danh sách cần rà trước khi bật đánh giá tự động.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-LIFE-001 / UC-CRM-007; FR-CUS-RISK-001 / UC-CRM-008

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-146"></a>

## DEC-146 — Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?

Cần quyết định: Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?

Mã nguồn: E10-Q07. Người quyết định: Chủ nghiệp vụ bán hàng và Giám đốc. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q07

[Nguồn, dòng 31](../../../crm-ban-hang/review/questions.md#L31). Nội dung đầy đủ:

> Giai đoạn phễu, chủ cơ hội, tiêu chí thắng/thua và mẫu số đo chuyển đổi theo kỳ/cohort là gì?

Phương án khuyến nghị đã có:

> Lịch sử chuyển giai đoạn có bằng chứng; đếm một cơ hội duy nhất trong cùng tập đo.

Phương án khác đã có:

> Chỉ báo cáo số cơ hội từng giai đoạn, chưa công bố tỷ lệ chuyển đổi.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-OPP-001 / UC-CRM-009

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-147"></a>

## DEC-147 — Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?

Cần quyết định: Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?

Mã nguồn: E10-Q08. Người quyết định: Giám đốc và chủ nghiệp vụ bán hàng. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q08

[Nguồn, dòng 32](../../../crm-ban-hang/review/questions.md#L32). Nội dung đầy đủ:

> Ai duyệt báo giá, hiệu lực/thu hồi và bằng chứng chấp thuận đúng phiên bản được ghi thế nào?

Phương án khuyến nghị đã có:

> Bản phát hành bất biến có revision/hash, bằng chứng chấp thuận gắn đúng bản.

Phương án khác đã có:

> Ghi nhận bằng chứng thỏa thuận thủ công và người xác nhận thay luồng duyệt điện tử.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-OPP-001 / UC-CRM-009; FR-SALE-QUOT-001 / UC-CRM-010; FR-SALE-SAFE-001 / UC-CRM-012; FR-SALE-CONT-001 / UC-CRM-013

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-148"></a>

## DEC-148 — Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?

Cần quyết định: Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?

Mã nguồn: E10-Q09. Người quyết định: Dinh dưỡng viên và người duyệt báo giá. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q09

[Nguồn, dòng 33](../../../crm-ban-hang/review/questions.md#L33). Nội dung đầy đủ:

> Điều kiện thực đơn được đính kèm báo giá, quyền chia sẻ và xử lý nguồn thay đổi/thu hồi là gì?

Phương án khuyến nghị đã có:

> Bản chụp projection được phép, có revision/hash; nguồn không đủ thì chặn phát hành.

Phương án khác đã có:

> Chỉ đính kèm tài liệu thủ công đã được người có quyền duyệt và kiểm nội dung.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-MENU-001 / UC-CRM-011; FR-SALE-SAFE-001 / UC-CRM-012

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-149"></a>

## DEC-149 — Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?

Cần quyết định: Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?

Mã nguồn: E10-Q10. Người quyết định: Giám đốc và kế toán phụ trách hợp đồng. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q10

[Nguồn, dòng 34](../../../crm-ban-hang/review/questions.md#L34). Nội dung đầy đủ:

> Bằng chứng ký, người duyệt/kích hoạt, nhập hợp đồng hiện hữu và chấm dứt hợp đồng cần những bước nào?

Phương án khuyến nghị đã có:

> Lưu nguồn văn bản, người xác nhận và thời điểm; chỉ kích hoạt sau đủ bằng chứng.

Phương án khác đã có:

> Quản lý tham chiếu kho hợp đồng đã duyệt, không dựng quy trình ký điện tử mới.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-CONT-001 / UC-CRM-013; FR-SALE-ACTV-001 / UC-CRM-014; FR-SALE-AMND-001 / UC-CRM-015

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-150"></a>

## DEC-150 — Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?

Cần quyết định: Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?

Mã nguồn: E10-Q11. Người quyết định: Kế toán và chủ nghiệp vụ bán hàng. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q11

[Nguồn, dòng 35](../../../crm-ban-hang/review/questions.md#L35). Nội dung đầy đủ:

> Biên ngày từ–đến, múi giờ, ngày kết thúc bỏ trống và phạm vi giá khác điểm/ca được hiểu thế nào?

Phương án khuyến nghị đã có:

> Chốt một quy ước ngày cho hợp đồng và consumer; giữ khóa phạm vi hiện có cho tới khi có quyết định.

Phương án khác đã có:

> Đề xuất phạm vi giá theo điểm/ca qua phiên thay đổi riêng nếu thực tế cần.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-CONT-001 / UC-CRM-013; FR-SALE-ACTV-001 / UC-CRM-014; FR-SALE-AMND-001 / UC-CRM-015; FR-SALE-PRIC-001 / UC-CRM-016

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-151"></a>

## DEC-151 — Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?

Cần quyết định: Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?

Mã nguồn: E10-Q12. Người quyết định: Kế toán, người duyệt hợp đồng và vận hành. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q12

[Nguồn, dòng 36](../../../crm-ban-hang/review/questions.md#L36). Nội dung đầy đủ:

> Phụ lục hồi tố, thu hồi/thay thế giá và ảnh hưởng đơn đã khóa hoặc kỳ đã đối soát được xử lý thế nào?

Phương án khuyến nghị đã có:

> Mặc định thiết kế giữ lịch sử và chờ quyết định riêng cho hồi tố; chỉ dùng giá mới khi đủ hiệu lực.

Phương án khác đã có:

> Có quy trình điều chỉnh riêng với chứng từ và phê duyệt; không sửa trực tiếp lịch sử.

Tác động / phần chặn được nguồn mô tả:

> FR-SALE-ACTV-001 / UC-CRM-014; FR-SALE-AMND-001 / UC-CRM-015; FR-SALE-PRIC-001 / UC-CRM-016

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-152"></a>

## DEC-152 — Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?

Cần quyết định: Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?

Mã nguồn: E10-Q13. Người quyết định: Trưởng kỹ thuật, chủ các nguồn và QA. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q13

[Nguồn, dòng 37](../../../crm-ban-hang/review/questions.md#L37). Nội dung đầy đủ:

> Hợp đồng kỹ thuật E10 về quyền dịch vụ, receipt, khóa chống trùng, thời hạn lưu, phân trang, lỗi và tải được duyệt ra sao?

Phương án khuyến nghị đã có:

> Adapter từng nguồn; khóa nghiệp vụ bền vững và đối soát sau timeout; profile theo nền.

Phương án khác đã có:

> Tích hợp theo lô có đối soát được duyệt trước khi mở giao tiếp trực tiếp.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-LEAD-001 / UC-CRM-003; FR-SALE-QUOT-001 / UC-CRM-010; FR-SALE-SAFE-001 / UC-CRM-012; FR-SALE-PRIC-001 / UC-CRM-016

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-153"></a>

## DEC-153 — Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?

Cần quyết định: Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?

Mã nguồn: E10-Q14. Người quyết định: Giám đốc, chăm sóc khách, kế toán và QA. Release: R10. [Buổi 7](meeting-agenda.md#buoi-7).

### E10-Q14

[Nguồn, dòng 38](../../../crm-ban-hang/review/questions.md#L38). Nội dung đầy đủ:

> Ai xác nhận danh sách toàn bộ khách đang phục vụ và hợp đồng hiệu lực, tại ngày chốt nào, bằng chứng R10 ở đâu?

Phương án khuyến nghị đã có:

> Manifest nguồn có ngày chốt và chữ ký xác nhận, đối chiếu từng khách/hợp đồng, công khai thiếu.

Phương án khác đã có:

> Đối chiếu nhiều nguồn vận hành/kế toán rồi người có thẩm quyền duyệt danh sách thống nhất.

Tác động / phần chặn được nguồn mô tả:

> FR-CUS-VIEW-001 / UC-CRM-001; FR-SALE-ACTV-001 / UC-CRM-014

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-154"></a>

## DEC-154 — Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng?

Cần quyết định: Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng?

Mã nguồn: E11-Q01. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q01

[Nguồn, dòng 25](../../../mua-hang-san-xuat/review/questions.md#L25). Nội dung đầy đủ:

> Nhu cầu mua có trừ tồn khả dụng, hàng đang về và dự phòng không? Ngưỡng nào được dùng?

Phương án khuyến nghị đã có:

> Tách nhu cầu gộp khỏi lượng đề nghị mua; chưa tự trừ tồn hoặc đặt mức tối thiểu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-074; không tính lượng mua ròng khi thiếu chính sách.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-155"></a>

## DEC-155 — Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào?

Cần quyết định: Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào?

Mã nguồn: E11-Q03. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q03

[Nguồn, dòng 27](../../../mua-hang-san-xuat/review/questions.md#L27). Nội dung đầy đủ:

> Lô đông lạnh/khô cần mã, hạn dùng, vị trí, đơn vị và quy tắc xuất nào?

Phương án khuyến nghị đã có:

> Chỉ quản lý lô FROZEN/DRY; chưa chọn FIFO/FEFO hay bắt buộc hạn dùng.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Ghi lô chi tiết, phân bổ và xuất kho BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-156"></a>

## DEC-156 — Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao?

Cần quyết định: Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao?

Mã nguồn: E11-Q04. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q04

[Nguồn, dòng 28](../../../mua-hang-san-xuat/review/questions.md#L28). Nội dung đầy đủ:

> Nhận thiếu/thừa, nhiều lần, hàng hỏng, trả lại và chỉnh phiếu được xử lý ra sao?

Phương án khuyến nghị đã có:

> Giữ lượng đặt, lượng thực nhận, lượng chấp nhận riêng; cần quyết định trước ghi nhận chính thức.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Công nợ và đối chiếu thực mua còn thiếu căn cứ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-157"></a>

## DEC-157 — Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không?

Cần quyết định: Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không?

Mã nguồn: E11-Q05. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q05

[Nguồn, dòng 29](../../../mua-hang-san-xuat/review/questions.md#L29). Nội dung đầy đủ:

> Chụp ảnh nào, lúc nào, ai xác nhận; lưu bao lâu; có cần OCR hoặc làm việc offline không?

Phương án khuyến nghị đã có:

> Dùng tệp nội bộ E1 và ảnh gắn đúng phiếu; không OCR, không tự chọn thời hạn lưu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chứng từ thực và điều kiện hoàn tất phiếu BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-158"></a>

## DEC-158 — Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào?

Cần quyết định: Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào?

Mã nguồn: E11-Q06. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q06

[Nguồn, dòng 30](../../../mua-hang-san-xuat/review/questions.md#L30). Nội dung đầy đủ:

> Công nợ NCC ghi nhận theo sự kiện nào; kỳ đối chiếu, số đầu kỳ, thanh toán và điều chỉnh có căn cứ nào?

Phương án khuyến nghị đã có:

> Tách phiếu nhận, nghĩa vụ phải trả và chứng từ thanh toán; chưa suy đã trả từ đã nhận.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không tự tạo lịch trả nợ hoặc bù trừ; số dư/kỳ chính thức BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-159"></a>

## DEC-159 — Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung?

Cần quyết định: Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung?

Mã nguồn: E11-Q07. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q07

[Nguồn, dòng 31](../../../mua-hang-san-xuat/review/questions.md#L31). Nội dung đầy đủ:

> Thực mua được gán cho ngày phục vụ/cơ sở thế nào khi mua nhiều ngày, chuyển kho hoặc mua chung?

Phương án khuyến nghị đã có:

> Giữ nguồn mua và phân bổ riêng, chưa chọn phương pháp phân bổ.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-076 không có tỷ lệ chính thức cho dòng chưa phân bổ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-160"></a>

## DEC-160 — BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào?

Cần quyết định: BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào?

Mã nguồn: E11-Q08. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q08

[Nguồn, dòng 32](../../../mua-hang-san-xuat/review/questions.md#L32). Nội dung đầy đủ:

> BO-02 dùng mẫu số, dấu/giá trị tuyệt đối, tập ngày và xử lý ngày không doanh thu như thế nào?

Phương án khuyến nghị đã có:

> Đề nghị so hai tỷ lệ cùng phạm vi và cùng mẫu số đã duyệt; không thay mục tiêu ≤ 3 điểm phần trăm.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> R11 BLOCKED tới khi có công thức đo và dữ liệu thật; không dùng chênh tương đối 3 %.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-161"></a>

## DEC-161 — Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào?

Cần quyết định: Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào?

Mã nguồn: E11-Q09. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q09

[Nguồn, dòng 33](../../../mua-hang-san-xuat/review/questions.md#L33). Nội dung đầy đủ:

> Phân ca cần vai trò, năng lực, ca trùng và cách thay người như thế nào?

Phương án khuyến nghị đã có:

> Lưu phân công nháp theo cơ sở/ca; chưa đặt số người hoặc giờ ca.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kiểm đủ nhân lực và phân ca chính thức BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-162"></a>

## DEC-162 — Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi?

Cần quyết định: Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi?

Mã nguồn: E11-Q10. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q10

[Nguồn, dòng 34](../../../mua-hang-san-xuat/review/questions.md#L34). Nội dung đầy đủ:

> Checklist trước giao có mục nào; ai kiểm và ai cho phép giao khi có lỗi?

Phương án khuyến nghị đã có:

> Tách kết quả QC khỏi phiếu giao E7; mục không đạt/thiếu không tự coi đạt.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Cổng sẵn sàng giao và bàn giao E7 BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-163"></a>

## DEC-163 — Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì?

Cần quyết định: Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì?

Mã nguồn: E11-Q11. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q11

[Nguồn, dòng 35](../../../mua-hang-san-xuat/review/questions.md#L35). Nội dung đầy đủ:

> Mẫu lưu theo bữa hay từng món; lượng mẫu, nhiệt độ, hạn lưu, hủy mẫu và bằng chứng là gì?

Phương án khuyến nghị đã có:

> Có mã mẫu gắn bữa/cơ sở, người ghi và thời điểm; không tự đặt hạn hoặc định lượng mẫu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> R11 cần 100% bữa có mẫu lưu, nhưng xác nhận mẫu hợp lệ còn BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-164"></a>

## DEC-164 — Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào?

Cần quyết định: Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào?

Mã nguồn: E11-Q12. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q12

[Nguồn, dòng 36](../../../mua-hang-san-xuat/review/questions.md#L36). Nội dung đầy đủ:

> Thay món tác động kế hoạch đã chốt/đang sản xuất và thông báo người liên quan thế nào?

Phương án khuyến nghị đã có:

> Chỉ tạo ứng viên nháp; nguồn đổi phải kiểm lại, không sửa trực tiếp order/plan.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Áp dụng thay đổi xuống E6/E7 BLOCKED; không quyết CG05/06/07.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-165"></a>

## DEC-165 — Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt?

Cần quyết định: Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt?

Mã nguồn: E11-Q13. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q13

[Nguồn, dòng 37](../../../mua-hang-san-xuat/review/questions.md#L37). Nội dung đầy đủ:

> Danh sách quyền E11, chuẩn API, khóa chống trùng, lưu receipt, xử lý đồng thời và tải nào được duyệt?

Phương án khuyến nghị đã có:

> Đề nghị version kiểm khi ghi, audit và chống lặp; không chọn TTL, retry hoặc SLA mới.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Kiểm tích hợp/độ bền và profile tải BLOCKED; E1-Q01–05 giữ mở.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-166"></a>

## DEC-166 — Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào?

Cần quyết định: Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào?

Mã nguồn: E11-Q14. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q14

[Nguồn, dòng 38](../../../mua-hang-san-xuat/review/questions.md#L38). Nội dung đầy đủ:

> Nhận hàng có cập nhật giá E3 không; chọn ngày hiệu lực, nguồn xác nhận VAT và giá có phần lẻ thế nào?

Phương án khuyến nghị đã có:

> Đối chiếu PriceInput; không ghi đè giá hiệu lực hoặc tự đặt giá tham chiếu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Port giá chỉ ranh giới; CK/DATA-COST và rounding chưa chốt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-167"></a>

## DEC-167 — Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân?

Cần quyết định: Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân?

Mã nguồn: E11-Q15. Người quyết định: chưa rõ. Release: R11. [Buổi 6](meeting-agenda.md#buoi-6).

### E11-Q15

[Nguồn, dòng 39](../../../mua-hang-san-xuat/review/questions.md#L39). Nội dung đầy đủ:

> Căn cứ dị ứng dùng cho kiểm thay món là gì khi không mở hồ sơ sức khỏe cá nhân?

Phương án khuyến nghị đã có:

> Dùng nhãn chất gây dị ứng của món và ràng buộc thực đơn đã được phép; thiếu căn cứ thì chặn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Không tạo form sức khỏe; kiểm thay món thực BLOCKED khi thiếu dữ liệu/rule đã duyệt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-168"></a>

## DEC-168 — Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì?

Cần quyết định: Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì?

Mã nguồn: E12-Q01. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q01

[Nguồn, dòng 25](../../../phan-hoi-bao-cao/review/questions.md#L25). Nội dung đầy đủ:

> Thang đánh giá, tiêu chí, cách gộp điểm và thời điểm được đánh giá là gì?

Phương án khuyến nghị đã có:

> Dùng thang có phiên bản và nguồn quyết định; chưa chọn số mức hoặc trung bình.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-FB-RATE-001; nhận điểm và thống kê đánh giá thật BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-169"></a>

## DEC-169 — Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao?

Cần quyết định: Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao?

Mã nguồn: E12-Q02. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q02

[Nguồn, dòng 26](../../../phan-hoi-bao-cao/review/questions.md#L26). Nội dung đầy đủ:

> Ai được gửi/xem phản hồi; xác minh QR, số lần gửi, sửa/rút, ẩn danh và trùng xử lý ra sao?

Phương án khuyến nghị đã có:

> Kế thừa identity E6 khi được chốt; giữ nguồn và receipt, không chọn quy tắc một người một điểm thay stakeholder.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-079; E6 CG01/08 và quyền xem danh tính còn chờ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-170"></a>

## DEC-170 — Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào?

Cần quyết định: Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào?

Mã nguồn: E12-Q03. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q03

[Nguồn, dòng 27](../../../phan-hoi-bao-cao/review/questions.md#L27). Nội dung đầy đủ:

> Khiếu nại có danh mục, SLA, phân công, bằng chứng và điều kiện đóng/mở lại nào?

Phương án khuyến nghị đã có:

> Tách tiếp nhận khỏi giải quyết; chưa đặt SLA hoặc người xử lý.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-FB-CASE-001; xử lý/đóng thật BLOCKED; không tự điều chỉnh tiền E7.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-171"></a>

## DEC-171 — Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào?

Cần quyết định: Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào?

Mã nguồn: E12-Q04. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q04

[Nguồn, dòng 28](../../../phan-hoi-bao-cao/review/questions.md#L28). Nội dung đầy đủ:

> Mẫu số tỷ lệ chọn là người được mời chọn, số suất hay chỉ người đã chọn; tập ngày/ca, đổi/hủy/chọn hộ xử lý thế nào?

Phương án khuyến nghị đã có:

> Giữ provenance lựa chọn thật và định nghĩa có phiên bản; hiển thị chưa xác định trước khi duyệt. Không chọn sẵn một mẫu số.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-FB-SELR-001; R12-CHOICE và xếp hạng tỷ lệ BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-172"></a>

## DEC-172 — Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao?

Cần quyết định: Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao?

Mã nguồn: E12-Q05. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q05

[Nguồn, dòng 29](../../../phan-hoi-bao-cao/review/questions.md#L29). Nội dung đầy đủ:

> Đề xuất cải tiến từ phản hồi được ai review, dùng cửa sổ quan sát nào, chuyển MENU ra sao?

Phương án khuyến nghị đã có:

> Người thật review căn cứ; kiểm lại E2/dị ứng/E3, không đổi thực đơn trực tiếp.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-FB-PROP-001; xếp hạng/tự chuyển adapter chưa có căn cứ.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-173"></a>

## DEC-173 — Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào?

Cần quyết định: Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào?

Mã nguồn: E12-Q06. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q06

[Nguồn, dòng 30](../../../phan-hoi-bao-cao/review/questions.md#L30). Nội dung đầy đủ:

> Danh mục chỉ số và định nghĩa từng dashboard PER-05/06/07/08 được chọn thế nào?

Phương án khuyến nghị đã có:

> Review catalog M-FBR-01…09 theo công việc từng vai trò; không coi danh sách đề xuất là mặc định.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-RPT-ROLE-001; R12-DASH cần manifest chỉ số được duyệt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-174"></a>

## DEC-174 — Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope?

Cần quyết định: Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope?

Mã nguồn: E12-Q07. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q07

[Nguồn, dòng 31](../../../phan-hoi-bao-cao/review/questions.md#L31). Nội dung đầy đủ:

> Ai được xem cost, giá nhập, doanh thu, biên lợi nhuận và danh tính người phản hồi trong từng scope?

Phương án khuyến nghị đã có:

> Quyền trường riêng, deny by default, projection ở server/tool/DB; không tự cấp do tên vai trò.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-RPT-CPCT-001, FR-AIO-DQA-001; ma trận quyền thật BLOCKED; E10-Q15 vẫn mở.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-175"></a>

## DEC-175 — Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào?

Cần quyết định: Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào?

Mã nguồn: E12-Q08. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q08

[Nguồn, dòng 32](../../../phan-hoi-bao-cao/review/questions.md#L32). Nội dung đầy đủ:

> Cost % theo khách dùng tập ghép, nguồn số suất, phân bổ, mẫu số và trọng số nào; xử lý thiếu/0 thế nào?

Phương án khuyến nghị đã có:

> Giữ riêng cost % thực đơn và dự toán E3; không bình quân tỷ lệ hoặc suy từ số giao. Chờ định nghĩa tổng hợp có nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-081 theo khách BLOCKED; E11-Q07/08, O-01 và E7 không tự chốt.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-176"></a>

## DEC-176 — Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì?

Cần quyết định: Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì?

Mã nguồn: E12-Q09. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q09

[Nguồn, dòng 33](../../../phan-hoi-bao-cao/review/questions.md#L33). Nội dung đầy đủ:

> Đầu vào, phạm vi và bằng chứng review đề xuất FEAT-082/083 là gì?

Phương án khuyến nghị đã có:

> Allowlist đọc theo người hỏi; mọi thay món/định lượng kiểm lại ba nguồn cùng hash; không cấp apply.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Runtime/duyệt đề xuất thật BLOCKED; kế thừa AIO-Q01–06, không trả lời lại.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-177"></a>

## DEC-177 — Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì?

Cần quyết định: Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì?

Mã nguồn: E12-Q10. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q10

[Nguồn, dòng 34](../../../phan-hoi-bao-cao/review/questions.md#L34). Nội dung đầy đủ:

> Giá lệch so với giá nào, theo đơn vị/VAT/kỳ nào; ngưỡng và hành vi cảnh báo là gì?

Phương án khuyến nghị đã có:

> So nguồn cùng căn cứ và để ngưỡng trống; không mượn BO-02/NFR-COST-002.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-PDEV-001; cảnh báo chính thức BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-178"></a>

## DEC-178 — FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp?

Cần quyết định: FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp?

Mã nguồn: E12-Q11. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q11

[Nguồn, dòng 35](../../../phan-hoi-bao-cao/review/questions.md#L35). Nội dung đầy đủ:

> FEAT-084 được đọc trường CRM nào và ai review nhắc việc/nội dung báo giá nháp?

Phương án khuyến nghị đã có:

> Chỉ đọc projection E10 theo quyền; không tạo task/quote, gửi hoặc cam kết giá.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-CRMS-001/CRMQ-001; contract đọc/review chờ, không sửa E10.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-179"></a>

## DEC-179 — FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm?

Cần quyết định: FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm?

Mã nguồn: E12-Q12. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q12

[Nguồn, dòng 36](../../../phan-hoi-bao-cao/review/questions.md#L36). Nội dung đầy đủ:

> FEAT-085 cho phép hỏi chỉ số nào, độ chi tiết nào và cách xử lý truy vấn có thể suy ngược số bị cấm?

Phương án khuyến nghị đã có:

> Catalog câu hỏi/chỉ số có nguồn, kiểm từng công cụ và output; thiếu định nghĩa thì không trả số.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-AIO-DQA-001; rubric số liệu và kiểm suy ngược cần review.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-180"></a>

## DEC-180 — Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì?

Cần quyết định: Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì?

Mã nguồn: E12-Q13. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q13

[Nguồn, dòng 37](../../../phan-hoi-bao-cao/review/questions.md#L37). Nội dung đầy đủ:

> Nhóm người ăn phi y tế, nguồn mục tiêu, chỉ số/ngưỡng và thời kỳ áp dụng là gì?

Phương án khuyến nghị đã có:

> Mục tiêu cấp nhóm, không theo bệnh lý/cá nhân; số cụ thể chờ NUTR-Q01–04.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-NUTR-GRPT-001/GRPC-001; không tự đặt kcal hoặc dung sai.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-181"></a>

## DEC-181 — Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không?

Cần quyết định: Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không?

Mã nguồn: E12-Q14. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q14

[Nguồn, dòng 38](../../../phan-hoi-bao-cao/review/questions.md#L38). Nội dung đầy đủ:

> Ai duyệt/kích hoạt mục tiêu nhóm; ưu tiên mục tiêu trùng, hiệu lực và kết quả kiểm có chặn công bố không?

Phương án khuyến nghị đã có:

> Mục tiêu nháp có phiên bản; chưa thêm cổng MENU hoặc chọn ưu tiên bản mới.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-086 activation và áp kết quả chính thức BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-182"></a>

## DEC-182 — Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào?

Cần quyết định: Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào?

Mã nguồn: E12-Q15. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q15

[Nguồn, dòng 39](../../../phan-hoi-bao-cao/review/questions.md#L39). Nội dung đầy đủ:

> Nội dung đồng ý nhật ký, quyền chủ thể, rút đồng ý và phạm vi dữ liệu tối thiểu được duyệt thế nào?

Phương án khuyến nghị đã có:

> Đồng ý tự nguyện riêng cho bữa đã ăn; không chọn sẵn, không ảnh hưởng chọn món; không hồ sơ sức khỏe.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FEAT-087 nhận thật BLOCKED; không mở O-03.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-183"></a>

## DEC-183 — Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào?

Cần quyết định: Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào?

Mã nguồn: E12-Q16. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q16

[Nguồn, dòng 40](../../../phan-hoi-bao-cao/review/questions.md#L40). Nội dung đầy đủ:

> Nhật ký lưu bao lâu; xóa nội dung, bản sao, cache và audit cá nhân được chứng minh thế nào?

Phương án khuyến nghị đã có:

> Kế thừa xóa ≤ 72 giờ của nền; tách receipt/hoàn tất; không đặt retention hoặc xóa giao dịch nguồn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-NUTR-DDEL-001; vận hành xóa/retention BLOCKED.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-184"></a>

## DEC-184 — Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào?

Cần quyết định: Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào?

Mã nguồn: E12-Q17. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q17

[Nguồn, dòng 41](../../../phan-hoi-bao-cao/review/questions.md#L41). Nội dung đầy đủ:

> Bằng chứng nào xác nhận cá nhân đã ăn; ai ghi, sửa sai/trùng và chọn đúng snapshot suất thế nào?

Phương án khuyến nghị đã có:

> Cân nhắc xác nhận tự nguyện của người ăn có scope và snapshot; chưa chọn làm chính sách. Không suy từ order/giao/chọn món.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> FR-NUTR-DREC-001; nhận bữa thật BLOCKED; phần xem/xóa và ranh giới vẫn thiết kế độc lập.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-185"></a>

## DEC-185 — Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào?

Cần quyết định: Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào?

Mã nguồn: E12-Q18. Người quyết định: chưa rõ. Release: R12. [Buổi 9](meeting-agenda.md#buoi-9).

### E12-Q18

[Nguồn, dòng 42](../../../phan-hoi-bao-cao/review/questions.md#L42). Nội dung đầy đủ:

> Contract kỹ thuật E12: envelope, giới hạn, idempotency, receipt, version, refresh/cache và profile tải được duyệt thế nào?

Phương án khuyến nghị đã có:

> Adapter theo nguồn, quyền hiện tại và provenance; không tự đặt TTL, retry, quota hoặc chọn hạ tầng.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Freeze API, tích hợp, race và kiểm tải BLOCKED; E1-Q01–05/AIO-Q giữ nguyên.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-186"></a>

## DEC-186 — Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì?

Cần quyết định: Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì?

Mã nguồn: E13-Q01. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q01

[Nguồn, dòng 25](../../../chi-phi-loi-nhuan/review/questions.md#L25). Nội dung đầy đủ:

> Danh mục loại chi phí, tiêu chí trực tiếp/chung và chống trùng với khoản khoán E3 là gì?

Phương án khuyến nghị đã có:

> Duyệt danh mục có phiên bản; mỗi khoản chỉ thuộc một nguồn và một nhóm trong cùng báo cáo.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Ghi nhận chính thức và tổng chi phí; FR-EXP-COST-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-187"></a>

## DEC-187 — Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào?

Cần quyết định: Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào?

Mã nguồn: E13-Q02. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q02

[Nguồn, dòng 26](../../../chi-phi-loi-nhuan/review/questions.md#L26). Nội dung đầy đủ:

> Kỳ chi phí có biên ngày, múi giờ, lịch khóa và người có quyền khóa nào?

Phương án khuyến nghị đã có:

> Chốt cùng scope đối soát; không mặc định tháng hoặc người khóa.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Khóa kỳ và đồng bộ kỳ E7; FR-EXP-PER-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-188"></a>

## DEC-188 — Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì?

Cần quyết định: Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì?

Mã nguồn: E13-Q03. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q03

[Nguồn, dòng 27](../../../chi-phi-loi-nhuan/review/questions.md#L27). Nội dung đầy đủ:

> Nguồn giờ công thực tế và cách xác nhận giờ theo người/cơ sở/ca là gì?

Phương án khuyến nghị đã có:

> Giữ tham chiếu phân ca E11 riêng với giờ thực tế có chứng cứ; không mặc định phần mềm chấm công.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chấm công chính thức; E11-Q09; FR-EXP-TIME-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-189"></a>

## DEC-189 — Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao?

Cần quyết định: Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao?

Mã nguồn: E13-Q04. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q04

[Nguồn, dòng 28](../../../chi-phi-loi-nhuan/review/questions.md#L28). Nội dung đầy đủ:

> Đơn giá nhân công hoặc bảng lương nào được dùng; hiệu lực, giờ đặc biệt, sửa sai xử lý ra sao?

Phương án khuyến nghị đã có:

> Tham chiếu phiên bản nguồn được duyệt; không xây quy trình tính lương.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Chi phí nhân công; FR-EXP-LAB-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-190"></a>

## DEC-190 — Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao?

Cần quyết định: Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao?

Mã nguồn: E13-Q05. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q05

[Nguồn, dòng 29](../../../chi-phi-loi-nhuan/review/questions.md#L29). Nội dung đầy đủ:

> Giám đốc duyệt phương pháp phân bổ nào, cơ sở tính, phạm vi và thời gian hiệu lực ra sao?

Phương án khuyến nghị đã có:

> Trình các lựa chọn theo suất/doanh thu/giờ công/diện tích/kết hợp cùng dữ liệu đối chiếu; không chọn sẵn.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Phân bổ và lợi nhuận khách BLOCKED; FR-EXP-METH-001, FR-EXP-APRV-001, FR-EXP-ALLOC-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-191"></a>

## DEC-191 — Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào?

Cần quyết định: Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào?

Mã nguồn: E13-Q06. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q06

[Nguồn, dòng 30](../../../chi-phi-loi-nhuan/review/questions.md#L30). Nội dung đầy đủ:

> Chi phí chung cấp công ty được đưa về cơ sở nào và ở bước nào?

Phương án khuyến nghị đã có:

> Tách pool cấp công ty, chưa phân bổ không giấu vào cơ sở hoặc khách; chỉ dùng sau quyết định.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Tổng cơ sở và tổng công ty; FR-EXP-RECON-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-192"></a>

## DEC-192 — Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào?

Cần quyết định: Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào?

Mã nguồn: E13-Q07. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q07

[Nguồn, dòng 31](../../../chi-phi-loi-nhuan/review/questions.md#L31). Nội dung đầy đủ:

> Khách nhiều cơ sở, chuyển cơ sở và khách gộp ở E10 giữ khóa đối chiếu thế nào?

Phương án khuyến nghị đã có:

> Giữ customerRef gốc, kitchenRef và revision nguồn; tổng hợp sau đối chiếu từng cơ sở.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Tổng theo khách nhiều cơ sở; FR-EXP-PROF-001.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-193"></a>

## DEC-193 — Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào?

Cần quyết định: Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào?

Mã nguồn: E13-Q09. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q09

[Nguồn, dòng 33](../../../chi-phi-loi-nhuan/review/questions.md#L33). Nội dung đầy đủ:

> Làm tròn, phần dư, độ chính xác tiền và mẫu số bằng 0 được xử lý thế nào?

Phương án khuyến nghị đã có:

> Đối chiếu số gốc decimal; phần dư hiện riêng, không tự dồn cho khách cuối; chặn nếu chưa có quy tắc.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Phân bổ thực và biên lợi nhuận; không mượn dung sai Cost.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-194"></a>

## DEC-194 — Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào?

Cần quyết định: Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào?

Mã nguồn: E13-Q11. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q11

[Nguồn, dòng 35](../../../chi-phi-loi-nhuan/review/questions.md#L35). Nội dung đầy đủ:

> Quyền chi tiết PER-07/PER-08 theo cơ sở, nhóm kế toán, retention và audit lương được cấp thế nào?

Phương án khuyến nghị đã có:

> Deny by default; chỉ cấp từng quyền cần dùng cho hai persona, không suy mọi kế toán đều thấy mọi cơ sở.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Cấp quyền thật/lưu trữ; FR-EXP-SAFE-001; E1-Q01–05.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-195"></a>

## DEC-195 — Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào?

Cần quyết định: Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào?

Mã nguồn: E13-Q12. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q12

[Nguồn, dòng 36](../../../chi-phi-loi-nhuan/review/questions.md#L36). Nội dung đầy đủ:

> Contract nguồn, tính mới, khóa chống trùng, phiên bản, receipt, tải và cơ chế export nội bộ được duyệt thế nào?

Phương án khuyến nghị đã có:

> Nguồn không đầy đủ thì BLOCKED; chụp manifest và không ghi lại snapshot cũ; chưa đặt TTL, SLA, định dạng xuất.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Freeze API/tích hợp/tải; E7-Q08, E10-Q13, E11-Q13, E12-Q18.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-196"></a>

## DEC-196 — Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào?

Cần quyết định: Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào?

Mã nguồn: E13-Q13. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q13

[Nguồn, dòng 37](../../../chi-phi-loi-nhuan/review/questions.md#L37). Nội dung đầy đủ:

> Định nghĩa và quyền chỉ số lợi nhuận/biên lợi nhuận E13 chuyển sang E12 được duyệt thế nào?

Phương án khuyến nghị đã có:

> Đề xuất chỉ đọc tổng hợp có version và trạng thái; không thay cost % E12, không chốt E10-Q15.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> Biên lợi nhuận và kết nối dashboard; E12-Q06/07/08.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.

<a id="dec-197"></a>

## DEC-197 — Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu?

Cần quyết định: Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu?

Mã nguồn: E13-Q14. Người quyết định: chưa rõ. Release: R13. [Buổi 5](meeting-agenda.md#buoi-5).

### E13-Q14

[Nguồn, dòng 38](../../../chi-phi-loi-nhuan/review/questions.md#L38). Nội dung đầy đủ:

> Bằng chứng R7, R11 hoàn tất và người xác nhận bộ đối chiếu độc lập R13 ở đâu?

Phương án khuyến nghị đã có:

> Lập bộ chứng từ cùng kỳ/cơ sở, số chuẩn độc lập; Giám đốc xác nhận phương pháp rồi đối chiếu.

Phương án khác đã có:

Chưa tách riêng; các lựa chọn nêu trong câu hỏi nguồn vẫn để mở.

Tác động / phần chặn được nguồn mô tả:

> R13 chưa nghiệm thu; không dùng kiểm mock thay dữ liệu thật.

Tác động riêng cho từng lựa chọn chưa được nguồn phân định: cần xác nhận; không dùng tác động chung làm bằng chứng một phương án đã được chọn.
