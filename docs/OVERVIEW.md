# Tổng quan tiến độ tài liệu Gia Phát

Phiên bản: 0.9.0 · Ngày: 11/11/2026 · Trạng thái: Draft.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.9.0 | 2026-11-11 | BA | Bổ sung BA nền tảng/API MENU,86ca rule nháp,12màn HTML,preview/dashboard; khởi đầu E6; chưa backend |
| 0.8.0 | 2026-11-11 | BA | Thêm gói BA nháp E4/E5: 11 FR/story, 13 API, 6 wireframe ASCII, 60 ca thiết kế; schema65 bảng; chưa backend |
| 0.7.0 | 2026-11-11 | BA | Đồng bộ thiết kế kế toán,61 bảng,8 API bổ sung,4 màn,6 story; thống nhất tiêu chí và đặt câu hỏi dữ liệu thật |
| 0.6.0 | 2026-11-11 | BA | Xác nhận một phần nghiệp vụ VAT/chiết khấu; bổ sung CR, hướng dẫn kế toán và12 ca mới, chưa triển khai backend |
| 0.5.0 | 2026-11-11 | BA | Thêm gói review32 điểm mở, phiếu kế toán và20 mẫu số học; không có quyết định hoặc test backend mới |
| 0.4.0 | 2026-11-11 | BA | Thêm 28 story và 108 AC/test Cost; 62 chưa chạy, 46 cần đầu vào; không tăng tiến độ phần mềm |
| 0.3.0 | 2026-11-11 | BA | Bổ sung 37 endpoint API đề xuất và wireframe 18 màn Cost đã kiểm tra |
| 0.2.0 | 2026-11-11 | BA | Thêm 16 use case, user flow và ma trận truy vết Cost; ghi rõ câu hỏi review, chưa nghiệm thu nghiệp vụ |
| 0.1.0 | 2026-11-11 | BA | Ghi nhận đợt đồng bộ thiết kế Cost; phân biệt tài liệu với phần mềm đã triển khai |

## Tình trạng hiện tại

Phạm vi theo [PRD](gia-phat/01-prd.md) và [roadmap](gia-phat/02-roadmap.md): 78 tính năng, trong đó MVP nội bộ gồm 23 tính năng. Năm epic MVP đã có SRS nháp: nền tảng (5 tính năng), thực đơn (8), Cost (5), Dinh dưỡng (2), Agent Nội bộ (3). Bao phủ SRS nháp là 23/78 ≈ 29% toàn sản phẩm, 23/23 = 100% MVP; **không phải mức hoàn thành phát triển, phê duyệt nghiệp vụ hoặc nghiệm thu**. E4/E5 còn các câu hỏi và cổng dữ liệu cần xác nhận.

| Nhóm | Kết quả có trên workspace | Việc còn lại |
| :--- | :--- | :--- |
| Tổng quan | Kế hoạch, BRD, URD, PRD, roadmap nháp | Chốt điểm mở, duyệt phạm vi, ước lượng công sức và lịch |
| E1: Nền tảng | [SRS v0.2.1](nen-tang/srs/spec.md); [ERD v0.5.0](nen-tang/srs/erd.md); [DBML v0.5.0](nen-tang/srs/schema.dbml) | Duyệt thiết kế, đặc tả triển khai và migration |
| E2: Thực đơn | [SRS v0.3.3](thuc-don-dinh-luong/srs/spec.md), 13 use case, flow, backlog/AC, test case; wireframe soạn tuần có cost theo cơ sở | DL-01 và các điểm mở; phần test quy tắc chưa đầy đủ; chưa chạy test phần mềm |
| E3: Cost | [Epic v0.6.0](cost/epic-spec.md), [SRS v0.3.2](cost/srs/spec.md); **9/9 mục đồng bộ phụ thuộc đã xử lý**; [16 use case và ma trận FR](cost/srs/usecase-diagram.md); [user flow](cost/ui/user-flow.md) ; [API 37 endpoint](cost/api/api-spec.md); [wireframe 18 màn](cost/html-wireframe/cost-workbench.html) ; [28 story](cost/userstories/backlog.md), [108 AC/test](cost/test/test-cases.md) | BA/QA review, chốt điểm mở, có môi trường và dữ liệu kế toán để chạy test |
| E4: Dinh dưỡng | [SRS](dinh-duong/srs/spec.md), 5 UC/story, ERD, 7 API, 3 wireframe ASCII, 28 ca thiết kế | NUTR-Q01–04, DATA-NUTR-Q01; chưa dữ liệu đối soát 5 suất hoặc backend |
| E5: Agent Nội bộ | [SRS](agent-noi-bo/srs/spec.md), 6 UC/story, ERD, 6 API, 3 wireframe ASCII, 32 ca thiết kế | AIO-Q01–06, O-04, baseline thời gian và 20 yêu cầu thử; chưa model/backend |
| E6: Chọn món/order | [Gói review v0.2](chon-mon-order/preview.html):19UC,57AC,26endpoint,13màn,RTM | 17capability có điều kiện;2gate O-03; ORD-Q01–15 chờ; chưa backend |
| E7–E13 | Có phạm vi trong PRD/roadmap | Chưa có SRS riêng trong workspace |

## Đợt đồng bộ Cost ngày 11/11/2026

- Thêm 11 bảng, tổng miền Cost 15 bảng; toàn schema 57 bảng. Bản chụp duyệt và kết quả tính lại tách biệt; mỗi ngày/cơ sở/vòng duyệt có bản riêng.
- Dự toán có phiên bản, số suất theo món, phân rã công thức và khoản khoán đã chụp. Một cảnh báo/ngày có nhiều chi tiết cơ sở.
- Thêm 6 tham số Cost và đồng bộ quy tắc duyệt tham số. VAT và các lựa chọn nghiệp vụ vẫn chờ xác nhận.
- Wireframe có cost theo ngày/cơ sở, trạng thái thiếu giá/VAT, chưa đủ món, quyền xem, cảnh báo/chặn; dữ liệu minh hoạ.
- Kiểm cú pháp DBML và xuất MySQL đạt; kiểm tương tác wireframe desktop/mobile đạt. Chưa chạy migration, chưa có API hay engine cost production.

