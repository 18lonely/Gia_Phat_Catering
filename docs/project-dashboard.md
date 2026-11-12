# Dashboard tài liệu BA — Gia Phát

Phiên bản0.1.0 · 11/11/2026 · Draft. Chỉ đo hồ sơ tài liệu; không đo phần mềm đã hoàn thành.

| Phiên bản | Ngày | Nội dung |
| :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | Bổ sung dashboard từ inventory workspace và kiểm truy vết |

## Phạm vi

E1–E5 có SRS nháp cho23/23 tính năng MVP. E6 có gói review19capability:17thiết kế có điều kiện và2gate; không cộng19 vào mức hoàn tất BA được phê duyệt. E7–E13 chưa có SRS riêng. Toàn sản phẩm78tính năng theo PRD;23/78≈29% là độ phủ SRS nháp MVP, không phải tiến độ phát triển.

## Độ phủ cấu trúc

Bảng số liệu được cập nhật sau lần kiểm tại [completion-check-result.json](gia-phat/validation/completion-check-result.json). Đếm mãFR→story→test là liên kết cấu trúc, không chứng minh chất lượng/tính đủ nghiệp vụ. FR không có UI trực tiếp (audit,service account,hook) không cần màn hình riêng; không dùng tỷ lệ tham chiếu trực tiếp để suy chất lượng UI.

### Số liệu từ lần kiểm cấu trúc

| Epic | FR trong SRS | FR có story | FR có test liên kết | HTTP endpoint | UC / story | Wireframe |
| :--- | ---: | :--- | :--- | ---: | :--- | :--- |
| E1 | 26 | 26/26 (100.0%) | 26/26 (100.0%) | 25 | 26 UC / 26 story | 6 màn trong1HTML |
| E2 | 55 | 54/55 (98.2%) | 54/55 (98.2%) | 60 | 13 UC / 53 story | 3 màn HTML có sẵn |
| E3 | 45 | 43/45 (95.6%) | 43/45 (95.6%) | 37 | 16 UC / 28 story | 18 màn Cost +4 màn kế toán có sẵn |
| E4 | 5 | 5/5 (100.0%) | 5/5 (100.0%) | 7 | 5 UC / 5 story | 3 màn HTML mới |
| E5 | 6 | 6/6 (100.0%) | 6/6 (100.0%) | 6 | 6 UC / 6 story | 3 màn HTML mới |

Mẫu số gồm cả FR gated/hoãn: E2 thiếu mapping cho RCP-007 chờ O-02; Cost giữ2FR hoãn,43/43FR có luồng đã có story/test. Bảng không cộng6FR kế toán mở rộng vào45FR Cost gốc. Các phần đã có được kế thừa, không tính là mới làm trong đợt này.

Về gắn màn hình: E1 có26/26FR được nối tới nhóm UI hoặc panel kỹ thuật qua RTM; E4 có5/5, E5 có6/6. Đây là truy vết bố cục, không có nghĩa mọi hành vi được mô phỏng đầy đủ. E2/Cost có UI cũ nhưng chưa chuẩn hóa đầy đủ mapping FR→screen theo cùng cách; không đưa tỷ lệ thấp từ tìm chuỗi trực tiếp thành kết luận thiếu giao diện. Cần rà mapping này khi review chi tiết.

## Việc còn chặn

- Nền tảng: E1-Q về chuẩn API, idempotency, MFA, thông báo và quyền quản trị; N/O gốc chưa đóng.
- MENU: DL-01 chưa duyệt;86 ca rule mới đều BLOCKED; O-02 và3 câu API còn mở.
- Cost: dữ liệu10món/10ngày chưa có; CK và nhánh Cost chưa chốt. Nguyên tắc đã xác nhận giữ nguyên.
- Dinh dưỡng/Agent:11 câu hỏi của gói trước còn mở; dữ liệu5suất,20yêu cầu và baseline chưa có.
- E6: ORD-Q01–15 chờ; đã có UC/API/UI/AC/RTM để review; O-03 vẫn gated hồ sơ/gợi ý sức khỏe.

## Điều hướng

[Nền tảng](nen-tang/preview.html) · [MENU](thuc-don-dinh-luong/preview.html) · [Cost](cost/preview.html) · [Dinh dưỡng](dinh-duong/preview.html) · [Agent](agent-noi-bo/preview.html) · [E6 review](chon-mon-order/preview.html).

