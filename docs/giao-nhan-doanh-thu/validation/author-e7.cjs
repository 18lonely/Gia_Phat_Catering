const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../../..'),base=path.join(root,'docs/giao-nhan-doanh-thu');
function walk(p){return fs.readdirSync(p,{withFileTypes:true}).flatMap(x=>x.isDirectory()?walk(path.join(p,x.name)):[path.join(p,x.name)]);}
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const baseline=path.join(__dirname,'protected-baseline.json');
if(fs.existsSync(baseline))throw Error('Initial authoring already ran; edit documents directly.');
const protectedFiles=['docs/chon-mon-order','docs/cost','docs/nen-tang/srs'].flatMap(x=>walk(path.join(root,x)));
fs.writeFileSync(baseline,JSON.stringify(Object.fromEntries(protectedFiles.map(p=>[path.relative(root,p).replaceAll('\\','/'),hash(p)])),null,2));
function md(file,title,body){const p=path.join(base,file);fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,'---\nid: DOC-E7-'+file.replace(/[^a-z0-9]/gi,'-').toUpperCase()+'\ntitle: '+title+'\nversion: 0.1.0\nphase: Specification\ndomain: Gia Phát\nauthor: BA\nlast_updated: 2026-11-12\n---\n# '+title+'\n\nDraft · 12/11/2026 · Thiết kế BA có điều kiện, chưa phê duyệt / chưa triển khai.\n\n'+body.trim()+'\n');}
const table=(h,rows)=>'| '+h.join(' | ')+' |\n| '+h.map(()=>':---').join(' | ')+' |\n'+rows.map(r=>'| '+r.join(' | ')+' |').join('\n');
const features=[['049','Giao hàng và xác nhận nhận','Theo suất; xác nhận bằng link'],['050','Biên bản chênh lệch','Giao bù, giảm trừ theo thoả thuận'],['051','Doanh thu ghi nhận','Số tính tiền × giá chụp tại thời điểm order'],['052','Đối soát, thu tiền, khoá kỳ','Mở lại kỳ cần Giám đốc duyệt'],['053','Xuất file MISA','Theo mẫu nhập của MISA']];
const rows=[
['049','DLV','NOTE','Lập phiếu giao nhận','Bếp trưởng / quản lý cơ sở','orderId, orderRevisionRef, planRevisionRef, số giao, bằng chứng giao','Đối chiếu scope và nguồn; giữ số chốt/số giao riêng, ghi phiếu và provenance, không sửa order E6','Phiếu chờ khách xác nhận','E6-CG-05/06/08; E7-Q02','POST','/v1/deliveries','01',
['số chốt synthetic 100, số giao 98, nguồn được xác nhận hợp lệ theo giả định','lập phiếu giao 98','giữ số chốt 100 và giao 98; không sửa order'],
['số giao -1','lưu phiếu','ERR-DLV-422-01; không tạo phiếu'],
['order revision nguồn đã thay','lưu phiếu tham chiếu bản cũ','ERR-E7-409-01; không tự chuyển revision']],
['049','DLV','ACK','Xác nhận số nhận qua link','Đại diện khách được xác minh','deliveryId, số nhận, version, bằng chứng xác nhận','Chỉ ghi khi người nhận được xác minh đúng scope theo policy đã duyệt; mở link không là xác nhận; giữ số nhận thực và dấu vết','Xác nhận nhận hoặc chênh lệch','E6-CG-01/08; E7-Q01; Q-13','POST','/v1/deliveries/{id}/confirmations','02',
['phiếu synthetic giao 98 và quyền link được xác minh theo policy giả định hợp lệ','nhập nhận 98 và xác nhận','lưu số nhận 98, actor/thời điểm và version'],
['link bị thu hồi hoặc không đủ scope','xác nhận nhận','ERR-E7-403-01; không ghi số nhận'],
['khách không trả lời','đến thời điểm chờ xử lý','BLOCKED Q-13; không tự lấy số giao/chốt làm số nhận']],
['050','DLV','DIFF','Lập biên bản chênh lệch','Dinh dưỡng viên / vận hành được cấp quyền','deliveryId, số giao/nhận tham chiếu, mô tả, evidenceRef','Giữ bằng chứng hai phía; so sánh số giao/nhận; thiếu số nhận thì chưa xác định chênh, không điền 0','Biên bản có version, liên kết phiếu','E7-Q02; E6-CG-08','POST','/v1/delivery-discrepancies','03',
['phiếu synthetic giao 100 nhận 98 có bằng chứng','lập biên bản','ghi chênh 2, chưa tự giảm tiền'],
['thiếu bằng chứng nhận','kết luận chênh lệch đã thống nhất','ERR-DLV-422-02; giữ nháp'],
['phiếu thuộc kỳ khóa','sửa số làm thay đổi kỳ','ERR-FIN-409-02; cần mở lại hợp lệ']],
['050','DLV','RES','Ghi thỏa thuận xử lý chênh lệch','Vận hành được cấp quyền','discrepancyId, phương án giao bù/giảm trừ, evidenceRef, version','Ghi thỏa thuận hai phía; giao bù gắn phiếu gốc và số bù thực; giảm trừ giữ dòng điều chỉnh riêng; không tự cộng cả hai cách cho một phần thiếu','Thỏa thuận và nguồn số tính tiền','E7-Q02/03; CK-Q07–09 khi liên quan CK','POST','/v1/delivery-discrepancies/{id}/resolutions','03',
['thiếu synthetic 2 suất, thỏa thuận bù 2 và phiếu bù được xác nhận','ghi xử lý','giữ phiếu gốc, liên kết bù, không đếm hai lần'],
['chưa có thỏa thuận','áp giảm trừ','ERR-DLV-422-02; không đổi phải trả'],
['phần thiếu đã giao bù','thêm giảm trừ cùng phần thiếu','BLOCKED E7-Q02; không tự cộng hai cách']],
['051','FIN','REV','Tính doanh thu từ số tính tiền','Kế toán doanh thu','orderRevisionRef, pricingSnapshotId, billableServings, basisEvidenceRef','Kiểm căn cứ số tính tiền và giá chụp đúng order/version; tính số tính tiền × giá chụp; tách phải trả, VAT/doanh thu chưa VAT và CK riêng; thiếu context thì chưa xác định','Bản tính nháp có provenance','E7-Q03/04; Q-13; E6-CG-04/05/07','POST','/v1/revenue-calculations','04',
['synthetic số tính tiền 100 có căn cứ, giá chụp 40000 gồm VAT thử 8%, CK riêng 200000','tính doanh thu','phải trả 4000000, CK 200000 riêng, trước VAT 4000000/1.08 trước làm tròn; không phải trả 3800000'],
['context giá UNKNOWN hoặc số tính tiền không có căn cứ','tính chính thức','ERR-FIN-422-01; chưa xác định, không điền 0'],
['giá hiện tại đổi 42000 sau order','tính lại cùng snapshot','vẫn dùng giá chụp 40000']],
['051','FIN','VIEW','Tra cứu doanh thu và nguồn','Kế toán doanh thu','customerId, fromDate, toDate, trạng thái','Đọc bản tính có sẵn theo scope; tách dòng đủ/thiếu; không cộng dòng chưa xác định như 0 vào tổng hoàn tất','Danh sách, nguồn và tổng có nhãn đủ/thiếu','E7-Q04/08; E6-CG-08','GET','/v1/revenues','04',
['hai bản tính synthetic hợp lệ trong scope','lọc khách/ngày','trả đúng tập và nguồn số tính tiền/giá chụp'],
['khách ngoài scope','tra cứu','ERR-E7-404-01; không lộ tên hoặc tổng'],
['khoảng ngày không có dữ liệu','tra cứu','trả danh sách rỗng, không tạo calculation qua GET']],
['052','FIN','REC','Lập kỳ đối soát','Kế toán doanh thu','customerId, fromDate, toDate, revenueRefs','Chụp tập nguồn/version; liệt kê dòng thiếu/tranh chấp, không bỏ dòng lỗi để báo đủ','Kỳ nháp và danh sách chặn','E7-Q05; Q-13; E6-CG-08','POST','/v1/reconciliation-periods','05',
['synthetic tập doanh thu tháng có nguồn hợp lệ','lập kỳ','kỳ nháp giữ tập nguồn và tổng, chưa tự thống nhất'],
['fromDate sau toDate','lập kỳ','ERR-FIN-422-02; không tạo kỳ'],
['có phiếu chưa được khách xác nhận','chuẩn bị chốt kỳ','BLOCKED Q-13; dòng chờ không bị bỏ qua']],
['052','FIN','AGRE','Ghi nhận thống nhất đối soát','Kế toán và đại diện khách','periodId, version, agreementEvidenceRef','Đối chiếu tổng và nguồn đúng revision với bằng chứng khách; còn chênh lệch chưa thống nhất; không tự ghi thu','Kỳ thống nhất có bằng chứng','E7-Q05; Q-13; E6-CG-01/08','POST','/v1/reconciliation-periods/{id}/agreements','05',
['kỳ synthetic đủ nguồn và biên bản khách khớp revision','ghi thống nhất','lưu evidence/revision; số đã thu không đổi'],
['tổng biên bản khác tổng kỳ','ghi thống nhất','ERR-FIN-422-02; giữ chưa thống nhất'],
['nguồn kỳ thay khi khách đang xác nhận','ghi theo bản cũ','ERR-E7-409-01; không áp bằng chứng cũ cho bản mới']],
['052','FIN','RCPT','Ghi nhận thu tiền','Kế toán doanh thu','periodId, số tiền, ngày nhận, chứng từ, version','Kiểm tiền dương, đúng khách/kỳ và chứng từ; ghi khoản thu có dấu vết; không suy đã thu từ thống nhất hoặc xuất MISA','Khoản thu và còn phải thu riêng','E7-Q06; E7-Q05 về thu sau khóa','POST','/v1/reconciliation-periods/{id}/receipts','06',
['kỳ mở synthetic phải trả 4000000, chứng từ thu 1000000 hợp lệ','ghi thu 1000000','đã thu 1000000, còn 3000000; phải trả gốc không đổi'],
['tiền thu -1','ghi thu','ERR-FIN-422-03; không tạo khoản thu'],
['mất phản hồi lệnh thu','định gửi thao tác mới','hiện chưa rõ kết quả, đối chiếu chứng từ; replay BLOCKED E7-Q08']],
['052','FIN','LOCK','Khóa kỳ đối soát','Kế toán doanh thu','periodId, version, nguồn quyết định','Kiểm đủ nguồn/điều kiện khóa đã được duyệt; giữ snapshot bất biến; chặn mọi đường ghi ảnh hưởng kỳ','Kỳ LOCKED và audit','E7-Q05; Q-13','POST','/v1/reconciliation-periods/{id}/locks','05',
['kỳ synthetic đã thống nhất và đủ điều kiện khóa giả định được duyệt','khóa kỳ','snapshot giữ nguyên, mọi sửa số bị chặn'],
['còn nguồn chưa xác định','khóa kỳ','ERR-FIN-422-02; không khóa'],
['hai lệnh khóa cùng version','ghi cạnh tranh','một chuyển trạng thái; lệnh còn lại ERR-E7-409-01']],
['052','FIN','RREQ','Đề nghị mở lại kỳ','Kế toán doanh thu','periodId, version, lý do, nội dung sửa, evidenceRef','Kỳ phải khóa; lý do ≥10 ký tự theo nền; tạo yêu cầu, không mở khóa','Yêu cầu chờ Giám đốc, kỳ vẫn khóa','E7-Q05; O-06 về ủy quyền giữ mở','POST','/v1/reconciliation-periods/{id}/reopen-requests','07',
['kỳ synthetic khóa, lý do hợp lệ và bằng chứng','gửi đề nghị','yêu cầu chờ; số liệu kỳ vẫn khóa'],
['lý do dưới 10 ký tự','gửi đề nghị','ERR-FIN-422-02; không lưu'],
['đề nghị chưa duyệt','sửa doanh thu kỳ','ERR-FIN-409-02; chờ không là mở']],
['052','FIN','RDEC','Duyệt hoặc từ chối mở lại kỳ','Giám đốc','requestId, requestVersion, periodVersion, approve/reject, reason','Kiểm Giám đốc khác người lập/sửa cuối theo BR-SEC-008; đúng version mới mở; từ chối giữ khóa; giữ snapshot cũ, sửa sau mở phải đối soát lại','Quyết định; kỳ REOPENED hoặc LOCKED','E7-Q05; O-06 không tự cấp người thay','POST','/v1/reopen-requests/{id}/decisions','07',
['Giám đốc synthetic khác người lập/sửa cuối, yêu cầu hợp lệ','duyệt đúng version','kỳ REOPENED, snapshot khóa cũ còn nguyên'],
['người duyệt là người lập hoặc không phải Giám đốc','duyệt','ERR-E7-403-01; kỳ vẫn khóa'],
['Giám đốc chọn từ chối','ghi quyết định','yêu cầu từ chối, kỳ LOCKED, số liệu không đổi']],
['053','FIN','MISA','Chuẩn bị và yêu cầu xuất MISA','Kế toán doanh thu','periodId, revision, templateRef đã xác nhận','Kiểm quyền/nguồn kỳ và mẫu nhập/mapping được duyệt; ghi yêu cầu xuất có nguồn/trạng thái/lỗi; thiếu mẫu thì chặn, không tự tạo cột','Yêu cầu xuất; file chỉ sau mapping được duyệt','E7-Q07/08; E7-Q05 về kỳ được phép xuất','POST','/v1/misa-exports','08',
['kỳ synthetic hợp lệ, mẫu nhập/mapping MISA đã duyệt trong môi trường thử','xuất và thử nhập MISA','file được nhận; lưu evidence nhập, không ghi đã thu'],
['chưa có mẫu chính thức','yêu cầu xuất','ERR-FIN-422-04; không file/cột giả'],
['kỳ đã mở lại sau xuất','xem file cũ','hiện revision cũ và cần rà lại, không sửa bytes cũ hoặc coi hiện hành']]
].map((r,i)=>{const [feat,mod,sub,title,actor,input,logic,output,gate,method,url,ui,...cases]=r;return {n:i+1,feat:'FEAT-'+feat,mod,fr:'FR-'+mod+'-'+sub+'-001',uc:'UC-'+mod+'-'+String(i+1).padStart(3,'0'),us:'US-'+mod+'-'+String(i+1).padStart(3,'0'),api:'API-E7-'+String(i+1).padStart(3,'0'),title,actor,input,logic,output,gate,method,url,ui:'UI-E7-'+ui,cases};});
fs.writeFileSync(path.join(__dirname,'design-index.json'),JSON.stringify(rows,null,2));
const roadmap=fs.readFileSync(path.join(root,'docs/gia-phat/02-roadmap.md'),'utf8');
const r7=roadmap.split('\n').find(x=>x.startsWith('| '+String.fromCharCode(96)+'R7'));
const gnext=roadmap.split('\n').find(x=>x.startsWith('**Cổng G-Next**'));


