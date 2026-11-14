# Product Requirements Document (PRD): Nền tảng Gia Phát

## Metadata

- **Product Name**: Nền tảng Gia Phát (website công khai · cổng khách hàng và người ăn · quản trị nội bộ · 2 AI agent)
- **Document Version**: 0.1.3
- **Status**: Draft
- **Product Owner**: [Chưa chỉ định, phụ thuộc điểm mở O-06]
- **Lead BA**: [Chưa chỉ định]
- **Last Updated**: 2026-11-14
- **Tài liệu liên quan**: [BRD](06-brd.md) · [URD](05-urd.md) · [Kế hoạch tổng thể](00-ke-hoach-tong-the.md) · [Bảng quy tắc thực đơn](brainstorms/quy-tac-thuc-don.md)

### Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Tóm tắt thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.3 | 2026-11-14 | BA | Ràng buộc công nghệ mục 5 đổi sang Rust/Axum theo D-22, CR-CORE-2026-001; không đổi tính năng |
| 0.1.2 | 2026-11-11 | BA | Liên kết hồ sơ bổ sung E1–E5/E6 khởi đầu; giữ quy tắc và điểm mở |
| 0.1.1 | 2026-11-11 | BA | Liên kết gói BA nháp E4/E5, ghi gate còn mở; không thay phạm vi hay nghiệm thu release |
| 0.1.0 | 2026-11-10 | BA | Khởi tạo từ BRD v0.1.0, URD v0.1.0 và các quyết định D-01 → D-21 |

Quy ước: **[D-xx]** = quyết định đã chốt trong kế hoạch tổng thể · **[ĐỀ XUẤT]** = chờ duyệt · **[O-xx]** = điểm mở, giữ nguyên trạng thái mở.

---

## 1. Tầm nhìn & Mục tiêu sản phẩm

### 1.1 Tuyên ngôn sứ mệnh

Dành cho **doanh nghiệp mua suất ăn tập thể và nhân viên của họ**, những người hiện không biết trước mình ăn gì, bao nhiêu gram, giá trị dinh dưỡng thế nào và không được chọn món; và dành cho **đội vận hành Gia Phát**, những người đang kiểm quy chuẩn thực đơn và cost bằng tay trên Word, Sheets, Zalo.

Nền tảng Gia Phát là **một hệ thống đặt suất ăn minh bạch**: mỗi món công khai định lượng, dinh dưỡng, dị ứng và giá bán; từng người ăn tự chọn món trong định mức công ty; mọi thực đơn đều được máy kiểm theo quy chuẩn và ngưỡng cost trước khi công bố; hai AI agent hỗ trợ dựng thực đơn cho khách và cho nội bộ.

Khác với cách làm hiện tại, cost được biết **trước** khi chốt thực đơn, và lựa chọn của người ăn là dữ liệu thật để cải tiến thực đơn.

### 1.2 Mục tiêu kinh doanh

Mức mục tiêu là [ĐỀ XUẤT], lấy từ mục 3 của BRD.

- **O1. Kiểm soát cost trước khi nấu**
  - **KR1.1**: 100% ngày phục vụ có cost dự toán ≤ 52% doanh thu suất ăn (BO-01)
  - **KR1.2**: Chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm theo ngày và cơ sở (BO-02)
- **O2. Thực đơn đúng chuẩn, không phụ thuộc một người**
  - **KR2.1**: 100% thực đơn công bố không vi phạm quy tắc cứng (BO-04)
  - **KR2.2**: Thời gian dinh dưỡng viên dựng một thực đơn tuần giảm ≥ 50% so với hiện tại (BO-03)
- **O3. Người ăn tự chọn món, order chạy trên hệ thống**
  - **KR3.1**: ≥ 70% suất có lựa chọn của người ăn trước hạn chốt, tính trên các công ty bật tính năng (BO-05)
  - **KR3.2**: ≥ 90% order ghi nhận qua cổng thay vì Zalo (BO-06)
  - **KR3.3**: Khách ký biên bản đối soát trong ≤ 5 ngày làm việc sau kỳ (BO-07)
