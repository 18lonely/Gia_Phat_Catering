# Đặc tả Epic E3 (Cost)

## Metadata

| Trường | Giá trị |
| :--- | :--- |
| Template | `07-prd-epic.md` · BA-Kit v1.0 |
| Epic | E3 · `cost` |
| Đợt phát hành | R3 · v0.3.0 (đợt Now) |
| Phân hệ | COST |
| Tính năng PRD | `FEAT-014` → `FEAT-018` |
| Phiên bản | 0.6.0 |
| Trạng thái | Draft: **cách tính cost chưa chốt**: 4 điểm mở ở mục 2.6 quyết định công thức |
| Ngày | 2026-11-11 |
| Tài liệu liên quan | [PRD](../gia-phat/01-prd.md) · [Roadmap](../gia-phat/02-roadmap.md) · [Bảng quy tắc](../gia-phat/brainstorms/quy-tac-thuc-don.md) (nhóm G) · [SRS epic thực đơn](../thuc-don-dinh-luong/srs/spec.md) · [ERD](../nen-tang/srs/erd.md) (mục 5) · `Yêu cầu về thực đơn và cost tp.docx` (phần "Quy chuẩn kiểm soát cost") |

Quy ước: **[D-xx]** đã chốt · **[ĐỀ XUẤT]** chờ duyệt · **[O-xx] / [H-x] / [E3-Qx]** điểm mở, giữ nguyên trạng thái mở.

---

## 1. Thông tin tổng quan

### 1.1 Mục tiêu nghiệp vụ

Sau epic này, khi dinh dưỡng viên dựng một thực đơn, hệ thống cho biết **mỗi ngày tốn bao nhiêu tiền nguyên liệu trên một suất và chiếm bao nhiêu phần trăm giá bán**, dựa trên giá nhập do kế toán nhập. Thực đơn có ngày vượt ngưỡng (mặc định 52%) không gửi duyệt được khi chế độ `CHAN`; chế độ chạy thử `CANH_BAO` chỉ cảnh báo. Mặc định `CANH_BAO` là đề xuất của SRS, cần xác nhận trước áp dụng. Khi giá nhập đổi làm một thực đơn đã duyệt vượt ngưỡng, người phụ trách được báo.

Đây là yêu cầu trung tâm của phần "Quy chuẩn kiểm soát cost" trong file docx: *"Kiểm tra tổng cost trước khi chốt thực đơn và chuyển bếp triển khai."*

### 1.2 Đóng góp vào mục tiêu sản phẩm

| Mục tiêu (PRD) | Epic này đóng góp |
| :--- | :--- |
| KR1.1: 100% ngày phục vụ có cost dự toán ≤ 52% | Trực tiếp: tính cost và chặn ở bước gửi duyệt |
| KR1.2: chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm | Một nửa: epic này tạo ra **dự toán**; số thực mua có ở R11 |
| KR2.2: giảm thời gian dựng thực đơn | Gián tiếp: thay bảng tính cost làm tay |

### 1.3 Người dùng

| Persona | Làm gì trong epic này |
| :--- | :--- |
| PER-07 Kế toán (mua hàng) | Quản lý nhà cung cấp; nhập và cập nhật giá nhập; xem bảng dự toán |
| PER-05 Dinh dưỡng viên | Xem cost món, cost suất, cost % khi dựng thực đơn; lập bảng tính cost cho món đặc thù; xử lý cảnh báo |
| PER-08 Giám đốc | Duyệt ngưỡng cost; xem cost % theo ngày; quyết định khi thực đơn vượt ngưỡng ([E3-Q9]) |
| PER-06 Quản lý cơ sở | Xem bảng dự toán của cơ sở mình |
| Agent Nội bộ (từ R5) | Gọi dịch vụ tính cost để dựng thực đơn trong ngưỡng |
| Agent Dinh dưỡng viên (từ R9) | **Không** truy cập giá nhập và cost; chỉ nhận câu trả lời "đạt / không đạt ngân sách" |

### 1.4 Phạm vi