[Bàn giao đợt này](gia-phat/review/ba-completion-handoff.md) · [OVERVIEW](OVERVIEW.md). Ngày triển khai,story point và người chịu trách nhiệm cụ thể chưa được tự gán.

## Inventory E6 — gói review v0.2

| Feature | UC/story | AC | HTTP/port | UI | Test design | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|19(14P0/5P1)|19/19|57|26/2|13màn trong1HTML|57mới +10gốc +12hệ thống có overlap|0test backend;17thiết kế có điều kiện,2gate O-03|

[Bằng chứng](chon-mon-order/validation/report.md) · [RTM](chon-mon-order/test/traceability.md). Schema65bảng không đổi. Mọi số là inventory tài liệu, không tăng tỷ lệ phần mềm hoàn tất.

## Review quyết định E6 — 11/11/2026

[DR-01–04](chon-mon-order/review/decision-review.md) đã rà identity/scope, số suất, khóa hạn và kế hoạch. Có xác nhận đầu vào danh sách/người quản lý, chưa chốt cơ chế identity. 8phát hiện; sửa các mâu thuẫn tài liệu có căn cứ, bổ sung8ca review riêng. Chưa freeze schema/API, chưa backend; không mở E7–E13. [Kết quả kiểm](chon-mon-order/validation/decision-review-report.md).

## Rà tiến độ theo feature — 11/11/2026

Độ phủ thiết kế nháp ngoài gate-only:40/78≈51,3% (23feature E1–E5 +17E6). E6:17/19≈89,5%capability có thiết kế có điều kiện,19/19có dòng RTM; không phải tỷ lệ hoàn tất được duyệt hoặc effort. Chưa có backend/UAT trong gói này. Bộ ca E6 hiện có87mô tả (10+57+12+8), có overlap,0test backend. [Phương pháp và giới hạn](gia-phat/review/progress-assessment.md) · [Prompt làm tiếp](gia-phat/review/next-session-prompt.md).

## Bổ sung E6 độc lập — 11/11/2026

[Bàn giao E6 độc lập](chon-mon-order/review/independent-handoff.md):12ca invariant NOT RUN và fixture/checklist/profile1000CCU synthetic; tổng99mô tả ca (10+57+12+8+12), có overlap. Bộ57ca vẫn29NOT RUN/28BLOCKED;8DR vẫn BLOCKED;0test backend. Độ phủ40/78 và17/19 không đổi;0/8finding được xác nhận đóng.

## Review contract tiếp nối — 11/11/2026

[Bàn giao review delta/evidence E6](chon-mon-order/review/contract-handoff.md): đồng bộ alias, làm rõ giới hạn deltaByDish/READY và mock, bổ sung fixture/evidence. Không thêm feature hoặc ca:40/78thiết kế nháp;17/19E6 có điều kiện;99mô tả ca overlap,0backend;0/8RV đóng.

## Adapter/validation E6 — 11/11/2026

[Handoff adapter E6](chon-mon-order/review/adapter-handoff.md):26/26route có review validation,0/26thực thi.6oracle synthetic bổ sung, không thêm ca;99mô tả ca overlap.40/78feature,17/19E6 có điều kiện,0/8RV đóng không đổi.

## Hợp nhất gap/DTO E6 — 11/11/2026

[Bàn giao DTO/gap E6](chon-mon-order/review/dto-handoff.md):34/34DTO có dòng review,14/14nhóm gap có vai trò/điều kiện đóng;0/14gap được duyệt đóng.40/78feature,17/19E6 có điều kiện,0/8RV đóng và99mô tả ca overlap không đổi;0backend.

## Rà 19 UC E6 — 12/11/2026

[Ma trận UC](chon-mon-order/review/uc-operation-review.md):19/19đã rà actor/trigger/hậu điều kiện;12UC có ghi HTTP,3worker,2đọc,2gate. Độ phủ thiết kế nháp40/78 (51,3%), E6 có điều kiện17/19 (89,5%), RTM19/19; không tăng vì sửa diễn đạt. 34/34DTO đã rà hiện diện;0/14gap và0/8RVđóng. 99mô tả ca overlap;57ca29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED;0backend.26HTTP/2port,13màn,8sơ đồ,65bảng không đổi. [Kiểm và manifest](chon-mon-order/validation/uc-review-report.md).

