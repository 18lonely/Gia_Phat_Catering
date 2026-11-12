---
id: DOC-E11-VALIDATION-REPORT
title: Báo cáo kiểm gói BA nháp E11
version: 0.1.0
phase: Review
domain: Gia Phát
tags: [e11, validation, draft]
depends_on: [DOC-PRD-GIA-PHAT]
related_diagrams: []
author: BA
last_updated: 2026-11-12
---
# Báo cáo kiểm gói BA nháp E11

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Mở và kiểm riêng tài liệu E11 |

## Phạm vi và số liệu

5/5 feature P1 FEAT-074–078 có thiết kế nháp có điều kiện; 0 feature E11 chỉ gate. 15 FR, 15 UC Cockburn, 15 story, 45 AC và 45 ca chức năng: 13 BLOCKED, 32 NOT RUN. Có 10 ca hệ thống có overlap: 5 BLOCKED, 5 NOT RUN. Khung nghiệm thu R11 có 3 dòng BLOCKED, không cộng vào số ca chức năng. Actual/Evidence của mọi ca sản phẩm để trống.

15 HTTP endpoint và 4 port ranh giới đề xuất; 9 màn trong một file HTML; 5 sơ đồ trạng thái và 2 sơ đồ luồng. 15 câu E11-Q01–15 có cột Trả lời trống. Có bảng từ điển delta nhưng không sửa schema 65 bảng.

Độ phủ **thiết kế tài liệu nháp (60 + 5) / 78 = 65/78 ≈ 83,3 %**. Ba feature chỉ gate FEAT-046/047/063 được ghi riêng, không cộng vào tử số. Đây không phải BA được duyệt, tiến độ phần mềm hoặc nghiệm thu R11/G-Next. E12/E13 chưa mở; không đặc tả FEAT-082/083.

## Nguồn đã đọc trước khi viết

Đã đọc các mục nghiệp vụ và điểm nối liên quan trong nguồn dưới đây; không coi nội dung nháp là chính sách được duyệt. Các tài liệu dài được rà theo mục, mã và trường cần cho E11.

| Nguồn | Nội dung đọc / áp dụng |
| :--- | :--- |
| [OVERVIEW](../../OVERVIEW.md) | Mốc cuối E10, lịch sử và giới hạn phạm vi |
| [Tiến độ ngày 12/11/2026](../../gia-phat/review/progress-status-2026-11-12.md) | Nền 60/78, 3 feature chỉ gate, 65 bảng, điểm mở |
| [PRD](../../gia-phat/01-prd.md) | BO-02, PER-05/06/07/08, FEAT-074–078, ranh giới E12/E13 |
| [Roadmap](../../gia-phat/02-roadmap.md) | R11, điều kiện R3/R6, G-Next, mẫu lưu và mục tiêu 3 điểm phần trăm |
| [Handoff E10](../../crm-ban-hang/review/handoff.md), [report E10](../../crm-ban-hang/validation/report.md) | Cấu trúc gói, các thư mục và quy tắc bàn giao; đã liệt kê cây thư mục |
| [Cost SRS](../../cost/srs/spec.md) | Dự toán theo phiên bản, lượng/giá, hao hụt và NFR-COST-002 |
| [Quy tắc kế toán](../../cost/accounting/business-rules.md) | Giá gồm VAT phải trả; cờ hóa đơn và chiết khấu riêng |
| [Cost API](../../cost/api/api-spec.md) | PriceInput, EstimateQuantity/Full, projection quyền, snapshot và nguồn chứng từ |
| [MENU SRS](../../thuc-don-dinh-luong/srs/spec.md) | Định lượng sống, đơn vị, loại bảo quản, vai trò món, dị ứng, rule và duyệt |
| [Order SRS](../../chon-mon-order/srs/spec.md) | Kế hoạch theo món và revision; GET không build/publish/ack/start |
| [CG E6](../../chon-mon-order/review/contract-gap-register.md) | Các điểm OPEN; đặc biệt CG05/06/07/08 và không đặc tả tiếp phần đang chờ |
| [Giao nhận SRS](../../giao-nhan-doanh-thu/srs/spec.md) | Số giao/nhận/tính tiền riêng, Q-13, căn cứ doanh thu và kỳ |
| [Nền tảng SRS](../../nen-tang/srs/spec.md) | Quyền mỗi request theo cơ sở, audit, tách tạo/duyệt và file |
| [ERD](../../nen-tang/srs/erd.md), [DBML](../../nen-tang/srs/schema.dbml) | Phân biệt khung PUR/PLAN trong ERD với 65 bảng thực có trong DBML |
| Quy tắc `.claude/ba-kit/rules/*.md` | Đã đọc 19 quy tắc: mã, Cockburn, INVEST, GWT, dữ liệu, API, lỗi, state, wireframe, RTM, metadata và phiên bản |
| Mẫu `.claude/ba-kit/_templates` | Đã liệt kê thư mục; đọc mẫu 07, 08, 19, 26, 27, 28, 29, 31, 37, 38, 42, 43 |
| Script E10 chỉ đọc | Tham khảo renderer và UI checker; tạo bản riêng E11, không chạy generator/checker E10 |