| Trong epic | Ngoài epic |
| :--- | :--- |
| Danh mục nhà cung cấp (tối thiểu: tên, loại, liên hệ) | Đơn mua, nhận hàng, công nợ nhà cung cấp (R11) |
| Giá nhập theo nguyên liệu × nhà cung cấp × cơ sở × ngày hiệu lực | Giá nhập tự cập nhật từ phiếu nhận hàng (R11) |
| Nhập giá từ bảng tính | Đối chiếu dự toán với thực mua (`FEAT-076`) (R11) |
| Cost món theo công thức hiệu lực | Chi phí nhân công, gas, điện, khấu hao; lợi nhuận theo khách (R13) |
| Cost suất, cost % theo ngày, so với ngưỡng | Số suất thật từ order: R6 (R3 dùng số suất dự kiến nhập tay, [E3-Q8]) |
| Bảng dự toán theo docx mục IV | Agent rà soát thực đơn khi giá đổi (`FEAT-082`) (R12) |
| 8 quy tắc `BR-COST` cần giá nhập, đăng ký vào bộ kiểm quy tắc của E2 | |
| Bước kiểm cost ở cổng gửi duyệt thực đơn | |
| Cảnh báo giá cũ và cảnh báo thực đơn vượt ngưỡng do giá đổi | |
| Bảng tính cost riêng cho món đặc thù | |
| Dịch vụ "đạt / không đạt ngân sách" cho agent phía khách | |

---

## 2. Cấu trúc chi tiết

### 2.1 Công thức tính: phương án đang đề xuất

Viết lại từ ERD mục 5.3, bổ sung các lựa chọn cần quyết. **Chưa phải công thức chính thức.**

```text
Giá 1 đơn vị dùng      = giá nhập tham chiếu ÷ hệ số quy đổi của nguyên liệu
Cost 1 dòng công thức  = định lượng chuẩn × giá 1 đơn vị dùng
Cost món               = Σ cost các dòng có cờ "tính vào cost"

Cost suất của ngày     = cost phần món chính                    ← [E3-Q1]
                       + Σ cost món phụ + cost rau + cost canh
                       + các khoản khoán trên một suất          ← [O-01]

Doanh thu chưa VAT     = giá suất ÷ (1 + VAT%)                  ← [O-01]
Cost %                 = cost suất của ngày ÷ doanh thu chưa VAT × 100
Đạt khi                Cost % ≤ ngưỡng (tham số COST_NGUONG_PCT, mặc định 52)
```

Bốn chỗ chưa chốt làm kết quả khác nhau:

| Chỗ chưa chốt | Các phương án | Ảnh hưởng |
| :--- | :--- | :--- |
| **Cost phần món chính** khi mỗi người chọn 1 trong 3 món có cost khác nhau [E3-Q1] | (a) Lấy món đắt nhất · (b) Bình quân 3 món · (c) Bình quân theo tỷ lệ chọn dự kiến · (d) Lấy món mặc định | (a) an toàn nhất, chặn nhiều thực đơn nhất. (b), (d) đơn giản nhưng có thể vượt ngưỡng thật nếu nhiều người chọn món đắt. (c) sát nhất nhưng cần dữ liệu lựa chọn, chỉ có sau R6 |
| **Tỷ lệ hao hụt** [E3-Q2] | Định lượng trong docx là "món sống" đầu vào: (a) đã gồm xương, vỏ → không cộng thêm · (b) là phần ăn được → phải chia cho (1 − hao hụt) | Với gà, sườn, cá (hao hụt lớn) hai cách lệch nhau hàng chục phần trăm cost món |
| **Thành phần cost và VAT** [O-01] | Gạo, gia vị, dầu ăn, tráng miệng, hộp/khay có tính không; tính trực tiếp hay khoán một số tiền mỗi suất; thuế suất VAT; giá nhập có gồm VAT đầu vào không | Dịch chuyển cả tử số lẫn mẫu số của cost % |
| **Giá tham chiếu** khi một nguyên liệu có nhiều nhà cung cấp [E3-Q4] | (a) Kế toán đánh dấu một giá · (b) Giá mới nhất · (c) Giá thấp nhất · (d) Bình quân | Quyết định cost có "nhảy" khi thêm một báo giá mới hay không |

### 2.2 Phân rã năng lực

Mỗi nhóm ứng với một nhóm `FR-COST-[FEATURE]-[SEQ]` sẽ viết ở SRS của epic.

