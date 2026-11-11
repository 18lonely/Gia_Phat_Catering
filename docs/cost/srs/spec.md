# Tài liệu Đặc tả Yêu cầu Kỹ thuật (SRS) — Epic E3 · Cost

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Epic | E3 · `cost` — đợt phát hành R3 (v0.3.0) |
| Phân hệ | COST |
| Tính năng PRD | `FEAT-014` → `FEAT-018` |
| Phiên bản | 0.3.2 |
| Trạng thái | Draft — **công thức ở mục 3.3 viết dưới dạng tham số**: bốn lựa chọn chưa chốt (O-01, E3-Q1, E3-Q2, E3-Q4) được đặc tả thành tham số cấu hình, giá trị mặc định là đề xuất |
| Ngày | 2026-11-11 |
| Tiêu chuẩn | IEEE Std 830-1998 / ISO/IEC/IEEE 29148 |

### Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.3.2 | 2026-11-11 | BA | Liên kết hồ sơ bổ sung E1–E5/E6 khởi đầu; giữ quy tắc và điểm mở |
| 0.3.1 | 2026-11-11 | BA | Liên kết hợp đồng E4/E5; giữ nguyên FR và cổng duyệt/Cost |
| 0.3.0 | 2026-11-11 | BA | Đồng bộ thiết kế mở rộng kế toán; giữ45 FR Cost gốc,6 FR-ACC đề xuất tách riêng; chuẩn nghiệm thu giữ NFR-COST-002. |
| 0.2.0 | 2026-11-11 | BA | Ghi xác nhận giá cost gồm VAT phải trả, cờ hóa đơn riêng và chiết khấu khách ghi riêng; bổ sung phạm vi CR, chưa chốt chi tiết/API/migration. |
| 0.1.4 | 2026-11-11 | BA | Liên kết backlog/AC/test và ghi QA-COST-Q01 cần thống nhất mã NCC ngừng; chưa đổi quy tắc/mã lỗi. |
| 0.1.3 | 2026-11-11 | BA | Bổ sung liên kết hợp đồng API và wireframe; không thay quyết định nghiệp vụ. |
| 0.1.2 | 2026-11-11 | BA | Liên kết 16 use case/user flow và câu hỏi phát hiện; làm rõ mô tả số quy tắc, kiểu lưu tiền và nguồn tài liệu theo đặc tả hiện có. |
| 0.1.1 | 2026-11-11 | BA | Đồng bộ 9 mục phụ thuộc với ERD/DBML, tham số và wireframe; làm rõ chế độ cảnh báo; ghi nhận điểm cần xác nhận khi thiết kế dữ liệu. |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo từ epic-spec cost v0.1.0 |

Quy ước: **[D-xx]** đã chốt · **[ĐỀ XUẤT]** chờ duyệt · **[O-xx] / [E3-Qx]** điểm mở, giữ nguyên trạng thái mở. Con số không ghi nguồn là [ĐỀ XUẤT].

---

## 1. Giới thiệu

### 1.1 Mục đích

Đặc tả hành vi của phân hệ COST trong đợt R3: nhà cung cấp, giá nhập, cost món, cost suất và ngưỡng, bảng dự toán, cảnh báo khi giá biến động.

### 1.2 Phạm vi

Theo mục 1.4 của [epic-spec](../epic-spec.md). Không gồm: đơn mua, nhận hàng, công nợ, đối chiếu dự toán với thực mua (R11); chi phí ngoài nguyên liệu (R13); số suất từ order (R6).

### 1.3 Cách tài liệu này xử lý các điểm chưa chốt

Bốn lựa chọn quyết định công thức chưa có câu trả lời. Thay vì chờ, SRS đặc tả mỗi lựa chọn thành **một tham số cấu hình** của phân hệ, liệt kê các giá trị được hỗ trợ và đề xuất một giá trị mặc định. Khi Gia Phát quyết, chỉ cần đặt tham số; nếu quyết định rơi ngoài các giá trị đã liệt kê thì phải sửa SRS.

| Điểm mở | Tham số | Giá trị hỗ trợ | Mặc định [ĐỀ XUẤT] |
| :--- | :--- | :--- | :--- |
| E3-Q1 | `COST_MON_CHINH_CACH_TINH` | `DAT_NHAT` · `BINH_QUAN` · `MAC_DINH` | `DAT_NHAT` |
| E3-Q2 | `COST_AP_HAO_HUT` | `KHONG` · `CO` | `KHONG` |
| E3-Q4 | (không phải tham số) | Kế toán đánh dấu giá tham chiếu | — |
| O-01 | `VAT_PCT`; danh sách khoản khoán; cờ "tính vào cost" của từng nguyên liệu | Xem `FR-COST-MEAL-004` | Chưa có giá trị |

Lý do chọn mặc định: `DAT_NHAT` không bao giờ cho kết quả thấp hơn thực tế, nên không có ngày nào "đạt trên giấy, vượt ngoài bếp". `KHONG` khớp cách đọc trực tiếp chữ "định lượng món sống" của docx.

### 1.4 Thuật ngữ

| Thuật ngữ | Nghĩa |
| :--- | :--- |
| Giá nhập | Giá mua một đơn vị mua của nguyên liệu từ một nhà cung cấp, có ngày hiệu lực |
| Giá tham chiếu | Giá nhập được dùng để tính cost của một nguyên liệu tại một cơ sở và một ngày |
| Cost món | Tiền nguyên liệu cho một suất của một món, theo định lượng chuẩn |
| Cost suất | Tiền nguyên liệu cho một suất hoàn chỉnh của một ngày |
| Cost % | Cost suất ÷ doanh thu chưa VAT của suất × 100 |
| Ngưỡng | Giá trị tham số `COST_NGUONG_PCT` có hiệu lực tại ngày phục vụ; mặc định 52 [D-08] |
| Khoản khoán | Số tiền cố định cộng vào cost mỗi suất cho những thứ không tính theo công thức (ví dụ gia vị) |
| Món đặc thù | Món có cờ "đặc thù" (nguyên liệu giá cao): cần bảng tính cost được duyệt trước khi vào thực đơn |
| Ngày tính | Ngày dùng để chọn công thức hiệu lực và giá hiệu lực; với thực đơn là ngày phục vụ |

### 1.5 Tài liệu tham chiếu

[Epic-spec cost](../epic-spec.md) · [Bảng quy tắc](../../gia-phat/brainstorms/quy-tac-thuc-don.md) nhóm G · [SRS epic thực đơn v0.3.1](../../thuc-don-dinh-luong/srs/spec.md) · [SRS nền tảng v0.2.0](../../nen-tang/srs/spec.md) · [ERD v0.3.0](../../nen-tang/srs/erd.md) mục 5 · [Use case và truy vết](usecase-diagram.md) · [User flow](../ui/user-flow.md) · `Yêu cầu về thực đơn và cost tp.docx`

---

## 2. Mô tả tổng quan

### 2.1 Bối cảnh

COST là một module trong API NestJS. Nó **đọc** nguyên liệu, công thức, món, loại suất, thực đơn qua dịch vụ nội bộ của MENU, không truy vấn thẳng bảng của MENU. Nó **gắn vào** MENU ở hai chỗ: đăng ký 4 quy tắc `BR-COST-001`, `005`, `006`, `007` vào bộ kiểm (`FR-MENU-RUL-001`), bổ sung cho 4 quy tắc đã hiện thực tại E2 theo mục 3.3.3; và đăng ký một bước kiểm vào cổng gửi duyệt thực đơn (`FR-MENU-APV-006`).

Dịch vụ COST cung cấp cho module khác:

| Dịch vụ | Dùng bởi | Trả về |
| :--- | :--- | :--- |
| Cost món tại một ngày, một cơ sở | E5 (Agent Nội bộ), R11 | Cost và bảng phân rã |
| Cost % của một thực đơn (đã lưu hoặc chưa lưu) | E5 | Cost % từng ngày, phân rã |
| Đạt / không đạt ngân sách | E9 (Agent Dinh dưỡng viên) | Một trạng thái DAT / KHONG_DAT / KHONG_XAC_DINH cho cả thực đơn; không có con số |
| Bảng dự toán đã lưu | R11 | Các dòng dự toán để đối chiếu thực mua |

### 2.2 Quyền theo vai trò

