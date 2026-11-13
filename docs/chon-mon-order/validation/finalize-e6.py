from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];D=B.parent
def write(p,title,body):
 f=B/p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(f'---\nid: DOC-E6-{p.upper().replace("/","-").replace(".MD","")}\ntitle: {title}\nversion: 0.2.0\nphase: Specification\ndomain: Gia Phát\nauthor: BA\nlast_updated: 2026-11-11\n---\n# {title}\n\nDraft · 11/11/2026 · Chưa phê duyệt nghiệp vụ / chưa triển khai backend.\n\n'+body+'\n',encoding='utf-8')
def replace(p,old,new):
 f=D/p;s=f.read_text(encoding='utf-8');s=s.replace(old,new);f.write_text(s,encoding='utf-8')
def add(p,s):
 f=D/p;f.write_text(f.read_text(encoding='utf-8')+'\n'+s+'\n',encoding='utf-8')
write('ui/screen-catalog.md','Danh mục 13 màn wireframe E6','''[Mở wireframe tương tác](../html-wireframe/order-workbench.html). Tất cả dữ liệu là **synthetic**; trạng thái chỉ trong bộ nhớ; không gọi backend. Màn 06 mô phỏng một lựa chọn độc lập; màn 08–13 dùng fixture gộp S=60 để review số suất, không giả hai fixture là cùng dữ liệu thật. Màn setup chủ yếu minh họa gate và quyền, không CRUD đầy đủ.

| Screen | Tên / actor | Feature / UC | Nhánh mô phỏng / giới hạn |
| :--- | :--- | :--- | :--- |
| UI-ORD-01 | Cấp tài khoản / quản trị khách | FEAT-030 / UC-ORD-001 | lý do thiếu, khác khách, preview quyền; chưa tạo account |
| UI-ORD-02 | QR / người ăn | FEAT-031/032 / UC-ORD-002/003 | account/guest, token revoked; identity policy chưa chốt |
| UI-ORD-03 | Quản lý QR/người / người đặt tổng | FEAT-033 / UC-ORD-004 | rotation/removal và cảnh báo bảo toàn lịch sử |
| UI-ORD-04 | Phục vụ / DDV | FEAT-034 / UC-ORD-005 | xem bếp/ca, tác động snapshot; chưa CRUD lịch |
| UI-ORD-05 | Định mức/mode / người đặt tổng | FEAT-035/044 / UC-ORD-006/015 | nhãn quota, mode pending; không tự áp chính sách |
| UI-ORD-06 | Chọn ngày/xem món / người ăn | FEAT-036/045 / UC-ORD-007/016 | bằng/vượt 1đ, đổi, replay, thiếu nguồn, khóa, empty/offline/stale |
| UI-ORD-07 | Chọn tuần / tài khoản | FEAT-037 / UC-ORD-008 | policy chưa chốt; giả định atomic/partial; guest403 |
| UI-ORD-08 | Chốt tổng / người đặt tổng | FEAT-038 / UC-ORD-009 | T<S+C; T=S+C; preview/confirm/quay lại; chưa chốt ORD-Q06 |
| UI-ORD-09 | Job khóa/nhắc / vận hành | FEAT-039/040/043 / UC-ORD-010/011/014 | thiếu total/default, retry, nhắc gated; không provider |
| UI-ORD-10 | Đổi sau khóa / người đề nghị và duyệt | FEAT-041 / UC-ORD-012 | pending, tự duyệt, gate policy, approve/reject/replay |
| UI-ORD-11 | Nhập hộ / DDV | FEAT-042 / UC-ORD-013 | source/evidence/reason, sau hạn sang đề nghị; không gửi Zalo |
| UI-ORD-12 | Gate sức khỏe / người ăn | FEAT-046/047 / UC-ORD-017/018 | chỉ thông báo chưa mở; không form sức khỏe |
| UI-ORD-13 | Phiếu bếp / bếp | FEAT-048 / UC-ORD-019 | version cũ/mới, tổng MAIN và delta mẫu; chưa phân rã món phụ |

Desktop: sidebar + nội dung; mobile: thanh màn cuộn riêng, form một cột; có label, focus, aria-live, modal xác nhận. Test UI chỉ chứng minh hành vi mô phỏng đã kiểm, không chứng minh quyền/transaction/backend thực.
''')
write('test/checklist.md','Checklist review và kiểm thử E6','''- [ ] BA xác nhận nguồn D-04/D-14/D-19/D-21 và 14P0/5P1; không mở rộng E7–E13.
- [ ] Chủ sản phẩm trả ORD-Q01–15, Q-14/Q-16/O-06 và giữ O-03 chặn FEAT-046/047 khi chưa có bằng chứng.
- [ ] Tech lead review scope user/guest/service, token revocation, persistent dedupe, envelope E1-Q01, schema delta.
- [ ] QA review [57 AC/test](review-test-cases.md), [10 ca gốc](test-cases.md) và [ca hệ thống](system-test-cases.md); loại trùng mục tiêu khi lập test run.
- [ ] Kiểm S/C/T/D và toàn tổ hợp; không dùng registered count làm total, không dùng số món làm số suất.
- [ ] Race writer/lock/approval; rollback; mất response; duplicate/out-of-order event; nguồn MENU bị thu hồi.
- [ ] UI desktop/mobile, keyboard, dialog, empty/error/loading/unknown result, old plan version và missing nutrition.
- [ ] Security IDOR/guest scope/allowlist; không lộ cost/PII/token; không thu sức khỏe gated.
- [ ] Regression VAT phải trả/không hóa đơn/chiết khấu riêng; NFR-COST-002; CK và DATA-COST giữ nguyên.
- [ ] Khi có backend: 1000 CCU trong10 phút,0 mất/trùng; pilot2 khách/2tuần theo roadmap. Chưa đánh dấu đạt.
''')
write('test/system-test-cases.md','Ca hệ thống và tích hợp E6','''Toàn bộ fixture synthetic; **Actual/Evidence: chưa có**. Các bước chạy cần môi trường backend và quyền đọc evidence test, không chạy trên dữ liệu thật. Mã NFR/BR/lỗi tham chiếu [SRS](../srs/spec.md) và [quy tắc chi tiết](../srs/operational-rules.md).

| TC | Truy vết | Tiền điều kiện / bước thực hiện | Expected | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-E6-SYS-01 | NFR-ORD-001; FR-ORD-SEL-001 | Seed 1000 identity hợp lệ/2 khách; chạy đọc/chọn/đổi/retry trong10phút trước deadline; lưu response latency và đối chiếu DB | p95 đọc≤300ms/ghi≤800ms;0 lựa chọn thành công mất/trùng; không đồng nhất CCU với TPS | BLOCKED profile tải/ORD-Q01/Q-16/môi trường |
| TC-E6-SYS-02 | NFR-ORD-002; BR-ORD-002/004 | Hai PUT cùng version + job khóa cùng scope tại deadline; ghi thứ tự transaction | Một writer hợp lệ hoặc job thắng; không write sau guard khóa; sum counter=selection; snapshot một lần | BLOCKED ORD-Q07 |
| TC-E6-SYS-03 | NFR-ORD-002; PORT-LOCK | Crash sau commit order/outbox trước publish plan; khởi động worker và replay event | Order vẫn LOCKED; plan được tạo một lần; không mở lại order hoặc tạo v2 do retry | NOT RUN |
| TC-E6-SYS-04 | BR-ORD-008; FR-PLAN-MEAL-001 | A rev2 và B rev2 phát đồng thời; replay A rev1 đến muộn | Plan giữ revision mới nhất của cả A/B; không lost update, không rollback bởi event cũ | BLOCKED ORD-Q10/14 |
| TC-E6-SYS-05 | NFR-ORD-003; BR-ORD-006 | Client A đổi mọi id/filter sang B; thử guest/day khác; kiểm JSON,error và log hiển thị | 404/403 theo scope;0 cost,giá nhập,chiết khấu/PII ngoài quyền | NOT RUN |
| TC-E6-SYS-06 | BR-ORD-010; FR-ORD-SEL-001 | MENU WITHDRAWN sau GET trước PUT; thử lock order cũ | PUT409; không dùng nguồn thu hồi cho lock; lịch sử giữ, workflow xử lý chờ policy | BLOCKED ORD-Q12 |
| TC-E6-SYS-07 | BR-ORD-005; FR-ORD-CHG-001 | Lỗi ghi audit giữa approve; đọc order,approval,outbox | Rollback tất cả; không revision/plan giả thành công; retry cùng key đối soát | NOT RUN |
| TC-E6-SYS-08 | BR-ORD-012; FR-ORD-REM-001 | Người ăn chọn sau khi job lập recipient trước gửi; kênh tắt hoặc duplicate event | Kiểm lại điều kiện trước gửi; không nhắc sai/không gửi khi kênh tắt; dedupe | BLOCKED Q-14/E1-Q04 |
| TC-E6-SYS-09 | FR-NUTR-DSP-001; BR-ORD-006 | NUTR trả incomplete hoặc có internal breakdown; adapter tạo SafeDish | totals=null + missing; allowlist không lộ breakdown giá/cost; nhãn ước tính | NOT RUN |
| TC-E6-SYS-10 | FR-ORD-CHG-001; Cost CK-Q07 | Order đổi số suất sau khóa, có pricing snapshot và discount record synthetic | Giữ snapshot cũ; liên kết revision mới rõ; khoản chiết khấu cần review, không tự trừ amountDue | BLOCKED CK-Q07/ORD-Q08 |
| TC-E6-SYS-11 | FR-ORD-SEL-001; ERR-ORD-409-02/500-01 | Mất response PUT; retry key/body cũ rồi key cũ/body khác, crash trước commit | Replay resource cũ; khác body409-02; trước commit không lưu dữ liệu một phần | NOT RUN |
| TC-E6-SYS-12 | R6 / FR-ORD-SUB-001/DEF-001/PLAN-MEAL-001 | Pilot2 khách2tuần; ghi tổng, lựa chọn, mặc định, khóa, thay đổi và phiếu bếp hàng ngày | 100% phần chưa chọn về default khi đủ điều kiện; vượt định mức bị chặn; đối chiếu nguồn/revision; exception không bị che | BLOCKED G-Now/dữ liệu thật/môi trường |

57 ca mới +10 ca gốc +12 ca hệ thống là **79 mô tả test**, không phải79 mục tiêu độc lập; có overlap. Không có test backend đã chạy, không dùng kết quả kiểm HTML làm actual các ca trên.
''')
write('review/dependencies.md','Hợp đồng phụ thuộc và điểm cần đồng bộ','''| Miền / nguồn | E6 dùng gì | Tác động / ràng buộc |
| :--- | :--- | :--- |
| [Nền tảng](../../nen-tang/srs/spec.md), [schema](../../nen-tang/srs/schema.dbml) | Phiên, authorize, audit, params, files, jobs | users.customer_id và user_type SERVICE đã có; thiếu scope nhiều điểm/guest session và policy binding. Không nói SERVICE hoàn toàn chưa có; ORD-Q11/E1-Q02/04 |
| [MENU](../../thuc-don-dinh-luong/srs/spec.md) | PUBLISHED, default MAIN, recipe/price version, WITHDRAWN | ORD-Q04/12 xử lý nguồn thay; không vượt cổng MENU; FR-MENU-RCP-007 giữ BLOCKED O-02 |
| [Cost](../../cost/srs/spec.md), [kế toán](../../cost/accounting/business-rules.md) | Kiểm định mức theo giá bán/cơ cấu; tham chiếu pricing snapshot | Không lộ cost người ăn; không tạo nguồn giá song song. VAT cost phải trả; invoice flag riêng; chiết khấu riêng không giảm phải trả. CK-Q01–10, DATA-COST-Q01–06 không đóng; chưa10món/10ngày thật |
| [Dinh dưỡng](../../dinh-duong/srs/spec.md) | 4 chỉ số và provenance qua safe adapter | Missing không0; nhãn ước tính định lượng sống; NUTR-Q03/04 còn mở. Không dùng dung sai Cost cho dinh dưỡng |
| [Agent Nội bộ](../../agent-noi-bo/srs/spec.md) | Nguồn DRAFT MENU gián tiếp | Agent không chọn/chốt/duyệt order; E6 chỉ đọc MENU sau công bố, không lấy candidate VALID thay PUBLISHED |

Đã thêm liên kết ngược từ SRS E1–E5 và ERD nền tới gói E6. Không sửa công thức Cost, schema DBML, CK/DATA-COST hoặc thuật toán Agent. API/port đều đề xuất, chưa server hoặc migration. NFR-COST-002 giữ cost món≤1đ và cost% ngày≤0,01 điểm phần trăm.
''')
# Correct overly broad schema wording after inspecting actual existing SERVICE user type.
replace('chon-mon-order/srs/data-dictionary.md','Phải bổ sung scope khách/điểm và guest; không giả user_roles đã có customer_id','users.customer_id và user_type SERVICE đã có; cần scope nhiều điểm/guest và policy binding, không giả user_roles đã có customer_id')
replace('chon-mon-order/srs/data-dictionary.md','Không chứa được guest/service không user một cách tự nhiên','Service có thể tham chiếu users loại SERVICE; guest không user chưa có cách audit trực tiếp')
replace('chon-mon-order/srs/operational-rules.md','log actor service cần delta ORD-Q11','log actor service gắn users loại SERVICE; guest principal cần review ORD-Q11')
replace('chon-mon-order/html-wireframe/order-workbench.html',"'\\nMAIN tổng '+p.total+' suất · delta '","'\\nMón A (MAIN, recipe SYN-A, STD): '+p.total+' suất; B=0; C=0 · delta A '")
# Update current-state prose without deleting revision history.
replace('chon-mon-order/srs/spec.md','Phạm vi chưa đủ chi tiết để triển khai: câu hỏi/gated được ghi từng dòng; chưa có API đủ19 feature, UI, toàn bộ AC hoặc UAT. Không tự coi mọi tính năng E6 đã bao phủ SRS hoàn chỉnh.','Gói v0.2 có UC/API/data/UI/AC/test và RTM để review; nghiệp vụ còn gate nên chưa đủ điều kiện triển khai toàn bộ. FEAT-046/047 chỉ đặc tả cổng chặn, chưa đặc tả thu sức khỏe/gợi ý.')
replace('chon-mon-order/srs/spec.md','Tiếp theo cần use case chi tiết từng nhóm, API đầy đủ, wireframe, AC mỗi story và RTM toàn bộ19feature; không lấy các ca trọng yếu làm bộ test đủ E6.','Chi tiết bổ sung: [quy tắc vận hành](operational-rules.md), [UC](usecase-diagram.md), [data dictionary](data-dictionary.md), [RTM](../test/traceability.md), [wireframe](../html-wireframe/order-workbench.html), [AC](../userstories/acceptance-criteria.md). Các câu hỏi mở vẫn chặn baseline/triển khai; không lấy số liên kết làm độ hoàn tất nghiệp vụ.')
replace('chon-mon-order/srs/spec.md','SRS khởi đầu E6','SRS E6 để review')
replace('chon-mon-order/srs/spec.md','Ma trận đầy đủ phải bổ sung khi thiết kế API phần còn lại.','Ma trận hợp nhất nằm tại [quy tắc vận hành mục7](operational-rules.md).')
replace('chon-mon-order/epic-spec.md','E6: Chọn món và Order: gói khởi đầu','E6: Chọn món và Order: gói BA để review')
replace('chon-mon-order/epic-spec.md','Gói này **khởi đầu đặc tả**, chưa hoàn tất toàn bộ chuỗi13 loại tài liệu của epic.','Gói v0.2 có đầy đủ nhóm tài liệu review: UC, flow/state/data, API, wireframe, backlog/AC/test, RTM và preview; còn các gate chưa được phê duyệt.')
add('chon-mon-order/epic-spec.md','## Bổ sung v0.2.0\n\n[Preview](preview.html) · [Scope assessment](review/scope-assessment.md) · [Bàn giao](review/handoff.md) · [Báo cáo kiểm tra](validation/report.md). 19UC,57AC,26HTTP endpoint,2port,13màn wireframe; 2 feature O-03 chỉ có gate. Giữ10ca gốc, bổ sung57ca theoAC và12ca hệ thống; không có kết quả kiểm thử backend.')
write('gap-analysis.md','Khoảng trống sau gói E6 review','''Đã bổ sung cấu trúc review cho19 capability:19UC,57AC,26HTTP endpoint,2port,13màn,RTM feature→FR→UC→API/data/UI→story→AC→test. **Độ phủ liên kết19/19; 17 thiết kế có điều kiện,2 gate O-03. Không phải19 tính năng hoàn tất.**

| Khoảng trống | Tác động / công việc còn lại |
| :--- | :--- |
| ORD-Q01–10 vẫn chờ; mới ORD-Q11–15 | Chốt identity, scope, S/C/T, tuần, deadline, sửa khóa, phân rã plan; ghi bằng chứng trước sửa trạng thái |
| FEAT-046/047 O-03 | Chưa contract ghi/happy path sức khỏe; chỉ gate. Không đánh dấu API/data đầy đủ cho hai feature |
| Schema delta chưa merge | Tech lead review các quan hệ/unique/audit/snapshot/outbox và cập nhật DBML sau quyết định; không migration phiên này |
| Wireframe mô phỏng | Setup/registry là preview và gate; plan chỉ fixture MAIN, chưa phân rã side; backend quyền/race/idempotency chưa kiểm |
| NFR/pilot chưa có môi trường/dữ liệu | 1000CCU,2khách2tuần, G-Now chưa đạt bằng evidence; không chuyển ca NOT RUN/BLOCKED sang PASS |
| E1–E5 còn gate | Giữ O-02, CK/DATA-COST, NUTR/AIO và E1-Q; không mở E7–E13 |

[Bàn giao](review/handoff.md) · [Câu hỏi](review/questions.md) · [Kiểm tra](validation/report.md).
''')
for domain in ['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo']:
 add(domain+'/srs/spec.md','## Liên kết phụ thuộc E6: bổ sung 11/11/2026\n\n[Gói E6 để review](../../chon-mon-order/preview.html) · [Hợp đồng phụ thuộc](../../chon-mon-order/review/dependencies.md) · [Đối chiếu schema](../../chon-mon-order/srs/data-dictionary.md). E6 giữ nguồn công bố/quyền và quy tắc của phân hệ này; delta chưa merge, không thay gate hoặc chứng minh phần mềm đã triển khai.')
