---
id: DOC-E6-VALIDATION-REPORT
title: Báo cáo kiểm tra gói BA E6
version: 0.2.0
phase: Validation
domain: Gia Phát
author: BA
last_updated: 2026-11-11
---
# Báo cáo kiểm tra gói BA E6

11/11/2026 · **Tự kiểm tài liệu và wireframe; không phải nghiệm thu nghiệp vụ hoặc kiểm thử phần mềm.**

| Hạng mục | Kết quả / bằng chứng | Giới hạn |
| :--- | :--- | :--- |
| Phạm vi |19feature giữ14P0/5P1;19UC/story;57AC; [RTM](../test/traceability.md) |17thiết kế có điều kiện,2gate O-03; không đủ căn cứ đóng mọi nghiệp vụ |
| Kiểm cấu trúc | [check-result.json](check-result.json), script [check-e6.py](check-e6.py): mã, route, file link, số màn, hash DBML/quy tắc kế toán | Không chứng minh đầy đủ mọi tổ hợp nghiệp vụ; không kiểm toàn bộ Markdown anchor |
| Test thiết kế |57ca mới:29 NOT RUN,28 BLOCKED;10ca khởi đầu giữ nguyên;12ca hệ thống bổ sung |79 mô tả có overlap;0test backend; Actual/Evidence chưa có |
| API |26method/path không trùng,2port; không endpoint FEAT-046/047 | Contract đề xuất; identity/provisioning/weekly policy/plan acknowledgement còn gate |
| Mermaid |8/8 parse và render SVG/HTML; [kết quả](diagram-render-result.json), [gallery](../srs/diagrams/index.html) | Kiểm cú pháp/render, không phê duyệt nội dung |
| Wireframe |13màn kiểm1440/390/360px, không tràn ngang trang,0lỗiJS; [ui-result.json](ui-result.json) | Mô phỏng trong bộ nhớ; không security/race/load backend; chưa chứng nhận WCAG |
| Trực quan | Đã xem ảnh [desktop plan](desktop-plan.png), [mobile selection](mobile-selection.png) | Phiếu bếp fixture MAIN A; món phụ/đa định lượng chờ ORD-Q10 |
| Preview | Điều hướng/tìm tài liệu,1section hiển thị mỗi lần; [ảnh](preview-desktop.png) | Markdown nguồn là chuẩn; cần render lại sau sửa |
| Schema/quy tắc bảo toàn | DBML65bảng không đổi hash; nguồn CK và DATA-COST không đổi hash | Delta chỉ đề xuất, không migration hoặc schema được duyệt |

## Nhánh UI đã kiểm

Chọn bằng định mức/vượt1đ; đổi A→B không nhân counter; replay cùng yêu cầu; offline/stale/empty không ghi; QR revoked; guest chọn tuần403; policy chưa chốt và hai phương án tuần synthetic; T<S+C; dialog quay lại/xác nhận; thiếu default; đến hạn chặn ghi; lock replay; nhắc chưa cấu hình; tự duyệt403; gate duyệt; approval replay; bản kế hoạch cũ giữ100 trong khi bản mới105; chứng cứ nhập hộ; sau khóa chuyển đề nghị; không form sức khỏe; text input không bị render thành HTML.

Kiểm hệ thống thực phải chạy các ca [system-test-cases](../test/system-test-cases.md) khi có backend. Wireframe không chứng minh transaction, duplicate identity, provider delivery, source event hay bảo mật thực.

## Cách tái kiểm

```powershell
python docs/chon-mon-order/validation/check-e6.py
node docs/chon-mon-order/validation/render-e6.cjs
node docs/chon-mon-order/validation/check-ui.cjs
```

Renderer dùng cách hiện có tại `docs/gia-phat/validation/render-review.cjs`, clone giới hạn E6 để không ghi đè46sơ đồ/preview E1–E5. Dependency cục bộ ở TEMP/gia-phat-cost-validation; có thể truyền thư mục khác làm đối số. Không CDN khi mở preview. Đã đọc bản rule tại `.claude/ba-kit`. Không có AGENTS.md trong workspace đã quét.

Lần kiểm cấu trúc đầu phát hiện link tới handoff/report chưa tạo; đã bổ sung hai file trước lần kiểm cuối. Không đánh dấu đạt bằng cách bỏ qua liên kết gãy. [Bàn giao](../review/handoff.md) ghi điểm chặn/công việc sau; [manifest](change-manifest.md) liệt kê file thay đổi.

## Hồi quy tài liệu phụ thuộc

Đã chạy lại check-mvp-review.py:50Markdown,65bảng,0lỗi; Cost check-backlog.py/check-usecases.py/check-reconciliation.py đạt cấu trúc và số học synthetic. Giữ28story/108ca Cost (62NOT RUN,46BLOCKED),16UC/43FR có luồng và2FR hoãn; không chuyển thành PASS backend. Không chạy lại UI Cost vì không sửa UI đó. Không có dữ liệu kế toán thật mới.

Customer master phải tồn tại trước service context; quy trình tạo khách tối thiểu/reuse CRM và provisioning identity còn ORD-Q03/11. Catalog không đại diện cho toàn bộ bước onboarding đã sẵn sàng build.
