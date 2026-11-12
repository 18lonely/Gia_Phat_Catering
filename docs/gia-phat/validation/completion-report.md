# Báo cáo kiểm tra gói bổ sung BA

Phiên bản0.1.0 · 11/11/2026 · Tự kiểm thiết kế; chưa nghiệm thu phần mềm.

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | Ghi bằng chứng kiểm gói BA và giới hạn |

## Kết quả kiểm gói tài liệu

| Hạng mục | Kết quả | Giới hạn |
| :--- | :--- | :--- |
| check-completion.py | Đạt:172 file Markdown trong phạm vi kiểm không có liên kết file gãy; E1 đủ26FR→story/test; MENU55FR được nối API/port hoặc gated rõ | Không chứng minh độ phủ mọi tổ hợp nghiệp vụ; không kiểm toàn bộ anchor Markdown lịch sử |
| E1 |26UC/story,78AC,140ca thiết kế gồm78ca theoFR,15BR,24ERR,23NFR;25HTTP endpoint | Ca P1/gate và NFR chưa đủ đầu vào;0test backend đã chạy |
| MENU |60method/path không trùng;54/55FR có story/test liên kết;RCP-007 chờO-02;86ca rule nháp cho43quy tắc |86ca vẫn BLOCKED DL-01; không thay con số dự kiến khoảng140ca bằng kết quả đã đạt |
| Render Mermaid |46/46 sơ đồ E1–E5 parse và xuất SVG/HTML đạt | Kiểm cú pháp/render; nội dung vẫn cần stakeholder review |
| Wireframe mới |12màn trong3HTML; thử360/390px không tràn ngang trang; kiểm desktop1440px;0lỗi JS trong lần chạy cuối | Chỉ mô phỏng, không gọi backend/model; không phải chứng nhận WCAG đầy đủ |
| Preview |5trang đọc tài liệu cục bộ; chuyển mục/tìm tài liệu hoạt động, một section hiển thị mỗi lần | Markdown là nguồn; cần render lại khi sửa |
| E6 |19FR capability,19story,5endpoint,10ca trọng yếu và10câu hỏi | Gói khởi đầu, còn thiếu UC/API/UI/AC/RTM đầy đủ; không tính hoàn thành E6 |

[Bàn giao](../review/ba-completion-handoff.md) · [inventory](completion-check-result.json) · [kết quả render](diagram-render-result.json) · [kết quả UI](ui-review-result.json).

Đã sửa lỗi cú pháp dấu chấm phẩy trong nhãn sequence và escape xuống dòng của hai wireframe phát hiện ở lần chạy đầu. Kết quả trên thuộc lần chạy lại sau sửa. Script render-diagrams đi kèm skill không tìm đúng thư mục hỗ trợ; dùng renderer Mermaid cục bộ, không bỏ qua diagram lỗi để báo đạt.

## Nhánh UI đã kiểm

- Nền tảng:5lần đăng nhập sai; xóa ô mật khẩu sau submit; bắt buộc cơ sở cho bếp; không tự duyệt tham số; duyệt lặp không thêm audit giả; offline không ghi; retry job không nhân đôi.
- Dinh dưỡng:fixture món40kcal/tổ hợp50kcal; không cộng haiMAIN khi chỉ chọn1; thiếu nguồn không trả tổng; snapshot cũ giữ số khi nguồn đổi; version409; chuỗi HTML nguồn được hiển thị như text.
- Agent:tuần thứHai;4outcome khôngVALID đều chặn apply; xác nhận/quay lại; áp dụng chỉDRAFT; replay không apply lầnhai; nguồn stale409; chỉnh tạo run mới/diff; log escape HTML, chi phí UNKNOWN không thành0.
- Đã xem trực quan ảnh desktop/mobile và mẫu sơ đồ sequence/state. Số liệu sinh ở UI là fixture, không thay phép tính Decimal/backend hoặc bảng thành phần thật.

Ảnh: [nền tảng](foundation-desktop.png), [dinh dưỡng](nutrition-desktop.png), [agent mobile](agent-mobile.png), [preview](preview-desktop.png), [sequence](diagram-sequence.png), [state](diagram-states.png).

## Hồi quy tài liệu đã có

Chạy lại `check-mvp-review.py` và các script Cost `check-backlog.py`, `check-usecases.py`, `check-reconciliation.py`; không đổi108ca Cost baseline/32điểm review thành PASS phần mềm. `check-accounting-design.cjs` chỉ kiểm cú pháp ở đợt này, không chạy lại tương tác kế toán vì không sửa UI kế toán. DBML không đổi so v0.5.0, vẫn65bảng; delta E6 là đề xuất trong ERD, chưa merge/migration.

## Tái chạy và giới hạn

```powershell
python docs/gia-phat/validation/check-completion.py
python docs/gia-phat/validation/check-mvp-review.py
node docs/gia-phat/validation/render-review.cjs
node docs/gia-phat/validation/check-review-ui.cjs
python docs/cost/validation/check-backlog.py
python docs/cost/validation/check-usecases.py
python docs/cost/validation/check-reconciliation.py
```

Renderer và UI checker dùng thư viện đã có ở `$env:TEMP/gia-phat-cost-validation/node_modules`; có thể truyền thư mục dependency khác làm tham số đầu. Không cần CDN/mạng để mở preview đã xuất. Không có backend, provider AI, dữ liệu kế toán thật hoặc UAT trong phạm vi kiểm này.

## Bổ sung tiếp nối E6 — 11/11/2026

Mô tả E6 khởi đầu trong báo cáo này là mốc lịch sử. [Gói E6 v0.2 mới](../../chon-mon-order/validation/report.md) bổ sung19UC,57AC,26HTTP endpoint,2port,13màn vàRTM; các gate vẫn mở, schema65bảng không đổi, chưa backend/UAT. Dùng báo cáo E6 để xem bằng chứng kiểm riêng; không ghi đè kết quả46sơ đồ/12màn của E1–E5.