Xem [báo cáo kiểm tra](cost/validation/report.md). Các điểm phát hiện mới E3-Q14–Q16 nằm tại [SRS Cost mục 4.5](cost/srs/spec.md).

## Thứ tự tiếp theo

1. Review [use case và user flow Cost](cost/ui/user-flow.md), ưu tiên câu hỏi về giá đổi lúc chờ duyệt, dự toán tuần và quyền đọc khoản khoán. Báo cáo kiểm tra: [use case/flow](cost/validation/usecase-report.md).
2. Chốt O-01, E3-Q1/Q2/Q4 và E3-Q14–Q16 với người phụ trách được nêu trong SRS.
3. Review [backlog/AC và bộ test Cost](cost/validation/backlog-report.md), ưu tiên QA-COST-Q01 và các ca BLOCKED; Tech lead review API/migration, QA chuẩn bị môi trường chạy.
4. Review [gói BA E4/E5](gia-phat/review/mvp-e4-e5-handoff.md); chốt nguồn/công thức dinh dưỡng và điều kiện agent trả nháp đạt; chuẩn bị dữ liệu R4/R5, chưa chuyển thành kết quả nghiệm thu.

## Đợt backlog và kiểm thử Cost

Đã viết 28 story, 108 cặp AC/test, truy vết 43 FR có luồng; 2 FR hoãn giữ riêng. Phủ bằng kịch bản 24 BR dữ liệu/tính toán, 14 lỗi SRS, 6 lỗi API đề xuất và 8 NFR. 62 ca NOT RUN, 46 ca BLOCKED; **chưa chạy test chức năng backend**. [Báo cáo](cost/validation/backlog-report.md) và [RTM](cost/test/traceability.md).

## Gói review Cost đã chuẩn bị

[Gói bàn giao](cost/review/handoff.md) gồm [32 điểm mở](cost/review/decision-register.md), [46 ca cần đầu vào](cost/review/blocked-tests.md), [phiếu dữ liệu kế toán](cost/review/accountant-input.md) và [10 món/10 ngày giả định](cost/test/fixtures/README.md). Kiểm số học mẫu đạt bằng Decimal; chưa có dữ liệu thực tế, quyết định được ký hoặc test backend mới. [Rà soát khoảng trống](cost/gap-analysis.md).

## Nghiệp vụ kế toán đã làm rõ

[Quy tắc](cost/accounting/business-rules.md): cost nguyên liệu gồm VAT phải trả; không yêu cầu hóa đơn là cờ riêng; chiết khấu khách theo% hoặc tiền/suất được ghi riêng theo đơn, không giảm tiền phải trả. [Hướng dẫn](cost/user-guide.md), [CR tác động](cost/cr/CR-COST-2026-001.md) và [12 ca bổ sung](cost/accounting/acceptance.md). Chi tiết thuế suất/cơ sở%/thanh toán chiết khấu còn mở; đã có thiết kế API/schema/UI mở rộng liên kết ở mục dưới; chưa có test backend.

## Đồng bộ thiết kế kế toán và rà bàn giao

[API extension8 giao tiếp](cost/api/accounting-contract.md), PriceInput v0.2 cho37 endpoint Cost hiện có; [4 bảng mới trong tổng61 bảng](nen-tang/srs/erd.md); [4 màn kế toán](cost/html-wireframe/accounting-workbench.html); [6 story/18 ca thiết kế](cost/userstories/accounting-backlog.md). Các bộ ca12 nghiệp vụ/18 thiết kế có thể kiểm cùng mục tiêu, không cộng thành phần trăm nghiệm thu.

Epic/roadmap đã theo NFR-COST-002 thay cho1% cũ; điều kiện CHAN/CANH_BAO được đồng bộ. [Báo cáo](cost/validation/accounting-design-report.md) phân biệt phần tự rà đạt với phần chờ stakeholder. Dữ liệu10 món/10 ngày chưa có theo xác nhận người dùng, câu hỏi đặt tại [phiếu kế toán](cost/review/accountant-input.md). [Nhánh Cost](cost/review/cost-branch-decisions.md) và10 câu CK còn chờ xác nhận, không tự đóng.

## Gói BA Dinh dưỡng và Agent Nội bộ ngày 11/11/2026

[Gói review](gia-phat/review/mvp-e4-e5-handoff.md) liên kết SRS, use case, flow, ERD/từ điển, API, wireframe ASCII, backlog, AC, test và RTM của hai phân hệ. 11 FR/11 story, 33 AC; tổng60 ca thiết kế (33 chức năng,19 lỗi hợp đồng,8 NFR), chưa chạy backend. Có11 câu hỏi mới chờ xác nhận. Schema tổng65 bảng;61 bảng trong báo cáo kế toán là mốc lịch sử, không phải số hiện hành. Không thay các quy tắc VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06 hoặc NFR-COST-002.

Dinh dưỡng kế thừa công thức khung từ ERD nhưng phải chốt ý nghĩa định lượng sống/phần ăn được và dung sai R4. Agent gọi bộ kiểm MENU/COST; đề xuất không trả VALID khi vượt cost, kể cả CANH_BAO, chờ AIO-Q02. Không tự đổi cổng duyệt MENU. Wireframe ASCII là phác thảo tài liệu, chưa kiểm UI chạy thật.

## Bổ sung BA E1–E5 và khởi đầu E6

