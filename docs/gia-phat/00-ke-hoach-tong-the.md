# Kế hoạch tổng thể: tính năng & thứ tự viết tài liệu (khung ba-kit) Gia Phát

## Metadata

| Trường | Giá trị |
|---|---|
| Sản phẩm | Nền tảng Gia Phát: website công khai + cổng khách hàng/người ăn + quản trị nội bộ + 2 AI agent |
| `{product_name}` dùng cho ba-kit | `gia-phat` |
| Phiên bản | v0.3.0 (đổi backend sang Rust/Axum theo CR-CORE-2026-001; còn điểm mở, chưa ký baseline) |
| Ngày | 14/11/2026 |
| Tài liệu nguồn | `GiaPhat_CMAP_CRM.html` (bản 1.0, 04/11/2026) · `Yêu cầu về thực đơn và cost tp.docx` · comgiaphat.com · [Bản phân tích điểm bất hợp lý](../../GiaPhat_PhanTich_ThietKe.md) |
| Công nghệ đã chốt | ReactJS · Rust/Axum · MySQL · mục tiêu 1000 người dùng đồng thời (D-22 thay NodeJS/NestJS) |

## Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung |
|---|---|---|
| v0.3.0 | 14/11/2026 | Đổi backend sang Rust/Axum (D-22), sửa mục 2.1, 3.1, 5.1, thêm R-08; liên kết kiến trúc hệ thống và kiến trúc AI agent. Xem [CR-CORE-2026-001](../nen-tang/cr/CR-CORE-2026-001.md) |
| v0.2.0 | 11/11/2026 | Đồng bộ E1–E5, thêm sổ phạm vi/dashboard/preview và E6 khởi đầu; giữ lịch sử quyết định và điểm mở |
| v0.1.0 | 10/11/2026 | Bản khung đầu tiên sau 2 vòng hỏi đáp |

## Cách đọc

- **[ĐÃ CHỐT]** = anh đã trả lời trực tiếp. **[ĐỀ XUẤT]** = phương án kỹ thuật tôi đề nghị, anh có thể đổi. **[CHỜ Q-xx]** = chưa quyết, không tự suy đoán, câu hỏi nằm ở mục 9.
- Mã phân hệ (AUTH, MENU, COST…) dùng luôn cho mã yêu cầu `FR-[MODULE]-[FEATURE]-[SEQ]` theo `rules/01-fr-naming-convention.md`.
- Ưu tiên: **P0** bắt buộc cho bản đầu · **P1** nên có · **P2** để sau.

---

## Trạng thái hiện hành ngày 11/11/2026

- E1–E5 đã có các loại hồ sơ BA theo chuỗi mục6.2, gồm preview HTML và sơ đồ; mức chi tiết/gate khác nhau, không coi là baseline đã duyệt. Các khoảng trống nghiệp vụ còn lại ghi ở gap-analysis từng epic.
- Bước1 có [sổ phạm vi](brainstorms/pham-vi-san-pham.md), nhưng điều kiện “không còn câu hỏi chặn” chưa đạt. Bước2 vẫn chờ DL-01; các bước3–8 là bản nháp đã có, không phải đã nghiệm thu.
- E6 mới có [gói khởi đầu](../chon-mon-order/epic-spec.md); E7–E13 chưa có SRS riêng. Hồ sơ sức khỏe/gợi ý cá nhân vẫn gated O-03.
- [Dashboard hiện hành](../project-dashboard.md) và [bàn giao bổ sung](review/ba-completion-handoff.md) thay việc suy tiến độ từ dấu đánh dấu lịch sử.

Mục1–5 và9 bên dưới giữ bối cảnh các vòng trao đổi trước. Các nhãn CHỜ đã được quyết định D giải quyết không tự trở thành câu hỏi mở lại. Khi câu khung cũ khác SRS cập nhật, dùng xác nhận người dùng và tài liệu chuyên biệt hiện hành: Cost gồmVAT phải trả; hóa đơn riêng; chiết khấu khoản riêng; CHAN/CANH_BAO theo SRS; đối soát NFR-COST-002. Không dùng câu khung cũ “chặn tuyệt đối” để thay cổng MENU.

## 1. Quyết định đã chốt

| # | Quyết định | Nguồn |
|---|---|---|
| D-01 | Viết lại toàn bộ comgiaphat.com bằng React, bỏ WordPress + Elementor. | Trả lời vòng 1 |
| D-02 | Một subdomain quản trị nội bộ, phủ các chức năng trong bản HTML C-MAP/CRM. | Yêu cầu gốc |
| D-03 | Bốn nhóm dùng tính năng chọn menu/dinh dưỡng: **khách vãng lai**, **người đặt tổng**, **người ăn có tài khoản**, **người ăn qua QR** (không tài khoản). | Vòng 2 |
| D-04 | Mỗi ngày 3 món chính; **mỗi người ăn chọn 1 trong 3**. Bếp nấu theo số lượng từng món đã chọn. | Vòng 2 |
| D-05 | **Hai AI agent tách biệt**: Agent Dinh dưỡng viên (phía khách) và Agent Nội bộ. | Vòng 1 |
| D-06 | Agent Dinh dưỡng viên tư vấn **cả hai mức**: thực đơn cho tập thể và gợi ý cá nhân cho người ăn tự khai thông tin. | Vòng 2 |
| D-07 | Agent Nội bộ làm 4 việc: dựng thực đơn + kiểm cost · mua hàng & nguyên liệu · hỗ trợ CRM/CSKH · hỏi đáp số liệu. | Vòng 2 |
| D-08 | Quy chuẩn thực đơn, bảng định lượng (mức 40k/suất) và ngưỡng cost 52% theo file docx là nguồn quy tắc nghiệp vụ. | Yêu cầu gốc |
| D-09 | Các quyết định ngày 04/11/2026 trong bản HTML (2 cơ sở, HĐ nguyên tắc năm, ghi nhận doanh thu khi khách xác nhận, MISA dùng riêng…) giữ nguyên, **trừ** điểm "mỗi công ty một người đặt tổng nhập số": bị D-03/D-04 thay đổi. | Bản HTML + vòng 2 |

