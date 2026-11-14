---
id: DOC-HUONG-DAN-DOC
title: Hướng dẫn đọc bộ tài liệu Gia Phát và bảng thuật ngữ
version: 0.1.1
phase: Review
domain: Gia Phát
tags: [huong-dan, thuat-ngu, onboarding]
author: BA
last_updated: 2026-11-14
---
# Hướng dẫn đọc bộ tài liệu Gia Phát và bảng thuật ngữ

Phiên bản 0.1.1 · 14/11/2026 · Người viết: BA.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.1 | 2026-11-14 | BA | Công nghệ đổi sang Rust/Axum theo D-22; thêm hai tài liệu kiến trúc vào lộ trình đọc của Dev |
| 0.1.0 | 2026-11-13 | BA | Khởi tạo: bản đồ thư mục, lộ trình đọc theo vai trò, 4 ví dụ đọc, cách giải mã mã định danh, bảng thuật ngữ |

File này giúp người mới đọc được kho tài liệu `D:\BA` mà không bị lạc giữa hơn 1.200 file và hàng trăm loại mã. Nó **không thay** nội dung của tài liệu nào; khi có khác biệt, tài liệu gốc được dẫn link là căn cứ.

---

## 1. Dự án này là gì (đọc trong 1 phút)

**Gia Phát** là doanh nghiệp cung cấp suất ăn tập thể (công ty, nhà máy, văn phòng), có 2 cơ sở bếp và website comgiaphat.com. Kho tài liệu này là **hồ sơ phân tích nghiệp vụ (BA)** cho một nền tảng mới gồm:

- **Website công khai** thay WordPress, có thực đơn mẫu, giá, dinh dưỡng, form để lại thông tin.
- **Cổng khách hàng và người ăn**: người ăn tự chọn 1 trong 3 món chính mỗi ngày (qua tài khoản hoặc mã QR công ty); người đặt tổng chốt số suất.
- **Quản trị nội bộ**: nguyên liệu, món, công thức định lượng, thực đơn tuần, **cost** (chi phí nguyên liệu) với ngưỡng 52% doanh thu, giao nhận, doanh thu, CRM, mua hàng, báo cáo, lợi nhuận.
- **Hai AI agent**: Agent Nội bộ (giúp dinh dưỡng viên dựng thực đơn) và Agent Dinh dưỡng viên (phía khách).

Công nghệ đã chốt: ReactJS, Rust/Axum, MySQL; chịu tải 1.000 người dùng đồng thời. Backend đổi từ NodeJS/NestJS sang Rust ngày 14/11/2026 theo [CR-CORE-2026-001](nen-tang/cr/CR-CORE-2026-001.md).

> **Điều quan trọng nhất cần nhớ khi đọc:** toàn bộ kho là **tài liệu nháp (Draft)**. Chưa có backend, chưa có migration, chưa có UAT, **0 câu hỏi mở được trả lời, 0 tính năng được phê duyệt, 0 ca kiểm thử sản phẩm đã chạy**. Mọi con số "độ phủ" (ví dụ 75/78 ≈ 96,2%) chỉ đo **tài liệu đã viết**, không đo phần mềm đã làm hay nghiệp vụ đã duyệt.

---

## 2. Bản đồ kho tài liệu

### 2.1 Các file ở gốc

| File | Là gì | Khi nào đọc |
| :--- | :--- | :--- |
| [GiaPhat_PhanTich_ThietKe.md](../GiaPhat_PhanTich_ThietKe.md) | Bản phân tích ban đầu (10/11/2026): so bản thiết kế C-MAP/CRM cũ với mục tiêu mới, chỉ ra mâu thuẫn mức A/B/C | Muốn hiểu **vì sao** dự án được tổ chức như hiện nay |
| [docs/OVERVIEW.md](OVERVIEW.md) | Nhật ký tiến độ, ghi theo kiểu **chỉ thêm vào cuối** (append-only) | Muốn biết trạng thái mới nhất: đọc **mục cuối cùng** trước |
| [docs/project-dashboard.md](project-dashboard.md) | Bảng số liệu độ phủ FR → story → test theo epic | Muốn số đếm tổng hợp |
| `docs/HUONG-DAN-DOC.md` | File này | Lần đầu vào kho |

### 2.2 Tầng sản phẩm: `docs/gia-phat/`

Viết một lần cho toàn sản phẩm, theo thứ tự:

| File | Nội dung | Mã định danh chính xuất hiện |
| :--- | :--- | :--- |
| [00-ke-hoach-tong-the.md](gia-phat/00-ke-hoach-tong-the.md) | Kế hoạch tổng: quyết định đã chốt, tác nhân, kiến trúc đề xuất, danh mục tính năng, thứ tự viết tài liệu, rủi ro, câu hỏi | `D-xx`, `Q-xx`, `A-xx`, `R-xx` |
| [brainstorms/pham-vi-san-pham.md](gia-phat/brainstorms/pham-vi-san-pham.md) | Sổ chốt phạm vi | `Q-xx` |
| [brainstorms/quy-tac-thuc-don.md](gia-phat/brainstorms/quy-tac-thuc-don.md) | 43 quy tắc thực đơn và cost viết lại từ file docx, chờ duyệt | `BR-MENU-xxx`, `BR-COST-xxx`, `H-x` |
| [06-brd.md](gia-phat/06-brd.md) | BRD: mục tiêu kinh doanh, phạm vi, ROI, rủi ro, giả định, điểm mở | `BO-xx`, `BN-xx`, `AS-xx`, `DP-xx`, `O-xx`, `C-xx` |
| [05-urd.md](gia-phat/05-urd.md) | URD: chân dung và nhu cầu người dùng | `A-xx`, `UN-xx` |
| [01-prd.md](gia-phat/01-prd.md) | PRD: tầm nhìn, OKR, persona, **78 tính năng** | `FEAT-xxx`, `PER-xx`, `KRx.x` |
| [02-roadmap.md](gia-phat/02-roadmap.md) | Lộ trình Now / Next / Later, 13 đợt phát hành, cổng chuyển đợt | `R1`→`R13`, `G-Now`, `G-Next`, `DL-xx` |
| `review/decision-pack/` | **Gói quyết định** (13/11/2026): gom 224 câu hỏi mở thành 214 nhóm `DEC`, xếp 9 buổi họp | `DEC-xx`, `XC-xx`, `BA-Qxx` |
| [review/cau-hoi-theo-nghiep-vu.md](gia-phat/review/cau-hoi-theo-nghiep-vu.md) | Cùng 224 câu đó, xếp theo nghiệp vụ và mức quan trọng | `P-MVP`, `P-NOW`, `P-NEXT`, `P-LATER` |
| `validation/` | Script và kết quả kiểm tra của tầng sản phẩm | |

### 2.3 Tầng epic: 13 thư mục, mỗi thư mục một epic

| Epic | Thư mục | Phân hệ (module) | Tiền tố use case | Đợt |
| :--- | :--- | :--- | :--- | :--- |
| E1 | [nen-tang](nen-tang/preview.html) | AUTH, SYS | `UC-CORE` | Now |
| E2 | [thuc-don-dinh-luong](thuc-don-dinh-luong/preview.html) | MENU | `UC-MENU` | Now |
| E3 | [cost](cost/preview.html) | COST (+ ACC kế toán) | `UC-COST` | Now |
| E4 | [dinh-duong](dinh-duong/preview.html) | NUTR | `UC-NUTR` | Now |
| E5 | [agent-noi-bo](agent-noi-bo/preview.html) | AIO | `UC-AIO` | Now (MVP v1.0.0) |
| E6 | [chon-mon-order](chon-mon-order/preview.html) | ORD, CUS (người ăn), PLAN | `UC-ORD` | Next |
| E7 | [giao-nhan-doanh-thu](giao-nhan-doanh-thu/preview.html) | DLV, FIN | `UC-DLV`, `UC-FIN` | Next |
| E8 | [website-cong-khai](website-cong-khai/preview.html) | PUB | `UC-PUB` | Next |
| E9 | [agent-dinh-duong-vien](agent-dinh-duong-vien/preview.html) | AIN | `UC-AIN` | Next |
| E10 | [crm-ban-hang](crm-ban-hang/preview.html) | CUS, SALE | `UC-CRM` | Later |
| E11 | [mua-hang-san-xuat](mua-hang-san-xuat/preview.html) | PUR, PLAN (phân ca, QC) | `UC-PUR` | Later |
| E12 | [phan-hoi-bao-cao](phan-hoi-bao-cao/preview.html) | FB, RPT, một phần AIO | `UC-FBR` | Later |
| E13 | [chi-phi-loi-nhuan](chi-phi-loi-nhuan/preview.html) | EXP | `UC-EXP` | Later |

