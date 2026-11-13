const c=require('./common.cjs');const {read,md,json,link,tableRows,clean}=c;
const scan=JSON.parse(read('docs/gia-phat/review/decision-pack/validation/cross-epic-result.json'));
const at=(file,needle)=>{const lines=read(file).split(/\r?\n/),i=lines.findIndex(x=>x.includes(needle));if(i<0)throw Error(file+': '+needle);return {file,line:i+1,excerpt:lines[i]};};
const d=(e,s)=>`docs/${e}/${s}`;
const manual=[];
function add(severity,title,refs,description,action,owner){manual.push({id:'XC-'+String(scan.findings.length+manual.length+1).padStart(2,'0'),severity,title,refs:refs.map(([f,n])=>at(f,n)),description,action,owner,method:'Đọc đối chiếu trực tiếp các đoạn được dẫn; không sửa nguồn, không đóng câu.'});}
add('Cao','O-01 về VAT đầu vào còn diễn đạt cũ trong ERD',[
 [d('nen-tang','srs/erd.md'),'Có gồm VAT đầu vào hay không'],[d('cost','accounting/business-rules.md'),'ACC-CONF-02'],[d('chi-phi-loi-nhuan','review/dependencies.md'),'ERD có diễn đạt cũ']],
 'ERD còn hỏi giá nhập có gồm VAT đầu vào; xác nhận kế toán E3 và dependency E13 đã nêu cost gồm VAT phải trả. Đây là phần có câu trả lời ngầm, cần xác nhận phạm vi O-01 còn mở; VAT bán ra và khoản khoán chưa được đóng.',
 'Ở phiên có quyết định ký, đánh dấu phần VAT đầu vào đã có căn cứ và sửa diễn đạt cũ theo CR; giữ các nhánh O-01 chưa trả lời. Gốc ưu tiên: ACC-CONF-02 của E3.', 'Kế toán, BA');
add('Cao','Các mẫu số cost không được thay thế nhau',[
 [d('cost','srs/spec.md'),'| Cost % |'],[d('mua-hang-san-xuat','review/questions.md'),'| E11-Q08 |'],[d('phan-hoi-bao-cao','review/questions.md'),'| E12-Q08 |'],[d('chi-phi-loi-nhuan','review/questions.md'),'| E13-Q08 |']],
 'E3 định nghĩa cost suất trên doanh thu chưa VAT; E11 hỏi mẫu số BO-02; E12 hỏi tập ghép/trọng số theo khách; E13 hỏi thành phần kết quả kinh doanh. Các chỉ số có liên quan nhưng chưa có ánh xạ được duyệt. Không phát hiện căn cứ để coi chúng là cùng một tỷ lệ.',
 'Lập bảng định nghĩa nguồn và bộ đối chiếu cùng phạm vi sau khi từng câu được ký. Dùng E3 làm gốc cost/VAT/chiết khấu, E7 làm gốc doanh thu. BO-01 ≤ 52 % và BO-02 ≤ 3 điểm phần trăm không phải dung sai NFR-COST-002.', 'Kế toán, Giám đốc, chủ dashboard');
add('Cao','Doanh thu E13 phụ thuộc số tính tiền và VAT E7 còn mở',[
 [d('giao-nhan-doanh-thu','review/questions.md'),'| E7-Q03 |'],[d('giao-nhan-doanh-thu','review/questions.md'),'| E7-Q04 |'],[d('chi-phi-loi-nhuan','review/dependencies.md'),'Doanh thu đã đối soát']],
 'E13 yêu cầu doanh thu đã đối soát có revision; E7 chưa chốt số tính tiền, căn cứ VAT và dung sai đối chiếu. Bản snapshot đề xuất không chứng minh doanh thu chính thức đã đủ nguồn.',
 'Giữ gate R13; sau quyết định E7 mới chuẩn hóa hợp đồng đọc doanh thu và evidence. Không suy số tính tiền từ số giao/nhận. Không mượn dung sai Cost cho R7/R13.', 'Kế toán, Giám đốc');
