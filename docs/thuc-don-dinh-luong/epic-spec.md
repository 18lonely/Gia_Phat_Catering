# Đặc tả Epic E2: Thực đơn & Định lượng

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `07-prd-epic.md` · BA-Kit v1.0 |
| Epic | E2 · `thuc-don-dinh-luong` |
| Đợt phát hành | R2 · v0.2.0 (đợt Now) |
| Phân hệ | MENU |
| Tính năng PRD | `FEAT-006` → `FEAT-013` |
| Phiên bản | 0.1.0 |
| Trạng thái | Draft |
| Ngày | 2026-11-10 |
| Tài liệu liên quan | [PRD](../gia-phat/01-prd.md) · [Roadmap](../gia-phat/02-roadmap.md) · [Bảng quy tắc thực đơn](../gia-phat/brainstorms/quy-tac-thuc-don.md) · [SRS nền tảng](../nen-tang/srs/spec.md) · [ERD](../nen-tang/srs/erd.md) |

Quy ước: **[D-xx]** đã chốt · **[ĐỀ XUẤT]** chờ duyệt · **[O-xx] / [H-x] / [E2-Qx]** điểm mở, giữ nguyên trạng thái mở.

---

## 1. Thông tin tổng quan

### 1.1 Mục tiêu nghiệp vụ

Sau epic này, dinh dưỡng viên dựng được một thực đơn tuần cho một loại suất trên hệ thống, và hệ thống tự cho biết thực đơn đó vi phạm quy tắc nào trong file quy chuẩn. Thực đơn vi phạm quy tắc cứng không gửi duyệt được; thực đơn chỉ được công bố sau khi một người khác duyệt.

Epic này tạo ra **dữ liệu gốc** mà mọi epic sau đứng trên: cost (E3) cần công thức, dinh dưỡng (E4) cần định lượng, Agent Nội bộ (E5) cần món đã duyệt và bộ kiểm quy tắc, chọn món (E6) cần thực đơn đã công bố và giá bán món.

### 1.2 Đóng góp vào mục tiêu sản phẩm

| Mục tiêu (PRD) | Epic này đóng góp |
| :--- | :--- |
| KR2.1: 100% thực đơn công bố không vi phạm quy tắc cứng | Trực tiếp: bộ kiểm quy tắc và cổng duyệt |
| KR2.2: giảm ≥ 50% thời gian dựng thực đơn | Một phần: kiểm tự động thay cho rà tay; phần còn lại ở E5 |
| KR1.1: 100% ngày có cost ≤ 52% | Gián tiếp: cung cấp công thức và định lượng cho E3 |

### 1.3 Người dùng

| Persona | Làm gì trong epic này |
| :--- | :--- |
| PER-05 Dinh dưỡng viên | Nhập nguyên liệu, món, công thức, giá bán; tạo loại suất; dựng thực đơn; gửi duyệt |
| PER-08 Giám đốc (hoặc người được uỷ quyền, [O-06]) | Duyệt món, công thức, giá bán, thực đơn |
| PER-06 Quản lý cơ sở, bếp trưởng | Xem món, công thức, thực đơn đã công bố |
| PER-07 Kế toán | Xem nguyên liệu và đơn vị để nhập giá ở E3 |

### 1.4 Phạm vi

| Trong epic | Ngoài epic |
| :--- | :--- |
| Danh mục nguyên liệu, nhóm nguyên liệu, phương pháp chế biến, chất gây dị ứng | Giá nhập, cost món, cost suất, bảng dự toán (E3) |
| Món với 12 thuộc tính; cặp món kỵ nhau | 4 chỉ số dinh dưỡng (E4) |
| Công thức có phiên bản, định lượng min–max | Agent dựng thực đơn (E5) |
| Giá bán món | Thực đơn riêng theo công ty khách, hiển thị cho khách, chọn món (E6) |
| Loại suất | Món thay thế khi thiếu hàng (`FEAT-078`) (R11) |
| Thực đơn tuần, món mặc định mỗi ngày | Mục tiêu dinh dưỡng theo nhóm người ăn (R12) |
| Bộ kiểm quy tắc thực đơn | |
| Duyệt và công bố | |
| Nhập dữ liệu gốc từ bảng tính | |