| Quyền | `DINH_DUONG_VIEN` | `KT_MUA_HANG` | `KT_DOANH_THU` | `GIAM_DOC` | `QL_CO_SO` | `BEP_TRUONG` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `cost.supplier.read` | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| `cost.supplier.write` | — | ✓ | — | — | — | — |
| `cost.price.read` — xem giá nhập | ✓ | ✓ | ✓ | ✓ | Cơ sở mình | — |
| `cost.price.write` — nhập giá | — | ✓ | — | — | — | — |
| `cost.cost.read` — xem cost món, cost suất, cost % | ✓ | ✓ | ✓ | ✓ | Cơ sở mình | — |
| `cost.sheet.write` — lập bảng tính cost món đặc thù | ✓ | — | — | — | — | — |
| `cost.sheet.approve` — duyệt bảng tính cost | — | — | — | ✓ | — | — |
| `cost.estimate.write` — lập bảng dự toán | ✓ | ✓ | — | — | — | — |
| `cost.estimate.read` — xem bảng dự toán có giá | ✓ | ✓ | ✓ | ✓ | Cơ sở mình | — |
| `cost.estimate.qty` — xem dự toán chỉ có số lượng, không có giá | ✓ | ✓ | ✓ | ✓ | Cơ sở mình | Cơ sở mình |
| `cost.allowance.write` — đề nghị sửa khoản khoán | — | ✓ | — | — | — | — |
| `cost.allowance.approve` — duyệt khoản khoán | — | — | — | ✓ | — | — |
| `cost.alert.read` — xem cảnh báo cost | ✓ | ✓ | — | ✓ | — | — |

Bếp trưởng không xem giá và cost là [ĐỀ XUẤT] — [E3-Q11]. Người duyệt: [O-06].

Tài khoản dịch vụ: `svc-agent-noi-bo` nhận quyền theo người đang dùng (`BR-SEC-009`). `svc-agent-dinh-duong-vien` **chỉ** có quyền gọi `FR-COST-RUL-003` và không có quyền nào ở bảng trên (`BR-SEC-010`).

### 2.3 Ràng buộc

- Giá nhập và khoản khoán lưu số nguyên đồng. Kết quả tính lưu số thập phân theo ERD v0.3.0 mục 5.4 để không mất phần lẻ; đây là lựa chọn lưu trữ đề xuất. Phép tính trung gian không dùng số thực dấu phẩy động; làm tròn hiển thị, cost % và lượng mua theo `BR-CALC-006`, `BR-EST-002`.
- Giá nhập và kết quả đã chụp không bị sửa đè: thay đổi là dòng mới.
- Mọi lệnh ghi sinh nhật ký thay đổi (`FR-SYS-AUD-001`).
- Không dịch vụ, API hay thông báo nào hướng ra cổng khách hoặc website chứa giá nhập, cost hay cost %.

### 2.4 Giả định và phụ thuộc

Theo mục 2.5 của epic-spec: R2; DL-01, DL-02, DL-06; bảng tính tay của kế toán cho 10 món và 10 ngày mẫu.

---

## 3. Yêu cầu chi tiết

### 3.1 Yêu cầu chức năng

#### Nhà cung cấp — `FEAT-014`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-SUP-001` | Tạo, sửa nhà cung cấp | P0 | Bản tối thiểu để gắn với giá nhập. | tên, loại (thường xuyên / tiểu thương), số điện thoại, ghi chú | Nhà cung cấp `ACTIVE` | `BR-PRC-001` | `ERR-COST-409-01` |
| `FR-COST-SUP-002` | Ngừng nhà cung cấp | P0 | Chuyển `INACTIVE`. Giá đã nhập của nhà cung cấp này vẫn giữ và vẫn dùng được cho các ngày đã qua; không nhập được giá mới. Giá tham chiếu đang trỏ tới nhà cung cấp này sinh cảnh báo. | mã, lý do | Trạng thái mới | `BR-PRC-007` | — |
| `FR-COST-SUP-003` | Danh sách nhà cung cấp | P0 | Lọc theo tên, loại, trạng thái. | bộ lọc | Danh sách | — | — |

#### Giá nhập — `FEAT-014`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-PRC-001` | Nhập một giá | P0 | Tạo một dòng giá cho nguyên liệu `ACTIVE`: giá trên một **đơn vị mua** của nguyên liệu. Cơ sở để trống = áp dụng cả hai cơ sở. | nguyên liệu, nhà cung cấp, cơ sở (tuỳ chọn), giá, ngày hiệu lực, đánh dấu tham chiếu | Dòng giá | `BR-PRC-002` → `006` | `ERR-COST-422-01`, `ERR-COST-422-02`, `ERR-COST-409-02`, `ERR-COST-404-01` |
| `FR-COST-PRC-002` | Đặt giá tham chiếu | P0 | Với mỗi nguyên liệu, cơ sở và ngày hiệu lực có đúng một dòng được đánh dấu tham chiếu. Đánh dấu dòng mới thì bỏ đánh dấu dòng cũ cùng ngày hiệu lực. Dòng đầu tiên của một nguyên liệu tự là tham chiếu. | mã dòng giá | — | `BR-PRC-005` | — |
| `FR-COST-PRC-003` | Lấy giá tham chiếu | P0 | Trả giá tham chiếu của một nguyên liệu tại một cơ sở và một ngày, theo thứ tự ưu tiên ở `BR-PRC-006`. | nguyên liệu, cơ sở, ngày | Giá, nhà cung cấp, ngày hiệu lực của giá | `BR-PRC-006` | `ERR-COST-404-02` |
| `FR-COST-PRC-004` | Nhập giá dạng lưới | P0 | Một màn hình liệt kê nguyên liệu (lọc theo nhóm, loại bảo quản, "đang dùng trong công thức hiệu lực") với giá tham chiếu hiện tại; kế toán gõ giá mới và ngày hiệu lực cho nhiều dòng rồi lưu một lần. Dòng không đổi bị bỏ qua. Lưu tất cả hoặc không gì cả. | danh sách (nguyên liệu, nhà cung cấp, cơ sở, giá, ngày hiệu lực) | Số dòng đã tạo | Như `001` | Như `001`, báo theo dòng |
| `FR-COST-PRC-005` | Nhập giá từ bảng tính | P0 | Dùng khung nhập của E2 (`FR-MENU-IMP-001` → `003`) với mẫu "giá nhập": tải mẫu, kiểm tệp, nhập. | tệp `.xlsx` | Số dòng đã tạo | `BR-CAT-023`, `BR-PRC-002` → `005` | `ERR-MENU-422-20` |
| `FR-COST-PRC-006` | Lịch sử giá | P0 | Danh sách giá của một nguyên liệu theo ngày hiệu lực, nhà cung cấp, cơ sở; đánh dấu dòng tham chiếu và dòng đang áp dụng hôm nay. | nguyên liệu | Danh sách | — | — |
| `FR-COST-PRC-007` | Huỷ một giá chưa hiệu lực | P0 | Chỉ huỷ được dòng có ngày hiệu lực sau hôm nay. Dòng đã hiệu lực không sửa, không huỷ. | mã dòng, lý do | — | `BR-PRC-004` | `ERR-COST-409-03` |
| `FR-COST-PRC-008` | Nguyên liệu chưa có giá | P0 | Liệt kê nguyên liệu nằm trong công thức `ACTIVE` mà không lấy được giá tham chiếu cho hôm nay, theo từng cơ sở. | cơ sở | Danh sách kèm số món bị ảnh hưởng | — | — |
| `FR-COST-PRC-009` | Cảnh báo giá cũ | P0 | Tác vụ hằng ngày: nguyên liệu đang dùng trong công thức `ACTIVE` có giá tham chiếu với ngày hiệu lực cũ hơn ngưỡng của loại bảo quản thì sinh một cảnh báo cho `KT_MUA_HANG`. Một nguyên liệu chỉ có một cảnh báo đang mở. | — | Cảnh báo | `BR-PRC-008`; `BR-COST-005` | — |
| `FR-COST-PRC-010` | Cảnh báo giá lệch bất thường | P1 | Khi nhập giá mới lệch quá `GIA_NHAP_LECH_CANH_BAO_PCT` so với giá tham chiếu liền trước: hỏi xác nhận trước khi lưu; không chặn. | — | Hộp xác nhận | `BR-PRC-009` | — |
| `FR-COST-PRC-011` | Đính kèm chứng từ | P1 | Gắn một ảnh hoặc PDF cho một dòng giá hoặc cho cả một lần nhập lưới. | tệp | — | — | `ERR-SYS-413-01`, `ERR-SYS-415-01` |

Giá nhập có cần người thứ hai duyệt không: [E3-Q6]. SRS này **không** có bước duyệt giá nhập.