- **O4. Website sinh khách hàng tiềm năng đo được**
  - **KR4.1**: 100% lead có nguồn ghi trong CRM (BO-08)
  - **KR4.2**: Số phiên truy cập tự nhiên sau 60 ngày chuyển đổi ≥ 90% mức trước đó (BO-09)
- **O5. Chịu tải giờ chốt**
  - **KR5.1**: 1000 người dùng đồng thời với p95 API ≤ 300 ms (đọc) và ≤ 800 ms (ghi), không tính AI (BO-10)

---

## 2. Đối tượng mục tiêu & Chân dung người dùng

Chi tiết ở mục 2 của URD. Cột "Hành vi công nghệ" chưa có dữ liệu vì chưa phỏng vấn người dùng.

| Persona ID | Tác nhân | Vai trò / Nhóm | Loại | Mục tiêu chính | Nỗi đau hiện tại | Hành vi công nghệ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `PER-01` | A-01 | Khách vãng lai | Chính | Biết giá, thực đơn, định lượng trước khi liên hệ | Website chỉ có giới thiệu chung | [CẦN PHỎNG VẤN] |
| `PER-02` | A-02, A-03 | Người đặt tổng (kiêm người nhận) | Chính | Chốt số suất và đối soát ít thao tác | Nhắn Zalo, số liệu cuối tháng dễ lệch | [CẦN PHỎNG VẤN] |
| `PER-03` | A-04 | Người ăn có tài khoản | Chính | Chọn món, biết mình ăn gì, được gợi ý | Không được chọn, không có thông tin món | [CẦN PHỎNG VẤN] |
| `PER-04` | A-05 | Người ăn qua QR | Chính | Chọn món trong tối đa 3 lần chạm | Như PER-03 | [CẦN PHỎNG VẤN] |
| `PER-05` | A-06 | Dinh dưỡng viên kiêm CSKH | Chính | Thực đơn đúng chuẩn, cost trong ngưỡng | Tự nhớ và tự kiểm mọi quy tắc; là điểm nghẽn đơn | [CẦN PHỎNG VẤN] |
| `PER-06` | A-07, A-08 | Quản lý cơ sở, bếp trưởng | Chính / Hỗ trợ | Biết số suất từng món ngay sau hạn chốt | Ghi giấy, số đến qua Zalo | [CẦN PHỎNG VẤN] |
| `PER-07` | A-09 | Kế toán | Chính | Nhập giá một lần, doanh thu tự sinh | Nhập lại số liệu, đối soát tay | [CẦN PHỎNG VẤN] |
| `PER-08` | A-10 | Giám đốc | Chính | Thấy cost %, doanh thu, công nợ theo ngày và khách | Số liệu rải rác | [CẦN PHỎNG VẤN] |
| `PER-09` | A-11 | Agent Dinh dưỡng viên | Hệ thống | Tạo thực đơn nháp cho khách | Không có | Không áp dụng |
| `PER-10` | A-12 | Agent Nội bộ | Hệ thống | Hỗ trợ dựng thực đơn, mua hàng, CRM, số liệu | Không có | Không áp dụng |

---

## 3. Phạm vi sản phẩm

### 3.1 Nằm trong phạm vi

Sản phẩm chia ba đợt phát hành. **Bản đầu (MVP) = đợt Now.**