Bảng `menus` có cột `customer_id` từ đầu, nhưng trong R2 chỉ dùng thực đơn chung của loại suất (`customer_id` để trống).

---

## 2. Cấu trúc chi tiết

### 2.1 Phân rã năng lực

Mỗi năng lực ứng với một nhóm `FR-MENU-[FEATURE]-[SEQ]` sẽ viết ở SRS của epic.

#### `FEAT-006` Danh mục nguyên liệu: nhóm FR `FR-MENU-ING`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-ING-01 | Tạo, sửa, huỷ nguyên liệu với đơn vị mua, đơn vị dùng, hệ số quy đổi | P0 | Đơn vị dùng không chỉ có gram: bìa, quả (docx) |
| CAP-ING-02 | Khai tỷ lệ hao hụt; bắt buộc với nguyên liệu có xương, vỏ | P0 | `BR-COST-010` |
| CAP-ING-03 | Quản lý nhóm nguyên liệu chính | P0 | Danh sách khởi tạo: [H-3] |
| CAP-ING-04 | Khai loại bảo quản và độ ổn định nguồn cung | P0 | Dùng ở E3 và `BR-MENU-044` |
| CAP-ING-05 | Khai mùa vụ của rau | P1 | `BR-MENU-018` |
| CAP-ING-06 | Không cho huỷ nguyên liệu đang nằm trong công thức hiệu lực | P0 | `ERR-SYS-409-01` |

#### `FEAT-007` Danh mục món: nhóm FR `FR-MENU-DISH`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-DISH-01 | Tạo, sửa món với đủ 12 thuộc tính phục vụ kiểm quy tắc | P0 | Danh sách thuộc tính ở cuối bảng quy tắc |
| CAP-DISH-02 | Quản lý danh mục phương pháp chế biến, đánh dấu phương pháp chiên và phương pháp ít dầu mỡ | P0 | [H-1], [H-8] |
| CAP-DISH-03 | Gắn món gốc để các biến thể đổi tên vẫn được đếm là một món | P0 | `BR-MENU-014` |
| CAP-DISH-04 | Khai chất gây dị ứng của món | P0 | Hiển thị cho khách ở E6 |
| CAP-DISH-05 | Khai cặp món kỵ nhau | P0 | `BR-MENU-034`; danh sách: [H-4] |
| CAP-DISH-06 | Duyệt món: người duyệt khác người tạo; chỉ món `ACTIVE` vào được thực đơn | P0 | `BR-SEC-008` |
| CAP-DISH-07 | Không cho gắn cờ Healthy nếu phương pháp chế biến không thuộc danh sách ít dầu mỡ | P0 | `BR-MENU-003` |
| CAP-DISH-08 | Ảnh món | P1 | Dùng cho website và cổng khách |
| CAP-DISH-09 | Tìm và lọc món theo vai trò, nhóm nguyên liệu, phương pháp, trạng thái | P0 | Không có |

#### `FEAT-008` Công thức có phiên bản: nhóm FR `FR-MENU-RCP`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-RCP-01 | Tạo công thức: danh sách nguyên liệu, đánh dấu nguyên liệu chính, định lượng sống tối thiểu – tối đa – chuẩn | P0 | Docx ghi khoảng, ví dụ 65–70g |
| CAP-RCP-02 | Duyệt công thức; công thức `ACTIVE` không sửa được | P0 | `BR-SEC-008` |
| CAP-RCP-03 | Tạo phiên bản mới từ phiên bản đang hiệu lực, có ngày hiệu lực | P0 | Phiên bản cũ chuyển `SUPERSEDED` |
| CAP-RCP-04 | So sánh hai phiên bản | P1 | Không có |
| CAP-RCP-05 | Kiểm định lượng nguyên liệu chính nằm trong khoảng chuẩn và chất độn không vượt mức | P0 | `BR-COST-008`, `009` |
| CAP-RCP-06 | Nhiều cỡ định lượng cho một món | Chưa xếp | Phụ thuộc [O-02]; mô hình dữ liệu đã chừa cột `portion_code` |
| CAP-RCP-07 | Món `ACTIVE` phải có ít nhất 1 công thức `ACTIVE` | P0 | Không có |