[Bàn giao](gia-phat/review/ba-completion-handoff.md) · [Dashboard](project-dashboard.md) · [Kiểm tra](gia-phat/validation/completion-report.md).

- E1 bổ sung26UC/story,78AC,25HTTP endpoint và port nội bộ; bộ test BR/ERR/NFR,flow/state/gap và6màn HTML. Còn E1-Q01–05, N/O gốc.
- E2 bổ sung60endpoint thiết kế,API traceability,ERD miền,86ca rule nháp;54/55FR có story/test liên kết,FR-MENU-RCP-007 vẫn chờO-02. DL-01 chưa được duyệt.
- E3 giữ thiết kế đã có, thêm sequence/state/chỉ mụcERD và preview; không thay CK/DATA-COST hoặc công thức.
- E4/E5 bổ sung epic,sơ đồ/checklist/gap và6màn HTML; vẫn giữ11câu hỏi nghiệp vụ. Wireframe mô phỏng không gọiAI hoặc backend.
- Có5trang preview nhúng tài liệu/sơ đồ: [E1](nen-tang/preview.html), [E2](thuc-don-dinh-luong/preview.html), [E3](cost/preview.html), [E4](dinh-duong/preview.html), [E5](agent-noi-bo/preview.html).

E6 đã bắt đầu soạn tài liệu, chưa tăng số tính năng được coi là đặc tả đầy đủ. Schema tổng vẫn65bảng; deltaE6 chưa merge. Phần mềm/migration/UAT vẫn chưa triển khai trong workspace này. Thứ tự tiếp theo: review điểm mở/gap E1–E5 và tiếp tục UC/API/UI/AC/RTM E6 theo phần đủ căn cứ.

## Hoàn thiện gói E6 để review ngày 11/11/2026

[Preview E6](chon-mon-order/preview.html) · [Báo cáo kiểm tra](chon-mon-order/validation/report.md) · [Bàn giao](chon-mon-order/review/handoff.md). Đã bổ sung19UC,57AC,26HTTP endpoint,2port,13màn vàRTM19feature. Giữ10ca gốc, thêm57ca theoAC và12ca hệ thống; không cộng thành79 mục tiêu độc lập. 17capability có thiết kế có điều kiện,2feature chỉgate O-03. ORD-Q01–10 không đóng, bổ sung ORD-Q11–15; schema65bảng không thay. Chưa backend/migration/UAT. Các mục “E6 khởi đầu” phía trên là mốc lịch sử, không phản ánh inventory hiện tại. Tiếp theo review E6 trước mở E7–E13.

## Review quyết định E6 ngày 11/11/2026

[DR-01–04](chon-mon-order/review/decision-review.md) đã rà identity/scope, số suất, khóa hạn và kế hoạch. Có xác nhận đầu vào danh sách/người quản lý, chưa chốt cơ chế identity. 8phát hiện; sửa các mâu thuẫn tài liệu có căn cứ, bổ sung8ca review riêng. Chưa freeze schema/API, chưa backend; không mở E7–E13. [Kết quả kiểm](chon-mon-order/validation/decision-review-report.md).

## Bổ sung E6 độc lập ngày 11/11/2026

[Bàn giao bổ sung E6 độc lập](chon-mon-order/review/independent-handoff.md) cập nhật consistency, khóa/plan và dependency Nền tảng; thêm12ca invariant NOT RUN cùng fixture synthetic. Tổng99mô tả ca có overlap, không99mục tiêu độc lập;40/78feature có thiết kế nháp,17/19capability E6 có điều kiện; chưa backend/migration/UAT.


## Mốc hiện hành: mở gói BA nháp E7, 12/11/2026

Theo xác nhận người dùng 12/11/2026, mở **chỉ E7**; chỉ dẫn này thay phạm vi cũ “không mở E7–E13” đối với E7. E8–E13 chưa mở. E6 dừng chờ trả lời CG01/08/05/06, không hỏi lại/tự điền/đặc tả tiếp phần phụ thuộc;14/14 CG OPEN. Các mục phía trên là lịch sử và được giữ nguyên.

[Preview E7](giao-nhan-doanh-thu/preview.html) · [Bàn giao](giao-nhan-doanh-thu/review/handoff.md) · [Câu hỏi](giao-nhan-doanh-thu/review/questions.md) · [Phụ thuộc E6→E7](giao-nhan-doanh-thu/review/dependencies.md) · [Kiểm tra](giao-nhan-doanh-thu/validation/report.md).

E7 FEAT-049→053:5/5 feature có thiết kế nháp có điều kiện,0 feature chỉ gate;13 FR/UC/story,39 AC và39 ca tương ứng,8 ca hệ thống có overlap,18 endpoint đề xuất,8 màn HTML,4 sơ đồ flow/state. FEAT-053 có preflight/provenance/luồng xuất, chưa mapping cột và chưa thử nhập MISA. Q-13 CHỜ TRẢ LỜI, cột trả lời trống; nhánh phụ thuộc BLOCKED. Không coi contract E6 đã freeze.

Độ phủ tài liệu nháp **45/78≈57,7%** =23 E1–E5 +17 E6 +5 E7; tách riêng2 feature E6 gate-only O-03. Đây không phải BA được duyệt hoặc tiến độ phần mềm.65 bảng giữ nguyên;0 backend/migration/UAT. E6 vẫn99 mô tả ca overlap,0/14 CG đóng; E6-EVID-001/002, Cost/VAT/CK, CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 và O-02/O-03/O-04 không đổi.


## Mốc hiện hành: gói BA nháp E8, 12/11/2026

