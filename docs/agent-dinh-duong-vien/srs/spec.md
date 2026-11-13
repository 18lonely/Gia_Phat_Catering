---
id: DOC-E9-SRS-SPEC-MD
title: "SRS: Agent Dinh dưỡng viên E9"
version: 0.1.0
phase: Specification
domain: Gia Phát
author: BA
last_updated: 2026-11-12
---
# SRS: Agent Dinh dưỡng viên E9

Draft · 12/11/2026 · Chưa duyệt, chưa freeze; 0 backend/migration/UAT; không gọi mô hình AI.

## 1. Giới thiệu

[Phạm vi](../epic-spec.md) gồm FEAT-060→065, trong đó063 gate-only. Candidate là phương án nháp có revision/hash, chưa là MENU. Proposal là đề xuất gửi cho người thật; receipt chứng minh tiếp nhận, không chứng minh duyệt/áp dụng. Reservation là phần ngân sách AI giữ chỗ, không cost thực phẩm. [Nguồn và gate](../review/dependencies.md).

## 2. Tổng quan

PER-01/02 dùng mặt tiền khách; PER-08 quản trị khi được cấp quyền. PER-03/04 chỉ thấy gate063. Web desktop/mobile; HTML offline synthetic. Provider/identity/consent/quota chưa chọn; E2/E4/E5/E6/E8 nháp chưa freeze. Hai agent tách identity/queue/tool/hạn mức/cấu hình lời nhắc; không viết system prompt. Không có giao tiếp phần cứng.

## 3.1 FR: input, processing, output