#### Cost món — `FEAT-015`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-DISH-001` | Tính cost món | P0 | Tính cost một suất của một món theo công thức hiệu lực và giá tham chiếu tại ngày tính và cơ sở. Công thức ở mục 3.3.1. Không lưu kết quả. | món, cỡ định lượng, ngày tính, cơ sở | Cost món (đồng), bảng phân rã | `BR-CALC-001` → `003`, `006` | `ERR-COST-422-03`, `ERR-MENU-404-01` |
| `FR-COST-DISH-002` | Bảng phân rã cost món | P0 | Mỗi dòng: nguyên liệu, là nguyên liệu chính hay không, định lượng chuẩn, đơn vị, giá một đơn vị dùng, thành tiền, tỷ trọng %, nhà cung cấp và ngày hiệu lực của giá đã dùng. | như `001` | Bảng | — | — |
| `FR-COST-DISH-003` | Thiếu giá | P0 | Nếu một nguyên liệu có cờ "tính vào cost" không có giá tham chiếu: không trả cost; trả danh sách nguyên liệu thiếu giá. | — | Danh sách thiếu | `BR-CALC-003` | `ERR-COST-422-03` |
| `FR-COST-DISH-004` | Cost trong danh sách món và hộp chọn món | P0 | Với người có `cost.cost.read`: danh sách món và hộp chọn món của màn soạn thực đơn hiện cost món tại ngày tương ứng (hôm nay; ngày phục vụ của ô). Món thiếu giá hiện "thiếu giá". Người không có quyền không nhận trường này trong phản hồi API. | — | Cột cost | — | — |
| `FR-COST-DISH-005` | So sánh cost hai phiên bản công thức | P1 | Cost của phiên bản đang hiệu lực và phiên bản đề nghị tại cùng ngày tính, kèm chênh lệch đồng và %. Hiện ở màn duyệt công thức. | 2 mã công thức, ngày, cơ sở | Bảng so sánh | — | `ERR-COST-422-03` |
| `FR-COST-DISH-006` | Lập bảng tính cost món đặc thù | P0 | Với món có cờ "đặc thù": dinh dưỡng viên chụp lại bảng phân rã cost tại một ngày, ghi chú, gửi duyệt. | món, ngày tính, cơ sở, ghi chú | Bảng tính `PENDING` | `BR-CALC-007` | `ERR-COST-422-03`, `ERR-COST-422-04` |
| `FR-COST-DISH-007` | Duyệt bảng tính cost món đặc thù | P0 | Duyệt → `APPROVED`; trả lại kèm lý do. Người duyệt khác người lập. | mã, quyết định, lý do | Trạng thái mới | `BR-SEC-008`, `BR-CALC-007` | `ERR-SYS-403-01`, `ERR-SYS-422-01` |
| `FR-COST-DISH-008` | Gợi ý nhóm cost của món | P1 | Từ cost món, gợi ý nhóm "thấp" hoặc "cao" khi tạo hoặc sửa món. Không tự ghi; người dùng quyết. Ngưỡng phân nhóm: [E3-Q7] | món | Gợi ý | — | — |

#### Cost suất và ngưỡng — `FEAT-016`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-MEAL-001` | Tính cost suất và cost % của một ngày | P0 | Theo mục 3.3.2. Dùng cho thực đơn đã lưu và thực đơn chưa lưu. | thực đơn hoặc nội dung thực đơn, ngày, cơ sở | Cost suất, doanh thu chưa VAT, cost %, ngưỡng, đạt / không đạt, phân rã | `BR-CALC-004` → `006`; `BR-COST-001` → `004` | `ERR-COST-422-03`, `ERR-COST-422-05` |
| `FR-COST-MEAL-002` | Cost % trên màn soạn thực đơn | P0 | Mỗi cột ngày hiện cost % và nhãn đạt / vượt; cập nhật sau mỗi lần đổi món, cùng lượt với bộ kiểm quy tắc. Ngày chưa đủ món hiện cost của phần đã có và ghi "chưa đủ món". Ngày có món thiếu giá hiện "thiếu giá". | — | — | — | — |
| `FR-COST-MEAL-003` | Phân rã cost của một ngày | P0 | Phần món chính (kèm cost từng món chính và cách tính đang dùng), từng món phụ, rau, canh, từng khoản khoán; tổng; doanh thu chưa VAT; cost %; số tiền còn dư hoặc vượt so với ngưỡng. | thực đơn, ngày, cơ sở | Bảng | — | — |
| `FR-COST-MEAL-004` | Quản lý khoản khoán | P0 | Danh sách khoản khoán trên một suất: tên, số tiền, loại suất áp dụng (hoặc mọi loại suất), ngày hiệu lực. Thay đổi là đề nghị chờ duyệt. Danh sách khoản ban đầu: [O-01] | tên, số tiền, loại suất, ngày hiệu lực, lý do | Đề nghị `PENDING` | `BR-CALC-008`, `BR-SEC-008` | `ERR-COST-422-06`, `ERR-SYS-403-01` |
| `FR-COST-MEAL-005` | Kiểm cost ở cổng gửi duyệt thực đơn | P0 | Đăng ký vào `FR-MENU-APV-006`. Khi gửi duyệt: tính cost % mọi ngày theo cơ sở kiểm (`BR-CALC-009`); có ngày vượt ngưỡng ở chế độ `CHAN`, hoặc thiếu giá/VAT, hoặc có món đặc thù chưa có bảng tính đã duyệt → không cho gửi duyệt, trả chi tiết từng ngày theo quyền. Ở `CANH_BAO`, vượt ngưỡng chỉ cảnh báo theo `FR-COST-MEAL-008`, không bỏ qua lỗi thiếu đầu vào. | mã thực đơn | Đạt / không đạt + chi tiết | `BR-COST-001`, `007`; `BR-CALC-009` | `ERR-COST-422-07`, `ERR-COST-422-03`, `ERR-COST-422-04` |
| `FR-COST-MEAL-006` | Chụp kết quả khi duyệt | P0 | Khi thực đơn chuyển `APPROVED`: lưu cho từng ngày cost suất, cost %, ngưỡng, giá trị các tham số cách tính, và danh sách (nguyên liệu, giá, ngày hiệu lực của giá) đã dùng. Kết quả chụp không đổi khi giá hoặc tham số đổi sau. | — | Bản chụp | `BR-CALC-010` | — |
| `FR-COST-MEAL-007` | Ngoại lệ vượt ngưỡng | Chưa xếp | Cho phép người có thẩm quyền duyệt một thực đơn có ngày vượt ngưỡng, kèm lý do. Có làm hay không: [E3-Q9]. SRS này **chặn tuyệt đối khi chế độ là `CHAN`**; `CANH_BAO` theo `FR-COST-MEAL-008` không phải cơ chế duyệt ngoại lệ. | — | — | — | — |
| `FR-COST-MEAL-008` | Chế độ chỉ cảnh báo | P0 | Tham số `COST_CHE_DO_KIEM` có hai giá trị: `CANH_BAO` (ngày vượt ngưỡng hiện cảnh báo nhưng không chặn gửi duyệt) và `CHAN`. Mặc định `CANH_BAO`; chuyển sang `CHAN` cần Giám đốc duyệt. Dùng cho giai đoạn chạy thử (rủi ro E3-R4). | giá trị, lý do | Tham số mới | `BR-SYS-002` | — |

#### Quy tắc cost trong bộ kiểm — `FEAT-016`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-RUL-001` | Đăng ký quy tắc cost vào bộ kiểm | P0 | Đăng ký `BR-COST-001`, `005`, `006`, `007` thành quy tắc của bộ kiểm quy tắc E2, để vi phạm hiện trong bảng kiểm cùng các quy tắc thực đơn. `BR-COST-002` → `004` là cách tính, không phải quy tắc kiểm. `BR-COST-011` hiện thực ở `FR-COST-ALR-001`. Cách tính ở mục 3.3.3. | — | Kết quả trong bảng kiểm | `BR-COST-001`, `005`, `006`, `007` | — |
| `FR-COST-RUL-002` | Ẩn con số với người không có quyền | P0 | Kết quả của các quy tắc cost trong bảng kiểm: người có `cost.cost.read` thấy cost % và số tiền; người không có quyền chỉ thấy "đạt / không đạt". | — | — | — | — |
| `FR-COST-RUL-003` | Dịch vụ đạt / không đạt ngân sách | P0 | Nhận nội dung một thực đơn (loại suất, tuần, món theo ngày); trả cho **cả thực đơn** một giá trị: `DAT`, `KHONG_DAT`, hoặc `KHONG_XAC_DINH` (thiếu giá). Không trả cost, cost %, ngưỡng, ngày nào vượt, hay món nào gây vượt. Giới hạn 30 lời gọi mỗi phiên trò chuyện. | nội dung thực đơn | Một giá trị | `BR-SEC-010`, `BR-CALC-011` | `ERR-COST-429-01`, `ERR-MENU-422-14` |

