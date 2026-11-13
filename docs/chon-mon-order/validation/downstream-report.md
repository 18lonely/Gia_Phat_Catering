# Rà tài liệu hạ nguồn và evidence QA ngày 12/11/2026

DOCUMENT_CLARIFIED, chỉ BA. Workspace D:/BA không có Git; không tìm thấy AGENTS.md kể cả tìm file ẩn trong workspace và D:/. Đã đọc năm mốc người dùng yêu cầu trước sửa. Skill user-flow/test-checklist: đọc rule/template tại .claude/ba-kit. Không chạy generator.

## Kết quả đối chiếu

| Phạm vi | Kết quả / căn cứ |
| :--- | :--- |
| Backlog19story | Sửa010/011 cùng PORT-LOCK;014 gửi khác theo dõi;016 đọc;017/018 gate;019 bếp GET. Bỏ nhận định AC chỉ có chọn/chốt đã lỗi thời. Grant A không chốt scope tài khoản; mã/gate giữ nguyên |
| Checklist | Sửa yêu cầu trả toàn bộ câu hỏi để giữ E6-EVID-002; bổ sung phân loại thao tác và dẫn evidence, không thêm TC |
| User-flow, sequence2sơ đồ, usecase diagram | Tách transaction khóa, outbox worker và GET; không hiểu khóa là plan đã có hoặc publish. UC010/011 một transaction; PORT-REM khác GET023 |
| State2sơ đồ | Không cần sửa: transition IN_PRODUCTION đã ghi chờ ORD-Q14, publish/xem không tự start; đề nghị rejected không sửa order |
| ERD và data-dictionary2sơ đồ | Không cần sửa: mô tả quan hệ nguồn/snapshot và delta đề xuất, không trigger GET/thu sức khỏe hoặc quyết scope toàn tài khoản |
| SRS spec, operational-rules, lock-plan-review | Không cần sửa trong phạm vi này: đã tách worker/read, default trong khóa, gate và publish/ack/start. Các proposal/policy còn mở không được phê duyệt lại |
| Evidence protocol + fixtures README | Bổ sung actor/principal, trigger, quan sát trước/sau và evidence theo GET/ghi/lock/plan/reminder/theo dõi/gate; tách producer+read cùng TC019-1/3. Sửa checklist fixture đòi key/receipt/commit chung cho mọi thao tác |
| Hướng dẫn57ca, INV, AC/API/catalog/RTM | Không cần sửa: hướng dẫn57ca đã phân loại và tách producer/read; protocol bổ sung chi tiết thu evidence. Giữ toàn bộ mã, ca, Status/Actual/Evidence; không review lại DTO/UC |

Đối chiếu nguồn: [SRS](../srs/spec.md), [API](../api/api-spec.md), [catalog](../api/endpoint-catalog.json), [UC](../review/uc-operation-review.md), [AC](../userstories/acceptance-criteria.md), [57ca](../test/review-test-cases.md), [INV](../test/invariant-cases.md). Đây không là sổ gap mới; trạng thái duy nhất tại [contract-gap-register](../review/contract-gap-register.md).

## Kiểm và bảo toàn

- check-e6.py: exit0,0lỗi;19UC/57AC/26HTTP/2port/65bảng;29NOT RUN/28BLOCKED.
- render-e6.cjs: exit0;60tài liệu preview,8/8sơ đồ render,0lỗi. Đọc lại nguồn phát hiện trùng node tuần/worker trong sơ đồ UC; đã tách node và render lại.
- check-contract-review.py: exit0;12INV,11file bảo vệ,0lỗi.
- check-dto-review.py: exit0;34DTO/14gap,13file bảo vệ,0lỗi.
- check-adapter-review.py: exit0;26route/6oracle synthetic,12file bảo vệ,0lỗi;0route thực thi.
- Đối chiếu SHA256 toàn bộ file có trước phiên ngoài danh sách sửa cho phép, bảo toàn mã truy vết ở nguồn sửa, ca/status/evidence và snapshot lịch sử: xem kết quả bảo toàn bên dưới. Baseline trước sửa: [downstream-baseline-sha256.json](downstream-baseline-sha256.json). [Manifest](downstream-change-manifest.md) và [kết quả bảo toàn](downstream-check-result.json).

Không sửa wireframe nên không chạy check-ui/chụp desktop/mobile. Kiểm tài liệu/render không là backend, tải hoặc nghiệm thu. Dữ liệu ví dụ là synthetic; không có evidence mới đóng policy/persistence.

## Tiến độ và phần chặn

40/78feature nháp (51,3%),17/19E6 có điều kiện (89,5%),19/19RTM;19UC/57AC/26HTTP/2port/13màn/8sơ đồ/65bảng.34/34DTO và19/19UC đã rà từ phiên trước.99mô tả có overlap;57ca29NOT RUN/28BLOCKED,12INV NOT RUN,8DR BLOCKED;0test backend.14/14gap OPEN,0/14CG và0/8RVđóng.

Identity/scope, C→S/vượtT, nguồn plan/định lượng, hạn/quyền, persistence/event/receipt/envelope và policy còn thiếu evidence theo điều kiện sổ gap. Giữ E6-EVID-001/002, Cost/VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03; chưa backend/migration/E7–E13. Tiếp theo đối chiếu assumption trong10ca gốc và12ca hệ thống bằng protocol mới, chỉ sửa phần có căn cứ; không thêm ca hoặc đổi status. [Prompt tiếp nối](../../gia-phat/review/next-session-prompt.md).