| FR / feature | Tên / actor / ưu tiên | Input | Processing | Output | BR | Gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FR-AIN-SESS-001 / FEAT-060 | Mở phiên yêu cầu; PER-01, PER-02; P0 | kênh, bằng chứng identity/consent theo policy | Kiểm policy truy cập và nhóm từ server; cấp sessionRef opaque gắn chủ thể; chưa chốt guest không tự tạo users/eaters | Phiên được phép hoặc từ chối | BR-AIN-001, BR-AIN-011, BR-AIN-014 | E9-Q02, E9-Q10 |
| FR-AIN-GEN-001 / FEAT-060 | Yêu cầu thực đơn tập thể; PER-01, PER-02; P0 | sessionRef, loại suất, số suất nguyên dương, tuần/ngày, khẩu vị/kiêng kỵ theo danh mục | Kiểm đầu vào/policy/nguồn và reserve hạn mức trước nhận; dựng candidate chỉ món/công thức đã duyệt qua tools; không tự tính dinh dưỡng/cost | Run và candidate chờ kiểm; không trả nháp chưa kiểm là hợp lệ | BR-AIN-001, BR-AIN-002, BR-AIN-008, BR-AIN-014 | E9-Q01, E9-Q03, E9-Q07, E9-Q11, E9-Q12, E9-Q13 |
| FR-AIN-CHK-001 / FEAT-060 | Kiểm và xem phương án; PER-01, PER-02; P0 | runRef, candidateRevision/hash, phiên bản nguồn | Orchestrator gọi FR-MENU-RUL-002 không lưu; buộc toàn phương án khớp hash/ruleVersion; lọc kết quả nhạy cảm trước model/UI; nguồn thiếu/cứng fail không hợp lệ | Candidate đã kiểm, bảng kiểm an toàn hoặc trạng thái chặn | BR-AIN-002, BR-AIN-003, BR-AIN-013, BR-AIN-014 | E9-Q05, E9-Q12, E9-Q13 |
| FR-AIN-EXPL-001 / FEAT-061 | Giải thích thực đơn; PER-01, PER-02; P0 | candidateRef/revision và mục cần giải thích | Chỉ diễn giải projection món, định lượng, bảng kiểm public và 4 chỉ số từ E4; gắn nguồn và nhãn; không tự tính, không nêu nguyên nhân cost | Giải thích có nguồn, hoặc thiếu dữ liệu | BR-AIN-003, BR-AIN-006, BR-AIN-007, BR-AIN-013 | E9-Q04, E9-Q05, E9-Q12 |
| FR-AIN-EDIT-001 / FEAT-061 | Chỉnh thực đơn và kiểm lại; PER-01, PER-02; P0 | candidateRef, baseRevision, chỉ dẫn đổi ngày/vị trí/món | Làm rõ yêu cầu mơ hồ; tạo revision mới với diff; luôn chạy lại máy E2 toàn tuần và kiểm nguồn, không tái dùng pass cũ | Nháp revision mới đã kiểm hoặc nhánh không đạt | BR-AIN-002, BR-AIN-003, BR-AIN-008 | E9-Q03, E9-Q05, E9-Q12, E9-Q13 |
| FR-AIN-SEND-001 / FEAT-062 | Gửi đề xuất về Gia Phát; PER-01, PER-02; P0 | candidateRef/revision, nguồn kênh, liên hệ tối thiểu và consent được duyệt | Lệnh do khách xác nhận; kiểm lại quyền/evidence hiện hành; ghi proposal và nguồn bền vững trước ACK; chuyển qua port tối thiểu khi có đầu nhận; không gọi applyDraft | Mã tiếp nhận khi đã lưu; chỉ đề xuất chờ người thật | BR-AIN-001, BR-AIN-004, BR-AIN-011 | E9-Q06, E9-Q10, E9-Q13 |
| FR-AIN-STAT-001 / FEAT-062 | Xem trạng thái đề xuất; PER-01, PER-02; P0 | proposalRef | Kiểm quyền sở hữu; chỉ phản ánh trạng thái có evidence từ nơi nhận; không suy giao thành công từ thông báo; wording sau tiếp nhận chờ Q06 | Trạng thái tiếp nhận an toàn, không cam kết SLA | BR-AIN-001, BR-AIN-004 | E9-Q06, E9-Q13 |
| FR-AIN-GATE-001 / FEAT-063 | Từ chối gợi ý cá nhân khi gate đóng; PER-03, PER-04; P1 gate-only | chỉ yêu cầu xem khả dụng, không nhận profile/consent sức khỏe | O-03 chưa mở và FEAT-047 gate-only: không gọi recommendation, không đọc/thu/suy luận hồ sơ; điều kiện mở ghi riêng, chưa xây luồng mở | CLOSED, lý do khả dụng chung; không gợi ý | BR-AIN-005, BR-AIN-014 | E9-Q14 |
| FR-AIN-LIMT-001 / FEAT-064 | Kiểm và giữ hạn mức lượt/ngân sách; Hệ thống; PER-08 giám sát; P0 | principal/group từ server, policyVersion, dự trù upper bound chi phí | Admission giữ chỗ nguyên tử lượt và ngân sách ngày; spentConfirmed + outstandingReserved + upperBound không vượt cap; unknown không bằng 0; mỗi bước tool/model cần quyền và budget lease còn hiệu lực | ADMITTED/QUOTA_BLOCKED/BUDGET_BLOCKED/UNKNOWN_BLOCKED | BR-AIN-008, BR-AIN-014 | E9-Q01, E9-Q07, E9-Q13 |
| FR-AIN-CONF-001 / FEAT-064 | Xem và đề nghị đổi hạn mức; PER-08 có quyền được cấp; P0 | group, policyVersion, giới hạn lượt, cap ngày/đơn vị/múi giờ, lý do | Kiểm quyền server; version và hiệu lực; nếu policy cần duyệt thì tạo đề nghị, tách người tạo/sửa cuối khỏi duyệt theo E1; chưa chốt policy không kích hoạt | Cấu hình/đề nghị và audit; không tự đặt số | BR-AIN-009, BR-AIN-014 | E9-Q07, E9-Q08, E9-Q13 |
| FR-AIN-SAFE-001 / FEAT-065 | Chặn truy cập dữ liệu kinh tế nội bộ; Hệ thống; P0 | mọi tool request, quyền và DTO đầu vào/ra | Deny by default ở registry, API, service identity, DB grants; projection allowlist đệ quy trước model và response; không cho quyền AIO qua hội thoại; chặn cost, giá nhập, cost %, khoản khoán, chiết khấu và suy ngược | Từ chối an toàn, event không payload nhạy cảm | BR-AIN-001, BR-AIN-006, BR-AIN-007, BR-AIN-012, BR-AIN-013 | E9-Q05, E9-Q13 |
| FR-AIN-MED-001 / FEAT-065 | Giữ ranh giới câu hỏi bệnh lý; Hệ thống; P0 | nội dung người dùng tại biên an toàn; không tạo hồ sơ | Chặn nhánh chẩn đoán/điều trị và cá nhân hóa sức khỏe; không hỏi thêm bệnh; nội dung nhắc bắt buộc chờ duyệt E9-Q09; không lưu raw sức khỏe hoặc đưa vào tool/model | Trạng thái ngoài phạm vi và placeholder lời nhắc chờ xác nhận | BR-AIN-005, BR-AIN-007, BR-AIN-010, BR-AIN-011 | E9-Q03, E9-Q09, E9-Q10, E9-Q14 |
| FR-AIN-LOG-001 / FEAT-064 | Đối soát lượt và chi phí AI; PER-08 có quyền được cấp; P0 | ngày/group, runRef, sự kiện usage có provenance | Đối soát theo run/event duy nhất, tách confirmed/estimated/unknown/reserved; không biến unknown=0; xem theo quyền không raw hội thoại; log AIN không đọc log AIO | Báo cáo quota/ngân sách AI và sai lệch chưa xử lý | BR-AIN-008, BR-AIN-011 | E9-Q07, E9-Q08, E9-Q10, E9-Q13 |

