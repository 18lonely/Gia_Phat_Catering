# Tài liệu Đặc tả Yêu cầu Kỹ thuật (SRS): Epic E2 · Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Epic | E2 · `thuc-don-dinh-luong`: đợt phát hành R2 (v0.2.0) |
| Phân hệ | MENU |
| Tính năng PRD | `FEAT-006` → `FEAT-013` |
| Phiên bản | 0.3.4 |
| Trạng thái | Draft: **phần 3.3 (bộ kiểm quy tắc) mới có khung và cách tính; con số từng quy tắc chờ DL-01** |
| Ngày | 2026-11-14 |
| Tiêu chuẩn | IEEE Std 830-1998 / ISO/IEC/IEEE 29148 |

### Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.3.4 | 2026-11-14 | BA | Đổi tên công nghệ backend sang Rust/Axum theo D-22, CR-CORE-2026-001; không đổi FR, BR |
| 0.3.3 | 2026-11-11 | BA | Liên kết hồ sơ bổ sung E1–E5/E6 khởi đầu; giữ quy tắc và điểm mở |
| 0.3.2 | 2026-11-11 | BA | Liên kết hợp đồng E4/E5; giữ nguyên FR và cổng duyệt/Cost |
| 0.3.1 | 2026-11-11 | BA | Đồng bộ quyền xem kết quả cost và điểm tích hợp Cost R3; không chốt các điểm mở. |
| 0.1.0 | 2026-11-10 | BA | Khởi tạo từ epic-spec v0.1.0 |
| 0.2.0 | 2026-11-10 | BA | Đưa vào 10 điểm phát sinh khi viết tiêu chí nghiệm thu: thêm `BR-CAT-020`, `BR-MNU-010`, `ERR-MENU-409-10`; làm rõ `FR-MENU-DISH-005`, `DISH-007`, `PRC-002`, `MNU-005`, `MNU-006`, `MNU-008`, `APV-001`, `BR-MNU-008`, mục 3.3.1. Chi tiết ở mục 4.4 |
| 0.3.0 | 2026-11-11 | BA | Đưa vào 11 chỗ chưa quy định phát hiện khi viết test case: thêm `BR-CAT-021`, `022`, `023`, `ERR-MENU-422-21`; mở rộng `BR-CAT-017`, `BR-MNU-007`; làm rõ `FR-MENU-RCP-001`, `FR-MENU-IMP-002`. Phân trang ngoài khoảng xử lý ở SRS nền tảng v0.1.1. Chi tiết ở mục 4.4 |

Quy ước: **[D-xx]** đã chốt · **[ĐỀ XUẤT]** chờ duyệt · **[O-xx] / [H-x] / [E2-Qx]** điểm mở, giữ nguyên trạng thái mở. Con số không ghi nguồn là [ĐỀ XUẤT].

---

## 1. Giới thiệu

### 1.1 Mục đích

Đặc tả hành vi của phân hệ MENU trong đợt R2: danh mục nguyên liệu và món, công thức có phiên bản, giá bán món, loại suất, thực đơn tuần, bộ kiểm quy tắc, duyệt và công bố, nhập dữ liệu từ bảng tính.

### 1.2 Phạm vi

Theo mục 1.4 của [epic-spec](../epic-spec.md). Không gồm: giá nhập và cost (E3), dinh dưỡng (E4), agent (E5), thực đơn riêng theo khách và hiển thị cho khách (E6).

### 1.3 Thuật ngữ

| Thuật ngữ | Nghĩa |
| :--- | :--- |
| Vai trò món | Món chính, món phụ, rau, canh |
| Nhóm nguyên liệu chính | Nhóm dùng để so trùng giữa các món: lợn, gà, bò, cá… |
| Món gốc | Món mà các biến thể đổi tên hoặc trình bày quy về, để đếm lặp |
| Định lượng sống | Khối lượng nguyên liệu trước chế biến cho 1 suất, theo docx |
| Loại suất | Cấu hình một suất: ngưỡng giá, số món chính đưa ra, số món phụ, có rau, có canh |
| Món mặc định | Món chính gán cho người không chọn trước hạn chốt [D-14] |
| Quy tắc cứng / mềm | Vi phạm quy tắc cứng thì chặn; vi phạm quy tắc mềm thì cảnh báo và trừ điểm |
| Điểm quy tắc | 100 trừ tổng điểm phạt của các quy tắc mềm không đạt; sàn là 0 |

### 1.4 Tài liệu tham chiếu

[Epic-spec](../epic-spec.md) · [Bảng quy tắc thực đơn](../../gia-phat/brainstorms/quy-tac-thuc-don.md) · [SRS nền tảng](../../nen-tang/srs/spec.md) · [ERD](../../nen-tang/srs/erd.md) · [schema.dbml](../../nen-tang/srs/schema.dbml) · `Yêu cầu về thực đơn và cost tp.docx`

---

## 2. Mô tả tổng quan

### 2.1 Bối cảnh

MENU là một module (crate) trong API Rust/Axum [D-22, [CR-CORE-2026-001](../../nen-tang/cr/CR-CORE-2026-001.md)]. Nó dùng AUTH và SYS của nền tảng (phân quyền, nhật ký, tham số, thông báo, tệp) và cung cấp cho các module sau ba dịch vụ nội bộ:

| Dịch vụ | Dùng bởi | Nội dung |
| :--- | :--- | :--- |
| Tra cứu món và công thức đã duyệt | E3, E4, E5, E6, E9 | Chỉ trả bản ghi `ACTIVE` |
| Kiểm quy tắc thực đơn | E5, E9 | Cùng bộ kiểm mà người dùng thấy trên màn hình (`CAP-RUL-09`) |
| Tra cứu thực đơn đã công bố | E6, E8 | Chỉ trả thực đơn `PUBLISHED` |

### 2.2 Quyền theo vai trò

| Quyền | `DINH_DUONG_VIEN` | `GIAM_DOC` | `QL_CO_SO`, `BEP_TRUONG` | `KT_MUA_HANG`, `KT_DOANH_THU` |
| :--- | :---: | :---: | :---: | :---: |
| `menu.catalog.read`: xem nguyên liệu, món, công thức | ✓ | ✓ | ✓ | ✓ |
| `menu.catalog.write`: tạo, sửa, huỷ nguyên liệu, món, công thức, loại suất | ✓ | Không | Không | Không |
| `menu.catalog.approve`: duyệt món, công thức | Không | ✓ | Không | Không |
| `menu.price.read`: xem giá bán món | ✓ | ✓ | Không | ✓ |
| `menu.price.write`: đặt giá bán | ✓ | Không | Không | Không |
| `menu.price.approve`: duyệt giá bán | Không | ✓ | Không | Không |
| `menu.menu.read`: xem thực đơn mọi trạng thái | ✓ | ✓ | Chỉ `PUBLISHED` | Chỉ `PUBLISHED` |
| `menu.menu.write`: dựng, sửa, gửi duyệt, công bố, thu hồi | ✓ | Không | Không | Không |
| `menu.menu.approve`: duyệt thực đơn | Không | ✓ | Không | Không |
| `menu.rule.write`: đề nghị sửa danh mục quy tắc | ✓ | Không | Không | Không |
| `menu.rule.approve`: duyệt sửa danh mục quy tắc | Không | ✓ | Không | Không |
| `menu.import`: nhập từ bảng tính | ✓ | Không | Không | Không |

Cột `GIAM_DOC` là người duyệt theo giả định của bản thiết kế cũ; người duyệt thật và người thay khi vắng: [O-06]. Quyền duyệt chuyển được qua `FR-AUTH-RBAC-003`.

### 2.3 Ràng buộc

- Tuân theo quy ước API, khuôn lỗi, khoá phiên bản, nhật ký của SRS nền tảng.
- Mọi lệnh tạo, sửa, huỷ, duyệt sinh bản ghi nhật ký (`FR-SYS-AUD-001`).
- Con số của quy tắc nằm trong `menu_rules.params`, không viết cứng trong mã.

### 2.4 Giả định và phụ thuộc

Theo mục 2.4 của epic-spec: R1, DL-01, DL-03 → DL-05, [O-02], [O-06].

---

## 3. Yêu cầu chi tiết

### 3.1 Yêu cầu chức năng