#### `FEAT-014` Bảng giá nhập: nhóm FR `FR-COST-SUP`, `FR-COST-PRC`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-SUP-01 | Tạo, sửa, ngừng nhà cung cấp: tên, loại (thường xuyên / tiểu thương), liên hệ | P0 | Bản tối thiểu; mở rộng ở R11 |
| CAP-PRC-01 | Nhập giá nhập cho một nguyên liệu: nhà cung cấp, giá trên một đơn vị mua, ngày hiệu lực, cơ sở áp dụng (hoặc cả hai cơ sở) | P0 | [D-13]; không sửa đè, giá mới là dòng mới |
| CAP-PRC-02 | Xác định giá tham chiếu dùng để tính cost | P0 | Cách chọn: [E3-Q4] |
| CAP-PRC-03 | Nhập giá cho nhiều nguyên liệu trên một màn hình dạng lưới | P0 | Kế toán cập nhật hàng chục giá mỗi lần đi chợ |
| CAP-PRC-04 | Nhập giá từ bảng tính, theo quy ước `BR-CAT-023` | P0 | Dùng lại khung nhập của E2 |
| CAP-PRC-05 | Đính kèm ảnh chứng từ cho một lần nhập giá | P1 | Chứng từ tiểu thương viết tay |
| CAP-PRC-06 | Xem lịch sử giá của một nguyên liệu theo thời gian và nhà cung cấp | P0 | Docx: "theo dõi giá nhập thực tế" |
| CAP-PRC-07 | Cảnh báo nguyên liệu có giá quá cũ | P0 | `BR-COST-005`; ngưỡng theo loại bảo quản là tham số |
| CAP-PRC-08 | Danh sách nguyên liệu đang dùng trong công thức hiệu lực nhưng **chưa có giá** | P0 | Thiếu giá thì không tính được cost |
| CAP-PRC-09 | Cảnh báo khi giá mới lệch quá X% so với giá trước | P1 | Bắt lỗi gõ nhầm (25.000 thành 250.000); X là tham số |
| CAP-PRC-10 | Có cần người thứ hai duyệt giá nhập không | Chưa xếp | [E3-Q6] |

#### `FEAT-015` Cost món: nhóm FR `FR-COST-DISH`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-DISH-01 | Tính cost một món theo công thức hiệu lực và giá tham chiếu tại một ngày, một cơ sở | P0 | Công thức ở mục 2.1 |
| CAP-DISH-02 | Hiện bảng phân rã cost món: từng nguyên liệu, định lượng, giá, thành tiền, tỷ trọng | P0 | Docx mục III: "phân bổ cost hợp lý giữa nguyên liệu chính và phụ" |
| CAP-DISH-03 | Khi thiếu giá của một nguyên liệu: không trả cost, nêu rõ nguyên liệu nào thiếu | P0 | Không tính cost thiếu thành phần |
| CAP-DISH-04 | So sánh cost của hai phiên bản công thức | P1 | Hỗ trợ quyết định khi tạo phiên bản mới |
| CAP-DISH-05 | Hiện cost món trong danh sách món và trong hộp chọn món khi dựng thực đơn | P0 | Chỉ cho vai trò có quyền xem cost |
| CAP-DISH-06 | Bảng tính cost riêng cho món đặc thù: lập, gửi duyệt, duyệt; món đặc thù chưa có bảng tính đã duyệt thì không vào được thực đơn | P0 | `BR-COST-007` |
| CAP-DISH-07 | Gợi ý nhóm cost (thấp / cao) của món từ cost đã tính | P1 | Thay cho việc gắn tay; ngưỡng phân nhóm: [E3-Q7] |