| D-10 | Khách vãng lai **được thấy giá suất** trên website công khai. (Q-01) | Vòng 3 |
| D-11 | Người ăn có form **đăng ký / đăng nhập và phải xác minh** trước khi dùng. Cách xác minh cụ thể còn mở (Q-02b). | Vòng 3 |
| D-12 | **Suất tuỳ biến**: mức giá suất, số món chính, số món phụ cấu hình được. Khi khách chọn món theo ý thích, hệ thống **tự tính giá suất** hoặc **chặn khi vượt định mức**. (Q-05) → thêm tính năng MENU-10. | Vòng 3 |
| D-13 | Giá nhập nguyên liệu và cost do **nội bộ nhập**; không lấy từ nguồn ngoài. | Vòng 3 |

| D-14 | Người không chọn trước hạn chốt nhận **món mặc định** của ngày; người đặt tổng được sửa trước hạn. Tổng số suất do người đặt tổng chốt. (Q-03) | Vòng 4 |
| D-15 | Giá 40.000đ/suất là giá **đã gồm VAT**. (Q-04, phần VAT) | Vòng 4 |
| D-16 | Quy tắc định tính trong docx được chuyển thành con số theo bản đề xuất [quy-tac-thuc-don.md](brainstorms/quy-tac-thuc-don.md); người soạn docx duyệt. (Q-06) | Vòng 4 |
| D-17 | Dữ liệu dinh dưỡng theo "Bảng thành phần thực phẩm Việt Nam" (Viện Dinh dưỡng); bản đầu hiện 4 chỉ số: năng lượng, đạm, béo, bột đường; ghi rõ là ước tính từ định lượng sống. (Q-08) | Vòng 4 |
| D-18 | Mỗi món có **giá bán riêng** do nội bộ đặt; giá suất tuỳ biến = tổng giá bán các món đã chọn. (Q-20) | Vòng 4 |
| D-19 | Người ăn xác minh bằng **mã QR của công ty**. (Q-02b) | Vòng 4 |
| D-20 | Không có danh sách mức giá cố định: **dinh dưỡng viên tự tạo loại suất** (ngưỡng giá, số món chính, số món phụ). (Q-07) | Vòng 4 |

| D-21 | **Công ty đặt định mức chung** (giá suất, số món chính, số món phụ); người ăn chọn trong định mức, hệ thống chặn lựa chọn vượt định mức. Người ăn không tự dựng suất giá riêng, không phát sinh phần chênh phải tự trả. (Q-21) | Vòng 5 |

| D-22 | Backend viết bằng **Rust với Axum**, thay NodeJS/NestJS; không lai ngôn ngữ. Frontend giữ ReactJS, cơ sở dữ liệu giữ MySQL 8. Tên thư viện cụ thể là [ĐỀ XUẤT]. Xem [CR-CORE-2026-001](../nen-tang/cr/CR-CORE-2026-001.md). | Phiên 14/11/2026 |

### Hệ quả trực tiếp của D-03 và D-04 lên bản thiết kế cũ

1. **Số ĐẶT không còn do một người nhập.** Nó là tổng lựa chọn cá nhân theo từng món chính, cộng phần người đặt tổng nhập cho những người không tự chọn. Cần quy tắc cho người không chọn trước hạn [CHỜ Q-03].
2. **Người ăn không còn ẩn danh.** Bản cũ chỉ có "nhóm người ăn"; nay cần thực thể Người ăn (có tài khoản) và Phiên QR (không tài khoản) → phát sinh nghĩa vụ bảo vệ dữ liệu cá nhân, nhất là dữ liệu sức khoẻ ở D-06.
3. **Kế hoạch sản xuất theo món**, còn giao/nhận/tính tiền theo suất. Bảy loại số lượng phải ghi rõ cấp nào theo món, cấp nào theo suất.
4. **Điểm tải cao nhất** là lúc người ăn dồn vào chọn món sát hạn chốt: đây mới là chỗ mục tiêu 1000 CCU có ý nghĩa.

---

## 2. Bức tranh hệ thống

### 2.1 Bốn mặt tiền, một lõi

| Mặt tiền | Địa chỉ [ĐỀ XUẤT] | Người dùng | Nội dung |
|---|---|---|---|
| Website công khai | `comgiaphat.com` | Khách vãng lai | Giới thiệu, dịch vụ, tin tức/blog, thực đơn mẫu, công cụ dinh dưỡng, chat với Agent Dinh dưỡng viên, form tư vấn → lead |
| Cổng khách hàng | `app.comgiaphat.com` | Người đặt tổng, người nhận | Thực đơn kỳ, tổng hợp lựa chọn, chốt số, xác nhận nhận hàng, đối soát |
| Cổng người ăn | Cùng app với cổng khách hàng; QR mở thẳng trang chọn món | Người ăn có tài khoản / qua QR | Chọn 1 trong 3 món chính, xem định lượng – dinh dưỡng – dị ứng, hồ sơ cá nhân, đánh giá bữa ăn |
| Quản trị nội bộ | `admin.comgiaphat.com` | Giám đốc, dinh dưỡng viên/CSKH, quản lý cơ sở, bếp trưởng, kế toán | Toàn bộ phân hệ M1–M10 của bản HTML + thực đơn/cost + Agent Nội bộ |
| **Lõi** | `api.comgiaphat.com` | Không áp dụng | Một API Rust (Axum), một MySQL, dùng chung cho cả bốn mặt tiền |

### 2.2 Tác nhân (actor): đầu vào cho `rules/17-actor-role-definition.md`

| Mã | Tác nhân | Đăng nhập | Ghi chú |
|---|---|---|---|
| A-01 | Khách vãng lai | Không | Giới hạn lượt dùng AI |
| A-02 | Người đặt tổng | Có | Thuộc một công ty khách; có thể kiêm người nhận |
| A-03 | Người nhận | Link hoặc tài khoản | Xác nhận số nhận & chất lượng |
| A-04 | Người ăn có tài khoản | Có | Hồ sơ dinh dưỡng cá nhân (tự nguyện) |
| A-05 | Người ăn qua QR | Không | Cách định danh để chống chọn trùng [CHỜ Q-02] |
| A-06 | Dinh dưỡng viên kiêm CSKH | Có | Duyệt mọi đầu ra của AI trước khi công bố |
| A-07 | Quản lý cơ sở | Có | Phạm vi dữ liệu theo cơ sở |
| A-08 | Bếp trưởng | Có | Phiếu sản xuất, số sản xuất |
| A-09 | Kế toán (mua hàng / doanh thu) | Có | |
| A-10 | Giám đốc | Có | Duyệt ngoại lệ, giá, cost |
| A-11 | Agent Dinh dưỡng viên | Tài khoản dịch vụ | Chỉ đọc dữ liệu đã duyệt, **không thấy cost** |
| A-12 | Agent Nội bộ | Tài khoản dịch vụ | Quyền theo người đang dùng nó |