## Tài liệu hạ nguồn và evidence QA — 12/11/2026

DOCUMENT_CLARIFIED: đã rà backlog/checklist/user-flow,8/8sơ đồ hiện có và hướng dẫn QA theo ranh giới UC; không lặp review19UC/34DTO. [Kết quả và file thay đổi](chon-mon-order/validation/downstream-report.md).40/78feature thiết kế nháp (51,3%),17/19capability E6 có điều kiện (89,5%),19/19RTM;19UC/57AC/26HTTP/2port/13màn/8sơ đồ/65bảng giữ nguyên.99mô tả ca overlap;57ca29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED;0backend.14/14gap OPEN,0/14CG và0/8RVđóng. Chặn theo sổ gap hiện hành; E6-EVID-001/002, Cost/VAT/chiết khấu và O-02/O-03 không đổi.

## Rà ca gốc và hệ thống — 12/11/2026

DOCUMENT_CLARIFIED: đã đối chiếu10/10ca gốc và12/12ca hệ thống (22/22) với SRS/API/catalog/UC/AC/evidence-protocol; sửa ranh giới GET/ghi/PORT-LOCK/worker/PORT-REM, scope synthetic và tách evidence producer/read trong cùng mã ca. Không thêm ca, không đổi Status/Actual/Evidence.40/78feature nháp (51,3%),17/19E6 có điều kiện (89,5%),19/19RTM;99mô tả ca có overlap,0backend. Bộ57ca29NOT RUN/28BLOCKED;12INV NOT RUN;8DR BLOCKED.14/14gap OPEN,0/14CG và0/8RVđóng;34/34DTO và19/19UC đã rà từ trước, không rà lại. Các ràng buộc E6-EVID-001/002, Cost và O-02/O-03 giữ nguyên. [Kết quả và manifest](chon-mon-order/validation/case-review-report.md).

## Đối chiếu fixture E6 — 12/11/2026

DOCUMENT_CLARIFIED: đọc4/4file fixture (README +3JSON), đối chiếu phạm vi áp dụng cho22/22ca gốc/hệ thống; sửa README tách replay HTTP/worker, reset từng fault và evidence producer/read. Không cần sửa3JSON số học/oracle; không thêm ca hoặc seed runtime.40/78feature nháp (51,3%),17/19E6 có điều kiện (89,5%),19/19RTM;99mô tả ca overlap,0backend. Gốc2NOT RUN/8BLOCKED; hệ thống5NOT RUN/7BLOCKED;57ca29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED.14/14CG OPEN,0/14CG và0/8RVđóng.34/34DTO,19/19UC và22/22ca đã rà từ trước; phiên này chỉ kiểm ánh xạ fixture. Status/Actual/Evidence, E6-EVID-001/002, Cost và O-02/O-03 giữ nguyên.

[Báo cáo phiên fixture](chon-mon-order/validation/fixture-review-report.md).

## Đề xuất chờ người dùng duyệt — 12/11/2026

DOCUMENT_CLARIFIED: theo yêu cầu mới, đã bổ sung phương án khuyến nghị, lựa chọn khác và tác động trong [sổ CG duy nhất](chon-mon-order/review/contract-gap-register.md), mục “Đề xuất trình người dùng duyệt”. Chưa có phương án được duyệt; không thay API/schema/UC/ca/fixture/wireframe. CG02/03 và ba nội dung E6-EVID-002 giữ mở, không hỏi lại. Ưu tiên duyệt hướng CG01/08/05/06 rồi từng phần CG12; CG04/07/09/10/11 cần review kỹ thuật tiếp. Giữ 40/78 feature nháp, 17/19 E6 có điều kiện, 19/19 RTM, 99 mô tả ca overlap, 0 backend; 14/14 CG OPEN, 0/14 CG và 0/8 RV đóng.


## Mốc hiện hành — mở gói BA nháp E7, 12/11/2026