Theo thay đổi phạm vi người dùng xác nhận12/11/2026, mở **chỉ E8**; thay chỉ dẫn lịch sử “không mở E8–E13” chỉ đối với E8. E9–E13 chưa mở. E6 CG01/08/05/06 và E7 Q-13/E7-Q01–08 giữ CHỜ TRẢ LỜI, không hỏi lại/tự điền/đặc tả tiếp phần phụ thuộc.14/14CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. Các mục phía trên là lịch sử.

[Preview E8](website-cong-khai/preview.html) · [Bàn giao](website-cong-khai/review/handoff.md) · [Câu hỏi](website-cong-khai/review/questions.md) · [Phụ thuộc](website-cong-khai/review/dependencies.md) · [Kiểm tra](website-cong-khai/validation/report.md).

E8 FEAT-054→059:6/6feature có thiết kế nháp có điều kiện (5P0; FEAT-057 P1),0E8feature chỉgate.12FR/UC/story,36AC/ca (12BLOCKED,24NOT RUN),12ca hệ thống overlap (6BLOCKED,6NOT RUN),16HTTP endpoint đề xuất +1port lead→E10 tối thiểu,9màn HTML,3state+2flow. E10 chưa mở; không có CMS/backend/migration.12câu E8-Q01–12 CHỜ TRẢ LỜI, cột trả lời trống; generation/giá public/nguồn/lead/CMS/cutover/analytics chưa được chọn hoặc freeze.

Độ phủ **thiết kế tài liệu nháp51/78≈65,4%** =23E1–E5+17E6+5E7+6E8; tách riêng2feature E6 chỉgate O-03. Không phải BA được duyệt, tiến độ phần mềm hay effort. R8 và G-Next chưa nghiệm thu; R4/DL-08/quyền tên miền chưa có bằng chứng đạt. FEAT-054/055/059 không cần dữ liệu thực đơn, nhưng đưa lên Now vẫn chờ O-04.

531file E1–E7 và PRD/roadmap bảo toàn SHA256;65bảng giữ nguyên;4file tổng quan chỉ append. Kiểm cấu trúc/liên kết/render và UI mock E8, đã xem ảnh desktop/mobile; không dùng mock PASS thay test sản phẩm.0backend/migration/UAT. Cost gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng không là VAT0%; CK%/tiền suất riêng theo đơn không giảm phải trả. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002, O-02/O-03/O-04 không đổi.


## Mốc hiện hành: gói BA nháp E9, 12/11/2026

Theo thay đổi phạm vi người dùng xác nhận 12/11/2026, chỉ mở E9; thay chỉ dẫn lịch sử “không mở E9–E13” đối với E9. E10–E13 chưa mở. E6 CG01/08/05/06, E7 Q-13/E7-Q01–08 và E8-Q01–12 giữ CHỜ TRẢ LỜI: không hỏi lại, tự điền hoặc đặc tả tiếp phần phụ thuộc. Các mục trên giữ nguyên là lịch sử.

[Preview E9](agent-dinh-duong-vien/preview.html) · [Bàn giao](agent-dinh-duong-vien/review/handoff.md) · [Câu hỏi](agent-dinh-duong-vien/review/questions.md) · [Phụ thuộc](agent-dinh-duong-vien/review/dependencies.md) · [Báo cáo kiểm](agent-dinh-duong-vien/validation/report.md).

E9 đúng FEAT-060→065: 5 P0 có thiết kế nháp có điều kiện; FEAT-063 P1 chỉ gate vì dùng FEAT-047 đang chặn O-03. Không có thuật toán gợi ý, thu/suy luận sức khỏe hoặc contract hồ sơ. 13 FR/UC/story,39 AC/ca chức năng (12 BLOCKED,27 NOT RUN),13 ca hệ thống overlap;11 HTTP endpoint và4 port đề xuất,7 màn HTML,3 state +2 flow.14 câu E9-Q01–14 để trống trả lời.

Độ phủ **thiết kế tài liệu nháp56/78≈71,8%** =51 hiện có +5 E9;3 feature gate-only FEAT-046/047/063 ghi riêng. Không phải BA được duyệt, effort hoặc tiến độ phần mềm. R5/R6/R8 chưa có bằng chứng xong; R9/G-Next chưa nghiệm thu. Nguồn E2/E4/E5/E6/E8 là nháp, không contract freeze.

Đã kiểm cấu trúc/liên kết, render5 sơ đồ/preview và116 kiểm UI mock tại1440/390/360px; đã xem7 màn desktop/mobile qua6 ảnh ghép. Bằng chứng và kết quả cuối ở báo cáo E9. Toàn bộ E1–E8 +PRD/roadmap được đối chiếu SHA256 với baseline trước viết; schema65 bảng không đổi;4 file tổng quan chỉ append. Mọi ca sản phẩm NOT RUN/BLOCKED, không dùng kiểm mock thay UAT.

0 backend/migration/gọi mô hình AI; không system prompt, không chọn provider/model/quota/cap/token price. CRM E10 chỉ điểm nối tối thiểu, nơi nhận/người duyệt còn chờ. FEAT-061 luôn kiểm lại máy E2 sau chỉnh; FEAT-062 chỉ đề xuất chờ người thật; FEAT-065 chặn quyền/công cụ/DB và projection, không chỉ prompt.

14/14 CG E6 OPEN; E6-EVID-001/002 còn hiệu lực. O-02/O-03/O-04, AIO-Q01–06 không đóng. Cost nguyên liệu gồm VAT phải trả NCC; không yêu cầu hóa đơn là cờ riêng, không VAT0%; CK%/tiền suất khoản riêng theo đơn, không giảm phải trả. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002 không đổi.


## Mốc hiện hành: chỉnh diễn đạt UC E7–E9, 12/11/2026