---

## 3. Kiến trúc kỹ thuật cho 1000 người dùng đồng thời [ĐỀ XUẤT]

Bản chi tiết có sơ đồ và cấu trúc mã nguồn: [Kiến trúc hệ thống](../nen-tang/srs/architecture.md). Ngôn ngữ backend là [ĐÃ CHỐT D-22]; tên thư viện là [ĐỀ XUẤT].

### 3.1 Thành phần

| Lớp | Lựa chọn | Lý do |
|---|---|---|
| Website công khai | **Next.js (React)** có SSR/ISR | Site công khai và blog cần SEO; React thuần render phía trình duyệt sẽ mất thứ hạng tìm kiếm hiện có. Giữ nguyên URL bài viết cũ hoặc chuyển hướng 301. |
| Cổng khách/người ăn + quản trị | **React SPA** (Vite), 2 bản build riêng | Không cần SEO; tách bản quản trị để không lộ mã nội bộ ra ngoài. |
| API | **Rust (Axum + Tokio), modular monolith**: mỗi phân hệ một crate trong cùng Cargo workspace, chạy ≥ 2 bản sau bộ cân bằng tải | Đội nhỏ, một cơ sở mã; không tách microservice. API không giữ trạng thái nên nhân bản được. |
| Worker | Rust + **apalis** trên Redis (tiến trình riêng, dùng chung crate nghiệp vụ với API) | Chạy AI agent, gửi thông báo, chốt số tại hạn chốt, tính nhu cầu nguyên liệu, xuất file: không chạy trong luồng xử lý yêu cầu web. |
| Cơ sở dữ liệu | **MySQL 8**: 1 primary + 1 read replica | Ghi vào primary; trang thực đơn, báo cáo, hỏi đáp số liệu đọc từ replica. |
| Bộ nhớ đệm / hàng đợi | **Redis** | Cache thực đơn đã công bố, phiên đăng nhập, giới hạn tần suất, hàng đợi của worker. |
| Tệp | Lưu trữ đối tượng tương thích S3 + CDN | Ảnh món, ảnh chứng từ, mẫu lưu, tệp hợp đồng. |
| Mô hình ngôn ngữ | Gọi qua API nhà cung cấp, từ worker [CHỜ Q-09] | Xem mục 5. |

### 3.2 Hai điểm nghẽn thật và cách xử lý

| Điểm nghẽn | Xử lý |
|---|---|
| **Dồn chọn món sát hạn chốt** (hàng trăm người ghi cùng lúc) | Thực đơn ngày đọc từ Redis; mỗi lựa chọn là một lệnh ghi nhỏ có khoá duy nhất `(người ăn, ngày, ca)` và khoá chống gửi lặp; tổng theo món cập nhật bằng bộ đếm, không `COUNT` lại mỗi lần; hạn chốt do một job duy nhất khoá và chụp số. |
| **Lời gọi AI** (chậm vài giây đến vài chục giây, tốn tiền theo lượt) | Luôn qua hàng đợi, trả kết quả dạng luồng (streaming); giới hạn số lượt chạy song song và ngân sách theo ngày cho từng nhóm người dùng; khách vãng lai giới hạn theo IP/phiên; khi quá tải thì xếp hàng chứ không làm chậm việc chọn món. |

### 3.3 Chỉ tiêu phi chức năng: đầu vào cho `rules/04-nfr-standards.md` (con số [ĐỀ XUẤT], chốt ở SRS)

| Mã | Chỉ tiêu | Mục tiêu |
|---|---|---|
| NFR-PERF-001 | Đồng thời | 1000 người dùng hoạt động, trong đó ≥ 300 thao tác ghi/phút vào giờ chốt |
| NFR-PERF-002 | Thời gian phản hồi API | p95 ≤ 300 ms (đọc), ≤ 800 ms (ghi), không tính AI |
| NFR-PERF-003 | AI | Ký tự đầu tiên ≤ 5 s; thực đơn tuần hoàn chỉnh ≤ 60 s |
| NFR-AVAIL-001 | Sẵn sàng | ≥ 99,5% trong khung 05:00–18:00 các ngày phục vụ |
| NFR-SEC-001 | Phân quyền | Vai trò × cơ sở × công ty khách; người ăn chỉ thấy dữ liệu của mình |
| NFR-SEC-002 | Dữ liệu sức khoẻ | Mã hoá khi lưu, có đồng ý rõ ràng, xoá được theo yêu cầu |
| NFR-DATA-001 | Sao lưu | Hằng ngày, giữ 30 ngày, có diễn tập khôi phục |
| NFR-AUD-001 | Nhật ký | Mọi thay đổi số liệu, giá, công thức, quyết định duyệt và mọi lượt chạy AI đều truy vết được |

---

## 4. Danh mục tính năng

### 4.1 PUB: Website công khai (thay WordPress)

| Mã | Tính năng | Tác nhân | Ưu tiên |
|---|---|---|---|
| PUB-01 | Trang chủ, dịch vụ (cơm văn phòng, suất ăn công nghiệp, sự kiện), dự án, đối tác, nhận xét khách | A-01 | P0 |
| PUB-02 | Tin tức/blog + chuyển toàn bộ bài viết cũ, giữ URL hoặc 301 | A-01 | P0 |
| PUB-03 | Trang thực đơn mẫu theo mức giá suất: món, định lượng, dinh dưỡng, dị ứng | A-01 | P0 |
| PUB-04 | Công cụ dựng thực đơn thử: chọn mức giá, số suất, kiêng kỵ → xem thực đơn tuần mẫu | A-01 | P1 |
| PUB-05 | Chat với Agent Dinh dưỡng viên (giới hạn lượt) | A-01 | P1 |
| PUB-06 | Form yêu cầu tư vấn → tạo lead thẳng vào CRM, kèm thực đơn khách vừa dựng | A-01 | P0 |
| PUB-07 | Quản trị nội dung (bài viết, ảnh, banner) trong trang quản trị | A-06 | P0 |

Có hiện giá/báo giá sơ bộ cho khách vãng lai hay không: [CHỜ Q-01].

### 4.2 AUTH: Tài khoản & phân quyền

