# Gói review BA — Dinh dưỡng và Agent Nội bộ MVP

Phiên bản 0.1.0 · 2026-11-11 · **Draft, chưa ký duyệt nghiệp vụ, chưa triển khai backend.**

| Phiên bản | Ngày | Người thực hiện | Nội dung |
| :--- | :--- | :--- | :--- |
| 0.1.0 | 2026-11-11 | BA | Bổ sung đặc tả E4/E5, đồng bộ phụ thuộc và tự kiểm cấu trúc/truy vết |

## 1. Phạm vi và căn cứ

Đã đọc OVERVIEW, PRD, roadmap, báo cáo thiết kế kế toán và bàn giao Cost. Workspace có E1/E2/E3 và kế toán mở rộng; chưa có SRS riêng E4/E5 trước gói này. Kế thừa nutrient_values, agent_runs và các bảng MENU/COST, không xây lại phần kế toán. Không tìm thấy AGENTS.md trong workspace; D:\BA không phải Git repository, vì vậy danh mục thay đổi dưới đây là danh mục file đã ghi, không phải git diff.

Áp dụng các skill BA tại `.agents/skills`: srs, api-design, usecase, user-flow, erd, wireframe-ascii, userstory, ac, test-cases, update-overview. Quy chuẩn đọc tại `.claude/ba-kit/rules`. Không đặt story point, ngân sách, thời hạn hoặc kết quả nghiệm thu giả khi chưa có đội/người duyệt.

## 2. Tài liệu review

| Thành phần | E4 — Dinh dưỡng | E5 — Agent Nội bộ |
| :--- | :--- | :--- |
| Phạm vi | FEAT-019/020, R4 | FEAT-021/022/023, R5 |
| SRS | [5 FR, 5 BR, 4 NFR](../../dinh-duong/srs/spec.md) | [6 FR, 6 BR, 4 NFR](../../agent-noi-bo/srs/spec.md) |
| UC / flow | 5 UC trong [backlog](../../dinh-duong/userstories/backlog.md), [flow](../../dinh-duong/ui/user-flow.md) | 6 UC trong [backlog](../../agent-noi-bo/userstories/backlog.md), [flow](../../agent-noi-bo/ui/user-flow.md) |
| Dữ liệu | [ERD và từ điển](../../dinh-duong/srs/erd.md) | [ERD và từ điển](../../agent-noi-bo/srs/erd.md) |
| API | [7 endpoint](../../dinh-duong/api/api-spec.md), [catalog](../../dinh-duong/api/endpoint-catalog.json) | [6 endpoint và port MENU/COST](../../agent-noi-bo/api/api-spec.md), [catalog](../../agent-noi-bo/api/endpoint-catalog.json) |
| UI | [3 màn ASCII](../../dinh-duong/ui/wireframe-ascii.md) | [3 màn ASCII](../../agent-noi-bo/ui/wireframe-ascii.md) |
| AC / test | [15 AC](../../dinh-duong/userstories/acceptance-criteria.md), [28 ca](../../dinh-duong/test/test-cases.md), [RTM](../../dinh-duong/test/traceability.md) | [18 AC](../../agent-noi-bo/userstories/acceptance-criteria.md), [32 ca](../../agent-noi-bo/test/test-cases.md), [RTM](../../agent-noi-bo/test/traceability.md) |
| Câu hỏi | [NUTR-Q01–04, DATA-NUTR-Q01](../../dinh-duong/review/questions.md) | [AIO-Q01–06](../../agent-noi-bo/review/questions.md) |

Tổng 11 FR, 11 story/UC, 33 AC, 60 test case thiết kế: 33 ca chức năng, 19 lỗi hợp đồng, 8 NFR. Test lỗi/NFR liên kết SRS trực tiếp, không giả thành thêm story. Cả 11 câu hỏi mới đều **CHỜ XÁC NHẬN**. Story có AC nhưng chưa tự coi là sprint-ready vì còn quyết định phụ thuộc.

## 3. Thiết kế cần tập trung review

1. **Dinh dưỡng:** nguồn/ấn bản/trang, ý nghĩa qty_std trước/sau bỏ xương/vỏ, phạm vi suất và làm tròn. Chưa có 5 suất tính tay thật; các số 40 kcal/50 kcal chỉ là fixture giả định kiểm số học. Không nhân lại hao hụt Cost và không cộng mọi lựa chọn món chính vào một suất.
2. **Agent:** dựng/chỉnh nháp, kiểm qua MENU/COST bằng cùng phiên bản; thiếu giá/VAT không tự điền. Đề xuất VALID phải không vượt cost kể cả CANH_BAO đang chờ AIO-Q02. Không đổi cổng MENU; apply chỉ DRAFT và phải kiểm lại quyền/nguồn. DONE không đồng nghĩa đạt; NEEDS_INPUT/NO_SOLUTION/BLOCKED_DATA không có nháp cho apply.
3. **Lịch sử và cạnh tranh:** giữ revision/snapshot bất biến, khóa version, idempotency, apply nguyên tử; schema có cấu trúc đề xuất, chưa có migration hoặc đảm bảo thực thi transaction. Tech lead cần chốt adapter MENU/worker/outbox/quota và rollout legacy.
4. **Phạm vi:** không agent khách, hồ sơ sức khỏe, CRM, mua hàng hoặc hỏi đáp số liệu Later; không dựng API cho nghiệp vụ ngoài MVP. Agent không tự tính số hoặc công bố.