`FR-COST-RUL-003` trả theo cả thực đơn thay vì từng ngày để khó dò ngược ra cost hơn (rủi ro E3-R6); đây là [ĐỀ XUẤT] và làm agent phía khách kém hữu ích hơn khi sửa thực đơn — cần cân nhắc khi thiết kế E9.

#### Bảng dự toán — `FEAT-017`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-EST-001` | Lập bảng dự toán một ngày | P0 | Cho một ngày của thực đơn (trạng thái bất kỳ), một cơ sở, và số suất theo từng món chính: sinh các dòng dự toán theo mục 3.3.4. Lưu thành một bản có số thứ tự. | thực đơn, ngày, cơ sở, số suất từng món chính | Bảng dự toán | `BR-EST-001` → `004` | `ERR-COST-422-03`, `ERR-COST-422-08` |
| `FR-COST-EST-002` | Nhập số suất dự kiến | P0 | Số suất nhập cho từng món chính của ngày; tổng là số suất của ngày. Món phụ, rau, canh tính theo tổng. Nguồn số suất trước khi có order: [E3-Q8] | số nguyên ≥ 0 cho từng món chính | — | `BR-EST-001` | `ERR-COST-422-08` |
| `FR-COST-EST-003` | Dự toán cả tuần | P0 | Lập cho mọi ngày của thực đơn trong một lần; thêm bảng gộp theo nguyên liệu cho cả tuần. | thực đơn, cơ sở, số suất theo ngày và món chính | Bảng theo ngày + bảng gộp tuần | `BR-EST-003` | Như `001` |
| `FR-COST-EST-004` | Các cột của bảng dự toán | P0 | Mỗi dòng: tên nguyên liệu, nhà cung cấp, giá nhập trên đơn vị mua, định lượng trên một suất (theo từng món dùng nó), số suất, tổng định lượng theo đơn vị dùng, lượng cần mua theo đơn vị mua, thành tiền. Cuối bảng: tổng chi phí, doanh thu chưa VAT, cost %. | — | — | Docx mục IV | — |
| `FR-COST-EST-005` | Xem dự toán không có giá | P0 | Với quyền `cost.estimate.qty`: cùng bảng nhưng không có cột giá, thành tiền, tổng chi phí, cost %. Dùng cho bếp trưởng. | — | — | — | — |
| `FR-COST-EST-006` | Lập lại và lịch sử | P0 | Lập lại cho cùng thực đơn, ngày, cơ sở tạo bản mới; bản cũ giữ nguyên. Mỗi bản ghi thời điểm lập, người lập, số suất, các giá đã dùng. | — | Danh sách các bản | `BR-EST-004` | — |
| `FR-COST-EST-007` | Xuất bảng dự toán | P1 | Xuất `.xlsx` và PDF. Bản không có giá khi người xuất chỉ có quyền `cost.estimate.qty`. | mã bảng | Tệp | — | — |

#### Cảnh báo khi giá biến động — `FEAT-018`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-COST-ALR-001` | Tính lại thực đơn khi có giá mới | P1 | Khi một giá tham chiếu mới được tạo hoặc đến ngày hiệu lực: tác vụ nền tính lại cost % của mọi ngày phục vụ từ hôm nay trở đi thuộc thực đơn `APPROVED` hoặc `PUBLISHED` có dùng nguyên liệu đó. Bản chụp lúc duyệt không bị sửa; kết quả mới lưu riêng. Hoàn tất trong ≤ 5 phút. | — | Kết quả tính lại | `BR-COST-011` | — |
| `FR-COST-ALR-002` | Cảnh báo thực đơn vượt ngưỡng do giá mới | P1 | Ngày nào chuyển từ đạt sang vượt ngưỡng thì sinh cảnh báo cho `DINH_DUONG_VIEN` và `GIAM_DOC`: thực đơn, ngày, cost % lúc duyệt → hiện tại, nguyên liệu và giá gây ra. Mỗi (thực đơn, ngày) chỉ có một cảnh báo đang mở; cập nhật nếu giá đổi tiếp. | — | Cảnh báo + thông báo | `BR-COST-011` | — |
| `FR-COST-ALR-003` | Danh sách và xử lý cảnh báo | P1 | Liệt kê cảnh báo đang mở. Một cảnh báo đóng khi: thực đơn được thu hồi và sửa; hoặc giá đổi lại làm ngày đó đạt; hoặc người có `cost.alert.read` đóng tay kèm lý do. | bộ lọc; mã, lý do | — | `BR-AUD-001` | `ERR-SYS-422-01` |
| `FR-COST-ALR-004` | Chặn chuyển bếp | Chưa xếp | Docx: "rà soát… trước khi triển khai". R3 chưa có bước chuyển bếp. Hiện thực ở đợt nào và chặn hay chỉ cảnh báo: [E3-Q10] | — | — | — | — |
| `FR-COST-ALR-005` | Xem trước tác động của một giá | P2 | Nhập giá giả định cho một nguyên liệu; trả danh sách ngày thực đơn sẽ vượt ngưỡng. Không lưu gì. | nguyên liệu, giá, cơ sở | Danh sách | — | — |

### 3.2 Quy tắc nghiệp vụ của dữ liệu và cách tính

Quy tắc từ docx (`BR-COST-001` → `012`) nằm ở [bảng quy tắc](../../gia-phat/brainstorms/quy-tac-thuc-don.md). Bảng dưới là quy tắc về dữ liệu và cách tính của phân hệ.