Lỗi áp theo điều kiện trong [catalog](../api/endpoint-catalog.json) và [ma trận](error-matrix.md); mọi FR kiểm quyền/scope và projection trước trả. GET của CHK chỉ đọc; worker là bên thực hiện kiểm, GET không chạy model/validator hay sinh dữ liệu. GATE không có POST gợi ý. SAFE/MED/LIMT là bước kiểm bắt buộc trong orchestration, không API để khách tự cấp quyền hoặc gọi model.

### FEAT-063: điều kiện mở, hiện chưa đạt

Gate chỉ được xét mở khi có quyết định O-03 có nguồn/phạm vi; FEAT-046/047 có đặc tả được duyệt về dữ liệu, consent, quyền/xóa và contract; xác nhận persona PER-03/PER-04 cùng identity được phép; review E9-Q14 và bằng chứng kiểm an toàn trước phát hành. Hiện không điều kiện nào được coi đã đạt chỉ vì có SRS nháp. Chưa thiết kế thuật toán, tiêu chí xếp hạng hoặc endpoint nhận hồ sơ/gợi ý. Khi đóng: chỉ trả CLOSED, không đọc/thu/suy luận sức khỏe, không gọi FEAT-047, không gán gợi ý hoặc tự thay lựa chọn/order. Mở gate trong tương lai cần phiên BA riêng có căn cứ, không bật bằng câu lệnh chat hay flag client.

## 3.2 BR