#### `FEAT-010` Giá bán món: nhóm FR `FR-MENU-PRC`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-PRC-01 | Đặt giá bán cho món, có ngày hiệu lực; giá đã gồm VAT | P0 | [D-15], [D-18] |
| CAP-PRC-02 | Duyệt giá; giá đã hiệu lực không sửa, chỉ thêm giá mới | P0 | Không có |
| CAP-PRC-03 | Xem lịch sử giá của một món | P1 | Không có |

#### `FEAT-009` Loại suất: nhóm FR `FR-MENU-MTY`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-MTY-01 | Tạo loại suất với ngưỡng giá, số món chính đưa ra, số món phụ, có rau, có canh | P0 | [D-20] |
| CAP-MTY-02 | Đánh dấu loại suất công khai | P1 | Dùng ở E8 |
| CAP-MTY-03 | Không cho sửa cơ cấu loại suất đã có thực đơn công bố; phải tạo loại suất mới | P0 | Tránh làm sai thực đơn đã duyệt |

#### `FEAT-011` Thực đơn kỳ: nhóm FR `FR-MENU-MNU`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-MNU-01 | Tạo thực đơn tuần cho một loại suất | P0 | Một thực đơn mỗi loại suất mỗi tuần |
| CAP-MNU-02 | Xếp món vào từng ngày theo vị trí: món chính, món phụ, rau, canh | P0 | Số ô theo cấu hình loại suất |
| CAP-MNU-03 | Chọn món mặc định cho từng ngày trong các món chính | P0 | [D-14] |
| CAP-MNU-04 | Kiểm tổng giá bán của mọi tổ hợp món chính + phụ + rau + canh không vượt ngưỡng giá của loại suất | P0 | `BR-COST-012`; chi tiết: [E2-Q1] |
| CAP-MNU-05 | Sao chép thực đơn từ một tuần trước làm bản nháp | P1 | Không có |
| CAP-MNU-06 | Xem lịch sử món đã dùng 4 tuần gần nhất khi đang dựng | P1 | Hỗ trợ tránh lặp |
| CAP-MNU-07 | Chọn ngày phục vụ trong tuần (bỏ ngày nghỉ) | P0 | Không có |
| CAP-MNU-08 | In hoặc xuất thực đơn tuần | P1 | Không có |

#### `FEAT-012` Bộ kiểm quy tắc: nhóm FR `FR-MENU-RUL`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-RUL-01 | Chạy toàn bộ quy tắc đang áp dụng mỗi khi thực đơn nháp thay đổi; kết quả hiện trong ≤ 2 giây | P0 | Không có |
| CAP-RUL-02 | Quy tắc cứng không đạt → chặn gửi duyệt | P0 | Không có |
| CAP-RUL-03 | Quy tắc mềm không đạt → cảnh báo và trừ điểm; hiện điểm tổng trên thang 100 | P0 | Không có |
| CAP-RUL-04 | Mỗi vi phạm nêu rõ quy tắc nào, ngày nào, món nào | P0 | Ví dụ "Thịt lợn xuất hiện 3 ngày liền: T2, T3, T4" |
| CAP-RUL-05 | Quy tắc mềm–nặng không đạt phải ghi lý do chấp nhận mới gửi duyệt được | P0 | Không có |
| CAP-RUL-06 | Điểm dưới ngưỡng `QUY_TAC_DIEM_TOI_THIEU` → cần người duyệt thứ hai | P1 | Ngưỡng đề xuất 80 |
| CAP-RUL-07 | Quản lý danh mục quy tắc: bật/tắt, sửa con số, đổi loại cứng/mềm, có duyệt | P0 | Con số nằm trong dữ liệu, không trong mã |
| CAP-RUL-08 | Quy tắc "ngày liên tiếp" xét cả ngày cuối của tuần trước | P0 | [E2-Q2] |
| CAP-RUL-09 | Cung cấp bộ kiểm dưới dạng dịch vụ nội bộ để E5 và E9 gọi | P0 | Agent dùng cùng một bộ kiểm với người |