| Mã | Tính năng | Ưu tiên |
|---|---|---|
| AUTH-01 | Đăng nhập nội bộ; phân quyền vai trò × cơ sở | P0 |
| AUTH-02 | Tài khoản người đặt tổng do Gia Phát cấp theo hợp đồng | P0 |
| AUTH-03 | Tài khoản người ăn: cách tạo (tự đăng ký bằng mã công ty / công ty nhập danh sách / đăng nhập bằng số điện thoại) [CHỜ Q-02] | P0 |
| AUTH-04 | Phiên QR không tài khoản: QR theo điểm phục vụ, cách định danh chống chọn trùng [CHỜ Q-02] | P0 |
| AUTH-05 | Đồng ý xử lý dữ liệu cá nhân/sức khoẻ; rút đồng ý; xoá dữ liệu | P0 (nếu làm D-06 mức cá nhân) |
| AUTH-06 | Nhật ký đăng nhập, khoá tài khoản, đặt lại mật khẩu | P0 |

### 4.3 MENU: Món, công thức, định lượng, thực đơn

Đây là phân hệ lõi mới. Bản HTML đặt nó ở "M3 cơ bản"; nay phải làm đầy đủ ngay từ đầu vì cả hai agent và việc chọn món đều đứng trên nó.

| Mã | Tính năng | Ưu tiên |
|---|---|---|
| MENU-01 | Danh mục nguyên liệu: đơn vị mua, đơn vị dùng (gram, bìa, quả), hệ số quy đổi, tỷ lệ hao hụt (xương, vỏ), mùa vụ, độ ổn định nguồn cung | P0 |
| MENU-02 | Danh mục món với đủ thuộc tính để áp quy tắc: vai trò (chính / phụ / rau / canh), nguyên liệu chính, phương pháp chế biến, vị, khô/sốt, cờ Healthy, độ cầu kỳ sơ chế, mức chịu vận chuyển, nhóm cost (thấp/cao), dị ứng | P0 |
| MENU-03 | Công thức có phiên bản: nguyên liệu chính, nguyên liệu phụ/chất độn, **định lượng sống theo từng mức giá suất** (khoảng min–max), người duyệt, ngày hiệu lực | P0 |
| MENU-04 | Loại suất (combo): mức giá, cơ cấu (cơm + 1 món chính trong 3 + số món phụ + rau + canh) [CHỜ Q-05] | P0 |
| MENU-05 | Thực đơn kỳ (tuần) theo loại suất / theo khách: mỗi ngày 3 món chính (1 Healthy), món phụ, rau, canh | P0 |
| MENU-06 | **Bộ kiểm quy tắc thực đơn** (code xác định, không phải AI): quy tắc cứng → chặn; quy tắc mềm → điểm & cảnh báo. Mỗi quy tắc có mã `BR-MENU-xxx` truy về câu trong docx | P0 |
| MENU-07 | Quy trình duyệt & công bố thực đơn: nháp → kiểm quy tắc → kiểm cost → duyệt → công bố lên cổng | P0 |
| MENU-08 | Món thay thế khi thiếu hàng: cùng vai trò, không vi phạm dị ứng, kiểm lại quy tắc & cost | P1 |
| MENU-09 | Rau theo mùa: lịch mùa vụ và ưu tiên khi dựng thực đơn | P1 |
| MENU-10 | **Bộ tính giá suất tuỳ biến** [ĐÃ CHỐT D-12]: cấu hình định mức (giá suất, số món chính, số món phụ) theo khách; khi chọn món tự do thì tính giá suất theo món đã chọn, hoặc chặn lựa chọn làm vượt định mức. Cách tính giá từng món và ai được tuỳ biến: [CHỜ Q-20, Q-21] | P0 |

Quy tắc trong docx cần chuyển thành `BR-MENU-xxx` (số lượng sơ bộ: ~30 quy tắc). Phần lớn đang ở dạng định tính ("hạn chế tối đa", "không nên", "hài hoà"): phải phân loại cứng/mềm và gắn con số trước khi viết SRS [CHỜ Q-06].

### 4.4 COST: Giá nguyên liệu, dự toán, ngưỡng 52%

| Mã | Tính năng | Ưu tiên |
|---|---|---|
| COST-01 | Bảng giá nhập theo nguyên liệu × nhà cung cấp × ngày hiệu lực; nhập tay và nhập từ file | P0 |
| COST-02 | Cost một món = Σ định lượng sống × giá nhập hiệu lực (đã tính hao hụt) | P0 |
| COST-03 | Cost một suất/ngày và tỷ lệ trên giá suất; **chặn công bố khi vượt ngưỡng** (ngưỡng là tham số, mặc định 52%) | P0 |
| COST-04 | Bảng dự toán theo docx mục IV: tên nguyên liệu, giá nhập, định lượng/suất, số suất, tổng chi phí | P0 |
| COST-05 | Tính lại định lượng khi đổi mức giá suất (từ bảng chuẩn 40k) [CHỜ Q-07] | P0 |
| COST-06 | Cảnh báo khi giá nhập biến động làm thực đơn đã duyệt vượt ngưỡng | P1 |
| COST-07 | Đối chiếu cost dự toán với chi phí thực mua theo ngày/cơ sở | P1 |
| COST-08 | Cân đối món phụ theo cost món chính (món chính cao → món phụ thấp): thành quy tắc mềm trong MENU-06 | P1 |

Công thức 52% tính trên doanh thu trước hay sau VAT, gồm những khoản nào (gạo, gia vị, dầu, gas, hộp/khay): [CHỜ Q-04]. Cost và giá nhập **không bao giờ** hiển thị ở cổng khách.

### 4.5 NUTR: Dinh dưỡng

| Mã | Tính năng | Ưu tiên |
|---|---|---|
| NUTR-01 | Bảng thành phần dinh dưỡng theo nguyên liệu (năng lượng, đạm, béo, bột đường, xơ, muối…): nguồn dữ liệu [CHỜ Q-08] | P0 |
| NUTR-02 | Tính dinh dưỡng món và suất từ định lượng sống (có hệ số phần ăn được) | P0 |
| NUTR-03 | Hiển thị cho khách: định lượng, thành phần, dinh dưỡng, dị ứng của từng món/suất | P0 |
| NUTR-04 | Hồ sơ dinh dưỡng cá nhân (tự nguyện): chiều cao, cân nặng, mục tiêu, dị ứng, kiêng kỵ; phạm vi bệnh lý [CHỜ Q-10] | P1 |
| NUTR-05 | Gợi ý chọn 1 trong 3 món chính theo hồ sơ cá nhân | P1 |
| NUTR-06 | Mục tiêu dinh dưỡng theo nhóm người ăn (lao động nặng, văn phòng…) và kiểm thực đơn theo mục tiêu | P1 |
| NUTR-07 | Nhật ký dinh dưỡng cá nhân theo các bữa đã ăn | P2 |