| Mã | Phạm vi | KHI → THÌ / ngoại lệ | Căn cứ |
| :--- | :--- | :--- | :--- |
| BR-AIN-001 | Mọi FR | KHI agent thay người dùng THÌ quyền là giao quyền chủ thể và svc-agent-dinh-duong-vien; guest chỉ sau Q02, kiểm từng request/tool và scope; không có ngoại lệ nâng quyền. | E1 BR-SEC-009/010; BN-16 |
| BR-AIN-002 | GEN/CHK/EDIT | KHI dựng hoặc chỉnh THÌ chỉ món/công thức đã duyệt/hiệu lực; chạy E2 FR-MENU-RUL-002 toàn phương án và cùng hash, nguồn/ruleVersion; vi phạm cứng/validator lỗi/nguồn thiếu không được VALID. | PRD 4.4; FEAT-061 |
| BR-AIN-003 | EXPL/CHK | KHI diễn giải THÌ dùng số hệ thống và provenance; giữ nhãn ước tính từ định lượng sống; thiếu khác 0; dị ứng chưa có khác không dị ứng; không tự tính cost/định lượng/dinh dưỡng. | E4; PRD 4.4 |
| BR-AIN-004 | SEND/STAT | KHI gửi nháp THÌ chỉ đề xuất, có lệnh xác nhận khách và receipt bền vững; người thật Gia Phát duyệt trước áp dụng. Không tự tạo menus/order/giá cam kết; chưa chọn điểm nhận giữ BLOCKED. | FEAT-062; E9-Q06 |
| BR-AIN-005 | GATE/MED | KHI O-03/FEAT-047 chưa mở THÌ gate063 đóng, không nhận profile/consent sức khỏe, không thu/suy luận; không thiết kế thuật toán. Mở gate cần quyết định có nguồn và review contract trước, không tự mở bằng config khách. | FEAT-063 dùng FEAT-047 |
| BR-AIN-006 | SAFE; mọi FR | KHI AIN chạy THÌ không có tool/quyền SELECT giá nhập, cost, cost %, dự toán, khoản khoán, chiết khấu; không alias/proxy AIO, SQL/HTTP tùy ý; prompt không thay ACL. Không ngoại lệ kể cả người hỏi có quyền cost nội bộ. | BN-16; E1 BR-SEC-010 |
| BR-AIN-007 | SAFE/EXPL/MED | KHI output/input đi qua biên THÌ allowlist lồng nhau và lọc trước model/UI/error/log/cache; cấm suy ngược từ giá suất/định lượng, hỏi gián tiếp, injection; text người dùng không thành chỉ dẫn hệ thống. Không lưu raw sức khỏe. | FEAT-065; E1 NFR-PRIV-002 |
| BR-AIN-008 | LIMT/LOG/CONF | KHI nhận lượt có chi phí THÌ reserve nguyên tử theo principal/group và cap ngày trước gọi; chi phí confirmed + reserve không vượt cap; thiếu upper bound/đơn vị/policy hoặc usage unknown không được giả định 0/hoàn chỗ. Retry không tăng lượt hai lần. | FEAT-064; R9; E9-Q07/13 |
| BR-AIN-009 | CONF | KHI đổi hạn mức THÌ kiểm quyền, version, ngày hiệu lực, audit trước/sau/lý do theo E1; cần duyệt thì tách người tạo/sửa cuối; cơ chế chưa quyết định không kích hoạt. Không hồi tố xóa chi phí. | E1 BR-SYS-001/002; E9-Q08 |
| BR-AIN-010 | MED; mọi FR | KHI có câu bệnh lý THÌ không chẩn đoán, không chế độ ăn điều trị; lời nhắc bắt buộc theo nội dung được xác nhận Q09; chưa có nội dung giữ runtime BLOCKED, không tự viết lời khuyên y tế. | PRD ngoài phạm vi; R9 |
| BR-AIN-011 | SESS/SEND/LOG | KHI xử lý dữ liệu cá nhân THÌ tối thiểu hóa, consent có phiên bản và quyền xem/xóa theo Q10; không gửi PII không cần thiết tới model. Retention chat không suy từ retention audit. | E1 NFR-PRIV-001/002 |
| BR-AIN-012 | Mọi FR | KHI tham chiếu kinh tế THÌ cost nguyên liệu gồm VAT phải trả NCC; không yêu cầu hóa đơn là cờ riêng, không VAT 0%; CK %/tiền suất khoản riêng theo đơn, không giảm tiền phải trả. AIN không được đọc các khoản đó. | Cost accounting; CK/DATA-COST/NFR-COST-002 giữ nguyên |
| BR-AIN-013 | CHK/EXPL | KHI kiểm gặp nhánh kinh tế THÌ chỉ biên tin cậy nội bộ xử lý; adapter không phát số/lý do/rule cost ra AIN. Hành vi vượt ngưỡng và CANH_BAO chờ Q05, không thay cổng MENU. Giá suất chỉ nếu nguồn public được duyệt Q04. | AIO-Q02; E8-Q03 |
| BR-AIN-014 | Mọi FR | KHI thiếu quyết định/nguồn THÌ nhánh đó BLOCKED; không đóng câu hỏi hoặc coi dữ liệu synthetic là nghiệm thu; E6/E7/E8 không đặc tả tiếp producer. | Chỉ dẫn người dùng 12/11/2026 |