| Đợt | Epic | Phân hệ | Kết quả khi xong |
| :--- | :--- | :--- | :--- |
| **Now** (MVP) | E1 → E5 | AUTH, SYS, MENU, COST, NUTR, AIO (phần thực đơn) | Dinh dưỡng viên dựng thực đơn tuần bằng Agent Nội bộ; hệ thống kiểm quy tắc và ngưỡng cost; có bảng dự toán và dinh dưỡng từng suất. Người dùng: nội bộ Gia Phát. |
| **Next** | E6 → E9 | ORD, CUS (người ăn), PLAN (kế hoạch), DLV, FIN, PUB, AIN | Người ăn chọn món, công ty chốt số, giao nhận và đối soát trên hệ thống; website mới thay WordPress; khách dùng Agent Dinh dưỡng viên. |
| **Later** | E10 → E13 | CUS, SALE, PUR, PLAN (phân ca, QC), FB, RPT, AIO (phần còn lại), EXP | CRM đầy đủ, mua hàng và sản xuất, phản hồi, báo cáo, lợi nhuận theo khách. |

Lý do MVP chỉ gồm nội bộ: mọi mặt tiền phía khách đều cần món, công thức, giá bán, cost và dinh dưỡng đã duyệt (BRD R-01).

### 3.2 Nằm ngoài phạm vi

- Căn tin bệnh viện Quảng Ninh.
- Thay thế MISA; hệ thống chỉ xuất file theo mẫu nhập của MISA.
- Người ăn tự thanh toán, ví điện tử, cổng thanh toán [D-21].
- Ứng dụng di động cài từ kho ứng dụng.
- Tư vấn y khoa, chẩn đoán, chế độ ăn điều trị.
- Đồng bộ tự động với Zalo cá nhân.
- Ghi lượng thức ăn bỏ thừa.
- Trường học, bệnh viện, tiệc cỗ: **chưa xác định** [O-05].

---

## 4. Bóc tách danh mục tính năng

Cột "Mã cũ" là mã dùng trong kế hoạch tổng thể và BRD. Mã `FR-[MODULE]-[FEATURE]-[SEQ]` được cấp ở SRS từng epic, với MODULE lấy từ cột "Phân hệ".

### 4.1 Đợt Now (MVP)