### 4.6 ORD: Chọn món, order, chốt số

| Mã | Tính năng | Tác nhân | Ưu tiên |
|---|---|---|---|
| ORD-01 | Người ăn chọn 1 trong 3 món chính cho từng ngày (đặt trước cả tuần được) | A-04, A-05 | P0 |
| ORD-02 | Người đặt tổng xem tổng lựa chọn theo món, bổ sung số cho người chưa chọn, chốt | A-02 | P0 |
| ORD-03 | Quy tắc cho người không chọn trước hạn (món mặc định / chia theo tỷ lệ / người đặt tổng quyết) [CHỜ Q-03] | Không áp dụng | P0 |
| ORD-04 | Hạn chốt theo khách/điểm/ca; hệ thống khoá và phát hành kế hoạch v1 | Hệ thống | P0 |
| ORD-05 | Đổi sau chốt: tính chênh lệch, duyệt theo ngưỡng, tạo phiên bản kế hoạch mới | A-02, A-06, A-07, A-10 | P0 |
| ORD-06 | Nhập hộ khi khách gửi qua Zalo/điện thoại, ghi nguồn và bằng chứng | A-06 | P0 |
| ORD-07 | Nhắc người chưa chọn trước hạn chốt | Hệ thống | P1 |
| ORD-08 | Chế độ không cho chọn (công ty muốn một người đặt như cũ): cấu hình theo khách | A-02 | P1 |

Có cho người ăn chọn cả món phụ/rau/canh không, hay chỉ món chính: [CHỜ Q-05]. Người ăn có tự trả tiền không: [CHỜ Q-11].

### 4.7 Các phân hệ vận hành kế thừa bản HTML

Giữ nội dung bản HTML, sửa theo [bản phân tích](../../GiaPhat_PhanTich_ThietKe.md). Cột "Sửa" chỉ ghi điểm khác với bản cũ.

| Mã | Phân hệ (mã cũ) | Sửa so với bản HTML | Ưu tiên |
|---|---|---|---|
| CUS | Khách hàng 360° (M1) | Thêm Người ăn, Phiên QR, Lịch phục vụ của điểm; lead từ PUB-06 vào tự động | P0 |
| SALE | Cơ hội, báo giá, hợp đồng, phụ lục giá (M2) | Giá theo **loại suất**; báo giá kèm thực đơn và cost nội bộ | P0 |
| PLAN | Kế hoạch ngày, phân ca, phiếu sản xuất, QC, mẫu lưu (M4 phần kế hoạch + M6) | Số chốt/sản xuất **theo món**; ghi rõ cấp chi tiết của 7 loại số | P0 kế hoạch · P1 phân ca, QC |
| PUR | Nhu cầu nguyên liệu, mua hàng, tồn, công nợ NCC (M5) | Chỉ quản lý lô cho hàng đông lạnh/khô; hàng tươi mua–dùng trong ngày; giá nhập ghi về COST-01 | P1 |
| DLV | Giao hàng, xác nhận nhận, chênh lệch (M7) | Giao/nhận **theo suất**; thêm quy tắc số tạm tính khi khách không phản hồi [CHỜ Q-13] | P0 |
| FB | Đánh giá, khiếu nại, phân tích món, đề xuất thực đơn (M8) | Có dữ liệu chọn món thật của từng người → "tỷ lệ được chọn" tính trực tiếp, không qua đầu mối | P1 |
| FIN | Doanh thu, giảm trừ, đối soát, thu tiền, khoá kỳ, xuất MISA (M9) | Mở lại kỳ cần Giám đốc duyệt | P0 |
| EXP | Chi phí cơ sở, chấm công, lợi nhuận theo khách (M10) | Không đổi | P2 |
| RPT | Dashboard theo vai trò, tháp điều hành | Thêm cost % theo ngày, theo khách | P1 |
| SYS | Tham số, nhật ký, thông báo, khoá kỳ, danh mục chủ | Kênh thông báo cho khách và người ăn [CHỜ Q-14] | P0 |

---

## 5. Hai AI agent

### 5.1 Nguyên tắc chung

Cấu trúc kỹ thuật của hai agent (agent runtime, công cụ, MCP, RAG, lan can): [Kiến trúc AI agent](../nen-tang/srs/agent-architecture.md).

1. **AI không tự tính số.** Cost, định lượng, dinh dưỡng, kiểm quy tắc đều do hàm xác định trong MENU/COST/NUTR thực hiện; agent gọi các hàm đó như công cụ và chỉ diễn giải kết quả.
2. **AI chỉ dùng món, công thức đã duyệt.** Không bịa món, không bịa định lượng.
3. **Đầu ra là bản nháp.** Thực đơn do AI tạo luôn đi qua MENU-07, người thật duyệt mới công bố.
4. **Mỗi kết quả kèm bảng kiểm**: quy tắc nào đạt, quy tắc nào vi phạm, cost % (chỉ nội bộ).
5. **Tách hoàn toàn hai agent**: lời nhắc hệ thống, bộ công cụ, tài khoản dịch vụ, hàng đợi, hạn mức chi phí, nhật ký đều riêng. Việc agent phía khách không thấy cost được chặn ở tầng công cụ và quyền cơ sở dữ liệu, không dựa vào lời nhắc.
6. **Mọi lượt chạy đều ghi lại**: ai hỏi, hỏi gì, công cụ nào được gọi, kết quả, chi phí.

### 5.2 AIN: Agent Dinh dưỡng viên (phía khách)

| Mã | Khả năng | Người dùng | Ưu tiên |
|---|---|---|---|
| AIN-01 | Tạo thực đơn tuần cho tập thể theo mức giá suất, số suất, khẩu vị, kiêng kỵ: đúng quy chuẩn docx | A-01 (mẫu), A-02 | P0 |
| AIN-02 | Giải thích thực đơn: vì sao chọn món, định lượng, dinh dưỡng từng suất | A-01, A-02, A-04 | P0 |
| AIN-03 | Chỉnh theo yêu cầu ("đổi cá thứ Tư", "bớt món chiên") và kiểm lại quy tắc | A-02 | P0 |
| AIN-04 | Gửi thực đơn nháp cho Gia Phát duyệt; với khách vãng lai thì chuyển thành lead | A-01, A-02 | P0 |
| AIN-05 | Gợi ý cá nhân: nên chọn món nào trong 3 món hôm nay theo hồ sơ đã khai | A-04, A-05 | P1 |
| AIN-06 | Trả lời câu hỏi dinh dưỡng chung trong phạm vi thực đơn Gia Phát | Tất cả | P1 |