add('Trung bình','Tên và kiểu version/định danh ở delta chưa thống nhất',[
 [d('mua-hang-san-xuat','srs/data-dictionary.md'),'| Phiên bản | version | Integer'],[d('phan-hoi-bao-cao','srs/data-dictionary.md'),'| Phiên bản | version | Opaque token'],[d('chi-phi-loi-nhuan','srs/data-dictionary.md'),'Mọi thực thể đề xuất có id BIGINT']],
 'E11 dùng Integer, E12 dùng opaque token, E13 dùng INTEGER và chọn BIGINT UNSIGNED đề xuất; E10 chưa chọn khóa vật lý mới. Đây là khác mức trừu tượng, chưa chứng minh mâu thuẫn runtime. Nếu consumer ép version thành số thì mất tính opaque.',
 'Tech lead xác nhận kiểu wire và mapping riêng từng nguồn; không đổi schema 65 bảng. Thống nhất quy ước reference/revision/version trước freeze.', 'Tech lead, chủ dữ liệu E10–E13');
add('Trung bình','Lead và proposal xuất hiện ở ba delta',[
 [d('website-cong-khai','srs/data-dictionary.md'),'| pub_lead_intake |'],[d('agent-dinh-duong-vien','api/data-mapping.md'),'| ain_proposals |'],[d('crm-ban-hang','srs/data-dictionary.md'),'| crm_intakes |']],
 'Ba cấu trúc có contact/consent/source/receipt cùng chức năng tiếp nhận nhưng khác producer và vòng đời. Chưa có tên bảng vật lý trùng chính xác; vẫn có nguy cơ ghi nhiều bản cho một nguồn hoặc coi receipt là duyệt.',
 'Xác nhận nguồn chủ, khóa bàn giao và phạm vi consent qua E8-Q06, E9-Q06/10, E10-Q13. Giữ các delta độc lập cho đến khi có quyết định; không tự gộp bảng.', 'Kinh doanh, phụ trách dữ liệu, Tech lead');
add('Cao','Đồng ý nhật ký khác đồng ý sức khỏe; bữa đã ăn cần evidence riêng',[
 [d('phan-hoi-bao-cao','review/questions.md'),'| E12-Q15 |'],[d('phan-hoi-bao-cao','review/questions.md'),'| E12-Q17 |'],[d('phan-hoi-bao-cao','review/dependencies.md'),'FEAT-087 độc lập'],[d('agent-dinh-duong-vien','review/questions.md'),'| E9-Q14 |']],
 'Nguồn đã phân biệt FEAT-087 phi y tế với FEAT-046/047/063. Đây là câu trả lời ngầm về ranh giới, cần xác nhận; không trả lời consent/retention hoặc bằng chứng đã ăn. Chọn món, giao hàng và nhận hàng không chứng minh cá nhân đã ăn.',
 'Giữ nhóm O-03 riêng; trình E12-Q15/16/17 theo chính sách nhật ký. Không mở thu thập sức khỏe, không suy đã ăn từ E6/E7.', 'Giám đốc, phụ trách dữ liệu, Dinh dưỡng viên');
add('Trung bình','Người duyệt trong các epic mới vẫn chưa được O-06 chỉ định',[
 [d('mua-hang-san-xuat','review/questions.md'),'| E11-Q02 |'],[d('chi-phi-loi-nhuan','review/questions.md'),'| E13-Q10 |'],[d('crm-ban-hang','review/questions.md'),'| E10-Q03 |'],[d('nen-tang','srs/spec.md'),'| O-06 |']],
 'Tách người lập/người sửa cuối khỏi người duyệt là nguyên tắc nền. Các epic mới đã mô tả approval nhưng người duyệt, hạn mức và người thay còn mở; không thể dùng tên persona để tự cấp quyền.',
 'Trình ma trận theo nghiệp vụ trong nhóm O-06; ghi phạm vi từng chữ ký. Các vai trò chỉ tham gia review chưa được tính là người có quyền quyết định.', 'Giám đốc, BA');