Thứ tự E1 → E13 là thứ tự **phụ thuộc dữ liệu**: epic sau dùng dữ liệu epic trước (ví dụ Cost cần công thức của Thực đơn mới tính được).

### 2.4 Bên trong một thư mục epic

Mọi epic theo cùng một khuôn (một số epic thiếu vài file hoặc có thêm file riêng). Đọc từ trên xuống là đi từ "cái gì" tới "kiểm thế nào":

| Đường dẫn | Là gì | Câu hỏi nó trả lời |
| :--- | :--- | :--- |
| `preview.html` | Trang HTML gom toàn bộ tài liệu và sơ đồ của epic, mở bằng trình duyệt | "Cho tôi xem nhanh toàn bộ epic" |
| `epic-spec.md` | Đặc tả epic: tính năng nào, P0/P1/P2, kế hoạch release | Epic này làm gì, ưu tiên gì |
| `srs/spec.md` | **SRS**: yêu cầu chức năng (FR), quy tắc (BR), lỗi (ERR), phi chức năng (NFR), điểm mở | Hệ thống phải làm **chính xác** gì |
| `srs/usecase-diagram.md` | Sơ đồ use case và ma trận FR ↔ UC | Ai dùng chức năng nào |
| `srs/flows.md` | Sơ đồ tuần tự / hoạt động | Các hệ thống gọi nhau theo thứ tự nào |
| `srs/states.md` | Sơ đồ trạng thái | Một đối tượng (phiếu, thực đơn…) đi qua những trạng thái nào |
| `srs/erd.md`, `srs/data-dictionary.md` | Mô hình dữ liệu / từ điển dữ liệu (các epic sau gọi là **delta**, tức phần đề xuất thêm, chưa gộp vào schema chung) | Lưu dữ liệu gì, ràng buộc gì |
| `srs/error-matrix.md` | Ma trận mã lỗi | Lỗi nào, HTTP gì, hiện thông báo gì |
| `srs/diagrams/` | Sơ đồ đã render ra SVG/HTML | Xem sơ đồ đẹp thay cho mã Mermaid |
| `usecases/UC-xxx-nnn.md` | Use case chi tiết (chuẩn Cockburn) | Từng bước người dùng và hệ thống làm gì, ngoại lệ nào |
| `usecases/index.md` | Mục lục use case | |
| `ui/user-flow.md` | Luồng người dùng, có quy ước dùng chung về lỗi/quyền | Người dùng đi qua các màn nào |
| `ui/screens.md`, `ui/screen-catalog.md`, `ui/wireframe-ascii.md` | Danh mục màn hình / phác thảo ký tự | Có những màn nào |
| `html-wireframe/*.html` | Wireframe HTML bấm được, **dữ liệu minh họa** | Màn hình trông thế nào |
| `api/api-spec.md`, `api/endpoint-catalog.json` | Thiết kế API đề xuất (bản người đọc và bản máy đọc) | Endpoint nào, quyền gì, request/response gì |
| `api/data-mapping.md` | Ánh xạ trường API ↔ bảng dữ liệu ↔ màn hình | Trường này lấy từ đâu |
| `userstories/backlog.md` | User story, điểm ước lượng, ưu tiên | Việc giao cho đội phát triển |
| `userstories/acceptance-criteria.md` | Tiêu chí nghiệm thu dạng Given / When / Then | Thế nào là "xong" |
| `test/checklist.md` | Dàn ý kịch bản test | Cần test những nhóm gì |
| `test/test-cases.md` | Test case chi tiết, có cột Trạng thái / Actual / Evidence | Test từng bước thế nào |
| `test/system-cases.md`, `invariant-cases.md`… | Ca kiểm thử mức hệ thống / bất biến | Kiểm xuyên nhiều chức năng |
| `test/traceability.md` | **RTM**: ma trận truy vết FR → story → AC → test → API | Mỗi yêu cầu đã có story/test chưa |
| `test/fixtures/` | Dữ liệu giả lập (synthetic) dùng cho test | Dữ liệu mẫu |
| `test/evidence-protocol.md` | Quy ước ghi bằng chứng khi chạy test thật sau này | |
| `test/rN-acceptance.md` | Ca nghiệm thu mức release (R9, R10…) | Đợt này đạt khi nào |
| `review/questions.md` | **Câu hỏi mở** của epic, cột Trả lời để trống | Còn chưa biết gì |
| `review/dependencies.md` | Phụ thuộc vào epic khác (producer) | Epic này chờ ai |
| `review/handoff.md` | Gói bàn giao: tóm tắt, cách đọc, việc còn lại | Đọc đầu tiên nếu bạn là người review |
| `gap-analysis.md` | Rà khoảng trống | Tài liệu còn thiếu gì |
| `validation/` | Script kiểm (`.cjs`, `.py`), kết quả (`.json`), ảnh chụp, `report.md` | Tài liệu đã được tự kiểm những gì |

> Mẹo: thư mục `validation/` phục vụ kiểm chất lượng **tài liệu**. Người đọc nghiệp vụ chỉ cần `validation/report.md`; các file `.json`, `.cjs`, `.py` và `baseline*.json` dành cho người bảo trì kho.

---

## 3. Lộ trình đọc theo vai trò

### 3.1 Người mới, 30 phút

1. Mục 1 của file này.
2. [GiaPhat_PhanTich_ThietKe.md](../GiaPhat_PhanTich_ThietKe.md) mục 1 "Kết luận ngắn".
3. [Roadmap](gia-phat/02-roadmap.md): khung Now / Next / Later và sơ đồ phụ thuộc.
4. [PRD](gia-phat/01-prd.md) mục 1 (mục tiêu) và mục 2 (persona).
5. Mục cuối của [OVERVIEW](OVERVIEW.md) để biết trạng thái hiện tại.
6. Mở một `preview.html` bất kỳ (gợi ý: [Cost](cost/preview.html)) để thấy một epic hoàn chỉnh trông thế nào.

### 3.2 Giám đốc / người ra quyết định

1. [Gói quyết định: đọc trong 5 phút](gia-phat/review/decision-pack/README.md).
2. [Chương trình họp](gia-phat/review/decision-pack/meeting-agenda.md): buổi 1 → 3 là các quyết định chặn MVP.
3. [Câu hỏi theo nghiệp vụ](gia-phat/review/cau-hoi-theo-nghiep-vu.md): lọc mức 🔴 Cao (`P-MVP`).
4. [BRD](gia-phat/06-brd.md) mục 3 (mục tiêu), 8 (ROI), 11 (điểm mở `O-01` → `O-06`).

### 3.3 Dev / Tech lead

1. [SRS nền tảng](nen-tang/srs/spec.md) (NFR toàn hệ thống, phân quyền, nhật ký) và [ERD](nen-tang/srs/erd.md) / [schema.dbml](nen-tang/srs/schema.dbml) (65 bảng).
   - [Kiến trúc hệ thống](nen-tang/srs/architecture.md): các tầng, cấu trúc mã nguồn Rust và React.
   - [Kiến trúc AI agent](nen-tang/srs/agent-architecture.md): công cụ, MCP, RAG, lan can.
