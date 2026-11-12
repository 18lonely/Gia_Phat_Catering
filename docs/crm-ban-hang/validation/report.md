---
id: DOC-E10-VALIDATION-REPORT
title: Báo cáo kiểm gói BA nháp E10
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# Báo cáo kiểm gói BA nháp E10

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 12/11/2026 | BA | Kiểm tài liệu và mock E10; không kiểm sản phẩm |

## Phạm vi

4 feature P1 FEAT-070–073 có thiết kế nháp có điều kiện; không feature chỉ gate trong E10. 16 FR/UC/story, 48 AC/ca chức năng: 21 BLOCKED, 27 NOT RUN. 10 ca hệ thống có overlap: 5 BLOCKED, 5 NOT RUN. 23 HTTP endpoint và 7 port logic; 9 màn trong một HTML; 4 sơ đồ trạng thái và 2 luồng. 15 câu E10-Q01–15 chờ trả lời, cột trả lời trống.

Độ phủ tài liệu mới 60/78 ≈ 76,9%; FEAT-046/047/063 giữ chỉ gate. Schema 65 bảng không thay. Không backend, migration, gọi mô hình AI, commit hoặc xóa file; E11–E13 chưa mở.

## Kiểm và bằng chứng

Kết quả cuối được ghi sau lần kiểm cuối trong các tệp JSON của validation. Đây là kiểm artifact, không nghiệm thu R10/G-Next hoặc kết quả ca sản phẩm.

- `node docs/crm-ban-hang/validation/check-e10.cjs`: kiểm file bắt buộc, mã, quan hệ 1–1, ba AC/story, một ca/AC, oracle, catalog/spec, liên kết/anchor, câu hỏi trống, trạng thái ca, số dính chữ trong Markdown mới, schema và hash/prefix.
- `node docs/crm-ban-hang/validation/render-e10.cjs`: renderer riêng E10 dùng Mermaid/marked/Playwright đã có cục bộ, tạo preview 38 tài liệu và 6 sơ đồ. Không chạy hoặc sửa renderer E9.
- `node docs/crm-ban-hang/validation/check-ui-e10.cjs`: kiểm 9 màn ở 1440, 390, 360 px, nhãn, trạng thái, hộp review, projection mẫu riêng và preview; lưu ảnh từng màn và ảnh ghép.
- Baseline chứa SHA256 và kích thước của toàn bộ 763 file trong docs trước khi ghi file đầu tiên của E10. Ngoại lệ chỉ OVERVIEW và project-dashboard: kiểm hash byte prefix cũ; mọi file khác phải giữ toàn bộ hash và không bị xóa. Không reset baseline.

## Nguồn và cách làm

Đã đối chiếu mốc hiện hành và phiên chỉnh UC E7–E9; đọc PRD/roadmap R10/G-Next, URD/BRD; tham chiếu cấu trúc, tài liệu, API, ca kiểm, wireframe và script E9. Đối chiếu E8 lead, E9 handoff, E7 giao nhận/doanh thu, E6 order/lịch/sổ CG, MENU, Cost và E1 quyền/audit/schema.

Áp dụng lần lượt skill prd-epic → srs → usecase → userstory → ac → state/user-flow → api-design/api-map → wireframe-html → test-checklist → test-cases → preview → update-overview. Quy tắc và mẫu lấy tại `.claude/ba-kit` theo yêu cầu. Không tìm thấy AGENTS.md. `rg` không có nên dùng PowerShell/Node để đọc và tìm. Script `scripts/render_diagrams.py` được skill preview nhắc tới không tồn tại; dùng renderer cục bộ riêng E10 và giữ kết quả render, không coi bước thiếu script là đã chạy.

E9 thực tế append OVERVIEW, dashboard và hai file review; không append PRD/roadmap. Vì vậy chỉ hai file OVERVIEW/dashboard được append ở phiên E10, không sửa PRD/roadmap hoặc hai file review cũ. Nội dung lịch sử có lỗi số dính chữ không bị sửa; checker chỉ kiểm văn bản mới trong E10.

## Giới hạn

Không có dữ liệu sản phẩm, môi trường/backend hoặc bằng chứng phê duyệt để chạy 48 ca chức năng, 10 ca hệ thống hay nghiệm thu R10. Actual/Evidence của ca sản phẩm vẫn trống. Kiểm HTML không chứng minh quyền server, lưu bền vững, tính giá hoặc bảo vệ dữ liệu trong sản phẩm. Chưa audit WCAG đầy đủ hoặc kiểm trên thiết bị thật.

Các câu nguồn E1–E9 giữ chờ; chi tiết tại [phụ thuộc](../review/dependencies.md). Cost gồm VAT phải trả nhà cung cấp; cờ hóa đơn riêng; CK%/tiền suất riêng không giảm phải trả nhà cung cấp. Không chọn tiêu chí trùng, ngưỡng nguy cơ rời, công thức margin, biên ngày hiệu lực hoặc người duyệt thay người có thẩm quyền.

## Kết quả cuối phiên

- Kiểm cấu trúc/truy vết/liên kết/mã và oracle: không lỗi. Số kiểm cùng toàn bộ chi tiết nằm tại [structure-result.json](structure-result.json); chạy lại sau khi hoàn tất manifest và báo cáo để đối chiếu bản cuối.
- Render: 6/6 sơ đồ thành SVG/HTML, 0 lỗi; [diagram-render-result.json](diagram-render-result.json). Preview nhúng 38 tài liệu nội dung và sơ đồ; báo cáo validation được liên kết riêng để tránh vòng lặp render.
- UI: 256 kiểm mock, 0 lỗi, 0 request mạng; [ui-result.json](ui-result.json). Có 27 ảnh từng màn ở ba kích thước và 9 ảnh ghép. Đã xem bố cục desktop/mobile; sau rà trực quan đã đổi điều hướng mobile thành lưới và tăng chiều cao bản khách để không che cuối nội dung. Bảng rộng có vùng cuộn riêng và nhãn hướng dẫn. [Ảnh 360 px màn 1–3](screenshots/360-sheet-1.png), [4–6](screenshots/360-sheet-2.png), [7–9](screenshots/360-sheet-3.png).
- SHA256: **761 file cũ giữ nguyên toàn bộ hash; 2 file chỉ append với byte prefix cũ giữ nguyên; 0 thay đổi ngoài phép, 0 file cũ bị xóa**. Chi tiết [hash-result.json](hash-result.json); [baseline gốc](baseline.json) không bị ghi lại. PRD, roadmap và schema giữ nguyên hash.
- Chỉ append [OVERVIEW](../../OVERVIEW.md) và [project-dashboard](../../project-dashboard.md), không sửa hai file review từng được E9 append.

Lần tạo wireframe đầu báo thiếu thư mục đích; đã tạo đúng thư mục E10 rồi chạy lại thành công. `render_diagrams.py` không có nên không chạy được tên script đó; chức năng render đã hoàn thành bằng renderer riêng E10. Không có bước kiểm tài liệu/UI bắt buộc nào còn bị chặn bởi công cụ. Các ca sản phẩm và R10/G-Next chưa chạy vì chưa có sản phẩm, dữ liệu và quyết định cần thiết; không có ca sản phẩm PASS.

Danh sách toàn bộ file tạo mới và hash tại [files-created.json](files-created.json). Không chạy lại script author/complete/build-ui sau bàn giao vì chúng tạo lại bản nháp; dùng checker và renderer riêng khi cần kiểm, chỉ sửa theo phản hồi có nguồn.