Đã viết lại 38/38 UC (E7: 13/13; E8: 12/12; E9: 13/13), làm rõ actor, trigger, điều kiện, bước xử lý và ngoại lệ; sửa số dính chữ trong phạm vi được phép và viết lại 3 handoff. Đây chỉ là phiên chỉnh diễn đạt, không thêm phạm vi. Độ phủ giữ 56/78 ≈ 71,8%; số FR/AC/ca/endpoint/màn/sơ đồ và Status/Actual/Evidence giữ nguyên. FEAT-063 vẫn chỉ gate; không mở E10–E13.

Mọi câu hỏi mở giữ nguyên, cột trả lời để trống: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05; CK-Q01–10/DATA-COST-Q01–06; AIO-Q01–06/NUTR-Q01–04. Không backend, migration, gọi mô hình AI, thay PRD/roadmap hoặc schema 65 bảng.


## Mốc hiện hành: gói BA nháp E10, 12/11/2026

Theo yêu cầu người dùng ngày 12/11/2026, chỉ mở tài liệu E10: CRM và bán hàng cho FEAT-070–073, đều P1. Chỉ dẫn lịch sử “E10–E13 chưa mở” được thay đối với E10; E11–E13 vẫn chưa mở. FEAT-084 không có đặc tả hoặc công cụ AI mới. Các mục phía trên giữ nguyên là lịch sử.

[Preview E10](crm-ban-hang/preview.html) · [Bàn giao](crm-ban-hang/review/handoff.md) · [Câu hỏi](crm-ban-hang/review/questions.md) · [Phụ thuộc](crm-ban-hang/review/dependencies.md) · [Báo cáo kiểm](crm-ban-hang/validation/report.md).

E10 có 4/4 feature thiết kế nháp có điều kiện, 0 feature chỉ gate; 16 FR tương ứng 16 UC và 16 story; 48 AC tương ứng 48 ca chức năng (21 BLOCKED, 27 NOT RUN). 10 ca hệ thống có overlap (5 BLOCKED, 5 NOT RUN), không cộng vào tỷ lệ nghiệm thu. 23 HTTP endpoint và 7 port logic đề xuất; 9 màn trong một HTML, 4 sơ đồ trạng thái và 2 sơ đồ luồng đã render SVG/HTML. 15 câu E10-Q01–15 giữ CHỜ TRẢ LỜI, cột trả lời trống.

Độ phủ **thiết kế tài liệu nháp 60/78 ≈ 76,9%** = 23 E1–E5 + 17 E6 + 5 E7 + 6 E8 + 5 E9 + 4 E10. Ba feature chỉ gate FEAT-046/047/063 ghi riêng, không tính vào độ phủ. Đây không phải BA được duyệt, công sức hoặc tiến độ phần mềm. Mở tài liệu E10 không miễn G-Next; R10 chưa nghiệm thu. Nguồn E1–E9 vẫn nháp, không cố định hợp đồng giao tiếp.

Hồ sơ 360° ghi trạng thái thiếu nguồn riêng; không tự tính doanh thu từ số giao. Tiêu chí phát hiện trùng chưa chọn; gộp phải có người duyệt và hoàn tác có lịch sử. Vòng đời/nguy cơ rời theo lịch từng điểm, chưa đặt ngưỡng. Báo giá có phiên bản, bản khách không chứa cost hoặc biên lợi nhuận. Hợp đồng/phụ lục có giá theo loại suất, khoảng hiệu lực không chồng, không ghi đè pricing snapshot lịch sử.

Baseline chụp toàn bộ 763 file cũ trước khi viết E10; mọi file cũ ngoài hai tổng quan này được yêu cầu giữ nguyên SHA256. Hai tổng quan chỉ append, giữ nguyên byte prefix cũ; kết quả cuối tại báo cáo kiểm. PRD/roadmap không sửa hoặc append vì E9 không append hai file đó. Schema 65 bảng giữ nguyên; dữ liệu mới chỉ đề xuất. Đã kiểm cấu trúc/truy vết/liên kết, render và UI mock ở 1440, 390, 360 px; kiểm mock không thay test sản phẩm.

Các câu vẫn chờ: E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13, E7-Q01–08; E8-Q01–12; E9-Q01–14; O-01 đến O-05 và O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04. Không hỏi lại hoặc tự trả lời, không đặc tả tiếp producer đang chờ. E8-Q06 và E9-Q06 vẫn chặn bàn giao lead/đề xuất thật; E10 không tự được coi là đầu nhận đã duyệt.

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; cờ không yêu cầu hóa đơn là cờ riêng, không VAT 0%. CK% và tiền suất riêng theo đơn không giảm số phải trả nhà cung cấp; không tự khấu trừ số khách phải trả. NFR-COST-002 giữ nguyên. Không backend, migration, gọi mô hình AI hoặc UAT; không commit hoặc xóa file.


## Mốc hiện hành: gói BA nháp E11, 12/11/2026

Theo yêu cầu người dùng, chỉ mở tài liệu E11: Mua hàng và sản xuất cho FEAT-074–078, đều P1. Chỉ dẫn lịch sử “E11–E13 chưa mở” được thay riêng đối với E11; E12/E13 chưa mở. Không đặc tả FEAT-082/083. Các mục phía trên giữ nguyên byte và là lịch sử.

[Preview E11](mua-hang-san-xuat/preview.html) · [Bàn giao](mua-hang-san-xuat/review/handoff.md) · [Câu hỏi](mua-hang-san-xuat/review/questions.md) · [Phụ thuộc](mua-hang-san-xuat/review/dependencies.md) · [Báo cáo kiểm](mua-hang-san-xuat/validation/report.md).