## Điểm nối E11 ↔ E2/E3/E6/E7

- E2 → E11: định lượng, quy đổi, loại bảo quản, vai trò và dị ứng. Thay món phải cùng vai trò, luôn kiểm lại dị ứng và rule, rồi qua cổng duyệt MENU. DL-01/O-02 không được mở bằng E11.
- E3 ↔ E11: dùng dự toán có phiên bản và PriceInput. Cost gồm VAT phải trả NCC; giữ NFR-COST-002. Nhận hàng chưa tự cập nhật giá hiệu lực; E11-Q14 giữ ranh giới. BO-02 cần cách đo Q07/08, không tự lấy doanh thu hoặc đổi ngưỡng.
- E6 → E11: nhu cầu/phân ca cần nguồn kế hoạch đúng revision. CG06 và ORD-Q còn mở; E11 chỉ ghi cổng thiếu nguồn, không thiết kế tiếp quy trình build/publish/ack/start hoặc sửa order.
- E11 ↔ E7: QC/mẫu là dữ liệu chuẩn bị giao, không phải khách đã nhận. Công nợ NCC riêng với phải thu khách; không suy doanh thu từ số giao hoặc QC. Q-13/E7-Q01–08 giữ nguyên.

## Skill đã dùng và ngoại lệ theo chỉ dẫn người dùng

Đã đọc và áp dụng theo thứ tự: prd-epic → srs → usecase → userstory → ac → state/user-flow → api-design/api-map → wireframe-html → test-checklist/test-cases → preview. Nguồn skill ở `.agents/skills/<tên>/SKILL.md`.

Không gán story point dù mẫu skill có bước đó. Không tự chốt NFR mới từ số ví dụ của template. Bước review checklist chưa có phê duyệt nên ghi rõ, vẫn viết ca nháp theo yêu cầu. Không tìm hoặc chạy `scripts/render_diagrams.py`; dùng renderer E11 cục bộ. `rg` không có trong môi trường, đã dùng PowerShell/Node để đọc và tìm. Không tìm thấy AGENTS.md trong workspace khi rà đầu phiên.

## Kiểm và bằng chứng

Baseline chụp SHA256 và kích thước của **873 file hiện có trong docs**, trước khi ghi bất kỳ tài liệu hoặc script E11 nào. [Baseline](baseline.json) không ghi lại. Hai ngoại lệ append kiểm bằng hash byte prefix cũ, mọi file cũ khác phải giữ nguyên toàn bộ hash; checker cũng phát hiện file mới ngoài gói trong docs.