**Quy tắc chạy trong R2**: 31 quy tắc `BR-MENU` và 4 quy tắc `BR-COST` không cần giá nhập (`008`, `009`, `010`, `012`). 8 quy tắc `BR-COST` còn lại cần giá nhập nên bật ở R3. Con số cuối cùng phụ thuộc kết quả duyệt DL-01.

#### `FEAT-013` Duyệt và công bố: nhóm FR `FR-MENU-APV`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-APV-01 | Gửi duyệt thực đơn; người duyệt khác người tạo và người sửa cuối | P0 | `BR-SEC-008` |
| CAP-APV-02 | Duyệt hoặc trả lại kèm lý do | P0 | Không có |
| CAP-APV-03 | Công bố thực đơn đã duyệt; kết quả kiểm quy tắc đóng băng | P0 | Không có |
| CAP-APV-04 | Thu hồi thực đơn đã công bố, bắt buộc lý do | P0 | Ảnh hưởng tới lựa chọn món ở E6: xử lý ở SRS E6 |
| CAP-APV-05 | Sửa thực đơn đã công bố: thu hồi → sửa → kiểm → duyệt lại | P0 | Không sửa trực tiếp |
| CAP-APV-06 | Thông báo cho người duyệt khi có nội dung chờ duyệt, và cho người tạo khi có kết quả | P0 | `FR-SYS-NTF-001` |
| CAP-APV-07 | Chỗ móc để E3 thêm bước kiểm cost trước khi duyệt | P0 | R2 chưa kiểm cost |

#### Nhập dữ liệu gốc: nhóm FR `FR-MENU-IMP`

Không có trong danh mục PRD nhưng cần để nghiệm thu R2 (roadmap DL-03 → DL-05).

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-IMP-01 | Tải mẫu bảng tính cho nguyên liệu, món, công thức, giá bán | P0 | Mẫu cột khớp mô hình dữ liệu |
| CAP-IMP-02 | Nhập từ bảng tính: kiểm từng dòng, báo lỗi theo số dòng, không nhập nếu còn lỗi | P0 | Tất cả hoặc không gì cả |
| CAP-IMP-03 | Dữ liệu nhập vào ở trạng thái chờ duyệt, không tự `ACTIVE` | P0 | `BR-SEC-008` |

### 2.2 Vòng đời các đối tượng chính

| Đối tượng | Trạng thái | Chuyển tiếp |
| :--- | :--- | :--- |
| Món | `DRAFT` → `PENDING` → `ACTIVE` → `INACTIVE` | Gửi duyệt → duyệt → ngừng dùng. Trả lại: `PENDING` → `DRAFT` |
| Công thức | `DRAFT` → `PENDING` → `ACTIVE` → `SUPERSEDED` | Phiên bản mới `ACTIVE` làm phiên bản cũ thành `SUPERSEDED` |
| Giá bán món | `PENDING` → `APPROVED` | Có hiệu lực từ `effective_from` |
| Loại suất | `DRAFT` → `ACTIVE` → `INACTIVE` | Không áp dụng |
| Thực đơn | `DRAFT` → `CHECKED` → `PENDING` → `APPROVED` → `PUBLISHED` → `WITHDRAWN` | `CHECKED` = không còn vi phạm quy tắc cứng. Trả lại: `PENDING` → `DRAFT`. Sửa sau thu hồi: `WITHDRAWN` → `DRAFT` |

Sơ đồ trạng thái đầy đủ viết ở bước `/state`.

### 2.3 Kế hoạch phát hành trong epic

Bốn lát cắt, mỗi lát dùng thử được độc lập. Chưa có ngày: phụ thuộc [O-04].