5/5 feature có thiết kế nháp có điều kiện, 0 feature E11 chỉ gate. 15 FR / 15 UC / 15 story; 45 AC và 45 ca chức năng (13 BLOCKED, 32 NOT RUN); 10 ca hệ thống có overlap (5 BLOCKED, 5 NOT RUN). 15 HTTP endpoint và 4 port ranh giới đề xuất; 9 màn HTML, 5 state và 2 flow. 15 câu E11-Q01–15 có cột Trả lời trống. Mọi ca sản phẩm NOT RUN hoặc BLOCKED, Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (60 + 5) / 78 = 65/78 ≈ 83,3 %**. Ba feature chỉ gate FEAT-046/047/063 ghi riêng. Đây không phải BA được duyệt hoặc tiến độ phần mềm; R11/G-Next chưa nghiệm thu. R11 giữ mục tiêu BO-02: chênh lệch cost thực mua so với dự toán ≤ 3 điểm phần trăm theo ngày/cơ sở; 100% bữa có mẫu lưu. Cách đo và chính sách mẫu còn chờ.

E2 cung cấp định lượng/vai trò/dị ứng/rule và cổng duyệt; E3 cung cấp dự toán/giá gồm VAT; E6 cung cấp kế hoạch có revision nhưng CG06 còn chờ; E7 giữ giao nhận/doanh thu. Lô chỉ quản lý cho hàng đông lạnh và khô. Thay món cùng vai trò, luôn kiểm lại dị ứng, quy tắc E2 và cost E3, không bỏ cổng MENU. Không tự chọn tồn tối thiểu, người duyệt, kỳ công nợ hoặc hạn lưu mẫu.

Cost gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng, không phải VAT 0 %. CK % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả NCC và không tự khấu trừ số khách phải trả. NFR-COST-002 giữ ≤ 1 đ cho cost món và ≤ 0,01 điểm phần trăm cho cost % ngày. FR-MENU-RCP-007/O-02 và FEAT-046/047/063/O-03 vẫn chặn; không thu sức khỏe.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; O-01–O-06; CK-Q01–10; DATA-COST-Q01–06; AIO-Q01–06; NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp producer đang chờ.

Baseline gồm 873 file cũ; schema 65 bảng giữ nguyên. Chỉ hai tổng quan này được append; kết quả hash và kiểm tài liệu/UI cuối ở báo cáo E11. Không backend, migration, gọi mô hình AI, commit hoặc xóa file.


## Mốc hiện hành: gói BA nháp E12, 12/11/2026

Theo yêu cầu người dùng, chỉ mở tài liệu E12: Phản hồi và báo cáo cho FEAT-079–087: 7 P1 và 2 P2. Chỉ dẫn lịch sử “E12/E13 chưa mở” được thay riêng đối với E12; E13/FEAT-088 chưa mở. Các mục phía trên giữ nguyên byte và là lịch sử.

[Preview E12](phan-hoi-bao-cao/preview.html) · [Bàn giao](phan-hoi-bao-cao/review/handoff.md) · [Câu hỏi](phan-hoi-bao-cao/review/questions.md) · [Phụ thuộc](phan-hoi-bao-cao/review/dependencies.md) · [Báo cáo kiểm](phan-hoi-bao-cao/validation/report.md).

9/9 feature có thiết kế nháp có điều kiện, 0 feature E12 chỉ gate. 20 FR / 20 UC / 20 story; 60 AC và 60 ca chức năng (23 BLOCKED, 37 NOT RUN). Có 12 ca hệ thống và 8 ca lỗi overlap (5 BLOCKED, 15 NOT RUN); 3 dòng R12 BLOCKED. 20 HTTP endpoint đề xuất và 7 port chỉ đọc/kiểm thuần; 12 màn HTML, 5 state và 2 flow. 18 câu E12-Q01–18 có cột Trả lời trống. Mọi ca sản phẩm NOT RUN hoặc BLOCKED, Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (65 + 9) / 78 = 74/78 ≈ 94,9 %**. Ba feature FEAT-046/047/063 chỉ gate O-03 ghi riêng, không cộng tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. R12 cần R6, R7, R10, R11 xong; chưa có bằng chứng. G-Next và R12 chưa nghiệm thu.

Tỷ lệ món chỉ từ lựa chọn thật E6, mẫu số chưa chọn, không suy từ sản xuất. Dashboard bốn vai trò có catalog nguồn/công thức/mẫu số/quyền; cost % ngày giữ định nghĩa E3, cost % theo khách chờ Q08. Bốn feature AI FEAT-082–085 chỉ công cụ đọc theo quyền người dùng tại tool/DB và đề xuất nháp chờ người thật duyệt; không tự ghi nghiệp vụ. FEAT-084 chỉ nối đọc E10, không sửa E10.

FEAT-086 là mục tiêu nhóm, công thức/ngưỡng chờ NUTR-Q01–04. FEAT-087 chỉ bữa đã ăn và giá trị dinh dưỡng của suất, tự nguyện/có đồng ý/xóa được; không thu, suy luận hoặc lưu sức khỏe và không gợi ý cá nhân. Thiết kế độc lập không dùng FEAT-046/047; mở rộng sang hồ sơ/gợi ý chỉ gate O-03. Identity, bằng chứng đã ăn và retention còn chờ, không suy đã ăn từ lựa chọn/giao nhận.

Cost nguyên liệu gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất riêng theo đơn, không giảm phải trả NCC và không tự trừ tiền khách. NFR-COST-002 giữ ≤ 1 đ cho cost món và ≤ 0,01 điểm phần trăm cho cost % ngày; BO-02 ≤ 3 điểm phần trăm thuộc mục tiêu R11. FR-MENU-RCP-007/O-02 và FEAT-046/047/063/O-03 vẫn chặn.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại, tự trả lời hoặc đặc tả tiếp producer đang chờ.

Baseline chụp 945 file cũ trước viết E12; schema giữ 65 bảng. Chỉ hai tổng quan được append; kết quả bốn checker và ảnh desktop/mobile tại báo cáo E12. Không backend, migration, gọi mô hình AI, system prompt thật, chọn nhà cung cấp/model AI, commit hoặc xóa file.