md('epic-spec.md','E7: Giao nhận & doanh thu',[
'## Mục tiêu và phạm vi',
'Khép vòng từ order đến đối soát theo [PRD](../gia-phat/01-prd.md) và [roadmap](../gia-phat/02-roadmap.md). Chỉ dẫn người dùng 12/11/2026 mở tài liệu E7 thay lệnh cũ không mở E7–E13 **chỉ đối với E7**. E8–E13 chưa mở. E6 dừng chờ CG01/08/05/06, không đặc tả tiếp producer hoặc giả contract freeze.',
table(['Feature','Tên','P0 theo PRD','P1'],features.map(f=>['FEAT-'+f[0],f[1],f[2],'Không có trong PRD; không tự thêm'])),
'Trong phạm vi: 13 FR cho phiếu theo suất, link xác nhận, biên bản/thỏa thuận chênh lệch, số tính tiền × giá chụp, đối soát/thu tiền/khóa/mở lại, chuẩn bị xuất theo mẫu MISA.\n\nNgoài phạm vi: backend, migration, SQL, sửa DBML65 bảng; CRM/E8–E13; điều phối xe/kho/lợi nhuận, phát hành hóa đơn, tích hợp trực tiếp MISA; tự chi trả/bù trừ CK. Không lấy dòng món làm số suất.',
'## R7 nguyên văn từ roadmap',table(['Release','Tên đợt phát hành','Mục tiêu chính','Danh sách Feature ID','Cỡ','Điều kiện bắt đầu','Ngày dự kiến','Tiêu chí nghiệm thu'],[])+'\n'+r7,gnext,
'R6 xong và chốt Q-13 là điều kiện release, chưa đạt chỉ vì mở hồ sơ nháp. G-Next là cổng Later, không là quyền mở E8–E13 phiên này. Không gán ngày triển khai/effort/người phụ trách.',
'## Tiêu chí bàn giao hồ sơ nháp',
'Mỗi feature có FR/UC/story/AC/API/UI/test và gate tại chỗ. [RTM](test/traceability.md) · [Phụ thuộc](review/dependencies.md) · [Câu hỏi](review/questions.md) · [Kiểm](validation/report.md).\n\n5/5 feature có thiết kế có điều kiện, 0 feature E7 chỉ gate. FEAT-053 có preflight/provenance/luồng xuất nhưng **chưa mapping cột file**. Đây không phải BA được duyệt hoặc phần mềm hoàn thành.'
].join('\n\n'));
md('review/questions.md','Sổ câu hỏi mở E7',[
'Tất cả **CHỜ TRẢ LỜI**. Cột trả lời để trống, phương án tham khảo chưa được chọn; không yêu cầu trả lời trong phiên này.',
table(['Mã','Câu hỏi','Phương án tham khảo / đánh đổi','Nhánh BLOCKED','Trả lời','Nguồn / người / ngày'],[
['Q-13','Khách không xác nhận số nhận thì xử lý thế nào, sau khoảng chờ nào và ai quyết định số tính tiền?','Giữ chờ và xử lý thủ công có bằng chứng; hoặc suy định theo thỏa thuận khách có thời hạn/thông báo/tranh chấp. Chưa chọn.','ACK im lặng; số tính tiền và thống nhất/khóa kỳ liên quan','',''],
['E7-Q01','Ai xác nhận link nhận hàng; cơ chế xác minh, hiệu lực, thu hồi/cấp lại là gì?','Phiên có quyền hoặc token giới hạn scope cần review Auth; không lấy QR E6 làm quyền ký nhận.','Link; CG01/08 chờ, không đặc tả thêm producer E6','',''],
['E7-Q02','Ai thống nhất chênh lệch; giao nhiều lần/giao bù/nhận thừa/giảm trừ được duyệt và sửa thế nào?','Giữ phiếu gốc + thỏa thuận/phiếu bù; cần chống đếm trùng và quyền.','RES, tổng giao/nhận sau bù, tác động kỳ khóa','',''],
['E7-Q03','Số tính tiền dựa số chốt/giao/nhận hay thỏa thuận? Giảm trừ quy ra suất hay tiền thế nào?','Căn cứ từng đơn có evidence; không mặc định số nhận/số chốt.','REV; giảm trừ khác CK riêng','',''],
['E7-Q04','Doanh thu đối soát trước/sau VAT; làm tròn dòng/đơn/kỳ và chuẩn khớp biên bản cụ thể?','Hiện phải trả, VAT, doanh thu trước VAT riêng; không mượn dung sai Cost.','Tổng chính thức và R7','',''],
['E7-Q05','Phạm vi kỳ, chống chồng kỳ, điều kiện khóa, thu sau khóa, mở lại/tái đối soát/tái xuất thế nào?','Snapshot từng vòng; chỉ Giám đốc duyệt mới mở. Điều kiện khác chưa chọn.','AGRE/LOCK và sửa sau REOPENED','',''],
['E7-Q06','Thu một phần/thừa, phân bổ nhiều kỳ, sửa/hủy chứng từ và hoàn tiền thế nào?','Chứng từ/phân bổ riêng; không suy CK đã bù trừ.','Thanh toán nâng cao/chống trùng nghiệp vụ','',''],
['E7-Q07','Sản phẩm/phiên bản MISA nào; mẫu nhập chính thức, mapping/tài khoản/mã khách, evidence nhập thành công là gì?','Nhận mẫu có version và thử nhập môi trường được cấp; chưa giả CSV/XLSX, cột, mã thuế/tài khoản.','File bytes/mapping cột/thử nhập MISA','',''],
['E7-Q08','Envelope, idempotency/receipt/retention, bộ lọc, scope role, audit link, profile tải/xuất dùng chuẩn nào?','Kế thừa an toàn nền; review kỹ thuật, không đặt TTL/retry/limits tùy ý.','Wire contract/persistence/fault/load','','']]),
'E6-CG-01/08/05/06 giữ CHỜ TRẢ LỜI trong [sổ E6 duy nhất](../../chon-mon-order/review/contract-gap-register.md), không hỏi lại. 14/14 CG OPEN. CK-Q01–10, DATA-COST-Q01–06, NFR-COST-002, O-02/O-03/O-04, E6-EVID-001/002 không đổi. Chỉ đóng khi có bằng chứng/phạm vi quyết định, không vì kiểm tài liệu.'
].join('\n\n'));
md('review/dependencies.md','Phụ thuộc E6 → E7 và cổng nguồn',[
'Mỗi dòng là **giả định có điều kiện** rằng producer cung cấp nguồn được xác nhận hợp lệ về sau. Trước đó tích hợp BLOCKED. Không freeze E6, không tạo route E6 hoặc tự quyết CG đang chờ.',
table(['Dữ liệu cần','Nguồn / đường đọc hiện có','CG liên quan','E7 sử dụng và giới hạn'],[
['Số suất chốt','FR-ORD-SUB-001/LOCK-001; orders.total_servings; API-ORD-019 OrderRevision','CG03/04/05/11','NOTE/REV giữ số chốt riêng; không lấy Summary live thay bản khóa hoặc tính lại T/S/C; hủy/zero chưa chốt'],
['Order revision','API-ORD-019; revisionId/revisionNo/orderVersion; delta order_revisions chưa merge','CG04/05/07/11','Đúng revision và pricing snapshot.order_version; revisionNo khác version; thiếu nguồn BLOCKED'],
['Plan revision','API-ORD-020/025; planId/revisionNo/sources; delta production_plan_revisions','CG06/07/11','Truy nguồn bếp; GET/READY không là publish/ack/start; bản đủ điều kiện giao chưa chốt → BLOCKED CG06, không thiết kế cách chọn bản'],
['Điểm phục vụ','API-ORD-013; service_points.customer_id/kitchen_id; service_schedules','CG08/05/06','Điểm thuộc khách/cơ sở và lịch phải có căn cứ; không tự tạo master/thay lịch'],
['Khách','customers; users.customer_id; cổng customer/account E6 chưa có master API đầy đủ','CG01/02/08','Binding/read contract BLOCKED; không lấy users.customer_id quyết scope một/nhiều khách'],
['Giá chụp','order_pricing_snapshots unique(order_id,order_version); context_status/inputs_snapshot; orders.unit_price_vnd','CG04/05/07/11; CK','Dùng đúng snapshot; không tạo thay producer; servings snapshot không tự là billableServings'],
['Quyền/envelope','FR-AUTH-RBAC-001 nền; adapter E6','CG01/08/09/11','Authorize E7 riêng; không chốt default/null/envelope E6']]),
'Nguồn: [SRS E6](../../chon-mon-order/srs/spec.md), [API](../../chon-mon-order/api/api-spec.md), [mapping](../../chon-mon-order/api/data-mapping.md), [lifecycle](../../chon-mon-order/srs/lock-plan-review.md), [dependencies](../../chon-mon-order/review/dependencies.md), [sổ CG](../../chon-mon-order/review/contract-gap-register.md).',
'Phần độc lập: giữ số giao/nhận riêng, đọc provenance, bảo vệ kỳ khóa, tách CK trên đầu vào giả định hợp lệ. Không đặc tả lại thời điểm khóa E6, điều kiện phát hành plan, identity hay owner master. E7 không ghi orders.status thành DELIVERED/CONFIRMED chỉ vì DBML có enum; tác động nguồn phải chờ contract được duyệt.',
'R6/Q-13 là gate R7; G-Next nguyên roadmap chưa có evidence đạt. MISA chỉ theo mẫu nhập PRD, chưa mapping cột. VAT cost phải trả NCC; invoice flag riêng; CK không giảm phải trả; không đóng CK/DATA-COST. Synthetic không thay pilot 2 khách/tháng đối soát thật.'
].join('\n\n'));
const br=[
['BR-E7-001','KHI đọc/ghi THÌ kiểm quyền/scope hiện tại; không ngoại lệ bằng link công khai','Nền FR-AUTH-RBAC-001; CG01/08 và E7-Q01'],
['BR-E7-002','KHI dùng E6 THÌ giữ order revision/order version/plan revision riêng; thiếu không =0, không tự lấy bản mới','Mapping E6; CG04/05/06/07/08'],
['BR-E7-003','KHI ghi THÌ kiểm version, audit actor/time/trước-sau; lỗi không thành công một phần; GET không ghi','Đề xuất; persistence E7-Q08'],
['BR-E7-004','KHI nhận khác giao/chốt THÌ giữ từng số và thỏa thuận bù/giảm trừ; không tự xử lý im lặng','FEAT-049/050; Q-13/E7-Q02'],
['BR-E7-005','KHI tính doanh thu THÌ số tính tiền có căn cứ × giá chụp order; không lấy giá sống hoặc dòng món','FEAT-051; E7-Q03'],
['BR-E7-006','KHI xử lý VAT THÌ invoiceRequested riêng, thiếu context chưa xác định; cost nguyên liệu gồm VAT phải trả NCC','Kế toán; E7-Q04 còn mở'],
['BR-E7-007','KHI có CK % hoặc tiền/suất THÌ khoản riêng theo đơn, không giảm phải trả hoặc suy đã chi; giảm trừ chênh không là CK','Kế toán đã xác nhận; CK-Q01–10 giữ'],
['BR-E7-008','KHI ghi thu THÌ tiền dương, chứng từ đúng khách/kỳ, không ghi trùng; AGREED/export không là PAID','FEAT-052; E7-Q06/08'],
['BR-E7-009','KHI kỳ khóa THÌ không sửa trước Giám đốc duyệt mở; chờ/từ chối vẫn khóa; duyệt khác lập/sửa cuối; lý do ≥10 ký tự','R7; BR-SEC-008/BR-AUD-001 nền; O-06 giữ mở'],
['BR-E7-010','KHI thiếu nguồn/policy THÌ ghi BLOCKED kèm mã, không dùng synthetic thay evidence thật','Chỉ dẫn 12/11/2026'],
['BR-E7-011','KHI xuất MISA THÌ dùng mẫu được xác nhận/giữ revision nguồn; thiếu mẫu không tự tạo cột','FEAT-053/R7; E7-Q07']
];
md('srs/spec.md','SRS E7: Giao nhận, doanh thu và đối soát',[
'## 1. Giới thiệu',
'[PRD](../../gia-phat/01-prd.md) · [Epic](../epic-spec.md) · [Nền tảng](../../nen-tang/srs/spec.md) · [Kế toán](../../cost/accounting/business-rules.md).\n\nPhiếu ghi sự kiện giao/nhận theo suất. Kỳ đối soát là tập dữ liệu một khách/khoảng ngày. Revision là bản nguồn; version là token thay đổi, không tráo hai khái niệm.',
'## 2. Tổng quan',
'Bếp/vận hành ghi giao, đại diện khách xác nhận, kế toán đối soát/thu tiền, Giám đốc duyệt mở lại. [Quyền/UI](../ui/screens.md) là đề xuất, không tự cấp quyền chỉ vì role đã có. Web desktop/mobile; phiên này HTML offline. [Phụ thuộc](../review/dependencies.md) chặn E6/auth/link; [câu hỏi](../review/questions.md) chặn Q-13, căn cứ tiền, mẫu MISA. CG01/08/05/06 chỉ là cổng đầu vào, không đặc tả cách producer vượt cổng.',
'## 3.1 FR: tất cả P0 theo PRD',
table(['FR / Feature','Tên / actor','Input logic','Xử lý','Output','Gate'],rows.map(r=>[r.fr+' / '+r.feat,r.title+': '+r.actor,r.input,r.logic,r.output,r.gate])),
'BR-E7-001/002/003/010 áp mọi FR. ACK/DIFF/RES thêm004; REV/VIEW/REC/AGRE thêm005/006/007; RCPT thêm008; LOCK/RREQ/RDEC thêm009; MISA thêm011. [Lỗi](error-matrix.md) và [RTM](../test/traceability.md).',
'## 3.2 Business rules',table(['Mã','KHI → THÌ; ngoại lệ','Căn cứ / trạng thái'],br),
'## 3.3 Giao diện ngoài','[API](../api/api-spec.md), [mapping](../api/data-mapping.md), [wireframe](../html-wireframe/revenue-workbench.html). MISA là file theo mẫu, không thêm webhook/connector.',
'## 3.4 NFR',table(['Mã','Chỉ tiêu / phương pháp','Giới hạn'],[
['NFR-E7-001','0 truy cập chéo khách/cơ sở hoặc lộ cost/secret link qua response/log hiển thị; thử từng route/role/scope','Link BLOCKED E7-Q01/CG01'],
['NFR-E7-002','0 sửa kỳ LOCKED trước Giám đốc duyệt; 100% sửa số có audit; thử mọi đường ghi/race/fault','R1/R7; chưa runtime'],
['NFR-E7-003','Doanh thu một tháng khớp biên bản 2 khách; file nhập được MISA','R7; dữ liệu/mẫu/rounding chưa có; không mượn dung sai Cost'],
['NFR-E7-004','Kế thừa nền p95 đọc ≤300ms, ghi ≤800ms tại profile 1000 người đồng thời','Profile E7/xuất E7-Q08; không tự dùng 1000TPS template'],
['NFR-E7-005','390px/1440px không tràn ngang toàn trang; label/focus và lỗi/BLOCKED đọc được','Chỉ kiểm HTML mới; chưa audit accessibility đầy đủ']]),
'## 3.5 Lỗi và phụ lục','[Error matrix](error-matrix.md) · [States](states.md) · [Delta](data-dictionary.md) · [Flow](../ui/user-flow.md) · [RTM](../test/traceability.md).\n\nKhông sửa O-02/O-03/O-04 hoặc E6-EVID-001/002; không hỏi lại scope/C→S/S+C vượt T.'
].join('\n\n'));
const errs=[
['ERR-E7-401-01','401','Phiên không hợp lệ','Phiên hết hạn. Đăng nhập lại.','auth_required','High','Đăng nhập, không tự gửi lại lệnh'],
['ERR-E7-403-01','403','Thiếu quyền/link không hợp lệ/tự duyệt','Không đủ quyền xác nhận thao tác.','forbidden','High','Kiểm quyền, không hiện secret'],
['ERR-E7-404-01','404','Không tồn tại hoặc ngoài scope','Không tìm thấy dữ liệu.','not_found','Medium','Kiểm phạm vi'],
['ERR-E7-409-01','409','Version/nguồn đã thay','Dữ liệu đã đổi. Tải lại và đối chiếu.','stale_version','High','Không tự ghi đè'],
['ERR-E7-503-01','503','Nguồn không sẵn sàng/policy chưa chốt','Chưa đủ điều kiện xử lý.','dependency_blocked','High','Hiện gate, không điền 0'],
['ERR-DLV-422-01','422','Suất âm/không nguyên hoặc sai tham chiếu','Kiểm tra số suất và phiếu nguồn.','invalid_quantity','Medium','Sửa dữ liệu'],
['ERR-DLV-422-02','422','Thiếu bằng chứng/thỏa thuận','Chưa đủ bằng chứng để thống nhất.','agreement_missing','Medium','Giữ nháp'],
['ERR-FIN-422-01','422','Thiếu căn cứ số tính tiền/giá/VAT','Chưa xác định được doanh thu.','pricing_unresolved','High','Kiểm nguồn'],
['ERR-FIN-422-02','422','Kỳ/biên bản/lý do/điều kiện khóa sai','Kiểm tra điều kiện đối soát và lý do.','period_invalid','Medium','Rà dòng chặn'],
['ERR-FIN-422-03','422','Tiền thu sai hoặc chứng từ trùng','Kiểm tra số tiền và chứng từ thu.','receipt_invalid','Medium','Đối chiếu trước gửi lại'],
['ERR-FIN-409-02','409','Ghi ảnh hưởng kỳ khóa','Kỳ đã khóa. Cần Giám đốc duyệt mở lại.','period_locked','High','Lập yêu cầu'],
['ERR-FIN-422-04','422','Thiếu mẫu/mapping MISA','Chưa có mẫu nhập MISA được xác nhận.','template_missing','High','Không xuất file giả'],
['ERR-E7-500-01','500','Lỗi xử lý/kết quả chưa rõ','Chưa xác định kết quả. Đối chiếu trước thử lại.','unexpected','High','Tra requestId, không ghi lặp']
];
md('srs/error-matrix.md','Ma trận lỗi E7',table(['Mã','HTTP','Trigger / log reason','UI message','Localization key','Severity','Next action'],errs.map(e=>[...e.slice(0,4),'e7.'+e[4],...e.slice(5)]))+'\n\nMã đề xuất consumer E7, không đổi E6. Log không chứa token/upstream body. 503 hiển thị mã gate, không là quyền thay policy.');


