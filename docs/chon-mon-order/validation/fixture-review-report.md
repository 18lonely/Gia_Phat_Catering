# Đối chiếu fixture E6 — 12/11/2026

DOCUMENT_CLARIFIED · Chỉ BA, chưa backend/migration/E7–E13. Workspace D:/BA không Git/AGENTS.md. Đã đọc các tài liệu yêu cầu, kiểm kê và đọc4/4file fixture; áp dụng skill test-cases và rule/template hiện có tại .claude/ba-kit. Không sinh ca hoặc sổ gap mới.

## Kết quả

[README fixture](../test/fixtures/README.md) có ánh xạ22/22ca với phạm vi mẫu và thiếu tiền điều kiện thực thi. Sửa sai lệch hướng dẫn Retry gộp ba giai đoạn thành key/body: tách replay HTTP trước/sau commit với redelivery worker sau outbox. Bổ sung reset giữa các biến thể (không reset giữa commit và replay), phân biệt principal nghiệp vụ/seed/evidence, một transaction PORT-LOCK, producer plan/GET bếp, PORT-REM/GET theo dõi và NUTR incomplete/timeout/cache.

Không cần sửa3/3JSON: consistency giữ version41/8/2/5 và phép thay nguồn100→105; delta giữ tổng100 nhưng recipe đổi-60/+60; adapter giữ6fragment oracle zero/missing/timeout/scope/allergen/list rỗng. README làm rõ các mẫu không là một seed database: selection version3 không là Given version1; summary2selection không là S60/C10/T100; A2+B1→A3 không là lịch concurrent A2/B2. Các khác biệt này là giới hạn mục đích, không lỗi số học cần đổi JSON. Không tự thêm grant/credential, payload/envelope/default/pageSize, nguồn/freshness/nullability hoặc policy. Thiếu setup runtime dẫn CG hiện có.

SRS/API/catalog/UC/AC/protocol và toàn bộ bộ ca không cần sửa. Không sửa wireframe, Cost/schema hoặc snapshot handoff/report/result/manifest/baseline lịch sử. Sổ [contract-gap-register](../review/contract-gap-register.md) duy nhất giữ14OPEN; nhật ký sửa là DOCUMENT_CLARIFIED.

## Bảo toàn và kiểm

[Baseline SHA256 trước sửa](fixture-review-baseline-sha256.json):1220file. [Checker chuyên biệt](check-fixture-review.py) bảo vệ mọi file ngoài allowlist phiên, gồm3JSON và toàn bộ ca/Status/Actual/Evidence; kiểm số học/oracle,22ánh xạ và preview. [Kết quả kiêm manifest file thay đổi](fixture-review-check-result.json).

Đã đọc checker/output trước chạy: check-e6.py chỉ ghi check-result.json; render-e6.cjs ghi preview/diagram artifacts và diagram-render-result.json. Checker mới chỉ ghi fixture-review-check-result.json. Không chạy check-downstream-review.py/check-case-review.py vì baseline/allowlist thuộc phiên cũ và ghi đè result/manifest lịch sử. Không chạy check-adapter-review.py/check-contract-review.py để tránh ghi đè kết quả cũ; các phép kiểm fixture phù hợp được kiểm ở checker phiên này, không sửa checker lịch sử.

Kết quả kiểm:
- check-fixture-review.py: exit0,0lỗi;1194file ngoài allowlist giữ hash,3JSON không đổi;22mã ca/truy vết/Status/Actual/Evidence được bảo toàn bằng hash toàn file. Baseline trước sửa có1220file.
- check-e6.py: lượt đầu phát hiện liên kết tới kết quả checker mới chưa tạo; sau khi tạo đủ artifact, chạy lại exit0,0lỗi.
- render-e6.cjs: exit0;60tài liệu,8/8sơ đồ,0lỗi. Diagram artifacts có hash không đổi; preview được cập nhật.

Nguồn thay đổi gồm fixtures/README.md, review/contract-gap-register.md, gap-analysis.md, docs/project-dashboard.md, docs/gia-phat/review/progress-assessment.md và next-session-prompt.md; thêm baseline/checker/result/report phiên. Preview là đầu ra render. Manifest cuối ghi theo SHA256 thực tế, không liệt kê file được ghi lại nhưng nội dung không đổi. Không chạy check-ui hoặc xem viewport vì không sửa wireframe; không chạy generator bị cấm. Kiểm tài liệu/số học/render không chứng minh backend, quyền, transaction, pilot hay nghiệm thu.

## Tiến độ, chặn và bước tiếp

Đọc4/4file, kiểm3/3JSON và ánh xạ fixture22/22ca; không phải22ca thực thi. Gốc2NOT RUN/8BLOCKED; hệ thống5NOT RUN/7BLOCKED;57theoAC29NOT RUN/28BLOCKED;12INV NOT RUN;8DR BLOCKED.99mô tả overlap,0backend.40/78feature nháp (51,3%),17/19E6 có điều kiện (89,5%),19/19RTM;19UC/57AC/26HTTP/2port/13màn/8sơ đồ/65bảng.34/34DTO,19/19UC và22/22ca đã rà từ trước; không lặp review.0/14CG và0/8RVđóng.

Chặn identity/scope, C→S/vượtT, deadline/remediation/approval, persistence/receipt/outbox, plan nguồn/completeness, adapter provenance/freshness/envelope và policy nhắc; pilot/tải cần dữ liệu/môi trường thật. Giữ E6-EVID-001/002, Cost/VAT/chiết khấu, CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03; GATE-046/047 không nhận profile/consent/thu sức khỏe/chạy thuật toán.

Tiếp theo chỉ đối chiếu evidence mới với điều kiện đóng trong sổ CG, hoặc sửa sai lệch BA cụ thể có căn cứ; khi chưa có đầu vào mới, không tạo thêm review/ca/fixture trùng và không tự chốt policy. [Prompt tiếp nối](../../gia-phat/review/next-session-prompt.md).