2. Với epic được giao: `srs/spec.md` → `api/api-spec.md` → `srs/states.md` → `review/dependencies.md`.
3. Đọc kỹ cột **Gate / Điểm mở** trong mỗi bảng: phần có gate chưa được phép "đóng băng" (freeze) để code.

### 3.4 QA / Tester

1. `test/checklist.md` → `test/test-cases.md` → `test/traceability.md` của epic.
2. `review/blocked-tests.md` (nếu có) để biết ca nào đang chờ đầu vào gì.
3. `test/fixtures/README.md`: dữ liệu mẫu là **giả lập**, chưa phải dữ liệu nghiệm thu.

### 3.5 Kế toán

1. [Quy tắc kế toán đã làm rõ](cost/accounting/business-rules.md) và [hướng dẫn](cost/user-guide.md).
2. [Phiếu dữ liệu kế toán](cost/review/accountant-input.md): dữ liệu 10 món / 10 ngày cần cung cấp.
3. [Sổ điểm mở Cost](cost/review/decision-register.md).

---

## 4. Ví dụ đọc

### Ví dụ 1: lần theo một yêu cầu từ PRD xuống test case

Mục tiêu: hiểu trọn vẹn chức năng "nhập nhiều giá nguyên liệu cùng lúc".

**Bước 1. PRD cho biết tính năng tồn tại.** Trong [01-prd.md](gia-phat/01-prd.md), bảng tính năng có dòng:

| `FEAT-014` | COST | COST-01 | Bảng giá nhập | P0 | PER-07 | Theo nguyên liệu × nhà cung cấp × ngày hiệu lực; nhập tay và nhập từ file |

Đọc: tính năng số 14, thuộc phân hệ COST, bắt buộc cho bản đầu (P0), người dùng chính là `PER-07` (Kế toán).

**Bước 2. SRS chia tính năng thành yêu cầu chức năng.** Trong [cost/srs/spec.md](cost/srs/spec.md), mục "Giá nhập: `FEAT-014`" có:

| `FR-COST-PRC-004` | Nhập giá dạng lưới | P0 | … Lưu tất cả hoặc không gì cả. | … |

Giải mã `FR-COST-PRC-004`: **FR** = yêu cầu chức năng, **COST** = phân hệ, **PRC** = nhóm chức năng "price" (giá), **004** = số thứ tự.

**Bước 3. Use case mô tả từng bước.** [UC-COST-003](cost/usecases/UC-COST-003.md) ghi:

- Tác nhân: Kế toán mua hàng. Cấp độ: *Sea level* (một mục tiêu người dùng hoàn thành trong một lần ngồi).
- Quyền: `cost.price.read`, `cost.price.write`.
- Luồng chính bước 5: "ghi toàn bộ dòng hợp lệ cùng audit trong một giao dịch hoặc không ghi dòng nào".
- Ngoại lệ `3a`: một dòng lỗi → trả `ERR-COST-422-01`… và **không lưu dòng nào**.
- Truy vết: `FR-COST-PRC-004`; màn hình `SCR-COST-03`.

Ký hiệu `3a` nghĩa là "nhánh rẽ thứ nhất tại bước 3 của luồng chính".

**Bước 4. User story giao việc.** [cost/userstories/backlog.md](cost/userstories/backlog.md):

> US-COST-004: Nhập lưới nguyên tử. Là một **kế toán mua hàng**, tôi muốn **lưu nhiều giá trong một lượt** để **giảm thao tác mà không ghi dở dang**.

Bảng tóm tắt cho biết điểm ước lượng 3, P0, giao tiếp đề xuất `API-COST-006`, `API-COST-037`.

**Bước 5. Tiêu chí nghiệm thu nói "xong" là gì.** [acceptance-criteria.md](cost/userstories/acceptance-criteria.md):

```gherkin
Scenario: AC-COST-004-02 Một dòng sai rollback
  Given lô có I1 giá 110000 và I2 giá 0
  When lưu lô; kiểm số giá trước/sau
  Then báo ERR-COST-422-01 gắn dòng I2; không tạo giá I1 hoặc I2
```

Đọc: *Given* = bối cảnh ban đầu, *When* = hành động, *Then* = kết quả bắt buộc. `AC-COST-004-02` = tiêu chí thứ 2 của story 004.

**Bước 6. API.** [cost/api/api-spec.md](cost/api/api-spec.md), `API-COST-006: Lưu lưới giá`: `POST /v1/cost/price-batches`, quyền `cost.price.write`, trả 201, "toàn lô nguyên tử".

**Bước 7. Test case.** [cost/test/test-cases.md](cost/test/test-cases.md) có `TC-COST-004-01` với cột **Trạng thái: NOT RUN (chưa có backend)** và **Actual / Evidence / Defect: Chưa chạy / Chưa có / Chưa có**.

**Bước 8. RTM xác nhận chuỗi liên kết.** [cost/test/traceability.md](cost/test/traceability.md):

| FR-COST-PRC-004 | US-COST-004 | AC-COST-004-01 … 05 | TC-COST-004-01 … 05 | API-COST-006, API-COST-037 | Draft; xem gate từng ca |

Kết luận đọc: chức năng đã được **đặc tả đủ chuỗi**, nhưng **chưa được code và chưa test**.

### Ví dụ 2: từ một câu hỏi mở tới buổi họp quyết định