#### Nguyên liệu: `FEAT-006`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-ING-001` | Tạo nguyên liệu | P0 | Tạo nguyên liệu ở trạng thái `ACTIVE`. Hệ thống cấp mã. | tên, nhóm, đơn vị mua, đơn vị dùng, hệ số quy đổi, loại bảo quản, có xương/vỏ, tỷ lệ hao hụt, nguồn cung ổn định | Nguyên liệu | `BR-CAT-001`, `002`, `003` | `ERR-MENU-409-01`, `ERR-MENU-422-01`, `ERR-MENU-422-02` |
| `FR-MENU-ING-002` | Sửa nguyên liệu | P0 | Sửa mọi trường trừ mã. Sửa đơn vị dùng hoặc hệ số quy đổi bị chặn nếu nguyên liệu đang nằm trong công thức `ACTIVE`. | như trên + `version` | Nguyên liệu | `BR-CAT-004` | `ERR-MENU-409-02`, `ERR-SYS-409-02` |
| `FR-MENU-ING-003` | Ngừng dùng / huỷ nguyên liệu | P0 | Chuyển `INACTIVE` hoặc huỷ. Bị chặn nếu đang nằm trong công thức `ACTIVE`; lỗi trả kèm danh sách công thức. | mã, lý do | Trạng thái mới | `BR-CAT-005` | `ERR-SYS-409-01` |
| `FR-MENU-ING-004` | Danh sách và tìm nguyên liệu | P0 | Lọc theo tên, nhóm, loại bảo quản, trạng thái; phân trang. | bộ lọc | Danh sách | Không áp dụng | Không áp dụng |
| `FR-MENU-ING-005` | Quản lý nhóm nguyên liệu | P0 | Tạo, sửa, huỷ nhóm; mỗi nhóm khai nguồn đạm (thịt, cá, trứng, thuỷ sản, đậu, không). Danh sách khởi tạo: [H-3] | tên, nguồn đạm | Nhóm | `BR-CAT-005` | `ERR-MENU-409-01` |
| `FR-MENU-ING-006` | Khai mùa vụ | P1 | Một nguyên liệu có 0 hoặc nhiều khoảng tháng trong mùa. | mã nguyên liệu, tháng từ, tháng đến | Mùa vụ | Không áp dụng | `ERR-MENU-422-03` |

#### Món: `FEAT-007`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-DISH-001` | Tạo món | P0 | Tạo món ở trạng thái `DRAFT` với 12 thuộc tính: vai trò, nhóm nguyên liệu chính, phương pháp chế biến, món gốc, Healthy, vị chua, kết cấu, thanh nhẹ, cầu kỳ, chịu vận chuyển, phù hợp bếp lớn, nhóm cost, đặc thù. | tên, mô tả, 12 thuộc tính, chất gây dị ứng | Món `DRAFT` | `BR-CAT-006`, `007` | `ERR-MENU-409-01`, `ERR-MENU-422-04`, `ERR-MENU-422-05` |
| `FR-MENU-DISH-002` | Sửa món | P0 | `DRAFT`: sửa tự do. `ACTIVE`: sửa thuộc tính ảnh hưởng quy tắc tạo một đề nghị thay đổi chờ duyệt (`change_requests`); món vẫn `ACTIVE` với giá trị cũ và hiện nhãn "chờ duyệt thay đổi" cho đến khi đề nghị được duyệt. Mỗi món tối đa 1 đề nghị đang chờ. | như trên + `version`, lý do | Món | `BR-CAT-008`, `BR-AUD-001` | `ERR-SYS-409-02`, `ERR-SYS-422-01` |
| `FR-MENU-DISH-003` | Gửi duyệt món | P0 | `DRAFT` → `PENDING`. Điều kiện: đủ thuộc tính bắt buộc và có ít nhất 1 công thức ở trạng thái `PENDING` hoặc `ACTIVE`. | mã món | Món `PENDING` | `BR-CAT-009` | `ERR-MENU-422-06` |
| `FR-MENU-DISH-004` | Duyệt / trả lại món | P0 | Duyệt: `PENDING` → `ACTIVE`. Trả lại: → `DRAFT` kèm lý do. Duyệt được nhiều món một lần. | danh sách mã, quyết định, lý do | Trạng thái mới | `BR-SEC-008`, `BR-CAT-009` | `ERR-SYS-403-01`, `ERR-MENU-422-06` |
| `FR-MENU-DISH-005` | Ngừng dùng món | P0 | `ACTIVE` → `INACTIVE`. Bị chặn nếu món nằm trong thực đơn `PUBLISHED` có ngày phục vụ từ hôm nay trở đi. Món nằm trong thực đơn `DRAFT`/`CHECKED` hoặc thực đơn đã phục vụ xong **không** bị chặn; thực đơn nháp chứa món đã ngừng sẽ bị chặn ở bước gửi duyệt (`ERR-MENU-422-17`). | mã, lý do | Trạng thái mới | `BR-CAT-005` | `ERR-SYS-409-01` |
| `FR-MENU-DISH-006` | Danh sách và tìm món | P0 | Lọc theo tên, vai trò, nhóm nguyên liệu, phương pháp, Healthy, trạng thái; phân trang. | bộ lọc | Danh sách | Không áp dụng | Không áp dụng |
| `FR-MENU-DISH-007` | Quản lý phương pháp chế biến | P0 | Mỗi phương pháp có 2 cờ: là chiên/rán; là ít dầu mỡ. Danh sách khởi tạo: [H-8]; phương pháp nào là ít dầu mỡ: [H-1]. Không bỏ được cờ ít dầu mỡ khi còn món Healthy đang dùng phương pháp đó. | tên, 2 cờ | Phương pháp | `BR-CAT-005`, `BR-CAT-020` | `ERR-MENU-409-01`, `ERR-SYS-409-01` |
| `FR-MENU-DISH-008` | Quản lý cặp món kỵ nhau | P0 | Khai cặp 2 món không được xếp cùng ngày. Danh sách khởi tạo: [H-4] | món A, món B, ghi chú | Cặp kỵ | Không áp dụng | `ERR-MENU-409-01`, `ERR-MENU-422-07` |
| `FR-MENU-DISH-009` | Ảnh món | P1 | Gắn 1 ảnh cho món qua `FR-SYS-FILE-001`. | mã món, tệp | Không áp dụng | Không áp dụng | `ERR-SYS-413-01`, `ERR-SYS-415-01` |

#### Công thức: `FEAT-008`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-RCP-001` | Tạo công thức | P0 | Tạo công thức `DRAFT` cho một món: ≥ 1 dòng nguyên liệu, ≥ 1 dòng đánh dấu nguyên liệu chính. Mỗi dòng: định lượng tối thiểu, tối đa, chuẩn; đơn vị tự lấy từ đơn vị dùng của nguyên liệu. | mã món, cỡ định lượng (mặc định `STD`), ngày hiệu lực, các dòng | Công thức `DRAFT`, phiên bản kế tiếp | `BR-CAT-010`, `011`, `012`, `021`, `022` | `ERR-MENU-422-08`, `ERR-MENU-422-09`, `ERR-MENU-422-10`, `ERR-MENU-422-21` |
| `FR-MENU-RCP-002` | Sửa công thức nháp | P0 | Chỉ sửa được khi `DRAFT`. | như trên + `version` | Công thức | `BR-CAT-013` | `ERR-MENU-409-03` |
| `FR-MENU-RCP-003` | Gửi duyệt, duyệt, trả lại công thức | P0 | `DRAFT` → `PENDING` → `ACTIVE` hoặc về `DRAFT`. Khi duyệt: nếu ngày hiệu lực ≤ hôm nay thì phiên bản `ACTIVE` trước đó cùng món, cùng cỡ chuyển `SUPERSEDED`; nếu ngày hiệu lực ở tương lai thì cả hai cùng `ACTIVE` và tác vụ nền chuyển phiên bản cũ vào ngày hiệu lực. | mã, quyết định, lý do | Trạng thái mới | `BR-SEC-008`, `BR-CAT-014` | `ERR-SYS-403-01` |
| `FR-MENU-RCP-004` | Tạo phiên bản mới | P0 | Sao chép một phiên bản `ACTIVE` thành `DRAFT` với số phiên bản kế tiếp. | mã công thức, ngày hiệu lực, lý do | Công thức `DRAFT` | `BR-CAT-013`, `BR-AUD-001` | Không áp dụng |
| `FR-MENU-RCP-005` | Lấy công thức hiệu lực | P0 | Trả công thức `ACTIVE` của món và cỡ định lượng có ngày hiệu lực lớn nhất không vượt ngày D. | mã món, cỡ, ngày D | Công thức | `BR-CAT-014` | `ERR-MENU-404-01` |
| `FR-MENU-RCP-006` | So sánh hai phiên bản | P1 | Hiện từng dòng nguyên liệu thêm, bớt, đổi định lượng. | 2 mã công thức | Bảng khác biệt | Không áp dụng | Không áp dụng |
| `FR-MENU-RCP-007` | Nhiều cỡ định lượng | Chưa xếp | Một món có nhiều công thức với cỡ định lượng khác nhau, mỗi cỡ một giá bán. Có làm hay không: [O-02]. Nếu không làm, mọi công thức dùng cỡ `STD`. | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |

#### Giá bán món: `FEAT-010`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-PRC-001` | Đặt giá bán | P0 | Tạo giá `PENDING` cho một món và cỡ định lượng; giá đã gồm VAT [D-15]. | mã món, cỡ, giá, ngày hiệu lực | Giá `PENDING` | `BR-CAT-015`, `016` | `ERR-MENU-422-11`, `ERR-MENU-409-04` |
| `FR-MENU-PRC-002` | Duyệt / trả lại giá | P0 | `PENDING` → `APPROVED`. Giá `APPROVED` không sửa, không huỷ nếu ngày hiệu lực đã đến. | mã, quyết định, lý do | Trạng thái mới | `BR-SEC-008`, `BR-CAT-016` | `ERR-SYS-403-01`, `ERR-MENU-409-10` |
| `FR-MENU-PRC-003` | Lấy giá hiệu lực | P0 | Trả giá `APPROVED` có ngày hiệu lực lớn nhất không vượt ngày D. | mã món, cỡ, ngày D | Giá | Không áp dụng | `ERR-MENU-404-02` |
| `FR-MENU-PRC-004` | Lịch sử giá | P1 | Danh sách giá của một món theo thời gian. | mã món | Danh sách | Không áp dụng | Không áp dụng |