| Mã BR | Tên quy tắc | Phát biểu (KHI – THÌ) | Ngoại lệ |
| :--- | :--- | :--- | :--- |
| `BR-PRC-001` | Tên nhà cung cấp không trùng | So trùng như `BR-CAT-001` | — |
| `BR-PRC-002` | Giá nhập hợp lệ | Giá là số nguyên đồng > 0, tính trên **một đơn vị mua** của nguyên liệu | Giá 0 không được nhận; nguyên liệu không mất tiền thì bỏ cờ "tính vào cost" |
| `BR-PRC-003` | Ngày hiệu lực của giá nhập | Ngày hiệu lực được ở quá khứ tối đa `GIA_NHAP_HOI_TO_NGAY` ngày (mặc định 7) và không quá 30 ngày ở tương lai | — |
| `BR-PRC-004` | Giá đã hiệu lực là bất biến | KHI giá có ngày hiệu lực ≤ hôm nay THÌ không sửa, không huỷ; sửa bằng cách nhập dòng mới | Nhập giá hồi tố theo `BR-PRC-003` không sửa dòng cũ mà thêm dòng |
| `BR-PRC-005` | Một giá tham chiếu | Với mỗi (nguyên liệu, cơ sở hoặc "cả hai", ngày hiệu lực) có đúng một dòng tham chiếu; không trùng (nguyên liệu, nhà cung cấp, cơ sở, ngày hiệu lực) | — |
| `BR-PRC-006` | Thứ tự chọn giá tham chiếu | Giá tham chiếu tại (nguyên liệu, cơ sở C, ngày D) = dòng tham chiếu có ngày hiệu lực lớn nhất ≤ D, ưu tiên dòng riêng của cơ sở C; nếu cơ sở C không có dòng riêng nào ≤ D thì dùng dòng "cả hai cơ sở" | — |
| `BR-PRC-007` | Nhà cung cấp ngừng | KHI nhà cung cấp `INACTIVE` THÌ không nhập được giá mới cho nhà cung cấp đó; giá cũ vẫn dùng để tính | — |
| `BR-PRC-008` | Ngưỡng giá cũ | Giá tham chiếu bị coi là cũ khi (hôm nay − ngày hiệu lực) > `GIA_NHAP_CU_TUOI_NGAY` với nguyên liệu tươi, > `GIA_NHAP_CU_KHO_NGAY` với nguyên liệu khô và đông lạnh | `BR-COST-005`; con số chờ DL-01 |
| `BR-PRC-009` | Ngưỡng lệch bất thường | Giá mới lệch quá `GIA_NHAP_LECH_CANH_BAO_PCT` % (mặc định 30) so với giá tham chiếu liền trước cùng cơ sở thì hỏi xác nhận | Nguyên liệu chưa có giá trước đó |
| `BR-CALC-001` | Công thức và giá theo ngày tính | Cost tại ngày D dùng công thức hiệu lực tại D (`BR-CAT-014`) và giá tham chiếu tại D (`BR-PRC-006`) | Thực đơn đã gửi duyệt dùng công thức đã gắn vào ô, không lấy lại |
| `BR-CALC-002` | Nguyên liệu tính vào cost | Chỉ cộng các dòng công thức có nguyên liệu mang cờ "tính vào cost" | Danh sách nguyên liệu không tính: [O-01] |
| `BR-CALC-003` | Không tính thiếu | KHI một nguyên liệu cần tính không có giá tham chiếu THÌ không trả cost của món, của ngày và của mọi tổng chứa nó; trả danh sách thiếu | — |
| `BR-CALC-004` | Cost phần món chính | Theo tham số `COST_MON_CHINH_CACH_TINH`: `DAT_NHAT` = cost lớn nhất trong các món chính của ngày × số món chính được chọn; `BINH_QUAN` = trung bình cộng cost các món chính × số món chính được chọn; `MAC_DINH` = cost của món mặc định × số món chính được chọn | [E3-Q1]. Giá trị `THEO_TY_LE` (theo lựa chọn thật) để dành cho sau R6 |
| `BR-CALC-005` | Doanh thu chưa VAT | Doanh thu chưa VAT của suất = ngưỡng giá của loại suất ÷ (1 + `VAT_PCT` ÷ 100) | [O-01]; `BR-COST-002`. Khi `VAT_PCT` chưa được đặt thì không tính được cost %: `ERR-COST-422-05` |
| `BR-CALC-006` | Làm tròn | Phép tính trung gian không làm tròn. Cost món và cost suất hiển thị làm tròn đến đồng (nửa lên). Cost % làm tròn 2 chữ số thập phân (nửa lên). **So với ngưỡng bằng giá trị cost % đã làm tròn**: đạt khi ≤ ngưỡng | — |
| `BR-CALC-007` | Bảng tính cost món đặc thù | KHI món có cờ "đặc thù" THÌ chỉ được coi là đủ điều kiện vào thực đơn khi có ít nhất một bảng tính cost `APPROVED` lập trong vòng `COST_BANG_TINH_HIEU_LUC_NGAY` ngày (mặc định 90) tính đến ngày phục vụ | `BR-COST-007` |
| `BR-CALC-008` | Khoản khoán | Số tiền là số nguyên đồng ≥ 0; có ngày hiệu lực; khoản áp dụng cho một loại suất ưu tiên hơn khoản áp dụng cho mọi loại suất cùng tên | — |
| `BR-CALC-009` | Cơ sở dùng để kiểm ngưỡng | Thực đơn dùng chung cho cả hai cơ sở được kiểm theo **từng cơ sở**; một ngày đạt khi đạt ở mọi cơ sở có giá. Cơ sở không có giá riêng dùng giá chung | [E3-Q3] |
| `BR-CALC-010` | Bản chụp là bất biến | Bản chụp lúc duyệt và bảng dự toán đã lưu không bị sửa bởi thay đổi giá, công thức, tham số về sau | — |
| `BR-CALC-011` | Kết quả ngân sách cho agent phía khách | `DAT` khi mọi ngày của thực đơn đạt ở mọi cơ sở; `KHONG_DAT` khi có ít nhất một ngày vượt; `KHONG_XAC_DINH` khi không tính được | — |
| `BR-EST-001` | Số suất | Số suất mỗi món chính là số nguyên ≥ 0; tổng > 0. Số suất món phụ, rau, canh = tổng số suất các món chính ÷ số món chính được chọn | — |
| `BR-EST-002` | Lượng cần mua | Tổng định lượng theo đơn vị dùng = Σ (định lượng chuẩn × số suất của món). Lượng cần mua = tổng định lượng ÷ hệ số quy đổi; nếu `COST_AP_HAO_HUT` = `CO` thì chia thêm cho (1 − hao hụt % ÷ 100). Làm tròn lên 2 chữ số thập phân của đơn vị mua | [E3-Q2] |
| `BR-EST-003` | Gộp theo nguyên liệu | Một nguyên liệu dùng ở nhiều món, nhiều ngày được gộp thành một dòng ở bảng tuần, giữ được phân rã theo món và ngày | — |
| `BR-EST-004` | Dự toán là bản chụp | Mỗi bản dự toán lưu giá và công thức tại thời điểm lập; lập lại tạo bản mới | — |

### 3.3 Cách tính

#### 3.3.1 Cost món

```text
Đầu vào: món M, cỡ định lượng, ngày tính D, cơ sở C
R        = công thức hiệu lực của M tại D
Với mỗi dòng i của R có nguyên liệu tính vào cost:
  p_i    = giá tham chiếu của nguyên liệu i tại (C, D)            # đồng / đơn vị mua
  u_i    = p_i ÷ hệ số quy đổi của nguyên liệu i                  # đồng / đơn vị dùng
  q_i    = định lượng chuẩn của dòng i                            # đơn vị dùng
  nếu COST_AP_HAO_HUT = CO và nguyên liệu i có hao hụt h_i %:
    q_i  = q_i ÷ (1 − h_i ÷ 100)
  c_i    = q_i × u_i
Cost món = Σ c_i
Tỷ trọng dòng i = c_i ÷ Cost món × 100
```

Ví dụ minh họa (số giả định, không phải giá của Gia Phát): thịt lợn 70 g, giá 120.000 đồng/kg, hệ số 1000 → 70 × 120 = 8.400 đồng; trứng cút 3 quả, giá 800 đồng/quả, hệ số 1 → 2.400 đồng; cost món = 10.800 đồng.

#### 3.3.2 Cost suất và cost % của một ngày

```text
Đầu vào: ngày D của thực đơn thuộc loại suất S, cơ sở C
K        = số món chính được chọn của S (mặc định 1)
A        = cost phần món chính theo BR-CALC-004
B        = Σ cost các món phụ + cost rau + cost canh của ngày D
E        = Σ các khoản khoán hiệu lực tại D áp dụng cho S
Cost suất        = A + B + E
Doanh thu chưa VAT = ngưỡng giá của S ÷ (1 + VAT_PCT ÷ 100)
Cost %           = làm tròn 2 chữ số (Cost suất ÷ Doanh thu chưa VAT × 100)
Đạt              khi Cost % ≤ COST_NGUONG_PCT hiệu lực tại D
Còn dư / vượt    = COST_NGUONG_PCT ÷ 100 × Doanh thu chưa VAT − Cost suất
```

Mẫu số là **ngưỡng giá của loại suất**, không phải tổng giá bán các món người ăn chọn, vì công ty trả theo định mức [D-21]. Điều này phụ thuộc cách trả lời [E2-Q1] của epic thực đơn; nếu doanh thu thật của một suất là tổng giá các món đã chọn thì mẫu số phải đổi.

Ví dụ minh họa: loại suất 40.000 đồng, `VAT_PCT` = 8 → doanh thu chưa VAT = 37.037,04 đồng; ngưỡng 52% → cost suất tối đa 19.259 đồng. Nếu A = 10.800, B = 6.500, E = 1.500 → cost suất = 18.800 → cost % = 50,76 → đạt, còn dư 459 đồng.

#### 3.3.3 Quy tắc cost trong bộ kiểm

| Mã | Phạm vi | Loại (chờ DL-01) | Không đạt khi… |
| :--- | :---: | :--- | :--- |
| `BR-COST-001` | Ngày | Cứng khi `COST_CHE_DO_KIEM` = `CHAN`; mềm khi `CANH_BAO` | Cost % của ngày > ngưỡng ở ít nhất một cơ sở |
| `BR-COST-005` | Ngày | Mềm | Có nguyên liệu của ngày dùng giá tham chiếu bị coi là cũ (`BR-PRC-008`) |
| `BR-COST-006` | Ngày | Mềm | Định nghĩa "cao", "thấp": [E3-Q7]. Phương án đề xuất của bảng quy tắc: có món chính nhóm cost cao **và** món phụ nhóm cost cao trong cùng ngày |
| `BR-COST-007` | Ngày | Cứng | Có món đặc thù không thoả `BR-CALC-007` |

`BR-COST-008`, `009`, `010`, `012` đã hiện thực ở E2. `BR-COST-002`, `003`, `004` là định nghĩa cách tính (mục 3.3.1, 3.3.2). `BR-COST-011` là `FR-COST-ALR-001`, `002`.