| Lát | Nội dung | Năng lực | Điều kiện bắt đầu | Tiêu chí xong |
| :--- | :--- | :--- | :--- | :--- |
| R2.1 | Danh mục | `ING-01` → `04`, `06`; `DISH-01` → `07`, `09`; `IMP-01` → `03` (nguyên liệu, món) | R1 xong; [H-3], [H-8] có câu trả lời | Nhập được 30 món và nguyên liệu của chúng từ bảng tính; món chưa duyệt không chọn được ở nơi khác |
| R2.2 | Công thức, giá bán, loại suất | `RCP-01` → `03`, `05`, `07`; `PRC-01`, `02`; `MTY-01`, `03`; `IMP` (công thức, giá) | R2.1 xong; [O-02] có câu trả lời | 30 món có công thức và giá bán đã duyệt; người tạo không tự duyệt được; tạo được loại suất 40.000đ |
| R2.3 | Thực đơn và bộ kiểm | `MNU-01` → `04`, `07`; `RUL-01` → `05`, `07` → `09` | R2.2 xong; DL-01 xong | Mỗi quy tắc được duyệt có ít nhất 1 ca kiểm thử đạt và 1 ca vi phạm; kết quả kiểm hiện trong ≤ 2 giây với thực đơn 6 ngày |
| R2.4 | Duyệt, công bố và phần P1 | `APV-01` → `07`; `RUL-06`; `MNU-05`, `06`, `08`; `ING-05`; `DISH-08`; `RCP-04`; `PRC-03`; `MTY-02` | R2.3 xong; [O-06] có câu trả lời | Thực đơn vi phạm quy tắc cứng không gửi duyệt được; dinh dưỡng viên dựng và công bố được thực đơn thật cho 1 tuần |

Tiêu chí nghiệm thu của cả R2 theo roadmap: đủ 30 món có đủ thuộc tính và công thức đã duyệt; mỗi quy tắc có ca kiểm thử; thực đơn vi phạm quy tắc cứng không gửi duyệt được; công thức không tự duyệt được.

### 2.4 Phụ thuộc

| Phụ thuộc | Loại | Chặn |
| :--- | :--- | :--- |
| R1: tài khoản, phân quyền, nhật ký, tham số, thông báo | Kỹ thuật | Toàn epic |
| DL-01: người soạn docx duyệt 43 quy tắc, trả lời H-1 → H-9 | Nghiệp vụ | R2.1 (H-3, H-8), R2.3 (toàn bộ) |
| DL-03 → DL-05: danh sách nguyên liệu, 30 món, công thức, giá bán | Dữ liệu | Nghiệm thu R2.1, R2.2 |
| [O-02]: một hay nhiều cỡ định lượng | Nghiệp vụ | R2.2 |
| [O-06]: ai duyệt | Nghiệp vụ | R2.4 |

### 2.5 Rủi ro của epic

| Mã | Rủi ro | Giảm thiểu |
| :--- | :--- | :--- |
| E2-R1 | 30 món chưa đủ để dựng thực đơn 6 ngày đạt quy tắc (mỗi ngày cần 3 món chính khác nhóm nguyên liệu, không lặp trong tuần → tối thiểu 18 món chính) | Khi lập DL-04, ưu tiên phủ đủ vai trò và nhóm nguyên liệu trước khi tính tổng số; kiểm lại con số 30 sau khi có danh sách |
| E2-R2 | Quy tắc được duyệt quá chặt, không thực đơn nào đạt | Chạy bộ kiểm trên 4 thực đơn tuần gần nhất của Gia Phát trước khi chốt con số |
| E2-R3 | Gắn thuộc tính món không nhất quán (cùng kiểu món, người gắn "sốt", người gắn "khô") | Có định nghĩa và ví dụ cho từng thuộc tính ngay trên màn hình nhập |
| E2-R4 | Người duyệt là điểm nghẽn mới | Uỷ quyền khi vắng (`FR-AUTH-RBAC-003`); duyệt nhiều bản ghi một lần |

### 2.6 Điểm mở

Giữ nguyên trạng thái mở.