#### `FEAT-016` Cost suất và ngưỡng: nhóm FR `FR-COST-MEAL`, `FR-COST-RUL`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-MEAL-01 | Tính cost suất và cost % của từng ngày trong thực đơn | P0 | [E3-Q1], [O-01] |
| CAP-MEAL-02 | Hiện cost % từng ngày ngay trên màn hình soạn thực đơn, cập nhật sau mỗi lần đổi món | P0 | Cùng nhịp với bảng kiểm quy tắc |
| CAP-MEAL-03 | Hiện phân rã cost của một ngày: phần món chính, từng món phụ, rau, canh, khoản khoán | P0 | Để biết đổi món nào thì hạ được cost |
| CAP-MEAL-04 | Quản lý các khoản khoán trên một suất (ví dụ gia vị, dầu ăn) dưới dạng tham số có ngày hiệu lực | P0 | Danh sách khoản: [O-01] |
| CAP-MEAL-05 | Đăng ký bước kiểm cost vào cổng gửi duyệt thực đơn của E2: ngày nào vượt ngưỡng thì chặn ở `CHAN`, chỉ cảnh báo ở `CANH_BAO` | P0 | Qua chỗ móc `FR-MENU-APV-006`; `BR-COST-001` |
| CAP-MEAL-06 | Chụp lại cost % và giá đã dùng khi thực đơn được duyệt | P0 | Kết quả đã duyệt không đổi khi giá đổi sau |
| CAP-MEAL-07 | Ngoại lệ khi vượt ngưỡng | Chưa xếp | Chặn tuyệt đối hay Giám đốc duyệt ngoại lệ: [E3-Q9] |
| CAP-MEAL-08 | Chế độ kiểm `CANH_BAO` / `CHAN`; mặc định đề xuất `CANH_BAO`, chuyển sang chặn cần Giám đốc duyệt | P0 | `FR-COST-MEAL-008`; E3-R4; không miễn lỗi thiếu giá/VAT |
| CAP-RUL-01 | Đăng ký 8 quy tắc `BR-COST-001` → `007`, `011` vào bộ kiểm quy tắc | P0 | Con số chờ DL-01 |
| CAP-RUL-02 | Quy tắc cân đối: món chính cost cao đi với món phụ cost thấp | P1 | `BR-COST-006`; định nghĩa "cao", "thấp": [E3-Q7] |
| CAP-RUL-03 | Dịch vụ "đạt / không đạt ngân sách" cho agent phía khách: nhận một thực đơn, trả đúng một giá trị có/không cho mỗi ngày | P0 | Không trả con số; `BR-SEC-010` |

#### `FEAT-017` Bảng dự toán: nhóm FR `FR-COST-EST`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-EST-01 | Lập bảng dự toán cho một ngày của thực đơn với số suất cho trước: tên nguyên liệu, giá nhập, định lượng trên một suất, số suất, tổng chi phí | P0 | Đủ 5 cột của docx mục IV |
| CAP-EST-02 | Nhập số suất dự kiến theo từng món chính | P0 | R3 chưa có order; nguồn số suất: [E3-Q8] |
| CAP-EST-03 | Gộp dự toán theo nguyên liệu cho cả tuần | P0 | Một nguyên liệu dùng ở nhiều món, nhiều ngày |
| CAP-EST-04 | Dự toán theo cơ sở, dùng giá của cơ sở đó | P0 | Hai cơ sở có thể mua giá khác nhau |
| CAP-EST-05 | Quy đổi tổng định lượng sang đơn vị mua (gram → kg; có tính hao hụt nếu áp dụng) | P0 | [E3-Q2] |
| CAP-EST-06 | Xuất bảng dự toán ra bảng tính và PDF | P1 | Không có |
| CAP-EST-07 | Lưu bảng dự toán kèm thời điểm và giá đã dùng; lập lại thì tạo bản mới | P0 | Để đối chiếu với thực mua ở R11 |

#### `FEAT-018` Cảnh báo khi giá biến động: nhóm FR `FR-COST-ALR`

| Mã | Năng lực | Ưu tiên | Ghi chú |
| :--- | :--- | :---: | :--- |
| CAP-ALR-01 | Khi có giá mới, tính lại cost % của mọi thực đơn đã duyệt hoặc đã công bố còn ngày phục vụ từ hôm nay trở đi | P1 | Chạy nền |
| CAP-ALR-02 | Thực đơn nào có ngày vượt ngưỡng do giá mới thì báo dinh dưỡng viên và Giám đốc | P1 | `BR-COST-011` |
| CAP-ALR-03 | Màn hình liệt kê thực đơn bị ảnh hưởng: ngày, cost % cũ → mới, nguyên liệu gây ra | P1 | Không có |
| CAP-ALR-04 | "Chặn chuyển bếp cho đến khi xử lý" | Chưa xếp | Docx yêu cầu rà soát trước khi triển khai; R3 chưa có bước chuyển bếp: làm ở R6 hay R11: [E3-Q10] |
| CAP-ALR-05 | Xem trước: nếu đổi giá nguyên liệu X thành Y thì những thực đơn nào vượt ngưỡng | P2 | Hỗ trợ đàm phán giá |

### 2.3 Quyền xem cost

Giá nhập và cost là dữ liệu nội bộ nhạy cảm. Đề xuất, chi tiết ở SRS:

| Dữ liệu | Dinh dưỡng viên | Kế toán | Giám đốc | Quản lý cơ sở | Bếp trưởng | Agent Nội bộ | Agent phía khách |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Giá nhập | Xem | Nhập | Xem | Xem (cơ sở mình) | Không | Theo người dùng | **Không** |
| Cost món, cost suất, cost % | Xem | Xem | Xem | Xem (cơ sở mình) | Không | Theo người dùng | **Không** |
| Bảng dự toán | Lập | Xem | Xem | Xem (cơ sở mình) | Xem số lượng, không xem giá | Theo người dùng | **Không** |
| "Đạt / không đạt ngân sách" | Không | Không | Không | Không | Không | Không | Có |

Bếp trưởng có được xem giá không: [E3-Q11].

### 2.4 Kế hoạch phát hành trong epic

Chưa có ngày: phụ thuộc [O-04].

| Lát | Nội dung | Năng lực | Điều kiện bắt đầu | Tiêu chí xong |
| :--- | :--- | :--- | :--- | :--- |
| R3.1 | Giá nhập | `SUP-01`; `PRC-01` → `04`, `06`, `08` | R2.1 xong (có nguyên liệu); [E3-Q4] có câu trả lời; DL-06 (bảng giá hiện hành) | 100% nguyên liệu của 30 món đầu tiên có giá tham chiếu cho cả hai cơ sở |
| R3.2 | Cost món | `DISH-01` → `03`, `05`, `06` | R3.1 và R2.2 xong; [E3-Q2] có câu trả lời | Cost của10 món mẫu lệch không quá1 đồng so với tính tay, theo NFR-COST-002 |
| R3.3 | Cost suất, ngưỡng, quy tắc | `MEAL-01` → `06`; `RUL-01`, `03` | R3.2 và R2.4 xong; [O-01], [E3-Q1] có câu trả lời; DL-01 xong | Cost% của10 ngày mẫu lệch không quá0,01 điểm phần trăm theo NFR-COST-002; ở CHAN vượt ngưỡng chặn gửi duyệt, ở CANH_BAO chỉ cảnh báo; thiếu đầu vào vẫn chặn; tài khoản agent phía khách không đọc được bảng giá và cost |
| R3.4 | Dự toán, cảnh báo, phần P1 | `EST-01` → `07`; `ALR-01` → `03`; `PRC-05`, `07`, `09`; `DISH-04`, `07`; `RUL-02` | R3.3 xong | Bảng dự toán có đủ 5 cột của docx; đổi giá làm một thực đơn mẫu vượt ngưỡng thì người phụ trách nhận cảnh báo trong ≤ 5 phút |

Tiêu chí nghiệm thu R3 đồng bộ NFR-COST-002:10 món lệch không quá1đ,10 ngày cost% lệch không quá0,01 điểm phần trăm so với kế toán. CHAN chặn gửi duyệt khi vượt; CANH_BAO cảnh báo, không miễn lỗi thiếu dữ liệu. Công bố theo cổng MENU hiện có, không suy ra lệnh cấm Cost tuyệt đối. Dự toán đủ các cột SRS EST004.

### 2.5 Phụ thuộc và rủi ro

| Phụ thuộc | Loại | Chặn |
| :--- | :--- | :--- |
| R2: nguyên liệu, công thức, thực đơn, bộ kiểm quy tắc, chỗ móc gửi duyệt | Kỹ thuật | Toàn epic |
| DL-02: kế toán xác nhận VAT và thành phần cost ([O-01]) | Nghiệp vụ | R3.3 |
| DL-06: bảng giá nhập hiện hành theo nhà cung cấp | Dữ liệu | Nghiệm thu R3.1 |
| DL-01: con số của 8 quy tắc cost | Nghiệp vụ | R3.3 |
| Bảng tính cost tay của kế toán cho 10 món và 10 ngày mẫu | Dữ liệu | Nghiệm thu R3.2, R3.3 |