#### 3.3.4 Bảng dự toán

```text
Đầu vào: ngày D, cơ sở C, số suất n_m cho từng món chính m; N = Σ n_m ÷ K
Số suất của món: món chính m → n_m; món phụ, rau, canh → N
Với mỗi (món, dòng công thức i):
  định lượng/suất = q_i                      (đã gồm hao hụt nếu COST_AP_HAO_HUT = CO — xem ghi chú)
  tổng định lượng = q_i × số suất của món
Gộp theo nguyên liệu:
  tổng định lượng nguyên liệu = Σ qua các món
  lượng cần mua  = làm tròn lên 2 chữ số (tổng định lượng ÷ hệ số quy đổi)      # BR-EST-002
  thành tiền     = lượng cần mua × giá tham chiếu
Tổng chi phí     = Σ thành tiền + Σ khoản khoán × N
Doanh thu chưa VAT = N × ngưỡng giá ÷ (1 + VAT_PCT ÷ 100)
Cost % dự toán   = Tổng chi phí ÷ Doanh thu chưa VAT × 100
```

Cost % của bảng dự toán dùng **số suất thật theo từng món chính**, nên có thể khác cost % ở mục 3.3.2 (vốn tính theo `COST_MON_CHINH_CACH_TINH`). Bảng dự toán hiện cả hai con số và ghi rõ cách tính của từng số.

Ghi chú hao hụt: khi `COST_AP_HAO_HUT` = `CO`, hao hụt được áp một lần, ở bước tính `q_i`; không áp lần nữa ở bước lượng cần mua.

### 3.4 Yêu cầu phi chức năng riêng của epic

| Mã NFR | Yêu cầu | Cách kiểm |
| :--- | :--- | :--- |
| `NFR-COST-001` | Cost % của một thực đơn 6 ngày × 7 món tính trong p95 ≤ 1 giây, để tổng thời gian cùng bộ kiểm quy tắc không vượt 2 giây của `NFR-MENU-001` | Đo 50 lần |
| `NFR-COST-002` | Kết quả tính là xác định và khớp bảng tính tay: với bộ 10 món và 10 ngày mẫu của kế toán, lệch không quá 1 đồng ở cost món và 0,01 điểm phần trăm ở cost % | So sánh tự động |
| `NFR-COST-003` | Lưu lưới 200 dòng giá trong ≤ 3 giây | Đo |
| `NFR-COST-004` | `FR-COST-ALR-001` hoàn tất trong ≤ 5 phút với 50 thực đơn đang hiệu lực và 100 giá đổi cùng lúc | Kiểm thử tải |
| `NFR-COST-005` | Không phản hồi API nào gửi tới tài khoản không có `cost.price.read` hoặc `cost.cost.read` chứa trường giá nhập, cost, cost % | Rà toàn bộ API của MENU và COST bằng 4 tài khoản thiếu quyền |
| `NFR-COST-006` | Tài khoản MySQL của agent phía khách không có quyền `SELECT` trên `suppliers`, `ingredient_prices`, `cost_estimates`, `cost_estimate_lines` và các bảng mới của epic | Kiểm quyền cơ sở dữ liệu |
| `NFR-COST-007` | Log ứng dụng của `FR-COST-RUL-003` không ghi cost hay cost % | Rà log |
| `NFR-COST-008` | Không dùng số thực dấu phẩy động cho tiền và định lượng | Rà mã; ca kiểm 0,1 + 0,2 |

### 3.5 Ma trận lỗi

| Mã ERR | HTTP | Điều kiện phát sinh | Khoá bản địa hoá | Thông báo hiển thị | Mức | Hành động tiếp theo |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `ERR-COST-404-01` | 404 | Nguyên liệu hoặc nhà cung cấp không tồn tại hoặc không còn dùng | `cost.ref_not_found` | "Không tìm thấy nguyên liệu hoặc nhà cung cấp." | Medium | Chọn lại |
| `ERR-COST-404-02` | 404 | Không có giá tham chiếu cho nguyên liệu tại cơ sở và ngày yêu cầu | `cost.price_not_found` | "Nguyên liệu {tên} chưa có giá nhập cho ngày {ngày}." | High | Nhập giá |
| `ERR-COST-409-01` | 409 | Tên nhà cung cấp trùng | `cost.supplier_duplicate` | "Nhà cung cấp này đã tồn tại." | Medium | Dùng bản ghi có sẵn |
| `ERR-COST-409-02` | 409 | Đã có giá cho cùng nguyên liệu, nhà cung cấp, cơ sở, ngày hiệu lực | `cost.price_exists` | "Đã có giá của nhà cung cấp này cho ngày hiệu lực đã chọn." | Medium | Đổi ngày hiệu lực |
| `ERR-COST-409-03` | 409 | Sửa hoặc huỷ giá đã hiệu lực | `cost.price_immutable` | "Giá đã hiệu lực không sửa hoặc huỷ được. Hãy nhập giá mới." | Medium | Nhập dòng mới |
| `ERR-COST-422-01` | 422 | Giá không phải số nguyên > 0 | `cost.price_invalid` | "Giá nhập phải là số nguyên lớn hơn 0." | Medium | Sửa giá |
| `ERR-COST-422-02` | 422 | Ngày hiệu lực ngoài khoảng cho phép (`BR-PRC-003`) hoặc nhà cung cấp đã ngừng | `cost.price_date_invalid` | "Ngày hiệu lực không hợp lệ, hoặc nhà cung cấp đã ngừng." | Medium | Sửa ngày hoặc nhà cung cấp |
| `ERR-COST-422-03` | 422 | Không tính được cost vì thiếu giá của ít nhất một nguyên liệu | `cost.missing_price` | "Chưa tính được cost vì thiếu giá: {danh sách nguyên liệu}." | High | Nhập giá còn thiếu |
| `ERR-COST-422-04` | 422 | Món đặc thù chưa có bảng tính cost đã duyệt còn hiệu lực; hoặc lập bảng tính cho món không có cờ đặc thù | `cost.sheet_required` | "Món {tên} cần bảng tính cost được duyệt trước khi vào thực đơn." | High | Lập và gửi duyệt bảng tính |
| `ERR-COST-422-05` | 422 | Chưa đặt `VAT_PCT`, hoặc doanh thu chưa VAT bằng 0 | `cost.vat_not_set` | "Chưa cấu hình thuế suất VAT nên chưa tính được cost %." | Critical | Người có quyền đặt tham số |
| `ERR-COST-422-06` | 422 | Khoản khoán có số tiền âm, không phải số nguyên, hoặc thiếu ngày hiệu lực | `cost.allowance_invalid` | "Khoản khoán không hợp lệ." | Medium | Sửa |
| `ERR-COST-422-07` | 422 | Gửi duyệt thực đơn có ngày vượt ngưỡng khi `COST_CHE_DO_KIEM` = `CHAN` | `cost.over_threshold` | "Thực đơn có {n} ngày vượt ngưỡng cost: {ngày và cost %}." | High | Đổi món hoặc định lượng |
| `ERR-COST-422-08` | 422 | Số suất âm, không phải số nguyên, hoặc tổng bằng 0 | `cost.servings_invalid` | "Số suất không hợp lệ." | Medium | Sửa số suất |
| `ERR-COST-429-01` | 429 | Vượt giới hạn gọi dịch vụ ngân sách trong một phiên | `cost.budget_rate_limited` | (không hiện cho người dùng cuối; agent trả lời rằng cần gửi thực đơn cho Gia Phát xem) | Low | — |

Người không có `cost.cost.read` nhận `ERR-COST-422-07` với thông báo rút gọn "Thực đơn có {n} ngày vượt ngân sách", không có cost %.

---

## 4. Phụ lục

### 4.1 Ma trận truy vết

| Tính năng PRD | Năng lực (epic-spec) | FR |
| :--- | :--- | :--- |
| `FEAT-014` | `CAP-SUP-01` | `FR-COST-SUP-001` → `003` |
| `FEAT-014` | `CAP-PRC-01` → `10` | `FR-COST-PRC-001` → `011` |
| `FEAT-015` | `CAP-DISH-01` → `07` | `FR-COST-DISH-001` → `008` |
| `FEAT-016` | `CAP-MEAL-01` → `08` | `FR-COST-MEAL-001` → `008` |
| `FEAT-016` | `CAP-RUL-01` → `03` | `FR-COST-RUL-001` → `003` |
| `FEAT-017` | `CAP-EST-01` → `07` | `FR-COST-EST-001` → `007` |
| `FEAT-018` | `CAP-ALR-01` → `05` | `FR-COST-ALR-001` → `005` |