Theo xác nhận người dùng 12/11/2026, mở **chỉ E7**; chỉ dẫn này thay phạm vi cũ “không mở E7–E13” đối với E7. E8–E13 chưa mở. E6 dừng chờ trả lời CG01/08/05/06, không hỏi lại/tự điền/đặc tả tiếp phần phụ thuộc;14/14 CG OPEN. Các mục phía trên là lịch sử và được giữ nguyên.

[Preview E7](giao-nhan-doanh-thu/preview.html) · [Bàn giao](giao-nhan-doanh-thu/review/handoff.md) · [Câu hỏi](giao-nhan-doanh-thu/review/questions.md) · [Phụ thuộc E6→E7](giao-nhan-doanh-thu/review/dependencies.md) · [Kiểm tra](giao-nhan-doanh-thu/validation/report.md).

E7 FEAT-049→053:5/5 feature có thiết kế nháp có điều kiện,0 feature chỉ gate;13 FR/UC/story,39 AC và39 ca tương ứng,8 ca hệ thống có overlap,18 endpoint đề xuất,8 màn HTML,4 sơ đồ flow/state. FEAT-053 có preflight/provenance/luồng xuất, chưa mapping cột và chưa thử nhập MISA. Q-13 CHỜ TRẢ LỜI, cột trả lời trống; nhánh phụ thuộc BLOCKED. Không coi contract E6 đã freeze.

Độ phủ tài liệu nháp **45/78≈57,7%** =23 E1–E5 +17 E6 +5 E7; tách riêng2 feature E6 gate-only O-03. Đây không phải BA được duyệt hoặc tiến độ phần mềm.65 bảng giữ nguyên;0 backend/migration/UAT. E6 vẫn99 mô tả ca overlap,0/14 CG đóng; E6-EVID-001/002, Cost/VAT/CK, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 và O-02/O-03/O-04 không đổi.


## Mốc hiện hành — gói BA nháp E8, 12/11/2026

Theo thay đổi phạm vi người dùng xác nhận12/11/2026, mở **chỉ E8**; thay chỉ dẫn lịch sử “không mở E8–E13” chỉ đối với E8. E9–E13 chưa mở. E6 CG01/08/05/06 và E7 Q-13/E7-Q01–08 giữ CHỜ TRẢ LỜI, không hỏi lại/tự điền/đặc tả tiếp phần phụ thuộc.14/14CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. Các mục phía trên là lịch sử.

[Preview E8](website-cong-khai/preview.html) · [Bàn giao](website-cong-khai/review/handoff.md) · [Câu hỏi](website-cong-khai/review/questions.md) · [Phụ thuộc](website-cong-khai/review/dependencies.md) · [Kiểm tra](website-cong-khai/validation/report.md).

E8 FEAT-054→059:6/6feature có thiết kế nháp có điều kiện (5P0; FEAT-057 P1),0E8feature chỉgate.12FR/UC/story,36AC/ca (12BLOCKED,24NOT RUN),12ca hệ thống overlap (6BLOCKED,6NOT RUN),16HTTP endpoint đề xuất +1port lead→E10 tối thiểu,9màn HTML,3state+2flow. E10 chưa mở; không có CMS/backend/migration.12câu E8-Q01–12 CHỜ TRẢ LỜI, cột trả lời trống; generation/giá public/nguồn/lead/CMS/cutover/analytics chưa được chọn hoặc freeze.

Độ phủ **thiết kế tài liệu nháp51/78≈65,4%** =23E1–E5+17E6+5E7+6E8; tách riêng2feature E6 chỉgate O-03. Không phải BA được duyệt, tiến độ phần mềm hay effort. R8 và G-Next chưa nghiệm thu; R4/DL-08/quyền tên miền chưa có bằng chứng đạt. FEAT-054/055/059 không cần dữ liệu thực đơn, nhưng đưa lên Now vẫn chờ O-04.

531file E1–E7 và PRD/roadmap bảo toàn SHA256;65bảng giữ nguyên;4file tổng quan chỉ append. Kiểm cấu trúc/liên kết/render và UI mock E8, đã xem ảnh desktop/mobile; không dùng mock PASS thay test sản phẩm.0backend/migration/UAT. Cost gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng không là VAT0%; CK%/tiền suất riêng theo đơn không giảm phải trả. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002, O-02/O-03/O-04 không đổi.


