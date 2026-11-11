# Rà10ca gốc và12ca hệ thống — 12/11/2026

DOCUMENT_CLARIFIED · Chỉ BA, chưa backend/migration/E7–E13. Đã kiểm workspace D:/BA, không Git/AGENTS.md; đọc năm tài liệu yêu cầu trước sửa. Dùng skill test-cases; đọc rule/template tại .claude/ba-kit. Không chạy generator hoặc lặp review34DTO/19UC/downstream.

## Kết quả đối chiếu22/22ca

Căn cứ: [SRS](../srs/spec.md), [quy tắc](../srs/operational-rules.md), [API](../api/api-spec.md), [catalog](../api/endpoint-catalog.json), [UC](../review/uc-operation-review.md), [AC](../userstories/acceptance-criteria.md), [adapter](../api/adapter-contract-review.md) và [evidence protocol](../test/evidence-protocol.md).

| Phạm vi | Kết quả |
| :--- | :--- |
| Gốc SEL-01/SUB-01/DEF-01/SEC-01/PLAN-01 | Sửa5dòng: PUT replay cùng key/body; POST SUBMITTED trước khóa; default/khóa cùng PORT-LOCK; service principal; scope fixture A/không B; GET không ghi; worker là producer |
| Gốc SEL-02/SEL-03/SUB-02/CHG-01/QR-01 | Không cần sửa5dòng Given/When/Then: giữ expected có điều kiện và gate; hướng dẫn chung làm rõ principal/evidence, không chốt policy |
| SYS-01/02/03/05/08/09/11 | Sửa7dòng: retry phân theo method, service khóa, tạo plan khác publish, scope principal thử nghiệm, PORT-REM khác GET023, SafeDish chỉ đọc nguồn có sẵn, phân biệt mất response sau commit với fault trước commit |
| SYS-04/06/07/10/12 | Không cần sửa5dòng expected/steps; thêm hướng dẫn producer/read, người duyệt/quyền evidence, dữ liệu pilot và transaction cho phần cần áp dụng |
| Ca liên thông | Giữ một caseId; producer có event/commit/source/plan revision và snapshot riêng; read có principal, request/response và snapshot ngay trước/sau; GET không publish/ack/start-production |
| Gate và grant |22ca không có ca gate riêng, không thêm trùng bộ57ca. GATE-046/047 không nhận profile/consent/thu sức khỏe/chạy thuật toán. Fixture quyền A không chốt một/nhiều công ty |
| Những file không cần sửa | SRS/API/catalog/UC/AC/evidence-protocol và các bộ57ca/12INV/8DR giữ hash. Wireframe giữ nguyên; không kiểm UI không liên quan |

SYS-09 theo adapter hiện có: incomplete thì cả4chỉ số null + missing an toàn, không tổng một phần; totals=null là mô tả nghiệp vụ AC, không thêm wire field. Không tự chốt nullability/defaults/envelope/retry/retention hoặc source freshness.

## Bảo toàn và kiểm

Baseline toàn workspace trước sửa: [SHA256](case-review-baseline-sha256.json), [bản gốc hai file](case-review-original.json). [Checker chuyên biệt](check-case-review.py) bảo vệ mọi file ngoài allowlist, so từng mã ca/truy vết/status và Actual/Evidence; [kết quả kiêm manifest đầy đủ](case-review-check-result.json).

Nguồn Markdown thay đổi: test/test-cases.md, test/system-test-cases.md, review/contract-gap-register.md, gap-analysis.md, docs/project-dashboard.md, docs/gia-phat/review/progress-assessment.md, docs/gia-phat/review/next-session-prompt.md. Preview và diagram artifacts là đầu ra render; JSON kiểm được ghi theo checker. File mới chỉ phục vụ baseline, kiểm bảo toàn và báo cáo phiên, không sổ gap hoặc ca mới.

- check-e6.py: các lượt chuẩn bị phát hiện liên kết tới báo cáo/kết quả chưa được tạo; đã tạo đủ artifact và chạy lại, exit0/0lỗi ở lượt cuối.
- render-e6.cjs: exit0;60tài liệu,8/8sơ đồ,0lỗi.
- check-case-review.py: exit0/0lỗi;1188file bảo vệ giữ hash,22mã/truy vết/status và Actual/Evidence được bảo toàn. Snapshot handoff/report lịch sử, downstream baseline/result/manifest đều nguyên trạng.
- Không chạy check-downstream-review.py: đã đọc scope, baseline phiên trước bảo vệ hai file ca nay được phép sửa; script còn ghi đè manifest/result lịch sử. Giữ nguyên script/baseline/report/result downstream, không sửa để pass.
- Không sửa contract/DTO/fixture/UI nên không chạy lại checker cho các phần đó. Không dùng kiểm tài liệu/render làm evidence backend/quyền/transaction/nghiệm thu.

## Tiến độ và phần chặn

Rà tài liệu10/10gốc +12/12hệ thống =22/22; không phải22ca đã chạy. Gốc2NOT RUN/8BLOCKED; hệ thống5NOT RUN/7BLOCKED.57ca theoAC vẫn29NOT RUN/28BLOCKED;12INV NOT RUN;8DR BLOCKED; Actual/Evidence chưa có,0backend. Inventory99mô tả (10+57+12+8+12) có overlap.

40/78feature thiết kế nháp (51,3%);17/19capability E6 có điều kiện (89,5%);19/19RTM;19UC/57AC/26HTTP/2port/13màn/8sơ đồ/65bảng.34/34DTO và19/19UC đã rà từ trước.14/14gap OPEN,0/14CG và0/8RVđóng; trạng thái duy nhất tại [sổ gap](../review/contract-gap-register.md).

Chặn identity/scope, C→S/vượtT, deadline/remediation, nguồn/completeness/định lượng plan, quyền duyệt, persistence/receipt/outbox, envelope/freshness và policy nhắc; pilot/tải cần môi trường/dữ liệu thật. Giữ E6-EVID-001/002; không hỏi lại ba policy. Giữ Cost/VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03. Synthetic không thay dữ liệu thật.

Tiếp theo: đối chiếu fixture synthetic hiện có với tiền điều kiện/oracle22ca; chỉ sửa sai lệch có căn cứ, không thêm ca hoặc tự chốt policy. [Prompt tiếp nối](../../gia-phat/review/next-session-prompt.md). Giữ nguyên snapshot handoff/report lịch sử.