Công cụ được phép: tra món đã duyệt · lấy định lượng theo mức giá · tính dinh dưỡng · kiểm quy tắc thực đơn · **kiểm "đạt/không đạt ngân sách" (chỉ trả về có/không, không trả về con số cost)** · lưu bản nháp · tạo lead.

Giới hạn bắt buộc: không chẩn đoán, không tư vấn điều trị, không thay lời bác sĩ; có lời nhắc rõ ràng khi người dùng nêu bệnh lý; không lộ giá nhập, cost, biên lợi nhuận; không cam kết giá hay hợp đồng; khách vãng lai bị giới hạn số lượt.

### 5.3 AIO: Agent Nội bộ

| Mã | Khả năng | Người dùng | Ưu tiên |
|---|---|---|---|
| AIO-01 | Dựng thực đơn tuần theo quy chuẩn, tính định lượng theo mức giá, kiểm ngưỡng cost, nêu phương án khi vượt | A-06 | P0 |
| AIO-02 | Rà soát thực đơn đã duyệt khi giá nhập đổi; đề xuất đổi món/điều chỉnh định lượng | A-06, A-10 | P1 |
| AIO-03 | Lập bảng dự toán và nhu cầu nguyên liệu từ kế hoạch đã chốt | A-09 | P1 |
| AIO-04 | Cảnh báo giá nhập lệch, đối chiếu dự toán với thực mua | A-09, A-10 | P1 |
| AIO-05 | CRM: tóm tắt khách, nhắc việc, soạn nháp báo giá, nêu khách có nguy cơ rời kèm căn cứ | A-06, A-10 | P1 |
| AIO-06 | Hỏi đáp số liệu bằng lời (doanh thu, công nợ, cost theo khách, OTIF) | A-10, A-09 | P2 |

Công cụ: toàn bộ công cụ của AIN + đọc cost/giá nhập + đọc kế hoạch, tồn, đơn mua + đọc CRM + truy vấn báo cáo.

Giới hạn bắt buộc: quyền của agent = quyền của người đang dùng (quản lý cơ sở không hỏi được số liệu cơ sở khác); hỏi đáp số liệu chỉ qua các khung nhìn báo cáo định sẵn, chỉ đọc, không cho AI tự viết câu lệnh ghi dữ liệu; mọi hành động thay đổi dữ liệu là bản nháp chờ người duyệt.

---

## 6. Thứ tự viết tài liệu theo ba-kit

### 6.1 Tầng sản phẩm: viết một lần, theo đúng thứ tự

| Bước | Lệnh | File đầu ra | Nội dung phải có | Điều kiện để sang bước sau |
|---|---|---|---|---|
| 0 | Không áp dụng | `docs/gia-phat/00-ke-hoach-tong-the.md` | File này | Anh trả lời mục 9 |
| 1 ✅ nháp v0.1.0 (11/11/2026), gate chưa đạt | `/brainstorm` | `docs/gia-phat/brainstorms/pham-vi-san-pham.md` | Chốt các câu hỏi mở Q-01 → Q-19, ghi quyết định và lý do | Không còn mục [CHỜ] chặn P0 |
| 2 | `/brainstorm` | `docs/gia-phat/brainstorms/quy-tac-thuc-don.md` | Chuyển từng câu trong docx thành quy tắc cứng/mềm có con số, cùng dinh dưỡng viên | Mỗi quy tắc có mã, loại, ngưỡng |
| 3 ✅ nháp v0.1.0 (10/11/2026) | `/brd` | [`docs/gia-phat/06-brd.md`](06-brd.md) | Mục tiêu kinh doanh, phạm vi, rủi ro, chi phí–lợi ích (gồm chi phí AI và hạ tầng) | Giám đốc duyệt |
| 4 ✅ nháp v0.1.0 (10/11/2026) | `/urd` | [`docs/gia-phat/05-urd.md`](05-urd.md) | Chân dung và hành trình của A-01 → A-10 | Không áp dụng |
| 5 ✅ nháp v0.1.0 (10/11/2026) | `/prd` | [`docs/gia-phat/01-prd.md`](01-prd.md) | Tầm nhìn, phạm vi, bảng bóc tách tính năng (lấy từ mục 4, 5) | Không áp dụng |
| 6 ✅ nháp v0.1.0 (10/11/2026) | `/roadmap` | [`docs/gia-phat/02-roadmap.md`](02-roadmap.md) | Now / Next / Later (lấy từ mục 7) | Không áp dụng |
| 7 ✅ nháp v0.1.0 (10/11/2026) | `/srs` | [`docs/nen-tang/srs/spec.md`](../nen-tang/srs/spec.md) | NFR toàn hệ thống, kiến trúc mục 3, phân quyền, nhật ký | NFR có con số đo được |
| 8 ✅ nháp v0.1.0 (10/11/2026) | `/erd` → `/dbdiagram` | [`docs/nen-tang/srs/erd.md`](../nen-tang/srs/erd.md), [`schema.dbml`](../nen-tang/srs/schema.dbml) | Mô hình dữ liệu tổng (bổ sung các thực thể thiếu đã nêu trong bản phân tích) | Mọi epic sau dùng chung mô hình này |

### 6.2 Tầng epic: lặp lại cho từng epic

Chuỗi chuẩn cho một epic (`{feature}` = tên thư mục epic):

| Thứ tự | Lệnh | File đầu ra |
|---|---|---|
| 1 | `/prd-epic` | `docs/{feature}/epic-spec.md` |
| 2 | `/srs` | `docs/{feature}/srs/spec.md` (FR, BR, ERR, NFR riêng) |
| 3 | `/usecase-diagram` → `/usecase` | `docs/{feature}/srs/usecase-diagram.md`, `usecases/{id}.md` |
| 4 | `/user-flow` | `docs/{feature}/ui/user-flow.md` |
| 5 | `/activity-swimlane` hoặc `/sequence` | `docs/{feature}/srs/activity-swimlane.puml`, `flows.md` |
| 6 | `/state` | `docs/{feature}/srs/states.md` |
| 7 | `/erd` | `docs/{feature}/srs/erd.md` (phần riêng của epic) |
| 8 | `/api-design` | `docs/{feature}/api/api-spec.md` |
| 9 | `/wireframe-html` | `docs/{feature}/html-wireframe/{màn hình}.html` |
| 10 | `/userstory` → `/ac` | `docs/{feature}/userstories/backlog.md`, `acceptance-criteria.md` |
| 11 | `/test-checklist` → `/test-cases` | `docs/{feature}/test/checklist.md`, `test-cases.md` |
| 12 | `/gap` | `docs/{feature}/gap-analysis.md` |
| 13 | `/preview` | `docs/{feature}/preview.html` |