## Mốc hiện hành — gói BA nháp E9, 12/11/2026

Theo thay đổi phạm vi người dùng xác nhận 12/11/2026, chỉ mở E9; thay chỉ dẫn lịch sử “không mở E9–E13” đối với E9. E10–E13 chưa mở. E6 CG01/08/05/06, E7 Q-13/E7-Q01–08 và E8-Q01–12 giữ CHỜ TRẢ LỜI: không hỏi lại, tự điền hoặc đặc tả tiếp phần phụ thuộc. Các mục trên giữ nguyên là lịch sử.

[Preview E9](agent-dinh-duong-vien/preview.html) · [Bàn giao](agent-dinh-duong-vien/review/handoff.md) · [Câu hỏi](agent-dinh-duong-vien/review/questions.md) · [Phụ thuộc](agent-dinh-duong-vien/review/dependencies.md) · [Báo cáo kiểm](agent-dinh-duong-vien/validation/report.md).

E9 đúng FEAT-060→065: 5 P0 có thiết kế nháp có điều kiện; FEAT-063 P1 chỉ gate vì dùng FEAT-047 đang chặn O-03. Không có thuật toán gợi ý, thu/suy luận sức khỏe hoặc contract hồ sơ. 13 FR/UC/story,39 AC/ca chức năng (12 BLOCKED,27 NOT RUN),13 ca hệ thống overlap;11 HTTP endpoint và4 port đề xuất,7 màn HTML,3 state +2 flow.14 câu E9-Q01–14 để trống trả lời.

Độ phủ **thiết kế tài liệu nháp56/78≈71,8%** =51 hiện có +5 E9;3 feature gate-only FEAT-046/047/063 ghi riêng. Không phải BA được duyệt, effort hoặc tiến độ phần mềm. R5/R6/R8 chưa có bằng chứng xong; R9/G-Next chưa nghiệm thu. Nguồn E2/E4/E5/E6/E8 là nháp, không contract freeze.

Đã kiểm cấu trúc/liên kết, render5 sơ đồ/preview và116 kiểm UI mock tại1440/390/360px; đã xem7 màn desktop/mobile qua6 ảnh ghép. Bằng chứng và kết quả cuối ở báo cáo E9. Toàn bộ E1–E8 +PRD/roadmap được đối chiếu SHA256 với baseline trước viết; schema65 bảng không đổi;4 file tổng quan chỉ append. Mọi ca sản phẩm NOT RUN/BLOCKED, không dùng kiểm mock thay UAT.

0 backend/migration/gọi mô hình AI; không system prompt, không chọn provider/model/quota/cap/token price. CRM E10 chỉ điểm nối tối thiểu, nơi nhận/người duyệt còn chờ. FEAT-061 luôn kiểm lại máy E2 sau chỉnh; FEAT-062 chỉ đề xuất chờ người thật; FEAT-065 chặn quyền/công cụ/DB và projection, không chỉ prompt.

14/14 CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04, AIO-Q01–06 không đóng. Cost nguyên liệu gồm VAT phải trả NCC; không yêu cầu hóa đơn là cờ riêng, không VAT0%; CK%/tiền suất khoản riêng theo đơn, không giảm phải trả. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 không đổi.


## Mốc hiện hành — chỉnh diễn đạt UC E7–E9, 12/11/2026

Đã viết lại 38/38 UC (E7: 13/13; E8: 12/12; E9: 13/13), làm rõ actor, trigger, điều kiện, bước xử lý và ngoại lệ; sửa số dính chữ trong phạm vi được phép và viết lại 3 handoff. Đây chỉ là phiên chỉnh diễn đạt, không thêm phạm vi. Độ phủ giữ 56/78 ≈ 71,8%; số FR/AC/ca/endpoint/màn/sơ đồ và Status/Actual/Evidence giữ nguyên. FEAT-063 vẫn chỉ gate; không mở E10–E13.

Mọi câu hỏi mở giữ nguyên, cột trả lời để trống: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05; CK-Q01–10/DATA-COST-Q01–06; AIO-Q01–06/NUTR-Q01–04. Không backend, migration, gọi mô hình AI, thay PRD/roadmap hoặc schema 65 bảng.

