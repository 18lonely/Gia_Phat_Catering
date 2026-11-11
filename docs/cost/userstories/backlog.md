# Backlog Cost

Phiên bản 0.1.0 · 11/11/2026 · Draft để BA/QA/Tech lead review.

Nguồn: [SRS Cost](../srs/spec.md), [16 use case](../srs/usecase-diagram.md), [API đề xuất](../api/api-spec.md), [user flow](../ui/user-flow.md).

Story Point là ước lượng sơ bộ của BA để thảo luận, chưa được đội dev cam kết; không dùng cộng điểm để suy ra tiến độ. P0/P1/P2 giữ theo SRS. Mỗi story có giá trị độc lập để review nhưng dùng nền MENU/SYS, engine và danh mục giá chung; chưa tuyên bố mọi story đủ INVEST để vào sprint.

Điều kiện đưa vào sprint: chốt điểm mở ảnh hưởng story, review hợp đồng API/migration, có fixture và người duyệt AC, đội dev ước lượng lại. Các story 5 điểm cần tách tiếp nếu vượt một sprint. Những kịch bản có oracle chưa xác định mang BLOCKED; kịch bản xác định theo SRS vẫn chỉ là NOT RUN và không tự phê duyệt đề xuất nghiệp vụ.

| Story | Nội dung | SP sơ bộ | Ưu tiên | FR | UC | Điểm mở |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| [US-COST-001](#us-cost-001) | Danh mục nhà cung cấp | 3 | P0 | FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003 | UC-COST-001 | FLOW-COST-Q03 |
| [US-COST-002](#us-cost-002) | Nhập giá nguyên liệu | 3 | P0 | FR-COST-PRC-001 | UC-COST-002 | E3-Q13; E3-Q6 |
| [US-COST-003](#us-cost-003) | Chọn và tra giá tham chiếu | 3 | P0 | FR-COST-PRC-002, FR-COST-PRC-003 | UC-COST-002 | E3-Q4; E3-Q14; FLOW-COST-Q01 |
| [US-COST-004](#us-cost-004) | Nhập lưới nguyên tử | 3 | P0 | FR-COST-PRC-004 | UC-COST-003 | — |
| [US-COST-005](#us-cost-005) | Nhập XLSX giá | 5 | P0 | FR-COST-PRC-005 | UC-COST-004 | — |
| [US-COST-006](#us-cost-006) | Lịch sử và hủy giá tương lai | 3 | P0 | FR-COST-PRC-006, FR-COST-PRC-007 | UC-COST-002,005 | FLOW-COST-Q01; E3-Q14 |
| [US-COST-007](#us-cost-007) | Theo dõi giá thiếu và giá cũ | 3 | P0 | FR-COST-PRC-008, FR-COST-PRC-009 | UC-COST-005 | E3-Q5; FLOW-COST-Q03; DL-01 |
| [US-COST-008](#us-cost-008) | Xác nhận biến động giá | 2 | P1 | FR-COST-PRC-010 | UC-COST-002 | E3-Q6 |
| [US-COST-009](#us-cost-009) | Chứng từ giá | 2 | P1 | FR-COST-PRC-011 | UC-COST-002 | — |
| [US-COST-010](#us-cost-010) | Cost món và bảng phân rã | 5 | P0 | FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004 | UC-COST-006 | O-01; E3-Q2; FLOW-COST-Q04 |
| [US-COST-011](#us-cost-011) | So sánh công thức | 2 | P1 | FR-COST-DISH-005 | UC-COST-006 | FLOW-COST-Q04 |
| [US-COST-012](#us-cost-012) | Lập bảng món đặc thù | 3 | P0 | FR-COST-DISH-006 | UC-COST-007 | E3-Q16 |
| [US-COST-013](#us-cost-013) | Duyệt bảng món đặc thù | 3 | P0 | FR-COST-DISH-007 | UC-COST-007 | O-06; E3-Q16 |
| [US-COST-014](#us-cost-014) | Gợi ý nhóm cost | 2 | P1 | FR-COST-DISH-008 | UC-COST-006 | E3-Q7 |
| [US-COST-015](#us-cost-015) | Cost ngày trên thực đơn | 5 | P0 | FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003 | UC-COST-009 | O-01; E3-Q1; E3-Q3; E2-Q1 |
| [US-COST-016](#us-cost-016) | Khoản khoán | 3 | P0 | FR-COST-MEAL-004 | UC-COST-008 | O-01; FLOW-COST-Q05 |
| [US-COST-017](#us-cost-017) | Cổng gửi duyệt | 3 | P0 | FR-COST-MEAL-005 | UC-COST-010 | E3-Q3; E3-Q9; E3-Q16 |
| [US-COST-018](#us-cost-018) | Snapshot lúc duyệt | 3 | P0 | FR-COST-MEAL-006 | UC-COST-010 | FLOW-COST-Q06 |
| [US-COST-019](#us-cost-019) | Chế độ kiểm Cost | 2 | P0 | FR-COST-MEAL-008 | UC-COST-011 | — |
| [US-COST-020](#us-cost-020) | Bộ kiểm và ẩn con số | 3 | P0 | FR-COST-RUL-001, FR-COST-RUL-002 | UC-COST-009 | DL-01; E3-Q7 |
| [US-COST-021](#us-cost-021) | Ngân sách cho agent phía khách | 3 | P0 | FR-COST-RUL-003 | UC-COST-015 | FLOW-COST-Q09 |
| [US-COST-022](#us-cost-022) | Dự toán ngày | 5 | P0 | FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004 | UC-COST-012 | E3-Q8; E3-Q15; E3-Q2; O-01 |
| [US-COST-023](#us-cost-023) | Dự toán tuần | 5 | P0 | FR-COST-EST-003 | UC-COST-012 | FLOW-COST-Q07 |
| [US-COST-024](#us-cost-024) | Lịch sử và bản chỉ lượng | 3 | P0 | FR-COST-EST-005, FR-COST-EST-006 | UC-COST-013 | E3-Q11 |
| [US-COST-025](#us-cost-025) | Xuất dự toán | 3 | P1 | FR-COST-EST-007 | UC-COST-013 | E3-Q11 |
| [US-COST-026](#us-cost-026) | Tính lại và mở cảnh báo | 5 | P1 | FR-COST-ALR-001, FR-COST-ALR-002 | UC-COST-014 | FLOW-COST-Q08 |
| [US-COST-027](#us-cost-027) | Xử lý cảnh báo | 3 | P1 | FR-COST-ALR-003 | UC-COST-014 | — |
| [US-COST-028](#us-cost-028) | Mô phỏng giá | 3 | P2 | FR-COST-ALR-005 | UC-COST-016 | FLOW-COST-Q10 |

<a id="us-cost-001"></a>

## US-COST-001 — Danh mục nhà cung cấp

Là một **kế toán mua hàng**, tôi muốn **tạo, sửa, tìm và ngừng nhà cung cấp** để **quản lý nguồn giá mà vẫn giữ lịch sử**.

- Phạm vi: FR-COST-SUP-001, FR-COST-SUP-002, FR-COST-SUP-003; [UC-COST-001](../usecases/UC-COST-001.md).
- Giao tiếp đề xuất: API-COST-001, API-COST-002, API-COST-003; màn: SCR-COST-01, SCR-COST-02.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q03.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-001) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-002"></a>

## US-COST-002 — Nhập giá nguyên liệu

Là một **kế toán mua hàng**, tôi muốn **thêm giá trên đơn vị mua và ngày hiệu lực** để **có dữ liệu giá truy vết được**.

- Phạm vi: FR-COST-PRC-001; [UC-COST-002](../usecases/UC-COST-002.md).
- Giao tiếp đề xuất: API-COST-005, API-COST-037; màn: SCR-COST-03, SCR-COST-04.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q13; E3-Q6.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-002) (6 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-003"></a>

## US-COST-003 — Chọn và tra giá tham chiếu

Là một **kế toán mua hàng**, tôi muốn **chọn giá và tra theo ngày, cơ sở** để **tính cost theo đúng nguồn giá**.

- Phạm vi: FR-COST-PRC-002, FR-COST-PRC-003; [UC-COST-002](../usecases/UC-COST-002.md).
- Giao tiếp đề xuất: API-COST-008, API-COST-010; màn: SCR-COST-03, SCR-COST-04.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q4; E3-Q14; FLOW-COST-Q01.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-003) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-004"></a>

## US-COST-004 — Nhập lưới nguyên tử

Là một **kế toán mua hàng**, tôi muốn **lưu nhiều giá trong một lượt** để **giảm thao tác mà không ghi dở dang**.

- Phạm vi: FR-COST-PRC-004; [UC-COST-003](../usecases/UC-COST-003.md).
- Giao tiếp đề xuất: API-COST-006, API-COST-037; màn: SCR-COST-03.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: —.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-004) (5 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-005"></a>

## US-COST-005 — Nhập XLSX giá

Là một **kế toán mua hàng**, tôi muốn **kiểm tệp trước khi nhập** để **xử lý dữ liệu hàng loạt có báo lỗi theo dòng**.

- Phạm vi: FR-COST-PRC-005; [UC-COST-004](../usecases/UC-COST-004.md).
- Giao tiếp đề xuất: API-COST-012, API-COST-013, API-COST-014; màn: SCR-COST-05.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: —.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-005) (5 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-006"></a>

## US-COST-006 — Lịch sử và hủy giá tương lai

Là một **kế toán mua hàng**, tôi muốn **xem lịch sử và hủy giá chưa hiệu lực** để **sửa kế hoạch giá mà không sửa dữ liệu quá khứ**.

- Phạm vi: FR-COST-PRC-006, FR-COST-PRC-007; [UC-COST-002](../usecases/UC-COST-002.md); [UC-COST-005](../usecases/UC-COST-005.md).
- Giao tiếp đề xuất: API-COST-004, API-COST-009; màn: SCR-COST-03, SCR-COST-04, SCR-COST-06, SCR-COST-07.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q01; E3-Q14.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-006) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-007"></a>

## US-COST-007 — Theo dõi giá thiếu và giá cũ

Là một **kế toán mua hàng**, tôi muốn **nhận danh sách nguyên liệu cần cập nhật** để **ưu tiên cập nhật giá đang ảnh hưởng thực đơn**.

- Phạm vi: FR-COST-PRC-008, FR-COST-PRC-009; [UC-COST-005](../usecases/UC-COST-005.md).
- Giao tiếp đề xuất: API-COST-011; màn: SCR-COST-06, SCR-COST-07.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q5; FLOW-COST-Q03; DL-01.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-007) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-008"></a>

## US-COST-008 — Xác nhận biến động giá

Là một **kế toán mua hàng**, tôi muốn **xác nhận giá thay đổi lớn** để **tránh nhập nhầm mà vẫn cho lưu giá thực tế**.

- Phạm vi: FR-COST-PRC-010; [UC-COST-002](../usecases/UC-COST-002.md).
- Giao tiếp đề xuất: API-COST-005, API-COST-006, API-COST-007; màn: SCR-COST-03, SCR-COST-04.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q6.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-008) (4 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-009"></a>

## US-COST-009 — Chứng từ giá

Là một **kế toán mua hàng**, tôi muốn **gắn chứng từ cho giá hoặc lô giá** để **truy lại nguồn nhập**.

- Phạm vi: FR-COST-PRC-011; [UC-COST-002](../usecases/UC-COST-002.md).
- Giao tiếp đề xuất: API-COST-005, API-COST-006; màn: SCR-COST-03, SCR-COST-04.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: —.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-009) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-010"></a>

## US-COST-010 — Cost món và bảng phân rã

Là một **dinh dưỡng viên**, tôi muốn **xem cost món theo ngày và công thức** để **chọn món có căn cứ về chi phí**.

- Phạm vi: FR-COST-DISH-001, FR-COST-DISH-002, FR-COST-DISH-003, FR-COST-DISH-004; [UC-COST-006](../usecases/UC-COST-006.md).
- Giao tiếp đề xuất: API-COST-015; màn: SCR-COST-08.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: O-01; E3-Q2; FLOW-COST-Q04.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-010) (8 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-011"></a>

## US-COST-011 — So sánh công thức

Là một **người duyệt công thức**, tôi muốn **so sánh cost hai phiên bản** để **thấy tác động trước quyết định**.

- Phạm vi: FR-COST-DISH-005; [UC-COST-006](../usecases/UC-COST-006.md).
- Giao tiếp đề xuất: API-COST-016; màn: SCR-COST-08.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q04.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-011) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-012"></a>

## US-COST-012 — Lập bảng món đặc thù

Là một **dinh dưỡng viên**, tôi muốn **chụp bảng cost và gửi duyệt** để **có căn cứ xét món đặc thù**.

- Phạm vi: FR-COST-DISH-006; [UC-COST-007](../usecases/UC-COST-007.md).
- Giao tiếp đề xuất: API-COST-018, API-COST-019, API-COST-020; màn: SCR-COST-09, SCR-COST-10.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q16.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-012) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-013"></a>

## US-COST-013 — Duyệt bảng món đặc thù

Là một **Giám đốc**, tôi muốn **duyệt hoặc trả lại bảng tính** để **kiểm soát món đặc thù trước khi dùng**.

- Phạm vi: FR-COST-DISH-007; [UC-COST-007](../usecases/UC-COST-007.md).
- Giao tiếp đề xuất: API-COST-018, API-COST-019, API-COST-021; màn: SCR-COST-09, SCR-COST-10.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: O-06; E3-Q16.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-013) (4 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-014"></a>

## US-COST-014 — Gợi ý nhóm cost

Là một **dinh dưỡng viên**, tôi muốn **nhận gợi ý nhóm cao/thấp** để **phân loại món có tham khảo chi phí**.

- Phạm vi: FR-COST-DISH-008; [UC-COST-006](../usecases/UC-COST-006.md).
- Giao tiếp đề xuất: API-COST-017; màn: SCR-COST-08.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q7.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-014) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-015"></a>

## US-COST-015 — Cost ngày trên thực đơn

Là một **dinh dưỡng viên**, tôi muốn **xem cost suất và phân rã theo ngày/cơ sở** để **điều chỉnh thực đơn trong ngân sách**.

- Phạm vi: FR-COST-MEAL-001, FR-COST-MEAL-002, FR-COST-MEAL-003; [UC-COST-009](../usecases/UC-COST-009.md).
- Giao tiếp đề xuất: API-COST-025; màn: SCR-COST-12.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: O-01; E3-Q1; E3-Q3; E2-Q1.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-015) (6 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-016"></a>

## US-COST-016 — Khoản khoán

Là một **kế toán mua hàng**, tôi muốn **đề nghị khoản khoán để Giám đốc duyệt** để **tính đúng khoản cố định trên suất**.

- Phạm vi: FR-COST-MEAL-004; [UC-COST-008](../usecases/UC-COST-008.md).
- Giao tiếp đề xuất: API-COST-022, API-COST-023, API-COST-024; màn: SCR-COST-11.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: O-01; FLOW-COST-Q05.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-016) (4 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-017"></a>

## US-COST-017 — Cổng gửi duyệt

Là một **dinh dưỡng viên**, tôi muốn **kiểm Cost trước gửi thực đơn** để **ngăn thiếu dữ liệu và tuân thủ chế độ ngưỡng**.

- Phạm vi: FR-COST-MEAL-005; [UC-COST-010](../usecases/UC-COST-010.md).
- Giao tiếp đề xuất: hook nội bộ/SYS theo API mục 7; màn: SCR-COST-12.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q3; E3-Q9; E3-Q16.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-017) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-018"></a>

## US-COST-018 — Snapshot lúc duyệt

Là một **Giám đốc**, tôi muốn **lưu căn cứ cost cùng quyết định duyệt** để **truy lại số liệu đã dùng sau khi giá thay đổi**.

- Phạm vi: FR-COST-MEAL-006; [UC-COST-010](../usecases/UC-COST-010.md).
- Giao tiếp đề xuất: API-COST-026; màn: SCR-COST-12.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q06.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-018) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-019"></a>

## US-COST-019 — Chế độ kiểm Cost

Là một **quản trị tham số**, tôi muốn **đề nghị chế độ kiểm để người khác duyệt** để **chuyển giai đoạn chạy thử sang kiểm soát chặn**.

- Phạm vi: FR-COST-MEAL-008; [UC-COST-011](../usecases/UC-COST-011.md).
- Giao tiếp đề xuất: hook nội bộ/SYS theo API mục 7; màn: SCR-COST-13.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: —.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-019) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-020"></a>

## US-COST-020 — Bộ kiểm và ẩn con số

Là một **người soạn thực đơn**, tôi muốn **xem quy tắc Cost theo quyền** để **biết vi phạm mà không lộ dữ liệu ngoài phạm vi**.

- Phạm vi: FR-COST-RUL-001, FR-COST-RUL-002; [UC-COST-009](../usecases/UC-COST-009.md).
- Giao tiếp đề xuất: API-COST-025; màn: SCR-COST-12.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: DL-01; E3-Q7.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-020) (4 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-021"></a>

## US-COST-021 — Ngân sách cho agent phía khách

Là một **agent dinh dưỡng viên phía khách**, tôi muốn **nhận trạng thái ngân sách tổng** để **hỗ trợ thực đơn mà không đọc giá nội bộ**.

- Phạm vi: FR-COST-RUL-003; [UC-COST-015](../usecases/UC-COST-015.md).
- Giao tiếp đề xuất: API-COST-036; màn: SVC-COST-01 / tác vụ nền.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q09.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-021) (7 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-022"></a>

## US-COST-022 — Dự toán ngày

Là một **kế toán mua hàng**, tôi muốn **lập dự toán với số suất từng món** để **biết lượng mua và chi phí dự kiến**.

- Phạm vi: FR-COST-EST-001, FR-COST-EST-002, FR-COST-EST-004; [UC-COST-012](../usecases/UC-COST-012.md).
- Giao tiếp đề xuất: API-COST-027, API-COST-030; màn: SCR-COST-14, SCR-COST-15.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q8; E3-Q15; E3-Q2; O-01.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-022) (4 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-023"></a>

## US-COST-023 — Dự toán tuần

Là một **kế toán mua hàng**, tôi muốn **lập và gộp dự toán nhiều ngày** để **chuẩn bị nhu cầu nguyên liệu trong tuần**.

- Phạm vi: FR-COST-EST-003; [UC-COST-012](../usecases/UC-COST-012.md).
- Giao tiếp đề xuất: API-COST-028; màn: SCR-COST-14, SCR-COST-15.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q07.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-023) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-024"></a>

## US-COST-024 — Lịch sử và bản chỉ lượng

Là một **bếp trưởng**, tôi muốn **xem dự toán thuộc cơ sở và lịch sử phù hợp quyền** để **nhận lượng cần chuẩn bị từ đúng phiên bản**.

- Phạm vi: FR-COST-EST-005, FR-COST-EST-006; [UC-COST-013](../usecases/UC-COST-013.md).
- Giao tiếp đề xuất: API-COST-027, API-COST-029, API-COST-030, API-COST-037; màn: SCR-COST-15.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q11.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-024) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-025"></a>

## US-COST-025 — Xuất dự toán

Là một **kế toán mua hàng**, tôi muốn **xuất XLSX hoặc PDF theo quyền** để **chia sẻ bảng chuẩn bị nguyên liệu**.

- Phạm vi: FR-COST-EST-007; [UC-COST-013](../usecases/UC-COST-013.md).
- Giao tiếp đề xuất: API-COST-031; màn: SCR-COST-15.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: E3-Q11.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-025) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-026"></a>

## US-COST-026 — Tính lại và mở cảnh báo

Là một **dinh dưỡng viên**, tôi muốn **được báo khi giá mới khiến ngày đã duyệt vượt cost** để **kịp điều chỉnh thực đơn**.

- Phạm vi: FR-COST-ALR-001, FR-COST-ALR-002; [UC-COST-014](../usecases/UC-COST-014.md).
- Giao tiếp đề xuất: API-COST-032, API-COST-033; màn: SCR-COST-16, SCR-COST-17.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q08.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-026) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-027"></a>

## US-COST-027 — Xử lý cảnh báo

Là một **dinh dưỡng viên**, tôi muốn **xem và đóng cảnh báo với lý do** để **theo dõi việc xử lý biến động giá**.

- Phạm vi: FR-COST-ALR-003; [UC-COST-014](../usecases/UC-COST-014.md).
- Giao tiếp đề xuất: API-COST-032, API-COST-033, API-COST-034; màn: SCR-COST-16, SCR-COST-17.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: —.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-027) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

<a id="us-cost-028"></a>

## US-COST-028 — Mô phỏng giá

Là một **người nội bộ được cấp quyền mô phỏng**, tôi muốn **thử một giá giả định** để **đánh giá tác động trước khi nhập thật**.

- Phạm vi: FR-COST-ALR-005; [UC-COST-016](../usecases/UC-COST-016.md).
- Giao tiếp đề xuất: API-COST-035; màn: SCR-COST-18.
- Phụ thuộc: dữ liệu và tiền điều kiện trong use case; các đầu vào engine phải hợp lệ. Điểm mở: FLOW-COST-Q10.
- Nghiệm thu: [AC](acceptance-criteria.md#us-cost-028) (3 kịch bản). Evidence cần bàn giao: kết quả API/ảnh UI nếu có, dữ liệu trước/sau, audit cho lệnh ghi, báo cáo test.

## Hai mục hoãn, chưa đưa vào sprint

| Mục quyết định | FR | Chủ sở hữu | Điều kiện mở lại |
| :--- | :--- | :--- | :--- |
| DEC-COST-01 | FR-COST-MEAL-007 | Giám đốc, E3-Q9 | Chốt có ngoại lệ hay không, người duyệt/lý do/audit; sau đó mới viết story/AC thành công |
| DEC-COST-02 | FR-COST-ALR-004 | Giám đốc, E3-Q10 | Chốt luồng chuyển bếp và cơ chế chặn/cảnh báo; chưa có bước chuyển bếp ở R3 |

Hai mục này không được tính là story đã có AC/test hay chức năng hoàn tất. Chế độ CANH_BAO không phải duyệt ngoại lệ CHAN.

## Lịch sử sửa đổi

| Phiên bản | Ngày | Người | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Khởi tạo bản nháp truy vết, giữ điểm mở và trạng thái chưa chạy |