Sau mỗi epic chạy `/update-overview` (`docs/OVERVIEW.md`) và `/dashboard` (`docs/project-dashboard.md`).

### 6.3 Thứ tự các epic

Xếp theo phụ thuộc dữ liệu: epic sau dùng dữ liệu của epic trước.

| # | Epic (`{feature}`) | Gồm phân hệ | Phụ thuộc | Vì sao ở vị trí này |
|---|---|---|---|---|
| E1 | [`nen-tang`: hồ sơ nháp](../nen-tang/preview.html) | AUTH, SYS | Không có | Tài khoản, phân quyền, nhật ký là nền của mọi thứ |
| E2 | `thuc-don-dinh-luong`: [epic-spec nháp v0.1.0](../thuc-don-dinh-luong/epic-spec.md) (10/11/2026) | MENU | E1 | Món, công thức, định lượng, bộ kiểm quy tắc: lõi dữ liệu |
| E3 | `cost`: [epic-spec nháp v0.1.0](../cost/epic-spec.md) (11/11/2026) | COST | E2 | Cần công thức và định lượng mới tính được cost |
| E4 | [`dinh-duong`: hồ sơ nháp](../dinh-duong/preview.html) | NUTR | E2 | Cần định lượng mới tính được dinh dưỡng |
| E5 | [`agent-noi-bo`: FEAT-021–023](../agent-noi-bo/preview.html) | AIO | E2, E3 | Giúp dinh dưỡng viên dựng thực đơn sớm, giảm điểm nghẽn một người |
| E6 | [`chon-mon-order`: gói BA review](../chon-mon-order/preview.html) | ORD, CUS (phần người ăn), PLAN (phần kế hoạch) | E1, E2 | Điểm tải cao nhất; cần thực đơn đã công bố |
| E7 | `giao-nhan-doanh-thu` | DLV, FIN | E6 | Khép vòng tiền |
| E8 | `website-cong-khai` | PUB | E2, E4 | Cần thực đơn mẫu và dinh dưỡng để hiển thị |
| E9 | `agent-dinh-duong-vien` | AIN | E2, E4, E6, E8 | Cần dữ liệu đã duyệt và các mặt tiền để gắn vào |
| E10 | `crm-ban-hang` | CUS, SALE | E1, E8 | Nhận lead từ website |
| E11 | `mua-hang-san-xuat` | PUR, PLAN (phân ca, QC) | E3, E6 | Không áp dụng |
| E12 | `phan-hoi-bao-cao` | FB, RPT, AIO-03 → 06 | E6, E7, E10, E11 | Cần dữ liệu vận hành tích luỹ |
| E13 | `chi-phi-loi-nhuan` | EXP | E7, E11 | Như giai đoạn 3 của bản HTML |

---

## 7. Lộ trình sơ bộ (đầu vào cho `/roadmap`)

Không ghi thời lượng vì chưa biết quy mô đội phát triển [CHỜ Q-15].

| Đợt | Epic | Kết quả nhìn thấy được |
|---|---|---|
| **Now** | E1 → E5 | Dinh dưỡng viên dựng thực đơn tuần bằng agent, hệ thống tự kiểm quy tắc và ngưỡng 52%, có bảng dự toán |
| **Next** | E6 → E9 | Người ăn chọn món, công ty chốt số, giao nhận – đối soát trên hệ thống; website mới thay WordPress; khách dùng Agent Dinh dưỡng viên |
| **Later** | E10 → E13 | CRM đầy đủ, mua hàng – sản xuất, phản hồi, báo cáo, lợi nhuận theo khách |

---

## 8. Rủi ro chính

| # | Rủi ro | Giảm thiểu |
|---|---|---|
| R-01 | Dữ liệu gốc chưa có: công thức theo mức giá, giá nhập, thành phần dinh dưỡng. Agent và tính năng chọn món không chạy được nếu thiếu. | Bước 2 mục 6.1 và E2–E4 làm trước; nhập dần các món dùng nhiều nhất. |
| R-02 | Một dinh dưỡng viên gánh quá nhiều vai. | E5 làm sớm; có người dự phòng quyền duyệt. |
| R-03 | Dữ liệu sức khoẻ cá nhân là dữ liệu nhạy cảm theo quy định bảo vệ dữ liệu cá nhân của Việt Nam (Nghị định 13/2023/NĐ-CP và luật liên quan). | Tự nguyện, có đồng ý, mã hoá, xoá được; cần ý kiến pháp lý trước khi mở NUTR-04. |
| R-04 | Agent phía khách nói sai về dinh dưỡng/bệnh lý, hoặc lộ cost. | Giới hạn ở mục 5.2; cost chặn ở tầng công cụ; kiểm thử riêng cho agent. |
| R-05 | Chi phí AI tăng theo lượt dùng công khai. | Hạn mức theo ngày, giới hạn khách vãng lai, cache kết quả thực đơn mẫu. |
| R-06 | Mất SEO khi bỏ WordPress. | Giữ URL, 301, sitemap, kiểm tra trước khi chuyển tên miền. |
| R-07 | Người ăn không chọn → số đặt thiếu ổn định, ảnh hưởng mua hàng. | Quy tắc mặc định Q-03, nhắc trước hạn, người đặt tổng chốt cuối. |
| R-08 | Nhân sự Rust khó tuyển hơn NodeJS; đội phát triển chưa xác định (Q-15). Thư viện hàng đợi, MCP và lời gọi mô hình AI phía Rust đổi nhanh. | Trả lời Q-15 trước khi dựng khung mã; ghim phiên bản thư viện; chi tiết ở [CR-CORE-2026-001](../nen-tang/cr/CR-CORE-2026-001.md) mục 3. |

---

## 9. Câu hỏi cần anh trả lời (chưa tự suy đoán)

**Chặn P0: cần trước khi viết BRD/PRD**

