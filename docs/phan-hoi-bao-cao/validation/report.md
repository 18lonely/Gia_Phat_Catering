---
id: DOC-E12-VALIDATION-REPORT
title: Báo cáo kiểm gói BA nháp E12
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [e12, validation, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Báo cáo kiểm gói BA nháp E12

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở và kiểm riêng gói tài liệu E12 |

## Phạm vi và số liệu

Đúng FEAT-079–087: 9/9 feature có thiết kế nháp có điều kiện, 0 feature E12 chỉ gate; 7 P1 và 2 P2. 20 FR / 20 UC Cockburn / 20 story; 60 AC và 60 ca chức năng: 23 BLOCKED, 37 NOT RUN. Có thêm 12 ca hệ thống và 8 ca lỗi có overlap: 5 BLOCKED, 15 NOT RUN. Khung R12 có 3 dòng BLOCKED. Actual/Evidence của mọi ca sản phẩm để trống. Kiểm tài liệu/mock không thay kiểm sản phẩm.

20 HTTP endpoint đề xuất, 7 port logic chỉ đọc/kiểm thuần; 12 màn trong một HTML; 5 sơ đồ trạng thái và 2 sơ đồ luồng. 18 câu E12-Q01–18 có cột Trả lời trống. Mỗi FR có chuỗi FR → UC → story → AC → test → API → màn trong RTM. Bảng/trường mới chỉ đề xuất trong từ điển; schema chung giữ 65 bảng.

Độ phủ **thiết kế tài liệu nháp (65 + 9) / 78 = 74/78 ≈ 94,9 %**. Ba feature chỉ gate FEAT-046/047/063 ghi riêng, không cộng tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. E13/FEAT-088 chưa mở. R6, R7, R10, R11 và G-Next chưa có bằng chứng đạt; không nghiệm thu R12 bằng việc mở hồ sơ.

## Nguồn đã đọc trước khi viết

Đã đọc nguồn theo mục nghiệp vụ, mã yêu cầu, điểm mở và điểm nối liên quan E12. Tài liệu dài được rà theo mục; không coi bản nháp là contract hoặc chính sách đã duyệt. Danh sách máy đọc: [source-register.json](source-register.json).

| Nguồn | Nội dung áp dụng |
| :--- | :--- |
| [OVERVIEW](../../OVERVIEW.md), mục cuối E11 | Nền hiện hành 65/78; giới hạn và câu nguồn giữ nguyên |
| [Tiến độ 12/11/2026](../../gia-phat/review/progress-status-2026-11-12.md) | Báo cáo được lập trước E11, còn ghi 60/78; không sửa báo cáo này, dùng mốc E11 mới hơn |
| [PRD](../../gia-phat/01-prd.md) | FEAT-079–087, BO/KR, PER-02…08, O-01–O-06 và ngoài phạm vi |
| [Roadmap](../../gia-phat/02-roadmap.md) | R12 cần R6/R7/R10/R11; 4 dashboard từ dữ liệu thật, tỷ lệ chọn từ lựa chọn thật; G-Next |
| [Handoff mẫu E11](../../mua-hang-san-xuat/review/handoff.md), [báo cáo mẫu E11](../../mua-hang-san-xuat/validation/report.md) | Đã liệt kê cây thư mục và script validation; chép cấu trúc artifact, không chạy generator lịch sử |
| [SRS E5](../../agent-noi-bo/srs/spec.md), [review E5](../../agent-noi-bo/review/questions.md) | Giao quyền, allowlist, nguồn, kiểm lại, AIO-Q01–06; review E5 chỉ có questions.md |
| [SRS E4](../../dinh-duong/srs/spec.md), [câu hỏi E4](../../dinh-duong/review/questions.md) | Bốn chỉ số/tổ hợp suất, nhãn ước tính, snapshot, NUTR-Q01–04; không tự đặt ngưỡng |
| [SRS E9](../../agent-dinh-duong-vien/srs/spec.md), [câu hỏi E9](../../agent-dinh-duong-vien/review/questions.md) | Biên AIN khác AIO, không chia quyền/cache, FEAT-063 gate O-03 |
| [SRS E2](../../thuc-don-dinh-luong/srs/spec.md) | Vai trò món, công thức, dị ứng, kiểm thuần FR-MENU-RUL-002, cổng MENU, O-02 |
| [SRS E3](../../cost/srs/spec.md), [quy tắc kế toán](../../cost/accounting/business-rules.md) | Cost % mục 3.3.2 khác dự toán mục 3.3.4; VAT/CK; NFR-COST-002; quyền cost |
| [SRS E6](../../chon-mon-order/srs/spec.md), [CG E6](../../chon-mon-order/review/contract-gap-register.md) | Lựa chọn thật, danh tính/scope, revision; CG/ORD/EVID chưa chốt |
| [SRS E7](../../giao-nhan-doanh-thu/srs/spec.md) | Số giao/nhận/tính tiền riêng; doanh thu có giá snapshot và evidence; Q-13 |
| [SRS E10](../../crm-ban-hang/srs/spec.md), [epic E10](../../crm-ban-hang/epic-spec.md), [câu hỏi E10](../../crm-ban-hang/review/questions.md) | FEAT-084 chỉ nối đọc theo người dùng, không sửa E10; nháp không là báo giá phát hành |
| [SRS E11](../../mua-hang-san-xuat/srs/spec.md), [câu hỏi E11](../../mua-hang-san-xuat/review/questions.md) | Nhu cầu gộp/mua ròng, đối chiếu thực mua, ngưỡng và phân bổ chưa chốt |
| [SRS nền](../../nen-tang/srs/spec.md), [ERD](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml) | Quyền/audit/giao quyền, xóa ≤ 72 giờ, không sức khỏe trong log; phân biệt bảng thực có và ERD khung |
| `.claude/ba-kit/rules/*.md` | Đã đọc 19 quy tắc mã, FR/BR/NFR, Cockburn, INVEST, GWT, metadata, phiên bản, API, dữ liệu, lỗi, state, RTM và wireframe |
| `.claude/ba-kit/_templates` | Đã liệt kê thư mục và đọc mẫu 07, 08, 19, 26, 27, 28, 29, 31, 37, 38, 42, 43 |
| Script mẫu chỉ đọc | render-e11.cjs và check-ui-e11.cjs làm mẫu; tạo bản riêng E12, không chạy script lịch sử |

## Bảng điểm nối E12 ↔ E2/E3/E4/E5/E6/E7/E9/E10/E11

| Gói | Điểm nối | Điều kiện / giới hạn E12 |
| :--- | :--- | :--- |
| E2 | Menu/recipe/vai trò/dị ứng và kiểm thuần | Đổi món/định lượng luôn kiểm lại; không ghi hoặc công bố; DL-01/O-02 giữ |
| E3 | Cost % ngày, dự toán, giá gồm VAT, quyền cost | Dùng đúng định nghĩa, không tự tạo mẫu số theo khách; CK/DATA-COST giữ |
| E4 | Snapshot dinh dưỡng suất và nguồn | FEAT-086 chờ ngưỡng; FEAT-087 chỉ giá trị suất, NUTR-Q01–04 giữ |
| E5 | Giao quyền, allowlist đọc, provenance | FEAT-082–085 chỉ nháp chờ người thật, không dùng apply; AIO-Q01–06 giữ |
| E6 | Lựa chọn thật và nguồn/identity/revision | Mẫu số Q04 chưa chọn; không dùng sản xuất, không suy đã ăn từ chọn; CG/ORD/EVID giữ |
| E7 | Doanh thu/đối soát có căn cứ | Không lấy số giao làm doanh thu hoặc bữa cá nhân đã ăn; Q-13/E7-Q giữ |
| E9 | Biên agent phía khách và gate cá nhân | Không chia quyền AIO; không mở FEAT-063, không gợi ý cá nhân; E9-Q giữ |
| E10 | Projection đọc CRM theo người dùng | Không CRUD/task/quote/gửi; E10-Q01–15 giữ; không sửa E10 |
| E11 | Nhu cầu gộp, so dự toán/thực mua | Không trừ tồn, đặt ngưỡng giá lệch hoặc phân bổ mới; E11-Q01–15 giữ |

[Dependencies](../review/dependencies.md) ghi nguồn và trách nhiệm chi tiết. FEAT-087 có thiết kế độc lập với O-03 vì không dùng eater_health_profiles, không thu/suy luận/lưu sức khỏe và không gợi ý; chỉ sự kiện bữa đã ăn cùng snapshot suất, đồng ý và quyền xóa. Bằng chứng đã ăn và retention còn chờ không tự mở hồ sơ FEAT-046/047. Mở rộng sang hai feature đó chỉ gate O-03, chưa có thiết kế nhánh mở.

## Skill và thứ tự áp dụng

Đã đọc `.agents/skills/<tên>/SKILL.md`, áp dụng lần lượt prd-epic → srs → usecase → userstory + ac → state + user-flow → api-design + api-map → wireframe-html → test-checklist + test-cases → preview → review. Dùng quy tắc tại `.claude/ba-kit`. Không gán story point, không lấy số NFR ví dụ của template thay nền hiện hành. Checklist chưa được BA/QA duyệt; ca được soạn ở mức nháp theo yêu cầu phiên. Không tìm/chạy scripts/render_diagrams.py; renderer E12 dùng thư viện cục bộ. Không tìm thấy AGENTS.md khi rà workspace; rg không có, dùng PowerShell/Node để đọc và tìm.

## Baseline và kiểm

Đã chụp [baseline.json](baseline.json) gồm SHA256 và kích thước của **945 file hiện có trong docs/** trước khi ghi tài liệu hoặc script E12. Baseline tạo một lần, không ghi đè. Hash-check kiểm full hash mọi file cũ, trừ hai tổng quan được kiểm byte prefix cũ và chỉ append; đồng thời phát hiện file mới ngoài gói trong docs.

| Checker | Phạm vi | Bằng chứng |
| :--- | :--- | :--- |
| check-e12.cjs | File bắt buộc, metadata, chuỗi truy vết và back-reference, mã mới không trùng nguồn cũ, link Markdown, số dính chữ, câu trả lời/Actual/Evidence trống, trạng thái ca, manifest | [structure-result.json](structure-result.json) |
| render-e12.cjs | Parse/render mọi khối Mermaid trong tài liệu nội dung E12 sang SVG/HTML; preview nhúng tài liệu | [diagram-render-result.json](diagram-render-result.json) |
| check-ui-e12.cjs | 12 màn tại 1440/390/360 px, nhãn, trạng thái, form/dialog, 4 góc nhìn dashboard, consent/xóa mô phỏng, preview; chặn và đếm request mạng | [ui-result.json](ui-result.json) |
| hash-check-e12.cjs | File cũ giữ hash; hai tổng quan chỉ append; file mới chỉ trong gói; schema 65 bảng | [hash-result.json](hash-result.json) |

Danh sách file mới: [files-created.json](files-created.json). Manifest là danh sách đường dẫn, không tự chứa hash biến động của chính nó.

## Kết quả và giới hạn

Kiểm cấu trúc/truy vết/mã/liên kết/số dính chữ: 0 lỗi ở lần kiểm sau khi result/manifest đầy đủ. Lần đầu có link result chưa tạo và manifest chưa khớp; đã cập nhật manifest, không bỏ qua link lỗi. Rà nội dung đã chuyển thêm 3 ca phụ thuộc thang đánh giá/receipt sang BLOCKED, tổng cuối 23 BLOCKED và 37 NOT RUN ở ca chức năng.

Render 7/7 sơ đồ thành SVG/HTML, 0 lỗi; preview nhúng 40 tài liệu nội dung. Báo cáo validation được liên kết riêng để tránh vòng lặp render. UI có 378 kiểm, 0 lỗi, 0 request mạng; 36 ảnh từng màn ở 1440/390/360 px và 8 ảnh ghép desktop/mobile. Đã xem cả 12 màn trên desktop/mobile; bổ sung khoảng cách giữa các khối và rút ngắn giá trị ô nhập để thông tin gate không bị cắt trên mobile. Nội dung giải thích đầy đủ nằm ngoài ô nhập, không có chồng/che nội dung hoặc tràn ngang toàn trang.

Bằng chứng xem ảnh: desktop [1–3](screenshots/1440-sheet-1.png), [4–6](screenshots/1440-sheet-2.png), [7–9](screenshots/1440-sheet-3.png), [10–12](screenshots/1440-sheet-4.png); mobile [1–3](screenshots/360-sheet-1.png), [4–6](screenshots/360-sheet-2.png), [7–9](screenshots/360-sheet-3.png), [10–12](screenshots/360-sheet-4.png).

**Hash-check còn 4 sai lệch so với baseline, không được coi là đạt 0 lỗi.** Baseline chụp lúc 15:10:45 ngày 12/11/2026. Trước thao tác append E12, bốn file dưới đã có hash/kích thước khác baseline và LastWriteTime khoảng 15:13:53 cùng ngày. Phiên E12 chưa có lệnh nào ghi vào chúng tại thời điểm phát hiện. Chưa xác định tác nhân hoặc nguyên nhân; không quy kết là thay đổi người dùng đã duyệt. Thử chuẩn hóa LF/CRLF không khớp hash cũ, nên không coi chỉ là đổi xuống dòng.

| File | Byte baseline | Byte quan sát trước append E12 | Xử lý trong phiên |
| :--- | :--- | :--- | :--- |
| docs/OVERVIEW.md | 26605 | 26058 | Giữ bản hiện tại; chỉ append thêm mốc E12 |
| docs/project-dashboard.md | 24305 | 23758 | Giữ bản hiện tại; chỉ append thêm mốc E12 |
| docs/gia-phat/review/next-session-prompt.md | 31080 | 30512 | Không sửa hoặc khôi phục |
| docs/gia-phat/review/progress-assessment.md | 17158 | 16632 | Không sửa hoặc khôi phục |

[pre-append-drift.json](pre-append-drift.json) lưu hash/kích thước/thời điểm quan sát trước append, tách riêng khỏi baseline gốc. Append E12 được kiểm theo đúng byte prefix vừa quan sát: cả hai prefix giữ nguyên, mỗi file chỉ thêm 3499 byte. Đây là bằng chứng phạm vi thao tác append của phiên, **không thay thế baseline và không miễn 4 lỗi hash**. Có 941/945 file cũ khớp toàn bộ SHA256, không file cũ bị xóa, không file mới ngoài gói trong docs; PRD, roadmap, schema 65 bảng và lịch sử E6–E11 giữ hash. Không tự khôi phục 4 file vì ngoài quyền sửa của phiên và không có bản byte gốc được phép phục hồi.

Ba checker cấu trúc/render/UI đạt; hash-check giữ 4 lỗi đã giải thích. Đã chạy lại cả 4 sau lần sửa tài liệu cuối. Vì vậy điều kiện “4 checker đạt, 0 file cũ thay đổi theo baseline” chưa đạt, dù phần tài liệu E12 và append được bàn giao. Phiên sau cần đối chiếu riêng thay đổi đồng thời này, không ghi đè baseline để làm checker xanh.

Chưa có sản phẩm, dữ liệu thật hoặc phê duyệt để chạy ca nghiệp vụ. Không có kiểm mock nào chứng minh quyền server/DB, persistence, tính toán cost, xóa dữ liệu thật hoặc nghiệm thu R12. Chưa audit WCAG đầy đủ hoặc kiểm thiết bị thật. Số UI/fixture đều synthetic. Ngày 12/11/2026 là ngày lập tài liệu, không phải ngày triển khai.

Không backend, migration, gọi mô hình AI, system prompt thật, lựa chọn nhà cung cấp/model AI, commit hoặc xóa file. Chỉ tạo/sửa gói E12 và append hai tổng quan. Không sửa PRD, roadmap, schema, progress-status hoặc baseline/manifest/report/result lịch sử E6–E11.