| Feature ID | Phân hệ | Mã cũ | Tên tính năng | Ưu tiên | Persona | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FEAT-001` | AUTH | AUTH-01 | Đăng nhập nội bộ và phân quyền | P0 | PER-05 → 08 | Phân quyền theo vai trò × cơ sở |
| `FEAT-002` | AUTH | AUTH-06 | Quản lý tài khoản | P0 | PER-05 → 08 | Nhật ký đăng nhập, khoá, đặt lại mật khẩu |
| `FEAT-003` | SYS | Không áp dụng | Nhật ký thay đổi | P0 | PER-08 | Ghi người, thời điểm, giá trị cũ → mới, lý do cho mọi thay đổi số liệu, giá, công thức |
| `FEAT-004` | SYS | Không áp dụng | Tham số hệ thống | P0 | PER-05, PER-08 | Ngưỡng cost, hạn chốt, ngưỡng điểm quy tắc là tham số, không viết cứng |
| `FEAT-005` | SYS | Không áp dụng | Trung tâm thông báo nội bộ | P0 | PER-05 → 08 | Cảnh báo có trạng thái mới / đã xem / đã xử lý |
| `FEAT-006` | MENU | MENU-01 | Danh mục nguyên liệu | P0 | PER-05, PER-07 | Đơn vị mua, đơn vị dùng (gram, bìa, quả), hệ số quy đổi, tỷ lệ hao hụt, mùa vụ |
| `FEAT-007` | MENU | MENU-02 | Danh mục món và thuộc tính | P0 | PER-05 | 12 thuộc tính phục vụ kiểm quy tắc (danh sách ở cuối bảng quy tắc) |
| `FEAT-008` | MENU | MENU-03 | Công thức có phiên bản | P0 | PER-05 | Định lượng sống min–max, nguyên liệu chính và phụ, người duyệt khác người tạo, ngày hiệu lực. Một hay nhiều cỡ định lượng: [O-02] |
| `FEAT-009` | MENU | MENU-04 | Loại suất | P0 | PER-05 | Dinh dưỡng viên tạo với 3 tham số: ngưỡng giá, số món chính, số món phụ [D-20] |
| `FEAT-010` | MENU | D-18 | Giá bán từng món | P0 | PER-05, PER-08 | Do nội bộ đặt, có ngày hiệu lực và người duyệt |
| `FEAT-011` | MENU | MENU-05 | Thực đơn kỳ (tuần) | P0 | PER-05 | Theo loại suất hoặc theo khách; mỗi ngày gồm các món chính để chọn, món phụ, rau, canh, và 1 món mặc định [D-14] |
| `FEAT-012` | MENU | MENU-06 | Bộ kiểm quy tắc thực đơn | P0 | PER-05 | Kiểm 43 quy tắc `BR-MENU`/`BR-COST`; quy tắc cứng chặn, quy tắc mềm trừ điểm |
| `FEAT-013` | MENU | MENU-07 | Duyệt và công bố thực đơn | P0 | PER-05, PER-08 | Nháp → kiểm quy tắc → kiểm cost → duyệt → công bố |
| `FEAT-014` | COST | COST-01 | Bảng giá nhập | P0 | PER-07 | Theo nguyên liệu × nhà cung cấp × ngày hiệu lực; nhập tay và nhập từ file |
| `FEAT-015` | COST | COST-02 | Cost món | P0 | PER-05, PER-07 | Σ định lượng sống × giá nhập hiệu lực, đã tính hao hụt |
| `FEAT-016` | COST | COST-03 | Cost suất và ngưỡng | P0 | PER-05, PER-08 | Tỷ lệ cost ÷ doanh thu; chặn công bố khi vượt. Cách tính mẫu số và thành phần cost: [O-01] |
| `FEAT-017` | COST | COST-04 | Bảng dự toán | P0 | PER-05, PER-07 | Tên nguyên liệu, giá nhập, định lượng/suất, số suất, tổng chi phí |
| `FEAT-018` | COST | COST-06 | Cảnh báo giá nhập biến động | P1 | PER-05, PER-08 | Báo khi thực đơn đã duyệt vượt ngưỡng do giá mới |
| `FEAT-019` | NUTR | NUTR-01 | Bảng thành phần dinh dưỡng | P0 | PER-05 | Theo nguyên liệu, nguồn Bảng thành phần thực phẩm Việt Nam [D-17] |
| `FEAT-020` | NUTR | NUTR-02 | Tính dinh dưỡng món và suất | P0 | PER-05 | 4 chỉ số: năng lượng, đạm, béo, bột đường; ghi nhãn "ước tính từ định lượng sống" |
| `FEAT-021` | AIO | AIO-01 | Agent Nội bộ dựng thực đơn | P0 | PER-05 | Đầu vào: loại suất, tuần, kiêng kỵ. Đầu ra: thực đơn nháp đạt FEAT-012 và FEAT-016, kèm bảng kiểm |
| `FEAT-022` | AIO | AIO-01 | Chỉnh thực đơn bằng lời | P0 | PER-05 | "Đổi cá thứ Tư" → agent đổi và kiểm lại |
| `FEAT-023` | AIO | Không áp dụng | Nhật ký lượt chạy agent | P0 | PER-08 | Ai hỏi, công cụ nào được gọi, kết quả, chi phí |

### 4.2 Đợt Next

| Feature ID | Phân hệ | Mã cũ | Tên tính năng | Ưu tiên | Persona | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FEAT-030` | AUTH | AUTH-02 | Tài khoản người đặt tổng | P0 | PER-02 | Gia Phát cấp theo hợp đồng |
| `FEAT-031` | AUTH | AUTH-03 | Đăng ký người ăn bằng QR công ty | P0 | PER-03 | Quét QR công ty để xác minh rồi tạo tài khoản [D-19] |
| `FEAT-032` | AUTH | AUTH-04 | Phiên chọn món qua QR | P0 | PER-04 | Không cần tài khoản; cách chống một người chọn nhiều lần chốt ở SRS |
| `FEAT-033` | AUTH | Không áp dụng | Quản lý QR và danh sách người ăn | P0 | PER-02 | Người đặt tổng gỡ tài khoản, đổi mã QR (BRD R-08) |
| `FEAT-034` | CUS | Không áp dụng | Công ty, điểm phục vụ, lịch phục vụ, người ăn | P0 | PER-05 | Dữ liệu tối thiểu để chạy order |
| `FEAT-035` | ORD | D-21 | Định mức suất của công ty | P0 | PER-02 | Một định mức chung: giá suất, số món chính, số món phụ |
| `FEAT-036` | ORD | ORD-01 | Người ăn chọn món | P0 | PER-03, PER-04 | Chọn 1 trong 3 món chính mỗi ngày; chặn tổ hợp vượt định mức (BR-COST-012) |
| `FEAT-037` | ORD | ORD-01 | Chọn trước cả tuần | P1 | PER-03 | Chỉ cho người có tài khoản |
| `FEAT-038` | ORD | ORD-02 | Tổng hợp và chốt số suất | P0 | PER-02 | Xem tổng theo món, số người chưa chọn; nhập tổng; chốt |
| `FEAT-039` | ORD | ORD-03 | Gán món mặc định | P0 | A-13 | Tại hạn chốt, phần chưa chọn nhận món mặc định [D-14] |
| `FEAT-040` | ORD | ORD-04 | Hạn chốt và khoá số | P0 | A-13 | Theo khách / điểm / ca; phát hành kế hoạch phiên bản 1 |
| `FEAT-041` | ORD | ORD-05 | Đổi sau chốt | P0 | PER-02, PER-05, PER-06, PER-08 | Tính chênh lệch, duyệt theo ngưỡng, tạo phiên bản mới |
| `FEAT-042` | ORD | ORD-06 | Nhập hộ order | P0 | PER-05 | Ghi nguồn và bằng chứng khi khách gửi qua Zalo |
| `FEAT-043` | ORD | ORD-07 | Nhắc người chưa chọn | P1 | A-13 | Kênh thông báo chốt ở SRS |
| `FEAT-044` | ORD | ORD-08 | Tắt chọn món theo khách | P1 | PER-02 | Quay về một người đặt cho cả công ty |
| `FEAT-045` | NUTR | NUTR-03 | Hiển thị định lượng, dinh dưỡng, dị ứng | P0 | PER-01 → 04 | Trên mọi mặt tiền phía khách |
| `FEAT-046` | NUTR | NUTR-04 | Hồ sơ dinh dưỡng cá nhân | P1 | PER-03 | Tự nguyện, có đồng ý, xoá được. Phạm vi bệnh lý: [O-03] |
| `FEAT-047` | NUTR | NUTR-05 | Gợi ý chọn món theo hồ sơ | P1 | PER-03 | Nên chọn món nào trong 3 món |
| `FEAT-048` | PLAN | Không áp dụng | Kế hoạch sản xuất theo món | P0 | PER-06 | Số chốt theo cơ sở × ca × món; phiếu sản xuất xem trên điện thoại |
| `FEAT-049` | DLV | M7 | Giao hàng và xác nhận nhận | P0 | PER-02, PER-06 | Theo suất; xác nhận bằng link |
| `FEAT-050` | DLV | M7 | Biên bản chênh lệch | P0 | PER-05 | Giao bù, giảm trừ theo thoả thuận |
| `FEAT-051` | FIN | M9 | Doanh thu ghi nhận | P0 | PER-07 | Số tính tiền × giá chụp tại thời điểm order |
| `FEAT-052` | FIN | M9 | Đối soát, thu tiền, khoá kỳ | P0 | PER-07, PER-02 | Mở lại kỳ cần Giám đốc duyệt |
| `FEAT-053` | FIN | M9 | Xuất file MISA | P0 | PER-07 | Theo mẫu nhập của MISA |
| `FEAT-054` | PUB | PUB-01 | Trang giới thiệu, dịch vụ, dự án, đối tác | P0 | PER-01 | Thay nội dung landing hiện tại |
| `FEAT-055` | PUB | PUB-02 | Tin tức / blog và chuyển bài cũ | P0 | PER-01 | Giữ URL hoặc 301 cho 100% bài |
| `FEAT-056` | PUB | PUB-03 | Thực đơn mẫu có giá | P0 | PER-01 | Giá suất, định lượng, dinh dưỡng, dị ứng [D-10] |
| `FEAT-057` | PUB | PUB-04 | Công cụ dựng thực đơn thử | P1 | PER-01 | Chọn loại suất, số suất, kiêng kỵ → thực đơn tuần mẫu |
| `FEAT-058` | PUB | PUB-06 | Form tư vấn → lead | P0 | PER-01 | Vào CRM kèm nguồn và thực đơn đã dựng |
| `FEAT-059` | PUB | PUB-07 | Quản trị nội dung | P0 | PER-05 | Bài viết, ảnh, banner |
| `FEAT-060` | AIN | AIN-01 | Agent tạo thực đơn tập thể | P0 | PER-01, PER-02 | Theo loại suất, số suất, khẩu vị, kiêng kỵ |
| `FEAT-061` | AIN | AIN-02, 03 | Giải thích và chỉnh thực đơn | P0 | PER-01, PER-02 | Kiểm lại quy tắc sau mỗi lần chỉnh |
| `FEAT-062` | AIN | AIN-04 | Gửi nháp về Gia Phát / tạo lead | P0 | PER-01, PER-02 | Người thật duyệt trước khi áp dụng |
| `FEAT-063` | AIN | AIN-05 | Gợi ý cá nhân qua agent | P1 | PER-03, PER-04 | Dùng FEAT-047 |
| `FEAT-064` | AIN | Không áp dụng | Giới hạn lượt và ngân sách | P0 | PER-08 | Theo nhóm người dùng; trần chi phí theo ngày |
| `FEAT-065` | AIN | Không áp dụng | Chặn truy cập cost | P0 | Không áp dụng | Agent phía khách không có công cụ và quyền đọc giá nhập, cost (BN-16) |