| Mã | Điểm mở | Ai trả lời | Chặn |
| :--- | :--- | :--- | :--- |
| O-02 | Một món một định lượng hay nhiều cỡ | Dinh dưỡng viên | `CAP-RCP-06`, R2.2 |
| O-06 | Ai duyệt món, công thức, giá, thực đơn; ai thay khi vắng | Giám đốc | R2.4 |
| H-1 → H-9 | 9 câu hỏi trong bảng quy tắc | Người soạn docx, kế toán | R2.1, R2.3 |
| E2-Q1 | Kiểm ngưỡng giá suất thế nào: mỗi món chính cộng với **toàn bộ** món phụ, rau, canh của ngày phải ≤ ngưỡng? Hay giá suất là cố định theo loại suất và giá món chỉ dùng khi khách chọn tự do? | Dinh dưỡng viên, Giám đốc | `CAP-MNU-04` |
| E2-Q2 | Quy tắc "không lặp trong tuần" và "ngày liên tiếp" có xét sang tuần trước không? (Thứ Bảy tuần trước và thứ Hai tuần này có tính là liên tiếp không?) | Người soạn docx | `CAP-RUL-08` |
| E2-Q3 | Tuần phục vụ gồm những ngày nào: thứ Hai → thứ Sáu, hay đến thứ Bảy? Có khác nhau giữa các khách không? | Dinh dưỡng viên | `CAP-MNU-07` |
| E2-Q4 | Một loại suất có một thực đơn chung cho mọi khách, hay ngay từ đầu mỗi khách lớn đã có thực đơn riêng? | Dinh dưỡng viên | Phạm vi mục 1.4 |

### 2.7 Bước tài liệu tiếp theo của epic

| Thứ tự | Lệnh | Trạng thái |
| :--- | :--- | :--- |
| 1 | `/prd-epic` | ✅ File này |
| 2 | `/srs` | ✅ [srs/spec.md](srs/spec.md) nháp v0.3.0 (11/11/2026; v0.2.0 thêm 10 điểm từ bước AC, v0.3.0 thêm 11 điểm từ bước test case). Con số từng quy tắc ở mục 3.3 chờ DL-01 |
| 3 | `/usecase-diagram` → `/usecase` | ✅ [Sơ đồ](srs/usecase-diagram.md) + 13 use case `UC-MENU-001` → `013` trong `usecases/`, nháp v0.1.0 (10/11/2026). Phát sinh 6 điểm mở E2-Q6 → Q11, ghi ở SRS mục 4.5 |
| 4 | `/user-flow` | ✅ [ui/user-flow.md](ui/user-flow.md) nháp v0.1.0 (10/11/2026): 16 màn hình, 6 luồng, 69 tình huống |
| 5 | `/state` | Viết được ngay từ mục 2.2 |
| 6 | `/api-design` | Sau SRS |
| 7 | `/wireframe-html` | Đang làm: ✅ [`SCR-MENU-10` Soạn thực đơn tuần](html-wireframe/soan-thuc-don-tuan.html) (10/11/2026). ✅ [`SCR-MENU-13`, `14` Chờ duyệt và Chi tiết duyệt](html-wireframe/cho-duyet.html) (10/11/2026). ✅ [`SCR-MENU-05`, `06`, `02` Chi tiết món, Soạn công thức, Form nguyên liệu](html-wireframe/chi-tiet-mon.html) (10/11/2026). Chưa dựng 10 màn hình còn lại: `01`, `03`, `04`, `07`, `08`, `09`, `11` (đã có trong màn soạn thực đơn), `12`, `15`, `16` |
| 8 | `/userstory` → `/ac` | ✅ [userstories/backlog.md](userstories/backlog.md) nháp v0.1.0 (10/11/2026): 53 story, 44 P0, 160 điểm sơ bộ. ✅ [userstories/acceptance-criteria.md](userstories/acceptance-criteria.md) nháp v0.1.0 (10/11/2026): 239 kịch bản; bộ kịch bản cho từng quy tắc thực đơn chờ DL-01; 10 điểm phát sinh chưa đưa vào SRS |
| 9 | `/test-checklist` → `/test-cases` | ✅ [test/checklist.md](test/checklist.md) nháp v0.1.0 (11/11/2026): 208 đề mục ở 9 nhóm, kèm ma trận truy vết 55 FR. ✅ [test/test-cases.md](test/test-cases.md) nháp v0.1.0 (11/11/2026): 335 test case (239 chức năng sinh từ AC + 96 bổ sung). Chưa có: test case từng quy tắc thực đơn (chờ DL-01), test case giao diện |

## 3. Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-10 | BA | Khởi tạo |