#### Loại suất: `FEAT-009`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-MTY-001` | Tạo loại suất | P0 | Tạo ở trạng thái `DRAFT`. | tên, ngưỡng giá (gồm VAT), số món chính đưa ra, số món chính được chọn, số món phụ, có rau, có canh | Loại suất | `BR-CAT-017` | `ERR-MENU-422-12` |
| `FR-MENU-MTY-002` | Kích hoạt / ngừng loại suất | P0 | `DRAFT` → `ACTIVE` → `INACTIVE`. Ngừng không ảnh hưởng thực đơn đã công bố. | mã, lý do | Trạng thái mới | Không áp dụng | Không áp dụng |
| `FR-MENU-MTY-003` | Sửa loại suất | P0 | Tên và cờ công khai: sửa bất kỳ lúc nào. Cơ cấu (ngưỡng giá, số món, rau, canh): chỉ sửa khi chưa có thực đơn nào từ `PENDING` trở đi. | như `001` + `version` | Loại suất | `BR-CAT-018` | `ERR-MENU-409-05` |
| `FR-MENU-MTY-004` | Đánh dấu công khai | P1 | Loại suất công khai hiện trên website ở E8. | mã, cờ | Không áp dụng | Không áp dụng | Không áp dụng |

#### Thực đơn tuần: `FEAT-011`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-MNU-001` | Tạo thực đơn tuần | P0 | Tạo thực đơn `DRAFT` cho một loại suất `ACTIVE` và một tuần; chọn các ngày phục vụ trong tuần. Các ngày được phép: [E2-Q3] | loại suất, ngày thứ Hai của tuần, danh sách ngày phục vụ | Thực đơn `DRAFT` với các ngày trống | `BR-MNU-001` | `ERR-MENU-409-06`, `ERR-MENU-422-13` |
| `FR-MENU-MNU-002` | Xếp món vào ngày | P0 | Thêm, đổi, bỏ món ở một vị trí của một ngày. Chỉ chọn được món `ACTIVE` có vai trò khớp vị trí. Hệ thống gắn công thức hiệu lực tại ngày phục vụ. Sau mỗi thay đổi, bộ kiểm chạy lại (`FR-MENU-RUL-001`). | mã ngày, vị trí, mã món | Ngày đã cập nhật + kết quả kiểm | `BR-MNU-002`, `003` | `ERR-MENU-422-14`, `ERR-MENU-404-01`, `ERR-MENU-409-07` |
| `FR-MENU-MNU-003` | Chọn món mặc định | P0 | Đặt một trong các món chính của ngày làm món mặc định. Bỏ món đang là mặc định khỏi ngày thì món mặc định bị xoá. | mã ngày, mã món | Không áp dụng | `BR-MNU-004` | `ERR-MENU-422-15` |
| `FR-MENU-MNU-004` | Kiểm ngưỡng giá suất | P0 | Với mỗi ngày và mỗi món chính: giá món chính + tổng giá các món phụ + giá rau + giá canh (giá hiệu lực tại ngày phục vụ) không vượt ngưỡng giá của loại suất. Cách kiểm này là [ĐỀ XUẤT]; cách đúng: [E2-Q1] | Không áp dụng (chạy cùng bộ kiểm) | Đạt / không đạt theo từng món chính | `BR-COST-012` | `ERR-MENU-404-02` |
| `FR-MENU-MNU-005` | Sao chép thực đơn | P1 | Tạo bản `DRAFT` cho tuần đích từ một thực đơn bất kỳ cùng loại suất. Món không còn `ACTIVE` bị bỏ trống và được liệt kê. Món mặc định của từng ngày được sao chép theo (trừ khi món đó bị bỏ trống). Mỗi ô gắn công thức hiệu lực tại ngày phục vụ mới. Bộ kiểm chạy ngay trên bản sao. | mã thực đơn nguồn, tuần đích | Thực đơn `DRAFT` | `BR-MNU-001` | `ERR-MENU-409-06` |
| `FR-MENU-MNU-006` | Lịch sử món đã dùng | P1 | Khi chọn món, hiện mỗi món đã xuất hiện ngày nào trong 4 tuần gần nhất của cùng loại suất. Chỉ tính thực đơn ở trạng thái `PUBLISHED`; không tính thực đơn nháp, chờ duyệt, đã thu hồi, đã huỷ, và không tính loại suất khác. | loại suất, tuần | Bảng món × ngày | Không áp dụng | Không áp dụng |
| `FR-MENU-MNU-007` | Xem và danh sách thực đơn | P0 | Lọc theo loại suất, tuần, trạng thái. Vai trò không có quyền ghi chỉ thấy `PUBLISHED`. | bộ lọc | Danh sách / chi tiết | Không áp dụng | Không áp dụng |
| `FR-MENU-MNU-008` | Xuất thực đơn | P1 | Xuất thực đơn tuần ra PDF: ngày × vị trí × tên món, đánh dấu món mặc định; tiêu đề ghi loại suất và khoảng ngày. Tệp **không** chứa giá bán, giá nhập hay cost. Thực đơn chưa `PUBLISHED` có dòng "BẢN NHÁP: CHƯA CÔNG BỐ" trên mỗi trang. | mã thực đơn | Tệp PDF | Không áp dụng | Không áp dụng |
| `FR-MENU-MNU-009` | Huỷ thực đơn nháp | P0 | Huỷ thực đơn `DRAFT` hoặc `CHECKED`. | mã, lý do | Không áp dụng | Không áp dụng | `ERR-MENU-409-08` |

#### Bộ kiểm quy tắc: `FEAT-012`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-RUL-001` | Kiểm thực đơn | P0 | Chạy mọi quy tắc đang áp dụng trên một thực đơn. Trả kết quả từng quy tắc, điểm quy tắc, và cờ "còn vi phạm cứng". Ghi kết quả vào `menu_rule_results`, thay kết quả cũ. Với quy tắc cost, chỉ người có `cost.cost.read` nhận cost % và số tiền; người thiếu quyền chỉ nhận đạt/không đạt. API phải loại bỏ số nhạy cảm cả trong detail và thông báo lỗi, không chỉ ẩn ở UI (`FR-COST-RUL-002`, `NFR-COST-005`). Cách tính từng quy tắc ở mục 3.3. | mã thực đơn | Danh sách kết quả, điểm, cờ | Toàn bộ `BR-MENU`, `BR-COST` đang bật | Không áp dụng |
| `FR-MENU-RUL-002` | Kiểm thực đơn chưa lưu | P0 | Như `001` nhưng nhận nội dung thực đơn trong yêu cầu và không ghi gì. Dùng cho agent ở E5, E9 thử phương án. | loại suất, tuần, các ngày và món | Như `001` | Như `001` | `ERR-MENU-422-14` |
| `FR-MENU-RUL-003` | Chi tiết vi phạm | P0 | Mỗi kết quả không đạt nêu: mã quy tắc, tên, loại, ngày liên quan, món liên quan, giá trị đo được, giới hạn. | Không áp dụng | Ví dụ: "BR-MENU-012 · Thịt lợn ở món chính 3 ngày liền (T2, T3, T4) · giới hạn 2" | Không áp dụng | Không áp dụng |
| `FR-MENU-RUL-004` | Ghi lý do chấp nhận | P0 | Với quy tắc mềm–nặng không đạt, người dựng ghi lý do ≥ 10 ký tự. Lý do bị xoá nếu lần kiểm sau quy tắc đó đạt. | mã kết quả, lý do | Không áp dụng | `BR-MNU-006` | `ERR-SYS-422-01` |
| `FR-MENU-RUL-005` | Danh mục quy tắc | P0 | Xem danh sách quy tắc: mã, tên, loại, điểm phạt, phạm vi ngày/tuần, tham số, đang bật. | Không áp dụng | Danh sách | Không áp dụng | Không áp dụng |
| `FR-MENU-RUL-006` | Sửa quy tắc | P0 | Đề nghị bật/tắt, đổi loại, đổi điểm phạt, đổi tham số. Có hiệu lực sau khi duyệt. Thực đơn `DRAFT`, `CHECKED` được kiểm lại bằng quy tắc mới ở lần kiểm kế tiếp; thực đơn từ `PENDING` trở đi giữ kết quả lúc gửi duyệt ([E2-Q11]). | mã quy tắc, giá trị mới, lý do | Đề nghị chờ duyệt | `BR-SEC-008`, `BR-MNU-007`, `BR-AUD-001` | `ERR-SYS-403-01`, `ERR-MENU-422-16` |
| `FR-MENU-RUL-007` | Cần người duyệt thứ hai khi điểm thấp | P1 | Thực đơn có điểm dưới tham số `QUY_TAC_DIEM_TOI_THIEU` cần 2 người duyệt khác nhau. | Không áp dụng | Không áp dụng | `BR-MNU-008` | Không áp dụng |