## 3.3 Giao diện ngoài

[API/allowlist](../api/api-spec.md), [mapping](../api/data-mapping.md), [màn hình](../ui/screens.md). Phân tách control plane (quyền/quota/receipt) khỏi tool model được phép gọi; model không được tự gửi đề xuất. Không endpoint áp dụng MENU/order/báo giá, không CRM CRUD.

## 3.4 NFR

| Mã | Yêu cầu đo/kiểm | Gate / test |
| :--- | :--- | :--- |
| NFR-AIN-001 | 0 lần lộ dữ liệu kinh tế nội bộ ở tool/model/API/UI/error/log/cache; quyền DB không SELECT bảng cấm; kiểm trực tiếp và gián tiếp, không chỉ prompt | TC-AIN-S01–S05; R9-COST |
| NFR-AIN-002 | 100% thực đơn trả về trong bộ30 đạt quy tắc cứng; mọi revision có E2 evidence cùng hash và nguồn; 0 món ngoài danh mục đã duyệt | DL-01/O-02; R9-MENU; S06 |
| NFR-AIN-003 | 20 câu bệnh lý:100% có lời nhắc được duyệt, không chẩn đoán/điều trị; 0 hồ sơ sức khỏe phát sinh | Q09/Q10; R9-MED; S07 |
| NFR-AIN-004 | Tổng chi phí AI mỗi ngày không vượt trần đã đặt; bao gồm retry/lượt lỗi/đến muộn theo policy; 0 double charge/oversubscription trong admission đồng thời | Q01/07/13; R9-BUDGET; S08/S09 |
| NFR-AIN-005 | 100% ACK proposal có record+source+revision+receipt bền vững; 100% thay cấu hình có audit; replay không tạo trùng | Q06/13; S10 |
| NFR-AIN-006 | Không raw sức khỏe/secret trong log; consent trước dữ liệu cá nhân; quyền xem/xóa theo nền ≤72 giờ cho yêu cầu xóa dữ liệu cá nhân, phạm vi chat/provider/backups chờ Q10; không tự đặt retention | Q10/O-04; S11 |
| NFR-AIN-007 | Kế thừa nền 1000 người đồng thời, p95 đọc≤300ms/ghi≤800ms; AI ngoài luồng web, tín hiệu đầu≤5s và thực đơn≤60s theo NFR-PERF-003, không stream candidate chưa kiểm. Profile riêng R9/queue và deadline wire chờ Q13 | Không mượn 20 ca R5 làm30 ca R9; S12 |
| NFR-AIN-008 | 360/390/1440px không tràn toàn trang, nhãn và focus bàn phím; WCAG2.1AA theo nền, chưa audit đầy đủ | S13; kiểm mock UI riêng |
| NFR-AIN-009 | TLS≥1.2 ưu tiên1.3 theo nền; không secret client; quyền kiểm từng request/tool và thu hồi; tách service account/DB grants/queue/quota AIO-AIN | Q01/02; S01/S02/S11 |

## 3.5 Lỗi và 4. Phụ lục

[Ma trận lỗi](error-matrix.md) · [states](states.md) · [từ điển](data-dictionary.md) · [UC](../usecases/index.md) · [RTM](../test/traceability.md). BLOCKED là trạng thái thiết kế, không HTTP status. Không tuyên bố kiểm tài liệu/UI thay nghiệm thu hệ thống.