add('Trung bình','Hai chức năng dựng thực đơn public có khả năng dùng chung',[
 [d('website-cong-khai','review/questions.md'),'| E8-Q05 |'],[d('agent-dinh-duong-vien','review/questions.md'),'| E9-Q11 |'],[d('website-cong-khai','api/endpoint-catalog.json'),'/v1/public/menu-trials'],[d('agent-dinh-duong-vien','api/endpoint-catalog.json'),'/v1/nutrition-agent/requests']],
 'Quét path/method không thấy trùng, nhưng FEAT-057 và FEAT-060 cùng dựng thực đơn public; E9-Q11 đã hỏi dùng chung hay tách bộ dựng/port kiểm. Khác URL không chứng minh khác chức năng.',
 'Review quyết định dùng chung port kiểm hay bộ dựng riêng, giữ quyền và quota từng agent. Không tự hợp nhất endpoint hoặc dùng credential AIO cho AIN.', 'Tech lead, Dinh dưỡng viên, chủ website');
add('Trung bình','Dữ liệu giá có phần lẻ và giá cost nguyên đồng còn gate',[
 [d('crm-ban-hang','srs/data-dictionary.md'),'customer_price_terms.customer_id/meal_type_id/quoted_unit_price'],[d('mua-hang-san-xuat','srs/data-dictionary.md'),'| Giá cost |'],[d('chi-phi-loi-nhuan','review/questions.md'),'| E13-Q09 |']],
 'E10 giữ quoted_unit_price decimal(18,6), E11 có giá cost Integer money và phần lẻ chờ review, E13 chưa chọn precision/làm tròn/phần dư. Các trường khác nghĩa nên không kết luận trùng kiểu sai; cần mapping để tránh cắt phần lẻ khi truyền nguồn.',
 'Chốt chuẩn hóa PriceInput và quy tắc làm tròn từng chỉ số theo nguồn. Giữ NFR-COST-002 ≤ 1 đ và ≤ 0,01 điểm phần trăm, không dùng làm quy tắc làm tròn mọi tiền.', 'Kế toán, Tech lead');
add('Trung bình','Chiết khấu riêng chưa có chính sách đưa vào lợi nhuận',[
 [d('cost','accounting/business-rules.md'),'| CK-Q05 |'],[d('cost','accounting/business-rules.md'),'| CK-Q09 |'],[d('chi-phi-loi-nhuan','review/dependencies.md'),'Chưa quyết định khoản chiết khấu']],
 'E3 giữ khoản chiết khấu riêng theo đơn; E13 hỏi cách ghi vào kết quả kinh doanh. Không có xung đột trực tiếp đã chứng minh, nhưng không thể tự trừ CK khỏi doanh thu hoặc phải trả NCC để tạo lợi nhuận.',
 'Kế toán xác nhận kỳ ghi nhận, trạng thái xử lý và cách chống đếm đôi. Giữ nguyên phải trả NCC và không tự khấu trừ tiền khách.', 'Kế toán, Giám đốc');
add('Thấp','MISA chỉ có câu nguồn E7; không tạo quyết định xuất MISA cho E11/E13',[
 [d('giao-nhan-doanh-thu','review/questions.md'),'| E7-Q07 |'],[d('mua-hang-san-xuat','review/dependencies.md'),'công nợ NCC không là phải thu'],[d('chi-phi-loi-nhuan','review/questions.md'),'| E13-Q12 |']],
 'E7 hỏi mẫu nhập MISA; E13 chỉ hỏi export nội bộ; E11 phân biệt công nợ NCC với phải thu khách. Không thấy căn cứ trong sổ để gộp cả ba thành một quyết định MISA.',
 'Giữ E7-Q07 riêng; BA hỏi lại phạm vi chỉ khi có nhu cầu xuất khác được xác nhận. Không tự đặt định dạng file, mapping hay nhà cung cấp.', 'Kế toán, BA');
add('Trung bình','E1 và E5 diễn giải thời gian phản hồi đầu khác nhau',[
 [d('nen-tang','review/questions.md'),'NFR-PERF-003'],[d('agent-noi-bo','review/questions.md'),'| AIO-Q01 |']],
 'E1 ghi ký tự đầu trong 5 giây; ghi chú E1 nêu polling E5 và đề xuất hiểu là phản hồi tiến trình đầu, không phải token đầu. Đây mới là đề xuất, không tự sửa NFR gốc.',
 'Tech lead và QA xác nhận cách đo sau khi O-04/AIO-Q01 có nguồn. Giữ giới hạn phản hồi và thời gian dựng thực đơn là hai chỉ số riêng.', 'Tech lead, QA, Giám đốc');
