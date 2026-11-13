from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]
items=[
('Chuẩn hóa giá mua','kế toán mua hàng','nhập giá báo theo cách ghi VAT','cost dùng đúng số phải trả','FR-ACC-001','API-COST-005/006/007/012/013/014; API-ACC-001','ingredient_prices','SCR-ACC-01','P0','3','Rounding giá mua; policy migration',[
('Giá hai cách ghi cho cùng cost','100000 EXCLUSIVE VAT8% và108000 INCLUSIVE, có nguồn','preview rồi tạo hai fixture độc lập','cùng giá cost108000;70g cùng7560, không cộng VAT hai lần'),
('Thiếu VAT và phần lẻ','EXCLUSIVE thiếu rate/amount; fixture khác quote1 rate8%','thử commit','không ghi giá ở cả hai; báo thiếu VAT hoặc rounding-unresolved, không tự làm tròn'),
('Lô nguyên tử và legacy','lô2 dòng một dòng UNKNOWN; lịch sử giá legacy có snapshot','kiểm/commit lô và đọc lịch sử','không ghi lô; legacy gắn cờ, snapshot không bị chuẩn hóa lại')]),
('Context giá và hóa đơn','kế toán được cấp quyền','xem điều kiện giá chụp theo đơn','không nhầm yêu cầu hóa đơn với thuế suất','FR-ACC-002','API-ACC-002','order_pricing_snapshots','SCR-ACC-02','P0','3','Sale context và quyền mới',[
('Cờ hóa đơn độc lập','đơn100×40000 đã gồmVAT8%; context đầy đủ','đổi cờ hóa đơn trên hai fixture trước chụp','amountDue đều4000000; revenueExVat=4000000/1.08, không đổi do cờ'),
('Không suy diễn doanh thu','priceBasis UNKNOWN hoặc VAT chưa rõ','đọc context','UNRESOLVED; revenueExVat=null; không trả doanh thu0 hoặc gross giả là net'),
('Phạm vi order/snapshot','kế toán chỉ kháchA; orderB ngoài quyền','gọi contextB và gán snapshotB cho draftA','404 ngoài scope hoặc409 snapshot không thuộc order; không lộ dữ liệuB')]),
('Tính thử khoản riêng','kế toán được cấp quyền','xem chiết khấu riêng trước khi ghi','kiểm số mà không thay tiền đơn','FR-ACC-003','API-ACC-003','Không ghi; đọc order_pricing_snapshots','SCR-ACC-03','P0','3','CK-Q01/02/03/04/10',[
('Hai cách tính','đơn100×40000; giả định base GROSS;5% hoặc2000/suất','tính từng cách','khoản thử200000;amountDue4000000;canConfirm=false, chưa thanh toán'),
('Basis chưa chốt','PERCENT5% nhưng baseUNRESOLVED','preview','calculatedAmount=null và câuCK-Q01; không thay bằng0'),
('Không cộng hai kiểu','request có cả ratePct và amountPerServing','preview','422; không tự cộng hai khoản; preview không ghi order/draft')]),
('Lưu bản nháp khoản riêng','kế toán được cấp quyền','lưu điều kiện chiết khấu theo đơn','review và truy lại điều kiện','FR-ACC-004','API-ACC-004/005/006','order_discount_records; order_discount_events','SCR-ACC-03/04','P0','3','CK-Q04; chưa duyệt/chi trả',[
('Lưu draft có lịch sử','snapshot đúng version, fixed2000×100, keyK','tạo draft','DRAFT khoản thử200000;event DRAFT_CREATED;amountDue không đổi'),
('Retry không tạo trùng','draft đã commit nhưng phản hồi mất','retry cùng key/hash; sau đó khác hash','lần cùng trả bản cũ; khác hash409; chỉ một draft/event tạo'),
('Không vượt gate','draft tồn tại, CK chưa trả lời','gửi statusCONFIRMED hoặc gọi thao tác thanh toán','không chuyển trạng thái/không ghi thanh toán; thiếu quyền bị403')]),
('Thỏa thuận giá nháp','kế toán được cấp quyền','ghi cách báo giá và yêu cầu hóa đơn khách','chuẩn bị dữ liệu hợp đồng có nguồn','FR-ACC-005','API-ACC-007/008','customer_price_terms','SCR-ACC-02','P0','3','Quyền terms và activation sales policy',[
('Nháp chưa đủ vẫn thể hiện thiếu','kháchA,mealType1,quote40000,basisUNKNOWN,invoice=false,rate=null','tạo term draft','DRAFT; không kích hoạt; không tự gánrate0'),
('Khoảng ngày sai','effectiveTo trước effectiveFrom','lưu','422 và không tạo term'),
('Không hồi tố context','term draft mới của khách; order cũ có snapshot','sửa điều kiện tương lai','snapshot order cũ giữ nguyên; không tự đổi tiền phải trả')]),
('Đơn đổi cần rà lại','kế toán được cấp quyền','biết khoản riêng chịu ảnh hưởng khi đơn đổi','không dùng nhầm số lượng cũ để chi trả','FR-ACC-006','Sự kiện nội bộ order.changed','order_discount_records; order_discount_events; order_pricing_snapshots','SCR-ACC-04','P0','3','CK-Q07/08/09; chỉ cơ chế đánh dấu review',[
('Đổi số suất','draft dựa trênorder v1=100suất;order v2=80suất','xử lý order.changed một lần','draft NEEDS_REVIEW; giữ giá trị cũ để so, không tự sửa200000 thành160000 và không chi tiền'),
('Sự kiện lặp','eventKeyE đã xử lý','nhận E lần hai','không thêm event duplicate, không nhân khoản chiết khấu'),
('Hủy khi chưa rõ chính sách','order bị hủy; khoản đang cần review','worker nhận sự kiện','giữ dấu vết, yêu cầuCK-Q08/09; không xóa khoản hoặc tự thu hồi/bù trừ')])]
data=[];md='# Backlog kế toán mở rộng\n\nPhiên bản0.1.0 ·11/11/2026 · Draft, phụ thuộc CR-COST-2026-001.\n\n| Phiên bản | Ngày | Nội dung |\n| :--- | :--- | :--- |\n| 0.1.0 | 2026-11-11 | 6 story,18 AC/test bổ sung thiết kế; không gộp vào45 FR Cost gốc |\n\n'
md+='Ưu tiên P0 là đề xuất bên trong extension khi được đưa vào release, không tự thêm vào R3. SP là sơ bộ3/story, đội dev phải ước lượng lại. FR-ACC-001–006 là mã yêu cầu thiết kế mới, chưa nâng thành yêu cầu baseline đã được chủ sở hữu duyệt. Các quyền mới chưa cấp; story không sẵn sàng triển khai production trước gate. [Hợp đồng](../api/accounting-contract.md), [mô hình](../../nen-tang/srs/erd.md), [wireframe](../html-wireframe/accounting-workbench.html), [CK câu hỏi](../accounting/business-rules.md).\n\n'
tc='# AC và test thiết kế kế toán\n\nPhiên bản0.1.0 ·11/11/2026 ·18 ca, chưa chạy backend. Khác12 ca TC-ACC-001–012: bộ này truy vết hợp đồng/dữ liệu/UI; không cộng hai bộ thành số ca độc lập đã nghiệm thu.\n\n'
for n,item in enumerate(items,1):
 title,actor,want,why,fr,api,tables,screen,priority,sp,gate,cases=item;sid=f'US-ACC-{n:03}'
 entry=dict(id=sid,fr=fr,api=api,tables=tables,screen=screen,gate=gate,cases=[])
 md+=f'## {sid}: {title}\n\nLà một {actor}, tôi muốn {want} để {why}.\n\n| Trường | Nội dung |\n| :--- | :--- |\n| FR / ưu tiên / SP sơ bộ | {fr} / {priority} / {sp} |\n| API | {api} |\n| Dữ liệu | {tables} |\n| Màn | {screen} |\n| Gate | {gate} |\n| AC/test | [AC và test](../accounting/design-tests.md), nhóm {sid} |\n\n'
 tc+=f'## {sid}: {fr}\n\nNguồn: {api}; {tables}; {screen}. Gate: {gate}.\n\n'
 for j,(title,g,w,t) in enumerate(cases,1):
  aid=f'AC-ACC-D{n:02}-{j:02}';tid=f'TC-ACC-D{n:02}-{j:02}'
  entry['cases'].append(dict(id=tid,ac=aid,given=g,when=w,then=t,status='BLOCKED_POLICY_OR_ENVIRONMENT'))
  tc+=f'### {tid}: {title}\n\n```gherkin\nScenario: {aid}\n  Given {g}\n  When {w}\n  Then {t}\n```\n\nBước QA: tạo fixture trên ở môi trường test; gọi API hoặc sự kiện đúng version; kiểm response và bản ghi trước/sau, quyền, audit. Expected: Then ở trên. Trạng thái: **BLOCKED ({gate}); chưa có môi trường/backend**. Actual/evidence/defect: Chưa chạy / chưa có / chưa có.\n\n'
 data.append(entry)
(B/'userstories/accounting-backlog.md').write_text(md,encoding='utf-8')
(B/'accounting/design-tests.md').write_text(tc,encoding='utf-8')
(B/'accounting/design-catalog.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('6 extension stories;18 design scenarios')