[Báo cáo phiên và giới hạn kiểm](review-sessions/uc-refresh-2026-11-12/report.md): kiểm bảo toàn/truy vết/liên kết/UC đạt; check-e7.cjs đạt. Kiểm số dính chữ còn báo lỗi trong report.md lịch sử của ba gói vì các file đó bị cấm sửa. Không chạy check-e8.cjs/check-e9.cjs: chúng khóa hash các gói trước khi chỉnh; dùng checker phiên, không ghi đè kết quả lịch sử.


## Mốc hiện hành — gói BA nháp E10, 12/11/2026

Theo yêu cầu người dùng ngày 12/11/2026, chỉ mở tài liệu E10 — CRM và bán hàng cho FEAT-070–073, đều P1. Chỉ dẫn lịch sử “E10–E13 chưa mở” được thay đối với E10; E11–E13 vẫn chưa mở. FEAT-084 không có đặc tả hoặc công cụ AI mới. Các mục phía trên giữ nguyên là lịch sử.

[Preview E10](crm-ban-hang/preview.html) · [Bàn giao](crm-ban-hang/review/handoff.md) · [Câu hỏi](crm-ban-hang/review/questions.md) · [Phụ thuộc](crm-ban-hang/review/dependencies.md) · [Báo cáo kiểm](crm-ban-hang/validation/report.md).

E10 có 4/4 feature thiết kế nháp có điều kiện, 0 feature chỉ gate; 16 FR tương ứng 16 UC và 16 story; 48 AC tương ứng 48 ca chức năng (21 BLOCKED, 27 NOT RUN). 10 ca hệ thống có overlap (5 BLOCKED, 5 NOT RUN), không cộng vào tỷ lệ nghiệm thu. 23 HTTP endpoint và 7 port logic đề xuất; 9 màn trong một HTML, 4 sơ đồ trạng thái và 2 sơ đồ luồng đã render SVG/HTML. 15 câu E10-Q01–15 giữ CHỜ TRẢ LỜI, cột trả lời trống.

Độ phủ **thiết kế tài liệu nháp 60/78 ≈ 76,9%** = 23 E1–E5 + 17 E6 + 5 E7 + 6 E8 + 5 E9 + 4 E10. Ba feature chỉ gate FEAT-046/047/063 ghi riêng, không tính vào độ phủ. Đây không phải BA được duyệt, công sức hoặc tiến độ phần mềm. Mở tài liệu E10 không miễn G-Next; R10 chưa nghiệm thu. Nguồn E1–E9 vẫn nháp, không cố định hợp đồng giao tiếp.

Hồ sơ 360° ghi trạng thái thiếu nguồn riêng; không tự tính doanh thu từ số giao. Tiêu chí phát hiện trùng chưa chọn; gộp phải có người duyệt và hoàn tác có lịch sử. Vòng đời/nguy cơ rời theo lịch từng điểm, chưa đặt ngưỡng. Báo giá có phiên bản, bản khách không chứa cost hoặc biên lợi nhuận. Hợp đồng/phụ lục có giá theo loại suất, khoảng hiệu lực không chồng, không ghi đè pricing snapshot lịch sử.

Baseline chụp toàn bộ 763 file cũ trước khi viết E10; mọi file cũ ngoài hai tổng quan này được yêu cầu giữ nguyên SHA256. Hai tổng quan chỉ append, giữ nguyên byte prefix cũ; kết quả cuối tại báo cáo kiểm. PRD/roadmap không sửa hoặc append vì E9 không append hai file đó. Schema 65 bảng giữ nguyên; dữ liệu mới chỉ đề xuất. Đã kiểm cấu trúc/truy vết/liên kết, render và UI mock ở 1440, 390, 360 px; kiểm mock không thay test sản phẩm.

Các câu vẫn chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04. Không hỏi lại hoặc tự trả lời, không đặc tả tiếp producer đang chờ. E8-Q06 và E9-Q06 vẫn chặn bàn giao lead/đề xuất thật; E10 không tự được coi là đầu nhận đã duyệt.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không VAT 0%. CK% và tiền suất riêng theo đơn không giảm số phải trả nhà cung cấp; không tự khấu trừ số khách phải trả. NFR-COST-002 giữ nguyên. Không backend, migration, gọi mô hình AI hoặc UAT; không commit hoặc xóa file.