1. Trong [chon-mon-order/review/questions.md](chon-mon-order/review/questions.md) có `ORD-Q01`: "Định danh duy nhất người ăn có tài khoản/QR bằng gì…", trạng thái **CHỜ XÁC NHẬN**.
2. Trong [sổ quyết định](gia-phat/review/decision-pack/decision-register.md), dòng `ORD-Q01` cho biết: nhóm quyết định `DEC-07`, người quyết định "Gia Phát, BA", chặn release `R6`, mức `P-NEXT`, "9 ca (gate trực tiếp)", cột **Trả lời trống**.
3. [decision-groups.md#dec-07](gia-phat/review/decision-pack/decision-groups.md#dec-07) gom các câu cùng chủ đề và chỉ tới **Buổi 4** trong [chương trình họp](gia-phat/review/decision-pack/meeting-agenda.md).
4. Sau khi có quyết định ký kèm nguồn, BA mới được sửa tài liệu E6 bằng quy trình phân tích tác động (CR).

Bài học: một câu hỏi xuất hiện ở **nhiều nơi** (sổ của epic, sổ hợp nhất, nhóm DEC, buổi họp), nhưng **nguồn gốc** luôn là file `review/questions.md` của epic; các sổ khác chỉ dẫn link về đó.

### Ví dụ 3: giải mã một câu dày mã trong OVERVIEW

Câu gốc (mốc E8):

> 14/14 CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04 và AIO-Q01–06 không đóng.

Đọc thành lời:

- `CG` = contract gap, khoảng trống hợp đồng giao tiếp của E6 (sổ: [contract-gap-register.md](chon-mon-order/review/contract-gap-register.md)). "14/14 OPEN" = cả 14 khoảng trống đều chưa đóng.
- `E6-EVID-001/002` = hai bằng chứng xác nhận đầu vào đã thu được cho E6 (ví dụ có xác nhận danh sách người ăn do người quản lý cung cấp), vẫn đang được dùng.
- `O-02` (một món một hay nhiều cỡ định lượng), `O-03` (gợi ý cá nhân có xét bệnh lý không), `O-04` (đội phát triển, hạ tầng, nhà cung cấp AI): các điểm mở cấp sản phẩm trong BRD, chưa trả lời.
- `AIO-Q01–06` = 6 câu hỏi của Agent Nội bộ (E5), chưa đóng.

Cách làm chung: tra tiền tố trong **mục 5** bên dưới, rồi tìm mã bằng chức năng tìm kiếm của trình soạn thảo (ví dụ tìm `CG01` trong `docs/`).

### Ví dụ 4: đọc một dòng ma trận lỗi

Từ [giao-nhan-doanh-thu/srs/error-matrix.md](giao-nhan-doanh-thu/srs/error-matrix.md):

| ERR-E7-409-01 | 409 | Version/nguồn đã thay | Dữ liệu đã đổi. Tải lại và đối chiếu. | e7.stale_version | High | Không tự ghi đè |

- `ERR` + `E7` (phạm vi) + `409` (mã HTTP: xung đột) + `01` (số thứ tự).
- Cột *Trigger*: khi nào lỗi xảy ra; *UI message*: câu hiển thị cho người dùng; *Localization key*: khóa để dịch; *Severity*: mức nghiêm trọng; *Next action*: hệ thống / người dùng làm gì tiếp.

---

## 5. Cách giải mã mã định danh

### 5.1 Ngữ pháp chung

Hầu hết mã theo dạng `LOẠI-PHÂNHỆ[-NHÓM]-SỐ`:

| Mẫu | Ví dụ | Đọc là |
| :--- | :--- | :--- |
| `FR-[MODULE]-[FEATURE]-[SEQ]` | `FR-MENU-RCP-007` | Yêu cầu chức năng, phân hệ MENU, nhóm công thức (recipe), số 7 |
| `BR-[NHÓM]-[SEQ]` | `BR-PRC-005` | Quy tắc nghiệp vụ nhóm giá, số 5 |
| `ERR-[PHẠM VI]-[HTTP]-[SEQ]` | `ERR-COST-422-01` | Lỗi phân hệ COST, HTTP 422, số 1 |
| `UC-[TIỀN TỐ]-[SEQ]` | `UC-ORD-016` | Use case số 16 của E6 |
| `US-[TIỀN TỐ]-[SEQ]` | `US-COST-004` | User story số 4 của Cost |
| `AC-[TIỀN TỐ]-[STORY]-[SEQ]` | `AC-COST-004-02` | Tiêu chí thứ 2 của story 004 |
| `TC-[TIỀN TỐ]-[STORY]-[SEQ]` | `TC-COST-004-02` | Test case khớp với AC cùng số |
| `API-[TIỀN TỐ]-[SEQ]` | `API-COST-006` | Endpoint đề xuất số 6 |
| `[EPIC]-Q[SEQ]` | `E9-Q14`, `ORD-Q01` | Câu hỏi mở của epic |

Khoảng mã viết bằng gạch nối hoặc mũi tên: `FEAT-049→053` hay `E7-Q01–08` nghĩa là **từ … đến …** (gồm cả hai đầu). Dấu `/` gộp nhiều mã cùng tiền tố: `CG01/08/05/06` = `CG01`, `CG08`, `CG05`, `CG06`.

### 5.2 Bảng tiền tố mã

**Tầng sản phẩm**

| Tiền tố | Nghĩa | Nơi định nghĩa |
| :--- | :--- | :--- |
| `A-xx` | Tác nhân (actor), A-01 khách vãng lai … A-12 Agent Nội bộ | Kế hoạch tổng mục 2.2, URD |
| `PER-xx` | Persona (chân dung người dùng) trong PRD, gắn với một hay nhiều `A-xx` | PRD mục 2 |
| `D-xx` | Quyết định đã chốt (D-01 → D-21) | Kế hoạch tổng mục 1 |
| `Q-xx` | Câu hỏi đầu dự án gửi chủ đầu tư | Kế hoạch tổng mục 9 |
| `O-xx` | Điểm mở cấp sản phẩm (O-01 → O-06) | BRD mục 11 |
| `BO-xx` | Mục tiêu kinh doanh đo được (Business Objective), ví dụ BO-01 cost ≤ 52% | BRD mục 3 |
| `BN-xx` | Nhu cầu nghiệp vụ (Business Need) | BRD mục 6 |
| `UN-xx` | Nhu cầu người dùng (User Need) | URD |
| `AS-xx` | Giả định (Assumption) | BRD mục 10 |
| `DP-xx` | Phụ thuộc bên ngoài (Dependency) | BRD mục 10 |
| `C-xx` | Hạng mục chi phí | BRD mục 8 |
| `R-xx` | Rủi ro (R-01, R-04…); **khác** `R1`→`R13` là đợt phát hành | Kế hoạch tổng mục 8, BRD mục 9 |
| `O1`→`O5`, `KRx.x` | Objective và Key Result trong OKR của PRD | PRD mục 1.2 |
| `FEAT-xxx` | Tính năng (78 tính năng, FEAT-001 → FEAT-088, có quãng trống) | PRD |
| `MENU-01`, `COST-01`, `AIN-01`… | Mã tính năng gốc trong danh mục của kế hoạch tổng | Kế hoạch tổng mục 4, 5 |
| `E1`→`E13` | Epic | Kế hoạch tổng mục 6.3 |
| `R1`→`R13` | Đợt phát hành (release), một release ứng với một epic | Roadmap |
| `G-Now`, `G-Next` | Cổng chuyển đợt: điều kiện để mở đợt kế tiếp | Roadmap |
| `DL-xx` | Việc chuẩn bị dữ liệu của Gia Phát (không phải phần mềm) | Roadmap |
| `H-x` | Câu hỏi cần người soạn docx trả lời trong bảng quy tắc | quy-tac-thuc-don.md |

**Tầng epic: yêu cầu và thiết kế**

| Tiền tố | Nghĩa |
| :--- | :--- |
| `FR-…` | Functional Requirement, yêu cầu chức năng |
| `NFR-…` | Non-Functional Requirement, yêu cầu phi chức năng (hiệu năng, độ chính xác, bảo mật) |
| `BR-…` | Business Rule, quy tắc nghiệp vụ. Các nhóm hay gặp: `BR-MENU`, `BR-MNU` (thực đơn), `BR-CAT` (danh mục), `BR-PRC` (giá), `BR-CALC` (tính toán), `BR-EST` (dự toán), `BR-COST`, `BR-SEC` (bảo mật), `BR-AUD` (nhật ký), `BR-AIN`, `BR-AIO`, `BR-PUR`, `BR-CRM`, `BR-FBR`, `BR-EXP` |
| `ERR-…` | Mã lỗi. `ERR-AUTH` (xác thực / phân quyền), `ERR-SYS` (lỗi chung) dùng cho mọi epic |
| `UC-…` | Use case |
| `US-…` | User story |
| `AC-…` | Acceptance Criteria, tiêu chí nghiệm thu |
| `API-…` | Endpoint HTTP đề xuất |
| `PORT-…` | Cổng giao tiếp nội bộ giữa các phân hệ (không phải HTTP công khai) |
| `SCR-…`, `UI-…` | Màn hình (screen) |
| `SYN-…`, `MOCK-…`, `REAL-…` | Dữ liệu giả lập / dữ liệu minh họa / dữ liệu thật (thường "chưa nhận") |

**Tầng epic: kiểm thử**

| Tiền tố | Nghĩa |
| :--- | :--- |
| `TC-…` | Test case |
| `TC-…-SYS-…`, `TC-…-S…` | Ca kiểm thử mức hệ thống |
| `TC-RULE-MENU-xxx-PASS/FAIL` | Ca kiểm một quy tắc thực đơn: một ca đạt và một ca vi phạm |
| `CL-F`, `CL-B`, `CL-S` | Mục checklist: chức năng theo story (F), dữ liệu biên (B), phân quyền và bảo mật (S) |
| `TC-MENU-B-xx`, `TC-MENU-S-xx` | Test case sinh từ checklist biên / bảo mật |

**Tầng epic và gói quyết định: câu hỏi, khoảng trống, quyết định**

| Tiền tố | Nghĩa |
| :--- | :--- |
| `E1-Q`, `E2-Q` … `E13-Q` | Câu hỏi mở của từng epic |
| `ORD-Q`, `AIO-Q`, `NUTR-Q` | Câu hỏi mở theo phân hệ (E6, E5, E4) |
| `N-xx` | Câu hỏi mở trong SRS nền tảng |
| `CK-Q` | Câu hỏi về **chiết khấu** (Cost) |
| `DATA-COST-Q` | Câu hỏi về dữ liệu Cost (bộ 10 món / 10 ngày) |
| `FLOW-COST-Q` | Câu hỏi phát sinh khi vẽ user flow Cost |
| `QA-COST-Q` | Câu hỏi của QA về Cost |
| `E6-CG-xx` / `CGxx` | Contract Gap: khoảng trống hợp đồng giao tiếp E6 |
| `E6-EVID-xxx` | Bằng chứng đầu vào đã thu cho E6 |
| `DR-xx` | Mục rà quyết định (Decision Review) của E6 |
| `GAP-…` | Phát hiện trong rà khoảng trống (`gap-analysis.md`) |
| `CR-…` | Change Request, phiếu yêu cầu thay đổi, ví dụ `CR-COST-2026-001` |
| `DEC-xx` | Nhóm quyết định trong gói quyết định (gom các câu cùng chủ đề và cùng người ký) |
| `XC-xx` | Phát hiện rà nhất quán **liên epic** (cross-epic consistency) |
| `BA-Qxx` | Câu BA phải tự xác minh trước khi hỏi (ví dụ ai có thẩm quyền ký) |
| `P-MVP`, `P-NOW`, `P-NEXT`, `P-LATER` | Mức quan trọng của câu hỏi: chặn MVP / việc Now / đợt Next / đợt Later |

**Vai trò hệ thống (tên quyền / nhóm người dùng viết hoa)**

| Mã | Vai trò |
| :--- | :--- |
| `GIAM_DOC` | Giám đốc |
| `DINH_DUONG_VIEN` | Dinh dưỡng viên (DDV) |
| `QL_CO_SO` | Quản lý cơ sở bếp |
| `BEP_TRUONG` | Bếp trưởng |
| `KT_MUA_HANG` | Kế toán mua hàng |
| `KT_DOANH_THU` | Kế toán doanh thu |
| `cost.price.write`, `menu.*`… | Tên quyền chi tiết dạng `phân_hệ.đối_tượng.hành_động` |

---

## 6. Bảng thuật ngữ

### 6.1 Loại tài liệu BA

| Thuật ngữ | Giải thích |
| :--- | :--- |
| **BA** (Business Analyst) | Người phân tích nghiệp vụ; tác giả của các tài liệu trong kho |
| **BRD** (Business Requirements Document) | Tài liệu yêu cầu nghiệp vụ: vì sao làm, mục tiêu, phạm vi, ROI, rủi ro |
| **URD** (User Requirements Document) | Tài liệu yêu cầu người dùng: ai dùng, họ cần gì, hành trình |
| **PRD** (Product Requirements Document) | Tài liệu yêu cầu sản phẩm: tầm nhìn, persona, danh sách tính năng |
| **Roadmap** | Lộ trình: thứ tự và điều kiện phát hành các đợt |
| **Epic** | Một khối tính năng lớn, ở đây mỗi epic là một thư mục trong `docs/` |
| **Epic spec** | Đặc tả một epic: tính năng, ưu tiên, kế hoạch release |
| **SRS** (Software Requirements Specification) | Đặc tả yêu cầu phần mềm chi tiết: FR, NFR, BR, ma trận lỗi |
| **FR** (Functional Requirement) | Yêu cầu chức năng: hệ thống phải làm gì |
| **NFR** (Non-Functional Requirement) | Yêu cầu phi chức năng: nhanh cỡ nào, chính xác cỡ nào, an toàn thế nào |
| **BR** (Business Rule) | Quy tắc nghiệp vụ, ví dụ "không 2 món chính cùng chiên" |
| **Use case (UC)** | Kịch bản tương tác giữa tác nhân và hệ thống để đạt một mục tiêu |
| **Chuẩn Cockburn** | Khuôn viết use case của Alistair Cockburn: tác nhân, tiền điều kiện, kích hoạt, luồng chính, nhánh, hậu điều kiện, đảm bảo tối thiểu |
| **Sea level** | Cấp độ use case: một mục tiêu người dùng hoàn thành trong một lần thao tác (khác cấp "tóm tắt" và cấp "chi tiết con") |
| **Tác nhân (actor)** | Người hoặc hệ thống tương tác với phần mềm |
| **Persona** | Chân dung đại diện một nhóm người dùng |
| **Tiền điều kiện / Hậu điều kiện** | Điều phải đúng trước khi bắt đầu / sau khi kết thúc thành công |
| **Kích hoạt (trigger)** | Sự kiện bắt đầu use case |
| **Đảm bảo tối thiểu** | Điều hệ thống vẫn giữ được kể cả khi thất bại (ví dụ không ghi dở dang) |
| **User story (US)** | Câu mô tả nhu cầu: "Là một …, tôi muốn … để …" |
| **Story point** | Điểm ước lượng độ lớn tương đối của story (1, 2, 3, 5…) |
| **Backlog** | Danh sách story chờ làm |
| **AC** (Acceptance Criteria) | Tiêu chí nghiệm thu: điều kiện để story được coi là xong |
| **Gherkin / Given-When-Then** | Cú pháp viết AC: bối cảnh / hành động / kết quả |
| **User flow** | Luồng người dùng đi qua các màn hình |
| **Wireframe** | Bản phác giao diện. **ASCII**: vẽ bằng ký tự; **HTML**: bấm được nhưng dữ liệu giả |
| **Preview** | Trang HTML gom toàn bộ tài liệu một epic để xem nhanh |
| **ERD** (Entity Relationship Diagram) | Sơ đồ quan hệ dữ liệu |
| **DBML** | Ngôn ngữ mô tả schema cơ sở dữ liệu (dùng với dbdiagram.io, xuất được SQL) |
| **Data dictionary** | Từ điển dữ liệu: bảng, trường, kiểu, ràng buộc |
| **Data mapping** | Ánh xạ trường giữa API, cơ sở dữ liệu và màn hình |
| **State diagram** | Sơ đồ trạng thái của một đối tượng |
| **Sequence / Activity / Swimlane** | Sơ đồ tuần tự / hoạt động / hoạt động chia làn theo vai trò |
| **Mermaid** | Cú pháp vẽ sơ đồ bằng chữ trong file `.md`; đã render sẵn ra `srs/diagrams/*.svg` |
| **Ma trận lỗi (error matrix)** | Bảng mã lỗi, HTTP, thông báo, mức nghiêm trọng, hành động tiếp |
| **Checklist** | Dàn ý các nhóm kịch bản cần test |
| **Test case (TC)** | Kịch bản test chi tiết: tiền điều kiện, bước, kết quả mong đợi |
| **RTM** (Requirements Traceability Matrix) | Ma trận truy vết: nối FR ↔ story ↔ AC ↔ test ↔ API |
| **Truy vết** | Việc ghi rõ mỗi mục bắt nguồn từ đâu và được kiểm ở đâu |
| **Gap analysis** | Rà khoảng trống: tài liệu còn thiếu luồng hoặc quyết định nào |
| **Handoff** | Gói bàn giao cho người review hoặc đội kế tiếp |
| **CR** (Change Request) | Yêu cầu thay đổi; phải phân tích tác động trước khi sửa tài liệu |
| **Decision pack / Sổ quyết định** | Gói gom mọi câu hỏi mở để stakeholder ký quyết định |
| **Decision register** | Sổ ghi câu hỏi, người quyết định, phương án, câu trả lời |
| **Meeting agenda** | Chương trình họp: câu hỏi nào bàn ở buổi nào, với ai |
| **Cross-epic consistency** | Rà nhất quán giữa các epic (cùng một khái niệm có bị định nghĩa khác nhau không) |
| **Frontmatter** | Khối `---` đầu file chứa `id`, `version`, `phase`, `author`, `last_updated`, `depends_on` |
| **Lịch sử sửa đổi** | Bảng phiên bản ở đầu mỗi tài liệu; dòng trên cùng là bản mới nhất |
| **Append-only** | Chỉ được thêm vào cuối, không sửa phần cũ. OVERVIEW viết kiểu này nên các mục phía trên là **lịch sử** |
| **Stakeholder** | Bên liên quan có quyền quyết định hoặc chịu ảnh hưởng |
| **Product Owner / Lead BA** | Người sở hữu sản phẩm / BA chính; trong PRD hiện "chưa chỉ định" |

### 6.2 Trạng thái và nhãn

| Nhãn | Giải thích |
| :--- | :--- |
| **Draft / Nháp** | Bản đang soạn, chưa duyệt. Gần như mọi file đều ở trạng thái này |
| **[ĐÃ CHỐT]** | Chủ đầu tư đã trả lời trực tiếp |
| **[ĐỀ XUẤT]** | Phương án BA đề nghị, có thể đổi |
| **[CHỜ Q-xx]** | Chưa quyết, đang chờ câu hỏi Q-xx |
| **[CẦN SỐ LIỆU] / [CẦN PHỎNG VẤN]** | Thiếu dữ liệu thật, cần Gia Phát cung cấp hoặc cần phỏng vấn người dùng |
| **CHỜ XÁC NHẬN / CHỜ TRẢ LỜI / OPEN** | Câu hỏi chưa có câu trả lời. Cột "Trả lời" để trống có chủ ý |
| **PARTIALLY_CONFIRMED** | Đã xác nhận một phần, phần còn lại vẫn mở (ví dụ O-01 về VAT) |
| **P0 / P1 / P2** | Ưu tiên: bắt buộc cho bản đầu / nên có / để sau |
| **Cỡ S / M / L / XL** | So sánh độ lớn tương đối giữa các đợt, **không phải** thời gian |
| **Now / Next / Later** | Ba đợt lớn: MVP nội bộ (E1 → E5) / mở cho khách (E6 → E9) / vận hành đầy đủ (E10 → E13) |
| **MVP** | Minimum Viable Product, bản đầu dùng được: 23 tính năng, R1 → R5 |
| **Gate (cổng)** | Điều kiện phải đạt trước khi làm tiếp. "BLOCKED vì gate O-03" = chờ O-03 được trả lời |
| **Gate-only** | Tính năng chỉ có mô tả cổng chặn, **chưa có thiết kế** (FEAT-046, 047, 063 chờ O-03); không tính vào độ phủ |
| **Thiết kế nháp có điều kiện** | Đã có thiết kế, nhưng đúng chỉ khi các câu hỏi liên quan được trả lời như giả định |
| **Độ phủ thiết kế tài liệu nháp** | Số tính năng đã có bộ tài liệu nháp / 78. Ví dụ 75/78 ≈ 96,2%. **Không** phải tiến độ phần mềm |
| **NOT RUN** | Ca test đã viết nhưng chưa chạy (vì chưa có backend) |
| **BLOCKED** | Ca test hoặc chức năng không chạy được vì thiếu đầu vào / quyết định |
| **Actual / Evidence / Defect** | Kết quả thực tế / bằng chứng / lỗi tìm thấy: hiện đều trống |
| **Overlap** | Các ca test trùng mục tiêu với nhau, nên **không cộng** thành số mục tiêu độc lập |
| **Freeze (đóng băng)** | Chốt hợp đồng API / schema để code. Hiện chưa freeze gì |
| **Producer / consumer** | Epic cung cấp dữ liệu / epic dùng dữ liệu. "Không đặc tả tiếp producer đang chờ" = không tự viết thay phần của epic khác |
| **Quy tắc cứng / mềm** | Cứng: vi phạm thì chặn công bố. Mềm (nặng / vừa / nhẹ): trừ 3 / 2 / 1 điểm trên thang 100 điểm của thực đơn tuần |
| **CHAN / CANH_BAO** | Hai chế độ kiểm cost (tham số `COST_CHE_DO_KIEM`): `CHAN` chặn gửi duyệt khi cost vượt ngưỡng; `CANH_BAO` chỉ cảnh báo. Mặc định `CANH_BAO`, đổi sang `CHAN` cần Giám đốc duyệt |
| **VALID** | Trạng thái bản nháp của agent đạt mọi kiểm tra. Không được trả VALID khi vượt cost |
| **ACTIVE** | Trạng thái công thức đang hiệu lực |
| **Đ / S / B** | Cách duyệt bảng quy tắc: Đồng ý / Sửa / Bỏ |
| **Mục lịch sử** | Trong OVERVIEW và PRD, các mục cũ giữ nguyên byte; chỉ **mục "Mốc hiện hành" cuối cùng** phản ánh hiện tại |

### 6.3 Kỹ thuật: API, dữ liệu, kiến trúc

| Thuật ngữ | Giải thích |
| :--- | :--- |
| **API / endpoint** | Giao diện lập trình; endpoint là một địa chỉ cụ thể, ví dụ `POST /v1/cost/price-batches` |
| **HTTP 200/201/202** | Thành công / đã tạo mới / đã nhận, đang xử lý nền |
| **HTTP 400/401/403/404** | Yêu cầu sai / chưa đăng nhập / không đủ quyền / không tìm thấy (hoặc ngoài phạm vi được xem) |
| **HTTP 409** | Xung đột: dữ liệu đã bị người khác đổi, hoặc trùng |
| **HTTP 413/415/422** | Tệp quá lớn / định dạng không hỗ trợ / dữ liệu sai quy tắc nghiệp vụ |
| **HTTP 429/500/503** | Vượt hạn mức gọi / lỗi máy chủ / dịch vụ chưa sẵn sàng |
| **Endpoint catalog** | Danh sách endpoint dạng JSON để máy đọc |
| **Port (control port)** | Điểm giao tiếp nội bộ giữa hai phân hệ, không mở ra ngoài |
| **Contract (hợp đồng giao tiếp)** | Thỏa thuận cố định về định dạng dữ liệu trao đổi giữa hai bên |
| **DTO** | Data Transfer Object, khuôn dữ liệu của request/response (ví dụ `PriceBatchInput`) |
| **Adapter** | Lớp chuyển đổi dữ liệu giữa hai phân hệ, kiểm lại quyền và tham chiếu |
| **Delta** | Phần đề xuất **thêm vào** schema chung, chưa gộp (merge) |
| **Schema / 65 bảng** | Cấu trúc cơ sở dữ liệu chung hiện có 65 bảng, giữ nguyên qua các đợt |
| **Migration** | Script tạo / sửa bảng thật trong cơ sở dữ liệu. Chưa có |
| **PK / FK** | Khóa chính / khóa ngoại |
| **Enum** | Tập giá trị cố định của một trường (ví dụ trạng thái `DRAFT`, `CONFIRMED`) |
| **Snapshot (bản chụp)** | Bản sao dữ liệu tại một thời điểm (ví dụ giá lúc duyệt), không bị đổi khi dữ liệu gốc thay đổi |
| **Version / revision** | Số phiên bản của bản ghi; dùng để phát hiện sửa đè (lỗi 409) |
| **Hiệu lực (effective date)** | Ngày bắt đầu áp dụng của giá, công thức, hợp đồng |
| **Audit / nhật ký** | Bản ghi ai làm gì, lúc nào; bắt buộc cho mọi thao tác sửa số liệu |
| **Atomic / nguyên tử / giao dịch (transaction)** | Cả lô thành công hoặc không có gì được ghi |
| **Commit / rollback** | Xác nhận ghi / hủy toàn bộ thay đổi trong giao dịch |
| **Idempotency / idempotency key** | Gửi lại cùng một lệnh (cùng khóa) không tạo bản ghi thứ hai; dùng khi mất phản hồi mạng |
| **Mất phản hồi** | Đã gửi lệnh ghi nhưng không nhận được trả lời: "chưa biết đã lưu hay chưa", phải đối soát trước khi gửi lại |
| **TTL** | Thời gian sống của một khóa / bản ghi tạm |
| **Outbox** | Kỹ thuật lưu sự kiện cùng giao dịch rồi phát sau, để không mất sự kiện |
| **Queue (hàng đợi)** | Xếp việc chậm (gọi AI, gửi thông báo) chạy nền để không làm sập API |
| **Stateless** | Máy chủ API không giữ trạng thái phiên, chạy được nhiều bản song song |
| **Redis / cache** | Bộ nhớ đệm nhanh cho thực đơn, phiên đăng nhập |
| **CCU** (Concurrent Users) | Số người dùng đồng thời; mục tiêu 1.000 |
| **p95** | 95% lượt gọi nhanh hơn mức này. Mục tiêu: đọc ≤ 300 ms, ghi ≤ 800 ms |
| **RBAC** | Phân quyền theo vai trò |
| **MFA** | Xác thực nhiều lớp |
| **Scope (phạm vi)** | Dữ liệu một người được phép thấy, ví dụ quản lý cơ sở A không đọc dữ liệu cơ sở B |
| **Identity / binding** | Cách xác định duy nhất một người ăn và gắn họ với công ty / mã QR |
| **Service account (svc-…)** | Tài khoản kỹ thuật cho agent hay tác vụ tự động |
| **Projection / redaction** | Chỉ trả ra các trường được phép / che bớt dữ liệu nhạy cảm (ví dụ cost không lộ ra cổng khách) |
| **Provenance** | Nguồn gốc của một con số (lấy từ đâu, phiên bản nào) |
| **Localization key** | Khóa văn bản để dịch thông báo, ví dụ `e7.stale_version` |
| **Hook** | Điểm móc để phân hệ khác chèn kiểm tra, ví dụ Cost đăng ký kiểm vào cổng gửi duyệt của MENU |
| **Engine** | Bộ tính toán (ví dụ engine cost) |
| **Decimal** | Kiểu số thập phân chính xác, dùng khi tính tiền để không sai số làm tròn |

### 6.4 Kiểm thử và kiểm tra tài liệu

| Thuật ngữ | Giải thích |
| :--- | :--- |
| **Fixture** | Bộ dữ liệu chuẩn bị sẵn để chạy test |
| **Synthetic (giả lập)** | Dữ liệu bịa có chủ đích, không phải số thật của Gia Phát |
| **Oracle** | Kết quả đúng dùng để so (ví dụ bảng tính tay của kế toán) |
| **Evidence** | Bằng chứng khi chạy test: ảnh, log, dữ liệu trước/sau |
| **Evidence protocol** | Quy ước ghi bằng chứng (mã lần chạy, môi trường, người chạy, hash dữ liệu…) |
| **UAT** | User Acceptance Testing, nghiệm thu bởi người dùng. Chưa làm |
| **Nghiệm thu** | Xác nhận chính thức đạt tiêu chí. Chưa đợt nào được nghiệm thu |
| **System case** | Ca test xuyên nhiều chức năng |
| **Invariant case** | Ca kiểm một điều luôn phải đúng (bất biến), ví dụ tổng suất không âm |
| **Mock / kiểm UI mock** | Kiểm wireframe với dữ liệu giả; **không** thay cho test sản phẩm |
| **Baseline** | Ảnh chụp trạng thái file trước một đợt viết, để kiểm không ai sửa nhầm file cũ |
| **SHA256 / hash** | "Dấu vân tay" của file; khác hash nghĩa là nội dung đã đổi |
| **Checker** | Script tự kiểm cấu trúc, liên kết, số đếm của tài liệu (`check-*.cjs`, `check-*.py`) |
| **Render** | Chuyển mã sơ đồ thành ảnh SVG / HTML |
| **Viewport 1440 / 390 / 360** | Độ rộng màn hình dùng khi chụp kiểm wireframe: máy tính / điện thoại |
| **Manifest / files-created.json** | Danh sách file tạo trong một đợt |
| **QA** | Người / hoạt động đảm bảo chất lượng |

### 6.5 Nghiệp vụ suất ăn Gia Phát

| Thuật ngữ | Giải thích |
| :--- | :--- |
| **Suất (suất ăn)** | Một phần ăn cho một người; đơn vị đặt, giao, nhận và tính tiền |
| **Loại suất** | Cấu hình do dinh dưỡng viên tạo: ngưỡng giá, số món chính, số món phụ (D-20) |
| **Định mức** | Giới hạn công ty đặt cho người ăn (giá suất, số món); chọn vượt định mức bị chặn (D-21) |
| **Món chính / món phụ / rau / canh** | Vai trò món trong suất. Mỗi ngày 3 món chính, người ăn chọn 1 (D-04) |
| **Món mặc định** | Món gán cho người không chọn trước hạn chốt (D-14) |
| **Healthy** | Cờ món lành mạnh (ví dụ luộc); phương pháp nào được tính còn chờ `H-1` |
| **Thực đơn kỳ / thực đơn tuần** | Thực đơn thứ Hai → thứ Bảy theo loại suất hoặc theo khách |
| **Công thức (recipe)** | Danh sách nguyên liệu và định lượng của một món, có phiên bản và người duyệt khác người tạo |
| **Định lượng sống** | Khối lượng nguyên liệu trước khi chế biến (ví dụ thịt 85–90 g); dinh dưỡng được tính "ước tính từ định lượng sống" |
| **Hao hụt / hệ số quy đổi** | Phần mất khi sơ chế / tỷ lệ đổi đơn vị mua sang đơn vị dùng (kg → gram, bìa, quả) |
| **Nguyên liệu (NL)** | Danh mục chủ các nguyên liệu, có đơn vị, mùa vụ, loại bảo quản |
| **Lô** | Nhóm hàng cùng đợt nhập; chỉ quản lý lô cho hàng đông lạnh và khô |
| **Cost** | Chi phí nguyên liệu. Theo quy tắc kế toán đã xác nhận: **gồm VAT phải trả nhà cung cấp** |
| **Cost món / cost ngày / cost %** | Chi phí một món / một ngày phục vụ / tỷ lệ cost trên doanh thu suất ăn |
| **Ngưỡng 52%** | Cost dự toán không vượt 52% doanh thu suất ăn (BO-01) |
| **BO-02 (3 điểm %)** | Chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm theo ngày và cơ sở |
| **NFR-COST-002** | Chuẩn chính xác: so với bảng tính tay của kế toán trên 10 món / 10 ngày, lệch không quá 1 đồng (cost món) và 0,01 điểm % (cost %) |
| **Điểm phần trăm** | Chênh lệch tuyệt đối giữa hai tỷ lệ: 50% → 53% là tăng 3 điểm phần trăm |
| **Giá nhập / giá tham chiếu** | Giá mua nguyên liệu theo NCC và ngày; giá tham chiếu là giá được chọn để tính cost |
| **Dự toán** | Bảng ước tính chi phí trước khi nấu, có phiên bản |
| **Khoản khoán** | Khoản chi phí ước tính cố định (không tính từ công thức), ví dụ gia vị |
| **Món đặc thù** | Món cần bảng tính riêng được duyệt (không tính theo công thức chuẩn) |
| **NCC** | Nhà cung cấp |
| **VAT** | Thuế giá trị gia tăng. Giá 40.000 đ/suất đã gồm VAT (D-15). Cờ "không yêu cầu hóa đơn" là cờ riêng, **không** có nghĩa VAT 0% |
| **CK (chiết khấu)** | Chiết khấu cho khách theo % hoặc tiền/suất, ghi **khoản riêng theo đơn**, không làm giảm số phải trả NCC và không tự trừ tiền khách |
| **Cơ sở** | Một bếp của Gia Phát (hiện có 2 cơ sở) |
| **Ca** | Ca phục vụ (ví dụ ca trưa) / ca làm việc của nhân viên |
| **Điểm phục vụ** | Nơi giao suất của một khách hàng |
| **Hạn chốt** | Mốc giờ khóa lựa chọn món / số suất trước ngày phục vụ |
| **Order** | Đơn đặt suất của công ty khách |
| **Người đặt tổng / người nhận** | Đại diện công ty chốt tổng số suất / ký nhận khi giao |
| **Người ăn có tài khoản / qua QR** | Nhân viên công ty khách tự chọn món bằng tài khoản hoặc quét mã QR công ty |
| **Khách vãng lai** | Người xem website, chưa là khách hàng |
| **DDV** | Dinh dưỡng viên (kiêm CSKH): soạn thực đơn, công thức; hiện là "điểm nghẽn đơn" |
| **CSKH** | Chăm sóc khách hàng |
| **Kế hoạch sản xuất** | Số suất theo từng món cho từng cơ sở / ngày / ca, sinh ra sau hạn chốt |
| **Phiếu giao nhận** | Chứng từ ghi số suất giao, số khách nhận |
| **Đối soát** | So khớp số liệu giao / nhận / tính tiền với khách theo kỳ, kết thúc bằng **biên bản đối soát** |
| **Kỳ khóa** | Kỳ kế toán đã chốt; không sửa đè, điều chỉnh bằng bút toán riêng có người duyệt |
| **MISA** | Phần mềm kế toán chính thức của Gia Phát; hệ thống mới xuất file để nhập vào MISA |
| **Zalo OA / ZNS** | Tài khoản doanh nghiệp Zalo / tin nhắn thông báo Zalo; kênh khách đang dùng |
| **Lead** | Khách hàng tiềm năng (ví dụ từ form website) |
| **CRM / hồ sơ 360°** | Quản lý quan hệ khách hàng / toàn bộ lịch sử một khách ở một chỗ |
| **Phễu bán hàng** | Các giai đoạn từ lead đến hợp đồng |
| **Báo giá** | Có phiên bản; bản gửi khách không chứa cost hay biên lợi nhuận |
| **Hợp đồng nguyên tắc / phụ lục giá** | Hợp đồng khung năm / phụ lục quy định giá theo loại suất và khoảng hiệu lực |
| **Nguy cơ rời** | Tín hiệu khách sắp ngừng dùng dịch vụ |
| **QC / mẫu lưu** | Kiểm soát chất lượng / mẫu thức ăn lưu lại mỗi bữa (mục tiêu 100% bữa có mẫu lưu) |
| **Tồn / tồn tối thiểu** | Lượng hàng trong kho / mức tối thiểu trước khi phải đặt thêm |
| **Phân bổ chi phí** | Chia chi phí chung (nhân công, điện, gas…) cho từng khách để tính lợi nhuận; phương pháp còn chờ Giám đốc duyệt |
| **Chấm công** | Ghi giờ làm theo người / cơ sở / ca, chỉ để tính chi phí nhân công, không tính lương |
| **Biên lợi nhuận (margin)** | Phần lợi nhuận trên doanh thu; thông tin nội bộ, không lộ ra khách |
| **4 chỉ số dinh dưỡng** | Năng lượng (kcal), đạm, béo, bột đường; nguồn "Bảng thành phần thực phẩm Việt Nam" của Viện Dinh dưỡng (D-17) |
| **Dị ứng** | Thông tin chất gây dị ứng của món, luôn được kiểm lại khi thay món |
| **Dữ liệu sức khỏe** | Bệnh lý, chỉ số cơ thể. Dự án **không thu** loại dữ liệu này cho tới khi O-03 được trả lời |
| **Tiệc cỗ** | Đơn tiệc tính theo mâm, có đặt cọc; tách loại đơn khỏi suất ăn |
| **C-MAP/CRM (bản HTML cũ)** | Bản thiết kế 04/11/2026 trước dự án này; được phân tích ở file gốc |

### 6.6 AI agent

| Thuật ngữ | Giải thích |
| :--- | :--- |
| **AI agent** | Chương trình dùng mô hình ngôn ngữ, có thể gọi công cụ để làm việc thay người |
| **Agent Nội bộ (AIO)** | Hỗ trợ dinh dưỡng viên dựng thực đơn (E5), sau mở rộng sang mua hàng, CRM, hỏi đáp số liệu (E12) |
| **Agent Dinh dưỡng viên (AIN)** | Phía khách: tạo thực đơn tập thể, gợi ý (E9) |
| **Mô hình ngôn ngữ (LLM) / model** | Phần "hiểu và viết chữ" của agent. Nguyên tắc: **AI không tự tính số**; cost, định lượng, kiểm quy tắc do code xác định thực hiện |
| **Tool (công cụ)** | Chức năng có sẵn mà agent được phép gọi (ví dụ bộ kiểm MENU / COST) |
| **Tool allowlist** | Danh sách công cụ agent được phép dùng |
| **System prompt** | Chỉ dẫn nền cho mô hình. Dự án chưa viết system prompt thật |
| **Provider** | Nhà cung cấp mô hình AI; chưa chọn (chờ O-04) |
| **Token / quota / cap** | Đơn vị tính phí AI / hạn mức sử dụng / trần chi phí |
| **Run (lượt chạy)** | Một lần agent xử lý yêu cầu, có nhật ký |
| **Nháp (draft) của agent** | Kết quả agent đề xuất, luôn chờ người thật duyệt; agent không tự ghi nghiệp vụ |
| **Guest** | Người dùng chưa đăng nhập (khách vãng lai) dùng agent, bị giới hạn |
| **Consent** | Sự đồng ý của người dùng cho việc dùng dữ liệu |

### 6.7 Công cụ sinh tài liệu

Kế hoạch tổng nhắc tới các **lệnh** như `/brainstorm`, `/brd`, `/prd`, `/srs`, `/usecase`, `/userstory`, `/ac`, `/test-cases`, `/gap`, `/preview`, `/cr`, `/update-overview`, `/dashboard`. Đây là các bước trong bộ khung soạn tài liệu BA (gọi là **ba-kit**), mỗi lệnh sinh ra một loại file ở mục 2.4. Người đọc không cần chạy chúng; chỉ cần biết file nào do bước nào sinh ra để hiểu thứ tự.

---

## 7. Những bẫy thường gặp khi đọc

1. **Nhầm độ phủ tài liệu với tiến độ phần mềm.** "75/78 ≈ 96,2%" chỉ là số tính năng có tài liệu nháp. Phần mềm: 0%.
2. **Đọc mục đầu của OVERVIEW và tưởng là hiện tại.** OVERVIEW viết nối dài; câu như "không mở E7–E13" ở phía trên đã bị các mốc sau thay thế. Luôn đọc **mục cuối**.
3. **Cộng số ca test giữa các bộ.** Ca chức năng, ca hệ thống và ca R-acceptance có overlap; tài liệu nói rõ "không cộng thành mục tiêu độc lập".
4. **Coi phương án khuyến nghị là quyết định.** Trong sổ quyết định, cột phương án là **trích nguồn, chưa chọn**; cột Trả lời trống nghĩa là chưa ai trả lời.
5. **Nhầm `R-01` (rủi ro) với `R1` (đợt phát hành)**, hay `O-01` (điểm mở) với `O1` (objective trong OKR).
6. **Tin dữ liệu trong wireframe và fixture.** Chúng là giả lập để minh họa, không phải số của Gia Phát.
7. **Bỏ qua cột Gate.** Một FR, story hay test có gate nghĩa là phần đó **chưa đủ căn cứ** để triển khai.

---

## 8. Tra cứu nhanh

- Tìm một mã bất kỳ: tìm kiếm toàn thư mục `docs/` theo đúng chuỗi mã (ví dụ `FR-COST-PRC-004`). Nơi xuất hiện trong bảng có cột "Mã" đầu tiên thường là nơi định nghĩa.
- Định nghĩa câu hỏi mở: file `review/questions.md` của epic tương ứng, hoặc [sổ quyết định](gia-phat/review/decision-pack/decision-register.md).
- Định nghĩa quy tắc thực đơn: [quy-tac-thuc-don.md](gia-phat/brainstorms/quy-tac-thuc-don.md).
- Định nghĩa quy tắc Cost và kế toán: [cost/srs/spec.md](cost/srs/spec.md), [cost/accounting/business-rules.md](cost/accounting/business-rules.md).
- Định nghĩa dữ liệu chung: [nen-tang/srs/erd.md](nen-tang/srs/erd.md), [schema.dbml](nen-tang/srs/schema.dbml).