#### Duyệt và công bố: `FEAT-013`

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-APV-001` | Gửi duyệt thực đơn | P0 | `DRAFT`/`CHECKED` → `PENDING`. Hệ thống chạy lại bộ kiểm ngay trước khi chuyển. Điều kiện ở `BR-MNU-005`. Thông báo cho người có quyền duyệt theo `BR-MNU-010`. | mã thực đơn | Thực đơn `PENDING` | `BR-MNU-005`, `006`, `010` | `ERR-MENU-422-17`, `ERR-MENU-422-18`, `ERR-MENU-422-19` |
| `FR-MENU-APV-002` | Duyệt / trả lại thực đơn | P0 | Duyệt: → `APPROVED`, đóng băng kết quả kiểm và công thức đã gắn. Trả lại: → `DRAFT` kèm lý do. Thông báo cho người tạo. | mã, quyết định, lý do | Trạng thái mới | `BR-SEC-008`, `BR-MNU-008` | `ERR-SYS-403-01` |
| `FR-MENU-APV-003` | Công bố | P0 | `APPROVED` → `PUBLISHED`. Từ lúc này thực đơn xuất hiện ở dịch vụ tra cứu thực đơn đã công bố. | mã | Thực đơn `PUBLISHED` | `BR-MNU-009` | `ERR-MENU-409-09` |
| `FR-MENU-APV-004` | Thu hồi | P0 | `PUBLISHED` → `WITHDRAWN`, bắt buộc lý do. Phát sự kiện để E6 xử lý lựa chọn món đã có. | mã, lý do | Thực đơn `WITHDRAWN` | `BR-AUD-001` | `ERR-SYS-422-01` |
| `FR-MENU-APV-005` | Sửa sau thu hồi | P0 | `WITHDRAWN` → `DRAFT`; sau đó đi lại toàn bộ chu trình kiểm, duyệt, công bố. | mã | Thực đơn `DRAFT` | Không áp dụng | Không áp dụng |
| `FR-MENU-APV-006` | Chỗ móc kiểm cost | P0 | `FR-MENU-APV-001` gọi một danh sách bộ kiểm trước khi chuyển trạng thái. R2 đăng ký bộ kiểm quy tắc; R3 đăng ký thêm bộ kiểm cost mà không sửa MENU. Vượt ngưỡng chỉ chặn ở chế độ `CHAN`; `CANH_BAO` không chặn do vượt ngưỡng, nhưng thiếu giá/VAT hoặc bảng tính món đặc thù hợp lệ vẫn không đủ điều kiện gửi duyệt. Chế độ và mặc định là đề xuất theo SRS Cost. | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng |

#### Nhập từ bảng tính

| Mã FR | Tên chức năng | Ưu tiên | Mô tả | Input | Output | BR | Mã lỗi |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `FR-MENU-IMP-001` | Tải mẫu | P0 | 4 mẫu `.xlsx`: nguyên liệu, món, công thức, giá bán. Mỗi mẫu có dòng tiêu đề, dòng ví dụ, và trang liệt kê giá trị hợp lệ của các cột liệt kê. | loại mẫu | Tệp `.xlsx` | Không áp dụng | Không áp dụng |
| `FR-MENU-IMP-002` | Kiểm tệp nhập | P0 | Đọc tệp, kiểm từng dòng theo đúng quy tắc của FR tạo tương ứng, trả danh sách lỗi theo số dòng và cột. Không ghi gì. Tối đa 2.000 dòng mỗi tệp. | loại, tệp | Số dòng hợp lệ, danh sách lỗi | Như FR tạo tương ứng; `BR-CAT-023` | `ERR-MENU-422-20`, `ERR-SYS-413-01`, `ERR-SYS-415-01` |
| `FR-MENU-IMP-003` | Thực hiện nhập | P0 | Chỉ chạy khi tệp không còn lỗi. Ghi toàn bộ trong một giao dịch: tất cả hoặc không gì cả. Món và công thức vào `DRAFT`; giá vào `PENDING`; nguyên liệu vào `ACTIVE`. | loại, tệp | Số bản ghi đã tạo | `BR-CAT-019` | `ERR-MENU-422-20` |

### 3.2 Quy tắc nghiệp vụ của dữ liệu và vòng đời

Các quy tắc xây thực đơn (`BR-MENU-001` → `051`, `BR-COST-001` → `012`) nằm ở [bảng quy tắc](../../gia-phat/brainstorms/quy-tac-thuc-don.md) và mục 3.3. Bảng dưới là quy tắc về tính đúng đắn của dữ liệu và vòng đời.

| Mã BR | Tên quy tắc | Phát biểu (KHI – THÌ) | Ngoại lệ |
| :--- | :--- | :--- | :--- |
| `BR-CAT-001` | Tên không trùng | KHI tạo hoặc sửa nguyên liệu, món, nhóm, phương pháp, loại suất THÌ tên (bỏ dấu cách thừa, không phân biệt hoa thường) không trùng bản ghi chưa huỷ cùng loại | Không áp dụng |
| `BR-CAT-002` | Hệ số quy đổi | Hệ số quy đổi > 0. KHI đơn vị mua là `kg` và đơn vị dùng là `g` THÌ hệ số phải bằng 1000 | Không áp dụng |
| `BR-CAT-003` | Hao hụt bắt buộc | KHI nguyên liệu có xương hoặc vỏ THÌ tỷ lệ hao hụt bắt buộc, trong khoảng 0,01–99,99 | `BR-COST-010` |
| `BR-CAT-004` | Khoá đơn vị khi đang dùng | KHI nguyên liệu nằm trong công thức `ACTIVE` THÌ không sửa được đơn vị dùng và hệ số quy đổi | Tạo nguyên liệu mới thay thế |
| `BR-CAT-005` | Không huỷ khi đang dùng | KHI một bản ghi danh mục đang được bản ghi hiệu lực khác tham chiếu THÌ không huỷ, không ngừng dùng được | Không áp dụng |
| `BR-CAT-006` | Healthy cần phương pháp ít dầu mỡ | KHI món gắn cờ Healthy THÌ phương pháp chế biến phải có cờ ít dầu mỡ | `BR-MENU-003`; danh sách: [H-1] |
| `BR-CAT-007` | Món gốc một cấp | KHI gắn món gốc THÌ món gốc phải cùng vai trò, không phải chính nó, và bản thân món gốc không có món gốc | Không áp dụng |
| `BR-CAT-008` | Thuộc tính ảnh hưởng quy tắc | Các thuộc tính: vai trò, nhóm nguyên liệu chính, phương pháp, món gốc, Healthy, vị chua, kết cấu, thanh nhẹ, cầu kỳ, chịu vận chuyển, phù hợp bếp lớn, nhóm cost, đặc thù. KHI sửa một trong số này trên món `ACTIVE` THÌ cần duyệt lại | Không áp dụng |
| `BR-CAT-009` | Món hoạt động cần công thức | KHI duyệt món THÌ món phải có ≥ 1 công thức `ACTIVE`. Duyệt món và công thức đầu tiên của nó trong cùng một lần được phép | Không áp dụng |
| `BR-CAT-010` | Cấu trúc công thức | Công thức có ≥ 1 dòng; ≥ 1 dòng là nguyên liệu chính; một nguyên liệu xuất hiện tối đa 1 lần; mọi nguyên liệu ở trạng thái `ACTIVE` | Không áp dụng |
| `BR-CAT-011` | Khoảng định lượng | 0 < tối thiểu ≤ chuẩn ≤ tối đa | Không áp dụng |
| `BR-CAT-012` | Nhóm nguyên liệu chính khớp món | KHI món có vai trò món chính hoặc món phụ THÌ ít nhất 1 dòng nguyên liệu chính của công thức thuộc nhóm nguyên liệu chính của món | Rau, canh không áp dụng |
| `BR-CAT-013` | Công thức đã duyệt là bất biến | KHI công thức ở `PENDING`, `ACTIVE`, `SUPERSEDED` THÌ không sửa được nội dung; thay đổi qua phiên bản mới | `PENDING` bị trả lại về `DRAFT` thì sửa được |
| `BR-CAT-014` | Một công thức hiệu lực mỗi ngày | Với mỗi món, cỡ định lượng và ngày D, có đúng 1 công thức hiệu lực: bản `ACTIVE` có ngày hiệu lực lớn nhất ≤ D | Không áp dụng |
| `BR-CAT-015` | Giá bán hợp lệ | Giá bán là số nguyên ≥ 0, bội số của 100 đồng | Không áp dụng |
| `BR-CAT-016` | Giá đã hiệu lực là bất biến | KHI giá `APPROVED` có ngày hiệu lực ≤ hôm nay THÌ không sửa, không huỷ; giá mới là dòng mới có ngày hiệu lực > hôm nay | Không áp dụng |
| `BR-CAT-017` | Cấu hình loại suất | Ngưỡng giá > 0 và là bội số của 100 đồng; số món chính đưa ra ≥ số món chính được chọn ≥ 1; số món phụ từ 0 đến 5 | Không áp dụng |
| `BR-CAT-018` | Khoá cơ cấu loại suất | KHI loại suất có thực đơn từ `PENDING` trở đi THÌ không sửa được cơ cấu | Tạo loại suất mới |
| `BR-CAT-019` | Nhập không bỏ qua duyệt | Dữ liệu nhập từ bảng tính không vào thẳng `ACTIVE`/`APPROVED` | Nguyên liệu (không có bước duyệt) |
| `BR-CAT-020` | Giữ cờ ít dầu mỡ khi còn món Healthy dùng | KHI bỏ cờ ít dầu mỡ của một phương pháp chế biến mà còn món `ACTIVE` hoặc `PENDING` có cờ Healthy dùng phương pháp đó THÌ không lưu, trả danh sách món | Bỏ cờ Healthy của các món đó trước (qua đề nghị thay đổi) |
| `BR-CAT-021` | Độ chính xác của số | Hệ số quy đổi tối đa 4 chữ số thập phân; tỷ lệ hao hụt tối đa 2; định lượng tối đa 3. KHI nhập nhiều chữ số thập phân hơn THÌ từ chối, không tự làm tròn (`ERR-MENU-422-01`, `ERR-MENU-422-02`, `ERR-MENU-422-09` tương ứng) | Không áp dụng |
| `BR-CAT-022` | Ngày hiệu lực của công thức | KHI lưu hoặc gửi duyệt công thức THÌ ngày hiệu lực phải từ hôm nay trở đi, và phải **sau** ngày hiệu lực của mọi phiên bản `ACTIVE` hoặc `PENDING` khác của cùng món và cùng cỡ định lượng. Vi phạm → `ERR-MENU-422-21` | Công thức đầu tiên của món chỉ cần từ hôm nay trở đi |
| `BR-CAT-023` | Quy ước đọc tệp nhập | (a) Đọc cột theo **tên cột**, không theo vị trí: đổi thứ tự cột được chấp nhận. (b) Cột không có trong mẫu bị bỏ qua, kèm cảnh báo nêu tên cột; thiếu cột của mẫu thì từ chối. (c) Dòng trống hoàn toàn bị bỏ qua. (d) Dấu cách đầu và cuối ô được cắt. (e) Ô số lưu ở dạng văn bản được đọc như số nếu phân tích được. (f) Dấu thập phân nhận cả phẩy và chấm; không nhận dấu phân cách hàng nghìn. (g) Thứ tự dòng không quan trọng: món gốc có thể nằm sau món biến thể; các dòng công thức của một món được gộp theo tên món, không cần liền nhau. (h) Chỉ đọc trang tính có tên đúng mẫu; trang khác bị bỏ qua kèm cảnh báo. (i) Chỉ nhận `.xlsx` không đặt mật khẩu | Không áp dụng |
| `BR-MNU-001` | Một thực đơn mỗi loại suất mỗi tuần | KHI tạo hoặc sao chép thực đơn THÌ không tồn tại thực đơn chưa huỷ, chưa thu hồi của cùng loại suất và tuần | Thực đơn riêng theo khách: E6, [E2-Q4] |
| `BR-MNU-002` | Số ô theo loại suất | Mỗi ngày có đúng: số món chính đưa ra ô món chính, số món phụ ô món phụ, 1 ô rau nếu có rau, 1 ô canh nếu có canh. Không thêm được món vượt số ô | `BR-MENU-001`, `004`, `005` |
| `BR-MNU-003` | Một món một lần mỗi ngày | Một món xuất hiện tối đa 1 lần trong một ngày | Không áp dụng |
| `BR-MNU-004` | Món mặc định | Món mặc định phải là một món chính của ngày đó | [D-14] |
| `BR-MNU-005` | Điều kiện gửi duyệt | KHI gửi duyệt THÌ: mọi ô của mọi ngày đã có món; mọi ngày có món mặc định; mọi món còn `ACTIVE`; không còn quy tắc cứng không đạt | Không áp dụng |
| `BR-MNU-006` | Lý do cho vi phạm mềm–nặng | KHI gửi duyệt mà còn quy tắc mềm có điểm phạt 3 không đạt THÌ mỗi vi phạm đó phải có lý do chấp nhận | Không áp dụng |
| `BR-MNU-007` | Giới hạn sửa quy tắc | Điểm phạt quy tắc mềm là 1, 2 hoặc 3; quy tắc cứng có điểm phạt 0. Tham số số học phải ≥ 0; tham số kiểu đếm (số ngày, số món, số lần) phải là số nguyên | Không áp dụng |
| `BR-MNU-008` | Hai người duyệt khi điểm thấp | KHI điểm quy tắc < `QUY_TAC_DIEM_TOI_THIEU` THÌ cần 2 người duyệt khác nhau, cả hai khác người tạo. Điểm đúng bằng ngưỡng cần 1 người duyệt. KHI một người trả lại THÌ thực đơn về `DRAFT` và mọi quyết định duyệt của vòng đó mất hiệu lực; lần gửi duyệt sau là vòng mới, duyệt lại từ đầu | Không thực hiện được nếu chỉ có một người duyệt: [O-06] |
| `BR-MNU-009` | Công bố không quá muộn | KHI công bố THÌ ngày phục vụ đầu tiên của thực đơn phải sau hôm nay | Không áp dụng |
| `BR-MNU-010` | Thông báo duyệt | KHI một lần gửi duyệt gồm nhiều mục cùng loại THÌ mỗi người có quyền duyệt nhận **một** thông báo gộp ghi số mục. Người gửi không nhận thông báo chờ duyệt cho nội dung của chính mình, kể cả khi người đó có quyền duyệt | Không áp dụng |

### 3.3 Bộ kiểm quy tắc: cách tính

#### 3.3.1 Khung chung

1. **Đầu vào**: thực đơn (loại suất, các ngày phục vụ, món ở từng ô kèm thuộc tính của món), và các ngày phục vụ ngay trước tuần đó của cùng loại suất nếu quy tắc cần (xem [E2-Q2]).
2. **Phạm vi**: quy tắc cấp `DAY` chạy một lần cho mỗi ngày; quy tắc cấp `WEEK` chạy một lần cho cả thực đơn. Ngày chưa có món nào không sinh kết quả cấp ngày.
   - **"Ngày liên tiếp"** trong các quy tắc tuần (`BR-MENU-012`, `016`, `017`) là các **ngày phục vụ** liền nhau trong thực đơn: ngày nghỉ không ngắt chuỗi. Ví dụ thực đơn phục vụ T2, T3, T5 thì ba ngày đó là liên tiếp. Cách hiểu này là [ĐỀ XUẤT], cần người soạn docx xác nhận cùng [H-2].
3. **Ô trống**: ngày chưa đủ món vẫn được kiểm; quy tắc về cơ cấu (`001`, `002`, `004`, `005`) báo không đạt, các quy tắc khác chỉ xét các món đã có.
4. **Điểm**: `điểm = max(0, 100 − Σ điểm phạt)`. Một quy tắc cấp `DAY` không đạt ở 3 ngày bị trừ 3 lần.
5. **Kết quả**: mỗi quy tắc × phạm vi cho một dòng đạt / không đạt kèm chi tiết (`FR-MENU-RUL-003`).
6. **Thời gian**: kiểm xong một thực đơn 6 ngày trong ≤ 2 giây (`NFR-MENU-001`).

#### 3.3.2 Cách tính từng quy tắc chạy trong R2

Cột "Tham số" là tên khoá trong `menu_rules.params`. **Giá trị, loại cứng/mềm và điểm phạt lấy từ bảng quy tắc sau khi DL-01 duyệt**: tài liệu này không lặp lại con số để tránh hai nơi lệch nhau.

| Mã | Phạm vi | Tham số | Cách tính (không đạt khi…) |
| :--- | :---: | :--- | :--- |
| `BR-MENU-001` | DAY | Không áp dụng | Số món ở ô món chính ≠ số món chính đưa ra của loại suất |
| `BR-MENU-002` | DAY | `healthy_count` | Số món chính có cờ Healthy ≠ `healthy_count` |
| `BR-MENU-003` | DAY | Không áp dụng | Có món Healthy mà phương pháp không có cờ ít dầu mỡ |
| `BR-MENU-004` | DAY | Không áp dụng | Thiếu rau hoặc canh khi loại suất yêu cầu |
| `BR-MENU-005` | DAY | Không áp dụng | Số món phụ ≠ số món phụ của loại suất |
| `BR-MENU-010` | DAY | Không áp dụng | Có 2 món chính cùng nhóm nguyên liệu chính |
| `BR-MENU-011` | DAY | `max_pairs` | Số cặp (món phụ, món chính) cùng nhóm nguyên liệu chính > `max_pairs` |
| `BR-MENU-012` | WEEK | `max_consecutive_days` | Một nhóm nguyên liệu chính có mặt ở món chính trong số ngày phục vụ liên tiếp > `max_consecutive_days`. Thịt lợn có giới hạn riêng hay không: [H-2] |
| `BR-MENU-013` | WEEK | `max_per_week` | Một món gốc (xem `014`) xuất hiện > `max_per_week` lần trong tuần |
| `BR-MENU-014` | Không áp dụng | Không áp dụng | Không phải quy tắc kiểm; là cách đếm: món có món gốc được đếm theo món gốc |
| `BR-MENU-015` | WEEK | `min_groups` | Số nhóm nguyên liệu chính khác nhau ở món chính trong tuần < `min_groups` |
| `BR-MENU-016` | WEEK | `min_gap_days` | Cùng một món rau xuất hiện ở 2 ngày phục vụ cách nhau < `min_gap_days` |
| `BR-MENU-017` | WEEK | `min_gap_days` | Như `016` cho canh |
| `BR-MENU-018` | DAY | Không áp dụng | Rau của ngày có khai mùa vụ và tháng của ngày phục vụ nằm ngoài mọi khoảng mùa |
| `BR-MENU-019` | WEEK | `max_per_week` | Một món phụ (theo món gốc) xuất hiện > `max_per_week` lần |
| `BR-MENU-020` | DAY | Không áp dụng | 2 món chính không Healthy cùng phương pháp chế biến |
| `BR-MENU-021` | DAY | `max_fried_sides` | Số món phụ có phương pháp chiên > `max_fried_sides` |
| `BR-MENU-022` | DAY | `max_fried` | Số món (mọi vai trò) có phương pháp chiên > `max_fried` |
| `BR-MENU-023` | DAY | `max_same_method` | Có phương pháp chế biến xuất hiện ở > `max_same_method` món |
| `BR-MENU-030` | DAY | `max_sour` | Số món có cờ vị chua > `max_sour` |
| `BR-MENU-031` | DAY | `max_sauce` | Số món kết cấu `SAUCE` > `max_sauce` |
| `BR-MENU-032` | DAY | `max_dry` | Số món kết cấu `DRY`, không tính ô rau, > `max_dry` |
| `BR-MENU-033` | DAY | `min_light` | Số món có cờ thanh nhẹ ở ô món chính và món phụ < `min_light` |
| `BR-MENU-034` | DAY | Không áp dụng | Có 2 món của ngày thuộc một cặp kỵ nhau (so theo món gốc) |
| `BR-MENU-040` | DAY | `max_complex` | Số món có cờ cầu kỳ > `max_complex` |
| `BR-MENU-041` | WEEK | `max_complex` | Tổng số lượt món cầu kỳ trong tuần > `max_complex` |
| `BR-MENU-042` | DAY | Không áp dụng | Có món không chịu vận chuyển. Trong R2 thực đơn chưa gắn với điểm giao nên quy tắc chỉ cảnh báo có món loại này; kiểm theo thời gian giao viết ở E6 |
| `BR-MENU-043` | DAY | Không áp dụng | Có món không có cờ phù hợp bếp lớn |
| `BR-MENU-044` | DAY | Không áp dụng | Có món mà nguyên liệu chính trong công thức không có cờ nguồn cung ổn định |
| `BR-MENU-050` | WEEK | `min_protein_sources` | Số nguồn đạm khác nhau (theo nhóm nguyên liệu chính của món chính và món phụ) < `min_protein_sources` |
| `BR-MENU-051` | Không áp dụng | Không áp dụng | Chưa có định nghĩa [H-5]; không chạy |
| `BR-COST-008` | Không áp dụng | Không áp dụng | Kiểm khi lưu công thức, không phải khi kiểm thực đơn: định lượng chuẩn của nguyên liệu chính nằm ngoài khoảng chuẩn. Khoảng chuẩn lấy từ đâu: [E2-Q5] |
| `BR-COST-009` | Không áp dụng | Không áp dụng | Kiểm khi lưu công thức: tổng định lượng nguyên liệu không phải chính vượt mức cho phép. Mức cho phép lấy từ đâu: [E2-Q5] |
| `BR-COST-010` | Không áp dụng | Không áp dụng | Kiểm khi lưu nguyên liệu: `BR-CAT-003` |
| `BR-COST-012` | DAY | Không áp dụng | `FR-MENU-MNU-004` |

Quy tắc `BR-COST-001` → `007`, `011` cần giá nhập: đặc tả ở SRS epic `cost`.

#### 3.3.3 Phần chưa viết được

| Nội dung | Chờ |
| :--- | :--- |
| Loại cứng/mềm, điểm phạt, giá trị tham số của từng quy tắc | DL-01 |
| Danh sách phương pháp ít dầu mỡ, nhóm nguyên liệu, phương pháp chế biến, cặp kỵ | [H-1], [H-3], [H-8], [H-4] |
| Quy tắc tuần có xét tuần trước không | [E2-Q2] |
| Bộ ca kiểm thử cho từng quy tắc (1 ca đạt, 1 ca vi phạm) | DL-01, rồi `/test-cases` |

### 3.4 Yêu cầu phi chức năng riêng của epic

NFR toàn hệ thống ở SRS nền tảng. Bổ sung:

| Mã NFR | Yêu cầu | Cách kiểm |
| :--- | :--- | :--- |
| `NFR-MENU-001` | `FR-MENU-RUL-001` trả kết quả trong ≤ 2 giây (p95) cho thực đơn 6 ngày, mỗi ngày ≤ 10 món | Đo trên 50 lần kiểm |
| `NFR-MENU-002` | `FR-MENU-RUL-002` chịu được 20 lần gọi đồng thời (agent thử phương án) với p95 ≤ 2 giây | Kiểm thử tải |
| `NFR-MENU-003` | `FR-MENU-IMP-002` kiểm xong tệp 2.000 dòng trong ≤ 30 giây; chạy qua tác vụ nền nếu vượt 5 giây | Đo với tệp mẫu |
| `NFR-MENU-004` | Danh sách món và nguyên liệu trả về trong p95 ≤ 300 ms với 2.000 món, 1.000 nguyên liệu | Kiểm thử với dữ liệu giả lập |
| `NFR-MENU-005` | Kết quả của bộ kiểm là xác định: cùng đầu vào và cùng danh mục quy tắc luôn cho cùng kết quả | Chạy lặp 100 lần trên bộ ca kiểm thử |
| `NFR-MENU-006` | Mỗi thuộc tính của món có chú giải định nghĩa và 1 ví dụ ngay trên màn hình nhập | Rà soát giao diện (rủi ro E2-R3) |

### 3.5 Ma trận lỗi

| Mã ERR | HTTP | Điều kiện phát sinh | Khoá bản địa hoá | Thông báo hiển thị | Mức | Hành động tiếp theo |
| :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| `ERR-MENU-404-01` | 404 | Món không có công thức hiệu lực tại ngày phục vụ | `menu.recipe_not_effective` | "Món {tên} chưa có công thức hiệu lực cho ngày {ngày}." | High | Tạo hoặc duyệt công thức |
| `ERR-MENU-404-02` | 404 | Món không có giá bán hiệu lực tại ngày phục vụ | `menu.price_not_effective` | "Món {tên} chưa có giá bán hiệu lực cho ngày {ngày}." | High | Đặt và duyệt giá bán |
| `ERR-MENU-409-01` | 409 | Trùng tên (`BR-CAT-001`) hoặc trùng cặp kỵ | `menu.duplicate_name` | "Tên này đã tồn tại." | Medium | Đổi tên hoặc dùng bản ghi có sẵn |
| `ERR-MENU-409-02` | 409 | Sửa đơn vị/hệ số của nguyên liệu đang trong công thức hiệu lực | `menu.ingredient_unit_locked` | "Không sửa được đơn vị vì nguyên liệu đang dùng trong {n} công thức." | Medium | Tạo nguyên liệu mới |
| `ERR-MENU-409-03` | 409 | Sửa công thức không ở trạng thái nháp | `menu.recipe_immutable` | "Công thức đã gửi duyệt không sửa được. Hãy tạo phiên bản mới." | Medium | Tạo phiên bản mới |
| `ERR-MENU-409-04` | 409 | Đã có giá cho cùng món, cỡ, ngày hiệu lực | `menu.price_exists` | "Đã có giá bán cho ngày hiệu lực này." | Medium | Chọn ngày khác |
| `ERR-MENU-409-05` | 409 | Sửa cơ cấu loại suất đã có thực đơn gửi duyệt | `menu.meal_type_locked` | "Loại suất đã có thực đơn nên không sửa được cơ cấu. Hãy tạo loại suất mới." | Medium | Tạo loại suất mới |
| `ERR-MENU-409-06` | 409 | Đã có thực đơn cho loại suất và tuần này | `menu.menu_exists` | "Tuần này đã có thực đơn cho loại suất đã chọn." | Medium | Mở thực đơn đã có |
| `ERR-MENU-409-07` | 409 | Sửa nội dung thực đơn không ở `DRAFT`/`CHECKED` | `menu.menu_not_editable` | "Thực đơn đang ở trạng thái {trạng thái} nên không sửa được." | Medium | Thu hồi hoặc chờ kết quả duyệt |
| `ERR-MENU-409-08` | 409 | Huỷ thực đơn đã gửi duyệt trở đi | `menu.menu_not_cancellable` | "Chỉ huỷ được thực đơn nháp." | Medium | Thu hồi nếu đã công bố |
| `ERR-MENU-409-09` | 409 | Công bố thực đơn có ngày phục vụ đầu tiên không sau hôm nay | `menu.publish_too_late` | "Thực đơn có ngày phục vụ đã qua hoặc là hôm nay nên không công bố được." | High | Bỏ các ngày đã qua, gửi duyệt lại |
| `ERR-MENU-409-10` | 409 | Sửa hoặc huỷ giá bán `APPROVED` có ngày hiệu lực đã đến (`BR-CAT-016`) | `menu.price_immutable` | "Giá đã hiệu lực không sửa hoặc huỷ được. Hãy đặt giá mới với ngày hiệu lực từ ngày mai." | Medium | Đặt giá mới |
| `ERR-MENU-422-01` | 422 | Hệ số quy đổi ≤ 0 hoặc sai với cặp kg–g | `menu.conversion_invalid` | "Hệ số quy đổi không hợp lệ." | Medium | Sửa hệ số |
| `ERR-MENU-422-02` | 422 | Thiếu tỷ lệ hao hụt cho nguyên liệu có xương/vỏ | `menu.waste_required` | "Nguyên liệu có xương hoặc vỏ cần khai tỷ lệ hao hụt." | Medium | Nhập tỷ lệ |
| `ERR-MENU-422-03` | 422 | Tháng mùa vụ ngoài 1–12 | `menu.season_invalid` | "Tháng phải từ 1 đến 12." | Medium | Sửa tháng |
| `ERR-MENU-422-04` | 422 | Gắn Healthy cho món có phương pháp không ít dầu mỡ | `menu.healthy_method` | "Món Healthy phải dùng phương pháp chế biến ít dầu mỡ." | Medium | Đổi phương pháp hoặc bỏ cờ |
| `ERR-MENU-422-05` | 422 | Món gốc sai (`BR-CAT-007`) | `menu.base_dish_invalid` | "Món gốc phải cùng vai trò và không phải là biến thể của món khác." | Medium | Chọn món gốc khác |
| `ERR-MENU-422-06` | 422 | Gửi duyệt hoặc duyệt món chưa có công thức | `menu.dish_no_recipe` | "Món cần có công thức trước khi duyệt." | High | Tạo công thức |
| `ERR-MENU-422-07` | 422 | Cặp kỵ gồm 2 món giống nhau | `menu.conflict_same_dish` | "Hai món của cặp phải khác nhau." | Medium | Chọn lại |
| `ERR-MENU-422-08` | 422 | Công thức sai cấu trúc (`BR-CAT-010`) | `menu.recipe_structure` | "Công thức cần ít nhất một nguyên liệu chính và không lặp nguyên liệu." | Medium | Sửa các dòng |
| `ERR-MENU-422-09` | 422 | Khoảng định lượng sai (`BR-CAT-011`) | `menu.qty_range` | "Định lượng phải thoả: tối thiểu ≤ chuẩn ≤ tối đa." | Medium | Sửa định lượng |
| `ERR-MENU-422-10` | 422 | Nguyên liệu chính không thuộc nhóm của món (`BR-CAT-012`) | `menu.main_group_mismatch` | "Công thức cần có nguyên liệu chính thuộc nhóm {nhóm} của món." | Medium | Sửa công thức hoặc nhóm của món |
| `ERR-MENU-422-11` | 422 | Giá bán sai (`BR-CAT-015`) hoặc ngày hiệu lực không sau hôm nay | `menu.price_invalid` | "Giá bán phải là bội số của 100 đồng và có hiệu lực từ ngày mai trở đi." | Medium | Sửa giá hoặc ngày |
| `ERR-MENU-422-12` | 422 | Cấu hình loại suất sai (`BR-CAT-017`) | `menu.meal_type_invalid` | "Cấu hình loại suất không hợp lệ." | Medium | Sửa cấu hình |
| `ERR-MENU-422-13` | 422 | Ngày bắt đầu tuần không phải thứ Hai, hoặc không chọn ngày phục vụ nào | `menu.week_invalid` | "Tuần phải bắt đầu từ thứ Hai và có ít nhất một ngày phục vụ." | Medium | Chọn lại |
| `ERR-MENU-422-14` | 422 | Xếp món không hoạt động, sai vai trò, vượt số ô, hoặc lặp trong ngày | `menu.slot_invalid` | "Không xếp được món {tên} vào vị trí này." | Medium | Chọn món khác |
| `ERR-MENU-422-15` | 422 | Món mặc định không phải món chính của ngày | `menu.default_invalid` | "Món mặc định phải là một món chính của ngày." | Medium | Chọn lại |
| `ERR-MENU-422-16` | 422 | Sửa quy tắc sai (`BR-MNU-007`) | `menu.rule_invalid` | "Giá trị quy tắc không hợp lệ." | Medium | Sửa giá trị |
| `ERR-MENU-422-17` | 422 | Gửi duyệt khi còn ô trống, thiếu món mặc định, hoặc có món không còn hoạt động | `menu.menu_incomplete` | "Thực đơn chưa đủ: {danh sách}." | High | Bổ sung |
| `ERR-MENU-422-18` | 422 | Gửi duyệt khi còn quy tắc cứng không đạt | `menu.hard_rule_failed` | "Thực đơn còn {n} vi phạm quy tắc bắt buộc." | High | Sửa thực đơn |
| `ERR-MENU-422-19` | 422 | Gửi duyệt khi vi phạm mềm–nặng chưa có lý do | `menu.waiver_required` | "Cần ghi lý do cho {n} cảnh báo mức nặng." | Medium | Ghi lý do |
| `ERR-MENU-422-20` | 422 | Tệp nhập còn dòng lỗi, sai mẫu, hoặc vượt 2.000 dòng | `menu.import_invalid` | "Tệp còn {n} lỗi. Xem danh sách lỗi theo dòng." | Medium | Sửa tệp, nhập lại |
| `ERR-MENU-422-21` | 422 | Ngày hiệu lực của công thức ở quá khứ, hoặc không sau ngày hiệu lực của phiên bản `ACTIVE`/`PENDING` khác cùng món và cỡ (`BR-CAT-022`) | `menu.recipe_effective_date` | "Ngày hiệu lực phải từ hôm nay và sau ngày hiệu lực của phiên bản hiện có ({ngày})." | Medium | Chọn ngày muộn hơn |

---

## 4. Phụ lục

### 4.1 Sơ đồ

Sơ đồ trạng thái, use case, luồng người dùng viết ở các bước `/state`, `/usecase`, `/user-flow`. Mô hình dữ liệu: mục 4 của [ERD](../../nen-tang/srs/erd.md).

### 4.2 Ma trận truy vết

| Tính năng PRD | Năng lực (epic-spec) | FR |
| :--- | :--- | :--- |
| `FEAT-006` | `CAP-ING-01` → `06` | `FR-MENU-ING-001` → `006` |
| `FEAT-007` | `CAP-DISH-01` → `09` | `FR-MENU-DISH-001` → `009` |
| `FEAT-008` | `CAP-RCP-01` → `07` | `FR-MENU-RCP-001` → `007` |
| `FEAT-010` | `CAP-PRC-01` → `03` | `FR-MENU-PRC-001` → `004` |
| `FEAT-009` | `CAP-MTY-01` → `03` | `FR-MENU-MTY-001` → `004` |
| `FEAT-011` | `CAP-MNU-01` → `08` | `FR-MENU-MNU-001` → `009` |
| `FEAT-012` | `CAP-RUL-01` → `09` | `FR-MENU-RUL-001` → `007`; mục 3.3 |
| `FEAT-013` | `CAP-APV-01` → `07` | `FR-MENU-APV-001` → `006`; `FR-SYS-NTF-001` |
| (nhập dữ liệu) | `CAP-IMP-01` → `03` | `FR-MENU-IMP-001` → `003` |

### 4.3 Thay đổi cần cập nhật ở tài liệu khác

Phát sinh khi viết SRS này.

| Tài liệu | Cần bổ sung | Trạng thái |
| :--- | :--- | :--- |
| `schema.dbml`, ERD | Chỗ lưu giá trị đề nghị khi món `ACTIVE` chờ duyệt lại thuộc tính (`FR-MENU-DISH-002`) | ✅ Bảng `change_requests`: ERD v0.2.0 mục 3.5 |
| `schema.dbml`, ERD | Thực đơn cần 2 người duyệt (`BR-MNU-008`) | ✅ Bảng `approvals`: ERD v0.2.0 mục 3.5 |
| `schema.dbml`, ERD | Đề nghị sửa quy tắc chờ duyệt (`FR-MENU-RUL-006`) | ✅ Bảng `change_requests` |
| Bảng quy tắc | Thêm cột phạm vi (ngày/tuần) và tên tham số cho khớp mục 3.3.2 | Chưa làm: nên làm cùng lúc người soạn docx duyệt (DL-01) để họ không phải đọc hai phiên bản |

Hệ quả với FR đã viết: một món `ACTIVE` đang có đề nghị `PENDING` hiển thị nhãn "chờ duyệt thay đổi" nhưng **vẫn ở trạng thái `ACTIVE`** với giá trị cũ, không chuyển về `PENDING` như mô tả ban đầu ở `FR-MENU-DISH-002`. Trạng thái `PENDING` của món chỉ dùng cho món mới chưa từng được duyệt.

### 4.4 Các điểm đưa vào ở v0.2.0 và v0.3.0

**Mười điểm đưa vào ở v0.2.0.**

Nguồn: mục "Phát sinh khi viết tiêu chí nghiệm thu" của [acceptance-criteria.md](../userstories/acceptance-criteria.md). Cách xử lý dưới đây là [ĐỀ XUẤT] của BA, chưa có người nghiệp vụ duyệt.

| # | Điểm | Cách xử lý | Nơi ghi | Kịch bản |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Bỏ cờ ít dầu mỡ khi còn món Healthy dùng | Chặn | `BR-CAT-020`, `FR-MENU-DISH-007` | AC-MENU-06-3 |
| 2 | Sửa hoặc huỷ giá đã hiệu lực | Chặn, có mã lỗi riêng | `ERR-MENU-409-10`, `FR-MENU-PRC-002` | AC-MENU-21-4 |
| 3 | Ngừng dùng món đang ở thực đơn nháp | Cho ngừng; thực đơn nháp bị chặn khi gửi duyệt | `FR-MENU-DISH-005` | AC-MENU-28-4 |
| 4 | Ngày nghỉ có ngắt chuỗi ngày liên tiếp | Không ngắt | Mục 3.3.1 | AC-MENU-37-3 |
| 5 | Gửi duyệt nhiều mục sinh mấy thông báo | Một thông báo gộp mỗi người duyệt | `BR-MNU-010` | AC-MENU-47-3 |
| 6 | Người gửi có nhận thông báo cho nội dung của mình | Không | `BR-MNU-010` | AC-MENU-47-4 |
| 7 | Lịch sử món 4 tuần tính thực đơn nào | Chỉ `PUBLISHED`, cùng loại suất | `FR-MENU-MNU-006` | AC-MENU-52-3, 52-4 |
| 8 | PDF có chứa giá | Không | `FR-MENU-MNU-008` | AC-MENU-53-4 |
| 9 | Sao chép có mang theo món mặc định | Có | `FR-MENU-MNU-005` | AC-MENU-51-1 |
| 10 | Người thứ hai trả lại | Quyết định của vòng đó mất hiệu lực | `BR-MNU-008` | AC-MENU-50-4 |

**Mười một điểm đưa vào ở v0.3.0.** Nguồn: mục "Chỗ SRS chưa nêu" của [test-cases.md](../test/test-cases.md). Cách xử lý là [ĐỀ XUẤT] của BA, chưa có người nghiệp vụ duyệt.

| # | Điểm | Cách xử lý | Nơi ghi | Test case |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Số có nhiều chữ số thập phân hơn mức lưu được | Từ chối, không tự làm tròn | `BR-CAT-021` | `TC-MENU-B-05`, `TC-MENU-B-07` |
| 2 | Ngày hiệu lực công thức ở quá khứ | Không cho; từ hôm nay trở đi | `BR-CAT-022`, `ERR-MENU-422-21` | `TC-MENU-B-09` |
| 3 | Hai phiên bản công thức cùng ngày hiệu lực | Không cho; phiên bản mới phải có ngày hiệu lực sau | `BR-CAT-022`, `ERR-MENU-422-21` | `TC-MENU-B-09` |
| 4 | Ngưỡng giá loại suất có buộc bội số 100 đồng | Có | `BR-CAT-017` | `TC-MENU-B-12` |
| 5 | Tham số đếm của quy tắc nhận số thập phân | Không; phải là số nguyên | `BR-MNU-007` | `TC-MENU-B-22` |
| 6 | Tham số phân trang ngoài khoảng | Từ chối, không tự chỉnh | SRS nền tảng v0.1.1: `ERR-SYS-422-03` | `TC-MENU-B-26` |
| 7 | Tệp nhập thừa cột, đổi thứ tự cột | Bỏ qua cột lạ kèm cảnh báo; đọc theo tên cột | `BR-CAT-023` (a), (b) | `TC-MENU-X-01` |
| 8 | Dòng trống; số dạng văn bản; dấu thập phân | Bỏ qua dòng trống; đọc số dạng văn bản; nhận cả phẩy và chấm | `BR-CAT-023` (c), (e), (f) | `TC-MENU-X-02` |
| 9 | Món gốc nằm ở dòng sau trong cùng tệp | Chấp nhận | `BR-CAT-023` (g) | `TC-MENU-X-07` |
| 10 | Dòng công thức của một món không liền nhau | Gộp theo tên món | `BR-CAT-023` (g) | `TC-MENU-X-10` |
| 11 | Tệp `.xlsx` nhiều trang tính | Đọc trang đúng tên mẫu, bỏ qua trang khác kèm cảnh báo | `BR-CAT-023` (h) | `TC-MENU-X-14` |

### 4.5 Điểm mở

Giữ nguyên trạng thái mở.

| Mã | Điểm mở | Ai trả lời | FR / BR bị ảnh hưởng |
| :--- | :--- | :--- | :--- |
| O-02 | Một món một định lượng hay nhiều cỡ | Dinh dưỡng viên | `FR-MENU-RCP-007`, `FR-MENU-PRC-001` |
| O-06 | Ai duyệt; ai thay khi vắng | Giám đốc | Mục 2.2; mọi FR duyệt; `BR-MNU-008` |
| DL-01 | Duyệt 43 quy tắc | Người soạn docx | Mục 3.3 |
| H-1, H-3, H-4, H-8 | Danh sách phương pháp ít dầu mỡ, nhóm nguyên liệu, cặp kỵ, phương pháp chế biến | Người soạn docx | `FR-MENU-DISH-007`, `008`, `FR-MENU-ING-005`, `BR-CAT-006` |
| H-2 | "Nhiều ngày liên tiếp" là mấy ngày; thịt lợn có nới không | Người soạn docx | `BR-MENU-012` |
| H-5 | Mức năng lượng/đạm tối thiểu | Dinh dưỡng viên | `BR-MENU-051` |
| E2-Q1 | Cách kiểm ngưỡng giá suất | Dinh dưỡng viên, Giám đốc | `FR-MENU-MNU-004`, `BR-COST-012` |
| E2-Q2 | Quy tắc tuần có xét tuần trước không | Người soạn docx | Mục 3.3.1, `BR-MENU-012`, `013`, `016`, `017` |
| E2-Q3 | Tuần phục vụ gồm những ngày nào | Dinh dưỡng viên | `FR-MENU-MNU-001` |
| E2-Q4 | Thực đơn chung hay riêng theo khách | Dinh dưỡng viên | `BR-MNU-001` |
| E2-Q6 | Dinh dưỡng viên có được rút lại thực đơn đang chờ duyệt để sửa không? (Hiện: không) | Dinh dưỡng viên, người duyệt | `FR-MENU-APV-001`; `UC-MENU-009` |
| E2-Q7 | Người duyệt món, công thức, thực đơn và người duyệt giá bán là một người hay hai người khác nhau? | Giám đốc | Mục 2.2; `UC-MENU-010` |
| E2-Q8 | Có cần thu hồi và sửa **từng ngày** của thực đơn đã công bố, thay vì cả tuần? | Dinh dưỡng viên | `FR-MENU-APV-004`, `005`; `UC-MENU-011` |
| E2-Q9 | Công bố là bước bấm riêng sau khi duyệt, hay tự công bố ngay khi duyệt xong? (Hiện: tách hai bước) | Dinh dưỡng viên | `FR-MENU-APV-003` |
| E2-Q10 | Nhập bảng tính chỉ tạo mới, hay cần cả cập nhật hàng loạt bản ghi đã có? (Hiện: chỉ tạo mới) | Dinh dưỡng viên | `FR-MENU-IMP-003`; `UC-MENU-012` |
| E2-Q11 | Thực đơn đang chờ duyệt có kiểm lại khi quy tắc hoặc thuộc tính món đổi không? (Hiện: giữ kết quả lúc gửi duyệt) | Người duyệt | `FR-MENU-RUL-006`; `UC-MENU-013` |
| E2-Q5 | Khoảng định lượng chuẩn và mức chất độn cho phép lưu ở đâu: theo từng món (chính là `qty_min`–`qty_max` của công thức, khi đó `BR-COST-008` tự thoả), hay có một **bảng chuẩn theo loại nguyên liệu và kiểu món** như bảng trong docx để mọi công thức phải nằm trong đó? | Dinh dưỡng viên | `BR-COST-008`, `009` |

## Phụ thuộc E4/E5: bản thiết kế ngày 11/11/2026

[Dinh dưỡng](../../dinh-duong/srs/spec.md) đọc recipe_items.qty_std và nguồn dinh dưỡng; không dùng COST_AP_HAO_HUT để đổi công thức. [Agent Nội bộ](../../agent-noi-bo/api/api-spec.md) gọi FR-MENU-RUL-002 và API-COST-025 với cùng candidate/version; apply chỉ tạo DRAFT, không tự duyệt/công bố. Adapter MENU và tính nguyên tử chờ AIO-Q06. Đề xuất chỉ trả candidate VALID khi cost không vượt kể cả CANH_BAO (AIO-Q02 còn mở); cổng MENU hiện hành vẫn giữ nguyên. Chưa có API/worker/backend triển khai trong gói này.

## Hồ sơ bổ sung để review ngày 11/11/2026

[Preview toàn hồ sơ](../preview.html) · [API](../api/api-spec.md) · [Luồng tuần tự](flows.md) · [Trạng thái](states.md) · [Gap](../gap-analysis.md). Gói bổ sung không tự đóng câu hỏi, thay quy tắc nghiệp vụ hoặc chứng minh backend đã triển khai. [Bàn giao](../../gia-phat/review/ba-completion-handoff.md).

## Liên kết phụ thuộc E6: bổ sung 11/11/2026

[Gói E6 để review](../../chon-mon-order/preview.html) · [Hợp đồng phụ thuộc](../../chon-mon-order/review/dependencies.md) · [Đối chiếu schema](../../chon-mon-order/srs/data-dictionary.md). E6 giữ nguồn công bố/quyền và quy tắc của phân hệ này; delta chưa merge, không thay gate hoặc chứng minh phần mềm đã triển khai.