### 4.3 Đợt Later

| Feature ID | Phân hệ | Mã cũ | Tên tính năng | Ưu tiên | Persona | Mô tả vắn tắt |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `FEAT-070` | CUS | M1 | Hồ sơ khách hàng 360° | P1 | PER-05, PER-08 | Liên hệ, điểm, hợp đồng, order, doanh thu, phản hồi; phát hiện và gộp trùng |
| `FEAT-071` | CUS | M1 | Vòng đời khách và tín hiệu nguy cơ rời | P1 | PER-05, PER-08 | Theo lịch phục vụ của điểm |
| `FEAT-072` | SALE | M2 | Phễu cơ hội, báo giá có phiên bản | P1 | PER-05 | Báo giá kèm thực đơn; cost chỉ nội bộ thấy |
| `FEAT-073` | SALE | M2 | Hợp đồng và phụ lục giá hiệu lực | P1 | PER-05, PER-08 | Giá theo loại suất |
| `FEAT-074` | PUR | M5 | Nhu cầu nguyên liệu và đơn mua | P1 | PER-07 | Lô chỉ quản lý cho hàng đông lạnh và khô |
| `FEAT-075` | PUR | M5 | Nhận hàng, công nợ nhà cung cấp | P1 | PER-06, PER-07 | Ảnh chứng từ |
| `FEAT-076` | COST | COST-07 | Đối chiếu dự toán với thực mua | P1 | PER-07, PER-08 | Theo ngày và cơ sở |
| `FEAT-077` | PLAN | M6 | Phân ca, kiểm tra trước giao, sổ mẫu lưu | P1 | PER-06 | Chưa có |
| `FEAT-078` | MENU | MENU-08 | Món thay thế khi thiếu hàng | P1 | PER-05 | Cùng vai trò, kiểm lại dị ứng, quy tắc, cost |
| `FEAT-079` | FB | M8 | Đánh giá bữa ăn, khiếu nại | P1 | PER-02 → 05 | Chưa có |
| `FEAT-080` | FB | M8 | Phân tích món và đề xuất thực đơn | P1 | PER-05 | Tỷ lệ được chọn tính từ lựa chọn thật của người ăn |
| `FEAT-081` | RPT | Không áp dụng | Dashboard theo vai trò | P1 | PER-05 → 08 | Thêm cost % theo ngày và theo khách |
| `FEAT-082` | AIO | AIO-02 | Rà soát thực đơn khi giá đổi | P1 | PER-05, PER-08 | Đề xuất đổi món hoặc định lượng |
| `FEAT-083` | AIO | AIO-03, 04 | Dự toán, nhu cầu nguyên liệu, cảnh báo giá lệch | P1 | PER-07 | Chưa có |
| `FEAT-084` | AIO | AIO-05 | Hỗ trợ CRM | P1 | PER-05, PER-08 | Tóm tắt khách, nhắc việc, nháp báo giá |
| `FEAT-085` | AIO | AIO-06 | Hỏi đáp số liệu | P2 | PER-07, PER-08 | Chỉ đọc, theo quyền người hỏi |
| `FEAT-086` | NUTR | NUTR-06 | Mục tiêu dinh dưỡng theo nhóm người ăn | P1 | PER-05 | Kiểm thực đơn theo mục tiêu |
| `FEAT-087` | NUTR | NUTR-07 | Nhật ký dinh dưỡng cá nhân | P2 | PER-03 | Theo các bữa đã ăn |
| `FEAT-088` | EXP | M10 | Chi phí cơ sở, chấm công, lợi nhuận theo khách | P2 | PER-07, PER-08 | Cần nguyên tắc phân bổ chi phí |