## Mốc hiện hành: gói BA nháp E13, 12/11/2026

Theo yêu cầu người dùng, mở riêng tài liệu E13: Chi phí và lợi nhuận cho FEAT-088, EXP / M10, P2, PER-07/PER-08. Chỉ dẫn lịch sử “E13 chưa mở” được thay đối với E13; mọi byte trước mục này giữ nguyên là lịch sử. Đây là epic cuối theo PRD; việc tiếp theo là review/chốt câu hỏi với stakeholder trên bằng chứng, không coi các release đã nghiệm thu.

[Preview E13](chi-phi-loi-nhuan/preview.html) · [Bàn giao](chi-phi-loi-nhuan/review/handoff.md) · [Câu hỏi](chi-phi-loi-nhuan/review/questions.md) · [Phụ thuộc](chi-phi-loi-nhuan/review/dependencies.md) · [Báo cáo kiểm](chi-phi-loi-nhuan/validation/report.md).

1/1 feature có thiết kế nháp có điều kiện; 0 feature E13 chỉ gate. 12 FR / 12 UC / 12 story; 36 AC và 36 ca chức năng (16 BLOCKED, 20 NOT RUN). Có 13 ca hệ thống overlap (4 BLOCKED, 9 NOT RUN), 4 dòng R13 BLOCKED; 18 endpoint đề xuất, 5 port ranh giới; 8 màn, 5 state và 2 flow. 14 câu E13-Q01–14 có cột Trả lời trống. Mọi ca sản phẩm NOT RUN hoặc BLOCKED, Actual/Evidence trống.

Độ phủ **thiết kế tài liệu nháp (74 + 1) / 78 = 75/78 ≈ 96,2 %**. FEAT-046/047/063 chỉ gate O-03 ghi riêng, không cộng tử số. Đây không phải BA được duyệt hoặc tiến độ phần mềm. R13 cần R7, R11 xong và Giám đốc duyệt nguyên tắc phân bổ chi phí; chưa có bằng chứng, R13/G-Next chưa nghiệm thu.

Chưa chọn phương pháp phân bổ: phương pháp là dữ liệu có phiên bản/người duyệt; chưa có bản duyệt thì lợi nhuận khách BLOCKED, chỉ xem chi phí trực tiếp. Mọi báo cáo giữ phiên bản phương pháp và nguồn. Đối chiếu từng cơ sở có phần chưa phân bổ và chênh lệch riêng; cầu nối khớp khi còn phần chưa phân bổ chưa đủ R13. Không giấu phần dư vào khách nào. Doanh thu lấy E7 đã đối soát; cost nguyên liệu giữ nguồn E3/E11, không định nghĩa lại.

Chấm công chỉ phục vụ chi phí nhân công theo người/cơ sở/ca/giờ/nguồn đơn giá; không tính lương, bảo hiểm hoặc thuế TNCN. Chi tiết lương chỉ PER-07/PER-08 theo quyền tối thiểu; báo cáo khách nội bộ chỉ tổng hợp, tài liệu gửi khách không có lợi nhuận/biên lợi nhuận. Kỳ khóa không ghi đè; điều chỉnh là bút toán riêng có lý do và người duyệt, chưa chọn kỳ đích/người cụ thể.

Cost nguyên liệu gồm VAT phải trả NCC; cờ không yêu cầu hóa đơn riêng, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không giảm phải trả NCC hoặc tự giảm phải trả khách. NFR-COST-002 giữ ≤ 1 đ và ≤ 0,01 điểm phần trăm; BO-01 ≤ 52 % và BO-02 ≤ 3 điểm phần trăm là mục tiêu kinh doanh. FR-MENU-RCP-007/O-02 và FEAT-046/047/063/O-03 giữ gate.

Giữ chờ E6 CG01–14, ORD-Q01–15, E6-EVID-001/002; E7 Q-13/E7-Q01–08; E8-Q01–12; E9-Q01–14; E10-Q01–15; E11-Q01–15; E12-Q01–18; O-01–O-06; CK-Q01–10, DATA-COST-Q01–06; AIO-Q01–06, NUTR-Q01–04; DL-01; E1-Q01–05. Không hỏi lại hoặc tự đặc tả tiếp producer đang chờ.

Baseline E13 chụp 1070 file cũ, lần đối chiếu ngay sau không phát hiện thay đổi. Bốn checker và ảnh desktop/mobile tại báo cáo E13; hai tổng quan chỉ append, schema giữ 65 bảng. Không sửa bằng chứng hash lịch sử E12. Không backend, migration, gọi mô hình AI, commit hoặc xóa file.


## Mốc hiện hành: gói quyết định, 13/11/2026

Theo yêu cầu người dùng, chuẩn bị gói quyết định cho 13 epic và PRD; không mở epic hoặc viết thêm đặc tả. Các mốc phía trên giữ nguyên byte và là lịch sử.

[Đọc trong 5 phút](gia-phat/review/decision-pack/README.md) · [Sổ quyết định](gia-phat/review/decision-pack/decision-register.md) · [Nhóm quyết định](gia-phat/review/decision-pack/decision-groups.md) · [Chương trình họp](gia-phat/review/decision-pack/meeting-agenda.md) · [Rà nhất quán](gia-phat/review/decision-pack/cross-epic-consistency.md) · [Báo cáo kiểm](gia-phat/review/decision-pack/validation/report.md).

219 mã câu hỏi/gap nguồn, 197 nhóm DEC, 9 buổi họp theo vai trò. Chênh +50 so với ước tính 169 do bổ sung các câu cũ còn mở và phân biệt mã bằng chứng E6 với câu hỏi; bảng đếm từng sổ và căn cứ nằm trong báo cáo. Các cột Trả lời/Quyết định để trống; 0 câu được đóng. Các nhóm chặn MVP đều ở buổi 1–3; buổi 4 ưu tiên E6 CG01/08/05/06 rồi CG12.