| Mã | Rủi ro | Giảm thiểu |
| :--- | :--- | :--- |
| E3-R1 | Giá nhập không được cập nhật đều → cost đúng công thức nhưng sai thực tế | `CAP-PRC-07` cảnh báo giá cũ; hiện ngày của giá cũ nhất ngay cạnh cost %; dashboard số nguyên liệu quá hạn cập nhật |
| E3-R2 | Kế toán thêm việc nhập giá hằng ngày ngoài Sheets và MISA | `CAP-PRC-03` nhập dạng lưới; `CAP-PRC-04` nhập từ bảng tính; cân nhắc bỏ sheet giá cũ sau khi chạy song song |
| E3-R3 | Hệ thống tính ra cost % khác con số Gia Phát vẫn tính lâu nay, do định nghĩa khác | Chốt [O-01], [E3-Q1], [E3-Q2] bằng cách **tính lại 10 ngày thật gần đây theo từng phương án** rồi so với số của kế toán |
| E3-R4 | Ngưỡng 52% áp vào làm đa số thực đơn hiện tại không đạt | Chạy thử trên 4 thực đơn tuần gần nhất trước khi bật chặn; có giai đoạn chỉ cảnh báo, chưa chặn |
| E3-R5 | Lộ cost ra cổng khách hoặc qua agent | `BR-SEC-010`: chặn ở quyền cơ sở dữ liệu và ở tầng công cụ; dịch vụ ngân sách chỉ trả có/không; kiểm thử riêng |
| E3-R6 | Dịch vụ "đạt / không đạt" bị dò ngược ra cost bằng cách thử nhiều thực đơn | Giới hạn số lần gọi; cân nhắc trả kết quả theo cả thực đơn thay vì từng ngày |

### 2.6 Điểm mở

Giữ nguyên trạng thái mở. Bốn điểm in đậm quyết định công thức ở mục 2.1.

| Mã | Điểm mở | Ai trả lời | Chặn |
| :--- | :--- | :--- | :--- |
| **O-01** | Cost gồm những khoản nào; khoản nào khoán; thuế suất VAT; giá nhập có gồm VAT đầu vào không | Kế toán | `CAP-MEAL-01`, `04`; R3.3 |
| **E3-Q1** | Cost phần món chính tính thế nào khi 3 món có cost khác nhau: món đắt nhất, bình quân, theo tỷ lệ chọn, hay món mặc định | Giám đốc, kế toán | `CAP-MEAL-01`; R3.3 |
| **E3-Q2** | Định lượng "món sống" trong docx đã gồm xương, vỏ chưa: tức có nhân thêm hao hụt khi tính cost và khi tính lượng mua không | Người soạn docx, bếp trưởng | `CAP-DISH-01`, `CAP-EST-05`; R3.2 |
| **E3-Q4** | Một nguyên liệu có nhiều nhà cung cấp thì giá nào dùng để tính cost | Kế toán | `CAP-PRC-02`; R3.1 |
| E3-Q3 | Hai cơ sở có mua giá khác nhau không; nếu có, kiểm ngưỡng theo cơ sở nào khi một thực đơn dùng chung cho cả hai | Kế toán | `CAP-EST-04`, `CAP-MEAL-01` |
| E3-Q5 | Tần suất cập nhật giá thực tế: hằng ngày theo chợ, hằng tuần, hay khi nhà cung cấp báo giá | Kế toán | `CAP-PRC-07`; rủi ro E3-R1 |
| E3-Q6 | Giá nhập do kế toán nhập có cần người thứ hai duyệt không | Giám đốc | `CAP-PRC-10` |
| E3-Q7 | "Cost cao", "cost thấp" của `BR-COST-006` xác định thế nào: theo ngưỡng tiền, theo phần trăm giá suất, hay gắn tay như hiện nay | Người soạn docx | `CAP-RUL-02`, `CAP-DISH-07` |
| E3-Q8 | Trước khi có order (R6), số suất trong bảng dự toán lấy từ đâu | Dinh dưỡng viên | `CAP-EST-02` |
| E3-Q9 | Thực đơn vượt ngưỡng: chặn tuyệt đối, hay Giám đốc được duyệt ngoại lệ có lý do | Giám đốc | `CAP-MEAL-07` |
| E3-Q10 | "Chặn chuyển bếp" khi thực đơn đã duyệt vượt ngưỡng do giá đổi: hiện thực ở đợt nào, và có thật sự chặn hay chỉ cảnh báo | Giám đốc | `CAP-ALR-04` |
| E3-Q11 | Bếp trưởng có được xem giá nhập và cost không | Giám đốc | Mục 2.3 |
| DL-01 | Con số của `BR-COST-001` → `007`, `011` | Người soạn docx, kế toán | `CAP-RUL-01` |