`CAP-PRC-10` (duyệt giá nhập) không có FR: chờ [E3-Q6]. `FR-COST-MEAL-008` (chế độ chỉ cảnh báo) đã đồng bộ về `CAP-MEAL-08` trong epic-spec v0.2.0; phương án vẫn là đề xuất cho giai đoạn chạy thử.

### 4.2 Tham số của phân hệ

Bổ sung vào danh mục tham số của SRS nền tảng (phụ lục 4.3).

| Mã tham số | Ý nghĩa | Mặc định | Cần duyệt | Nguồn |
| :--- | :--- | :--- | :---: | :--- |
| `COST_NGUONG_PCT` | Ngưỡng cost % | 52 | Có | Docx [D-08] (đã có ở nền tảng) |
| `VAT_PCT` | Thuế suất VAT của suất ăn | Chưa có | Có | [O-01] (đã có ở nền tảng) |
| `COST_MON_CHINH_CACH_TINH` | Cách tính cost phần món chính | `DAT_NHAT` | Có | [E3-Q1] |
| `COST_AP_HAO_HUT` | Có nhân hao hụt vào định lượng khi tính cost và lượng mua | `KHONG` | Có | [E3-Q2] |
| `COST_CHE_DO_KIEM` | `CANH_BAO` hoặc `CHAN` | `CANH_BAO` | Có | Rủi ro E3-R4 |
| `COST_BANG_TINH_HIEU_LUC_NGAY` | Số ngày bảng tính cost món đặc thù còn hiệu lực | 90 | Không | [ĐỀ XUẤT] |
| `GIA_NHAP_CU_TUOI_NGAY` | Ngưỡng giá cũ, hàng tươi | 7 | Không | `BR-COST-005` (đã có ở nền tảng) |
| `GIA_NHAP_CU_KHO_NGAY` | Ngưỡng giá cũ, hàng khô và đông lạnh | 30 | Không | `BR-COST-005` (đã có ở nền tảng) |
| `GIA_NHAP_HOI_TO_NGAY` | Số ngày được nhập giá hồi tố | 7 | Không | [ĐỀ XUẤT] |
| `GIA_NHAP_LECH_CANH_BAO_PCT` | Mức lệch giá cần hỏi xác nhận | 30 | Không | [ĐỀ XUẤT] |

### 4.3 Thay đổi cần cập nhật ở tài liệu khác

**Đã đồng bộ 9/9 mục ở mức tài liệu ngày 11/11/2026**; chưa triển khai database hay nghiệm thu nghiệp vụ. [ERD v0.3.0, mục 5.4](../../nen-tang/srs/erd.md) và [DBML v0.3.0](../../nen-tang/srs/schema.dbml) mô tả bảng/cột/ràng buộc. [SRS nền tảng v0.2.0](../../nen-tang/srs/spec.md), [SRS thực đơn v0.3.1](../../thuc-don-dinh-luong/srs/spec.md) và [wireframe v0.2.0](../../thuc-don-dinh-luong/html-wireframe/soan-thuc-don-tuan.html) đã cập nhật. Nội dung bên dưới là danh sách thay đổi đã thực hiện.

| Tài liệu | Cần bổ sung |
| :--- | :--- |
| ERD, `schema.dbml` | Bảng bảng tính cost món đặc thù (món, ngày tính, cơ sở, các dòng đã chụp, trạng thái); dùng `approvals` cho phần duyệt |
| ERD, `schema.dbml` | Bảng khoản khoán (tên, số tiền, loại suất, ngày hiệu lực); dùng `cost_allowances`, duyệt qua `approvals` |
| ERD, `schema.dbml` | Bảng bản chụp cost lúc duyệt theo (thực đơn, ngày, cơ sở) và các dòng giá đã dùng. đã bỏ `menu_days.cost_pct`, thay bằng `menu_cost_snapshots` theo ngày/cơ sở/vòng duyệt |
| ERD, `schema.dbml` | Bảng cảnh báo cost (thực đơn, ngày, cơ sở, cost % cũ → mới, trạng thái) và bảng kết quả tính lại |
| ERD, `schema.dbml` | `cost_estimates` thêm số thứ tự bản, số suất theo từng món chính, giá trị tham số cách tính |
| ERD | Mục 5.3: thay công thức bằng tham chiếu tới mục 3.3 của tài liệu này |
| SRS nền tảng | Phụ lục 4.3: thêm 6 tham số mới ở mục 4.2 |
| SRS epic thực đơn | `FR-MENU-RUL-001`: bảng kiểm cần ẩn con số của quy tắc cost theo quyền (`FR-COST-RUL-002`) |
| Wireframe soạn thực đơn | Thêm dòng cost % dưới mỗi cột ngày |

### 4.4 Điểm mở

Giữ nguyên trạng thái mở.

| Mã | Điểm mở | Ai trả lời | Cách SRS đang xử lý | FR / BR bị ảnh hưởng |
| :--- | :--- | :--- | :--- | :--- |
| O-01 | Thành phần cost; khoản khoán; VAT; giá nhập có gồm VAT đầu vào | Kế toán | Cờ "tính vào cost" từng nguyên liệu + khoản khoán + `VAT_PCT`; Cost gồm VAT phải trả theo ACC-CONF-02; giá báo chưa VAT cần chuẩn hóa trước khi tính, xem bổ sung kế toán | `BR-CALC-002`, `005`, `008`; `FR-COST-MEAL-004` |
| E3-Q1 | Cost phần món chính | Giám đốc, kế toán | Tham số, mặc định `DAT_NHAT` | `BR-CALC-004` |
| E3-Q2 | Định lượng sống đã gồm xương, vỏ chưa | Người soạn docx, bếp trưởng | Tham số, mặc định `KHONG` | Mục 3.3.1; `BR-EST-002` |
| E3-Q3 | Hai cơ sở mua giá khác nhau; kiểm ngưỡng theo cơ sở nào | Kế toán | Kiểm theo từng cơ sở, phải đạt ở mọi cơ sở | `BR-CALC-009`, `BR-PRC-006` |
| E3-Q4 | Giá nào là giá tham chiếu | Kế toán | Kế toán đánh dấu | `FR-COST-PRC-002`, `BR-PRC-005` |
| E3-Q5 | Tần suất cập nhật giá thực tế | Kế toán | Ngưỡng giá cũ là tham số | `BR-PRC-008` |
| E3-Q6 | Giá nhập có cần duyệt | Giám đốc | Không có bước duyệt; chỉ hỏi xác nhận khi lệch bất thường | `FR-COST-PRC-010` |
| E3-Q7 | Định nghĩa cost cao / thấp | Người soạn docx | Dùng nhóm cost gắn tay ở E2 | `BR-COST-006`, `FR-COST-DISH-008` |
| E3-Q8 | Nguồn số suất trước khi có order | Dinh dưỡng viên | Nhập tay theo từng món chính | `FR-COST-EST-002` |
| E3-Q9 | Vượt ngưỡng: chặn tuyệt đối hay cho ngoại lệ | Giám đốc | Chặn tuyệt đối khi ở chế độ `CHAN`; có chế độ `CANH_BAO` | `FR-COST-MEAL-007`, `008` |
| E3-Q10 | Chặn chuyển bếp | Giám đốc | Chưa hiện thực | `FR-COST-ALR-004` |
| E3-Q11 | Bếp trưởng có xem giá và cost | Giám đốc | Không; chỉ xem dự toán dạng số lượng | Mục 2.2 |
| E2-Q1 | Giá món dùng để làm gì khi công ty đã đặt định mức | Dinh dưỡng viên, Giám đốc | Mẫu số của cost % là ngưỡng giá loại suất | Mục 3.3.2 |
| DL-01 | Loại và con số của các quy tắc cost | Người soạn docx, kế toán | Loại ghi "chờ DL-01" | Mục 3.3.3 |
| E3-Q12 | Khi tính `BINH_QUAN` hoặc `DAT_NHAT`, món chính Healthy (thường rẻ hơn) có được tính vào không | Giám đốc | Có, tính mọi món chính của ngày | `BR-CALC-004` |
| E3-Q13 | Cho nhập giá hồi tố tối đa mấy ngày; giá hồi tố có làm tính lại các bản chụp không | Kế toán | 7 ngày; không tính lại bản chụp, chỉ ảnh hưởng lần tính sau | `BR-PRC-003`, `BR-CALC-010` |


### 4.5 Điểm cần xác nhận phát hiện khi đồng bộ mô hình