Độ phủ thiết kế tài liệu nháp giữ **75/78 ≈ 96,2 %**. FEAT-046/047/063 chỉ gate O-03; không thu dữ liệu sức khỏe. Đây là gói chuẩn bị quyết định, **không phải BA được duyệt**: 0 feature được phê duyệt, 0 ca sản phẩm đã chạy. G-Now/G-Next và R1–R13 không tự được nghiệm thu.

Rà liên epic ghi 12 phát hiện cần xác nhận; không sửa nguồn. Cost gồm VAT phải trả NCC, cờ không yêu cầu hóa đơn độc lập; chiết khấu riêng theo đơn không giảm phải trả NCC hoặc tự giảm tiền khách. NFR-COST-002 giữ ≤ 1 đ và ≤ 0,01 điểm phần trăm; BO-01/BO-02 là mục tiêu kinh doanh. FR-MENU-RCP-007 giữ gate O-02.

Baseline gói chụp 1175 file cũ trong docs trước khi viết; chỉ hai tổng quan được append, schema giữ 65 bảng. Bốn sai lệch hash E12 do commit 71e2a4c đã được giải thích trong báo cáo, không khôi phục hoặc chụp lại baseline E12. Phiên sau chỉ xử lý từng DEC theo quyết định đã ký có nguồn, phân tích tác động bằng skill cr. Không backend, migration, gọi AI, commit hoặc xóa file.


## Mốc hiện hành: rà tiếp gói quyết định, 13/11/2026

Độ phủ thiết kế tài liệu nháp giữ **75/78**. **0 câu được trả lời**, 0 feature được duyệt, 0 ca sản phẩm đã chạy; đây không phải BA được duyệt. 224 mã nguồn gồm 219 câu gốc và 5 câu mới; 196 nhóm DEC. Thẩm quyền còn thiếu và 4 gate release chưa rõ đã có BA-Q; không chọn thay stakeholder. 12 XC có trạng thái, phần phụ thuộc tiếp tục BLOCKED.

[Gói quyết định](gia-phat/review/decision-pack/README.md) · [Báo cáo rà tiếp](gia-phat/review/decision-pack/followup-2026-11-13/report.md).

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.9.1 | 13/11/2026 | BA | Append mốc XC-01–12, DEC-27 và BA-Q |

Hiệu chỉnh số nhóm trong cùng mốc: rà tiêu chí một chữ ký yêu cầu tách 18 câu khỏi nhóm chủ đề cũ. Tổng hiện hành là **214 nhóm DEC**, vẫn 224 câu nguồn và 0 câu trả lời; xem bảng ánh xạ và bảng tách trong gói quyết định.


## Mốc hiện hành: đổi backend sang Rust/Axum và kiến trúc AI agent, 14/11/2026

Theo yêu cầu người dùng ngày 14/11/2026, backend đổi từ NodeJS/NestJS sang **Rust với Axum** (quyết định D-22); frontend giữ ReactJS, cơ sở dữ liệu giữ MySQL 8. Phân tích tác động và danh sách file sửa: [CR-CORE-2026-001](nen-tang/cr/CR-CORE-2026-001.md). Các mục phía trên giữ nguyên byte và là lịch sử; chỗ nào phía trên ghi NodeJS/NestJS là mốc trước CR này.

Hai tài liệu mới, trạng thái Draft: [Kiến trúc hệ thống](nen-tang/srs/architecture.md) (kiến trúc chạy, lựa chọn công nghệ, cấu trúc mã nguồn Rust và React, ánh xạ 13 epic sang crate) và [Kiến trúc AI agent](nen-tang/srs/agent-architecture.md) (agent runtime, hai bộ công cụ, hai MCP server, RAG hai chỉ mục, lan can). Ngôn ngữ backend là đã chốt; tên thư viện (SQLx, apalis, utoipa, rmcp), kho vector Qdrant và Next.js cho website công khai là đề xuất.

Đã sửa tên công nghệ trong kế hoạch tổng thể v0.3.0, BRD v0.1.1, PRD v0.1.3, hướng dẫn đọc v0.1.1, bản phân tích gốc, SRS nền tảng v0.3.0 và một câu trong SRS E2 v0.3.4, E3 v0.3.3, E4 v0.1.2. Dựng lại preview và sơ đồ E1 đến E5 bằng `render-review.cjs`: 160 tài liệu, 49 sơ đồ, 0 lỗi render; lần dựng này cũng đưa vào preview các thay đổi Markdown của những phiên trước.

Không đổi: FR, BR, ERR, NFR, use case, story, AC, test case, endpoint, wireframe; schema giữ 65 bảng. Độ phủ thiết kế tài liệu nháp giữ **75/78 ≈ 96,2 %**. **0 câu hỏi được trả lời**, 0 feature được duyệt, 0 ca sản phẩm đã chạy. Q-09, Q-12, Q-15, O-04, AIO-Q01 đến Q06, E9-Q01 đến Q14 và O-03 giữ trạng thái mở. Phát sinh một câu hỏi mới chưa có mã: ai duyệt tài liệu trước khi đưa vào kho RAG; cần đưa vào gói quyết định ở lần rà kế tiếp.

Các file bị sửa lệch hash so với baseline của những đợt trước; đây là thay đổi có chủ đích theo CR, không khôi phục và không chụp lại baseline lịch sử. Không backend, migration, gọi mô hình AI hoặc commit.

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.10.0 | 14/11/2026 | BA | Append mốc D-22, CR-CORE-2026-001 và hai tài liệu kiến trúc |