let ucLinks=[],stories=[],acs=[],tests=[],rtm=[];
for(const r of rows){
 const cs=r.cases.map((c,j)=>({id:'AC-E7-'+String(r.n).padStart(3,'0')+'-'+(j+1),tc:'TC-E7-'+String(r.n).padStart(3,'0')+'-'+(j+1),c,status:j===0||c.join(' ').includes('BLOCKED')?'BLOCKED':'NOT RUN'}));
 md('usecases/'+r.uc+'.md',r.uc+': '+r.title,[
 'FR: '+r.fr+' · '+r.feat+' · [SRS](../srs/spec.md) · [API](../api/api-spec.md) · '+r.ui+'.',
 'Level: Sea level. Actor chính: '+r.actor+'. Bên quan tâm: khách cần đúng số nhận/phải trả, kế toán cần truy nguồn, vận hành cần bằng chứng. Trigger: actor chọn “'+r.title+'”.',
 'Tiền điều kiện: phiên/scope hợp lệ, nguồn tồn tại; '+r.gate+' có quyết định phù hợp cho happy path. Đây là giả định, chưa có evidence thực tế.',
 'Luồng chính:\n1. Actor mở '+r.ui+', đọc nguồn/trạng thái.\n2. Actor cung cấp/chọn '+r.input+'.\n3. Hệ thống kiểm quyền, nguồn/version và gate.\n4. '+r.logic+'.\n5. Trả '+r.output+' và nguồn.',
 'Hậu điều kiện: '+r.output+'. Bảo đảm tối thiểu: lỗi không ghi thành công một phần; không sửa E6 hoặc kỳ khóa; GET không ghi.',
 'Extensions:\n- 3a. '+r.cases[1][0]+' → '+r.cases[1][2]+'.\n- 3b. '+r.cases[2][0]+' → '+r.cases[2][2]+'.\n- 3c. Hết phiên ERR-E7-401-01; thiếu quyền ERR-E7-403-01; ngoài scope ERR-E7-404-01; thiếu nguồn/policy ERR-E7-503-01. Dừng nhánh, không tự mở gate.\n- 4a. Mất phản hồi: kết quả chưa rõ; đối chiếu chứng từ/version trước lệnh mới, replay E7-Q08 BLOCKED.',
 'BR-E7-001/002/003/010 và BR miền tại SRS. [AC](../userstories/acceptance-criteria.md): '+cs.map(c=>c.id).join(', ')+'. [Test](../test/test-cases.md) cùng 3 mục tiêu, không cộng thành 6.'
 ].join('\n\n'));
 ucLinks.push('['+r.uc+': '+r.title+']('+r.uc+'.md)');
 stories.push([r.us,r.fr,r.uc,'Là '+r.actor+', tôi muốn '+r.title.toLowerCase()+' để '+r.output.toLowerCase()+'.','P0',r.gate]);
 acs.push('## '+r.us+' / '+r.fr+'\n\n'+cs.map((c,j)=>'### '+c.id+': '+['Thành công có điều kiện','Lỗi nghiệp vụ','Biên / an toàn'][j]+'\n\n'+String.fromCharCode(96).repeat(3)+'gherkin\nGiven '+c.c[0]+'\nWhen '+c.c[1]+'\nThen '+c.c[2]+'\n'+String.fromCharCode(96).repeat(3)+'\n\nTrạng thái kiểm: '+c.status+'. Gate happy path: '+r.gate+'.').join('\n\n'));
 for(const c of cs)tests.push([c.tc,r.fr+' / '+r.us+' / '+c.id,c.c[0]+'; synthetic','1. Mở '+r.ui+' bằng '+r.actor+'. 2. '+c.c[1]+'. 3. Đọc kết quả, đối chiếu before/after/audit hoặc read-only.',c.c[2],c.status,'','']);
 rtm.push([r.feat,r.fr,'['+r.uc+'](../usecases/'+r.uc+'.md)',r.us,cs.map(x=>x.id).join(', '),r.api,r.ui,cs.map(x=>x.tc).join(', '),r.gate]);
}
md('usecases/index.md','Danh mục use case E7',ucLinks.map(x=>'- '+x).join('\n'));
md('userstories/backlog.md','Backlog E7',table(['Story','FR','UC','Story','Ưu tiên','Phụ thuộc'],stories)+'\n\n13 story nháp, chưa sprint-ready: I/E/T của INVEST phụ thuộc policy/contract/dữ liệu/môi trường; N/V có mô tả, S cần refinement. Không gán story point/ngày/người phụ trách. [AC](acceptance-criteria.md) · [RTM](../test/traceability.md).');
md('userstories/acceptance-criteria.md','Acceptance criteria E7 (Given / When / Then)',acs.join('\n\n'));
md('test/test-cases.md','Test cases E7','39 ca theo 39 AC, không cộng thành 78. NOT RUN = oracle độc lập đã mô tả, chưa chạy sản phẩm; BLOCKED = cần policy/contract/dữ liệu. Actual/Evidence trống; HTML mock pass không thay status.\n\n'+table(['Test','FR / Story / AC','Tiền điều kiện / dữ liệu','Bước chạy','Expected','Status','Actual','Evidence'],tests));
md('test/traceability.md','RTM E7',table(['Feature','FR','UC','Story','AC','API','UI','Test','Gate'],rtm)+'\n\n13/13 FR có luồng có UC/story/3AC/API/UI/test; 5/5 feature có thiết kế nháp có điều kiện; 0 feature E7 chỉ gate. FEAT-053 có preflight/yêu cầu xuất nhưng file mapping BLOCKED E7-Q07. Hai feature E6 FEAT-046/047 chỉ gate O-03 tính riêng. Độ phủ nháp (23 E1–E5 +17 E6 +5 E7)/78 =45/78≈57,7%; không phải BA duyệt hay tiến độ phần mềm.');
const reads=[
['014','/v1/deliveries','FR-DLV-NOTE-001','FEAT-049','UI-E7-01','Danh sách phiếu theo scope/ngày, có empty và missing source'],
['015','/v1/deliveries/{id}','FR-DLV-ACK-001','FEAT-049','UI-E7-02','Chi tiết theo quyền/link đã xác minh; không tự xác nhận'],
['016','/v1/delivery-discrepancies/{id}','FR-DLV-DIFF-001','FEAT-050','UI-E7-03','Biên bản/bằng chứng, không tự thống nhất'],
['017','/v1/reconciliation-periods/{id}','FR-FIN-REC-001','FEAT-052','UI-E7-05','Kỳ/nguồn/thu tiền/yêu cầu mở lại theo quyền; không chốt'],
['018','/v1/misa-exports/{id}','FR-FIN-MISA-001','FEAT-053','UI-E7-08','Trạng thái/fileRef khi có file thật; không tạo file']
];
const catalog=rows.map(r=>({id:r.api,method:r.method,path:r.url,features:[r.feat],fr:[r.fr],ui:[r.ui],status:'PROPOSED_CONDITIONAL',gates:r.gate})).concat(reads.map(r=>({id:'API-E7-'+r[0],method:'GET',path:r[1],fr:[r[2]],features:[r[3]],ui:[r[4]],status:'PROPOSED_CONDITIONAL',gates:'E7-Q08; scope/source gates inherited',behavior:r[5]})));
fs.mkdirSync(path.join(base,'api'),{recursive:true});
fs.writeFileSync(path.join(base,'api/endpoint-catalog.json'),JSON.stringify(catalog,null,2));
md('api/api-spec.md','API đề xuất E7',[
'## Ranh giới',
'18 endpoint đề xuất (13 luồng chính +5 đọc bổ sung); không server. Input logic không là wire shape E6. Không callback/webhook/MISA connector ngoài PRD. [Catalog](endpoint-catalog.json) · [Mapping](data-mapping.md).',
'Header đề xuất: Authorization theo AUTH, Content-Type application/json khi có body, requestId để tra. Lệnh ghi phải chống trùng nhưng header/key scope/TTL/replay giữ BLOCKED E7-Q08. ID chuỗi; ngày YYYY-MM-DD theo Asia/Ho_Chi_Minh; thời điểm UTC; tiền VND decimal truyền chuỗi đề xuất; số suất nguyên không âm, tiền thu dương. Limits/nullable/omit chưa freeze; không tự default0.',
'Resolve resource→order→point→customer/kitchen từ nguồn tin cậy, không tin scope client. Khách chỉ nhận projection phiếu/kỳ của mình; không cost/giá mua/CK nội bộ/secret. GET chỉ đọc. POST tạo bản ghi đề xuất201; quyết định/trạng thái200. Resource trả nguồn/version. Envelope E1-Q01/E7-Q08 chưa freeze, không áp template skill thay E6.',
table(['API / method / route','FR / actor','Request logic','Xử lý / success data','Gate'],rows.map(r=>[r.api+': '+r.method+' '+r.url,r.fr+'; '+r.actor,r.input,r.logic+' → '+r.output,r.gate])),
table(['API đọc bổ sung','GET route','FR / UI','Output logic'],reads.map(r=>['API-E7-'+r[0],r[1],r[2]+' / '+r[4],r[5]])),
'GET list yêu cầu scope/khoảng ngày rõ; phân trang/giới hạn chờ E7-Q08, không mặc định lấy tất cả. Detail dùng id trong path; không ghi ngầm. UI01/02/03/05/08 dùng GET014–018 tương ứng; POST output phục vụ UI rồi đọc lại có quyền.',
'## DTO logic và validation',
'Delivery: id, orderRef, sourceRevisionRefs, số chốt tham chiếu, số giao, số nhận chưa xác định khi chưa xác nhận, trạng thái/version. Confirmation: deliveryId/version, receivedServings/evidence; actor resolve theo policy được duyệt, không tin actorId client. Link auth chưa đặc tả tiếp vì CG01/E7-Q01.',
'Discrepancy: phiếu/version/mô tả/evidence. Resolution: thỏa thuận/loại xử lý, phiếu bù hoặc căn cứ giảm trừ; công thức ảnh hưởng tiền E7-Q02/03. Không route sửa order E6.',
'RevenueCalculation: order revision/pricing snapshot, số tính tiền/căn cứ; giá lấy server; grossAmountDue/revenueExVat/discountSeparate riêng; chưa xác định không0. Không tin tổng tiền client. Period: customer/from/to, tập nguồn/version, completeness/gates, tổng phải trả/đã thu/trạng thái. Agreement: periodVersion/evidence đúng nguồn.',
'Receipt: tiền dương/chứng từ/ngày nhận/periodVersion; đa kỳ/thu thừa/sửa hủy E7-Q06. Lock: kỳ/version/evidence điều kiện; ReopenRequest: lý do≥10 ký tự/nội dung; Decision: approve/reject/reason/requestVersion/periodVersion; Giám đốc khác creator/lastEditor. Admin không tự có quyền duyệt.',
'ExportRequest: period/version/templateRef; thiếu mẫu → BLOCKED. Chưa biết extension/encoding/delimiter/headers/tài khoản/mã thuế. Result đề xuất trạng thái/source revision/error summary/fileRef khi thực sự có; fileRef không chứng minh nhập MISA đạt.',
'## Lỗi / retry / atomicity',
'Lỗi chung401/403/404/stale409/dependency503/unknown500 và lỗi miền422 theo [matrix](../srs/error-matrix.md). Kỳ khóa409-02 chặn mọi POST ảnh hưởng snapshot, không chỉ disable nút. Ghi dữ liệu/audit/receipt nguyên tử là đề xuất cần persistence E7-Q08; chưa chọn lock strategy. Mất response=UNKNOWN; đối chiếu trước lệnh mới, không tự retry. Cùng chứng từ không cộng thu hai lần. Không trả token trong log/danh sách.'
].join('\n\n'));
const fence=String.fromCharCode(96).repeat(3);
md('srs/states.md','State diagram E7',[
'## Phiếu giao nhận',
'Tên trạng thái là delta E7, không đổi orders enum. Nguồn hợp lệ BLOCKED CG05/06/08; xác nhận BLOCKED CG01/E7-Q01. Không đặc tả cách vượt cổng.',
fence+'mermaid\nstateDiagram-v2\n [*] --> DRAFT\n DRAFT --> WAITING_CONFIRMATION: ghi giao - nguồn hợp lệ có điều kiện\n WAITING_CONFIRMATION --> CONFIRMED: nhận đúng số và đủ quyền\n WAITING_CONFIRMATION --> DISPUTED: xác nhận có chênh lệch\n WAITING_CONFIRMATION --> WAITING_CONFIRMATION: không trả lời - BLOCKED Q13\n DISPUTED --> RESOLUTION_PENDING: lập biên bản\n RESOLUTION_PENDING --> RESOLVED: thỏa thuận và evidence - Q02\n'+fence,
'CONFIRMED không tự xác định số tính tiền/đã thu/đối soát. Phiếu bù liên kết, không sửa gốc. Zero/hủy/nhận thừa/giao nhiều lần chưa transition tự động.',
'## Kỳ đối soát',
fence+'mermaid\nstateDiagram-v2\n [*] --> DRAFT\n DRAFT --> RECONCILING: lập tập nguồn\n RECONCILING --> RECONCILING: thiếu hoặc tranh chấp - BLOCKED\n RECONCILING --> AGREED: đủ nguồn và evidence đúng revision\n AGREED --> LOCKED: điều kiện khóa được duyệt - Q05\n LOCKED --> REOPENED: Giám đốc duyệt đúng version\n REOPENED --> RECONCILING: sửa có audit và đối soát lại\n'+fence,
'Thu tiền là chiều dữ liệu riêng; AGREED/LOCKED không suy PAID. Chưa chọn có phải thu đủ trước khóa. LOCKED chặn cả phiếu/doanh thu/chứng từ/import.',
'## Yêu cầu mở lại',
fence+'mermaid\nstateDiagram-v2\n [*] --> REQUESTED: kỳ khóa và lý do hợp lệ\n REQUESTED --> APPROVED: Giám đốc khác lập và sửa cuối\n REQUESTED --> REJECTED: từ chối\n REQUESTED --> REQUESTED: chưa duyệt - kỳ vẫn khóa\n APPROVED --> [*]: kỳ REOPENED - giữ snapshot cũ\n REJECTED --> [*]: kỳ vẫn LOCKED\n'+fence,
'Kiểm version tại ghi; quyết định cũ không mở kỳ mới. O-06 không tự cấp người thay. File đã xuất giữ revision cũ/cần rà lại, không sửa bytes hoặc auto tái xuất. [Q05/07/08](../review/questions.md).'
].join('\n\n'));
md('ui/user-flow.md','User flow E7: happy/error/edge',[
fence+'mermaid\nflowchart TD\n A[UI01 Phiếu giao - nguồn có điều kiện] --> B{Nguồn và quyền đủ?}\n B -->|Không| X[Hiện gate CG - không ghi]\n B -->|Có| C[UI02 Khách xác nhận link]\n C --> D{Khách trả lời?}\n D -->|Không| Q[BLOCKED Q13 - giữ chờ]\n D -->|Có| E{Có chênh lệch?}\n E -->|Có| F[UI03 Biên bản và thỏa thuận]\n E -->|Không| G[UI04 Số tính tiền và giá chụp]\n F --> G\n G --> H{Đủ căn cứ tính?}\n H -->|Không| Y[BLOCKED Q03 Q04]\n H -->|Có| I[UI05 Đối soát đúng revision]\n I --> J[UI06 Thu tiền riêng]\n I --> K[UI05 Khóa có điều kiện]\n K --> L[UI07 Yêu cầu mở lại]\n L --> M{Giám đốc duyệt?}\n M -->|Chưa hoặc từ chối| K\n M -->|Có| I\n I --> N[UI08 Kiểm mẫu MISA]\n N --> O{Mẫu được duyệt?}\n O -->|Không| P[BLOCKED Q07 - không file giả]\n O -->|Có| R[Xuất và thử nhập - chưa thực thi]\n'+fence,
table(['Tình huống','UI / phản hồi','Hậu điều kiện'],[
['Happy có điều kiện','01→02→04→05, 03 khi chênh; 06 thu riêng; 08 theo mẫu','Giữ evidence/nguồn, không auto PAID'],
['Nguồn E6 đổi/thiếu','01/04 hiện revision và gate','Không tự chọn bản mới'],
['Link hết hiệu lực/ngoài scope','02 báo lỗi quyền','Không hiện khách khác/không ghi'],
['Khách im lặng','02 chờ, 04/05 dòng BLOCKED Q-13','Không suy số nhận/tính tiền'],
['Nhận ít/thừa/giao bù','03 giữ evidence và Q02/03','Không tự giảm tiền hoặc cộng bù trùng'],
['Mất phản hồi/Offline','Giữ form, hiện chưa rõ kết quả','Đối chiếu chứng từ/version trước retry'],
['Khóa/yêu cầu đang chờ','05/07 readonly, trạng thái yêu cầu riêng','Không sửa qua màn/API khác'],
['Loading/Empty/Error','Toolbar mô phỏng; rỗng không là0; lỗi có hướng xử lý','GET không tạo dữ liệu']]),
'Wireframe chỉ dữ liệu synthetic, không auth/link/nguồn E6 thực. Nút mô phỏng không là quyết định được duyệt.'
].join('\n\n'));
const screens=[
['01','Phiếu giao','Khách/điểm/ngày/ca, số chốt/giao, order/plan revision, evidence','BEP_TRUONG/QL_CO_SO theo cơ sở, CG05/06/08'],
['02','Xác nhận nhận','Số giao/nhận, nguồn phiếu, trạng thái link','Đại diện khách đủ quyền; CG01/E7-Q01 chưa chọn cơ chế'],
['03','Chênh lệch','Giao/nhận, bằng chứng, thỏa thuận bù/giảm trừ','PER-05, chi tiết E7-Q02'],
['04','Doanh thu','Số tính tiền, giá chụp, VAT/phải trả/CK riêng, dòng thiếu','KT_DOANH_THU; khách không đọc CK nội bộ/cost'],
['05','Kỳ đối soát','Khoảng ngày/tập nguồn/version/biên bản/tổng/khóa','KT_DOANH_THU; khách chỉ kỳ thuộc scope'],
['06','Thu tiền','Chứng từ/tiền nhận/đã thu/còn thu','KT_DOANH_THU; đa kỳ/sửa hủy chưa mở'],
['07','Mở lại kỳ','Lý do/người lập-sửa cuối/quyết định/trạng thái','KT_DOANH_THU lập; GIAM_DOC khác người lập/sửa cuối duyệt'],
['08','MISA','Kỳ/revision/mẫu nhập/trạng thái kiểm/yêu cầu xuất','KT_DOANH_THU; thiếu mẫu không tải file']
];
md('ui/screens.md','Màn hình và quyền E7',table(['UI','Màn hình','Dữ liệu','FR','Vai trò / gate'],screens.map(s=>['UI-E7-'+s[0],s[1],s[2],rows.filter(r=>r.ui==='UI-E7-'+s[0]).map(r=>r.fr).join(', '),s[3]]))+'\n\nQuyền chi tiết E7-Q08 chưa cấp bằng tài liệu; server kiểm theo FR-AUTH-RBAC-001: ngoài scope404/thiếu quyền403. [Wireframe](../html-wireframe/revenue-workbench.html) có 8 màn synthetic, không backend.');


