# Bàn giao bổ sung BA E1–E5 và khởi đầu E6

Phiên bản0.1.0 · 11/11/2026 · Draft. Chưa ký baseline nghiệp vụ, chưa triển khai backend.

| Phiên bản | Ngày | Người thực hiện | Thay đổi |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung khoảng trống BA, preview/dashboard và lát cắt E6 |

## Kết quả và file chính

| Phân hệ | Bổ sung | Điểm vào review |
| :--- | :--- | :--- |
| E1 Nền tảng | Epic,26UC/story,78AC,ca BR/ERR/NFR,25endpoint HTTP và port nội bộ,flow/sequence/state,checklist/gap,6màn HTML | [Preview](../../nen-tang/preview.html), [API](../../nen-tang/api/api-spec.md), [RTM](../../nen-tang/test/traceability.md) |
| E2 MENU | Hợp đồng API/catalog/RTM riêng,ERD miền nối schema tổng,86ca quy tắc nháp,sequence/state/gap/preview,RTM chuẩn hóa story cũ | [Preview](../../thuc-don-dinh-luong/preview.html), [API](../../thuc-don-dinh-luong/api/api-spec.md), [rule tests](../../thuc-don-dinh-luong/test/rule-test-cases.md) |
| E3 Cost | Sequence/state,chỉ mục ERD miền,preview các tài liệu có sẵn; không viết lại nghiệp vụ đã làm | [Preview](../../cost/preview.html) |
| E4/E5 | Epic,sơ đồUC,sequence/state,checklist/gap,HTML tương tác3màn mỗi phân hệ,preview | [Dinh dưỡng](../../dinh-duong/preview.html), [Agent](../../agent-noi-bo/preview.html) |
| E6 | Epic/SRS capability19tính năng,backlog19story,ERD kế thừa+delta đề xuất,5endpoint trọng yếu,sequence/state,10ca và10câu hỏi | [Epic](../../chon-mon-order/epic-spec.md), [SRS](../../chon-mon-order/srs/spec.md), [phần còn thiếu](../../chon-mon-order/gap-analysis.md) |
| Dùng chung | Sổ phạm vi,dashboard,đồng bộ kế hoạch/OVERVIEW và liên kết phụ thuộc | [Phạm vi](../brainstorms/pham-vi-san-pham.md), [dashboard](../../project-dashboard.md), [OVERVIEW](../../OVERVIEW.md) |

Các trang preview nhúng nội dung Markdown và SVG cục bộ, không cần máy chủ/mạng. Đây là công cụ xem tài liệu, không phải ứng dụng nghiệp vụ. Dữ liệu wireframe nằm trong bộ nhớ trang và được ghi rõ GIẢ ĐỊNH. Các file `.md` là nguồn, preview cần render lại sau sửa nguồn.

## Kiểm chứng

[Báo cáo kiểm tra](../validation/completion-report.md) ghi kết quả kiểm mã/liên kết/coverage, Mermaid, wireframe và hồi quy tài liệu Cost. [Kết quả máy đọc](../validation/completion-check-result.json). Không coi kiểm JS/HTML/DBML là test backend hoặc UAT.

Script render-diagrams của skill có đường dẫn cũ `.agents/skills/skills/diagram-design` nên không render được. Dùng [render-review.cjs](../validation/render-review.cjs) với Mermaid/marked/Playwright cục bộ đã có để xuất SVG và preview; không tải thư viện từ CDN. Giữ giao diện đơn sắc phù hợp wireframe BA hiện có, không tạo bộ nhận diện thương hiệu mới.

## Phần còn thiếu / chưa được quyết định

- E1/E2 có hợp đồng để review nhưng còn E1-Q01–05 và MENU-API-Q01–03. Envelope/cursor của các extension chưa đồng nhất với nền; phải chốt trước build, không che bằng việc có catalog.
-86ca quy tắc MENU đã viết theo cấu hình/đề xuất hiện có, vẫn BLOCKED DL-01. Ca tương ứng rule ngoài R2 chỉ phục vụ review, không tự mở phạm vi.
- NUTR/AIO và các điểm mở Cost giữ nguyên. Đối soát thật,model,ngân sách,baseline thời gian và UAT chưa có.
- E6 là **gói khởi đầu**, chưa UC chi tiết/API đầy đủ/wireframe/3AC mỗi story/RTM toàn19feature. FEAT-046/047 gated O-03. Delta E6 chưa mergeDBML, schema tổng vẫn65bảng.
- E7–E13 chưa triển khai tài liệu riêng. Ngày,công sức,người phụ trách cụ thể vẫn chờ quyết định.

## Những xác nhận không thay đổi

Cost nguyên liệu gồmVAT phải trảNCC; không yêu cầu hóa đơn là cờ riêng, không suyVAT0. Chiết khấu% hoặc tiền/suất là khoản riêng theođơn, không tự giảm phải trả. CK-Q01–10 vẫn chờ, DATA-COST-Q01–06 vẫn trong phiếu kế toán, chưa có10món/10ngày thật. NFR-COST-002: cost món lệch≤1đ, cost% ngày≤0,01điểm phần trăm. Không viết backend/migration trong đợt này.

## Bổ sung tiếp nối E6 — 11/11/2026

Mô tả E6 khởi đầu trong báo cáo này là mốc lịch sử. [Gói E6 v0.2 mới](../../chon-mon-order/review/handoff.md) bổ sung19UC,57AC,26HTTP endpoint,2port,13màn vàRTM; các gate vẫn mở, schema65bảng không đổi, chưa backend/UAT. Dùng báo cáo E6 để xem bằng chứng kiểm riêng; không ghi đè kết quả46sơ đồ/12màn của E1–E5.