## 4. File hiện có được đồng bộ

- [OVERVIEW v0.8.0](../../OVERVIEW.md): SRS nháp 23/23 MVP, 23/78 toàn sản phẩm; không tăng tiến độ phần mềm.
- [PRD v0.1.1](../01-prd.md), [roadmap v0.1.2](../02-roadmap.md): liên kết đặc tả, giữ tiêu chí R4/R5 và ghi chỗ cần diễn giải/chốt.
- [ERD tổng v0.5.0](../../nen-tang/srs/erd.md), [DBML v0.5.0](../../nen-tang/srs/schema.dbml): giữ61 bảng cũ, thêm4 bảng =65; nutrient_values thêm3 cột nguồn/version. Không chạy migration.
- [SRS MENU](../../thuc-don-dinh-luong/srs/spec.md), [SRS Cost](../../cost/srs/spec.md): chỉ bổ sung liên kết ownership/cổng E4/E5; không đổi FR Cost hay FR MENU.
- [Kiểm thiết kế kế toán](../../cost/validation/check-accounting-design.cjs): cập nhật số bảng kỳ vọng65 theo schema mới; các assertion nghiệp vụ giữ nguyên. Báo cáo lịch sử61 bảng không bị viết lại thành kết quả kiểm mới.

Các thư mục mới `docs/dinh-duong/` và `docs/agent-noi-bo/` chứa trọn gói ở mục2, gồm11 file UC riêng. Công cụ kiểm mới: [check-mvp-review.py](../validation/check-mvp-review.py), [kết quả máy đọc](../validation/mvp-check-result.json). SRS/API/UI hiện là nguồn đọc review, không phải code thực thi.

## 5. Kiểm tra và giới hạn bằng chứng

Kết quả chi tiết được ghi sau khi chạy tại [báo cáo kiểm](../validation/mvp-validation-report.md). Script kiểm local link, ID, FR→UC/story→AC/test, BR/ERR/NFR có ca, API/UI/table và số học Decimal giả định. DBML xuất MySQL chỉ kiểm cú pháp và references. Không chứng minh thuật toán backend, migration, phân quyền thực thi, độ chính xác nguồn dinh dưỡng hoặc chất lượng model.

Wireframe ASCII chưa chạy trình duyệt; không có bằng chứng responsive/accessibility tương tác. Các Mermaid là source sơ đồ trong Markdown, chưa render/kiểm hình ảnh. 0 test backend/UAT được chạy trong gói. NOT RUN và BLOCKED không chuyển PASS chỉ vì script tài liệu đạt.

## 6. Giữ nguyên xác nhận kế toán

Cost nguyên liệu gồm VAT phải trả nhà cung cấp; không yêu cầu hóa đơn là cờ riêng, không suy VAT0. Chiết khấu % hoặc tiền/suất là khoản riêng theo đơn, không tự giảm phải trả. [CK-Q01–10](../../cost/accounting/business-rules.md) vẫn chờ xác nhận; [DATA-COST-Q01–06](../../cost/review/accountant-input.md) vẫn trong phiếu kế toán, chưa có 10 món/10 ngày thật. NFR-COST-002: cost món lệch tối đa1đ, cost% ngày tối đa0,01 điểm phần trăm; không dùng dung sai này cho dinh dưỡng.

## 7. Điều kiện tiếp theo

| Nhóm review đề xuất | Nội dung cần chốt | Bằng chứng cần có |
| :--- | :--- | :--- |
| Dinh dưỡng viên, bếp trưởng | NUTR-Q01–04; mapping, phần ăn được, tổ hợp suất | Nguồn thành phần có ấn bản/trang; 30 món; 5 suất tính tay độc lập |
| Chủ sản phẩm, Giám đốc | AIO-Q01–05; provider/quota, quyền log, tiêu chí nháp đạt | Quyết định có người/ngày/nguồn; 20 yêu cầu khả thi; baseline thời gian trước MVP |
| Tech lead, BA | AIO-Q06, contract, migration legacy, CHECK/JSON, idempotency và atomic apply | Thiết kế triển khai được review, không chỉ DBML compile |
| QA | Fixture, trace, môi trường, tải, bảo mật, chạy lỗi/race/timeout | Build/backend, dữ liệu có nguồn, actual/evidence/defect/retest |

Đây là phân công theo vai trò đề xuất; chưa gửi lời mời hay tự gán người phụ trách. Gói công việc BA đã chuẩn bị để review, không phải baseline đã được ký duyệt.