md('api/data-mapping.md','Mapping API → schema hiện có → UI',[
'Nguồn [DBML65 bảng](../../nen-tang/srs/schema.dbml) và [ERD nền](../../nen-tang/srs/erd.md), [delta E6](../../chon-mon-order/srs/data-dictionary.md). Tên cột hiện hữu dưới đây đã đối chiếu; bảng/cột E7 chưa tồn tại, chỉ delta đề xuất. Không migration/merge.',
table(['API logical field','Schema hiện có / delta đề xuất','UI','Chuyển đổi / gate'],[
['customerId','customers.id; service_points.customer_id','01/04/05','Resolve qua điểm/order; không tin client; CG08'],
['servicePointId / kitchenId','orders.service_point_id → service_points.id/kitchen_id','01','FK hiện hữu không chứng minh scope đã cấp; CG08'],
['serviceDate / shift','orders.service_date / shift','01','Ngày nghiệp vụ Asia/Ho_Chi_Minh; không default ca E7 từ DB'],
['orderedServings','orders.total_servings; bản khóa tại delta order_revisions E6','01/03','Suất, không tổng dòng món; thiếu nguồn không0; CG03/05'],
['orderVersion','orders.version; order_pricing_snapshots.order_version','01/04','Phân biệt version live và version chụp; CG04/05'],
['orderRevisionRef','Delta E6 order_revisions.id/revision_no, chưa trong65 bảng','01/04','Opaque source ref; không tự xác định revision hiện hành; CG04/05/07'],
['planRevisionRef','Delta E6 production_plan_revisions; chưa trong65 bảng','01','Không bằng order revision; không suy READY là được giao; CG06'],
['pricingSnapshotId','order_pricing_snapshots.id/order_id/order_version','04','Cùng order và version với nguồn; không chọn snapshot mới nhất tùy ý'],
['quotedUnitPrice / salePriceBasis','order_pricing_snapshots.quoted_unit_price / sale_price_basis','04','VND decimal; giá tại order, không đọc giá hiện tại'],
['vatRatePct / invoiceRequested','order_pricing_snapshots.vat_rate_pct / invoice_requested','04','Null khác0; invoice=false không đổi VAT'],
['pricingContextStatus','order_pricing_snapshots.context_status','04','UNRESOLVED/LEGACY_UNVERIFIED không biến RESOLVED bằng mock'],
['originalAmountDue / originalRevenueExVat','order_pricing_snapshots.gross_amount_due / revenue_ex_vat','04','Số gốc từ snapshot; KHÔNG ghi đè khi E7 xác định số tính tiền khác'],
['discountSeparate','order_discount_records.calculated_amount/status/pricing_snapshot_id','04 nội bộ','Khoản riêng; không giảm E7 amountDue hoặc suy đã chi; CK giữ mở'],
['deliveredServings / receivedServings','Delta e7_delivery_notes/e7_receipt_confirmations','01/02/03','Suất nguyên≥0; received chưa biết không0; zero nghiệp vụ Q02/Q13'],
['billableServings / basisEvidenceRef','Delta e7_revenue_snapshots','04','Căn cứ E7-Q03; không mặc định ordered/delivered/received hoặc pricing.servings'],
['grossAmountDue / revenueExVat','Delta e7_revenue_snapshots','04/05','Tính từ căn cứ và giá chụp; rounding E7-Q04; không giảm vì CK'],
['periodId / sourceRevision / totals','Delta e7_reconciliation_periods/lines','05/07','Snapshot kỳ có lineage; nguồn thiếu gắn gate, không bỏ dòng'],
['receiptAmount / receiptEvidenceRef','Delta e7_cash_receipts; files.id cho bằng chứng','06','Tiền dương VND, chứng từ theo scope; phân bổ/dup Q06/08'],
['reopenRequest / decision','change_requests/approvals hiện hữu + delta liên kết kỳ','07','Reuse cần review entity/snapshot/type, không khẳng định đã hỗ trợ E7'],
['actor / audit / attachment','users.id, audit_logs, files.id','Mọi màn có quyền','Actor guest chưa có audit binding CG01; không tạo người giả'],
['templateRef / exportSourceRevision / fileRef','Delta e7_export_runs; files.id nếu file được tạo','08','Chưa mapping cột MISA; định dạng/file bytes BLOCKED Q07']
]),
'API đọc bổ sung014–018 dùng cùng mapping, không tạo dữ liệu. DTO tiền dùng chuỗi decimal đề xuất, số suất int; ID chuỗi. Kiểu/length/nullability wire chi tiết E7-Q08 chưa freeze. Không serialize inputs_snapshot/secret/cost vào projection khách.'
].join('\n\n'));
md('srs/data-dictionary.md','Delta dữ liệu E7: đề xuất chưa merge',[
'65 bảng chung giữ nguyên. DBML có orders.status DELIVERED/CONFIRMED/DISPUTED/RECONCILED nhưng chưa có thực thể phiếu/kỳ/thu/MISA, không đủ làm bằng chứng persistence. Không sửa orders.status từ E7 khi chưa có contract tác động nguồn. [Mapping](../api/data-mapping.md).',
table(['Thực thể delta','Trường logic / kiểu đề xuất','Quan hệ / ràng buộc / null','Gate'],[
['e7_delivery_notes','id ID; orderId ID; orderRevisionRef/planRevisionRef opaque; deliveredServings int; state; version int; evidenceRef','PK id; orderId→orders; số giao≥0; nguồn bắt buộc theo policy đã xác nhận; không dùng thiếu=0','CG05/06/08; Q02'],
['e7_receipt_confirmations','id; deliveryId; receivedServings int; actorRef; confirmedAt UTC; evidenceRef; version','Gắn phiếu/version; chưa có xác nhận thì chưa có số nhận, không default0. Sửa xác nhận cần policy, giữ lịch sử','CG01; Q01/02/13'],
['e7_discrepancies / resolutions','id; deliveryId; description; evidenceRef; resolutionType; linkedSupplementRef; adjustmentBasis','Mỗi thỏa thuận gắn phần chênh và bằng chứng; không tự cả bù+giảm trừ. Chưa field tiền tự tính khi thiếu basis','Q02/03'],
['e7_revenue_snapshots','id; orderId; orderRevisionRef; pricingSnapshotId; billableServings; basisEvidenceRef; grossAmountDue/revenueExVat decimal; contextStatus','Giữ nguồn bất biến; cùng order/version; kết quả chưa xác định nullable logic, không0. Số gốc snapshot không ghi đè','Q03/04/08'],
['e7_reconciliation_periods / lines','id; customerId; fromDate/toDate; revision; state; sourceRefs; totals; completeness','Một tập nguồn có version; phạm vi/chồng kỳ và tái chụp cần duyệt; snapshot khóa bất biến','Q05'],
['e7_cash_receipts','id; periodId; amount decimal; receivedDate; evidenceRef; version','Tiền dương, chứng từ/scope hợp lệ; uniqueness nghiệp vụ và allocation chưa freeze','Q06/08'],
['Reuse change_requests / approvals + liên kết kỳ','entityRef; requestVersion; periodVersion; creator/lastEditor; reason; decision','Đề xuất dùng workflow nền, không tạo hai nguồn duyệt; Giám đốc khác người lập/sửa cuối; lý do≥10 ký tự; yêu cầu không mở khóa','Q05/08; O-06'],
['e7_export_runs','id; periodRef/revision; templateRef; status; errorSummary; fileRef; sourceFingerprint','FileRef chỉ có khi thật sự tạo; template chưa biết; giữ bytes/revision cũ khi kỳ mở lại','Q07/08']
]),
'Trường tối thiểu dùng kiểm toán: actor/time/before-after/reason/resourceVersion và request reference, kế thừa audit nền; độ dài, nullability vật lý, unique/index, precision và retention chưa quyết → BLOCKED E7-Q08. ID logic theo nền bigint qua API dạng chuỗi. Không có DDL hoặc bảng được merge. Các enum trong state diagram là nhãn đề xuất.',
'Quan hệ logic: customer→period→lines→revenue snapshot→order/pricing snapshot; order→delivery→confirmation/discrepancy→resolution; period→receipt/reopen/export. Order/plan revision phụ thuộc delta E6 chưa freeze, không coi FK đó đã triển khai.'
].join('\n\n'));
const checks=[
['CHK-E7-01','Số chốt/giao/nhận/tính tiền tách; missing khác0; revision đúng','BR-E7-002/004/005','TC-E7-001-1/3, TC-E7-002-3, TC-E7-005-1/2/3'],
['CHK-E7-02','Quyền/scope/link/không leak','BR-E7-001; NFR-E7-001','TC-E7-002-2, TC-E7-006-2, TC-E7-SYS-01'],
['CHK-E7-03','VAT/invoice/CK riêng','BR-E7-006/007','TC-E7-005-1/2, TC-E7-SYS-02'],
['CHK-E7-04','Giao bù/giảm trừ có thỏa thuận','BR-E7-004','TC-E7-003-1/2, TC-E7-004-1/2/3'],
['CHK-E7-05','Thu tiền/dup/mất phản hồi','BR-E7-003/008','TC-E7-009-1/2/3, TC-E7-SYS-03'],
['CHK-E7-06','Khóa/reopen qua mọi đường','BR-E7-009; NFR-E7-002','TC-E7-010-1/2/3, TC-E7-011-1/2/3, TC-E7-012-1/2/3'],
['CHK-E7-07','MISA và nghiệm thu tháng','BR-E7-011; NFR-E7-003','TC-E7-013-1/2/3, TC-E7-SYS-04'],
['CHK-E7-08','Gate/hạ tầng/error/không fake evidence','BR-E7-010; NFR-E7-004/005','TC-E7-SYS-05/06/07/08']
];
md('test/checklist.md','Checklist kiểm E7',table(['Checklist','Mục kiểm','Rule/NFR','Ca thiết kế'],checks)+'\n\nRà checklist không là test sản phẩm PASS. Các rule/error còn chung được phủ tại [system cases](system-cases.md); các FR đã truy vết [RTM](traceability.md).');
const sys=[
['TC-E7-SYS-01','NFR-E7-001 / BR-E7-001','2 khách/cơ sở synthetic, từng role và phiên hết hạn','Gọi tất cả18 route với đúng/sai scope, thiếu role, hết phiên; kiểm body/log','401 ERR-E7-401-01,403 ERR-E7-403-01,404 ERR-E7-404-01; không lộ dữ liệu/secret','BLOCKED E7-Q01/08'],
['TC-E7-SYS-02','BR-E7-006/007','Giá inclusive synthetic 40000, VAT thử8%, invoice true/false; CK riêng200000','Giữ nguồn, đổi cờ hóa đơn trong bộ dữ liệu thử độc lập; tính/đọc','Phải trả không đổi chỉ vì invoice=false; CK không giảm phải trả; missing VAT không0','NOT RUN'],
['TC-E7-SYS-03','BR-E7-003/008 / NFR-E7-002','Chứng từ thu synthetic và fault trước/sau commit','Gửi đồng thời/lặp chứng từ; ngắt phản hồi; tra dữ liệu/audit trước lệnh mới','Không cộng hai lần, không success một phần; ERR-FIN-422-03 khi chứng từ trùng; replay oracle chi tiết chờ Q08','BLOCKED E7-Q06/08'],
['TC-E7-SYS-04','NFR-E7-003 / BR-E7-011','Tháng biên bản thật 2 khách và mẫu MISA có version (chưa có)','Đối chiếu từng dòng/tổng, xuất và thử nhập MISA, lưu evidence','Khớp theo chuẩn được duyệt; MISA nhận file; synthetic không đủ nghiệm thu','BLOCKED E7-Q04/07 và dữ liệu thật'],
['TC-E7-SYS-05','BR-E7-002/010','Nguồn E6 thiếu/không sẵn sàng hoặc gate chưa chốt','Thử NOTE/REV/REC; kiểm không ghi và hiển thị reason','ERR-E7-503-01 + mã gate; không lấy0 hoặc tự quyết CG05/06','NOT RUN'],
['TC-E7-SYS-06','NFR-E7-004','Profile E7 synthetic 1000CCU sau khi được duyệt','Đo p95 đọc/ghi, error và duplication, tách job xuất','Đọc≤300ms/ghi≤800ms theo nền; chưa có target xuất file mới','BLOCKED E7-Q08/môi trường'],
['TC-E7-SYS-07','NFR-E7-005','HTML mới synthetic, viewport390/1440','Mở8 màn, thử validation, trạng thái loading/empty/error/offline và reopen; chụp/xem ảnh','Không tràn toàn trang; label/focus/nhãn BLOCKED rõ; chỉ chứng minh mock','NOT RUN (kết quả mock riêng validation/ui-result.json)'],
['TC-E7-SYS-08','BR-E7-003/010','Fault server có requestId synthetic','Mô phỏng lỗi nội bộ sau gửi và kiểm UI/log','ERR-E7-500-01 không lộ upstream body; UNKNOWN, không auto-submit','BLOCKED E7-Q08']
];
md('test/system-cases.md','Ca hệ thống, rule và NFR E7',table(['Mã','Truy vết','Tiền điều kiện','Bước chạy','Expected','Status','Actual','Evidence'],sys.map(s=>[...s,'','']))+'\n\n8 ca bổ sung có overlap với39 ca AC, không cộng thành47 mục tiêu độc lập. 0 test backend. SYS07 có thể kiểm mock riêng, không đổi thành PASS sản phẩm.');
md('test/evidence-protocol.md','Protocol bằng chứng E7',[
'Test case giữ Actual/Evidence trống đến khi chạy sản phẩm. Với POST ghi actor/scope, nguồn/version trước, request (ẩn token), response/requestId, resource/audit sau và chứng từ; mất response phải phân biệt trước/sau commit. GET chụp nguồn trước/sau để chứng minh không tạo dữ liệu. Không dùng mock làm persistence evidence.',
'Ca thành công có gate: ghi quyết định/policy version đã được duyệt trước khi chạy; không giả policy bằng fixture. Link cần proof hợp lệ theo policy được duyệt, không in token. Kỳ LOCKED thử cả delivery/discrepancy/revenue/receipt và quyết định stale/tự duyệt; snapshot cũ phải còn nguyên.',
'Q-13 cần ví dụ được xác nhận trước oracle timeout/fallback. MISA cần sản phẩm/version/template, file hash/revision nguồn, biên nhận nhập hoặc lỗi thực tế. R7 cần tháng dữ liệu thật 2 khách và biên bản; không dùng synthetic. Không gửi yêu cầu ra ngoài trong phiên BA.',
'Giữ E6 CG/EVID, CK/DATA-COST và các snapshot lịch sử. Mỗi lần kiểm tài liệu ghi scope và công cụ riêng trong validation E7.'
].join('\n\n'));
fs.mkdirSync(path.join(base,'test/fixtures'),{recursive:true});
fs.writeFileSync(path.join(base,'test/fixtures/synthetic.json'),JSON.stringify({label:'synthetic: not real accounting or production data',orderedServings:100,deliveredServings:98,receivedServings:null,billableServings:100,billableBasis:'ASSUMED AGREEMENT FOR ARITHMETIC ONLY; E7-Q03 OPEN',quotedUnitPrice:'40000',salePriceBasis:'INCLUSIVE',vatRatePct:'8',invoiceRequested:false,amountDue:'4000000',discountSeparate:'200000',receivedPayment:'1000000',remainingDue:'3000000',note:'VAT8% chỉ số thử; không tự suy billable=ordered; Q13 unresolved'},null,2));
md('test/fixtures/README.md','Fixture synthetic E7','[synthetic.json](synthetic.json) chỉ kiểm số học/tách khoản:100×40000=4000000; CK200000 không giảm phải trả; thu1000000 còn3000000. Số tính tiền100 là giả định thỏa thuận riêng, không suy từ giao98/nhận chưa biết. VAT8% là số thử. Không có seed/runtime hoặc dữ liệu thật. Doanh thu chưa VAT=4000000/1.08 trước làm tròn; rounding E7-Q04 chưa chốt.');
md('review/handoff.md','Bàn giao BA nháp E7',[
'Nguồn mở E7: người dùng12/11/2026. E8–E13 chưa mở. E6 dừng chờ CG01/08/05/06,14/14 CG OPEN; không sửa E6. Thiết kế consumer có điều kiện, không giải quyết thay producer.',
'[Epic](../epic-spec.md) · [SRS](../srs/spec.md) · [UC](../usecases/index.md) · [Story](../userstories/backlog.md) · [AC](../userstories/acceptance-criteria.md) · [API](../api/api-spec.md) · [Mapping](../api/data-mapping.md) · [UI](../ui/screens.md) · [Test](../test/test-cases.md) · [RTM](../test/traceability.md) · [Preview](../preview.html).',
'5 feature thiết kế nháp;13 FR/UC/story;39 AC và39 ca tương ứng;8 ca hệ thống có overlap;18 endpoint;8 màn;4 flow/state diagrams. MISA chưa mapping cột/thử nhập; dữ liệu ví dụ synthetic. [Kiểm](../validation/report.md).',
'Độ phủ nháp45/78≈57,7%;2 feature E6 chỉ gate tính riêng; không BA duyệt/tiến độ phần mềm.0 backend/migration/UAT,65 bảng không đổi. CK-Q01–10/DATA-COST-Q01–06/NFR-COST-002, O-02/O-03/O-04, E6-EVID-001/002 giữ.',
'Tiếp nối: [Questions](questions.md)/[Dependencies](dependencies.md); đồng bộ chỉ theo evidence mới hoặc sai lệch cụ thể E7. Không tự trả lời Q-13, không hỏi lại4CG E6, không mở E8–E13; không chạy generator E6/sửa snapshot cũ.'
].join('\n\n'));
console.log('Initial E7 draft authored; protected '+protectedFiles.length+' files.');