**Cách chốt nhanh bốn điểm in đậm** [ĐỀ XUẤT]: lấy 10 ngày phục vụ thật gần đây, với mỗi ngày tính cost % theo từng tổ hợp phương án, đặt cạnh con số kế toán đã tính. Phương án nào khớp con số đang dùng thì đó là định nghĩa hiện hành của Gia Phát; nếu không phương án nào khớp thì đây là lúc phát hiện cách tính hiện tại đang thiếu hoặc thừa khoản gì.

### 2.7 Bước tài liệu tiếp theo của epic

| Thứ tự | Lệnh | Trạng thái |
| :--- | :--- | :--- |
| 1 | `/prd-epic` | ✅ File này |
| 2 | `/srs` | ✅ [srs/spec.md](srs/spec.md) nháp v0.3.0: 45 FR, 24 quy tắc, 14 mã lỗi. Đã đồng bộ 9/9 mục phụ thuộc; ERD/DBML v0.3.0. Các lựa chọn nghiệp vụ và E3-Q14 → Q16 vẫn mở. |
| 3 | `/usecase-diagram` → `/usecase` | ✅ [Sơ đồ và 16 use case](srs/usecase-diagram.md), nháp v0.1.0: 43 FR có luồng, 2 FR hoãn được ghi rõ |
| 4 | `/user-flow` | ✅ [User flow](ui/user-flow.md), nháp v0.1.1: 18 màn đề xuất, 7 luồng chính, 10 câu hỏi cần review |
| 5 | `/api-design` | ✅ [API v0.1.0](api/api-spec.md): 37 endpoint đề xuất, hook nội bộ và truy vết 45 FR; chưa triển khai |
| 6 | `/wireframe-html` | ✅ [18 màn tương tác](html-wireframe/cost-workbench.html), dữ liệu giả; [kiểm tra](validation/api-wireframe-report.md) |
| 7 | `/userstory` → `/ac` | ✅ [28 story](userstories/backlog.md), [108 AC](userstories/acceptance-criteria.md) nháp; giữ P0/P1/P2 và điểm mở |
| 8 | `/test-checklist` → `/test-cases` | ✅ [Checklist](test/checklist.md), [108 test case](test/test-cases.md), [RTM](test/traceability.md) nháp; BA/QA chưa ký duyệt, chưa chạy backend |

## 3. Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.6.0 | 2026-11-11 | BA | Đồng bộ tiêu chí đối soát với NFR-COST-002, điều kiện CHAN/CANH_BAO và thiết kế kế toán mở rộng. |
| 0.5.0 | 2026-11-11 | BA | Bổ sung kế toán theo xác nhận người dùng và CR tác động VAT/chiết khấu; không tự mở phạm vi triển khai đơn/thanh toán. |
| 0.4.1 | 2026-11-11 | BA | Liên kết gói review, dữ liệu đối soát giả định và phiếu kế toán; điểm mở giữ nguyên. |
| 0.4.0 | 2026-11-11 | BA | Bổ sung backlog/AC/test và truy vết; ghi rõ NOT RUN/BLOCKED, chưa nghiệm thu. |
| 0.3.0 | 2026-11-11 | BA | Thêm API và wireframe Cost để review; giữ các điểm mở và giới hạn mô phỏng. |
| 0.2.0 | 2026-11-11 | BA | Đồng bộ CAP-MEAL-08 (chỉ cảnh báo) từ SRS; liên kết mô hình dữ liệu Cost; chưa chốt công thức. |
| 0.2.1 | 2026-11-11 | BA | Cập nhật trạng thái hoàn thành nháp use case/user flow và liên kết SRS v0.1.2. |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo |

Mô hình dữ liệu đã đồng bộ: [ERD mục 5.4](../nen-tang/srs/erd.md) · [schema DBML](../nen-tang/srs/schema.dbml). Các điểm mở bổ sung E3-Q14 → Q16 xem [SRS mục 4.5](srs/spec.md).

Gói review tiếp theo: [bàn giao](review/handoff.md), [sổ quyết định](review/decision-register.md), [gap analysis](gap-analysis.md). Dữ liệu đối soát hiện là mẫu giả định; không thay bảng tính kế toán cho NFR-COST-002.

## Bổ sung kế toán

[Quy tắc đã xác nhận và phần mở](accounting/business-rules.md) · [CR tác động](cr/CR-COST-2026-001.md) · [Hướng dẫn](user-guide.md). Mục2.4 đã đồng bộ tiêu chí cụ thể NFR-COST-002 và điều kiện chế độ; còn cần stakeholder review bản bàn giao, chưa nghiệm thu phần mềm.