const schema=read('docs/nen-tang/srs/schema.dbml');const names=[...schema.matchAll(/^Table\s+(\w+)/gm)].map(m=>m[1]);
let inventory=[];
for(const [epic,dir,prefix] of [
 ['E7','giao-nhan-doanh-thu',/^(e7_|Reuse )/],['E8','website-cong-khai',/^pub_/],['E9','agent-dinh-duong-vien',/^ain_/],['E10','crm-ban-hang',/^(crm_|sale_)/],['E11','mua-hang-san-xuat',/^[a-zA-Z]+ \/ /],['E12','phan-hoi-bao-cao',/^(feedback_|dish_metric|role_metric|review_proposal|group_nutrition|diary_)/]
]){const file=`docs/${dir}/`+(epic==='E9'?'api/data-mapping.md':'srs/data-dictionary.md');for(const r of tableRows(file).filter(r=>prefix.test(r.cells[0])))inventory.push({epic,file,line:r.line,entity:r.cells[0],fields:r.cells.slice(1).join(' | '),existingNames:names.filter(n=>new RegExp('(?<![a-z_])'+n+'(?![a-z_])').test(r.cells[0]))});}
const file=d('chi-phi-loi-nhuan','srs/data-dictionary.md');let current;read(file).split(/\r?\n/).forEach((line,i)=>{if(/^## [a-z_]+$/.test(line)){current={epic:'E13',file,line:i+1,entity:line.slice(3),fields:'',existingNames:[]};inventory.push(current);}else if(current&&line.startsWith('|')&&!line.startsWith('| :')&&!line.startsWith('| Tên logic'))current.fields+=line+'\n';});
json('validation/delta-inventory.json',{schemaFile:'docs/nen-tang/srs/schema.dbml',schemaTables:names.length,inventory,note:'Đơn vị là dòng thực thể logic hoặc nhóm thực thể; không phải số bảng vật lý. Trường chung nằm ở từ điển được dẫn. E9 dẫn tiếp mapping như từ điển chỉ định.'});
json('validation/manual-findings.json',manual);
let body=`## Phạm vi và cách kiểm\n\nQuét tự động [scan-cross-epic.cjs](validation/scan-cross-epic.cjs): mã FR/BR/NFR/ERR/UC tại hàng định nghĩa đầu cột hoặc heading UC trong SRS/usecase; bỏ bảng truy vết. Endpoint so method + path, path độc lập method, chuẩn hóa tên biến đường dẫn và so FR để tìm chức năng chung. Port được đọc riêng cùng catalog; không coi port là HTTP. Quét không suy rằng mã tham chiếu lại là khai báo trùng.\n\nKết quả: ${scan.definitionOccurrences} vị trí mã; ${scan.endpoints} bản ghi endpoint/port; **${scan.findings.length} ứng viên trùng tự động**. [Kết quả máy](validation/cross-epic-result.json). Đây là giới hạn tìm kiếm có cấu trúc; không chứng minh ngữ nghĩa hoàn toàn nhất quán.\n\nKiểm thủ công: đọc bảy từ điển E7–E13, mapping E9 được từ điển dẫn tới; đối chiếu tên với ${names.length} bảng trong DBML; so các trường reference/version/giá và các producer/consumer có cùng chức năng. Đọc đoạn E3/E7 làm gốc và các câu hỏi/dependency E11–E13. Các phát hiện dưới ghi rõ vị trí, không sửa nguồn.\n\n## Phát hiện\n\n`;
for(const f of scan.findings)body+=`## ${f.id}: ${f.key}\n\nMức: ${f.severity}. Máy phát hiện ${f.kind}; cần BA và Tech lead phân loại tái dùng hay xung đột.\n\n`+f.occurrences.map(o=>`- [${o.file}:${o.line}](${link(o.file,o.line)}).`).join('\n')+'\n\nĐề xuất: đối chiếu chủ sở hữu định nghĩa/route trước khi sửa; chưa đóng gate. Người xác nhận: Tech lead, BA.\n\n';
for(const f of manual)body+=`## ${f.id}: ${f.title}\n\nMức: **${f.severity}**. ${f.description}\n\nNguồn và dòng:\n\n`+f.refs.map(o=>`- [${o.file}:${o.line}](${link(o.file,o.line)}).`).join('\n')+`\n\nĐề xuất xử lý: ${f.action}\n\nCần xác nhận: ${f.owner}. Cách kiểm: ${f.method}\n\n`;
body+=`## Danh mục delta ngoài schema\n\n${inventory.length} dòng thực thể/nhóm đề xuất được liệt kê dưới, kèm toàn bộ trường riêng từ nguồn. [Bản máy](validation/delta-inventory.json). Không có tên vật lý đề xuất giống hệt nhau giữa các epic trong danh mục này. Các trường cùng nghĩa khác tên/kiểu và chức năng chồng nhau xem XC-04, XC-05, XC-09. E7 tái dùng approvals/change_requests là nguồn nền, không phải bảng mới. Tên ghép có dấu “/” là nhóm logic chưa chốt số bảng.\n\n`;
for(const e of inventory)body+=`### ${e.epic}: ${e.entity}\n\n[Nguồn, dòng ${e.line}](${link(e.file,e.line)}). ${e.existingNames.length?'Tái dùng nền: '+e.existingNames.join(', ')+'.':'Tên đề xuất chưa phải bảng được merge.'}\n\nTrích trường và ràng buộc nguồn:\n\n`+e.fields.split('\n').filter(Boolean).map(s=>'> '+s).join('\n')+'\n\n';
body+='## Trường chung của các delta\n\nCác trường dưới áp dụng cùng những trường riêng đã liệt kê; tên/kiểu vẫn là đề xuất nguồn.\n\n';
for(const dir of ['mua-hang-san-xuat','phan-hoi-bao-cao']){
 const f=d(dir,'srs/data-dictionary.md');const common=tableRows(f).filter(r=>r.cells.length===8&&!r.cells[0].startsWith(':')&&!['Logical','Tên logic'].includes(r.cells[0]));
 body+=`### ${dir}\n\n`+common.map(r=>`[Dòng ${r.line}](${link(f,r.line)}):\n\n> ${r.cells.join(' | ')}\n`).join('\n')+'\n';
}
for(const needle of ['Mọi thực thể đề xuất có id BIGINT','Danh mục loại chi phí có version']){const r=at(d('chi-phi-loi-nhuan','srs/data-dictionary.md'),needle);body+=`[Trường chung E13, dòng ${r.line}](${link(r.file,r.line)}):\n\n> ${r.excerpt}\n\n`;}
body+=`## Ranh giới nguyên tắc\n\nCost nguyên liệu gồm VAT phải trả nhà cung cấp. Cờ “không yêu cầu hóa đơn” độc lập, không phải VAT 0 %. Chiết khấu % hoặc tiền/suất riêng theo đơn, không giảm phải trả NCC và không tự khấu trừ phải trả khách. NFR-COST-002 giữ ≤ 1 đ cho cost món, ≤ 0,01 điểm phần trăm cho cost % ngày; BO-01/BO-02 là mục tiêu kinh doanh. FR-MENU-RCP-007 vẫn chặn O-02; FEAT-046/047/063 vẫn chỉ gate O-03, không thu dữ liệu sức khỏe.\n\n## Cần BA làm rõ\n\nCác phát hiện ghi “cần xác nhận” không đóng câu hỏi. Danh sách mọi mã thiếu vai trò/release nằm trong [báo cáo](validation/report.md). Chưa có contract nguồn freeze hoặc dữ liệu thực để xác nhận tương thích kiểu. Không suy thời hạn, hạn mức, phương pháp phân bổ, mẫu số hay người ký từ ví dụ.\n`;
md('cross-epic-consistency.md','CONSISTENCY','Rà nhất quán liên epic',body);
console.log(JSON.stringify({manual:manual.length,deltaRows:inventory.length,schemaTables:names.length}));