Tổng: 23 tính năng đợt Now · 36 đợt Next · 19 đợt Later.

### 4.4 Nguyên tắc sản phẩm cho hai AI agent

Áp dụng cho FEAT-021 → 023, 060 → 065, 082 → 085.

1. Agent không tự tính cost, định lượng, dinh dưỡng; nó gọi hàm tính của hệ thống và diễn giải kết quả.
2. Agent chỉ dùng món và công thức ở trạng thái đã duyệt.
3. Đầu ra của agent là bản nháp; công bố phải qua FEAT-013.
4. Mỗi thực đơn agent trả về kèm bảng kiểm quy tắc đạt / vi phạm.
5. Hai agent tách lời nhắc hệ thống, bộ công cụ, tài khoản dịch vụ, hàng đợi, hạn mức chi phí.
6. Agent phía khách không chẩn đoán, không tư vấn điều trị, không cam kết giá hay hợp đồng.

---

## 5. Giả định & Ràng buộc

**Ràng buộc**

- Công nghệ: ReactJS (Next.js cho website công khai [ĐỀ XUẤT]), Rust/Axum, MySQL [D-22, thay NodeJS/NestJS theo [CR-CORE-2026-001](../nen-tang/cr/CR-CORE-2026-001.md)].
- Tải: 1000 người dùng đồng thời.
- MISA vẫn là sổ kế toán chính thức.
- Không tuyển thêm nhân sự vận hành.
- Thời hạn phát hành: **chưa có** [O-04].