| Mã | Câu hỏi |
|---|---|
| Q-01 | Khách vãng lai có được thấy **giá suất / báo giá sơ bộ** không, hay chỉ thấy thực đơn mẫu và phải để lại thông tin? |
| Q-02 | Người ăn được định danh thế nào? (a) Có tài khoản: tự đăng ký bằng mã công ty, công ty nhập danh sách, hay đăng nhập bằng số điện thoại/Zalo? (b) Qua QR: nhập mã nhân viên, số điện thoại, hay hoàn toàn ẩn danh (chấp nhận rủi ro một người chọn nhiều lần)? |
| Q-03 | Người ăn **không chọn** trước hạn chốt thì tính thế nào: món mặc định, chia theo tỷ lệ những người đã chọn, hay người đặt tổng tự nhập phần còn lại? |
| Q-04 | Ngưỡng 52% tính trên giá suất **trước hay sau VAT**? Cost gồm những gì: gạo, gia vị, dầu ăn, gas, hộp/khay, tráng miệng? |
| Q-05 | Cơ cấu một suất 40k: cơm + 1 món chính + **mấy món phụ** + rau + canh? Người ăn chỉ chọn món chính, hay chọn cả món phụ/rau/canh? |
| Q-06 | Ai cùng tôi chuyển quy tắc định tính trong docx thành con số (ví dụ "nhiều ngày liên tiếp" = mấy ngày; "lặp trong tuần" = tối đa mấy lần; phương pháp nào được tính là Healthy)? |
| Q-07 | Gia Phát đang bán những **mức giá suất** nào ngoài 40k? Với mỗi mức đã có bảng định lượng riêng chưa, hay cần quy tắc suy ra từ bảng 40k? |
| Q-08 | Dữ liệu dinh dưỡng lấy từ đâu: bảng thành phần thực phẩm Việt Nam của Viện Dinh dưỡng, dữ liệu dinh dưỡng viên đang có, hay nguồn khác? Cần hiển thị những chỉ số nào? |

Trạng thái sau vòng 3 (10/11/2026): Q-01 đã chốt (D-10) · Q-05 đã chốt hướng (D-12) · Q-02 chốt một nửa (D-11) · Q-03, Q-04, Q-06, Q-08 đã giải thích và có phương án đề xuất, chờ anh xác nhận · Q-07 chưa trả lời.

Trạng thái sau vòng 4 (10/11/2026): đã chốt Q-02b, Q-03, Q-06, Q-07, Q-08, Q-20 (D-14 → D-20). **Còn mở trong nhóm P0**: Q-04 phần "cost gồm những khoản nào" và thuế suất VAT (chuyển thành H-6, H-7 trong bảng quy tắc) · Q-21 · Q-22 (mới: một món một định lượng hay nhiều cỡ định lượng, H-9 trong bảng quy tắc).

**Phát sinh từ vòng 3**

| Mã | Câu hỏi |
|---|---|
| Q-02b | Xác minh người ăn bằng gì: mã OTP qua số điện thoại, mã công ty/QR của công ty, người đặt tổng duyệt danh sách, hay kết hợp? |
| Q-20 | Giá suất tuỳ biến tính từ đâu: mỗi món có **giá bán riêng** do nội bộ đặt, hay hệ thống suy ra từ cost ÷ tỷ lệ cost mục tiêu? |
| Q-21 | Ai được tuỳ biến suất: **công ty** đặt định mức chung rồi người ăn chọn trong định mức, hay **từng người ăn** tự dựng suất với giá khác nhau? |

**Chặn thiết kế agent và hạ tầng**

| Mã | Câu hỏi |
|---|---|
| Q-09 | Mô hình AI: anh đã chọn nhà cung cấp chưa (Claude, GPT, Gemini…)? Ngân sách AI mỗi tháng khoảng bao nhiêu? Có yêu cầu dữ liệu không ra khỏi Việt Nam không? |
| Q-10 | Gợi ý cá nhân dừng ở mức nào: chỉ mục tiêu chung (giảm cân, tăng cơ, ăn nhạt) và dị ứng, hay cả **bệnh lý** (tiểu đường, huyết áp, gout…)? |
| Q-11 | Người ăn có **tự trả tiền** phần nào không (ví dụ chọn món đắt hơn thì bù), hay công ty trả toàn bộ như hiện nay? |
| Q-12 | Hạ tầng: chạy trên máy chủ nào (VPS trong nước, AWS, Google Cloud…)? Ai vận hành sau khi lên? |
| Q-15 | Đội phát triển gồm mấy người, kỹ năng gì, thời hạn mong muốn cho bản đầu? |

**Kế thừa từ bản HTML: vẫn đang là "giả định"**

| Mã | Câu hỏi |
|---|---|
| Q-13 | Khách không xác nhận số nhận: có chấp nhận quy tắc "quá N ngày không phản đối thì lấy số giao làm số tạm tính, chốt lại khi đối soát tháng" không? N bằng bao nhiêu? |
| Q-14 | Gia Phát đã có **Zalo OA** chưa? Kênh thông báo cho người đặt tổng và người ăn là gì (Zalo ZNS, SMS, email, thông báo trong app)? |
| Q-16 | Hạn chốt ca trưa 15:00 ngày D-1 và ngưỡng đổi sau chốt (5% / 10 suất / trước 06:00) có đúng thực tế không? Ngưỡng là "nhỏ hơn trong hai" hay "lớn hơn trong hai"? |
| Q-17 | Vai trò Giám đốc trong bản HTML là giả định: ai là người duyệt ngoại lệ, và ai thay khi vắng? |
| Q-18 | Số khách doanh nghiệp đang phục vụ, tổng số người ăn mỗi ngày, số điểm giao là bao nhiêu? (Website ghi 125+ đối tác, dashboard mẫu ghi 26 khách.) |
| Q-19 | Trường học, bệnh viện, tiệc cỗ có nằm trong phạm vi bản đầu không? (Trường học và bệnh viện có yêu cầu dinh dưỡng riêng.) |

## Cập nhật E6 ngày 11/11/2026

Hoàn thiện gói tài liệu để review theo [bàn giao E6](../chon-mon-order/review/handoff.md), chưa chốt baseline hoặc release. Có UC/flow/state/data/API/wireframe/story/AC/test/RTM/preview. ORD-Q01–15 và O-03 còn chờ; delta schema không merge; không triển khai backend/E7–E13. Các nhãn gói khởi đầu trong lịch sử là mốc trước phiên này.