Đây là điểm mở, không coi là quyết định của Gia Phát:

| Mã | Vấn đề | Xử lý trong bản thiết kế | Người xác nhận |
| :--- | :--- | :--- | :--- |
| E3-Q14 | FR-COST-PRC-002 cho đổi cờ tham chiếu nhưng BR-PRC-004 cấm sửa giá đã hiệu lực; có được đổi riêng cờ không? | Chưa cho phép thay đổi hồi tố cờ trên giá đã hiệu lực; snapshot cũ giữ bất biến. Cần quyết định trước khi triển khai thao tác này | Kế toán |
| E3-Q15 | Ngày dùng nhiều món chính: FR-COST-EST-002 gọi tổng lượt chọn là tổng suất, nhưng BR-EST-001 yêu cầu chia main_pick | Mô hình theo BR-EST-001; tổng lượt chọn phải chia hết cho main_pick. MVP main_pick=1 không bị ảnh hưởng; cần chốt trước khi mở main_pick>1 | Dinh dưỡng viên |
| E3-Q16 | Món đặc thù có bảng tính ở cơ sở A có hợp lệ cho cơ sở B không; mốc 90 ngày tính theo ngày lập hay ngày tính giá? | Lưu cả cơ sở, ngày tính và thời điểm lập, chưa suy ra quyền dùng chéo cơ sở. Cần xác nhận bộ lọc hiệu lực trước triển khai | Giám đốc, kế toán |

ERD dùng một cảnh báo đầu mục/ngày với nhiều chi tiết cơ sở để giữ đúng FR-COST-ALR-002. Các lựa chọn kỹ thuật về lưu số decimal, JSON snapshot và khoá duy nhất được ghi là đề xuất ở ERD mục 5.4.

### 4.6 Diễn giải use case và user flow

Đã có [16 use case và ma trận 45 FR](usecase-diagram.md), cùng [user flow](../ui/user-flow.md) gồm 18 màn đề xuất, 7 luồng chính và trạng thái lỗi/offline. Có 43 FR được diễn giải bằng luồng; `FR-COST-MEAL-007` và `FR-COST-ALR-004` vẫn hoãn theo E3-Q9/Q10. P1/P2 không được nâng thành P0.

User flow ghi nhận 10 câu hỏi FLOW-COST-Q01 → Q10. Đây là khoảng trống cần review, không phải thay đổi đã duyệt của SRS; đặc biệt cần chốt xử lý giá đổi trong thời gian PENDING, giao dịch dự toán tuần và quyền đọc khoản khoán trước khi hoàn thiện API. Không đổi trạng thái các điểm mở tại 4.4–4.5.

## Phụ lục — Thiết kế API và giao diện

[API v0.1.0](../api/api-spec.md): 37 endpoint đề xuất, truy vết 45 FR qua API, hook nội bộ hoặc hoãn. [Wireframe 18 màn](../html-wireframe/cost-workbench.html) dùng dữ liệu giả; [hướng dẫn và giới hạn](../html-wireframe/README.md). Mã lỗi kỹ thuật bổ sung, concurrency token và outbox trong API còn là đề xuất triển khai; chưa bổ sung vào schema hiện tại. [Báo cáo kiểm tra](../validation/api-wireframe-report.md).

## Phụ lục — Backlog và kiểm thử

[28 user story](../userstories/backlog.md) · [108 AC](../userstories/acceptance-criteria.md) · [Checklist](../test/checklist.md) · [Test case](../test/test-cases.md) · [RTM](../test/traceability.md). Đây là kịch bản đã viết, chưa chạy backend. Hai FR hoãn vẫn chưa có story/test thực thi.

**QA-COST-Q01:** mã ERR-COST-404-01 và ERR-COST-422-02 cùng bao hàm NCC đã ngừng; BA/Tech lead cần thống nhất mã phản hồi. Không đổi hành vi cấm nhập giá mới. Chi tiết và ca bị chặn: [báo cáo backlog](../validation/backlog-report.md).

## Bổ sung nghiệp vụ kế toán theo xác nhận ngày11/11/2026

Nguồn và quy tắc: [nghiệp vụ kế toán](../accounting/business-rules.md), [CR-COST-2026-001](../cr/CR-COST-2026-001.md), [hướng dẫn thao tác](../user-guide.md), [12 ca bổ sung](../accounting/acceptance.md).

Thông tin mới ưu tiên hơn giả định “giá nhập dùng nguyên như nhập”: giá dùng tính cost phải gồm VAT thực tế phải trả NCC. Giá báo đã gồm VAT giữ nguyên, giá chưa gồm cần chuẩn hóa; chưa biết số cuối thì không tự mặc định VAT0. O-01 được xác nhận một phần, chưa đóng toàn bộ.

Khách không lấy VAT nghĩa là không yêu cầu hóa đơn; cờ này độc lập với thuế suất/cách ghi giá. Chiết khấu cho khách theo% hoặc tiền cố định/suất, ghi khoản riêng theo đơn; khách vẫn trả đủ đơn giá suất, không tự giảm tiền phải trả. Không cộng khoản chiết khấu này vào cost nguyên liệu hoặc trừ mẫu số kiểm52% khi chưa có quyết định chỉ số.

Công thức3.3.2 dùng giá suất đã gồm VAT vẫn áp dụng cho fixture đúng giả định đó, chưa là hợp đồng hoàn chỉnh cho mọi thỏa thuận khách. Phần triển khai theo đơn phụ thuộc E6/R6 và xử lý thanh toán liên quan; không coi việc có phụ lục là đã bổ sung các FR triển khai vào45 FR R3. API v0.2.0, DBML v0.4.0 và4 màn kế toán đã có thiết kế bổ sung; các nhánh CK còn gate, chưa là chức năng đã triển khai.

## Liên kết baseline thiết kế kế toán và nhánh mở

[API bổ sung](../api/accounting-contract.md), [6 FR/story mở rộng](../userstories/accounting-backlog.md), [18 ca thiết kế](../accounting/design-tests.md), [4 màn](../html-wireframe/accounting-workbench.html), [phương án4 nhóm nhánh](../review/cost-branch-decisions.md). Các đề xuất nhánh chưa thay quyết định E3-Q16/Q05/Q06/Q07. Dữ liệu thực tế được người dùng xác nhận chưa có; [câu hỏi dữ liệu](../review/accountant-input.md) thay cho kết quả nghiệm thu giả.

Làm rõ BR-PRC-002 trong extension: giá nhập nguyên đồng là `price_vnd` cuối sau chuẩn hóa. Giá báo nguồn là Decimal riêng, chưa dùng thẳng tính cost. Gross phần lẻ chưa có chính sách làm tròn thì không ghi; lỗi normalization và mapping ca cũ xem [API kế toán](../api/accounting-contract.md).

## Phụ thuộc E4/E5 — bản thiết kế ngày 11/11/2026

[Dinh dưỡng](../../dinh-duong/srs/spec.md) đọc recipe_items.qty_std và nguồn dinh dưỡng; không dùng COST_AP_HAO_HUT để đổi công thức. [Agent Nội bộ](../../agent-noi-bo/api/api-spec.md) gọi FR-MENU-RUL-002 và API-COST-025 với cùng candidate/version; apply chỉ tạo DRAFT, không tự duyệt/công bố. Adapter MENU và tính nguyên tử chờ AIO-Q06. Đề xuất chỉ trả candidate VALID khi cost không vượt kể cả CANH_BAO (AIO-Q02 còn mở); cổng MENU hiện hành vẫn giữ nguyên. Chưa có API/worker/backend triển khai trong gói này.

## Hồ sơ bổ sung để review — 11/11/2026

[Preview toàn hồ sơ](../preview.html) · [API](../api/api-spec.md) · [Luồng tuần tự](flows.md) · [Trạng thái](states.md) · [Gap](../gap-analysis.md). Gói bổ sung không tự đóng câu hỏi, thay quy tắc nghiệp vụ hoặc chứng minh backend đã triển khai. [Bàn giao](../../gia-phat/review/ba-completion-handoff.md).

## Liên kết phụ thuộc E6 — bổ sung 11/11/2026

[Gói E6 để review](../../chon-mon-order/preview.html) · [Hợp đồng phụ thuộc](../../chon-mon-order/review/dependencies.md) · [Đối chiếu schema](../../chon-mon-order/srs/data-dictionary.md). E6 giữ nguồn công bố/quyền và quy tắc của phân hệ này; delta chưa merge, không thay gate hoặc chứng minh phần mềm đã triển khai.