**Giả định** (lấy từ BRD mục 10)

- Người ăn có điện thoại vào được web để chọn món.
- Các công ty khách chấp nhận cho nhân viên quét QR và tự chọn món.
- Dinh dưỡng viên có thời gian nhập dữ liệu gốc trước khi mở cổng.
- Mỗi công ty khách có một người đặt tổng chốt tổng số suất.

**Phụ thuộc chặn đợt Now**

| Phụ thuộc | Chặn tính năng |
| :--- | :--- |
| Người soạn docx duyệt 43 quy tắc | FEAT-012, FEAT-021 |
| Kế toán trả lời [O-01] | FEAT-016, FEAT-017 |
| Dinh dưỡng viên trả lời [O-02] | FEAT-008, FEAT-010 |
| Chọn nhà cung cấp mô hình AI và hạ tầng [O-04] | FEAT-021 → 023 |
| Có người duyệt thứ hai [O-06] | FEAT-008, FEAT-013 |

---

## 6. Điểm mở

Giữ nguyên trạng thái mở.

| Mã | Điểm mở | Ai trả lời | Tính năng bị ảnh hưởng |
| :--- | :--- | :--- | :--- |
| O-01 | Cost gồm những khoản nào; thuế suất VAT | Kế toán | FEAT-015 → 017 |
| O-02 | Một món một định lượng hay nhiều cỡ định lượng | Dinh dưỡng viên | FEAT-008, 010, 036 |
| O-03 | Gợi ý cá nhân có xét bệnh lý không | Giám đốc | FEAT-046, 047, 063 |
| O-04 | Đội phát triển, hạ tầng, nhà cung cấp AI, ngân sách | Giám đốc | Lộ trình; FEAT-021, 060, 064 |
| O-05 | Trường học, bệnh viện, tiệc cỗ có trong bản đầu không | Giám đốc | Mục 3 |
| O-06 | Ai duyệt ngoại lệ và ai thay khi vắng | Giám đốc | FEAT-001, 008, 013, 041, 052 |