add('nen-tang/srs/erd.md','## Rà soát delta E6 ngày 11/11/2026\n\n[Data dictionary E6](../../chon-mon-order/srs/data-dictionary.md) chỉ rõ khoảng trống QR/scope, revision order/plan, quan hệ pricing và invariant MAIN. DBML vẫn65bảng và không thay trong phiên; delta chưa phê duyệt/chưa migration. users loại SERVICE đã có, guest session/audit cần ORD-Q11; eater_health_profiles có trong schema không mở O-03.')
for f in ['gia-phat/01-prd.md','gia-phat/02-roadmap.md']:
 replace(f,'[E6 khởi đầu](../chon-mon-order/epic-spec.md) chưa phải đặc tả hoàn chỉnh hoặc release đã làm','[E6 gói review v0.2](../chon-mon-order/preview.html) đã bổ sung UC/API/UI/AC/RTM; còn gate nghiệp vụ và chưa triển khai release')
 add(f,'## Cập nhật hồ sơ E6 ngày 11/11/2026\n\n[Bàn giao E6](../chon-mon-order/review/handoff.md): giữ14P0/5P1 và G-Now/R6; 17capability có thiết kế có điều kiện, FEAT-046/047 chỉ gate O-03. Không đổi ưu tiên/ngày release; ORD-Q01–15 chờ xác nhận. Độ phủ liên kết tài liệu không phải phần mềm hoặc UAT.')