| Checker riêng | Phạm vi | Kết quả chi tiết |
| :--- | :--- | :--- |
| `check-e11.cjs` | File bắt buộc, metadata, mã không trùng E1–E10, chuỗi FR/UC/story/AC/test/API/màn, link Markdown, câu hỏi trống, trạng thái ca, số dính chữ ở văn bản mới, manifest | [structure-result.json](structure-result.json) |
| `render-e11.cjs` | Parse/render toàn bộ khối Mermaid trong tài liệu nội dung E11 bằng Mermaid cục bộ; xuất SVG/HTML và preview có tài liệu nhúng | [diagram-render-result.json](diagram-render-result.json) |
| `check-ui-e11.cjs` | 9 màn ở 1440/390/360 px, overflow, nhãn, trạng thái, form, dialog, preview, request mạng; chụp từng màn và ảnh ghép | [ui-result.json](ui-result.json) |
| `hash-check-e11.cjs` | Mọi file cũ so baseline, phát hiện xóa/thay đổi; chỉ cho 2 file tổng quan append | [hash-result.json](hash-result.json) |

Danh sách file tạo mới: [files-created.json](files-created.json); manifest là danh sách đường dẫn, không tự chứa hash biến động của chính nó.

## Giới hạn

Không có sản phẩm, dữ liệu thật hoặc quyết định để chạy ca nghiệp vụ. Kiểm artifact không chứng minh quyền server, persistence, số dư công nợ, tính cost, giữ mẫu đúng quy định hoặc nghiệm thu R11. Không audit WCAG đầy đủ, không kiểm thiết bị thật. Các fixture VAT 8 %, 10 bữa, 50 %/53 % đều synthetic, không phải chính sách đã chọn.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; O-01–O-06; CK-Q01–10; DATA-COST-Q01–06; AIO-Q01–06; NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, không trả lời thay hoặc viết tiếp phần phụ thuộc. Không chọn NCC thật, người phụ trách, ngày triển khai hoặc story point.

## Kết quả cuối phiên

- Kiểm cấu trúc/truy vết/mã/liên kết và số dính chữ: 0 lỗi ở lần kiểm cuối. Lần đầu có 2 liên kết tới result chưa được tạo; sau khi các checker ghi kết quả, chạy lại để xác nhận liên kết tồn tại. Không bỏ qua liên kết lỗi.
- Render: 7/7 sơ đồ thành SVG/HTML, 0 lỗi. Preview nhúng 35 tài liệu nội dung; báo cáo validation được liên kết riêng để tránh vòng lặp render.
- UI: 283 kiểm, 0 lỗi, 0 request mạng. Có 27 ảnh từng màn tại 1440/390/360 px và 6 ảnh ghép desktop/mobile. Đã xem cả 9 màn qua 6 ảnh ghép sau lần sửa giao diện: bổ sung trường nhập theo nghiệp vụ, tăng khoảng cách nút, hiển thị ngày 12/11/2026. Không phát hiện che/chồng nội dung hoặc tràn ngang; nội dung dài cuộn dọc. Trường text dài có thể cuộn trong ô nhập như hành vi native.
- Bằng chứng rà trực quan: [desktop 1–3](screenshots/1440-sheet-1.png), [4–6](screenshots/1440-sheet-2.png), [7–9](screenshots/1440-sheet-3.png); [mobile 1–3](screenshots/360-sheet-1.png), [4–6](screenshots/360-sheet-2.png), [7–9](screenshots/360-sheet-3.png).
- SHA256: 871 file cũ giữ nguyên toàn bộ hash; 2 tổng quan chỉ append với byte prefix cũ giữ nguyên; 0 file cũ bị xóa hoặc sửa ngoài phép, 0 file mới ngoài gói trong docs. PRD, roadmap và schema giữ nguyên. Baseline không ghi đè.
- Đã append mốc E11 vào OVERVIEW và project-dashboard. Không sửa progress-status hoặc kết quả/manifest/report lịch sử E6–E10.

Chạy lại cả 4 checker sau lần sửa cuối. Không dùng kết quả kiểm mock làm PASS cho sản phẩm. Giữ script author/refine để truy nguồn tạo artifact; không chạy lại chúng khi review từng thay đổi vì có thể ghi lại bản nháp. Phiên sau dùng checker/renderer riêng và prompt cuối handoff.