Điểm phát sinh từ URD, chốt ở SRS epic `chon-mon-order`: xử lý thế nào khi người đặt tổng chốt tổng số suất nhỏ hơn số người đã tự chọn (FEAT-038).

## Liên kết đặc tả MVP hiện hành (E4/E5)

- E4/R4: [SRS Dinh dưỡng](../dinh-duong/srs/spec.md), [câu hỏi nguồn/dung sai/dữ liệu](../dinh-duong/review/questions.md).
- E5/R5: [SRS Agent Nội bộ](../agent-noi-bo/srs/spec.md), [câu hỏi vận hành và nghiệm thu](../agent-noi-bo/review/questions.md).
- [Gói review và kiểm truy vết](review/mvp-e4-e5-handoff.md). Đây là tài liệu nháp, chưa chứng minh release đã triển khai hoặc qua cổng G-Now.

NUTR-Q04 cần chốt ý nghĩa “khớp” của 5 suất R4; không mượn dung sai Cost. AIO-Q02 cần xác nhận hành vi agent khi Cost ở CANH_BAO; tiêu chí R5 không vượt ngưỡng vẫn giữ, không đổi cổng gửi duyệt MENU. R5 vẫn phụ thuộc R2/R3 theo roadmap; R4 thuộc cổng G-Now, không tự thêm phụ thuộc cứng vào generation. O-04 và các điểm mở khác không tự đóng.

## Tiến độ hồ sơ BA sau bổ sung ngày 11/11/2026

[Dashboard](../project-dashboard.md) và [bàn giao](review/ba-completion-handoff.md) ghi chi tiết E1–E5; [E6 gói review v0.2](../chon-mon-order/preview.html) đã bổ sung UC/API/UI/AC/RTM; còn gate nghiệp vụ và chưa triển khai release. Phạm vi/ưu tiên, G-Now và tiêu chí nghiệm thu roadmap giữ nguyên. O-03 vẫn gated FEAT-046/047, không tự mở thu thập sức khỏe.

## Cập nhật hồ sơ E6 ngày 11/11/2026

[Bàn giao E6](../chon-mon-order/review/handoff.md): giữ14P0/5P1 và G-Now/R6; 17capability có thiết kế có điều kiện, FEAT-046/047 chỉ gate O-03. Không đổi ưu tiên/ngày release; ORD-Q01–15 chờ xác nhận. Độ phủ liên kết tài liệu không phải phần mềm hoặc UAT.