replace('gia-phat/00-ke-hoach-tong-the.md','[`chon-mon-order`: khởi đầu](../chon-mon-order/epic-spec.md)','[`chon-mon-order`: gói BA review](../chon-mon-order/preview.html)')
add('gia-phat/00-ke-hoach-tong-the.md','## Cập nhật E6 ngày 11/11/2026\n\nHoàn thiện gói tài liệu để review theo [bàn giao E6](../chon-mon-order/review/handoff.md), chưa chốt baseline hoặc release. Có UC/flow/state/data/API/wireframe/story/AC/test/RTM/preview. ORD-Q01–15 và O-03 còn chờ; delta schema không merge; không triển khai backend/E7–E13. Các nhãn gói khởi đầu trong lịch sử là mốc trước phiên này.')
replace('gia-phat/brainstorms/pham-vi-san-pham.md','E6 mới có gói khởi đầu; E7–E9 chưa có SRS riêng','E6 có gói BA review v0.2 còn gate; E7–E9 chưa có SRS riêng')
replace('gia-phat/brainstorms/pham-vi-san-pham.md','[ORD-Q01–10]','[ORD-Q01–15]')
replace('OVERVIEW.md','[Gói khởi đầu](chon-mon-order/epic-spec.md):19FR capability,5endpoint trọng yếu,10ca,10câu hỏi | Chưa UC/API/UI/AC/RTM đầy đủ; chưa backend; O-03 gated','[Gói review v0.2](chon-mon-order/preview.html):19UC,57AC,26endpoint,13màn,RTM | 17capability có điều kiện;2gate O-03; ORD-Q01–15 chờ; chưa backend')
add('OVERVIEW.md','## Hoàn thiện gói E6 để review ngày 11/11/2026\n\n[Preview E6](chon-mon-order/preview.html) · [Báo cáo kiểm tra](chon-mon-order/validation/report.md) · [Bàn giao](chon-mon-order/review/handoff.md). Đã bổ sung19UC,57AC,26HTTP endpoint,2port,13màn vàRTM19feature. Giữ10ca gốc, thêm57ca theoAC và12ca hệ thống; không cộng thành79 mục tiêu độc lập. 17capability có thiết kế có điều kiện,2feature chỉgate O-03. ORD-Q01–10 không đóng, bổ sung ORD-Q11–15; schema65bảng không thay. Chưa backend/migration/UAT. Các mục “E6 khởi đầu” phía trên là mốc lịch sử, không phản ánh inventory hiện tại. Tiếp theo review E6 trước mở E7–E13.')
replace('project-dashboard.md','E6 đã bắt đầu với19capability, chưa bộ đặc tả hoàn chỉnh; không cộng19 vào mức hoàn tất BA.','E6 có gói review19capability:17thiết kế có điều kiện và2gate; không cộng19 vào mức hoàn tất BA được phê duyệt.')
replace('project-dashboard.md','E6:10 câu hỏi mới; còn UC/API/UI/AC/RTM đầy đủ; O-03 gated hồ sơ/gợi ý sức khỏe.','E6: ORD-Q01–15 chờ; đã có UC/API/UI/AC/RTM để review; O-03 vẫn gated hồ sơ/gợi ý sức khỏe.')
replace('project-dashboard.md','[E6 khởi đầu](chon-mon-order/epic-spec.md)','[E6 review](chon-mon-order/preview.html)')
add('project-dashboard.md','## Inventory E6: gói review v0.2\n\n| Feature | UC/story | AC | HTTP/port | UI | Test design | Trạng thái |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n|19(14P0/5P1)|19/19|57|26/2|13màn trong1HTML|57mới +10gốc +12hệ thống có overlap|0test backend;17thiết kế có điều kiện,2gate O-03|\n\n[Bằng chứng](chon-mon-order/validation/report.md) · [RTM](chon-mon-order/test/traceability.md). Schema65bảng không đổi. Mọi số là inventory tài liệu, không tăng tỷ lệ phần mềm hoàn tất.')
for f,link in [('gia-phat/review/ba-completion-handoff.md','../../chon-mon-order/review/handoff.md'),('gia-phat/validation/completion-report.md','../../chon-mon-order/validation/report.md')]:
 add(f,'## Bổ sung tiếp nối E6 ngày 11/11/2026\n\nMô tả E6 khởi đầu trong báo cáo này là mốc lịch sử. [Gói E6 v0.2 mới]('+link+') bổ sung19UC,57AC,26HTTP endpoint,2port,13màn vàRTM; các gate vẫn mở, schema65bảng không đổi, chưa backend/UAT. Dùng báo cáo E6 để xem bằng chứng kiểm riêng; không ghi đè kết quả46sơ đồ/12màn của E1–E5.')
# Renderer clone: same rendering approach, but confined to E6 and its evidence directory.
src=(D/'gia-phat/validation/render-review.cjs').read_text(encoding='utf-8')
src=src.replace("const folders=['nen-tang','thuc-don-dinh-luong','cost','dinh-duong','agent-noi-bo'];","const folders=['chon-mon-order'];")
(B/'validation/render-e6.cjs').write_text(src,encoding='utf-8')
